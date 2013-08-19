
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class StorageModuleLocationTypeType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    
    kInternal=_Type_(1, "kInternal", "internal")
    
    kExternal=_Type_(2, "kExternal", "external")
    

    @staticmethod
    def isValidValue (value):
        return StorageModuleLocationTypeType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return StorageModuleLocationTypeType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "StorageModuleLocationTypeType", 
            "enums": [
                {
                    "yangName": "storage_module_location_type_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "storage_module_location_type_internal", 
                    "displayName": "internal", 
                    "name": "kInternal", 
                    "value": "1"
                }, 
                {
                    "yangName": "storage_module_location_type_external", 
                    "displayName": "external", 
                    "name": "kExternal", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_module.qwilt_tech_storage_module_module_gen import StorageModuleLocationTypeType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_strg_module"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_storage_module"
        ]
    }
}
"""


