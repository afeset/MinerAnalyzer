


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class InterfaceMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newInterface (self):
        raise NotImplementedError()

    def setInterfaceObj (self, key, interfaceObj):
        raise NotImplementedError()

    def getInterfaceObj (self, key):
        raise NotImplementedError()

    def deleteInterface (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      , line
                      
                      , trxContext=None):
        raise NotImplementedError()

    def write (self
               , line
               , trxContext=None
               ):
        raise NotImplementedError()

    def read (self
              , line
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , line
                       
                       , trxContext=None):
        raise NotImplementedError()


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyInterfaceMaapi", 
        "name": "interface", 
        "keyLeaf": {
            "varName": "interface", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "interface", 
        "namespace": "interface", 
        "moduleYangNamespacePrefix": "qtc-line", 
        "className": "InterfaceMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.interface.interface_maapi_list_gen import InterfaceMaapiList", 
        "baseClassName": "InterfaceMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
        "containerModule": "interface_maapi_gen", 
        "baseModule": "interface_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": false, 
            "yangName": "line", 
            "namespace": "line", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "line", 
                "yangName": "number", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "dispatcher", 
            "namespace": "dispatcher", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "dispatcher"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": true, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "interface", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.interface.system_defaults.system_defaults_maapi_list_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "type_", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "type_", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
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


