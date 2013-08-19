


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceOnlineStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceStatusType


class StatusOperData (object):

    def __init__ (self):

        self.firmwareVersion = ""
        self._myHasFirmwareVersion=False
        self._myFirmwareVersionRequested=False
        
        self.index = ""
        self._myHasIndex=False
        self._myIndexRequested=False
        
        self.fruDevice = ""
        self._myHasFruDevice=False
        self._myFruDeviceRequested=False
        
        self.manufactureDate = ""
        self._myHasManufactureDate=False
        self._myManufactureDateRequested=False
        
        self.onlineStatus = PowerSupplyDeviceOnlineStatusType.kNotAvailable
        self._myHasOnlineStatus=False
        self._myOnlineStatusRequested=False
        
        self.partNumber = ""
        self._myHasPartNumber=False
        self._myPartNumberRequested=False
        
        self.serialNumber = ""
        self._myHasSerialNumber=False
        self._mySerialNumberRequested=False
        
        self.status = PowerSupplyDeviceStatusType.kUnknown
        self._myHasStatus=False
        self._myStatusRequested=False
        
        self.location = ""
        self._myHasLocation=False
        self._myLocationRequested=False
        
        self.onlineStatusRaw = ""
        self._myHasOnlineStatusRaw=False
        self._myOnlineStatusRawRequested=False
        
        self.statusRaw = ""
        self._myHasStatusRaw=False
        self._myStatusRawRequested=False
        
        self.inputType = ""
        self._myHasInputType=False
        self._myInputTypeRequested=False
        
        self.ratedInputWattage = ""
        self._myHasRatedInputWattage=False
        self._myRatedInputWattageRequested=False
        
        self.maximumOutputWattage = ""
        self._myHasMaximumOutputWattage=False
        self._myMaximumOutputWattageRequested=False
        
        self.manufacturer = ""
        self._myHasManufacturer=False
        self._myManufacturerRequested=False
        
        self.revision = ""
        self._myHasRevision=False
        self._myRevisionRequested=False
        


    def copyFrom (self, other):

        self.firmwareVersion=other.firmwareVersion
        self._myHasFirmwareVersion=other._myHasFirmwareVersion
        self._myFirmwareVersionRequested=other._myFirmwareVersionRequested
        
        self.index=other.index
        self._myHasIndex=other._myHasIndex
        self._myIndexRequested=other._myIndexRequested
        
        self.fruDevice=other.fruDevice
        self._myHasFruDevice=other._myHasFruDevice
        self._myFruDeviceRequested=other._myFruDeviceRequested
        
        self.manufactureDate=other.manufactureDate
        self._myHasManufactureDate=other._myHasManufactureDate
        self._myManufactureDateRequested=other._myManufactureDateRequested
        
        self.onlineStatus=other.onlineStatus
        self._myHasOnlineStatus=other._myHasOnlineStatus
        self._myOnlineStatusRequested=other._myOnlineStatusRequested
        
        self.partNumber=other.partNumber
        self._myHasPartNumber=other._myHasPartNumber
        self._myPartNumberRequested=other._myPartNumberRequested
        
        self.serialNumber=other.serialNumber
        self._myHasSerialNumber=other._myHasSerialNumber
        self._mySerialNumberRequested=other._mySerialNumberRequested
        
        self.status=other.status
        self._myHasStatus=other._myHasStatus
        self._myStatusRequested=other._myStatusRequested
        
        self.location=other.location
        self._myHasLocation=other._myHasLocation
        self._myLocationRequested=other._myLocationRequested
        
        self.onlineStatusRaw=other.onlineStatusRaw
        self._myHasOnlineStatusRaw=other._myHasOnlineStatusRaw
        self._myOnlineStatusRawRequested=other._myOnlineStatusRawRequested
        
        self.statusRaw=other.statusRaw
        self._myHasStatusRaw=other._myHasStatusRaw
        self._myStatusRawRequested=other._myStatusRawRequested
        
        self.inputType=other.inputType
        self._myHasInputType=other._myHasInputType
        self._myInputTypeRequested=other._myInputTypeRequested
        
        self.ratedInputWattage=other.ratedInputWattage
        self._myHasRatedInputWattage=other._myHasRatedInputWattage
        self._myRatedInputWattageRequested=other._myRatedInputWattageRequested
        
        self.maximumOutputWattage=other.maximumOutputWattage
        self._myHasMaximumOutputWattage=other._myHasMaximumOutputWattage
        self._myMaximumOutputWattageRequested=other._myMaximumOutputWattageRequested
        
        self.manufacturer=other.manufacturer
        self._myHasManufacturer=other._myHasManufacturer
        self._myManufacturerRequested=other._myManufacturerRequested
        
        self.revision=other.revision
        self._myHasRevision=other._myHasRevision
        self._myRevisionRequested=other._myRevisionRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isFirmwareVersionRequested():
            self.firmwareVersion=other.firmwareVersion
            self._myHasFirmwareVersion=other._myHasFirmwareVersion
            self._myFirmwareVersionRequested=other._myFirmwareVersionRequested
        
        if self.isIndexRequested():
            self.index=other.index
            self._myHasIndex=other._myHasIndex
            self._myIndexRequested=other._myIndexRequested
        
        if self.isFruDeviceRequested():
            self.fruDevice=other.fruDevice
            self._myHasFruDevice=other._myHasFruDevice
            self._myFruDeviceRequested=other._myFruDeviceRequested
        
        if self.isManufactureDateRequested():
            self.manufactureDate=other.manufactureDate
            self._myHasManufactureDate=other._myHasManufactureDate
            self._myManufactureDateRequested=other._myManufactureDateRequested
        
        if self.isOnlineStatusRequested():
            self.onlineStatus=other.onlineStatus
            self._myHasOnlineStatus=other._myHasOnlineStatus
            self._myOnlineStatusRequested=other._myOnlineStatusRequested
        
        if self.isPartNumberRequested():
            self.partNumber=other.partNumber
            self._myHasPartNumber=other._myHasPartNumber
            self._myPartNumberRequested=other._myPartNumberRequested
        
        if self.isSerialNumberRequested():
            self.serialNumber=other.serialNumber
            self._myHasSerialNumber=other._myHasSerialNumber
            self._mySerialNumberRequested=other._mySerialNumberRequested
        
        if self.isStatusRequested():
            self.status=other.status
            self._myHasStatus=other._myHasStatus
            self._myStatusRequested=other._myStatusRequested
        
        if self.isLocationRequested():
            self.location=other.location
            self._myHasLocation=other._myHasLocation
            self._myLocationRequested=other._myLocationRequested
        
        if self.isOnlineStatusRawRequested():
            self.onlineStatusRaw=other.onlineStatusRaw
            self._myHasOnlineStatusRaw=other._myHasOnlineStatusRaw
            self._myOnlineStatusRawRequested=other._myOnlineStatusRawRequested
        
        if self.isStatusRawRequested():
            self.statusRaw=other.statusRaw
            self._myHasStatusRaw=other._myHasStatusRaw
            self._myStatusRawRequested=other._myStatusRawRequested
        
        if self.isInputTypeRequested():
            self.inputType=other.inputType
            self._myHasInputType=other._myHasInputType
            self._myInputTypeRequested=other._myInputTypeRequested
        
        if self.isRatedInputWattageRequested():
            self.ratedInputWattage=other.ratedInputWattage
            self._myHasRatedInputWattage=other._myHasRatedInputWattage
            self._myRatedInputWattageRequested=other._myRatedInputWattageRequested
        
        if self.isMaximumOutputWattageRequested():
            self.maximumOutputWattage=other.maximumOutputWattage
            self._myHasMaximumOutputWattage=other._myHasMaximumOutputWattage
            self._myMaximumOutputWattageRequested=other._myMaximumOutputWattageRequested
        
        if self.isManufacturerRequested():
            self.manufacturer=other.manufacturer
            self._myHasManufacturer=other._myHasManufacturer
            self._myManufacturerRequested=other._myManufacturerRequested
        
        if self.isRevisionRequested():
            self.revision=other.revision
            self._myHasRevision=other._myHasRevision
            self._myRevisionRequested=other._myRevisionRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasFirmwareVersion():
            self.firmwareVersion=other.firmwareVersion
            self._myHasFirmwareVersion=other._myHasFirmwareVersion
            self._myFirmwareVersionRequested=other._myFirmwareVersionRequested
        
        if other.hasIndex():
            self.index=other.index
            self._myHasIndex=other._myHasIndex
            self._myIndexRequested=other._myIndexRequested
        
        if other.hasFruDevice():
            self.fruDevice=other.fruDevice
            self._myHasFruDevice=other._myHasFruDevice
            self._myFruDeviceRequested=other._myFruDeviceRequested
        
        if other.hasManufactureDate():
            self.manufactureDate=other.manufactureDate
            self._myHasManufactureDate=other._myHasManufactureDate
            self._myManufactureDateRequested=other._myManufactureDateRequested
        
        if other.hasOnlineStatus():
            self.onlineStatus=other.onlineStatus
            self._myHasOnlineStatus=other._myHasOnlineStatus
            self._myOnlineStatusRequested=other._myOnlineStatusRequested
        
        if other.hasPartNumber():
            self.partNumber=other.partNumber
            self._myHasPartNumber=other._myHasPartNumber
            self._myPartNumberRequested=other._myPartNumberRequested
        
        if other.hasSerialNumber():
            self.serialNumber=other.serialNumber
            self._myHasSerialNumber=other._myHasSerialNumber
            self._mySerialNumberRequested=other._mySerialNumberRequested
        
        if other.hasStatus():
            self.status=other.status
            self._myHasStatus=other._myHasStatus
            self._myStatusRequested=other._myStatusRequested
        
        if other.hasLocation():
            self.location=other.location
            self._myHasLocation=other._myHasLocation
            self._myLocationRequested=other._myLocationRequested
        
        if other.hasOnlineStatusRaw():
            self.onlineStatusRaw=other.onlineStatusRaw
            self._myHasOnlineStatusRaw=other._myHasOnlineStatusRaw
            self._myOnlineStatusRawRequested=other._myOnlineStatusRawRequested
        
        if other.hasStatusRaw():
            self.statusRaw=other.statusRaw
            self._myHasStatusRaw=other._myHasStatusRaw
            self._myStatusRawRequested=other._myStatusRawRequested
        
        if other.hasInputType():
            self.inputType=other.inputType
            self._myHasInputType=other._myHasInputType
            self._myInputTypeRequested=other._myInputTypeRequested
        
        if other.hasRatedInputWattage():
            self.ratedInputWattage=other.ratedInputWattage
            self._myHasRatedInputWattage=other._myHasRatedInputWattage
            self._myRatedInputWattageRequested=other._myRatedInputWattageRequested
        
        if other.hasMaximumOutputWattage():
            self.maximumOutputWattage=other.maximumOutputWattage
            self._myHasMaximumOutputWattage=other._myHasMaximumOutputWattage
            self._myMaximumOutputWattageRequested=other._myMaximumOutputWattageRequested
        
        if other.hasManufacturer():
            self.manufacturer=other.manufacturer
            self._myHasManufacturer=other._myHasManufacturer
            self._myManufacturerRequested=other._myManufacturerRequested
        
        if other.hasRevision():
            self.revision=other.revision
            self._myHasRevision=other._myHasRevision
            self._myRevisionRequested=other._myRevisionRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.firmwareVersion=other.firmwareVersion
        self._myHasFirmwareVersion=other._myHasFirmwareVersion
        
        self.index=other.index
        self._myHasIndex=other._myHasIndex
        
        self.fruDevice=other.fruDevice
        self._myHasFruDevice=other._myHasFruDevice
        
        self.manufactureDate=other.manufactureDate
        self._myHasManufactureDate=other._myHasManufactureDate
        
        self.onlineStatus=other.onlineStatus
        self._myHasOnlineStatus=other._myHasOnlineStatus
        
        self.partNumber=other.partNumber
        self._myHasPartNumber=other._myHasPartNumber
        
        self.serialNumber=other.serialNumber
        self._myHasSerialNumber=other._myHasSerialNumber
        
        self.status=other.status
        self._myHasStatus=other._myHasStatus
        
        self.location=other.location
        self._myHasLocation=other._myHasLocation
        
        self.onlineStatusRaw=other.onlineStatusRaw
        self._myHasOnlineStatusRaw=other._myHasOnlineStatusRaw
        
        self.statusRaw=other.statusRaw
        self._myHasStatusRaw=other._myHasStatusRaw
        
        self.inputType=other.inputType
        self._myHasInputType=other._myHasInputType
        
        self.ratedInputWattage=other.ratedInputWattage
        self._myHasRatedInputWattage=other._myHasRatedInputWattage
        
        self.maximumOutputWattage=other.maximumOutputWattage
        self._myHasMaximumOutputWattage=other._myHasMaximumOutputWattage
        
        self.manufacturer=other.manufacturer
        self._myHasManufacturer=other._myHasManufacturer
        
        self.revision=other.revision
        self._myHasRevision=other._myHasRevision
        


    def setAllNumericToZero (self):
        
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        pass


    # has...() methods

    def hasFirmwareVersion (self):
        return self._myHasFirmwareVersion

    def hasIndex (self):
        return self._myHasIndex

    def hasFruDevice (self):
        return self._myHasFruDevice

    def hasManufactureDate (self):
        return self._myHasManufactureDate

    def hasOnlineStatus (self):
        return self._myHasOnlineStatus

    def hasPartNumber (self):
        return self._myHasPartNumber

    def hasSerialNumber (self):
        return self._myHasSerialNumber

    def hasStatus (self):
        return self._myHasStatus

    def hasLocation (self):
        return self._myHasLocation

    def hasOnlineStatusRaw (self):
        return self._myHasOnlineStatusRaw

    def hasStatusRaw (self):
        return self._myHasStatusRaw

    def hasInputType (self):
        return self._myHasInputType

    def hasRatedInputWattage (self):
        return self._myHasRatedInputWattage

    def hasMaximumOutputWattage (self):
        return self._myHasMaximumOutputWattage

    def hasManufacturer (self):
        return self._myHasManufacturer

    def hasRevision (self):
        return self._myHasRevision




    # setHas...() methods

    def setHasFirmwareVersion (self):
        self._myHasFirmwareVersion=True

    def setHasIndex (self):
        self._myHasIndex=True

    def setHasFruDevice (self):
        self._myHasFruDevice=True

    def setHasManufactureDate (self):
        self._myHasManufactureDate=True

    def setHasOnlineStatus (self):
        self._myHasOnlineStatus=True

    def setHasPartNumber (self):
        self._myHasPartNumber=True

    def setHasSerialNumber (self):
        self._myHasSerialNumber=True

    def setHasStatus (self):
        self._myHasStatus=True

    def setHasLocation (self):
        self._myHasLocation=True

    def setHasOnlineStatusRaw (self):
        self._myHasOnlineStatusRaw=True

    def setHasStatusRaw (self):
        self._myHasStatusRaw=True

    def setHasInputType (self):
        self._myHasInputType=True

    def setHasRatedInputWattage (self):
        self._myHasRatedInputWattage=True

    def setHasMaximumOutputWattage (self):
        self._myHasMaximumOutputWattage=True

    def setHasManufacturer (self):
        self._myHasManufacturer=True

    def setHasRevision (self):
        self._myHasRevision=True




    # isRequested...() methods

    def isFirmwareVersionRequested (self):
        return self._myFirmwareVersionRequested

    def isIndexRequested (self):
        return self._myIndexRequested

    def isFruDeviceRequested (self):
        return self._myFruDeviceRequested

    def isManufactureDateRequested (self):
        return self._myManufactureDateRequested

    def isOnlineStatusRequested (self):
        return self._myOnlineStatusRequested

    def isPartNumberRequested (self):
        return self._myPartNumberRequested

    def isSerialNumberRequested (self):
        return self._mySerialNumberRequested

    def isStatusRequested (self):
        return self._myStatusRequested

    def isLocationRequested (self):
        return self._myLocationRequested

    def isOnlineStatusRawRequested (self):
        return self._myOnlineStatusRawRequested

    def isStatusRawRequested (self):
        return self._myStatusRawRequested

    def isInputTypeRequested (self):
        return self._myInputTypeRequested

    def isRatedInputWattageRequested (self):
        return self._myRatedInputWattageRequested

    def isMaximumOutputWattageRequested (self):
        return self._myMaximumOutputWattageRequested

    def isManufacturerRequested (self):
        return self._myManufacturerRequested

    def isRevisionRequested (self):
        return self._myRevisionRequested




    # setRequested...() methods

    def setFirmwareVersionRequested (self):
        self._myFirmwareVersionRequested=True

    def setIndexRequested (self):
        self._myIndexRequested=True

    def setFruDeviceRequested (self):
        self._myFruDeviceRequested=True

    def setManufactureDateRequested (self):
        self._myManufactureDateRequested=True

    def setOnlineStatusRequested (self):
        self._myOnlineStatusRequested=True

    def setPartNumberRequested (self):
        self._myPartNumberRequested=True

    def setSerialNumberRequested (self):
        self._mySerialNumberRequested=True

    def setStatusRequested (self):
        self._myStatusRequested=True

    def setLocationRequested (self):
        self._myLocationRequested=True

    def setOnlineStatusRawRequested (self):
        self._myOnlineStatusRawRequested=True

    def setStatusRawRequested (self):
        self._myStatusRawRequested=True

    def setInputTypeRequested (self):
        self._myInputTypeRequested=True

    def setRatedInputWattageRequested (self):
        self._myRatedInputWattageRequested=True

    def setMaximumOutputWattageRequested (self):
        self._myMaximumOutputWattageRequested=True

    def setManufacturerRequested (self):
        self._myManufacturerRequested=True

    def setRevisionRequested (self):
        self._myRevisionRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myFirmwareVersionRequested:
            x = "+FirmwareVersion="
            if self._myHasFirmwareVersion:
                leafStr = str(self.firmwareVersion)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myIndexRequested:
            x = "+Index="
            if self._myHasIndex:
                leafStr = str(self.index)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFruDeviceRequested:
            x = "+FruDevice="
            if self._myHasFruDevice:
                leafStr = str(self.fruDevice)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myManufactureDateRequested:
            x = "+ManufactureDate="
            if self._myHasManufactureDate:
                leafStr = str(self.manufactureDate)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOnlineStatusRequested:
            x = "+OnlineStatus="
            if self._myHasOnlineStatus:
                leafStr = str(self.onlineStatus)
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
        if self._mySerialNumberRequested:
            x = "+SerialNumber="
            if self._myHasSerialNumber:
                leafStr = str(self.serialNumber)
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
        if self._myLocationRequested:
            x = "+Location="
            if self._myHasLocation:
                leafStr = str(self.location)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOnlineStatusRawRequested:
            x = "+OnlineStatusRaw="
            if self._myHasOnlineStatusRaw:
                leafStr = str(self.onlineStatusRaw)
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
        if self._myInputTypeRequested:
            x = "+InputType="
            if self._myHasInputType:
                leafStr = str(self.inputType)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRatedInputWattageRequested:
            x = "+RatedInputWattage="
            if self._myHasRatedInputWattage:
                leafStr = str(self.ratedInputWattage)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMaximumOutputWattageRequested:
            x = "+MaximumOutputWattage="
            if self._myHasMaximumOutputWattage:
                leafStr = str(self.maximumOutputWattage)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myManufacturerRequested:
            x = "+Manufacturer="
            if self._myHasManufacturer:
                leafStr = str(self.manufacturer)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRevisionRequested:
            x = "+Revision="
            if self._myHasRevision:
                leafStr = str(self.revision)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+FirmwareVersion="
        if self._myHasFirmwareVersion:
            leafStr = str(self.firmwareVersion)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFirmwareVersionRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Index="
        if self._myHasIndex:
            leafStr = str(self.index)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myIndexRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FruDevice="
        if self._myHasFruDevice:
            leafStr = str(self.fruDevice)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFruDeviceRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ManufactureDate="
        if self._myHasManufactureDate:
            leafStr = str(self.manufactureDate)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myManufactureDateRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OnlineStatus="
        if self._myHasOnlineStatus:
            leafStr = str(self.onlineStatus)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOnlineStatusRequested:
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
        x = "+Location="
        if self._myHasLocation:
            leafStr = str(self.location)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myLocationRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OnlineStatusRaw="
        if self._myHasOnlineStatusRaw:
            leafStr = str(self.onlineStatusRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOnlineStatusRawRequested:
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
        x = "+InputType="
        if self._myHasInputType:
            leafStr = str(self.inputType)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInputTypeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RatedInputWattage="
        if self._myHasRatedInputWattage:
            leafStr = str(self.ratedInputWattage)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRatedInputWattageRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MaximumOutputWattage="
        if self._myHasMaximumOutputWattage:
            leafStr = str(self.maximumOutputWattage)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMaximumOutputWattageRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Manufacturer="
        if self._myHasManufacturer:
            leafStr = str(self.manufacturer)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myManufacturerRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Revision="
        if self._myHasRevision:
            leafStr = str(self.revision)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRevisionRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setFirmwareVersionRequested()
        self.setIndexRequested()
        self.setFruDeviceRequested()
        self.setManufactureDateRequested()
        self.setOnlineStatusRequested()
        self.setPartNumberRequested()
        self.setSerialNumberRequested()
        self.setStatusRequested()
        self.setLocationRequested()
        self.setOnlineStatusRawRequested()
        self.setStatusRawRequested()
        self.setInputTypeRequested()
        self.setRatedInputWattageRequested()
        self.setMaximumOutputWattageRequested()
        self.setManufacturerRequested()
        self.setRevisionRequested()
        
        


    def setFirmwareVersion (self, firmwareVersion):
        self.firmwareVersion = firmwareVersion
        self.setHasFirmwareVersion()

    def setIndex (self, index):
        self.index = index
        self.setHasIndex()

    def setFruDevice (self, fruDevice):
        self.fruDevice = fruDevice
        self.setHasFruDevice()

    def setManufactureDate (self, manufactureDate):
        self.manufactureDate = manufactureDate
        self.setHasManufactureDate()

    def setOnlineStatus (self, onlineStatus):
        self.onlineStatus = onlineStatus
        self.setHasOnlineStatus()

    def setPartNumber (self, partNumber):
        self.partNumber = partNumber
        self.setHasPartNumber()

    def setSerialNumber (self, serialNumber):
        self.serialNumber = serialNumber
        self.setHasSerialNumber()

    def setStatus (self, status):
        self.status = status
        self.setHasStatus()

    def setLocation (self, location):
        self.location = location
        self.setHasLocation()

    def setOnlineStatusRaw (self, onlineStatusRaw):
        self.onlineStatusRaw = onlineStatusRaw
        self.setHasOnlineStatusRaw()

    def setStatusRaw (self, statusRaw):
        self.statusRaw = statusRaw
        self.setHasStatusRaw()

    def setInputType (self, inputType):
        self.inputType = inputType
        self.setHasInputType()

    def setRatedInputWattage (self, ratedInputWattage):
        self.ratedInputWattage = ratedInputWattage
        self.setHasRatedInputWattage()

    def setMaximumOutputWattage (self, maximumOutputWattage):
        self.maximumOutputWattage = maximumOutputWattage
        self.setHasMaximumOutputWattage()

    def setManufacturer (self, manufacturer):
        self.manufacturer = manufacturer
        self.setHasManufacturer()

    def setRevision (self, revision):
        self.revision = revision
        self.setHasRevision()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.device.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "platform", 
            "isCurrent": false
        }, 
        {
            "namespace": "power", 
            "isCurrent": false
        }, 
        {
            "namespace": "power_supply", 
            "isCurrent": false
        }, 
        {
            "namespace": "device", 
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
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_platform_power"
        ]
    }, 
    "createTime": "2013"
}
"""


