


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ControllerMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newController (self):
        raise NotImplementedError()

    def setControllerObj (self, key, controllerObj):
        raise NotImplementedError()

    def getControllerObj (self, key):
        raise NotImplementedError()

    def deleteController (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      
                      , trxContext=None):
        raise NotImplementedError()

    def write (self
               , trxContext=None
               ):
        raise NotImplementedError()

    def read (self
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       
                       , trxContext=None):
        raise NotImplementedError()


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyControllerMaapi", 
        "name": "controller", 
        "keyLeaf": {
            "varName": "controller", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "controller", 
        "namespace": "controller", 
        "moduleYangNamespacePrefix": "qt-strg-ctrl", 
        "className": "ControllerMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.controller_maapi_list_gen import ControllerMaapiList", 
        "baseClassName": "ControllerMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
        "containerModule": "controller_maapi_gen", 
        "baseModule": "controller_maapi_list_base_gen"
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
            "isCurrent": true, 
            "yangName": "controller", 
            "namespace": "controller", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "keyLeaf": {
                "varName": "controller", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "controller"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "memberName": "timeouts", 
            "yangName": "timeouts", 
            "className": "BlinkyTimeoutsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.timeouts.timeouts_maapi_list_gen import BlinkyTimeoutsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.system_defaults.system_defaults_maapi_list_gen import BlinkySystemDefaultsMaapi", 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "internalId", 
            "yangName": "internal-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "internalId", 
            "yangName": "internal-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
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


