


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ZoneData(object):

    def __init__ (self):

        self.enabled = True
        self._myHasEnabled=False
        
        self.description = ""
        self._myHasDescription=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasEnabled (self):
        return self._myHasEnabled

    def hasDescription (self):
        return self._myHasDescription

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasEnabled=False

        self._myHasDescription=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

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

        return "{ZoneData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ZoneData", 
        "namespace": "zone", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.zones.zone.zone_data_gen import ZoneData"
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
            "namespace": "zones", 
            "isCurrent": false
        }, 
        {
            "namespace": "zone", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
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
            "qwilt_tech_content"
        ]
    }, 
    "createTime": "2013"
}
"""


