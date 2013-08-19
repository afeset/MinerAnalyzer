



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.sys.blinky.example.oper.oper.config_a.op_b.op_c.op_c_oper_data_gen import OpCOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef






import struct



class BlinkyOperOpCList(BlinkyOperNode):

    _kCallpointName = "op-b-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    
    GET_NEXT_FUNCTOR = 'GET_NEXT_FUNCTOR'


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "op-b-callpoint"
        
        self.myGetObjectFunctor = None
        
        self.myGetNextFunctor = None
        

    def getCallpointName (self):
        return self.kCallpointName

    def setParent (self, parentNode):
        for logFunc in self._log("set-parent").debug2Func(): logFunc("called")
        BlinkyOperNode.setParent(self, parentNode)

        

        return ReturnCodes.kOk

    def distributeConfigObjectToDescendants (self, configObj):
        for logFunc in self._log("distribute-config-object-to-descendants").debug3Func(): logFunc("called. configObj=%s", configObj)

        
        return ReturnCodes.kOk

    def getOperRelativePath (self, operRelativePath):
        for logFunc in self._log("get-oper-relative-path").debug3Func(): logFunc("called")
        
        val = Value()
        val.setXmlTag(("op-b", "http://qwilt.com/model/oper", "oper"))
        operRelativePath.addKeyPathPostfix(val)
        
        val = Value()
        val.setXmlTag(("op-c", "http://qwilt.com/model/oper", "oper"))
        operRelativePath.addKeyPathPostfix(val)
        
        for logFunc in self._log("getOperRelativePath-done").debug3Func(): logFunc("done. operRelativePath=%s", operRelativePath)


    def setOperDataRequestedFields (self, operData, keyPath):
        __pychecker__="maxbranches=100 maxlines=500"
        for logFunc in self._log("set-oper-data-requested-fields").debug3Func(): logFunc("called. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
        flattenedSelfKeyPath = self.myKeyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        requestedKeyPath = keyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        
        if requestedKeyPath.isEqual(flattenedSelfKeyPath) or (requestedKeyPath.getLen() <= flattenedSelfKeyPath.getLen()):
        
            operData.setAllRequested()
        else:
            
            for logFunc in self._log("set-oper-data-requested-fields-checking-fields").debug3Func(): logFunc("requestedKeyPath=%s, flattenedSelfKeyPath=%s", requestedKeyPath, flattenedSelfKeyPath)
            if requestedKeyPath.getLen() > flattenedSelfKeyPath.getLen():
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "ip-val"):
                    for logFunc in self._log("set-oper-data-requested-fields-ipval-requested").debug3Func(): logFunc(
                        "ip-val requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setIpValRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "id"):
                    for logFunc in self._log("set-oper-data-requested-fields-id-requested").debug3Func(): logFunc(
                        "id requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setIdRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "val"):
                    for logFunc in self._log("set-oper-data-requested-fields-val-requested").debug3Func(): logFunc(
                        "val requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setValRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "ip-prefix-val"):
                    for logFunc in self._log("set-oper-data-requested-fields-ipprefixval-requested").debug3Func(): logFunc(
                        "ip-prefix-val requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setIpPrefixValRequested()
                
            else:
                for logFunc in self._log("set-oper-data-requested-fields-bad-keypath").errorFunc(): logFunc(
                    "don't know how to handle this keyPath. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                return ReturnCodes.kGeneralError

        for logFunc in self._log("set-oper-data-requested-fields-done").debug3Func(): logFunc("done. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
        return ReturnCodes.kOk

    

    def fillTagValues (self, keyPath, tagValueList, operData):
        initialListSize = tagValueList.getLen()
        for logFunc in self._log("fill-tag-values").debug3Func(): logFunc("called. operData=%s, keyPath=%s, initialListSize=%d", operData.debugStr(True), keyPath, initialListSize)
        # fill tag values up to current
        if self.myKeyPath.isEqualLen(keyPath, keyPath.getLen()):
            i = keyPath.getLen()
            while i < self.myKeyPath.getLen():
                valBegin = Value()
                (tag, ns, prefix) = self.myKeyPath.getAt(i).asXmlTag()
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)
                for logFunc in self._log("fill-tag-values-adding").debug3Func(): logFunc("adding xml begin. i=%d, valBegin=%s, self.myKeyPath.getLen()=%d", i, valBegin, self.myKeyPath.getLen())
                i+=1
        
        if operData.isIpValRequested() and operData.hasIpVal():
            val = Value()
            val.setIPv4(operData.ipVal)
            tagValueList.push(("ip-val", "http://qwilt.com/model/oper"), val)
        
        if operData.isIdRequested() and operData.hasId():
            val = Value()
            val.setInt64(operData.id)
            tagValueList.push(("id", "http://qwilt.com/model/oper"), val)
        
        if operData.isValRequested() and operData.hasVal():
            val = Value()
            val.setInt64(operData.val)
            tagValueList.push(("val", "http://qwilt.com/model/oper"), val)
        
        if operData.isIpPrefixValRequested() and operData.hasIpPrefixVal():
            val = Value()
            val.setIPv4Prefix(operData.ipPrefixVal)
            tagValueList.push(("ip-prefix-val", "http://qwilt.com/model/oper"), val)
        
        
        if self.myKeyPath.isEqualLen(keyPath, keyPath.getLen()):
            i = self.myKeyPath.getLen() - 1
            while i >= keyPath.getLen():
                valEnd = Value()
                (tag, ns, prefix) = self.myKeyPath.getAt(i).asXmlTag()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
                i-=1

        for logFunc in self._log("fill-tag-values-ended").debug3Func(): logFunc("ended. operData=%s, keyPath=%s, initialListSize=%d, finalListSize=%d",
                                                  operData.debugStr(True), keyPath, initialListSize, tagValueList.getLen())
        return ReturnCodes.kOk

    def fillValue (self, value, keyPath, operData):
        __pychecker__="maxbranches=100 maxlines=500"
        for logFunc in self._log("fill-value").debug3Func(): logFunc("called. keyPath=%s, operData=%s", keyPath, operData.debugStr(True))
        flattenedSelfKeyPath = self.myKeyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        requestedKeyPath = keyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "ip-val"):
            if operData.isIpValRequested():
                 if operData.hasIpVal():
                     value.setIPv4(operData.ipVal)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "id"):
            if operData.isIdRequested():
                 if operData.hasId():
                     value.setInt64(operData.id)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "val"):
            if operData.isValRequested():
                 if operData.hasVal():
                     value.setInt64(operData.val)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "ip-prefix-val"):
            if operData.isIpPrefixValRequested():
                 if operData.hasIpPrefixVal():
                     value.setIPv4Prefix(operData.ipPrefixVal)
                 else:
                     value.setEmpty()
        
        
        for logFunc in self._log("fill-value-ended").debug3Func(): logFunc("ended. keyPath=%s, operData=%s, value=%s", keyPath, operData.debugStr(True), value)
        return ReturnCodes.kOk


    def replyObject (self, dpTrxCtx, keyPath, operData):
        for logFunc in self._log("reply-object").debug3Func(): logFunc("called. dpTrxCtx=%s, operData=%s, keyPath=%s", dpTrxCtx, operData.debugStr(True), keyPath)
        tagValueList = TagValues()
        res = self.fillTagValues(keyPath, tagValueList, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-object-fill-tag-values-failed").errorFunc(): logFunc(
                "fillTagValues() failed. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
            return ReturnCodes.kGeneralError
        res = self.myDomain.sendTagValues(dpTrxCtx, tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-object-send-tag-values-failed").errorFunc(): logFunc(
                "myDomain.sendTagValues() failed. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def replyElement (self, dpTrxCtx, keyPath, operData):
        for logFunc in self._log("reply-element").debug3Func(): logFunc("called. dpTrxCtx=%s, operData=%s, keyPath=%s", dpTrxCtx, operData.debugStr(True), keyPath)
        val = Value()
        res = self.fillValue(val, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-element-fill-value-failed").errorFunc(): logFunc(
                "fillValue() failed. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
            return ReturnCodes.kGeneralError
        res = self.myDomain.sendValue(dpTrxCtx, val)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-element-send-value-failed").errorFunc(): logFunc(
                "myDomain.sendValue() failed. operData=%s, keyPath=%s, value=%s", operData.debugStr(True), keyPath, val)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def getObject (self, trxContext, keyPath):
        for logFunc in self._log("get-object").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)
        operData = OpCOperData()

        res = self.handleGetRequest(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-object-handle-get-request-failed").errorFunc(): logFunc(
                "handleGetRequest() failed. operData=%s, keyPath=%s, trxContext=%s", operData.debugStr(True), keyPath, trxContext)
            return ReturnCodes.kGeneralError

        res = self.replyObject(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-object-reply-object-failed").errorFunc(): logFunc(
                "handleGetRequest() failed. operData=%s, keyPath=%s, trxContext=%s", operData.debugStr(True), keyPath, trxContext)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def handleGetRequest (self, trxContext, keyPath, operData):
        for logFunc in self._log("handle-get-request").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        

        res = self.setOperDataRequestedFields(operData, keyPath)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("handle-get-request-set-oper-data-requested-fields-failed").errorFunc(): logFunc(
                "setOperDataRequestedFields() failed. keyPath=%s, trxContext=%s", keyPath, trxContext)
            return ReturnCodes.kGeneralError

        if self.myIsActive:
            if self.myGetObjectFunctor:
                timeoutGuardName = str(self.myKeyPath) + "-" + "get-object-functor";
                timeoutGuard = TimeoutGuard(self._log, timeoutGuardName, 
                                            self.getFunctorTimeout(self.GET_OBJ_FUNCTOR), 
                                            self.getFunctorMildTimeout(self.GET_OBJ_FUNCTOR))
                
                
                index = self.myKeyPath.getLen() - 0
                for logFunc in self._log("handle-get-request-extracting-data").debug3Func(): logFunc(
                    "index=%d, keyPath[index]=%s", index, keyPath.getAt(index))
                keyPathValue = keyPath.getAt(index).getValue()
                opC = keyPathValue
                
                
                
                
                res = self.myGetObjectFunctor(trxContext, 
                                              
                                              opC, 
                                              
                                              operData)
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myGetObjectFunctor.__name__)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("handle-get-request-functor-failed").errorFunc(): logFunc(
                        "functor failed. keyPath=%s, trxContext=%s", keyPath, trxContext)
                    return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def getElement (self, trxContext, keyPath):
        for logFunc in self._log("get-element").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        operData = OpCOperData()
        res = self.handleGetRequest(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-element-handle-get-request-failed").errorFunc(): logFunc(
                "handleGetRequest() failed. keyPath=%s, trxContext=%s, operData=%s", keyPath, trxContext, operData.debugStr(True))
            return ReturnCodes.kGeneralError

        res = self.replyElement(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-element-reply-element-failed").errorFunc(): logFunc(
                "replyElement() failed. keyPath=%s, trxContext=%s, operData=%s", keyPath, trxContext, operData.debugStr(True))
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk



    def setBasicFunctors (self, getObjFunctor, getNextFunctor):
        if self.myIsActive:
            for logFunc in self._log("set-basic-functors-active").errorFunc(): logFunc("illegal when blinky is active.")
        self.myGetObjectFunctor = getObjFunctor
        self.myGetNextFunctor = getNextFunctor
        self.myFunctorsSet = True





    def getNext (self, trxContext, keypath, next):
        for logFunc in self._log("get-next").debug3Func(): logFunc("called. keypath=%s, next=%s, trxContext=%s", keypath, next, trxContext)

        var = 0
        isCompleted = True
        if self.myIsActive:
            if self.myGetNextFunctor:
                timeoutGuardName = str(self.myKeyPath) + "-" + "get-next-functor"
                
                
                
                
                
                timeoutGuard = TimeoutGuard(self._log, timeoutGuardName, 
                                            self.getFunctorTimeout(self.GET_NEXT_FUNCTOR), 
                                            self.getFunctorMildTimeout(self.GET_NEXT_FUNCTOR))
                var_PBR = PassByRef(var)
                next_PBR = PassByRef(next)
                isCompleted_PBR = PassByRef(None)
                res = self.myGetNextFunctor(trxContext, 
                                            
                                            var_PBR,
                                            next_PBR,
                                            isCompleted_PBR)
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myGetNextFunctor.__name__)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("get-next-functor-failed").errorFunc(): logFunc(
                        "functor failed. res=%s, keypath=%s, trxContext=%s", res, keypath, trxContext)
                    return ReturnCodes.kGeneralError
                var = var_PBR.value()
                next = next_PBR.value()
                isCompleted = isCompleted_PBR.value()
                for logFunc in self._log("get-next-send-next-key-functor-returned").debug3Func(): logFunc(
                    "functor returned. keypath=%s, trxContext=%s, var=%s, next=%s, isCompeted=%s", 
                    keypath, trxContext, var, next, isCompleted)

        nextKeyValue = Value()
        if isCompleted == True:
            nextKeyValue.setEmpty()
        else:
            nextKeyValue.setInt64(var)

        res = self.myDomain.sendNextKeyValue(trxContext, nextKeyValue, next)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-next-send-next-key-value-failed").errorFunc(): logFunc(
                "domain.sendNextKeyValue() failed. res=%s, keypath=%s, trxContext=%s, nextKeyValue=%s, next=%s", 
                res, keypath, trxContext, nextKeyValue, next)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk;



