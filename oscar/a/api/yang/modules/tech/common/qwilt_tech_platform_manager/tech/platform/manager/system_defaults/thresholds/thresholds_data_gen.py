


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ThresholdsData(object):

    def __init__ (self):

        self.pollLatencyError = 0
        self._myHasPollLatencyError=False
        
        self.overallPollDurationWarning = 0
        self._myHasOverallPollDurationWarning=False
        
        self.pollLatencyWarning = 0
        self._myHasPollLatencyWarning=False
        
        self.singlePollDurationWarning = 0
        self._myHasSinglePollDurationWarning=False
        
        self.singlePollDurationError = 0
        self._myHasSinglePollDurationError=False
        
        self.overallPollDurationError = 0
        self._myHasOverallPollDurationError=False
        

    def copyFrom (self, other):

        self.pollLatencyError=other.pollLatencyError
        self._myHasPollLatencyError=other._myHasPollLatencyError
        
        self.overallPollDurationWarning=other.overallPollDurationWarning
        self._myHasOverallPollDurationWarning=other._myHasOverallPollDurationWarning
        
        self.pollLatencyWarning=other.pollLatencyWarning
        self._myHasPollLatencyWarning=other._myHasPollLatencyWarning
        
        self.singlePollDurationWarning=other.singlePollDurationWarning
        self._myHasSinglePollDurationWarning=other._myHasSinglePollDurationWarning
        
        self.singlePollDurationError=other.singlePollDurationError
        self._myHasSinglePollDurationError=other._myHasSinglePollDurationError
        
        self.overallPollDurationError=other.overallPollDurationError
        self._myHasOverallPollDurationError=other._myHasOverallPollDurationError
        
    # has...() methods

    def hasPollLatencyError (self):
        return self._myHasPollLatencyError

    def hasOverallPollDurationWarning (self):
        return self._myHasOverallPollDurationWarning

    def hasPollLatencyWarning (self):
        return self._myHasPollLatencyWarning

    def hasSinglePollDurationWarning (self):
        return self._myHasSinglePollDurationWarning

    def hasSinglePollDurationError (self):
        return self._myHasSinglePollDurationError

    def hasOverallPollDurationError (self):
        return self._myHasOverallPollDurationError


    # setHas...() methods

    def setHasPollLatencyError (self):
        self._myHasPollLatencyError=True

    def setHasOverallPollDurationWarning (self):
        self._myHasOverallPollDurationWarning=True

    def setHasPollLatencyWarning (self):
        self._myHasPollLatencyWarning=True

    def setHasSinglePollDurationWarning (self):
        self._myHasSinglePollDurationWarning=True

    def setHasSinglePollDurationError (self):
        self._myHasSinglePollDurationError=True

    def setHasOverallPollDurationError (self):
        self._myHasOverallPollDurationError=True


    def clearAllHas (self):

        self._myHasPollLatencyError=False

        self._myHasOverallPollDurationWarning=False

        self._myHasPollLatencyWarning=False

        self._myHasSinglePollDurationWarning=False

        self._myHasSinglePollDurationError=False

        self._myHasOverallPollDurationError=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasPollLatencyError:
            x = "+"
        leafStr = str(self.pollLatencyError)
        items.append(x + "PollLatencyError="+leafStr)

        x=""
        if self._myHasOverallPollDurationWarning:
            x = "+"
        leafStr = str(self.overallPollDurationWarning)
        items.append(x + "OverallPollDurationWarning="+leafStr)

        x=""
        if self._myHasPollLatencyWarning:
            x = "+"
        leafStr = str(self.pollLatencyWarning)
        items.append(x + "PollLatencyWarning="+leafStr)

        x=""
        if self._myHasSinglePollDurationWarning:
            x = "+"
        leafStr = str(self.singlePollDurationWarning)
        items.append(x + "SinglePollDurationWarning="+leafStr)

        x=""
        if self._myHasSinglePollDurationError:
            x = "+"
        leafStr = str(self.singlePollDurationError)
        items.append(x + "SinglePollDurationError="+leafStr)

        x=""
        if self._myHasOverallPollDurationError:
            x = "+"
        leafStr = str(self.overallPollDurationError)
        items.append(x + "OverallPollDurationError="+leafStr)

        return "{ThresholdsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ThresholdsData", 
        "namespace": "thresholds", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.system_defaults.thresholds.thresholds_data_gen import ThresholdsData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "platform", 
            "isCurrent": false
        }, 
        {
            "namespace": "manager", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "thresholds", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyError", 
            "yangName": "poll-latency-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationWarning", 
            "yangName": "overall-poll-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarning", 
            "yangName": "poll-latency-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationWarning", 
            "yangName": "single-poll-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationError", 
            "yangName": "single-poll-duration-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationError", 
            "yangName": "overall-poll-duration-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
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
            "common", 
            "qwilt_tech_platform_manager"
        ]
    }, 
    "createTime": "2013"
}
"""


