


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class Ipv6MaapiBase(object):
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



    # descendants

    # prefixList
    def newPrefixList (self):
        raise NotImplementedError()

    def setPrefixListObj (self, obj):
        raise NotImplementedError()

    def getPrefixListObj (self):
        raise NotImplementedError()

    def hasPrefixList (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "ipv6", 
        "namespace": "ipv6", 
        "className": "Ipv6Maapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.zones.zone.ipv6.ipv6_maapi_gen import Ipv6Maapi", 
        "baseClassName": "Ipv6MaapiBase", 
        "baseModule": "ipv6_maapi_base_gen"
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
            "yangName": "ipv6", 
            "namespace": "ipv6", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "ipv6"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "prefixList", 
            "yangName": "prefix", 
            "className": "BlinkyPrefixMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.zones.zone.ipv6.prefix.prefix_maapi_list_gen import BlinkyPrefixMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [], 
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
    "leaves": [], 
    "createTime": "2013"
}
"""


