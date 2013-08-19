


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class VariableCollectionMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newVariableCollection (self):
        raise NotImplementedError()

    def setVariableCollectionObj (self, key, variableCollectionObj):
        raise NotImplementedError()

    def getVariableCollectionObj (self, key):
        raise NotImplementedError()

    def deleteVariableCollection (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      , linux_
                      
                      , trxContext=None):
        raise NotImplementedError()

    def write (self
               , linux_
               , trxContext=None
               ):
        raise NotImplementedError()

    def read (self
              , linux_
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , linux_
                       
                       , trxContext=None):
        raise NotImplementedError()


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyVariableCollectionMaapi", 
        "name": "variableCollection", 
        "keyLeaf": {
            "varName": "variableCollection", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "variable-collection", 
        "namespace": "variable_collection", 
        "moduleYangNamespacePrefix": "qt-lnx-variables", 
        "className": "VariableCollectionMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable_collection_maapi_list_gen import VariableCollectionMaapiList", 
        "baseClassName": "VariableCollectionMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
        "containerModule": "variable_collection_maapi_gen", 
        "baseModule": "variable_collection_maapi_list_base_gen"
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
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "memberName": "variableList", 
            "yangName": "variable", 
            "className": "BlinkyVariableMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.variable_maapi_list_list_gen import BlinkyVariableMaapiList", 
            "isList": true, 
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
        }
    ], 
    "createTime": "2013"
}
"""


