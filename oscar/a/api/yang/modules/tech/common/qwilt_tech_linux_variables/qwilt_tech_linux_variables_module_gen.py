
# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes


class InitPhase(object):

    class _Type_(EnumWithValue):
        def __init__ (self, value, name, displayName):
            EnumWithValue.__init__(self, value, name)
            self._displayName = displayName

        def getDisplayName (self):
            return self._displayName

    
    kInitial=_Type_(1, "kInitial", "initial")
    
    kPostNetwork=_Type_(2, "kPostNetwork", "post-network")
    

    @staticmethod
    def isValidValue (value):
        return InitPhase._Type_.isValueValid(value)

    @staticmethod
    def getByValue (value):
        return InitPhase._Type_.getByValue(value)




"""
Extracted from the below data: 
{
    "conditionalDebugName": null, 
    "enumTypes": [
        {
            "className": "InitPhase", 
            "enums": [
                {
                    "yangName": "initial", 
                    "displayName": "initial", 
                    "name": "kInitial", 
                    "value": "1"
                }, 
                {
                    "yangName": "post_network", 
                    "displayName": "post-network", 
                    "name": "kPostNetwork", 
                    "value": "2"
                }
            ], 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.qwilt_tech_linux_variables_module_gen import InitPhase"
        }
    ], 
    "createTime": "2013", 
    "module": {
        "prefix": "qt_lnx_variables"
    }, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_linux_variables"
        ]
    }
}
"""


