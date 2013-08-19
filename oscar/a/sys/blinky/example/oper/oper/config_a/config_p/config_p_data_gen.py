


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ConfigPData(object):

    def __init__ (self):

        self.id = 0
        self._myHasId=False
        

    def copyFrom (self, other):

        self.id=other.id
        self._myHasId=other._myHasId
        
    # has...() methods

    def hasId (self):
        return self._myHasId


    # setHas...() methods

    def setHasId (self):
        self._myHasId=True


    def clearAllHas (self):

        self._myHasId=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasId:
            x = "+"
        leafStr = str(self.id)
        items.append(x + "Id="+leafStr)

        return "{ConfigPData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ConfigPData", 
        "namespace": "config_p", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.config_p_data_gen import ConfigPData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "config_p", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "id", 
            "yangName": "id", 
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


