


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class TableMaapiBase(object):
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
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , table
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , table
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # fish_List
    def newFish_List (self):
        raise NotImplementedError()

    def setFish_ListObj (self, obj):
        raise NotImplementedError()

    def getFish_ListObj (self):
        raise NotImplementedError()

    def hasFish_List (self):
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
        "name": "table", 
        "namespace": "table", 
        "className": "TableMaapi", 
        "importStatement": "from a.build.example.yang.modules.room.table.table_maapi_gen import TableMaapi", 
        "baseClassName": "TableMaapiBase", 
        "baseModule": "table_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "room", 
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "room", 
            "memberName": "fish_List", 
            "yangName": "fish", 
            "className": "BlinkyFishMaapiList", 
            "importStatement": "from a.build.example.yang.modules.room.table.fish_.fish__maapi_list_gen import BlinkyFishMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/room"
        }, 
        {
            "moduleYangNamespacePrefix": "room", 
            "memberName": "size", 
            "yangName": "size", 
            "className": "BlinkySizeMaapi", 
            "importStatement": "from a.build.example.yang.modules.room.table.size.size_maapi_gen import BlinkySizeMaapi", 
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
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
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
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
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


