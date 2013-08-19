


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class LakeMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newLake (self):
        raise NotImplementedError()

    def setLakeObj (self, key, lakeObj):
        raise NotImplementedError()

    def getLakeObj (self, key):
        raise NotImplementedError()

    def deleteLake (self, key):
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
        "containerClassName": "BlinkyLakeMaapi", 
        "name": "lake", 
        "keyLeaf": {
            "varName": "lake", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "lake", 
        "namespace": "lake", 
        "moduleYangNamespacePrefix": "lake-example", 
        "className": "LakeMaapiList", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.lake_maapi_list_gen import LakeMaapiList", 
        "baseClassName": "LakeMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
        "containerModule": "lake_maapi_gen", 
        "baseModule": "lake_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": true, 
            "yangName": "lake", 
            "namespace": "lake", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "lake", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lake"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "fish_List", 
            "yangName": "fish", 
            "className": "BlinkyFishMaapiList", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.fish__maapi_list_list_gen import BlinkyFishMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "size", 
            "yangName": "size", 
            "className": "BlinkySizeMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.size.size_maapi_list_gen import BlinkySizeMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
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
            "lake_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


