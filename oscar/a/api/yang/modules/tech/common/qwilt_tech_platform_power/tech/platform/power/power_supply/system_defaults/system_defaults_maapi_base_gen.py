


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SystemDefaultsMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , powerSupply
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , powerSupply
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , powerSupply
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # device
    def newDevice (self):
        raise NotImplementedError()

    def setDeviceObj (self, obj):
        raise NotImplementedError()

    def getDeviceObj (self):
        raise NotImplementedError()

    def hasDevice (self):
        raise NotImplementedError()

    # simulation
    def newSimulation (self):
        raise NotImplementedError()

    def setSimulationObj (self, obj):
        raise NotImplementedError()

    def getSimulationObj (self):
        raise NotImplementedError()

    def hasSimulation (self):
        raise NotImplementedError()




    # config leaves

    # muteReporting
    def requestMuteReporting (self, requested):
        raise NotImplementedError()

    def isMuteReportingRequested (self):
        raise NotImplementedError()

    def getMuteReporting (self):
        raise NotImplementedError()

    def hasMuteReporting (self):
        raise NotImplementedError()

    def setMuteReporting (self, muteReporting):
        raise NotImplementedError()

    # location
    def requestLocation (self, requested):
        raise NotImplementedError()

    def isLocationRequested (self):
        raise NotImplementedError()

    def getLocation (self):
        raise NotImplementedError()

    def hasLocation (self):
        raise NotImplementedError()

    def setLocation (self, location):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
        "baseClassName": "SystemDefaultsMaapiBase", 
        "baseModule": "system_defaults_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "yangName": "power", 
            "namespace": "power", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "power"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "isCurrent": false, 
            "yangName": "power-supply", 
            "namespace": "power_supply", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "keyLeaf": {
                "varName": "powerSupply", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "power-supply"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "memberName": "device", 
            "yangName": "device", 
            "className": "BlinkyDeviceMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.system_defaults.device.device_maapi_gen import BlinkyDeviceMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "memberName": "simulation", 
            "yangName": "simulation", 
            "className": "BlinkySimulationMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.system_defaults.simulation.simulation_maapi_gen import BlinkySimulationMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "qwilt_tech_platform_power"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


