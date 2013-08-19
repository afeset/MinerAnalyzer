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
# This is a communication module that allows a client to pass stats counters to the stats process over a file
#                                                                                                                      #
########################################################################################################################
import os.path
from a.infra.format.json.comm_over_file import CommOverFile
from a.infra.process import processFatal 

class StatsCommOverFileClient():
    def __init__(self, commChanName, logger):
        self._logger = logger.createLoggerSameProperties()
        self._logger.setInstance(commChanName + '-stats-client')
        self._commObj = CommOverFile(commChanName, self._logger)

    def init (self, baseDir):
        dirname = os.path.join(baseDir, "status")

        # create the directory if it doesnt exist
        try:
            if not os.path.exists(dirname):
                os.mkdir(dirname)
        except OSError as e:
            self._logger("mkdir-error").error("Error creating directory %s. Error string - %s", e.filename, e.strerror)
            processFatal("Error creating directory %s", e.filename)

        filename = os.path.join(dirname, "counters.json")
        # expiration period is not relevant for the client
        self._commObj.init(filename)

    def send (self, data):
        self._commObj.send(data)

    def getData (self):
        return self._commObj.getData()

    def getTime (self):
        return self._commObj.getTime()

