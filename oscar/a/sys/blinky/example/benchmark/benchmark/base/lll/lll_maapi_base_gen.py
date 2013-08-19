


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class LllMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , lll
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , lll
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , lll
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # aaa
    def newAaa (self):
        raise NotImplementedError()

    def setAaaObj (self, obj):
        raise NotImplementedError()

    def getAaaObj (self):
        raise NotImplementedError()

    def hasAaa (self):
        raise NotImplementedError()

    # ccc
    def newCcc (self):
        raise NotImplementedError()

    def setCccObj (self, obj):
        raise NotImplementedError()

    def getCccObj (self):
        raise NotImplementedError()

    def hasCcc (self):
        raise NotImplementedError()

    # bbb
    def newBbb (self):
        raise NotImplementedError()

    def setBbbObj (self, obj):
        raise NotImplementedError()

    def getBbbObj (self):
        raise NotImplementedError()

    def hasBbb (self):
        raise NotImplementedError()




    # config leaves

    # color
    def requestColor (self, requested):
        raise NotImplementedError()

    def isColorRequested (self):
        raise NotImplementedError()

    def getColor (self):
        raise NotImplementedError()

    def hasColor (self):
        raise NotImplementedError()

    def setColor (self, color):
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






"""
Extracted from the below data: 
{
    "node": {
        "name": "lll", 
        "namespace": "lll", 
        "className": "LllMaapi", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.lll_maapi_gen import LllMaapi", 
        "baseClassName": "LllMaapiBase", 
        "baseModule": "lll_maapi_base_gen"
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
                "defaultVal": null, 
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
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.aaa.aaa_maapi_gen import BlinkyAaaMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "ccc", 
            "yangName": "ccc", 
            "className": "BlinkyCccMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.ccc.ccc_maapi_gen import BlinkyCccMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "bbb", 
            "yangName": "bbb", 
            "className": "BlinkyBbbMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.bbb.bbb_maapi_gen import BlinkyBbbMaapi", 
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


