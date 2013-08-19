


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class Ipv4MaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , interface
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , interface
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # arp
    def newArp (self):
        raise NotImplementedError()

    def setArpObj (self, obj):
        raise NotImplementedError()

    def getArpObj (self):
        raise NotImplementedError()

    def hasArp (self):
        raise NotImplementedError()

    # ping
    def newPing (self):
        raise NotImplementedError()

    def setPingObj (self, obj):
        raise NotImplementedError()

    def getPingObj (self):
        raise NotImplementedError()

    def hasPing (self):
        raise NotImplementedError()




    # config leaves

    # method
    def requestMethod (self, requested):
        raise NotImplementedError()

    def isMethodRequested (self):
        raise NotImplementedError()

    def getMethod (self):
        raise NotImplementedError()

    def hasMethod (self):
        raise NotImplementedError()

    def setMethod (self, method):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "ipv4", 
        "namespace": "ipv4", 
        "className": "Ipv4Maapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.ipv4.ipv4_maapi_gen import Ipv4Maapi", 
        "baseClassName": "Ipv4MaapiBase", 
        "baseModule": "ipv4_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "connectivity-check", 
            "namespace": "connectivity_check", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "connectivity-check"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "ipv4", 
            "namespace": "ipv4", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "ipv4"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "arp", 
            "yangName": "arp", 
            "className": "BlinkyArpMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.ipv4.arp.arp_maapi_gen import BlinkyArpMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "ping", 
            "yangName": "ping", 
            "className": "BlinkyPingMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.ipv4.ping.ping_maapi_gen import BlinkyPingMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "method", 
            "yangName": "method", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "arp", 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "method", 
            "yangName": "method", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "arp", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


