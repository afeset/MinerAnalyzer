
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class Accessmodetype(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kReadOnly=_Type_(1, "kReadOnly", "read-only")
    

    @staticmethod
    def isValidValue (value):
        return Accessmodetype._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return Accessmodetype._Type_.getByValue(value)


class Truthvalue(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kFalse=_Type_(2, "kFalse", "false")
    
    kTrue=_Type_(1, "kTrue", "true")
    

    @staticmethod
    def isValidValue (value):
        return Truthvalue._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return Truthvalue._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "Accessmodetype", 
            "enums": [
                {
                    "yangName": "access_mode_read_only", 
                    "displayName": "read-only", 
                    "name": "kReadOnly", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.common.qwilt_types.qwilt_types_module_gen import Accessmodetype"
        }, 
        {
            "className": "Truthvalue", 
            "enums": [
                {
                    "yangName": "false", 
                    "displayName": "false", 
                    "name": "kFalse", 
                    "value": "2"
                }, 
                {
                    "yangName": "true", 
                    "displayName": "true", 
                    "name": "kTrue", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.common.qwilt_types.qwilt_types_module_gen import Truthvalue"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qtypes"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "common", 
            "qwilt_types"
        ]
    }
}
"""


