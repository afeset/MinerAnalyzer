


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SomeListMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newSomeList (self):
        raise NotImplementedError()

    def setSomeListObj (self, key, someListObj):
        raise NotImplementedError()

    def getSomeListObj (self, key):
        raise NotImplementedError()

    def deleteSomeList (self, key):
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
        "containerClassName": "BlinkySomeListMaapi", 
        "name": "someList", 
        "keyLeaf": {
            "varName": "someList", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "some-list", 
        "namespace": "some_list", 
        "moduleYangNamespacePrefix": "lake-example", 
        "className": "SomeListMaapiList", 
        "importStatement": "from a.sys.blinky.example.lake_example.ref_practice.some_list.some_list_maapi_list_gen import SomeListMaapiList", 
        "baseClassName": "SomeListMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
        "containerModule": "some_list_maapi_gen", 
        "baseModule": "some_list_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "ref-practice", 
            "namespace": "ref_practice", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "ref-practice"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": true, 
            "yangName": "some-list", 
            "namespace": "some_list", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "someList", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "some-list"
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
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "44", 
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
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "44", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


