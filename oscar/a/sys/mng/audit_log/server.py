#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import os
import time
import glob
import a.infra.format.json
import a.infra.process
import a.api.user_log.msg.sys


if  __package__ is None:
    G_NAME_MODULE_SYS_AUDIT_LOG_SERVER = "unknown"
    G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_GENERAL = "unknown"    
    G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_READ = "unknown"    
    G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_WRTIE = "unknown"   
    G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_CLEAR = "unknown"
else:
    from . import G_NAME_MODULE_SYS_AUDIT_LOG_SERVER
    from . import G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_GENERAL
    from . import G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_READ
    from . import G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_WRITE
    from . import G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_CLEAR
    
class Server(object):

    INPUT_GENERATION_COMMAND_START_TIME_PLACE_HOLDER = "%start-time"

    _STATE_FILE_KEY_START_TIME = "start-time"

    def __init__(self, logger):
        self._logGeneral = logger.createLogger(G_NAME_MODULE_SYS_AUDIT_LOG_SERVER, G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_GENERAL)
        self._logRead = logger.createLogger(G_NAME_MODULE_SYS_AUDIT_LOG_SERVER, G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_READ)
        self._logWrite = logger.createLogger(G_NAME_MODULE_SYS_AUDIT_LOG_SERVER, G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_WRITE)
        self._logClear = logger.createLogger(G_NAME_MODULE_SYS_AUDIT_LOG_SERVER, G_NAME_GROUP_SYS_AUDIT_LOG_SERVER_CLEAR)

        self._inputFilesGlobPatterns = []
        self._outputFd = None
        self._stateFileName = None

    def initInputFilesGlobPatterns (self, inputFilesGlobPatterns):
        self._inputFilesGlobPatterns = inputFilesGlobPatterns

    def initOutputFd (self, outputFd):
        self._outputFd = outputFd

    def initStateFile (self, state):
        self._stateFileName = state

    def viewLog (self):
        self._logGeneral("start").info("starting")

        files = self._calcInputFilesList()
        self._logGeneral("input-files-list").debug1("input files: %s", files)
        records = []
        for fileName in files:
            self._readInputFile(fileName, records)

        self._writeData(records)

        return True

    def viewLogRaw (self):
        self._logGeneral("start-raw").info("starting (raw mode)")

        files = self._calcInputFilesList()
        self._logGeneral("input-files-list").debug1("input files: %s", files)
        for fileName in files:
            try:
                fd = open(fileName)
                print fd.read()
                fd.close()
            except:
                self._logGeneral("failed-read-file").exception("failed read input file: %s", fileName)

        return True

    def clearLog (self):
        newStartTime = time.time()
        if self._stateFileName is None:
            self._logClear("no-file-set").error("failed to clear log file - no state file was set")
            return False

        if not os.path.exists(os.path.dirname(self._stateFileName)):
            try:
                os.makedirs(os.path.dirname(self._stateFileName))
            except:
                self._logClear("failed-create-state-dir").exception("failed to create state file directory")
                return False
        
        data = {}
        if os.path.exists(self._stateFileName):
            try:
                data = a.infra.format.json.readFromFile (self._logClear, self._stateFileName)
            except:
                self._logClear("failed-read-prev-state").exception("failed to read prev state file")
                return False

        if not isinstance(data,dict):
            self._logClear("failed-read-prev-state").error("prev state file is of invalid structure: %s", data)
            return False

        data[self._STATE_FILE_KEY_START_TIME] = newStartTime

        try:
            data = a.infra.format.json.writeToFile (self._logClear, data, self._stateFileName, indent=4)
        except:
            self._logClear("failed-write-state-file").exception("failed to write prev file")
            return False

        time.sleep(1)#sleep for one second to avoid delta T issues (none expected but Gaash wanted to stay on the safe side)
        self._logClear("cleared-log").notice("cleared user log")
        self._logClear("cleared-log-d").debug1("cleared user log - new start time is %d", newStartTime)

        a.infra.process.logUserMessage(a.api.user_log.msg.sys.ClearAuditLog())
        
        return True

    class _Record:
        def __init__ (self, logger, inputString):
            SEVERITY_POSSITION = 0
            TIME_STAMP_POSSITION = 1
            HOSTNAME_POSSITION = 2
            PROCESS_POSSITION = 3
            AUDIT_STRING_POSSITION = 4
            USER_MARK_STRING_POSSITION = 5
            UID_POSSITION = 6

            self.inputString = inputString

            messageAsList = self.inputString.split()

            origLocalTimeString = messageAsList[TIME_STAMP_POSSITION]

            origLocalTimeStringNoMilli = origLocalTimeString.split(".")[0]
            milliString = (origLocalTimeString.split(".")[1])
            localTime = time.strptime(origLocalTimeStringNoMilli, "%d-%b-%Y::%H:%M:%S")

            newLocalTimeString =  time.strftime("%b %e %H:%M:%S", localTime)+".%s"%milliString
            messageAsList[TIME_STAMP_POSSITION] = newLocalTimeString
            logger("time-change").debug5("time string %s was changed to %s (local time: %s)", origLocalTimeString, newLocalTimeString, localTime)

            self.time = time.mktime(localTime)+(int (milliString))/1000
            logger("time-stamp").debug5("record time stamp: %s, current time: %s", self.time, time.time())

            origUserMarkString = messageAsList[USER_MARK_STRING_POSSITION]
            newUserMarkString = None
            messageAsList[USER_MARK_STRING_POSSITION] = newUserMarkString
            logger("uid-mark-change").debug5("user mark string '%s' was changed to '%s'", origUserMarkString, newUserMarkString)

            origUid = messageAsList[UID_POSSITION]
            newUid = origUid.split("/")[0]+":"
            messageAsList[UID_POSSITION] = newUid
            logger("uid-change").debug5("user string '%s' was changed to '%s'", origUid, newUid)

            origSeverity = messageAsList[SEVERITY_POSSITION]
            newSeverity = None
            messageAsList[SEVERITY_POSSITION] = newSeverity
            logger("severity-change").debug5("severity '%s' was changed to '%s'", origSeverity, newSeverity)

            origHostname = messageAsList[HOSTNAME_POSSITION]
            newHostname = None
            messageAsList[HOSTNAME_POSSITION] = newHostname
            logger("hostname-change").debug5("hostname '%s' was changed to '%s'", origHostname, newSeverity)

            origAudit = messageAsList[AUDIT_STRING_POSSITION]
            newAudit = None
            messageAsList[AUDIT_STRING_POSSITION] = newAudit
            logger("audit-change").debug5("audit mark '%s' was changed to '%s'", origAudit, newAudit)

            origProcess = messageAsList[PROCESS_POSSITION]
            newProcess = None
            messageAsList[PROCESS_POSSITION] = newProcess
            logger("audit-change").debug5("audit mark '%s' was changed to '%s'", newProcess, origProcess)

            
            cleanList = [token for token in messageAsList if token != None]

            self.outputString = " ".join(cleanList)
            logger("string-change").debug5("message '%s' was changed to '%s'", self.inputString, self.outputString)

            

    def _calcStartTime (self):
        startTime = 0
        if not self._stateFileName is None:
            try:
                if os.path.exists(self._stateFileName):
                    stateFileData = a.infra.format.json.readFromFile (self._logRead, self._stateFileName)
                    if self._STATE_FILE_KEY_START_TIME in stateFileData:
                        startTime = stateFileData[self._STATE_FILE_KEY_START_TIME]
                        self._logRead("read-start-time").debug1("read start time to be %d", startTime)
                    else:
                        self._logRead("no-start-time-flag").debug2("no start time flag in file %s", self._stateFileName)
                else:
                    self._logRead("no-state-file").debug2("no state file %s", self._stateFileName)
            except:
                self._logRead("failed-reading-state-file").warning("failed to read state file for logging start time", exc_info=1)
        else:
            self._logRead("no-state-file-set").debug2("no state file set")

        return startTime

    def _calcInputFilesList (self):
        files = []
        for pattern in self._inputFilesGlobPatterns:
            files += glob.glob(pattern)

        files.sort(key = lambda x: os.path.basename(x))

        return files

    def _readInputFile(self, fileName, targetList):       
        try:                
            self._logRead("read-next-file").debug2("reading next file: %s.", fileName)
            fd = open(fileName)
            data = fd.readlines()
            fd.close()
        except:
            self._logRead("read-file-failed").exception("failed to read file: %s", fileName)
            return

        for line in data:
            try:                
                #removed due to performance issues self._logRead("parse-next-line").debug5("parsing next line from file %s: ", fileName, line)
                if not self._basicFilter(line):
                    #removed due to performance issues self._logRead("line-filtered").debug5("line was filtered out: %s", fileName, line)
                    continue
                record = self._Record(self._logRead, line)
                targetList.append(record)
            except Exception as exception:
                self._logRead("read-chain-failed").exception("failed to read msg: %s", str(exception))
                #not returning - gathering what we can


    def _basicFilter (self, line):
        filterOutStrings = ["user: system", "CLI done"]        
        for stringToFind in filterOutStrings:
            if stringToFind in line:
                #removed due to performance issues self._logRead("filter-out-str").debug5("filter out line '%s' due to string '%s'", line, stringToFind)
                return False

        includeStrings = ["CLI", "Failed to login", "logged in", "Logged out"]
        for stringToFind in includeStrings:
            if stringToFind in line:
                self._logRead("filter-in-str").debug5("include line '%s' due to string '%s'", line, stringToFind)
                return True

        self._logRead("filter-out-default").debug5("filter out line '%s'")
        return False

    def _writeData(self, records):
        startTime = self._calcStartTime()
        for record in records:
            if record.time < startTime:
                self._logWrite("time-skip").debug5("skipping record '%s' as timestamp %d is before %d", record.inputString, record.time, startTime)
            else:
                self._outputFd.write("%s\n"%record.outputString)




