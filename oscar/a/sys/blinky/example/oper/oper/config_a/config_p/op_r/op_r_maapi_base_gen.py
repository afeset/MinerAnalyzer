


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class OpRMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , configP
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , configP
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , configP
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # opValueR
    def requestOpValueR (self, requested):
        raise NotImplementedError()

    def isOpValueRRequested (self):
        raise NotImplementedError()

    def getOpValueR (self):
        raise NotImplementedError()

    def hasOpValueR (self):
        raise NotImplementedError()

    def setOpValueR (self, opValueR):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "opR", 
        "namespace": "op_r", 
        "className": "OpRMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.op_r.op_r_maapi_gen import OpRMaapi", 
        "baseClassName": "OpRMaapiBase", 
        "baseModule": "op_r_maapi_base_gen"
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
            "yangName": "config-p", 
            "namespace": "config_p", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "keyLeaf": {
                "varName": "configP", 
                "defaultVal": null, 
                "typeHandler": "handler: IntHandler"
            }, 
            "name": "config-p"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "op-r", 
            "namespace": "op_r", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-r"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opValueR", 
            "yangName": "op-value-r", 
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
            "memberName": "opValueR", 
            "yangName": "op-value-r", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


