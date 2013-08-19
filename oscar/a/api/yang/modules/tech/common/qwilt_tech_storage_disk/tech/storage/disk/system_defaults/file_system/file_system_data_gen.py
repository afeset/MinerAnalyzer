


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import FileSystemTypeType


class FileSystemData(object):

    def __init__ (self):

        self.autoInit = False
        self._myHasAutoInit=False
        
        self.checkUuid = False
        self._myHasCheckUuid=False
        
        self.readAhead = 0
        self._myHasReadAhead=False
        
        self.fileSystemType = FileSystemTypeType.kNone
        self._myHasFileSystemType=False
        

    def copyFrom (self, other):

        self.autoInit=other.autoInit
        self._myHasAutoInit=other._myHasAutoInit
        
        self.checkUuid=other.checkUuid
        self._myHasCheckUuid=other._myHasCheckUuid
        
        self.readAhead=other.readAhead
        self._myHasReadAhead=other._myHasReadAhead
        
        self.fileSystemType=other.fileSystemType
        self._myHasFileSystemType=other._myHasFileSystemType
        
    # has...() methods

    def hasAutoInit (self):
        return self._myHasAutoInit

    def hasCheckUuid (self):
        return self._myHasCheckUuid

    def hasReadAhead (self):
        return self._myHasReadAhead

    def hasFileSystemType (self):
        return self._myHasFileSystemType


    # setHas...() methods

    def setHasAutoInit (self):
        self._myHasAutoInit=True

    def setHasCheckUuid (self):
        self._myHasCheckUuid=True

    def setHasReadAhead (self):
        self._myHasReadAhead=True

    def setHasFileSystemType (self):
        self._myHasFileSystemType=True


    def clearAllHas (self):

        self._myHasAutoInit=False

        self._myHasCheckUuid=False

        self._myHasReadAhead=False

        self._myHasFileSystemType=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasAutoInit:
            x = "+"
        leafStr = str(self.autoInit)
        items.append(x + "AutoInit="+leafStr)

        x=""
        if self._myHasCheckUuid:
            x = "+"
        leafStr = str(self.checkUuid)
        items.append(x + "CheckUuid="+leafStr)

        x=""
        if self._myHasReadAhead:
            x = "+"
        leafStr = str(self.readAhead)
        items.append(x + "ReadAhead="+leafStr)

        x=""
        if self._myHasFileSystemType:
            x = "+"
        leafStr = str(self.fileSystemType)
        items.append(x + "FileSystemType="+leafStr)

        return "{FileSystemData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "FileSystemData", 
        "namespace": "file_system", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.file_system.file_system_data_gen import FileSystemData"
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
            "namespace": "file_system", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "autoInit", 
            "yangName": "auto-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "checkUuid", 
            "yangName": "check-uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "readAhead", 
            "yangName": "read-ahead", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "fileSystemType", 
            "yangName": "file-system-type", 
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
            "qwilt_tech_storage_disk"
        ]
    }, 
    "createTime": "2013"
}
"""


