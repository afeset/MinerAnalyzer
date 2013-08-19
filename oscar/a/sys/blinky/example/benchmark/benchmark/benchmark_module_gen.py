
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class ColorT(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kBlue=_Type_(30, "kBlue", "blue")
    
    kGreen=_Type_(20, "kGreen", "green")
    
    kRed=_Type_(10, "kRed", "red")
    

    @staticmethod
    def isValidValue (value):
        return ColorT._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return ColorT._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "ColorT", 
            "enums": [
                {
                    "yangName": "blue", 
                    "displayName": "blue", 
                    "name": "kBlue", 
                    "value": "30"
                }, 
                {
                    "yangName": "green", 
                    "displayName": "green", 
                    "name": "kGreen", 
                    "value": "20"
                }, 
                {
                    "yangName": "red", 
                    "displayName": "red", 
                    "name": "kRed", 
                    "value": "10"
                }
            ], 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.benchmark_module_gen import ColorT"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "bnch"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "benchmark", 
            "benchmark"
        ]
    }
}
"""


