


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

from timeouts_maapi_base_gen import TimeoutsMaapiBase




class BlinkyTimeoutsMaapi(TimeoutsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-timeouts")
        self.domain = None

        

        
        self.activateRequested = False
        self.activate = None
        self.activateSet = False
        
        self.getStatusRequested = False
        self.getStatus = None
        self.getStatusSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestActivate(True)
        
        self.requestGetStatus(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestActivate(True)
        
        self.requestGetStatus(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestActivate(False)
        
        self.requestGetStatus(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestActivate(False)
        
        self.requestGetStatus(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setActivate(None)
        self.activateSet = False
        
        self.setGetStatus(None)
        self.getStatusSet = False
        
        

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



    def requestActivate (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-activate').debug3Func(): logFunc('called. requested=%s', requested)
        self.activateRequested = requested
        self.activateSet = False

    def isActivateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-activate-requested').debug3Func(): logFunc('called. requested=%s', self.activateRequested)
        return self.activateRequested

    def getActivate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-activate').debug3Func(): logFunc('called. self.activateSet=%s, self.activate=%s', self.activateSet, self.activate)
        if self.activateSet:
            return self.activate
        return None

    def hasActivate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-activate').debug3Func(): logFunc('called. self.activateSet=%s, self.activate=%s', self.activateSet, self.activate)
        if self.activateSet:
            return True
        return False

    def setActivate (self, activate):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-activate').debug3Func(): logFunc('called. activate=%s, old=%s', activate, self.activate)
        self.activateSet = True
        self.activate = activate

    def requestGetStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-getstatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.getStatusRequested = requested
        self.getStatusSet = False

    def isGetStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-getstatus-requested').debug3Func(): logFunc('called. requested=%s', self.getStatusRequested)
        return self.getStatusRequested

    def getGetStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-getstatus').debug3Func(): logFunc('called. self.getStatusSet=%s, self.getStatus=%s', self.getStatusSet, self.getStatus)
        if self.getStatusSet:
            return self.getStatus
        return None

    def hasGetStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-getstatus').debug3Func(): logFunc('called. self.getStatusSet=%s, self.getStatus=%s', self.getStatusSet, self.getStatus)
        if self.getStatusSet:
            return True
        return False

    def setGetStatus (self, getStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-getstatus').debug3Func(): logFunc('called. getStatus=%s, old=%s', getStatus, self.getStatus)
        self.getStatusSet = True
        self.getStatus = getStatus


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.activate = 0
        self.activateSet = False
        
        self.getStatus = 0
        self.getStatusSet = False
        

    def _getSelfKeyPath (self, disk
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("file-system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
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

        
        if self.hasActivate():
            valActivate = Value()
            if self.activate is not None:
                valActivate.setInt64(self.activate)
            else:
                valActivate.setEmpty()
            tagValueList.push(("activate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valActivate)
        
        if self.hasGetStatus():
            valGetStatus = Value()
            if self.getStatus is not None:
                valGetStatus.setInt64(self.getStatus)
            else:
                valGetStatus.setEmpty()
            tagValueList.push(("get-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valGetStatus)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isActivateRequested():
            valActivate = Value()
            valActivate.setEmpty()
            tagValueList.push(("activate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valActivate)
        
        if self.isGetStatusRequested():
            valGetStatus = Value()
            valGetStatus.setEmpty()
            tagValueList.push(("get-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valGetStatus)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isActivateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "activate") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-activate').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "activate", "activate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-activate-bad-value').infoFunc(): logFunc('activate not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setActivate(tempVar)
            for logFunc in self._log('read-tag-values-activate').debug3Func(): logFunc('read activate. activate=%s, tempValue=%s', self.activate, tempValue.getType())
        
        if self.isGetStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "get-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-getstatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "getStatus", "get-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-get-status-bad-value').infoFunc(): logFunc('getStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setGetStatus(tempVar)
            for logFunc in self._log('read-tag-values-get-status').debug3Func(): logFunc('read getStatus. getStatus=%s, tempValue=%s', self.getStatus, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "timeouts", 
        "namespace": "timeouts", 
        "className": "TimeoutsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.timeouts.timeouts_maapi_gen import TimeoutsMaapi", 
        "baseClassName": "TimeoutsMaapiBase", 
        "baseModule": "timeouts_maapi_base_gen"
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
            "yangName": "file-system", 
            "namespace": "file_system", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "file-system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "timeouts", 
            "namespace": "timeouts", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "timeouts"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activate", 
            "yangName": "activate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "getStatus", 
            "yangName": "get-status", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "activate", 
            "yangName": "activate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "getStatus", 
            "yangName": "get-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


