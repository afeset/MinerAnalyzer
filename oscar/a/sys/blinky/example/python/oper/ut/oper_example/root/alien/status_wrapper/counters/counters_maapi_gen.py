


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

from counters_maapi_base_gen import CountersMaapiBase




class BlinkyCountersMaapi(CountersMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-counters")
        self.domain = None

        

        
        self.strTestRequested = False
        self.strTest = None
        self.strTestSet = False
        
        self.moodRequested = False
        self.mood = None
        self.moodSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStrTest(True)
        
        self.requestMood(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStrTest(False)
        
        self.requestMood(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStrTest(True)
        
        self.requestMood(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStrTest(False)
        
        self.requestMood(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , alien
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(alien, trxContext)

    def read (self
              , alien
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(alien, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , alien
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(alien, 
                                  True,
                                  trxContext)



    def requestStrTest (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-strtest').debug3Func(): logFunc('called. requested=%s', requested)
        self.strTestRequested = requested
        self.strTestSet = False

    def isStrTestRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-strtest-requested').debug3Func(): logFunc('called. requested=%s', self.strTestRequested)
        return self.strTestRequested

    def getStrTest (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-strtest').debug3Func(): logFunc('called. self.strTestSet=%s, self.strTest=%s', self.strTestSet, self.strTest)
        if self.strTestSet:
            return self.strTest
        return None

    def hasStrTest (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-strtest').debug3Func(): logFunc('called. self.strTestSet=%s, self.strTest=%s', self.strTestSet, self.strTest)
        if self.strTestSet:
            return True
        return False

    def setStrTest (self, strTest):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-strtest').debug3Func(): logFunc('called. strTest=%s, old=%s', strTest, self.strTest)
        self.strTestSet = True
        self.strTest = strTest

    def requestMood (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mood').debug3Func(): logFunc('called. requested=%s', requested)
        self.moodRequested = requested
        self.moodSet = False

    def isMoodRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mood-requested').debug3Func(): logFunc('called. requested=%s', self.moodRequested)
        return self.moodRequested

    def getMood (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mood').debug3Func(): logFunc('called. self.moodSet=%s, self.mood=%s', self.moodSet, self.mood)
        if self.moodSet:
            return self.mood
        return None

    def hasMood (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mood').debug3Func(): logFunc('called. self.moodSet=%s, self.mood=%s', self.moodSet, self.mood)
        if self.moodSet:
            return True
        return False

    def setMood (self, mood):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mood').debug3Func(): logFunc('called. mood=%s, old=%s', mood, self.mood)
        self.moodSet = True
        self.mood = mood


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.strTest = 0
        self.strTestSet = False
        
        self.mood = 0
        self.moodSet = False
        

    def _getSelfKeyPath (self, alien
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", "oe"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status-wrapper", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", "oe"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(alien);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alien", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", "oe"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("root", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", "oe"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        alien, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(alien, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(alien, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       alien, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(alien, 
                                       
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               alien, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isStrTestRequested():
            valStrTest = Value()
            valStrTest.setEmpty()
            tagValueList.push(("str-test", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"), valStrTest)
        
        if self.isMoodRequested():
            valMood = Value()
            valMood.setEmpty()
            tagValueList.push(("mood", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"), valMood)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isStrTestRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "str-test") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-strtest').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "strTest", "str-test", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-str-test-bad-value').infoFunc(): logFunc('strTest not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStrTest(tempVar)
            for logFunc in self._log('read-tag-values-str-test').debug3Func(): logFunc('read strTest. strTest=%s, tempValue=%s', self.strTest, tempValue.getType())
        
        if self.isMoodRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mood") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mood').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mood", "mood", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mood-bad-value').infoFunc(): logFunc('mood not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMood(tempVar)
            for logFunc in self._log('read-tag-values-mood').debug3Func(): logFunc('read mood. mood=%s, tempValue=%s', self.mood, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.status_wrapper.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oe", 
            "yangName": "root", 
            "namespace": "root", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "name": "root"
        }, 
        {
            "moduleYangNamespacePrefix": "oe", 
            "isCurrent": false, 
            "yangName": "alien", 
            "namespace": "alien", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "keyLeaf": {
                "varName": "alien", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "alien"
        }, 
        {
            "moduleYangNamespacePrefix": "oe", 
            "yangName": "status-wrapper", 
            "namespace": "status_wrapper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "name": "status-wrapper"
        }, 
        {
            "moduleYangNamespacePrefix": "oe", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "strTest", 
            "yangName": "str-test", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "mood", 
            "yangName": "mood", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "python", 
            "oper", 
            "ut", 
            "oper_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "strTest", 
            "yangName": "str-test", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "mood", 
            "yangName": "mood", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


