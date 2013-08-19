


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ChairMaapiBase(object):
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

    # status
    def newStatus (self):
        raise NotImplementedError()

    def setStatusObj (self, obj):
        raise NotImplementedError()

    def getStatusObj (self):
        raise NotImplementedError()

    def hasStatus (self):
        raise NotImplementedError()




    # config leaves

    # color
    def requestColor (self, requested):
        raise NotImplementedError()

    def isColorRequested (self):
        raise NotImplementedError()

    def getColor (self):
        raise NotImplementedError()

    def hasColor (self):
        raise NotImplementedError()

    def setColor (self, color):
        raise NotImplementedError()

    # pretty
    def requestPretty (self, requested):
        raise NotImplementedError()

    def isPrettyRequested (self):
        raise NotImplementedError()

    def getPretty (self):
        raise NotImplementedError()

    def hasPretty (self):
        raise NotImplementedError()

    def setPretty (self, pretty):
        raise NotImplementedError()

    # numOfLegs
    def requestNumOfLegs (self, requested):
        raise NotImplementedError()

    def isNumOfLegsRequested (self):
        raise NotImplementedError()

    def getNumOfLegs (self):
        raise NotImplementedError()

    def hasNumOfLegs (self):
        raise NotImplementedError()

    def setNumOfLegs (self, numOfLegs):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "chair", 
        "namespace": "chair", 
        "className": "ChairMaapi", 
        "importStatement": "from a.sys.blinky.example.python.simple.container.ut.simple_example.chair.chair_maapi_gen import ChairMaapi", 
        "baseClassName": "ChairMaapiBase", 
        "baseModule": "chair_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "se", 
            "yangName": "chair", 
            "namespace": "chair", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "name": "chair"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "se", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.sys.blinky.example.python.simple.container.ut.simple_example.chair.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "yellow", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "pretty", 
            "yangName": "pretty", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "numOfLegs", 
            "yangName": "num-of-legs", 
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
            "python", 
            "simple", 
            "container", 
            "ut", 
            "simple_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "yellow", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "pretty", 
            "yangName": "pretty", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "numOfLegs", 
            "yangName": "num-of-legs", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


