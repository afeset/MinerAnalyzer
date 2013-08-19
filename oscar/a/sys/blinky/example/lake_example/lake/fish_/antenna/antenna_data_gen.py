


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

        self.a = 0
        self._myHasA=False
        
        self.c = 0
        self._myHasC=False
        
        self.b = 0
        self._myHasB=False
        
        self.e = 0
        self._myHasE=False
        
        self.d = 0
        self._myHasD=False
        
        self.height = 0
        self._myHasHeight=False
        
        self.a1 = ""
        self._myHasA1=False
        
        self.b1 = ""
        self._myHasB1=False
        
        self.c1 = ""
        self._myHasC1=False
        

    def copyFrom (self, other):

        self.a=other.a
        self._myHasA=other._myHasA
        
        self.c=other.c
        self._myHasC=other._myHasC
        
        self.b=other.b
        self._myHasB=other._myHasB
        
        self.e=other.e
        self._myHasE=other._myHasE
        
        self.d=other.d
        self._myHasD=other._myHasD
        
        self.height=other.height
        self._myHasHeight=other._myHasHeight
        
        self.a1=other.a1
        self._myHasA1=other._myHasA1
        
        self.b1=other.b1
        self._myHasB1=other._myHasB1
        
        self.c1=other.c1
        self._myHasC1=other._myHasC1
        
    # has...() methods

    def hasA (self):
        return self._myHasA

    def hasC (self):
        return self._myHasC

    def hasB (self):
        return self._myHasB

    def hasE (self):
        return self._myHasE

    def hasD (self):
        return self._myHasD

    def hasHeight (self):
        return self._myHasHeight

    def hasA1 (self):
        return self._myHasA1

    def hasB1 (self):
        return self._myHasB1

    def hasC1 (self):
        return self._myHasC1


    # setHas...() methods

    def setHasA (self):
        self._myHasA=True

    def setHasC (self):
        self._myHasC=True

    def setHasB (self):
        self._myHasB=True

    def setHasE (self):
        self._myHasE=True

    def setHasD (self):
        self._myHasD=True

    def setHasHeight (self):
        self._myHasHeight=True

    def setHasA1 (self):
        self._myHasA1=True

    def setHasB1 (self):
        self._myHasB1=True

    def setHasC1 (self):
        self._myHasC1=True


    def clearAllHas (self):

        self._myHasA=False

        self._myHasC=False

        self._myHasB=False

        self._myHasE=False

        self._myHasD=False

        self._myHasHeight=False

        self._myHasA1=False

        self._myHasB1=False

        self._myHasC1=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasA:
            x = "+"
        leafStr = str(self.a)
        items.append(x + "A="+leafStr)

        x=""
        if self._myHasC:
            x = "+"
        leafStr = str(self.c)
        items.append(x + "C="+leafStr)

        x=""
        if self._myHasB:
            x = "+"
        leafStr = str(self.b)
        items.append(x + "B="+leafStr)

        x=""
        if self._myHasE:
            x = "+"
        leafStr = str(self.e)
        items.append(x + "E="+leafStr)

        x=""
        if self._myHasD:
            x = "+"
        leafStr = str(self.d)
        items.append(x + "D="+leafStr)

        x=""
        if self._myHasHeight:
            x = "+"
        leafStr = str(self.height)
        items.append(x + "Height="+leafStr)

        x=""
        if self._myHasA1:
            x = "+"
        leafStr = str(self.a1)
        items.append(x + "A1="+leafStr)

        x=""
        if self._myHasB1:
            x = "+"
        leafStr = str(self.b1)
        items.append(x + "B1="+leafStr)

        x=""
        if self._myHasC1:
            x = "+"
        leafStr = str(self.c1)
        items.append(x + "C1="+leafStr)

        return "{AntennaData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "AntennaData", 
        "namespace": "antenna", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.antenna_data_gen import AntennaData"
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
            "namespace": "antenna", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "a", 
            "yangName": "a", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "c", 
            "yangName": "c", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "b", 
            "yangName": "b", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "e", 
            "yangName": "e", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "d", 
            "yangName": "d", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "a1", 
            "yangName": "a1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "b1", 
            "yangName": "b1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c1", 
            "yangName": "c1", 
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


