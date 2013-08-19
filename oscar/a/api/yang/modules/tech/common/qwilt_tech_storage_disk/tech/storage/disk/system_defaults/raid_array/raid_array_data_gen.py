


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayRaidType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import RaidArrayImplementationType


class RaidArrayData(object):

    def __init__ (self):

        self.osDevice = ""
        self._myHasOsDevice=False
        
        self.implementation = RaidArrayImplementationType.kNone
        self._myHasImplementation=False
        
        self.raidType = RaidArrayRaidType.kNone
        self._myHasRaidType=False
        
        self.name = ""
        self._myHasName=False
        
        self.autoInit = False
        self._myHasAutoInit=False
        

    def copyFrom (self, other):

        self.osDevice=other.osDevice
        self._myHasOsDevice=other._myHasOsDevice
        
        self.implementation=other.implementation
        self._myHasImplementation=other._myHasImplementation
        
        self.raidType=other.raidType
        self._myHasRaidType=other._myHasRaidType
        
        self.name=other.name
        self._myHasName=other._myHasName
        
        self.autoInit=other.autoInit
        self._myHasAutoInit=other._myHasAutoInit
        
    # has...() methods

    def hasOsDevice (self):
        return self._myHasOsDevice

    def hasImplementation (self):
        return self._myHasImplementation

    def hasRaidType (self):
        return self._myHasRaidType

    def hasName (self):
        return self._myHasName

    def hasAutoInit (self):
        return self._myHasAutoInit


    # setHas...() methods

    def setHasOsDevice (self):
        self._myHasOsDevice=True

    def setHasImplementation (self):
        self._myHasImplementation=True

    def setHasRaidType (self):
        self._myHasRaidType=True

    def setHasName (self):
        self._myHasName=True

    def setHasAutoInit (self):
        self._myHasAutoInit=True


    def clearAllHas (self):

        self._myHasOsDevice=False

        self._myHasImplementation=False

        self._myHasRaidType=False

        self._myHasName=False

        self._myHasAutoInit=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasOsDevice:
            x = "+"
        leafStr = str(self.osDevice)
        items.append(x + "OsDevice="+leafStr)

        x=""
        if self._myHasImplementation:
            x = "+"
        leafStr = str(self.implementation)
        items.append(x + "Implementation="+leafStr)

        x=""
        if self._myHasRaidType:
            x = "+"
        leafStr = str(self.raidType)
        items.append(x + "RaidType="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasAutoInit:
            x = "+"
        leafStr = str(self.autoInit)
        items.append(x + "AutoInit="+leafStr)

        return "{RaidArrayData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "RaidArrayData", 
        "namespace": "raid_array", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.raid_array.raid_array_data_gen import RaidArrayData"
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
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "raid_array", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "osDevice", 
            "yangName": "os-device", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "implementation", 
            "yangName": "implementation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "raidType", 
            "yangName": "raid-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "autoInit", 
            "yangName": "auto-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
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
            "qwilt_tech_storage_disk"
        ]
    }, 
    "createTime": "2013"
}
"""


