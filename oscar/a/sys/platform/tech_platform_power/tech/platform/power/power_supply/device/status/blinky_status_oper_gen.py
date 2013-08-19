



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.device.status.status_oper_data_gen import StatusOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef






from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceOnlineStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceStatusType



class BlinkyOperStatus(BlinkyOperNode):

    _kCallpointName = "tech-platform-power-power-supply-device-status-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "tech-platform-power-power-supply-device-status-callpoint"
        
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
        val.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr"))
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
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "firmware-version"):
                    for logFunc in self._log("set-oper-data-requested-fields-firmwareversion-requested").debug3Func(): logFunc(
                        "firmware-version requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setFirmwareVersionRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "index"):
                    for logFunc in self._log("set-oper-data-requested-fields-index-requested").debug3Func(): logFunc(
                        "index requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setIndexRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "fru-device"):
                    for logFunc in self._log("set-oper-data-requested-fields-frudevice-requested").debug3Func(): logFunc(
                        "fru-device requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setFruDeviceRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "manufacture-date"):
                    for logFunc in self._log("set-oper-data-requested-fields-manufacturedate-requested").debug3Func(): logFunc(
                        "manufacture-date requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setManufactureDateRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "online-status"):
                    for logFunc in self._log("set-oper-data-requested-fields-onlinestatus-requested").debug3Func(): logFunc(
                        "online-status requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOnlineStatusRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "part-number"):
                    for logFunc in self._log("set-oper-data-requested-fields-partnumber-requested").debug3Func(): logFunc(
                        "part-number requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setPartNumberRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "serial-number"):
                    for logFunc in self._log("set-oper-data-requested-fields-serialnumber-requested").debug3Func(): logFunc(
                        "serial-number requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setSerialNumberRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "status"):
                    for logFunc in self._log("set-oper-data-requested-fields-status-requested").debug3Func(): logFunc(
                        "status requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStatusRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "location"):
                    for logFunc in self._log("set-oper-data-requested-fields-location-requested").debug3Func(): logFunc(
                        "location requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setLocationRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "online-status-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-onlinestatusraw-requested").debug3Func(): logFunc(
                        "online-status-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOnlineStatusRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "status-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-statusraw-requested").debug3Func(): logFunc(
                        "status-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStatusRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "input-type"):
                    for logFunc in self._log("set-oper-data-requested-fields-inputtype-requested").debug3Func(): logFunc(
                        "input-type requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInputTypeRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "rated-input-wattage"):
                    for logFunc in self._log("set-oper-data-requested-fields-ratedinputwattage-requested").debug3Func(): logFunc(
                        "rated-input-wattage requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRatedInputWattageRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "maximum-output-wattage"):
                    for logFunc in self._log("set-oper-data-requested-fields-maximumoutputwattage-requested").debug3Func(): logFunc(
                        "maximum-output-wattage requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setMaximumOutputWattageRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "manufacturer"):
                    for logFunc in self._log("set-oper-data-requested-fields-manufacturer-requested").debug3Func(): logFunc(
                        "manufacturer requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setManufacturerRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "revision"):
                    for logFunc in self._log("set-oper-data-requested-fields-revision-requested").debug3Func(): logFunc(
                        "revision requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRevisionRequested()
                
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
        
        if operData.isFirmwareVersionRequested() and operData.hasFirmwareVersion():
            val = Value()
            val.setString(operData.firmwareVersion)
            tagValueList.push(("firmware-version", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isIndexRequested() and operData.hasIndex():
            val = Value()
            val.setString(operData.index)
            tagValueList.push(("index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isFruDeviceRequested() and operData.hasFruDevice():
            val = Value()
            val.setString(operData.fruDevice)
            tagValueList.push(("fru-device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isManufactureDateRequested() and operData.hasManufactureDate():
            val = Value()
            val.setString(operData.manufactureDate)
            tagValueList.push(("manufacture-date", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isOnlineStatusRequested() and operData.hasOnlineStatus():
            val = Value()
            val.setEnum(operData.onlineStatus.getValue())
            tagValueList.push(("online-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isPartNumberRequested() and operData.hasPartNumber():
            val = Value()
            val.setString(operData.partNumber)
            tagValueList.push(("part-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isSerialNumberRequested() and operData.hasSerialNumber():
            val = Value()
            val.setString(operData.serialNumber)
            tagValueList.push(("serial-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isStatusRequested() and operData.hasStatus():
            val = Value()
            val.setEnum(operData.status.getValue())
            tagValueList.push(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isLocationRequested() and operData.hasLocation():
            val = Value()
            val.setString(operData.location)
            tagValueList.push(("location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isOnlineStatusRawRequested() and operData.hasOnlineStatusRaw():
            val = Value()
            val.setString(operData.onlineStatusRaw)
            tagValueList.push(("online-status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isStatusRawRequested() and operData.hasStatusRaw():
            val = Value()
            val.setString(operData.statusRaw)
            tagValueList.push(("status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isInputTypeRequested() and operData.hasInputType():
            val = Value()
            val.setString(operData.inputType)
            tagValueList.push(("input-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isRatedInputWattageRequested() and operData.hasRatedInputWattage():
            val = Value()
            val.setString(operData.ratedInputWattage)
            tagValueList.push(("rated-input-wattage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isMaximumOutputWattageRequested() and operData.hasMaximumOutputWattage():
            val = Value()
            val.setString(operData.maximumOutputWattage)
            tagValueList.push(("maximum-output-wattage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isManufacturerRequested() and operData.hasManufacturer():
            val = Value()
            val.setString(operData.manufacturer)
            tagValueList.push(("manufacturer", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        if operData.isRevisionRequested() and operData.hasRevision():
            val = Value()
            val.setString(operData.revision)
            tagValueList.push(("revision", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), val)
        
        
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
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "firmware-version"):
            if operData.isFirmwareVersionRequested():
                 if operData.hasFirmwareVersion():
                     value.setString(operData.firmwareVersion)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "index"):
            if operData.isIndexRequested():
                 if operData.hasIndex():
                     value.setString(operData.index)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "fru-device"):
            if operData.isFruDeviceRequested():
                 if operData.hasFruDevice():
                     value.setString(operData.fruDevice)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "manufacture-date"):
            if operData.isManufactureDateRequested():
                 if operData.hasManufactureDate():
                     value.setString(operData.manufactureDate)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "online-status"):
            if operData.isOnlineStatusRequested():
                 if operData.hasOnlineStatus():
                     value.setEnum(operData.onlineStatus.getValue())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "part-number"):
            if operData.isPartNumberRequested():
                 if operData.hasPartNumber():
                     value.setString(operData.partNumber)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "serial-number"):
            if operData.isSerialNumberRequested():
                 if operData.hasSerialNumber():
                     value.setString(operData.serialNumber)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "status"):
            if operData.isStatusRequested():
                 if operData.hasStatus():
                     value.setEnum(operData.status.getValue())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "location"):
            if operData.isLocationRequested():
                 if operData.hasLocation():
                     value.setString(operData.location)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "online-status-raw"):
            if operData.isOnlineStatusRawRequested():
                 if operData.hasOnlineStatusRaw():
                     value.setString(operData.onlineStatusRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "status-raw"):
            if operData.isStatusRawRequested():
                 if operData.hasStatusRaw():
                     value.setString(operData.statusRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "input-type"):
            if operData.isInputTypeRequested():
                 if operData.hasInputType():
                     value.setString(operData.inputType)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "rated-input-wattage"):
            if operData.isRatedInputWattageRequested():
                 if operData.hasRatedInputWattage():
                     value.setString(operData.ratedInputWattage)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "maximum-output-wattage"):
            if operData.isMaximumOutputWattageRequested():
                 if operData.hasMaximumOutputWattage():
                     value.setString(operData.maximumOutputWattage)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "manufacturer"):
            if operData.isManufacturerRequested():
                 if operData.hasManufacturer():
                     value.setString(operData.manufacturer)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "revision"):
            if operData.isRevisionRequested():
                 if operData.hasRevision():
                     value.setString(operData.revision)
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.device.status.status_oper_data_gen import StatusOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "qt-pltf-pwr", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "status", 
        "namespace": "status", 
        "logGroupName": "blinky-status-oper", 
        "className": "BlinkyOperStatus", 
        "logModuleName": "a-sys-platform-tech-platform-power-tech-platform-power-power-supply-device-status-blinky-status-oper-gen", 
        "importStatement": "from a.sys.platform.tech_platform_power.tech.platform.power.power_supply.device.status.blinky_status_oper_gen import BlinkyOperStatus", 
        "callpointName": "tech-platform-power-power-supply-device-status-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
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
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "yangName": "power", 
            "namespace": "power", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "power"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "isCurrent": false, 
            "yangName": "power-supply", 
            "namespace": "power_supply", 
            "isList": true, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "keyLeaf": {
                "varName": "powerSupply", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "power-supply"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "yangName": "device", 
            "namespace": "device", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "device"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "firmwareVersion", 
            "yangName": "firmware-version", 
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
            "memberName": "fruDevice", 
            "yangName": "fru-device", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureDate", 
            "yangName": "manufacture-date", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "onlineStatus", 
            "yangName": "online-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "partNumber", 
            "yangName": "part-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "serialNumber", 
            "yangName": "serial-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
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
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "onlineStatusRaw", 
            "yangName": "online-status-raw", 
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
            "memberName": "inputType", 
            "yangName": "input-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "ratedInputWattage", 
            "yangName": "rated-input-wattage", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumOutputWattage", 
            "yangName": "maximum-output-wattage", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufacturer", 
            "yangName": "manufacturer", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "revision", 
            "yangName": "revision", 
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
        "tech_platform_power"
    ], 
    "createTime": "2013"
}
"""


