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
import a.sys.std_process.micro_captain
import a.sys.mng.user_log.server
import a.sys.mng.user_log.service
import a.sys.mng.user_log.log_infra


G_NAME_MODULE_APP_USER_LOG_SERVER = "app-user-log-server"
G_NAME_GROUP_APP_USER_LOG_SERVER_DEFAULT = "default"

class UserLogServerApp(a.sys.std_process.micro_captain.MicroAppInterface):
    INIT_PARAM_FILES_DIR_ENV_VAR_NAME = "QB_USER_LOG_SERVER_INIT_PARAM_FILES_DIR"
    #init params handling
    INIT_PARAM_FILE_NAME = "user-log-server-init-params.json"
    #kept fields
    INIT_PARAM_INPUT_GENERATION_COMMAND_PATTERN   = "input-generation-command-pattern"    
    INIT_PARAM_STATE_DIR                  = "state-dir"
    INIT_PARAM_PYTHON_FILES_LIST_FILE     = "python-files-list-file"
    INIT_PARAM_USER_LOG_INFRA_LOGGER_DICT = "user-log-infra-logger-dict"    

    _OPTION_PARSER_FLAG_VIEW_LOG = "view"
    _OPTION_PARSER_FLAG_CLEAR_LOG = "clearLogMode"
    _OPTION_PARSER_FLAG_LIST_MSGS = "listMsgMode"
    _OPTION_PARSER_FLAG_INCLUDE_DECLARED = "includeDeclared"
    _OPTION_PARSER_FLAG_INCLUDE_ACTIVE = "includeActive"

    _STATE_FILE_NAME =  "state.json"
    

    def __init__ (self):
        self._clearLog = False      
        self._listMsgs = False      
        self._includeDeclared = False      
        self._includeActive = False      

    def initLogger(self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_APP_USER_LOG_SERVER, G_NAME_GROUP_APP_USER_LOG_SERVER_DEFAULT)

    def createCaptainClients (self):
        self._userLogInfraLogger = a.sys.mng.user_log.log_infra.LogInfra()        
        self._userLogInfraLogger.initLoggerToUse(self._log)
        self._userLogInfraLogger.initCaptain(self._captain)
        self._userLogInfraLogger.initCaptainClientBehavior(skipInitFromParamFile=True)
        self._captain._addClient(self._userLogInfraLogger.getCaptainClientName(), self._userLogInfraLogger)

        userLogService = a.sys.mng.user_log.service.Service(self._log)
        userLogService.initCaptain(self._captain)
        self._captain._addClient(userLogService.CAPTAIN_CLIENT_NAME, userLogService)   

    def initFromParamFile(self, initParamFilesDirName):
        data = a.infra.format.json.readFromFile(self._log, 
                                                os.path.join(initParamFilesDirName, self.INIT_PARAM_FILE_NAME))
        self.initFromDictionary(data)

    def initFromDictionary(self, data):
        self.init(data[self.INIT_PARAM_INPUT_GENERATION_COMMAND_PATTERN], 
                  data[self.INIT_PARAM_STATE_DIR],
                  data[self.INIT_PARAM_PYTHON_FILES_LIST_FILE],
                  data[self.INIT_PARAM_USER_LOG_INFRA_LOGGER_DICT])

    def init (self, inputGenerationCommandPattern, stateDir, pythonFilesListFile, userLogInfraLoggerDict):
        self._userLogServer = a.sys.mng.user_log.server.Server(self._log)
        self._userLogServer.initInputGenerationCommandPattern(inputGenerationCommandPattern)
        self._userLogServer.initOutputFd(sys.stdout)
        self._userLogServer.initStateFile(os.path.join(stateDir, self._STATE_FILE_NAME))
        self._userLogServer.initMsgsFiles(pythonFilesListFile)
        self._userLogInfraLogger.manualReplaceCaptainClient_initFromDictionary(userLogInfraLoggerDict)
        
    def addToOptParser(self, optParser):
        optParser.add_option("--clear", action="store_true", dest=self._OPTION_PARSER_FLAG_CLEAR_LOG, default=False, help="Clear log file")
        optParser.add_option("--list-msgs", action="store_true", dest=self._OPTION_PARSER_FLAG_LIST_MSGS, default=False, help="list msgs")
        optParser.add_option("--include-declared", action="store_true", dest=self._OPTION_PARSER_FLAG_INCLUDE_DECLARED, default=False, help="When listing messages - include the declared messages")
        optParser.add_option("--include-active", action="store_true", dest=self._OPTION_PARSER_FLAG_INCLUDE_ACTIVE, default=False, help="When listing messages - include the active messages")

    def parseCmdLine(self, options, args):
        __pychecker__='no-argsused'
        if hasattr(options, self._OPTION_PARSER_FLAG_CLEAR_LOG):
            if getattr(options, self._OPTION_PARSER_FLAG_CLEAR_LOG):
                self._clearLog = True

        if hasattr(options, self._OPTION_PARSER_FLAG_LIST_MSGS):
            if getattr(options, self._OPTION_PARSER_FLAG_LIST_MSGS):
                self._listMsgs = True

        if hasattr(options, self._OPTION_PARSER_FLAG_INCLUDE_DECLARED):
            if getattr(options, self._OPTION_PARSER_FLAG_INCLUDE_DECLARED):
                self._includeDeclared = True

        if hasattr(options, self._OPTION_PARSER_FLAG_INCLUDE_ACTIVE):
            if getattr(options, self._OPTION_PARSER_FLAG_INCLUDE_ACTIVE):
                self._includeActive = True


    def run (self):     
        if self._clearLog:
            rc = self._userLogServer.clearLog()
            if not rc:
                self._log("clear-failed").error("failed to clear the log")
        elif self._listMsgs:
            rc = self._userLogServer.viewMsgsList(self._includeDeclared, self._includeActive)
        else:
            rc = self._userLogServer.viewLog()

        if not rc:
            return 1
        return 0


    def processName (self):
        #not set, will get the data from init param file
        return None

    def changedEarlyLogLevel (self):        
        return logging.WARN

    @classmethod
    def  s_writeStateFileIfNoneExists (cls, stateDir):      
        a.sys.mng.user_log.server.Server.s_writeStateFileIfNoneExists(os.path.join(stateDir, cls._STATE_FILE_NAME))        

    @classmethod
    def s_getInitParamsFilesDirEnvVarName (cls):        
        return cls.INIT_PARAM_FILES_DIR_ENV_VAR_NAME

    @classmethod
    def s_createInitParamFiles(cls, dbglog, initParamFilesDir, dictionary):        
        a.infra.format.json.writeToFile(dbglog, dictionary, os.path.join(initParamFilesDir, cls.INIT_PARAM_FILE_NAME), indent=4)


    


