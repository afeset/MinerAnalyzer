


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

from status_maapi_base_gen import StatusMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalFailurePredictedType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalStateType


class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.productIdRequested = False
        self.productId = None
        self.productIdSet = False
        
        self.sasAddressRequested = False
        self.sasAddress = None
        self.sasAddressSet = False
        
        self.modelNumberRequested = False
        self.modelNumber = None
        self.modelNumberSet = False
        
        self.serialNumberRequested = False
        self.serialNumber = None
        self.serialNumberSet = False
        
        self.usedRaidSpaceRequested = False
        self.usedRaidSpace = None
        self.usedRaidSpaceSet = False
        
        self.statusRawRequested = False
        self.statusRaw = None
        self.statusRawSet = False
        
        self.firmwareRevisionRequested = False
        self.firmwareRevision = None
        self.firmwareRevisionSet = False
        
        self.sizeRequested = False
        self.size = None
        self.sizeSet = False
        
        self.failurePredictedRequested = False
        self.failurePredicted = None
        self.failurePredictedSet = False
        
        self.sizeRawRequested = False
        self.sizeRaw = None
        self.sizeRawSet = False
        
        self.deviceLifeStatusRequested = False
        self.deviceLifeStatus = None
        self.deviceLifeStatusSet = False
        
        self.deviceLifeRemainingRequested = False
        self.deviceLifeRemaining = None
        self.deviceLifeRemainingSet = False
        
        self.powerStatusRequested = False
        self.powerStatus = None
        self.powerStatusSet = False
        
        self.stateRequested = False
        self.state = None
        self.stateSet = False
        
        self.progressRequested = False
        self.progress = None
        self.progressSet = False
        
        self.statusRequested = False
        self.status = None
        self.statusSet = False
        
        self.manufactureYearRequested = False
        self.manufactureYear = None
        self.manufactureYearSet = False
        
        self.failurePredictedRawRequested = False
        self.failurePredictedRaw = None
        self.failurePredictedRawSet = False
        
        self.mediaTypeRequested = False
        self.mediaType = None
        self.mediaTypeSet = False
        
        self.manufactureDayRequested = False
        self.manufactureDay = None
        self.manufactureDaySet = False
        
        self.availableRaidSpaceRequested = False
        self.availableRaidSpace = None
        self.availableRaidSpaceSet = False
        
        self.partNumberRequested = False
        self.partNumber = None
        self.partNumberSet = False
        
        self.hotSpareRequested = False
        self.hotSpare = None
        self.hotSpareSet = False
        
        self.capableSpeedRequested = False
        self.capableSpeed = None
        self.capableSpeedSet = False
        
        self.certifiedRequested = False
        self.certified = None
        self.certifiedSet = False
        
        self.deviceWriteCacheRequested = False
        self.deviceWriteCache = None
        self.deviceWriteCacheSet = False
        
        self.stateRawRequested = False
        self.stateRaw = None
        self.stateRawSet = False
        
        self.manufactureWeekRequested = False
        self.manufactureWeek = None
        self.manufactureWeekSet = False
        
        self.negotiatedSpeedRequested = False
        self.negotiatedSpeed = None
        self.negotiatedSpeedSet = False
        
        self.vendorIdRequested = False
        self.vendorId = None
        self.vendorIdSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestProductId(True)
        
        self.requestSasAddress(True)
        
        self.requestModelNumber(True)
        
        self.requestSerialNumber(True)
        
        self.requestUsedRaidSpace(True)
        
        self.requestStatusRaw(True)
        
        self.requestFirmwareRevision(True)
        
        self.requestSize(True)
        
        self.requestFailurePredicted(True)
        
        self.requestSizeRaw(True)
        
        self.requestDeviceLifeStatus(True)
        
        self.requestDeviceLifeRemaining(True)
        
        self.requestPowerStatus(True)
        
        self.requestState(True)
        
        self.requestProgress(True)
        
        self.requestStatus(True)
        
        self.requestManufactureYear(True)
        
        self.requestFailurePredictedRaw(True)
        
        self.requestMediaType(True)
        
        self.requestManufactureDay(True)
        
        self.requestAvailableRaidSpace(True)
        
        self.requestPartNumber(True)
        
        self.requestHotSpare(True)
        
        self.requestCapableSpeed(True)
        
        self.requestCertified(True)
        
        self.requestDeviceWriteCache(True)
        
        self.requestStateRaw(True)
        
        self.requestManufactureWeek(True)
        
        self.requestNegotiatedSpeed(True)
        
        self.requestVendorId(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestProductId(False)
        
        self.requestSasAddress(False)
        
        self.requestModelNumber(False)
        
        self.requestSerialNumber(False)
        
        self.requestUsedRaidSpace(False)
        
        self.requestStatusRaw(False)
        
        self.requestFirmwareRevision(False)
        
        self.requestSize(False)
        
        self.requestFailurePredicted(False)
        
        self.requestSizeRaw(False)
        
        self.requestDeviceLifeStatus(False)
        
        self.requestDeviceLifeRemaining(False)
        
        self.requestPowerStatus(False)
        
        self.requestState(False)
        
        self.requestProgress(False)
        
        self.requestStatus(False)
        
        self.requestManufactureYear(False)
        
        self.requestFailurePredictedRaw(False)
        
        self.requestMediaType(False)
        
        self.requestManufactureDay(False)
        
        self.requestAvailableRaidSpace(False)
        
        self.requestPartNumber(False)
        
        self.requestHotSpare(False)
        
        self.requestCapableSpeed(False)
        
        self.requestCertified(False)
        
        self.requestDeviceWriteCache(False)
        
        self.requestStateRaw(False)
        
        self.requestManufactureWeek(False)
        
        self.requestNegotiatedSpeed(False)
        
        self.requestVendorId(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestProductId(True)
        
        self.requestSasAddress(True)
        
        self.requestModelNumber(True)
        
        self.requestSerialNumber(True)
        
        self.requestUsedRaidSpace(True)
        
        self.requestStatusRaw(True)
        
        self.requestFirmwareRevision(True)
        
        self.requestSize(True)
        
        self.requestFailurePredicted(True)
        
        self.requestSizeRaw(True)
        
        self.requestDeviceLifeStatus(True)
        
        self.requestDeviceLifeRemaining(True)
        
        self.requestPowerStatus(True)
        
        self.requestState(True)
        
        self.requestProgress(True)
        
        self.requestStatus(True)
        
        self.requestManufactureYear(True)
        
        self.requestFailurePredictedRaw(True)
        
        self.requestMediaType(True)
        
        self.requestManufactureDay(True)
        
        self.requestAvailableRaidSpace(True)
        
        self.requestPartNumber(True)
        
        self.requestHotSpare(True)
        
        self.requestCapableSpeed(True)
        
        self.requestCertified(True)
        
        self.requestDeviceWriteCache(True)
        
        self.requestStateRaw(True)
        
        self.requestManufactureWeek(True)
        
        self.requestNegotiatedSpeed(True)
        
        self.requestVendorId(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestProductId(False)
        
        self.requestSasAddress(False)
        
        self.requestModelNumber(False)
        
        self.requestSerialNumber(False)
        
        self.requestUsedRaidSpace(False)
        
        self.requestStatusRaw(False)
        
        self.requestFirmwareRevision(False)
        
        self.requestSize(False)
        
        self.requestFailurePredicted(False)
        
        self.requestSizeRaw(False)
        
        self.requestDeviceLifeStatus(False)
        
        self.requestDeviceLifeRemaining(False)
        
        self.requestPowerStatus(False)
        
        self.requestState(False)
        
        self.requestProgress(False)
        
        self.requestStatus(False)
        
        self.requestManufactureYear(False)
        
        self.requestFailurePredictedRaw(False)
        
        self.requestMediaType(False)
        
        self.requestManufactureDay(False)
        
        self.requestAvailableRaidSpace(False)
        
        self.requestPartNumber(False)
        
        self.requestHotSpare(False)
        
        self.requestCapableSpeed(False)
        
        self.requestCertified(False)
        
        self.requestDeviceWriteCache(False)
        
        self.requestStateRaw(False)
        
        self.requestManufactureWeek(False)
        
        self.requestNegotiatedSpeed(False)
        
        self.requestVendorId(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , disk
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(disk, trxContext)

    def read (self
              , disk
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(disk, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , disk
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(disk, 
                                  True,
                                  trxContext)



    def requestProductId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-productid').debug3Func(): logFunc('called. requested=%s', requested)
        self.productIdRequested = requested
        self.productIdSet = False

    def isProductIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-productid-requested').debug3Func(): logFunc('called. requested=%s', self.productIdRequested)
        return self.productIdRequested

    def getProductId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-productid').debug3Func(): logFunc('called. self.productIdSet=%s, self.productId=%s', self.productIdSet, self.productId)
        if self.productIdSet:
            return self.productId
        return None

    def hasProductId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-productid').debug3Func(): logFunc('called. self.productIdSet=%s, self.productId=%s', self.productIdSet, self.productId)
        if self.productIdSet:
            return True
        return False

    def setProductId (self, productId):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-productid').debug3Func(): logFunc('called. productId=%s, old=%s', productId, self.productId)
        self.productIdSet = True
        self.productId = productId

    def requestSasAddress (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-sasaddress').debug3Func(): logFunc('called. requested=%s', requested)
        self.sasAddressRequested = requested
        self.sasAddressSet = False

    def isSasAddressRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-sasaddress-requested').debug3Func(): logFunc('called. requested=%s', self.sasAddressRequested)
        return self.sasAddressRequested

    def getSasAddress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-sasaddress').debug3Func(): logFunc('called. self.sasAddressSet=%s, self.sasAddress=%s', self.sasAddressSet, self.sasAddress)
        if self.sasAddressSet:
            return self.sasAddress
        return None

    def hasSasAddress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-sasaddress').debug3Func(): logFunc('called. self.sasAddressSet=%s, self.sasAddress=%s', self.sasAddressSet, self.sasAddress)
        if self.sasAddressSet:
            return True
        return False

    def setSasAddress (self, sasAddress):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-sasaddress').debug3Func(): logFunc('called. sasAddress=%s, old=%s', sasAddress, self.sasAddress)
        self.sasAddressSet = True
        self.sasAddress = sasAddress

    def requestModelNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-modelnumber').debug3Func(): logFunc('called. requested=%s', requested)
        self.modelNumberRequested = requested
        self.modelNumberSet = False

    def isModelNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-modelnumber-requested').debug3Func(): logFunc('called. requested=%s', self.modelNumberRequested)
        return self.modelNumberRequested

    def getModelNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-modelnumber').debug3Func(): logFunc('called. self.modelNumberSet=%s, self.modelNumber=%s', self.modelNumberSet, self.modelNumber)
        if self.modelNumberSet:
            return self.modelNumber
        return None

    def hasModelNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-modelnumber').debug3Func(): logFunc('called. self.modelNumberSet=%s, self.modelNumber=%s', self.modelNumberSet, self.modelNumber)
        if self.modelNumberSet:
            return True
        return False

    def setModelNumber (self, modelNumber):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-modelnumber').debug3Func(): logFunc('called. modelNumber=%s, old=%s', modelNumber, self.modelNumber)
        self.modelNumberSet = True
        self.modelNumber = modelNumber

    def requestSerialNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-serialnumber').debug3Func(): logFunc('called. requested=%s', requested)
        self.serialNumberRequested = requested
        self.serialNumberSet = False

    def isSerialNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-serialnumber-requested').debug3Func(): logFunc('called. requested=%s', self.serialNumberRequested)
        return self.serialNumberRequested

    def getSerialNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-serialnumber').debug3Func(): logFunc('called. self.serialNumberSet=%s, self.serialNumber=%s', self.serialNumberSet, self.serialNumber)
        if self.serialNumberSet:
            return self.serialNumber
        return None

    def hasSerialNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-serialnumber').debug3Func(): logFunc('called. self.serialNumberSet=%s, self.serialNumber=%s', self.serialNumberSet, self.serialNumber)
        if self.serialNumberSet:
            return True
        return False

    def setSerialNumber (self, serialNumber):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-serialnumber').debug3Func(): logFunc('called. serialNumber=%s, old=%s', serialNumber, self.serialNumber)
        self.serialNumberSet = True
        self.serialNumber = serialNumber

    def requestUsedRaidSpace (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-usedraidspace').debug3Func(): logFunc('called. requested=%s', requested)
        self.usedRaidSpaceRequested = requested
        self.usedRaidSpaceSet = False

    def isUsedRaidSpaceRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-usedraidspace-requested').debug3Func(): logFunc('called. requested=%s', self.usedRaidSpaceRequested)
        return self.usedRaidSpaceRequested

    def getUsedRaidSpace (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-usedraidspace').debug3Func(): logFunc('called. self.usedRaidSpaceSet=%s, self.usedRaidSpace=%s', self.usedRaidSpaceSet, self.usedRaidSpace)
        if self.usedRaidSpaceSet:
            return self.usedRaidSpace
        return None

    def hasUsedRaidSpace (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-usedraidspace').debug3Func(): logFunc('called. self.usedRaidSpaceSet=%s, self.usedRaidSpace=%s', self.usedRaidSpaceSet, self.usedRaidSpace)
        if self.usedRaidSpaceSet:
            return True
        return False

    def setUsedRaidSpace (self, usedRaidSpace):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-usedraidspace').debug3Func(): logFunc('called. usedRaidSpace=%s, old=%s', usedRaidSpace, self.usedRaidSpace)
        self.usedRaidSpaceSet = True
        self.usedRaidSpace = usedRaidSpace

    def requestStatusRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-statusraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.statusRawRequested = requested
        self.statusRawSet = False

    def isStatusRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-statusraw-requested').debug3Func(): logFunc('called. requested=%s', self.statusRawRequested)
        return self.statusRawRequested

    def getStatusRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-statusraw').debug3Func(): logFunc('called. self.statusRawSet=%s, self.statusRaw=%s', self.statusRawSet, self.statusRaw)
        if self.statusRawSet:
            return self.statusRaw
        return None

    def hasStatusRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-statusraw').debug3Func(): logFunc('called. self.statusRawSet=%s, self.statusRaw=%s', self.statusRawSet, self.statusRaw)
        if self.statusRawSet:
            return True
        return False

    def setStatusRaw (self, statusRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-statusraw').debug3Func(): logFunc('called. statusRaw=%s, old=%s', statusRaw, self.statusRaw)
        self.statusRawSet = True
        self.statusRaw = statusRaw

    def requestFirmwareRevision (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-firmwarerevision').debug3Func(): logFunc('called. requested=%s', requested)
        self.firmwareRevisionRequested = requested
        self.firmwareRevisionSet = False

    def isFirmwareRevisionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-firmwarerevision-requested').debug3Func(): logFunc('called. requested=%s', self.firmwareRevisionRequested)
        return self.firmwareRevisionRequested

    def getFirmwareRevision (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-firmwarerevision').debug3Func(): logFunc('called. self.firmwareRevisionSet=%s, self.firmwareRevision=%s', self.firmwareRevisionSet, self.firmwareRevision)
        if self.firmwareRevisionSet:
            return self.firmwareRevision
        return None

    def hasFirmwareRevision (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-firmwarerevision').debug3Func(): logFunc('called. self.firmwareRevisionSet=%s, self.firmwareRevision=%s', self.firmwareRevisionSet, self.firmwareRevision)
        if self.firmwareRevisionSet:
            return True
        return False

    def setFirmwareRevision (self, firmwareRevision):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-firmwarerevision').debug3Func(): logFunc('called. firmwareRevision=%s, old=%s', firmwareRevision, self.firmwareRevision)
        self.firmwareRevisionSet = True
        self.firmwareRevision = firmwareRevision

    def requestSize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-size').debug3Func(): logFunc('called. requested=%s', requested)
        self.sizeRequested = requested
        self.sizeSet = False

    def isSizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-size-requested').debug3Func(): logFunc('called. requested=%s', self.sizeRequested)
        return self.sizeRequested

    def getSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-size').debug3Func(): logFunc('called. self.sizeSet=%s, self.size=%s', self.sizeSet, self.size)
        if self.sizeSet:
            return self.size
        return None

    def hasSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-size').debug3Func(): logFunc('called. self.sizeSet=%s, self.size=%s', self.sizeSet, self.size)
        if self.sizeSet:
            return True
        return False

    def setSize (self, size):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-size').debug3Func(): logFunc('called. size=%s, old=%s', size, self.size)
        self.sizeSet = True
        self.size = size

    def requestFailurePredicted (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-failurepredicted').debug3Func(): logFunc('called. requested=%s', requested)
        self.failurePredictedRequested = requested
        self.failurePredictedSet = False

    def isFailurePredictedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-failurepredicted-requested').debug3Func(): logFunc('called. requested=%s', self.failurePredictedRequested)
        return self.failurePredictedRequested

    def getFailurePredicted (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-failurepredicted').debug3Func(): logFunc('called. self.failurePredictedSet=%s, self.failurePredicted=%s', self.failurePredictedSet, self.failurePredicted)
        if self.failurePredictedSet:
            return self.failurePredicted
        return None

    def hasFailurePredicted (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-failurepredicted').debug3Func(): logFunc('called. self.failurePredictedSet=%s, self.failurePredicted=%s', self.failurePredictedSet, self.failurePredicted)
        if self.failurePredictedSet:
            return True
        return False

    def setFailurePredicted (self, failurePredicted):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-failurepredicted').debug3Func(): logFunc('called. failurePredicted=%s, old=%s', failurePredicted, self.failurePredicted)
        self.failurePredictedSet = True
        self.failurePredicted = failurePredicted

    def requestSizeRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-sizeraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.sizeRawRequested = requested
        self.sizeRawSet = False

    def isSizeRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-sizeraw-requested').debug3Func(): logFunc('called. requested=%s', self.sizeRawRequested)
        return self.sizeRawRequested

    def getSizeRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-sizeraw').debug3Func(): logFunc('called. self.sizeRawSet=%s, self.sizeRaw=%s', self.sizeRawSet, self.sizeRaw)
        if self.sizeRawSet:
            return self.sizeRaw
        return None

    def hasSizeRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-sizeraw').debug3Func(): logFunc('called. self.sizeRawSet=%s, self.sizeRaw=%s', self.sizeRawSet, self.sizeRaw)
        if self.sizeRawSet:
            return True
        return False

    def setSizeRaw (self, sizeRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-sizeraw').debug3Func(): logFunc('called. sizeRaw=%s, old=%s', sizeRaw, self.sizeRaw)
        self.sizeRawSet = True
        self.sizeRaw = sizeRaw

    def requestDeviceLifeStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-devicelifestatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.deviceLifeStatusRequested = requested
        self.deviceLifeStatusSet = False

    def isDeviceLifeStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-devicelifestatus-requested').debug3Func(): logFunc('called. requested=%s', self.deviceLifeStatusRequested)
        return self.deviceLifeStatusRequested

    def getDeviceLifeStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-devicelifestatus').debug3Func(): logFunc('called. self.deviceLifeStatusSet=%s, self.deviceLifeStatus=%s', self.deviceLifeStatusSet, self.deviceLifeStatus)
        if self.deviceLifeStatusSet:
            return self.deviceLifeStatus
        return None

    def hasDeviceLifeStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-devicelifestatus').debug3Func(): logFunc('called. self.deviceLifeStatusSet=%s, self.deviceLifeStatus=%s', self.deviceLifeStatusSet, self.deviceLifeStatus)
        if self.deviceLifeStatusSet:
            return True
        return False

    def setDeviceLifeStatus (self, deviceLifeStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-devicelifestatus').debug3Func(): logFunc('called. deviceLifeStatus=%s, old=%s', deviceLifeStatus, self.deviceLifeStatus)
        self.deviceLifeStatusSet = True
        self.deviceLifeStatus = deviceLifeStatus

    def requestDeviceLifeRemaining (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-deviceliferemaining').debug3Func(): logFunc('called. requested=%s', requested)
        self.deviceLifeRemainingRequested = requested
        self.deviceLifeRemainingSet = False

    def isDeviceLifeRemainingRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-deviceliferemaining-requested').debug3Func(): logFunc('called. requested=%s', self.deviceLifeRemainingRequested)
        return self.deviceLifeRemainingRequested

    def getDeviceLifeRemaining (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-deviceliferemaining').debug3Func(): logFunc('called. self.deviceLifeRemainingSet=%s, self.deviceLifeRemaining=%s', self.deviceLifeRemainingSet, self.deviceLifeRemaining)
        if self.deviceLifeRemainingSet:
            return self.deviceLifeRemaining
        return None

    def hasDeviceLifeRemaining (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-deviceliferemaining').debug3Func(): logFunc('called. self.deviceLifeRemainingSet=%s, self.deviceLifeRemaining=%s', self.deviceLifeRemainingSet, self.deviceLifeRemaining)
        if self.deviceLifeRemainingSet:
            return True
        return False

    def setDeviceLifeRemaining (self, deviceLifeRemaining):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-deviceliferemaining').debug3Func(): logFunc('called. deviceLifeRemaining=%s, old=%s', deviceLifeRemaining, self.deviceLifeRemaining)
        self.deviceLifeRemainingSet = True
        self.deviceLifeRemaining = deviceLifeRemaining

    def requestPowerStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-powerstatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.powerStatusRequested = requested
        self.powerStatusSet = False

    def isPowerStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-powerstatus-requested').debug3Func(): logFunc('called. requested=%s', self.powerStatusRequested)
        return self.powerStatusRequested

    def getPowerStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-powerstatus').debug3Func(): logFunc('called. self.powerStatusSet=%s, self.powerStatus=%s', self.powerStatusSet, self.powerStatus)
        if self.powerStatusSet:
            return self.powerStatus
        return None

    def hasPowerStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-powerstatus').debug3Func(): logFunc('called. self.powerStatusSet=%s, self.powerStatus=%s', self.powerStatusSet, self.powerStatus)
        if self.powerStatusSet:
            return True
        return False

    def setPowerStatus (self, powerStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-powerstatus').debug3Func(): logFunc('called. powerStatus=%s, old=%s', powerStatus, self.powerStatus)
        self.powerStatusSet = True
        self.powerStatus = powerStatus

    def requestState (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-state').debug3Func(): logFunc('called. requested=%s', requested)
        self.stateRequested = requested
        self.stateSet = False

    def isStateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-state-requested').debug3Func(): logFunc('called. requested=%s', self.stateRequested)
        return self.stateRequested

    def getState (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-state').debug3Func(): logFunc('called. self.stateSet=%s, self.state=%s', self.stateSet, self.state)
        if self.stateSet:
            return self.state
        return None

    def hasState (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-state').debug3Func(): logFunc('called. self.stateSet=%s, self.state=%s', self.stateSet, self.state)
        if self.stateSet:
            return True
        return False

    def setState (self, state):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-state').debug3Func(): logFunc('called. state=%s, old=%s', state, self.state)
        self.stateSet = True
        self.state = state

    def requestProgress (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-progress').debug3Func(): logFunc('called. requested=%s', requested)
        self.progressRequested = requested
        self.progressSet = False

    def isProgressRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-progress-requested').debug3Func(): logFunc('called. requested=%s', self.progressRequested)
        return self.progressRequested

    def getProgress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-progress').debug3Func(): logFunc('called. self.progressSet=%s, self.progress=%s', self.progressSet, self.progress)
        if self.progressSet:
            return self.progress
        return None

    def hasProgress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-progress').debug3Func(): logFunc('called. self.progressSet=%s, self.progress=%s', self.progressSet, self.progress)
        if self.progressSet:
            return True
        return False

    def setProgress (self, progress):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-progress').debug3Func(): logFunc('called. progress=%s, old=%s', progress, self.progress)
        self.progressSet = True
        self.progress = progress

    def requestStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-status').debug3Func(): logFunc('called. requested=%s', requested)
        self.statusRequested = requested
        self.statusSet = False

    def isStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-status-requested').debug3Func(): logFunc('called. requested=%s', self.statusRequested)
        return self.statusRequested

    def getStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusSet=%s, self.status=%s', self.statusSet, self.status)
        if self.statusSet:
            return self.status
        return None

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusSet=%s, self.status=%s', self.statusSet, self.status)
        if self.statusSet:
            return True
        return False

    def setStatus (self, status):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. status=%s, old=%s', status, self.status)
        self.statusSet = True
        self.status = status

    def requestManufactureYear (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-manufactureyear').debug3Func(): logFunc('called. requested=%s', requested)
        self.manufactureYearRequested = requested
        self.manufactureYearSet = False

    def isManufactureYearRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-manufactureyear-requested').debug3Func(): logFunc('called. requested=%s', self.manufactureYearRequested)
        return self.manufactureYearRequested

    def getManufactureYear (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-manufactureyear').debug3Func(): logFunc('called. self.manufactureYearSet=%s, self.manufactureYear=%s', self.manufactureYearSet, self.manufactureYear)
        if self.manufactureYearSet:
            return self.manufactureYear
        return None

    def hasManufactureYear (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-manufactureyear').debug3Func(): logFunc('called. self.manufactureYearSet=%s, self.manufactureYear=%s', self.manufactureYearSet, self.manufactureYear)
        if self.manufactureYearSet:
            return True
        return False

    def setManufactureYear (self, manufactureYear):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-manufactureyear').debug3Func(): logFunc('called. manufactureYear=%s, old=%s', manufactureYear, self.manufactureYear)
        self.manufactureYearSet = True
        self.manufactureYear = manufactureYear

    def requestFailurePredictedRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-failurepredictedraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.failurePredictedRawRequested = requested
        self.failurePredictedRawSet = False

    def isFailurePredictedRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-failurepredictedraw-requested').debug3Func(): logFunc('called. requested=%s', self.failurePredictedRawRequested)
        return self.failurePredictedRawRequested

    def getFailurePredictedRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-failurepredictedraw').debug3Func(): logFunc('called. self.failurePredictedRawSet=%s, self.failurePredictedRaw=%s', self.failurePredictedRawSet, self.failurePredictedRaw)
        if self.failurePredictedRawSet:
            return self.failurePredictedRaw
        return None

    def hasFailurePredictedRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-failurepredictedraw').debug3Func(): logFunc('called. self.failurePredictedRawSet=%s, self.failurePredictedRaw=%s', self.failurePredictedRawSet, self.failurePredictedRaw)
        if self.failurePredictedRawSet:
            return True
        return False

    def setFailurePredictedRaw (self, failurePredictedRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-failurepredictedraw').debug3Func(): logFunc('called. failurePredictedRaw=%s, old=%s', failurePredictedRaw, self.failurePredictedRaw)
        self.failurePredictedRawSet = True
        self.failurePredictedRaw = failurePredictedRaw

    def requestMediaType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mediatype').debug3Func(): logFunc('called. requested=%s', requested)
        self.mediaTypeRequested = requested
        self.mediaTypeSet = False

    def isMediaTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mediatype-requested').debug3Func(): logFunc('called. requested=%s', self.mediaTypeRequested)
        return self.mediaTypeRequested

    def getMediaType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mediatype').debug3Func(): logFunc('called. self.mediaTypeSet=%s, self.mediaType=%s', self.mediaTypeSet, self.mediaType)
        if self.mediaTypeSet:
            return self.mediaType
        return None

    def hasMediaType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mediatype').debug3Func(): logFunc('called. self.mediaTypeSet=%s, self.mediaType=%s', self.mediaTypeSet, self.mediaType)
        if self.mediaTypeSet:
            return True
        return False

    def setMediaType (self, mediaType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mediatype').debug3Func(): logFunc('called. mediaType=%s, old=%s', mediaType, self.mediaType)
        self.mediaTypeSet = True
        self.mediaType = mediaType

    def requestManufactureDay (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-manufactureday').debug3Func(): logFunc('called. requested=%s', requested)
        self.manufactureDayRequested = requested
        self.manufactureDaySet = False

    def isManufactureDayRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-manufactureday-requested').debug3Func(): logFunc('called. requested=%s', self.manufactureDayRequested)
        return self.manufactureDayRequested

    def getManufactureDay (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-manufactureday').debug3Func(): logFunc('called. self.manufactureDaySet=%s, self.manufactureDay=%s', self.manufactureDaySet, self.manufactureDay)
        if self.manufactureDaySet:
            return self.manufactureDay
        return None

    def hasManufactureDay (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-manufactureday').debug3Func(): logFunc('called. self.manufactureDaySet=%s, self.manufactureDay=%s', self.manufactureDaySet, self.manufactureDay)
        if self.manufactureDaySet:
            return True
        return False

    def setManufactureDay (self, manufactureDay):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-manufactureday').debug3Func(): logFunc('called. manufactureDay=%s, old=%s', manufactureDay, self.manufactureDay)
        self.manufactureDaySet = True
        self.manufactureDay = manufactureDay

    def requestAvailableRaidSpace (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-availableraidspace').debug3Func(): logFunc('called. requested=%s', requested)
        self.availableRaidSpaceRequested = requested
        self.availableRaidSpaceSet = False

    def isAvailableRaidSpaceRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-availableraidspace-requested').debug3Func(): logFunc('called. requested=%s', self.availableRaidSpaceRequested)
        return self.availableRaidSpaceRequested

    def getAvailableRaidSpace (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-availableraidspace').debug3Func(): logFunc('called. self.availableRaidSpaceSet=%s, self.availableRaidSpace=%s', self.availableRaidSpaceSet, self.availableRaidSpace)
        if self.availableRaidSpaceSet:
            return self.availableRaidSpace
        return None

    def hasAvailableRaidSpace (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-availableraidspace').debug3Func(): logFunc('called. self.availableRaidSpaceSet=%s, self.availableRaidSpace=%s', self.availableRaidSpaceSet, self.availableRaidSpace)
        if self.availableRaidSpaceSet:
            return True
        return False

    def setAvailableRaidSpace (self, availableRaidSpace):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-availableraidspace').debug3Func(): logFunc('called. availableRaidSpace=%s, old=%s', availableRaidSpace, self.availableRaidSpace)
        self.availableRaidSpaceSet = True
        self.availableRaidSpace = availableRaidSpace

    def requestPartNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-partnumber').debug3Func(): logFunc('called. requested=%s', requested)
        self.partNumberRequested = requested
        self.partNumberSet = False

    def isPartNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-partnumber-requested').debug3Func(): logFunc('called. requested=%s', self.partNumberRequested)
        return self.partNumberRequested

    def getPartNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-partnumber').debug3Func(): logFunc('called. self.partNumberSet=%s, self.partNumber=%s', self.partNumberSet, self.partNumber)
        if self.partNumberSet:
            return self.partNumber
        return None

    def hasPartNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-partnumber').debug3Func(): logFunc('called. self.partNumberSet=%s, self.partNumber=%s', self.partNumberSet, self.partNumber)
        if self.partNumberSet:
            return True
        return False

    def setPartNumber (self, partNumber):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-partnumber').debug3Func(): logFunc('called. partNumber=%s, old=%s', partNumber, self.partNumber)
        self.partNumberSet = True
        self.partNumber = partNumber

    def requestHotSpare (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-hotspare').debug3Func(): logFunc('called. requested=%s', requested)
        self.hotSpareRequested = requested
        self.hotSpareSet = False

    def isHotSpareRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-hotspare-requested').debug3Func(): logFunc('called. requested=%s', self.hotSpareRequested)
        return self.hotSpareRequested

    def getHotSpare (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-hotspare').debug3Func(): logFunc('called. self.hotSpareSet=%s, self.hotSpare=%s', self.hotSpareSet, self.hotSpare)
        if self.hotSpareSet:
            return self.hotSpare
        return None

    def hasHotSpare (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-hotspare').debug3Func(): logFunc('called. self.hotSpareSet=%s, self.hotSpare=%s', self.hotSpareSet, self.hotSpare)
        if self.hotSpareSet:
            return True
        return False

    def setHotSpare (self, hotSpare):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-hotspare').debug3Func(): logFunc('called. hotSpare=%s, old=%s', hotSpare, self.hotSpare)
        self.hotSpareSet = True
        self.hotSpare = hotSpare

    def requestCapableSpeed (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-capablespeed').debug3Func(): logFunc('called. requested=%s', requested)
        self.capableSpeedRequested = requested
        self.capableSpeedSet = False

    def isCapableSpeedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-capablespeed-requested').debug3Func(): logFunc('called. requested=%s', self.capableSpeedRequested)
        return self.capableSpeedRequested

    def getCapableSpeed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-capablespeed').debug3Func(): logFunc('called. self.capableSpeedSet=%s, self.capableSpeed=%s', self.capableSpeedSet, self.capableSpeed)
        if self.capableSpeedSet:
            return self.capableSpeed
        return None

    def hasCapableSpeed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-capablespeed').debug3Func(): logFunc('called. self.capableSpeedSet=%s, self.capableSpeed=%s', self.capableSpeedSet, self.capableSpeed)
        if self.capableSpeedSet:
            return True
        return False

    def setCapableSpeed (self, capableSpeed):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-capablespeed').debug3Func(): logFunc('called. capableSpeed=%s, old=%s', capableSpeed, self.capableSpeed)
        self.capableSpeedSet = True
        self.capableSpeed = capableSpeed

    def requestCertified (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-certified').debug3Func(): logFunc('called. requested=%s', requested)
        self.certifiedRequested = requested
        self.certifiedSet = False

    def isCertifiedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-certified-requested').debug3Func(): logFunc('called. requested=%s', self.certifiedRequested)
        return self.certifiedRequested

    def getCertified (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-certified').debug3Func(): logFunc('called. self.certifiedSet=%s, self.certified=%s', self.certifiedSet, self.certified)
        if self.certifiedSet:
            return self.certified
        return None

    def hasCertified (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-certified').debug3Func(): logFunc('called. self.certifiedSet=%s, self.certified=%s', self.certifiedSet, self.certified)
        if self.certifiedSet:
            return True
        return False

    def setCertified (self, certified):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-certified').debug3Func(): logFunc('called. certified=%s, old=%s', certified, self.certified)
        self.certifiedSet = True
        self.certified = certified

    def requestDeviceWriteCache (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-devicewritecache').debug3Func(): logFunc('called. requested=%s', requested)
        self.deviceWriteCacheRequested = requested
        self.deviceWriteCacheSet = False

    def isDeviceWriteCacheRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-devicewritecache-requested').debug3Func(): logFunc('called. requested=%s', self.deviceWriteCacheRequested)
        return self.deviceWriteCacheRequested

    def getDeviceWriteCache (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-devicewritecache').debug3Func(): logFunc('called. self.deviceWriteCacheSet=%s, self.deviceWriteCache=%s', self.deviceWriteCacheSet, self.deviceWriteCache)
        if self.deviceWriteCacheSet:
            return self.deviceWriteCache
        return None

    def hasDeviceWriteCache (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-devicewritecache').debug3Func(): logFunc('called. self.deviceWriteCacheSet=%s, self.deviceWriteCache=%s', self.deviceWriteCacheSet, self.deviceWriteCache)
        if self.deviceWriteCacheSet:
            return True
        return False

    def setDeviceWriteCache (self, deviceWriteCache):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-devicewritecache').debug3Func(): logFunc('called. deviceWriteCache=%s, old=%s', deviceWriteCache, self.deviceWriteCache)
        self.deviceWriteCacheSet = True
        self.deviceWriteCache = deviceWriteCache

    def requestStateRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-stateraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.stateRawRequested = requested
        self.stateRawSet = False

    def isStateRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-stateraw-requested').debug3Func(): logFunc('called. requested=%s', self.stateRawRequested)
        return self.stateRawRequested

    def getStateRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-stateraw').debug3Func(): logFunc('called. self.stateRawSet=%s, self.stateRaw=%s', self.stateRawSet, self.stateRaw)
        if self.stateRawSet:
            return self.stateRaw
        return None

    def hasStateRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-stateraw').debug3Func(): logFunc('called. self.stateRawSet=%s, self.stateRaw=%s', self.stateRawSet, self.stateRaw)
        if self.stateRawSet:
            return True
        return False

    def setStateRaw (self, stateRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-stateraw').debug3Func(): logFunc('called. stateRaw=%s, old=%s', stateRaw, self.stateRaw)
        self.stateRawSet = True
        self.stateRaw = stateRaw

    def requestManufactureWeek (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-manufactureweek').debug3Func(): logFunc('called. requested=%s', requested)
        self.manufactureWeekRequested = requested
        self.manufactureWeekSet = False

    def isManufactureWeekRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-manufactureweek-requested').debug3Func(): logFunc('called. requested=%s', self.manufactureWeekRequested)
        return self.manufactureWeekRequested

    def getManufactureWeek (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-manufactureweek').debug3Func(): logFunc('called. self.manufactureWeekSet=%s, self.manufactureWeek=%s', self.manufactureWeekSet, self.manufactureWeek)
        if self.manufactureWeekSet:
            return self.manufactureWeek
        return None

    def hasManufactureWeek (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-manufactureweek').debug3Func(): logFunc('called. self.manufactureWeekSet=%s, self.manufactureWeek=%s', self.manufactureWeekSet, self.manufactureWeek)
        if self.manufactureWeekSet:
            return True
        return False

    def setManufactureWeek (self, manufactureWeek):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-manufactureweek').debug3Func(): logFunc('called. manufactureWeek=%s, old=%s', manufactureWeek, self.manufactureWeek)
        self.manufactureWeekSet = True
        self.manufactureWeek = manufactureWeek

    def requestNegotiatedSpeed (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-negotiatedspeed').debug3Func(): logFunc('called. requested=%s', requested)
        self.negotiatedSpeedRequested = requested
        self.negotiatedSpeedSet = False

    def isNegotiatedSpeedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-negotiatedspeed-requested').debug3Func(): logFunc('called. requested=%s', self.negotiatedSpeedRequested)
        return self.negotiatedSpeedRequested

    def getNegotiatedSpeed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-negotiatedspeed').debug3Func(): logFunc('called. self.negotiatedSpeedSet=%s, self.negotiatedSpeed=%s', self.negotiatedSpeedSet, self.negotiatedSpeed)
        if self.negotiatedSpeedSet:
            return self.negotiatedSpeed
        return None

    def hasNegotiatedSpeed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-negotiatedspeed').debug3Func(): logFunc('called. self.negotiatedSpeedSet=%s, self.negotiatedSpeed=%s', self.negotiatedSpeedSet, self.negotiatedSpeed)
        if self.negotiatedSpeedSet:
            return True
        return False

    def setNegotiatedSpeed (self, negotiatedSpeed):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-negotiatedspeed').debug3Func(): logFunc('called. negotiatedSpeed=%s, old=%s', negotiatedSpeed, self.negotiatedSpeed)
        self.negotiatedSpeedSet = True
        self.negotiatedSpeed = negotiatedSpeed

    def requestVendorId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-vendorid').debug3Func(): logFunc('called. requested=%s', requested)
        self.vendorIdRequested = requested
        self.vendorIdSet = False

    def isVendorIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-vendorid-requested').debug3Func(): logFunc('called. requested=%s', self.vendorIdRequested)
        return self.vendorIdRequested

    def getVendorId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-vendorid').debug3Func(): logFunc('called. self.vendorIdSet=%s, self.vendorId=%s', self.vendorIdSet, self.vendorId)
        if self.vendorIdSet:
            return self.vendorId
        return None

    def hasVendorId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-vendorid').debug3Func(): logFunc('called. self.vendorIdSet=%s, self.vendorId=%s', self.vendorIdSet, self.vendorId)
        if self.vendorIdSet:
            return True
        return False

    def setVendorId (self, vendorId):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-vendorid').debug3Func(): logFunc('called. vendorId=%s, old=%s', vendorId, self.vendorId)
        self.vendorIdSet = True
        self.vendorId = vendorId


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.productId = 0
        self.productIdSet = False
        
        self.sasAddress = 0
        self.sasAddressSet = False
        
        self.modelNumber = 0
        self.modelNumberSet = False
        
        self.serialNumber = 0
        self.serialNumberSet = False
        
        self.usedRaidSpace = 0
        self.usedRaidSpaceSet = False
        
        self.statusRaw = 0
        self.statusRawSet = False
        
        self.firmwareRevision = 0
        self.firmwareRevisionSet = False
        
        self.size = 0
        self.sizeSet = False
        
        self.failurePredicted = 0
        self.failurePredictedSet = False
        
        self.sizeRaw = 0
        self.sizeRawSet = False
        
        self.deviceLifeStatus = 0
        self.deviceLifeStatusSet = False
        
        self.deviceLifeRemaining = 0
        self.deviceLifeRemainingSet = False
        
        self.powerStatus = 0
        self.powerStatusSet = False
        
        self.state = 0
        self.stateSet = False
        
        self.progress = 0
        self.progressSet = False
        
        self.status = 0
        self.statusSet = False
        
        self.manufactureYear = 0
        self.manufactureYearSet = False
        
        self.failurePredictedRaw = 0
        self.failurePredictedRawSet = False
        
        self.mediaType = 0
        self.mediaTypeSet = False
        
        self.manufactureDay = 0
        self.manufactureDaySet = False
        
        self.availableRaidSpace = 0
        self.availableRaidSpaceSet = False
        
        self.partNumber = 0
        self.partNumberSet = False
        
        self.hotSpare = 0
        self.hotSpareSet = False
        
        self.capableSpeed = 0
        self.capableSpeedSet = False
        
        self.certified = 0
        self.certifiedSet = False
        
        self.deviceWriteCache = 0
        self.deviceWriteCacheSet = False
        
        self.stateRaw = 0
        self.stateRawSet = False
        
        self.manufactureWeek = 0
        self.manufactureWeekSet = False
        
        self.negotiatedSpeed = 0
        self.negotiatedSpeedSet = False
        
        self.vendorId = 0
        self.vendorIdSet = False
        

    def _getSelfKeyPath (self, disk
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("physical", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(disk);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("disk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", "qt-strg-dsk"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("storage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", "qt-strg"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        disk, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(disk, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(disk, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       disk, 
                       
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

        keyPath = self._getSelfKeyPath(disk, 
                                       
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
                               disk, 
                               
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

        
        if self.isProductIdRequested():
            valProductId = Value()
            valProductId.setEmpty()
            tagValueList.push(("product-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valProductId)
        
        if self.isSasAddressRequested():
            valSasAddress = Value()
            valSasAddress.setEmpty()
            tagValueList.push(("sas-address", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valSasAddress)
        
        if self.isModelNumberRequested():
            valModelNumber = Value()
            valModelNumber.setEmpty()
            tagValueList.push(("model-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valModelNumber)
        
        if self.isSerialNumberRequested():
            valSerialNumber = Value()
            valSerialNumber.setEmpty()
            tagValueList.push(("serial-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valSerialNumber)
        
        if self.isUsedRaidSpaceRequested():
            valUsedRaidSpace = Value()
            valUsedRaidSpace.setEmpty()
            tagValueList.push(("used-raid-space", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valUsedRaidSpace)
        
        if self.isStatusRawRequested():
            valStatusRaw = Value()
            valStatusRaw.setEmpty()
            tagValueList.push(("status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valStatusRaw)
        
        if self.isFirmwareRevisionRequested():
            valFirmwareRevision = Value()
            valFirmwareRevision.setEmpty()
            tagValueList.push(("firmware-revision", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valFirmwareRevision)
        
        if self.isSizeRequested():
            valSize = Value()
            valSize.setEmpty()
            tagValueList.push(("size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valSize)
        
        if self.isFailurePredictedRequested():
            valFailurePredicted = Value()
            valFailurePredicted.setEmpty()
            tagValueList.push(("failure-predicted", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valFailurePredicted)
        
        if self.isSizeRawRequested():
            valSizeRaw = Value()
            valSizeRaw.setEmpty()
            tagValueList.push(("size-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valSizeRaw)
        
        if self.isDeviceLifeStatusRequested():
            valDeviceLifeStatus = Value()
            valDeviceLifeStatus.setEmpty()
            tagValueList.push(("device-life-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valDeviceLifeStatus)
        
        if self.isDeviceLifeRemainingRequested():
            valDeviceLifeRemaining = Value()
            valDeviceLifeRemaining.setEmpty()
            tagValueList.push(("device-life-remaining", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valDeviceLifeRemaining)
        
        if self.isPowerStatusRequested():
            valPowerStatus = Value()
            valPowerStatus.setEmpty()
            tagValueList.push(("power-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPowerStatus)
        
        if self.isStateRequested():
            valState = Value()
            valState.setEmpty()
            tagValueList.push(("state", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valState)
        
        if self.isProgressRequested():
            valProgress = Value()
            valProgress.setEmpty()
            tagValueList.push(("progress", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valProgress)
        
        if self.isStatusRequested():
            valStatus = Value()
            valStatus.setEmpty()
            tagValueList.push(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valStatus)
        
        if self.isManufactureYearRequested():
            valManufactureYear = Value()
            valManufactureYear.setEmpty()
            tagValueList.push(("manufacture-year", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valManufactureYear)
        
        if self.isFailurePredictedRawRequested():
            valFailurePredictedRaw = Value()
            valFailurePredictedRaw.setEmpty()
            tagValueList.push(("failure-predicted-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valFailurePredictedRaw)
        
        if self.isMediaTypeRequested():
            valMediaType = Value()
            valMediaType.setEmpty()
            tagValueList.push(("media-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valMediaType)
        
        if self.isManufactureDayRequested():
            valManufactureDay = Value()
            valManufactureDay.setEmpty()
            tagValueList.push(("manufacture-day", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valManufactureDay)
        
        if self.isAvailableRaidSpaceRequested():
            valAvailableRaidSpace = Value()
            valAvailableRaidSpace.setEmpty()
            tagValueList.push(("available-raid-space", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valAvailableRaidSpace)
        
        if self.isPartNumberRequested():
            valPartNumber = Value()
            valPartNumber.setEmpty()
            tagValueList.push(("part-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valPartNumber)
        
        if self.isHotSpareRequested():
            valHotSpare = Value()
            valHotSpare.setEmpty()
            tagValueList.push(("hot-spare", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valHotSpare)
        
        if self.isCapableSpeedRequested():
            valCapableSpeed = Value()
            valCapableSpeed.setEmpty()
            tagValueList.push(("capable-speed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valCapableSpeed)
        
        if self.isCertifiedRequested():
            valCertified = Value()
            valCertified.setEmpty()
            tagValueList.push(("certified", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valCertified)
        
        if self.isDeviceWriteCacheRequested():
            valDeviceWriteCache = Value()
            valDeviceWriteCache.setEmpty()
            tagValueList.push(("device-write-cache", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valDeviceWriteCache)
        
        if self.isStateRawRequested():
            valStateRaw = Value()
            valStateRaw.setEmpty()
            tagValueList.push(("state-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valStateRaw)
        
        if self.isManufactureWeekRequested():
            valManufactureWeek = Value()
            valManufactureWeek.setEmpty()
            tagValueList.push(("manufacture-week", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valManufactureWeek)
        
        if self.isNegotiatedSpeedRequested():
            valNegotiatedSpeed = Value()
            valNegotiatedSpeed.setEmpty()
            tagValueList.push(("negotiated-speed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valNegotiatedSpeed)
        
        if self.isVendorIdRequested():
            valVendorId = Value()
            valVendorId.setEmpty()
            tagValueList.push(("vendor-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"), valVendorId)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isProductIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "product-id") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-productid').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "productId", "product-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-product-id-bad-value').infoFunc(): logFunc('productId not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setProductId(tempVar)
            for logFunc in self._log('read-tag-values-product-id').debug3Func(): logFunc('read productId. productId=%s, tempValue=%s', self.productId, tempValue.getType())
        
        if self.isSasAddressRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "sas-address") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-sasaddress').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "sasAddress", "sas-address", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-sas-address-bad-value').infoFunc(): logFunc('sasAddress not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSasAddress(tempVar)
            for logFunc in self._log('read-tag-values-sas-address').debug3Func(): logFunc('read sasAddress. sasAddress=%s, tempValue=%s', self.sasAddress, tempValue.getType())
        
        if self.isModelNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "model-number") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-modelnumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "modelNumber", "model-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-model-number-bad-value').infoFunc(): logFunc('modelNumber not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setModelNumber(tempVar)
            for logFunc in self._log('read-tag-values-model-number').debug3Func(): logFunc('read modelNumber. modelNumber=%s, tempValue=%s', self.modelNumber, tempValue.getType())
        
        if self.isSerialNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "serial-number") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-serialnumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "serialNumber", "serial-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-serial-number-bad-value').infoFunc(): logFunc('serialNumber not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSerialNumber(tempVar)
            for logFunc in self._log('read-tag-values-serial-number').debug3Func(): logFunc('read serialNumber. serialNumber=%s, tempValue=%s', self.serialNumber, tempValue.getType())
        
        if self.isUsedRaidSpaceRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "used-raid-space") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-usedraidspace').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "usedRaidSpace", "used-raid-space", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-used-raid-space-bad-value').infoFunc(): logFunc('usedRaidSpace not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setUsedRaidSpace(tempVar)
            for logFunc in self._log('read-tag-values-used-raid-space').debug3Func(): logFunc('read usedRaidSpace. usedRaidSpace=%s, tempValue=%s', self.usedRaidSpace, tempValue.getType())
        
        if self.isStatusRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "status-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-statusraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "statusRaw", "status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-status-raw-bad-value').infoFunc(): logFunc('statusRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStatusRaw(tempVar)
            for logFunc in self._log('read-tag-values-status-raw').debug3Func(): logFunc('read statusRaw. statusRaw=%s, tempValue=%s', self.statusRaw, tempValue.getType())
        
        if self.isFirmwareRevisionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "firmware-revision") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-firmwarerevision').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "firmwareRevision", "firmware-revision", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-firmware-revision-bad-value').infoFunc(): logFunc('firmwareRevision not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFirmwareRevision(tempVar)
            for logFunc in self._log('read-tag-values-firmware-revision').debug3Func(): logFunc('read firmwareRevision. firmwareRevision=%s, tempValue=%s', self.firmwareRevision, tempValue.getType())
        
        if self.isSizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-size').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "size", "size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-size-bad-value').infoFunc(): logFunc('size not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSize(tempVar)
            for logFunc in self._log('read-tag-values-size').debug3Func(): logFunc('read size. size=%s, tempValue=%s', self.size, tempValue.getType())
        
        if self.isFailurePredictedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "failure-predicted") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-failurepredicted').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "failurePredicted", "failure-predicted", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-failure-predicted-bad-value').infoFunc(): logFunc('failurePredicted not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFailurePredicted(tempVar)
            for logFunc in self._log('read-tag-values-failure-predicted').debug3Func(): logFunc('read failurePredicted. failurePredicted=%s, tempValue=%s', self.failurePredicted, tempValue.getType())
        
        if self.isSizeRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "size-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-sizeraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "sizeRaw", "size-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-size-raw-bad-value').infoFunc(): logFunc('sizeRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSizeRaw(tempVar)
            for logFunc in self._log('read-tag-values-size-raw').debug3Func(): logFunc('read sizeRaw. sizeRaw=%s, tempValue=%s', self.sizeRaw, tempValue.getType())
        
        if self.isDeviceLifeStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "device-life-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-devicelifestatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "deviceLifeStatus", "device-life-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-device-life-status-bad-value').infoFunc(): logFunc('deviceLifeStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDeviceLifeStatus(tempVar)
            for logFunc in self._log('read-tag-values-device-life-status').debug3Func(): logFunc('read deviceLifeStatus. deviceLifeStatus=%s, tempValue=%s', self.deviceLifeStatus, tempValue.getType())
        
        if self.isDeviceLifeRemainingRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "device-life-remaining") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-deviceliferemaining').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "deviceLifeRemaining", "device-life-remaining", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-device-life-remaining-bad-value').infoFunc(): logFunc('deviceLifeRemaining not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDeviceLifeRemaining(tempVar)
            for logFunc in self._log('read-tag-values-device-life-remaining').debug3Func(): logFunc('read deviceLifeRemaining. deviceLifeRemaining=%s, tempValue=%s', self.deviceLifeRemaining, tempValue.getType())
        
        if self.isPowerStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "power-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-powerstatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "powerStatus", "power-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-power-status-bad-value').infoFunc(): logFunc('powerStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPowerStatus(tempVar)
            for logFunc in self._log('read-tag-values-power-status').debug3Func(): logFunc('read powerStatus. powerStatus=%s, tempValue=%s', self.powerStatus, tempValue.getType())
        
        if self.isStateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "state") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-state').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "state", "state", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-state-bad-value').infoFunc(): logFunc('state not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setState(tempVar)
            for logFunc in self._log('read-tag-values-state').debug3Func(): logFunc('read state. state=%s, tempValue=%s', self.state, tempValue.getType())
        
        if self.isProgressRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "progress") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-progress').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "progress", "progress", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-progress-bad-value').infoFunc(): logFunc('progress not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setProgress(tempVar)
            for logFunc in self._log('read-tag-values-progress').debug3Func(): logFunc('read progress. progress=%s, tempValue=%s', self.progress, tempValue.getType())
        
        if self.isStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-status').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "status", "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-status-bad-value').infoFunc(): logFunc('status not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStatus(tempVar)
            for logFunc in self._log('read-tag-values-status').debug3Func(): logFunc('read status. status=%s, tempValue=%s', self.status, tempValue.getType())
        
        if self.isManufactureYearRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "manufacture-year") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-manufactureyear').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "manufactureYear", "manufacture-year", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-manufacture-year-bad-value').infoFunc(): logFunc('manufactureYear not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setManufactureYear(tempVar)
            for logFunc in self._log('read-tag-values-manufacture-year').debug3Func(): logFunc('read manufactureYear. manufactureYear=%s, tempValue=%s', self.manufactureYear, tempValue.getType())
        
        if self.isFailurePredictedRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "failure-predicted-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-failurepredictedraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "failurePredictedRaw", "failure-predicted-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-failure-predicted-raw-bad-value').infoFunc(): logFunc('failurePredictedRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFailurePredictedRaw(tempVar)
            for logFunc in self._log('read-tag-values-failure-predicted-raw').debug3Func(): logFunc('read failurePredictedRaw. failurePredictedRaw=%s, tempValue=%s', self.failurePredictedRaw, tempValue.getType())
        
        if self.isMediaTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "media-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mediatype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mediaType", "media-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-media-type-bad-value').infoFunc(): logFunc('mediaType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMediaType(tempVar)
            for logFunc in self._log('read-tag-values-media-type').debug3Func(): logFunc('read mediaType. mediaType=%s, tempValue=%s', self.mediaType, tempValue.getType())
        
        if self.isManufactureDayRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "manufacture-day") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-manufactureday').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "manufactureDay", "manufacture-day", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-manufacture-day-bad-value').infoFunc(): logFunc('manufactureDay not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setManufactureDay(tempVar)
            for logFunc in self._log('read-tag-values-manufacture-day').debug3Func(): logFunc('read manufactureDay. manufactureDay=%s, tempValue=%s', self.manufactureDay, tempValue.getType())
        
        if self.isAvailableRaidSpaceRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "available-raid-space") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-availableraidspace').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "availableRaidSpace", "available-raid-space", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-available-raid-space-bad-value').infoFunc(): logFunc('availableRaidSpace not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAvailableRaidSpace(tempVar)
            for logFunc in self._log('read-tag-values-available-raid-space').debug3Func(): logFunc('read availableRaidSpace. availableRaidSpace=%s, tempValue=%s', self.availableRaidSpace, tempValue.getType())
        
        if self.isPartNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "part-number") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-partnumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "partNumber", "part-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-part-number-bad-value').infoFunc(): logFunc('partNumber not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPartNumber(tempVar)
            for logFunc in self._log('read-tag-values-part-number').debug3Func(): logFunc('read partNumber. partNumber=%s, tempValue=%s', self.partNumber, tempValue.getType())
        
        if self.isHotSpareRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "hot-spare") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-hotspare').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "hotSpare", "hot-spare", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-hot-spare-bad-value').infoFunc(): logFunc('hotSpare not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHotSpare(tempVar)
            for logFunc in self._log('read-tag-values-hot-spare').debug3Func(): logFunc('read hotSpare. hotSpare=%s, tempValue=%s', self.hotSpare, tempValue.getType())
        
        if self.isCapableSpeedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "capable-speed") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-capablespeed').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "capableSpeed", "capable-speed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-capable-speed-bad-value').infoFunc(): logFunc('capableSpeed not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCapableSpeed(tempVar)
            for logFunc in self._log('read-tag-values-capable-speed').debug3Func(): logFunc('read capableSpeed. capableSpeed=%s, tempValue=%s', self.capableSpeed, tempValue.getType())
        
        if self.isCertifiedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "certified") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-certified').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "certified", "certified", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-certified-bad-value').infoFunc(): logFunc('certified not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCertified(tempVar)
            for logFunc in self._log('read-tag-values-certified').debug3Func(): logFunc('read certified. certified=%s, tempValue=%s', self.certified, tempValue.getType())
        
        if self.isDeviceWriteCacheRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "device-write-cache") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-devicewritecache').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "deviceWriteCache", "device-write-cache", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-device-write-cache-bad-value').infoFunc(): logFunc('deviceWriteCache not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDeviceWriteCache(tempVar)
            for logFunc in self._log('read-tag-values-device-write-cache').debug3Func(): logFunc('read deviceWriteCache. deviceWriteCache=%s, tempValue=%s', self.deviceWriteCache, tempValue.getType())
        
        if self.isStateRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "state-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-stateraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "stateRaw", "state-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-state-raw-bad-value').infoFunc(): logFunc('stateRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStateRaw(tempVar)
            for logFunc in self._log('read-tag-values-state-raw').debug3Func(): logFunc('read stateRaw. stateRaw=%s, tempValue=%s', self.stateRaw, tempValue.getType())
        
        if self.isManufactureWeekRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "manufacture-week") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-manufactureweek').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "manufactureWeek", "manufacture-week", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-manufacture-week-bad-value').infoFunc(): logFunc('manufactureWeek not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setManufactureWeek(tempVar)
            for logFunc in self._log('read-tag-values-manufacture-week').debug3Func(): logFunc('read manufactureWeek. manufactureWeek=%s, tempValue=%s', self.manufactureWeek, tempValue.getType())
        
        if self.isNegotiatedSpeedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "negotiated-speed") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-negotiatedspeed').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "negotiatedSpeed", "negotiated-speed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-negotiated-speed-bad-value').infoFunc(): logFunc('negotiatedSpeed not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNegotiatedSpeed(tempVar)
            for logFunc in self._log('read-tag-values-negotiated-speed').debug3Func(): logFunc('read negotiatedSpeed. negotiatedSpeed=%s, tempValue=%s', self.negotiatedSpeed, tempValue.getType())
        
        if self.isVendorIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "vendor-id") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-vendorid').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "vendorId", "vendor-id", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-vendor-id-bad-value').infoFunc(): logFunc('vendorId not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setVendorId(tempVar)
            for logFunc in self._log('read-tag-values-vendor-id').debug3Func(): logFunc('read vendorId. vendorId=%s, tempValue=%s', self.vendorId, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "isCurrent": false, 
            "yangName": "disk", 
            "namespace": "disk", 
            "isList": true, 
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
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "physical"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "productId", 
            "yangName": "product-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "sasAddress", 
            "yangName": "sas-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "modelNumber", 
            "yangName": "model-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "serialNumber", 
            "yangName": "serial-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "usedRaidSpace", 
            "yangName": "used-raid-space", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "firmwareRevision", 
            "yangName": "firmware-revision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "size", 
            "yangName": "size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "failurePredicted", 
            "yangName": "failure-predicted", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "sizeRaw", 
            "yangName": "size-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceLifeStatus", 
            "yangName": "device-life-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceLifeRemaining", 
            "yangName": "device-life-remaining", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "powerStatus", 
            "yangName": "power-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "progress", 
            "yangName": "progress", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureYear", 
            "yangName": "manufacture-year", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "failurePredictedRaw", 
            "yangName": "failure-predicted-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mediaType", 
            "yangName": "media-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureDay", 
            "yangName": "manufacture-day", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "availableRaidSpace", 
            "yangName": "available-raid-space", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "partNumber", 
            "yangName": "part-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "hotSpare", 
            "yangName": "hot-spare", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "capableSpeed", 
            "yangName": "capable-speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "certified", 
            "yangName": "certified", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceWriteCache", 
            "yangName": "device-write-cache", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "stateRaw", 
            "yangName": "state-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureWeek", 
            "yangName": "manufacture-week", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "negotiatedSpeed", 
            "yangName": "negotiated-speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
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
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_storage_disk"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "productId", 
            "yangName": "product-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "sasAddress", 
            "yangName": "sas-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "modelNumber", 
            "yangName": "model-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "serialNumber", 
            "yangName": "serial-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "usedRaidSpace", 
            "yangName": "used-raid-space", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "firmwareRevision", 
            "yangName": "firmware-revision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "size", 
            "yangName": "size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "failurePredicted", 
            "yangName": "failure-predicted", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "sizeRaw", 
            "yangName": "size-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceLifeStatus", 
            "yangName": "device-life-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceLifeRemaining", 
            "yangName": "device-life-remaining", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "powerStatus", 
            "yangName": "power-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "progress", 
            "yangName": "progress", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureYear", 
            "yangName": "manufacture-year", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "failurePredictedRaw", 
            "yangName": "failure-predicted-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mediaType", 
            "yangName": "media-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureDay", 
            "yangName": "manufacture-day", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "availableRaidSpace", 
            "yangName": "available-raid-space", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "partNumber", 
            "yangName": "part-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "hotSpare", 
            "yangName": "hot-spare", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "capableSpeed", 
            "yangName": "capable-speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "certified", 
            "yangName": "certified", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "deviceWriteCache", 
            "yangName": "device-write-cache", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "stateRaw", 
            "yangName": "state-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureWeek", 
            "yangName": "manufacture-week", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "negotiatedSpeed", 
            "yangName": "negotiated-speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "vendorId", 
            "yangName": "vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


