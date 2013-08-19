


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType


class SimulateData(object):

    def __init__ (self):

        self.id = ""
        self._myHasId=False
        
        self.name = AlarmNameType.kTemperatureSensorWarning
        self._myHasName=False
        
        self.entity = ""
        self._myHasEntity=False
        

    def copyFrom (self, other):

        self.id=other.id
        self._myHasId=other._myHasId
        
        self.name=other.name
        self._myHasName=other._myHasName
        
        self.entity=other.entity
        self._myHasEntity=other._myHasEntity
        
    # has...() methods

    def hasId (self):
        return self._myHasId

    def hasName (self):
        return self._myHasName

    def hasEntity (self):
        return self._myHasEntity


    # setHas...() methods

    def setHasId (self):
        self._myHasId=True

    def setHasName (self):
        self._myHasName=True

    def setHasEntity (self):
        self._myHasEntity=True


    def clearAllHas (self):

        self._myHasId=False

        self._myHasName=False

        self._myHasEntity=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasId:
            x = "+"
        leafStr = str(self.id)
        items.append(x + "Id="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasEntity:
            x = "+"
        leafStr = str(self.entity)
        items.append(x + "Entity="+leafStr)

        return "{SimulateData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SimulateData", 
        "namespace": "simulate", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.simulate.simulate_data_gen import SimulateData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "system", 
            "isCurrent": false
        }, 
        {
            "namespace": "alarms", 
            "isCurrent": false
        }, 
        {
            "namespace": "simulate", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "entity", 
            "yangName": "entity", 
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
            "qwilt_tech_system_alarms"
        ]
    }, 
    "createTime": "2013"
}
"""


