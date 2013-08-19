


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class PrefixMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newPrefix (self):
        raise NotImplementedError()

    def setPrefixObj (self, key, prefixObj):
        raise NotImplementedError()

    def getPrefixObj (self, key):
        raise NotImplementedError()

    def deletePrefix (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      , zone
                      
                      , trxContext=None):
        raise NotImplementedError()

    def write (self
               , zone
               , trxContext=None
               ):
        raise NotImplementedError()

    def read (self
              , zone
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , zone
                       
                       , trxContext=None):
        raise NotImplementedError()


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyPrefixMaapi", 
        "name": "prefix", 
        "keyLeaf": {
            "varName": "prefix", 
            "yangName": "prefix", 
            "typeHandler": "handler: Ipv6PrefixHandlerPy"
        }, 
        "yangName": "prefix", 
        "namespace": "prefix", 
        "moduleYangNamespacePrefix": "qtc", 
        "className": "PrefixMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.zones.zone.ipv6.prefix.prefix_maapi_list_gen import PrefixMaapiList", 
        "baseClassName": "PrefixMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
        "containerModule": "prefix_maapi_gen", 
        "baseModule": "prefix_maapi_list_base_gen"
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
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "zone"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "ipv6", 
            "namespace": "ipv6", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "ipv6"
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
                "yangName": "prefix", 
                "typeHandler": "handler: Ipv6PrefixHandlerPy"
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
            "typeHandler": "handler: Ipv6PrefixHandlerPy", 
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
            "typeHandler": "handler: Ipv6PrefixHandlerPy", 
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


