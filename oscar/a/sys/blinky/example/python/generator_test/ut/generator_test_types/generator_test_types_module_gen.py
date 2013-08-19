
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class GenderT(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kMale=_Type_(20, "kMale", "male")
    
    kFemale=_Type_(10, "kFemale", "female")
    

    @staticmethod
    def isValidValue (value):
        return GenderT._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return GenderT._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "GenderT", 
            "enums": [
                {
                    "yangName": "male", 
                    "displayName": "male", 
                    "name": "kMale", 
                    "value": "20"
                }, 
                {
                    "yangName": "female", 
                    "displayName": "female", 
                    "name": "kFemale", 
                    "value": "10"
                }
            ], 
            "importStatement": "from a.sys.blinky.example.python.generator_test.ut.generator_test_types.generator_test_types_module_gen import GenderT"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "let"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "python", 
            "generator_test", 
            "ut", 
            "generator_test_types"
        ]
    }
}
"""


