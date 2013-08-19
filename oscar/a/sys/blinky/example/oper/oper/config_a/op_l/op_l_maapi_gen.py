


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

from op_l_maapi_base_gen import OpLMaapiBase




class BlinkyOpLMaapi(OpLMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-opL")
        self.domain = None

        

        
        self.configDummyRequested = False
        self.configDummy = None
        self.configDummySet = False
        
        self.valueOpL1Requested = False
        self.valueOpL1 = None
        self.valueOpL1Set = False
        
        self.valueOpL2Requested = False
        self.valueOpL2 = None
        self.valueOpL2Set = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestConfigDummy(True)
        
        
        self.requestValueOpL1(True)
        
        self.requestValueOpL2(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestConfigDummy(True)
        
        
        self.requestValueOpL1(False)
        
        self.requestValueOpL2(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestConfigDummy(False)
        
        
        self.requestValueOpL1(True)
        
        self.requestValueOpL2(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestConfigDummy(False)
        
        
        self.requestValueOpL1(False)
        
        self.requestValueOpL2(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setConfigDummy(None)
        self.configDummySet = False
        
        

    def write (self
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(trxContext)

    def read (self
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
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



    def requestConfigDummy (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-configdummy').debug3Func(): logFunc('called. requested=%s', requested)
        self.configDummyRequested = requested
        self.configDummySet = False

    def isConfigDummyRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-configdummy-requested').debug3Func(): logFunc('called. requested=%s', self.configDummyRequested)
        return self.configDummyRequested

    def getConfigDummy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-configdummy').debug3Func(): logFunc('called. self.configDummySet=%s, self.configDummy=%s', self.configDummySet, self.configDummy)
        if self.configDummySet:
            return self.configDummy
        return None

    def hasConfigDummy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-configdummy').debug3Func(): logFunc('called. self.configDummySet=%s, self.configDummy=%s', self.configDummySet, self.configDummy)
        if self.configDummySet:
            return True
        return False

    def setConfigDummy (self, configDummy):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-configdummy').debug3Func(): logFunc('called. configDummy=%s, old=%s', configDummy, self.configDummy)
        self.configDummySet = True
        self.configDummy = configDummy

    def requestValueOpL1 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-valueopl1').debug3Func(): logFunc('called. requested=%s', requested)
        self.valueOpL1Requested = requested
        self.valueOpL1Set = False

    def isValueOpL1Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-valueopl1-requested').debug3Func(): logFunc('called. requested=%s', self.valueOpL1Requested)
        return self.valueOpL1Requested

    def getValueOpL1 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-valueopl1').debug3Func(): logFunc('called. self.valueOpL1Set=%s, self.valueOpL1=%s', self.valueOpL1Set, self.valueOpL1)
        if self.valueOpL1Set:
            return self.valueOpL1
        return None

    def hasValueOpL1 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-valueopl1').debug3Func(): logFunc('called. self.valueOpL1Set=%s, self.valueOpL1=%s', self.valueOpL1Set, self.valueOpL1)
        if self.valueOpL1Set:
            return True
        return False

    def setValueOpL1 (self, valueOpL1):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-valueopl1').debug3Func(): logFunc('called. valueOpL1=%s, old=%s', valueOpL1, self.valueOpL1)
        self.valueOpL1Set = True
        self.valueOpL1 = valueOpL1

    def requestValueOpL2 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-valueopl2').debug3Func(): logFunc('called. requested=%s', requested)
        self.valueOpL2Requested = requested
        self.valueOpL2Set = False

    def isValueOpL2Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-valueopl2-requested').debug3Func(): logFunc('called. requested=%s', self.valueOpL2Requested)
        return self.valueOpL2Requested

    def getValueOpL2 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-valueopl2').debug3Func(): logFunc('called. self.valueOpL2Set=%s, self.valueOpL2=%s', self.valueOpL2Set, self.valueOpL2)
        if self.valueOpL2Set:
            return self.valueOpL2
        return None

    def hasValueOpL2 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-valueopl2').debug3Func(): logFunc('called. self.valueOpL2Set=%s, self.valueOpL2=%s', self.valueOpL2Set, self.valueOpL2)
        if self.valueOpL2Set:
            return True
        return False

    def setValueOpL2 (self, valueOpL2):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-valueopl2').debug3Func(): logFunc('called. valueOpL2=%s, old=%s', valueOpL2, self.valueOpL2)
        self.valueOpL2Set = True
        self.valueOpL2 = valueOpL2


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.configDummy = 0
        self.configDummySet = False
        
        self.valueOpL1 = 0
        self.valueOpL1Set = False
        
        self.valueOpL2 = 0
        self.valueOpL2Set = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("op-l", "http://qwilt.com/model/oper", "oper"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("config-a", "http://qwilt.com/model/oper", "oper"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
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
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
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
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasConfigDummy():
            valConfigDummy = Value()
            if self.configDummy is not None:
                valConfigDummy.setInt64(self.configDummy)
            else:
                valConfigDummy.setEmpty()
            tagValueList.push(("config-dummy", "http://qwilt.com/model/oper"), valConfigDummy)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isConfigDummyRequested():
            valConfigDummy = Value()
            valConfigDummy.setEmpty()
            tagValueList.push(("config-dummy", "http://qwilt.com/model/oper"), valConfigDummy)
        
        if self.isValueOpL1Requested():
            valValueOpL1 = Value()
            valValueOpL1.setEmpty()
            tagValueList.push(("value-op-l1", "http://qwilt.com/model/oper"), valValueOpL1)
        
        if self.isValueOpL2Requested():
            valValueOpL2 = Value()
            valValueOpL2.setEmpty()
            tagValueList.push(("value-op-l2", "http://qwilt.com/model/oper"), valValueOpL2)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isConfigDummyRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "config-dummy") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-configdummy').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "configDummy", "config-dummy", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-config-dummy-bad-value').infoFunc(): logFunc('configDummy not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setConfigDummy(tempVar)
            for logFunc in self._log('read-tag-values-config-dummy').debug3Func(): logFunc('read configDummy. configDummy=%s, tempValue=%s', self.configDummy, tempValue.getType())
        
        if self.isValueOpL1Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "value-op-l1") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-valueopl1').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "valueOpL1", "value-op-l1", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-value-op-l1-bad-value').infoFunc(): logFunc('valueOpL1 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setValueOpL1(tempVar)
            for logFunc in self._log('read-tag-values-value-op-l1').debug3Func(): logFunc('read valueOpL1. valueOpL1=%s, tempValue=%s', self.valueOpL1, tempValue.getType())
        
        if self.isValueOpL2Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "value-op-l2") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-valueopl2').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "valueOpL2", "value-op-l2", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-value-op-l2-bad-value').infoFunc(): logFunc('valueOpL2 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setValueOpL2(tempVar)
            for logFunc in self._log('read-tag-values-value-op-l2').debug3Func(): logFunc('read valueOpL2. valueOpL2=%s, tempValue=%s', self.valueOpL2, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "opL", 
        "namespace": "op_l", 
        "className": "OpLMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_l.op_l_maapi_gen import OpLMaapi", 
        "baseClassName": "OpLMaapiBase", 
        "baseModule": "op_l_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "config-a", 
            "namespace": "config_a", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "config-a"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "op-l", 
            "namespace": "op_l", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-l"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpL1", 
            "yangName": "value-op-l1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpL2", 
            "yangName": "value-op-l2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "configDummy", 
            "yangName": "config-dummy", 
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
            "oper", 
            "oper"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "configDummy", 
            "yangName": "config-dummy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpL1", 
            "yangName": "value-op-l1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpL2", 
            "yangName": "value-op-l2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


