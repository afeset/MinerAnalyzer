


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ConfigUData(object):

    def __init__ (self):

        self.valueConfigU1 = ""
        self._myHasValueConfigU1=False
        

    def copyFrom (self, other):

        self.valueConfigU1=other.valueConfigU1
        self._myHasValueConfigU1=other._myHasValueConfigU1
        
    # has...() methods

    def hasValueConfigU1 (self):
        return self._myHasValueConfigU1


    # setHas...() methods

    def setHasValueConfigU1 (self):
        self._myHasValueConfigU1=True


    def clearAllHas (self):

        self._myHasValueConfigU1=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasValueConfigU1:
            x = "+"
        leafStr = str(self.valueConfigU1)
        items.append(x + "ValueConfigU1="+leafStr)

        return "{ConfigUData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ConfigUData", 
        "namespace": "config_u", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_u.config_u_data_gen import ConfigUData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "config_u", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueConfigU1", 
            "yangName": "value-config-u1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
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


