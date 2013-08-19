


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

from status_wrapper_maapi_base_gen import StatusWrapperMaapiBase

from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.status_wrapper.counters.counters_maapi_gen import BlinkyCountersMaapi



class BlinkyStatusWrapperMaapi(StatusWrapperMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-statusWrapper")
        self.domain = None

        
        self.countersObj = None
        

        
        self.dummyRequested = False
        self.dummy = None
        self.dummySet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDummy(True)
        
        
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDummy(True)
        
        
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDummy(False)
        
        
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDummy(False)
        
        
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setDummy(None)
        self.dummySet = False
        
        
        if self.countersObj:
            self.countersObj.clearAllSet()
        

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

    def newCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-counters').debug3Func(): logFunc('called.')
        counters = BlinkyCountersMaapi(self._log)
        counters.init(self.domain)
        return counters

    def setCountersObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-counters').debug3Func(): logFunc('called. obj=%s', obj)
        self.countersObj = obj

    def getCountersObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-counters').debug3Func(): logFunc('called. self.countersObj=%s', self.countersObj)
        return self.countersObj

    def hasCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-counters').debug3Func(): logFunc('called. self.countersObj=%s', self.countersObj)
        if self.countersObj:
            return True
        return False



    def requestDummy (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-dummy').debug3Func(): logFunc('called. requested=%s', requested)
        self.dummyRequested = requested
        self.dummySet = False

    def isDummyRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-dummy-requested').debug3Func(): logFunc('called. requested=%s', self.dummyRequested)
        return self.dummyRequested

    def getDummy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-dummy').debug3Func(): logFunc('called. self.dummySet=%s, self.dummy=%s', self.dummySet, self.dummy)
        if self.dummySet:
            return self.dummy
        return None

    def hasDummy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-dummy').debug3Func(): logFunc('called. self.dummySet=%s, self.dummy=%s', self.dummySet, self.dummy)
        if self.dummySet:
            return True
        return False

    def setDummy (self, dummy):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-dummy').debug3Func(): logFunc('called. dummy=%s, old=%s', dummy, self.dummy)
        self.dummySet = True
        self.dummy = dummy


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.countersObj:
            self.countersObj._clearAllReadData()
        

        
        self.dummy = 0
        self.dummySet = False
        

    def _getSelfKeyPath (self, alien
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
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

        
        if self.countersObj:
            res = self.countersObj._collectItemsToDelete(alien, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-counters-failed').errorFunc(): logFunc('countersObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasDummy():
            valDummy = Value()
            if self.dummy is not None:
                valDummy.setInt64(self.dummy)
            else:
                valDummy.setEmpty()
            tagValueList.push(("dummy", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"), valDummy)
        

        
        if self.countersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", "oe")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.countersObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-counters-failed').errorFunc(): logFunc('countersObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isDummyRequested():
            valDummy = Value()
            valDummy.setEmpty()
            tagValueList.push(("dummy", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"), valDummy)
        

        
        if self.countersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", "oe")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.countersObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-counters-failed').errorFunc(): logFunc('countersObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isDummyRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "dummy") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-dummy').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "dummy", "dummy", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-dummy-bad-value').infoFunc(): logFunc('dummy not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDummy(tempVar)
            for logFunc in self._log('read-tag-values-dummy').debug3Func(): logFunc('read dummy. dummy=%s, tempValue=%s', self.dummy, tempValue.getType())
        

        
        if self.countersObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "counters", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.countersObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-counters-failed').errorFunc(): logFunc('countersObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "counters", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "statusWrapper", 
        "namespace": "status_wrapper", 
        "className": "StatusWrapperMaapi", 
        "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.status_wrapper.status_wrapper_maapi_gen import StatusWrapperMaapi", 
        "baseClassName": "StatusWrapperMaapiBase", 
        "baseModule": "status_wrapper_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "name": "status-wrapper"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oe", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.status_wrapper.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "dummy", 
            "yangName": "dummy", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "dummy", 
            "yangName": "dummy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


