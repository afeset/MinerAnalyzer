


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ConfigPMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newConfigP (self):
        raise NotImplementedError()

    def setConfigPObj (self, key, configPObj):
        raise NotImplementedError()

    def getConfigPObj (self, key):
        raise NotImplementedError()

    def deleteConfigP (self, key):
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
        "containerClassName": "BlinkyConfigPMaapi", 
        "name": "configP", 
        "keyLeaf": {
            "varName": "configP", 
            "yangName": "id", 
            "typeHandler": "handler: IntHandler"
        }, 
        "yangName": "config-p", 
        "namespace": "config_p", 
        "moduleYangNamespacePrefix": "oper", 
        "className": "ConfigPMaapiList", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.config_p_maapi_list_gen import ConfigPMaapiList", 
        "baseClassName": "ConfigPMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/oper", 
        "containerModule": "config_p_maapi_gen", 
        "baseModule": "config_p_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "config-a", 
            "namespace": "config_a", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "config-a"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "isCurrent": true, 
            "yangName": "config-p", 
            "namespace": "config_p", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "keyLeaf": {
                "varName": "configP", 
                "yangName": "id", 
                "typeHandler": "handler: IntHandler"
            }, 
            "name": "config-p"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opR", 
            "yangName": "op-r", 
            "className": "BlinkyOpRMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.op_r.op_r_maapi_list_gen import BlinkyOpRMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "oper", 
            "oper"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


