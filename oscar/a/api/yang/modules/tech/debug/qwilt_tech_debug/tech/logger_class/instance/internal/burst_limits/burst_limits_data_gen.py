


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class BurstLimitsData(object):

    def __init__ (self):

        self.infoDropLevel = 0
        self._myHasInfoDropLevel=False
        
        self.debug2DropLevel = 0
        self._myHasDebug2DropLevel=False
        
        self.noticeDropLevel = 0
        self._myHasNoticeDropLevel=False
        
        self.debug5DropLevel = 0
        self._myHasDebug5DropLevel=False
        
        self.warningDropLevel = 0
        self._myHasWarningDropLevel=False
        
        self.alertDropLevel = 0
        self._myHasAlertDropLevel=False
        
        self.debug3DropLevel = 0
        self._myHasDebug3DropLevel=False
        
        self.emergencyDropLevel = 0
        self._myHasEmergencyDropLevel=False
        
        self.debug4DropLevel = 0
        self._myHasDebug4DropLevel=False
        
        self.debug1DropLevel = 0
        self._myHasDebug1DropLevel=False
        
        self.criticalDropLevel = 0
        self._myHasCriticalDropLevel=False
        
        self.burstMax = 0
        self._myHasBurstMax=False
        
        self.errorDropLevel = 0
        self._myHasErrorDropLevel=False
        

    def copyFrom (self, other):

        self.infoDropLevel=other.infoDropLevel
        self._myHasInfoDropLevel=other._myHasInfoDropLevel
        
        self.debug2DropLevel=other.debug2DropLevel
        self._myHasDebug2DropLevel=other._myHasDebug2DropLevel
        
        self.noticeDropLevel=other.noticeDropLevel
        self._myHasNoticeDropLevel=other._myHasNoticeDropLevel
        
        self.debug5DropLevel=other.debug5DropLevel
        self._myHasDebug5DropLevel=other._myHasDebug5DropLevel
        
        self.warningDropLevel=other.warningDropLevel
        self._myHasWarningDropLevel=other._myHasWarningDropLevel
        
        self.alertDropLevel=other.alertDropLevel
        self._myHasAlertDropLevel=other._myHasAlertDropLevel
        
        self.debug3DropLevel=other.debug3DropLevel
        self._myHasDebug3DropLevel=other._myHasDebug3DropLevel
        
        self.emergencyDropLevel=other.emergencyDropLevel
        self._myHasEmergencyDropLevel=other._myHasEmergencyDropLevel
        
        self.debug4DropLevel=other.debug4DropLevel
        self._myHasDebug4DropLevel=other._myHasDebug4DropLevel
        
        self.debug1DropLevel=other.debug1DropLevel
        self._myHasDebug1DropLevel=other._myHasDebug1DropLevel
        
        self.criticalDropLevel=other.criticalDropLevel
        self._myHasCriticalDropLevel=other._myHasCriticalDropLevel
        
        self.burstMax=other.burstMax
        self._myHasBurstMax=other._myHasBurstMax
        
        self.errorDropLevel=other.errorDropLevel
        self._myHasErrorDropLevel=other._myHasErrorDropLevel
        
    # has...() methods

    def hasInfoDropLevel (self):
        return self._myHasInfoDropLevel

    def hasDebug2DropLevel (self):
        return self._myHasDebug2DropLevel

    def hasNoticeDropLevel (self):
        return self._myHasNoticeDropLevel

    def hasDebug5DropLevel (self):
        return self._myHasDebug5DropLevel

    def hasWarningDropLevel (self):
        return self._myHasWarningDropLevel

    def hasAlertDropLevel (self):
        return self._myHasAlertDropLevel

    def hasDebug3DropLevel (self):
        return self._myHasDebug3DropLevel

    def hasEmergencyDropLevel (self):
        return self._myHasEmergencyDropLevel

    def hasDebug4DropLevel (self):
        return self._myHasDebug4DropLevel

    def hasDebug1DropLevel (self):
        return self._myHasDebug1DropLevel

    def hasCriticalDropLevel (self):
        return self._myHasCriticalDropLevel

    def hasBurstMax (self):
        return self._myHasBurstMax

    def hasErrorDropLevel (self):
        return self._myHasErrorDropLevel


    # setHas...() methods

    def setHasInfoDropLevel (self):
        self._myHasInfoDropLevel=True

    def setHasDebug2DropLevel (self):
        self._myHasDebug2DropLevel=True

    def setHasNoticeDropLevel (self):
        self._myHasNoticeDropLevel=True

    def setHasDebug5DropLevel (self):
        self._myHasDebug5DropLevel=True

    def setHasWarningDropLevel (self):
        self._myHasWarningDropLevel=True

    def setHasAlertDropLevel (self):
        self._myHasAlertDropLevel=True

    def setHasDebug3DropLevel (self):
        self._myHasDebug3DropLevel=True

    def setHasEmergencyDropLevel (self):
        self._myHasEmergencyDropLevel=True

    def setHasDebug4DropLevel (self):
        self._myHasDebug4DropLevel=True

    def setHasDebug1DropLevel (self):
        self._myHasDebug1DropLevel=True

    def setHasCriticalDropLevel (self):
        self._myHasCriticalDropLevel=True

    def setHasBurstMax (self):
        self._myHasBurstMax=True

    def setHasErrorDropLevel (self):
        self._myHasErrorDropLevel=True


    def clearAllHas (self):

        self._myHasInfoDropLevel=False

        self._myHasDebug2DropLevel=False

        self._myHasNoticeDropLevel=False

        self._myHasDebug5DropLevel=False

        self._myHasWarningDropLevel=False

        self._myHasAlertDropLevel=False

        self._myHasDebug3DropLevel=False

        self._myHasEmergencyDropLevel=False

        self._myHasDebug4DropLevel=False

        self._myHasDebug1DropLevel=False

        self._myHasCriticalDropLevel=False

        self._myHasBurstMax=False

        self._myHasErrorDropLevel=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasInfoDropLevel:
            x = "+"
        leafStr = str(self.infoDropLevel)
        items.append(x + "InfoDropLevel="+leafStr)

        x=""
        if self._myHasDebug2DropLevel:
            x = "+"
        leafStr = str(self.debug2DropLevel)
        items.append(x + "Debug2DropLevel="+leafStr)

        x=""
        if self._myHasNoticeDropLevel:
            x = "+"
        leafStr = str(self.noticeDropLevel)
        items.append(x + "NoticeDropLevel="+leafStr)

        x=""
        if self._myHasDebug5DropLevel:
            x = "+"
        leafStr = str(self.debug5DropLevel)
        items.append(x + "Debug5DropLevel="+leafStr)

        x=""
        if self._myHasWarningDropLevel:
            x = "+"
        leafStr = str(self.warningDropLevel)
        items.append(x + "WarningDropLevel="+leafStr)

        x=""
        if self._myHasAlertDropLevel:
            x = "+"
        leafStr = str(self.alertDropLevel)
        items.append(x + "AlertDropLevel="+leafStr)

        x=""
        if self._myHasDebug3DropLevel:
            x = "+"
        leafStr = str(self.debug3DropLevel)
        items.append(x + "Debug3DropLevel="+leafStr)

        x=""
        if self._myHasEmergencyDropLevel:
            x = "+"
        leafStr = str(self.emergencyDropLevel)
        items.append(x + "EmergencyDropLevel="+leafStr)

        x=""
        if self._myHasDebug4DropLevel:
            x = "+"
        leafStr = str(self.debug4DropLevel)
        items.append(x + "Debug4DropLevel="+leafStr)

        x=""
        if self._myHasDebug1DropLevel:
            x = "+"
        leafStr = str(self.debug1DropLevel)
        items.append(x + "Debug1DropLevel="+leafStr)

        x=""
        if self._myHasCriticalDropLevel:
            x = "+"
        leafStr = str(self.criticalDropLevel)
        items.append(x + "CriticalDropLevel="+leafStr)

        x=""
        if self._myHasBurstMax:
            x = "+"
        leafStr = str(self.burstMax)
        items.append(x + "BurstMax="+leafStr)

        x=""
        if self._myHasErrorDropLevel:
            x = "+"
        leafStr = str(self.errorDropLevel)
        items.append(x + "ErrorDropLevel="+leafStr)

        return "{BurstLimitsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "BurstLimitsData", 
        "namespace": "burst_limits", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.internal.burst_limits.burst_limits_data_gen import BurstLimitsData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "logger_class", 
            "isCurrent": false
        }, 
        {
            "namespace": "instance", 
            "isCurrent": false
        }, 
        {
            "namespace": "internal", 
            "isCurrent": false
        }, 
        {
            "namespace": "burst_limits", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "infoDropLevel", 
            "yangName": "info-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug2DropLevel", 
            "yangName": "debug2-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "noticeDropLevel", 
            "yangName": "notice-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug5DropLevel", 
            "yangName": "debug5-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "warningDropLevel", 
            "yangName": "warning-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "alertDropLevel", 
            "yangName": "alert-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug3DropLevel", 
            "yangName": "debug3-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "emergencyDropLevel", 
            "yangName": "emergency-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug4DropLevel", 
            "yangName": "debug4-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "debug1DropLevel", 
            "yangName": "debug1-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "criticalDropLevel", 
            "yangName": "critical-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "burstMax", 
            "yangName": "burst-max", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "errorDropLevel", 
            "yangName": "error-drop-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "module": {}, 
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
    "createTime": "2013"
}
"""


