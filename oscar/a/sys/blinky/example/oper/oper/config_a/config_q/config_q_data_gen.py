


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ConfigQData(object):

    def __init__ (self):

        self.valueConfigQ = 0
        self._myHasValueConfigQ=False
        

    def copyFrom (self, other):

        self.valueConfigQ=other.valueConfigQ
        self._myHasValueConfigQ=other._myHasValueConfigQ
        
    # has...() methods

    def hasValueConfigQ (self):
        return self._myHasValueConfigQ


    # setHas...() methods

    def setHasValueConfigQ (self):
        self._myHasValueConfigQ=True


    def clearAllHas (self):

        self._myHasValueConfigQ=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasValueConfigQ:
            x = "+"
        leafStr = str(self.valueConfigQ)
        items.append(x + "ValueConfigQ="+leafStr)

        return "{ConfigQData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ConfigQData", 
        "namespace": "config_q", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_q.config_q_data_gen import ConfigQData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "config_q", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "valueConfigQ", 
            "yangName": "value-config-q", 
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


