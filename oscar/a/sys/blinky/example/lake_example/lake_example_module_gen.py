
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class DesignColorT(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kWhite=_Type_(2, "kWhite", "white")
    
    kBrown=_Type_(3, "kBrown", "brown")
    
    kYellow=_Type_(1, "kYellow", "yellow")
    

    @staticmethod
    def isValidValue (value):
        return DesignColorT._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DesignColorT._Type_.getByValue(value)


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
            "className": "DesignColorT", 
            "enums": [
                {
                    "yangName": "white", 
                    "displayName": "white", 
                    "name": "kWhite", 
                    "value": "2"
                }, 
                {
                    "yangName": "brown", 
                    "displayName": "brown", 
                    "name": "kBrown", 
                    "value": "3"
                }, 
                {
                    "yangName": "yellow", 
                    "displayName": "yellow", 
                    "name": "kYellow", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.sys.blinky.example.lake_example.lake_example_module_gen import DesignColorT"
        }, 
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
            "importStatement": "from a.sys.blinky.example.lake_example.lake_example_module_gen import ColorT"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "lake_example"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "lake_example"
        ]
    }
}
"""


