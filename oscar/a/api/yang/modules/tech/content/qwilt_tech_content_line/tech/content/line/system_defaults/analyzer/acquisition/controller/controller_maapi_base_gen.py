


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ControllerMaapiBase(object):
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
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , line
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , line
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # efficiencyAlgorithm
    def newEfficiencyAlgorithm (self):
        raise NotImplementedError()

    def setEfficiencyAlgorithmObj (self, obj):
        raise NotImplementedError()

    def getEfficiencyAlgorithmObj (self):
        raise NotImplementedError()

    def hasEfficiencyAlgorithm (self):
        raise NotImplementedError()




    # config leaves

    # lazyFileOpen
    def requestLazyFileOpen (self, requested):
        raise NotImplementedError()

    def isLazyFileOpenRequested (self):
        raise NotImplementedError()

    def getLazyFileOpen (self):
        raise NotImplementedError()

    def hasLazyFileOpen (self):
        raise NotImplementedError()

    def setLazyFileOpen (self, lazyFileOpen):
        raise NotImplementedError()

    # logPeriodicStats
    def requestLogPeriodicStats (self, requested):
        raise NotImplementedError()

    def isLogPeriodicStatsRequested (self):
        raise NotImplementedError()

    def getLogPeriodicStats (self):
        raise NotImplementedError()

    def hasLogPeriodicStats (self):
        raise NotImplementedError()

    def setLogPeriodicStats (self, logPeriodicStats):
        raise NotImplementedError()

    # maxSessions
    def requestMaxSessions (self, requested):
        raise NotImplementedError()

    def isMaxSessionsRequested (self):
        raise NotImplementedError()

    def getMaxSessions (self):
        raise NotImplementedError()

    def hasMaxSessions (self):
        raise NotImplementedError()

    def setMaxSessions (self, maxSessions):
        raise NotImplementedError()

    # sessionQueueLowWaterMarkPercent
    def requestSessionQueueLowWaterMarkPercent (self, requested):
        raise NotImplementedError()

    def isSessionQueueLowWaterMarkPercentRequested (self):
        raise NotImplementedError()

    def getSessionQueueLowWaterMarkPercent (self):
        raise NotImplementedError()

    def hasSessionQueueLowWaterMarkPercent (self):
        raise NotImplementedError()

    def setSessionQueueLowWaterMarkPercent (self, sessionQueueLowWaterMarkPercent):
        raise NotImplementedError()

    # maxActiveSessions
    def requestMaxActiveSessions (self, requested):
        raise NotImplementedError()

    def isMaxActiveSessionsRequested (self):
        raise NotImplementedError()

    def getMaxActiveSessions (self):
        raise NotImplementedError()

    def hasMaxActiveSessions (self):
        raise NotImplementedError()

    def setMaxActiveSessions (self, maxActiveSessions):
        raise NotImplementedError()

    # algorithm
    def requestAlgorithm (self, requested):
        raise NotImplementedError()

    def isAlgorithmRequested (self):
        raise NotImplementedError()

    def getAlgorithm (self):
        raise NotImplementedError()

    def hasAlgorithm (self):
        raise NotImplementedError()

    def setAlgorithm (self, algorithm):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "controller", 
        "namespace": "controller", 
        "className": "ControllerMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.acquisition.controller.controller_maapi_gen import ControllerMaapi", 
        "baseClassName": "ControllerMaapiBase", 
        "baseModule": "controller_maapi_base_gen"
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
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "analyzer", 
            "namespace": "analyzer", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "analyzer"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "acquisition", 
            "namespace": "acquisition", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "acquisition"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "controller", 
            "namespace": "controller", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "controller"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "efficiencyAlgorithm", 
            "yangName": "efficiency-algorithm", 
            "className": "BlinkyEfficiencyAlgorithmMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.acquisition.controller.efficiency_algorithm.efficiency_algorithm_maapi_gen import BlinkyEfficiencyAlgorithmMaapi", 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "lazyFileOpen", 
            "yangName": "lazy-file-open", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "logPeriodicStats", 
            "yangName": "log-periodic-stats", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessions", 
            "yangName": "max-sessions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "sessionQueueLowWaterMarkPercent", 
            "yangName": "session-queue-low-water-mark-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxActiveSessions", 
            "yangName": "max-active-sessions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "algorithm", 
            "yangName": "algorithm", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "lazyFileOpen", 
            "yangName": "lazy-file-open", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "logPeriodicStats", 
            "yangName": "log-periodic-stats", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessions", 
            "yangName": "max-sessions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "sessionQueueLowWaterMarkPercent", 
            "yangName": "session-queue-low-water-mark-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxActiveSessions", 
            "yangName": "max-active-sessions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "algorithm", 
            "yangName": "algorithm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


