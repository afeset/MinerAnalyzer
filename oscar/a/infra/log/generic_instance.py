# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: nirs

import logger
import qbl_formatter
import flex_file_handler
import logging
import os
import a.infra.format.json
import a.infra.process

if  __package__ is None:
    G_NAME_MODULE_LOG = "unknown"
    G_NAME_GROUP_LOG_GENERIC_INSTANCE = "unknown"
else:
    from . import G_NAME_MODULE_LOG
    from . import G_NAME_GROUP_LOG_GENERIC_INSTANCE


class TempJunkDummyLoggerHelper(object):
    def __getattr__ (self, attr):
        __pychecker__ = "no-argsused"
        def doNothing (*args, **kwargs):
            __pychecker__ = "no-argsused"
            pass
        def doNothingFunc (*args, **kwargs):
            __pychecker__ = "no-argsused"
            return []
        if attr.endswith("Func"):
            return doNothingFunc
        return doNothing

class TempJunkDummyLogger(TempJunkDummyLoggerHelper):
    def __call__ (self, *args, **kwargs):
        __pychecker__ = "no-argsused"
        return TempJunkDummyLoggerHelper()
    def __getattr__ (self, attr):
        __pychecker__ = "no-argsused"        
        def doNothingReturnLogger (*args, **kwargs):
            __pychecker__ = "no-argsused"
            return TempJunkDummyLogger()
        if attr.startswith("createLogger"):           
            return doNothingReturnLogger
        return TempJunkDummyLoggerHelper.__getattr__ (self, attr)



