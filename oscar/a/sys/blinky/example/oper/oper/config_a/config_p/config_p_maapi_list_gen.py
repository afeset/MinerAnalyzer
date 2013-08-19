


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

from config_p_maapi_list_base_gen import ConfigPMaapiListBase
from config_p_maapi_gen import BlinkyConfigPMaapi

class BlinkyConfigPMaapiList(ConfigPMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-configP")
        self.domain = None

        self.configPs = {}
        self.configPKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newConfigP (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-configp').debug3Func(): logFunc('called.')
        configP = BlinkyConfigPMaapi(self._log)
        configP.init(self.domain)
        return configP

    def setConfigPObj (self, key, configPObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-configp-obj').debug3Func(): logFunc('called. key=%s, configPObj=%s', key, configPObj)
        if key not in self.configPs:
            self.configPKeys.append(key)
        self.configPs[str(key)] = configPObj

    def getConfigPObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-configp-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.configPs.keys():
            for logFunc in self._log('get-configp-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.configPs[str(key)])
            return self.configPs[str(key)]
        for logFunc in self._log('get-configp-obj-missing').errorFunc(): logFunc('configP %s not in configPs. existing items: %s', key, self.configPs.keys())
        return None

    def deleteConfigP (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-configp').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.configPKeys:
            for logFunc in self._log('delete-configP-not-found').warningFunc(): logFunc('key=%s is missing from the configPKeys list', key)
            if str(key) in self.configPs.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-configp-not-found-but-in-dict').errorFunc(): logFunc('configPs dictionary & configPKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.configPs.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-configP-not-found-but-in-list').errorFunc(): logFunc('configPs dictionary & configPKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.configPKeys.remove(str(key))
        del self.configPs[str(key)]

    def hasConfigPObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.configPs.keys():
            if self.configPs[str(key)]:
                has = True
        for logFunc in self._log('has-configp-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.configPKeys])
        return self.configPKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for configP in self.configPs.values():
            configP.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for configP in self.configPs.values():
            configP.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for configP in self.configPs.values():
            configP.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for configP in self.configPs.values():
            configP.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for configP in self.configPs.values():
            if configP:
                configP._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.configPs.keys():
            if self.configPs[key]:
                self.configPs[key].clearAllSet()
            else:
                self.configPKeys.remove(str(key))
                del self.configPs[str(key)]

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("config-a", "http://qwilt.com/model/oper", "oper"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def readListKeys (self
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.configPs = {}
        self.configPKeys = []

        keyPath = self._getSelfKeyPath(
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("config-p", "http://qwilt.com/model/oper", "oper"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.configPKeys.append(key.getCannonicalStr())
            self.configPs[key.getCannonicalStr()] = None

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

        for key in self.configPs.keys():
            if self.configPs[key]:
                res = self.configPs[key]._collectItemsToDelete(
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-configP-failed').errorFunc(): logFunc('configPObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("config-p", "http://qwilt.com/model/oper", "oper"))
                keyPath.addKeyPathPostfix(xmlVal)
                valKey = Value()
                valKey.setInt64(key)
                keyPath.addKeyPathPostfix(valKey)

                itemsToDelete.append(keyPath)

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        for key in self.configPs.keys():
            if self.configPs[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("config-p", "http://qwilt.com/model/oper", "oper")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setInt64(key)
                tagValueList.push(("id", "http://qwilt.com/model/oper"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.configPs[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-configP-failed').errorFunc(): logFunc('configP._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.configPs.keys():
            if self.configPs[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("config-p", "http://qwilt.com/model/oper", "oper")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setInt64(key)
                tagValueList.push(("id", "http://qwilt.com/model/oper"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.configPs[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-configP-failed').errorFunc(): logFunc('configP._fillReadTagValues() failed. key=%s', key)
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

        for key in self.configPs.keys():
            if self.configPs[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "config-p") or \
                    (ns != "http://qwilt.com/model/oper") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "config-p", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "id") or \
                    (ns != "http://qwilt.com/model/oper"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "id", "http://qwilt.com/model/oper", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asInt64()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.configPs[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-configP-failed').errorFunc(): logFunc('configP._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "config-p") or \
                    (ns != "http://qwilt.com/model/oper") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "config-p", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyConfigPMaapi", 
        "name": "configP", 
        "keyLeaf": {
            "varName": "configP", 
            "yangName": "id", 
            "typeHandler": "handler: IntHandler"
        }, 
        "yangName": "config-p", 
        "namespace": "config_p", 
        "moduleYangNamespacePrefix": "oper", 
        "className": "ConfigPMaapiList", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.config_p_maapi_list_gen import ConfigPMaapiList", 
        "baseClassName": "ConfigPMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/oper", 
        "containerModule": "config_p_maapi_gen", 
        "baseModule": "config_p_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "config-a", 
            "namespace": "config_a", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "config-a"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "isCurrent": true, 
            "yangName": "config-p", 
            "namespace": "config_p", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "keyLeaf": {
                "varName": "configP", 
                "yangName": "id", 
                "typeHandler": "handler: IntHandler"
            }, 
            "name": "config-p"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opR", 
            "yangName": "op-r", 
            "className": "BlinkyOpRMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.op_r.op_r_maapi_list_gen import BlinkyOpRMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "oper", 
            "oper"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


