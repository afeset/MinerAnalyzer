# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

import os     
import logging
import a.infra.format.json
import a.sys.std_process.micro_captain
import a.sys.mng.user_log.service

G_NAME_MODULE_APP_USER_LOG_SERVICE = "app-user-log-service"
G_NAME_GROUP_APP_USER_LOG_SERVICE_DEFAULT = "default"

class UserLogServiceApp(a.sys.std_process.micro_captain.MicroAppInterface):
    #init params handling
    INIT_PARAM_FILE_NAME = "user-log-service-app-init-params.json"
    #kept fields
    INIT_PARAM_USER_LOG_INFRA_LOGGER_DICT = "user-log-infra-logger-dict"

    OPTION_MESSAGE_NAME = "--message-name"
    _OPTION_PARSER_FLAG_MESSAGE_NAME = "message_name"

    def __init__ (self):
        self._messageName = None
        self._messageArgs = []
        
    def initLogger(self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_APP_USER_LOG_SERVICE, G_NAME_GROUP_APP_USER_LOG_SERVICE_DEFAULT)

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
        self.init(data[self.INIT_PARAM_USER_LOG_INFRA_LOGGER_DICT])

    def init (self, userLogInfraLoggerDict):
        self._userLogInfraLogger.manualReplaceCaptainClient_initFromDictionary(userLogInfraLoggerDict)


    def addToOptParser(self, optParser):
        optParser.add_option(self.OPTION_MESSAGE_NAME, action="store", type="string", dest=self._OPTION_PARSER_FLAG_MESSAGE_NAME, help="Message name to sendClear log file")

    def parseCmdLine(self, options, args):
        if hasattr(options, self._OPTION_PARSER_FLAG_MESSAGE_NAME):
            self._messageName = getattr(options, self._OPTION_PARSER_FLAG_MESSAGE_NAME)
            self._log("message-name").debug1("message name is: %s", self._messageName)
        else:
            a.infra.process.processFatal("Command line missing message name")
        self._messageArgs = ["'%s'"%arg for arg in args[1:]]
        self._log("message-args").debug1("message args are: %s", self._messageArgs)

    def run (self):   
        try:
            objIndex = self._messageName.rindex(".")
            moduleName = self._messageName[0:objIndex]
            self._log("module-name").debug1("module name is %s", moduleName)
            messageObject = self._messageName[(objIndex+1):]
            self._log("message-object").debug1("message object name is: %s", messageObject)

            messageCreationCommand = "%s(%s)"%(self._messageName, ",".join(self._messageArgs))
            self._log("creation-command").debug1("message creation command command is: %s", messageCreationCommand)

            __import__(moduleName)
            msgObj = eval(messageCreationCommand)

            a.infra.process.logUserMessage(msgObj)
        except:
            self._log("failed").exception("Failed to send message %s[%s]", self._messageName, ",".join(self._messageArgs))
            return 1

        return 0


    def changedEarlyLogLevel (self):        
        return logging.WARN

    def processName (self):
        #not set, will get the data from init param file
        return None

    @classmethod
    def s_getInitParamsFilesDirEnvVarName (cls):        
        return None

    @classmethod
    def s_createInitParamFiles(cls, dbglog, initParamFilesDir, dictionary):        
        a.infra.format.json.writeToFile(dbglog, dictionary, os.path.join(initParamFilesDir, cls.INIT_PARAM_FILE_NAME), indent=4)





