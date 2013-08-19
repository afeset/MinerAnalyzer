

#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmDeclarationStateType
import a.api.alarms.alarm.alarm_base

PLATFORM_ALARM_SOURCE_NAME = "platform-source"
PLATFORM_ALARM_NAME_POWER_SUPPLIES_NO_REDUNDANCY = AlarmNameType.kPowerSuppliesNoRedundancy
PLATFORM_ALARM_NAME_POWER_SUPPLY_FAILURE         = AlarmNameType.kPowerSupplyFailure
PLATFORM_ALARM_NAME_FANS_NO_REDUNDANCY           = AlarmNameType.kFansNoRedundancy
PLATFORM_ALARM_NAME_FAN_FAILURE                  = AlarmNameType.kFanFailure
PLATFORM_ALARM_NAME_SYSTEM_TEMPERATURE_WARNING   = AlarmNameType.kTemperatureWarning
PLATFORM_ALARM_NAME_SYSTEM_TEMPERATURE_CRITICAL  = AlarmNameType.kTemperatureCritical
PLATFORM_ALARM_NAME_TEMPERATURE_SENSOR_WARNING   = AlarmNameType.kTemperatureSensorWarning
PLATFORM_ALARM_NAME_TEMPERATURE_SENSOR_CRITICAL  = AlarmNameType.kTemperatureSensorCritical


POWER_SUBSYSTEM_ENTITY_PATTERN       = "PowerSubSystem"
FAN_SUBSYSTEM_ENTITY_PATTERN         = "FanSubSystem"
SYSTEM_TEMPERATURE_ENTITY_PATTERN    = "SystemTemperature"

POWER_SUPPLY_ENTITY_PATTERN = "PowerSupply<X>/<Y>"
FAN_ENTITY_PATTERN          = "Fan<X>/<Y>"
TEMP_SENSOR_ENTITY_PATTERN  = "TempSensor<X>/<Y>"

a.api.alarms.alarm.alarm_base.registerAlarm(PLATFORM_ALARM_NAME_POWER_SUPPLIES_NO_REDUNDANCY, SeverityType.kError, AlarmDeclarationStateType.kActive,\
                                            PLATFORM_ALARM_SOURCE_NAME, "3.0.0", "",\
                                            "Power supplies are not redundant", POWER_SUBSYSTEM_ENTITY_PATTERN)

a.api.alarms.alarm.alarm_base.registerAlarm(PLATFORM_ALARM_NAME_POWER_SUPPLY_FAILURE, SeverityType.kError, AlarmDeclarationStateType.kActive,\
                                            PLATFORM_ALARM_SOURCE_NAME, "3.0.0", "",\
                                            "%s is down"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, POWER_SUPPLY_ENTITY_PATTERN)

a.api.alarms.alarm.alarm_base.registerAlarm(PLATFORM_ALARM_NAME_FANS_NO_REDUNDANCY, SeverityType.kError, AlarmDeclarationStateType.kActive,\
                                            PLATFORM_ALARM_SOURCE_NAME, "3.0.0", "",\
                                            "Fans are not redundant", FAN_SUBSYSTEM_ENTITY_PATTERN)

a.api.alarms.alarm.alarm_base.registerAlarm(PLATFORM_ALARM_NAME_FAN_FAILURE, SeverityType.kError, AlarmDeclarationStateType.kActive,\
                                            PLATFORM_ALARM_SOURCE_NAME, "3.0.0", "",\
                                            "%s is down"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, FAN_ENTITY_PATTERN)

a.api.alarms.alarm.alarm_base.registerAlarm(PLATFORM_ALARM_NAME_SYSTEM_TEMPERATURE_WARNING, SeverityType.kWarning, AlarmDeclarationStateType.kActive,\
                                            PLATFORM_ALARM_SOURCE_NAME, "3.5.0", "",\
                                            "System temperature status is warning", SYSTEM_TEMPERATURE_ENTITY_PATTERN)

a.api.alarms.alarm.alarm_base.registerAlarm(PLATFORM_ALARM_NAME_SYSTEM_TEMPERATURE_CRITICAL, SeverityType.kCritical, AlarmDeclarationStateType.kActive,\
                                            PLATFORM_ALARM_SOURCE_NAME, "3.5.0", "",\
                                            "System temperature status is critical", SYSTEM_TEMPERATURE_ENTITY_PATTERN)

a.api.alarms.alarm.alarm_base.registerAlarm(PLATFORM_ALARM_NAME_TEMPERATURE_SENSOR_WARNING, SeverityType.kWarning, AlarmDeclarationStateType.kActive,\
                                            PLATFORM_ALARM_SOURCE_NAME, "3.5.0", "",\
                                            "%s temperature reading is at the warning level"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, TEMP_SENSOR_ENTITY_PATTERN)

a.api.alarms.alarm.alarm_base.registerAlarm(PLATFORM_ALARM_NAME_TEMPERATURE_SENSOR_CRITICAL, SeverityType.kCritical, AlarmDeclarationStateType.kActive,\
                                            PLATFORM_ALARM_SOURCE_NAME, "3.5.0", "",\
                                            "%s temperature reading is at the critical level"%a.api.alarms.alarm.alarm_base.ENTITY_FORMAT_STRING, TEMP_SENSOR_ENTITY_PATTERN)

