#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import os
import sys
import shutil
import a.infra.process
import a.infra.format.json
import a.sys.blinky.pearl

if  __package__ is None:
    G_NAME_MODULE_BLINKY = "unknown"
    G_NAME_GROUP_BLINKY_PEARL = "unknown"
else:
    from . import G_NAME_MODULE_BLINKY 
    from . import G_NAME_GROUP_BLINKY_PEARL 

class Blinky:
    """A temp class used as blinky"""

    OSEF_KEY = "blinky"
    CAPTAIN_CLIENT_NAME = OSEF_KEY

    #init params things
    INIT_PARAM_FILE_NAME = "confd-init-params.json"
    #kept fields
    INIT_PARAM_DATA_CONFD_PERSISTENT_DIR = "confd-persistent-dir"
    INIT_PARAM_DATA_CONFD_VOLATILE_DIR = "confd-volatile-dir"

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_BLINKY, G_NAME_GROUP_BLINKY_PEARL)

    def initCaptain (self, captain):
        self._captain = captain

    def init (self, confdPersistentDir, confdVolatileDir):
        self._confdPersistentDir = confdPersistentDir
        self._confdVolatileDir = confdVolatileDir

    def keyPath (self, *args):
        newBlinky = Blinky(self._log)
        newBlinky.init(os.path.join(self._confdPersistentDir, *args), os.path.join(self._confdVolatileDir, *args))
        return newBlinky

    def remove (self):
        if os.path.exists(self._confdPersistentDir):
            shutil.rmtree(self._confdPersistentDir)
        if os.path.exists(self._confdVolatileDir):
            shutil.rmtree(self._confdVolatileDir)

    def isExists (self):
        if os.path.exists(self._confdPersistentDir):
            return True
        if os.path.exists(self._confdVolatileDir):
            return True
        return False
        

    def listDirectChildKeyPath (self):
        dirs = []
        if os.path.exists(self._confdPersistentDir):
            files = os.listdir(self._confdPersistentDir)
            for fileName in files:
                if os.path.isdir(os.path.join(self._confdPersistentDir, fileName)):
                    if not fileName in dirs:
                        dirs += [fileName]

        if os.path.exists(self._confdVolatileDir):
            files = os.listdir(self._confdVolatileDir)
            for fileName in files:
                if os.path.isdir(os.path.join(self._confdVolatileDir, fileName)):
                    if not fileName in dirs:
                        dirs += [fileName]
            
        return sorted(dirs)

    def initFromDictionary (self, data):
        self.init(data[self.INIT_PARAM_DATA_CONFD_PERSISTENT_DIR], data[self.INIT_PARAM_DATA_CONFD_VOLATILE_DIR])

    def captainClient_initFromParamFile (self):
        initParamFilesDirName = self._captain.getInitParamFilesDirName()
        data = a.infra.format.json.readFromFile(self._log, os.path.join(initParamFilesDirName, self.INIT_PARAM_FILE_NAME))
        self.initFromDictionary(data)

    def captainClient_addToOsef (self):
        self._captain.getOsef()[self.OSEF_KEY] = self

    def getConfdPersistentDir (self):
        return self._confdPersistentDir

    def getConfdVolatileDir (self):
        return self._confdVolatileDir

    @classmethod
    def s_createInitParamFile (cls, dbgLog, initParamFilesDirName, data):
        a.infra.format.json.writeToFile(dbgLog, data, os.path.join(initParamFilesDirName, cls.INIT_PARAM_FILE_NAME), indent=4)


