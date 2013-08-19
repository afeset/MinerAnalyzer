


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class AlarmMaapiBase(object):
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







    # oper leaves

    # noRedundancyReason
    def requestNoRedundancyReason (self, requested):
        raise NotImplementedError()

    def isNoRedundancyReasonRequested (self):
        raise NotImplementedError()

    def getNoRedundancyReason (self):
        raise NotImplementedError()

    def hasNoRedundancyReason (self):
        raise NotImplementedError()

    def setNoRedundancyReason (self, noRedundancyReason):
        raise NotImplementedError()

    # noRedundancy
    def requestNoRedundancy (self, requested):
        raise NotImplementedError()

    def isNoRedundancyRequested (self):
        raise NotImplementedError()

    def getNoRedundancy (self):
        raise NotImplementedError()

    def hasNoRedundancy (self):
        raise NotImplementedError()

    def setNoRedundancy (self, noRedundancy):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "alarm", 
        "namespace": "alarm", 
        "className": "AlarmMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.alarm.alarm_maapi_gen import AlarmMaapi", 
        "baseClassName": "AlarmMaapiBase", 
        "baseModule": "alarm_maapi_base_gen"
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
            "yangName": "alarm", 
            "namespace": "alarm", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "alarm"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "noRedundancyReason", 
            "yangName": "no-redundancy-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "noRedundancy", 
            "yangName": "no-redundancy", 
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
            "qwilt_tech_platform_power"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "noRedundancyReason", 
            "yangName": "no-redundancy-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "noRedundancy", 
            "yangName": "no-redundancy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


