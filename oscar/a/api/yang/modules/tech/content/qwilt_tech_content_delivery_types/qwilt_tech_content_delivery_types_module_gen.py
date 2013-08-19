
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class LoadBalanceSchemeType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kRoundRobin=_Type_(1, "kRoundRobin", "round-robin")
    
    kSourceIp=_Type_(2, "kSourceIp", "source-ip")
    
    kAnalyticsInterface=_Type_(0, "kAnalyticsInterface", "analytics-interface")
    

    @staticmethod
    def isValidValue (value):
        return LoadBalanceSchemeType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return LoadBalanceSchemeType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "LoadBalanceSchemeType", 
            "enums": [
                {
                    "yangName": "round_robin", 
                    "displayName": "round-robin", 
                    "name": "kRoundRobin", 
                    "value": "1"
                }, 
                {
                    "yangName": "source_ip", 
                    "displayName": "source-ip", 
                    "name": "kSourceIp", 
                    "value": "2"
                }, 
                {
                    "yangName": "analytics_interface", 
                    "displayName": "analytics-interface", 
                    "name": "kAnalyticsInterface", 
                    "value": "0"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_delivery_types.qwilt_tech_content_delivery_types_module_gen import LoadBalanceSchemeType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qtc_dt"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content_delivery_types"
        ]
    }
}
"""


