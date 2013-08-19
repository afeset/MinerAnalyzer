


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

from ordered_list_maapi_list_base_gen import OrderedListMaapiListBase
from ordered_list_maapi_gen import BlinkyOrderedListMaapi

class BlinkyOrderedListMaapiList(OrderedListMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-orderedList")
        self.domain = None

        self.orderedLists = {}
        self.orderedListKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newOrderedList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-orderedlist').debug3Func(): logFunc('called.')
        orderedList = BlinkyOrderedListMaapi(self._log)
        orderedList.init(self.domain)
        return orderedList

    def setOrderedListObj (self, key, orderedListObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-orderedlist-obj').debug3Func(): logFunc('called. key=%s, orderedListObj=%s', key, orderedListObj)
        if key not in self.orderedLists:
            self.orderedListKeys.append(key)
        self.orderedLists[str(key)] = orderedListObj

    def getOrderedListObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-orderedlist-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.orderedLists.keys():
            for logFunc in self._log('get-orderedlist-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.orderedLists[str(key)])
            return self.orderedLists[str(key)]
        for logFunc in self._log('get-orderedlist-obj-missing').errorFunc(): logFunc('orderedList %s not in orderedLists. existing items: %s', key, self.orderedLists.keys())
        return None

    def deleteOrderedList (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-orderedlist').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.orderedListKeys:
            for logFunc in self._log('delete-orderedList-not-found').warningFunc(): logFunc('key=%s is missing from the orderedListKeys list', key)
            if str(key) in self.orderedLists.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-orderedlist-not-found-but-in-dict').errorFunc(): logFunc('orderedLists dictionary & orderedListKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.orderedLists.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-orderedList-not-found-but-in-list').errorFunc(): logFunc('orderedLists dictionary & orderedListKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.orderedListKeys.remove(str(key))
        del self.orderedLists[str(key)]

    def hasOrderedListObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.orderedLists.keys():
            if self.orderedLists[str(key)]:
                has = True
        for logFunc in self._log('has-orderedlist-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.orderedListKeys])
        return self.orderedListKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for orderedList in self.orderedLists.values():
            orderedList.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for orderedList in self.orderedLists.values():
            orderedList.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for orderedList in self.orderedLists.values():
            orderedList.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for orderedList in self.orderedLists.values():
            orderedList.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for orderedList in self.orderedLists.values():
            if orderedList:
                orderedList._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.orderedLists.keys():
            if self.orderedLists[key]:
                self.orderedLists[key].clearAllSet()
            else:
                self.orderedListKeys.remove(str(key))
                del self.orderedLists[str(key)]

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("list-ordered-by-user", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def readListKeys (self
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.orderedLists = {}
        self.orderedListKeys = []

        keyPath = self._getSelfKeyPath(
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("ordered-list", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.orderedListKeys.append(key.getCannonicalStr())
            self.orderedLists[key.getCannonicalStr()] = None

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

        for key in self.orderedLists.keys():
            if self.orderedLists[key]:
                res = self.orderedLists[key]._collectItemsToDelete(
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-orderedList-failed').errorFunc(): logFunc('orderedListObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("ordered-list", "http://qwilt.com/model/lake-example", "lake-example"))
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

        for key in self.orderedLists.keys():
            if self.orderedLists[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("ordered-list", "http://qwilt.com/model/lake-example", "lake-example")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/model/lake-example"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.orderedLists[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-orderedList-failed').errorFunc(): logFunc('orderedList._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.orderedLists.keys():
            if self.orderedLists[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("ordered-list", "http://qwilt.com/model/lake-example", "lake-example")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/model/lake-example"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.orderedLists[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-orderedList-failed').errorFunc(): logFunc('orderedList._fillReadTagValues() failed. key=%s', key)
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

        for key in self.orderedLists.keys():
            if self.orderedLists[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "ordered-list") or \
                    (ns != "http://qwilt.com/model/lake-example") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "ordered-list", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "name") or \
                    (ns != "http://qwilt.com/model/lake-example"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "name", "http://qwilt.com/model/lake-example", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.orderedLists[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-orderedList-failed').errorFunc(): logFunc('orderedList._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "ordered-list") or \
                    (ns != "http://qwilt.com/model/lake-example") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "ordered-list", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyOrderedListMaapi", 
        "name": "orderedList", 
        "keyLeaf": {
            "varName": "orderedList", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "ordered-list", 
        "namespace": "ordered_list", 
        "moduleYangNamespacePrefix": "lake-example", 
        "className": "OrderedListMaapiList", 
        "importStatement": "from a.sys.blinky.example.lake_example.list_ordered_by_user.ordered_list.ordered_list_maapi_list_gen import OrderedListMaapiList", 
        "baseClassName": "OrderedListMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
        "containerModule": "ordered_list_maapi_gen", 
        "baseModule": "ordered_list_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "list-ordered-by-user", 
            "namespace": "list_ordered_by_user", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "list-ordered-by-user"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": true, 
            "yangName": "ordered-list", 
            "namespace": "ordered_list", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "orderedList", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "ordered-list"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "value", 
            "yangName": "value", 
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
            "lake_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


