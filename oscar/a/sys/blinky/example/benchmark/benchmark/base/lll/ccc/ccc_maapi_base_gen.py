


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class CccMaapiBase(object):
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

    # c9str
    def requestC9str (self, requested):
        raise NotImplementedError()

    def isC9strRequested (self):
        raise NotImplementedError()

    def getC9str (self):
        raise NotImplementedError()

    def hasC9str (self):
        raise NotImplementedError()

    def setC9str (self, c9str):
        raise NotImplementedError()

    # c2str
    def requestC2str (self, requested):
        raise NotImplementedError()

    def isC2strRequested (self):
        raise NotImplementedError()

    def getC2str (self):
        raise NotImplementedError()

    def hasC2str (self):
        raise NotImplementedError()

    def setC2str (self, c2str):
        raise NotImplementedError()

    # c8str
    def requestC8str (self, requested):
        raise NotImplementedError()

    def isC8strRequested (self):
        raise NotImplementedError()

    def getC8str (self):
        raise NotImplementedError()

    def hasC8str (self):
        raise NotImplementedError()

    def setC8str (self, c8str):
        raise NotImplementedError()

    # c6str
    def requestC6str (self, requested):
        raise NotImplementedError()

    def isC6strRequested (self):
        raise NotImplementedError()

    def getC6str (self):
        raise NotImplementedError()

    def hasC6str (self):
        raise NotImplementedError()

    def setC6str (self, c6str):
        raise NotImplementedError()

    # c5str
    def requestC5str (self, requested):
        raise NotImplementedError()

    def isC5strRequested (self):
        raise NotImplementedError()

    def getC5str (self):
        raise NotImplementedError()

    def hasC5str (self):
        raise NotImplementedError()

    def setC5str (self, c5str):
        raise NotImplementedError()

    # c1str
    def requestC1str (self, requested):
        raise NotImplementedError()

    def isC1strRequested (self):
        raise NotImplementedError()

    def getC1str (self):
        raise NotImplementedError()

    def hasC1str (self):
        raise NotImplementedError()

    def setC1str (self, c1str):
        raise NotImplementedError()

    # c7str
    def requestC7str (self, requested):
        raise NotImplementedError()

    def isC7strRequested (self):
        raise NotImplementedError()

    def getC7str (self):
        raise NotImplementedError()

    def hasC7str (self):
        raise NotImplementedError()

    def setC7str (self, c7str):
        raise NotImplementedError()

    # c10str
    def requestC10str (self, requested):
        raise NotImplementedError()

    def isC10strRequested (self):
        raise NotImplementedError()

    def getC10str (self):
        raise NotImplementedError()

    def hasC10str (self):
        raise NotImplementedError()

    def setC10str (self, c10str):
        raise NotImplementedError()

    # c3str
    def requestC3str (self, requested):
        raise NotImplementedError()

    def isC3strRequested (self):
        raise NotImplementedError()

    def getC3str (self):
        raise NotImplementedError()

    def hasC3str (self):
        raise NotImplementedError()

    def setC3str (self, c3str):
        raise NotImplementedError()

    # c4str
    def requestC4str (self, requested):
        raise NotImplementedError()

    def isC4strRequested (self):
        raise NotImplementedError()

    def getC4str (self):
        raise NotImplementedError()

    def hasC4str (self):
        raise NotImplementedError()

    def setC4str (self, c4str):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "ccc", 
        "namespace": "ccc", 
        "className": "CccMaapi", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.ccc.ccc_maapi_gen import CccMaapi", 
        "baseClassName": "CccMaapiBase", 
        "baseModule": "ccc_maapi_base_gen"
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
            "yangName": "ccc", 
            "namespace": "ccc", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "ccc"
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "c9str", 
            "yangName": "c9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c2str", 
            "yangName": "c2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c8str", 
            "yangName": "c8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c6str", 
            "yangName": "c6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c5str", 
            "yangName": "c5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c1str", 
            "yangName": "c1str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c7str", 
            "yangName": "c7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c10str", 
            "yangName": "c10str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c3str", 
            "yangName": "c3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c4str", 
            "yangName": "c4str", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "c9str", 
            "yangName": "c9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c2str", 
            "yangName": "c2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c8str", 
            "yangName": "c8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c6str", 
            "yangName": "c6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c5str", 
            "yangName": "c5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c1str", 
            "yangName": "c1str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c7str", 
            "yangName": "c7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c10str", 
            "yangName": "c10str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c3str", 
            "yangName": "c3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c4str", 
            "yangName": "c4str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


