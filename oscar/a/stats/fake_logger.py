#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# ver 1.0 
#
# Author: galm
#
########################################################################################################################
#                                                                                                                      #
# Fake logger that only wrapes python's default logger
#                                                                                                                      #
########################################################################################################################

import logging
import os

LOG_FILE_EXTENTION = ".log"

loggingNameToLoggingType = {
    'debug':logging.DEBUG,
    'info':logging.INFO,
    'warning':logging.WARNING,
    'error':logging.ERROR,
    'critical':logging.CRITICAL
}

class FakeLogger(object):
    def __init__ (self, outputPath, loggerName, loggingLevel):
        self.myOutputDir = outputPath
        self.myLogger = logging.getLogger(loggerName)
        logFile = os.path.join(outputPath, loggerName+LOG_FILE_EXTENTION)
        self.hdlr = logging.FileHandler(logFile)
        self.hdlr.setLevel(loggingNameToLoggingType[loggingLevel])
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.hdlr.setFormatter(formatter)

        self.myLogger.addHandler(self.hdlr) 
        self.myLogger.setLevel(loggingNameToLoggingType[loggingLevel])
    
    def closeLog (self):
        self.myLogger.info("Closing log hanler")
        self.myLogger.removeHandler(self.hdlr)
        self.hdlr.close()
    def error (self, strLog):
        self.myLogger.error(strLog)
    def fatal (self, strLog):
        self.myLogger.critical(strLog)
    def info (self, strLog):
        self.myLogger.info(strLog)
    def warning (self, strLog):
        self.myLogger.warning(strLog)
    def notice (self, strLog):
        self.myLogger.debug(strLog)
    def debug1 (self, strLog):
        self.myLogger.debug(strLog)
    def debug2 (self, strLog):
        self.myLogger.debug(strLog)
    def debug3 (self, strLog):
        self.myLogger.debug(strLog)
    def debug4 (self, strLog):
        self.myLogger.debug(strLog)
    def debug5 (self, strLog):
        self.myLogger.debug(strLog)

    
