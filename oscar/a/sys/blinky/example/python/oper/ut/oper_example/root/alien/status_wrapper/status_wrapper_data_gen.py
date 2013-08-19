


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class StatusWrapperData(object):

    def __init__ (self):

        self.dummy = 0
        self._myHasDummy=False
        

    def copyFrom (self, other):

        self.dummy=other.dummy
        self._myHasDummy=other._myHasDummy
        
    # has...() methods

    def hasDummy (self):
        return self._myHasDummy


    # setHas...() methods

    def setHasDummy (self):
        self._myHasDummy=True


    def clearAllHas (self):

        self._myHasDummy=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDummy:
            x = "+"
        leafStr = str(self.dummy)
        items.append(x + "Dummy="+leafStr)

        return "{StatusWrapperData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusWrapperData", 
        "namespace": "status_wrapper", 
        "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.status_wrapper.status_wrapper_data_gen import StatusWrapperData"
    }, 
    "ancestors": [
        {
            "namespace": "root", 
            "isCurrent": false
        }, 
        {
            "namespace": "alien", 
            "isCurrent": false
        }, 
        {
            "namespace": "status_wrapper", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "dummy", 
            "yangName": "dummy", 
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
            "python", 
            "oper", 
            "ut", 
            "oper_example"
        ]
    }, 
    "createTime": "2013"
}
"""


