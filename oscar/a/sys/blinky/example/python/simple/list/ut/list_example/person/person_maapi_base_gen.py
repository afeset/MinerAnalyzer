


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class PersonMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , person
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , person
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , person
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # employed
    def requestEmployed (self, requested):
        raise NotImplementedError()

    def isEmployedRequested (self):
        raise NotImplementedError()

    def getEmployed (self):
        raise NotImplementedError()

    def hasEmployed (self):
        raise NotImplementedError()

    def setEmployed (self, employed):
        raise NotImplementedError()

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

    # height
    def requestHeight (self, requested):
        raise NotImplementedError()

    def isHeightRequested (self):
        raise NotImplementedError()

    def getHeight (self):
        raise NotImplementedError()

    def hasHeight (self):
        raise NotImplementedError()

    def setHeight (self, height):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "person", 
        "namespace": "person", 
        "className": "PersonMaapi", 
        "importStatement": "from a.sys.blinky.example.python.simple.list.ut.list_example.person.person_maapi_gen import PersonMaapi", 
        "baseClassName": "PersonMaapiBase", 
        "baseModule": "person_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "le", 
            "isCurrent": true, 
            "yangName": "people", 
            "namespace": "person", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/list-example", 
            "keyLeaf": {
                "varName": "person", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "person"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/list-example", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "employed", 
            "yangName": "employed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/list-example", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/list-example", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "175", 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "python", 
            "simple", 
            "list", 
            "ut", 
            "list_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/list-example", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "employed", 
            "yangName": "employed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/list-example", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/list-example", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "175", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


