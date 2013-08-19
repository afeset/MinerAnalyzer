


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

        self.length = 0
        self._myHasLength=False
        
        self.boringLevel = 0
        self._myHasBoringLevel=False
        

    def copyFrom (self, other):

        self.length=other.length
        self._myHasLength=other._myHasLength
        
        self.boringLevel=other.boringLevel
        self._myHasBoringLevel=other._myHasBoringLevel
        
    # has...() methods

    def hasLength (self):
        return self._myHasLength

    def hasBoringLevel (self):
        return self._myHasBoringLevel


    # setHas...() methods

    def setHasLength (self):
        self._myHasLength=True

    def setHasBoringLevel (self):
        self._myHasBoringLevel=True


    def clearAllHas (self):

        self._myHasLength=False

        self._myHasBoringLevel=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasLength:
            x = "+"
        leafStr = str(self.length)
        items.append(x + "Length="+leafStr)

        x=""
        if self._myHasBoringLevel:
            x = "+"
        leafStr = str(self.boringLevel)
        items.append(x + "BoringLevel="+leafStr)

        return "{SizeData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SizeData", 
        "namespace": "size", 
        "importStatement": "from a.build.example.yang.modules.tv.show.size.size_data_gen import SizeData"
    }, 
    "ancestors": [
        {
            "namespace": "show", 
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
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "boringLevel", 
            "yangName": "boring-level", 
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
            "tv"
        ]
    }, 
    "createTime": "2013"
}
"""


