


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class AaaMaapiBase(object):
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





    # config leaves

    # a1int64
    def requestA1int64 (self, requested):
        raise NotImplementedError()

    def isA1int64Requested (self):
        raise NotImplementedError()

    def getA1int64 (self):
        raise NotImplementedError()

    def hasA1int64 (self):
        raise NotImplementedError()

    def setA1int64 (self, a1int64):
        raise NotImplementedError()

    # a8str
    def requestA8str (self, requested):
        raise NotImplementedError()

    def isA8strRequested (self):
        raise NotImplementedError()

    def getA8str (self):
        raise NotImplementedError()

    def hasA8str (self):
        raise NotImplementedError()

    def setA8str (self, a8str):
        raise NotImplementedError()

    # a5str
    def requestA5str (self, requested):
        raise NotImplementedError()

    def isA5strRequested (self):
        raise NotImplementedError()

    def getA5str (self):
        raise NotImplementedError()

    def hasA5str (self):
        raise NotImplementedError()

    def setA5str (self, a5str):
        raise NotImplementedError()

    # a3str
    def requestA3str (self, requested):
        raise NotImplementedError()

    def isA3strRequested (self):
        raise NotImplementedError()

    def getA3str (self):
        raise NotImplementedError()

    def hasA3str (self):
        raise NotImplementedError()

    def setA3str (self, a3str):
        raise NotImplementedError()

    # a6str
    def requestA6str (self, requested):
        raise NotImplementedError()

    def isA6strRequested (self):
        raise NotImplementedError()

    def getA6str (self):
        raise NotImplementedError()

    def hasA6str (self):
        raise NotImplementedError()

    def setA6str (self, a6str):
        raise NotImplementedError()

    # a2str
    def requestA2str (self, requested):
        raise NotImplementedError()

    def isA2strRequested (self):
        raise NotImplementedError()

    def getA2str (self):
        raise NotImplementedError()

    def hasA2str (self):
        raise NotImplementedError()

    def setA2str (self, a2str):
        raise NotImplementedError()

    # a4str
    def requestA4str (self, requested):
        raise NotImplementedError()

    def isA4strRequested (self):
        raise NotImplementedError()

    def getA4str (self):
        raise NotImplementedError()

    def hasA4str (self):
        raise NotImplementedError()

    def setA4str (self, a4str):
        raise NotImplementedError()

    # a7str
    def requestA7str (self, requested):
        raise NotImplementedError()

    def isA7strRequested (self):
        raise NotImplementedError()

    def getA7str (self):
        raise NotImplementedError()

    def hasA7str (self):
        raise NotImplementedError()

    def setA7str (self, a7str):
        raise NotImplementedError()

    # a9str
    def requestA9str (self, requested):
        raise NotImplementedError()

    def isA9strRequested (self):
        raise NotImplementedError()

    def getA9str (self):
        raise NotImplementedError()

    def hasA9str (self):
        raise NotImplementedError()

    def setA9str (self, a9str):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "aaa", 
        "namespace": "aaa", 
        "className": "AaaMaapi", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.aaa.aaa_maapi_gen import AaaMaapi", 
        "baseClassName": "AaaMaapiBase", 
        "baseModule": "aaa_maapi_base_gen"
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
            "isCurrent": false, 
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
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "yangName": "aaa", 
            "namespace": "aaa", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "aaa"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "a1int64", 
            "yangName": "a1int64", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a8str", 
            "yangName": "a8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a5str", 
            "yangName": "a5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a3str", 
            "yangName": "a3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a6str", 
            "yangName": "a6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a2str", 
            "yangName": "a2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a4str", 
            "yangName": "a4str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a7str", 
            "yangName": "a7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a9str", 
            "yangName": "a9str", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "a1int64", 
            "yangName": "a1int64", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a8str", 
            "yangName": "a8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a5str", 
            "yangName": "a5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a3str", 
            "yangName": "a3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a6str", 
            "yangName": "a6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a2str", 
            "yangName": "a2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a4str", 
            "yangName": "a4str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a7str", 
            "yangName": "a7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a9str", 
            "yangName": "a9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


