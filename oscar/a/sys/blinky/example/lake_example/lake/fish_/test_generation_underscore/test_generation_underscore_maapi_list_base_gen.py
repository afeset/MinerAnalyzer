


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class TestGenerationUnderscoreMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newTestGenerationUnderscore (self):
        raise NotImplementedError()

    def setTestGenerationUnderscoreObj (self, key, testGenerationUnderscoreObj):
        raise NotImplementedError()

    def getTestGenerationUnderscoreObj (self, key):
        raise NotImplementedError()

    def deleteTestGenerationUnderscore (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      , lake
                      , fish_
                      
                      , trxContext=None):
        raise NotImplementedError()

    def write (self
               , lake
               , fish_
               , trxContext=None
               ):
        raise NotImplementedError()

    def read (self
              , lake
              , fish_
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , lake
                       , fish_
                       
                       , trxContext=None):
        raise NotImplementedError()


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyTestGenerationUnderscoreMaapi", 
        "name": "testGenerationUnderscore", 
        "keyLeaf": {
            "varName": "testGenerationUnderscore", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "test-generation_underscore", 
        "namespace": "test_generation_underscore", 
        "moduleYangNamespacePrefix": "lake-example", 
        "className": "TestGenerationUnderscoreMaapiList", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.test_generation_underscore.test_generation_underscore_maapi_list_gen import TestGenerationUnderscoreMaapiList", 
        "baseClassName": "TestGenerationUnderscoreMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
        "containerModule": "test_generation_underscore_maapi_gen", 
        "baseModule": "test_generation_underscore_maapi_list_base_gen"
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
                "yangName": "name", 
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
                "yangName": "id", 
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
                "yangName": "name", 
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


