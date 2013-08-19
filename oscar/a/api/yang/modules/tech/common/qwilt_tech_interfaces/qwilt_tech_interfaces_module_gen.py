
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class MibAdminStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDown=_Type_(2, "kDown", "down")
    
    kTesting=_Type_(3, "kTesting", "testing")
    
    kUp=_Type_(1, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return MibAdminStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return MibAdminStatusType._Type_.getByValue(value)


class ConnectivityOperationalStatusReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kLinkOperationalStatusDown=_Type_(5, "kLinkOperationalStatusDown", "link-operational-status-down")
    
    kInterfaceFunctionsDoesNotRequireConnectivityCheck=_Type_(4, "kInterfaceFunctionsDoesNotRequireConnectivityCheck", "interface-functions-does-not-require-connectivity-check")
    
    kInterfaceHasNoIpAddress=_Type_(3, "kInterfaceHasNoIpAddress", "interface-has-no-ip-address")
    
    kUnknown=_Type_(0, "kUnknown", "unknown")
    
    kArpTestFailure=_Type_(7, "kArpTestFailure", "arp-test-failure")
    
    kPingTestFailure=_Type_(6, "kPingTestFailure", "ping-test-failure")
    
    kNeighborDiscoveryTestFailure=_Type_(8, "kNeighborDiscoveryTestFailure", "neighbor-discovery-test-failure")
    
    kInterfaceAdministrativelyDown=_Type_(2, "kInterfaceAdministrativelyDown", "interface-administratively-down")
    
    kSuccess=_Type_(1, "kSuccess", "success")
    

    @staticmethod
    def isValidValue (value):
        return ConnectivityOperationalStatusReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return ConnectivityOperationalStatusReasonType._Type_.getByValue(value)


class InterfaceIpv4ConnectivityFailureReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kArpTestFailure=_Type_(4, "kArpTestFailure", "arp-test-failure")
    
    kPingTestFailure=_Type_(5, "kPingTestFailure", "ping-test-failure")
    
    kLinkOperDown=_Type_(3, "kLinkOperDown", "link-oper-down")
    
    kOther=_Type_(2, "kOther", "other")
    

    @staticmethod
    def isValidValue (value):
        return InterfaceIpv4ConnectivityFailureReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return InterfaceIpv4ConnectivityFailureReasonType._Type_.getByValue(value)


class ConnectivityOperationalStatusType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDown=_Type_(2, "kDown", "down")
    
    kNotApplicable=_Type_(3, "kNotApplicable", "not-applicable")
    
    kUnknown=_Type_(0, "kUnknown", "unknown")
    
    kUp=_Type_(1, "kUp", "up")
    

    @staticmethod
    def isValidValue (value):
        return ConnectivityOperationalStatusType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return ConnectivityOperationalStatusType._Type_.getByValue(value)


class InterfaceIpv6ConnectivityFailureReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kPingTestFailure=_Type_(5, "kPingTestFailure", "ping-test-failure")
    
    kLinkOperDown=_Type_(3, "kLinkOperDown", "link-oper-down")
    
    kNeighborDiscoveryTestFailure=_Type_(4, "kNeighborDiscoveryTestFailure", "neighbor-discovery-test-failure")
    
    kOther=_Type_(2, "kOther", "other")
    

    @staticmethod
    def isValidValue (value):
        return InterfaceIpv6ConnectivityFailureReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return InterfaceIpv6ConnectivityFailureReasonType._Type_.getByValue(value)


class DriverTypeType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kOs=_Type_(1, "kOs", "os")
    
    kDedicated=_Type_(2, "kDedicated", "dedicated")
    
    kVirtual=_Type_(3, "kVirtual", "virtual")
    

    @staticmethod
    def isValidValue (value):
        return DriverTypeType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DriverTypeType._Type_.getByValue(value)


class InterfaceFailureReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(1, "kUnknown", "unknown")
    
    kLinkOperDown=_Type_(3, "kLinkOperDown", "link-oper-down")
    
    kOther=_Type_(2, "kOther", "other")
    

    @staticmethod
    def isValidValue (value):
        return InterfaceFailureReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return InterfaceFailureReasonType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "MibAdminStatusType", 
            "enums": [
                {
                    "yangName": "mib_admin_status_type_down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "2"
                }, 
                {
                    "yangName": "mib_admin_status_type_testing", 
                    "displayName": "testing", 
                    "name": "kTesting", 
                    "value": "3"
                }, 
                {
                    "yangName": "mib_admin_status_type_up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import MibAdminStatusType"
        }, 
        {
            "className": "ConnectivityOperationalStatusReasonType", 
            "enums": [
                {
                    "yangName": "link_operational_status_down", 
                    "displayName": "link-operational-status-down", 
                    "name": "kLinkOperationalStatusDown", 
                    "value": "5"
                }, 
                {
                    "yangName": "interface_functions_does_not_require_connectivity_check", 
                    "displayName": "interface-functions-does-not-require-connectivity-check", 
                    "name": "kInterfaceFunctionsDoesNotRequireConnectivityCheck", 
                    "value": "4"
                }, 
                {
                    "yangName": "interface_has_no_ip_address", 
                    "displayName": "interface-has-no-ip-address", 
                    "name": "kInterfaceHasNoIpAddress", 
                    "value": "3"
                }, 
                {
                    "yangName": "unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "0"
                }, 
                {
                    "yangName": "arp_test_failure", 
                    "displayName": "arp-test-failure", 
                    "name": "kArpTestFailure", 
                    "value": "7"
                }, 
                {
                    "yangName": "ping_test_failure", 
                    "displayName": "ping-test-failure", 
                    "name": "kPingTestFailure", 
                    "value": "6"
                }, 
                {
                    "yangName": "neighbor_discovery_test_failure", 
                    "displayName": "neighbor-discovery-test-failure", 
                    "name": "kNeighborDiscoveryTestFailure", 
                    "value": "8"
                }, 
                {
                    "yangName": "interface_administratively_down", 
                    "displayName": "interface-administratively-down", 
                    "name": "kInterfaceAdministrativelyDown", 
                    "value": "2"
                }, 
                {
                    "yangName": "success", 
                    "displayName": "success", 
                    "name": "kSuccess", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import ConnectivityOperationalStatusReasonType"
        }, 
        {
            "className": "InterfaceIpv4ConnectivityFailureReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "interface_ipv4_connectivity_failure_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "interface_failure_alarm_reason_arp_test_failure", 
                    "displayName": "arp-test-failure", 
                    "name": "kArpTestFailure", 
                    "value": "4"
                }, 
                {
                    "yangName": "interface_failure_alarm_reason_ping_test_failure", 
                    "displayName": "ping-test-failure", 
                    "name": "kPingTestFailure", 
                    "value": "5"
                }, 
                {
                    "yangName": "interface_failure_alarm_reason_link_oper_down", 
                    "displayName": "link-oper-down", 
                    "name": "kLinkOperDown", 
                    "value": "3"
                }, 
                {
                    "yangName": "interface_ipv4_connectivity_failure_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceIpv4ConnectivityFailureReasonType"
        }, 
        {
            "className": "ConnectivityOperationalStatusType", 
            "enums": [
                {
                    "yangName": "down", 
                    "displayName": "down", 
                    "name": "kDown", 
                    "value": "2"
                }, 
                {
                    "yangName": "not_applicable", 
                    "displayName": "not-applicable", 
                    "name": "kNotApplicable", 
                    "value": "3"
                }, 
                {
                    "yangName": "unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "0"
                }, 
                {
                    "yangName": "up", 
                    "displayName": "up", 
                    "name": "kUp", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import ConnectivityOperationalStatusType"
        }, 
        {
            "className": "InterfaceIpv6ConnectivityFailureReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "interface_ipv6_connectivity_failure_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "interface_failure_alarm_reason_ping_test_failure", 
                    "displayName": "ping-test-failure", 
                    "name": "kPingTestFailure", 
                    "value": "5"
                }, 
                {
                    "yangName": "interface_failure_alarm_reason_link_oper_down", 
                    "displayName": "link-oper-down", 
                    "name": "kLinkOperDown", 
                    "value": "3"
                }, 
                {
                    "yangName": "interface_failure_alarm_reason_neighbor_discovery_test_failure", 
                    "displayName": "neighbor-discovery-test-failure", 
                    "name": "kNeighborDiscoveryTestFailure", 
                    "value": "4"
                }, 
                {
                    "yangName": "interface_ipv6_connectivity_failure_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceIpv6ConnectivityFailureReasonType"
        }, 
        {
            "className": "DriverTypeType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "os", 
                    "displayName": "os", 
                    "name": "kOs", 
                    "value": "1"
                }, 
                {
                    "yangName": "dedicated", 
                    "displayName": "dedicated", 
                    "name": "kDedicated", 
                    "value": "2"
                }, 
                {
                    "yangName": "virtual", 
                    "displayName": "virtual", 
                    "name": "kVirtual", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import DriverTypeType"
        }, 
        {
            "className": "InterfaceFailureReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "interface_failure_alarm_reason_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "1"
                }, 
                {
                    "yangName": "interface_failure_alarm_reason_link_oper_down", 
                    "displayName": "link-oper-down", 
                    "name": "kLinkOperDown", 
                    "value": "3"
                }, 
                {
                    "yangName": "interface_failure_alarm_reason_other", 
                    "displayName": "other", 
                    "name": "kOther", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceFailureReasonType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_if"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_interfaces"
        ]
    }
}
"""


