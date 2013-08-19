


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_storage_module.qwilt_tech_storage_module_module_gen import StorageModuleLocationTypeType


class ModuleData(object):

    def __init__ (self):

        self.description = ""
        self._myHasDescription=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.controller = ""
        self._myHasController=False
        
        self.locationType = StorageModuleLocationTypeType.kNone
        self._myHasLocationType=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.controller=other.controller
        self._myHasController=other._myHasController
        
        self.locationType=other.locationType
        self._myHasLocationType=other._myHasLocationType
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasDescription (self):
        return self._myHasDescription

    def hasEnabled (self):
        return self._myHasEnabled

    def hasController (self):
        return self._myHasController

    def hasLocationType (self):
        return self._myHasLocationType

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasController (self):
        self._myHasController=True

    def setHasLocationType (self):
        self._myHasLocationType=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasDescription=False

        self._myHasEnabled=False

        self._myHasController=False

        self._myHasLocationType=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDescription:
            x = "+"
        leafStr = str(self.description)
        items.append(x + "Description="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasController:
            x = "+"
        leafStr = str(self.controller)
        items.append(x + "Controller="+leafStr)

        x=""
        if self._myHasLocationType:
            x = "+"
        leafStr = str(self.locationType)
        items.append(x + "LocationType="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{ModuleData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ModuleData", 
        "namespace": "module", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_module.tech.storage.module.module_data_gen import ModuleData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "storage", 
            "isCurrent": false
        }, 
        {
            "namespace": "module", 
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
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "controller", 
            "yangName": "controller", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "locationType", 
            "yangName": "location-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "common", 
            "qwilt_tech_storage_module"
        ]
    }, 
    "createTime": "2013"
}
"""


