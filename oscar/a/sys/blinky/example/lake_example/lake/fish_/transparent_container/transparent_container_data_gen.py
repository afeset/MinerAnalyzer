


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class TransparentContainerData(object):

    def __init__ (self):

        self.val = 0
        self._myHasVal=False
        

    def copyFrom (self, other):

        self.val=other.val
        self._myHasVal=other._myHasVal
        
    # has...() methods

    def hasVal (self):
        return self._myHasVal


    # setHas...() methods

    def setHasVal (self):
        self._myHasVal=True


    def clearAllHas (self):

        self._myHasVal=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasVal:
            x = "+"
        leafStr = str(self.val)
        items.append(x + "Val="+leafStr)

        return "{TransparentContainerData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "TransparentContainerData", 
        "namespace": "transparent_container", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.transparent_container.transparent_container_data_gen import TransparentContainerData"
    }, 
    "ancestors": [
        {
            "namespace": "lake", 
            "isCurrent": false
        }, 
        {
            "namespace": "fish_", 
            "isCurrent": false
        }, 
        {
            "namespace": "transparent_container", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "val", 
            "yangName": "val", 
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
            "lake_example"
        ]
    }, 
    "createTime": "2013"
}
"""


