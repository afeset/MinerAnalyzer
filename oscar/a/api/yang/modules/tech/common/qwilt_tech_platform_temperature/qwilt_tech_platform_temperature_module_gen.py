
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class TemperatureOperationalStatusReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kWarningTemperatureRange=_Type_(4, "kWarningTemperatureRange", "warning-temperature-range")
    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kCriticalTemperatureRange=_Type_(5, "kCriticalTemperatureRange", "critical-temperature-range")
    
    kSimulation=_Type_(6, "kSimulation", "simulation")
    
    kNormalTemperatureRange=_Type_(3, "kNormalTemperatureRange", "normal-temperature-range")
    
    kOther=_Type_(2, "kOther", "other")
    

    @staticmethod
    def isValidValue (value):
        return TemperatureOperationalStatusReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return TemperatureOperationalStatusReasonType._Type_.getByValue(value)


class TemperatureOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kUnknown=_Type_(4, "kUnknown", "unknown")
    
    kOk=_Type_(1, "kOk", "ok")
    
    kWarning=_Type_(2, "kWarning", "warning")
    
    kCritical=_Type_(3, "kCritical", "critical")
    

    @staticmethod
    def isValidValue (value):
        return TemperatureOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return TemperatureOperationalStatusType._Type_.getByValue(value)


class SensorOperationalStatusReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kSimulation=_Type_(4, "kSimulation", "simulation")
    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kOther=_Type_(2, "kOther", "other")
    
    kOutOfRange=_Type_(3, "kOutOfRange", "out-of-range")
    

    @staticmethod
    def isValidValue (value):
        return SensorOperationalStatusReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return SensorOperationalStatusReasonType._Type_.getByValue(value)


class SensorDeviceStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kOk=_Type_(1, "kOk", "ok")
    
    kNone=_Type_(4, "kNone", "none")
    
    kUnknown=_Type_(0, "kUnknown", "unknown")
    
    kOther=_Type_(5, "kOther", "other")
    
    kNonCritical=_Type_(3, "kNonCritical", "non-critical")
    
    kCritical=_Type_(2, "kCritical", "critical")
    

    @staticmethod
    def isValidValue (value):
        return SensorDeviceStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return SensorDeviceStatusType._Type_.getByValue(value)


class SensorForceOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kOk=_Type_(1, "kOk", "ok")
    
    kWarning=_Type_(2, "kWarning", "warning")
    
    kCritical=_Type_(3, "kCritical", "critical")
    

    @staticmethod
    def isValidValue (value):
        return SensorForceOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return SensorForceOperationalStatusType._Type_.getByValue(value)


class TemperatureAlarmReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kOther=_Type_(2, "kOther", "other")
    
    kOutOfRange=_Type_(3, "kOutOfRange", "out-of-range")
    

    @staticmethod
    def isValidValue (value):
        return TemperatureAlarmReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return TemperatureAlarmReasonType._Type_.getByValue(value)


class TemperatureForceOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kOk=_Type_(1, "kOk", "ok")
    
    kWarning=_Type_(2, "kWarning", "warning")
    
    kCritical=_Type_(3, "kCritical", "critical")
    

    @staticmethod
    def isValidValue (value):
        return TemperatureForceOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return TemperatureForceOperationalStatusType._Type_.getByValue(value)


class SensorOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kOk=_Type_(1, "kOk", "ok")
    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(4, "kUnknown", "unknown")
    
    kOther=_Type_(5, "kOther", "other")
    
    kWarning=_Type_(2, "kWarning", "warning")
    
    kCritical=_Type_(3, "kCritical", "critical")
    

    @staticmethod
    def isValidValue (value):
        return SensorOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return SensorOperationalStatusType._Type_.getByValue(value)


class TemperatureStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kUnknown=_Type_(0, "kUnknown", "unknown")
    
    kOk=_Type_(1, "kOk", "ok")
    
    kCritical=_Type_(3, "kCritical", "critical")
    
    kNonCritical=_Type_(2, "kNonCritical", "non-critical")
    

    @staticmethod
    def isValidValue (value):
        return TemperatureStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return TemperatureStatusType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "TemperatureOperationalStatusReasonType", 
            "enums": [
                {
                    "yangName": "temperature_reason_warning_range", 
                    "displayName": "warning-temperature-range", 
                    "name": "kWarningTemperatureRange", 
                    "value": "4"
                }, 
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "temperature_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "temperature_reason_critical_range", 
                    "displayName": "critical-temperature-range", 
                    "name": "kCriticalTemperatureRange", 
                    "value": "5"
                }, 
                {
                    "yangName": "temperature_reason_simulation", 
                    "displayName": "simulation", 
                    "name": "kSimulation", 
                    "value": "6"
                }, 
                {
                    "yangName": "temperature_reason_normal_range", 
                    "displayName": "normal-temperature-range", 
                    "name": "kNormalTemperatureRange", 
                    "value": "3"
                }, 
                {
                    "yangName": "temperature_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureOperationalStatusReasonType"
        }, 
        {
            "className": "TemperatureOperationalStatusType", 
            "enums": [
                {
                    "yangName": "temperature_operational_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "4"
                }, 
                {
                    "yangName": "temperature_operational_status_ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "1"
                }, 
                {
                    "yangName": "temperature_operational_status_warning", 
                    "displayName": "warning", 
                    "name": "kWarning", 
                    "value": "2"
                }, 
                {
                    "yangName": "temperature_operational_status_critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureOperationalStatusType"
        }, 
        {
            "className": "SensorOperationalStatusReasonType", 
            "enums": [
                {
                    "yangName": "sensor_reason_simulation", 
                    "displayName": "simulation", 
                    "name": "kSimulation", 
                    "value": "4"
                }, 
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "sensor_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "sensor_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }, 
                {
                    "yangName": "sensor_out_of_range", 
                    "displayName": "out-of-range", 
                    "name": "kOutOfRange", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorOperationalStatusReasonType"
        }, 
        {
            "className": "SensorDeviceStatusType", 
            "enums": [
                {
                    "yangName": "sensor_device_status_ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "1"
                }, 
                {
                    "yangName": "sensor_device_status_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "4"
                }, 
                {
                    "yangName": "sensor_device_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "0"
                }, 
                {
                    "yangName": "sensor_device_status_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "5"
                }, 
                {
                    "yangName": "sensor_device_status_non_critical", 
                    "displayName": "non-critical", 
                    "name": "kNonCritical", 
                    "value": "3"
                }, 
                {
                    "yangName": "sensor_device_status_critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorDeviceStatusType"
        }, 
        {
            "className": "SensorForceOperationalStatusType", 
            "enums": [
                {
                    "yangName": "sensor_force_operational_status_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "sensor_force_operational_status_ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "1"
                }, 
                {
                    "yangName": "sensor_force_operational_status_warning", 
                    "displayName": "warning", 
                    "name": "kWarning", 
                    "value": "2"
                }, 
                {
                    "yangName": "sensor_force_operational_status_critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorForceOperationalStatusType"
        }, 
        {
            "className": "TemperatureAlarmReasonType", 
            "enums": [
                {
                    "yangName": "temperature_alarm_reason_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "temperature_alarm_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "temperature_alarm_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }, 
                {
                    "yangName": "temperature_alarm_reason_out_of_range", 
                    "displayName": "out-of-range", 
                    "name": "kOutOfRange", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureAlarmReasonType"
        }, 
        {
            "className": "TemperatureForceOperationalStatusType", 
            "enums": [
                {
                    "yangName": "temperature_force_operational_status_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "temperature_force_operational_status_ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "1"
                }, 
                {
                    "yangName": "temperature_force_operational_status_warning", 
                    "displayName": "warning", 
                    "name": "kWarning", 
                    "value": "2"
                }, 
                {
                    "yangName": "temperature_force_operational_status_critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureForceOperationalStatusType"
        }, 
        {
            "className": "SensorOperationalStatusType", 
            "enums": [
                {
                    "yangName": "sensor_status_ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "1"
                }, 
                {
                    "yangName": "sensor_status_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "sensor_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "4"
                }, 
                {
                    "yangName": "sensor_status_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "5"
                }, 
                {
                    "yangName": "sensor_status_warning", 
                    "displayName": "warning", 
                    "name": "kWarning", 
                    "value": "2"
                }, 
                {
                    "yangName": "sensor_status_critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorOperationalStatusType"
        }, 
        {
            "className": "TemperatureStatusType", 
            "enums": [
                {
                    "yangName": "temperature_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "0"
                }, 
                {
                    "yangName": "temperature_status_ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "1"
                }, 
                {
                    "yangName": "temperature_status_critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "3"
                }, 
                {
                    "yangName": "temperature_status_non_critical", 
                    "displayName": "non-critical", 
                    "name": "kNonCritical", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureStatusType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_pltf_temperature"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_platform_temperature"
        ]
    }
}
"""


