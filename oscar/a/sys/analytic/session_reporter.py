# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: adana

#import time
import time
import collections
import topper_record_utils
import a.infra.container.linked_list

__pychecker__="no-reuseattr"

MILLI_SEC = 1000
SORT_DELAY = 60
REPORT_INTERVAL_IN_SEC = 5*60 # 5 minutes
SESSION_AGEING_IN_SEC = 2*60 # 2 minutes

TIME_UNTIL_AUTO_ADVANCE = 20
MIN_TIME_BETWEEN_KEEP_ALIVES = 30

DEFAULT_FIELDS_SEPERATOR = ","

class sessionRetCodes:
    retOk = 0
    retOutOfBound = 1

class SessionReportCfg:
    def __init__(self, cfg):
        self.minTransactionDurationMsec = cfg.sessionMinTransactionDurationMsec
        self.minTransactionVolume = cfg.sessionMinTransactionVolume
        #self.minSessionDuration = cfg.minSessionDuration
        #self.minSessionVolume = cfg.minSessionVolume

# session info in a specific time slice
class SessionSliceInfo(object):
    def __init__(self, cfg, startTimeInMilli, sliceDurationInMSec):
        self._cfg = cfg
        self.startTimeInMilli = startTimeInMilli
        self.lineVol = 0
        self.deliveryVol = 0
        self.endTimeInMilli = startTimeInMilli
        self.sessionStartIndication = False
        self.lineTransactionsDuration = 0
        self.deliveryTransactionsDuration = 0
        self.numLineStartTransactions = 0
        self.numLineEndTransactions = 0
        self.numLineContinuingTransactions = 0
        self.numDeliveryStartTransactions = 0
        self.numDeliveryEndTransactions = 0
        self.numDeliveryContinuingTransactions = 0
        self.numFRecordsInSlice = 0
        self._sliceDurationInMSec = sliceDurationInMSec

    def isTimeContainedInSlice(self, timeInMilli):
        if (timeInMilli < self.startTimeInMilli) or (timeInMilli >= self.startTimeInMilli + self._sliceDurationInMSec):
            return False

        return True

    # update session with new f record info
    def update(self, fRecord, endTimeInMilli, isSessionStart):
        self.sessionStartIndication |= isSessionStart
        vol = fRecord.getVolume()

        if (fRecord.downloadTimeMsec >= self._cfg.minTransactionDurationMsec) and (vol >= self._cfg.minTransactionVolume):
            if not fRecord.isDelivered:
                self.lineVol += vol
                self.lineTransactionsDuration += fRecord.downloadTimeMsec
    
                if fRecord.isTransactionStart:
                    self.numLineStartTransactions += 1
                else:
                    if (endTimeInMilli - fRecord.downloadTimeMsec) < self.startTimeInMilli:
                        self.numLineContinuingTransactions += 1

                if fRecord.isTransactionEnd:
                    self.numLineEndTransactions += 1
            else:
                self.deliveryVol += vol
                self.deliveryTransactionsDuration += fRecord.downloadTimeMsec
    
                if fRecord.isTransactionStart:
                    self.numDeliveryStartTransactions += 1
                else:
                    if (endTimeInMilli - fRecord.downloadTimeMsec) < self.startTimeInMilli:
                        self.numDeliveryContinuingTransactions += 1
    
                if fRecord.isTransactionEnd:
                    self.numDeliveryEndTransactions += 1


        self.endTimeInMilli = max(self.endTimeInMilli, endTimeInMilli)

        self.numFRecordsInSlice += 1

    # return true if the current time slice has any data in it
    def hasData(self):
        if self.numFRecordsInSlice != 0:
            return True

        return False

    def adjustStartTime(self, newStartTime):
        self.startTimeInMilli = newStartTime

    # set S record data with the current time slice info
    def updateSRecord(self, record):
        record.timeOfDay = ((self.startTimeInMilli + self._sliceDurationInMSec) / MILLI_SEC) - 1 # place the record in the last second of the report window
        record.nanosec = (self.startTimeInMilli % MILLI_SEC) * 1000000
        record.lineVolume = self.lineVol
        record.deliveryVolume = self.deliveryVol
        record.duration = self.endTimeInMilli - self.startTimeInMilli
        record.isSessionStart = self.sessionStartIndication
        record.sumLineTransactionDuration = self.lineTransactionsDuration
        record.sumDeliveryTransactionDuration = self.deliveryTransactionsDuration
        record.numLineStartTransaction = self.numLineStartTransactions
        record.numLineEndTransaction = self.numLineEndTransactions
        record.numLineContinuingTransaction = self.numLineContinuingTransactions
        record.numDeliveryStartTransaction = self.numDeliveryStartTransactions
        record.numDeliveryEndTransaction = self.numDeliveryEndTransactions
        record.numDeliveryContinuingTransaction = self.numDeliveryContinuingTransactions

