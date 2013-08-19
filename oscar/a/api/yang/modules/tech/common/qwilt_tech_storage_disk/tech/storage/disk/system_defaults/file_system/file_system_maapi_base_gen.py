


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class FileSystemMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , disk
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , disk
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , disk
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # commands
    def newCommands (self):
        raise NotImplementedError()

    def setCommandsObj (self, obj):
        raise NotImplementedError()

    def getCommandsObj (self):
        raise NotImplementedError()

    def hasCommands (self):
        raise NotImplementedError()

    # timeouts
    def newTimeouts (self):
        raise NotImplementedError()

    def setTimeoutsObj (self, obj):
        raise NotImplementedError()

    def getTimeoutsObj (self):
        raise NotImplementedError()

    def hasTimeouts (self):
        raise NotImplementedError()




    # config leaves

    # autoInit
    def requestAutoInit (self, requested):
        raise NotImplementedError()

    def isAutoInitRequested (self):
        raise NotImplementedError()

    def getAutoInit (self):
        raise NotImplementedError()

    def hasAutoInit (self):
        raise NotImplementedError()

    def setAutoInit (self, autoInit):
        raise NotImplementedError()

    # checkUuid
    def requestCheckUuid (self, requested):
        raise NotImplementedError()

    def isCheckUuidRequested (self):
        raise NotImplementedError()

    def getCheckUuid (self):
        raise NotImplementedError()

    def hasCheckUuid (self):
        raise NotImplementedError()

    def setCheckUuid (self, checkUuid):
        raise NotImplementedError()

    # readAhead
    def requestReadAhead (self, requested):
        raise NotImplementedError()

    def isReadAheadRequested (self):
        raise NotImplementedError()

    def getReadAhead (self):
        raise NotImplementedError()

    def hasReadAhead (self):
        raise NotImplementedError()

    def setReadAhead (self, readAhead):
        raise NotImplementedError()

    # fileSystemType
    def requestFileSystemType (self, requested):
        raise NotImplementedError()

    def isFileSystemTypeRequested (self):
        raise NotImplementedError()

    def getFileSystemType (self):
        raise NotImplementedError()

    def hasFileSystemType (self):
        raise NotImplementedError()

    def setFileSystemType (self, fileSystemType):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "fileSystem", 
        "namespace": "file_system", 
        "className": "FileSystemMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.file_system.file_system_maapi_gen import FileSystemMaapi", 
        "baseClassName": "FileSystemMaapiBase", 
        "baseModule": "file_system_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "isCurrent": false, 
            "yangName": "disk", 
            "namespace": "disk", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "keyLeaf": {
                "varName": "disk", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "yangName": "file-system", 
            "namespace": "file_system", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "name": "file-system"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "commands", 
            "yangName": "commands", 
            "className": "BlinkyCommandsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.file_system.commands.commands_maapi_gen import BlinkyCommandsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "timeouts", 
            "yangName": "timeouts", 
            "className": "BlinkyTimeoutsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.file_system.timeouts.timeouts_maapi_gen import BlinkyTimeoutsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "autoInit", 
            "yangName": "auto-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "checkUuid", 
            "yangName": "check-uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readAhead", 
            "yangName": "read-ahead", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "fileSystemType", 
            "yangName": "file-system-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }
    ], 
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
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "autoInit", 
            "yangName": "auto-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "checkUuid", 
            "yangName": "check-uuid", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "readAhead", 
            "yangName": "read-ahead", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "fileSystemType", 
            "yangName": "file-system-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


