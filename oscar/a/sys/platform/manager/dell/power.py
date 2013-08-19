# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 
import re

# PowerSupplies Enums
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerRedundancyStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerNoRedundancyReasonType

from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceOnlineStatusType

from a.infra.basic.return_codes import ReturnCodes
import a.sys.platform.manager.power

#-----------------------------------------------------------------------------#
class PowerSuppliesSubsystem(a.sys.platform.manager.power.PowerSuppliesSubsystem):        
    def __init__ (self, logger):
        a.sys.platform.manager.power.PowerSuppliesSubsystem.__init__(self, logger)
        self._powerSuppliesReporter = None
        self._fruReporter = None

    def initPowerSuppliesReporter (self, powerSuppliesReporter):
        """ Inits the PowerSource instance for this to get updated information from.
        """
        self._log("init-power-supply-reporter").debug1("power-supply-reporter initialized to %s", powerSuppliesReporter)
        self._powerSuppliesReporter = powerSuppliesReporter

    def initFruReporter (self, fruReporter):
        """ Inits the FruSource instance for this to get updated information from.
        """
        self._log("init-fru-reporter").debug1("fru-reporter initialized to %s", fruReporter)
        self._fruReporter = fruReporter


    def _createManagedUnit (self, name):
        """ To be implemented in platform-specific extension class """
        powerSupply = PowerSupplyUnit(self._log, name)
        powerSupply.initPowerSuppliesReporter(self._powerSuppliesReporter)
        powerSupply.initFruReporter(self._fruReporter)
        return powerSupply


    ################## LOGIC ###################

    def update (self):
        """ update the status with data from the reporter
        When no data is available (for any reason - reporter doesn't work, or returns None data), the updates status/alarm fields are left unset, and
        receive default values (which are usually "unknown") when gotten by blinky-oper.
        """
        updatedPowerStatus = self.newStatus()

        if self._powerSuppliesReporter is None:
            self._log("update-data-no-power-supplis-reporter").error("can't update data, no power-supplies-reporter has been initialized yet")
        else:
            powerSuppliesInformation = self._powerSuppliesReporter.getData()        
            if powerSuppliesInformation is not None:
                self._updatePowerSuppliesStatus(updatedPowerStatus, powerSuppliesInformation)            
            else:
                self._log("update").warning("did not get power supplies information from the power-supplies-omreporer (got None instead)")

        self._updateData(updatedPowerStatus)                        
        return (ReturnCodes.kOk, None)


    def _updatePowerSuppliesStatus (self, updatedPowerSuppliesStatus, powerSuppliesInformation):
        powerSuppliesStatus = powerSuppliesInformation.powerStatus

        if powerSuppliesStatus is None:
            self._log("update-power-supplies-status-no-status").debug1("no status to update, powerSuppliesStatus is None")
            return
        
        if powerSuppliesStatus.hasRedundancyStatusRaw():
            updatedPowerSuppliesStatus.setRedundancyStatusRaw(powerSuppliesStatus.redundancyStatusRaw)
            try:
                if powerSuppliesInformation.subsystemStatusRaw is not None:
                    updatedPowerSuppliesStatus.setRedundancyStatus(self._subsystemStatusRawToEnum(powerSuppliesInformation.subsystemStatusRaw))
                else:
                    updatedPowerSuppliesStatus.setRedundancyStatus(self._redundancyStatusRawToEnum(powerSuppliesStatus.redundancyStatusRaw))
            except:
                self._log("update-power-supplies-status-unrecognized-redundancy-status").debug1("cannot parse redundancy-status-raw=%s", powerSuppliesStatus.redundancyStatusRaw)
                

    def _redundancyStatusRawToEnum (self, redundancyStatusRaw):
        """ Converts the raw-status into an enum, or raises KeyError if cannot convert """
        return {"Full"      : PowerRedundancyStatusType.kFull,
                "Lost"      : PowerRedundancyStatusType.kLost,
                "Unknown"   : PowerRedundancyStatusType.kUnknown}[redundancyStatusRaw]


    def _subsystemStatusRawToEnum (self, redundancyStatusRaw):
        """ Converts the raw-status into an enum, or raises KeyError if cannot convert """
        return {"Ok"       : PowerRedundancyStatusType.kFull,
                "Critical" : PowerRedundancyStatusType.kLost,
                "Unknown"  : PowerRedundancyStatusType.kUnknown}[redundancyStatusRaw]

#-----------------------------------------------------------------------------#

