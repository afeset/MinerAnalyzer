


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

from controller_maapi_list_base_gen import ControllerMaapiListBase
from controller_maapi_gen import BlinkyControllerMaapi

class BlinkyControllerMaapiList(ControllerMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-controller")
        self.domain = None

        self.controllers = {}
        self.controllerKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newController (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-controller').debug3Func(): logFunc('called.')
        controller = BlinkyControllerMaapi(self._log)
        controller.init(self.domain)
        return controller

    def setControllerObj (self, key, controllerObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-controller-obj').debug3Func(): logFunc('called. key=%s, controllerObj=%s', key, controllerObj)
        if key not in self.controllers:
            self.controllerKeys.append(key)
        self.controllers[str(key)] = controllerObj

    def getControllerObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-controller-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.controllers.keys():
            for logFunc in self._log('get-controller-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.controllers[str(key)])
            return self.controllers[str(key)]
        for logFunc in self._log('get-controller-obj-missing').errorFunc(): logFunc('controller %s not in controllers. existing items: %s', key, self.controllers.keys())
        return None

    def deleteController (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-controller').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.controllerKeys:
            for logFunc in self._log('delete-controller-not-found').warningFunc(): logFunc('key=%s is missing from the controllerKeys list', key)
            if str(key) in self.controllers.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-controller-not-found-but-in-dict').errorFunc(): logFunc('controllers dictionary & controllerKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.controllers.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-controller-not-found-but-in-list').errorFunc(): logFunc('controllers dictionary & controllerKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.controllerKeys.remove(str(key))
        del self.controllers[str(key)]

    def hasControllerObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.controllers.keys():
            if self.controllers[str(key)]:
                has = True
        for logFunc in self._log('has-controller-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.controllerKeys])
        return self.controllerKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for controller in self.controllers.values():
            controller.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for controller in self.controllers.values():
            controller.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for controller in self.controllers.values():
            controller.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for controller in self.controllers.values():
            controller.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for controller in self.controllers.values():
            if controller:
                controller._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.controllers.keys():
            if self.controllers[key]:
                self.controllers[key].clearAllSet()
            else:
                self.controllerKeys.remove(str(key))
                del self.controllers[str(key)]

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("storage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", "qt-strg"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def readListKeys (self
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.controllers = {}
        self.controllerKeys = []

        keyPath = self._getSelfKeyPath(
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.controllerKeys.append(key.getCannonicalStr())
            self.controllers[key.getCannonicalStr()] = None

        return ReturnCodes.kOk

    def write (self
               , trxContext=None
               ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(
                                   trxContext)

    def read (self
              
              , trxContext=None):
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  True,
                                  trxContext)

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called.')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-read-fill-read-tag-values-failed').errorFunc(): logFunc('_fillReadTagValues() failed')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed.')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed.')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        for key in self.controllers.keys():
            if self.controllers[key]:
                res = self.controllers[key]._collectItemsToDelete(
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-controller-failed').errorFunc(): logFunc('controllerObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl"))
                keyPath.addKeyPathPostfix(xmlVal)
                valKey = Value()
                valKey.setString(key)
                keyPath.addKeyPathPostfix(valKey)

                itemsToDelete.append(keyPath)

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        for key in self.controllers.keys():
            if self.controllers[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.controllers[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-controller-failed').errorFunc(): logFunc('controller._fillWriteTagValues() failed. key=%s', key)
                    return ReturnCodes.kGeneralError

                if tagValueList.getLen() == tagValueListLen:
                    # descendant didn't add anything, no need to read it.
                    tagValueList.pop()
                    tagValueList.pop()
                else:
                    valEnd = Value()
                    valEnd.setXmlEnd((tag, ns, prefix))
                    tagValueList.push((tag, ns), valEnd)

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        for key in self.controllers.keys():
            if self.controllers[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", "qt-strg-ctrl")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.controllers[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-controller-failed').errorFunc(): logFunc('controller._fillReadTagValues() failed. key=%s', key)
                    return ReturnCodes.kGeneralError

                if tagValueList.getLen() == tagValueListLen:
                    # descendant didn't add anything, no need to read it.
                    tagValueList.pop()
                    tagValueList.pop()
                else:
                    valEnd = Value()
                    valEnd.setXmlEnd((tag, ns, prefix))
                    tagValueList.push((tag, ns), valEnd)

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)

        res = ReturnCodes.kOk

        for key in self.controllers.keys():
            if self.controllers[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "controller") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "name") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.controllers[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-controller-failed').errorFunc(): logFunc('controller._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "controller") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyControllerMaapi", 
        "name": "controller", 
        "keyLeaf": {
            "varName": "controller", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "controller", 
        "namespace": "controller", 
        "moduleYangNamespacePrefix": "qt-strg-ctrl", 
        "className": "ControllerMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.controller_maapi_list_gen import ControllerMaapiList", 
        "baseClassName": "ControllerMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
        "containerModule": "controller_maapi_gen", 
        "baseModule": "controller_maapi_list_base_gen"
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
            "isCurrent": true, 
            "yangName": "controller", 
            "namespace": "controller", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "keyLeaf": {
                "varName": "controller", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "controller"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "memberName": "timeouts", 
            "yangName": "timeouts", 
            "className": "BlinkyTimeoutsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.timeouts.timeouts_maapi_list_gen import BlinkyTimeoutsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.system_defaults.system_defaults_maapi_list_gen import BlinkySystemDefaultsMaapi", 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "internalId", 
            "yangName": "internal-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "internalId", 
            "yangName": "internal-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


