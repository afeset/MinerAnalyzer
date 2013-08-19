


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class NameResolutionMaapiBase(object):
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

    # staticResolution
    def newStaticResolution (self):
        raise NotImplementedError()

    def setStaticResolutionObj (self, obj):
        raise NotImplementedError()

    def getStaticResolutionObj (self):
        raise NotImplementedError()

    def hasStaticResolution (self):
        raise NotImplementedError()

    # dns
    def newDns (self):
        raise NotImplementedError()

    def setDnsObj (self, obj):
        raise NotImplementedError()

    def getDnsObj (self):
        raise NotImplementedError()

    def hasDns (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "nameResolution", 
        "namespace": "name_resolution", 
        "className": "NameResolutionMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.name_resolution_maapi_gen import NameResolutionMaapi", 
        "baseClassName": "NameResolutionMaapiBase", 
        "baseModule": "name_resolution_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "name-resolution"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "memberName": "staticResolution", 
            "yangName": "static", 
            "className": "BlinkyStaticResolutionMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.static_resolution.static_resolution_maapi_gen import BlinkyStaticResolutionMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys", 
            "memberName": "dns", 
            "yangName": "dns", 
            "className": "BlinkyDnsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.dns.dns_maapi_gen import BlinkyDnsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system"
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
            "qwilt_tech_system"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


