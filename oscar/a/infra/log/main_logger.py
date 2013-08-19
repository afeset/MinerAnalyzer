# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

import generic_instance
import logging

class MainLogger(generic_instance.GenericInstance):
    LOGGER_NAME = "main-logger"

    def __init__ (self, earlyLogLevel = logging.NOTICE, defaultLogLevel = logging.NOTICE, processName = "None"):
        generic_instance.GenericInstance.__init__(self, self.LOGGER_NAME, earlyLogLevel, defaultLogLevel, 
                                                  processName, True)

    @classmethod
    def s_getFromOsefUnsafe (cls, osef):
        return generic_instance.GenericInstance._s_getFromOsefUnsafe(osef, cls.LOGGER_NAME)        

    @classmethod
    def s_getFromOsefOrCrash (cls, osef):
        return generic_instance.GenericInstance._s_getFromOsefOrCrash(osef, cls.LOGGER_NAME)        

    @classmethod
    def s_createInitParamFile (cls, dbgLog, initParamFilesDirName, dictionary):
        generic_instance.GenericInstance._s_createInitParamFile(dbgLog, initParamFilesDirName, cls.LOGGER_NAME, dictionary)        



