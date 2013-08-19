
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class TestAlarmReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kOther=_Type_(1, "kOther", "other")
    
    kUserConfiguration=_Type_(2, "kUserConfiguration", "user-configuration")
    

    @staticmethod
    def isValidValue (value):
        return TestAlarmReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return TestAlarmReasonType._Type_.getByValue(value)


class AlarmNameType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kTemperatureSensorWarning=_Type_(24, "kTemperatureSensorWarning", "temperature-sensor-warning")
    
    kContentDiskFailure=_Type_(12, "kContentDiskFailure", "content-disk-failure")
    
    kFanFailure=_Type_(19, "kFanFailure", "fan-failure")
    
    kFansNoRedundancy=_Type_(18, "kFansNoRedundancy", "fans-no-redundancy")
    
    kSystemAlarmTestAlarmRaised=_Type_(11, "kSystemAlarmTestAlarmRaised", "system-alarm-test-alarm-raised")
    
    kInterfaceIpv6ConnectivityFailure=_Type_(15, "kInterfaceIpv6ConnectivityFailure", "interface-ipv6-connectivity-failure")
    
    kInterfaceIpv4ConnectivityFailure=_Type_(14, "kInterfaceIpv4ConnectivityFailure", "interface-ipv4-connectivity-failure")
    
    kPowerSupplyFailure=_Type_(17, "kPowerSupplyFailure", "power-supply-failure")
    
    kNoAlarm=_Type_(0, "kNoAlarm", "no-alarm")
    
    kReportsQueueGettingFull=_Type_(20, "kReportsQueueGettingFull", "reports-queue-getting-full")
    
    kTemperatureSensorCritical=_Type_(25, "kTemperatureSensorCritical", "temperature-sensor-critical")
    
    kPowerSuppliesNoRedundancy=_Type_(16, "kPowerSuppliesNoRedundancy", "power-supplies-no-redundancy")
    
    kInterfaceFailure=_Type_(13, "kInterfaceFailure", "interface-failure")
    
    kTemperatureCritical=_Type_(23, "kTemperatureCritical", "temperature-critical")
    
    kTemperatureWarning=_Type_(22, "kTemperatureWarning", "temperature-warning")
    
    kReportsQueueFull=_Type_(21, "kReportsQueueFull", "reports-queue-full")
    

    @staticmethod
    def isValidValue (value):
        return AlarmNameType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return AlarmNameType._Type_.getByValue(value)


class AlarmDeclarationStateType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kActive=_Type_(2, "kActive", "active")
    
    kRegistered=_Type_(1, "kRegistered", "registered")
    
    kDeprecated=_Type_(3, "kDeprecated", "deprecated")
    

    @staticmethod
    def isValidValue (value):
        return AlarmDeclarationStateType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return AlarmDeclarationStateType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "TestAlarmReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "test_alarm_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "1"
                }, 
                {
                    "yangName": "user_configuration", 
                    "displayName": "user-configuration", 
                    "name": "kUserConfiguration", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import TestAlarmReasonType"
        }, 
        {
            "className": "AlarmNameType", 
            "enums": [
                {
                    "yangName": "temperature_sensor_warning", 
                    "displayName": "temperature-sensor-warning", 
                    "name": "kTemperatureSensorWarning", 
                    "value": "24"
                }, 
                {
                    "yangName": "content_disk_failure", 
                    "displayName": "content-disk-failure", 
                    "name": "kContentDiskFailure", 
                    "value": "12"
                }, 
                {
                    "yangName": "fan_failure", 
                    "displayName": "fan-failure", 
                    "name": "kFanFailure", 
                    "value": "19"
                }, 
                {
                    "yangName": "fans_no_redundancy", 
                    "displayName": "fans-no-redundancy", 
                    "name": "kFansNoRedundancy", 
                    "value": "18"
                }, 
                {
                    "yangName": "system_alarm_test_alarm_raised", 
                    "displayName": "system-alarm-test-alarm-raised", 
                    "name": "kSystemAlarmTestAlarmRaised", 
                    "value": "11"
                }, 
                {
                    "yangName": "interface_ipv6_connectivity_failure", 
                    "displayName": "interface-ipv6-connectivity-failure", 
                    "name": "kInterfaceIpv6ConnectivityFailure", 
                    "value": "15"
                }, 
                {
                    "yangName": "interface_ipv4_connectivity_failure", 
                    "displayName": "interface-ipv4-connectivity-failure", 
                    "name": "kInterfaceIpv4ConnectivityFailure", 
                    "value": "14"
                }, 
                {
                    "yangName": "power_supply_failure", 
                    "displayName": "power-supply-failure", 
                    "name": "kPowerSupplyFailure", 
                    "value": "17"
                }, 
                {
                    "yangName": "no_alarm", 
                    "displayName": "no-alarm", 
                    "name": "kNoAlarm", 
                    "value": "0"
                }, 
                {
                    "yangName": "reports_queue_getting_full", 
                    "displayName": "reports-queue-getting-full", 
                    "name": "kReportsQueueGettingFull", 
                    "value": "20"
                }, 
                {
                    "yangName": "temperature_sensor_critical", 
                    "displayName": "temperature-sensor-critical", 
                    "name": "kTemperatureSensorCritical", 
                    "value": "25"
                }, 
                {
                    "yangName": "power_supplies_no_redundancy", 
                    "displayName": "power-supplies-no-redundancy", 
                    "name": "kPowerSuppliesNoRedundancy", 
                    "value": "16"
                }, 
                {
                    "yangName": "interface_failure", 
                    "displayName": "interface-failure", 
                    "name": "kInterfaceFailure", 
                    "value": "13"
                }, 
                {
                    "yangName": "temperature_critical", 
                    "displayName": "temperature-critical", 
                    "name": "kTemperatureCritical", 
                    "value": "23"
                }, 
                {
                    "yangName": "temperature_warning", 
                    "displayName": "temperature-warning", 
                    "name": "kTemperatureWarning", 
                    "value": "22"
                }, 
                {
                    "yangName": "reports_queue_full", 
                    "displayName": "reports-queue-full", 
                    "name": "kReportsQueueFull", 
                    "value": "21"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType"
        }, 
        {
            "className": "AlarmDeclarationStateType", 
            "enums": [
                {
                    "yangName": "active", 
                    "displayName": "active", 
                    "name": "kActive", 
                    "value": "2"
                }, 
                {
                    "yangName": "registered_", 
                    "displayName": "registered", 
                    "name": "kRegistered", 
                    "value": "1"
                }, 
                {
                    "yangName": "deprecated", 
                    "displayName": "deprecated", 
                    "name": "kDeprecated", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmDeclarationStateType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_sys_alarms"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_system_alarms"
        ]
    }
}
"""


