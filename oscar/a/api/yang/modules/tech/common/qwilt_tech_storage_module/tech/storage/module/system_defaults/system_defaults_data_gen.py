


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_storage_module.qwilt_tech_storage_module_module_gen import StorageModuleLocationTypeType


class SystemDefaultsData(object):

    def __init__ (self):

        self.controller = ""
        self._myHasController=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.description = ""
        self._myHasDescription=False
        
        self.locationType = StorageModuleLocationTypeType.kNone
        self._myHasLocationType=False
        

    def copyFrom (self, other):

        self.controller=other.controller
        self._myHasController=other._myHasController
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.locationType=other.locationType
        self._myHasLocationType=other._myHasLocationType
        
    # has...() methods

    def hasController (self):
        return self._myHasController

    def hasEnabled (self):
        return self._myHasEnabled

    def hasDescription (self):
        return self._myHasDescription

    def hasLocationType (self):
        return self._myHasLocationType


    # setHas...() methods

    def setHasController (self):
        self._myHasController=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasLocationType (self):
        self._myHasLocationType=True


    def clearAllHas (self):

        self._myHasController=False

        self._myHasEnabled=False

        self._myHasDescription=False

        self._myHasLocationType=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasController:
            x = "+"
        leafStr = str(self.controller)
        items.append(x + "Controller="+leafStr)

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
        if self._myHasLocationType:
            x = "+"
        leafStr = str(self.locationType)
        items.append(x + "LocationType="+leafStr)

        return "{SystemDefaultsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemDefaultsData", 
        "namespace": "system_defaults", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_module.tech.storage.module.system_defaults.system_defaults_data_gen import SystemDefaultsData"
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
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "controller", 
            "yangName": "controller", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "locationType", 
            "yangName": "location-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
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


