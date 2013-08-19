


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class AntennaMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , lake
              , fish_
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , lake
              , fish_
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , lake
                       , fish_
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # partList
    def newPartList (self):
        raise NotImplementedError()

    def setPartListObj (self, obj):
        raise NotImplementedError()

    def getPartListObj (self):
        raise NotImplementedError()

    def hasPartList (self):
        raise NotImplementedError()




    # config leaves

    # a
    def requestA (self, requested):
        raise NotImplementedError()

    def isARequested (self):
        raise NotImplementedError()

    def getA (self):
        raise NotImplementedError()

    def hasA (self):
        raise NotImplementedError()

    def setA (self, a):
        raise NotImplementedError()

    # c
    def requestC (self, requested):
        raise NotImplementedError()

    def isCRequested (self):
        raise NotImplementedError()

    def getC (self):
        raise NotImplementedError()

    def hasC (self):
        raise NotImplementedError()

    def setC (self, c):
        raise NotImplementedError()

    # b
    def requestB (self, requested):
        raise NotImplementedError()

    def isBRequested (self):
        raise NotImplementedError()

    def getB (self):
        raise NotImplementedError()

    def hasB (self):
        raise NotImplementedError()

    def setB (self, b):
        raise NotImplementedError()

    # e
    def requestE (self, requested):
        raise NotImplementedError()

    def isERequested (self):
        raise NotImplementedError()

    def getE (self):
        raise NotImplementedError()

    def hasE (self):
        raise NotImplementedError()

    def setE (self, e):
        raise NotImplementedError()

    # d
    def requestD (self, requested):
        raise NotImplementedError()

    def isDRequested (self):
        raise NotImplementedError()

    def getD (self):
        raise NotImplementedError()

    def hasD (self):
        raise NotImplementedError()

    def setD (self, d):
        raise NotImplementedError()

    # height
    def requestHeight (self, requested):
        raise NotImplementedError()

    def isHeightRequested (self):
        raise NotImplementedError()

    def getHeight (self):
        raise NotImplementedError()

    def hasHeight (self):
        raise NotImplementedError()

    def setHeight (self, height):
        raise NotImplementedError()

    # a1
    def requestA1 (self, requested):
        raise NotImplementedError()

    def isA1Requested (self):
        raise NotImplementedError()

    def getA1 (self):
        raise NotImplementedError()

    def hasA1 (self):
        raise NotImplementedError()

    def setA1 (self, a1):
        raise NotImplementedError()

    # b1
    def requestB1 (self, requested):
        raise NotImplementedError()

    def isB1Requested (self):
        raise NotImplementedError()

    def getB1 (self):
        raise NotImplementedError()

    def hasB1 (self):
        raise NotImplementedError()

    def setB1 (self, b1):
        raise NotImplementedError()

    # c1
    def requestC1 (self, requested):
        raise NotImplementedError()

    def isC1Requested (self):
        raise NotImplementedError()

    def getC1 (self):
        raise NotImplementedError()

    def hasC1 (self):
        raise NotImplementedError()

    def setC1 (self, c1):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "antenna", 
        "namespace": "antenna", 
        "className": "AntennaMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.antenna_maapi_gen import AntennaMaapi", 
        "baseClassName": "AntennaMaapiBase", 
        "baseModule": "antenna_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "lake", 
            "namespace": "lake", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "lake", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lake"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "fish", 
            "namespace": "fish_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "fish_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fish_"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "antenna", 
            "namespace": "antenna", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "antenna"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "partList", 
            "yangName": "parts", 
            "className": "BlinkyPartMaapiList", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.part.part_maapi_list_gen import BlinkyPartMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "a", 
            "yangName": "a", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "c", 
            "yangName": "c", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "b", 
            "yangName": "b", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "e", 
            "yangName": "e", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "d", 
            "yangName": "d", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a1", 
            "yangName": "a1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b1", 
            "yangName": "b1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c1", 
            "yangName": "c1", 
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
            "lake_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "a", 
            "yangName": "a", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "c", 
            "yangName": "c", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "b", 
            "yangName": "b", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "e", 
            "yangName": "e", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "d", 
            "yangName": "d", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a1", 
            "yangName": "a1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b1", 
            "yangName": "b1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c1", 
            "yangName": "c1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


