


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class HostMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newHost (self):
        raise NotImplementedError()

    def setHostObj (self, key, hostObj):
        raise NotImplementedError()

    def getHostObj (self, key):
        raise NotImplementedError()

    def deleteHost (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      , ipv4
                      
                      , trxContext=None):
        raise NotImplementedError()

    def write (self
               , ipv4
               , trxContext=None
               ):
        raise NotImplementedError()

    def read (self
              , ipv4
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , ipv4
                       
                       , trxContext=None):
        raise NotImplementedError()


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyHostMaapi", 
        "name": "host", 
        "keyLeaf": {
            "varName": "host", 
            "yangName": "hostname", 
            "typeHandler": "handler: BuiltinStringHandler"
        }, 
        "yangName": "host", 
        "namespace": "host", 
        "moduleYangNamespacePrefix": "qt-sys", 
        "className": "HostMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.static_resolution.hosts.ipv4.host.host_maapi_list_gen import HostMaapiList", 
        "baseClassName": "HostMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
        "containerModule": "host_maapi_gen", 
        "baseModule": "host_maapi_list_base_gen"
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
            "isCurrent": false, 
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
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "isCurrent": true, 
            "yangName": "host", 
            "namespace": "host", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "keyLeaf": {
                "varName": "host", 
                "yangName": "hostname", 
                "typeHandler": "handler: BuiltinStringHandler"
            }, 
            "name": "host"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "moduleYangNamespacePrefix": "qt-sys", 
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "hostname", 
            "yangName": "hostname", 
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
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "hostname", 
            "yangName": "hostname", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


