


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class RootMaapiBase(object):
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



    # descendants

    # alienList
    def newAlienList (self):
        raise NotImplementedError()

    def setAlienListObj (self, obj):
        raise NotImplementedError()

    def getAlienListObj (self):
        raise NotImplementedError()

    def hasAlienList (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "root", 
        "namespace": "root", 
        "className": "RootMaapi", 
        "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.root_maapi_gen import RootMaapi", 
        "baseClassName": "RootMaapiBase", 
        "baseModule": "root_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oe", 
            "yangName": "root", 
            "namespace": "root", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "name": "root"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oe", 
            "memberName": "alienList", 
            "yangName": "alien", 
            "className": "BlinkyAlienMaapiList", 
            "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.alien_maapi_list_gen import BlinkyAlienMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
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
    "leaves": [], 
    "createTime": "2013"
}
"""


