#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import os
import time
import re
import a.infra.string.utils

if  __package__ is None:
    G_NAME_MODULE_SYS_BASH_LOG_SERVER = "unknown"
    G_NAME_GROUP_SYS_BASH_LOG_SERVER_GENERAL = "unknown"    
    G_NAME_GROUP_SYS_BASH_LOG_SERVER_READ = "unknown"    
    G_NAME_GROUP_SYS_BASH_LOG_SERVER_WRTIE = "unknown"   
else:
    from . import G_NAME_MODULE_SYS_BASH_LOG_SERVER
    from . import G_NAME_GROUP_SYS_BASH_LOG_SERVER_GENERAL
    from . import G_NAME_GROUP_SYS_BASH_LOG_SERVER_READ
    from . import G_NAME_GROUP_SYS_BASH_LOG_SERVER_WRITE
    
class Server(object):

    INPUT_GENERATION_COMMAND_START_TIME_PLACE_HOLDER = "%start-time"

    _STATE_FILE_KEY_START_TIME = "start-time"

    def __init__(self, logger):
        self._logGeneral = logger.createLogger(G_NAME_MODULE_SYS_BASH_LOG_SERVER, G_NAME_GROUP_SYS_BASH_LOG_SERVER_GENERAL)
        self._logRead = logger.createLogger(G_NAME_MODULE_SYS_BASH_LOG_SERVER, G_NAME_GROUP_SYS_BASH_LOG_SERVER_READ)
        self._logWrite = logger.createLogger(G_NAME_MODULE_SYS_BASH_LOG_SERVER, G_NAME_GROUP_SYS_BASH_LOG_SERVER_WRITE)

        self._inputFilesDir = []
        self._outputFd = None

    def initInputFilesDir (self, inputFilesDir):
        self._inputFilesDir = inputFilesDir

    def initOutputFd (self, outputFd):
        self._outputFd = outputFd

    def viewLog (self):
        self._logGeneral("start").info("starting")

        records = {}
        for fileName in os.listdir(self._inputFilesDir):
            try:
                user = fileName.split(".")[0]
            except:
                self._logRead("no-user").exception("cannot get user name from file name %s", fileName)
                user = "unknown"
            fileFullName = os.path.join(self._inputFilesDir, fileName)
            records[fileFullName] = self._getRecordsFromFile(fileFullName, user)

        self._writeData(records)

        return True


    class _Record:
        def __init__ (self, time, user, text):
            self.time = time
            self.user = user
            self.text = text


    def _getRecordsFromFile(self, fileFullName, user):       
        try:                
            self._logRead("read-next-file").debug2("reading next file: %s.", fileFullName)
            fd = open(fileFullName)
            data = fd.readlines()
            fd.close()
        except:
            self._logRead("read-file-failed").exception("failed to read file: %s", fileFullName)
            return

        records = []
        readTime = None
        for line in data:  
            line = line.strip()
            if readTime is not None:
                records.append(self._Record(readTime, user, line))
                readTime = None
                continue

            match = re.match("^#(\d[\d]*)$",line)
            if match:
                readTime = int(match.group(1))
            else:
                records.append(self._Record(None, user, line))

        return records


    def _writeData(self, recordsPerFile):
        record = self._getNextRecord(recordsPerFile)
        while record is not None:
            if record.time:
                timeStr = time.strftime("%b %e %H:%M:%S.000", time.localtime(record.time))
            else:
                timeStr = "                   "
            try:
                print "%s: %s: %s"%(timeStr, record.user, record.text)
            except:
                print "%s: %s: %s"%(timeStr, record.user, a.infra.string.utils.Utils.s_turnToPrintable(record.text))

            record = self._getNextRecord(recordsPerFile)


    def _getNextRecord(self, recordsPerFile):
        minTime = None
        minTimeFile = None
        for fileName in sorted(recordsPerFile):
            recordsList = recordsPerFile[fileName]
            
            if not recordsList:
                self._logWrite("no-more-data-for-file").debug5("no more data for file %s", fileName)
                #empty list
                continue
            
            newVal = recordsList[0].time
            self._logWrite("data").debug5("file: %s, value: %s", fileName, newVal)
            if minTimeFile is None:
                #first none empty list
                self._logWrite("first").debug3("first data: file: %s, value: %s", fileName, newVal)
                minTimeFile = fileName
                minTime = newVal
                continue
            
            if minTime is None:          
                #we already reached min possible value (no time found)
                self._logWrite("min-is-none").debug4("continue as min found value is None")
                continue
            
            if (newVal is None) or (newVal < minTime):
                #found new min
                self._logWrite("new-min").debug3("new min from file %s: %s", fileName, newVal)
                minTimeFile = fileName
                minTime = newVal

        if minTimeFile is None:
            self._logWrite("no-more-data").debug1("no more data")
            return None

        self._logWrite("found-min").debug2("final min value is %s (from file %s)", minTime, minTimeFile)
        return recordsPerFile[minTimeFile].pop(0)
            
