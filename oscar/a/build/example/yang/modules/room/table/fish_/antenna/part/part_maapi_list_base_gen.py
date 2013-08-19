


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class PartMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newPart (self):
        raise NotImplementedError()

    def setPartObj (self, key, partObj):
        raise NotImplementedError()

    def getPartObj (self, key):
        raise NotImplementedError()

    def deletePart (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      , table
                      , fish_
                      
                      , trxContext=None):
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


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyPartMaapi", 
        "name": "part", 
        "keyLeaf": {
            "varName": "part", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "parts", 
        "namespace": "part", 
        "moduleYangNamespacePrefix": "room", 
        "className": "PartMaapiList", 
        "importStatement": "from a.build.example.yang.modules.room.table.fish_.antenna.part.part_maapi_list_gen import PartMaapiList", 
        "baseClassName": "PartMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/model/room", 
        "containerModule": "part_maapi_gen", 
        "baseModule": "part_maapi_list_base_gen"
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
                "yangName": "name", 
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
                "yangName": "id", 
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
                "yangName": "name", 
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


