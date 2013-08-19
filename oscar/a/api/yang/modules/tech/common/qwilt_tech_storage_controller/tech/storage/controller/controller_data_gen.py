


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.qwilt_tech_storage_controller_module_gen import StorageControllerImplementationType


class ControllerData(object):

    def __init__ (self):

        self.implementation = StorageControllerImplementationType.kDellH810
        self._myHasImplementation=False
        
        self.internalId = ""
        self._myHasInternalId=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.implementation=other.implementation
        self._myHasImplementation=other._myHasImplementation
        
        self.internalId=other.internalId
        self._myHasInternalId=other._myHasInternalId
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasImplementation (self):
        return self._myHasImplementation

    def hasInternalId (self):
        return self._myHasInternalId

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasImplementation (self):
        self._myHasImplementation=True

    def setHasInternalId (self):
        self._myHasInternalId=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasImplementation=False

        self._myHasInternalId=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasImplementation:
            x = "+"
        leafStr = str(self.implementation)
        items.append(x + "Implementation="+leafStr)

        x=""
        if self._myHasInternalId:
            x = "+"
        leafStr = str(self.internalId)
        items.append(x + "InternalId="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{ControllerData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ControllerData", 
        "namespace": "controller", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.controller_data_gen import ControllerData"
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
            "namespace": "controller", 
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
            "memberName": "internalId", 
            "yangName": "internal-id", 
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
            "qwilt_tech_storage_controller"
        ]
    }, 
    "createTime": "2013"
}
"""


