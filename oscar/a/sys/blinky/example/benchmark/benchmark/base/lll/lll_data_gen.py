


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.sys.blinky.example.benchmark.benchmark.benchmark_module_gen import ColorT


class LllData(object):

    def __init__ (self):

        self.color = ColorT.kRed
        self._myHasColor=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.color=other.color
        self._myHasColor=other._myHasColor
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasColor (self):
        return self._myHasColor

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasColor (self):
        self._myHasColor=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasColor=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasColor:
            x = "+"
        leafStr = str(self.color)
        items.append(x + "Color="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{LllData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "LllData", 
        "namespace": "lll", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.lll_data_gen import LllData"
    }, 
    "ancestors": [
        {
            "namespace": "base", 
            "isCurrent": false
        }, 
        {
            "namespace": "lll", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
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


