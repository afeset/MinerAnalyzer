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
# This is a communication module that allows passing stats counters over a file
#                                                                                                                      #
########################################################################################################################
import os.path
from a.infra.format.json.comm_over_file import CommOverFile
from a.infra.process import processFatal 

DEF_STATS_FILE_EXPIRATION_PERIOD = 120

class StatsCommOverFile:

    def __init__(self, processName, logger):
        self._processName = processName
        self._commObj = CommOverFile(self._processName + "-stats-comm-chan", logger)

    def init (self, directoryGlob, expirationPeriod = DEF_STATS_FILE_EXPIRATION_PERIOD):
        self._expirationPeriod = expirationPeriod

        dirname = directoryGlob.replace('*', self._processName)
        filename = os.path.join(dirname, "status/counters.json")
        self._commObj.init(filename)

    def receive (self):
        return self._commObj.receive(self._expirationPeriod)

    def getData (self):
        return self._commObj.getData()

    def getTime (self):
        return self._commObj.getTime()

