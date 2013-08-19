


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class PartData(object):

    def __init__ (self):

        self.catalogId = 0
        self._myHasCatalogId=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.catalogId=other.catalogId
        self._myHasCatalogId=other._myHasCatalogId
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasCatalogId (self):
        return self._myHasCatalogId

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasCatalogId (self):
        self._myHasCatalogId=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasCatalogId=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasCatalogId:
            x = "+"
        leafStr = str(self.catalogId)
        items.append(x + "CatalogId="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{PartData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "PartData", 
        "namespace": "part", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.part.part_data_gen import PartData"
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
            "isCurrent": false
        }, 
        {
            "namespace": "part", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "catalogId", 
            "yangName": "catalog-id", 
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
            "lake_example"
        ]
    }, 
    "createTime": "2013"
}
"""