# Session information
class SessionInfo(a.infra.container.linked_list.Node):
    def __init__(self, cfg, fRecord, reportIntervalInSec):
        a.infra.container.linked_list.Node.__init__(self)
        
        self._cfg = cfg

        self._isInSessionDb = False
        self._sessionId = fRecord.sessionId
        self._titleId = fRecord.titleId
        self._startTimeInMilli = fRecord.unixStartTime
        self._lastEntryTod = fRecord.timeOfDay
        self._siteName = fRecord.siteName
        self._timeSlices = collections.deque()
        self._isSessionEnd = False
        self._reportIntervalInMSec = reportIntervalInSec * MILLI_SEC
        self._sessionIdExtractorIndex = fRecord.sessionIdExtractorIndex

        # Add two time slices one for current and one for next
        self._timeSlices.append(SessionSliceInfo(self._cfg, self._startTimeInMilli, self._reportIntervalInMSec)) 
        self._timeSlices.append(SessionSliceInfo(self._cfg, self._startTimeInMilli + self._reportIntervalInMSec, self._reportIntervalInMSec)) 

        self._numFRecords = 0

    # Returns true if the session is currently placed in the session database
    @property
    def isInSessionDb(self):
        return self._isInSessionDb

    @isInSessionDb.setter
    def isInSessionDb(self, val):
        self._isInSessionDb = val

    # returns the number of F records in this session
    @property
    def numFRecords(self):
        return self._numFRecords

    @property
    def sessionId(self):
        return self._sessionId

    @property
    def startTime(self):
        return self._startTimeInMilli

    @property
    def startTimeInSec(self):
        return (self._startTimeInMilli / MILLI_SEC)

    @property
    def lastEntryTod(self):
        return self._lastEntryTod

    @property
    def isSessionEnd(self):
        return self._isSessionEnd

    # adjust the start time for all time slices in the session
    def adjustStartTime(self, newStartTime):
        self._startTimeInMilli = newStartTime

        sliceStartTime = self._startTimeInMilli
        for tslice in self._timeSlices:
            tslice.adjustStartTime(sliceStartTime)
            sliceStartTime += self._reportIntervalInMSec

    # Add an frecord to the session 
    def addFRecord(self, fRecord):
        endTimeMilli  = fRecord.unixStartTime + fRecord.transactionDownloadTimeMsec

        # search for the time slice this F record belongs to
        foundTimeSlice = False
        for tslice in self._timeSlices:
            if tslice.isTimeContainedInSlice(endTimeMilli):
                foundTimeSlice = True
                break

        if not foundTimeSlice:
            return sessionRetCodes.retOutOfBound

        tslice.update(fRecord, endTimeMilli, (self._numFRecords == 0))

        self._lastEntryTod = max(self._lastEntryTod, fRecord.timeOfDay)
        self._numFRecords += 1

        return sessionRetCodes.retOk

    def createSRecordFromSlice(self, timeSlice, isSessionEnd):
        record = topper_record_utils.SRecordHelper(None)
        record.createNewRecord()
        
        timeSlice.updateSRecord(record)
        record.sessionId = self._sessionId
        record.titleId = self._titleId
        record.siteName = self._siteName
        record.isSessionEnd = isSessionEnd
        record.sessionIdExtractorIndex = self._sessionIdExtractorIndex

        # if this is not the session end than we need to fix the duration to be the entire time slice
        if not isSessionEnd:
            record.duration = self._reportIntervalInMSec

        return record

    def processCurrTimeSlice(self, reporterObj):
        currSlice = self._timeSlices.popleft()
        nextSlice = self._timeSlices[0]
        
        # if next slice has no data than the session has aged if not than add a new time slice
        if not nextSlice.hasData():
            self._isSessionEnd = True
            # session has ended remove it from the session data base
            reporterObj.removeFromSessionDb(self)
        else:
            self._timeSlices.append(SessionSliceInfo(self._cfg, nextSlice.startTimeInMilli + self._reportIntervalInMSec, self._reportIntervalInMSec)) 
            # session has not ended therefore the session should be placed to report in REPORT_INTERVAL_IN_SEC from now
            reporterObj._timeSlicesArray.addItemAtOffset((self._reportIntervalInMSec / MILLI_SEC), self)

        sRecord = self.createSRecordFromSlice(currSlice, self._isSessionEnd)

        return sRecord

