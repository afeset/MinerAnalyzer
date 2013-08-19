
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class LogSeverity(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kDebug1=_Type_(8, "kDebug1", "debug1")
    
    kDebug5=_Type_(12, "kDebug5", "debug5")
    
    kDebug4=_Type_(11, "kDebug4", "debug4")
    
    kNotice=_Type_(6, "kNotice", "notice")
    
    kDebug2=_Type_(9, "kDebug2", "debug2")
    
    kCritical=_Type_(3, "kCritical", "critical")
    
    kInfo=_Type_(7, "kInfo", "info")
    
    kError=_Type_(4, "kError", "error")
    
    kNone=_Type_(-2, "kNone", "none")
    
    kDebug3=_Type_(10, "kDebug3", "debug3")
    
    kAlert=_Type_(2, "kAlert", "alert")
    
    kAny=_Type_(-1, "kAny", "any")
    
    kWarning=_Type_(5, "kWarning", "warning")
    
    kEmergency=_Type_(1, "kEmergency", "emergency")
    

    @staticmethod
    def isValidValue (value):
        return LogSeverity._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return LogSeverity._Type_.getByValue(value)


class DestinationType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kTextCsv=_Type_(2, "kTextCsv", "text-csv")
    
    kBinary=_Type_(0, "kBinary", "binary")
    
    kText=_Type_(1, "kText", "text")
    
    kTextSingleLine=_Type_(3, "kTextSingleLine", "text-single-line")
    

    @staticmethod
    def isValidValue (value):
        return DestinationType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return DestinationType._Type_.getByValue(value)


class EnableDecision(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kPassThrough=_Type_(-1, "kPassThrough", "pass-through")
    
    kDisable=_Type_(0, "kDisable", "disable")
    
    kEnable=_Type_(1, "kEnable", "enable")
    

    @staticmethod
    def isValidValue (value):
        return EnableDecision._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return EnableDecision._Type_.getByValue(value)


class LogWriteModeType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kSafe=_Type_(0, "kSafe", "safe")
    
    kFast=_Type_(1, "kFast", "fast")
    

    @staticmethod
    def isValidValue (value):
        return LogWriteModeType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return LogWriteModeType._Type_.getByValue(value)


class LogArchiveModeType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNoCompression=_Type_(1, "kNoCompression", "no-compression")
    
    kGzipFast=_Type_(4, "kGzipFast", "gzip-fast")
    
    kNone=_Type_(0, "kNone", "none")
    
    kBz2Fast=_Type_(7, "kBz2Fast", "bz2-fast")
    
    kBz2Standard=_Type_(6, "kBz2Standard", "bz2-standard")
    
    kGzipStandard=_Type_(3, "kGzipStandard", "gzip-standard")
    
    kGzipBest=_Type_(2, "kGzipBest", "gzip-best")
    
    kBz2Best=_Type_(5, "kBz2Best", "bz2-best")
    

    @staticmethod
    def isValidValue (value):
        return LogArchiveModeType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return LogArchiveModeType._Type_.getByValue(value)


class MatchBoolean(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kTrue=_Type_(1, "kTrue", "true")
    
    kFalse=_Type_(0, "kFalse", "false")
    
    kAny=_Type_(-1, "kAny", "any")
    

    @staticmethod
    def isValidValue (value):
        return MatchBoolean._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return MatchBoolean._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "LogSeverity", 
            "enums": [
                {
                    "yangName": "debug1", 
                    "displayName": "debug1", 
                    "name": "kDebug1", 
                    "value": "8"
                }, 
                {
                    "yangName": "debug5", 
                    "displayName": "debug5", 
                    "name": "kDebug5", 
                    "value": "12"
                }, 
                {
                    "yangName": "debug4", 
                    "displayName": "debug4", 
                    "name": "kDebug4", 
                    "value": "11"
                }, 
                {
                    "yangName": "notice", 
                    "displayName": "notice", 
                    "name": "kNotice", 
                    "value": "6"
                }, 
                {
                    "yangName": "debug2", 
                    "displayName": "debug2", 
                    "name": "kDebug2", 
                    "value": "9"
                }, 
                {
                    "yangName": "critical", 
                    "displayName": "critical", 
                    "name": "kCritical", 
                    "value": "3"
                }, 
                {
                    "yangName": "info", 
                    "displayName": "info", 
                    "name": "kInfo", 
                    "value": "7"
                }, 
                {
                    "yangName": "error", 
                    "displayName": "error", 
                    "name": "kError", 
                    "value": "4"
                }, 
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "-2"
                }, 
                {
                    "yangName": "debug3", 
                    "displayName": "debug3", 
                    "name": "kDebug3", 
                    "value": "10"
                }, 
                {
                    "yangName": "alert", 
                    "displayName": "alert", 
                    "name": "kAlert", 
                    "value": "2"
                }, 
                {
                    "yangName": "any", 
                    "displayName": "any", 
                    "name": "kAny", 
                    "value": "-1"
                }, 
                {
                    "yangName": "warning", 
                    "displayName": "warning", 
                    "name": "kWarning", 
                    "value": "5"
                }, 
                {
                    "yangName": "emergency", 
                    "displayName": "emergency", 
                    "name": "kEmergency", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogSeverity"
        }, 
        {
            "className": "DestinationType", 
            "enums": [
                {
                    "yangName": "text_csv", 
                    "displayName": "text-csv", 
                    "name": "kTextCsv", 
                    "value": "2"
                }, 
                {
                    "yangName": "binary", 
                    "displayName": "binary", 
                    "name": "kBinary", 
                    "value": "0"
                }, 
                {
                    "yangName": "text", 
                    "displayName": "text", 
                    "name": "kText", 
                    "value": "1"
                }, 
                {
                    "yangName": "text_single_line", 
                    "displayName": "text-single-line", 
                    "name": "kTextSingleLine", 
                    "value": "3"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import DestinationType"
        }, 
        {
            "className": "EnableDecision", 
            "enums": [
                {
                    "yangName": "pass_through", 
                    "displayName": "pass-through", 
                    "name": "kPassThrough", 
                    "value": "-1"
                }, 
                {
                    "yangName": "disable", 
                    "displayName": "disable", 
                    "name": "kDisable", 
                    "value": "0"
                }, 
                {
                    "yangName": "enable", 
                    "displayName": "enable", 
                    "name": "kEnable", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import EnableDecision"
        }, 
        {
            "className": "LogWriteModeType", 
            "enums": [
                {
                    "yangName": "safe", 
                    "displayName": "safe", 
                    "name": "kSafe", 
                    "value": "0"
                }, 
                {
                    "yangName": "fast", 
                    "displayName": "fast", 
                    "name": "kFast", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogWriteModeType"
        }, 
        {
            "className": "LogArchiveModeType", 
            "enums": [
                {
                    "yangName": "no_compression", 
                    "displayName": "no-compression", 
                    "name": "kNoCompression", 
                    "value": "1"
                }, 
                {
                    "yangName": "gzip_fast", 
                    "displayName": "gzip-fast", 
                    "name": "kGzipFast", 
                    "value": "4"
                }, 
                {
                    "yangName": "log_archive_mode_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }, 
                {
                    "yangName": "bz2_fast", 
                    "displayName": "bz2-fast", 
                    "name": "kBz2Fast", 
                    "value": "7"
                }, 
                {
                    "yangName": "bz2_standard", 
                    "displayName": "bz2-standard", 
                    "name": "kBz2Standard", 
                    "value": "6"
                }, 
                {
                    "yangName": "gzip_standard", 
                    "displayName": "gzip-standard", 
                    "name": "kGzipStandard", 
                    "value": "3"
                }, 
                {
                    "yangName": "gzip_best", 
                    "displayName": "gzip-best", 
                    "name": "kGzipBest", 
                    "value": "2"
                }, 
                {
                    "yangName": "bz2_best", 
                    "displayName": "bz2-best", 
                    "name": "kBz2Best", 
                    "value": "5"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogArchiveModeType"
        }, 
        {
            "className": "MatchBoolean", 
            "enums": [
                {
                    "yangName": "true", 
                    "displayName": "true", 
                    "name": "kTrue", 
                    "value": "1"
                }, 
                {
                    "yangName": "false", 
                    "displayName": "false", 
                    "name": "kFalse", 
                    "value": "0"
                }, 
                {
                    "yangName": "any", 
                    "displayName": "any", 
                    "name": "kAny", 
                    "value": "-1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import MatchBoolean"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_debug"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "debug", 
            "qwilt_tech_debug"
        ]
    }
}
"""


