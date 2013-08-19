# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: amiry

# Keep track of HTTP clients that consistently do not follow our redirects and mark them as "non deliverable"

import time, os, re, shutil, glob
from a.sys.filter.time.sliding_window import SlidingWindow
from a.infra.file.rotating_file_size_enforcer import RotatingFileSizeEnforcer
import a.infra.format.json

G_NAME_GROUP_DELIVERY_TRACKING = "delivery-tracking"

# Default thresholds (Used if not exist in brownie)
G_DEFAULT_WAIT_STATE_RATIO_THRESHOLD = 0.05
G_DEFAULT_MIN_WAIT_STATE_TO_BLOCK = 3

# Non confugurable values
G_DELTA_SIZE_LIMIT = 5000
G_MAX_DELTA_FILES_IN_FOLDER = 5
G_NO_DELIVERY_TABLE_FILE_NAME = "no-delivery-table.json"

# Session states
G_SESSION_STATE_WAIT             = 1 # Session is not being delivered, but wasn't identified as ignored-redirect yet
G_SESSION_STATE_IGNORED_REDIRECT = 2 # Session is identified as ignored-redirect
G_SESSION_STATE_ACTIVE           = 3 # Session is being delivered
G_SESSION_STATE_ERROR            = 4 # Additional state to indicate that we don't need to count it anymore


