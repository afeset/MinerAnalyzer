


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class StatusMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , sensor
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , sensor
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , sensor
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # maximumCritical
    def requestMaximumCritical (self, requested):
        raise NotImplementedError()

    def isMaximumCriticalRequested (self):
        raise NotImplementedError()

    def getMaximumCritical (self):
        raise NotImplementedError()

    def hasMaximumCritical (self):
        raise NotImplementedError()

    def setMaximumCritical (self, maximumCritical):
        raise NotImplementedError()

    # operationalStatus
    def requestOperationalStatus (self, requested):
        raise NotImplementedError()

    def isOperationalStatusRequested (self):
        raise NotImplementedError()

    def getOperationalStatus (self):
        raise NotImplementedError()

    def hasOperationalStatus (self):
        raise NotImplementedError()

    def setOperationalStatus (self, operationalStatus):
        raise NotImplementedError()

    # temperature
    def requestTemperature (self, requested):
        raise NotImplementedError()

    def isTemperatureRequested (self):
        raise NotImplementedError()

    def getTemperature (self):
        raise NotImplementedError()

    def hasTemperature (self):
        raise NotImplementedError()

    def setTemperature (self, temperature):
        raise NotImplementedError()

    # minimumWarning
    def requestMinimumWarning (self, requested):
        raise NotImplementedError()

    def isMinimumWarningRequested (self):
        raise NotImplementedError()

    def getMinimumWarning (self):
        raise NotImplementedError()

    def hasMinimumWarning (self):
        raise NotImplementedError()

    def setMinimumWarning (self, minimumWarning):
        raise NotImplementedError()

    # minimumCritical
    def requestMinimumCritical (self, requested):
        raise NotImplementedError()

    def isMinimumCriticalRequested (self):
        raise NotImplementedError()

    def getMinimumCritical (self):
        raise NotImplementedError()

    def hasMinimumCritical (self):
        raise NotImplementedError()

    def setMinimumCritical (self, minimumCritical):
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

    # maximumWarning
    def requestMaximumWarning (self, requested):
        raise NotImplementedError()

    def isMaximumWarningRequested (self):
        raise NotImplementedError()

    def getMaximumWarning (self):
        raise NotImplementedError()

    def hasMaximumWarning (self):
        raise NotImplementedError()

    def setMaximumWarning (self, maximumWarning):
        raise NotImplementedError()

    # operationalStatusReason
    def requestOperationalStatusReason (self, requested):
        raise NotImplementedError()

    def isOperationalStatusReasonRequested (self):
        raise NotImplementedError()

    def getOperationalStatusReason (self):
        raise NotImplementedError()

    def hasOperationalStatusReason (self):
        raise NotImplementedError()

    def setOperationalStatusReason (self, operationalStatusReason):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
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
            "isCurrent": false, 
            "yangName": "sensor", 
            "namespace": "sensor", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "keyLeaf": {
                "varName": "sensor", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "sensor"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maximumCritical", 
            "yangName": "maximum-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "temperature", 
            "yangName": "temperature", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minimumWarning", 
            "yangName": "minimum-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minimumCritical", 
            "yangName": "minimum-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
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
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maximumWarning", 
            "yangName": "maximum-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
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
            "qwilt_tech_platform_temperature"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maximumCritical", 
            "yangName": "maximum-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "temperature", 
            "yangName": "temperature", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minimumWarning", 
            "yangName": "minimum-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minimumCritical", 
            "yangName": "minimum-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
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
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maximumWarning", 
            "yangName": "maximum-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


