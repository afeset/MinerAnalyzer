


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class BaseMaapiBase(object):
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

    # lllList
    def newLllList (self):
        raise NotImplementedError()

    def setLllListObj (self, obj):
        raise NotImplementedError()

    def getLllListObj (self):
        raise NotImplementedError()

    def hasLllList (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "base", 
        "namespace": "base", 
        "className": "BaseMaapi", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.base_maapi_gen import BaseMaapi", 
        "baseClassName": "BaseMaapiBase", 
        "baseModule": "base_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "bnch", 
            "yangName": "base", 
            "namespace": "base", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "base"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "lllList", 
            "yangName": "lll", 
            "className": "BlinkyLllMaapiList", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.lll_maapi_list_gen import BlinkyLllMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
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
            "benchmark", 
            "benchmark"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


