


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.content.qwilt_tech_content_line_types.qwilt_tech_content_line_types_module_gen import AcquisitionAlgorithmType


class ControllerData(object):

    def __init__ (self):

        self.lazyFileOpen = False
        self._myHasLazyFileOpen=False
        
        self.logPeriodicStats = False
        self._myHasLogPeriodicStats=False
        
        self.maxSessions = 0
        self._myHasMaxSessions=False
        
        self.sessionQueueLowWaterMarkPercent = 0
        self._myHasSessionQueueLowWaterMarkPercent=False
        
        self.maxActiveSessions = 0
        self._myHasMaxActiveSessions=False
        
        self.algorithm = AcquisitionAlgorithmType.kPassThrough
        self._myHasAlgorithm=False
        

    def copyFrom (self, other):

        self.lazyFileOpen=other.lazyFileOpen
        self._myHasLazyFileOpen=other._myHasLazyFileOpen
        
        self.logPeriodicStats=other.logPeriodicStats
        self._myHasLogPeriodicStats=other._myHasLogPeriodicStats
        
        self.maxSessions=other.maxSessions
        self._myHasMaxSessions=other._myHasMaxSessions
        
        self.sessionQueueLowWaterMarkPercent=other.sessionQueueLowWaterMarkPercent
        self._myHasSessionQueueLowWaterMarkPercent=other._myHasSessionQueueLowWaterMarkPercent
        
        self.maxActiveSessions=other.maxActiveSessions
        self._myHasMaxActiveSessions=other._myHasMaxActiveSessions
        
        self.algorithm=other.algorithm
        self._myHasAlgorithm=other._myHasAlgorithm
        
    # has...() methods

    def hasLazyFileOpen (self):
        return self._myHasLazyFileOpen

    def hasLogPeriodicStats (self):
        return self._myHasLogPeriodicStats

    def hasMaxSessions (self):
        return self._myHasMaxSessions

    def hasSessionQueueLowWaterMarkPercent (self):
        return self._myHasSessionQueueLowWaterMarkPercent

    def hasMaxActiveSessions (self):
        return self._myHasMaxActiveSessions

    def hasAlgorithm (self):
        return self._myHasAlgorithm


    # setHas...() methods

    def setHasLazyFileOpen (self):
        self._myHasLazyFileOpen=True

    def setHasLogPeriodicStats (self):
        self._myHasLogPeriodicStats=True

    def setHasMaxSessions (self):
        self._myHasMaxSessions=True

    def setHasSessionQueueLowWaterMarkPercent (self):
        self._myHasSessionQueueLowWaterMarkPercent=True

    def setHasMaxActiveSessions (self):
        self._myHasMaxActiveSessions=True

    def setHasAlgorithm (self):
        self._myHasAlgorithm=True


    def clearAllHas (self):

        self._myHasLazyFileOpen=False

        self._myHasLogPeriodicStats=False

        self._myHasMaxSessions=False

        self._myHasSessionQueueLowWaterMarkPercent=False

        self._myHasMaxActiveSessions=False

        self._myHasAlgorithm=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasLazyFileOpen:
            x = "+"
        leafStr = str(self.lazyFileOpen)
        items.append(x + "LazyFileOpen="+leafStr)

        x=""
        if self._myHasLogPeriodicStats:
            x = "+"
        leafStr = str(self.logPeriodicStats)
        items.append(x + "LogPeriodicStats="+leafStr)

        x=""
        if self._myHasMaxSessions:
            x = "+"
        leafStr = str(self.maxSessions)
        items.append(x + "MaxSessions="+leafStr)

        x=""
        if self._myHasSessionQueueLowWaterMarkPercent:
            x = "+"
        leafStr = str(self.sessionQueueLowWaterMarkPercent)
        items.append(x + "SessionQueueLowWaterMarkPercent="+leafStr)

        x=""
        if self._myHasMaxActiveSessions:
            x = "+"
        leafStr = str(self.maxActiveSessions)
        items.append(x + "MaxActiveSessions="+leafStr)

        x=""
        if self._myHasAlgorithm:
            x = "+"
        leafStr = str(self.algorithm)
        items.append(x + "Algorithm="+leafStr)

        return "{ControllerData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ControllerData", 
        "namespace": "controller", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.acquisition.controller.controller_data_gen import ControllerData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "content", 
            "isCurrent": false
        }, 
        {
            "namespace": "line", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "analyzer", 
            "isCurrent": false
        }, 
        {
            "namespace": "acquisition", 
            "isCurrent": false
        }, 
        {
            "namespace": "controller", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "lazyFileOpen", 
            "yangName": "lazy-file-open", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "logPeriodicStats", 
            "yangName": "log-periodic-stats", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessions", 
            "yangName": "max-sessions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "sessionQueueLowWaterMarkPercent", 
            "yangName": "session-queue-low-water-mark-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxActiveSessions", 
            "yangName": "max-active-sessions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "algorithm", 
            "yangName": "algorithm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "createTime": "2013"
}
"""


