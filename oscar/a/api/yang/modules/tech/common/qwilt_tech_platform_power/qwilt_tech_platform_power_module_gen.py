
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class PowerNoRedundancyReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kOther=_Type_(2, "kOther", "other")
    
    kNoRedundancy=_Type_(3, "kNoRedundancy", "no-redundancy")
    

    @staticmethod
    def isValidValue (value):
        return PowerNoRedundancyReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerNoRedundancyReasonType._Type_.getByValue(value)


class PowerOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDegraded=_Type_(2, "kDegraded", "degraded")
    
    kUnknown=_Type_(3, "kUnknown", "unknown")
    
    kUp=_Type_(1, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return PowerOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerOperationalStatusType._Type_.getByValue(value)


class PowerSupplyForceOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDown=_Type_(2, "kDown", "down")
    
    kNone=_Type_(0, "kNone", "none")
    
    kUp=_Type_(1, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return PowerSupplyForceOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerSupplyForceOperationalStatusType._Type_.getByValue(value)


class PowerForceOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kDegraded=_Type_(2, "kDegraded", "degraded")
    
    kUp=_Type_(1, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return PowerForceOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerForceOperationalStatusType._Type_.getByValue(value)


class PowerSupplyOperationalStatusReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kAbsent=_Type_(3, "kAbsent", "absent")
    
    kSimulation=_Type_(5, "kSimulation", "simulation")
    
    kPowerSourceLost=_Type_(4, "kPowerSourceLost", "power-source-lost")
    
    kOther=_Type_(2, "kOther", "other")
    

    @staticmethod
    def isValidValue (value):
        return PowerSupplyOperationalStatusReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerSupplyOperationalStatusReasonType._Type_.getByValue(value)


class PowerSupplyOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDown=_Type_(2, "kDown", "down")
    
    kUnknown=_Type_(3, "kUnknown", "unknown")
    
    kUp=_Type_(1, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return PowerSupplyOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerSupplyOperationalStatusType._Type_.getByValue(value)


class PowerSupplyDeviceStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kUnknown=_Type_(0, "kUnknown", "unknown")
    
    kOk=_Type_(1, "kOk", "ok")
    
    kCritical=_Type_(2, "kCritical", "critical")
    
    kAbsent=_Type_(3, "kAbsent", "absent")
    

    @staticmethod
    def isValidValue (value):
        return PowerSupplyDeviceStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerSupplyDeviceStatusType._Type_.getByValue(value)


class PowerRedundancyStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kUnknown=_Type_(0, "kUnknown", "unknown")
    
    kFull=_Type_(2, "kFull", "full")
    
    kLost=_Type_(1, "kLost", "lost")
    

    @staticmethod
    def isValidValue (value):
        return PowerRedundancyStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerRedundancyStatusType._Type_.getByValue(value)


class PowerOperationalStatusReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kRedundant=_Type_(3, "kRedundant", "redundant")
    
    kSimulation=_Type_(5, "kSimulation", "simulation")
    
    kSingleSource=_Type_(4, "kSingleSource", "single-source")
    
    kOther=_Type_(2, "kOther", "other")
    

    @staticmethod
    def isValidValue (value):
        return PowerOperationalStatusReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerOperationalStatusReasonType._Type_.getByValue(value)


class PowerSupplyFailureReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kPowerSourceLost=_Type_(4, "kPowerSourceLost", "power-source-lost")
    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kOther=_Type_(2, "kOther", "other")
    
    kAbsent=_Type_(3, "kAbsent", "absent")
    

    @staticmethod
    def isValidValue (value):
        return PowerSupplyFailureReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerSupplyFailureReasonType._Type_.getByValue(value)


class PowerSupplyDeviceOnlineStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNotAvailable=_Type_(3, "kNotAvailable", "not-available")
    
    kPowerSourceLost=_Type_(2, "kPowerSourceLost", "power-source-lost")
    
    kUnknown=_Type_(0, "kUnknown", "unknown")
    
    kPresenceDetected=_Type_(1, "kPresenceDetected", "presence-detected")
    

    @staticmethod
    def isValidValue (value):
        return PowerSupplyDeviceOnlineStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return PowerSupplyDeviceOnlineStatusType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "PowerNoRedundancyReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "power_no_redundancy_alarm_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "power_no_redundancy_alarm_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }, 
                {
                    "yangName": "power_no_redundancy_alarm_reason_no_redundancy", 
                    "displayName": "no-redundancy", 
                    "name": "kNoRedundancy", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerNoRedundancyReasonType"
        }, 
        {
            "className": "PowerOperationalStatusType", 
            "enums": [
                {
                    "yangName": "power_status_degraded", 
                    "displayName": "degraded", 
                    "name": "kDegraded", 
                    "value": "2"
                }, 
                {
                    "yangName": "power_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "3"
                }, 
                {
                    "yangName": "power_status_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerOperationalStatusType"
        }, 
        {
            "className": "PowerSupplyForceOperationalStatusType", 
            "enums": [
                {
                    "yangName": "power_supply_force_operational_status_down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "2"
                }, 
                {
                    "yangName": "power_supply_force_operational_status_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "power_supply_force_operational_status_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyForceOperationalStatusType"
        }, 
        {
            "className": "PowerForceOperationalStatusType", 
            "enums": [
                {
                    "yangName": "power_force_operational_status_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "power_force_operational_status_degraded", 
                    "displayName": "degraded", 
                    "name": "kDegraded", 
                    "value": "2"
                }, 
                {
                    "yangName": "power_force_operational_status_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerForceOperationalStatusType"
        }, 
        {
            "className": "PowerSupplyOperationalStatusReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "power_supply_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "power_supply_reason_absent", 
                    "displayName": "absent", 
                    "name": "kAbsent", 
                    "value": "3"
                }, 
                {
                    "yangName": "power_supply_reason_simulation", 
                    "displayName": "simulation", 
                    "name": "kSimulation", 
                    "value": "5"
                }, 
                {
                    "yangName": "power_supply_reason_power_source_lost", 
                    "displayName": "power-source-lost", 
                    "name": "kPowerSourceLost", 
                    "value": "4"
                }, 
                {
                    "yangName": "power_supply_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyOperationalStatusReasonType"
        }, 
        {
            "className": "PowerSupplyOperationalStatusType", 
            "enums": [
                {
                    "yangName": "power_supply_status_down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "2"
                }, 
                {
                    "yangName": "power_supply_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "3"
                }, 
                {
                    "yangName": "power_supply_status_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyOperationalStatusType"
        }, 
        {
            "className": "PowerSupplyDeviceStatusType", 
            "enums": [
                {
                    "yangName": "power_supply_device_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "0"
                }, 
                {
                    "yangName": "power_supply_device_status_ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "1"
                }, 
                {
                    "yangName": "power_supply_device_status_critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "2"
                }, 
                {
                    "yangName": "power_supply_device_status_absent", 
                    "displayName": "absent", 
                    "name": "kAbsent", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceStatusType"
        }, 
        {
            "className": "PowerRedundancyStatusType", 
            "enums": [
                {
                    "yangName": "power_redudancy_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "0"
                }, 
                {
                    "yangName": "power_redudancy_full", 
                    "displayName": "full", 
                    "name": "kFull", 
                    "value": "2"
                }, 
                {
                    "yangName": "power_redudancy_lost", 
                    "displayName": "lost", 
                    "name": "kLost", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerRedundancyStatusType"
        }, 
        {
            "className": "PowerOperationalStatusReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "power_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "power_reason_redundant", 
                    "displayName": "redundant", 
                    "name": "kRedundant", 
                    "value": "3"
                }, 
                {
                    "yangName": "power_reason_simulation", 
                    "displayName": "simulation", 
                    "name": "kSimulation", 
                    "value": "5"
                }, 
                {
                    "yangName": "single_source", 
                    "displayName": "single-source", 
                    "name": "kSingleSource", 
                    "value": "4"
                }, 
                {
                    "yangName": "power_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerOperationalStatusReasonType"
        }, 
        {
            "className": "PowerSupplyFailureReasonType", 
            "enums": [
                {
                    "yangName": "no_redundancy_alarm_reason_power_source_lost", 
                    "displayName": "power-source-lost", 
                    "name": "kPowerSourceLost", 
                    "value": "4"
                }, 
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "no_redundancy_alarm_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "no_redundancy_alarm_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }, 
                {
                    "yangName": "no_redundancy_alarm_reason_absent", 
                    "displayName": "absent", 
                    "name": "kAbsent", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyFailureReasonType"
        }, 
        {
            "className": "PowerSupplyDeviceOnlineStatusType", 
            "enums": [
                {
                    "yangName": "power_supply_device_online_status_not_available", 
                    "displayName": "not-available", 
                    "name": "kNotAvailable", 
                    "value": "3"
                }, 
                {
                    "yangName": "power_supply_device_online_status_power_source_lost", 
                    "displayName": "power-source-lost", 
                    "name": "kPowerSourceLost", 
                    "value": "2"
                }, 
                {
                    "yangName": "power_supply_device_online_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "0"
                }, 
                {
                    "yangName": "power_supply_device_online_status_presence_detected", 
                    "displayName": "presence-detected", 
                    "name": "kPresenceDetected", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceOnlineStatusType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_pltf_pwr"
    }, 
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
    }
}
"""


