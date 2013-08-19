


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class InstanceMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newInstance (self):
        raise NotImplementedError()

    def setInstanceObj (self, key, instanceObj):
        raise NotImplementedError()

    def getInstanceObj (self, key):
        raise NotImplementedError()

    def deleteInstance (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      , loggerClass
                      
                      , trxContext=None):
        raise NotImplementedError()

    def write (self
               , loggerClass
               , trxContext=None
               ):
        raise NotImplementedError()

    def read (self
              , loggerClass
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , loggerClass
                       
                       , trxContext=None):
        raise NotImplementedError()


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyInstanceMaapi", 
        "name": "instance", 
        "keyLeaf": {
            "varName": "instance", 
            "yangName": "name", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "instance", 
        "namespace": "instance", 
        "moduleYangNamespacePrefix": "qt-debug", 
        "className": "InstanceMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.instance_maapi_list_gen import InstanceMaapiList", 
        "baseClassName": "InstanceMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
        "containerModule": "instance_maapi_gen", 
        "baseModule": "instance_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "logger-class", 
            "namespace": "logger_class", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "loggerClass", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "logger-class"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": true, 
            "yangName": "instance", 
            "namespace": "instance", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "instance", 
                "yangName": "name", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "instance"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "memberName": "internal", 
            "yangName": "internal", 
            "className": "BlinkyInternalMaapi", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.internal.internal_maapi_list_gen import BlinkyInternalMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "memberName": "destinationList", 
            "yangName": "destination", 
            "className": "BlinkyDestinationMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.destination_maapi_list_list_gen import BlinkyDestinationMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.system_defaults.system_defaults_maapi_list_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "memberName": "ruleList", 
            "yangName": "rule", 
            "className": "BlinkyRuleMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.rule.rule_maapi_list_list_gen import BlinkyRuleMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "debug", 
            "qwilt_tech_debug"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


