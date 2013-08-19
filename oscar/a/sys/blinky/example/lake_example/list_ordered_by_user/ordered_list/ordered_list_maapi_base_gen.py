


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class OrderedListMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , orderedList
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , orderedList
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , orderedList
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

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

    # value
    def requestValue (self, requested):
        raise NotImplementedError()

    def isValueRequested (self):
        raise NotImplementedError()

    def getValue (self):
        raise NotImplementedError()

    def hasValue (self):
        raise NotImplementedError()

    def setValue (self, value):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "orderedList", 
        "namespace": "ordered_list", 
        "className": "OrderedListMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.list_ordered_by_user.ordered_list.ordered_list_maapi_gen import OrderedListMaapi", 
        "baseClassName": "OrderedListMaapiBase", 
        "baseModule": "ordered_list_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "list-ordered-by-user", 
            "namespace": "list_ordered_by_user", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "list-ordered-by-user"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": true, 
            "yangName": "ordered-list", 
            "namespace": "ordered_list", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "orderedList", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "ordered-list"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "lake_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


