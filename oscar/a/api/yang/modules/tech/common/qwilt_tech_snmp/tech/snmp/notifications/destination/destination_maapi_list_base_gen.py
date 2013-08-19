


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class DestinationMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newDestination (self):
        raise NotImplementedError()

    def setDestinationObj (self, key, destinationObj):
        raise NotImplementedError()

    def getDestinationObj (self, key):
        raise NotImplementedError()

    def deleteDestination (self, key):
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
        "containerClassName": "BlinkyDestinationMaapi", 
        "name": "destination", 
        "keyLeaf": {
            "varName": "destination", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "destination", 
        "namespace": "destination", 
        "moduleYangNamespacePrefix": "qt-snmp", 
        "className": "DestinationMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.notifications.destination.destination_maapi_list_gen import DestinationMaapiList", 
        "baseClassName": "DestinationMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
        "containerModule": "destination_maapi_gen", 
        "baseModule": "destination_maapi_list_base_gen"
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
            "yangName": "notifications", 
            "namespace": "notifications", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "notifications"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "isCurrent": true, 
            "yangName": "destination", 
            "namespace": "destination", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "keyLeaf": {
                "varName": "destination", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "destination"
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
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "destination", 
            "yangName": "destination", 
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
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "version", 
            "yangName": "version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "v1", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "type_", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "trap", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "port", 
            "yangName": "port", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "162", 
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
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "destination", 
            "yangName": "destination", 
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
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "version", 
            "yangName": "version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "v1", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "type_", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "trap", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "port", 
            "yangName": "port", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "162", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


