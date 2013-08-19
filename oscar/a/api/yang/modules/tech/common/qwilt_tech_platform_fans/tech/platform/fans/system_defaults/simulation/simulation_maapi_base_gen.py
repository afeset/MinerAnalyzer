


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SimulationMaapiBase(object):
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





    # config leaves

    # forceOperationalStatus
    def requestForceOperationalStatus (self, requested):
        raise NotImplementedError()

    def isForceOperationalStatusRequested (self):
        raise NotImplementedError()

    def getForceOperationalStatus (self):
        raise NotImplementedError()

    def hasForceOperationalStatus (self):
        raise NotImplementedError()

    def setForceOperationalStatus (self, forceOperationalStatus):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "simulation", 
        "namespace": "simulation", 
        "className": "SimulationMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.system_defaults.simulation.simulation_maapi_gen import SimulationMaapi", 
        "baseClassName": "SimulationMaapiBase", 
        "baseModule": "simulation_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-pltf", 
            "yangName": "platform", 
            "namespace": "platform", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", 
            "name": "platform"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "yangName": "fans", 
            "namespace": "fans", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "fans"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "yangName": "simulation", 
            "namespace": "simulation", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "simulation"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "forceOperationalStatus", 
            "yangName": "force-operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
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
            "qwilt_tech_platform_fans"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "forceOperationalStatus", 
            "yangName": "force-operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


