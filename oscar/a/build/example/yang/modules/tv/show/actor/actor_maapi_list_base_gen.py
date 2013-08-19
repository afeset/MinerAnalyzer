


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ActorMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newActor (self):
        raise NotImplementedError()

    def setActorObj (self, key, actorObj):
        raise NotImplementedError()

    def getActorObj (self, key):
        raise NotImplementedError()

    def deleteActor (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      , show
                      
                      , trxContext=None):
        raise NotImplementedError()

    def write (self
               , show
               , trxContext=None
               ):
        raise NotImplementedError()

    def read (self
              , show
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , show
                       
                       , trxContext=None):
        raise NotImplementedError()


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyActorMaapi", 
        "name": "actor", 
        "keyLeaf": {
            "varName": "actor", 
            "yangName": "id", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "actor", 
        "namespace": "actor", 
        "moduleYangNamespacePrefix": "tv", 
        "className": "ActorMaapiList", 
        "importStatement": "from a.build.example.yang.modules.tv.show.actor.actor_maapi_list_gen import ActorMaapiList", 
        "baseClassName": "ActorMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/tv", 
        "containerModule": "actor_maapi_gen", 
        "baseModule": "actor_maapi_list_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "tv", 
            "isCurrent": false, 
            "yangName": "show", 
            "namespace": "show", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "keyLeaf": {
                "varName": "show", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "show"
        }, 
        {
            "moduleYangNamespacePrefix": "tv", 
            "isCurrent": true, 
            "yangName": "actor", 
            "namespace": "actor", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "keyLeaf": {
                "varName": "actor", 
                "yangName": "id", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "actor"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
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
            "tv"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
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