class DeliveryTracking:

    def __init__ (self, deltaFilesDir, dataDir, confDir, tempDir, counters, logger, archiver):
        self._deltaFilesDir = deltaFilesDir
        self._dataDir = dataDir
        self._confDir = confDir
        self._tempDir = tempDir
        self._counters = counters
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_DELIVERY_TRACKING)
        self._totalDeltaWriteTime = 0
        self._deltaSeqNum = 0
        self._sessions = None
        self._recentlyBlocked = None
        self._whitelist = None
        self._noDeliveryTable = {}
        self._noDeliveryTableChanged = False
        self._archiver = archiver
        self._isInitialized = False
        self._deltaPattern = "no-delivery-table-delta-"
        self._deltaSuffix = ".json"


        # File for delta updates
        self._deltaFile = RotatingFileSizeEnforcer(self._log, self._deltaFilesDir, self._deltaPattern, self._deltaSuffix)
        self._deltaFile.prepare()


    def updateConfig (self, windowSizeSec, windowNumFrames, maxSessionKeys, maxNoDeliveryTableSize, blockTTLSec, shortBlockTTLSec,
                      whitelistFile, newSessionIgnorePeriod, 
                      floodProtectionEnabled, floodProtectionWindowSizeSec, floodProtectionWindowNumFrames, 
                      floodProtectionRatio, minSessionsToAllowProtection,
                      shouldArchiveNoDeliveryTable, shouldArchiveDeliveryTrackingUpdatesToLine,
                      deliveryTrackingArchiveTableInterval):

        self._log("init").notice(
            "Update configuration. Window %d x %d sec, max session keys %d, max no delivery table size %d, TTL %d, Short TTL %d, "+
            "flood protection ratio %f, should archive table %s, should archive updates %s", 
            windowSizeSec, windowNumFrames, maxSessionKeys, maxNoDeliveryTableSize, blockTTLSec, shortBlockTTLSec, 
            floodProtectionRatio, shouldArchiveNoDeliveryTable, shouldArchiveDeliveryTrackingUpdatesToLine)

        self._maxSessionKeys = maxSessionKeys
        self._maxNoDeliveryTableSize = maxNoDeliveryTableSize
        self._blockTTLSec = blockTTLSec
        self._shortBlockTTLSec = shortBlockTTLSec
        self._whitelistFile = whitelistFile
        self._newSessionIgnorePeriod = newSessionIgnorePeriod
        self._floodProtectionEnabled = floodProtectionEnabled
        self._floodProtectionRatio = floodProtectionRatio
        self._minSessionsToAllowProtection = minSessionsToAllowProtection
        self._floodProtectionMode = False
        self._shouldArchiveNoDeliveryTable = shouldArchiveNoDeliveryTable
        self._shouldArchiveDeliveryTrackingUpdatesToLine = shouldArchiveDeliveryTrackingUpdatesToLine
        self._deliveryTrackingArchiveTableInterval = deliveryTrackingArchiveTableInterval
        self._lastTimeArchiveDeliveryTrackingTable = 0 # Archive on sturtup


        if self._sessions is None or \
           self._windowSizeSec != windowSizeSec or \
           windowNumFrames != self._windowNumFrames:

            if self._sessions is not None:
                self._log("new-window").notice("Creating new sliding window. All existing sessions will be lost")
            self._sessions = SlidingWindow(windowSizeSec, windowNumFrames)
            self._windowSizeSec = windowSizeSec
            self._windowNumFrames = windowNumFrames

        if self._recentlyBlocked is None or \
           self._floodProtectionWindowSizeSec != floodProtectionWindowSizeSec or \
           floodProtectionWindowNumFrames != self._floodProtectionWindowNumFrames:

            if self._recentlyBlocked is not None:
                self._log("new-flood-prot-window").notice("Creating new flood protection sliding windows")
            self._recentlyBlocked = SlidingWindow(floodProtectionWindowSizeSec, floodProtectionWindowNumFrames)
            self._floodProtectionWindowSizeSec = floodProtectionWindowSizeSec
            self._floodProtectionWindowNumFrames = floodProtectionWindowNumFrames

        self._isInitialized = True


    def isUpdateNeeded (self, prevState, creationTimeSeconds):
        """The celler is responsible to keep track of the last session state and pass it to handleSession()
           The caller must know if a call to handleSession is needed because it may need to reload the surrent
           session state (i.e reload the brownie file)
        """

        if prevState == G_SESSION_STATE_WAIT:
            return True        

        if creationTimeSeconds is None:
            return False

        # Ignore sessions that are newer then the grace period. 
        # PrevState is still none becaue we never actually called handleSession on this session
        if prevState is None:
            if time.time()*1000.0 > creationTimeSeconds*1000.0 + self._newSessionIgnorePeriod:
                return True

        return False


    def handleSession (self, brownieData, prevState):
        """Count the session in the delivery tracking data structure
           Each session is counted only one time.
           When a session changes state from wait-state to active (or to ignored) we need to decrement 
           the wait-state counter.

           We need to tell the caller wat is the state of the session and expect it to pass it to us in the next call.
           In the first call for a new session, caller should pass "None" in prevState

        Args:
            brownieData: The brownie dictionary
            prevState: The last known state of this session, returned from a previous call, or "None" for new session

        Returns:
            state: The current state of the session. Caller needs to pass it to us in the next call, 
            in "prevState" argument

        Raises:
            None
        """

        # If we already determined that we don't have anything to do with this session, ignore it
        if prevState == G_SESSION_STATE_ERROR:
            return G_SESSION_STATE_ERROR

        # Extract session data from the brownie
        originalClientIp = brownieData.get('originalClientIp')
        playerId = brownieData.get('deliveryTrackingPlayerId')
        signatureGroupId = brownieData.get('deliveryTrackingSignatureGroupId')

        # Make sure we have all the key components
        if originalClientIp is None or playerId is None or signatureGroupId is None:
            self._log("missing-key").warning("Can't compute key. Some of the feilds are missing. Brownie data %s", brownieData)
            self._counters['deliveryTrackingNumInvalidKeySessions'] += 1
            # Ignore this session in the future
            return G_SESSION_STATE_ERROR

        # Extract the threshold values

        waitStateRatioThreshold = brownieData.get('deliveryTrackingWaitStateRatioThreshold')
        minWaitStateToBlock = brownieData.get('deliveryTrackingMinWaitStateToBlock')

        # Set default values if not present
        if waitStateRatioThreshold is None:
            waitStateRatioThreshold = G_DEFAULT_WAIT_STATE_RATIO_THRESHOLD
            self._log("missing-threshold1").warning("Missing wait-state-ratio threshold in brownie. Set to default %f. Brownie data %s", 
                                                    waitStateRatioThreshold, brownieData)
        if minWaitStateToBlock is None:
            minWaitStateToBlock = G_DEFAULT_MIN_WAIT_STATE_TO_BLOCK
            self._log("missing-threshold2").warning("Missing min-wait-state-to-block in brownie. Set to default %d. Brownie data %s", 
                                                    minWaitStateToBlock, brownieData)

        # Compose the session key and counter names
        key = self._composeKey(originalClientIp, playerId, signatureGroupId)
        waitStateCounterName = key + ":WAIT";
        activeStateCounterName = key + ":ACTIVE";

        # If we don't have ANY history about this key, we treat it as a new key
        countWait = self._sessions.getCount(waitStateCounterName)
        countActive = self._sessions.getCount(activeStateCounterName)
        isNewKey = (countWait == 0 and countActive == 0)

        # Is it a new session? (seen for the first time by the caller)
        isNewSession = (prevState is None)

        # Get the current atate of the session.
        state = self._getState(brownieData)
        if state is None:
            # Could not determine a valid state. Error was already logged.
            # Ignore this session in the future
            return G_SESSION_STATE_ERROR

        #
        # And now for the interesting stuff...
        #

        # New key
        if isNewKey:
            # A new key is counted only if it's in wait state
            if state == G_SESSION_STATE_WAIT:

                # Enforce size limit
                if self._sessions.getNumKeys() >= self._maxSessionKeys:
                    self._log("max-sessions-limit").error("Sessions size limit exceeded. Ignore key %s", key)
                else:
                    # Increment the wait-state counter. 
                    # No point to check thresholds at this moment (too early)
                    self._counters['deliveryTrackingNumSessionsBornInWaitState'] += 1
                    self._sessions.add(waitStateCounterName, 1)

            # return the state to the caller so that we can keep track on it untill it gets active (or ignored)
            return state

        fixedNow = False
        nothingChanged = False

        # Existing key. We already have history about it
        if isNewSession:
            # A new session for an existing key is always counted
            if state == G_SESSION_STATE_WAIT:
                self._counters['deliveryTrackingNumSessionsBornInWaitState'] += 1
                self._sessions.add(waitStateCounterName, 1)
            elif state == G_SESSION_STATE_ACTIVE:
                self._counters['deliveryTrackingNumSessionsBornInActiveState'] += 1
                self._sessions.add(activeStateCounterName, 1)
            elif state == G_SESSION_STATE_IGNORED_REDIRECT:
                self._counters['deliveryTrackingNumSessionsBornInIgnoredRedirectState'] += 1
                nothingChanged = True
            else:
                nothingChanged = True

        else:
            # An existing session needs to be fixed if changed from wait state to active or to ignored-redirect.
            if prevState == G_SESSION_STATE_WAIT and state == G_SESSION_STATE_ACTIVE:
                self._counters['deliveryTrackingNumSessionsBecomeActiveState'] += 1
                self._sessions.add(waitStateCounterName, -1)
                self._sessions.add(activeStateCounterName, 1)
                fixedNow = True
            elif prevState == G_SESSION_STATE_WAIT and state == G_SESSION_STATE_IGNORED_REDIRECT:
                self._counters['deliveryTrackingNumSessionsBecomeIgnoredRedirectState'] += 1
                self._sessions.add(waitStateCounterName, -1)
                fixedNow = True
            else:
                nothingChanged = True

        # It's important not to check thresholds if nothing changed (OSC-1600)
        if nothingChanged:
            return state

        # Check it we crossed thresholds
        self._checkThresholdsAndBlockIfNeeded(waitStateCounterName, activeStateCounterName, waitStateRatioThreshold, 
                                              minWaitStateToBlock, key, fixedNow)

        self._log("handle-session").debug3(
            "Handle session. Key %s. isNewSession %s. isNewKey %s. Curr state %s. Prev state %s. Wait %s. Active %s", 
            key, isNewSession, isNewKey, state, prevState, countWait, countActive)

        return state


    def writeNoDeliveryDelta (self, clearFirst=False):
        """Writes a delta file to Line with all the changes in no-delivery-table since the last successfull 
        call to this function
        """

        # TODO(amiry) - 
        # Most of the times we will not have any updates to this table.
        # We don't want to traverse the full table every second just to find out that we don't
        # need to write anything, so we need to set a flag every time we insert a new key to the table.
        # Only if this flag is set we start the iteration.
        # 
        # Problem is that we still need to check for expired records even if there are no updates.
        # To solve this we will keep track of the minimal expiration time and travers when first expiration arrive

    
        # If we have too many delta files we postpone the write. (Line is not reading deltas)
        # This is to protect disk space
        #files = os.listdir(self._deltaFilesDir)
        files = glob.glob(os.path.join(self._deltaFilesDir, self._deltaPattern+"*"+self._deltaSuffix))
        if len(files) > G_MAX_DELTA_FILES_IN_FOLDER:
            self._log("too-many-delta-files").error("Too many delta files in folder %s [%d]. Do not write delta. (Line is down?)", 
                                                    self._deltaFilesDir, len(files))
            return

        self._log("write-delta").debug3("writeNoDeliveryDelta() - Start")

        numLines = 0
        currentTime = time.time()
        deltaLines = []
        keysAdded = []
        keysDeleted = []

        if clearFirst:
            numLines += 1
            deltaLines.append(
                {
                    "seqNum": self._deltaSeqNum + numLines, 
                    "cmd": "DELETE_ALL",
                })

        for key, entry in self._noDeliveryTable.iteritems():
            cmd = None

            # Important to check expiration BEFORE we check if we need to add the key
            # because we might be loading an old table from file
            # 
            # Note that if expiration time is smaller than the delta write interval we might send
            # DELETE commands to non-existing keys in Line.
            # Line is supposed to handle a case of deleting a non existing key

            if currentTime - entry['expiration'] > 0 or entry.get('isDeleted'):
                if not clearFirst:
                    # If we cleared the table there is no need to send delete commands
                    self._log("write-delta-2").debug3("writeNoDeliveryDelta() - Append DELETE command on %s", key)
                    cmd = "DELETE"
                # But we do need to remove the expired/deleted records from the table
                keysDeleted.append(key)
            elif not entry['writtenToLine']:
                self._log("write-delta-2").debug3("writeNoDeliveryDelta() - Append ADD command on %s", key)
                cmd = "ADD"
                keysAdded.append(key)

            if cmd is not None:

                key_values = self._splitKey(key)
                if key_values is None:
                    self._log("key-unpack").error("Write No Delivery Delta: Error unpacking key %s. Ignore and delete from table", key)
                    keysDeleted.append(key)
                    continue

                numLines += 1
                originalClientIp = key_values[0]
                playerId = key_values[1]
                signatureGroupId = key_values[2]

                deltaLines.append(
                    {
                        "seqNum": self._deltaSeqNum + numLines, 
                        "cmd": cmd, 
                        "key": { 
                            "originalClientIp": originalClientIp,
                            "deliveryTrackingPlayerId": playerId,
                            "deliveryTrackingSignatureGroupId": signatureGroupId
                        }
                    })

            # Limit the size of each delta unless in snapshot mode
            if numLines >= G_DELTA_SIZE_LIMIT:
                self._log("max-delta-size").notice("No-Delivery-Delta to big. Break after after %d entry. Will continue next time.", numLines)
                break

        if len(keysAdded) == 0 and len(keysDeleted) == 0:
            self._counters['deliveryTrackingNumDeltaWritesNothingToDo'] += 1
            return

        if self._writeDeltaFile(deltaLines):
            for key in keysAdded:
                entry = self._noDeliveryTable[key] 
                entry['writtenToLine'] = True
            for key in keysDeleted:
                self._log("key-deleted").notice("Delete key %s. Either expired or whitelisted", key) 
                del(self._noDeliveryTable[key])

            self._log("delta-file-sent").debug1("Delta file sent. Keys added: %d, Keys deleted: %d, Clear First: %s", 
                                                len(keysAdded), len(keysDeleted), clearFirst) 

            self._noDeliveryTableChanged = True
            self._deltaSeqNum += numLines
            deltaTime = time.time() - currentTime
            self._totalDeltaWriteTime += deltaTime
            self._counters['deliveryTrackingNumDeltaWritesSucceeded'] += 1
            self._counters['deliveryTrackingNumDeltaLinesWritten'] += numLines
            self._counters['deliveryTrackingAvgDeltaWriteTime'] = self._totalDeltaWriteTime / (self._counters['deliveryTrackingNumDeltaWritesSucceeded']*1.0)
        else:
            # Specific error was already logged
            self._counters['deliveryTrackingNumDeltaWritesFailed'] += 1
            self._log("write-delta-file").error("Could not write delta file") 


    def sendClearNoDeliveryTableCommand (self):
        """Send a clear command to Line. Do not clear the actual table
        caller is responsible to call this function if delivery tracking is disabled
        """

        if not self._isInitialized:
            self._log("uninitialized").warning("sendClearNoDeliveryTableCommand() called when delivery tracking is not initialized") 
            return False
    
        deltaLines = []
        deltaLines.append(
            {
                "seqNum": self._deltaSeqNum + 1, 
                "cmd": "DELETE_ALL",
            })

        if self._writeDeltaFile(deltaLines):
            self._deltaSeqNum += 1
            self._log("clear-table").notice("Send clear no-delivery-table command to Line") 
        else:
            # Specific error was already logged
            self._log("clear-table-error").error("Can't clear no-delivery table") 
            return False

        return True


    def clearNoDeliveryTable (self):
        self._log("user-clear-table").notice("Execute user clear table command")
        if self.sendClearNoDeliveryTableCommand():
            self._noDeliveryTable  = {}
            self._noDeliveryTableChanged = True
            self.saveNoDeliveryTable()
            self._sessions.reset()


    def removeKey (self, keyToRemove):
        self._log("user-remove-key-command").notice("Execute user remove key command. Regex=", keyToRemove)
        regex = re.compile(keyToRemove)
        for key, entry in self._noDeliveryTable.iteritems():
            if regex.match(key):
                self._log("user-remove-key").notice("Remove key", key)
                entry["isDeleted"] = True
                self._noDeliveryTableChanged = True
        self.saveNoDeliveryTable()


    def saveNoDeliveryTable(self):

        if not self._noDeliveryTableChanged:
            self._log("table-not-saved").debug3("No delivery table not saved. No change")
            return

        try:
            filename = os.path.join(self._dataDir, G_NO_DELIVERY_TABLE_FILE_NAME)
            a.infra.format.json.writeToFile(self._log, self._noDeliveryTable, filename)
            self._log("table-saved").debug3("No delivery table saved to file %s. %d entries", filename, len(self._noDeliveryTable))
            self._noDeliveryTableChanged = False

            currentTime = time.time()
            if (currentTime - self._lastTimeArchiveDeliveryTrackingTable < self._deliveryTrackingArchiveTableInterval):
                return

        except Exception as ex:
            self._log("write-table-error").error("Error in write no-delivery table to file %s. %s", filename, ex)
            return

        # Archive
        if self._shouldArchiveNoDeliveryTable and self._archiver:
            archiveFailed = False
            archiveFilename = None
            try:
                archiveFilename = os.path.join(self._tempDir, os.path.basename(filename))
                shutil.copyfile(filename, archiveFilename)
                if self._archiver.archiveFile(archiveFilename):
                    self._lastTimeArchiveDeliveryTrackingTable = time.time()
                else:
                    archiveFailed = True
            except Exception as ex:
                self._log("error-archive-table").error("Error in archive no-delivery-table. file %s. %s", archiveFilename, ex)
                archiveFailed = True

            if archiveFailed:
                os.remove(archiveFilename)


    def loadNoDeliveryTable (self):
        try:
            filename = os.path.join(self._dataDir, G_NO_DELIVERY_TABLE_FILE_NAME)
            self._noDeliveryTable = a.infra.format.json.readFromFile(self._log, filename)
            self._noDeliveryTableChanged = False
        except Exception as ex:
            self._log("read-table-error").warning("Error in load no-delivery table from file %s. %s", filename, ex)
            return

        self._log("table-loaded").notice("Loading No delivery table from file %s. %d entries", filename, len(self._noDeliveryTable))

        # TODO(amiry) - Validate json data. Less important because this is not a user file

        # Mark all entries to be written to in the next delta.
        # Whitelisted entries are deleted.
        # Expired entries will be removed when writing delta (in the normal expiration path).

        whitelisted = []
        for key in self._noDeliveryTable:
            rules = self._isWhitelisted(key)
            if rules:
                self._log("whitelisted-in-load-table").notice("Load No Delivery Table: Key %s not loaded due to whitelist rules %s", key, rules)
                whitelisted.append(key)
            else:
                self._noDeliveryTable[key]['writtenToLine'] = False

        for key in whitelisted:
            del(self._noDeliveryTable[key])

        if whitelisted:
            self._noDeliveryTableChanged = True

        # Don't wait to the next interval. This will also remove all expired entries.
        self.writeNoDeliveryDelta(clearFirst=True)


    def loadWhitelist (self):
        """Loads the whitelist json file. Should be called upon signal
        """

        if self._whitelistFile is None:
            self._whitelist = None
            return

        filename = os.path.join(self._confDir, self._whitelistFile)

        try:
            jsonData = a.infra.format.json.readFromFile(self._log, filename)
        except Exception as ex:
            self._log("read-whitelist-error").error("Error in read whitelist file %s. %s. Whitelist cleared", filename, ex)
            self._whitelist = None
            return

        self._log("load-whitelist").notice("Loading whitelist from file %s", filename)

        try:
            # Create a regex which is an "OR" between all strings in the whitelist strings-list, with capture.
            whitelist = jsonData['whitelist']
            for i in range(len(whitelist)):
                whitelist[i]="(%s)" % whitelist[i]
            regex = "|".join(whitelist)
            self._whitelist = re.compile(regex)
        except (ValueError, KeyError) as ex:
            # Since whitelist is a user file, validation is important
            self._log("invalid-whitelist").error("Invalid whitelist in json file %s. %s. Whitelist cleared", self._whitelistFile, ex)
            self._whitelist = None
            return

        # Delete all entries that are now whitelisted
        writeDelta = False
        for key in self._noDeliveryTable:
            rules = self._isWhitelisted(key)
            if rules:
                self._log("whitelisted-in-load-whitelist").notice("Load whitelist: Key %s deleted due to whitelist rules %s", key, rules)
                self._noDeliveryTable[key]['isDeleted'] = True
                self._noDeliveryTableChanged = True
                writeDelta = True

        if writeDelta:
            self.writeNoDeliveryDelta()


    def checkFloodProtection(self):

        if not self._floodProtectionEnabled:
            self._floodProtectionMode = False
            return

        # TODO(amiry) - This number is not accurate because it doesn't reflect the total number of sessions.
        # Only the sessions that were born in wait state.
        totalSessions = self._sessions.getNumKeys()
        if totalSessions == 0:
            return

        thresholdCrossed = False
        currentBlockCount = self._recentlyBlocked.getNumKeys()
        if currentBlockCount / (totalSessions*1.0) >= self._floodProtectionRatio and totalSessions >= self._minSessionsToAllowProtection:
            thresholdCrossed = True

        # It threshold is crossed and we are not in flood protection mode we enter flood protection
        if thresholdCrossed and not self._floodProtectionMode:
            self._log("enter-flood-protection-mode").notice(
                "Delivery Tracking enter flood protection mode. "
                "%d keys blocked in the last %d seconds, out of total %d keys. Min to block is %d", 
                currentBlockCount, self._floodProtectionWindowSizeSec, totalSessions, self._minSessionsToAllowProtection)
            self._floodProtectionMode = True

            """"
            CURRENTLY WE DO NOT SEND CLEAR COMMAND. WE JUST WANT TO KNOW ABOUT THIS STATE
            self.sendClearNoDeliveryTableCommand()
            """

            return

        # We are not in flood protection mode, and below threshold. We need at least "widow size" of 
        # silence to release the hook
        if self._floodProtectionMode and not thresholdCrossed and self._sessions.getNumKeys() == 0:
            self._log("leave-flood-protection-mode").notice("Delivery Tracking leave flood protection mode")
            self._floodProtectionMode = False


    def enable (self, startup):

        if startup:
            # On startup, also load the no delivery table
            self.loadNoDeliveryTable()
        else:
            # Need to send table to line
            for entry in self._noDeliveryTable.values():
                entry['writtenToLine'] = False
            self.sendClearNoDeliveryTableCommand()

        # reload the whitelist
        self.loadWhitelist()


    def disable (self):
        # When disabled we need to send a clear command to Line,
        # and reset all session counters.
        self.sendClearNoDeliveryTableCommand()
        self._sessions.reset()


    def getNumKeys (self):
        return self._sessions.getNumKeys()


    def getNoDeliveryTableSize (self):
        return len(self._noDeliveryTable)


    # --- Public for unit test ---
    def getSessionCountersForUnitTest (self, originalClientIp, playerId, signatureGroupId):
        key =  self._composeKey(originalClientIp, playerId, signatureGroupId)
        waitStateCounterName = key + ":WAIT";
        activeStateCounterName = key + ":ACTIVE";
        return (self._sessions.getCount(waitStateCounterName), self._sessions.getCount(activeStateCounterName))

    def getNoDeliveryTableEntryForUnitTest (self, originalClientIp, playerId, signatureGroupId):
        key =  self._composeKey(originalClientIp, playerId, signatureGroupId)
        return self._noDeliveryTable[key]

    def getFloodProtectionStateForUnitTest (self):
        return self._floodProtectionMode

    def clearSessionKeysForUnitTest (self):
        return self._sessions.reset()

    # ----------------------------


    def _getState (self, brownieData):
        wasUsed = brownieData.get('wasUsed', False)
        ignoredRedirect = brownieData.get('ignoredRedirect', False)

        if wasUsed and ignoredRedirect:
            self._log("bad-state").error("Brownie is used by delivery and marked an ignored-redirect. Impossible! Brownie data %s", 
                                         brownieData)
            self._counters['deliveryTrackingNumInvalidStateSessions'] += 1
            return None

        if not wasUsed and not ignoredRedirect:
            return G_SESSION_STATE_WAIT
        if not wasUsed:
            return G_SESSION_STATE_IGNORED_REDIRECT

        return G_SESSION_STATE_ACTIVE


    def _checkThresholdsAndBlockIfNeeded (self, waitStateCounterName, activeStateCounterName, waitStateRatioThreshold, 
                                          minWaitStateToBlock, key, fixedNow):

        numWait = self._sessions.getCount(waitStateCounterName)
        numActive = self._sessions.getCount(activeStateCounterName)

        # This can happen when state changes from wait to active or to ignored redirect.
        # numWait can be negative because we decrement it when session become active.
        # If the positive value dropped out of the sliding window we get a negative value.
        if numWait <= 0:
            return

        ratio = numWait / (numWait+numActive*1.0)
        if ratio >= waitStateRatioThreshold and numWait >= minWaitStateToBlock:
            self._blockKey(key)
        elif fixedNow:
            self._setShortTTLIfNeeded(key)


    def _blockKey (self, key):
        if key not in self._noDeliveryTable:

            """"
            CURRENTLY WE DO NOT ENFORCE FLOOD PROTECTION

            # Enforce flood-protection mode
            if self._floodProtectionMode:
                self._counters['deliveryTrackingNumSessionsBlockedInFloodProtection'] += 1
                self._log("flood-prot").error("Block key: Key % s not blocked due to flood protection mode")
                return
            """

            # Enforce size limit
            if len(self._noDeliveryTable) >= self._maxNoDeliveryTableSize:
                self._counters['deliveryTrackingNumSessionsBlockedOverSizeLimit'] += 1
                self._log("size-limit").error("Block key: Key % s not blocked due to no-delivery-table size limit %d", key, len(self._noDeliveryTable))
                return

            # Enforce whitelist
            rules = self._isWhitelisted(key)
            if rules:
                self._counters['deliveryTrackingNumSessionsWhitelisted'] += 1
                self._log("whitelist").notice("Block Key: Key %s not blocked due to whitelist rules %s", key, rules)
                return

            self._counters['deliveryTrackingNumBlocked'] += 1
            expiration = time.time() + self._blockTTLSec
            self._noDeliveryTable[key] = {'writtenToLine':False, 'expiration':expiration, 'shortTTL':False}
            self._noDeliveryTableChanged = True
            self._recentlyBlocked.add(key, 1)
            self._log("whitelist").notice("Block Key: Key %s blocked", key)

        else:
            # If the key is already blocked with short ttl we need to set it back to the normal TTL
            if self._noDeliveryTable[key].get('shortTTL'):
                # Do not rewrite to Line
                expiration = time.time() + self._blockTTLSec
                self._noDeliveryTable[key]['shortTTL'] = False
                self._noDeliveryTable[key]['expiration'] = expiration
                self._noDeliveryTableChanged = True


    def _setShortTTLIfNeeded (self, key):
        if key in self._noDeliveryTable:
            # Do not rewrite to Line
            expiration = time.time() + self._shortBlockTTLSec
            self._noDeliveryTable[key]['shortTTL'] = True
            self._noDeliveryTable[key]['expiration'] = expiration
            self._noDeliveryTableChanged = True


    def _isWhitelisted (self, key):
        if self._whitelist is not None:
            # Check against whitelist
            match = self._whitelist.match(key)
            if match:
                rules = []
                for g in match.groups():
                    if g is not None:
                        rules.append(g)
                return rules
        return None


    def _composeKey (self, originalClientIp, playerId, signatureGroupId):
        # We assume that this delimiter is safe to use (Will mever appear in the data)
        return ":QWILT:".join([originalClientIp, playerId, signatureGroupId])


    def _splitKey (self, key):
        values = key.split(":QWILT:")
        if len(values) != 3:
            return None
        return values


    def _writeDeltaFile (self, deltaLines):

        # First we rotate to get a fresh file name
        self._deltaFile.rotate()

        deltaFilename = self._deltaFile.getCurrentFileName()
        archiveFilename = None

        # If we need to archive the delta file, we first save a copy.
        # Remember that the delta file is consumed by the Line and deleted.
        if self._shouldArchiveDeliveryTrackingUpdatesToLine and self._archiver:
            try:
                archiveFilename = os.path.join(self._tempDir, os.path.basename(deltaFilename))
                a.infra.format.json.writeToFile(self._log, {"deltaLine":deltaLines}, archiveFilename)
            except Exception as ex:
                self._log("error-write-delta-file-for-archive").error(
                    "Error in write delta file for archiving. File %s. %s", archiveFilename, ex)

        # Now we create the delta file.
        try:
            if archiveFilename:
                shutil.copyfile(archiveFilename, deltaFilename)
            else:
                a.infra.format.json.writeToFile(self._log, {"deltaLine":deltaLines}, deltaFilename)
        except Exception as ex:
            self._log("error-write-delta-file").error("Error in write delta file %s. %s", deltaFilename, ex)
            return False

        # Finally we archive it
        if archiveFilename:
            archiveFailed = False
            try:
                if not self._archiver.archiveFile(archiveFilename):
                    archiveFailed = True
            except Exception as ex:
                self._log("error-archive-delta-file").error("Error in archive delta file %s. %s", archiveFilename, ex)
                archiveFailed = True
            if archiveFailed:
                os.remove(archiveFilename)

        # If we arrived here the delta write was okay. 
        # Archiving doesn't affect the return value
        return True