class GenericInstance:
    #management keys    
    DEFAULT_HANDLER_MNG_NAME = "default-handler"

    #kept fields
    INIT_PARAM_DATA_LOG_DIR="log-dir"
    INIT_PARAM_DATA_LOG_LEVEL="log-level"
    INIT_PARAM_DATA_LOG_FILE_SIZE="log-file-size"
    INIT_PARAM_DATA_LOG_TOTAL_SIZE="log-total-size"
    INIT_PARAM_DATA_LOG_STAY_ON_EARLY="stay-on-early"
    INIT_PARAM_DATA_LOG_PEARL_CONFIGURATION_FILE_NAMES_LIST="configuration-file-name"#string did not change to support install_operations PXE run
    INIT_PARAM_DATA_LOG_PEARL_CONFIGURATION_FILE_LOAD_PERIOD="configuration-file-load-period"    
    INIT_PARAM_DATA_IS_MULTI_PROCESS="is-multi-process"
    INIT_PARAM_DATA_MAX_MULTI_PROCESS_LOCK_RETRY_TIMEOUT="max-multi-process-lock-timeout"
    INIT_PARAM_DATA_SKIP_WELCOME_MESSAGES="skip-welcome-messages"

    def __init__ (self, loggerName, earlyLogLevel, defaultLogLevel, processName, fileNameNameDefaultUsePhasePearl):
        self.loggerName = loggerName
        if earlyLogLevel is None:
            earlyLogLevel = logging.NOTICE
        self.loggerManager = logger.LoggerManager(loggerName, processName, earlyLogLevel)
        self.earlyLogLevel = earlyLogLevel
        self.defaultLogLevel = defaultLogLevel
        self.fileNameNameDefaultUsePhasePearl = fileNameNameDefaultUsePhasePearl
        self.skipWelcomeMessages = False
        handler = logging.StreamHandler()
        handler.setLevel(logging.NOTSET)
        # create formatter
        formatter = logging.Formatter('ELG: %(asctime)s.%(msecs)03d <%(levelname)s> [%('+logger.G_RECORD_KEY_PROCESS_NAME+')s/%(threadName)s/%(instance)s] %('+logger.G_RECORD_KEY_PY_MODULE+')s::%('+logger.G_RECORD_KEY_CLASS+')s::%(funcName)s#%(lineno)d %(message)s', datefmt='%Y%m%d-%H%M%S')
        # add formatter to the handler
        handler.setFormatter(formatter)
        # add handler to logger
        self.loggerManager.addHandler(self.DEFAULT_HANDLER_MNG_NAME, handler)

        self._cfgOverrideFromCmdline = {}
        self._cfgEmptyDict = {self.INIT_PARAM_DATA_LOG_DIR: None,
                              self.INIT_PARAM_DATA_LOG_LEVEL: None,
                              self.INIT_PARAM_DATA_LOG_FILE_SIZE: 0,
                              self.INIT_PARAM_DATA_LOG_TOTAL_SIZE: 0,
                              self.INIT_PARAM_DATA_LOG_STAY_ON_EARLY: False,
                              self.INIT_PARAM_DATA_LOG_PEARL_CONFIGURATION_FILE_NAMES_LIST: None,
                              self.INIT_PARAM_DATA_LOG_PEARL_CONFIGURATION_FILE_LOAD_PERIOD: 0,
                              self.INIT_PARAM_DATA_IS_MULTI_PROCESS: False,
                              self.INIT_PARAM_DATA_MAX_MULTI_PROCESS_LOCK_RETRY_TIMEOUT: 0,                              
                              self.INIT_PARAM_DATA_SKIP_WELCOME_MESSAGES: True
                              }
        
        self._captainClientSkipInitFromParamFile = False#need to do it better!


    def setProcessName (self, processName):
        self.loggerManager.setProcessName(processName)

    def initCaptain (self, captain):
        self._captain = captain

    def initLoggerToUse (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_LOG, G_NAME_GROUP_LOG_GENERIC_INSTANCE, instance=self.loggerName)
        self.loggerManager.initLoggerToUse(self._log)

    def getLoggerManager (self):
        return self.loggerManager

    def init (self, initialLogLevel=None, logDir=None, logFileSize=0, logTotalSize=0, stayOnEarly = False,
              isMultiProcess=False, maxMultiProcessLockRetryTimeout=0, skipWelcomeMessages=False,
              pearlConfigurationFilesFullName=None, pearlConfigurationLoadPeriodInSeconds=0):        
        self.loggerManager.initCollectKickNumber()#late enough to start collecting the kick number

        self.skipWelcomeMessages = skipWelcomeMessages
        if stayOnEarly:
            self._log("init-stay-early").debug1("staying on early logger")    
        else:
            self._log("init").debug1("initialLogLevel='%s', logDir='%s'", initialLogLevel, logDir)
            if logDir is not None:
                handler = flex_file_handler.FlexFileHandler(loggerToUse=TempJunkDummyLogger(),
                                                            fileDir=logDir, 
                                                            fileBaseNamePrefix="log-", 
                                                            fileBaseNameSuffix=".qbl",
                                                            usePhases = self.fileNameNameDefaultUsePhasePearl, 
                                                            logFileSize = logFileSize, 
                                                            isMultiProcess = isMultiProcess, 
                                                            maxMultiProcessLockRetryTimeout = maxMultiProcessLockRetryTimeout,
                                                            isBinary = True)
                handler.setTotalSize(logTotalSize = logTotalSize)
                handler.setLevel(logging.NOTSET)
                formatter = qbl_formatter.QblFormatter()
                handler.setFormatter(formatter)
                self.loggerManager.replaceHandler(self.DEFAULT_HANDLER_MNG_NAME, handler)   
    
            if initialLogLevel is None:
                initialLogLevel = self.defaultLogLevel
            if initialLogLevel is not None:
                self.loggerManager.setDefaultLogLevel(initialLogLevel)
                
            if not pearlConfigurationFilesFullName is None:
                self.loggerManager.pearlSetConfigurationFiles (pearlConfigurationFilesFullName, pearlConfigurationLoadPeriodInSeconds)
            

        if not self.skipWelcomeMessages:
            self.loggerManager.logSelfMsg(logging.NOTICE, "===== WELCOME ====== WELCOME ====== WELCOME ======")    



    def initFromDictionary (self, data):
        self.init(initialLogLevel = logger.LevelTranslate.s_getPyLevelFromCpp(data[self.INIT_PARAM_DATA_LOG_LEVEL]),
                  logDir = data[self.INIT_PARAM_DATA_LOG_DIR],
                  logFileSize = data[self.INIT_PARAM_DATA_LOG_FILE_SIZE],
                  logTotalSize = data[self.INIT_PARAM_DATA_LOG_TOTAL_SIZE],
                  stayOnEarly = data[self.INIT_PARAM_DATA_LOG_STAY_ON_EARLY],
                  isMultiProcess=data[self.INIT_PARAM_DATA_IS_MULTI_PROCESS], 
                  maxMultiProcessLockRetryTimeout=data[self.INIT_PARAM_DATA_MAX_MULTI_PROCESS_LOCK_RETRY_TIMEOUT],
                  skipWelcomeMessages=data[self.INIT_PARAM_DATA_SKIP_WELCOME_MESSAGES],
                  pearlConfigurationFilesFullName = data[self.INIT_PARAM_DATA_LOG_PEARL_CONFIGURATION_FILE_NAMES_LIST],
                  pearlConfigurationLoadPeriodInSeconds = data[self.INIT_PARAM_DATA_LOG_PEARL_CONFIGURATION_FILE_LOAD_PERIOD])   
                                            
    def initCaptainClientBehavior (self, skipInitFromParamFile=False):
        self._captainClientSkipInitFromParamFile = skipInitFromParamFile

    def captainClient_initFromParamFile (self):
        if self._captainClientSkipInitFromParamFile:
            return#waiting to the manual setting using manualReplaceCaptainClient_initFromDictionary

        initParamFilesDirName = self._captain.getInitParamFilesDirName()
        initParamFileName = os.path.join(initParamFilesDirName, self.getInitParamFileName())
        try:
            if os.path.exists(initParamFileName):
                self._log("read-cfg-file").debug2("reading cfg file %s", initParamFileName)
                data = a.infra.format.json.readFromFile(self._log, initParamFileName)
            else:
                data = {}

        except Exception as exception:
            a.infra.process.processFatal("Failed to init logger %s: %s", self.loggerName, str(exception))
        
        self.manualReplaceCaptainClient_initFromDictionary(data)

    def manualReplaceCaptainClient_initFromDictionary (self, data):
        finalData = dict(self._cfgEmptyDict.items() + data.items() + self._cfgOverrideFromCmdline.items())
        self._log("final-init-values").debug2("Init values: from cmd: '%s', from file '%s', default '%s', final: '%s'", 
                                              self._cfgOverrideFromCmdline, data, self._cfgEmptyDict, finalData)
        self.initFromDictionary(finalData)


    def captainClient_addToOptParser (self):
        self._captain.getOptParser().add_option(self.getOptionStringLogDir(), type="string",
                                                action="store", dest=self._optionStringToDest(self.getOptionStringLogDir()), 
                                                help="The directory in into which the main logger output is written")
        self._captain.getOptParser().add_option(self.getOptionStringInitialLogLevel(), type="string",
                                                action="store", dest=self._optionStringToDest(self.getOptionStringInitialLogLevel()), 
                                                help="The log level of the logger")
        self._captain.getOptParser().add_option(self.getOptionStringLogFileSize(), type="int",
                                                action="store", dest=self._optionStringToDest(self.getOptionStringLogFileSize()), 
                                                help="The size of each log file")
        self._captain.getOptParser().add_option(self.getOptionStringLogTotalSize(), type="int",
                                                action="store", dest=self._optionStringToDest(self.getOptionStringLogTotalSize()), 
                                                help="The total size of all log files")
        self._captain.getOptParser().add_option(self.getFlagStringStayOnEarly(),                                                
                                                action="store_true", default=False, 
                                                dest=self._optionStringToDest(self.getFlagStringStayOnEarly()), 
                                                help="Stay on early log")
        self._captain.getOptParser().add_option(self.getFlagStringPassEarly(),                                                
                                                action="store_true", default=False, 
                                                dest=self._optionStringToDest(self.getFlagStringPassEarly()), 
                                                help="Dont stay on early log")


    def captainClient_parseCmdLine (self):       
        (options, args) = self._captain.getParsedCmd()

        def insertIfNotNone(dictionary,key,val):
            if val is not None:
                dictionary[key]=val

        insertIfNotNone(self._cfgOverrideFromCmdline, self.INIT_PARAM_DATA_LOG_LEVEL     , getattr(options, self._optionStringToDest(self.getOptionStringInitialLogLevel())))
        insertIfNotNone(self._cfgOverrideFromCmdline, self.INIT_PARAM_DATA_LOG_DIR       , getattr(options, self._optionStringToDest(self.getOptionStringLogDir()))         )
        insertIfNotNone(self._cfgOverrideFromCmdline, self.INIT_PARAM_DATA_LOG_FILE_SIZE , getattr(options, self._optionStringToDest(self.getOptionStringLogFileSize()))    )
        insertIfNotNone(self._cfgOverrideFromCmdline, self.INIT_PARAM_DATA_LOG_TOTAL_SIZE, getattr(options, self._optionStringToDest(self.getOptionStringLogTotalSize()))   )
        stayOnEarly = None
        if getattr(options, self._optionStringToDest(self.getFlagStringStayOnEarly())):
            stayOnEarly = True
        if getattr(options, self._optionStringToDest(self.getFlagStringPassEarly())):
            stayOnEarly = False
        insertIfNotNone(self._cfgOverrideFromCmdline, self.INIT_PARAM_DATA_LOG_STAY_ON_EARLY, stayOnEarly)

    def captainClient_addToOsef (self):
        self._log("add-to-osef").debug2("adding to osef: %s", self.getOsefKey())
        self._captain.getOsef()[self.getOsefKey()] = self

    def captainClient_lateShutdown (self):
        self.loggerManager.logPerformanceData("logger performace", onlyIfNotEmpty=True, splitByModule=True, splitByInterfaceType=True)
        handler = logging.StreamHandler()
        handler.setLevel(logging.NOTSET)
        # create formatter
        formatter = logging.Formatter('ELG: %(asctime)s.%(msecs)03d <%(levelname)s> [%('+logger.G_RECORD_KEY_PROCESS_NAME+')s/%(threadName)s/%(instance)s] %('+logger.G_RECORD_KEY_PY_MODULE+')s::%('+logger.G_RECORD_KEY_CLASS+')s::%(funcName)s#%(lineno)d %(message)s', datefmt='%Y%m%d-%H%M%S')
        # add formatter to the handler
        handler.setFormatter(formatter)
        if not self.skipWelcomeMessages:
            self.loggerManager.logSelfMsg(logging.NOTICE, "===== GOODBYE ====== GOODBYE ====== GOODBYE ======")   
        self.loggerManager.setDefaultLogLevel(self.earlyLogLevel)
        # replace handler to logger
        self.loggerManager.replaceHandler(self.DEFAULT_HANDLER_MNG_NAME, handler)   

    def getCaptainClientName (self):
        return self._s_getCaptainClientName(self.loggerName)

    def getOsefKey (self):
        return self._s_getOsefKey(self.loggerName)

    def getInitParamFileName (self):
        return self.__s_getInitParamFileName(self.loggerName)

    def getOptionStringLogDir (self):
        return self._s_getOptionStringLogDir(self.loggerName)

    def getOptionStringInitialLogLevel (self):
        return self._s_getOptionStringInitialLogLevel(self.loggerName)

    def getOptionStringLogFileSize (self):
        return self._s_getOptionStringLogFileSize(self.loggerName)

    def getOptionStringLogTotalSize (self):
        return self._s_getOptionStringLogTotalSize(self.loggerName)

    def getFlagStringStayOnEarly (self):
        return self._s_getFlagStringStayOnEarly(self.loggerName)

    def getFlagStringPassEarly (self):
        return self._s_getFlagStringPassEarly(self.loggerName)

    @staticmethod
    def _s_getCaptainClientName (loggerName):
        return loggerName

    @staticmethod
    def _s_getOsefKey (loggerName):
        return loggerName

    @staticmethod
    def _s_getFromOsefUnsafe (osef, loggerName):
        if not loggerName in osef:
            return None
        return osef[loggerName]

    @classmethod
    def _s_getFromOsefOrCrash (cls, osef, loggerName):
        logger = cls._s_getFromOsefUnsafe(osef, loggerName)
        if logger is None:
            a.infra.process.processFatal("Failed to bring logger '%s' from osef", loggerName)
        return logger

    @staticmethod
    def __s_getInitParamFileName (loggerName):
        return "%s-init-params.json"%loggerName

    @staticmethod
    def _s_getOptionStringLogDir (loggerName):
        return "--%s-dir"%loggerName

    @staticmethod
    def _s_getOptionStringInitialLogLevel (loggerName):
        return "--%s-initial-level"%loggerName

    @staticmethod
    def _s_getOptionStringLogFileSize (loggerName):
        return "--%s-file-size"%loggerName

    @staticmethod
    def _s_getOptionStringLogTotalSize (loggerName):
        return "--%s-total-size"%loggerName

    @staticmethod
    def _s_getFlagStringStayOnEarly (loggerName):
        return "--%s-early-log"%loggerName

    @staticmethod
    def _s_getFlagStringPassEarly (loggerName):
        return "--%s-pass-early-log"%loggerName

    def _optionStringToDest (self, optionString):
        return optionString.replace("-","_").lstrip("_")

    @classmethod
    def _s_createInitParamFile (cls, dbgLog, initParamFilesDirName, loggerName, dictionary):
        a.infra.format.json.writeToFile(dbgLog, dictionary, os.path.join(initParamFilesDirName, cls.__s_getInitParamFileName(loggerName)), indent=4)





