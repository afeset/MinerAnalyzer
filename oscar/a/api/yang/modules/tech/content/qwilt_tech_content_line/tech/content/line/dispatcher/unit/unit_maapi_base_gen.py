


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class UnitMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , line
              , unit
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , line
              , unit
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , line
                       , unit
                       
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




    # config leaves

    # threadPriority
    def requestThreadPriority (self, requested):
        raise NotImplementedError()

    def isThreadPriorityRequested (self):
        raise NotImplementedError()

    def getThreadPriority (self):
        raise NotImplementedError()

    def hasThreadPriority (self):
        raise NotImplementedError()

    def setThreadPriority (self, threadPriority):
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

    # threadAffinity
    def requestThreadAffinity (self, requested):
        raise NotImplementedError()

    def isThreadAffinityRequested (self):
        raise NotImplementedError()

    def getThreadAffinity (self):
        raise NotImplementedError()

    def hasThreadAffinity (self):
        raise NotImplementedError()

    def setThreadAffinity (self, threadAffinity):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "unit", 
        "namespace": "unit", 
        "className": "UnitMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.unit.unit_maapi_gen import UnitMaapi", 
        "baseClassName": "UnitMaapiBase", 
        "baseModule": "unit_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": false, 
            "yangName": "line", 
            "namespace": "line", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "line", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "dispatcher", 
            "namespace": "dispatcher", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "dispatcher"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": true, 
            "yangName": "unit", 
            "namespace": "unit", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "unit", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "unit"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.unit.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadAffinity", 
            "yangName": "thread-affinity", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadAffinity", 
            "yangName": "thread-affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


