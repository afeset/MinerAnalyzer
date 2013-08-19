
#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

import a.api.alarms.alarm.platform

import a.sys.blinky.maapi_domain # this is a patch because of bug in MAAPI import, when naamas fixes - remove it
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType

# power subsystem blinky maapi
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.alarm.alarm_maapi_gen
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.power_supply_maapi_list_gen import BlinkyPowerSupplyMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.power_supply_maapi_gen import BlinkyPowerSupplyMaapi

# fan subsystem blinky maapi
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.alarm.alarm_maapi_gen
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.fan_maapi_list_gen import BlinkyFanMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.fan_maapi_gen import BlinkyFanMaapi

# temperature subsystem blinky maapi
import a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.alarm.alarm_maapi_gen
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.sensor_maapi_list_gen import BlinkySensorMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.sensor_maapi_gen import BlinkySensorMaapi



from a.sys.mng.alarm.sources.source_base import AlarmSourceBase
from a.sys.mng.alarm.sources.source_base import AlarmSourceError
from a.sys.mng.alarm.sources.source_base import MaapiObject
from a.sys.mng.alarm.sources.source_base import StaticMaapiList

class PlatformSource(AlarmSourceBase):

    ALARM_SOURCE_INSTACE_NAME = a.api.alarms.alarm.platform.PLATFORM_ALARM_SOURCE_NAME
            

    def __init__ (self, logger):
        AlarmSourceBase.__init__(self, logger, PlatformSource.ALARM_SOURCE_INSTACE_NAME)

        self.powerSuppliesAlarmObject = PowerSuppliesAlarmMaapiObject(logger, self)
        self.fansAlarmObject          = FansMaapiAlarmObject(logger, self)
        self.temperatureAlarmObject   = TemperatureMaapiAlarmObject(logger, self)
        self.powerSupplyStaticList    = PowerSupplyStaticMaapiList(logger, self)
        self.fanStaticList            = FanStaticMaapiList(logger, self)
        self.tempSensorStaticList     = TempSensorStaticMaapiList(logger, self)


    def initSupportedAlarmNames (self):
        self._addSupportedAlarmName(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_POWER_SUPPLIES_NO_REDUNDANCY)
        self._addSupportedAlarmName(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_POWER_SUPPLY_FAILURE)
        self._addSupportedAlarmName(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_FANS_NO_REDUNDANCY)
        self._addSupportedAlarmName(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_FAN_FAILURE)
        self._addSupportedAlarmName(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_SYSTEM_TEMPERATURE_WARNING)
        self._addSupportedAlarmName(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_SYSTEM_TEMPERATURE_CRITICAL)
        self._addSupportedAlarmName(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_TEMPERATURE_SENSOR_WARNING)
        self._addSupportedAlarmName(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_TEMPERATURE_SENSOR_CRITICAL)
    

    def _pollUnsimulatedActiveAlarms (self):
        # get all the information via maapi
        tuplesKeyPowerSupply = self.powerSupplyStaticList.get()
        if tuplesKeyPowerSupply is None:
            self._log("poll-unsimulated-active-alarms").warning("list of tuples-key-power-supply is None, should have been a list")
            raise AlarmSourceError("could not get power-supplies information")

        tuplesKeyFan = self.fanStaticList.get()
        if tuplesKeyFan is None:
            self._log("poll-unsimulated-active-alarms").warning("list of tuples-key-fan is None, should have been a list")
            raise AlarmSourceError("could not get fans information")

        tuplesKeyTempSensor = self.tempSensorStaticList.get()
        if tuplesKeyTempSensor is None:
            self._log("poll-unsimulated-active-alarms").warning("list of tuples-key-temp-sensor is None, should have been a list")
            raise AlarmSourceError("could not get temperature sensor information")

        powerAlarmMaapi = self.powerSuppliesAlarmObject.get()
        if powerAlarmMaapi is None:
            self._log("poll-unsimulated-active-alarms").warning("power-supplies alarm is None, should have been an object")
            raise AlarmSourceError("could not get power-supplies information")

        fansAlarmMaapi = self.fansAlarmObject.get()
        if fansAlarmMaapi is None:
            self._log("poll-unsimulated-active-alarms").warning("fans alarm is None, should have been an object")
            raise AlarmSourceError("could not get fans information")

        temperatureAlarmMaapi = self.temperatureAlarmObject.get()
        if temperatureAlarmMaapi is None:
            self._log("poll-unsimulated-active-alarms").warning("temperatures alarm is None, should have been an object")
            raise AlarmSourceError("could not get temperature information")

        # go over all the information, and create alarms if relevant
        alarms = []        

        for (powerSupplyName, powerSupplyObject) in tuplesKeyPowerSupply:
            alarmsObj = powerSupplyObject.getAlarmObj()
            self._log("get-real-active-alarms").debug3("power supply %s, hasAlarm = %s, alarm=%s", powerSupplyName, alarmsObj.hasPowerSupplyFailure(), alarmsObj.powerSupplyFailure)
            if alarmsObj.hasPowerSupplyFailure() and alarmsObj.powerSupplyFailure:
                alarms.append(self._newAlarmInfo(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_POWER_SUPPLY_FAILURE, self._powerSupplyNameToEntity(powerSupplyName)))

        for (fanName, fanObject) in tuplesKeyFan:
            alarmsObj = fanObject.getAlarmObj()
            self._log("get-real-active-alarms").debug3("fan %s, hasAlarm = %s, alarm=%s", fanName, alarmsObj.hasFanFailure(), alarmsObj.fanFailure)
            if alarmsObj.hasFanFailure() and alarmsObj.fanFailure:
                alarms.append(self._newAlarmInfo(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_FAN_FAILURE, self._fanNameToEntity(fanName)))

        for (sensorName, sensorObject) in tuplesKeyTempSensor:
            alarmsObj = sensorObject.getAlarmObj()
            self._log("get-real-active-alarms").debug3("sensor %s, hasAlarm = %s, alarm=%s", sensorName, alarmsObj.hasTemperatureWarning(), alarmsObj.temperatureWarning)
            if alarmsObj.hasTemperatureWarning() and alarmsObj.temperatureWarning:
                alarms.append(self._newAlarmInfo(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_TEMPERATURE_SENSOR_WARNING, self._tempSensorNameToEntity(sensorName)))

            self._log("get-real-active-alarms").debug3("sensor %s, hasAlarm = %s, alarm=%s", sensorName, alarmsObj.hasTemperatureCritical(), alarmsObj.temperatureCritical)
            if alarmsObj.hasTemperatureCritical() and alarmsObj.temperatureCritical:
                alarms.append(self._newAlarmInfo(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_TEMPERATURE_SENSOR_CRITICAL, self._tempSensorNameToEntity(sensorName)))

        if powerAlarmMaapi.hasNoRedundancy() and powerAlarmMaapi.noRedundancy:
            self._log("get-real-active-alarms").debug3("raised power supplies no-redundancy alarm")
            alarms.append(self._newAlarmInfo(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_POWER_SUPPLIES_NO_REDUNDANCY, a.api.alarms.alarm.platform.POWER_SUBSYSTEM_ENTITY_PATTERN))

        if fansAlarmMaapi.hasNoRedundancy() and fansAlarmMaapi.noRedundancy:
            self._log("get-real-active-alarms").debug3("raised fans no-redundancy alarm")
            alarms.append(self._newAlarmInfo(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_FANS_NO_REDUNDANCY, a.api.alarms.alarm.platform.FAN_SUBSYSTEM_ENTITY_PATTERN))

        if temperatureAlarmMaapi.hasTemperatureWarning() and temperatureAlarmMaapi.temperatureWarning:
            self._log("get-real-active-alarms").debug3("raised temperature warning alarm")
            alarms.append(self._newAlarmInfo(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_SYSTEM_TEMPERATURE_WARNING, a.api.alarms.alarm.platform.SYSTEM_TEMPERATURE_ENTITY_PATTERN))

        if temperatureAlarmMaapi.hasTemperatureCritical() and temperatureAlarmMaapi.temperatureCritical:
            self._log("get-real-active-alarms").debug3("raised temperature critical alarm")
            alarms.append(self._newAlarmInfo(a.api.alarms.alarm.platform.PLATFORM_ALARM_NAME_SYSTEM_TEMPERATURE_CRITICAL, a.api.alarms.alarm.platform.SYSTEM_TEMPERATURE_ENTITY_PATTERN))

        self._log("get-real-active-alarms").debug3("alarms=%s", alarms)
        return alarms


    def _powerSupplyNameToEntity (self, name):
        return name

    def _fanNameToEntity (self, name):
        return name

    def _tempSensorNameToEntity (self, name):
        return name


