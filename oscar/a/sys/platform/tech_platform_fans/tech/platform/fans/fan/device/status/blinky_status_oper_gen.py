



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.status.status_oper_data_gen import StatusOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef






from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanDeviceStatusType



class BlinkyOperStatus(BlinkyOperNode):

    _kCallpointName = "tech-platform-fans-fan-device-status-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "tech-platform-fans-fan-device-status-callpoint"
        
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
        val.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans"))
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
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "status"):
                    for logFunc in self._log("set-oper-data-requested-fields-status-requested").debug3Func(): logFunc(
                        "status requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStatusRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "index"):
                    for logFunc in self._log("set-oper-data-requested-fields-index-requested").debug3Func(): logFunc(
                        "index requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setIndexRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "minimum-warning-rpm"):
                    for logFunc in self._log("set-oper-data-requested-fields-minimumwarningrpm-requested").debug3Func(): logFunc(
                        "minimum-warning-rpm requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setMinimumWarningRpmRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "current-rpm"):
                    for logFunc in self._log("set-oper-data-requested-fields-currentrpm-requested").debug3Func(): logFunc(
                        "current-rpm requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setCurrentRpmRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "maximum-warning-rpm"):
                    for logFunc in self._log("set-oper-data-requested-fields-maximumwarningrpm-requested").debug3Func(): logFunc(
                        "maximum-warning-rpm requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setMaximumWarningRpmRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "probe-name"):
                    for logFunc in self._log("set-oper-data-requested-fields-probename-requested").debug3Func(): logFunc(
                        "probe-name requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setProbeNameRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "status-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-statusraw-requested").debug3Func(): logFunc(
                        "status-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStatusRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "minimum-error-rpm"):
                    for logFunc in self._log("set-oper-data-requested-fields-minimumerrorrpm-requested").debug3Func(): logFunc(
                        "minimum-error-rpm requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setMinimumErrorRpmRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "maximum-error-rpm"):
                    for logFunc in self._log("set-oper-data-requested-fields-maximumerrorrpm-requested").debug3Func(): logFunc(
                        "maximum-error-rpm requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setMaximumErrorRpmRequested()
                
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
        
        if operData.isStatusRequested() and operData.hasStatus():
            val = Value()
            val.setEnum(operData.status.getValue())
            tagValueList.push(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), val)
        
        if operData.isIndexRequested() and operData.hasIndex():
            val = Value()
            val.setString(operData.index)
            tagValueList.push(("index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), val)
        
        if operData.isMinimumWarningRpmRequested() and operData.hasMinimumWarningRpm():
            val = Value()
            val.setString(operData.minimumWarningRpm)
            tagValueList.push(("minimum-warning-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), val)
        
        if operData.isCurrentRpmRequested() and operData.hasCurrentRpm():
            val = Value()
            val.setString(operData.currentRpm)
            tagValueList.push(("current-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), val)
        
        if operData.isMaximumWarningRpmRequested() and operData.hasMaximumWarningRpm():
            val = Value()
            val.setString(operData.maximumWarningRpm)
            tagValueList.push(("maximum-warning-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), val)
        
        if operData.isProbeNameRequested() and operData.hasProbeName():
            val = Value()
            val.setString(operData.probeName)
            tagValueList.push(("probe-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), val)
        
        if operData.isStatusRawRequested() and operData.hasStatusRaw():
            val = Value()
            val.setString(operData.statusRaw)
            tagValueList.push(("status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), val)
        
        if operData.isMinimumErrorRpmRequested() and operData.hasMinimumErrorRpm():
            val = Value()
            val.setString(operData.minimumErrorRpm)
            tagValueList.push(("minimum-error-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), val)
        
        if operData.isMaximumErrorRpmRequested() and operData.hasMaximumErrorRpm():
            val = Value()
            val.setString(operData.maximumErrorRpm)
            tagValueList.push(("maximum-error-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), val)
        
        
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
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "status"):
            if operData.isStatusRequested():
                 if operData.hasStatus():
                     value.setEnum(operData.status.getValue())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "index"):
            if operData.isIndexRequested():
                 if operData.hasIndex():
                     value.setString(operData.index)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "minimum-warning-rpm"):
            if operData.isMinimumWarningRpmRequested():
                 if operData.hasMinimumWarningRpm():
                     value.setString(operData.minimumWarningRpm)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "current-rpm"):
            if operData.isCurrentRpmRequested():
                 if operData.hasCurrentRpm():
                     value.setString(operData.currentRpm)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "maximum-warning-rpm"):
            if operData.isMaximumWarningRpmRequested():
                 if operData.hasMaximumWarningRpm():
                     value.setString(operData.maximumWarningRpm)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "probe-name"):
            if operData.isProbeNameRequested():
                 if operData.hasProbeName():
                     value.setString(operData.probeName)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "status-raw"):
            if operData.isStatusRawRequested():
                 if operData.hasStatusRaw():
                     value.setString(operData.statusRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "minimum-error-rpm"):
            if operData.isMinimumErrorRpmRequested():
                 if operData.hasMinimumErrorRpm():
                     value.setString(operData.minimumErrorRpm)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "maximum-error-rpm"):
            if operData.isMaximumErrorRpmRequested():
                 if operData.hasMaximumErrorRpm():
                     value.setString(operData.maximumErrorRpm)
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
        operData = StatusOperData()

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

        operData = StatusOperData()
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.status.status_oper_data_gen import StatusOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "qt-pltf-fans", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "status", 
        "namespace": "status", 
        "logGroupName": "blinky-status-oper", 
        "className": "BlinkyOperStatus", 
        "logModuleName": "a-sys-platform-tech-platform-fans-tech-platform-fans-fan-device-status-blinky-status-oper-gen", 
        "importStatement": "from a.sys.platform.tech_platform_fans.tech.platform.fans.fan.device.status.blinky_status_oper_gen import BlinkyOperStatus", 
        "callpointName": "tech-platform-fans-fan-device-status-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
        "dataClassName": "StatusOperData", 
        "getObjArgsNum": 2, 
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
            "moduleYangNamespacePrefix": "qt-pltf", 
            "yangName": "platform", 
            "namespace": "platform", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", 
            "name": "platform"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "yangName": "fans", 
            "namespace": "fans", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "fans"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "isCurrent": false, 
            "yangName": "fan", 
            "namespace": "fan", 
            "isList": true, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "keyLeaf": {
                "varName": "fan", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fan"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "yangName": "device", 
            "namespace": "device", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "device"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "index", 
            "yangName": "index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumWarningRpm", 
            "yangName": "minimum-warning-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "currentRpm", 
            "yangName": "current-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumWarningRpm", 
            "yangName": "maximum-warning-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "probeName", 
            "yangName": "probe-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumErrorRpm", 
            "yangName": "minimum-error-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumErrorRpm", 
            "yangName": "maximum-error-rpm", 
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
        "platform", 
        "tech_platform_fans"
    ], 
    "createTime": "2013"
}
"""


