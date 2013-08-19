


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from disk_maapi_base_gen import DiskMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.status.status_maapi_gen import BlinkyStatusMaapi
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.raid_array_maapi_gen import BlinkyRaidArrayMaapi
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.alarms.alarms_maapi_gen import BlinkyAlarmsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.file_system_maapi_gen import BlinkyFileSystemMaapi
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.physical_maapi_gen import BlinkyPhysicalMaapi

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskTypesType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskFunctionalTypesType


class BlinkyDiskMaapi(DiskMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-disk")
        self.domain = None

        
        self.statusObj = None
        
        self.systemDefaultsObj = None
        
        self.raidArrayObj = None
        
        self.alarmsObj = None
        
        self.fileSystemObj = None
        
        self.physicalObj = None
        

        
        self.diskTypeRequested = False
        self.diskType = None
        self.diskTypeSet = False
        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.functionalTypeRequested = False
        self.functionalType = None
        self.functionalTypeSet = False
        
        self.storageModuleRequested = False
        self.storageModule = None
        self.storageModuleSet = False
        
        self.tmpForceInitRequested = False
        self.tmpForceInit = None
        self.tmpForceInitSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDiskType(True)
        
        self.requestName(True)
        
        self.requestEnabled(True)
        
        self.requestFunctionalType(True)
        
        self.requestStorageModule(True)
        
        self.requestTmpForceInit(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        
        if not self.raidArrayObj:
            self.raidArrayObj = self.newRaidArray()
            self.raidArrayObj.requestConfigAndOper()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.requestConfigAndOper()
        
        if not self.fileSystemObj:
            self.fileSystemObj = self.newFileSystem()
            self.fileSystemObj.requestConfigAndOper()
        
        if not self.physicalObj:
            self.physicalObj = self.newPhysical()
            self.physicalObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDiskType(True)
        
        self.requestName(True)
        
        self.requestEnabled(True)
        
        self.requestFunctionalType(True)
        
        self.requestStorageModule(True)
        
        self.requestTmpForceInit(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        
        if not self.raidArrayObj:
            self.raidArrayObj = self.newRaidArray()
            self.raidArrayObj.requestConfig()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.requestConfig()
        
        if not self.fileSystemObj:
            self.fileSystemObj = self.newFileSystem()
            self.fileSystemObj.requestConfig()
        
        if not self.physicalObj:
            self.physicalObj = self.newPhysical()
            self.physicalObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDiskType(False)
        
        self.requestName(False)
        
        self.requestEnabled(False)
        
        self.requestFunctionalType(False)
        
        self.requestStorageModule(False)
        
        self.requestTmpForceInit(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        
        if not self.raidArrayObj:
            self.raidArrayObj = self.newRaidArray()
            self.raidArrayObj.requestOper()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.requestOper()
        
        if not self.fileSystemObj:
            self.fileSystemObj = self.newFileSystem()
            self.fileSystemObj.requestOper()
        
        if not self.physicalObj:
            self.physicalObj = self.newPhysical()
            self.physicalObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDiskType(False)
        
        self.requestName(False)
        
        self.requestEnabled(False)
        
        self.requestFunctionalType(False)
        
        self.requestStorageModule(False)
        
        self.requestTmpForceInit(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        
        if not self.raidArrayObj:
            self.raidArrayObj = self.newRaidArray()
            self.raidArrayObj.clearAllRequested()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.clearAllRequested()
        
        if not self.fileSystemObj:
            self.fileSystemObj = self.newFileSystem()
            self.fileSystemObj.clearAllRequested()
        
        if not self.physicalObj:
            self.physicalObj = self.newPhysical()
            self.physicalObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setDiskType(None)
        self.diskTypeSet = False
        
        self.setName(None)
        self.nameSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setFunctionalType(None)
        self.functionalTypeSet = False
        
        self.setStorageModule(None)
        self.storageModuleSet = False
        
        self.setTmpForceInit(None)
        self.tmpForceInitSet = False
        
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        
        if self.raidArrayObj:
            self.raidArrayObj.clearAllSet()
        
        if self.alarmsObj:
            self.alarmsObj.clearAllSet()
        
        if self.fileSystemObj:
            self.fileSystemObj.clearAllSet()
        
        if self.physicalObj:
            self.physicalObj.clearAllSet()
        

    def write (self
              , disk
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(disk, trxContext)

    def read (self
              , disk
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(disk, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , disk
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(disk, 
                                  True,
                                  trxContext)

    def newStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-status').debug3Func(): logFunc('called.')
        status = BlinkyStatusMaapi(self._log)
        status.init(self.domain)
        return status

    def setStatusObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. obj=%s', obj)
        self.statusObj = obj

    def getStatusObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        return self.statusObj

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        if self.statusObj:
            return True
        return False

    def newSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-systemdefaults').debug3Func(): logFunc('called.')
        systemDefaults = BlinkySystemDefaultsMaapi(self._log)
        systemDefaults.init(self.domain)
        return systemDefaults

    def setSystemDefaultsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemdefaults').debug3Func(): logFunc('called. obj=%s', obj)
        self.systemDefaultsObj = obj

    def getSystemDefaultsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        return self.systemDefaultsObj

    def hasSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        if self.systemDefaultsObj:
            return True
        return False

    def newRaidArray (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-raidarray').debug3Func(): logFunc('called.')
        raidArray = BlinkyRaidArrayMaapi(self._log)
        raidArray.init(self.domain)
        return raidArray

    def setRaidArrayObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-raidarray').debug3Func(): logFunc('called. obj=%s', obj)
        self.raidArrayObj = obj

    def getRaidArrayObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-raidarray').debug3Func(): logFunc('called. self.raidArrayObj=%s', self.raidArrayObj)
        return self.raidArrayObj

    def hasRaidArray (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-raidarray').debug3Func(): logFunc('called. self.raidArrayObj=%s', self.raidArrayObj)
        if self.raidArrayObj:
            return True
        return False

    def newAlarms (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-alarms').debug3Func(): logFunc('called.')
        alarms = BlinkyAlarmsMaapi(self._log)
        alarms.init(self.domain)
        return alarms

    def setAlarmsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-alarms').debug3Func(): logFunc('called. obj=%s', obj)
        self.alarmsObj = obj

    def getAlarmsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-alarms').debug3Func(): logFunc('called. self.alarmsObj=%s', self.alarmsObj)
        return self.alarmsObj

    def hasAlarms (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-alarms').debug3Func(): logFunc('called. self.alarmsObj=%s', self.alarmsObj)
        if self.alarmsObj:
            return True
        return False

    def newFileSystem (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-filesystem').debug3Func(): logFunc('called.')
        fileSystem = BlinkyFileSystemMaapi(self._log)
        fileSystem.init(self.domain)
        return fileSystem

    def setFileSystemObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-filesystem').debug3Func(): logFunc('called. obj=%s', obj)
        self.fileSystemObj = obj

    def getFileSystemObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-filesystem').debug3Func(): logFunc('called. self.fileSystemObj=%s', self.fileSystemObj)
        return self.fileSystemObj

    def hasFileSystem (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-filesystem').debug3Func(): logFunc('called. self.fileSystemObj=%s', self.fileSystemObj)
        if self.fileSystemObj:
            return True
        return False

    def newPhysical (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-physical').debug3Func(): logFunc('called.')
        physical = BlinkyPhysicalMaapi(self._log)
        physical.init(self.domain)
        return physical

    def setPhysicalObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-physical').debug3Func(): logFunc('called. obj=%s', obj)
        self.physicalObj = obj

    def getPhysicalObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-physical').debug3Func(): logFunc('called. self.physicalObj=%s', self.physicalObj)
        return self.physicalObj

    def hasPhysical (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-physical').debug3Func(): logFunc('called. self.physicalObj=%s', self.physicalObj)
        if self.physicalObj:
            return True
        return False



    def requestDiskType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-disktype').debug3Func(): logFunc('called. requested=%s', requested)
        self.diskTypeRequested = requested
        self.diskTypeSet = False

    def isDiskTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-disktype-requested').debug3Func(): logFunc('called. requested=%s', self.diskTypeRequested)
        return self.diskTypeRequested

    def getDiskType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-disktype').debug3Func(): logFunc('called. self.diskTypeSet=%s, self.diskType=%s', self.diskTypeSet, self.diskType)
        if self.diskTypeSet:
            return self.diskType
        return None

    def hasDiskType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-disktype').debug3Func(): logFunc('called. self.diskTypeSet=%s, self.diskType=%s', self.diskTypeSet, self.diskType)
        if self.diskTypeSet:
            return True
        return False

    def setDiskType (self, diskType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-disktype').debug3Func(): logFunc('called. diskType=%s, old=%s', diskType, self.diskType)
        self.diskTypeSet = True
        self.diskType = diskType

    def requestName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-name').debug3Func(): logFunc('called. requested=%s', requested)
        self.nameRequested = requested
        self.nameSet = False

    def isNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-name-requested').debug3Func(): logFunc('called. requested=%s', self.nameRequested)
        return self.nameRequested

    def getName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return self.name
        return None

    def hasName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return True
        return False

    def setName (self, name):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-name').debug3Func(): logFunc('called. name=%s, old=%s', name, self.name)
        self.nameSet = True
        self.name = name

    def requestEnabled (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-enabled').debug3Func(): logFunc('called. requested=%s', requested)
        self.enabledRequested = requested
        self.enabledSet = False

    def isEnabledRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-enabled-requested').debug3Func(): logFunc('called. requested=%s', self.enabledRequested)
        return self.enabledRequested

    def getEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return self.enabled
        return None

    def hasEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return True
        return False

    def setEnabled (self, enabled):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-enabled').debug3Func(): logFunc('called. enabled=%s, old=%s', enabled, self.enabled)
        self.enabledSet = True
        self.enabled = enabled

    def requestFunctionalType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-functionaltype').debug3Func(): logFunc('called. requested=%s', requested)
        self.functionalTypeRequested = requested
        self.functionalTypeSet = False

    def isFunctionalTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-functionaltype-requested').debug3Func(): logFunc('called. requested=%s', self.functionalTypeRequested)
        return self.functionalTypeRequested

    def getFunctionalType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-functionaltype').debug3Func(): logFunc('called. self.functionalTypeSet=%s, self.functionalType=%s', self.functionalTypeSet, self.functionalType)
        if self.functionalTypeSet:
            return self.functionalType
        return None

    def hasFunctionalType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-functionaltype').debug3Func(): logFunc('called. self.functionalTypeSet=%s, self.functionalType=%s', self.functionalTypeSet, self.functionalType)
        if self.functionalTypeSet:
            return True
        return False

    def setFunctionalType (self, functionalType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-functionaltype').debug3Func(): logFunc('called. functionalType=%s, old=%s', functionalType, self.functionalType)
        self.functionalTypeSet = True
        self.functionalType = functionalType

    def requestStorageModule (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-storagemodule').debug3Func(): logFunc('called. requested=%s', requested)
        self.storageModuleRequested = requested
        self.storageModuleSet = False

    def isStorageModuleRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-storagemodule-requested').debug3Func(): logFunc('called. requested=%s', self.storageModuleRequested)
        return self.storageModuleRequested

    def getStorageModule (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-storagemodule').debug3Func(): logFunc('called. self.storageModuleSet=%s, self.storageModule=%s', self.storageModuleSet, self.storageModule)
        if self.storageModuleSet:
            return self.storageModule
        return None

    def hasStorageModule (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-storagemodule').debug3Func(): logFunc('called. self.storageModuleSet=%s, self.storageModule=%s', self.storageModuleSet, self.storageModule)
        if self.storageModuleSet:
            return True
        return False

    def setStorageModule (self, storageModule):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-storagemodule').debug3Func(): logFunc('called. storageModule=%s, old=%s', storageModule, self.storageModule)
        self.storageModuleSet = True
        self.storageModule = storageModule

    def requestTmpForceInit (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-tmpforceinit').debug3Func(): logFunc('called. requested=%s', requested)
        self.tmpForceInitRequested = requested
        self.tmpForceInitSet = False

    def isTmpForceInitRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-tmpforceinit-requested').debug3Func(): logFunc('called. requested=%s', self.tmpForceInitRequested)
        return self.tmpForceInitRequested

    def getTmpForceInit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-tmpforceinit').debug3Func(): logFunc('called. self.tmpForceInitSet=%s, self.tmpForceInit=%s', self.tmpForceInitSet, self.tmpForceInit)
        if self.tmpForceInitSet:
            return self.tmpForceInit
        return None

    def hasTmpForceInit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-tmpforceinit').debug3Func(): logFunc('called. self.tmpForceInitSet=%s, self.tmpForceInit=%s', self.tmpForceInitSet, self.tmpForceInit)
        if self.tmpForceInitSet:
            return True
        return False

    def setTmpForceInit (self, tmpForceInit):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-tmpforceinit').debug3Func(): logFunc('called. tmpForceInit=%s, old=%s', tmpForceInit, self.tmpForceInit)
        self.tmpForceInitSet = True
        self.tmpForceInit = tmpForceInit


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        
        if self.raidArrayObj:
            self.raidArrayObj._clearAllReadData()
        
        if self.alarmsObj:
            self.alarmsObj._clearAllReadData()
        
        if self.fileSystemObj:
            self.fileSystemObj._clearAllReadData()
        
        if self.physicalObj:
            self.physicalObj._clearAllReadData()
        

        
        self.diskType = 0
        self.diskTypeSet = False
        
        self.name = 0
        self.nameSet = False
        
        self.enabled = 0
        self.enabledSet = False
        
        self.functionalType = 0
        self.functionalTypeSet = False
        
        self.storageModule = 0
        self.storageModuleSet = False
        
        self.tmpForceInit = 0
        self.tmpForceInitSet = False
        

    def _getSelfKeyPath (self, disk
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(disk);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("disk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("storage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", "qt-strg"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        disk, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(disk, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(disk, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       disk, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(disk, 
                                       
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               disk, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.statusObj:
            res = self.statusObj._collectItemsToDelete(disk, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-failed').errorFunc(): logFunc('statusObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(disk, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.raidArrayObj:
            res = self.raidArrayObj._collectItemsToDelete(disk, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-raid-array-failed').errorFunc(): logFunc('raidArrayObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.alarmsObj:
            res = self.alarmsObj._collectItemsToDelete(disk, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-alarms-failed').errorFunc(): logFunc('alarmsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.fileSystemObj:
            res = self.fileSystemObj._collectItemsToDelete(disk, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-file-system-failed').errorFunc(): logFunc('fileSystemObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.physicalObj:
            res = self.physicalObj._collectItemsToDelete(disk, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-physical-failed').errorFunc(): logFunc('physicalObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasDiskType():
            valDiskType = Value()
            if self.diskType is not None:
                valDiskType.setEnum(self.diskType.getValue())
            else:
                valDiskType.setEmpty()
            tagValueList.push(("disk-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valDiskType)
        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valName)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valEnabled)
        
        if self.hasFunctionalType():
            valFunctionalType = Value()
            if self.functionalType is not None:
                valFunctionalType.setEnum(self.functionalType.getValue())
            else:
                valFunctionalType.setEmpty()
            tagValueList.push(("functional-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valFunctionalType)
        
        if self.hasStorageModule():
            valStorageModule = Value()
            if self.storageModule is not None:
                valStorageModule.setString(self.storageModule)
            else:
                valStorageModule.setEmpty()
            tagValueList.push(("storage-module", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valStorageModule)
        
        if self.hasTmpForceInit():
            valTmpForceInit = Value()
            if self.tmpForceInit is not None:
                valTmpForceInit.setBool(self.tmpForceInit)
            else:
                valTmpForceInit.setEmpty()
            tagValueList.push(("tmp-force-init", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valTmpForceInit)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.raidArrayObj:
            valBegin = Value()
            (tag, ns, prefix) = ("raid-array" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.raidArrayObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-raid-array-failed').errorFunc(): logFunc('raidArrayObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.alarmsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("alarms" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.alarmsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-alarms-failed').errorFunc(): logFunc('alarmsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.fileSystemObj:
            valBegin = Value()
            (tag, ns, prefix) = ("file-system" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.fileSystemObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-file-system-failed').errorFunc(): logFunc('fileSystemObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.physicalObj:
            valBegin = Value()
            (tag, ns, prefix) = ("physical" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.physicalObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-physical-failed').errorFunc(): logFunc('physicalObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isDiskTypeRequested():
            valDiskType = Value()
            valDiskType.setEmpty()
            tagValueList.push(("disk-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valDiskType)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valName)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valEnabled)
        
        if self.isFunctionalTypeRequested():
            valFunctionalType = Value()
            valFunctionalType.setEmpty()
            tagValueList.push(("functional-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valFunctionalType)
        
        if self.isStorageModuleRequested():
            valStorageModule = Value()
            valStorageModule.setEmpty()
            tagValueList.push(("storage-module", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valStorageModule)
        
        if self.isTmpForceInitRequested():
            valTmpForceInit = Value()
            valTmpForceInit.setEmpty()
            tagValueList.push(("tmp-force-init", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valTmpForceInit)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.raidArrayObj:
            valBegin = Value()
            (tag, ns, prefix) = ("raid-array" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.raidArrayObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-raid-array-failed').errorFunc(): logFunc('raidArrayObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.alarmsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("alarms" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.alarmsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-alarms-failed').errorFunc(): logFunc('alarmsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.fileSystemObj:
            valBegin = Value()
            (tag, ns, prefix) = ("file-system" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.fileSystemObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-file-system-failed').errorFunc(): logFunc('fileSystemObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.physicalObj:
            valBegin = Value()
            (tag, ns, prefix) = ("physical" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.physicalObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-physical-failed').errorFunc(): logFunc('physicalObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isDiskTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "disk-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-disktype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "diskType", "disk-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-disk-type-bad-value').infoFunc(): logFunc('diskType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDiskType(tempVar)
            for logFunc in self._log('read-tag-values-disk-type').debug3Func(): logFunc('read diskType. diskType=%s, tempValue=%s', self.diskType, tempValue.getType())
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-name-bad-value').infoFunc(): logFunc('name not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setName(tempVar)
            for logFunc in self._log('read-tag-values-name').debug3Func(): logFunc('read name. name=%s, tempValue=%s', self.name, tempValue.getType())
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-enabled-bad-value').infoFunc(): logFunc('enabled not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEnabled(tempVar)
            for logFunc in self._log('read-tag-values-enabled').debug3Func(): logFunc('read enabled. enabled=%s, tempValue=%s', self.enabled, tempValue.getType())
        
        if self.isFunctionalTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "functional-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-functionaltype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "functionalType", "functional-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-functional-type-bad-value').infoFunc(): logFunc('functionalType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFunctionalType(tempVar)
            for logFunc in self._log('read-tag-values-functional-type').debug3Func(): logFunc('read functionalType. functionalType=%s, tempValue=%s', self.functionalType, tempValue.getType())
        
        if self.isStorageModuleRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "storage-module") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-storagemodule').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "storageModule", "storage-module", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-storage-module-bad-value').infoFunc(): logFunc('storageModule not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStorageModule(tempVar)
            for logFunc in self._log('read-tag-values-storage-module').debug3Func(): logFunc('read storageModule. storageModule=%s, tempValue=%s', self.storageModule, tempValue.getType())
        
        if self.isTmpForceInitRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tmp-force-init") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-tmpforceinit').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "tmpForceInit", "tmp-force-init", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tmp-force-init-bad-value').infoFunc(): logFunc('tmpForceInit not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTmpForceInit(tempVar)
            for logFunc in self._log('read-tag-values-tmp-force-init').debug3Func(): logFunc('read tmpForceInit. tmpForceInit=%s, tempValue=%s', self.tmpForceInit, tempValue.getType())
        

        
        if self.statusObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.statusObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-status-failed').errorFunc(): logFunc('statusObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.systemDefaultsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.raidArrayObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "raid-array") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "raid-array", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.raidArrayObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-raid-array-failed').errorFunc(): logFunc('raidArrayObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "raid-array") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "raid-array", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.alarmsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "alarms") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.alarmsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-alarms-failed').errorFunc(): logFunc('alarmsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "alarms") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.fileSystemObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "file-system") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "file-system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.fileSystemObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-file-system-failed').errorFunc(): logFunc('fileSystemObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "file-system") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "file-system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.physicalObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "physical") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "physical", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.physicalObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-physical-failed').errorFunc(): logFunc('physicalObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "physical") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "physical", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "disk", 
        "namespace": "disk", 
        "className": "DiskMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.disk_maapi_gen import DiskMaapi", 
        "baseClassName": "DiskMaapiBase", 
        "baseModule": "disk_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "isCurrent": true, 
            "yangName": "disk", 
            "namespace": "disk", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "keyLeaf": {
                "varName": "disk", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "disk"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "raidArray", 
            "yangName": "raid-array", 
            "className": "BlinkyRaidArrayMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.raid_array_maapi_gen import BlinkyRaidArrayMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "alarms", 
            "yangName": "alarms", 
            "className": "BlinkyAlarmsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.alarms.alarms_maapi_gen import BlinkyAlarmsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "fileSystem", 
            "yangName": "file-system", 
            "className": "BlinkyFileSystemMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.file_system_maapi_gen import BlinkyFileSystemMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "physical", 
            "yangName": "physical", 
            "className": "BlinkyPhysicalMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.physical_maapi_gen import BlinkyPhysicalMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "diskType", 
            "yangName": "disk-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "functionalType", 
            "yangName": "functional-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "storageModule", 
            "yangName": "storage-module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "tmpForceInit", 
            "yangName": "tmp-force-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_storage_disk"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "diskType", 
            "yangName": "disk-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "functionalType", 
            "yangName": "functional-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "storageModule", 
            "yangName": "storage-module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "tmpForceInit", 
            "yangName": "tmp-force-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


