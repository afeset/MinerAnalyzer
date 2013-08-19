



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.sys.blinky.example.oper.oper.config_a.op_v.op_v_oper_data_gen import OpVOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef





from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.blinky_op_y_oper_list_gen import BlinkyOperOpYList




class BlinkyOperOpVList(BlinkyOperNode):

    _kCallpointName = "op-v-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    
    GET_NEXT_FUNCTOR = 'GET_NEXT_FUNCTOR'


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "op-v-callpoint"
        
        self.myOpY = None
        self.myGetObjectFunctor = None
        
        self.myGetNextFunctor = None
        
        self.myOpY = BlinkyOperOpY(self._log)
        

    def getCallpointName (self):
        return self.kCallpointName

    def setParent (self, parentNode):
        for logFunc in self._log("set-parent").debug2Func(): logFunc("called")
        BlinkyOperNode.setParent(self, parentNode)

        
        self.myOpY.setParent(self)
        

        return ReturnCodes.kOk

    def distributeConfigObjectToDescendants (self, configObj):
        for logFunc in self._log("distribute-config-object-to-descendants").debug3Func(): logFunc("called. configObj=%s", configObj)

        
        res = self.myOpY.setConfigObj(configObj)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("distribute-config-object-to-descendants-opy-failed").errorFunc(): logFunc(
                "myOpY->setConfigObj() failed. res=%s, configObj=%s", res, configObj)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def getOperRelativePath (self, operRelativePath):
        for logFunc in self._log("get-oper-relative-path").debug3Func(): logFunc("called")
        
        val = Value()
        val.setXmlTag(("op-v", "http://qwilt.com/model/oper", "oper"))
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
            
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "op-y"):
                    for logFunc in self._log("set-oper-data-requested-fields-opy-requested").debug3Func(): logFunc(
                        "op-y requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOpYRequested()
                    res = self.myOpY.setOperDataRequestedFields(operData.myOpY, keyPath)
                    if res != ReturnCodes.kOk:
                        for logFunc in self._log("set-oper-data-requested-fields-opy-failed").errorFunc(): logFunc(
                            "myOpY.setOperDataRequestedFields() failed. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                        return ReturnCodes.kGeneralError
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "value-op-v1"):
                    for logFunc in self._log("set-oper-data-requested-fields-valueopv1-requested").debug3Func(): logFunc(
                        "value-op-v1 requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setValueOpV1Requested()
                
            else:
                for logFunc in self._log("set-oper-data-requested-fields-bad-keypath").errorFunc(): logFunc(
                    "don't know how to handle this keyPath. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                return ReturnCodes.kGeneralError

        for logFunc in self._log("set-oper-data-requested-fields-done").debug3Func(): logFunc("done. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
        return ReturnCodes.kOk

    
    def fillTagValuesOpY (self, keyPath, tagValueList, operData):
        initialListSize = tagValueList.getLen()
        for logFunc in self._log("fill-tag-values-opy").debug3Func(): logFunc("called. operData=%s, keyPath=%s, initialListSize=%d", operData.debugStr(True), keyPath, initialListSize)
        if operData.isOpYRequested() and operData.hasOpY():
            valBegin = Value()
            valBegin.setXmlBegin("op-y", "http://qwilt.com/model/oper", "oper")
            tagValueList.push(("op-y", "http://qwilt.com/model/oper"), valBegin)

            res = self.myOpY.fillTagValues(keyPath, tagValueList, operData.myOpY)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("fill-tag-values-opy-my-internal-failed").errorFunc(): logFunc(
                    "myOpY->fillTagValues() failed. operData=%s, keyPath=%s, initialListSize=%d, tagValueList.getLen()=%d", 
                    operData.debugStr(True), keyPath, initialListSize, tagValueList.getLen())
                while tagValueList.getLen() > initialListSize:
                    tagValueList.pop()
                return ReturnCodes.kGeneralError
            if tagValueList.getLen() == (initialListSize+1):
                # no values were added by opy - rollback the xmltag added
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd("op-y", "http://qwilt.com/model/oper", "oper")
                tagValueList.push(("op-y", "http://qwilt.com/model/oper"), valEnd)

        for logFunc in self._log("fill-tag-values-opy-ended").debug3Func(): logFunc("ended. operData=%s, keyPath=%s, initialListSize=%d, finalListSize=%d",
                                                                                  operData.debugStr(True), keyPath, initialListSize, tagValueList.getLen())
        return ReturnCodes.kOk

    def fillValueOpY (self, value, keyPath, operData):
        for logFunc in self._log("fill-value-opy").debug3Func(): logFunc("called. keyPath=%s, operData=%s", keyPath, operData.debugStr(True))
        if operData.isOpYRequested():
            if operData.hasOpY():
                res = self.myOpY.fillValue(value, keyPath, operData.myOpY)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("fill-value-opy-my-internal-failed").errorFunc(): logFunc(
                        "myOpY->fillValue() failed. keyPath, operData=%s", keyPath, operData.debugStr(True))
                    return ReturnCodes.kGeneralError
            else:
                value.setEmpty()
        for logFunc in self._log("fill-value-opy-ended").debug3Func(): logFunc("ended. keyPath, operData=%s, value=%s", keyPath, operData.debugStr(True), value)
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
        
        if operData.isValueOpV1Requested() and operData.hasValueOpV1():
            val = Value()
            val.setString(operData.valueOpV1)
            tagValueList.push(("value-op-v1", "http://qwilt.com/model/oper"), val)
        
        
        res = self.fillTagValuesOpY(keyPath, tagValueList, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("fill-tag-values-opy-failed").errorFunc(): logFunc(
                "fillTagValuesOpY failed. operData=%s, keyPath=%s, initialListSize=%d", operData.debugStr(True), keyPath, initialListSize)
            return ReturnCodes.kGeneralError
        
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
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "value-op-v1"):
            if operData.isValueOpV1Requested():
                 if operData.hasValueOpV1():
                     value.setString(operData.valueOpV1)
                 else:
                     value.setEmpty()
        
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "op-y"):
            res = self.fillValueOpY(value, keyPath, operData)
            if res != ReturnCodes.kOk:
                for logFunc in self._log("fill-value-opy-failed").errorFunc(): logFunc(
                    "fillValueOpY failed. keyPath=%s, operData=%s", keyPath, operData.debugStr(True))
                return ReturnCodes.kGeneralError
        
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
        operData = OpVOperData()

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
                opV = keyPathValue
                
                
                
                res = self.myGetObjectFunctor(trxContext, 
                                              
                                              opV, 
                                              
                                              operData)
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myGetObjectFunctor.__name__)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("handle-get-request-functor-failed").errorFunc(): logFunc(
                        "functor failed. keyPath=%s, trxContext=%s", keyPath, trxContext)
                    return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def getElement (self, trxContext, keyPath):
        for logFunc in self._log("get-element").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        operData = OpVOperData()
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

        var = ""
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
            nextKeyValue.setString(var)

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
        "dataImportStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_v_oper_data_gen import OpVOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "oper", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "op-v", 
        "namespace": "op_v", 
        "logGroupName": "blinky-op-v-oper_list", 
        "className": "BlinkyOperOpVList", 
        "logModuleName": "a-sys-blinky-example-oper-oper-config-a-op-v-blinky-op-v-oper-list-gen", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.blinky_op_v_oper_list_gen import BlinkyOperOpVList", 
        "callpointName": "op-v-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/model/oper", 
        "dataClassName": "OpVOperData", 
        "getObjArgsNum": 3, 
        "keyLeaf": {
            "varName": "opV", 
            "typeHandler": "handler: StringHandler"
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
            "isCurrent": true, 
            "yangName": "op-v", 
            "namespace": "op_v", 
            "isList": true, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "keyLeaf": {
                "varName": "opV", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "op-v"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyOperOpY", 
            "memberName": "OpY", 
            "yangName": "op-y", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.blinky_op_y_oper_list_gen import BlinkyOperOpYList"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpV1", 
            "yangName": "value-op-v1", 
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


