


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SchoolData(object):

    def __init__ (self):

        self.bestStudent = ""
        self._myHasBestStudent=False
        

    def copyFrom (self, other):

        self.bestStudent=other.bestStudent
        self._myHasBestStudent=other._myHasBestStudent
        
    # has...() methods

    def hasBestStudent (self):
        return self._myHasBestStudent


    # setHas...() methods

    def setHasBestStudent (self):
        self._myHasBestStudent=True


    def clearAllHas (self):

        self._myHasBestStudent=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasBestStudent:
            x = "+"
        leafStr = str(self.bestStudent)
        items.append(x + "BestStudent="+leafStr)

        return "{SchoolData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SchoolData", 
        "namespace": "school", 
        "importStatement": "from a.sys.blinky.example.ut.school_example.school.school_data_gen import SchoolData"
    }, 
    "ancestors": [
        {
            "namespace": "school", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "bestStudent", 
            "yangName": "best-student", 
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
            "ut", 
            "school_example"
        ]
    }, 
    "createTime": "2013"
}
"""


