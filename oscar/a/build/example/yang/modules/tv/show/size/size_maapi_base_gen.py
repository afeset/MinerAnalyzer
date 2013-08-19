


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

    # boringLevel
    def requestBoringLevel (self, requested):
        raise NotImplementedError()

    def isBoringLevelRequested (self):
        raise NotImplementedError()

    def getBoringLevel (self):
        raise NotImplementedError()

    def hasBoringLevel (self):
        raise NotImplementedError()

    def setBoringLevel (self, boringLevel):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "size", 
        "namespace": "size", 
        "className": "SizeMaapi", 
        "importStatement": "from a.build.example.yang.modules.tv.show.size.size_maapi_gen import SizeMaapi", 
        "baseClassName": "SizeMaapiBase", 
        "baseModule": "size_maapi_base_gen"
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
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "show"
        }, 
        {
            "moduleYangNamespacePrefix": "tv", 
            "yangName": "size", 
            "namespace": "size", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "name": "size"
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
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "boringLevel", 
            "yangName": "boring-level", 
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
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/tv", 
            "moduleYangNamespacePrefix": "tv", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "boringLevel", 
            "yangName": "boring-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


