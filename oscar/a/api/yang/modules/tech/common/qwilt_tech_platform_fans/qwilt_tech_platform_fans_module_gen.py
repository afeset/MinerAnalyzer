
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class FansOperationalStatusReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kNoRedundancy=_Type_(4, "kNoRedundancy", "no-redundancy")
    
    kRedundant=_Type_(3, "kRedundant", "redundant")
    
    kSimulation=_Type_(5, "kSimulation", "simulation")
    
    kOther=_Type_(2, "kOther", "other")
    

    @staticmethod
    def isValidValue (value):
        return FansOperationalStatusReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FansOperationalStatusReasonType._Type_.getByValue(value)


class FanForceOperationalStatusType(object):

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
        return FanForceOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FanForceOperationalStatusType._Type_.getByValue(value)


class FanOperationalStatusReasonType(object):

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
    
    kOther=_Type_(2, "kOther", "other")
    
    kLowRpm=_Type_(4, "kLowRpm", "low-rpm")
    

    @staticmethod
    def isValidValue (value):
        return FanOperationalStatusReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FanOperationalStatusReasonType._Type_.getByValue(value)


class FansRedundancyStatusType(object):

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
        return FansRedundancyStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FansRedundancyStatusType._Type_.getByValue(value)


class FanOperationalStatusType(object):

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
        return FanOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FanOperationalStatusType._Type_.getByValue(value)


class FansForceOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDown=_Type_(3, "kDown", "down")
    
    kNone=_Type_(0, "kNone", "none")
    
    kDegraded=_Type_(2, "kDegraded", "degraded")
    
    kUp=_Type_(1, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return FansForceOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FansForceOperationalStatusType._Type_.getByValue(value)


class FanFailureReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kOther=_Type_(2, "kOther", "other")
    
    kAbsent=_Type_(3, "kAbsent", "absent")
    
    kLowRpm=_Type_(4, "kLowRpm", "low-rpm")
    

    @staticmethod
    def isValidValue (value):
        return FanFailureReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FanFailureReasonType._Type_.getByValue(value)


class FanDeviceStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(3, "kNone", "none")
    
    kUnknown=_Type_(0, "kUnknown", "unknown")
    
    kOk=_Type_(1, "kOk", "ok")
    
    kCritical=_Type_(2, "kCritical", "critical")
    

    @staticmethod
    def isValidValue (value):
        return FanDeviceStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FanDeviceStatusType._Type_.getByValue(value)


class FansOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDown=_Type_(3, "kDown", "down")
    
    kDegraded=_Type_(2, "kDegraded", "degraded")
    
    kUnknown=_Type_(4, "kUnknown", "unknown")
    
    kUp=_Type_(1, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return FansOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FansOperationalStatusType._Type_.getByValue(value)


class FansNoRedundancyReasonType(object):

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
        return FansNoRedundancyReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return FansNoRedundancyReasonType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "FansOperationalStatusReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "fans_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "fans_reason_no_redundancy", 
                    "displayName": "no-redundancy", 
                    "name": "kNoRedundancy", 
                    "value": "4"
                }, 
                {
                    "yangName": "fans_reason_redundant", 
                    "displayName": "redundant", 
                    "name": "kRedundant", 
                    "value": "3"
                }, 
                {
                    "yangName": "fans_reason_simulation", 
                    "displayName": "simulation", 
                    "name": "kSimulation", 
                    "value": "5"
                }, 
                {
                    "yangName": "fans_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansOperationalStatusReasonType"
        }, 
        {
            "className": "FanForceOperationalStatusType", 
            "enums": [
                {
                    "yangName": "fan_force_operational_status_down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "2"
                }, 
                {
                    "yangName": "fan_force_operational_status_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "fan_force_operational_status_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanForceOperationalStatusType"
        }, 
        {
            "className": "FanOperationalStatusReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "fan_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "fan_reason_absent", 
                    "displayName": "absent", 
                    "name": "kAbsent", 
                    "value": "3"
                }, 
                {
                    "yangName": "fan_reason_simulation", 
                    "displayName": "simulation", 
                    "name": "kSimulation", 
                    "value": "5"
                }, 
                {
                    "yangName": "fan_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }, 
                {
                    "yangName": "fan_reason_low_rpm", 
                    "displayName": "low-rpm", 
                    "name": "kLowRpm", 
                    "value": "4"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanOperationalStatusReasonType"
        }, 
        {
            "className": "FansRedundancyStatusType", 
            "enums": [
                {
                    "yangName": "fans_redudancy_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "0"
                }, 
                {
                    "yangName": "fans_redudancy_full", 
                    "displayName": "full", 
                    "name": "kFull", 
                    "value": "2"
                }, 
                {
                    "yangName": "fans_redudancy_lost", 
                    "displayName": "lost", 
                    "name": "kLost", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansRedundancyStatusType"
        }, 
        {
            "className": "FanOperationalStatusType", 
            "enums": [
                {
                    "yangName": "fan_status_down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "2"
                }, 
                {
                    "yangName": "fan_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "3"
                }, 
                {
                    "yangName": "fan_status_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanOperationalStatusType"
        }, 
        {
            "className": "FansForceOperationalStatusType", 
            "enums": [
                {
                    "yangName": "fans_force_operational_status_down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "3"
                }, 
                {
                    "yangName": "fans_force_operational_status_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "fans_force_operational_status_degraded", 
                    "displayName": "degraded", 
                    "name": "kDegraded", 
                    "value": "2"
                }, 
                {
                    "yangName": "fans_force_operational_status_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansForceOperationalStatusType"
        }, 
        {
            "className": "FanFailureReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "fan_failure_alarm_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "fan_failure_alarm_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }, 
                {
                    "yangName": "fan_failure_alarm_reason_absent", 
                    "displayName": "absent", 
                    "name": "kAbsent", 
                    "value": "3"
                }, 
                {
                    "yangName": "fan_failure_alarm_reason_low_rpm", 
                    "displayName": "low-rpm", 
                    "name": "kLowRpm", 
                    "value": "4"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanFailureReasonType"
        }, 
        {
            "className": "FanDeviceStatusType", 
            "enums": [
                {
                    "yangName": "fan_device_status_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "3"
                }, 
                {
                    "yangName": "fan_device_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "0"
                }, 
                {
                    "yangName": "fan_device_status_ok", 
                    "displayName": "ok", 
                    "name": "kOk", 
                    "value": "1"
                }, 
                {
                    "yangName": "fan_device_status_critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanDeviceStatusType"
        }, 
        {
            "className": "FansOperationalStatusType", 
            "enums": [
                {
                    "yangName": "fans_status_down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "3"
                }, 
                {
                    "yangName": "fans_status_degraded", 
                    "displayName": "degraded", 
                    "name": "kDegraded", 
                    "value": "2"
                }, 
                {
                    "yangName": "fans_status_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "4"
                }, 
                {
                    "yangName": "fans_status_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansOperationalStatusType"
        }, 
        {
            "className": "FansNoRedundancyReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "fans_no_redundancy_alarm_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "fans_no_redundancy_alarm_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }, 
                {
                    "yangName": "fans_no_redundancy_alarm_reason_no_redundancy", 
                    "displayName": "no-redundancy", 
                    "name": "kNoRedundancy", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansNoRedundancyReasonType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_pltf_fans"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_platform_fans"
        ]
    }
}
"""


