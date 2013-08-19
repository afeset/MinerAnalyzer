


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

from variable_collection_maapi_list_base_gen import VariableCollectionMaapiListBase
from variable_collection_maapi_gen import BlinkyVariableCollectionMaapi

class BlinkyVariableCollectionMaapiList(VariableCollectionMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-variableCollection")
        self.domain = None

        self.variableCollections = {}
        self.variableCollectionKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newVariableCollection (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-variablecollection').debug3Func(): logFunc('called.')
        variableCollection = BlinkyVariableCollectionMaapi(self._log)
        variableCollection.init(self.domain)
        return variableCollection

    def setVariableCollectionObj (self, key, variableCollectionObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-variablecollection-obj').debug3Func(): logFunc('called. key=%s, variableCollectionObj=%s', key, variableCollectionObj)
        if key not in self.variableCollections:
            self.variableCollectionKeys.append(key)
        self.variableCollections[str(key)] = variableCollectionObj

    def getVariableCollectionObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-variablecollection-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.variableCollections.keys():
            for logFunc in self._log('get-variablecollection-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.variableCollections[str(key)])
            return self.variableCollections[str(key)]
        for logFunc in self._log('get-variablecollection-obj-missing').errorFunc(): logFunc('variableCollection %s not in variableCollections. existing items: %s', key, self.variableCollections.keys())
        return None

    def deleteVariableCollection (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-variablecollection').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.variableCollectionKeys:
            for logFunc in self._log('delete-variableCollection-not-found').warningFunc(): logFunc('key=%s is missing from the variableCollectionKeys list', key)
            if str(key) in self.variableCollections.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-variablecollection-not-found-but-in-dict').errorFunc(): logFunc('variableCollections dictionary & variableCollectionKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.variableCollections.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-variableCollection-not-found-but-in-list').errorFunc(): logFunc('variableCollections dictionary & variableCollectionKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.variableCollectionKeys.remove(str(key))
        del self.variableCollections[str(key)]

    def hasVariableCollectionObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.variableCollections.keys():
            if self.variableCollections[str(key)]:
                has = True
        for logFunc in self._log('has-variablecollection-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.variableCollectionKeys])
        return self.variableCollectionKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for variableCollection in self.variableCollections.values():
            variableCollection.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for variableCollection in self.variableCollections.values():
            variableCollection.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for variableCollection in self.variableCollections.values():
            variableCollection.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for variableCollection in self.variableCollections.values():
            variableCollection.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for variableCollection in self.variableCollections.values():
            if variableCollection:
                variableCollection._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.variableCollections.keys():
            if self.variableCollections[key]:
                self.variableCollections[key].clearAllSet()
            else:
                self.variableCollectionKeys.remove(str(key))
                del self.variableCollections[str(key)]

    def _getSelfKeyPath (self, linux_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        ancestorVal = Value()
        ancestorVal.setString(linux_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("linux", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux", "qt-lnx"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def readListKeys (self
                      , linux_
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.variableCollections = {}
        self.variableCollectionKeys = []

        keyPath = self._getSelfKeyPath(linux_, 
                                       
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("variable-collection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.variableCollectionKeys.append(key.getCannonicalStr())
            self.variableCollections[key.getCannonicalStr()] = None

        return ReturnCodes.kOk

    def write (self
               , linux_
               , trxContext=None
               ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(linux_, 
                                   trxContext)

    def read (self
              , linux_
              
              , trxContext=None):
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(linux_, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , linux_
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(linux_, 
                                  True,
                                  trxContext)

    def _internalWrite (self, 
                        linux_, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called.')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(linux_, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(linux_, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       linux_, 
                       
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

        keyPath = self._getSelfKeyPath(linux_, 
                                       
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
                               linux_, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        for key in self.variableCollections.keys():
            if self.variableCollections[key]:
                res = self.variableCollections[key]._collectItemsToDelete(linux_, 
                                                                     
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-variableCollection-failed').errorFunc(): logFunc('variableCollectionObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(linux_, 
                                               
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("variable-collection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables"))
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

        for key in self.variableCollections.keys():
            if self.variableCollections[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("variable-collection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.variableCollections[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-variableCollection-failed').errorFunc(): logFunc('variableCollection._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.variableCollections.keys():
            if self.variableCollections[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("variable-collection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.variableCollections[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-variableCollection-failed').errorFunc(): logFunc('variableCollection._fillReadTagValues() failed. key=%s', key)
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

        for key in self.variableCollections.keys():
            if self.variableCollections[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "variable-collection") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "variable-collection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "name") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.variableCollections[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-variableCollection-failed').errorFunc(): logFunc('variableCollection._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "variable-collection") or \
                    (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "variable-collection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyVariableCollectionMaapi", 
        "name": "variableCollection", 
        "keyLeaf": {
            "varName": "variableCollection", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "variable-collection", 
        "namespace": "variable_collection", 
        "moduleYangNamespacePrefix": "qt-lnx-variables", 
        "className": "VariableCollectionMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable_collection_maapi_list_gen import VariableCollectionMaapiList", 
        "baseClassName": "VariableCollectionMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
        "containerModule": "variable_collection_maapi_gen", 
        "baseModule": "variable_collection_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qt-lnx", 
            "isCurrent": false, 
            "yangName": "linux", 
            "namespace": "linux_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux", 
            "keyLeaf": {
                "varName": "linux_", 
                "yangName": "instance", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "linux_"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "isCurrent": true, 
            "yangName": "variable-collection", 
            "namespace": "variable_collection", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "keyLeaf": {
                "varName": "variableCollection", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "variable-collection"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "memberName": "variableList", 
            "yangName": "variable", 
            "className": "BlinkyVariableMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.variable_maapi_list_list_gen import BlinkyVariableMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
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
            "qwilt_tech_linux_variables"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
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


