


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ToysMaapiBase(object):
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
              , toys
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , kid
              , toys
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , kid
                       , toys
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # eyeNumber
    def requestEyeNumber (self, requested):
        raise NotImplementedError()

    def isEyeNumberRequested (self):
        raise NotImplementedError()

    def getEyeNumber (self):
        raise NotImplementedError()

    def hasEyeNumber (self):
        raise NotImplementedError()

    def setEyeNumber (self, eyeNumber):
        raise NotImplementedError()

    # transparentField
    def requestTransparentField (self, requested):
        raise NotImplementedError()

    def isTransparentFieldRequested (self):
        raise NotImplementedError()

    def getTransparentField (self):
        raise NotImplementedError()

    def hasTransparentField (self):
        raise NotImplementedError()

    def setTransparentField (self, transparentField):
        raise NotImplementedError()

    # id
    def requestId (self, requested):
        raise NotImplementedError()

    def isIdRequested (self):
        raise NotImplementedError()

    def getId (self):
        raise NotImplementedError()

    def hasId (self):
        raise NotImplementedError()

    def setId (self, id):
        raise NotImplementedError()

    # hasTail
    def requestHasTail (self, requested):
        raise NotImplementedError()

    def isHasTailRequested (self):
        raise NotImplementedError()

    def getHasTail (self):
        raise NotImplementedError()

    def hasHasTail (self):
        raise NotImplementedError()

    def setHasTail (self, hasTail):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "toys", 
        "namespace": "toys", 
        "className": "ToysMaapi", 
        "importStatement": "from a.build.example.yang.modules.family.kid.toys.toys_maapi_gen import ToysMaapi", 
        "baseClassName": "ToysMaapiBase", 
        "baseModule": "toys_maapi_base_gen"
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
            "isCurrent": true, 
            "yangName": "toys", 
            "namespace": "toys", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "keyLeaf": {
                "varName": "toys", 
                "defaultVal": null, 
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


