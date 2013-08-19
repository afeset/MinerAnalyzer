
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class OperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDown=_Type_(2, "kDown", "down")
    
    kLowerlayerdown=_Type_(7, "kLowerlayerdown", "lowerLayerDown")
    
    kTesting=_Type_(3, "kTesting", "testing")
    
    kUnknown=_Type_(4, "kUnknown", "unknown")
    
    kDormant=_Type_(5, "kDormant", "dormant")
    
    kNotpresent=_Type_(6, "kNotpresent", "notPresent")
    
    kUp=_Type_(1, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return OperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return OperationalStatusType._Type_.getByValue(value)


class DeviceCountersClearEventType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kOnPortUp=_Type_(1, "kOnPortUp", "on-port-up")
    
    kOnPortDown=_Type_(2, "kOnPortDown", "on-port-down")
    

    @staticmethod
    def isValidValue (value):
        return DeviceCountersClearEventType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DeviceCountersClearEventType._Type_.getByValue(value)


class ConnectivityCheckIpv6MethodType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kPing=_Type_(2, "kPing", "ping")
    
    kLink=_Type_(0, "kLink", "link")
    
    kNeighborDiscovery=_Type_(1, "kNeighborDiscovery", "neighbor-discovery")
    

    @staticmethod
    def isValidValue (value):
        return ConnectivityCheckIpv6MethodType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return ConnectivityCheckIpv6MethodType._Type_.getByValue(value)


class ConnectivityCheckIpv4MethodType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kArp=_Type_(1, "kArp", "arp")
    
    kPing=_Type_(2, "kPing", "ping")
    
    kLink=_Type_(0, "kLink", "link")
    

    @staticmethod
    def isValidValue (value):
        return ConnectivityCheckIpv4MethodType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return ConnectivityCheckIpv4MethodType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "OperationalStatusType", 
            "enums": [
                {
                    "yangName": "down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "2"
                }, 
                {
                    "yangName": "lowerLayerDown", 
                    "displayName": "lowerLayerDown", 
                    "name": "kLowerlayerdown", 
                    "value": "7"
                }, 
                {
                    "yangName": "testing", 
                    "displayName": "testing", 
                    "name": "kTesting", 
                    "value": "3"
                }, 
                {
                    "yangName": "unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "4"
                }, 
                {
                    "yangName": "dormant", 
                    "displayName": "dormant", 
                    "name": "kDormant", 
                    "value": "5"
                }, 
                {
                    "yangName": "notPresent", 
                    "displayName": "notPresent", 
                    "name": "kNotpresent", 
                    "value": "6"
                }, 
                {
                    "yangName": "up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import OperationalStatusType"
        }, 
        {
            "className": "DeviceCountersClearEventType", 
            "enums": [
                {
                    "yangName": "device_counters_clear_event_type_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "device_counters_clear_event_type_on_port_up", 
                    "displayName": "on-port-up", 
                    "name": "kOnPortUp", 
                    "value": "1"
                }, 
                {
                    "yangName": "device_counters_clear_event_type_on_port_down", 
                    "displayName": "on-port-down", 
                    "name": "kOnPortDown", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import DeviceCountersClearEventType"
        }, 
        {
            "className": "ConnectivityCheckIpv6MethodType", 
            "enums": [
                {
                    "yangName": "method_ping", 
                    "displayName": "ping", 
                    "name": "kPing", 
                    "value": "2"
                }, 
                {
                    "yangName": "method_link", 
                    "displayName": "link", 
                    "name": "kLink", 
                    "value": "0"
                }, 
                {
                    "yangName": "method_neighbor_discovery", 
                    "displayName": "neighbor-discovery", 
                    "name": "kNeighborDiscovery", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import ConnectivityCheckIpv6MethodType"
        }, 
        {
            "className": "ConnectivityCheckIpv4MethodType", 
            "enums": [
                {
                    "yangName": "method_arp", 
                    "displayName": "arp", 
                    "name": "kArp", 
                    "value": "1"
                }, 
                {
                    "yangName": "method_ping", 
                    "displayName": "ping", 
                    "name": "kPing", 
                    "value": "2"
                }, 
                {
                    "yangName": "method_link", 
                    "displayName": "link", 
                    "name": "kLink", 
                    "value": "0"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import ConnectivityCheckIpv4MethodType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_ift"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_interfaces_types"
        ]
    }
}
"""


