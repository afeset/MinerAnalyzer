


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class InterfaceData(object):

    def __init__ (self):

        self.description = ""
        self._myHasDescription=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasDescription (self):
        return self._myHasDescription

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasDescription=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDescription:
            x = "+"
        leafStr = str(self.description)
        items.append(x + "Description="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{InterfaceData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "InterfaceData", 
        "namespace": "interface", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.interface_data_gen import InterfaceData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "content", 
            "isCurrent": false
        }, 
        {
            "namespace": "interfaces", 
            "isCurrent": false
        }, 
        {
            "namespace": "interface", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
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
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content_interfaces"
        ]
    }, 
    "createTime": "2013"
}
"""


