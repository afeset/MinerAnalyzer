


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class KidMaapiBase(object):
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



    # descendants

    # size
    def newSize (self):
        raise NotImplementedError()

    def setSizeObj (self, obj):
        raise NotImplementedError()

    def getSizeObj (self):
        raise NotImplementedError()

    def hasSize (self):
        raise NotImplementedError()

    # toysList
    def newToysList (self):
        raise NotImplementedError()

    def setToysListObj (self, obj):
        raise NotImplementedError()

    def getToysListObj (self):
        raise NotImplementedError()

    def hasToysList (self):
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
        "name": "kid", 
        "namespace": "kid", 
        "className": "KidMaapi", 
        "importStatement": "from a.build.example.yang.modules.family.kid.kid_maapi_gen import KidMaapi", 
        "baseClassName": "KidMaapiBase", 
        "baseModule": "kid_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "family", 
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "family", 
            "memberName": "size", 
            "yangName": "size", 
            "className": "BlinkySizeMaapi", 
            "importStatement": "from a.build.example.yang.modules.family.kid.size.size_maapi_gen import BlinkySizeMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/family"
        }, 
        {
            "moduleYangNamespacePrefix": "family", 
            "memberName": "toysList", 
            "yangName": "toys", 
            "className": "BlinkyToysMaapiList", 
            "importStatement": "from a.build.example.yang.modules.family.kid.toys.toys_maapi_list_gen import BlinkyToysMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/family"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
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
            "family"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
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


