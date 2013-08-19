


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ShowMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
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



    # descendants

    # actorList
    def newActorList (self):
        raise NotImplementedError()

    def setActorListObj (self, obj):
        raise NotImplementedError()

    def getActorListObj (self):
        raise NotImplementedError()

    def hasActorList (self):
        raise NotImplementedError()

    # size
    def newSize (self):
        raise NotImplementedError()

    def setSizeObj (self, obj):
        raise NotImplementedError()

    def getSizeObj (self):
        raise NotImplementedError()

    def hasSize (self):
        raise NotImplementedError()




    # config leaves

    # ip
    def requestIp (self, requested):
        raise NotImplementedError()

    def isIpRequested (self):
        raise NotImplementedError()

    def getIp (self):
        raise NotImplementedError()

    def hasIp (self):
        raise NotImplementedError()

    def setIp (self, ip):
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
        "name": "show", 
        "namespace": "show", 
        "className": "ShowMaapi", 
        "importStatement": "from a.build.example.yang.modules.tv.show.show_maapi_gen import ShowMaapi", 
        "baseClassName": "ShowMaapiBase", 
        "baseModule": "show_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "tv", 
            "isCurrent": true, 
            "yangName": "show", 
            "namespace": "show", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "keyLeaf": {
                "varName": "show", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "show"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "tv", 
            "memberName": "actorList", 
            "yangName": "actor", 
            "className": "BlinkyActorMaapiList", 
            "importStatement": "from a.build.example.yang.modules.tv.show.actor.actor_maapi_list_gen import BlinkyActorMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/tv"
        }, 
        {
            "moduleYangNamespacePrefix": "tv", 
            "memberName": "size", 
            "yangName": "size", 
            "className": "BlinkySizeMaapi", 
            "importStatement": "from a.build.example.yang.modules.tv.show.size.size_maapi_gen import BlinkySizeMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/tv"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
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
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
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


