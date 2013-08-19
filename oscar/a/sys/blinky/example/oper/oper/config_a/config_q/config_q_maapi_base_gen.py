


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ConfigQMaapiBase(object):
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

    # valueConfigQ
    def requestValueConfigQ (self, requested):
        raise NotImplementedError()

    def isValueConfigQRequested (self):
        raise NotImplementedError()

    def getValueConfigQ (self):
        raise NotImplementedError()

    def hasValueConfigQ (self):
        raise NotImplementedError()

    def setValueConfigQ (self, valueConfigQ):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "configQ", 
        "namespace": "config_q", 
        "className": "ConfigQMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_q.config_q_maapi_gen import ConfigQMaapi", 
        "baseClassName": "ConfigQMaapiBase", 
        "baseModule": "config_q_maapi_base_gen"
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
            "yangName": "config-q", 
            "namespace": "config_q", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "config-q"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "valueConfigQ", 
            "yangName": "value-config-q", 
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
            "memberName": "valueConfigQ", 
            "yangName": "value-config-q", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


