# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

"""
This class implements an exceutable for a generic action.
The application class name is provided on the command line (--application-class)
This class is generated and run
The loaded class must implement the below functions:
A. ctor that gets logger as input
B. genericAction_run(self, args): where "args" is the list of argument - "argv" of parameters for this application only

Addtionally, it can implement
A. genericAction_passive2Active(self): for connecting to blinky
B. genericAction_initFromDictionary(self, data): for getting additional data

"""
import logging
import os
import a.infra.process
import a.infra.format.json
import a.sys.std_process.micro_captain
import a.infra.basic.return_codes

G_NAME_MODULE_APP_GENERIC_ACTION = "app-generic-act"
G_NAME_GROUP_APP_GENERIC_ACTION_DEFAULT = "default"

class GenericActionApp(a.sys.std_process.micro_captain.MicroAppInterface):
    INIT_PARAM_FILES_DIR_ENV_VAR_NAME = "QB_GENERIC_ACTION_INIT_PARAM_FILES_DIR"

    #init params handling
    INIT_PARAM_FILE_NAME = "generic-action-init-params.json"

    #kept fields
    INIT_PARAM_PER_APPLICATION_CLASS_DATA = "per-application-class-data"    

    #options to opt parse
    _OPTION_PARSER_OPTION_APPLICATION_CLASS="applicationClass"

    def __init__ (self):
        self._application = None
        self._applicationArgs = []        

    def initLogger(self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_APP_GENERIC_ACTION, G_NAME_GROUP_APP_GENERIC_ACTION_DEFAULT)

    def createCaptainClients (self):
        pass

    def initFromParamFile(self, initParamFilesDirName):
        data = a.infra.format.json.readFromFile(self._log, 
                                                os.path.join(initParamFilesDirName, self.INIT_PARAM_FILE_NAME))
        self.initFromDictionary(data)

    def initFromDictionary(self, data):
        self.init(data[self.INIT_PARAM_PER_APPLICATION_CLASS_DATA])

    def init (self, perApplicationClassData):
        __pychecker__='no-argsused'
        if self._applicationClass in perApplicationClassData:
            self._application.genericAction_initFromDictionary(perApplicationClassData[self._applicationClass])        
        
    def addToOptParser(self, optParser):
        optParser.add_option("--application-class", type="string", default=None,
                             action="store", dest=self._OPTION_PARSER_OPTION_APPLICATION_CLASS, 
                             help="application class to run")

    def parseCmdLine(self, options, args):
        self._applicationArgs = args
        self._applicationClass = getattr(options, self._OPTION_PARSER_OPTION_APPLICATION_CLASS)
        if self._applicationClass is None:
            a.infra.process.processFatal("missing application class to run")
        moduleList = self._applicationClass.split(".")
        moduleName = ".".join(moduleList[:-1])
        
        try:
            __import__(moduleName)
            reload(eval(moduleName))
        except:
            a.infra.process.processFatal("failed to load application class '%s'", moduleName)

        try:
            self._application = eval(self._applicationClass)(self._log)    
        except:
            a.infra.process.processFatal("failed to create object '%s'", self._applicationClass)


    def passive2Active (self):
        if hasattr(self._application, "genericAction_passive2Active"):
            self._application.genericAction_passive2Active()

    def run (self):
        rc = a.infra.basic.return_codes.ReturnCodes.kGeneralError

        self._log("run").notice("running class '%s' with args: %s", self._applicationClass, self._applicationArgs)
        try:
            rc = self._application.genericAction_run(self._applicationArgs)

        except SystemExit:
            raise

        except:            
            self._log("application-failed").exception("failed while running application")

        if rc != a.infra.basic.return_codes.ReturnCodes.kOk:
            return 1

        return 0
        
    def processName (self):
        #not set, will get the data from init param file
        return None

    def changedEarlyLogLevel (self):        
        return logging.WARN

    def isSupportTerminationBySignal (self):
        return True

    @classmethod
    def s_getInitParamsFilesDirEnvVarName (cls):        
        return cls.INIT_PARAM_FILES_DIR_ENV_VAR_NAME

    @classmethod
    def s_createInitParamFiles(cls, dbglog, initParamFilesDir, dictionary):        
        a.infra.format.json.writeToFile(dbglog, dictionary, os.path.join(initParamFilesDir, cls.INIT_PARAM_FILE_NAME), indent=4)    
