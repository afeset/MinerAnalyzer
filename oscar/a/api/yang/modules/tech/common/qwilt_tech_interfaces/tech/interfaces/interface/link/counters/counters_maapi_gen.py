


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

        

        
        self.resultDownRequested = False
        self.resultDown = None
        self.resultDownSet = False
        
        self.resultUnknownRequested = False
        self.resultUnknown = None
        self.resultUnknownSet = False
        
        self.testsRequested = False
        self.tests = None
        self.testsSet = False
        
        self.resultUpRequested = False
        self.resultUp = None
        self.resultUpSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestResultDown(True)
        
        self.requestResultUnknown(True)
        
        self.requestTests(True)
        
        self.requestResultUp(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestResultDown(False)
        
        self.requestResultUnknown(False)
        
        self.requestTests(False)
        
        self.requestResultUp(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestResultDown(True)
        
        self.requestResultUnknown(True)
        
        self.requestTests(True)
        
        self.requestResultUp(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestResultDown(False)
        
        self.requestResultUnknown(False)
        
        self.requestTests(False)
        
        self.requestResultUp(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , interface
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(interface, trxContext)

    def read (self
              , interface
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  True,
                                  trxContext)



    def requestResultDown (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-resultdown').debug3Func(): logFunc('called. requested=%s', requested)
        self.resultDownRequested = requested
        self.resultDownSet = False

    def isResultDownRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-resultdown-requested').debug3Func(): logFunc('called. requested=%s', self.resultDownRequested)
        return self.resultDownRequested

    def getResultDown (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-resultdown').debug3Func(): logFunc('called. self.resultDownSet=%s, self.resultDown=%s', self.resultDownSet, self.resultDown)
        if self.resultDownSet:
            return self.resultDown
        return None

    def hasResultDown (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-resultdown').debug3Func(): logFunc('called. self.resultDownSet=%s, self.resultDown=%s', self.resultDownSet, self.resultDown)
        if self.resultDownSet:
            return True
        return False

    def setResultDown (self, resultDown):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-resultdown').debug3Func(): logFunc('called. resultDown=%s, old=%s', resultDown, self.resultDown)
        self.resultDownSet = True
        self.resultDown = resultDown

    def requestResultUnknown (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-resultunknown').debug3Func(): logFunc('called. requested=%s', requested)
        self.resultUnknownRequested = requested
        self.resultUnknownSet = False

    def isResultUnknownRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-resultunknown-requested').debug3Func(): logFunc('called. requested=%s', self.resultUnknownRequested)
        return self.resultUnknownRequested

    def getResultUnknown (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-resultunknown').debug3Func(): logFunc('called. self.resultUnknownSet=%s, self.resultUnknown=%s', self.resultUnknownSet, self.resultUnknown)
        if self.resultUnknownSet:
            return self.resultUnknown
        return None

    def hasResultUnknown (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-resultunknown').debug3Func(): logFunc('called. self.resultUnknownSet=%s, self.resultUnknown=%s', self.resultUnknownSet, self.resultUnknown)
        if self.resultUnknownSet:
            return True
        return False

    def setResultUnknown (self, resultUnknown):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-resultunknown').debug3Func(): logFunc('called. resultUnknown=%s, old=%s', resultUnknown, self.resultUnknown)
        self.resultUnknownSet = True
        self.resultUnknown = resultUnknown

    def requestTests (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-tests').debug3Func(): logFunc('called. requested=%s', requested)
        self.testsRequested = requested
        self.testsSet = False

    def isTestsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-tests-requested').debug3Func(): logFunc('called. requested=%s', self.testsRequested)
        return self.testsRequested

    def getTests (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-tests').debug3Func(): logFunc('called. self.testsSet=%s, self.tests=%s', self.testsSet, self.tests)
        if self.testsSet:
            return self.tests
        return None

    def hasTests (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-tests').debug3Func(): logFunc('called. self.testsSet=%s, self.tests=%s', self.testsSet, self.tests)
        if self.testsSet:
            return True
        return False

    def setTests (self, tests):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-tests').debug3Func(): logFunc('called. tests=%s, old=%s', tests, self.tests)
        self.testsSet = True
        self.tests = tests

    def requestResultUp (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-resultup').debug3Func(): logFunc('called. requested=%s', requested)
        self.resultUpRequested = requested
        self.resultUpSet = False

    def isResultUpRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-resultup-requested').debug3Func(): logFunc('called. requested=%s', self.resultUpRequested)
        return self.resultUpRequested

    def getResultUp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-resultup').debug3Func(): logFunc('called. self.resultUpSet=%s, self.resultUp=%s', self.resultUpSet, self.resultUp)
        if self.resultUpSet:
            return self.resultUp
        return None

    def hasResultUp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-resultup').debug3Func(): logFunc('called. self.resultUpSet=%s, self.resultUp=%s', self.resultUpSet, self.resultUp)
        if self.resultUpSet:
            return True
        return False

    def setResultUp (self, resultUp):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-resultup').debug3Func(): logFunc('called. resultUp=%s, old=%s', resultUp, self.resultUp)
        self.resultUpSet = True
        self.resultUp = resultUp


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.resultDown = 0
        self.resultDownSet = False
        
        self.resultUnknown = 0
        self.resultUnknownSet = False
        
        self.tests = 0
        self.testsSet = False
        
        self.resultUp = 0
        self.resultUpSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("link", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(interface);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interfaces", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        interface, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(interface, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       interface, 
                       
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

        keyPath = self._getSelfKeyPath(interface, 
                                       
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
                               interface, 
                               
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

        
        if self.isResultDownRequested():
            valResultDown = Value()
            valResultDown.setEmpty()
            tagValueList.push(("result-down", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valResultDown)
        
        if self.isResultUnknownRequested():
            valResultUnknown = Value()
            valResultUnknown.setEmpty()
            tagValueList.push(("result-unknown", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valResultUnknown)
        
        if self.isTestsRequested():
            valTests = Value()
            valTests.setEmpty()
            tagValueList.push(("tests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTests)
        
        if self.isResultUpRequested():
            valResultUp = Value()
            valResultUp.setEmpty()
            tagValueList.push(("result-up", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valResultUp)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isResultDownRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "result-down") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-resultdown').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "resultDown", "result-down", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-result-down-bad-value').infoFunc(): logFunc('resultDown not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setResultDown(tempVar)
            for logFunc in self._log('read-tag-values-result-down').debug3Func(): logFunc('read resultDown. resultDown=%s, tempValue=%s', self.resultDown, tempValue.getType())
        
        if self.isResultUnknownRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "result-unknown") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-resultunknown').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "resultUnknown", "result-unknown", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-result-unknown-bad-value').infoFunc(): logFunc('resultUnknown not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setResultUnknown(tempVar)
            for logFunc in self._log('read-tag-values-result-unknown').debug3Func(): logFunc('read resultUnknown. resultUnknown=%s, tempValue=%s', self.resultUnknown, tempValue.getType())
        
        if self.isTestsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tests") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-tests').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "tests", "tests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tests-bad-value').infoFunc(): logFunc('tests not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTests(tempVar)
            for logFunc in self._log('read-tag-values-tests').debug3Func(): logFunc('read tests. tests=%s, tempValue=%s', self.tests, tempValue.getType())
        
        if self.isResultUpRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "result-up") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-resultup').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "resultUp", "result-up", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-result-up-bad-value').infoFunc(): logFunc('resultUp not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setResultUp(tempVar)
            for logFunc in self._log('read-tag-values-result-up').debug3Func(): logFunc('read resultUp. resultUp=%s, tempValue=%s', self.resultUp, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.link.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "link", 
            "namespace": "link", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "link"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "resultDown", 
            "yangName": "result-down", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "resultUnknown", 
            "yangName": "result-unknown", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "tests", 
            "yangName": "tests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "resultUp", 
            "yangName": "result-up", 
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
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "resultDown", 
            "yangName": "result-down", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "resultUnknown", 
            "yangName": "result-unknown", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "tests", 
            "yangName": "tests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "resultUp", 
            "yangName": "result-up", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


