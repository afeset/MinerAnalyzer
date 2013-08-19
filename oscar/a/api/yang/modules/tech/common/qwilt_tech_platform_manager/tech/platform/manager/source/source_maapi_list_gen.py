


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

from source_maapi_list_base_gen import SourceMaapiListBase
from source_maapi_gen import BlinkySourceMaapi

class BlinkySourceMaapiList(SourceMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-source")
        self.domain = None

        self.sources = {}
        self.sourceKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newSource (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-source').debug3Func(): logFunc('called.')
        source = BlinkySourceMaapi(self._log)
        source.init(self.domain)
        return source

    def setSourceObj (self, key, sourceObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-source-obj').debug3Func(): logFunc('called. key=%s, sourceObj=%s', key, sourceObj)
        if key not in self.sources:
            self.sourceKeys.append(key)
        self.sources[str(key)] = sourceObj

    def getSourceObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-source-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.sources.keys():
            for logFunc in self._log('get-source-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.sources[str(key)])
            return self.sources[str(key)]
        for logFunc in self._log('get-source-obj-missing').errorFunc(): logFunc('source %s not in sources. existing items: %s', key, self.sources.keys())
        return None

    def deleteSource (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-source').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.sourceKeys:
            for logFunc in self._log('delete-source-not-found').warningFunc(): logFunc('key=%s is missing from the sourceKeys list', key)
            if str(key) in self.sources.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-source-not-found-but-in-dict').errorFunc(): logFunc('sources dictionary & sourceKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.sources.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-source-not-found-but-in-list').errorFunc(): logFunc('sources dictionary & sourceKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.sourceKeys.remove(str(key))
        del self.sources[str(key)]

    def hasSourceObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.sources.keys():
            if self.sources[str(key)]:
                has = True
        for logFunc in self._log('has-source-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.sourceKeys])
        return self.sourceKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for source in self.sources.values():
            source.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for source in self.sources.values():
            source.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for source in self.sources.values():
            source.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for source in self.sources.values():
            source.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for source in self.sources.values():
            if source:
                source._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.sources.keys():
            if self.sources[key]:
                self.sources[key].clearAllSet()
            else:
                self.sourceKeys.remove(str(key))
                del self.sources[str(key)]

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("manager", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("platform", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", "qt-pltf"))
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
        self.sources = {}
        self.sourceKeys = []

        keyPath = self._getSelfKeyPath(
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.sourceKeys.append(key.getCannonicalStr())
            self.sources[key.getCannonicalStr()] = None

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

        for key in self.sources.keys():
            if self.sources[key]:
                res = self.sources[key]._collectItemsToDelete(
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-source-failed').errorFunc(): logFunc('sourceObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr"))
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

        for key in self.sources.keys():
            if self.sources[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.sources[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-source-failed').errorFunc(): logFunc('source._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.sources.keys():
            if self.sources[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.sources[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-source-failed').errorFunc(): logFunc('source._fillReadTagValues() failed. key=%s', key)
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

        for key in self.sources.keys():
            if self.sources[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "source") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "name") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.sources[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-source-failed').errorFunc(): logFunc('source._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "source") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkySourceMaapi", 
        "name": "source", 
        "keyLeaf": {
            "varName": "source", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "source", 
        "namespace": "source", 
        "moduleYangNamespacePrefix": "qt-pltf-mngr", 
        "className": "SourceMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_maapi_list_gen import SourceMaapiList", 
        "baseClassName": "SourceMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
        "containerModule": "source_maapi_gen", 
        "baseModule": "source_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qt-pltf", 
            "yangName": "platform", 
            "namespace": "platform", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", 
            "name": "platform"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "yangName": "manager", 
            "namespace": "manager", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "name": "manager"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "isCurrent": true, 
            "yangName": "source", 
            "namespace": "source", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "keyLeaf": {
                "varName": "source", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "source"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.system_defaults.system_defaults_maapi_list_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.counters.counters_maapi_list_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "simulationFile", 
            "yangName": "simulation-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeout", 
            "yangName": "command-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeout", 
            "yangName": "command-warning-timeout", 
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
            "qwilt_tech_platform_manager"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "simulationFile", 
            "yangName": "simulation-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeout", 
            "yangName": "command-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeout", 
            "yangName": "command-warning-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


