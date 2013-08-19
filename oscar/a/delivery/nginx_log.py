#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import os
import sys

import utils
from a.infra.file.rotating_file_size_enforcer import RotatingFileSizeEnforcer

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_NGINX_LOG = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_NGINX_LOG

#-----------------------------------------------------------------
class NginxLog (object):


    #---------------------------------------------------------------------------------------------------------
    def __init__ (self, logger):
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_NGINX_LOG)           

    #---------------------------------------------------------------------------------------------------------
    # After calling to init need to Reopen Nginx Log Files
    def init (self, conf):

        logsDirectoryPath     = conf.ngxLogDir
        logsDirectorySizeByte = conf.nginxDirectoryLogSizeByte
        errLogPath            = conf.ngxLogFileSymLink
        errLogSizeByte        = conf.nginxLogFileSizeByte

        self.__rotator = RotatingFileSizeEnforcer(self.__log,logsDirectoryPath,"log-",".txt")  
              
        self.__rotator.initSymlink(os.path.dirname(errLogPath),os.path.basename(errLogPath))


        self.__log("log-rotator").info("Log Symbolic Link %s",errLogPath);

        self.__errLogSizeByte = errLogSizeByte 

        try:       
            # old files might be deleted to obey directory size
            self.__rotator.setTotalSize(logsDirectorySizeByte)            

            # The sym Link is created old files might be deleted to obey directory size
            # the SymLink is linking between the errLogFile and Logs Directory
            self.__rotator.prepare()

            self.__log("log-rotator").info("Init Nginx Log, Directory Size = %d File Size = %d",logsDirectorySizeByte,errLogSizeByte)
  
        except Exception, e: 
            self.__log("log-rotator-err").exception("Failed to init Nginx Log Rotator - %s, %s",utils.parseErrnoToString(e), sys.exc_info()[1])
            return False            

        return True


    #---------------------------------------------------------------------------------------------------------
    # Check if ErrLogFile is reached it max size and need rotation    
    # Return True in case the File Rotated
    def tick (self):

        # == 0
        if not self.__errLogSizeByte:
            return False

        try:       
            curSizeByte = self.__rotator.getCurrentFileSize()

            if curSizeByte >= self.__errLogSizeByte:
                self.__rotator.rotate()
                self.__log("log-end").debug1("Rotate Nginx Error Log - File Size = %d > %d", curSizeByte, self.__errLogSizeByte)
                return True
            
            self.__log("log-end").debug3("No Rotate of Nginx Error Log - File Size = %d < %d", curSizeByte, self.__errLogSizeByte)

  
        except Exception, e: 
            self.__log("log-tick").error("Failed to tick Nginx Log Rotator - %s",utils.parseErrnoToString(e))
            return False

        return False

    #---------------------------------------------------------------------------------------------------------
    def end (self):


        try:
            curSizeByte = self.__rotator.getCurrentFileSize()
             
            if curSizeByte :
                self.__rotator.rotate()
                self.__log("log-end").info("Rotate Nginx Log in Exit - File Size = %d",curSizeByte)

        except Exception, e: 
            self.__log("log-end-err").error("Failed to rotate Nginx Log in Exit - %s",utils.parseErrnoToString(e))
            return False

        return True


