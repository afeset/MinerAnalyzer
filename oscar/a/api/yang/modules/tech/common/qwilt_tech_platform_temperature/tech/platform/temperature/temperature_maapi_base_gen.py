


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class TemperatureMaapiBase(object):
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

    # status
    def newStatus (self):
        raise NotImplementedError()

    def setStatusObj (self, obj):
        raise NotImplementedError()

    def getStatusObj (self):
        raise NotImplementedError()

    def hasStatus (self):
        raise NotImplementedError()

    # alarm
    def newAlarm (self):
        raise NotImplementedError()

    def setAlarmObj (self, obj):
        raise NotImplementedError()

    def getAlarmObj (self):
        raise NotImplementedError()

    def hasAlarm (self):
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

    # systemDefaults
    def newSystemDefaults (self):
        raise NotImplementedError()

    def setSystemDefaultsObj (self, obj):
        raise NotImplementedError()

    def getSystemDefaultsObj (self):
        raise NotImplementedError()

    def hasSystemDefaults (self):
        raise NotImplementedError()

    # sensorList
    def newSensorList (self):
        raise NotImplementedError()

    def setSensorListObj (self, obj):
        raise NotImplementedError()

    def getSensorListObj (self):
        raise NotImplementedError()

    def hasSensorList (self):
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

    # enabled
    def requestEnabled (self, requested):
        raise NotImplementedError()

    def isEnabledRequested (self):
        raise NotImplementedError()

    def getEnabled (self):
        raise NotImplementedError()

    def hasEnabled (self):
        raise NotImplementedError()

    def setEnabled (self, enabled):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "temperature", 
        "namespace": "temperature", 
        "className": "TemperatureMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.temperature_maapi_gen import TemperatureMaapi", 
        "baseClassName": "TemperatureMaapiBase", 
        "baseModule": "temperature_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "name": "temperature"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "memberName": "alarm", 
            "yangName": "alarm", 
            "className": "BlinkyAlarmMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.alarm.alarm_maapi_gen import BlinkyAlarmMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "memberName": "simulation", 
            "yangName": "simulation", 
            "className": "BlinkySimulationMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.simulation.simulation_maapi_gen import BlinkySimulationMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "memberName": "sensorList", 
            "yangName": "sensor", 
            "className": "BlinkySensorMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.sensor_maapi_list_gen import BlinkySensorMaapiList", 
            "isList": true, 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


