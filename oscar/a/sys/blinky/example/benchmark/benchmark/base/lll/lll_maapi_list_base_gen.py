


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class LllMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newLll (self):
        raise NotImplementedError()

    def setLllObj (self, key, lllObj):
        raise NotImplementedError()

    def getLllObj (self, key):
        raise NotImplementedError()

    def deleteLll (self, key):
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
        "containerClassName": "BlinkyLllMaapi", 
        "name": "lll", 
        "keyLeaf": {
            "varName": "lll", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "lll", 
        "namespace": "lll", 
        "moduleYangNamespacePrefix": "bnch", 
        "className": "LllMaapiList", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.lll_maapi_list_gen import LllMaapiList", 
        "baseClassName": "LllMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
        "containerModule": "lll_maapi_gen", 
        "baseModule": "lll_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "bnch", 
            "yangName": "base", 
            "namespace": "base", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "base"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "isCurrent": true, 
            "yangName": "lll", 
            "namespace": "lll", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "keyLeaf": {
                "varName": "lll", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lll"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "aaa", 
            "yangName": "aaa", 
            "className": "BlinkyAaaMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.aaa.aaa_maapi_list_gen import BlinkyAaaMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "ccc", 
            "yangName": "ccc", 
            "className": "BlinkyCccMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.ccc.ccc_maapi_list_gen import BlinkyCccMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "bbb", 
            "yangName": "bbb", 
            "className": "BlinkyBbbMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.bbb.bbb_maapi_list_gen import BlinkyBbbMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
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
            "benchmark", 
            "benchmark"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
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


