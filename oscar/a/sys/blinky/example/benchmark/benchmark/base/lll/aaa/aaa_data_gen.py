


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class AaaData(object):

    def __init__ (self):

        self.a1int64 = 0
        self._myHasA1int64=False
        
        self.a8str = ""
        self._myHasA8str=False
        
        self.a5str = ""
        self._myHasA5str=False
        
        self.a3str = ""
        self._myHasA3str=False
        
        self.a6str = ""
        self._myHasA6str=False
        
        self.a2str = ""
        self._myHasA2str=False
        
        self.a4str = ""
        self._myHasA4str=False
        
        self.a7str = ""
        self._myHasA7str=False
        
        self.a9str = ""
        self._myHasA9str=False
        

    def copyFrom (self, other):

        self.a1int64=other.a1int64
        self._myHasA1int64=other._myHasA1int64
        
        self.a8str=other.a8str
        self._myHasA8str=other._myHasA8str
        
        self.a5str=other.a5str
        self._myHasA5str=other._myHasA5str
        
        self.a3str=other.a3str
        self._myHasA3str=other._myHasA3str
        
        self.a6str=other.a6str
        self._myHasA6str=other._myHasA6str
        
        self.a2str=other.a2str
        self._myHasA2str=other._myHasA2str
        
        self.a4str=other.a4str
        self._myHasA4str=other._myHasA4str
        
        self.a7str=other.a7str
        self._myHasA7str=other._myHasA7str
        
        self.a9str=other.a9str
        self._myHasA9str=other._myHasA9str
        
    # has...() methods

    def hasA1int64 (self):
        return self._myHasA1int64

    def hasA8str (self):
        return self._myHasA8str

    def hasA5str (self):
        return self._myHasA5str

    def hasA3str (self):
        return self._myHasA3str

    def hasA6str (self):
        return self._myHasA6str

    def hasA2str (self):
        return self._myHasA2str

    def hasA4str (self):
        return self._myHasA4str

    def hasA7str (self):
        return self._myHasA7str

    def hasA9str (self):
        return self._myHasA9str


    # setHas...() methods

    def setHasA1int64 (self):
        self._myHasA1int64=True

    def setHasA8str (self):
        self._myHasA8str=True

    def setHasA5str (self):
        self._myHasA5str=True

    def setHasA3str (self):
        self._myHasA3str=True

    def setHasA6str (self):
        self._myHasA6str=True

    def setHasA2str (self):
        self._myHasA2str=True

    def setHasA4str (self):
        self._myHasA4str=True

    def setHasA7str (self):
        self._myHasA7str=True

    def setHasA9str (self):
        self._myHasA9str=True


    def clearAllHas (self):

        self._myHasA1int64=False

        self._myHasA8str=False

        self._myHasA5str=False

        self._myHasA3str=False

        self._myHasA6str=False

        self._myHasA2str=False

        self._myHasA4str=False

        self._myHasA7str=False

        self._myHasA9str=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasA1int64:
            x = "+"
        leafStr = str(self.a1int64)
        items.append(x + "A1int64="+leafStr)

        x=""
        if self._myHasA8str:
            x = "+"
        leafStr = str(self.a8str)
        items.append(x + "A8str="+leafStr)

        x=""
        if self._myHasA5str:
            x = "+"
        leafStr = str(self.a5str)
        items.append(x + "A5str="+leafStr)

        x=""
        if self._myHasA3str:
            x = "+"
        leafStr = str(self.a3str)
        items.append(x + "A3str="+leafStr)

        x=""
        if self._myHasA6str:
            x = "+"
        leafStr = str(self.a6str)
        items.append(x + "A6str="+leafStr)

        x=""
        if self._myHasA2str:
            x = "+"
        leafStr = str(self.a2str)
        items.append(x + "A2str="+leafStr)

        x=""
        if self._myHasA4str:
            x = "+"
        leafStr = str(self.a4str)
        items.append(x + "A4str="+leafStr)

        x=""
        if self._myHasA7str:
            x = "+"
        leafStr = str(self.a7str)
        items.append(x + "A7str="+leafStr)

        x=""
        if self._myHasA9str:
            x = "+"
        leafStr = str(self.a9str)
        items.append(x + "A9str="+leafStr)

        return "{AaaData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "AaaData", 
        "namespace": "aaa", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.aaa.aaa_data_gen import AaaData"
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
            "namespace": "aaa", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "a1int64", 
            "yangName": "a1int64", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "a8str", 
            "yangName": "a8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "a5str", 
            "yangName": "a5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "a3str", 
            "yangName": "a3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "a6str", 
            "yangName": "a6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "a2str", 
            "yangName": "a2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "a4str", 
            "yangName": "a4str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "a7str", 
            "yangName": "a7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "a9str", 
            "yangName": "a9str", 
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