class BlinkyJsonDataEngine:
    """ This class is used as an engine for "BlinkData" classes that need to simulate operations the blinky module
    """
    def __init__ (self, logger):
        self._log = logger

    def initBlinky (self, blinky):
        """set the required parameters for creating the connection             
        Args:
            moduleName: the name of the module using this BlinkyDataEngine - used for variable names collosion avoidance
            blinky: a pearl blinky object

        Returns:
            None

        Raises:
            None            
        """
        self._persistentDir = blinky.getConfdPersistentDir()
        self._volatileDir = blinky.getConfdVolatileDir()

    def writeOperationalPersistentField (self, fieldName, data):
        """write the data  - for operational persistent data           
        Args:
            fieldName
            data - must be json dumpable

        Returns:
            None

        Raises:
            None
            None

        Raises:
            None
        """
        for logFunc in self._log("write-operational-persistent").debug2Func(): logFunc("writing the operational field %s: '%s'", fieldName, data)
        self._write(data, self._getOperationalPersistentFieldFileName(fieldName))


    def readOperationalPersistentField (self, fieldName):
        """read the data  - for operational persistent data           
        Args:
            fieldName            

        Returns:
            the data previously written

        Raises:
            None
        """
        data = self._read(self._getOperationalPersistentFieldFileName(fieldName))
        for logFunc in self._log("read-operational-persistent").debug5Func(): logFunc("read the operational field %s. value: '%s'", fieldName, data)
        return data

    def isExistsOperationalPersistentField (self, fieldName):
        return os.path.exists(self._getOperationalPersistentFieldFileName(fieldName))

    def writeOperationalVolatileField (self, fieldName, data):
        """write the data  - for operational volatile data           
        Args:
            fieldName
            data - must be json dumpable

        Returns:
            None

        Raises:
            None
            None
        """
        for logFunc in self._log("write-operational-volatile").debug2Func(): logFunc("writing the operational field %s: '%s'", fieldName, data)
        self._write(data, self._getOperationalVolatileFieldFileName(fieldName))

    def readOperationalVolatileField (self, fieldName):
        """read the data  - for operational volatile data           
        Args:
            fieldName            

        Returns:
            the data previously written

        Raises:
            None
        """
        data = self._read(self._getOperationalVolatileFieldFileName(fieldName))
        for logFunc in self._log("read-operational-volatile").debug5Func(): logFunc("read the operational field %s. value: '%s'", fieldName, data)
        return data

    def isExistsOperationalVolatileField (self, fieldName):
        return os.path.exists(self._getOperationalVolatileFieldFileName(fieldName))

    def writeConfigurationField (self, fieldName, data, isDefaultTwin=False):
        """write the data  - for configuration data           
        Args:
            fieldName
            data - must be json dumpable

        Returns:
            None

        Raises:
            None
            None
        """
        if isDefaultTwin:
            fieldName = fieldName+"-default"
        for logFunc in self._log("write-cfg").debug2Func(): logFunc("writing the configuration fields %s: '%s'", fieldName, data)
        self._write(data, self._getConfigurationFieldFileName(fieldName))

    def readConfigurationField (self, fieldName):
        """read the data  - for configuration data           
        Args:
            fieldName            

        Returns:
            the data previously written

        Raises:
            None
        """
        fileName = self._getConfigurationFieldFileName(fieldName)
        if not os.path.exists(fileName):
            fieldName = fieldName+"-default" 
            fileName = self._getConfigurationFieldFileName(fieldName)
        data = self._read(fileName)
        for logFunc in self._log("read-cfg").debug5Func(): logFunc("read the configuration fields %s. value: '%s'", fieldName, data)
        return data

    def isExistsConfigurationField (self, fieldName):
        return (os.path.exists(self._getConfigurationFieldFileName(fieldName)) or os.path.exists(self._getConfigurationFieldFileName(fieldName+"-default" )))

    def isExistsNonDefaultConfigurationField (self, fieldName):
        return os.path.exists(self._getConfigurationFieldFileName(fieldName))

    def _write(self,data,fileName):
        try:
            a.infra.format.json.writeToFile(self._log, data, fileName, mkdir=True, indent=4)
        except IOError as (errno, strerror):
            a.infra.process.processFatal("I/O error(%d) on file '%s': {%s}",errno, fileName, strerror)
        except TypeError, ex:
            a.infra.process.processFatal(str(ex))

    def _read(self,fileName):
        if not os.path.exists(fileName):
            return None
        try:
            return a.infra.format.json.readFromFile(self._log, fileName)
        except IOError as (errno, strerror):            
            a.infra.process.processFatal("I/O error(%d) on file '%s': {%s}",errno, fileName, strerror)

    def _getOperationalPersistentFieldFileName (self, fieldName):
        return os.path.join(self._persistentDir, "oper-%s.json"%fieldName)

    def _getOperationalVolatileFieldFileName (self, fieldName):
        return os.path.join(self._volatileDir, "oper-%s.json"%fieldName)

    def _getConfigurationFieldFileName (self, fieldName):
        return os.path.join(self._persistentDir, "cfg-%s.json"%fieldName)



