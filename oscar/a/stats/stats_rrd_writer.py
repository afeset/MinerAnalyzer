#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# ver 1.0 
#
# Author: orens/amiry
#

import re
import time
import threading
import stats_queue_objects 
from event_report_limiter import EventReportLimiter

class StatsRrdWriter(threading.Thread):

    def __init__ (self):
        threading.Thread.__init__(self)
        self._log = None
        self._statsMgr = None
        self._runFlag = False
        self._aggrHistory = None
        self._updatePeriod = None
        self._burstCount = None
        self._burstInterval = None
        self._startupGracePeriod = None
        self._burstReportLimiter = EventReportLimiter(3600)
        self._updateReportLimiter = EventReportLimiter(3600)
        self._valuesDB = None
        # RE to find data from a line such as this one:    opening '/opt/qb/data/oscar/stats-manager/0/var/rrd/line/Stats1248231030895771650-Sunday-14April2013-1805-1365962728.rrd': No such file or directory
        self.myReNoSuchFile = re.compile("opening '(.*)': No such file or directory")


    def init (self, logger, statsMgr, aggrHistory, updatePeriod, burstCount, burstInterval, startupGracePeriod):
        self._log = logger
        self._statsMgr = statsMgr
        self._aggrHistory = aggrHistory
        self._updatePeriod = updatePeriod
        self._burstCount = burstCount
        self._burstInterval = burstInterval
        self._startupGracePeriod = startupGracePeriod
        # For each counter, holds value of heartbeat as found in rrd file.
        self._lastKnownHeartbeat = {}


    def run (self):

        self._log.notice("Stats RRD writer running. Entering grace period of %s seconds", self._startupGracePeriod)

        time.sleep(self._startupGracePeriod)
        self._log.notice("Stats RRD writer finished grace period. Start main loop")

        try:
            self._runFlag = True
            while (self._runFlag):
                startTime = time.time()
                self._doUpdates()
                self._statsMgr.notifyNoMoreGrace()

                # Finished updating the whole history dict.
                # Warn about a long update, or count it for the next warning
                maxAllowedUpdateTime = self._updatePeriod * 0.75
                updateTime = time.time() - startTime
                if updateTime > maxAllowedUpdateTime:
                    (shouldReport, numEvents) = self._updateReportLimiter.shouldReport()
                    if shouldReport:
                        self._log.error("StatsRrdWriter full update took too long: %s seconds, max allowed is %s. (Occured %s times since last reported)" % 
                                        (updateTime, maxAllowedUpdateTime, numEvents))
                else:
                    # sleep to make mainLoop() take exactly _updatePeriod
                    remainingTime = self._updatePeriod - updateTime
                    if remainingTime > 0:
                        time.sleep(remainingTime)

            self._log.notice("Stats RRD Writer thread exited")
        except:
            # Loop ended - thread is shutting down
            self._runFlag = False
            self._log.error("UNExpected exception on Stats RRD Writer. Exception info: %s" % stats_queue_objects.formatExceptionInfo())


    def end (self):
        self._log.notice("Stats RRD Writer requested to end thread")
        self._runFlag = False


    def _doUpdates (self):
        # Get a copy of all keys because dictionary might change in other thread during iteration.
        startTime = time.time()

        self._aggrHistory.lock()
        keys = self._aggrHistory.keys()
        self._aggrHistory.unlock()

        numCounters = len(keys)
        numHeartbeatUpdated = 0
        numProcessedKeys = 0
        numProcessedUpdates = 0
        counterIdx = 0
        self._log.debug2("_doUpdates() called, numCounters=%s", numCounters)

        while counterIdx < numCounters:
            burstStartTime = time.time()
            self._log.debug3("Start burst")
            remainingCounters = numCounters - counterIdx
            burstSize = min(self._burstCount, remainingCounters)
            # Each element in updates[] is a composite tuple: (key, (value, timestamp, valueType))
            updates = []
            # Each element in keysForInfo[] is a tuple: (key, desiredHeartbeat)
            keysForInfo = []

            # This makes sure that the aggr thread does not re-initialize the DB during the time we use it
            valuesDb = self._statsMgr.getAndLockValuesDb()

            self._aggrHistory.lock()

            i = 0
            while i < burstSize:
                key = keys[counterIdx]
                counterSamples = self._aggrHistory.getAndClear(key)
                keyUpdates = map(lambda x: (key, x), counterSamples)
                self._log.debug4("_doUpdates() got key=%s, keyUpdates=%s", key, keyUpdates)

                numUpdates = len(keyUpdates)
                if numUpdates > 0:
                    updates += keyUpdates
                    numProcessedKeys += 1
                    numProcessedUpdates += numUpdates
                
                    desiredHeartbeat = valuesDb.getDesiredHeartbeatForId(key)
                    if desiredHeartbeat:
                        if (key not in self._lastKnownHeartbeat) or (self._lastKnownHeartbeat[key] != desiredHeartbeat):
                            self._log.info("Append keysForInfo. Key %s: Last known heartbeat %s. Desired %s", 
                                           key, self._lastKnownHeartbeat.get(key), desiredHeartbeat)
                            keysForInfo.append((key, desiredHeartbeat))
                    else:
                        # This could happen when we find updates for a counter that was removed. No fuss.
                        self._log.debug5("_doUpdates() could not get heartbeat for key=%s, counter was probably deleted.", key)
    
                    self._log.debug3("Got heartbeat. Key: %s, heartbeat: %s", key, desiredHeartbeat)

                # Next counter
                counterIdx += 1
                i += 1

            self._aggrHistory.unlock()

            burstMiddleTime = time.time()
            rrdUpdates = []

            # Now we need to run all "rrd info" commands in order to get the current heartbeat.
            # If the current heartbeat is different than the desired heatbeat (stored in keysForInfo)
            # we will need to run an "rrd tune" command.
            self._log.debug3("keysForInfo=%s", keysForInfo)
            heartbeats = valuesDb.getMinHeartbeatFromDbForIds(map(lambda x: (x, x[0]), keysForInfo))
            self._log.debug3("heartbeats=%s", heartbeats)
            if len(heartbeats) != len(keysForInfo):
                self._log.error("_doUpdates() got wrong number of heartbeats=%s for keysForInfo=%s", heartbeats, keysForInfo)
            else:
                # Scan all 
                for heartbeat in heartbeats:
                    (key, desiredHeartbeat) = heartbeat[0]
                    actualHeartbeat = heartbeat[1]
                    # actualHeartbeat could be None
                    if actualHeartbeat and actualHeartbeat != desiredHeartbeat:
                        cmd = valuesDb.formatTuneHeartbeatCommand(key, desiredHeartbeat)
                        opTuple = ("tune", key, desiredHeartbeat)
                        rrdUpdates.append((opTuple, cmd))
                        numHeartbeatUpdated += 1
                    elif actualHeartbeat == desiredHeartbeat:
                        # Here we need to update the last known heartbeat, or else we will keep calling RRD 'info' 
                        self._log.debug5("Update last known heartbeat for key %s to %s - before tune", key, desiredHeartbeat)
                        self._lastKnownHeartbeat[key] = desiredHeartbeat


            self._log.debug3("_doUpdates() before filter, num updates=%s", len(updates))
            # Remove all entries for which the counter does not exist any more
            updates = filter(lambda x: valuesDb.isCounterIdExists(x[0]), updates)
            numUpdates = len(updates) # new length after the filter
            self._log.debug3("_doUpdates() after filter, num updates=%s", numUpdates)

            i = 0
            # Note: This should be improved per:
            # OSC-2455 - Stats - Unify RRD commands for the same counter
            while i < numUpdates:
                update = updates[i]
                key = update[0]
                data = update[1]
                self._log.debug4("StatsRrdWriter inserting data to DB: update=%s", update)
                cmd = valuesDb.formatUpdateCommand(key, data[1], data[0], data[2])
                opTuple = ("update", key)
                rrdUpdates.append((opTuple, cmd))
                i += 1

            # Now update RRD
            retValues = valuesDb.executeRrdCommands(rrdUpdates)
            self._log.debug3("executeRrdCommands() returned %s", retValues)
            createCommands = []
            keysToCreate = {}
            keysToSupressNotUnsigned = {}
            for retValue in retValues:
                opTuple = retValue[0]
                cmdType = opTuple[0]
                key = opTuple[1]
                commandSuccess = retValue[1][0]
                commandOutput = retValue[1][1]
                if not commandSuccess:

                    supressError = False

                    # Supress errors about historical times only for update commands
                    if (cmdType == "update") and (commandOutput.find("illegal attempt to update using time") != -1):
                        supressError = True

                    # Supress errors about bad counter values (issue a single error per counter)
                    elif (cmdType == "update") and (commandOutput.find("not a simple unsigned integer") != -1):
                        if keysToSupressNotUnsigned.get(key) is None:
                            keysToSupressNotUnsigned[key] = 1
                        else:
                            # Supress errors on additional samples from the same counter
                            supressError = True

                    elif (cmdType == "update") and (commandOutput.find("No such file or directory") != -1):
                        counter = valuesDb.getCounterById(key)
                        if not counter:
                            self._log.error("Could not get counter for key %s", key)
                        else:
                            match = self.myReNoSuchFile.search(commandOutput)
                            if match:
                                # Here, the rrdRelativePath is already set in mysql. 
                                # We create the file with the same name as appear in mysql
                                rrdPath = match.group(1)
                                createCommand = valuesDb.formatCreateCommand(counter, rrdPath)
                                if keysToCreate.get(key) is None:
                                    createCommands.append((None, createCommand))
                                    keysToCreate[key] = 1
                                else:
                                    # Supress errors on additional samples from the same counter
                                    supressError = True
                            else:
                                self._log.error("Failed to get RRD file name from command output %s", commandOutput)


                    if not supressError:
                        self._log.error("RRD command failed: opTuple=%s, commandOutput=%s", opTuple, commandOutput)
                else:
                    if cmdType == "tune":
                        heartbeat = opTuple[2]
                        self._log.debug5("Update last known heartbeat for key %s to %s - after tune", key, opTuple)
                        self._lastKnownHeartbeat[key] = heartbeat

            if createCommands:
                self._log.notice("Executing create commands for %d missing counters", len(createCommands))
                retValues = valuesDb.executeRrdCommands(createCommands)
                for retValue in retValues:
                    commandSuccess = retValue[1][0]
                    commandOutput = retValue[1][1]
                    if not commandSuccess:
                        self._log.error("RRD 'create' failed: commandOutput=%s", commandOutput)

            # We finished using the DB, allow counter discovery to re-initialize it if it wants to
            self._statsMgr.unlockValuesDb()

            burstTime = time.time() - burstStartTime
            self._log.debug3("End burst")

            # Warn about a long burst, or count it for the next warning
            maxAllowedBurstTime = self._burstInterval * 0.75
            if burstTime > maxAllowedBurstTime:
                (shouldReport, numEvents) = self._burstReportLimiter.shouldReport()
                if shouldReport:
                    self._log.warning("StatsRrdWriter burst took too long: %s seconds (time to copy keys %s), max allowed is %s. (Occured %s times since last reported)" % 
                                      (burstTime, burstMiddleTime - burstStartTime, maxAllowedBurstTime, numEvents) )

            # If we have more counters, sleep
            if counterIdx < numCounters:
                remainingTime = self._burstInterval - burstTime
                if remainingTime > 0:
                    time.sleep(remainingTime)
                    burstTime = time.time() - burstStartTime

        # End of loop of all counters
        loopTime = time.time() - startTime
        self._log.notice("Finished rrd writer cycle, took %s seconds, processed %s keys with %s updates out of %s keys, updated heartbeat of %s counters", 
                         loopTime, numProcessedKeys, numProcessedUpdates, len(keys), numHeartbeatUpdated)

