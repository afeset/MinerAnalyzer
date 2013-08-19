


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class DecisionMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , loggerClass
              , instance
              , rule
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , loggerClass
              , instance
              , rule
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       , rule
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # logBacktrace
    def requestLogBacktrace (self, requested):
        raise NotImplementedError()

    def isLogBacktraceRequested (self):
        raise NotImplementedError()

    def getLogBacktrace (self):
        raise NotImplementedError()

    def hasLogBacktrace (self):
        raise NotImplementedError()

    def setLogBacktrace (self, logBacktrace):
        raise NotImplementedError()

    # ignoreCondition
    def requestIgnoreCondition (self, requested):
        raise NotImplementedError()

    def isIgnoreConditionRequested (self):
        raise NotImplementedError()

    def getIgnoreCondition (self):
        raise NotImplementedError()

    def hasIgnoreCondition (self):
        raise NotImplementedError()

    def setIgnoreCondition (self, ignoreCondition):
        raise NotImplementedError()

    # log
    def requestLog (self, requested):
        raise NotImplementedError()

    def isLogRequested (self):
        raise NotImplementedError()

    def getLog (self):
        raise NotImplementedError()

    def hasLog (self):
        raise NotImplementedError()

    def setLog (self, log):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "decision", 
        "namespace": "decision", 
        "className": "DecisionMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.rule.decision.decision_maapi_gen import DecisionMaapi", 
        "baseClassName": "DecisionMaapiBase", 
        "baseModule": "decision_maapi_base_gen"
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
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "logger-class"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "instance", 
            "namespace": "instance", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "instance", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "instance"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "rule", 
            "namespace": "rule", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "rule", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "rule"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "decision", 
            "namespace": "decision", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "decision"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logBacktrace", 
            "yangName": "log-backtrace", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "ignoreCondition", 
            "yangName": "ignore-condition", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "log", 
            "yangName": "log", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logBacktrace", 
            "yangName": "log-backtrace", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "ignoreCondition", 
            "yangName": "ignore-condition", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "log", 
            "yangName": "log", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


