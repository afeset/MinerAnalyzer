


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SizeData(object):

    def __init__ (self):

        self.width = 15
        self._myHasWidth=False
        
        self.length = 0
        self._myHasLength=False
        
        self.patternName = "solid"
        self._myHasPatternName=False
        

    def copyFrom (self, other):

        self.width=other.width
        self._myHasWidth=other._myHasWidth
        
        self.length=other.length
        self._myHasLength=other._myHasLength
        
        self.patternName=other.patternName
        self._myHasPatternName=other._myHasPatternName
        
    # has...() methods

    def hasWidth (self):
        return self._myHasWidth

    def hasLength (self):
        return self._myHasLength

    def hasPatternName (self):
        return self._myHasPatternName


    # setHas...() methods

    def setHasWidth (self):
        self._myHasWidth=True

    def setHasLength (self):
        self._myHasLength=True

    def setHasPatternName (self):
        self._myHasPatternName=True


    def clearAllHas (self):

        self._myHasWidth=False

        self._myHasLength=False

        self._myHasPatternName=False


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

        x=""
        if self._myHasPatternName:
            x = "+"
        leafStr = str(self.patternName)
        items.append(x + "PatternName="+leafStr)

        return "{SizeData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SizeData", 
        "namespace": "size", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.size.size_data_gen import SizeData"
    }, 
    "ancestors": [
        {
            "namespace": "lake", 
            "isCurrent": false
        }, 
        {
            "namespace": "size", 
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
            "defaultVal": "15", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "patternName", 
            "yangName": "pattern-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "solid", 
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


