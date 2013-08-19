


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

    # neighbors
    def newNeighbors (self):
        raise NotImplementedError()

    def setNeighborsObj (self, obj):
        raise NotImplementedError()

    def getNeighborsObj (self):
        raise NotImplementedError()

    def hasNeighbors (self):
        raise NotImplementedError()

    # systemDefaults
    def newSystemDefaults (self):
        raise NotImplementedError()

    def setSystemDefaultsObj (self, obj):
        raise NotImplementedError()

    def getSystemDefaultsObj (self):
        raise NotImplementedError()

    def hasSystemDefaults (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "ipv6", 
        "namespace": "ipv6", 
        "className": "Ipv6Maapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.ipv6_maapi_gen import Ipv6Maapi", 
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
            "moduleYangNamespacePrefix": "qt-net", 
            "yangName": "network", 
            "namespace": "network", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network", 
            "name": "network"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "ipv6", 
            "namespace": "ipv6", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "ipv6"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "memberName": "neighbors", 
            "yangName": "neighbors", 
            "className": "BlinkyNeighborsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.neighbors_maapi_gen import BlinkyNeighborsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"
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
            "common", 
            "qwilt_tech_network_ipv6"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


