


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class TestGenerationUnderscoreMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , lake
              , fish_
              , testGenerationUnderscore
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , lake
              , fish_
              , testGenerationUnderscore
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , lake
                       , fish_
                       , testGenerationUnderscore
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # name
    def requestName (self, requested):
        raise NotImplementedError()

    def isNameRequested (self):
        raise NotImplementedError()

    def getName (self):
        raise NotImplementedError()

    def hasName (self):
        raise NotImplementedError()

    def setName (self, name):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "testGenerationUnderscore", 
        "namespace": "test_generation_underscore", 
        "className": "TestGenerationUnderscoreMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.test_generation_underscore.test_generation_underscore_maapi_gen import TestGenerationUnderscoreMaapi", 
        "baseClassName": "TestGenerationUnderscoreMaapiBase", 
        "baseModule": "test_generation_underscore_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "lake", 
            "namespace": "lake", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "lake", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lake"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "fish", 
            "namespace": "fish_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "fish_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fish_"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": true, 
            "yangName": "test-generation_underscore", 
            "namespace": "test_generation_underscore", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "testGenerationUnderscore", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "test-generation_underscore"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
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


