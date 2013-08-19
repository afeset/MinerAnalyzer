


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class OpLData(object):

    def __init__ (self):

        self.configDummy = 0
        self._myHasConfigDummy=False
        

    def copyFrom (self, other):

        self.configDummy=other.configDummy
        self._myHasConfigDummy=other._myHasConfigDummy
        
    # has...() methods

    def hasConfigDummy (self):
        return self._myHasConfigDummy


    # setHas...() methods

    def setHasConfigDummy (self):
        self._myHasConfigDummy=True


    def clearAllHas (self):

        self._myHasConfigDummy=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasConfigDummy:
            x = "+"
        leafStr = str(self.configDummy)
        items.append(x + "ConfigDummy="+leafStr)

        return "{OpLData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "OpLData", 
        "namespace": "op_l", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_l.op_l_data_gen import OpLData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_l", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "configDummy", 
            "yangName": "config-dummy", 
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


