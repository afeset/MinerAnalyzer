


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class DiskMaapiBase(object):
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

    # status
    def newStatus (self):
        raise NotImplementedError()

    def setStatusObj (self, obj):
        raise NotImplementedError()

    def getStatusObj (self):
        raise NotImplementedError()

    def hasStatus (self):
        raise NotImplementedError()

    # systemDefaults
    def newSystemDefaults (self):
        raise NotImplementedError()

    def setSystemDefaultsObj (self, obj):
        raise NotImplementedError()

    def getSystemDefaultsObj (self):
        raise NotImplementedError()

    def hasSystemDefaults (self):
        raise NotImplementedError()

    # raidArray
    def newRaidArray (self):
        raise NotImplementedError()

    def setRaidArrayObj (self, obj):
        raise NotImplementedError()

    def getRaidArrayObj (self):
        raise NotImplementedError()

    def hasRaidArray (self):
        raise NotImplementedError()

    # alarms
    def newAlarms (self):
        raise NotImplementedError()

    def setAlarmsObj (self, obj):
        raise NotImplementedError()

    def getAlarmsObj (self):
        raise NotImplementedError()

    def hasAlarms (self):
        raise NotImplementedError()

    # fileSystem
    def newFileSystem (self):
        raise NotImplementedError()

    def setFileSystemObj (self, obj):
        raise NotImplementedError()

    def getFileSystemObj (self):
        raise NotImplementedError()

    def hasFileSystem (self):
        raise NotImplementedError()

    # physical
    def newPhysical (self):
        raise NotImplementedError()

    def setPhysicalObj (self, obj):
        raise NotImplementedError()

    def getPhysicalObj (self):
        raise NotImplementedError()

    def hasPhysical (self):
        raise NotImplementedError()




    # config leaves

    # diskType
    def requestDiskType (self, requested):
        raise NotImplementedError()

    def isDiskTypeRequested (self):
        raise NotImplementedError()

    def getDiskType (self):
        raise NotImplementedError()

    def hasDiskType (self):
        raise NotImplementedError()

    def setDiskType (self, diskType):
        raise NotImplementedError()

    # name
    def requestName (self, requested):
        raise NotImplementedError()

    def isNameRequested (self):
        raise NotImplementedError()

    def getName (self):
        raise NotImplementedError()

    def hasName (self):
        raise NotImplementedError()

    def setName (self, name):
        raise NotImplementedError()

    # enabled
    def requestEnabled (self, requested):
        raise NotImplementedError()

    def isEnabledRequested (self):
        raise NotImplementedError()

    def getEnabled (self):
        raise NotImplementedError()

    def hasEnabled (self):
        raise NotImplementedError()

    def setEnabled (self, enabled):
        raise NotImplementedError()

    # functionalType
    def requestFunctionalType (self, requested):
        raise NotImplementedError()

    def isFunctionalTypeRequested (self):
        raise NotImplementedError()

    def getFunctionalType (self):
        raise NotImplementedError()

    def hasFunctionalType (self):
        raise NotImplementedError()

    def setFunctionalType (self, functionalType):
        raise NotImplementedError()

    # storageModule
    def requestStorageModule (self, requested):
        raise NotImplementedError()

    def isStorageModuleRequested (self):
        raise NotImplementedError()

    def getStorageModule (self):
        raise NotImplementedError()

    def hasStorageModule (self):
        raise NotImplementedError()

    def setStorageModule (self, storageModule):
        raise NotImplementedError()

    # tmpForceInit
    def requestTmpForceInit (self, requested):
        raise NotImplementedError()

    def isTmpForceInitRequested (self):
        raise NotImplementedError()

    def getTmpForceInit (self):
        raise NotImplementedError()

    def hasTmpForceInit (self):
        raise NotImplementedError()

    def setTmpForceInit (self, tmpForceInit):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "disk", 
        "namespace": "disk", 
        "className": "DiskMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.disk_maapi_gen import DiskMaapi", 
        "baseClassName": "DiskMaapiBase", 
        "baseModule": "disk_maapi_base_gen"
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
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "raidArray", 
            "yangName": "raid-array", 
            "className": "BlinkyRaidArrayMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.raid_array_maapi_gen import BlinkyRaidArrayMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "alarms", 
            "yangName": "alarms", 
            "className": "BlinkyAlarmsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.alarms.alarms_maapi_gen import BlinkyAlarmsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "fileSystem", 
            "yangName": "file-system", 
            "className": "BlinkyFileSystemMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.file_system_maapi_gen import BlinkyFileSystemMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "memberName": "physical", 
            "yangName": "physical", 
            "className": "BlinkyPhysicalMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.physical_maapi_gen import BlinkyPhysicalMaapi", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "diskType", 
            "yangName": "disk-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "functionalType", 
            "yangName": "functional-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "storageModule", 
            "yangName": "storage-module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "tmpForceInit", 
            "yangName": "tmp-force-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "diskType", 
            "yangName": "disk-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "functionalType", 
            "yangName": "functional-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "storageModule", 
            "yangName": "storage-module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-disk", 
            "moduleYangNamespacePrefix": "qt-strg-dsk", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "tmpForceInit", 
            "yangName": "tmp-force-init", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


