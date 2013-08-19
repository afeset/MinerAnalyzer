


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SizeDefaultMaapiBase(object):
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





    # config leaves

    # width
    def requestWidth (self, requested):
        raise NotImplementedError()

    def isWidthRequested (self):
        raise NotImplementedError()

    def getWidth (self):
        raise NotImplementedError()

    def hasWidth (self):
        raise NotImplementedError()

    def setWidth (self, width):
        raise NotImplementedError()

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






"""
Extracted from the below data: 
{
    "node": {
        "name": "sizeDefault", 
        "namespace": "size_default", 
        "className": "SizeDefaultMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.size_default.size_default_maapi_gen import SizeDefaultMaapi", 
        "baseClassName": "SizeDefaultMaapiBase", 
        "baseModule": "size_default_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "size-default", 
            "namespace": "size_default", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "size-default"
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "width", 
            "yangName": "width", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "30", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "20", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "width", 
            "yangName": "width", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "30", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "20", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


