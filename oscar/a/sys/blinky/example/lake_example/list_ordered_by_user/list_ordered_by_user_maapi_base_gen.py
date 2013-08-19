


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ListOrderedByUserMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # orderedListList
    def newOrderedListList (self):
        raise NotImplementedError()

    def setOrderedListListObj (self, obj):
        raise NotImplementedError()

    def getOrderedListListObj (self):
        raise NotImplementedError()

    def hasOrderedListList (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "listOrderedByUser", 
        "namespace": "list_ordered_by_user", 
        "className": "ListOrderedByUserMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.list_ordered_by_user.list_ordered_by_user_maapi_gen import ListOrderedByUserMaapi", 
        "baseClassName": "ListOrderedByUserMaapiBase", 
        "baseModule": "list_ordered_by_user_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "list-ordered-by-user", 
            "namespace": "list_ordered_by_user", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "list-ordered-by-user"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "orderedListList", 
            "yangName": "ordered-list", 
            "className": "BlinkyOrderedListMaapiList", 
            "importStatement": "from a.sys.blinky.example.lake_example.list_ordered_by_user.ordered_list.ordered_list_maapi_list_gen import BlinkyOrderedListMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "lake_example"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


