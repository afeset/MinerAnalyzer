


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class AlarmsData(object):

    def __init__ (self):

        self.enabled = False
        self._myHasEnabled=False
        
        self.raiseTestAlarm = False
        self._myHasRaiseTestAlarm=False
        
        self.pollInterval = 0
        self._myHasPollInterval=False
        

    def copyFrom (self, other):

        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.raiseTestAlarm=other.raiseTestAlarm
        self._myHasRaiseTestAlarm=other._myHasRaiseTestAlarm
        
        self.pollInterval=other.pollInterval
        self._myHasPollInterval=other._myHasPollInterval
        
    # has...() methods

    def hasEnabled (self):
        return self._myHasEnabled

    def hasRaiseTestAlarm (self):
        return self._myHasRaiseTestAlarm

    def hasPollInterval (self):
        return self._myHasPollInterval


    # setHas...() methods

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasRaiseTestAlarm (self):
        self._myHasRaiseTestAlarm=True

    def setHasPollInterval (self):
        self._myHasPollInterval=True


    def clearAllHas (self):

        self._myHasEnabled=False

        self._myHasRaiseTestAlarm=False

        self._myHasPollInterval=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasRaiseTestAlarm:
            x = "+"
        leafStr = str(self.raiseTestAlarm)
        items.append(x + "RaiseTestAlarm="+leafStr)

        x=""
        if self._myHasPollInterval:
            x = "+"
        leafStr = str(self.pollInterval)
        items.append(x + "PollInterval="+leafStr)

        return "{AlarmsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "AlarmsData", 
        "namespace": "alarms", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.alarms_data_gen import AlarmsData"
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
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "raiseTestAlarm", 
            "yangName": "raise-test-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
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


