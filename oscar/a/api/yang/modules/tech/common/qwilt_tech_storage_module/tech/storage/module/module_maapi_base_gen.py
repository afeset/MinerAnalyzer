


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ModuleMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , module
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , module
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , module
                       
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

    # actual
    def newActual (self):
        raise NotImplementedError()

    def setActualObj (self, obj):
        raise NotImplementedError()

    def getActualObj (self):
        raise NotImplementedError()

    def hasActual (self):
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




    # config leaves

    # description
    def requestDescription (self, requested):
        raise NotImplementedError()

    def isDescriptionRequested (self):
        raise NotImplementedError()

    def getDescription (self):
        raise NotImplementedError()

    def hasDescription (self):
        raise NotImplementedError()

    def setDescription (self, description):
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

    # controller
    def requestController (self, requested):
        raise NotImplementedError()

    def isControllerRequested (self):
        raise NotImplementedError()

    def getController (self):
        raise NotImplementedError()

    def hasController (self):
        raise NotImplementedError()

    def setController (self, controller):
        raise NotImplementedError()

    # locationType
    def requestLocationType (self, requested):
        raise NotImplementedError()

    def isLocationTypeRequested (self):
        raise NotImplementedError()

    def getLocationType (self):
        raise NotImplementedError()

    def hasLocationType (self):
        raise NotImplementedError()

    def setLocationType (self, locationType):
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






"""
Extracted from the below data: 
{
    "node": {
        "name": "module", 
        "namespace": "module", 
        "className": "ModuleMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_module.tech.storage.module.module_maapi_gen import ModuleMaapi", 
        "baseClassName": "ModuleMaapiBase", 
        "baseModule": "module_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "isCurrent": true, 
            "yangName": "module", 
            "namespace": "module", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "keyLeaf": {
                "varName": "module", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "module"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_module.tech.storage.module.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "memberName": "actual", 
            "yangName": "actual", 
            "className": "BlinkyActualMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_module.tech.storage.module.actual.actual_maapi_gen import BlinkyActualMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_module.tech.storage.module.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "controller", 
            "yangName": "controller", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "locationType", 
            "yangName": "location-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "qwilt_tech_storage_module"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "controller", 
            "yangName": "controller", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "locationType", 
            "yangName": "location-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


