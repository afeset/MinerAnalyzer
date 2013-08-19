


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SensorMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newSensor (self):
        raise NotImplementedError()

    def setSensorObj (self, key, sensorObj):
        raise NotImplementedError()

    def getSensorObj (self, key):
        raise NotImplementedError()

    def deleteSensor (self, key):
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
        "containerClassName": "BlinkySensorMaapi", 
        "name": "sensor", 
        "keyLeaf": {
            "varName": "sensor", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "sensor", 
        "namespace": "sensor", 
        "moduleYangNamespacePrefix": "qt-pltf-temperature", 
        "className": "SensorMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.sensor_maapi_list_gen import SensorMaapiList", 
        "baseClassName": "SensorMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
        "containerModule": "sensor_maapi_gen", 
        "baseModule": "sensor_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "yangName": "temperature", 
            "namespace": "temperature", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "name": "temperature"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "isCurrent": true, 
            "yangName": "sensor", 
            "namespace": "sensor", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "keyLeaf": {
                "varName": "sensor", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "sensor"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.status.status_maapi_list_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "memberName": "alarm", 
            "yangName": "alarm", 
            "className": "BlinkyAlarmMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.alarm.alarm_maapi_list_gen import BlinkyAlarmMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "memberName": "simulation", 
            "yangName": "simulation", 
            "className": "BlinkySimulationMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.simulation.simulation_maapi_list_gen import BlinkySimulationMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.system_defaults.system_defaults_maapi_list_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "memberName": "device", 
            "yangName": "device", 
            "className": "BlinkyDeviceMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.device.device_maapi_list_gen import BlinkyDeviceMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "qwilt_tech_platform_temperature"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


