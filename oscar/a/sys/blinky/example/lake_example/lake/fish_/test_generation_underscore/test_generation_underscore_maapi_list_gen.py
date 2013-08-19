


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

from test_generation_underscore_maapi_list_base_gen import TestGenerationUnderscoreMaapiListBase
from test_generation_underscore_maapi_gen import BlinkyTestGenerationUnderscoreMaapi

class BlinkyTestGenerationUnderscoreMaapiList(TestGenerationUnderscoreMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-testGenerationUnderscore")
        self.domain = None

        self.testGenerationUnderscores = {}
        self.testGenerationUnderscoreKeys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newTestGenerationUnderscore (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-testgenerationunderscore').debug3Func(): logFunc('called.')
        testGenerationUnderscore = BlinkyTestGenerationUnderscoreMaapi(self._log)
        testGenerationUnderscore.init(self.domain)
        return testGenerationUnderscore

    def setTestGenerationUnderscoreObj (self, key, testGenerationUnderscoreObj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-testgenerationunderscore-obj').debug3Func(): logFunc('called. key=%s, testGenerationUnderscoreObj=%s', key, testGenerationUnderscoreObj)
        if key not in self.testGenerationUnderscores:
            self.testGenerationUnderscoreKeys.append(key)
        self.testGenerationUnderscores[str(key)] = testGenerationUnderscoreObj

    def getTestGenerationUnderscoreObj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-testgenerationunderscore-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.testGenerationUnderscores.keys():
            for logFunc in self._log('get-testgenerationunderscore-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.testGenerationUnderscores[str(key)])
            return self.testGenerationUnderscores[str(key)]
        for logFunc in self._log('get-testgenerationunderscore-obj-missing').errorFunc(): logFunc('testGenerationUnderscore %s not in testGenerationUnderscores. existing items: %s', key, self.testGenerationUnderscores.keys())
        return None

    def deleteTestGenerationUnderscore (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-testgenerationunderscore').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.testGenerationUnderscoreKeys:
            for logFunc in self._log('delete-testGenerationUnderscore-not-found').warningFunc(): logFunc('key=%s is missing from the testGenerationUnderscoreKeys list', key)
            if str(key) in self.testGenerationUnderscores.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-testgenerationunderscore-not-found-but-in-dict').errorFunc(): logFunc('testGenerationUnderscores dictionary & testGenerationUnderscoreKeys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.testGenerationUnderscores.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-testGenerationUnderscore-not-found-but-in-list').errorFunc(): logFunc('testGenerationUnderscores dictionary & testGenerationUnderscoreKeys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.testGenerationUnderscoreKeys.remove(str(key))
        del self.testGenerationUnderscores[str(key)]

    def hasTestGenerationUnderscoreObj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.testGenerationUnderscores.keys():
            if self.testGenerationUnderscores[str(key)]:
                has = True
        for logFunc in self._log('has-testgenerationunderscore-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.testGenerationUnderscoreKeys])
        return self.testGenerationUnderscoreKeys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for testGenerationUnderscore in self.testGenerationUnderscores.values():
            testGenerationUnderscore.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for testGenerationUnderscore in self.testGenerationUnderscores.values():
            testGenerationUnderscore.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for testGenerationUnderscore in self.testGenerationUnderscores.values():
            testGenerationUnderscore.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for testGenerationUnderscore in self.testGenerationUnderscores.values():
            testGenerationUnderscore.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for testGenerationUnderscore in self.testGenerationUnderscores.values():
            if testGenerationUnderscore:
                testGenerationUnderscore._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.testGenerationUnderscores.keys():
            if self.testGenerationUnderscores[key]:
                self.testGenerationUnderscores[key].clearAllSet()
            else:
                self.testGenerationUnderscoreKeys.remove(str(key))
                del self.testGenerationUnderscores[str(key)]

    def _getSelfKeyPath (self, lake
                         , fish_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
        ancestorVal = Value()
        ancestorVal.setString(fish_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fish", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(lake);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("lake", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def readListKeys (self
                      , lake
                      , fish_
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.testGenerationUnderscores = {}
        self.testGenerationUnderscoreKeys = []

        keyPath = self._getSelfKeyPath(lake, 
                                       fish_, 
                                       
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("test-generation_underscore", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.testGenerationUnderscoreKeys.append(key.getCannonicalStr())
            self.testGenerationUnderscores[key.getCannonicalStr()] = None

        return ReturnCodes.kOk

    def write (self
               , lake
               , fish_
               , trxContext=None
               ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(lake, fish_, 
                                   trxContext)

    def read (self
              , lake
              , fish_
              
              , trxContext=None):
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lake, fish_, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , lake
                       , fish_
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lake, fish_, 
                                  True,
                                  trxContext)

    def _internalWrite (self, 
                        lake, 
                        fish_, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called.')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('internal-write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(lake, 
                                         fish_, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(lake, 
                                       fish_, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       lake, 
                       fish_, 
                       
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

        keyPath = self._getSelfKeyPath(lake, 
                                       fish_, 
                                       
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
                               lake, 
                               fish_, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        for key in self.testGenerationUnderscores.keys():
            if self.testGenerationUnderscores[key]:
                res = self.testGenerationUnderscores[key]._collectItemsToDelete(lake, 
                                                                     fish_, 
                                                                     
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-testGenerationUnderscore-failed').errorFunc(): logFunc('testGenerationUnderscoreObj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(lake, 
                                               fish_, 
                                               
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("test-generation_underscore", "http://qwilt.com/model/lake-example", "lake-example"))
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

        for key in self.testGenerationUnderscores.keys():
            if self.testGenerationUnderscores[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("test-generation_underscore", "http://qwilt.com/model/lake-example", "lake-example")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/model/lake-example"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.testGenerationUnderscores[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-testGenerationUnderscore-failed').errorFunc(): logFunc('testGenerationUnderscore._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.testGenerationUnderscores.keys():
            if self.testGenerationUnderscores[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("test-generation_underscore", "http://qwilt.com/model/lake-example", "lake-example")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("name", "http://qwilt.com/model/lake-example"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.testGenerationUnderscores[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-testGenerationUnderscore-failed').errorFunc(): logFunc('testGenerationUnderscore._fillReadTagValues() failed. key=%s', key)
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

        for key in self.testGenerationUnderscores.keys():
            if self.testGenerationUnderscores[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "test-generation_underscore") or \
                    (ns != "http://qwilt.com/model/lake-example") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "test-generation_underscore", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
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

                res = self.testGenerationUnderscores[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-testGenerationUnderscore-failed').errorFunc(): logFunc('testGenerationUnderscore._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "test-generation_underscore") or \
                    (ns != "http://qwilt.com/model/lake-example") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "test-generation_underscore", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyTestGenerationUnderscoreMaapi", 
        "name": "testGenerationUnderscore", 
        "keyLeaf": {
            "varName": "testGenerationUnderscore", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "test-generation_underscore", 
        "namespace": "test_generation_underscore", 
        "moduleYangNamespacePrefix": "lake-example", 
        "className": "TestGenerationUnderscoreMaapiList", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.test_generation_underscore.test_generation_underscore_maapi_list_gen import TestGenerationUnderscoreMaapiList", 
        "baseClassName": "TestGenerationUnderscoreMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
        "containerModule": "test_generation_underscore_maapi_gen", 
        "baseModule": "test_generation_underscore_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "lake", 
            "namespace": "lake", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "lake", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lake"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "fish", 
            "namespace": "fish_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "fish_", 
                "yangName": "id", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fish_"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": true, 
            "yangName": "test-generation_underscore", 
            "namespace": "test_generation_underscore", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "testGenerationUnderscore", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "test-generation_underscore"
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
        }
    ], 
    "createTime": "2013"
}
"""


