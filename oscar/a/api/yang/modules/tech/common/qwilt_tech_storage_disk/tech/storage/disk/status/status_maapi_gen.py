


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

from status_maapi_base_gen import StatusMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskOperationalStatusType


class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.osDeviceRequested = False
        self.osDevice = None
        self.osDeviceSet = False
        
        self.oprtationalStatusRequested = False
        self.oprtationalStatus = None
        self.oprtationalStatusSet = False
        
        self.operationalStatusReasonRequested = False
        self.operationalStatusReason = None
        self.operationalStatusReasonSet = False
        
        self.sizeRequested = False
        self.size = None
        self.sizeSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOsDevice(True)
        
        self.requestOprtationalStatus(True)
        
        self.requestOperationalStatusReason(True)
        
        self.requestSize(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOsDevice(False)
        
        self.requestOprtationalStatus(False)
        
        self.requestOperationalStatusReason(False)
        
        self.requestSize(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOsDevice(True)
        
        self.requestOprtationalStatus(True)
        
        self.requestOperationalStatusReason(True)
        
        self.requestSize(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOsDevice(False)
        
        self.requestOprtationalStatus(False)
        
        self.requestOperationalStatusReason(False)
        
        self.requestSize(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

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

    def requestOprtationalStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oprtationalstatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.oprtationalStatusRequested = requested
        self.oprtationalStatusSet = False

    def isOprtationalStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-oprtationalstatus-requested').debug3Func(): logFunc('called. requested=%s', self.oprtationalStatusRequested)
        return self.oprtationalStatusRequested

    def getOprtationalStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-oprtationalstatus').debug3Func(): logFunc('called. self.oprtationalStatusSet=%s, self.oprtationalStatus=%s', self.oprtationalStatusSet, self.oprtationalStatus)
        if self.oprtationalStatusSet:
            return self.oprtationalStatus
        return None

    def hasOprtationalStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-oprtationalstatus').debug3Func(): logFunc('called. self.oprtationalStatusSet=%s, self.oprtationalStatus=%s', self.oprtationalStatusSet, self.oprtationalStatus)
        if self.oprtationalStatusSet:
            return True
        return False

    def setOprtationalStatus (self, oprtationalStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-oprtationalstatus').debug3Func(): logFunc('called. oprtationalStatus=%s, old=%s', oprtationalStatus, self.oprtationalStatus)
        self.oprtationalStatusSet = True
        self.oprtationalStatus = oprtationalStatus

    def requestOperationalStatusReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-operationalstatusreason').debug3Func(): logFunc('called. requested=%s', requested)
        self.operationalStatusReasonRequested = requested
        self.operationalStatusReasonSet = False

    def isOperationalStatusReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-operationalstatusreason-requested').debug3Func(): logFunc('called. requested=%s', self.operationalStatusReasonRequested)
        return self.operationalStatusReasonRequested

    def getOperationalStatusReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-operationalstatusreason').debug3Func(): logFunc('called. self.operationalStatusReasonSet=%s, self.operationalStatusReason=%s', self.operationalStatusReasonSet, self.operationalStatusReason)
        if self.operationalStatusReasonSet:
            return self.operationalStatusReason
        return None

    def hasOperationalStatusReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-operationalstatusreason').debug3Func(): logFunc('called. self.operationalStatusReasonSet=%s, self.operationalStatusReason=%s', self.operationalStatusReasonSet, self.operationalStatusReason)
        if self.operationalStatusReasonSet:
            return True
        return False

    def setOperationalStatusReason (self, operationalStatusReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-operationalstatusreason').debug3Func(): logFunc('called. operationalStatusReason=%s, old=%s', operationalStatusReason, self.operationalStatusReason)
        self.operationalStatusReasonSet = True
        self.operationalStatusReason = operationalStatusReason

    def requestSize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-size').debug3Func(): logFunc('called. requested=%s', requested)
        self.sizeRequested = requested
        self.sizeSet = False

    def isSizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-size-requested').debug3Func(): logFunc('called. requested=%s', self.sizeRequested)
        return self.sizeRequested

    def getSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-size').debug3Func(): logFunc('called. self.sizeSet=%s, self.size=%s', self.sizeSet, self.size)
        if self.sizeSet:
            return self.size
        return None

    def hasSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-size').debug3Func(): logFunc('called. self.sizeSet=%s, self.size=%s', self.sizeSet, self.size)
        if self.sizeSet:
            return True
        return False

    def setSize (self, size):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-size').debug3Func(): logFunc('called. size=%s, old=%s', size, self.size)
        self.sizeSet = True
        self.size = size


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.osDevice = 0
        self.osDeviceSet = False
        
        self.oprtationalStatus = 0
        self.oprtationalStatusSet = False
        
        self.operationalStatusReason = 0
        self.operationalStatusReasonSet = False
        
        self.size = 0
        self.sizeSet = False
        

    def _getSelfKeyPath (self, disk
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
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

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isOsDeviceRequested():
            valOsDevice = Value()
            valOsDevice.setEmpty()
            tagValueList.push(("os-device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valOsDevice)
        
        if self.isOprtationalStatusRequested():
            valOprtationalStatus = Value()
            valOprtationalStatus.setEmpty()
            tagValueList.push(("oprtational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valOprtationalStatus)
        
        if self.isOperationalStatusReasonRequested():
            valOperationalStatusReason = Value()
            valOperationalStatusReason.setEmpty()
            tagValueList.push(("operational-status-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valOperationalStatusReason)
        
        if self.isSizeRequested():
            valSize = Value()
            valSize.setEmpty()
            tagValueList.push(("size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valSize)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
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
        
        if self.isOprtationalStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "oprtational-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-oprtationalstatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "oprtationalStatus", "oprtational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-oprtational-status-bad-value').infoFunc(): logFunc('oprtationalStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOprtationalStatus(tempVar)
            for logFunc in self._log('read-tag-values-oprtational-status').debug3Func(): logFunc('read oprtationalStatus. oprtationalStatus=%s, tempValue=%s', self.oprtationalStatus, tempValue.getType())
        
        if self.isOperationalStatusReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "operational-status-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-operationalstatusreason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "operationalStatusReason", "operational-status-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-operational-status-reason-bad-value').infoFunc(): logFunc('operationalStatusReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOperationalStatusReason(tempVar)
            for logFunc in self._log('read-tag-values-operational-status-reason').debug3Func(): logFunc('read operationalStatusReason. operationalStatusReason=%s, tempValue=%s', self.operationalStatusReason, tempValue.getType())
        
        if self.isSizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-size').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "size", "size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-size-bad-value').infoFunc(): logFunc('size not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSize(tempVar)
            for logFunc in self._log('read-tag-values-size').debug3Func(): logFunc('read size. size=%s, tempValue=%s', self.size, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
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
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "osDevice", 
            "yangName": "os-device", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "oprtationalStatus", 
            "yangName": "oprtational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "size", 
            "yangName": "size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "osDevice", 
            "yangName": "os-device", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "oprtationalStatus", 
            "yangName": "oprtational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "size", 
            "yangName": "size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


