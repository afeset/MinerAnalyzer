


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

from fish__maapi_list_base_gen import FishMaapiListBase
from fish__maapi_gen import BlinkyFishMaapi

class BlinkyFishMaapiList(FishMaapiListBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-fish_")
        self.domain = None

        self.fish_s = {}
        self.fish_Keys = []

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def newFish_ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-fish_').debug3Func(): logFunc('called.')
        fish_ = BlinkyFishMaapi(self._log)
        fish_.init(self.domain)
        return fish_

    def setFish_Obj (self, key, fish_Obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-fish_-obj').debug3Func(): logFunc('called. key=%s, fish_Obj=%s', key, fish_Obj)
        if key not in self.fish_s:
            self.fish_Keys.append(key)
        self.fish_s[str(key)] = fish_Obj

    def getFish_Obj (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-fish_-obj').debug3Func(): logFunc('called. key=%s', key)
        if str(key) in self.fish_s.keys():
            for logFunc in self._log('get-fish_-obj-done').debug3Func(): logFunc('Done. found key=%s, obj=%s', key, self.fish_s[str(key)])
            return self.fish_s[str(key)]
        for logFunc in self._log('get-fish_-obj-missing').errorFunc(): logFunc('fish_ %s not in fish_s. existing items: %s', key, self.fish_s.keys())
        return None

    def deleteFish_ (self, key):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('delete-fish_').debug3Func(): logFunc('called. key=%s', key)
        if str(key) not in self.fish_Keys:
            for logFunc in self._log('delete-fish_-not-found').warningFunc(): logFunc('key=%s is missing from the fish_Keys list', key)
            if str(key) in self.fish_s.keys():
                # internal problem - list & dictionary are not synced
                for logFunc in self._log('delete-fish_-not-found-but-in-dict').errorFunc(): logFunc('fish_s dictionary & fish_Keys list are out-of-sync. key %s exists in dict but not in list', key)
            return ReturnCodes.kGeneralError
        if str(key) not in self.fish_s.keys():
            # internal problem - list & dictionary are not synced
            for logFunc in self._log('delete-fish_-not-found-but-in-list').errorFunc(): logFunc('fish_s dictionary & fish_Keys list are out-of-sync. key %s exists in list but not in dict', key)
            return ReturnCodes.kGeneralError

        self.fish_Keys.remove(str(key))
        del self.fish_s[str(key)]

    def hasFish_Obj (self, key):
        self.myInitGuard.isInitOrCrash()
        has = False
        if str(key) in self.fish_s.keys():
            if self.fish_s[str(key)]:
                has = True
        for logFunc in self._log('has-fish_-done').debug3Func(): logFunc('done. key=%s exists=%s', key, has)
        return has

    def getListKeys (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-list-keys').debug3Func(): logFunc('called. keys=%s', [str(x) for x in self.fish_Keys])
        return self.fish_Keys

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called.')
        for fish_ in self.fish_s.values():
            fish_.requestConfigAndOper()

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called.')
        for fish_ in self.fish_s.values():
            fish_.requestConfig()

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called.')
        for fish_ in self.fish_s.values():
            fish_.requestOper()

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called.')
        for fish_ in self.fish_s.values():
            fish_.clearAllRequested()

    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')
        for fish_ in self.fish_s.values():
            if fish_:
                fish_._clearAllReadData()

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        for key in self.fish_s.keys():
            if self.fish_s[key]:
                self.fish_s[key].clearAllSet()
            else:
                self.fish_Keys.remove(str(key))
                del self.fish_s[str(key)]

    def _getSelfKeyPath (self, lake
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS. junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()

        
        
        
        
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
                      
                      , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-list-keys').debug3Func(): logFunc('called')

        # clear the old map
        self.fish_s = {}
        self.fish_Keys = []

        keyPath = self._getSelfKeyPath(lake, 
                                       
                                       None)

        xmlVal = Value()
        xmlVal.setXmlTag(("fish", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPostfix(xmlVal)

        keys = []

        res = self.domain.readMaapiKeys(keyPath, keys, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-list-keys-domain-failed').errorFunc(): logFunc('domain.readMaapiKeys() failed')
            return ReturnCodes.kGeneralError

        for key in keys:
            self.fish_Keys.append(key.getCannonicalStr())
            self.fish_s[key.getCannonicalStr()] = None

        return ReturnCodes.kOk

    def write (self
               , lake
               , trxContext=None
               ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(lake, 
                                   trxContext)

    def read (self
              , lake
              
              , trxContext=None):
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lake, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , lake
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lake, 
                                  True,
                                  trxContext)

    def _internalWrite (self, 
                        lake, 
                        
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
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(lake, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       lake, 
                       
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
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        for key in self.fish_s.keys():
            if self.fish_s[key]:
                res = self.fish_s[key]._collectItemsToDelete(lake, 
                                                                     
                                                                     key,
                                                                     itemsToDelete)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('collect-items-to-delete-fish_-failed').errorFunc(): logFunc('fish_Obj._collectItemsToDelete() failed. key=%s. PARAMS', key)
                    return ReturnCodes.kGeneralError

            else:
                keyPath = self._getSelfKeyPath(lake, 
                                               
                                               None)
                xmlVal = Value()
                xmlVal.setXmlTag(("fish", "http://qwilt.com/model/lake-example", "lake-example"))
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

        for key in self.fish_s.keys():
            if self.fish_s[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("fish", "http://qwilt.com/model/lake-example", "lake-example")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("id", "http://qwilt.com/model/lake-example"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.fish_s[key]._fillWriteTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-write-tag-values-fish_-failed').errorFunc(): logFunc('fish_._fillWriteTagValues() failed. key=%s', key)
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

        for key in self.fish_s.keys():
            if self.fish_s[key]:
                valBegin = Value()
                (tag, ns, prefix) = ("fish", "http://qwilt.com/model/lake-example", "lake-example")
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)

                valKey = Value()
                valKey.setString(key)
                tagValueList.push(("id", "http://qwilt.com/model/lake-example"), valKey)

                tagValueListLen = tagValueList.getLen()

                res = self.fish_s[key]._fillReadTagValues(tagValueList)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('fill-read-tag-values-fish_-failed').errorFunc(): logFunc('fish_._fillReadTagValues() failed. key=%s', key)
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

        for key in self.fish_s.keys():
            if self.fish_s[key]:
                ((tag, ns), valBegin) = tagValueList.popFront()
                if (tag != "fish") or \
                    (ns != "http://qwilt.com/model/lake-example") or \
                    (valBegin.getType() != Value.kXmlBegin):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                            "fish", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                            tag, ns, valBegin.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valKey) = tagValueList.popFront()
                if (tag != "id") or \
                    (ns != "http://qwilt.com/model/lake-example"):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-key').errorFunc(): logFunc('got unexpected tag-value for key. expected: (%s, %s), got: (%s, %s)',
                                                                          "id", "http://qwilt.com/model/lake-example", tag, ns)
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                key = valKey.asString()
                if res != ReturnCodes.kOk:
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                res = self.fish_s[key]._readTagValues(tagValueList, readAllOrFail)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log('read-tag-values-fish_-failed').errorFunc(): logFunc('fish_._readTagValues() failed. key=%s', key)
                    if readAllOrFail:
                        self._clearAllReadData()
                    return ReturnCodes.kGeneralError

                ((tag, ns), valEnd) = tagValueList.popFront()
                if (tag != "fish") or \
                    (ns != "http://qwilt.com/model/lake-example") or \
                    (valEnd.getType() != Value.kXmlEnd):
                    for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                          "fish", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                            tag, ns, valEnd.getType())
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. tagValueList=%s, readAllOrFail=%s', tagValueList, readAllOrFail)
        return ReturnCodes.kOk

"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyFishMaapi", 
        "name": "fish_", 
        "keyLeaf": {
            "varName": "fish_", 
            "yangName": "id", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "fish", 
        "namespace": "fish_", 
        "moduleYangNamespacePrefix": "lake-example", 
        "className": "FishMaapiList", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.fish__maapi_list_gen import FishMaapiList", 
        "baseClassName": "FishMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
        "containerModule": "fish__maapi_gen", 
        "baseModule": "fish__maapi_list_base_gen"
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
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "mood", 
            "yangName": "mood", 
            "className": "BlinkyMoodMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.mood.mood_maapi_list_gen import BlinkyMoodMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "antenna", 
            "yangName": "antenna", 
            "className": "BlinkyAntennaMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.antenna_maapi_list_gen import BlinkyAntennaMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "testGenerationUnderscoreList", 
            "yangName": "test-generation_underscore", 
            "className": "BlinkyTestGenerationUnderscoreMaapiList", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.test_generation_underscore.test_generation_underscore_maapi_list_list_gen import BlinkyTestGenerationUnderscoreMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "design", 
            "yangName": "design", 
            "className": "BlinkyDesignMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.design.design_maapi_list_gen import BlinkyDesignMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "transparentContainer", 
            "yangName": "transparent-container", 
            "className": "BlinkyTransparentContainerMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.transparent_container.transparent_container_maapi_list_gen import BlinkyTransparentContainerMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "finNumber", 
            "yangName": "fin-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "ip6", 
            "yangName": "ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
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
            "lake_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "finNumber", 
            "yangName": "fin-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "ip6", 
            "yangName": "ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
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


