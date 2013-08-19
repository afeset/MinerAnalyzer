


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class CommandsData(object):

    def __init__ (self):

        self.postMount = ""
        self._myHasPostMount=False
        
        self.preMountExtras = ""
        self._myHasPreMountExtras=False
        
        self.preMount = ""
        self._myHasPreMount=False
        
        self.postMountExtras = ""
        self._myHasPostMountExtras=False
        
        self.mkfs = ""
        self._myHasMkfs=False
        
        self.mkfsExtras = ""
        self._myHasMkfsExtras=False
        
        self.mountExtras = ""
        self._myHasMountExtras=False
        
        self.mount = ""
        self._myHasMount=False
        

    def copyFrom (self, other):

        self.postMount=other.postMount
        self._myHasPostMount=other._myHasPostMount
        
        self.preMountExtras=other.preMountExtras
        self._myHasPreMountExtras=other._myHasPreMountExtras
        
        self.preMount=other.preMount
        self._myHasPreMount=other._myHasPreMount
        
        self.postMountExtras=other.postMountExtras
        self._myHasPostMountExtras=other._myHasPostMountExtras
        
        self.mkfs=other.mkfs
        self._myHasMkfs=other._myHasMkfs
        
        self.mkfsExtras=other.mkfsExtras
        self._myHasMkfsExtras=other._myHasMkfsExtras
        
        self.mountExtras=other.mountExtras
        self._myHasMountExtras=other._myHasMountExtras
        
        self.mount=other.mount
        self._myHasMount=other._myHasMount
        
    # has...() methods

    def hasPostMount (self):
        return self._myHasPostMount

    def hasPreMountExtras (self):
        return self._myHasPreMountExtras

    def hasPreMount (self):
        return self._myHasPreMount

    def hasPostMountExtras (self):
        return self._myHasPostMountExtras

    def hasMkfs (self):
        return self._myHasMkfs

    def hasMkfsExtras (self):
        return self._myHasMkfsExtras

    def hasMountExtras (self):
        return self._myHasMountExtras

    def hasMount (self):
        return self._myHasMount


    # setHas...() methods

    def setHasPostMount (self):
        self._myHasPostMount=True

    def setHasPreMountExtras (self):
        self._myHasPreMountExtras=True

    def setHasPreMount (self):
        self._myHasPreMount=True

    def setHasPostMountExtras (self):
        self._myHasPostMountExtras=True

    def setHasMkfs (self):
        self._myHasMkfs=True

    def setHasMkfsExtras (self):
        self._myHasMkfsExtras=True

    def setHasMountExtras (self):
        self._myHasMountExtras=True

    def setHasMount (self):
        self._myHasMount=True


    def clearAllHas (self):

        self._myHasPostMount=False

        self._myHasPreMountExtras=False

        self._myHasPreMount=False

        self._myHasPostMountExtras=False

        self._myHasMkfs=False

        self._myHasMkfsExtras=False

        self._myHasMountExtras=False

        self._myHasMount=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasPostMount:
            x = "+"
        leafStr = str(self.postMount)
        items.append(x + "PostMount="+leafStr)

        x=""
        if self._myHasPreMountExtras:
            x = "+"
        leafStr = str(self.preMountExtras)
        items.append(x + "PreMountExtras="+leafStr)

        x=""
        if self._myHasPreMount:
            x = "+"
        leafStr = str(self.preMount)
        items.append(x + "PreMount="+leafStr)

        x=""
        if self._myHasPostMountExtras:
            x = "+"
        leafStr = str(self.postMountExtras)
        items.append(x + "PostMountExtras="+leafStr)

        x=""
        if self._myHasMkfs:
            x = "+"
        leafStr = str(self.mkfs)
        items.append(x + "Mkfs="+leafStr)

        x=""
        if self._myHasMkfsExtras:
            x = "+"
        leafStr = str(self.mkfsExtras)
        items.append(x + "MkfsExtras="+leafStr)

        x=""
        if self._myHasMountExtras:
            x = "+"
        leafStr = str(self.mountExtras)
        items.append(x + "MountExtras="+leafStr)

        x=""
        if self._myHasMount:
            x = "+"
        leafStr = str(self.mount)
        items.append(x + "Mount="+leafStr)

        return "{CommandsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "CommandsData", 
        "namespace": "commands", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.file_system.commands.commands_data_gen import CommandsData"
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
            "isCurrent": false
        }, 
        {
            "namespace": "commands", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "postMount", 
            "yangName": "post-mount", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "preMountExtras", 
            "yangName": "pre-mount-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "preMount", 
            "yangName": "pre-mount", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "postMountExtras", 
            "yangName": "post-mount-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "mkfs", 
            "yangName": "mkfs", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "mkfsExtras", 
            "yangName": "mkfs-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "mountExtras", 
            "yangName": "mount-extras", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "mount", 
            "yangName": "mount", 
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
            "qwilt_tech_storage_disk"
        ]
    }, 
    "createTime": "2013"
}
"""


