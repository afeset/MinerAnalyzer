


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

from lll_maapi_list_base_gen import LllMaapiListBase
from lll_maapi_gen import BlinkyLllMaapi

class BlinkyLllMaapiList(LllMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-lll")
        self.domain = None

        self.llls = {}
        self.lllKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newLll (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-lll').debug3Func(): logFunc('called.')
        lll = BlinkyLllMaapi(self._log)
        lll.init(self.domain)
        return lll

    def setLllObj (self, key, lllObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-lll-obj').debug3Func(): logFunc('called. key=%s, lllObj=%s', key, lllObj)
        if key not in self.llls:
            self.lllKeys.append(key)
        self.llls[str(key)] = lllObj

    def getLllObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-lll-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.llls.keys():
            for logFunc in self._log('get-lll-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.llls[str(key)])
            return self.llls[str(key)]
        for logFunc in self._log('get-lll-obj-missing').errorFunc(): logFunc('lll %s not in llls. existing items: %s', key, self.llls.keys())
        return None

    def deleteLll (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-lll').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.lllKeys:
            for logFunc in self._log('delete-lll-not-found').warningFunc(): logFunc('key=%s is missing from the lllKeys list', key)
            if str(key) in self.llls.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-lll-not-found-but-in-dict').errorFunc(): logFunc('llls dictionary & lllKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.llls.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-lll-not-found-but-in-list').errorFunc(): logFunc('llls dictionary & lllKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.lllKeys.remove(str(key))
        del self.llls[str(key)]

    def hasLllObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.llls.keys():
            if self.llls[str(key)]:
                has = True
        for logFunc in self._log('has-lll-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.lllKeys])
        return self.lllKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for lll in self.llls.values():
            lll.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for lll in self.llls.values():
            lll.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for lll in self.llls.values():
            lll.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for lll in self.llls.values():
            lll.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for lll in self.llls.values():
            if lll:
                lll._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.llls.keys():
            if self.llls[key]:
                self.llls[key].clearAllSet()
            else:
                self.lllKeys.remove(str(key))
                del self.llls[str(key)]

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("base", "http://qwilt.com/model/benchmark", "bnch"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def readListKeys (self
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.llls = {}
        self.lllKeys = []

        keyPath = self._getSelfKeyPath(
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("lll", "http://qwilt.com/model/benchmark", "bnch"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.lllKeys.append(key.getCannonicalStr())
            self.llls[key.getCannonicalStr()] = None

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

        for key in self.llls.keys():
            if self.llls[key]:
                res = self.llls[key]._collectItemsToDelete(
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-lll-failed').errorFunc(): logFunc('lllObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("lll", "http://qwilt.com/model/benchmark", "bnch"))
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

        for key in self.llls.keys():
            if self.llls[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("lll", "http://qwilt.com/model/benchmark", "bnch")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/model/benchmark"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.llls[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-lll-failed').errorFunc(): logFunc('lll._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.llls.keys():
            if self.llls[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("lll", "http://qwilt.com/model/benchmark", "bnch")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/model/benchmark"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.llls[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-lll-failed').errorFunc(): logFunc('lll._fillReadTagValues() failed. key=%s', key)
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

        for key in self.llls.keys():
            if self.llls[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "lll") or \
                    (ns != "http://qwilt.com/model/benchmark") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "lll", "http://qwilt.com/model/benchmark", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "name") or \
                    (ns != "http://qwilt.com/model/benchmark"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "name", "http://qwilt.com/model/benchmark", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.llls[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-lll-failed').errorFunc(): logFunc('lll._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "lll") or \
                    (ns != "http://qwilt.com/model/benchmark") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "lll", "http://qwilt.com/model/benchmark", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyLllMaapi", 
        "name": "lll", 
        "keyLeaf": {
            "varName": "lll", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "lll", 
        "namespace": "lll", 
        "moduleYangNamespacePrefix": "bnch", 
        "className": "LllMaapiList", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.lll_maapi_list_gen import LllMaapiList", 
        "baseClassName": "LllMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
        "containerModule": "lll_maapi_gen", 
        "baseModule": "lll_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "bnch", 
            "yangName": "base", 
            "namespace": "base", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "base"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "isCurrent": true, 
            "yangName": "lll", 
            "namespace": "lll", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "keyLeaf": {
                "varName": "lll", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lll"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "aaa", 
            "yangName": "aaa", 
            "className": "BlinkyAaaMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.aaa.aaa_maapi_list_gen import BlinkyAaaMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "ccc", 
            "yangName": "ccc", 
            "className": "BlinkyCccMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.ccc.ccc_maapi_list_gen import BlinkyCccMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "bbb", 
            "yangName": "bbb", 
            "className": "BlinkyBbbMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.bbb.bbb_maapi_list_gen import BlinkyBbbMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
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
            "sys", 
            "blinky", 
            "example", 
            "benchmark", 
            "benchmark"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
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


