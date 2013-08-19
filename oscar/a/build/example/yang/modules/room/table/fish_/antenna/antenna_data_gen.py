


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class AntennaData(object):

    def __init__ (self):

        self.height = 0
        self._myHasHeight=False
        

    def copyFrom (self, other):

        self.height=other.height
        self._myHasHeight=other._myHasHeight
        
    # has...() methods

    def hasHeight (self):
        return self._myHasHeight


    # setHas...() methods

    def setHasHeight (self):
        self._myHasHeight=True


    def clearAllHas (self):

        self._myHasHeight=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasHeight:
            x = "+"
        leafStr = str(self.height)
        items.append(x + "Height="+leafStr)

        return "{AntennaData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "AntennaData", 
        "namespace": "antenna", 
        "importStatement": "from a.build.example.yang.modules.room.table.fish_.antenna.antenna_data_gen import AntennaData"
    }, 
    "ancestors": [
        {
            "namespace": "table", 
            "isCurrent": false
        }, 
        {
            "namespace": "fish_", 
            "isCurrent": false
        }, 
        {
            "namespace": "antenna", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
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
            "build", 
            "example", 
            "yang", 
            "modules", 
            "room"
        ]
    }, 
    "createTime": "2013"
}
"""


