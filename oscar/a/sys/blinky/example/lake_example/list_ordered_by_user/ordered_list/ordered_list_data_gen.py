


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class OrderedListData(object):

    def __init__ (self):

        self.name = ""
        self._myHasName=False
        
        self.value = 0
        self._myHasValue=False
        

    def copyFrom (self, other):

        self.name=other.name
        self._myHasName=other._myHasName
        
        self.value=other.value
        self._myHasValue=other._myHasValue
        
    # has...() methods

    def hasName (self):
        return self._myHasName

    def hasValue (self):
        return self._myHasValue


    # setHas...() methods

    def setHasName (self):
        self._myHasName=True

    def setHasValue (self):
        self._myHasValue=True


    def clearAllHas (self):

        self._myHasName=False

        self._myHasValue=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasValue:
            x = "+"
        leafStr = str(self.value)
        items.append(x + "Value="+leafStr)

        return "{OrderedListData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "OrderedListData", 
        "namespace": "ordered_list", 
        "importStatement": "from a.sys.blinky.example.lake_example.list_ordered_by_user.ordered_list.ordered_list_data_gen import OrderedListData"
    }, 
    "ancestors": [
        {
            "namespace": "list_ordered_by_user", 
            "isCurrent": false
        }, 
        {
            "namespace": "ordered_list", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
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
            "memberName": "value", 
            "yangName": "value", 
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


