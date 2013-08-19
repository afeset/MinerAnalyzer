


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class OpYMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , opV
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , opV
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , opV
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # valueOpY1
    def requestValueOpY1 (self, requested):
        raise NotImplementedError()

    def isValueOpY1Requested (self):
        raise NotImplementedError()

    def getValueOpY1 (self):
        raise NotImplementedError()

    def hasValueOpY1 (self):
        raise NotImplementedError()

    def setValueOpY1 (self, valueOpY1):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "opY", 
        "namespace": "op_y", 
        "className": "OpYMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.op_y_maapi_gen import OpYMaapi", 
        "baseClassName": "OpYMaapiBase", 
        "baseModule": "op_y_maapi_base_gen"
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
            "isCurrent": false, 
            "yangName": "op-v", 
            "namespace": "op_v", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "keyLeaf": {
                "varName": "opV", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "op-v"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "op-y", 
            "namespace": "op_y", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-y"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpY1", 
            "yangName": "value-op-y1", 
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
            "memberName": "valueOpY1", 
            "yangName": "value-op-y1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


