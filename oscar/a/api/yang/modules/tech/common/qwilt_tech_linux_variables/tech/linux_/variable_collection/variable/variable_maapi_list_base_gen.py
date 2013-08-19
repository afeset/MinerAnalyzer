


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class VariableMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newVariable (self):
        raise NotImplementedError()

    def setVariableObj (self, key, variableObj):
        raise NotImplementedError()

    def getVariableObj (self, key):
        raise NotImplementedError()

    def deleteVariable (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      , linux_
                      , variableCollection
                      
                      , trxContext=None):
        raise NotImplementedError()

    def write (self
               , linux_
               , variableCollection
               , trxContext=None
               ):
        raise NotImplementedError()

    def read (self
              , linux_
              , variableCollection
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , linux_
                       , variableCollection
                       
                       , trxContext=None):
        raise NotImplementedError()


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyVariableMaapi", 
        "name": "variable", 
        "keyLeaf": {
            "varName": "variable", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "variable", 
        "namespace": "variable", 
        "moduleYangNamespacePrefix": "qt-lnx-variables", 
        "className": "VariableMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.variable_maapi_list_gen import VariableMaapiList", 
        "baseClassName": "VariableMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
        "containerModule": "variable_maapi_gen", 
        "baseModule": "variable_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qt-lnx", 
            "isCurrent": false, 
            "yangName": "linux", 
            "namespace": "linux_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux", 
            "keyLeaf": {
                "varName": "linux_", 
                "yangName": "instance", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "linux_"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "isCurrent": false, 
            "yangName": "variable-collection", 
            "namespace": "variable_collection", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "keyLeaf": {
                "varName": "variableCollection", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "variable-collection"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "isCurrent": true, 
            "yangName": "variable", 
            "namespace": "variable", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "keyLeaf": {
                "varName": "variable", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "variable"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.status.status_maapi_list_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.system_defaults.system_defaults_maapi_list_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "systemProtected", 
            "yangName": "system-protected", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "initPhase", 
            "yangName": "init-phase", 
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
            "qwilt_tech_linux_variables"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "systemProtected", 
            "yangName": "system-protected", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "initPhase", 
            "yangName": "init-phase", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


