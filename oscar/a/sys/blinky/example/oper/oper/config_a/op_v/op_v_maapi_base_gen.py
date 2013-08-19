


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class OpVMaapiBase(object):
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



    # descendants

    # opY
    def newOpY (self):
        raise NotImplementedError()

    def setOpYObj (self, obj):
        raise NotImplementedError()

    def getOpYObj (self):
        raise NotImplementedError()

    def hasOpY (self):
        raise NotImplementedError()

    # opW
    def newOpW (self):
        raise NotImplementedError()

    def setOpWObj (self, obj):
        raise NotImplementedError()

    def getOpWObj (self):
        raise NotImplementedError()

    def hasOpW (self):
        raise NotImplementedError()






    # oper leaves

    # valueOpV1
    def requestValueOpV1 (self, requested):
        raise NotImplementedError()

    def isValueOpV1Requested (self):
        raise NotImplementedError()

    def getValueOpV1 (self):
        raise NotImplementedError()

    def hasValueOpV1 (self):
        raise NotImplementedError()

    def setValueOpV1 (self, valueOpV1):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "opV", 
        "namespace": "op_v", 
        "className": "OpVMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_v_maapi_gen import OpVMaapi", 
        "baseClassName": "OpVMaapiBase", 
        "baseModule": "op_v_maapi_base_gen"
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
                "defaultVal": null, 
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
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.op_y_maapi_gen import BlinkyOpYMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opW", 
            "yangName": "op-w", 
            "className": "BlinkyOpWMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_w.op_w_maapi_gen import BlinkyOpWMaapi", 
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


