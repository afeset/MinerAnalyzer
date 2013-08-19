


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

from prefix_maapi_list_base_gen import PrefixMaapiListBase
from prefix_maapi_gen import BlinkyPrefixMaapi

class BlinkyPrefixMaapiList(PrefixMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-prefix")
        self.domain = None

        self.prefixs = {}
        self.prefixKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newPrefix (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-prefix').debug3Func(): logFunc('called.')
        prefix = BlinkyPrefixMaapi(self._log)
        prefix.init(self.domain)
        return prefix

    def setPrefixObj (self, key, prefixObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-prefix-obj').debug3Func(): logFunc('called. key=%s, prefixObj=%s', key, prefixObj)
        if key not in self.prefixs:
            self.prefixKeys.append(key)
        self.prefixs[str(key)] = prefixObj

    def getPrefixObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-prefix-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.prefixs.keys():
            for logFunc in self._log('get-prefix-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.prefixs[str(key)])
            return self.prefixs[str(key)]
        for logFunc in self._log('get-prefix-obj-missing').errorFunc(): logFunc('prefix %s not in prefixs. existing items: %s', key, self.prefixs.keys())
        return None

    def deletePrefix (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-prefix').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.prefixKeys:
            for logFunc in self._log('delete-prefix-not-found').warningFunc(): logFunc('key=%s is missing from the prefixKeys list', key)
            if str(key) in self.prefixs.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-prefix-not-found-but-in-dict').errorFunc(): logFunc('prefixs dictionary & prefixKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.prefixs.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-prefix-not-found-but-in-list').errorFunc(): logFunc('prefixs dictionary & prefixKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.prefixKeys.remove(str(key))
        del self.prefixs[str(key)]

    def hasPrefixObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.prefixs.keys():
            if self.prefixs[str(key)]:
                has = True
        for logFunc in self._log('has-prefix-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.prefixKeys])
        return self.prefixKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for prefix in self.prefixs.values():
            prefix.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for prefix in self.prefixs.values():
            prefix.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for prefix in self.prefixs.values():
            prefix.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for prefix in self.prefixs.values():
            prefix.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for prefix in self.prefixs.values():
            if prefix:
                prefix._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.prefixs.keys():
            if self.prefixs[key]:
                self.prefixs[key].clearAllSet()
            else:
                self.prefixKeys.remove(str(key))
                del self.prefixs[str(key)]

    def _getSelfKeyPath (self, zone
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ipv4", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(zone);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("zone", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("zones", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def readListKeys (self
                      , zone
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.prefixs = {}
        self.prefixKeys = []

        keyPath = self._getSelfKeyPath(zone, 
                                       
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("prefix", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.prefixKeys.append(key.getCannonicalStr())
            self.prefixs[key.getCannonicalStr()] = None

        return ReturnCodes.kOk

    def write (self
               , zone
               , trxContext=None
               ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(zone, 
                                   trxContext)

    def read (self
              , zone
              
              , trxContext=None):
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(zone, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , zone
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(zone, 
                                  True,
                                  trxContext)

    def _internalWrite (self, 
                        zone, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called.')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(zone, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(zone, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       zone, 
                       
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

        keyPath = self._getSelfKeyPath(zone, 
                                       
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
                               zone, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        for key in self.prefixs.keys():
            if self.prefixs[key]:
                res = self.prefixs[key]._collectItemsToDelete(zone, 
                                                                     
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-prefix-failed').errorFunc(): logFunc('prefixObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(zone, 
                                               
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("prefix", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
                keyPath.addKeyPathPostfix(xmlVal)
                valKey = Value()
                valKey.setIPv4Prefix(key)
                keyPath.addKeyPathPostfix(valKey)

                itemsToDelete.append(keyPath)

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        for key in self.prefixs.keys():
            if self.prefixs[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("prefix", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setIPv4Prefix(key)
                tagValueList.push(("prefix", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.prefixs[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-prefix-failed').errorFunc(): logFunc('prefix._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.prefixs.keys():
            if self.prefixs[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("prefix", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setIPv4Prefix(key)
                tagValueList.push(("prefix", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.prefixs[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-prefix-failed').errorFunc(): logFunc('prefix._fillReadTagValues() failed. key=%s', key)
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

        for key in self.prefixs.keys():
            if self.prefixs[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "prefix") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "prefix", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "prefix") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "prefix", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = (valKey.asIPv4Prefix())
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.prefixs[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-prefix-failed').errorFunc(): logFunc('prefix._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "prefix") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "prefix", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyPrefixMaapi", 
        "name": "prefix", 
        "keyLeaf": {
            "varName": "prefix", 
            "yangName": "prefix", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy"
        }, 
        "yangName": "prefix", 
        "namespace": "prefix", 
        "moduleYangNamespacePrefix": "qtc", 
        "className": "PrefixMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.zones.zone.ipv4.prefix.prefix_maapi_list_gen import PrefixMaapiList", 
        "baseClassName": "PrefixMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
        "containerModule": "prefix_maapi_gen", 
        "baseModule": "prefix_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "zones", 
            "namespace": "zones", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "zones"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "isCurrent": false, 
            "yangName": "zone", 
            "namespace": "zone", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "keyLeaf": {
                "varName": "zone", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "zone"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "ipv4", 
            "namespace": "ipv4", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "ipv4"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "isCurrent": true, 
            "yangName": "prefix", 
            "namespace": "prefix", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "keyLeaf": {
                "varName": "prefix", 
                "yangName": "prefix", 
                "typeHandler": "handler: Ipv4PrefixHandlerPy"
            }, 
            "name": "prefix"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "prefix", 
            "yangName": "prefix", 
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
            "content", 
            "qwilt_tech_content"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "prefix", 
            "yangName": "prefix", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


