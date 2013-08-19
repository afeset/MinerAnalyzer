


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskTypesType
from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import DiskFunctionalTypesType


class DiskData(object):

    def __init__ (self):

        self.diskType = DiskTypesType.kRaid0Disk
        self._myHasDiskType=False
        
        self.name = ""
        self._myHasName=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.functionalType = DiskFunctionalTypesType.kContent
        self._myHasFunctionalType=False
        
        self.storageModule = ""
        self._myHasStorageModule=False
        
        self.tmpForceInit = False
        self._myHasTmpForceInit=False
        

    def copyFrom (self, other):

        self.diskType=other.diskType
        self._myHasDiskType=other._myHasDiskType
        
        self.name=other.name
        self._myHasName=other._myHasName
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.functionalType=other.functionalType
        self._myHasFunctionalType=other._myHasFunctionalType
        
        self.storageModule=other.storageModule
        self._myHasStorageModule=other._myHasStorageModule
        
        self.tmpForceInit=other.tmpForceInit
        self._myHasTmpForceInit=other._myHasTmpForceInit
        
    # has...() methods

    def hasDiskType (self):
        return self._myHasDiskType

    def hasName (self):
        return self._myHasName

    def hasEnabled (self):
        return self._myHasEnabled

    def hasFunctionalType (self):
        return self._myHasFunctionalType

    def hasStorageModule (self):
        return self._myHasStorageModule

    def hasTmpForceInit (self):
        return self._myHasTmpForceInit


    # setHas...() methods

    def setHasDiskType (self):
        self._myHasDiskType=True

    def setHasName (self):
        self._myHasName=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasFunctionalType (self):
        self._myHasFunctionalType=True

    def setHasStorageModule (self):
        self._myHasStorageModule=True

    def setHasTmpForceInit (self):
        self._myHasTmpForceInit=True


    def clearAllHas (self):

        self._myHasDiskType=False

        self._myHasName=False

        self._myHasEnabled=False

        self._myHasFunctionalType=False

        self._myHasStorageModule=False

        self._myHasTmpForceInit=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDiskType:
            x = "+"
        leafStr = str(self.diskType)
        items.append(x + "DiskType="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasFunctionalType:
            x = "+"
        leafStr = str(self.functionalType)
        items.append(x + "FunctionalType="+leafStr)

        x=""
        if self._myHasStorageModule:
            x = "+"
        leafStr = str(self.storageModule)
        items.append(x + "StorageModule="+leafStr)

        x=""
        if self._myHasTmpForceInit:
            x = "+"
        leafStr = str(self.tmpForceInit)
        items.append(x + "TmpForceInit="+leafStr)

        return "{DiskData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DiskData", 
        "namespace": "disk", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.disk_data_gen import DiskData"
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
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "diskType", 
            "yangName": "disk-type", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "functionalType", 
            "yangName": "functional-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "storageModule", 
            "yangName": "storage-module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "tmpForceInit", 
            "yangName": "tmp-force-init", 
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