"""
Extracted from the below data: 
{
    "node": {
        "dataImportStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_c.op_c_oper_data_gen import OpCOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "oper", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "op-c", 
        "namespace": "op_c", 
        "logGroupName": "blinky-op-c-oper_list", 
        "className": "BlinkyOperOpCList", 
        "logModuleName": "a-sys-blinky-example-oper-oper-config-a-op-b-op-c-blinky-op-c-oper-list-gen", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_c.blinky_op_c_oper_list_gen import BlinkyOperOpCList", 
        "callpointName": "op-b-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/model/oper", 
        "dataClassName": "OpCOperData", 
        "getObjArgsNum": 3, 
        "keyLeaf": {
            "varName": "opC", 
            "typeHandler": "handler: IntHandler"
        }, 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "config-a", 
            "namespace": "config_a", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "config-a"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "op-b", 
            "namespace": "op_b", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-b"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "isCurrent": true, 
            "yangName": "op-c", 
            "namespace": "op_c", 
            "isList": true, 
            "isOper": true, 
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
    "leaves": [
        {
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ipVal", 
            "yangName": "ip-val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "val", 
            "yangName": "val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
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
    "env": [
        "a", 
        "sys", 
        "blinky", 
        "example", 
        "oper", 
        "oper"
    ], 
    "createTime": "2013"
}
"""


