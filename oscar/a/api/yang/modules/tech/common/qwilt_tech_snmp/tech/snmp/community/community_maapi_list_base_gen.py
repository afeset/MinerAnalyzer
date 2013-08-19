


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class CommunityMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newCommunity (self):
        raise NotImplementedError()

    def setCommunityObj (self, key, communityObj):
        raise NotImplementedError()

    def getCommunityObj (self, key):
        raise NotImplementedError()

    def deleteCommunity (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      
                      , trxContext=None):
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


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyCommunityMaapi", 
        "name": "community", 
        "keyLeaf": {
            "varName": "community", 
            "yangName": "entry-name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "community", 
        "namespace": "community", 
        "moduleYangNamespacePrefix": "qt-snmp", 
        "className": "CommunityMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.community.community_maapi_list_gen import CommunityMaapiList", 
        "baseClassName": "CommunityMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
        "containerModule": "community_maapi_gen", 
        "baseModule": "community_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qt-snmp", 
            "yangName": "snmp", 
            "namespace": "snmp", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "snmp"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "isCurrent": true, 
            "yangName": "community", 
            "namespace": "community", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "keyLeaf": {
                "varName": "community", 
                "yangName": "entry-name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "community"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "entryName", 
            "yangName": "entry-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "accessMode", 
            "yangName": "access-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "community", 
            "yangName": "community", 
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
            "common", 
            "qwilt_tech_snmp"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "entryName", 
            "yangName": "entry-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "accessMode", 
            "yangName": "access-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "community", 
            "yangName": "community", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


