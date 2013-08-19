


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

from system_defaults_maapi_base_gen import SystemDefaultsMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.system_defaults.timeouts.timeouts_maapi_gen import BlinkyTimeoutsMaapi

from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.qwilt_tech_storage_controller_module_gen import StorageControllerImplementationType


class BlinkySystemDefaultsMaapi(SystemDefaultsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-systemDefaults")
        self.domain = None

        
        self.timeoutsObj = None
        

        
        self.implementationRequested = False
        self.implementation = None
        self.implementationSet = False
        
        self.internalIdRequested = False
        self.internalId = None
        self.internalIdSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestImplementation(True)
        
        self.requestInternalId(True)
        
        
        
        if not self.timeoutsObj:
            self.timeoutsObj = self.newTimeouts()
            self.timeoutsObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestImplementation(True)
        
        self.requestInternalId(True)
        
        
        
        if not self.timeoutsObj:
            self.timeoutsObj = self.newTimeouts()
            self.timeoutsObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestImplementation(False)
        
        self.requestInternalId(False)
        
        
        
        if not self.timeoutsObj:
            self.timeoutsObj = self.newTimeouts()
            self.timeoutsObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestImplementation(False)
        
        self.requestInternalId(False)
        
        
        
        if not self.timeoutsObj:
            self.timeoutsObj = self.newTimeouts()
            self.timeoutsObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setImplementation(None)
        self.implementationSet = False
        
        self.setInternalId(None)
        self.internalIdSet = False
        
        
        if self.timeoutsObj:
            self.timeoutsObj.clearAllSet()
        

    def write (self
              , controller
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(controller, trxContext)

    def read (self
              , controller
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(controller, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , controller
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(controller, 
                                  True,
                                  trxContext)

    def newTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-timeouts').debug3Func(): logFunc('called.')
        timeouts = BlinkyTimeoutsMaapi(self._log)
        timeouts.init(self.domain)
        return timeouts

    def setTimeoutsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-timeouts').debug3Func(): logFunc('called. obj=%s', obj)
        self.timeoutsObj = obj

    def getTimeoutsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-timeouts').debug3Func(): logFunc('called. self.timeoutsObj=%s', self.timeoutsObj)
        return self.timeoutsObj

    def hasTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-timeouts').debug3Func(): logFunc('called. self.timeoutsObj=%s', self.timeoutsObj)
        if self.timeoutsObj:
            return True
        return False



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

    def requestInternalId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-internalid').debug3Func(): logFunc('called. requested=%s', requested)
        self.internalIdRequested = requested
        self.internalIdSet = False

    def isInternalIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-internalid-requested').debug3Func(): logFunc('called. requested=%s', self.internalIdRequested)
        return self.internalIdRequested

    def getInternalId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-internalid').debug3Func(): logFunc('called. self.internalIdSet=%s, self.internalId=%s', self.internalIdSet, self.internalId)
        if self.internalIdSet:
            return self.internalId
        return None

    def hasInternalId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-internalid').debug3Func(): logFunc('called. self.internalIdSet=%s, self.internalId=%s', self.internalIdSet, self.internalId)
        if self.internalIdSet:
            return True
        return False

    def setInternalId (self, internalId):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-internalid').debug3Func(): logFunc('called. internalId=%s, old=%s', internalId, self.internalId)
        self.internalIdSet = True
        self.internalId = internalId


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.timeoutsObj:
            self.timeoutsObj._clearAllReadData()
        

        
        self.implementation = 0
        self.implementationSet = False
        
        self.internalId = 0
        self.internalIdSet = False
        

    def _getSelfKeyPath (self, controller
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(controller);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl"))
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
                        controller, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(controller, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(controller, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       controller, 
                       
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

        keyPath = self._getSelfKeyPath(controller, 
                                       
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
                               controller, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.timeoutsObj:
            res = self.timeoutsObj._collectItemsToDelete(controller, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-timeouts-failed').errorFunc(): logFunc('timeoutsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasImplementation():
            valImplementation = Value()
            if self.implementation is not None:
                valImplementation.setEnum(self.implementation.getValue())
            else:
                valImplementation.setEmpty()
            tagValueList.push(("implementation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valImplementation)
        
        if self.hasInternalId():
            valInternalId = Value()
            if self.internalId is not None:
                valInternalId.setString(self.internalId)
            else:
                valInternalId.setEmpty()
            tagValueList.push(("internal-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valInternalId)
        

        
        if self.timeoutsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("timeouts" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.timeoutsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-timeouts-failed').errorFunc(): logFunc('timeoutsObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isImplementationRequested():
            valImplementation = Value()
            valImplementation.setEmpty()
            tagValueList.push(("implementation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valImplementation)
        
        if self.isInternalIdRequested():
            valInternalId = Value()
            valInternalId.setEmpty()
            tagValueList.push(("internal-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valInternalId)
        

        
        if self.timeoutsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("timeouts" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.timeoutsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-timeouts-failed').errorFunc(): logFunc('timeoutsObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isImplementationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "implementation") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-implementation').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "implementation", "implementation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", tag, ns)
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
        
        if self.isInternalIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "internal-id") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-internalid').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "internalId", "internal-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-internal-id-bad-value').infoFunc(): logFunc('internalId not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInternalId(tempVar)
            for logFunc in self._log('read-tag-values-internal-id').debug3Func(): logFunc('read internalId. internalId=%s, tempValue=%s', self.internalId, tempValue.getType())
        

        
        if self.timeoutsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "timeouts") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.timeoutsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-timeouts-failed').errorFunc(): logFunc('timeoutsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "timeouts") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
        "baseClassName": "SystemDefaultsMaapiBase", 
        "baseModule": "system_defaults_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "isCurrent": false, 
            "yangName": "controller", 
            "namespace": "controller", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "keyLeaf": {
                "varName": "controller", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "controller"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "memberName": "timeouts", 
            "yangName": "timeouts", 
            "className": "BlinkyTimeoutsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.system_defaults.timeouts.timeouts_maapi_gen import BlinkyTimeoutsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "implementation", 
            "yangName": "implementation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "internalId", 
            "yangName": "internal-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
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
            "qwilt_tech_storage_controller"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "implementation", 
            "yangName": "implementation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "internalId", 
            "yangName": "internal-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


