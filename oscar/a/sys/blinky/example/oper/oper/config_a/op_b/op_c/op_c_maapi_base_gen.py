


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class OpCMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , opC
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , opC
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , opC
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # ipVal
    def requestIpVal (self, requested):
        raise NotImplementedError()

    def isIpValRequested (self):
        raise NotImplementedError()

    def getIpVal (self):
        raise NotImplementedError()

    def hasIpVal (self):
        raise NotImplementedError()

    def setIpVal (self, ipVal):
        raise NotImplementedError()

    # id
    def requestId (self, requested):
        raise NotImplementedError()

    def isIdRequested (self):
        raise NotImplementedError()

    def getId (self):
        raise NotImplementedError()

    def hasId (self):
        raise NotImplementedError()

    def setId (self, id):
        raise NotImplementedError()

    # val
    def requestVal (self, requested):
        raise NotImplementedError()

    def isValRequested (self):
        raise NotImplementedError()

    def getVal (self):
        raise NotImplementedError()

    def hasVal (self):
        raise NotImplementedError()

    def setVal (self, val):
        raise NotImplementedError()

    # ipPrefixVal
    def requestIpPrefixVal (self, requested):
        raise NotImplementedError()

    def isIpPrefixValRequested (self):
        raise NotImplementedError()

    def getIpPrefixVal (self):
        raise NotImplementedError()

    def hasIpPrefixVal (self):
        raise NotImplementedError()

    def setIpPrefixVal (self, ipPrefixVal):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "opC", 
        "namespace": "op_c", 
        "className": "OpCMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_c.op_c_maapi_gen import OpCMaapi", 
        "baseClassName": "OpCMaapiBase", 
        "baseModule": "op_c_maapi_base_gen"
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
            "yangName": "op-b", 
            "namespace": "op_b", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-b"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "isCurrent": true, 
            "yangName": "op-c", 
            "namespace": "op_c", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "keyLeaf": {
                "varName": "opC", 
                "defaultVal": null, 
                "typeHandler": "handler: IntHandler"
            }, 
            "name": "op-c"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ipVal", 
            "yangName": "ip-val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
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
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "val", 
            "yangName": "val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "ipPrefixVal", 
            "yangName": "ip-prefix-val", 
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
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ipVal", 
            "yangName": "ip-val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
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
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "val", 
            "yangName": "val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "ipPrefixVal", 
            "yangName": "ip-prefix-val", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


