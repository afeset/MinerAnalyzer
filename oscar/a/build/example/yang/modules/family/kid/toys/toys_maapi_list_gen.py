


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

from toys_maapi_list_base_gen import ToysMaapiListBase
from toys_maapi_gen import BlinkyToysMaapi

class BlinkyToysMaapiList(ToysMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-toys")
        self.domain = None

        self.toyss = {}
        self.toysKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newToys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-toys').debug3Func(): logFunc('called.')
        toys = BlinkyToysMaapi(self._log)
        toys.init(self.domain)
        return toys

    def setToysObj (self, key, toysObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-toys-obj').debug3Func(): logFunc('called. key=%s, toysObj=%s', key, toysObj)
        if key not in self.toyss:
            self.toysKeys.append(key)
        self.toyss[str(key)] = toysObj

    def getToysObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-toys-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.toyss.keys():
            for logFunc in self._log('get-toys-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.toyss[str(key)])
            return self.toyss[str(key)]
        for logFunc in self._log('get-toys-obj-missing').errorFunc(): logFunc('toys %s not in toyss. existing items: %s', key, self.toyss.keys())
        return None

    def deleteToys (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-toys').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.toysKeys:
            for logFunc in self._log('delete-toys-not-found').warningFunc(): logFunc('key=%s is missing from the toysKeys list', key)
            if str(key) in self.toyss.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-toys-not-found-but-in-dict').errorFunc(): logFunc('toyss dictionary & toysKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.toyss.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-toys-not-found-but-in-list').errorFunc(): logFunc('toyss dictionary & toysKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.toysKeys.remove(str(key))
        del self.toyss[str(key)]

    def hasToysObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.toyss.keys():
            if self.toyss[str(key)]:
                has = True
        for logFunc in self._log('has-toys-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.toysKeys])
        return self.toysKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for toys in self.toyss.values():
            toys.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for toys in self.toyss.values():
            toys.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for toys in self.toyss.values():
            toys.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for toys in self.toyss.values():
            toys.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for toys in self.toyss.values():
            if toys:
                toys._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.toyss.keys():
            if self.toyss[key]:
                self.toyss[key].clearAllSet()
            else:
                self.toysKeys.remove(str(key))
                del self.toyss[str(key)]

    def _getSelfKeyPath (self, kid
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        ancestorVal = Value()
        ancestorVal.setString(kid);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("kid", "http://qwilt.com/model/family", "family"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def readListKeys (self
                      , kid
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.toyss = {}
        self.toysKeys = []

        keyPath = self._getSelfKeyPath(kid, 
                                       
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("toys", "http://qwilt.com/model/family", "family"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.toysKeys.append(key.getCannonicalStr())
            self.toyss[key.getCannonicalStr()] = None

        return ReturnCodes.kOk

    def write (self
               , kid
               , trxContext=None
               ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(kid, 
                                   trxContext)

    def read (self
              , kid
              
              , trxContext=None):
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(kid, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , kid
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(kid, 
                                  True,
                                  trxContext)

    def _internalWrite (self, 
                        kid, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called.')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(kid, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(kid, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       kid, 
                       
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

        keyPath = self._getSelfKeyPath(kid, 
                                       
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
                               kid, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        for key in self.toyss.keys():
            if self.toyss[key]:
                res = self.toyss[key]._collectItemsToDelete(kid, 
                                                                     
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-toys-failed').errorFunc(): logFunc('toysObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(kid, 
                                               
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("toys", "http://qwilt.com/model/family", "family"))
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

        for key in self.toyss.keys():
            if self.toyss[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("toys", "http://qwilt.com/model/family", "family")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("id", "http://qwilt.com/model/family"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.toyss[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-toys-failed').errorFunc(): logFunc('toys._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.toyss.keys():
            if self.toyss[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("toys", "http://qwilt.com/model/family", "family")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("id", "http://qwilt.com/model/family"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.toyss[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-toys-failed').errorFunc(): logFunc('toys._fillReadTagValues() failed. key=%s', key)
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

        for key in self.toyss.keys():
            if self.toyss[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "toys") or \
                    (ns != "http://qwilt.com/model/family") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "toys", "http://qwilt.com/model/family", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "id") or \
                    (ns != "http://qwilt.com/model/family"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "id", "http://qwilt.com/model/family", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.toyss[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-toys-failed').errorFunc(): logFunc('toys._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "toys") or \
                    (ns != "http://qwilt.com/model/family") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "toys", "http://qwilt.com/model/family", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyToysMaapi", 
        "name": "toys", 
        "keyLeaf": {
            "varName": "toys", 
            "yangName": "id", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "toys", 
        "namespace": "toys", 
        "moduleYangNamespacePrefix": "family", 
        "className": "ToysMaapiList", 
        "importStatement": "from a.build.example.yang.modules.family.kid.toys.toys_maapi_list_gen import ToysMaapiList", 
        "baseClassName": "ToysMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/family", 
        "containerModule": "toys_maapi_gen", 
        "baseModule": "toys_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "family", 
            "isCurrent": false, 
            "yangName": "kid", 
            "namespace": "kid", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "keyLeaf": {
                "varName": "kid", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "kid"
        }, 
        {
            "moduleYangNamespacePrefix": "family", 
            "isCurrent": true, 
            "yangName": "toys", 
            "namespace": "toys", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "keyLeaf": {
                "varName": "toys", 
                "yangName": "id", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "toys"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "build", 
            "example", 
            "yang", 
            "modules", 
            "family"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


