


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class BbbData(object):

    def __init__ (self):

        self.b4int64 = 0
        self._myHasB4int64=False
        
        self.b6str = ""
        self._myHasB6str=False
        
        self.b3str = ""
        self._myHasB3str=False
        
        self.b5str = ""
        self._myHasB5str=False
        
        self.b7str = ""
        self._myHasB7str=False
        
        self.b9str = ""
        self._myHasB9str=False
        
        self.b1str = ""
        self._myHasB1str=False
        
        self.b8str = ""
        self._myHasB8str=False
        
        self.b2str = ""
        self._myHasB2str=False
        

    def copyFrom (self, other):

        self.b4int64=other.b4int64
        self._myHasB4int64=other._myHasB4int64
        
        self.b6str=other.b6str
        self._myHasB6str=other._myHasB6str
        
        self.b3str=other.b3str
        self._myHasB3str=other._myHasB3str
        
        self.b5str=other.b5str
        self._myHasB5str=other._myHasB5str
        
        self.b7str=other.b7str
        self._myHasB7str=other._myHasB7str
        
        self.b9str=other.b9str
        self._myHasB9str=other._myHasB9str
        
        self.b1str=other.b1str
        self._myHasB1str=other._myHasB1str
        
        self.b8str=other.b8str
        self._myHasB8str=other._myHasB8str
        
        self.b2str=other.b2str
        self._myHasB2str=other._myHasB2str
        
    # has...() methods

    def hasB4int64 (self):
        return self._myHasB4int64

    def hasB6str (self):
        return self._myHasB6str

    def hasB3str (self):
        return self._myHasB3str

    def hasB5str (self):
        return self._myHasB5str

    def hasB7str (self):
        return self._myHasB7str

    def hasB9str (self):
        return self._myHasB9str

    def hasB1str (self):
        return self._myHasB1str

    def hasB8str (self):
        return self._myHasB8str

    def hasB2str (self):
        return self._myHasB2str


    # setHas...() methods

    def setHasB4int64 (self):
        self._myHasB4int64=True

    def setHasB6str (self):
        self._myHasB6str=True

    def setHasB3str (self):
        self._myHasB3str=True

    def setHasB5str (self):
        self._myHasB5str=True

    def setHasB7str (self):
        self._myHasB7str=True

    def setHasB9str (self):
        self._myHasB9str=True

    def setHasB1str (self):
        self._myHasB1str=True

    def setHasB8str (self):
        self._myHasB8str=True

    def setHasB2str (self):
        self._myHasB2str=True


    def clearAllHas (self):

        self._myHasB4int64=False

        self._myHasB6str=False

        self._myHasB3str=False

        self._myHasB5str=False

        self._myHasB7str=False

        self._myHasB9str=False

        self._myHasB1str=False

        self._myHasB8str=False

        self._myHasB2str=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasB4int64:
            x = "+"
        leafStr = str(self.b4int64)
        items.append(x + "B4int64="+leafStr)

        x=""
        if self._myHasB6str:
            x = "+"
        leafStr = str(self.b6str)
        items.append(x + "B6str="+leafStr)

        x=""
        if self._myHasB3str:
            x = "+"
        leafStr = str(self.b3str)
        items.append(x + "B3str="+leafStr)

        x=""
        if self._myHasB5str:
            x = "+"
        leafStr = str(self.b5str)
        items.append(x + "B5str="+leafStr)

        x=""
        if self._myHasB7str:
            x = "+"
        leafStr = str(self.b7str)
        items.append(x + "B7str="+leafStr)

        x=""
        if self._myHasB9str:
            x = "+"
        leafStr = str(self.b9str)
        items.append(x + "B9str="+leafStr)

        x=""
        if self._myHasB1str:
            x = "+"
        leafStr = str(self.b1str)
        items.append(x + "B1str="+leafStr)

        x=""
        if self._myHasB8str:
            x = "+"
        leafStr = str(self.b8str)
        items.append(x + "B8str="+leafStr)

        x=""
        if self._myHasB2str:
            x = "+"
        leafStr = str(self.b2str)
        items.append(x + "B2str="+leafStr)

        return "{BbbData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "BbbData", 
        "namespace": "bbb", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.bbb.bbb_data_gen import BbbData"
    }, 
    "ancestors": [
        {
            "namespace": "base", 
            "isCurrent": false
        }, 
        {
            "namespace": "lll", 
            "isCurrent": false
        }, 
        {
            "namespace": "bbb", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "b4int64", 
            "yangName": "b4int64", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "b6str", 
            "yangName": "b6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "b3str", 
            "yangName": "b3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "b5str", 
            "yangName": "b5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "b7str", 
            "yangName": "b7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "b9str", 
            "yangName": "b9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "b1str", 
            "yangName": "b1str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "b8str", 
            "yangName": "b8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "b2str", 
            "yangName": "b2str", 
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
            "benchmark", 
            "benchmark"
        ]
    }, 
    "createTime": "2013"
}
"""