class BlinkyInitCfgWriter:
    def __init__(self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_BLINKY, G_NAME_GROUP_BLINKY_PEARL)
        self.clearCachedData()

    def initBlinkyData (self, blinkyData):
        self._blinkyData = blinkyData

    def clearCachedData (self):
        self._cachedData = {}

    class CacheRecord:
        def __init__ (self, value, isNonDefault):
            self.value=value
            self.isNonDefault=isNonDefault

    def _genericUpdateField (self, emptyStringWhenNoData = False):
        callingFunction = sys._getframe(1).f_code.co_name
        fieldString=callingFunction[len("_refresh"):] 
        isDefinedFunction = getattr(self._blinkyData, "isDefined"+fieldString)               
        isDefinded = isDefinedFunction()
        #TODO(nirs) a lock is needed between the "isDefined" and the "read"         
        if isDefinded:
            readFunction = getattr(self._blinkyData, "read"+fieldString)
            value = readFunction()
            isNonDefault = True
            isNonDefaultFunctionName="isNonDefault"+fieldString
            if hasattr(self._blinkyData, isNonDefaultFunctionName):
                isNonDefault = isNonDefaultFunctionName()
            self._cachedData[fieldString] = self.CacheRecord(value, isNonDefault)
        elif fieldString in self._cachedData:#removing already existing data when not defined
            self._cachedData.pop(fieldString)

    def _genericGetValue (self):
        callingFunction = sys._getframe(1).f_code.co_name
        fieldString=callingFunction[len("get"):] 
        return self._cachedData[fieldString].value

    def _genericSetDefaultValue (self,value):
        callingFunction = sys._getframe(1).f_code.co_name
        fieldString=callingFunction[len("setDefault"):] 
        if not fieldString in self._cachedData:
            self._cachedData[fieldString] = self.CacheRecord(value, False)
        self._cachedData[fieldString].defaultValue=value

    def _genericCommitDefault (self):
        callingFunction = sys._getframe(1).f_code.co_name
        fieldString=callingFunction[len("_commitDefault"):] 
        writeFunction = getattr(self._blinkyData, "write"+fieldString+"Default")
        writeFunction(self._cachedData[fieldString].defaultValue)



class ModuleCentralBlinkyData:
    BLINKY_MODULE_KEY_PATH = os.path.join("sys", "blinky", "pearl")

    ACTUAL_SUFFIX = "-actual"

    CONFD_PERSISTENT_DIR = Blinky.INIT_PARAM_DATA_CONFD_PERSISTENT_DIR    
    CONFD_VOLATILE_DIR   = Blinky.INIT_PARAM_DATA_CONFD_VOLATILE_DIR

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_BLINKY, G_NAME_GROUP_BLINKY_PEARL)
        self._moduleCentralBlinkyDataEngine = a.sys.blinky.pearl.BlinkyJsonDataEngine(self._log)

    def initBlinky (self, blinky):
        self._blinky = blinky
        self._specificKeyPathBlinky = self._blinky.keyPath(self.BLINKY_MODULE_KEY_PATH)
        self._moduleCentralBlinkyDataEngine.initBlinky(self._specificKeyPathBlinky)

    def isExists (self):
        return self._specificKeyPathBlinky.isExists()

    def configuredToActual (self):
        self._moduleCentralBlinkyDataEngine.writeOperationalVolatileField(self.CONFD_PERSISTENT_DIR+self.ACTUAL_SUFFIX, self.readConfdPersistentDir())
        self._moduleCentralBlinkyDataEngine.writeOperationalVolatileField(self.CONFD_VOLATILE_DIR+self.ACTUAL_SUFFIX, self.readConfdVolatileDir())

    def isDefinedConfdPersistentDir (self):
        fieldName = self.CONFD_PERSISTENT_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultLConfdPersistentDir (self):
        fieldName = self.CONFD_PERSISTENT_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readConfdPersistentDir (self):
        fieldName = self.CONFD_PERSISTENT_DIR
        return self._moduleCentralBlinkyDataEngine.readConfigurationField(fieldName)       
    def writeConfdPersistentDirDefault (self, data):
        fieldName = self.CONFD_PERSISTENT_DIR
        self._moduleCentralBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)

    def isDefinedConfdVolatileDir (self):
        fieldName = self.CONFD_VOLATILE_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultLConfdVolatileDir (self):
        fieldName = self.CONFD_VOLATILE_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readConfdVolatileDir (self):
        fieldName = self.CONFD_VOLATILE_DIR
        return self._moduleCentralBlinkyDataEngine.readConfigurationField(fieldName)       
    def writeConfdVolatileDirDefault (self, data):
        fieldName = self.CONFD_VOLATILE_DIR
        self._moduleCentralBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)



class ModuleCentralBlinkyInitCfgWriter(BlinkyInitCfgWriter):
    def __init__(self,logger):
        BlinkyInitCfgWriter.__init__(self,logger)

    def _refreshConfdPersistentDir (self):
        self._genericUpdateField()
    def getConfdPersistentDir (self):
        return self._genericGetValue()
    def setDefaultConfdPersistentDir (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultConfdPersistentDir (self):
        self._genericCommitDefault()

    def _refreshConfdVolatileDir (self):
        self._genericUpdateField()
    def getConfdVolatileDir (self):
        return self._genericGetValue()
    def setDefaultConfdVolatileDir (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultConfdVolatileDir (self):
        self._genericCommitDefault()

    def refreshFromBlinky(self):
        self.clearCachedData()
        self._refreshConfdPersistentDir()
        self._refreshConfdVolatileDir()

    def commitAllDefaults (self):
        self._commitDefaultConfdPersistentDir()
        self._commitDefaultConfdVolatileDir()


