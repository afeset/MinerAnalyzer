


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class AlienMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newAlien (self):
        raise NotImplementedError()

    def setAlienObj (self, key, alienObj):
        raise NotImplementedError()

    def getAlienObj (self, key):
        raise NotImplementedError()

    def deleteAlien (self, key):
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
        "containerClassName": "BlinkyAlienMaapi", 
        "name": "alien", 
        "keyLeaf": {
            "varName": "alien", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "alien", 
        "namespace": "alien", 
        "moduleYangNamespacePrefix": "oe", 
        "className": "AlienMaapiList", 
        "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.alien_maapi_list_gen import AlienMaapiList", 
        "baseClassName": "AlienMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
        "containerModule": "alien_maapi_gen", 
        "baseModule": "alien_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oe", 
            "yangName": "root", 
            "namespace": "root", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "name": "root"
        }, 
        {
            "moduleYangNamespacePrefix": "oe", 
            "isCurrent": true, 
            "yangName": "alien", 
            "namespace": "alien", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "keyLeaf": {
                "varName": "alien", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "alien"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oe", 
            "memberName": "statusWrapper", 
            "yangName": "status-wrapper", 
            "className": "BlinkyStatusWrapperMaapi", 
            "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.status_wrapper.status_wrapper_maapi_list_gen import BlinkyStatusWrapperMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "150", 
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
            "oper", 
            "ut", 
            "oper_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "150", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


