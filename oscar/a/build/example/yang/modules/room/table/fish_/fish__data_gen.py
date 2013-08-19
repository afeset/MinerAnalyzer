


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class FishData(object):

    def __init__ (self):

        self.eyeNumber = 0
        self._myHasEyeNumber=False
        
        self.transparentField = False
        self._myHasTransparentField=False
        
        self.id = ""
        self._myHasId=False
        
        self.hasTail = False
        self._myHasHasTail=False
        

    def copyFrom (self, other):

        self.eyeNumber=other.eyeNumber
        self._myHasEyeNumber=other._myHasEyeNumber
        
        self.transparentField=other.transparentField
        self._myHasTransparentField=other._myHasTransparentField
        
        self.id=other.id
        self._myHasId=other._myHasId
        
        self.hasTail=other.hasTail
        self._myHasHasTail=other._myHasHasTail
        
    # has...() methods

    def hasEyeNumber (self):
        return self._myHasEyeNumber

    def hasTransparentField (self):
        return self._myHasTransparentField

    def hasId (self):
        return self._myHasId

    def hasHasTail (self):
        return self._myHasHasTail


    # setHas...() methods

    def setHasEyeNumber (self):
        self._myHasEyeNumber=True

    def setHasTransparentField (self):
        self._myHasTransparentField=True

    def setHasId (self):
        self._myHasId=True

    def setHasHasTail (self):
        self._myHasHasTail=True


    def clearAllHas (self):

        self._myHasEyeNumber=False

        self._myHasTransparentField=False

        self._myHasId=False

        self._myHasHasTail=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEyeNumber:
            x = "+"
        leafStr = str(self.eyeNumber)
        items.append(x + "EyeNumber="+leafStr)

        x=""
        if self._myHasTransparentField:
            x = "+"
        leafStr = str(self.transparentField)
        items.append(x + "TransparentField="+leafStr)

        x=""
        if self._myHasId:
            x = "+"
        leafStr = str(self.id)
        items.append(x + "Id="+leafStr)

        x=""
        if self._myHasHasTail:
            x = "+"
        leafStr = str(self.hasTail)
        items.append(x + "HasTail="+leafStr)

        return "{FishData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "FishData", 
        "namespace": "fish_", 
        "importStatement": "from a.build.example.yang.modules.room.table.fish_.fish__data_gen import FishData"
    }, 
    "ancestors": [
        {
            "namespace": "table", 
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
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
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
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
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


