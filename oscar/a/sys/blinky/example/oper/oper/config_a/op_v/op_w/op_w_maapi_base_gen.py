


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class OpWMaapiBase(object):
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

    # opWValue
    def requestOpWValue (self, requested):
        raise NotImplementedError()

    def isOpWValueRequested (self):
        raise NotImplementedError()

    def getOpWValue (self):
        raise NotImplementedError()

    def hasOpWValue (self):
        raise NotImplementedError()

    def setOpWValue (self, opWValue):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "opW", 
        "namespace": "op_w", 
        "className": "OpWMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_w.op_w_maapi_gen import OpWMaapi", 
        "baseClassName": "OpWMaapiBase", 
        "baseModule": "op_w_maapi_base_gen"
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
            "yangName": "op-w", 
            "namespace": "op_w", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-w"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opWValue", 
            "yangName": "op-w-value", 
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
            "memberName": "opWValue", 
            "yangName": "op-w-value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