class PowerSupplyUnit(a.sys.platform.manager.power.PowerSupplyUnit):
    """
    Gets the information Omreporters (PowerSource & FRU).
    """

    def __init__ (self, logger, instanceName):
        a.sys.platform.manager.power.PowerSupplyUnit.__init__(self, logger, instanceName)
        self._powerSuppliesReporter = None
        self._fruReporter           = None

    def initPowerSuppliesReporter (self, powerSuppliesReporter):
        """ Inits the PowerSource instance for this to get updated information from.
        """
        self._log("init-power-supply-reporter").debug1("power-supply-reporter initialized to %s", powerSuppliesReporter)
        self._powerSuppliesReporter = powerSuppliesReporter

    def initFruReporter (self, fruReporter):
        """ Inits the FruSource instance for this to get updated information from.
        """
        self._log("init-fru-reporter").debug1("fru-reporter initialized to %s", fruReporter)
        self._fruReporter = fruReporter
      
        
    ################## LOGIC ###################
          
    def update (self):
        """ update the status with data from the reporter
        When no data is available (for any reason - reporter doesn't work, or returns None data), the updates status/alarm fields are left unset, and
        receive default values (which are usually "unknown") when gotten by blinky-oper.
        """
        self._log("update").debug1("updating power-supply status from omreports")
        updatedDeviceStatus = a.sys.platform.manager.power.PowerSupplyUnit.newDeviceStatus()

        if self._powerSuppliesReporter is None:
            self._log("update-data-no-power-supplis-reporter").error("can't update data, no power-supplies-reporter has been initialized yet")
        else:
            powerSuppliesInformation = self._powerSuppliesReporter.getData()
            if powerSuppliesInformation is not None:
                self._updatePowerSupplyStatus(updatedDeviceStatus, self._getRelevantPowerSupplyStatus(powerSuppliesInformation.powerSupplyDeviceStatusList))
            else:
                self._log("update-data").warning("did not get power supplies information from the power-supplies-omreporer (got None instead)")

        if self._fruReporter is None:
            self._log("update-data-no-fru-reporter").error("can't update data, no fru-reporter has been initialized yet")
        else:
            deviceInformationList = self._fruReporter.getData()
            if deviceInformationList is not None:
                self._updateDeviceInformation(updatedDeviceStatus, self._getRelevantDeviceInformation(deviceInformationList))
            else:
                self._log("update-data").warning("did not get power supplies information from the fru-omreporer (got None instead)")
            
        self._updateData(updatedDeviceStatus)
        return (ReturnCodes.kOk, None)


    def _getRelevantDeviceInformation (self, deviceInformationList):
        myFruId = self._getFruId()
        if myFruId is None:
            self._log("get-relevant-device-information-no-fru-id").error("the fru-id of this power-supply was not configured, cannot get relevant fru data")
            return None

        for deviceInformation in deviceInformationList:
            if deviceInformation.fruDevice == myFruId:
                return deviceInformation

        self._log("get-relevant-device-information-not-found").debug1("a device with this power-supply's fru-id=%s was not found", myFruId)
        return None


    def _getRelevantPowerSupplyStatus (self, powerSupplyDeviceStatusList):
        myId = self._getId()
        if myId is None:
            self._log("get-relevant-device-information-no-id").error("the id (location) of this power-supply was not configured, cannot get relevant power-supply data")
            return None

        for deviceStatus in powerSupplyDeviceStatusList:
            if deviceStatus.hasLocation() and deviceStatus.location == myId:
                return deviceStatus

        self._log("get-relevant-device-information-not-found").debug1("a device with this power-supply's id=%s was not found", myId)
        return None


    def _updateDeviceInformation (self, updatedDeviceStatus, deviceInformation):    
        if deviceInformation is not None:
            if deviceInformation.fruDevice is not None:
                updatedDeviceStatus.setFruDevice(deviceInformation.fruDevice)
            if deviceInformation.serialNumber is not None:
                updatedDeviceStatus.setSerialNumber(deviceInformation.serialNumber)
            if deviceInformation.partNumber is not None:
                updatedDeviceStatus.setPartNumber(deviceInformation.partNumber)
            if deviceInformation.manufacturer is not None:
                updatedDeviceStatus.setManufacturer(deviceInformation.manufacturer)
            if deviceInformation.manufactureDate is not None:
                updatedDeviceStatus.setManufactureDate(deviceInformation.manufactureDate)
            if deviceInformation.revision is not None:
                updatedDeviceStatus.setRevision(deviceInformation.revision)


    def _updatePowerSupplyStatus (self, updatedDeviceStatus, deviceStatus):
        if deviceStatus is not None:   
            updatedDeviceStatus.copySetFrom(deviceStatus)         
            if deviceStatus.hasStatusRaw():
                try:
                    updatedDeviceStatus.setStatus(self._deviceStatusRawToEnum(deviceStatus.statusRaw))
                except:
                    self._log("update-power-supply-status-unrecognized-status").debug1("cannot parse status-raw=%s", deviceStatus.statusRaw)

            if deviceStatus.hasOnlineStatusRaw():
                try:                
                    updatedDeviceStatus.setOnlineStatus(self._deviceOnlineStatusRawToEnum(deviceStatus.onlineStatusRaw))
                except:
                    self._log("update-power-supply-status-unrecognized-online-status").debug1("cannot parse online-status-raw=%s", deviceStatus.onlineStatusRaw)

        else:
            updatedDeviceStatus.setStatus(PowerSupplyDeviceStatusType.kAbsent)


    def _deviceStatusRawToEnum (self, statusRaw):
        return {"Ok"        : PowerSupplyDeviceStatusType.kOk,
                "Critical"  : PowerSupplyDeviceStatusType.kCritical,
                "Unknown"   : PowerSupplyDeviceStatusType.kUnknown}[statusRaw]
        

    def _deviceOnlineStatusRawToEnum (self, onlineStatusRaw):
        try:
            return {"Presence Detected" : PowerSupplyDeviceOnlineStatusType.kPresenceDetected,
                    "Not Available"     : PowerSupplyDeviceOnlineStatusType.kNotAvailable}[onlineStatusRaw]                    
        except Exception as exc:                        
            if re.search("^.*Detected.*Lost.*$", onlineStatusRaw) is not None: # this means the input is lost
                return PowerSupplyDeviceOnlineStatusType.kPowerSourceLost                    
            raise exc