class KeepAliveItem(a.infra.container.linked_list.Node):
    def __init__(self, reportTime):
        self._reportTime = reportTime

    def createKeepAliveRecord(self, recordTime):
        record = topper_record_utils.SRecordHelper(None)
        record.createNewRecord()

        record.sessionId = 0
        record.titleId = 0
        record.isSessionEnd = 0
        record.timeOfDay = recordTime
        record.nanosec = 0
        record.lineVolume = 0
        record.deliveryVolume = 0
        record.duration = 0
        record.isSessionStart = 0
        record.sumLineTransactionDuration = 0
        record.sumDeliveryTransactionDuration = 0
        record.numLineStartTransaction = 0
        record.numLineEndTransaction = 0
        record.numLineContinuingTransaction = 0
        record.numDeliveryStartTransaction = 0
        record.numDeliveryEndTransaction = 0
        record.numDeliveryContinuingTransaction = 0
        record.sessionIdExtractorIndex = 0

        return record

    def processCurrTimeSlice(self, reporterObj):
        __pychecker__='no-argsused'
        return self.createKeepAliveRecord(self._reportTime)


# A cyclic array of session lists
class CyclicArrayOfLinkedLists(object):
    def __init__(self, arraySize):
        self._arraySize = arraySize
        self._currPos = 0
        self._array = []
        self._numItemsInArray = 0

        for i in range(arraySize):
            self._array.append(a.infra.container.linked_list.LinkedList())

        i = i + 1  #for pychecker

    @property
    def numItems(self):
        return self._numItemsInArray

    def advance(self):
        self._currPos = (self._currPos + 1) % self._arraySize 

    def popItemFromCurrentPos(self):
        item = self._array[self._currPos].popHead()

        if item:
            self._numItemsInArray -= 1

        return item

    def addItemAtOffset(self, offset, item):
        insertPos = (self._currPos + offset) % self._arraySize 

        self._array[insertPos].pushTail(item)

        self._numItemsInArray += 1
        
    def removeItem(self, item):
        item.removeFromList()
        self._numItemsInArray -= 1