class PowerSupplyStaticMaapiList(StaticMaapiList):
    def __init__ (self, logger, alarmSource):
        StaticMaapiList.__init__(self, logger, alarmSource)
        
    def _getMaapiList (self, logger):
        """ Creates and returns a MaapiList object (Blinky generated) specific for the extension class.
        Used by the Static list handler methods of the base.
        In failure cases - returns None.
        Failure does not cause immediate harm (further static maapi operation will simply not occur).

        Extensions of this class should implement this function (if static maapi list functionality desired)

        Returns: MaapiList
        Raises: None
        """
        return BlinkyPowerSupplyMaapiList(logger)

    def _getNewObject (self, list):
        """ Calls the extension-specific MaapiList NewObject method. """
        return list.newPowerSupply()

    def _requestObject (self, powerSupplyObject):
        """ Calls the extensions-specific request maapi fields """
        alarmObj = powerSupplyObject.newAlarm()
        alarmObj.requestPowerSupplyFailure(True)
        powerSupplyObject.setAlarmObj(alarmObj)

    def _setObject (self, list, key, object):
        """ Calls the extension-specific MaapiList setObject method. """
        return list.setPowerSupplyObj(key, object)



class FanStaticMaapiList(StaticMaapiList):
    def __init__ (self, logger, alarmSource):
        StaticMaapiList.__init__(self, logger, alarmSource)

    def _getMaapiList (self, logger):
        """ Creates and returns a MaapiList object (Blinky generated) specific for the extension class.
        Used by the Static list handler methods of the base.
        In failure cases - returns None.
        Failure does not cause immediate harm (further static maapi operation will simply not occur).

        Extensions of this class should implement this function (if static maapi list functionality desired)

        Returns: MaapiList
        Raises: None
        """
        return BlinkyFanMaapiList(logger)

    def _getNewObject (self, list):
        """ Calls the extension-specific MaapiList NewObject method. """
        return list.newFan()

    def _requestObject (self, fanObject):
        """ Calls the extensions-specific request maapi fields """
        alarmObj = fanObject.newAlarm()
        alarmObj.requestFanFailure(True)
        fanObject.setAlarmObj(alarmObj)

    def _setObject (self, list, key, object):
        """ Calls the extension-specific MaapiList setObject method. """
        return list.setFanObj(key, object)


