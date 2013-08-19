


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SizeMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , kid
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , kid
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , kid
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # length
    def requestLength (self, requested):
        raise NotImplementedError()

    def isLengthRequested (self):
        raise NotImplementedError()

    def getLength (self):
        raise NotImplementedError()

    def hasLength (self):
        raise NotImplementedError()

    def setLength (self, length):
        raise NotImplementedError()

    # smartness
    def requestSmartness (self, requested):
        raise NotImplementedError()

    def isSmartnessRequested (self):
        raise NotImplementedError()

    def getSmartness (self):
        raise NotImplementedError()

    def hasSmartness (self):
        raise NotImplementedError()

    def setSmartness (self, smartness):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "size", 
        "namespace": "size", 
        "className": "SizeMaapi", 
        "importStatement": "from a.build.example.yang.modules.family.kid.size.size_maapi_gen import SizeMaapi", 
        "baseClassName": "SizeMaapiBase", 
        "baseModule": "size_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "family", 
            "isCurrent": false, 
            "yangName": "kid", 
            "namespace": "kid", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "keyLeaf": {
                "varName": "kid", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "kid"
        }, 
        {
            "moduleYangNamespacePrefix": "family", 
            "yangName": "size", 
            "namespace": "size", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "name": "size"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "smartness", 
            "yangName": "smartness", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "build", 
            "example", 
            "yang", 
            "modules", 
            "family"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "smartness", 
            "yangName": "smartness", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


