
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class StorageControllerImplementationType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDellH810=_Type_(2, "kDellH810", "dell-h810")
    
    kDellH710=_Type_(1, "kDellH710", "dell-h710")
    
    kSimulatedSimple=_Type_(3, "kSimulatedSimple", "simulated-simple")
    
    kNone=_Type_(0, "kNone", "none")
    
    kUnknown=_Type_(5, "kUnknown", "unknown")
    
    kSimulatedFake=_Type_(4, "kSimulatedFake", "simulated-fake")
    

    @staticmethod
    def isValidValue (value):
        return StorageControllerImplementationType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return StorageControllerImplementationType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "StorageControllerImplementationType", 
            "enums": [
                {
                    "yangName": "storage_controller_implementation_type_dell_h810", 
                    "displayName": "dell-h810", 
                    "name": "kDellH810", 
                    "value": "2"
                }, 
                {
                    "yangName": "storage_controller_implementation_type_dell_h710", 
                    "displayName": "dell-h710", 
                    "name": "kDellH710", 
                    "value": "1"
                }, 
                {
                    "yangName": "storage_controller_implementation_type_simulated_simple", 
                    "displayName": "simulated-simple", 
                    "name": "kSimulatedSimple", 
                    "value": "3"
                }, 
                {
                    "yangName": "storage_controller_implementation_type_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "storage_controller_implementation_type_unknown", 
                    "displayName": "unknown", 
                    "name": "kUnknown", 
                    "value": "5"
                }, 
                {
                    "yangName": "storage_controller_implementation_type_simulated_fake", 
                    "displayName": "simulated-fake", 
                    "name": "kSimulatedFake", 
                    "value": "4"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.qwilt_tech_storage_controller_module_gen import StorageControllerImplementationType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_strg_ctrl"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_storage_controller"
        ]
    }
}
"""


