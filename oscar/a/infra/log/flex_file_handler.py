#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 
import os
import sys
import time
import datetime
import logging.handlers
import a.infra.file.rotating_file_size_enforcer
import a.infra.file.flex_output_file
import a.infra.lock.multi_process
   
   
class FlexFileHandler(logging.Handler):
    """
    A handler class which writes logging records, appropriately formatted,
    to a stream. Note that this class does not close the stream, as
    sys.stdout or sys.stderr may be used.
    """

    def __init__(self, loggerToUse, fileDir, fileBaseNamePrefix, fileBaseNameSuffix, usePhases = False,
                 logFileSize = 0, isBinary = False, isMultiProcess = False, maxMultiProcessLockRetryTimeout = 0):        
        """
        Open the specified file and use it as the stream for logging.
        """

        logging.Handler.__init__(self)
        self._flexFile = a.infra.file.flex_output_file.FlexOutputFile(logger = loggerToUse,
                                                                      fileDir=fileDir, 
                                                                      fileBaseNamePrefix = fileBaseNamePrefix,
                                                                      fileBaseNameSuffix = fileBaseNameSuffix,
                                                                      includeExtraExtensions = True)
        self._flexFile.initFileBaseNamePatternToDefault(usePhases)
        self._isMultiProcess = isMultiProcess
        self._maxMultiProcessLockRetryTimeout = maxMultiProcessLockRetryTimeout
        if self._isMultiProcess:
            self._flexFile.initMultiProcessControl(os.path.join(fileDir, "log.control.json"))

        self._isFdOpened = False
        self._openFileIfNeeded()

        self._isBinary = isBinary

        self.setLogFileSize(logFileSize)                


    def setLogFileSize (self, logFileSize):
        self._maxLogFileSize = logFileSize
        if not self._openFileIfNeeded():
            return
        if self._beginMultiProcessFileOperationsIfNeeded(updateSize=True):
            try:
                if self._shouldRollover(additionalSize=0):
                    self._doRollover()
            finally:
                self._endMultiProcessFileOperationsIfNeeded()

    def setTotalSize(self, logTotalSize):  
        if not self._openFileIfNeeded():
            return
        if self._beginMultiProcessFileOperationsIfNeeded(updateSize=True):
            try:
                self._flexFile.setTotalSize(totalSize = logTotalSize)                
            finally:
                self._endMultiProcessFileOperationsIfNeeded()

    def _doRollover(self):
        self._flexFile.reopenNextFile(dontReopenSameFile = True)
        self._currentFileSize = 0

    def _shouldRollover(self, additionalSize):
        if self._maxLogFileSize == 0:
            return False
        if (self._currentFileSize+additionalSize) > self._maxLogFileSize:
            return True
        return False

    def emit(self, record):
        try:
            msg = self.format(record)
            fs = "%s"
            if not self._isBinary:
                fs += "\n"
            data = fs % msg
            additionalSize = len(data)
            if not self._openFileIfNeeded():
                print >> sys.stderr, "Thrown log message (couldn't open file):", str(record.__dict__)
                return
            if self._beginMultiProcessFileOperationsIfNeeded(updateSize=True):
                try:                    
                    if self._shouldRollover(additionalSize=additionalSize):
                        self._doRollover()
                    self._flexFile.write(data)
                    self._flexFile.flush()
                    self._currentFileSize += additionalSize
                except:                    
                    print >> sys.stderr, "Thrown log message:", str(record.__dict__)                           
                finally:
                    self._endMultiProcessFileOperationsIfNeeded()
            else:
                print >> sys.stderr, "Thrown log message (file is locked):", str(record.__dict__)                           

        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def close(self):
        """
        Closes the stream.
        """
        if not self._isMultiProcess:
            self._flexFile.flush()
            self._flexFile.close()
        self._isFdOpened = False
        logging.Handler.close(self)

            
    def _openFileIfNeeded (self):
        if self._isFdOpened:
            return True

        if not self._beginMultiProcessFileOperationsIfNeeded(updateSize=False):
            return False
        try:
            self._flexFile.open(mode="a") #avoiding a situation is which short executable is called again and again and overrun its file
                                          #taking care of multi process logging
                            
            self._currentFileSize = self._flexFile.getFileSize()
            self._isFdOpened = True
        except:#cannot be due to lock issue as the lock is alreay taken
            a.infra.process.processFatal("Failed to open logger output file")            
        finally:
            self._endMultiProcessFileOperationsIfNeeded()

        return True

            

    def _beginMultiProcessFileOperationsIfNeeded (self, updateSize):
        if not self._isMultiProcess:
            return True
        roundNumber = 0
        startTime = datetime.datetime.now()#not using monotonic clock as it brings ctype
        wasTaken = False
        while datetime.datetime.now()-startTime < datetime.timedelta(seconds=self._maxMultiProcessLockRetryTimeout) :
            try:
                self._flexFile.beginMultiProcessFileOperations()
                wasTaken = True
                break
            except a.infra.lock.multi_process.LockError:
                pass

            sleepTime = 0.01
            if roundNumber>=10:
                sleepTime = 0.1
            time.sleep(sleepTime)
            roundNumber += 1

        if wasTaken and updateSize:
            self._currentFileSize = self._flexFile.getFileSize()

        return wasTaken

    def _endMultiProcessFileOperationsIfNeeded (self):
        if not self._isMultiProcess:
            return True
        self._flexFile.endMultiProcessFileOperations()

