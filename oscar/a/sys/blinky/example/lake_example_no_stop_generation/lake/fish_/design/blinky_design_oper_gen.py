



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.sys.blinky.example.lake_example.lake.fish_.design.design_oper_data_gen import DesignOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef






from a.infra.net.mac_address import MacAddress
from a.sys.blinky.example.lake_example.lake_example_module_gen import DesignColorT



class BlinkyOperDesign(BlinkyOperNode):

    _kCallpointName = "lake-fish-design-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "lake-fish-design-callpoint"
        
        self.myGetObjectFunctor = None
        
        

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
        val.setXmlTag(("design", "http://qwilt.com/model/lake-example", "lake-example"))
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
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/lake-example", "color"):
                    for logFunc in self._log("set-oper-data-requested-fields-color-requested").debug3Func(): logFunc(
                        "color requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setColorRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/lake-example", "pattern"):
                    for logFunc in self._log("set-oper-data-requested-fields-pattern-requested").debug3Func(): logFunc(
                        "pattern requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setPatternRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/lake-example", "mac-address"):
                    for logFunc in self._log("set-oper-data-requested-fields-macaddress-requested").debug3Func(): logFunc(
                        "mac-address requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setMacAddressRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/lake-example", "line-width"):
                    for logFunc in self._log("set-oper-data-requested-fields-linewidth-requested").debug3Func(): logFunc(
                        "line-width requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setLineWidthRequested()
                
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
        
        if operData.isColorRequested() and operData.hasColor():
            val = Value()
            val.setEnum(operData.color.getValue())
            tagValueList.push(("color", "http://qwilt.com/model/lake-example"), val)
        
        if operData.isPatternRequested() and operData.hasPattern():
            val = Value()
            val.setString(operData.pattern)
            tagValueList.push(("pattern", "http://qwilt.com/model/lake-example"), val)
        
        if operData.isMacAddressRequested() and operData.hasMacAddress():
            val = Value()
            val.setBinary(operData.macAddress.getAddress())
            tagValueList.push(("mac-address", "http://qwilt.com/model/lake-example"), val)
        
        if operData.isLineWidthRequested() and operData.hasLineWidth():
            val = Value()
            val.setInt8(operData.lineWidth)
            tagValueList.push(("line-width", "http://qwilt.com/model/lake-example"), val)
        
        
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
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/lake-example", "color"):
            if operData.isColorRequested():
                 if operData.hasColor():
                     value.setEnum(operData.color.getValue())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/lake-example", "pattern"):
            if operData.isPatternRequested():
                 if operData.hasPattern():
                     value.setString(operData.pattern)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/lake-example", "mac-address"):
            if operData.isMacAddressRequested():
                 if operData.hasMacAddress():
                     value.setBinary(operData.macAddress.getAddress())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/lake-example", "line-width"):
            if operData.isLineWidthRequested():
                 if operData.hasLineWidth():
                     value.setInt8(operData.lineWidth)
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
        operData = DesignOperData()

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
                
                
                
                
                
                res = self.myGetObjectFunctor(trxContext, 
                                              
                                              
                                              operData)
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myGetObjectFunctor.__name__)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("handle-get-request-functor-failed").errorFunc(): logFunc(
                        "functor failed. keyPath=%s, trxContext=%s", keyPath, trxContext)
                    return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def getElement (self, trxContext, keyPath):
        for logFunc in self._log("get-element").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        operData = DesignOperData()
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


    def setBasicFunctors (self, getObjFunctor):
        if self.myIsActive:
            for logFunc in self._log("set-basic-functor-active").errorFunc(): logFunc("illegal when blinky active.")
            return

        self.myGetObjectFunctor = getObjFunctor
        self.myFunctorsSet = True







"""
Extracted from the below data: 
{
    "node": {
        "dataImportStatement": "from a.sys.blinky.example.lake_example.lake.fish_.design.design_oper_data_gen import DesignOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "lake-example", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "design", 
        "namespace": "design", 
        "logGroupName": "blinky-design-oper", 
        "className": "BlinkyOperDesign", 
        "logModuleName": "a-sys-blinky-example-lake-example-no-stop-generation-lake-fish--design-blinky-design-oper-gen", 
        "importStatement": "from a.sys.blinky.example.lake_example_no_stop_generation.lake.fish_.design.blinky_design_oper_gen import BlinkyOperDesign", 
        "callpointName": "lake-fish-design-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
        "dataClassName": "DesignOperData", 
        "getObjArgsNum": 2, 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "lake", 
            "namespace": "lake", 
            "isList": true, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "lake", 
                "defaultVal": null, 
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
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "fish_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fish_"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "design", 
            "namespace": "design", 
            "isCurrent": true, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "design"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "pattern", 
            "yangName": "pattern", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "lineWidth", 
            "yangName": "line-width", 
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
        "lake_example_no_stop_generation"
    ], 
    "createTime": "2013"
}
"""


