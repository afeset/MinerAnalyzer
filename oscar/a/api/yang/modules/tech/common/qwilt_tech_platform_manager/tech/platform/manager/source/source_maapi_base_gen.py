


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SourceMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , source
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , source
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , source
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # systemDefaults
    def newSystemDefaults (self):
        raise NotImplementedError()

    def setSystemDefaultsObj (self, obj):
        raise NotImplementedError()

    def getSystemDefaultsObj (self):
        raise NotImplementedError()

    def hasSystemDefaults (self):
        raise NotImplementedError()

    # counters
    def newCounters (self):
        raise NotImplementedError()

    def setCountersObj (self, obj):
        raise NotImplementedError()

    def getCountersObj (self):
        raise NotImplementedError()

    def hasCounters (self):
        raise NotImplementedError()




    # config leaves

    # name
    def requestName (self, requested):
        raise NotImplementedError()

    def isNameRequested (self):
        raise NotImplementedError()

    def getName (self):
        raise NotImplementedError()

    def hasName (self):
        raise NotImplementedError()

    def setName (self, name):
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

    # simulationFile
    def requestSimulationFile (self, requested):
        raise NotImplementedError()

    def isSimulationFileRequested (self):
        raise NotImplementedError()

    def getSimulationFile (self):
        raise NotImplementedError()

    def hasSimulationFile (self):
        raise NotImplementedError()

    def setSimulationFile (self, simulationFile):
        raise NotImplementedError()

    # commandTimeout
    def requestCommandTimeout (self, requested):
        raise NotImplementedError()

    def isCommandTimeoutRequested (self):
        raise NotImplementedError()

    def getCommandTimeout (self):
        raise NotImplementedError()

    def hasCommandTimeout (self):
        raise NotImplementedError()

    def setCommandTimeout (self, commandTimeout):
        raise NotImplementedError()

    # commandWarningTimeout
    def requestCommandWarningTimeout (self, requested):
        raise NotImplementedError()

    def isCommandWarningTimeoutRequested (self):
        raise NotImplementedError()

    def getCommandWarningTimeout (self):
        raise NotImplementedError()

    def hasCommandWarningTimeout (self):
        raise NotImplementedError()

    def setCommandWarningTimeout (self, commandWarningTimeout):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "source", 
        "namespace": "source", 
        "className": "SourceMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_maapi_gen import SourceMaapi", 
        "baseClassName": "SourceMaapiBase", 
        "baseModule": "source_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "yangName": "manager", 
            "namespace": "manager", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "name": "manager"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "isCurrent": true, 
            "yangName": "source", 
            "namespace": "source", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "keyLeaf": {
                "varName": "source", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "source"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "simulationFile", 
            "yangName": "simulation-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeout", 
            "yangName": "command-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeout", 
            "yangName": "command-warning-timeout", 
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
            "qwilt_tech_platform_manager"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "simulationFile", 
            "yangName": "simulation-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeout", 
            "yangName": "command-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeout", 
            "yangName": "command-warning-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


