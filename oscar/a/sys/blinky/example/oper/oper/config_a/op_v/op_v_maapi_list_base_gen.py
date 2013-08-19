


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class OpVMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newOpV (self):
        raise NotImplementedError()

    def setOpVObj (self, key, opVObj):
        raise NotImplementedError()

    def getOpVObj (self, key):
        raise NotImplementedError()

    def deleteOpV (self, key):
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
        "containerClassName": "BlinkyOpVMaapi", 
        "name": "opV", 
        "keyLeaf": {
            "varName": "opV", 
            "yangName": "value-op-v1", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "op-v", 
        "namespace": "op_v", 
        "moduleYangNamespacePrefix": "oper", 
        "className": "OpVMaapiList", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_v_maapi_list_gen import OpVMaapiList", 
        "baseClassName": "OpVMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/oper", 
        "containerModule": "op_v_maapi_gen", 
        "baseModule": "op_v_maapi_list_base_gen"
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
            "yangName": "op-v", 
            "namespace": "op_v", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "keyLeaf": {
                "varName": "opV", 
                "yangName": "value-op-v1", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "op-v"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opY", 
            "yangName": "op-y", 
            "className": "BlinkyOpYMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.op_y_maapi_list_gen import BlinkyOpYMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opW", 
            "yangName": "op-w", 
            "className": "BlinkyOpWMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_w.op_w_maapi_list_gen import BlinkyOpWMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpV1", 
            "yangName": "value-op-v1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpV1", 
            "yangName": "value-op-v1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


