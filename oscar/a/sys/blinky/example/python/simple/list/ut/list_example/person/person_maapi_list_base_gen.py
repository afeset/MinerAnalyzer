


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class PersonMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newPerson (self):
        raise NotImplementedError()

    def setPersonObj (self, key, personObj):
        raise NotImplementedError()

    def getPersonObj (self, key):
        raise NotImplementedError()

    def deletePerson (self, key):
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
        "containerClassName": "BlinkyPersonMaapi", 
        "name": "person", 
        "keyLeaf": {
            "varName": "person", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "people", 
        "namespace": "person", 
        "moduleYangNamespacePrefix": "le", 
        "className": "PersonMaapiList", 
        "importStatement": "from a.sys.blinky.example.python.simple.list.ut.list_example.person.person_maapi_list_gen import PersonMaapiList", 
        "baseClassName": "PersonMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/list-example", 
        "containerModule": "person_maapi_gen", 
        "baseModule": "person_maapi_list_base_gen"
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
                "yangName": "name", 
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


