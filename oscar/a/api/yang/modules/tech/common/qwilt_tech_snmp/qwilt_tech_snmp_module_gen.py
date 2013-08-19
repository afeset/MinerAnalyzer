
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class SnmpNotificationVersionType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kV2c=_Type_(1, "kV2c", "v2c")
    
    kV1=_Type_(0, "kV1", "v1")
    

    @staticmethod
    def isValidValue (value):
        return SnmpNotificationVersionType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return SnmpNotificationVersionType._Type_.getByValue(value)


class SnmpNotificationTypeType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kTrap=_Type_(0, "kTrap", "trap")
    

    @staticmethod
    def isValidValue (value):
        return SnmpNotificationTypeType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return SnmpNotificationTypeType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "SnmpNotificationVersionType", 
            "enums": [
                {
                    "yangName": "snmp_notification_version_v2c", 
                    "displayName": "v2c", 
                    "name": "kV2c", 
                    "value": "1"
                }, 
                {
                    "yangName": "snmp_notification_version_v1", 
                    "displayName": "v1", 
                    "name": "kV1", 
                    "value": "0"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.qwilt_tech_snmp_module_gen import SnmpNotificationVersionType"
        }, 
        {
            "className": "SnmpNotificationTypeType", 
            "enums": [
                {
                    "yangName": "snmp_notification_type_trap", 
                    "displayName": "trap", 
                    "name": "kTrap", 
                    "value": "0"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.qwilt_tech_snmp_module_gen import SnmpNotificationTypeType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_snmp"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_snmp"
        ]
    }
}
"""


