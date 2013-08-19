


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class OpLMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
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





    # config leaves

    # configDummy
    def requestConfigDummy (self, requested):
        raise NotImplementedError()

    def isConfigDummyRequested (self):
        raise NotImplementedError()

    def getConfigDummy (self):
        raise NotImplementedError()

    def hasConfigDummy (self):
        raise NotImplementedError()

    def setConfigDummy (self, configDummy):
        raise NotImplementedError()




    # oper leaves

    # valueOpL1
    def requestValueOpL1 (self, requested):
        raise NotImplementedError()

    def isValueOpL1Requested (self):
        raise NotImplementedError()

    def getValueOpL1 (self):
        raise NotImplementedError()

    def hasValueOpL1 (self):
        raise NotImplementedError()

    def setValueOpL1 (self, valueOpL1):
        raise NotImplementedError()

    # valueOpL2
    def requestValueOpL2 (self, requested):
        raise NotImplementedError()

    def isValueOpL2Requested (self):
        raise NotImplementedError()

    def getValueOpL2 (self):
        raise NotImplementedError()

    def hasValueOpL2 (self):
        raise NotImplementedError()

    def setValueOpL2 (self, valueOpL2):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "opL", 
        "namespace": "op_l", 
        "className": "OpLMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_l.op_l_maapi_gen import OpLMaapi", 
        "baseClassName": "OpLMaapiBase", 
        "baseModule": "op_l_maapi_base_gen"
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
            "yangName": "op-l", 
            "namespace": "op_l", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-l"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpL1", 
            "yangName": "value-op-l1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpL2", 
            "yangName": "value-op-l2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "configDummy", 
            "yangName": "config-dummy", 
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
            "memberName": "configDummy", 
            "yangName": "config-dummy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpL1", 
            "yangName": "value-op-l1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpL2", 
            "yangName": "value-op-l2", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


