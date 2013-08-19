


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class FishMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , table
              , fish_
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , table
              , fish_
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , table
                       , fish_
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # antenna
    def newAntenna (self):
        raise NotImplementedError()

    def setAntennaObj (self, obj):
        raise NotImplementedError()

    def getAntennaObj (self):
        raise NotImplementedError()

    def hasAntenna (self):
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
        "name": "fish_", 
        "namespace": "fish_", 
        "className": "FishMaapi", 
        "importStatement": "from a.build.example.yang.modules.room.table.fish_.fish__maapi_gen import FishMaapi", 
        "baseClassName": "FishMaapiBase", 
        "baseModule": "fish__maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "room", 
            "isCurrent": false, 
            "yangName": "table", 
            "namespace": "table", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "keyLeaf": {
                "varName": "table", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "table"
        }, 
        {
            "moduleYangNamespacePrefix": "room", 
            "isCurrent": true, 
            "yangName": "fish", 
            "namespace": "fish_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "keyLeaf": {
                "varName": "fish_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fish_"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "room", 
            "memberName": "antenna", 
            "yangName": "antenna", 
            "className": "BlinkyAntennaMaapi", 
            "importStatement": "from a.build.example.yang.modules.room.table.fish_.antenna.antenna_maapi_gen import BlinkyAntennaMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/room"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
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
            "room"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
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


