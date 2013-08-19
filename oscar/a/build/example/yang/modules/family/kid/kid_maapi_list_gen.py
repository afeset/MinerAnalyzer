


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

from kid_maapi_list_base_gen import KidMaapiListBase
from kid_maapi_gen import BlinkyKidMaapi

class BlinkyKidMaapiList(KidMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-kid")
        self.domain = None

        self.kids = {}
        self.kidKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newKid (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-kid').debug3Func(): logFunc('called.')
        kid = BlinkyKidMaapi(self._log)
        kid.init(self.domain)
        return kid

    def setKidObj (self, key, kidObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-kid-obj').debug3Func(): logFunc('called. key=%s, kidObj=%s', key, kidObj)
        if key not in self.kids:
            self.kidKeys.append(key)
        self.kids[str(key)] = kidObj

    def getKidObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-kid-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.kids.keys():
            for logFunc in self._log('get-kid-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.kids[str(key)])
            return self.kids[str(key)]
        for logFunc in self._log('get-kid-obj-missing').errorFunc(): logFunc('kid %s not in kids. existing items: %s', key, self.kids.keys())
        return None

    def deleteKid (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-kid').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.kidKeys:
            for logFunc in self._log('delete-kid-not-found').warningFunc(): logFunc('key=%s is missing from the kidKeys list', key)
            if str(key) in self.kids.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-kid-not-found-but-in-dict').errorFunc(): logFunc('kids dictionary & kidKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.kids.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-kid-not-found-but-in-list').errorFunc(): logFunc('kids dictionary & kidKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.kidKeys.remove(str(key))
        del self.kids[str(key)]

    def hasKidObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.kids.keys():
            if self.kids[str(key)]:
                has = True
        for logFunc in self._log('has-kid-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.kidKeys])
        return self.kidKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for kid in self.kids.values():
            kid.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for kid in self.kids.values():
            kid.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for kid in self.kids.values():
            kid.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for kid in self.kids.values():
            kid.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for kid in self.kids.values():
            if kid:
                kid._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.kids.keys():
            if self.kids[key]:
                self.kids[key].clearAllSet()
            else:
                self.kidKeys.remove(str(key))
                del self.kids[str(key)]

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def readListKeys (self
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.kids = {}
        self.kidKeys = []

        keyPath = self._getSelfKeyPath(
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("kid", "http://qwilt.com/model/family", "family"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.kidKeys.append(key.getCannonicalStr())
            self.kids[key.getCannonicalStr()] = None

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

        for key in self.kids.keys():
            if self.kids[key]:
                res = self.kids[key]._collectItemsToDelete(
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-kid-failed').errorFunc(): logFunc('kidObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("kid", "http://qwilt.com/model/family", "family"))
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

        for key in self.kids.keys():
            if self.kids[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("kid", "http://qwilt.com/model/family", "family")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/model/family"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.kids[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-kid-failed').errorFunc(): logFunc('kid._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.kids.keys():
            if self.kids[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("kid", "http://qwilt.com/model/family", "family")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/model/family"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.kids[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-kid-failed').errorFunc(): logFunc('kid._fillReadTagValues() failed. key=%s', key)
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

        for key in self.kids.keys():
            if self.kids[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "kid") or \
                    (ns != "http://qwilt.com/model/family") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "kid", "http://qwilt.com/model/family", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "name") or \
                    (ns != "http://qwilt.com/model/family"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "name", "http://qwilt.com/model/family", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.kids[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-kid-failed').errorFunc(): logFunc('kid._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "kid") or \
                    (ns != "http://qwilt.com/model/family") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "kid", "http://qwilt.com/model/family", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyKidMaapi", 
        "name": "kid", 
        "keyLeaf": {
            "varName": "kid", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "kid", 
        "namespace": "kid", 
        "moduleYangNamespacePrefix": "family", 
        "className": "KidMaapiList", 
        "importStatement": "from a.build.example.yang.modules.family.kid.kid_maapi_list_gen import KidMaapiList", 
        "baseClassName": "KidMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/family", 
        "containerModule": "kid_maapi_gen", 
        "baseModule": "kid_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "family", 
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "family", 
            "memberName": "size", 
            "yangName": "size", 
            "className": "BlinkySizeMaapi", 
            "importStatement": "from a.build.example.yang.modules.family.kid.size.size_maapi_list_gen import BlinkySizeMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/family"
        }, 
        {
            "moduleYangNamespacePrefix": "family", 
            "memberName": "toysList", 
            "yangName": "toys", 
            "className": "BlinkyToysMaapiList", 
            "importStatement": "from a.build.example.yang.modules.family.kid.toys.toys_maapi_list_list_gen import BlinkyToysMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/family"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
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
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
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


