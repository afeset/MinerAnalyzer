


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class RefPracticeData(object):

    def __init__ (self):

        self.someLeafRef = ""
        self._myHasSomeLeafRef=False
        

    def copyFrom (self, other):

        self.someLeafRef=other.someLeafRef
        self._myHasSomeLeafRef=other._myHasSomeLeafRef
        
    # has...() methods

    def hasSomeLeafRef (self):
        return self._myHasSomeLeafRef


    # setHas...() methods

    def setHasSomeLeafRef (self):
        self._myHasSomeLeafRef=True


    def clearAllHas (self):

        self._myHasSomeLeafRef=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasSomeLeafRef:
            x = "+"
        leafStr = str(self.someLeafRef)
        items.append(x + "SomeLeafRef="+leafStr)

        return "{RefPracticeData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "RefPracticeData", 
        "namespace": "ref_practice", 
        "importStatement": "from a.sys.blinky.example.lake_example.ref_practice.ref_practice_data_gen import RefPracticeData"
    }, 
    "ancestors": [
        {
            "namespace": "ref_practice", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "someLeafRef", 
            "yangName": "some-leaf-ref", 
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


