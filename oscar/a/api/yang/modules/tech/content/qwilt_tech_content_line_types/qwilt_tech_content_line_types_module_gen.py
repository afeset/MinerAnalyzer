
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class AcquisitionAlgorithmType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kFirstHit=_Type_(3, "kFirstHit", "first-hit")
    
    kPassThrough=_Type_(0, "kPassThrough", "pass-through")
    
    kSecondHit=_Type_(1, "kSecondHit", "second-hit")
    
    kEfficiencyBased=_Type_(2, "kEfficiencyBased", "efficiency-based")
    

    @staticmethod
    def isValidValue (value):
        return AcquisitionAlgorithmType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return AcquisitionAlgorithmType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "AcquisitionAlgorithmType", 
            "enums": [
                {
                    "yangName": "acquisition_algorithm_first_hit", 
                    "displayName": "first-hit", 
                    "name": "kFirstHit", 
                    "value": "3"
                }, 
                {
                    "yangName": "acquisition_algorithm_pass_through", 
                    "displayName": "pass-through", 
                    "name": "kPassThrough", 
                    "value": "0"
                }, 
                {
                    "yangName": "acquisition_algorithm_second_hit", 
                    "displayName": "second-hit", 
                    "name": "kSecondHit", 
                    "value": "1"
                }, 
                {
                    "yangName": "acquisition_algorithm_efficiency_based", 
                    "displayName": "efficiency-based", 
                    "name": "kEfficiencyBased", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line_types.qwilt_tech_content_line_types_module_gen import AcquisitionAlgorithmType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_line_types"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content_line_types"
        ]
    }
}
"""


