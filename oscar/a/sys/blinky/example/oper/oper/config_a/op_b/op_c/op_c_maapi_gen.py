


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

from op_c_maapi_base_gen import OpCMaapiBase


import struct


class BlinkyOpCMaapi(OpCMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-opC")
        self.domain = None

        

        
        self.ipValRequested = False
        self.ipVal = None
        self.ipValSet = False
        
        self.idRequested = False
        self.id = None
        self.idSet = False
        
        self.valRequested = False
        self.val = None
        self.valSet = False
        
        self.ipPrefixValRequested = False
        self.ipPrefixVal = None
        self.ipPrefixValSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestIpVal(True)
        
        self.requestId(True)
        
        self.requestVal(True)
        
        self.requestIpPrefixVal(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestIpVal(False)
        
        self.requestId(False)
        
        self.requestVal(False)
        
        self.requestIpPrefixVal(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestIpVal(True)
        
        self.requestId(True)
        
        self.requestVal(True)
        
        self.requestIpPrefixVal(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestIpVal(False)
        
        self.requestId(False)
        
        self.requestVal(False)
        
        self.requestIpPrefixVal(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , opC
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(opC, trxContext)

    def read (self
              , opC
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(opC, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , opC
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(opC, 
                                  True,
                                  trxContext)



    def requestIpVal (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-ipval').debug3Func(): logFunc('called. requested=%s', requested)
        self.ipValRequested = requested
        self.ipValSet = False

    def isIpValRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-ipval-requested').debug3Func(): logFunc('called. requested=%s', self.ipValRequested)
        return self.ipValRequested

    def getIpVal (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ipval').debug3Func(): logFunc('called. self.ipValSet=%s, self.ipVal=%s', self.ipValSet, self.ipVal)
        if self.ipValSet:
            return self.ipVal
        return None

    def hasIpVal (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ipval').debug3Func(): logFunc('called. self.ipValSet=%s, self.ipVal=%s', self.ipValSet, self.ipVal)
        if self.ipValSet:
            return True
        return False

    def setIpVal (self, ipVal):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ipval').debug3Func(): logFunc('called. ipVal=%s, old=%s', ipVal, self.ipVal)
        self.ipValSet = True
        self.ipVal = ipVal

    def requestId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-id').debug3Func(): logFunc('called. requested=%s', requested)
        self.idRequested = requested
        self.idSet = False

    def isIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-id-requested').debug3Func(): logFunc('called. requested=%s', self.idRequested)
        return self.idRequested

    def getId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-id').debug3Func(): logFunc('called. self.idSet=%s, self.id=%s', self.idSet, self.id)
        if self.idSet:
            return self.id
        return None

    def hasId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-id').debug3Func(): logFunc('called. self.idSet=%s, self.id=%s', self.idSet, self.id)
        if self.idSet:
            return True
        return False

    def setId (self, id):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-id').debug3Func(): logFunc('called. id=%s, old=%s', id, self.id)
        self.idSet = True
        self.id = id

    def requestVal (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-val').debug3Func(): logFunc('called. requested=%s', requested)
        self.valRequested = requested
        self.valSet = False

    def isValRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-val-requested').debug3Func(): logFunc('called. requested=%s', self.valRequested)
        return self.valRequested

    def getVal (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-val').debug3Func(): logFunc('called. self.valSet=%s, self.val=%s', self.valSet, self.val)
        if self.valSet:
            return self.val
        return None

    def hasVal (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-val').debug3Func(): logFunc('called. self.valSet=%s, self.val=%s', self.valSet, self.val)
        if self.valSet:
            return True
        return False

    def setVal (self, val):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-val').debug3Func(): logFunc('called. val=%s, old=%s', val, self.val)
        self.valSet = True
        self.val = val

    def requestIpPrefixVal (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-ipprefixval').debug3Func(): logFunc('called. requested=%s', requested)
        self.ipPrefixValRequested = requested
        self.ipPrefixValSet = False

    def isIpPrefixValRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-ipprefixval-requested').debug3Func(): logFunc('called. requested=%s', self.ipPrefixValRequested)
        return self.ipPrefixValRequested

    def getIpPrefixVal (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ipprefixval').debug3Func(): logFunc('called. self.ipPrefixValSet=%s, self.ipPrefixVal=%s', self.ipPrefixValSet, self.ipPrefixVal)
        if self.ipPrefixValSet:
            return self.ipPrefixVal
        return None

    def hasIpPrefixVal (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ipprefixval').debug3Func(): logFunc('called. self.ipPrefixValSet=%s, self.ipPrefixVal=%s', self.ipPrefixValSet, self.ipPrefixVal)
        if self.ipPrefixValSet:
            return True
        return False

    def setIpPrefixVal (self, ipPrefixVal):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ipprefixval').debug3Func(): logFunc('called. ipPrefixVal=%s, old=%s', ipPrefixVal, self.ipPrefixVal)
        self.ipPrefixValSet = True
        self.ipPrefixVal = ipPrefixVal


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.ipVal = 0
        self.ipValSet = False
        
        self.id = 0
        self.idSet = False
        
        self.val = 0
        self.valSet = False
        
        self.ipPrefixVal = 0
        self.ipPrefixValSet = False
        

    def _getSelfKeyPath (self, opC
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setInt64(opC);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("op-c", "http://qwilt.com/model/oper", "oper"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("op-b", "http://qwilt.com/model/oper", "oper"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("config-a", "http://qwilt.com/model/oper", "oper"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        opC, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(opC, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(opC, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       opC, 
                       
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

        keyPath = self._getSelfKeyPath(opC, 
                                       
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
                               opC, 
                               
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

        
        if self.isIpValRequested():
            valIpVal = Value()
            valIpVal.setEmpty()
            tagValueList.push(("ip-val", "http://qwilt.com/model/oper"), valIpVal)
        
        if self.isIdRequested():
            valId = Value()
            valId.setEmpty()
            tagValueList.push(("id", "http://qwilt.com/model/oper"), valId)
        
        if self.isValRequested():
            valVal = Value()
            valVal.setEmpty()
            tagValueList.push(("val", "http://qwilt.com/model/oper"), valVal)
        
        if self.isIpPrefixValRequested():
            valIpPrefixVal = Value()
            valIpPrefixVal.setEmpty()
            tagValueList.push(("ip-prefix-val", "http://qwilt.com/model/oper"), valIpPrefixVal)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isIpValRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ip-val") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-ipval').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "ipVal", "ip-val", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = (tempValue.asIPv4())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ip-val-bad-value').infoFunc(): logFunc('ipVal not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setIpVal(tempVar)
            for logFunc in self._log('read-tag-values-ip-val').debug3Func(): logFunc('read ipVal. ipVal=%s, tempValue=%s', self.ipVal, tempValue.getType())
        
        if self.isIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "id") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-id').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "id", "id", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-id-bad-value').infoFunc(): logFunc('id not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setId(tempVar)
            for logFunc in self._log('read-tag-values-id').debug3Func(): logFunc('read id. id=%s, tempValue=%s', self.id, tempValue.getType())
        
        if self.isValRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "val") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-val').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "val", "val", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-val-bad-value').infoFunc(): logFunc('val not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setVal(tempVar)
            for logFunc in self._log('read-tag-values-val').debug3Func(): logFunc('read val. val=%s, tempValue=%s', self.val, tempValue.getType())
        
        if self.isIpPrefixValRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ip-prefix-val") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-ipprefixval').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "ipPrefixVal", "ip-prefix-val", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = (tempValue.asIPv4Prefix())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ip-prefix-val-bad-value').infoFunc(): logFunc('ipPrefixVal not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setIpPrefixVal(tempVar)
            for logFunc in self._log('read-tag-values-ip-prefix-val').debug3Func(): logFunc('read ipPrefixVal. ipPrefixVal=%s, tempValue=%s', self.ipPrefixVal, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "opC", 
        "namespace": "op_c", 
        "className": "OpCMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_c.op_c_maapi_gen import OpCMaapi", 
        "baseClassName": "OpCMaapiBase", 
        "baseModule": "op_c_maapi_base_gen"
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
            "yangName": "op-b", 
            "namespace": "op_b", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-b"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "isCurrent": true, 
            "yangName": "op-c", 
            "namespace": "op_c", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "keyLeaf": {
                "varName": "opC", 
                "defaultVal": null, 
                "typeHandler": "handler: IntHandler"
            }, 
            "name": "op-c"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ipVal", 
            "yangName": "ip-val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "val", 
            "yangName": "val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "ipPrefixVal", 
            "yangName": "ip-prefix-val", 
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
            "oper", 
            "oper"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ipVal", 
            "yangName": "ip-val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "val", 
            "yangName": "val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "ipPrefixVal", 
            "yangName": "ip-prefix-val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


