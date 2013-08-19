


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class BurstLimitsMaapiBase(object):
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
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , loggerClass
              , instance
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # infoDropLevel
    def requestInfoDropLevel (self, requested):
        raise NotImplementedError()

    def isInfoDropLevelRequested (self):
        raise NotImplementedError()

    def getInfoDropLevel (self):
        raise NotImplementedError()

    def hasInfoDropLevel (self):
        raise NotImplementedError()

    def setInfoDropLevel (self, infoDropLevel):
        raise NotImplementedError()

    # debug2DropLevel
    def requestDebug2DropLevel (self, requested):
        raise NotImplementedError()

    def isDebug2DropLevelRequested (self):
        raise NotImplementedError()

    def getDebug2DropLevel (self):
        raise NotImplementedError()

    def hasDebug2DropLevel (self):
        raise NotImplementedError()

    def setDebug2DropLevel (self, debug2DropLevel):
        raise NotImplementedError()

    # noticeDropLevel
    def requestNoticeDropLevel (self, requested):
        raise NotImplementedError()

    def isNoticeDropLevelRequested (self):
        raise NotImplementedError()

    def getNoticeDropLevel (self):
        raise NotImplementedError()

    def hasNoticeDropLevel (self):
        raise NotImplementedError()

    def setNoticeDropLevel (self, noticeDropLevel):
        raise NotImplementedError()

    # debug5DropLevel
    def requestDebug5DropLevel (self, requested):
        raise NotImplementedError()

    def isDebug5DropLevelRequested (self):
        raise NotImplementedError()

    def getDebug5DropLevel (self):
        raise NotImplementedError()

    def hasDebug5DropLevel (self):
        raise NotImplementedError()

    def setDebug5DropLevel (self, debug5DropLevel):
        raise NotImplementedError()

    # warningDropLevel
    def requestWarningDropLevel (self, requested):
        raise NotImplementedError()

    def isWarningDropLevelRequested (self):
        raise NotImplementedError()

    def getWarningDropLevel (self):
        raise NotImplementedError()

    def hasWarningDropLevel (self):
        raise NotImplementedError()

    def setWarningDropLevel (self, warningDropLevel):
        raise NotImplementedError()

    # alertDropLevel
    def requestAlertDropLevel (self, requested):
        raise NotImplementedError()

    def isAlertDropLevelRequested (self):
        raise NotImplementedError()

    def getAlertDropLevel (self):
        raise NotImplementedError()

    def hasAlertDropLevel (self):
        raise NotImplementedError()

    def setAlertDropLevel (self, alertDropLevel):
        raise NotImplementedError()

    # debug3DropLevel
    def requestDebug3DropLevel (self, requested):
        raise NotImplementedError()

    def isDebug3DropLevelRequested (self):
        raise NotImplementedError()

    def getDebug3DropLevel (self):
        raise NotImplementedError()

    def hasDebug3DropLevel (self):
        raise NotImplementedError()

    def setDebug3DropLevel (self, debug3DropLevel):
        raise NotImplementedError()

    # emergencyDropLevel
    def requestEmergencyDropLevel (self, requested):
        raise NotImplementedError()

    def isEmergencyDropLevelRequested (self):
        raise NotImplementedError()

    def getEmergencyDropLevel (self):
        raise NotImplementedError()

    def hasEmergencyDropLevel (self):
        raise NotImplementedError()

    def setEmergencyDropLevel (self, emergencyDropLevel):
        raise NotImplementedError()

    # debug4DropLevel
    def requestDebug4DropLevel (self, requested):
        raise NotImplementedError()

    def isDebug4DropLevelRequested (self):
        raise NotImplementedError()

    def getDebug4DropLevel (self):
        raise NotImplementedError()

    def hasDebug4DropLevel (self):
        raise NotImplementedError()

    def setDebug4DropLevel (self, debug4DropLevel):
        raise NotImplementedError()

    # debug1DropLevel
    def requestDebug1DropLevel (self, requested):
        raise NotImplementedError()

    def isDebug1DropLevelRequested (self):
        raise NotImplementedError()

    def getDebug1DropLevel (self):
        raise NotImplementedError()

    def hasDebug1DropLevel (self):
        raise NotImplementedError()

    def setDebug1DropLevel (self, debug1DropLevel):
        raise NotImplementedError()

    # criticalDropLevel
    def requestCriticalDropLevel (self, requested):
        raise NotImplementedError()

    def isCriticalDropLevelRequested (self):
        raise NotImplementedError()

    def getCriticalDropLevel (self):
        raise NotImplementedError()

    def hasCriticalDropLevel (self):
        raise NotImplementedError()

    def setCriticalDropLevel (self, criticalDropLevel):
        raise NotImplementedError()

    # burstMax
    def requestBurstMax (self, requested):
        raise NotImplementedError()

    def isBurstMaxRequested (self):
        raise NotImplementedError()

    def getBurstMax (self):
        raise NotImplementedError()

    def hasBurstMax (self):
        raise NotImplementedError()

    def setBurstMax (self, burstMax):
        raise NotImplementedError()

    # errorDropLevel
    def requestErrorDropLevel (self, requested):
        raise NotImplementedError()

    def isErrorDropLevelRequested (self):
        raise NotImplementedError()

    def getErrorDropLevel (self):
        raise NotImplementedError()

    def hasErrorDropLevel (self):
        raise NotImplementedError()

    def setErrorDropLevel (self, errorDropLevel):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "burstLimits", 
        "namespace": "burst_limits", 
        "className": "BurstLimitsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.system_defaults.internal.burst_limits.burst_limits_maapi_gen import BurstLimitsMaapi", 
        "baseClassName": "BurstLimitsMaapiBase", 
        "baseModule": "burst_limits_maapi_base_gen"
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
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "internal", 
            "namespace": "internal", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "internal"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "burst-limits", 
            "namespace": "burst_limits", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "burst-limits"
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "infoDropLevel", 
            "yangName": "info-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug2DropLevel", 
            "yangName": "debug2-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "noticeDropLevel", 
            "yangName": "notice-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug5DropLevel", 
            "yangName": "debug5-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warningDropLevel", 
            "yangName": "warning-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "alertDropLevel", 
            "yangName": "alert-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug3DropLevel", 
            "yangName": "debug3-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "emergencyDropLevel", 
            "yangName": "emergency-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug4DropLevel", 
            "yangName": "debug4-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug1DropLevel", 
            "yangName": "debug1-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "criticalDropLevel", 
            "yangName": "critical-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "burstMax", 
            "yangName": "burst-max", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "errorDropLevel", 
            "yangName": "error-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "infoDropLevel", 
            "yangName": "info-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug2DropLevel", 
            "yangName": "debug2-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "noticeDropLevel", 
            "yangName": "notice-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug5DropLevel", 
            "yangName": "debug5-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warningDropLevel", 
            "yangName": "warning-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "alertDropLevel", 
            "yangName": "alert-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug3DropLevel", 
            "yangName": "debug3-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "emergencyDropLevel", 
            "yangName": "emergency-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug4DropLevel", 
            "yangName": "debug4-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug1DropLevel", 
            "yangName": "debug1-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "criticalDropLevel", 
            "yangName": "critical-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "burstMax", 
            "yangName": "burst-max", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "errorDropLevel", 
            "yangName": "error-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


