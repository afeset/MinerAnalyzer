


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class Ipv4MaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newIpv4 (self):
        raise NotImplementedError()

    def setIpv4Obj (self, key, ipv4Obj):
        raise NotImplementedError()

    def getIpv4Obj (self, key):
        raise NotImplementedError()

    def deleteIpv4 (self, key):
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
        "containerClassName": "BlinkyIpv4Maapi", 
        "name": "ipv4", 
        "keyLeaf": {
            "varName": "ipv4", 
            "yangName": "address", 
            "typeHandler": "handler: Ipv4AddressHandlerPy"
        }, 
        "yangName": "ipv4", 
        "namespace": "ipv4", 
        "moduleYangNamespacePrefix": "qt-sys", 
        "className": "Ipv4MaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.static_resolution.hosts.ipv4.ipv4_maapi_list_gen import Ipv4MaapiList", 
        "baseClassName": "Ipv4MaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
        "containerModule": "ipv4_maapi_gen", 
        "baseModule": "ipv4_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "system", 
            "namespace": "system", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "name-resolution", 
            "namespace": "name_resolution", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "name-resolution"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "static", 
            "namespace": "static_resolution", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "static-resolution"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "hosts", 
            "namespace": "hosts", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "hosts"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "isCurrent": true, 
            "yangName": "ipv4", 
            "namespace": "ipv4", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "keyLeaf": {
                "varName": "ipv4", 
                "yangName": "address", 
                "typeHandler": "handler: Ipv4AddressHandlerPy"
            }, 
            "name": "ipv4"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "memberName": "hostList", 
            "yangName": "host", 
            "className": "BlinkyHostMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.static_resolution.hosts.ipv4.host.host_maapi_list_list_gen import BlinkyHostMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "moduleYangNamespacePrefix": "qt-sys", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "address", 
            "yangName": "address", 
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
            "qwilt_tech_system"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "moduleYangNamespacePrefix": "qt-sys", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "address", 
            "yangName": "address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


