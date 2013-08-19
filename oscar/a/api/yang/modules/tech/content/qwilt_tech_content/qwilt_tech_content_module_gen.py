
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class SiteListType(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kExclude=_Type_(2, "kExclude", "exclude")
    
    kInclude=_Type_(1, "kInclude", "include")
    

    @staticmethod
    def isValidValue (value):
        return SiteListType._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return SiteListType._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "SiteListType", 
            "enums": [
                {
                    "yangName": "exclude", 
                    "displayName": "exclude", 
                    "name": "kExclude", 
                    "value": "2"
                }, 
                {
                    "yangName": "include", 
                    "displayName": "include", 
                    "name": "kInclude", 
                    "value": "1"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.qwilt_tech_content_module_gen import SiteListType"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qtc"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content"
        ]
    }
}
"""


