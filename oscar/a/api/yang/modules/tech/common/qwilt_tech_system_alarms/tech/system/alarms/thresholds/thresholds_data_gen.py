


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

        self.singlePollDurationWarningMsec = 0
        self._myHasSinglePollDurationWarningMsec=False
        
        self.pollLatencyErrorSeconds = 0
        self._myHasPollLatencyErrorSeconds=False
        
        self.singlePollDurationErrorMsec = 0
        self._myHasSinglePollDurationErrorMsec=False
        
        self.overallPollDurationErrorMsec = 0
        self._myHasOverallPollDurationErrorMsec=False
        
        self.pollLatencyWarningSeconds = 0
        self._myHasPollLatencyWarningSeconds=False
        
        self.overallPollDurationWarningMsec = 0
        self._myHasOverallPollDurationWarningMsec=False
        

    def copyFrom (self, other):

        self.singlePollDurationWarningMsec=other.singlePollDurationWarningMsec
        self._myHasSinglePollDurationWarningMsec=other._myHasSinglePollDurationWarningMsec
        
        self.pollLatencyErrorSeconds=other.pollLatencyErrorSeconds
        self._myHasPollLatencyErrorSeconds=other._myHasPollLatencyErrorSeconds
        
        self.singlePollDurationErrorMsec=other.singlePollDurationErrorMsec
        self._myHasSinglePollDurationErrorMsec=other._myHasSinglePollDurationErrorMsec
        
        self.overallPollDurationErrorMsec=other.overallPollDurationErrorMsec
        self._myHasOverallPollDurationErrorMsec=other._myHasOverallPollDurationErrorMsec
        
        self.pollLatencyWarningSeconds=other.pollLatencyWarningSeconds
        self._myHasPollLatencyWarningSeconds=other._myHasPollLatencyWarningSeconds
        
        self.overallPollDurationWarningMsec=other.overallPollDurationWarningMsec
        self._myHasOverallPollDurationWarningMsec=other._myHasOverallPollDurationWarningMsec
        
    # has...() methods

    def hasSinglePollDurationWarningMsec (self):
        return self._myHasSinglePollDurationWarningMsec

    def hasPollLatencyErrorSeconds (self):
        return self._myHasPollLatencyErrorSeconds

    def hasSinglePollDurationErrorMsec (self):
        return self._myHasSinglePollDurationErrorMsec

    def hasOverallPollDurationErrorMsec (self):
        return self._myHasOverallPollDurationErrorMsec

    def hasPollLatencyWarningSeconds (self):
        return self._myHasPollLatencyWarningSeconds

    def hasOverallPollDurationWarningMsec (self):
        return self._myHasOverallPollDurationWarningMsec


    # setHas...() methods

    def setHasSinglePollDurationWarningMsec (self):
        self._myHasSinglePollDurationWarningMsec=True

    def setHasPollLatencyErrorSeconds (self):
        self._myHasPollLatencyErrorSeconds=True

    def setHasSinglePollDurationErrorMsec (self):
        self._myHasSinglePollDurationErrorMsec=True

    def setHasOverallPollDurationErrorMsec (self):
        self._myHasOverallPollDurationErrorMsec=True

    def setHasPollLatencyWarningSeconds (self):
        self._myHasPollLatencyWarningSeconds=True

    def setHasOverallPollDurationWarningMsec (self):
        self._myHasOverallPollDurationWarningMsec=True


    def clearAllHas (self):

        self._myHasSinglePollDurationWarningMsec=False

        self._myHasPollLatencyErrorSeconds=False

        self._myHasSinglePollDurationErrorMsec=False

        self._myHasOverallPollDurationErrorMsec=False

        self._myHasPollLatencyWarningSeconds=False

        self._myHasOverallPollDurationWarningMsec=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasSinglePollDurationWarningMsec:
            x = "+"
        leafStr = str(self.singlePollDurationWarningMsec)
        items.append(x + "SinglePollDurationWarningMsec="+leafStr)

        x=""
        if self._myHasPollLatencyErrorSeconds:
            x = "+"
        leafStr = str(self.pollLatencyErrorSeconds)
        items.append(x + "PollLatencyErrorSeconds="+leafStr)

        x=""
        if self._myHasSinglePollDurationErrorMsec:
            x = "+"
        leafStr = str(self.singlePollDurationErrorMsec)
        items.append(x + "SinglePollDurationErrorMsec="+leafStr)

        x=""
        if self._myHasOverallPollDurationErrorMsec:
            x = "+"
        leafStr = str(self.overallPollDurationErrorMsec)
        items.append(x + "OverallPollDurationErrorMsec="+leafStr)

        x=""
        if self._myHasPollLatencyWarningSeconds:
            x = "+"
        leafStr = str(self.pollLatencyWarningSeconds)
        items.append(x + "PollLatencyWarningSeconds="+leafStr)

        x=""
        if self._myHasOverallPollDurationWarningMsec:
            x = "+"
        leafStr = str(self.overallPollDurationWarningMsec)
        items.append(x + "OverallPollDurationWarningMsec="+leafStr)

        return "{ThresholdsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ThresholdsData", 
        "namespace": "thresholds", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.thresholds.thresholds_data_gen import ThresholdsData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "system", 
            "isCurrent": false
        }, 
        {
            "namespace": "alarms", 
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
            "memberName": "singlePollDurationWarningMsec", 
            "yangName": "single-poll-duration-warning-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyErrorSeconds", 
            "yangName": "poll-latency-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationErrorMsec", 
            "yangName": "single-poll-duration-error-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationErrorMsec", 
            "yangName": "overall-poll-duration-error-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarningSeconds", 
            "yangName": "poll-latency-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationWarningMsec", 
            "yangName": "overall-poll-duration-warning-msec", 
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
            "common", 
            "qwilt_tech_system_alarms"
        ]
    }, 
    "createTime": "2013"
}
"""


