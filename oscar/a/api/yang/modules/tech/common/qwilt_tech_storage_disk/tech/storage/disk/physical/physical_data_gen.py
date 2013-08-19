


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskPhysicalImplementationType


class PhysicalData(object):

    def __init__ (self):

        self.implementation = DiskPhysicalImplementationType.kDirectory
        self._myHasImplementation=False
        
        self.controller = ""
        self._myHasController=False
        
        self.id = ""
        self._myHasId=False
        

    def copyFrom (self, other):

        self.implementation=other.implementation
        self._myHasImplementation=other._myHasImplementation
        
        self.controller=other.controller
        self._myHasController=other._myHasController
        
        self.id=other.id
        self._myHasId=other._myHasId
        
    # has...() methods

    def hasImplementation (self):
        return self._myHasImplementation

    def hasController (self):
        return self._myHasController

    def hasId (self):
        return self._myHasId


    # setHas...() methods

    def setHasImplementation (self):
        self._myHasImplementation=True

    def setHasController (self):
        self._myHasController=True

    def setHasId (self):
        self._myHasId=True


    def clearAllHas (self):

        self._myHasImplementation=False

        self._myHasController=False

        self._myHasId=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasImplementation:
            x = "+"
        leafStr = str(self.implementation)
        items.append(x + "Implementation="+leafStr)

        x=""
        if self._myHasController:
            x = "+"
        leafStr = str(self.controller)
        items.append(x + "Controller="+leafStr)

        x=""
        if self._myHasId:
            x = "+"
        leafStr = str(self.id)
        items.append(x + "Id="+leafStr)

        return "{PhysicalData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "PhysicalData", 
        "namespace": "physical", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.physical_data_gen import PhysicalData"
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
            "namespace": "disk", 
            "isCurrent": false
        }, 
        {
            "namespace": "physical", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "implementation", 
            "yangName": "implementation", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "qwilt_tech_storage_disk"
        ]
    }, 
    "createTime": "2013"
}
"""


