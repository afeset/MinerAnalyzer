


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ConfigPMaapiBase(object):
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



    # descendants

    # opR
    def newOpR (self):
        raise NotImplementedError()

    def setOpRObj (self, obj):
        raise NotImplementedError()

    def getOpRObj (self):
        raise NotImplementedError()

    def hasOpR (self):
        raise NotImplementedError()




    # config leaves

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






"""
Extracted from the below data: 
{
    "node": {
        "name": "configP", 
        "namespace": "config_p", 
        "className": "ConfigPMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.config_p_maapi_gen import ConfigPMaapi", 
        "baseClassName": "ConfigPMaapiBase", 
        "baseModule": "config_p_maapi_base_gen"
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
                "defaultVal": null, 
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
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.op_r.op_r_maapi_gen import BlinkyOpRMaapi", 
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


