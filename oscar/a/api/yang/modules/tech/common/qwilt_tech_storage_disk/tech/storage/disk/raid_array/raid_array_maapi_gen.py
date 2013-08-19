


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

from raid_array_maapi_base_gen import RaidArrayMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.status.status_maapi_gen import BlinkyStatusMaapi

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayRaidType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayImplementationType


class BlinkyRaidArrayMaapi(RaidArrayMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-raidArray")
        self.domain = None

        
        self.statusObj = None
        

        
        self.autoInitRequested = False
        self.autoInit = None
        self.autoInitSet = False
        
        self.osDeviceRequested = False
        self.osDevice = None
        self.osDeviceSet = False
        
        self.implementationRequested = False
        self.implementation = None
        self.implementationSet = False
        
        self.raidTypeRequested = False
        self.raidType = None
        self.raidTypeSet = False
        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAutoInit(True)
        
        self.requestOsDevice(True)
        
        self.requestImplementation(True)
        
        self.requestRaidType(True)
        
        self.requestName(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAutoInit(True)
        
        self.requestOsDevice(True)
        
        self.requestImplementation(True)
        
        self.requestRaidType(True)
        
        self.requestName(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAutoInit(False)
        
        self.requestOsDevice(False)
        
        self.requestImplementation(False)
        
        self.requestRaidType(False)
        
        self.requestName(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestAutoInit(False)
        
        self.requestOsDevice(False)
        
        self.requestImplementation(False)
        
        self.requestRaidType(False)
        
        self.requestName(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setAutoInit(None)
        self.autoInitSet = False
        
        self.setOsDevice(None)
        self.osDeviceSet = False
        
        self.setImplementation(None)
        self.implementationSet = False
        
        self.setRaidType(None)
        self.raidTypeSet = False
        
        self.setName(None)
        self.nameSet = False
        
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        

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



    def requestAutoInit (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-autoinit').debug3Func(): logFunc('called. requested=%s', requested)
        self.autoInitRequested = requested
        self.autoInitSet = False

    def isAutoInitRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-autoinit-requested').debug3Func(): logFunc('called. requested=%s', self.autoInitRequested)
        return self.autoInitRequested

    def getAutoInit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-autoinit').debug3Func(): logFunc('called. self.autoInitSet=%s, self.autoInit=%s', self.autoInitSet, self.autoInit)
        if self.autoInitSet:
            return self.autoInit
        return None

    def hasAutoInit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-autoinit').debug3Func(): logFunc('called. self.autoInitSet=%s, self.autoInit=%s', self.autoInitSet, self.autoInit)
        if self.autoInitSet:
            return True
        return False

    def setAutoInit (self, autoInit):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-autoinit').debug3Func(): logFunc('called. autoInit=%s, old=%s', autoInit, self.autoInit)
        self.autoInitSet = True
        self.autoInit = autoInit

    def requestOsDevice (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-osdevice').debug3Func(): logFunc('called. requested=%s', requested)
        self.osDeviceRequested = requested
        self.osDeviceSet = False

    def isOsDeviceRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-osdevice-requested').debug3Func(): logFunc('called. requested=%s', self.osDeviceRequested)
        return self.osDeviceRequested

    def getOsDevice (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-osdevice').debug3Func(): logFunc('called. self.osDeviceSet=%s, self.osDevice=%s', self.osDeviceSet, self.osDevice)
        if self.osDeviceSet:
            return self.osDevice
        return None

    def hasOsDevice (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-osdevice').debug3Func(): logFunc('called. self.osDeviceSet=%s, self.osDevice=%s', self.osDeviceSet, self.osDevice)
        if self.osDeviceSet:
            return True
        return False

    def setOsDevice (self, osDevice):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-osdevice').debug3Func(): logFunc('called. osDevice=%s, old=%s', osDevice, self.osDevice)
        self.osDeviceSet = True
        self.osDevice = osDevice

    def requestImplementation (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-implementation').debug3Func(): logFunc('called. requested=%s', requested)
        self.implementationRequested = requested
        self.implementationSet = False

    def isImplementationRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-implementation-requested').debug3Func(): logFunc('called. requested=%s', self.implementationRequested)
        return self.implementationRequested

    def getImplementation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-implementation').debug3Func(): logFunc('called. self.implementationSet=%s, self.implementation=%s', self.implementationSet, self.implementation)
        if self.implementationSet:
            return self.implementation
        return None

    def hasImplementation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-implementation').debug3Func(): logFunc('called. self.implementationSet=%s, self.implementation=%s', self.implementationSet, self.implementation)
        if self.implementationSet:
            return True
        return False

    def setImplementation (self, implementation):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-implementation').debug3Func(): logFunc('called. implementation=%s, old=%s', implementation, self.implementation)
        self.implementationSet = True
        self.implementation = implementation

    def requestRaidType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-raidtype').debug3Func(): logFunc('called. requested=%s', requested)
        self.raidTypeRequested = requested
        self.raidTypeSet = False

    def isRaidTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-raidtype-requested').debug3Func(): logFunc('called. requested=%s', self.raidTypeRequested)
        return self.raidTypeRequested

    def getRaidType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-raidtype').debug3Func(): logFunc('called. self.raidTypeSet=%s, self.raidType=%s', self.raidTypeSet, self.raidType)
        if self.raidTypeSet:
            return self.raidType
        return None

    def hasRaidType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-raidtype').debug3Func(): logFunc('called. self.raidTypeSet=%s, self.raidType=%s', self.raidTypeSet, self.raidType)
        if self.raidTypeSet:
            return True
        return False

    def setRaidType (self, raidType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-raidtype').debug3Func(): logFunc('called. raidType=%s, old=%s', raidType, self.raidType)
        self.raidTypeSet = True
        self.raidType = raidType

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        

        
        self.autoInit = 0
        self.autoInitSet = False
        
        self.osDevice = 0
        self.osDeviceSet = False
        
        self.implementation = 0
        self.implementationSet = False
        
        self.raidType = 0
        self.raidTypeSet = False
        
        self.name = 0
        self.nameSet = False
        

    def _getSelfKeyPath (self, disk
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("raid-array", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
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
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasAutoInit():
            valAutoInit = Value()
            if self.autoInit is not None:
                valAutoInit.setBool(self.autoInit)
            else:
                valAutoInit.setEmpty()
            tagValueList.push(("auto-init", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valAutoInit)
        
        if self.hasOsDevice():
            valOsDevice = Value()
            if self.osDevice is not None:
                valOsDevice.setString(self.osDevice)
            else:
                valOsDevice.setEmpty()
            tagValueList.push(("os-device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valOsDevice)
        
        if self.hasImplementation():
            valImplementation = Value()
            if self.implementation is not None:
                valImplementation.setEnum(self.implementation.getValue())
            else:
                valImplementation.setEmpty()
            tagValueList.push(("implementation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valImplementation)
        
        if self.hasRaidType():
            valRaidType = Value()
            if self.raidType is not None:
                valRaidType.setEnum(self.raidType.getValue())
            else:
                valRaidType.setEmpty()
            tagValueList.push(("raid-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valRaidType)
        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valName)
        

        
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
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isAutoInitRequested():
            valAutoInit = Value()
            valAutoInit.setEmpty()
            tagValueList.push(("auto-init", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valAutoInit)
        
        if self.isOsDeviceRequested():
            valOsDevice = Value()
            valOsDevice.setEmpty()
            tagValueList.push(("os-device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valOsDevice)
        
        if self.isImplementationRequested():
            valImplementation = Value()
            valImplementation.setEmpty()
            tagValueList.push(("implementation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valImplementation)
        
        if self.isRaidTypeRequested():
            valRaidType = Value()
            valRaidType.setEmpty()
            tagValueList.push(("raid-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valRaidType)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valName)
        

        
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
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isAutoInitRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "auto-init") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-autoinit').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "autoInit", "auto-init", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-auto-init-bad-value').infoFunc(): logFunc('autoInit not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAutoInit(tempVar)
            for logFunc in self._log('read-tag-values-auto-init').debug3Func(): logFunc('read autoInit. autoInit=%s, tempValue=%s', self.autoInit, tempValue.getType())
        
        if self.isOsDeviceRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "os-device") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-osdevice').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "osDevice", "os-device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-os-device-bad-value').infoFunc(): logFunc('osDevice not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOsDevice(tempVar)
            for logFunc in self._log('read-tag-values-os-device').debug3Func(): logFunc('read osDevice. osDevice=%s, tempValue=%s', self.osDevice, tempValue.getType())
        
        if self.isImplementationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "implementation") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-implementation').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "implementation", "implementation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-implementation-bad-value').infoFunc(): logFunc('implementation not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setImplementation(tempVar)
            for logFunc in self._log('read-tag-values-implementation').debug3Func(): logFunc('read implementation. implementation=%s, tempValue=%s', self.implementation, tempValue.getType())
        
        if self.isRaidTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "raid-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-raidtype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "raidType", "raid-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-raid-type-bad-value').infoFunc(): logFunc('raidType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRaidType(tempVar)
            for logFunc in self._log('read-tag-values-raid-type').debug3Func(): logFunc('read raidType. raidType=%s, tempValue=%s', self.raidType, tempValue.getType())
        
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
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "raidArray", 
        "namespace": "raid_array", 
        "className": "RaidArrayMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.raid_array_maapi_gen import RaidArrayMaapi", 
        "baseClassName": "RaidArrayMaapiBase", 
        "baseModule": "raid_array_maapi_base_gen"
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
            "isCurrent": false, 
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
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "raid-array", 
            "namespace": "raid_array", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "raid-array"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.status.status_maapi_gen import BlinkyStatusMaapi", 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "autoInit", 
            "yangName": "auto-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "osDevice", 
            "yangName": "os-device", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "implementation", 
            "yangName": "implementation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "raidType", 
            "yangName": "raid-type", 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "autoInit", 
            "yangName": "auto-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "osDevice", 
            "yangName": "os-device", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "implementation", 
            "yangName": "implementation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "raidType", 
            "yangName": "raid-type", 
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
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


