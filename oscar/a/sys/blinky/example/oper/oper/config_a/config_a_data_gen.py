


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ConfigAData(object):

    def __init__ (self):

        pass
        

    def copyFrom (self, other):

        pass
        
    # has...() methods


    # setHas...() methods


    def clearAllHas (self):

        pass


    def __str__ (self):
        items=[]

        return "{ConfigAData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ConfigAData", 
        "namespace": "config_a", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_a_data_gen import ConfigAData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [], 
    "module": {}, 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "oper", 
            "oper"
        ]
    }, 
    "createTime": "2013"
}
"""


