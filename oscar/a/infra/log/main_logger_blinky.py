import main_logger
import os
import a.infra.process
import a.sys.blinky.pearl

if  __package__ is None:
    G_NAME_MODULE_LOG = "unknown"
    G_NAME_GROUP_LOG_GENERIC_INSTANCE = "unknown"
else:
    from . import G_NAME_MODULE_LOG
    from . import G_NAME_GROUP_LOG_GENERIC_INSTANCE


class _SingleProcessBlinkyData:
    """ this class is simulating the module retrieving data from blinky"""

    ACTUAL_SUFFIX = "-actual"

    LOG_DIR = main_logger.MainLogger.INIT_PARAM_DATA_LOG_DIR

    LOG_LEVEL = main_logger.MainLogger.INIT_PARAM_DATA_LOG_LEVEL

    def __init__ (self, processName, logger):
        self._log = logger.createLogger(G_NAME_MODULE_LOG, G_NAME_GROUP_LOG_GENERIC_INSTANCE)
        self._blinkyDataEngine = a.sys.blinky.pearl.BlinkyJsonDataEngine(self._log)
        self._processName = processName

    def initBlinky (self, keyPathSpecificBlinky):
        self._keyPathSpecificBlinky = keyPathSpecificBlinky
        self._blinkyDataEngine.initBlinky(self._keyPathSpecificBlinky)

    def removeFromBlinky (self):
        self._keyPathSpecificBlinky.remove()

    def configuredToActual (self):
        self._blinkyDataEngine.writeOperationalVolatileField(self.LOG_DIR+self.ACTUAL_SUFFIX, self.readLogDir())

    def isDefinedLogDir (self):
        fieldName = self.LOG_DIR
        return self._blinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultLogDir (self):
        fieldName = self.LOG_DIR
        return self._blinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readLogDir (self):
        fieldName = self.LOG_DIR
        return self._blinkyDataEngine.readConfigurationField(fieldName)       
    def writeLogDirDefault (self, data):
        fieldName = self.LOG_DIR
        self._blinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)

    def readLogLevel (self):
        """
        Raises:
            None
        """
        fieldName = self.LOG_LEVEL
        if self._blinkyDataEngine.isExistsConfigurationField(fieldName):
            return self._blinkyDataEngine.readOperationalPersistentField(fieldName)
        else:
            return "N"



class ModuleCentralBlinkyData:
    BLINKY_MODULE_KEY_PATH = os.path.join("infra", "log", "main_logger")
    BLINKY_PROCESS_TABLE_SUB_KEY_PATH = "processes"
    BLINKY_PROCESS_TABLE_KEY_PATH = os.path.join(BLINKY_MODULE_KEY_PATH, BLINKY_PROCESS_TABLE_SUB_KEY_PATH)

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_LOG, G_NAME_GROUP_LOG_GENERIC_INSTANCE)
        self._moduleCentralBlinkyDataEngine = a.sys.blinky.pearl.BlinkyJsonDataEngine(self._log)

    def initBlinky (self, blinky):
        self._blinky = blinky
        self._specificKeyPathBlinky = self._blinky.keyPath(self.BLINKY_MODULE_KEY_PATH)
        self._moduleCentralBlinkyDataEngine.initBlinky(self._specificKeyPathBlinky)

    def isExists (self):
        return self._specificKeyPathBlinky.isExists()

    def getProcessesList (self):
        return self._blinky.keyPath(self.BLINKY_PROCESS_TABLE_KEY_PATH).listDirectChildKeyPath()

    def getProcessBlinkyData (self, processName):
        singleProcessBlinkyData = _SingleProcessBlinkyData(processName, self._log)
        singleProcessBlinkyData.initBlinky(self._blinky.keyPath(self.BLINKY_PROCESS_TABLE_KEY_PATH, processName))
        return singleProcessBlinkyData        

    def removeProcessFromBlinky (self, processName):
        self.getProcessBlinkyData(processName).removeFromBlinky()
        



class SingleProcessBlinkyInitCfgWriter(a.sys.blinky.pearl.BlinkyInitCfgWriter):
    def __init__(self,logger):
        a.sys.blinky.pearl.BlinkyInitCfgWriter.__init__(self,logger)

    def _refreshLogDir (self):
        self._genericUpdateField()
    def getLogDir (self):
        return self._genericGetValue()
    def setDefaultLogDir (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultLogDir (self):
        self._genericCommitDefault()

    def refreshFromBlinky(self):
        self.clearCachedData()
        self._refreshLogDir()

    def commitAllDefaults (self):
        self._commitDefaultLogDir()

