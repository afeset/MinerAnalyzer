


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class CountersMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , alien
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , alien
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , alien
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # strTest
    def requestStrTest (self, requested):
        raise NotImplementedError()

    def isStrTestRequested (self):
        raise NotImplementedError()

    def getStrTest (self):
        raise NotImplementedError()

    def hasStrTest (self):
        raise NotImplementedError()

    def setStrTest (self, strTest):
        raise NotImplementedError()

    # mood
    def requestMood (self, requested):
        raise NotImplementedError()

    def isMoodRequested (self):
        raise NotImplementedError()

    def getMood (self):
        raise NotImplementedError()

    def hasMood (self):
        raise NotImplementedError()

    def setMood (self, mood):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.status_wrapper.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
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
            "isCurrent": false, 
            "yangName": "alien", 
            "namespace": "alien", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "keyLeaf": {
                "varName": "alien", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "alien"
        }, 
        {
            "moduleYangNamespacePrefix": "oe", 
            "yangName": "status-wrapper", 
            "namespace": "status_wrapper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "name": "status-wrapper"
        }, 
        {
            "moduleYangNamespacePrefix": "oe", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "strTest", 
            "yangName": "str-test", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "mood", 
            "yangName": "mood", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
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
            "memberName": "strTest", 
            "yangName": "str-test", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "mood", 
            "yangName": "mood", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


