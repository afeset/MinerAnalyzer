
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: royr
#
# This holds rotating file class

import os, json

if  __package__ is None:
    G_NAME_MODULE_ROTATING_FILE = "unknown"
    G_NAME_GROUP_ROTATING_FILE_GENERAL = "unknown"
else:
    from . import G_NAME_MODULE_ROTATING_FILE
    from . import G_NAME_GROUP_ROTATING_FILE_GENERAL

# constants
TEMP_SUFFIX = ".tmp"

# rotatingCriteria enum
NO_ROTATE = "NO_ROTATE"


class RotatingFile:
    _file = None
    _fileNum = 0
    _fileNamePrefix = ""
    _fileNameExtension = ""
    _currentTmpFileNamePath = None
    _openType = None
    _folderName = ""
    _rotatingCriteria = None
    _criteriaArg = None
    _isOpen = False


    def __init__ (self, logger, folderName, filePrefix, rotatingCriteria, criteriaArg, fileExtension = "", openType = "w"):
        self._logGeneral=logger.createLogger(G_NAME_MODULE_ROTATING_FILE, G_NAME_GROUP_ROTATING_FILE_GENERAL)
        self._folderName = folderName
        self._fileNamePrefix = filePrefix
        self._rotatingCriteria = rotatingCriteria
        self._criteriaArg = criteriaArg
        self._openType = openType
        self._fileNameExtension = fileExtension


    def open (self):
        if self._isOpen:
            self._logGeneral("file-already-open").notice("Can't open file - it's already opened")
        else:
            # If we closed and reopened the same instance we want to increment the file index
            # so we won't run over the last file that was closed
            if self._fileNum > 0:
                self._incrementFileIndex()

            self._currentTmpFileNamePath = self._getTmpFileNamePath()
            try:
                self._file = open(self._currentTmpFileNamePath, self._openType)
                self._isOpen = True
            except Exception as ex:
                self._logGeneral("cant-open-file").error("Can't open file %s with mode '%s'. exception=%s" % (self._currentTmpFileNamePath, self._openType, ex))
                return False

        return True


    def write (self, data):
        if isinstance(data, str):
            self._file.write(data)
            return True
        else:
            self._logGeneral("argument-not-string").error("Given argument to write to file is not str")
            return False


    def writeJsonFormat (self, data):
        try:
            json.dump(data, self._file)
            return True
        except Exception as ex:
            self._logGeneral("dumping-json").error("got exception trying to dump json data to file. exception=%s", ex)
            return False


    def rotateNow (self):
        if not self._isOpen:
            self._logGeneral("cant-rotate-file-not-open").notice("Can't rotate file - it's not open")
            return False
        else:
            try:
                # Close old file and rename it
                self._file.close()
            except Exception as ex:
                self._logGeneral("rotate-now-error").error("got exception while trying to close file. exception:%s", ex)
                return False

            # Atomic rename the file
            if not self._renameFromTmpToFinal(self._currentTmpFileNamePath):
                return False

            # Rotate and open new file
            self._incrementFileIndex()
            self._currentTmpFileNamePath = self._getTmpFileNamePath()

            self._file = self._openFileForWrite(self._currentTmpFileNamePath, self._openType)
            if self._file == None:
                return False
            else:
                self._isOpen = True
            
        return True


    def close (self):
        if not self._isOpen:
            self._logGeneral("cant-close-file-not-open").notice("Can't close file - it's not open")
            return False
        else:
            self._file.close()
            self._renameFromTmpToFinal(self._currentTmpFileNamePath)
            self._isOpen = False

        return True

    def _incrementFileIndex (self):
        self._fileNum += 1

    def _renameFromTmpToFinal (self, tmpFileName):
        finalFileNamePath = tmpFileName[:tmpFileName.rfind(".")]
        try:
            os.rename(tmpFileName, finalFileNamePath)
        except:
            self._logGeneral("failed-rename-file").error("Failed renaming file '%s' to file '%s'" , tmpFileName, finalFileNamePath)
            return False

        return True



    def _getTmpFileNamePath (self):
        tmpFileName = self._fileNamePrefix + ("%09u" % self._fileNum) + self._fileNameExtension + TEMP_SUFFIX
        return os.path.join(str(self._folderName), tmpFileName)


    def _openFileForWrite (self, filename, openMode="w"):
        try:
            fileDescriptor= open(filename,openMode)
            return fileDescriptor
        except Exception as ex:
            self._logGeneral("failed-open-file-for-read").error("failed to open %s for read- %s ", filename ,ex)
            return None   



            
            
