


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ConfigUMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , configU
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , configU
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , configU
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # valueConfigU1
    def requestValueConfigU1 (self, requested):
        raise NotImplementedError()

    def isValueConfigU1Requested (self):
        raise NotImplementedError()

    def getValueConfigU1 (self):
        raise NotImplementedError()

    def hasValueConfigU1 (self):
        raise NotImplementedError()

    def setValueConfigU1 (self, valueConfigU1):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "configU", 
        "namespace": "config_u", 
        "className": "ConfigUMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_u.config_u_maapi_gen import ConfigUMaapi", 
        "baseClassName": "ConfigUMaapiBase", 
        "baseModule": "config_u_maapi_base_gen"
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
            "yangName": "config-u", 
            "namespace": "config_u", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "keyLeaf": {
                "varName": "configU", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "config-u"
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueConfigU1", 
            "yangName": "value-config-u1", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueConfigU1", 
            "yangName": "value-config-u1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


