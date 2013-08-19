# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

import os     
import sys
import logging

import a.infra.format.json
import a.sys.mng.bash_log.server
import a.sys.std_process.micro_captain
import a.sys.mng.user_log.server
import a.sys.mng.user_log.service
import a.sys.mng.user_log.log_infra


G_NAME_MODULE_APP_BASH_LOG_SERVER = "app-bash-log-server"
G_NAME_GROUP_APP_BASH_LOG_SERVER_DEFAULT = "default"

class BashLogServerApp(a.sys.std_process.micro_captain.MicroAppInterface):
    INIT_PARAM_FILES_DIR_ENV_VAR_NAME = "QB_BASH_LOG_SERVER_INIT_PARAM_FILES_DIR"
    #init params handling
    INIT_PARAM_FILE_NAME = "bash-log-server-init-params.json"
    #kept fields
    INIT_PARAM_INPUT_FILES_DIR   = "input-files-dir"

    def __init__ (self):
        pass

    def initLogger(self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_APP_BASH_LOG_SERVER, G_NAME_GROUP_APP_BASH_LOG_SERVER_DEFAULT)

    def createCaptainClients (self):
        pass

    def initFromParamFile(self, initParamFilesDirName):
        data = a.infra.format.json.readFromFile(self._log, 
                                                os.path.join(initParamFilesDirName, self.INIT_PARAM_FILE_NAME))
        self.initFromDictionary(data)

    def initFromDictionary(self, data):
        self.init(data[self.INIT_PARAM_INPUT_FILES_DIR])

    def init (self, inputFilesDir):
        self._bashLogServer = a.sys.mng.bash_log.server.Server(self._log)
        self._bashLogServer.initInputFilesDir(inputFilesDir)
        self._bashLogServer.initOutputFd(sys.stdout)
        
    def run (self):    
        rc = self._bashLogServer.viewLog()
        if not rc:
            return 1
        return 0


    def processName (self):
        #not set, will get the data from init param file
        return None

    def changedEarlyLogLevel (self):        
        return logging.WARN

    @classmethod
    def s_getInitParamsFilesDirEnvVarName (cls):        
        return cls.INIT_PARAM_FILES_DIR_ENV_VAR_NAME

    @classmethod
    def s_createInitParamFiles(cls, dbglog, initParamFilesDir, dictionary):        
        a.infra.format.json.writeToFile(dbglog, dictionary, os.path.join(initParamFilesDir, cls.INIT_PARAM_FILE_NAME), indent=4)


    


