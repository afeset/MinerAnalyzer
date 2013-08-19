


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ToysMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newToys (self):
        raise NotImplementedError()

    def setToysObj (self, key, toysObj):
        raise NotImplementedError()

    def getToysObj (self, key):
        raise NotImplementedError()

    def deleteToys (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      , kid
                      
                      , trxContext=None):
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


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyToysMaapi", 
        "name": "toys", 
        "keyLeaf": {
            "varName": "toys", 
            "yangName": "id", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "toys", 
        "namespace": "toys", 
        "moduleYangNamespacePrefix": "family", 
        "className": "ToysMaapiList", 
        "importStatement": "from a.build.example.yang.modules.family.kid.toys.toys_maapi_list_gen import ToysMaapiList", 
        "baseClassName": "ToysMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/family", 
        "containerModule": "toys_maapi_gen", 
        "baseModule": "toys_maapi_list_base_gen"
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
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "kid"
        }, 
        {
            "moduleYangNamespacePrefix": "family", 
            "isCurrent": true, 
            "yangName": "toys", 
            "namespace": "toys", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "keyLeaf": {
                "varName": "toys", 
                "yangName": "id", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "toys"
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
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
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
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


