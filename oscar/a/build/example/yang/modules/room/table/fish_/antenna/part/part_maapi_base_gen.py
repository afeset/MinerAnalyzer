


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class PartMaapiBase(object):
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
              , part
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , table
              , fish_
              , part
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , table
                       , fish_
                       , part
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # catalogId
    def requestCatalogId (self, requested):
        raise NotImplementedError()

    def isCatalogIdRequested (self):
        raise NotImplementedError()

    def getCatalogId (self):
        raise NotImplementedError()

    def hasCatalogId (self):
        raise NotImplementedError()

    def setCatalogId (self, catalogId):
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
        "name": "part", 
        "namespace": "part", 
        "className": "PartMaapi", 
        "importStatement": "from a.build.example.yang.modules.room.table.fish_.antenna.part.part_maapi_gen import PartMaapi", 
        "baseClassName": "PartMaapiBase", 
        "baseModule": "part_maapi_base_gen"
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
            "isCurrent": false, 
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
        }, 
        {
            "moduleYangNamespacePrefix": "room", 
            "yangName": "antenna", 
            "namespace": "antenna", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "name": "antenna"
        }, 
        {
            "moduleYangNamespacePrefix": "room", 
            "isCurrent": true, 
            "yangName": "parts", 
            "namespace": "part", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "keyLeaf": {
                "varName": "part", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "part"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "catalogId", 
            "yangName": "catalog-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
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
            "room"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "catalogId", 
            "yangName": "catalog-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
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


