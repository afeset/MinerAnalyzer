



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.op_y_oper_data_gen import OpYOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef









class BlinkyOperOpY(BlinkyOperNode):

    _kCallpointName = "op-v-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "op-v-callpoint"
        
        
        
        

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
        val.setXmlTag(("op-v", "http://qwilt.com/model/oper", "oper"))
        operRelativePath.addKeyPathPostfix(val)
        
        val = Value()
        val.setXmlTag(("op-y", "http://qwilt.com/model/oper", "oper"))
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
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "value-op-y1"):
                    for logFunc in self._log("set-oper-data-requested-fields-valueopy1-requested").debug3Func(): logFunc(
                        "value-op-y1 requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setValueOpY1Requested()
                
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
        
        if operData.isValueOpY1Requested() and operData.hasValueOpY1():
            val = Value()
            val.setString(operData.valueOpY1)
            tagValueList.push(("value-op-y1", "http://qwilt.com/model/oper"), val)
        
        
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
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/model/oper", "value-op-y1"):
            if operData.isValueOpY1Requested():
                 if operData.hasValueOpY1():
                     value.setString(operData.valueOpY1)
                 else:
                     value.setEmpty()
        
        
        for logFunc in self._log("fill-value-ended").debug3Func(): logFunc("ended. keyPath=%s, operData=%s, value=%s", keyPath, operData.debugStr(True), value)
        return ReturnCodes.kOk






"""
Extracted from the below data: 
{
    "node": {
        "dataImportStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.op_y_oper_data_gen import OpYOperData", 
        "callpointResponsible": false, 
        "moduleYangNamespacePrefix": "oper", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "op-y", 
        "namespace": "op_y", 
        "logGroupName": "blinky-op-y-oper", 
        "className": "BlinkyOperOpY", 
        "logModuleName": "a-sys-blinky-example-oper-oper-config-a-op-v-op-y-blinky-op-y-oper-gen", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.blinky_op_y_oper_gen import BlinkyOperOpY", 
        "callpointName": "op-v-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/model/oper", 
        "dataClassName": "OpYOperData", 
        "getObjArgsNum": 3, 
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
            "isCurrent": false, 
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
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "op-y", 
            "namespace": "op_y", 
            "isCurrent": true, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-y"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpY1", 
            "yangName": "value-op-y1", 
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


