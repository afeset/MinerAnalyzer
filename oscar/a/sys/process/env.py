#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import os
import a.infra.format.json
import a.sys.blinky.pearl

if  __package__ is None:
    G_NAME_MODULE_SYS_PROCESS = "unknown"
    G_NAME_GROUP_SYS_PROCESS_ENV = "unknown"
else:
    from . import G_NAME_MODULE_SYS_PROCESS 
    from . import G_NAME_GROUP_SYS_PROCESS_ENV 


class ModuleCentralBlinkyData:
    BLINKY_MODULE_KEY_PATH = os.path.join("sys", "process", "env")

    ACTUAL_SUFFIX = "-actual"

    CONST_DIR       = "const-dir"
    DATA_DIR        = "data-dir"
    VAR_DIR         = "var-dir"    
    RAM_DIR         = "ram-dir" 

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_SYS_PROCESS, G_NAME_GROUP_SYS_PROCESS_ENV)
        self._moduleCentralBlinkyDataEngine = a.sys.blinky.pearl.BlinkyJsonDataEngine(self._log)

    def initBlinky (self, blinky):
        self._blinky = blinky
        self._specificKeyPathBlinky = self._blinky.keyPath(self.BLINKY_MODULE_KEY_PATH)
        self._moduleCentralBlinkyDataEngine.initBlinky(self._specificKeyPathBlinky)

    def removeFromBlinky (self):
        self._specificKeyPathBlinky.remove()

    def configuredToActual (self):
        self._moduleCentralBlinkyDataEngine.writeOperationalVolatileField(self.CONST_DIR+self.ACTUAL_SUFFIX, self.readConstDir())
        self._moduleCentralBlinkyDataEngine.writeOperationalVolatileField(self.DATA_DIR+self.ACTUAL_SUFFIX, self.readDataDir())
        self._moduleCentralBlinkyDataEngine.writeOperationalVolatileField(self.VAR_DIR+self.ACTUAL_SUFFIX, self.readVarDir())
        self._moduleCentralBlinkyDataEngine.writeOperationalVolatileField(self.RAM_DIR+self.ACTUAL_SUFFIX, self.readRamDir())

    def isDefinedConstDir (self):
        fieldName = self.CONST_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultConstDir (self):
        fieldName = self.CONST_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readConstDir (self):
        fieldName = self.CONST_DIR
        return self._moduleCentralBlinkyDataEngine.readConfigurationField(fieldName)
    def writeConstDirDefault (self, data):
        fieldName = self.CONST_DIR
        self._moduleCentralBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)

    def isDefinedDataDir (self):
        fieldName = self.DATA_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultDataDir (self):
        fieldName = self.DATA_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readDataDir (self):
        fieldName = self.DATA_DIR
        return self._moduleCentralBlinkyDataEngine.readConfigurationField(fieldName)
    def writeDataDirDefault (self, data):
        fieldName = self.DATA_DIR
        self._moduleCentralBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)

    def isDefinedVarDir (self):
        fieldName = self.VAR_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultVarDir (self):
        fieldName = self.VAR_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readVarDir (self):
        fieldName = self.VAR_DIR
        return self._moduleCentralBlinkyDataEngine.readConfigurationField(fieldName)
    def writeVarDirDefault (self, data):
        fieldName = self.VAR_DIR
        self._moduleCentralBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)

    def isDefinedRamDir (self):
        fieldName = self.RAM_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultRamDir (self):
        fieldName = self.RAM_DIR
        return self._moduleCentralBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readRamDir (self):
        fieldName = self.RAM_DIR
        return self._moduleCentralBlinkyDataEngine.readConfigurationField(fieldName)
    def writeRamDirDefault (self, data):
        fieldName = self.RAM_DIR
        self._moduleCentralBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
        

class ModuleCentralBlinkyInitCfgWriter(a.sys.blinky.pearl.BlinkyInitCfgWriter):
    def __init__(self,logger):
        a.sys.blinky.pearl.BlinkyInitCfgWriter.__init__(self,logger)

    def _refreshConstDir (self):
        self._genericUpdateField()# as processSimple does not hold this data
    def getConstDir (self):
        return self._genericGetValue()
    def setDefaultConstDir (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultConstDir (self):
        self._genericCommitDefault()

    def _refreshDataDir (self):
        self._genericUpdateField()# as processSimple does not hold this data
    def getDataDir (self):
        return self._genericGetValue()
    def setDefaultDataDir (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultDataDir (self):
        self._genericCommitDefault()
    
    def _refreshVarDir (self):
        self._genericUpdateField()# as processSimple does not hold this data
    def getVarDir (self):
        return self._genericGetValue()
    def setDefaultVarDir (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultVarDir (self):
        self._genericCommitDefault()

    def _refreshRamDir (self):
        self._genericUpdateField()# as processSimple does not hold this data
    def getRamDir (self):
        return self._genericGetValue()
    def setDefaultRamDir (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultRamDir (self):
        self._genericCommitDefault()


    def refreshFromBlinky(self):
        self.clearCachedData()
        self._refreshConstDir()
        self._refreshDataDir()
        self._refreshVarDir()
        self._refreshRamDir()

    def commitAllDefaults (self):
        self._commitDefaultConstDir()
        self._commitDefaultDataDir()
        self._commitDefaultVarDir()
        self._commitDefaultRamDir()

