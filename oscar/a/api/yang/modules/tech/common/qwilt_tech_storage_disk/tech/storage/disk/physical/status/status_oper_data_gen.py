


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperData
__pychecker__="no-classattr"

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalFailurePredictedType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import PhysicalStateType


class StatusOperData (object):

    def __init__ (self):

        self.productId = ""
        self._myHasProductId=False
        self._myProductIdRequested=False
        
        self.sasAddress = ""
        self._myHasSasAddress=False
        self._mySasAddressRequested=False
        
        self.modelNumber = ""
        self._myHasModelNumber=False
        self._myModelNumberRequested=False
        
        self.serialNumber = ""
        self._myHasSerialNumber=False
        self._mySerialNumberRequested=False
        
        self.usedRaidSpace = ""
        self._myHasUsedRaidSpace=False
        self._myUsedRaidSpaceRequested=False
        
        self.statusRaw = ""
        self._myHasStatusRaw=False
        self._myStatusRawRequested=False
        
        self.firmwareRevision = ""
        self._myHasFirmwareRevision=False
        self._myFirmwareRevisionRequested=False
        
        self.size = 0
        self._myHasSize=False
        self._mySizeRequested=False
        
        self.failurePredicted = PhysicalFailurePredictedType.kTrue
        self._myHasFailurePredicted=False
        self._myFailurePredictedRequested=False
        
        self.sizeRaw = ""
        self._myHasSizeRaw=False
        self._mySizeRawRequested=False
        
        self.deviceLifeStatus = ""
        self._myHasDeviceLifeStatus=False
        self._myDeviceLifeStatusRequested=False
        
        self.deviceLifeRemaining = ""
        self._myHasDeviceLifeRemaining=False
        self._myDeviceLifeRemainingRequested=False
        
        self.powerStatus = ""
        self._myHasPowerStatus=False
        self._myPowerStatusRequested=False
        
        self.state = PhysicalStateType.kReady
        self._myHasState=False
        self._myStateRequested=False
        
        self.progress = ""
        self._myHasProgress=False
        self._myProgressRequested=False
        
        self.status = PhysicalStatusType.kFailure
        self._myHasStatus=False
        self._myStatusRequested=False
        
        self.manufactureYear = ""
        self._myHasManufactureYear=False
        self._myManufactureYearRequested=False
        
        self.failurePredictedRaw = ""
        self._myHasFailurePredictedRaw=False
        self._myFailurePredictedRawRequested=False
        
        self.mediaType = ""
        self._myHasMediaType=False
        self._myMediaTypeRequested=False
        
        self.manufactureDay = ""
        self._myHasManufactureDay=False
        self._myManufactureDayRequested=False
        
        self.availableRaidSpace = ""
        self._myHasAvailableRaidSpace=False
        self._myAvailableRaidSpaceRequested=False
        
        self.partNumber = ""
        self._myHasPartNumber=False
        self._myPartNumberRequested=False
        
        self.hotSpare = ""
        self._myHasHotSpare=False
        self._myHotSpareRequested=False
        
        self.capableSpeed = ""
        self._myHasCapableSpeed=False
        self._myCapableSpeedRequested=False
        
        self.certified = ""
        self._myHasCertified=False
        self._myCertifiedRequested=False
        
        self.deviceWriteCache = ""
        self._myHasDeviceWriteCache=False
        self._myDeviceWriteCacheRequested=False
        
        self.stateRaw = ""
        self._myHasStateRaw=False
        self._myStateRawRequested=False
        
        self.manufactureWeek = ""
        self._myHasManufactureWeek=False
        self._myManufactureWeekRequested=False
        
        self.negotiatedSpeed = ""
        self._myHasNegotiatedSpeed=False
        self._myNegotiatedSpeedRequested=False
        
        self.vendorId = ""
        self._myHasVendorId=False
        self._myVendorIdRequested=False
        


    def copyFrom (self, other):

        self.productId=other.productId
        self._myHasProductId=other._myHasProductId
        self._myProductIdRequested=other._myProductIdRequested
        
        self.sasAddress=other.sasAddress
        self._myHasSasAddress=other._myHasSasAddress
        self._mySasAddressRequested=other._mySasAddressRequested
        
        self.modelNumber=other.modelNumber
        self._myHasModelNumber=other._myHasModelNumber
        self._myModelNumberRequested=other._myModelNumberRequested
        
        self.serialNumber=other.serialNumber
        self._myHasSerialNumber=other._myHasSerialNumber
        self._mySerialNumberRequested=other._mySerialNumberRequested
        
        self.usedRaidSpace=other.usedRaidSpace
        self._myHasUsedRaidSpace=other._myHasUsedRaidSpace
        self._myUsedRaidSpaceRequested=other._myUsedRaidSpaceRequested
        
        self.statusRaw=other.statusRaw
        self._myHasStatusRaw=other._myHasStatusRaw
        self._myStatusRawRequested=other._myStatusRawRequested
        
        self.firmwareRevision=other.firmwareRevision
        self._myHasFirmwareRevision=other._myHasFirmwareRevision
        self._myFirmwareRevisionRequested=other._myFirmwareRevisionRequested
        
        self.size=other.size
        self._myHasSize=other._myHasSize
        self._mySizeRequested=other._mySizeRequested
        
        self.failurePredicted=other.failurePredicted
        self._myHasFailurePredicted=other._myHasFailurePredicted
        self._myFailurePredictedRequested=other._myFailurePredictedRequested
        
        self.sizeRaw=other.sizeRaw
        self._myHasSizeRaw=other._myHasSizeRaw
        self._mySizeRawRequested=other._mySizeRawRequested
        
        self.deviceLifeStatus=other.deviceLifeStatus
        self._myHasDeviceLifeStatus=other._myHasDeviceLifeStatus
        self._myDeviceLifeStatusRequested=other._myDeviceLifeStatusRequested
        
        self.deviceLifeRemaining=other.deviceLifeRemaining
        self._myHasDeviceLifeRemaining=other._myHasDeviceLifeRemaining
        self._myDeviceLifeRemainingRequested=other._myDeviceLifeRemainingRequested
        
        self.powerStatus=other.powerStatus
        self._myHasPowerStatus=other._myHasPowerStatus
        self._myPowerStatusRequested=other._myPowerStatusRequested
        
        self.state=other.state
        self._myHasState=other._myHasState
        self._myStateRequested=other._myStateRequested
        
        self.progress=other.progress
        self._myHasProgress=other._myHasProgress
        self._myProgressRequested=other._myProgressRequested
        
        self.status=other.status
        self._myHasStatus=other._myHasStatus
        self._myStatusRequested=other._myStatusRequested
        
        self.manufactureYear=other.manufactureYear
        self._myHasManufactureYear=other._myHasManufactureYear
        self._myManufactureYearRequested=other._myManufactureYearRequested
        
        self.failurePredictedRaw=other.failurePredictedRaw
        self._myHasFailurePredictedRaw=other._myHasFailurePredictedRaw
        self._myFailurePredictedRawRequested=other._myFailurePredictedRawRequested
        
        self.mediaType=other.mediaType
        self._myHasMediaType=other._myHasMediaType
        self._myMediaTypeRequested=other._myMediaTypeRequested
        
        self.manufactureDay=other.manufactureDay
        self._myHasManufactureDay=other._myHasManufactureDay
        self._myManufactureDayRequested=other._myManufactureDayRequested
        
        self.availableRaidSpace=other.availableRaidSpace
        self._myHasAvailableRaidSpace=other._myHasAvailableRaidSpace
        self._myAvailableRaidSpaceRequested=other._myAvailableRaidSpaceRequested
        
        self.partNumber=other.partNumber
        self._myHasPartNumber=other._myHasPartNumber
        self._myPartNumberRequested=other._myPartNumberRequested
        
        self.hotSpare=other.hotSpare
        self._myHasHotSpare=other._myHasHotSpare
        self._myHotSpareRequested=other._myHotSpareRequested
        
        self.capableSpeed=other.capableSpeed
        self._myHasCapableSpeed=other._myHasCapableSpeed
        self._myCapableSpeedRequested=other._myCapableSpeedRequested
        
        self.certified=other.certified
        self._myHasCertified=other._myHasCertified
        self._myCertifiedRequested=other._myCertifiedRequested
        
        self.deviceWriteCache=other.deviceWriteCache
        self._myHasDeviceWriteCache=other._myHasDeviceWriteCache
        self._myDeviceWriteCacheRequested=other._myDeviceWriteCacheRequested
        
        self.stateRaw=other.stateRaw
        self._myHasStateRaw=other._myHasStateRaw
        self._myStateRawRequested=other._myStateRawRequested
        
        self.manufactureWeek=other.manufactureWeek
        self._myHasManufactureWeek=other._myHasManufactureWeek
        self._myManufactureWeekRequested=other._myManufactureWeekRequested
        
        self.negotiatedSpeed=other.negotiatedSpeed
        self._myHasNegotiatedSpeed=other._myHasNegotiatedSpeed
        self._myNegotiatedSpeedRequested=other._myNegotiatedSpeedRequested
        
        self.vendorId=other.vendorId
        self._myHasVendorId=other._myHasVendorId
        self._myVendorIdRequested=other._myVendorIdRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isProductIdRequested():
            self.productId=other.productId
            self._myHasProductId=other._myHasProductId
            self._myProductIdRequested=other._myProductIdRequested
        
        if self.isSasAddressRequested():
            self.sasAddress=other.sasAddress
            self._myHasSasAddress=other._myHasSasAddress
            self._mySasAddressRequested=other._mySasAddressRequested
        
        if self.isModelNumberRequested():
            self.modelNumber=other.modelNumber
            self._myHasModelNumber=other._myHasModelNumber
            self._myModelNumberRequested=other._myModelNumberRequested
        
        if self.isSerialNumberRequested():
            self.serialNumber=other.serialNumber
            self._myHasSerialNumber=other._myHasSerialNumber
            self._mySerialNumberRequested=other._mySerialNumberRequested
        
        if self.isUsedRaidSpaceRequested():
            self.usedRaidSpace=other.usedRaidSpace
            self._myHasUsedRaidSpace=other._myHasUsedRaidSpace
            self._myUsedRaidSpaceRequested=other._myUsedRaidSpaceRequested
        
        if self.isStatusRawRequested():
            self.statusRaw=other.statusRaw
            self._myHasStatusRaw=other._myHasStatusRaw
            self._myStatusRawRequested=other._myStatusRawRequested
        
        if self.isFirmwareRevisionRequested():
            self.firmwareRevision=other.firmwareRevision
            self._myHasFirmwareRevision=other._myHasFirmwareRevision
            self._myFirmwareRevisionRequested=other._myFirmwareRevisionRequested
        
        if self.isSizeRequested():
            self.size=other.size
            self._myHasSize=other._myHasSize
            self._mySizeRequested=other._mySizeRequested
        
        if self.isFailurePredictedRequested():
            self.failurePredicted=other.failurePredicted
            self._myHasFailurePredicted=other._myHasFailurePredicted
            self._myFailurePredictedRequested=other._myFailurePredictedRequested
        
        if self.isSizeRawRequested():
            self.sizeRaw=other.sizeRaw
            self._myHasSizeRaw=other._myHasSizeRaw
            self._mySizeRawRequested=other._mySizeRawRequested
        
        if self.isDeviceLifeStatusRequested():
            self.deviceLifeStatus=other.deviceLifeStatus
            self._myHasDeviceLifeStatus=other._myHasDeviceLifeStatus
            self._myDeviceLifeStatusRequested=other._myDeviceLifeStatusRequested
        
        if self.isDeviceLifeRemainingRequested():
            self.deviceLifeRemaining=other.deviceLifeRemaining
            self._myHasDeviceLifeRemaining=other._myHasDeviceLifeRemaining
            self._myDeviceLifeRemainingRequested=other._myDeviceLifeRemainingRequested
        
        if self.isPowerStatusRequested():
            self.powerStatus=other.powerStatus
            self._myHasPowerStatus=other._myHasPowerStatus
            self._myPowerStatusRequested=other._myPowerStatusRequested
        
        if self.isStateRequested():
            self.state=other.state
            self._myHasState=other._myHasState
            self._myStateRequested=other._myStateRequested
        
        if self.isProgressRequested():
            self.progress=other.progress
            self._myHasProgress=other._myHasProgress
            self._myProgressRequested=other._myProgressRequested
        
        if self.isStatusRequested():
            self.status=other.status
            self._myHasStatus=other._myHasStatus
            self._myStatusRequested=other._myStatusRequested
        
        if self.isManufactureYearRequested():
            self.manufactureYear=other.manufactureYear
            self._myHasManufactureYear=other._myHasManufactureYear
            self._myManufactureYearRequested=other._myManufactureYearRequested
        
        if self.isFailurePredictedRawRequested():
            self.failurePredictedRaw=other.failurePredictedRaw
            self._myHasFailurePredictedRaw=other._myHasFailurePredictedRaw
            self._myFailurePredictedRawRequested=other._myFailurePredictedRawRequested
        
        if self.isMediaTypeRequested():
            self.mediaType=other.mediaType
            self._myHasMediaType=other._myHasMediaType
            self._myMediaTypeRequested=other._myMediaTypeRequested
        
        if self.isManufactureDayRequested():
            self.manufactureDay=other.manufactureDay
            self._myHasManufactureDay=other._myHasManufactureDay
            self._myManufactureDayRequested=other._myManufactureDayRequested
        
        if self.isAvailableRaidSpaceRequested():
            self.availableRaidSpace=other.availableRaidSpace
            self._myHasAvailableRaidSpace=other._myHasAvailableRaidSpace
            self._myAvailableRaidSpaceRequested=other._myAvailableRaidSpaceRequested
        
        if self.isPartNumberRequested():
            self.partNumber=other.partNumber
            self._myHasPartNumber=other._myHasPartNumber
            self._myPartNumberRequested=other._myPartNumberRequested
        
        if self.isHotSpareRequested():
            self.hotSpare=other.hotSpare
            self._myHasHotSpare=other._myHasHotSpare
            self._myHotSpareRequested=other._myHotSpareRequested
        
        if self.isCapableSpeedRequested():
            self.capableSpeed=other.capableSpeed
            self._myHasCapableSpeed=other._myHasCapableSpeed
            self._myCapableSpeedRequested=other._myCapableSpeedRequested
        
        if self.isCertifiedRequested():
            self.certified=other.certified
            self._myHasCertified=other._myHasCertified
            self._myCertifiedRequested=other._myCertifiedRequested
        
        if self.isDeviceWriteCacheRequested():
            self.deviceWriteCache=other.deviceWriteCache
            self._myHasDeviceWriteCache=other._myHasDeviceWriteCache
            self._myDeviceWriteCacheRequested=other._myDeviceWriteCacheRequested
        
        if self.isStateRawRequested():
            self.stateRaw=other.stateRaw
            self._myHasStateRaw=other._myHasStateRaw
            self._myStateRawRequested=other._myStateRawRequested
        
        if self.isManufactureWeekRequested():
            self.manufactureWeek=other.manufactureWeek
            self._myHasManufactureWeek=other._myHasManufactureWeek
            self._myManufactureWeekRequested=other._myManufactureWeekRequested
        
        if self.isNegotiatedSpeedRequested():
            self.negotiatedSpeed=other.negotiatedSpeed
            self._myHasNegotiatedSpeed=other._myHasNegotiatedSpeed
            self._myNegotiatedSpeedRequested=other._myNegotiatedSpeedRequested
        
        if self.isVendorIdRequested():
            self.vendorId=other.vendorId
            self._myHasVendorId=other._myHasVendorId
            self._myVendorIdRequested=other._myVendorIdRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasProductId():
            self.productId=other.productId
            self._myHasProductId=other._myHasProductId
            self._myProductIdRequested=other._myProductIdRequested
        
        if other.hasSasAddress():
            self.sasAddress=other.sasAddress
            self._myHasSasAddress=other._myHasSasAddress
            self._mySasAddressRequested=other._mySasAddressRequested
        
        if other.hasModelNumber():
            self.modelNumber=other.modelNumber
            self._myHasModelNumber=other._myHasModelNumber
            self._myModelNumberRequested=other._myModelNumberRequested
        
        if other.hasSerialNumber():
            self.serialNumber=other.serialNumber
            self._myHasSerialNumber=other._myHasSerialNumber
            self._mySerialNumberRequested=other._mySerialNumberRequested
        
        if other.hasUsedRaidSpace():
            self.usedRaidSpace=other.usedRaidSpace
            self._myHasUsedRaidSpace=other._myHasUsedRaidSpace
            self._myUsedRaidSpaceRequested=other._myUsedRaidSpaceRequested
        
        if other.hasStatusRaw():
            self.statusRaw=other.statusRaw
            self._myHasStatusRaw=other._myHasStatusRaw
            self._myStatusRawRequested=other._myStatusRawRequested
        
        if other.hasFirmwareRevision():
            self.firmwareRevision=other.firmwareRevision
            self._myHasFirmwareRevision=other._myHasFirmwareRevision
            self._myFirmwareRevisionRequested=other._myFirmwareRevisionRequested
        
        if other.hasSize():
            self.size=other.size
            self._myHasSize=other._myHasSize
            self._mySizeRequested=other._mySizeRequested
        
        if other.hasFailurePredicted():
            self.failurePredicted=other.failurePredicted
            self._myHasFailurePredicted=other._myHasFailurePredicted
            self._myFailurePredictedRequested=other._myFailurePredictedRequested
        
        if other.hasSizeRaw():
            self.sizeRaw=other.sizeRaw
            self._myHasSizeRaw=other._myHasSizeRaw
            self._mySizeRawRequested=other._mySizeRawRequested
        
        if other.hasDeviceLifeStatus():
            self.deviceLifeStatus=other.deviceLifeStatus
            self._myHasDeviceLifeStatus=other._myHasDeviceLifeStatus
            self._myDeviceLifeStatusRequested=other._myDeviceLifeStatusRequested
        
        if other.hasDeviceLifeRemaining():
            self.deviceLifeRemaining=other.deviceLifeRemaining
            self._myHasDeviceLifeRemaining=other._myHasDeviceLifeRemaining
            self._myDeviceLifeRemainingRequested=other._myDeviceLifeRemainingRequested
        
        if other.hasPowerStatus():
            self.powerStatus=other.powerStatus
            self._myHasPowerStatus=other._myHasPowerStatus
            self._myPowerStatusRequested=other._myPowerStatusRequested
        
        if other.hasState():
            self.state=other.state
            self._myHasState=other._myHasState
            self._myStateRequested=other._myStateRequested
        
        if other.hasProgress():
            self.progress=other.progress
            self._myHasProgress=other._myHasProgress
            self._myProgressRequested=other._myProgressRequested
        
        if other.hasStatus():
            self.status=other.status
            self._myHasStatus=other._myHasStatus
            self._myStatusRequested=other._myStatusRequested
        
        if other.hasManufactureYear():
            self.manufactureYear=other.manufactureYear
            self._myHasManufactureYear=other._myHasManufactureYear
            self._myManufactureYearRequested=other._myManufactureYearRequested
        
        if other.hasFailurePredictedRaw():
            self.failurePredictedRaw=other.failurePredictedRaw
            self._myHasFailurePredictedRaw=other._myHasFailurePredictedRaw
            self._myFailurePredictedRawRequested=other._myFailurePredictedRawRequested
        
        if other.hasMediaType():
            self.mediaType=other.mediaType
            self._myHasMediaType=other._myHasMediaType
            self._myMediaTypeRequested=other._myMediaTypeRequested
        
        if other.hasManufactureDay():
            self.manufactureDay=other.manufactureDay
            self._myHasManufactureDay=other._myHasManufactureDay
            self._myManufactureDayRequested=other._myManufactureDayRequested
        
        if other.hasAvailableRaidSpace():
            self.availableRaidSpace=other.availableRaidSpace
            self._myHasAvailableRaidSpace=other._myHasAvailableRaidSpace
            self._myAvailableRaidSpaceRequested=other._myAvailableRaidSpaceRequested
        
        if other.hasPartNumber():
            self.partNumber=other.partNumber
            self._myHasPartNumber=other._myHasPartNumber
            self._myPartNumberRequested=other._myPartNumberRequested
        
        if other.hasHotSpare():
            self.hotSpare=other.hotSpare
            self._myHasHotSpare=other._myHasHotSpare
            self._myHotSpareRequested=other._myHotSpareRequested
        
        if other.hasCapableSpeed():
            self.capableSpeed=other.capableSpeed
            self._myHasCapableSpeed=other._myHasCapableSpeed
            self._myCapableSpeedRequested=other._myCapableSpeedRequested
        
        if other.hasCertified():
            self.certified=other.certified
            self._myHasCertified=other._myHasCertified
            self._myCertifiedRequested=other._myCertifiedRequested
        
        if other.hasDeviceWriteCache():
            self.deviceWriteCache=other.deviceWriteCache
            self._myHasDeviceWriteCache=other._myHasDeviceWriteCache
            self._myDeviceWriteCacheRequested=other._myDeviceWriteCacheRequested
        
        if other.hasStateRaw():
            self.stateRaw=other.stateRaw
            self._myHasStateRaw=other._myHasStateRaw
            self._myStateRawRequested=other._myStateRawRequested
        
        if other.hasManufactureWeek():
            self.manufactureWeek=other.manufactureWeek
            self._myHasManufactureWeek=other._myHasManufactureWeek
            self._myManufactureWeekRequested=other._myManufactureWeekRequested
        
        if other.hasNegotiatedSpeed():
            self.negotiatedSpeed=other.negotiatedSpeed
            self._myHasNegotiatedSpeed=other._myHasNegotiatedSpeed
            self._myNegotiatedSpeedRequested=other._myNegotiatedSpeedRequested
        
        if other.hasVendorId():
            self.vendorId=other.vendorId
            self._myHasVendorId=other._myHasVendorId
            self._myVendorIdRequested=other._myVendorIdRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.productId=other.productId
        self._myHasProductId=other._myHasProductId
        
        self.sasAddress=other.sasAddress
        self._myHasSasAddress=other._myHasSasAddress
        
        self.modelNumber=other.modelNumber
        self._myHasModelNumber=other._myHasModelNumber
        
        self.serialNumber=other.serialNumber
        self._myHasSerialNumber=other._myHasSerialNumber
        
        self.usedRaidSpace=other.usedRaidSpace
        self._myHasUsedRaidSpace=other._myHasUsedRaidSpace
        
        self.statusRaw=other.statusRaw
        self._myHasStatusRaw=other._myHasStatusRaw
        
        self.firmwareRevision=other.firmwareRevision
        self._myHasFirmwareRevision=other._myHasFirmwareRevision
        
        self.size=other.size
        self._myHasSize=other._myHasSize
        
        self.failurePredicted=other.failurePredicted
        self._myHasFailurePredicted=other._myHasFailurePredicted
        
        self.sizeRaw=other.sizeRaw
        self._myHasSizeRaw=other._myHasSizeRaw
        
        self.deviceLifeStatus=other.deviceLifeStatus
        self._myHasDeviceLifeStatus=other._myHasDeviceLifeStatus
        
        self.deviceLifeRemaining=other.deviceLifeRemaining
        self._myHasDeviceLifeRemaining=other._myHasDeviceLifeRemaining
        
        self.powerStatus=other.powerStatus
        self._myHasPowerStatus=other._myHasPowerStatus
        
        self.state=other.state
        self._myHasState=other._myHasState
        
        self.progress=other.progress
        self._myHasProgress=other._myHasProgress
        
        self.status=other.status
        self._myHasStatus=other._myHasStatus
        
        self.manufactureYear=other.manufactureYear
        self._myHasManufactureYear=other._myHasManufactureYear
        
        self.failurePredictedRaw=other.failurePredictedRaw
        self._myHasFailurePredictedRaw=other._myHasFailurePredictedRaw
        
        self.mediaType=other.mediaType
        self._myHasMediaType=other._myHasMediaType
        
        self.manufactureDay=other.manufactureDay
        self._myHasManufactureDay=other._myHasManufactureDay
        
        self.availableRaidSpace=other.availableRaidSpace
        self._myHasAvailableRaidSpace=other._myHasAvailableRaidSpace
        
        self.partNumber=other.partNumber
        self._myHasPartNumber=other._myHasPartNumber
        
        self.hotSpare=other.hotSpare
        self._myHasHotSpare=other._myHasHotSpare
        
        self.capableSpeed=other.capableSpeed
        self._myHasCapableSpeed=other._myHasCapableSpeed
        
        self.certified=other.certified
        self._myHasCertified=other._myHasCertified
        
        self.deviceWriteCache=other.deviceWriteCache
        self._myHasDeviceWriteCache=other._myHasDeviceWriteCache
        
        self.stateRaw=other.stateRaw
        self._myHasStateRaw=other._myHasStateRaw
        
        self.manufactureWeek=other.manufactureWeek
        self._myHasManufactureWeek=other._myHasManufactureWeek
        
        self.negotiatedSpeed=other.negotiatedSpeed
        self._myHasNegotiatedSpeed=other._myHasNegotiatedSpeed
        
        self.vendorId=other.vendorId
        self._myHasVendorId=other._myHasVendorId
        


    def setAllNumericToZero (self):
        
        self.size=0
        self.setHasSize()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasSize():
            if other.hasSize():
                self.size -= other.size
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasSize():
            if other.hasSize():
                self.size += other.size
        
        
        pass


    # has...() methods

    def hasProductId (self):
        return self._myHasProductId

    def hasSasAddress (self):
        return self._myHasSasAddress

    def hasModelNumber (self):
        return self._myHasModelNumber

    def hasSerialNumber (self):
        return self._myHasSerialNumber

    def hasUsedRaidSpace (self):
        return self._myHasUsedRaidSpace

    def hasStatusRaw (self):
        return self._myHasStatusRaw

    def hasFirmwareRevision (self):
        return self._myHasFirmwareRevision

    def hasSize (self):
        return self._myHasSize

    def hasFailurePredicted (self):
        return self._myHasFailurePredicted

    def hasSizeRaw (self):
        return self._myHasSizeRaw

    def hasDeviceLifeStatus (self):
        return self._myHasDeviceLifeStatus

    def hasDeviceLifeRemaining (self):
        return self._myHasDeviceLifeRemaining

    def hasPowerStatus (self):
        return self._myHasPowerStatus

    def hasState (self):
        return self._myHasState

    def hasProgress (self):
        return self._myHasProgress

    def hasStatus (self):
        return self._myHasStatus

    def hasManufactureYear (self):
        return self._myHasManufactureYear

    def hasFailurePredictedRaw (self):
        return self._myHasFailurePredictedRaw

    def hasMediaType (self):
        return self._myHasMediaType

    def hasManufactureDay (self):
        return self._myHasManufactureDay

    def hasAvailableRaidSpace (self):
        return self._myHasAvailableRaidSpace

    def hasPartNumber (self):
        return self._myHasPartNumber

    def hasHotSpare (self):
        return self._myHasHotSpare

    def hasCapableSpeed (self):
        return self._myHasCapableSpeed

    def hasCertified (self):
        return self._myHasCertified

    def hasDeviceWriteCache (self):
        return self._myHasDeviceWriteCache

    def hasStateRaw (self):
        return self._myHasStateRaw

    def hasManufactureWeek (self):
        return self._myHasManufactureWeek

    def hasNegotiatedSpeed (self):
        return self._myHasNegotiatedSpeed

    def hasVendorId (self):
        return self._myHasVendorId




    # setHas...() methods

    def setHasProductId (self):
        self._myHasProductId=True

    def setHasSasAddress (self):
        self._myHasSasAddress=True

    def setHasModelNumber (self):
        self._myHasModelNumber=True

    def setHasSerialNumber (self):
        self._myHasSerialNumber=True

    def setHasUsedRaidSpace (self):
        self._myHasUsedRaidSpace=True

    def setHasStatusRaw (self):
        self._myHasStatusRaw=True

    def setHasFirmwareRevision (self):
        self._myHasFirmwareRevision=True

    def setHasSize (self):
        self._myHasSize=True

    def setHasFailurePredicted (self):
        self._myHasFailurePredicted=True

    def setHasSizeRaw (self):
        self._myHasSizeRaw=True

    def setHasDeviceLifeStatus (self):
        self._myHasDeviceLifeStatus=True

    def setHasDeviceLifeRemaining (self):
        self._myHasDeviceLifeRemaining=True

    def setHasPowerStatus (self):
        self._myHasPowerStatus=True

    def setHasState (self):
        self._myHasState=True

    def setHasProgress (self):
        self._myHasProgress=True

    def setHasStatus (self):
        self._myHasStatus=True

    def setHasManufactureYear (self):
        self._myHasManufactureYear=True

    def setHasFailurePredictedRaw (self):
        self._myHasFailurePredictedRaw=True

    def setHasMediaType (self):
        self._myHasMediaType=True

    def setHasManufactureDay (self):
        self._myHasManufactureDay=True

    def setHasAvailableRaidSpace (self):
        self._myHasAvailableRaidSpace=True

    def setHasPartNumber (self):
        self._myHasPartNumber=True

    def setHasHotSpare (self):
        self._myHasHotSpare=True

    def setHasCapableSpeed (self):
        self._myHasCapableSpeed=True

    def setHasCertified (self):
        self._myHasCertified=True

    def setHasDeviceWriteCache (self):
        self._myHasDeviceWriteCache=True

    def setHasStateRaw (self):
        self._myHasStateRaw=True

    def setHasManufactureWeek (self):
        self._myHasManufactureWeek=True

    def setHasNegotiatedSpeed (self):
        self._myHasNegotiatedSpeed=True

    def setHasVendorId (self):
        self._myHasVendorId=True




    # isRequested...() methods

    def isProductIdRequested (self):
        return self._myProductIdRequested

    def isSasAddressRequested (self):
        return self._mySasAddressRequested

    def isModelNumberRequested (self):
        return self._myModelNumberRequested

    def isSerialNumberRequested (self):
        return self._mySerialNumberRequested

    def isUsedRaidSpaceRequested (self):
        return self._myUsedRaidSpaceRequested

    def isStatusRawRequested (self):
        return self._myStatusRawRequested

    def isFirmwareRevisionRequested (self):
        return self._myFirmwareRevisionRequested

    def isSizeRequested (self):
        return self._mySizeRequested

    def isFailurePredictedRequested (self):
        return self._myFailurePredictedRequested

    def isSizeRawRequested (self):
        return self._mySizeRawRequested

    def isDeviceLifeStatusRequested (self):
        return self._myDeviceLifeStatusRequested

    def isDeviceLifeRemainingRequested (self):
        return self._myDeviceLifeRemainingRequested

    def isPowerStatusRequested (self):
        return self._myPowerStatusRequested

    def isStateRequested (self):
        return self._myStateRequested

    def isProgressRequested (self):
        return self._myProgressRequested

    def isStatusRequested (self):
        return self._myStatusRequested

    def isManufactureYearRequested (self):
        return self._myManufactureYearRequested

    def isFailurePredictedRawRequested (self):
        return self._myFailurePredictedRawRequested

    def isMediaTypeRequested (self):
        return self._myMediaTypeRequested

    def isManufactureDayRequested (self):
        return self._myManufactureDayRequested

    def isAvailableRaidSpaceRequested (self):
        return self._myAvailableRaidSpaceRequested

    def isPartNumberRequested (self):
        return self._myPartNumberRequested

    def isHotSpareRequested (self):
        return self._myHotSpareRequested

    def isCapableSpeedRequested (self):
        return self._myCapableSpeedRequested

    def isCertifiedRequested (self):
        return self._myCertifiedRequested

    def isDeviceWriteCacheRequested (self):
        return self._myDeviceWriteCacheRequested

    def isStateRawRequested (self):
        return self._myStateRawRequested

    def isManufactureWeekRequested (self):
        return self._myManufactureWeekRequested

    def isNegotiatedSpeedRequested (self):
        return self._myNegotiatedSpeedRequested

    def isVendorIdRequested (self):
        return self._myVendorIdRequested




    # setRequested...() methods

    def setProductIdRequested (self):
        self._myProductIdRequested=True

    def setSasAddressRequested (self):
        self._mySasAddressRequested=True

    def setModelNumberRequested (self):
        self._myModelNumberRequested=True

    def setSerialNumberRequested (self):
        self._mySerialNumberRequested=True

    def setUsedRaidSpaceRequested (self):
        self._myUsedRaidSpaceRequested=True

    def setStatusRawRequested (self):
        self._myStatusRawRequested=True

    def setFirmwareRevisionRequested (self):
        self._myFirmwareRevisionRequested=True

    def setSizeRequested (self):
        self._mySizeRequested=True

    def setFailurePredictedRequested (self):
        self._myFailurePredictedRequested=True

    def setSizeRawRequested (self):
        self._mySizeRawRequested=True

    def setDeviceLifeStatusRequested (self):
        self._myDeviceLifeStatusRequested=True

    def setDeviceLifeRemainingRequested (self):
        self._myDeviceLifeRemainingRequested=True

    def setPowerStatusRequested (self):
        self._myPowerStatusRequested=True

    def setStateRequested (self):
        self._myStateRequested=True

    def setProgressRequested (self):
        self._myProgressRequested=True

    def setStatusRequested (self):
        self._myStatusRequested=True

    def setManufactureYearRequested (self):
        self._myManufactureYearRequested=True

    def setFailurePredictedRawRequested (self):
        self._myFailurePredictedRawRequested=True

    def setMediaTypeRequested (self):
        self._myMediaTypeRequested=True

    def setManufactureDayRequested (self):
        self._myManufactureDayRequested=True

    def setAvailableRaidSpaceRequested (self):
        self._myAvailableRaidSpaceRequested=True

    def setPartNumberRequested (self):
        self._myPartNumberRequested=True

    def setHotSpareRequested (self):
        self._myHotSpareRequested=True

    def setCapableSpeedRequested (self):
        self._myCapableSpeedRequested=True

    def setCertifiedRequested (self):
        self._myCertifiedRequested=True

    def setDeviceWriteCacheRequested (self):
        self._myDeviceWriteCacheRequested=True

    def setStateRawRequested (self):
        self._myStateRawRequested=True

    def setManufactureWeekRequested (self):
        self._myManufactureWeekRequested=True

    def setNegotiatedSpeedRequested (self):
        self._myNegotiatedSpeedRequested=True

    def setVendorIdRequested (self):
        self._myVendorIdRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myProductIdRequested:
            x = "+ProductId="
            if self._myHasProductId:
                leafStr = str(self.productId)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySasAddressRequested:
            x = "+SasAddress="
            if self._myHasSasAddress:
                leafStr = str(self.sasAddress)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myModelNumberRequested:
            x = "+ModelNumber="
            if self._myHasModelNumber:
                leafStr = str(self.modelNumber)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySerialNumberRequested:
            x = "+SerialNumber="
            if self._myHasSerialNumber:
                leafStr = str(self.serialNumber)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myUsedRaidSpaceRequested:
            x = "+UsedRaidSpace="
            if self._myHasUsedRaidSpace:
                leafStr = str(self.usedRaidSpace)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStatusRawRequested:
            x = "+StatusRaw="
            if self._myHasStatusRaw:
                leafStr = str(self.statusRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFirmwareRevisionRequested:
            x = "+FirmwareRevision="
            if self._myHasFirmwareRevision:
                leafStr = str(self.firmwareRevision)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySizeRequested:
            x = "+Size="
            if self._myHasSize:
                leafStr = str(self.size)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFailurePredictedRequested:
            x = "+FailurePredicted="
            if self._myHasFailurePredicted:
                leafStr = str(self.failurePredicted)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySizeRawRequested:
            x = "+SizeRaw="
            if self._myHasSizeRaw:
                leafStr = str(self.sizeRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myDeviceLifeStatusRequested:
            x = "+DeviceLifeStatus="
            if self._myHasDeviceLifeStatus:
                leafStr = str(self.deviceLifeStatus)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myDeviceLifeRemainingRequested:
            x = "+DeviceLifeRemaining="
            if self._myHasDeviceLifeRemaining:
                leafStr = str(self.deviceLifeRemaining)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPowerStatusRequested:
            x = "+PowerStatus="
            if self._myHasPowerStatus:
                leafStr = str(self.powerStatus)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStateRequested:
            x = "+State="
            if self._myHasState:
                leafStr = str(self.state)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myProgressRequested:
            x = "+Progress="
            if self._myHasProgress:
                leafStr = str(self.progress)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStatusRequested:
            x = "+Status="
            if self._myHasStatus:
                leafStr = str(self.status)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myManufactureYearRequested:
            x = "+ManufactureYear="
            if self._myHasManufactureYear:
                leafStr = str(self.manufactureYear)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFailurePredictedRawRequested:
            x = "+FailurePredictedRaw="
            if self._myHasFailurePredictedRaw:
                leafStr = str(self.failurePredictedRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMediaTypeRequested:
            x = "+MediaType="
            if self._myHasMediaType:
                leafStr = str(self.mediaType)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myManufactureDayRequested:
            x = "+ManufactureDay="
            if self._myHasManufactureDay:
                leafStr = str(self.manufactureDay)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myAvailableRaidSpaceRequested:
            x = "+AvailableRaidSpace="
            if self._myHasAvailableRaidSpace:
                leafStr = str(self.availableRaidSpace)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPartNumberRequested:
            x = "+PartNumber="
            if self._myHasPartNumber:
                leafStr = str(self.partNumber)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myHotSpareRequested:
            x = "+HotSpare="
            if self._myHasHotSpare:
                leafStr = str(self.hotSpare)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myCapableSpeedRequested:
            x = "+CapableSpeed="
            if self._myHasCapableSpeed:
                leafStr = str(self.capableSpeed)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myCertifiedRequested:
            x = "+Certified="
            if self._myHasCertified:
                leafStr = str(self.certified)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myDeviceWriteCacheRequested:
            x = "+DeviceWriteCache="
            if self._myHasDeviceWriteCache:
                leafStr = str(self.deviceWriteCache)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStateRawRequested:
            x = "+StateRaw="
            if self._myHasStateRaw:
                leafStr = str(self.stateRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myManufactureWeekRequested:
            x = "+ManufactureWeek="
            if self._myHasManufactureWeek:
                leafStr = str(self.manufactureWeek)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNegotiatedSpeedRequested:
            x = "+NegotiatedSpeed="
            if self._myHasNegotiatedSpeed:
                leafStr = str(self.negotiatedSpeed)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myVendorIdRequested:
            x = "+VendorId="
            if self._myHasVendorId:
                leafStr = str(self.vendorId)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ProductId="
        if self._myHasProductId:
            leafStr = str(self.productId)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myProductIdRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+SasAddress="
        if self._myHasSasAddress:
            leafStr = str(self.sasAddress)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySasAddressRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ModelNumber="
        if self._myHasModelNumber:
            leafStr = str(self.modelNumber)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myModelNumberRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+SerialNumber="
        if self._myHasSerialNumber:
            leafStr = str(self.serialNumber)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySerialNumberRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+UsedRaidSpace="
        if self._myHasUsedRaidSpace:
            leafStr = str(self.usedRaidSpace)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myUsedRaidSpaceRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+StatusRaw="
        if self._myHasStatusRaw:
            leafStr = str(self.statusRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStatusRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FirmwareRevision="
        if self._myHasFirmwareRevision:
            leafStr = str(self.firmwareRevision)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFirmwareRevisionRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Size="
        if self._myHasSize:
            leafStr = str(self.size)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySizeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FailurePredicted="
        if self._myHasFailurePredicted:
            leafStr = str(self.failurePredicted)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFailurePredictedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+SizeRaw="
        if self._myHasSizeRaw:
            leafStr = str(self.sizeRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySizeRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+DeviceLifeStatus="
        if self._myHasDeviceLifeStatus:
            leafStr = str(self.deviceLifeStatus)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myDeviceLifeStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+DeviceLifeRemaining="
        if self._myHasDeviceLifeRemaining:
            leafStr = str(self.deviceLifeRemaining)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myDeviceLifeRemainingRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PowerStatus="
        if self._myHasPowerStatus:
            leafStr = str(self.powerStatus)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPowerStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+State="
        if self._myHasState:
            leafStr = str(self.state)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStateRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Progress="
        if self._myHasProgress:
            leafStr = str(self.progress)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myProgressRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Status="
        if self._myHasStatus:
            leafStr = str(self.status)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ManufactureYear="
        if self._myHasManufactureYear:
            leafStr = str(self.manufactureYear)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myManufactureYearRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FailurePredictedRaw="
        if self._myHasFailurePredictedRaw:
            leafStr = str(self.failurePredictedRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFailurePredictedRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MediaType="
        if self._myHasMediaType:
            leafStr = str(self.mediaType)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMediaTypeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ManufactureDay="
        if self._myHasManufactureDay:
            leafStr = str(self.manufactureDay)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myManufactureDayRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+AvailableRaidSpace="
        if self._myHasAvailableRaidSpace:
            leafStr = str(self.availableRaidSpace)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myAvailableRaidSpaceRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PartNumber="
        if self._myHasPartNumber:
            leafStr = str(self.partNumber)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPartNumberRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+HotSpare="
        if self._myHasHotSpare:
            leafStr = str(self.hotSpare)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myHotSpareRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+CapableSpeed="
        if self._myHasCapableSpeed:
            leafStr = str(self.capableSpeed)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCapableSpeedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Certified="
        if self._myHasCertified:
            leafStr = str(self.certified)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCertifiedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+DeviceWriteCache="
        if self._myHasDeviceWriteCache:
            leafStr = str(self.deviceWriteCache)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myDeviceWriteCacheRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+StateRaw="
        if self._myHasStateRaw:
            leafStr = str(self.stateRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStateRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ManufactureWeek="
        if self._myHasManufactureWeek:
            leafStr = str(self.manufactureWeek)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myManufactureWeekRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+NegotiatedSpeed="
        if self._myHasNegotiatedSpeed:
            leafStr = str(self.negotiatedSpeed)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNegotiatedSpeedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+VendorId="
        if self._myHasVendorId:
            leafStr = str(self.vendorId)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myVendorIdRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setProductIdRequested()
        self.setSasAddressRequested()
        self.setModelNumberRequested()
        self.setSerialNumberRequested()
        self.setUsedRaidSpaceRequested()
        self.setStatusRawRequested()
        self.setFirmwareRevisionRequested()
        self.setSizeRequested()
        self.setFailurePredictedRequested()
        self.setSizeRawRequested()
        self.setDeviceLifeStatusRequested()
        self.setDeviceLifeRemainingRequested()
        self.setPowerStatusRequested()
        self.setStateRequested()
        self.setProgressRequested()
        self.setStatusRequested()
        self.setManufactureYearRequested()
        self.setFailurePredictedRawRequested()
        self.setMediaTypeRequested()
        self.setManufactureDayRequested()
        self.setAvailableRaidSpaceRequested()
        self.setPartNumberRequested()
        self.setHotSpareRequested()
        self.setCapableSpeedRequested()
        self.setCertifiedRequested()
        self.setDeviceWriteCacheRequested()
        self.setStateRawRequested()
        self.setManufactureWeekRequested()
        self.setNegotiatedSpeedRequested()
        self.setVendorIdRequested()
        
        


    def setProductId (self, productId):
        self.productId = productId
        self.setHasProductId()

    def setSasAddress (self, sasAddress):
        self.sasAddress = sasAddress
        self.setHasSasAddress()

    def setModelNumber (self, modelNumber):
        self.modelNumber = modelNumber
        self.setHasModelNumber()

    def setSerialNumber (self, serialNumber):
        self.serialNumber = serialNumber
        self.setHasSerialNumber()

    def setUsedRaidSpace (self, usedRaidSpace):
        self.usedRaidSpace = usedRaidSpace
        self.setHasUsedRaidSpace()

    def setStatusRaw (self, statusRaw):
        self.statusRaw = statusRaw
        self.setHasStatusRaw()

    def setFirmwareRevision (self, firmwareRevision):
        self.firmwareRevision = firmwareRevision
        self.setHasFirmwareRevision()

    def setSize (self, size):
        self.size = size
        self.setHasSize()

    def setFailurePredicted (self, failurePredicted):
        self.failurePredicted = failurePredicted
        self.setHasFailurePredicted()

    def setSizeRaw (self, sizeRaw):
        self.sizeRaw = sizeRaw
        self.setHasSizeRaw()

    def setDeviceLifeStatus (self, deviceLifeStatus):
        self.deviceLifeStatus = deviceLifeStatus
        self.setHasDeviceLifeStatus()

    def setDeviceLifeRemaining (self, deviceLifeRemaining):
        self.deviceLifeRemaining = deviceLifeRemaining
        self.setHasDeviceLifeRemaining()

    def setPowerStatus (self, powerStatus):
        self.powerStatus = powerStatus
        self.setHasPowerStatus()

    def setState (self, state):
        self.state = state
        self.setHasState()

    def setProgress (self, progress):
        self.progress = progress
        self.setHasProgress()

    def setStatus (self, status):
        self.status = status
        self.setHasStatus()

    def setManufactureYear (self, manufactureYear):
        self.manufactureYear = manufactureYear
        self.setHasManufactureYear()

    def setFailurePredictedRaw (self, failurePredictedRaw):
        self.failurePredictedRaw = failurePredictedRaw
        self.setHasFailurePredictedRaw()

    def setMediaType (self, mediaType):
        self.mediaType = mediaType
        self.setHasMediaType()

    def setManufactureDay (self, manufactureDay):
        self.manufactureDay = manufactureDay
        self.setHasManufactureDay()

    def setAvailableRaidSpace (self, availableRaidSpace):
        self.availableRaidSpace = availableRaidSpace
        self.setHasAvailableRaidSpace()

    def setPartNumber (self, partNumber):
        self.partNumber = partNumber
        self.setHasPartNumber()

    def setHotSpare (self, hotSpare):
        self.hotSpare = hotSpare
        self.setHasHotSpare()

    def setCapableSpeed (self, capableSpeed):
        self.capableSpeed = capableSpeed
        self.setHasCapableSpeed()

    def setCertified (self, certified):
        self.certified = certified
        self.setHasCertified()

    def setDeviceWriteCache (self, deviceWriteCache):
        self.deviceWriteCache = deviceWriteCache
        self.setHasDeviceWriteCache()

    def setStateRaw (self, stateRaw):
        self.stateRaw = stateRaw
        self.setHasStateRaw()

    def setManufactureWeek (self, manufactureWeek):
        self.manufactureWeek = manufactureWeek
        self.setHasManufactureWeek()

    def setNegotiatedSpeed (self, negotiatedSpeed):
        self.negotiatedSpeed = negotiatedSpeed
        self.setHasNegotiatedSpeed()

    def setVendorId (self, vendorId):
        self.vendorId = vendorId
        self.setHasVendorId()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "storage", 
            "isCurrent": false
        }, 
        {
            "namespace": "disk", 
            "isCurrent": false
        }, 
        {
            "namespace": "physical", 
            "isCurrent": false
        }, 
        {
            "namespace": "status", 
            "isCurrent": true
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
    "createTime": "2013"
}
"""