class SessionReporter(object):

    class Counters(object):
        def __init__(self):
            self.sessions_numSessionsCreated = 0
            self.sessions_maxConcurrentSessions = 0
            self.sessions_numAdjustSessionsStartTime = 0
            self.sessions_numDroppedOldFRecords = 0
            self.sessions_numDroppedNoSessionIdFRecords = 0
            self.sessions_numDroppedRedirectedFRecords = 0
            self.sessions_numDroppedInvalidFRecords = 0
            self.sessions_numFRecordsForAgedSessions = 0
            self.sessions_numDroppedOldSessions = 0
            self.sessions_timeAutoAdvanceCount = 0
            self.sessions_internalTime = 0
        
    def __init__(self):
        self._cfg = None
        self._timeSlicesArray = None
        self._sessionsDb = {}
        self._currTime = 0
        self._counters = SessionReporter.Counters()
        self._outputSRecords = collections.deque()
        self._fieldSeperator = DEFAULT_FIELDS_SEPERATOR
        self._lastTimeRecordWasProcessed = time.time()
        self._logger = None
        self.__currFRecord = topper_record_utils.FRecordHelper(None)
        self._lastKeepAliveTime = 0


        self._sortDelay = SORT_DELAY
        self._reportIntervalInSec = REPORT_INTERVAL_IN_SEC
        self._sessionAgingInSec = SESSION_AGEING_IN_SEC
        self._timeUntilAutoAdvance = TIME_UNTIL_AUTO_ADVANCE
        self._minTimeBetweenKeepAlives = MIN_TIME_BETWEEN_KEEP_ALIVES


    def initLogger(self, logger):
        self._logger = logger

    def initCfg(self, cfg):
        self._cfg = SessionReportCfg(cfg)
        self._sortDelay = cfg.sessionSortDealy
        self._reportIntervalInSec = cfg.sessionReportInterval
        self._sessionAgingInSec = cfg.sessionAgingTime
        self._timeUntilAutoAdvance = cfg.sessionTimeUntilAutoAdvance

        self._logger("session-cfg").debug1("sortDelay = %d, reportIntervalInSec = %d, sessionAgingInSec = %d, timeUntilAutoAdvance = %d", self._sortDelay,self._reportIntervalInSec,self._sessionAgingInSec,self._timeUntilAutoAdvance)

        self._timeSlicesArray = CyclicArrayOfLinkedLists((self._sortDelay + self._reportIntervalInSec + self._sessionAgingInSec) * 2)

        self.setRecordFieldSeperator(cfg.fieldsSeperator)

    def setRecordFieldSeperator(self, fieldsSeperator):
        self._fieldsSeperator = fieldsSeperator

    def getCounters(self):
        self._counters.sessions_internalTime = self._currTime
        return self._counters

    # returns the S record queue (where all output S records are placed)
    def getOutputSRecords(self):
        return self._outputSRecords

    def numSessions(self):
        return len(self._sessionsDb)

    def addToSessionDb(self, session):
        self._sessionsDb[session.sessionId] = session
        session.isInSessionDb = True

        self._counters.sessions_maxConcurrentSessions = max(self._counters.sessions_maxConcurrentSessions, self.numSessions())

    def removeFromSessionDb(self, session):
        # check if the session was already taken out of the data base
        if session.isInSessionDb:

            self._logger("remove-session").debug1("Removing session %d", session.sessionId)

            del self._sessionsDb[session.sessionId]
            session.isInSessionDb = False

    def adjustSessionStartTime(self, session, newStartTimeInSec):
        # remove the session from the its current time slice list. The session will be added to a different time slice later
        self._timeSlicesArray.removeItem(session)
        # adjust the session time start time
        session.adjustStartTime(newStartTimeInSec)

        self._counters.sessions_numAdjustSessionsStartTime += 1

    def writeSRecordToOutputQueue(self, sRecord):
        self._logger("writing-record").debug3("Writing record: %s" % self._fieldsSeperator.join(sRecord.record))
        self._outputSRecords.append(self._fieldsSeperator.join(sRecord.record))

    def processCurrTimeSlot(self):
        # scan all sessions in the current time slice
        item = self._timeSlicesArray.popItemFromCurrentPos()
        while item:
            sRecord = item.processCurrTimeSlice(self)
            # write session S record in the output queue
            self.writeSRecordToOutputQueue(sRecord)

            item = self._timeSlicesArray.popItemFromCurrentPos()

    def __advanceTimeInternal(self, newTime):
        if self._currTime >= newTime:
            return

        # if there are no sessions we can set the current time without advancing the time slice arraySize`
        if self._timeSlicesArray.numItems == 0:
            self._currTime = newTime
            self._logger("advance-time1").debug3("Advanced time to %d", self._currTime)
            return

        # scan all time slices and process all sessions that are stored in them
        for time in range((self._currTime + 1), (newTime + 1)):
            self._timeSlicesArray.advance()
            self.processCurrTimeSlot()
            self._currTime = time
            self._logger("advance-time2").debug3("Advanced time to %d", self._currTime)

    def advanceTime(self, newTime, currentTime):
        self._lastTimeRecordWasProcessed = currentTime
        self.__advanceTimeInternal(newTime - self._sortDelay)

    def keepAlive(self, newTime, currentTime):
        self.advanceTime(newTime, currentTime)
        
        if (newTime - self._lastKeepAliveTime) >= self._minTimeBetweenKeepAlives:
            # set keep alive to send a record in (self._reportIntervalInSec + self._sessionAgingInSec) from current time
            # time stamp used for keep alive is (current time + self._reportIntervalInSec - 1). The reason is so that time stamp will be same as session reports time stamps for the same time slot
            positionInArray = self._reportIntervalInSec + self._sessionAgingInSec + self._sortDelay
            self._timeSlicesArray.addItemAtOffset(positionInArray, KeepAliveItem(newTime + self._reportIntervalInSec - 1))
    
            self._lastKeepAliveTime = newTime

    def createNewSession(self, fRecord):
        newSession = SessionInfo(self._cfg, fRecord, self._reportIntervalInSec)
        
        self.addToSessionDb(newSession)

        self._counters.sessions_numSessionsCreated += 1

        self._logger("create-session").debug1("Creating session %d at time %d", newSession.sessionId, newSession.startTimeInSec)

        return newSession

    # Runs periodically (every second) and if no F record where processed in the last TIME_UNTIL_AUTO_ADVANCE seconds it advances the current time by 1 second
    # This is done so sessions will be processed even if the F records stop arriving
    def doPeriodicWork(self, currentTime):
        if (((currentTime - self._lastTimeRecordWasProcessed) > self._timeUntilAutoAdvance) and (self._timeSlicesArray.numItems > 0)):
            self.__advanceTimeInternal(self._currTime + 1)
            self._counters.sessions_timeAutoAdvanceCount += 1

    def processFRecord(self, record, currentTime):
        self.__currFRecord.setRecord(record)

        # advance the current time
        # we set the time to the newest frecord time - sort time in case where old frecords are received. In this case the current time will still be smaller than the frecord time 
        self.advanceTime(self.__currFRecord.timeOfDay, currentTime)

        # ignore frecord if its time is too old or there is no session id or if this is the frecord of a redirected line transaction
        if (self.__currFRecord.timeOfDay < self._currTime):
            self._counters.sessions_numDroppedOldFRecords += 1
            return

        if (self.__currFRecord.sessionId == 0): 
            self._counters.sessions_numDroppedNoSessionIdFRecords += 1
            return

        if (self.__currFRecord.wasRedirected):
            self._counters.sessions_numDroppedRedirectedFRecords += 1
            return


        fRecordStartTimeInSec = self.__currFRecord.unixStartTime / MILLI_SEC

        # find session in session db
        session = None
        if self.__currFRecord.sessionId in self._sessionsDb:
            # found session in db
            session = self._sessionsDb[self.__currFRecord.sessionId]

            # if the f record time is not too old and the its start time is smaller that the session start time then adjust the session start time the the new time
            if (fRecordStartTimeInSec >= self._currTime) and (self.__currFRecord.unixStartTime < session.startTime):
                self.adjustSessionStartTime(session, self.__currFRecord.unixStartTime)

            # check if the entry has aged. if so remove it from the session hash and create a new one.
            # the session is left in the timeslice array so it will be reported
            if (session.lastEntryTod + self._sessionAgingInSec) < self.__currFRecord.timeOfDay:
                self.removeFromSessionDb(session)
               
                if not session.isInList():
                    # Note: due to the fact the the session aging time is larger than the sort delay the case where session time is adjusted 
                    #       and the session is aged at the same time should never happen
                    self._logger("session-aged-and-adjusted").error("session time was adjusted and aged due as a result of the same F record")
                    
                # set session to None to signal that a new session should be created
                session = None

                self._counters.sessions_numFRecordsForAgedSessions += 1

        if session == None:
            if fRecordStartTimeInSec < self._currTime:
                # old session we don't create a record for it
                self._counters.sessions_numDroppedOldSessions += 1
                return

            session = self.createNewSession(self.__currFRecord)

        # add f record to the session
        if session.addFRecord(self.__currFRecord) != sessionRetCodes.retOk:
            if session.numFRecords == 0:
                # Remove this session because it was added using an invalid F record
                self.removeFromSessionDb(session)
                self._timeSlicesArray.removeItem(session)
                self._counters.sessions_numDroppedInvalidFRecords += 1
                return

        # if the session is not in any time slice add it to the appropriate time slice
        if not session.isInList():
            positionInArray = session.startTimeInSec + self._reportIntervalInSec + self._sessionAgingInSec - self._currTime
            self._timeSlicesArray.addItemAtOffset(positionInArray, session)

