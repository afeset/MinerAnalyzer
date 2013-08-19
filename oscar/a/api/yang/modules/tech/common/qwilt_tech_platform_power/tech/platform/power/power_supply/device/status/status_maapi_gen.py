


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


from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceOnlineStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceStatusType


class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.firmwareVersionRequested = False
        self.firmwareVersion = None
        self.firmwareVersionSet = False
        
        self.indexRequested = False
        self.index = None
        self.indexSet = False
        
        self.fruDeviceRequested = False
        self.fruDevice = None
        self.fruDeviceSet = False
        
        self.manufactureDateRequested = False
        self.manufactureDate = None
        self.manufactureDateSet = False
        
        self.onlineStatusRequested = False
        self.onlineStatus = None
        self.onlineStatusSet = False
        
        self.partNumberRequested = False
        self.partNumber = None
        self.partNumberSet = False
        
        self.serialNumberRequested = False
        self.serialNumber = None
        self.serialNumberSet = False
        
        self.statusRequested = False
        self.status = None
        self.statusSet = False
        
        self.locationRequested = False
        self.location = None
        self.locationSet = False
        
        self.onlineStatusRawRequested = False
        self.onlineStatusRaw = None
        self.onlineStatusRawSet = False
        
        self.statusRawRequested = False
        self.statusRaw = None
        self.statusRawSet = False
        
        self.inputTypeRequested = False
        self.inputType = None
        self.inputTypeSet = False
        
        self.ratedInputWattageRequested = False
        self.ratedInputWattage = None
        self.ratedInputWattageSet = False
        
        self.maximumOutputWattageRequested = False
        self.maximumOutputWattage = None
        self.maximumOutputWattageSet = False
        
        self.manufacturerRequested = False
        self.manufacturer = None
        self.manufacturerSet = False
        
        self.revisionRequested = False
        self.revision = None
        self.revisionSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestFirmwareVersion(True)
        
        self.requestIndex(True)
        
        self.requestFruDevice(True)
        
        self.requestManufactureDate(True)
        
        self.requestOnlineStatus(True)
        
        self.requestPartNumber(True)
        
        self.requestSerialNumber(True)
        
        self.requestStatus(True)
        
        self.requestLocation(True)
        
        self.requestOnlineStatusRaw(True)
        
        self.requestStatusRaw(True)
        
        self.requestInputType(True)
        
        self.requestRatedInputWattage(True)
        
        self.requestMaximumOutputWattage(True)
        
        self.requestManufacturer(True)
        
        self.requestRevision(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestFirmwareVersion(False)
        
        self.requestIndex(False)
        
        self.requestFruDevice(False)
        
        self.requestManufactureDate(False)
        
        self.requestOnlineStatus(False)
        
        self.requestPartNumber(False)
        
        self.requestSerialNumber(False)
        
        self.requestStatus(False)
        
        self.requestLocation(False)
        
        self.requestOnlineStatusRaw(False)
        
        self.requestStatusRaw(False)
        
        self.requestInputType(False)
        
        self.requestRatedInputWattage(False)
        
        self.requestMaximumOutputWattage(False)
        
        self.requestManufacturer(False)
        
        self.requestRevision(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestFirmwareVersion(True)
        
        self.requestIndex(True)
        
        self.requestFruDevice(True)
        
        self.requestManufactureDate(True)
        
        self.requestOnlineStatus(True)
        
        self.requestPartNumber(True)
        
        self.requestSerialNumber(True)
        
        self.requestStatus(True)
        
        self.requestLocation(True)
        
        self.requestOnlineStatusRaw(True)
        
        self.requestStatusRaw(True)
        
        self.requestInputType(True)
        
        self.requestRatedInputWattage(True)
        
        self.requestMaximumOutputWattage(True)
        
        self.requestManufacturer(True)
        
        self.requestRevision(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestFirmwareVersion(False)
        
        self.requestIndex(False)
        
        self.requestFruDevice(False)
        
        self.requestManufactureDate(False)
        
        self.requestOnlineStatus(False)
        
        self.requestPartNumber(False)
        
        self.requestSerialNumber(False)
        
        self.requestStatus(False)
        
        self.requestLocation(False)
        
        self.requestOnlineStatusRaw(False)
        
        self.requestStatusRaw(False)
        
        self.requestInputType(False)
        
        self.requestRatedInputWattage(False)
        
        self.requestMaximumOutputWattage(False)
        
        self.requestManufacturer(False)
        
        self.requestRevision(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , powerSupply
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(powerSupply, trxContext)

    def read (self
              , powerSupply
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(powerSupply, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , powerSupply
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(powerSupply, 
                                  True,
                                  trxContext)



    def requestFirmwareVersion (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-firmwareversion').debug3Func(): logFunc('called. requested=%s', requested)
        self.firmwareVersionRequested = requested
        self.firmwareVersionSet = False

    def isFirmwareVersionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-firmwareversion-requested').debug3Func(): logFunc('called. requested=%s', self.firmwareVersionRequested)
        return self.firmwareVersionRequested

    def getFirmwareVersion (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-firmwareversion').debug3Func(): logFunc('called. self.firmwareVersionSet=%s, self.firmwareVersion=%s', self.firmwareVersionSet, self.firmwareVersion)
        if self.firmwareVersionSet:
            return self.firmwareVersion
        return None

    def hasFirmwareVersion (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-firmwareversion').debug3Func(): logFunc('called. self.firmwareVersionSet=%s, self.firmwareVersion=%s', self.firmwareVersionSet, self.firmwareVersion)
        if self.firmwareVersionSet:
            return True
        return False

    def setFirmwareVersion (self, firmwareVersion):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-firmwareversion').debug3Func(): logFunc('called. firmwareVersion=%s, old=%s', firmwareVersion, self.firmwareVersion)
        self.firmwareVersionSet = True
        self.firmwareVersion = firmwareVersion

    def requestIndex (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-index').debug3Func(): logFunc('called. requested=%s', requested)
        self.indexRequested = requested
        self.indexSet = False

    def isIndexRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-index-requested').debug3Func(): logFunc('called. requested=%s', self.indexRequested)
        return self.indexRequested

    def getIndex (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-index').debug3Func(): logFunc('called. self.indexSet=%s, self.index=%s', self.indexSet, self.index)
        if self.indexSet:
            return self.index
        return None

    def hasIndex (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-index').debug3Func(): logFunc('called. self.indexSet=%s, self.index=%s', self.indexSet, self.index)
        if self.indexSet:
            return True
        return False

    def setIndex (self, index):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-index').debug3Func(): logFunc('called. index=%s, old=%s', index, self.index)
        self.indexSet = True
        self.index = index

    def requestFruDevice (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-frudevice').debug3Func(): logFunc('called. requested=%s', requested)
        self.fruDeviceRequested = requested
        self.fruDeviceSet = False

    def isFruDeviceRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-frudevice-requested').debug3Func(): logFunc('called. requested=%s', self.fruDeviceRequested)
        return self.fruDeviceRequested

    def getFruDevice (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-frudevice').debug3Func(): logFunc('called. self.fruDeviceSet=%s, self.fruDevice=%s', self.fruDeviceSet, self.fruDevice)
        if self.fruDeviceSet:
            return self.fruDevice
        return None

    def hasFruDevice (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-frudevice').debug3Func(): logFunc('called. self.fruDeviceSet=%s, self.fruDevice=%s', self.fruDeviceSet, self.fruDevice)
        if self.fruDeviceSet:
            return True
        return False

    def setFruDevice (self, fruDevice):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-frudevice').debug3Func(): logFunc('called. fruDevice=%s, old=%s', fruDevice, self.fruDevice)
        self.fruDeviceSet = True
        self.fruDevice = fruDevice

    def requestManufactureDate (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-manufacturedate').debug3Func(): logFunc('called. requested=%s', requested)
        self.manufactureDateRequested = requested
        self.manufactureDateSet = False

    def isManufactureDateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-manufacturedate-requested').debug3Func(): logFunc('called. requested=%s', self.manufactureDateRequested)
        return self.manufactureDateRequested

    def getManufactureDate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-manufacturedate').debug3Func(): logFunc('called. self.manufactureDateSet=%s, self.manufactureDate=%s', self.manufactureDateSet, self.manufactureDate)
        if self.manufactureDateSet:
            return self.manufactureDate
        return None

    def hasManufactureDate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-manufacturedate').debug3Func(): logFunc('called. self.manufactureDateSet=%s, self.manufactureDate=%s', self.manufactureDateSet, self.manufactureDate)
        if self.manufactureDateSet:
            return True
        return False

    def setManufactureDate (self, manufactureDate):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-manufacturedate').debug3Func(): logFunc('called. manufactureDate=%s, old=%s', manufactureDate, self.manufactureDate)
        self.manufactureDateSet = True
        self.manufactureDate = manufactureDate

    def requestOnlineStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-onlinestatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.onlineStatusRequested = requested
        self.onlineStatusSet = False

    def isOnlineStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-onlinestatus-requested').debug3Func(): logFunc('called. requested=%s', self.onlineStatusRequested)
        return self.onlineStatusRequested

    def getOnlineStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-onlinestatus').debug3Func(): logFunc('called. self.onlineStatusSet=%s, self.onlineStatus=%s', self.onlineStatusSet, self.onlineStatus)
        if self.onlineStatusSet:
            return self.onlineStatus
        return None

    def hasOnlineStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-onlinestatus').debug3Func(): logFunc('called. self.onlineStatusSet=%s, self.onlineStatus=%s', self.onlineStatusSet, self.onlineStatus)
        if self.onlineStatusSet:
            return True
        return False

    def setOnlineStatus (self, onlineStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-onlinestatus').debug3Func(): logFunc('called. onlineStatus=%s, old=%s', onlineStatus, self.onlineStatus)
        self.onlineStatusSet = True
        self.onlineStatus = onlineStatus

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

    def requestLocation (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-location').debug3Func(): logFunc('called. requested=%s', requested)
        self.locationRequested = requested
        self.locationSet = False

    def isLocationRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-location-requested').debug3Func(): logFunc('called. requested=%s', self.locationRequested)
        return self.locationRequested

    def getLocation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-location').debug3Func(): logFunc('called. self.locationSet=%s, self.location=%s', self.locationSet, self.location)
        if self.locationSet:
            return self.location
        return None

    def hasLocation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-location').debug3Func(): logFunc('called. self.locationSet=%s, self.location=%s', self.locationSet, self.location)
        if self.locationSet:
            return True
        return False

    def setLocation (self, location):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-location').debug3Func(): logFunc('called. location=%s, old=%s', location, self.location)
        self.locationSet = True
        self.location = location

    def requestOnlineStatusRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-onlinestatusraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.onlineStatusRawRequested = requested
        self.onlineStatusRawSet = False

    def isOnlineStatusRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-onlinestatusraw-requested').debug3Func(): logFunc('called. requested=%s', self.onlineStatusRawRequested)
        return self.onlineStatusRawRequested

    def getOnlineStatusRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-onlinestatusraw').debug3Func(): logFunc('called. self.onlineStatusRawSet=%s, self.onlineStatusRaw=%s', self.onlineStatusRawSet, self.onlineStatusRaw)
        if self.onlineStatusRawSet:
            return self.onlineStatusRaw
        return None

    def hasOnlineStatusRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-onlinestatusraw').debug3Func(): logFunc('called. self.onlineStatusRawSet=%s, self.onlineStatusRaw=%s', self.onlineStatusRawSet, self.onlineStatusRaw)
        if self.onlineStatusRawSet:
            return True
        return False

    def setOnlineStatusRaw (self, onlineStatusRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-onlinestatusraw').debug3Func(): logFunc('called. onlineStatusRaw=%s, old=%s', onlineStatusRaw, self.onlineStatusRaw)
        self.onlineStatusRawSet = True
        self.onlineStatusRaw = onlineStatusRaw

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

    def requestInputType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inputtype').debug3Func(): logFunc('called. requested=%s', requested)
        self.inputTypeRequested = requested
        self.inputTypeSet = False

    def isInputTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inputtype-requested').debug3Func(): logFunc('called. requested=%s', self.inputTypeRequested)
        return self.inputTypeRequested

    def getInputType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inputtype').debug3Func(): logFunc('called. self.inputTypeSet=%s, self.inputType=%s', self.inputTypeSet, self.inputType)
        if self.inputTypeSet:
            return self.inputType
        return None

    def hasInputType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inputtype').debug3Func(): logFunc('called. self.inputTypeSet=%s, self.inputType=%s', self.inputTypeSet, self.inputType)
        if self.inputTypeSet:
            return True
        return False

    def setInputType (self, inputType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inputtype').debug3Func(): logFunc('called. inputType=%s, old=%s', inputType, self.inputType)
        self.inputTypeSet = True
        self.inputType = inputType

    def requestRatedInputWattage (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-ratedinputwattage').debug3Func(): logFunc('called. requested=%s', requested)
        self.ratedInputWattageRequested = requested
        self.ratedInputWattageSet = False

    def isRatedInputWattageRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-ratedinputwattage-requested').debug3Func(): logFunc('called. requested=%s', self.ratedInputWattageRequested)
        return self.ratedInputWattageRequested

    def getRatedInputWattage (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ratedinputwattage').debug3Func(): logFunc('called. self.ratedInputWattageSet=%s, self.ratedInputWattage=%s', self.ratedInputWattageSet, self.ratedInputWattage)
        if self.ratedInputWattageSet:
            return self.ratedInputWattage
        return None

    def hasRatedInputWattage (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ratedinputwattage').debug3Func(): logFunc('called. self.ratedInputWattageSet=%s, self.ratedInputWattage=%s', self.ratedInputWattageSet, self.ratedInputWattage)
        if self.ratedInputWattageSet:
            return True
        return False

    def setRatedInputWattage (self, ratedInputWattage):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ratedinputwattage').debug3Func(): logFunc('called. ratedInputWattage=%s, old=%s', ratedInputWattage, self.ratedInputWattage)
        self.ratedInputWattageSet = True
        self.ratedInputWattage = ratedInputWattage

    def requestMaximumOutputWattage (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maximumoutputwattage').debug3Func(): logFunc('called. requested=%s', requested)
        self.maximumOutputWattageRequested = requested
        self.maximumOutputWattageSet = False

    def isMaximumOutputWattageRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maximumoutputwattage-requested').debug3Func(): logFunc('called. requested=%s', self.maximumOutputWattageRequested)
        return self.maximumOutputWattageRequested

    def getMaximumOutputWattage (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maximumoutputwattage').debug3Func(): logFunc('called. self.maximumOutputWattageSet=%s, self.maximumOutputWattage=%s', self.maximumOutputWattageSet, self.maximumOutputWattage)
        if self.maximumOutputWattageSet:
            return self.maximumOutputWattage
        return None

    def hasMaximumOutputWattage (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maximumoutputwattage').debug3Func(): logFunc('called. self.maximumOutputWattageSet=%s, self.maximumOutputWattage=%s', self.maximumOutputWattageSet, self.maximumOutputWattage)
        if self.maximumOutputWattageSet:
            return True
        return False

    def setMaximumOutputWattage (self, maximumOutputWattage):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maximumoutputwattage').debug3Func(): logFunc('called. maximumOutputWattage=%s, old=%s', maximumOutputWattage, self.maximumOutputWattage)
        self.maximumOutputWattageSet = True
        self.maximumOutputWattage = maximumOutputWattage

    def requestManufacturer (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-manufacturer').debug3Func(): logFunc('called. requested=%s', requested)
        self.manufacturerRequested = requested
        self.manufacturerSet = False

    def isManufacturerRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-manufacturer-requested').debug3Func(): logFunc('called. requested=%s', self.manufacturerRequested)
        return self.manufacturerRequested

    def getManufacturer (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-manufacturer').debug3Func(): logFunc('called. self.manufacturerSet=%s, self.manufacturer=%s', self.manufacturerSet, self.manufacturer)
        if self.manufacturerSet:
            return self.manufacturer
        return None

    def hasManufacturer (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-manufacturer').debug3Func(): logFunc('called. self.manufacturerSet=%s, self.manufacturer=%s', self.manufacturerSet, self.manufacturer)
        if self.manufacturerSet:
            return True
        return False

    def setManufacturer (self, manufacturer):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-manufacturer').debug3Func(): logFunc('called. manufacturer=%s, old=%s', manufacturer, self.manufacturer)
        self.manufacturerSet = True
        self.manufacturer = manufacturer

    def requestRevision (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-revision').debug3Func(): logFunc('called. requested=%s', requested)
        self.revisionRequested = requested
        self.revisionSet = False

    def isRevisionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-revision-requested').debug3Func(): logFunc('called. requested=%s', self.revisionRequested)
        return self.revisionRequested

    def getRevision (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-revision').debug3Func(): logFunc('called. self.revisionSet=%s, self.revision=%s', self.revisionSet, self.revision)
        if self.revisionSet:
            return self.revision
        return None

    def hasRevision (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-revision').debug3Func(): logFunc('called. self.revisionSet=%s, self.revision=%s', self.revisionSet, self.revision)
        if self.revisionSet:
            return True
        return False

    def setRevision (self, revision):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-revision').debug3Func(): logFunc('called. revision=%s, old=%s', revision, self.revision)
        self.revisionSet = True
        self.revision = revision


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.firmwareVersion = 0
        self.firmwareVersionSet = False
        
        self.index = 0
        self.indexSet = False
        
        self.fruDevice = 0
        self.fruDeviceSet = False
        
        self.manufactureDate = 0
        self.manufactureDateSet = False
        
        self.onlineStatus = 0
        self.onlineStatusSet = False
        
        self.partNumber = 0
        self.partNumberSet = False
        
        self.serialNumber = 0
        self.serialNumberSet = False
        
        self.status = 0
        self.statusSet = False
        
        self.location = 0
        self.locationSet = False
        
        self.onlineStatusRaw = 0
        self.onlineStatusRawSet = False
        
        self.statusRaw = 0
        self.statusRawSet = False
        
        self.inputType = 0
        self.inputTypeSet = False
        
        self.ratedInputWattage = 0
        self.ratedInputWattageSet = False
        
        self.maximumOutputWattage = 0
        self.maximumOutputWattageSet = False
        
        self.manufacturer = 0
        self.manufacturerSet = False
        
        self.revision = 0
        self.revisionSet = False
        

    def _getSelfKeyPath (self, powerSupply
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(powerSupply);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("power-supply", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("power", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("platform", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", "qt-pltf"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        powerSupply, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(powerSupply, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(powerSupply, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       powerSupply, 
                       
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

        keyPath = self._getSelfKeyPath(powerSupply, 
                                       
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
                               powerSupply, 
                               
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

        
        if self.isFirmwareVersionRequested():
            valFirmwareVersion = Value()
            valFirmwareVersion.setEmpty()
            tagValueList.push(("firmware-version", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valFirmwareVersion)
        
        if self.isIndexRequested():
            valIndex = Value()
            valIndex.setEmpty()
            tagValueList.push(("index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valIndex)
        
        if self.isFruDeviceRequested():
            valFruDevice = Value()
            valFruDevice.setEmpty()
            tagValueList.push(("fru-device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valFruDevice)
        
        if self.isManufactureDateRequested():
            valManufactureDate = Value()
            valManufactureDate.setEmpty()
            tagValueList.push(("manufacture-date", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valManufactureDate)
        
        if self.isOnlineStatusRequested():
            valOnlineStatus = Value()
            valOnlineStatus.setEmpty()
            tagValueList.push(("online-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valOnlineStatus)
        
        if self.isPartNumberRequested():
            valPartNumber = Value()
            valPartNumber.setEmpty()
            tagValueList.push(("part-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valPartNumber)
        
        if self.isSerialNumberRequested():
            valSerialNumber = Value()
            valSerialNumber.setEmpty()
            tagValueList.push(("serial-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valSerialNumber)
        
        if self.isStatusRequested():
            valStatus = Value()
            valStatus.setEmpty()
            tagValueList.push(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valStatus)
        
        if self.isLocationRequested():
            valLocation = Value()
            valLocation.setEmpty()
            tagValueList.push(("location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valLocation)
        
        if self.isOnlineStatusRawRequested():
            valOnlineStatusRaw = Value()
            valOnlineStatusRaw.setEmpty()
            tagValueList.push(("online-status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valOnlineStatusRaw)
        
        if self.isStatusRawRequested():
            valStatusRaw = Value()
            valStatusRaw.setEmpty()
            tagValueList.push(("status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valStatusRaw)
        
        if self.isInputTypeRequested():
            valInputType = Value()
            valInputType.setEmpty()
            tagValueList.push(("input-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valInputType)
        
        if self.isRatedInputWattageRequested():
            valRatedInputWattage = Value()
            valRatedInputWattage.setEmpty()
            tagValueList.push(("rated-input-wattage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valRatedInputWattage)
        
        if self.isMaximumOutputWattageRequested():
            valMaximumOutputWattage = Value()
            valMaximumOutputWattage.setEmpty()
            tagValueList.push(("maximum-output-wattage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valMaximumOutputWattage)
        
        if self.isManufacturerRequested():
            valManufacturer = Value()
            valManufacturer.setEmpty()
            tagValueList.push(("manufacturer", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valManufacturer)
        
        if self.isRevisionRequested():
            valRevision = Value()
            valRevision.setEmpty()
            tagValueList.push(("revision", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valRevision)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isFirmwareVersionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "firmware-version") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-firmwareversion').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "firmwareVersion", "firmware-version", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-firmware-version-bad-value').infoFunc(): logFunc('firmwareVersion not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFirmwareVersion(tempVar)
            for logFunc in self._log('read-tag-values-firmware-version').debug3Func(): logFunc('read firmwareVersion. firmwareVersion=%s, tempValue=%s', self.firmwareVersion, tempValue.getType())
        
        if self.isIndexRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "index") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-index').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "index", "index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-index-bad-value').infoFunc(): logFunc('index not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setIndex(tempVar)
            for logFunc in self._log('read-tag-values-index').debug3Func(): logFunc('read index. index=%s, tempValue=%s', self.index, tempValue.getType())
        
        if self.isFruDeviceRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "fru-device") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-frudevice').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fruDevice", "fru-device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-fru-device-bad-value').infoFunc(): logFunc('fruDevice not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFruDevice(tempVar)
            for logFunc in self._log('read-tag-values-fru-device').debug3Func(): logFunc('read fruDevice. fruDevice=%s, tempValue=%s', self.fruDevice, tempValue.getType())
        
        if self.isManufactureDateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "manufacture-date") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-manufacturedate').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "manufactureDate", "manufacture-date", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-manufacture-date-bad-value').infoFunc(): logFunc('manufactureDate not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setManufactureDate(tempVar)
            for logFunc in self._log('read-tag-values-manufacture-date').debug3Func(): logFunc('read manufactureDate. manufactureDate=%s, tempValue=%s', self.manufactureDate, tempValue.getType())
        
        if self.isOnlineStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "online-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-onlinestatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "onlineStatus", "online-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-online-status-bad-value').infoFunc(): logFunc('onlineStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOnlineStatus(tempVar)
            for logFunc in self._log('read-tag-values-online-status').debug3Func(): logFunc('read onlineStatus. onlineStatus=%s, tempValue=%s', self.onlineStatus, tempValue.getType())
        
        if self.isPartNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "part-number") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-partnumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "partNumber", "part-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
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
        
        if self.isSerialNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "serial-number") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-serialnumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "serialNumber", "serial-number", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
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
        
        if self.isStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-status').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "status", "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
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
        
        if self.isLocationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "location") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-location').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "location", "location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-location-bad-value').infoFunc(): logFunc('location not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLocation(tempVar)
            for logFunc in self._log('read-tag-values-location').debug3Func(): logFunc('read location. location=%s, tempValue=%s', self.location, tempValue.getType())
        
        if self.isOnlineStatusRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "online-status-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-onlinestatusraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "onlineStatusRaw", "online-status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-online-status-raw-bad-value').infoFunc(): logFunc('onlineStatusRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOnlineStatusRaw(tempVar)
            for logFunc in self._log('read-tag-values-online-status-raw').debug3Func(): logFunc('read onlineStatusRaw. onlineStatusRaw=%s, tempValue=%s', self.onlineStatusRaw, tempValue.getType())
        
        if self.isStatusRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "status-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-statusraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "statusRaw", "status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
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
        
        if self.isInputTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "input-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inputtype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inputType", "input-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-input-type-bad-value').infoFunc(): logFunc('inputType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInputType(tempVar)
            for logFunc in self._log('read-tag-values-input-type').debug3Func(): logFunc('read inputType. inputType=%s, tempValue=%s', self.inputType, tempValue.getType())
        
        if self.isRatedInputWattageRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rated-input-wattage") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-ratedinputwattage').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "ratedInputWattage", "rated-input-wattage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rated-input-wattage-bad-value').infoFunc(): logFunc('ratedInputWattage not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRatedInputWattage(tempVar)
            for logFunc in self._log('read-tag-values-rated-input-wattage').debug3Func(): logFunc('read ratedInputWattage. ratedInputWattage=%s, tempValue=%s', self.ratedInputWattage, tempValue.getType())
        
        if self.isMaximumOutputWattageRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "maximum-output-wattage") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maximumoutputwattage').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maximumOutputWattage", "maximum-output-wattage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-maximum-output-wattage-bad-value').infoFunc(): logFunc('maximumOutputWattage not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaximumOutputWattage(tempVar)
            for logFunc in self._log('read-tag-values-maximum-output-wattage').debug3Func(): logFunc('read maximumOutputWattage. maximumOutputWattage=%s, tempValue=%s', self.maximumOutputWattage, tempValue.getType())
        
        if self.isManufacturerRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "manufacturer") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-manufacturer').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "manufacturer", "manufacturer", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-manufacturer-bad-value').infoFunc(): logFunc('manufacturer not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setManufacturer(tempVar)
            for logFunc in self._log('read-tag-values-manufacturer').debug3Func(): logFunc('read manufacturer. manufacturer=%s, tempValue=%s', self.manufacturer, tempValue.getType())
        
        if self.isRevisionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "revision") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-revision').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "revision", "revision", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-revision-bad-value').infoFunc(): logFunc('revision not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRevision(tempVar)
            for logFunc in self._log('read-tag-values-revision').debug3Func(): logFunc('read revision. revision=%s, tempValue=%s', self.revision, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.device.status.status_maapi_gen import StatusMaapi", 
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
            "moduleYangNamespacePrefix": "qt-pltf", 
            "yangName": "platform", 
            "namespace": "platform", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", 
            "name": "platform"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "yangName": "power", 
            "namespace": "power", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "power"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "isCurrent": false, 
            "yangName": "power-supply", 
            "namespace": "power_supply", 
            "isList": true, 
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
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "device"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "firmwareVersion", 
            "yangName": "firmware-version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "index", 
            "yangName": "index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "fruDevice", 
            "yangName": "fru-device", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureDate", 
            "yangName": "manufacture-date", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "onlineStatus", 
            "yangName": "online-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "partNumber", 
            "yangName": "part-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "serialNumber", 
            "yangName": "serial-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "onlineStatusRaw", 
            "yangName": "online-status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "inputType", 
            "yangName": "input-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "ratedInputWattage", 
            "yangName": "rated-input-wattage", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumOutputWattage", 
            "yangName": "maximum-output-wattage", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufacturer", 
            "yangName": "manufacturer", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
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
    "configLeaves": [], 
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
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "firmwareVersion", 
            "yangName": "firmware-version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "index", 
            "yangName": "index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "fruDevice", 
            "yangName": "fru-device", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufactureDate", 
            "yangName": "manufacture-date", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "onlineStatus", 
            "yangName": "online-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "partNumber", 
            "yangName": "part-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "serialNumber", 
            "yangName": "serial-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "onlineStatusRaw", 
            "yangName": "online-status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "inputType", 
            "yangName": "input-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "ratedInputWattage", 
            "yangName": "rated-input-wattage", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumOutputWattage", 
            "yangName": "maximum-output-wattage", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "manufacturer", 
            "yangName": "manufacturer", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "revision", 
            "yangName": "revision", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


