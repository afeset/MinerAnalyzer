


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

        self.pollLatencyErrorSeconds = 0
        self._myHasPollLatencyErrorSeconds=False
        
        self.pollLatencyWarningSeconds = 0
        self._myHasPollLatencyWarningSeconds=False
        

    def copyFrom (self, other):

        self.pollLatencyErrorSeconds=other.pollLatencyErrorSeconds
        self._myHasPollLatencyErrorSeconds=other._myHasPollLatencyErrorSeconds
        
        self.pollLatencyWarningSeconds=other.pollLatencyWarningSeconds
        self._myHasPollLatencyWarningSeconds=other._myHasPollLatencyWarningSeconds
        
    # has...() methods

    def hasPollLatencyErrorSeconds (self):
        return self._myHasPollLatencyErrorSeconds

    def hasPollLatencyWarningSeconds (self):
        return self._myHasPollLatencyWarningSeconds


    # setHas...() methods

    def setHasPollLatencyErrorSeconds (self):
        self._myHasPollLatencyErrorSeconds=True

    def setHasPollLatencyWarningSeconds (self):
        self._myHasPollLatencyWarningSeconds=True


    def clearAllHas (self):

        self._myHasPollLatencyErrorSeconds=False

        self._myHasPollLatencyWarningSeconds=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasPollLatencyErrorSeconds:
            x = "+"
        leafStr = str(self.pollLatencyErrorSeconds)
        items.append(x + "PollLatencyErrorSeconds="+leafStr)

        x=""
        if self._myHasPollLatencyWarningSeconds:
            x = "+"
        leafStr = str(self.pollLatencyWarningSeconds)
        items.append(x + "PollLatencyWarningSeconds="+leafStr)

        return "{ThresholdsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ThresholdsData", 
        "namespace": "thresholds", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.system_defaults.housekeeper.thresholds.thresholds_data_gen import ThresholdsData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "log", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "housekeeper", 
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
            "memberName": "pollLatencyErrorSeconds", 
            "yangName": "poll-latency-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarningSeconds", 
            "yangName": "poll-latency-warning-seconds", 
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
            "debug", 
            "qwilt_tech_log"
        ]
    }, 
    "createTime": "2013"
}
"""


