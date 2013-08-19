#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika, nirs
# 

import a.infra.format.json

import datetime
import os

if  __package__ is None:
    G_NAME_GROUP_MARKER_FILE = "unknown"
else:
    from . import G_NAME_GROUP_MARKER_FILE

class MarkerFile:

    def __init__ (self, logger, fileName, formatVersion = 100, instance=None):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_MARKER_FILE, instance=instance)
        self._fileName = fileName
        self._formatVersion = formatVersion        

    def isMarked (self):
        return os.path.exists(self._fileName)

    def getData (self):
        """
        get the data kept in the file. 
        will throw an exception if file does not exists or in case of any other failure
        """
        return a.infra.format.json.readFromFile(self._log, self._fileName)
        

    def mark (self, creatorString):
        """
        return True in case of success
        """
        data = self._createData(creatorString)
        try:
            a.infra.format.json.writeToFile(self._log, data, self._fileName, indent=4)
        except:
            self._log("failed-write-file").error("Failed to write validity marker file '%s'", self._fileName)
            return False

        self._log("marked").debug1("Validity file '%s' was created with data: %s", self._fileName, data)
        return True


    def unMark (self):
        if os.path.exists(self._fileName):
            os.remove(self._fileName)

    def _createData (self, creatorString):
        dateTime = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
        data = {"creator"           : creatorString,
                "creation-date-utc" : dateTime,          
                "format-version"    : self._formatVersion}
        return data

    
class ValidityMarker(MarkerFile):
    def __init__ (self, logger, fileName, formatVersion = 100, instance=None):
        MarkerFile.__init__(self, logger, fileName, formatVersion, instance)

    def isValid (self):
        return self.isMarked()

    def markValid (self, creatorString):
        return self.mark(creatorString)

    def markInvalid (self):
        return self.unMark()



