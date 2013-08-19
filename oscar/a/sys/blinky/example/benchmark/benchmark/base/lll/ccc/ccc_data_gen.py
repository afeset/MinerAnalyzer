


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class CccData(object):

    def __init__ (self):

        self.c9str = ""
        self._myHasC9str=False
        
        self.c2str = ""
        self._myHasC2str=False
        
        self.c8str = ""
        self._myHasC8str=False
        
        self.c6str = ""
        self._myHasC6str=False
        
        self.c5str = ""
        self._myHasC5str=False
        
        self.c1str = ""
        self._myHasC1str=False
        
        self.c7str = ""
        self._myHasC7str=False
        
        self.c10str = ""
        self._myHasC10str=False
        
        self.c3str = ""
        self._myHasC3str=False
        
        self.c4str = ""
        self._myHasC4str=False
        

    def copyFrom (self, other):

        self.c9str=other.c9str
        self._myHasC9str=other._myHasC9str
        
        self.c2str=other.c2str
        self._myHasC2str=other._myHasC2str
        
        self.c8str=other.c8str
        self._myHasC8str=other._myHasC8str
        
        self.c6str=other.c6str
        self._myHasC6str=other._myHasC6str
        
        self.c5str=other.c5str
        self._myHasC5str=other._myHasC5str
        
        self.c1str=other.c1str
        self._myHasC1str=other._myHasC1str
        
        self.c7str=other.c7str
        self._myHasC7str=other._myHasC7str
        
        self.c10str=other.c10str
        self._myHasC10str=other._myHasC10str
        
        self.c3str=other.c3str
        self._myHasC3str=other._myHasC3str
        
        self.c4str=other.c4str
        self._myHasC4str=other._myHasC4str
        
    # has...() methods

    def hasC9str (self):
        return self._myHasC9str

    def hasC2str (self):
        return self._myHasC2str

    def hasC8str (self):
        return self._myHasC8str

    def hasC6str (self):
        return self._myHasC6str

    def hasC5str (self):
        return self._myHasC5str

    def hasC1str (self):
        return self._myHasC1str

    def hasC7str (self):
        return self._myHasC7str

    def hasC10str (self):
        return self._myHasC10str

    def hasC3str (self):
        return self._myHasC3str

    def hasC4str (self):
        return self._myHasC4str


    # setHas...() methods

    def setHasC9str (self):
        self._myHasC9str=True

    def setHasC2str (self):
        self._myHasC2str=True

    def setHasC8str (self):
        self._myHasC8str=True

    def setHasC6str (self):
        self._myHasC6str=True

    def setHasC5str (self):
        self._myHasC5str=True

    def setHasC1str (self):
        self._myHasC1str=True

    def setHasC7str (self):
        self._myHasC7str=True

    def setHasC10str (self):
        self._myHasC10str=True

    def setHasC3str (self):
        self._myHasC3str=True

    def setHasC4str (self):
        self._myHasC4str=True


    def clearAllHas (self):

        self._myHasC9str=False

        self._myHasC2str=False

        self._myHasC8str=False

        self._myHasC6str=False

        self._myHasC5str=False

        self._myHasC1str=False

        self._myHasC7str=False

        self._myHasC10str=False

        self._myHasC3str=False

        self._myHasC4str=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasC9str:
            x = "+"
        leafStr = str(self.c9str)
        items.append(x + "C9str="+leafStr)

        x=""
        if self._myHasC2str:
            x = "+"
        leafStr = str(self.c2str)
        items.append(x + "C2str="+leafStr)

        x=""
        if self._myHasC8str:
            x = "+"
        leafStr = str(self.c8str)
        items.append(x + "C8str="+leafStr)

        x=""
        if self._myHasC6str:
            x = "+"
        leafStr = str(self.c6str)
        items.append(x + "C6str="+leafStr)

        x=""
        if self._myHasC5str:
            x = "+"
        leafStr = str(self.c5str)
        items.append(x + "C5str="+leafStr)

        x=""
        if self._myHasC1str:
            x = "+"
        leafStr = str(self.c1str)
        items.append(x + "C1str="+leafStr)

        x=""
        if self._myHasC7str:
            x = "+"
        leafStr = str(self.c7str)
        items.append(x + "C7str="+leafStr)

        x=""
        if self._myHasC10str:
            x = "+"
        leafStr = str(self.c10str)
        items.append(x + "C10str="+leafStr)

        x=""
        if self._myHasC3str:
            x = "+"
        leafStr = str(self.c3str)
        items.append(x + "C3str="+leafStr)

        x=""
        if self._myHasC4str:
            x = "+"
        leafStr = str(self.c4str)
        items.append(x + "C4str="+leafStr)

        return "{CccData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "CccData", 
        "namespace": "ccc", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.ccc.ccc_data_gen import CccData"
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
            "namespace": "ccc", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c9str", 
            "yangName": "c9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c2str", 
            "yangName": "c2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c8str", 
            "yangName": "c8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c6str", 
            "yangName": "c6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c5str", 
            "yangName": "c5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c1str", 
            "yangName": "c1str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c7str", 
            "yangName": "c7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c10str", 
            "yangName": "c10str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c3str", 
            "yangName": "c3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "c4str", 
            "yangName": "c4str", 
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


