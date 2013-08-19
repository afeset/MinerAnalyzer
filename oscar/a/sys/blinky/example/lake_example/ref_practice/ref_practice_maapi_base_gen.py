


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class RefPracticeMaapiBase(object):
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

    # someListList
    def newSomeListList (self):
        raise NotImplementedError()

    def setSomeListListObj (self, obj):
        raise NotImplementedError()

    def getSomeListListObj (self):
        raise NotImplementedError()

    def hasSomeListList (self):
        raise NotImplementedError()




    # config leaves

    # someLeafRef
    def requestSomeLeafRef (self, requested):
        raise NotImplementedError()

    def isSomeLeafRefRequested (self):
        raise NotImplementedError()

    def getSomeLeafRef (self):
        raise NotImplementedError()

    def hasSomeLeafRef (self):
        raise NotImplementedError()

    def setSomeLeafRef (self, someLeafRef):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "refPractice", 
        "namespace": "ref_practice", 
        "className": "RefPracticeMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.ref_practice.ref_practice_maapi_gen import RefPracticeMaapi", 
        "baseClassName": "RefPracticeMaapiBase", 
        "baseModule": "ref_practice_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "ref-practice", 
            "namespace": "ref_practice", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "ref-practice"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "someListList", 
            "yangName": "some-list", 
            "className": "BlinkySomeListMaapiList", 
            "importStatement": "from a.sys.blinky.example.lake_example.ref_practice.some_list.some_list_maapi_list_gen import BlinkySomeListMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "someLeafRef", 
            "yangName": "some-leaf-ref", 
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
            "memberName": "someLeafRef", 
            "yangName": "some-leaf-ref", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


