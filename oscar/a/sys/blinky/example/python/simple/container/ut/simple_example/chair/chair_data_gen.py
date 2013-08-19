


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ChairData(object):

    def __init__ (self):

        self.color = "yellow"
        self._myHasColor=False
        
        self.pretty = False
        self._myHasPretty=False
        
        self.numOfLegs = 0
        self._myHasNumOfLegs=False
        

    def copyFrom (self, other):

        self.color=other.color
        self._myHasColor=other._myHasColor
        
        self.pretty=other.pretty
        self._myHasPretty=other._myHasPretty
        
        self.numOfLegs=other.numOfLegs
        self._myHasNumOfLegs=other._myHasNumOfLegs
        
    # has...() methods

    def hasColor (self):
        return self._myHasColor

    def hasPretty (self):
        return self._myHasPretty

    def hasNumOfLegs (self):
        return self._myHasNumOfLegs


    # setHas...() methods

    def setHasColor (self):
        self._myHasColor=True

    def setHasPretty (self):
        self._myHasPretty=True

    def setHasNumOfLegs (self):
        self._myHasNumOfLegs=True


    def clearAllHas (self):

        self._myHasColor=False

        self._myHasPretty=False

        self._myHasNumOfLegs=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasColor:
            x = "+"
        leafStr = str(self.color)
        items.append(x + "Color="+leafStr)

        x=""
        if self._myHasPretty:
            x = "+"
        leafStr = str(self.pretty)
        items.append(x + "Pretty="+leafStr)

        x=""
        if self._myHasNumOfLegs:
            x = "+"
        leafStr = str(self.numOfLegs)
        items.append(x + "NumOfLegs="+leafStr)

        return "{ChairData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ChairData", 
        "namespace": "chair", 
        "importStatement": "from a.sys.blinky.example.python.simple.container.ut.simple_example.chair.chair_data_gen import ChairData"
    }, 
    "ancestors": [
        {
            "namespace": "chair", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "yellow", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "pretty", 
            "yangName": "pretty", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "numOfLegs", 
            "yangName": "num-of-legs", 
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
            "simple", 
            "container", 
            "ut", 
            "simple_example"
        ]
    }, 
    "createTime": "2013"
}
"""


