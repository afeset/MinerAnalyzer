


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SizeDefaultData(object):

    def __init__ (self):

        self.width = 30
        self._myHasWidth=False
        
        self.length = 20
        self._myHasLength=False
        

    def copyFrom (self, other):

        self.width=other.width
        self._myHasWidth=other._myHasWidth
        
        self.length=other.length
        self._myHasLength=other._myHasLength
        
    # has...() methods

    def hasWidth (self):
        return self._myHasWidth

    def hasLength (self):
        return self._myHasLength


    # setHas...() methods

    def setHasWidth (self):
        self._myHasWidth=True

    def setHasLength (self):
        self._myHasLength=True


    def clearAllHas (self):

        self._myHasWidth=False

        self._myHasLength=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasWidth:
            x = "+"
        leafStr = str(self.width)
        items.append(x + "Width="+leafStr)

        x=""
        if self._myHasLength:
            x = "+"
        leafStr = str(self.length)
        items.append(x + "Length="+leafStr)

        return "{SizeDefaultData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SizeDefaultData", 
        "namespace": "size_default", 
        "importStatement": "from a.sys.blinky.example.lake_example.size_default.size_default_data_gen import SizeDefaultData"
    }, 
    "ancestors": [
        {
            "namespace": "size_default", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "width", 
            "yangName": "width", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "30", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "20", 
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


