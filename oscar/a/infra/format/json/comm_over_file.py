# 
# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# ver 1.0 
#
# Author: Adan Alper
#
########################################################################################################################
#                                                                                                                      #
# This is a communication module that allows passing of dictionaries between processes over a file
#                                                                                                                      #
########################################################################################################################
import time
if  __package__ is None:
    def readFromFile (logger, fileName):
        pass

    def writeToFile (logger, data, fileName, tempFileName = None, mkdir=False, indent=None):
        pass
else:
    from . import readFromFile
    from . import writeToFile


class CommOverFile(object):
    def __init__(self, commChanName, logger):
        self._commChanName = commChanName
        self._logger = logger.createLoggerSameProperties()
        self._logger.setInstance(self._commChanName)

    def init (self, fileName):
        self._fileName = fileName

        self._info = {}
        self._info["timestamp"] = time.time()
        self._info["data"] = None

        self._logger("initializing-channel").info("Initializing process communication over file %s", self._fileName)

    def send (self, data):
        self._info["timestamp"] = time.time()
        self._info["data"] = data
        
        self._logger("send").debug3("Sending data at time %s", str(self._info["timestamp"]))

        try:
            writeToFile(self._logger, self._info, self._fileName)
        except EnvironmentError:
            self._logger("send-error").error("Error sending data at time %s to File - %s", str(self._info["timestamp"]),self._fileName)

    def receive (self, expirationPeriod):
        try:
            self._logger("read-file").info("Reading data from file %s" % self._fileName)
            self._info = readFromFile(self._logger, self._fileName)
        except EnvironmentError as e:
            self._logger("read-file-fail").info("Failed reading data from file %s, Error string - %s", self._fileName, e.strerror)
            self._info = None
            return

        if self._info == None:
            self._logger("receive-no-data").warning("Error receiving data - No data found")
        else:
            now = time.time()
            msgTime = self._info["timestamp"]
            if ("data" not in self._info) or ("timestamp" not in self._info):
                self._logger("receive-error").error("Error receiving data - Malformed message received")
                self._info = None
            elif ((now - msgTime) > expirationPeriod):
                self._logger("receive-stale-data").warning("Error receiving data - Stale message received. Current time: %d, Message time: %d, Delta: %d sec. Expiration period: %d sec. Name %s",
                                                            now, msgTime, now - msgTime, expirationPeriod, self._commChanName)
                self._info = None
            else:
                self._logger("receive").debug3("Message received. Message time = %s", self._info["timestamp"])
                

    def getData (self):
        if self._info:
            return self._info["data"]

    def getTime (self):
        if self._info:
            return self._info["timestamp"]

