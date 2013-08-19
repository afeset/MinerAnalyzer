


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

from registered_maapi_list_base_gen import RegisteredMaapiListBase
from registered_maapi_gen import BlinkyRegisteredMaapi

class BlinkyRegisteredMaapiList(RegisteredMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-registered")
        self.domain = None

        self.registereds = {}
        self.registeredKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newRegistered (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-registered').debug3Func(): logFunc('called.')
        registered = BlinkyRegisteredMaapi(self._log)
        registered.init(self.domain)
        return registered

    def setRegisteredObj (self, key, registeredObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-registered-obj').debug3Func(): logFunc('called. key=%s, registeredObj=%s', key, registeredObj)
        if key not in self.registereds:
            self.registeredKeys.append(key)
        self.registereds[str(key)] = registeredObj

    def getRegisteredObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-registered-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.registereds.keys():
            for logFunc in self._log('get-registered-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.registereds[str(key)])
            return self.registereds[str(key)]
        for logFunc in self._log('get-registered-obj-missing').errorFunc(): logFunc('registered %s not in registereds. existing items: %s', key, self.registereds.keys())
        return None

    def deleteRegistered (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-registered').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.registeredKeys:
            for logFunc in self._log('delete-registered-not-found').warningFunc(): logFunc('key=%s is missing from the registeredKeys list', key)
            if str(key) in self.registereds.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-registered-not-found-but-in-dict').errorFunc(): logFunc('registereds dictionary & registeredKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.registereds.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-registered-not-found-but-in-list').errorFunc(): logFunc('registereds dictionary & registeredKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.registeredKeys.remove(str(key))
        del self.registereds[str(key)]

    def hasRegisteredObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.registereds.keys():
            if self.registereds[str(key)]:
                has = True
        for logFunc in self._log('has-registered-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.registeredKeys])
        return self.registeredKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for registered in self.registereds.values():
            registered.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for registered in self.registereds.values():
            registered.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for registered in self.registereds.values():
            registered.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for registered in self.registereds.values():
            registered.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for registered in self.registereds.values():
            if registered:
                registered._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.registereds.keys():
            if self.registereds[key]:
                self.registereds[key].clearAllSet()
            else:
                self.registeredKeys.remove(str(key))
                del self.registereds[str(key)]

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
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
        self.registereds = {}
        self.registeredKeys = []

        keyPath = self._getSelfKeyPath(
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("registered", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.registeredKeys.append(key.getCannonicalStr())
            self.registereds[key.getCannonicalStr()] = None

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

        for key in self.registereds.keys():
            if self.registereds[key]:
                res = self.registereds[key]._collectItemsToDelete(
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-registered-failed').errorFunc(): logFunc('registeredObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("registered", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
                keyPath.addKeyPathPostfix(xmlVal)
                valKey = Value()
                valKey.setEnum(key.getValue())
                keyPath.addKeyPathPostfix(valKey)

                itemsToDelete.append(keyPath)

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        for key in self.registereds.keys():
            if self.registereds[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("registered", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setEnum(key.getValue())
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.registereds[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-registered-failed').errorFunc(): logFunc('registered._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.registereds.keys():
            if self.registereds[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("registered", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setEnum(key.getValue())
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.registereds[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-registered-failed').errorFunc(): logFunc('registered._fillReadTagValues() failed. key=%s', key)
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

        for key in self.registereds.keys():
            if self.registereds[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "registered") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "registered", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "name") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asEnum()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.registereds[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-registered-failed').errorFunc(): logFunc('registered._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "registered") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "registered", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyRegisteredMaapi", 
        "name": "registered", 
        "keyLeaf": {
            "varName": "registered", 
            "yangName": "name", 
            "typeHandler": "handler: EnumHandlerPy"
        }, 
        "yangName": "registered", 
        "namespace": "registered", 
        "moduleYangNamespacePrefix": "qt-sys-alarms", 
        "className": "RegisteredMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.registered.registered_maapi_list_gen import RegisteredMaapiList", 
        "baseClassName": "RegisteredMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
        "containerModule": "registered_maapi_gen", 
        "baseModule": "registered_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "system", 
            "namespace": "system", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "isCurrent": true, 
            "yangName": "registered", 
            "namespace": "registered", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "keyLeaf": {
                "varName": "registered", 
                "yangName": "name", 
                "typeHandler": "handler: EnumHandlerPy"
            }, 
            "name": "registered"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "devComment", 
            "yangName": "dev-comment", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "softwareVersion", 
            "yangName": "software-version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "source", 
            "yangName": "source", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "severity", 
            "yangName": "severity", 
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
            "qwilt_tech_system_alarms"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "devComment", 
            "yangName": "dev-comment", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "softwareVersion", 
            "yangName": "software-version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "source", 
            "yangName": "source", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "severity", 
            "yangName": "severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


