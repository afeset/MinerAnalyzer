


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SystemDefaultsMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , controller
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , controller
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , controller
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

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

    # implementation
    def requestImplementation (self, requested):
        raise NotImplementedError()

    def isImplementationRequested (self):
        raise NotImplementedError()

    def getImplementation (self):
        raise NotImplementedError()

    def hasImplementation (self):
        raise NotImplementedError()

    def setImplementation (self, implementation):
        raise NotImplementedError()

    # internalId
    def requestInternalId (self, requested):
        raise NotImplementedError()

    def isInternalIdRequested (self):
        raise NotImplementedError()

    def getInternalId (self):
        raise NotImplementedError()

    def hasInternalId (self):
        raise NotImplementedError()

    def setInternalId (self, internalId):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
        "baseClassName": "SystemDefaultsMaapiBase", 
        "baseModule": "system_defaults_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "isCurrent": false, 
            "yangName": "controller", 
            "namespace": "controller", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "keyLeaf": {
                "varName": "controller", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "controller"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "memberName": "timeouts", 
            "yangName": "timeouts", 
            "className": "BlinkyTimeoutsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.system_defaults.timeouts.timeouts_maapi_gen import BlinkyTimeoutsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "implementation", 
            "yangName": "implementation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "internalId", 
            "yangName": "internal-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "qwilt_tech_storage_controller"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "implementation", 
            "yangName": "implementation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "internalId", 
            "yangName": "internal-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


