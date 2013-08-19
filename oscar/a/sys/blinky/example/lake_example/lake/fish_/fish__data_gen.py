


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.sys.blinky.example.lake_example.lake_example_module_gen import ColorT
import struct


class FishData(object):

    def __init__ (self):

        self.transparentField = False
        self._myHasTransparentField=False
        
        self.color = ColorT.kRed
        self._myHasColor=False
        
        self.eyeNumber = 0
        self._myHasEyeNumber=False
        
        self.hasTail = False
        self._myHasHasTail=False
        
        self.finNumber = 0
        self._myHasFinNumber=False
        
        self.length = 0
        self._myHasLength=False
        
        self.ip6 = None
        self._myHasIp6=False
        
        self.id = ""
        self._myHasId=False
        

    def copyFrom (self, other):

        self.transparentField=other.transparentField
        self._myHasTransparentField=other._myHasTransparentField
        
        self.color=other.color
        self._myHasColor=other._myHasColor
        
        self.eyeNumber=other.eyeNumber
        self._myHasEyeNumber=other._myHasEyeNumber
        
        self.hasTail=other.hasTail
        self._myHasHasTail=other._myHasHasTail
        
        self.finNumber=other.finNumber
        self._myHasFinNumber=other._myHasFinNumber
        
        self.length=other.length
        self._myHasLength=other._myHasLength
        
        self.ip6=other.ip6
        self._myHasIp6=other._myHasIp6
        
        self.id=other.id
        self._myHasId=other._myHasId
        
    # has...() methods

    def hasTransparentField (self):
        return self._myHasTransparentField

    def hasColor (self):
        return self._myHasColor

    def hasEyeNumber (self):
        return self._myHasEyeNumber

    def hasHasTail (self):
        return self._myHasHasTail

    def hasFinNumber (self):
        return self._myHasFinNumber

    def hasLength (self):
        return self._myHasLength

    def hasIp6 (self):
        return self._myHasIp6

    def hasId (self):
        return self._myHasId


    # setHas...() methods

    def setHasTransparentField (self):
        self._myHasTransparentField=True

    def setHasColor (self):
        self._myHasColor=True

    def setHasEyeNumber (self):
        self._myHasEyeNumber=True

    def setHasHasTail (self):
        self._myHasHasTail=True

    def setHasFinNumber (self):
        self._myHasFinNumber=True

    def setHasLength (self):
        self._myHasLength=True

    def setHasIp6 (self):
        self._myHasIp6=True

    def setHasId (self):
        self._myHasId=True


    def clearAllHas (self):

        self._myHasTransparentField=False

        self._myHasColor=False

        self._myHasEyeNumber=False

        self._myHasHasTail=False

        self._myHasFinNumber=False

        self._myHasLength=False

        self._myHasIp6=False

        self._myHasId=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasTransparentField:
            x = "+"
        leafStr = str(self.transparentField)
        items.append(x + "TransparentField="+leafStr)

        x=""
        if self._myHasColor:
            x = "+"
        leafStr = str(self.color)
        items.append(x + "Color="+leafStr)

        x=""
        if self._myHasEyeNumber:
            x = "+"
        leafStr = str(self.eyeNumber)
        items.append(x + "EyeNumber="+leafStr)

        x=""
        if self._myHasHasTail:
            x = "+"
        leafStr = str(self.hasTail)
        items.append(x + "HasTail="+leafStr)

        x=""
        if self._myHasFinNumber:
            x = "+"
        leafStr = str(self.finNumber)
        items.append(x + "FinNumber="+leafStr)

        x=""
        if self._myHasLength:
            x = "+"
        leafStr = str(self.length)
        items.append(x + "Length="+leafStr)

        x=""
        if self._myHasIp6:
            x = "+"
        leafStr = socket.inet_ntop(socket.AF_INET6, self.ip6)
        items.append(x + "Ip6="+leafStr)

        x=""
        if self._myHasId:
            x = "+"
        leafStr = str(self.id)
        items.append(x + "Id="+leafStr)

        return "{FishData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "FishData", 
        "namespace": "fish_", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.fish__data_gen import FishData"
    }, 
    "ancestors": [
        {
            "namespace": "lake", 
            "isCurrent": false
        }, 
        {
            "namespace": "fish_", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "finNumber", 
            "yangName": "fin-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "ip6", 
            "yangName": "ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
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
            "lake_example"
        ]
    }, 
    "createTime": "2013"
}
"""


