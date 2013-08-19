


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class PersonData(object):

    def __init__ (self):

        self.employed = False
        self._myHasEmployed=False
        
        self.name = ""
        self._myHasName=False
        
        self.height = 175
        self._myHasHeight=False
        

    def copyFrom (self, other):

        self.employed=other.employed
        self._myHasEmployed=other._myHasEmployed
        
        self.name=other.name
        self._myHasName=other._myHasName
        
        self.height=other.height
        self._myHasHeight=other._myHasHeight
        
    # has...() methods

    def hasEmployed (self):
        return self._myHasEmployed

    def hasName (self):
        return self._myHasName

    def hasHeight (self):
        return self._myHasHeight


    # setHas...() methods

    def setHasEmployed (self):
        self._myHasEmployed=True

    def setHasName (self):
        self._myHasName=True

    def setHasHeight (self):
        self._myHasHeight=True


    def clearAllHas (self):

        self._myHasEmployed=False

        self._myHasName=False

        self._myHasHeight=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEmployed:
            x = "+"
        leafStr = str(self.employed)
        items.append(x + "Employed="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasHeight:
            x = "+"
        leafStr = str(self.height)
        items.append(x + "Height="+leafStr)

        return "{PersonData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "PersonData", 
        "namespace": "person", 
        "importStatement": "from a.sys.blinky.example.python.simple.list.ut.list_example.person.person_data_gen import PersonData"
    }, 
    "ancestors": [
        {
            "namespace": "person", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "employed", 
            "yangName": "employed", 
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
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "175", 
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
            "python", 
            "simple", 
            "list", 
            "ut", 
            "list_example"
        ]
    }, 
    "createTime": "2013"
}
"""


