



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.status.status_oper_data_gen import StatusOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef






from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalFailurePredictedType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalStateType



class BlinkyOperStatus(BlinkyOperNode):

    _kCallpointName = "tech-storage-disk-physical-status-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "tech-storage-disk-physical-status-callpoint"
        
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
        val.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
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
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "product-id"):
                    for logFunc in self._log("set-oper-data-requested-fields-productid-requested").debug3Func(): logFunc(
                        "product-id requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setProductIdRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "sas-address"):
                    for logFunc in self._log("set-oper-data-requested-fields-sasaddress-requested").debug3Func(): logFunc(
                        "sas-address requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setSasAddressRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "model-number"):
                    for logFunc in self._log("set-oper-data-requested-fields-modelnumber-requested").debug3Func(): logFunc(
                        "model-number requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setModelNumberRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "serial-number"):
                    for logFunc in self._log("set-oper-data-requested-fields-serialnumber-requested").debug3Func(): logFunc(
                        "serial-number requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setSerialNumberRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "used-raid-space"):
                    for logFunc in self._log("set-oper-data-requested-fields-usedraidspace-requested").debug3Func(): logFunc(
                        "used-raid-space requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setUsedRaidSpaceRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "status-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-statusraw-requested").debug3Func(): logFunc(
                        "status-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStatusRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "firmware-revision"):
                    for logFunc in self._log("set-oper-data-requested-fields-firmwarerevision-requested").debug3Func(): logFunc(
                        "firmware-revision requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setFirmwareRevisionRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "size"):
                    for logFunc in self._log("set-oper-data-requested-fields-size-requested").debug3Func(): logFunc(
                        "size requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setSizeRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "failure-predicted"):
                    for logFunc in self._log("set-oper-data-requested-fields-failurepredicted-requested").debug3Func(): logFunc(
                        "failure-predicted requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setFailurePredictedRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "size-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-sizeraw-requested").debug3Func(): logFunc(
                        "size-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setSizeRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "device-life-status"):
                    for logFunc in self._log("set-oper-data-requested-fields-devicelifestatus-requested").debug3Func(): logFunc(
                        "device-life-status requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setDeviceLifeStatusRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "device-life-remaining"):
                    for logFunc in self._log("set-oper-data-requested-fields-deviceliferemaining-requested").debug3Func(): logFunc(
                        "device-life-remaining requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setDeviceLifeRemainingRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "power-status"):
                    for logFunc in self._log("set-oper-data-requested-fields-powerstatus-requested").debug3Func(): logFunc(
                        "power-status requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setPowerStatusRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "state"):
                    for logFunc in self._log("set-oper-data-requested-fields-state-requested").debug3Func(): logFunc(
                        "state requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStateRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "progress"):
                    for logFunc in self._log("set-oper-data-requested-fields-progress-requested").debug3Func(): logFunc(
                        "progress requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setProgressRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "status"):
                    for logFunc in self._log("set-oper-data-requested-fields-status-requested").debug3Func(): logFunc(
                        "status requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStatusRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "manufacture-year"):
                    for logFunc in self._log("set-oper-data-requested-fields-manufactureyear-requested").debug3Func(): logFunc(
                        "manufacture-year requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setManufactureYearRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "failure-predicted-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-failurepredictedraw-requested").debug3Func(): logFunc(
                        "failure-predicted-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setFailurePredictedRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "media-type"):
                    for logFunc in self._log("set-oper-data-requested-fields-mediatype-requested").debug3Func(): logFunc(
                        "media-type requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setMediaTypeRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "manufacture-day"):
                    for logFunc in self._log("set-oper-data-requested-fields-manufactureday-requested").debug3Func(): logFunc(
                        "manufacture-day requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setManufactureDayRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "available-raid-space"):
                    for logFunc in self._log("set-oper-data-requested-fields-availableraidspace-requested").debug3Func(): logFunc(
                        "available-raid-space requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setAvailableRaidSpaceRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "part-number"):
                    for logFunc in self._log("set-oper-data-requested-fields-partnumber-requested").debug3Func(): logFunc(
                        "part-number requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setPartNumberRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "hot-spare"):
                    for logFunc in self._log("set-oper-data-requested-fields-hotspare-requested").debug3Func(): logFunc(
                        "hot-spare requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setHotSpareRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "capable-speed"):
                    for logFunc in self._log("set-oper-data-requested-fields-capablespeed-requested").debug3Func(): logFunc(
                        "capable-speed requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setCapableSpeedRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "certified"):
                    for logFunc in self._log("set-oper-data-requested-fields-certified-requested").debug3Func(): logFunc(
                        "certified requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setCertifiedRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "device-write-cache"):
                    for logFunc in self._log("set-oper-data-requested-fields-devicewritecache-requested").debug3Func(): logFunc(
                        "device-write-cache requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setDeviceWriteCacheRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "state-raw"):
                    for logFunc in self._log("set-oper-data-requested-fields-stateraw-requested").debug3Func(): logFunc(
                        "state-raw requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setStateRawRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "manufacture-week"):
                    for logFunc in self._log("set-oper-data-requested-fields-manufactureweek-requested").debug3Func(): logFunc(
                        "manufacture-week requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setManufactureWeekRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "negotiated-speed"):
                    for logFunc in self._log("set-oper-data-requested-fields-negotiatedspeed-requested").debug3Func(): logFunc(
                        "negotiated-speed requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setNegotiatedSpeedRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "vendor-id"):
                    for logFunc in self._log("set-oper-data-requested-fields-vendorid-requested").debug3Func(): logFunc(
                        "vendor-id requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setVendorIdRequested()
                
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
        
        if operData.isProductIdRequested() and operData.hasProductId():
            val = Value()
            val.setString(operData.productId)
            tagValueList.push(("product-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isSasAddressRequested() and operData.hasSasAddress():
            val = Value()
            val.setString(operData.sasAddress)
            tagValueList.push(("sas-address", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isModelNumberRequested() and operData.hasModelNumber():
            val = Value()
            val.setString(operData.modelNumber)
            tagValueList.push(("model-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isSerialNumberRequested() and operData.hasSerialNumber():
            val = Value()
            val.setString(operData.serialNumber)
            tagValueList.push(("serial-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isUsedRaidSpaceRequested() and operData.hasUsedRaidSpace():
            val = Value()
            val.setString(operData.usedRaidSpace)
            tagValueList.push(("used-raid-space", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isStatusRawRequested() and operData.hasStatusRaw():
            val = Value()
            val.setString(operData.statusRaw)
            tagValueList.push(("status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isFirmwareRevisionRequested() and operData.hasFirmwareRevision():
            val = Value()
            val.setString(operData.firmwareRevision)
            tagValueList.push(("firmware-revision", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isSizeRequested() and operData.hasSize():
            val = Value()
            val.setInt64(operData.size)
            tagValueList.push(("size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isFailurePredictedRequested() and operData.hasFailurePredicted():
            val = Value()
            val.setEnum(operData.failurePredicted.getValue())
            tagValueList.push(("failure-predicted", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isSizeRawRequested() and operData.hasSizeRaw():
            val = Value()
            val.setString(operData.sizeRaw)
            tagValueList.push(("size-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isDeviceLifeStatusRequested() and operData.hasDeviceLifeStatus():
            val = Value()
            val.setString(operData.deviceLifeStatus)
            tagValueList.push(("device-life-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isDeviceLifeRemainingRequested() and operData.hasDeviceLifeRemaining():
            val = Value()
            val.setString(operData.deviceLifeRemaining)
            tagValueList.push(("device-life-remaining", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isPowerStatusRequested() and operData.hasPowerStatus():
            val = Value()
            val.setString(operData.powerStatus)
            tagValueList.push(("power-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isStateRequested() and operData.hasState():
            val = Value()
            val.setEnum(operData.state.getValue())
            tagValueList.push(("state", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isProgressRequested() and operData.hasProgress():
            val = Value()
            val.setString(operData.progress)
            tagValueList.push(("progress", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isStatusRequested() and operData.hasStatus():
            val = Value()
            val.setEnum(operData.status.getValue())
            tagValueList.push(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isManufactureYearRequested() and operData.hasManufactureYear():
            val = Value()
            val.setString(operData.manufactureYear)
            tagValueList.push(("manufacture-year", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isFailurePredictedRawRequested() and operData.hasFailurePredictedRaw():
            val = Value()
            val.setString(operData.failurePredictedRaw)
            tagValueList.push(("failure-predicted-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isMediaTypeRequested() and operData.hasMediaType():
            val = Value()
            val.setString(operData.mediaType)
            tagValueList.push(("media-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isManufactureDayRequested() and operData.hasManufactureDay():
            val = Value()
            val.setString(operData.manufactureDay)
            tagValueList.push(("manufacture-day", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isAvailableRaidSpaceRequested() and operData.hasAvailableRaidSpace():
            val = Value()
            val.setString(operData.availableRaidSpace)
            tagValueList.push(("available-raid-space", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isPartNumberRequested() and operData.hasPartNumber():
            val = Value()
            val.setString(operData.partNumber)
            tagValueList.push(("part-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isHotSpareRequested() and operData.hasHotSpare():
            val = Value()
            val.setString(operData.hotSpare)
            tagValueList.push(("hot-spare", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isCapableSpeedRequested() and operData.hasCapableSpeed():
            val = Value()
            val.setString(operData.capableSpeed)
            tagValueList.push(("capable-speed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isCertifiedRequested() and operData.hasCertified():
            val = Value()
            val.setString(operData.certified)
            tagValueList.push(("certified", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isDeviceWriteCacheRequested() and operData.hasDeviceWriteCache():
            val = Value()
            val.setString(operData.deviceWriteCache)
            tagValueList.push(("device-write-cache", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isStateRawRequested() and operData.hasStateRaw():
            val = Value()
            val.setString(operData.stateRaw)
            tagValueList.push(("state-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isManufactureWeekRequested() and operData.hasManufactureWeek():
            val = Value()
            val.setString(operData.manufactureWeek)
            tagValueList.push(("manufacture-week", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isNegotiatedSpeedRequested() and operData.hasNegotiatedSpeed():
            val = Value()
            val.setString(operData.negotiatedSpeed)
            tagValueList.push(("negotiated-speed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        if operData.isVendorIdRequested() and operData.hasVendorId():
            val = Value()
            val.setString(operData.vendorId)
            tagValueList.push(("vendor-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), val)
        
        
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
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "product-id"):
            if operData.isProductIdRequested():
                 if operData.hasProductId():
                     value.setString(operData.productId)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "sas-address"):
            if operData.isSasAddressRequested():
                 if operData.hasSasAddress():
                     value.setString(operData.sasAddress)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "model-number"):
            if operData.isModelNumberRequested():
                 if operData.hasModelNumber():
                     value.setString(operData.modelNumber)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "serial-number"):
            if operData.isSerialNumberRequested():
                 if operData.hasSerialNumber():
                     value.setString(operData.serialNumber)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "used-raid-space"):
            if operData.isUsedRaidSpaceRequested():
                 if operData.hasUsedRaidSpace():
                     value.setString(operData.usedRaidSpace)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "status-raw"):
            if operData.isStatusRawRequested():
                 if operData.hasStatusRaw():
                     value.setString(operData.statusRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "firmware-revision"):
            if operData.isFirmwareRevisionRequested():
                 if operData.hasFirmwareRevision():
                     value.setString(operData.firmwareRevision)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "size"):
            if operData.isSizeRequested():
                 if operData.hasSize():
                     value.setInt64(operData.size)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "failure-predicted"):
            if operData.isFailurePredictedRequested():
                 if operData.hasFailurePredicted():
                     value.setEnum(operData.failurePredicted.getValue())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "size-raw"):
            if operData.isSizeRawRequested():
                 if operData.hasSizeRaw():
                     value.setString(operData.sizeRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "device-life-status"):
            if operData.isDeviceLifeStatusRequested():
                 if operData.hasDeviceLifeStatus():
                     value.setString(operData.deviceLifeStatus)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "device-life-remaining"):
            if operData.isDeviceLifeRemainingRequested():
                 if operData.hasDeviceLifeRemaining():
                     value.setString(operData.deviceLifeRemaining)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "power-status"):
            if operData.isPowerStatusRequested():
                 if operData.hasPowerStatus():
                     value.setString(operData.powerStatus)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "state"):
            if operData.isStateRequested():
                 if operData.hasState():
                     value.setEnum(operData.state.getValue())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "progress"):
            if operData.isProgressRequested():
                 if operData.hasProgress():
                     value.setString(operData.progress)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "status"):
            if operData.isStatusRequested():
                 if operData.hasStatus():
                     value.setEnum(operData.status.getValue())
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "manufacture-year"):
            if operData.isManufactureYearRequested():
                 if operData.hasManufactureYear():
                     value.setString(operData.manufactureYear)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "failure-predicted-raw"):
            if operData.isFailurePredictedRawRequested():
                 if operData.hasFailurePredictedRaw():
                     value.setString(operData.failurePredictedRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "media-type"):
            if operData.isMediaTypeRequested():
                 if operData.hasMediaType():
                     value.setString(operData.mediaType)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "manufacture-day"):
            if operData.isManufactureDayRequested():
                 if operData.hasManufactureDay():
                     value.setString(operData.manufactureDay)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "available-raid-space"):
            if operData.isAvailableRaidSpaceRequested():
                 if operData.hasAvailableRaidSpace():
                     value.setString(operData.availableRaidSpace)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "part-number"):
            if operData.isPartNumberRequested():
                 if operData.hasPartNumber():
                     value.setString(operData.partNumber)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "hot-spare"):
            if operData.isHotSpareRequested():
                 if operData.hasHotSpare():
                     value.setString(operData.hotSpare)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "capable-speed"):
            if operData.isCapableSpeedRequested():
                 if operData.hasCapableSpeed():
                     value.setString(operData.capableSpeed)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "certified"):
            if operData.isCertifiedRequested():
                 if operData.hasCertified():
                     value.setString(operData.certified)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "device-write-cache"):
            if operData.isDeviceWriteCacheRequested():
                 if operData.hasDeviceWriteCache():
                     value.setString(operData.deviceWriteCache)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "state-raw"):
            if operData.isStateRawRequested():
                 if operData.hasStateRaw():
                     value.setString(operData.stateRaw)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "manufacture-week"):
            if operData.isManufactureWeekRequested():
                 if operData.hasManufactureWeek():
                     value.setString(operData.manufactureWeek)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "negotiated-speed"):
            if operData.isNegotiatedSpeedRequested():
                 if operData.hasNegotiatedSpeed():
                     value.setString(operData.negotiatedSpeed)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "vendor-id"):
            if operData.isVendorIdRequested():
                 if operData.hasVendorId():
                     value.setString(operData.vendorId)
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.status.status_oper_data_gen import StatusOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "qt-strg-dsk", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "status", 
        "namespace": "status", 
        "logGroupName": "blinky-status-oper", 
        "className": "BlinkyOperStatus", 
        "logModuleName": "a-storage-disk-tech-storage-tech-storage-disk-physical-status-blinky-status-oper-gen", 
        "importStatement": "from a.storage.disk.tech_storage.tech.storage.disk.physical.status.blinky_status_oper_gen import BlinkyOperStatus", 
        "callpointName": "tech-storage-disk-physical-status-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
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
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "isCurrent": false, 
            "yangName": "disk", 
            "namespace": "disk", 
            "isList": true, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "keyLeaf": {
                "varName": "disk", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "physical", 
            "namespace": "physical", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "physical"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "productId", 
            "yangName": "product-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "sasAddress", 
            "yangName": "sas-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "modelNumber", 
            "yangName": "model-number", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "usedRaidSpace", 
            "yangName": "used-raid-space", 
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
            "memberName": "firmwareRevision", 
            "yangName": "firmware-revision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "size", 
            "yangName": "size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "failurePredicted", 
            "yangName": "failure-predicted", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "sizeRaw", 
            "yangName": "size-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceLifeStatus", 
            "yangName": "device-life-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceLifeRemaining", 
            "yangName": "device-life-remaining", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "powerStatus", 
            "yangName": "power-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "progress", 
            "yangName": "progress", 
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
            "memberName": "manufactureYear", 
            "yangName": "manufacture-year", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "failurePredictedRaw", 
            "yangName": "failure-predicted-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "mediaType", 
            "yangName": "media-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureDay", 
            "yangName": "manufacture-day", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "availableRaidSpace", 
            "yangName": "available-raid-space", 
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
            "memberName": "hotSpare", 
            "yangName": "hot-spare", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "capableSpeed", 
            "yangName": "capable-speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "certified", 
            "yangName": "certified", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceWriteCache", 
            "yangName": "device-write-cache", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "stateRaw", 
            "yangName": "state-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureWeek", 
            "yangName": "manufacture-week", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "negotiatedSpeed", 
            "yangName": "negotiated-speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "vendorId", 
            "yangName": "vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "env": [
        "a", 
        "storage", 
        "disk", 
        "tech_storage"
    ], 
    "createTime": "2013"
}
"""


