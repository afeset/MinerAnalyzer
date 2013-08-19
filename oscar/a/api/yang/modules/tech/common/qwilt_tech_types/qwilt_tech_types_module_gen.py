
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class DecisionType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kTrue=_Type_(1, "kTrue", "true")
    
    kFalse=_Type_(0, "kFalse", "false")
    
    kPassThrough=_Type_(2, "kPassThrough", "pass-through")
    

    @staticmethod
    def isValidValue (value):
        return DecisionType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DecisionType._Type_.getByValue(value)


class SeverityType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(-1, "kNone", "none")
    
    kInformational=_Type_(6, "kInformational", "informational")
    
    kNotice=_Type_(5, "kNotice", "notice")
    
    kCritical=_Type_(2, "kCritical", "critical")
    
    kError=_Type_(3, "kError", "error")
    
    kDebug=_Type_(7, "kDebug", "debug")
    
    kAlert=_Type_(1, "kAlert", "alert")
    
    kWarning=_Type_(4, "kWarning", "warning")
    
    kEmergency=_Type_(0, "kEmergency", "emergency")
    

    @staticmethod
    def isValidValue (value):
        return SeverityType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return SeverityType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "DecisionType", 
            "enums": [
                {
                    "yangName": "decision_true", 
                    "displayName": "true", 
                    "name": "kTrue", 
                    "value": "1"
                }, 
                {
                    "yangName": "decision_false", 
                    "displayName": "false", 
                    "name": "kFalse", 
                    "value": "0"
                }, 
                {
                    "yangName": "decision_pass_through", 
                    "displayName": "pass-through", 
                    "name": "kPassThrough", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import DecisionType"
        }, 
        {
            "className": "SeverityType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "-1"
                }, 
                {
                    "yangName": "informational", 
                    "displayName": "informational", 
                    "name": "kInformational", 
                    "value": "6"
                }, 
                {
                    "yangName": "notice", 
                    "displayName": "notice", 
                    "name": "kNotice", 
                    "value": "5"
                }, 
                {
                    "yangName": "critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "2"
                }, 
                {
                    "yangName": "error", 
                    "displayName": "error", 
                    "name": "kError", 
                    "value": "3"
                }, 
                {
                    "yangName": "debug", 
                    "displayName": "debug", 
                    "name": "kDebug", 
                    "value": "7"
                }, 
                {
                    "yangName": "alert", 
                    "displayName": "alert", 
                    "name": "kAlert", 
                    "value": "1"
                }, 
                {
                    "yangName": "warning", 
                    "displayName": "warning", 
                    "name": "kWarning", 
                    "value": "4"
                }, 
                {
                    "yangName": "emergency", 
                    "displayName": "emergency", 
                    "name": "kEmergency", 
                    "value": "0"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_types"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_types"
        ]
    }
}
"""


