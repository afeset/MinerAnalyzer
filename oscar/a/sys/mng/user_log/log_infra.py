# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

import a.infra.log.generic_instance
import logging

class LogInfra(a.infra.log.generic_instance.GenericInstance):
    LOGGER_NAME = "user-log-infra-logger"

    def __init__ (self, processName = "None"):
        a.infra.log.generic_instance.GenericInstance.__init__(self, self.LOGGER_NAME, logging.NOTICE, logging.NOTICE, 
                                                              processName, False)

    def captainClient_setProcessName (self):
        self.setProcessName(self._captain.getProcessName())

    @classmethod
    def s_getFromOsefUnsafe (cls, osef):
        return a.infra.log.generic_instance.GenericInstance._s_getFromOsefUnsafe(osef, cls.LOGGER_NAME)        

    @classmethod
    def s_getFromOsefOrCrash (cls, osef):
        return a.infra.log.generic_instance.GenericInstance._s_getFromOsefOrCrash(osef, cls.LOGGER_NAME)        

    @classmethod
    def s_createInitParamFile (cls, dbgLog, initParamFilesDirName, dictionary):
        a.infra.log.generic_instance.GenericInstance._s_createInitParamFile(dbgLog, initParamFilesDirName, cls.LOGGER_NAME, dictionary)        



