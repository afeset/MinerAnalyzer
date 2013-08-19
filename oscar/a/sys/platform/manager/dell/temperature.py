# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 

import re

# Temperature Enums
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureStatusType

from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureAlarmReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorDeviceStatusType

from a.infra.basic.return_codes import ReturnCodes
import a.sys.platform.manager.temperature

#-----------------------------------------------------------------------------#
class TemperatureSubsystem(a.sys.platform.manager.temperature.TemperatureSubsystem):        
    def __init__ (self, logger):
        a.sys.platform.manager.temperature.TemperatureSubsystem.__init__(self, logger)
        self._temperatureReporter  = None

    def initTemperatureReporter (self, temperatureReporter):
        """ Inits the TemperatureSource instance for this to get updated information from.
        """
        self._log("init-temperature-reporter").debug1("temperature-reporter initialized to %s", temperatureReporter)
        self._temperatureReporter = temperatureReporter


    def _createManagedUnit (self, name):
        """ To be implemented in platform-specific extension class """
        sensor = SensorUnit(self._log, name)
        sensor.initTemperatureReporter(self._temperatureReporter)
        return sensor

    ################## LOGIC ###################

    def update (self):
        updatedTemperatureStatus = a.sys.platform.manager.temperature.TemperatureSubsystem.newStatus()    

        if self._temperatureReporter is None:
            self._log("update-data-no-temperature-reporter").error("can't update data, no sensor has been initialized yet")
        else:
            temperatureInformation = self._temperatureReporter.getData()    
            if temperatureInformation is not None:            
                self._updateTemperatureStatus(updatedTemperatureStatus, temperatureInformation.temperatureStatus)                
            else:
                self._log("update-data").warning("did not get temperature information from the temperature-omreporer (got None instead)")

        self._updateData(updatedTemperatureStatus)
        return (ReturnCodes.kOk, None)


    def _updateTemperatureStatus (self, updatedTemperatureStatus, temperatureStatus):
        if temperatureStatus is None:            
            return

        if temperatureStatus.hasTemperatureStatusRaw():
            updatedTemperatureStatus.setTemperatureStatusRaw(temperatureStatus.temperatureStatusRaw)
            try:
                updatedTemperatureStatus.setTemperatureStatus(self._temperatureStatusRawToEnum(temperatureStatus.temperatureStatusRaw))
            except:
                self._log("update-temperature-status-status-unrecognized").debug1("cannot parse raw-status=%s", temperatureStatus.temperatureStatusRaw)


    def _temperatureStatusRawToEnum (self, temperatureStatusRaw):        
        return {"Ok"           : TemperatureStatusType.kOk,
                "Non-Critical" : TemperatureStatusType.kNonCritical,
                "Critical"     : TemperatureStatusType.kCritical,
                "Unknown"      : TemperatureStatusType.kUnknown}[temperatureStatusRaw]



#-----------------------------------------------------------------------------#
class SensorUnit(a.sys.platform.manager.temperature.SensorUnit):
    """
    Gets the information Omreporters (TemperatureSource).
    """

    def __init__ (self, logger, instanceName):
        a.sys.platform.manager.temperature.SensorUnit.__init__(self, logger, instanceName)
        self._temperatureReporter           = None

    def initTemperatureReporter (self, temperatureReporter):
        """ Inits the TemperatureSource instance for this to get updated information from.
        """
        self._log("init-temperature-reporter").debug1("temperature-reporter initialized to %s", temperatureReporter)
        self._temperatureReporter = temperatureReporter

    def update (self):
        updatedDeviceStatus = a.sys.platform.manager.temperature.SensorUnit.newDeviceStatus()
        sensorData = self._emptySensorData(updatedDeviceStatus)

        if self._temperatureReporter is None:
            self._log("update-data-no-temperature-reporter").error("can't update data, no sensor has been initialized yet")
        else:
            temperatureInformation = self._temperatureReporter.getData()
            if temperatureInformation is not None:
                self._updateSensorStatus(updatedDeviceStatus, self._getRelevantSensorStatus(temperatureInformation.sensorDeviceStatusList))
                self._updateSensorData(sensorData, updatedDeviceStatus)
            else:
                self._log("update-data").warning("did not get temperature information from the temperature-omreporer (got None instead)")

        self._updateData(sensorData)
        return (ReturnCodes.kOk, None)


    def _getRelevantSensorStatus (self, sensorDeviceStatusList):
        myId = self._getId()
        if myId is None:
            self._log("get-relevant-device-information-no-id").error("the id (location) of this sensor was not configured, cannot get relevant power-supply data")
            return None

        for deviceStatus in sensorDeviceStatusList:
            if deviceStatus.hasProbeName() and deviceStatus.probeName == myId:
                return deviceStatus

        self._log("get-relevant-device-information-not-found").debug1("a device with this sensor's id=%s was not found", myId)
        return None

    def _updateSensorStatus (self, updatedDeviceStatus, deviceStatus):
        if deviceStatus is None:            
            updatedDeviceStatus.setStatus(SensorDeviceStatusType.kNone)
            return
        
        updatedDeviceStatus.copySetFrom(deviceStatus)
        if deviceStatus.hasStatusRaw():
            try:
                updatedDeviceStatus.setStatus(self._deviceStatusRawToEnum(deviceStatus.statusRaw))
            except:
                self._log("update-sensor-status").debug1("could not parse raw-status=%s", deviceStatus.statusRaw)

    def _emptySensorData (self, updatedDeviceStatus):
        return a.sys.platform.manager.temperature.SensorData(updatedDeviceStatus, 0,0,0,0,0)


    def _updateSensorData (self, sensorData, deviceStatus):
        if deviceStatus.hasTemperatureRaw():
            sensorData.temperature = self._temperatureStringToInteger(deviceStatus.temperatureRaw)
        if deviceStatus.hasMinimumWarningRaw():
            sensorData.minimumWarning = self._temperatureStringToInteger(deviceStatus.minimumWarningRaw)
        if deviceStatus.hasMinimumCriticalRaw():
            sensorData.minimumCritical = self._temperatureStringToInteger(deviceStatus.minimumCriticalRaw)
        if deviceStatus.hasMaximumWarningRaw():
            sensorData.maximumWarning  = self._temperatureStringToInteger(deviceStatus.maximumWarningRaw)
        if deviceStatus.hasMaximumCriticalRaw():
            sensorData.maximumCritical = self._temperatureStringToInteger(deviceStatus.maximumCriticalRaw)


    def _temperatureStringToInteger (self, tempString):
        matches = re.match("^\s*(?P<number>-?\d*(\.\d*)?)\s*C$", tempString)
        if matches is not None:
            matchDict = matches.groupdict()
            if 'number' in matchDict:
                numberString = matchDict['number']
                try:
                    number = int(round(float(numberString)))
                    self._log("temperature-string-to-integer").debug3("parsed temperature string %s to number %s", tempString, number)
                    return number
                except:
                    pass

        number = 0
        self._log("temperature-string-to-integer").debug3("failed parsing temperature string %s to number. returning %s", tempString, number)
        return number


    def _deviceStatusRawToEnum (self, statusRaw):
        return {"Ok"            : SensorDeviceStatusType.kOk,
                "Critical"      : SensorDeviceStatusType.kCritical,
                "Non-Critical"  : SensorDeviceStatusType.kNonCritical,
                "Unknown"       : SensorDeviceStatusType.kUnknown}[statusRaw]
        

