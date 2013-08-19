


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class DeviceData(object):

    def __init__ (self):

        self.id = ""
        self._myHasId=False
        
        self.fruId = ""
        self._myHasFruId=False
        

    def copyFrom (self, other):

        self.id=other.id
        self._myHasId=other._myHasId
        
        self.fruId=other.fruId
        self._myHasFruId=other._myHasFruId
        
    # has...() methods

    def hasId (self):
        return self._myHasId

    def hasFruId (self):
        return self._myHasFruId


    # setHas...() methods

    def setHasId (self):
        self._myHasId=True

    def setHasFruId (self):
        self._myHasFruId=True


    def clearAllHas (self):

        self._myHasId=False

        self._myHasFruId=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasId:
            x = "+"
        leafStr = str(self.id)
        items.append(x + "Id="+leafStr)

        x=""
        if self._myHasFruId:
            x = "+"
        leafStr = str(self.fruId)
        items.append(x + "FruId="+leafStr)

        return "{DeviceData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DeviceData", 
        "namespace": "device", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.system_defaults.device.device_data_gen import DeviceData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "platform", 
            "isCurrent": false
        }, 
        {
            "namespace": "power", 
            "isCurrent": false
        }, 
        {
            "namespace": "power_supply", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "device", 
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
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "fruId", 
            "yangName": "fru-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "qwilt_tech_platform_power"
        ]
    }, 
    "createTime": "2013"
}
"""


