


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class BbbMaapiBase(object):
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

    # b4int64
    def requestB4int64 (self, requested):
        raise NotImplementedError()

    def isB4int64Requested (self):
        raise NotImplementedError()

    def getB4int64 (self):
        raise NotImplementedError()

    def hasB4int64 (self):
        raise NotImplementedError()

    def setB4int64 (self, b4int64):
        raise NotImplementedError()

    # b6str
    def requestB6str (self, requested):
        raise NotImplementedError()

    def isB6strRequested (self):
        raise NotImplementedError()

    def getB6str (self):
        raise NotImplementedError()

    def hasB6str (self):
        raise NotImplementedError()

    def setB6str (self, b6str):
        raise NotImplementedError()

    # b3str
    def requestB3str (self, requested):
        raise NotImplementedError()

    def isB3strRequested (self):
        raise NotImplementedError()

    def getB3str (self):
        raise NotImplementedError()

    def hasB3str (self):
        raise NotImplementedError()

    def setB3str (self, b3str):
        raise NotImplementedError()

    # b5str
    def requestB5str (self, requested):
        raise NotImplementedError()

    def isB5strRequested (self):
        raise NotImplementedError()

    def getB5str (self):
        raise NotImplementedError()

    def hasB5str (self):
        raise NotImplementedError()

    def setB5str (self, b5str):
        raise NotImplementedError()

    # b7str
    def requestB7str (self, requested):
        raise NotImplementedError()

    def isB7strRequested (self):
        raise NotImplementedError()

    def getB7str (self):
        raise NotImplementedError()

    def hasB7str (self):
        raise NotImplementedError()

    def setB7str (self, b7str):
        raise NotImplementedError()

    # b9str
    def requestB9str (self, requested):
        raise NotImplementedError()

    def isB9strRequested (self):
        raise NotImplementedError()

    def getB9str (self):
        raise NotImplementedError()

    def hasB9str (self):
        raise NotImplementedError()

    def setB9str (self, b9str):
        raise NotImplementedError()

    # b1str
    def requestB1str (self, requested):
        raise NotImplementedError()

    def isB1strRequested (self):
        raise NotImplementedError()

    def getB1str (self):
        raise NotImplementedError()

    def hasB1str (self):
        raise NotImplementedError()

    def setB1str (self, b1str):
        raise NotImplementedError()

    # b8str
    def requestB8str (self, requested):
        raise NotImplementedError()

    def isB8strRequested (self):
        raise NotImplementedError()

    def getB8str (self):
        raise NotImplementedError()

    def hasB8str (self):
        raise NotImplementedError()

    def setB8str (self, b8str):
        raise NotImplementedError()

    # b2str
    def requestB2str (self, requested):
        raise NotImplementedError()

    def isB2strRequested (self):
        raise NotImplementedError()

    def getB2str (self):
        raise NotImplementedError()

    def hasB2str (self):
        raise NotImplementedError()

    def setB2str (self, b2str):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "bbb", 
        "namespace": "bbb", 
        "className": "BbbMaapi", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.bbb.bbb_maapi_gen import BbbMaapi", 
        "baseClassName": "BbbMaapiBase", 
        "baseModule": "bbb_maapi_base_gen"
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
            "yangName": "bbb", 
            "namespace": "bbb", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "bbb"
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
            "memberName": "b4int64", 
            "yangName": "b4int64", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b6str", 
            "yangName": "b6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b3str", 
            "yangName": "b3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b5str", 
            "yangName": "b5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b7str", 
            "yangName": "b7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b9str", 
            "yangName": "b9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b1str", 
            "yangName": "b1str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b8str", 
            "yangName": "b8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b2str", 
            "yangName": "b2str", 
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
            "memberName": "b4int64", 
            "yangName": "b4int64", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b6str", 
            "yangName": "b6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b3str", 
            "yangName": "b3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b5str", 
            "yangName": "b5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b7str", 
            "yangName": "b7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b9str", 
            "yangName": "b9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b1str", 
            "yangName": "b1str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b8str", 
            "yangName": "b8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b2str", 
            "yangName": "b2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