class TempSensorStaticMaapiList(StaticMaapiList):
    def __init__ (self, logger, alarmSource):
        StaticMaapiList.__init__(self, logger, alarmSource)

    def _getMaapiList (self, logger):
        """ Creates and returns a MaapiList object (Blinky generated) specific for the extension class.
        Used by the Static list handler methods of the base.
        In failure cases - returns None.
        Failure does not cause immediate harm (further static maapi operation will simply not occur).

        Extensions of this class should implement this function (if static maapi list functionality desired)

        Returns: MaapiList
        Raises: None
        """
        return BlinkySensorMaapiList(logger)

    def _getNewObject (self, list):
        """ Calls the extension-specific MaapiList NewObject method. """
        return list.newSensor()

    def _requestObject (self, sensorObject):
        """ Calls the extensions-specific request maapi fields """
        alarmObj = sensorObject.newAlarm()
        alarmObj.requestTemperatureWarning(True)
        alarmObj.requestTemperatureCritical(True)
        sensorObject.setAlarmObj(alarmObj)

    def _setObject (self, list, key, object):
        """ Calls the extension-specific MaapiList setObject method. """
        return list.setSensorObj(key, object)


class PowerSuppliesAlarmMaapiObject(MaapiObject):
    def __init__ (self, logger, alarmSource):
        MaapiObject.__init__(self, logger, alarmSource)

    def _getMaapiObject (self, logger):
        """ See base class
        """
        return a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.alarm.alarm_maapi_gen.BlinkyAlarmMaapi(logger)

    def _requestObject (self, alarmObject):
        """ Calls the extensions-specific request maapi fields """
        alarmObject.requestNoRedundancy(True)


class FansMaapiAlarmObject(MaapiObject):
    def __init__ (self, logger, alarmSource):
        MaapiObject.__init__(self, logger, alarmSource)

    def _getMaapiObject (self, logger):
        """ See base class
        """
        return a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.alarm.alarm_maapi_gen.BlinkyAlarmMaapi(logger)

    def _requestObject (self, alarmObject):
        """ Calls the extensions-specific request maapi fields """
        alarmObject.requestNoRedundancy(True)

class TemperatureMaapiAlarmObject(MaapiObject):
    def __init__ (self, logger, alarmSource):
        MaapiObject.__init__(self, logger, alarmSource)

    def _getMaapiObject (self, logger):
        """ See base class
        """
        return a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.alarm.alarm_maapi_gen.BlinkyAlarmMaapi(logger)

    def _requestObject (self, alarmObject):
        """ Calls the extensions-specific request maapi fields """
        alarmObject.requestTemperatureWarning(True)
        alarmObject.requestTemperatureCritical(True)
