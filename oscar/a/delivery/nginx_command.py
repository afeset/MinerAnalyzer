#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: hagaia
# 

import os

import utils

if  __package__ is None:
    G_NAME_MODULE_DELIVERY = "unknown"
    G_NAME_GROUP_DELIVERY_NGINX_COMMAND = "unknown"
else:
    from . import G_NAME_MODULE_DELIVERY 
    from . import G_NAME_GROUP_DELIVERY_NGINX_COMMAND

#-----------------------------------------------------------------
class NginxCommand(object):
     
    #-----------------------------------------------------------------------------------------------
    def __init__ (self, name, logger):
        self.__name = name
        self.__log = logger.createLogger(G_NAME_MODULE_DELIVERY, G_NAME_GROUP_DELIVERY_NGINX_COMMAND)

    #-----------------------------------------------------------------
    def init (self,deliveryConf):

        self.__conf = deliveryConf
        self.__ngxAppName  = os.path.join(self.__conf.ngxBinDir, self.__conf.kConf.kNginxExeName) 
        self.__ngxConfFile = self.__conf.ngxConfFile
        self.__baseCmd = self.__ngxAppName + " -c " + self.__ngxConfFile + " -p " + self.__conf.ngxVolatilePrefixDir
        self.__baseCmd = os.path.join(self.__baseCmd,"")
  
    #-----------------------------------------------------------------------------------------------
    def execute(self):
        """
            Execute Nginx
        """

        cmd = self.__baseCmd

        ## Run nginx with memory limit in case such size configured
        ## To do so it use open with shell=true (multiple commands...)
        if self.__conf.nginxWorkerMaxMemorySizeMbyte != 0:

            maxMemorySize = (self.__conf.nginxWorkerMaxMemorySizeMbyte * 1024)

            cmd = "ulimit -Sv " + str(maxMemorySize) + "; " + cmd
        
            return self.__runCommand("Execute Nginx", cmd, useShell=True)

        else:
            return self.__runCommand("Execute Nginx", cmd, useShell=False)

    #-----------------------------------------------------------------------------------------------    
    def stop(self):
        """
            Quick Shutdwon Nginx (not gracefully)
        """

        cmd = self.__baseCmd + " -s stop"
        
        self.__runCommand("Stop Nginx", cmd,self.__conf.kConf.kMaxWaitTimeForChildProcessMsec)


    #-----------------------------------------------------------------------------------------------    
    def quit(self):
        """
            Graceful Shutdown
        """

        cmd = self.__baseCmd + " -s quit"
        
        return self.__runCommand("Quit Nginx", cmd)

      
    #-----------------------------------------------------------------------------------------------          
    def reConfigure(self):
        """
            Configuration reload
            Start the new worker processes with a new configuration
            Gracefully shutdown the old worker processes 
        """

        cmd = self.__baseCmd + " -s reload"
        
        return self.__runCommand("Re-Configure Nginx", cmd)

    #-----------------------------------------------------------------------------------------------
    def reOpenLogs(self):
        """            
            Reopen Nginx Log Files 
        """

        cmd = self.__baseCmd + " -s reopen"
        
        return self.__runCommand("Reopen Nginx Logs", cmd,self.__conf.kConf.kMaxWaitTimeForChildProcessMsec)


    #private
    #-----------------------------------------------------------------------------------------------
    def __runCommand (self, strCommand, command , maxTimeMsec = 0, useShell = False):

        (rc,exception,sp) = utils.runPopen(command, close_fds = True, maxTimeMsec = maxTimeMsec, shell=useShell)

        if rc:
            self.__log("run-cmd").info("%s - %s", strCommand, command)
        else:
            self.__log("run-cmd-err").error("Failed to Execute Nginx Command - %s - %s - %s", strCommand, command, utils.parseErrnoToString(exception))

        return rc
        
        
        

