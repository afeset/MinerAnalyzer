



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.list.list_oper_data_gen import ListOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef






from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType



class BlinkyOperListList(BlinkyOperNode):

    _kCallpointName = "tech-system-alarms-list-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    
    GET_NEXT_FUNCTOR = 'GET_NEXT_FUNCTOR'


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "tech-system-alarms-list-callpoint"
        
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
        val.setXmlTag(("list", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
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
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "description"):
                    for logFunc in self._log("set-oper-data-requested-fields-description-requested").debug3Func(): logFunc(
                        "description requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setDescriptionRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "severity"):
                    for logFunc in self._log("set-oper-data-requested-fields-severity-requested").debug3Func(): logFunc(
                        "severity requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setSeverityRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "number"):
                    for logFunc in self._log("set-oper-data-requested-fields-number-requested").debug3Func(): logFunc(
                        "number requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setNumberRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "entity"):
                    for logFunc in self._log("set-oper-data-requested-fields-entity-requested").debug3Func(): logFunc(
                        "entity requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setEntityRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "source"):
                    for logFunc in self._log("set-oper-data-requested-fields-source-requested").debug3Func(): logFunc(
                        "source requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setSourceRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "simulated"):
                    for logFunc in self._log("set-oper-data-requested-fields-simulated-requested").debug3Func(): logFunc(
                        "simulated requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setSimulatedRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "name"):
                    for logFunc in self._log("set-oper-data-requested-fields-name-requested").debug3Func(): logFunc(
                        "name requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setNameRequested()
                
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
        
        if operData.isDescriptionRequested() and operData.hasDescription():
            val = Value()
            val.setString(operData.description)
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), val)
        
        if operData.isSeverityRequested() and operData.hasSeverity():
            val = Value()
            val.setEnum(operData.severity.getValue())
            tagValueList.push(("severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), val)
        
        if operData.isNumberRequested() and operData.hasNumber():
            val = Value()
            val.setInt64(operData.number)
            tagValueList.push(("number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), val)
        
        if operData.isEntityRequested() and operData.hasEntity():
            val = Value()
            val.setString(operData.entity)
            tagValueList.push(("entity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), val)
        
        if operData.isSourceRequested() and operData.hasSource():
            val = Value()
            val.setString(operData.source)
            tagValueList.push(("source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), val)
        
        if operData.isSimulatedRequested() and operData.hasSimulated():
            val = Value()
            val.setBool(operData.simulated)
            tagValueList.push(("simulated", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), val)
        
        if operData.isNameRequested() and operData.hasName():
            val = Value()
            val.setEnum(operData.name.getValue())
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), val)
        
        
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
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "description"):
            if operData.isDescriptionRequested():
                 if operData.hasDescription():
                     value.setString(operData.description)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "severity"):
            if operData.isSeverityRequested():
                 if operData.hasSeverity():
                     value.setEnum(operData.severity.getValue())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "number"):
            if operData.isNumberRequested():
                 if operData.hasNumber():
                     value.setInt64(operData.number)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "entity"):
            if operData.isEntityRequested():
                 if operData.hasEntity():
                     value.setString(operData.entity)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "source"):
            if operData.isSourceRequested():
                 if operData.hasSource():
                     value.setString(operData.source)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "simulated"):
            if operData.isSimulatedRequested():
                 if operData.hasSimulated():
                     value.setBool(operData.simulated)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "name"):
            if operData.isNameRequested():
                 if operData.hasName():
                     value.setEnum(operData.name.getValue())
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
        operData = ListOperData()

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
                list = keyPathValue
                
                
                
                
                
                res = self.myGetObjectFunctor(trxContext, 
                                              
                                              list, 
                                              
                                              operData)
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myGetObjectFunctor.__name__)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("handle-get-request-functor-failed").errorFunc(): logFunc(
                        "functor failed. keyPath=%s, trxContext=%s", keyPath, trxContext)
                    return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def getElement (self, trxContext, keyPath):
        for logFunc in self._log("get-element").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        operData = ListOperData()
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.list.list_oper_data_gen import ListOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "qt-sys-alarms", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "list", 
        "namespace": "list", 
        "logGroupName": "blinky-list-oper_list", 
        "className": "BlinkyOperListList", 
        "logModuleName": "a-sys-mng-alarm-tech-system-alarms-tech-system-alarms-list-blinky-list-oper-list-gen", 
        "importStatement": "from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.list.blinky_list_oper_list_gen import BlinkyOperListList", 
        "callpointName": "tech-system-alarms-list-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
        "dataClassName": "ListOperData", 
        "getObjArgsNum": 3, 
        "keyLeaf": {
            "varName": "list", 
            "typeHandler": "handler: IntHandler"
        }, 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "system", 
            "namespace": "system", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "isCurrent": true, 
            "yangName": "list", 
            "namespace": "list", 
            "isList": true, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "keyLeaf": {
                "varName": "list", 
                "defaultVal": null, 
                "typeHandler": "handler: IntHandler"
            }, 
            "name": "list"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "severity", 
            "yangName": "severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "entity", 
            "yangName": "entity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "source", 
            "yangName": "source", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "simulated", 
            "yangName": "simulated", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "name", 
            "yangName": "name", 
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
        "mng", 
        "alarm", 
        "tech_system_alarms"
    ], 
    "createTime": "2013"
}
"""


