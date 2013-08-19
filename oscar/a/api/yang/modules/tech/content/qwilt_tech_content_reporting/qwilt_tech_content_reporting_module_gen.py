
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class ReportingExportTypesType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kLimelight=_Type_(1, "kLimelight", "limelight")
    
    kNone=_Type_(0, "kNone", "none")
    

    @staticmethod
    def isValidValue (value):
        return ReportingExportTypesType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return ReportingExportTypesType._Type_.getByValue(value)


class ReportingExportQueueFullReasonType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kNone=_Type_(0, "kNone", "none")
    

    @staticmethod
    def isValidValue (value):
        return ReportingExportQueueFullReasonType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return ReportingExportQueueFullReasonType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "ReportingExportTypesType", 
            "enums": [
                {
                    "yangName": "reporting_export_type_limelight", 
                    "displayName": "limelight", 
                    "name": "kLimelight", 
                    "value": "1"
                }, 
                {
                    "yangName": "reporting_export_type_none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.qwilt_tech_content_reporting_module_gen import ReportingExportTypesType"
        }, 
        {
            "className": "ReportingExportQueueFullReasonType", 
            "enums": [
                {
                    "yangName": "none", 
                    "displayName": "none", 
                    "name": "kNone", 
                    "value": "0"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.qwilt_tech_content_reporting_module_gen import ReportingExportQueueFullReasonType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qtc_report"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content_reporting"
        ]
    }
}
"""


