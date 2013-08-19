


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class AntennaMaapiBase(object):
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

    # partList
    def newPartList (self):
        raise NotImplementedError()

    def setPartListObj (self, obj):
        raise NotImplementedError()

    def getPartListObj (self):
        raise NotImplementedError()

    def hasPartList (self):
        raise NotImplementedError()




    # config leaves

    # height
    def requestHeight (self, requested):
        raise NotImplementedError()

    def isHeightRequested (self):
        raise NotImplementedError()

    def getHeight (self):
        raise NotImplementedError()

    def hasHeight (self):
        raise NotImplementedError()

    def setHeight (self, height):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "antenna", 
        "namespace": "antenna", 
        "className": "AntennaMaapi", 
        "importStatement": "from a.build.example.yang.modules.room.table.fish_.antenna.antenna_maapi_gen import AntennaMaapi", 
        "baseClassName": "AntennaMaapiBase", 
        "baseModule": "antenna_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "name": "antenna"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "room", 
            "memberName": "partList", 
            "yangName": "parts", 
            "className": "BlinkyPartMaapiList", 
            "importStatement": "from a.build.example.yang.modules.room.table.fish_.antenna.part.part_maapi_list_gen import BlinkyPartMaapiList", 
            "isList": true, 
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
            "memberName": "height", 
            "yangName": "height", 
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
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


