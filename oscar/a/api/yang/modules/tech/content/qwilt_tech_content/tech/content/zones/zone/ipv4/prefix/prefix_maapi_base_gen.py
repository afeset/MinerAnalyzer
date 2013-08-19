


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class PrefixMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , zone
              , prefix
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , zone
              , prefix
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , zone
                       , prefix
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # prefix
    def requestPrefix (self, requested):
        raise NotImplementedError()

    def isPrefixRequested (self):
        raise NotImplementedError()

    def getPrefix (self):
        raise NotImplementedError()

    def hasPrefix (self):
        raise NotImplementedError()

    def setPrefix (self, prefix):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "prefix", 
        "namespace": "prefix", 
        "className": "PrefixMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.zones.zone.ipv4.prefix.prefix_maapi_gen import PrefixMaapi", 
        "baseClassName": "PrefixMaapiBase", 
        "baseModule": "prefix_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "zones", 
            "namespace": "zones", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "zones"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "isCurrent": false, 
            "yangName": "zone", 
            "namespace": "zone", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "keyLeaf": {
                "varName": "zone", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "zone"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "ipv4", 
            "namespace": "ipv4", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "ipv4"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "isCurrent": true, 
            "yangName": "prefix", 
            "namespace": "prefix", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "keyLeaf": {
                "varName": "prefix", 
                "defaultVal": null, 
                "typeHandler": "handler: Ipv4PrefixHandlerPy"
            }, 
            "name": "prefix"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "prefix", 
            "yangName": "prefix", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "prefix", 
            "yangName": "prefix", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


