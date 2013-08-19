


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class HouseKeeperData(object):

    def __init__ (self):

        self.threadPriority = ""
        self._myHasThreadPriority=False
        
        self.sleepMsec = 0
        self._myHasSleepMsec=False
        
        self.countersUpdateIntervalMsec = 0
        self._myHasCountersUpdateIntervalMsec=False
        
        self.threadAffinity = ""
        self._myHasThreadAffinity=False
        

    def copyFrom (self, other):

        self.threadPriority=other.threadPriority
        self._myHasThreadPriority=other._myHasThreadPriority
        
        self.sleepMsec=other.sleepMsec
        self._myHasSleepMsec=other._myHasSleepMsec
        
        self.countersUpdateIntervalMsec=other.countersUpdateIntervalMsec
        self._myHasCountersUpdateIntervalMsec=other._myHasCountersUpdateIntervalMsec
        
        self.threadAffinity=other.threadAffinity
        self._myHasThreadAffinity=other._myHasThreadAffinity
        
    # has...() methods

    def hasThreadPriority (self):
        return self._myHasThreadPriority

    def hasSleepMsec (self):
        return self._myHasSleepMsec

    def hasCountersUpdateIntervalMsec (self):
        return self._myHasCountersUpdateIntervalMsec

    def hasThreadAffinity (self):
        return self._myHasThreadAffinity


    # setHas...() methods

    def setHasThreadPriority (self):
        self._myHasThreadPriority=True

    def setHasSleepMsec (self):
        self._myHasSleepMsec=True

    def setHasCountersUpdateIntervalMsec (self):
        self._myHasCountersUpdateIntervalMsec=True

    def setHasThreadAffinity (self):
        self._myHasThreadAffinity=True


    def clearAllHas (self):

        self._myHasThreadPriority=False

        self._myHasSleepMsec=False

        self._myHasCountersUpdateIntervalMsec=False

        self._myHasThreadAffinity=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasThreadPriority:
            x = "+"
        leafStr = str(self.threadPriority)
        items.append(x + "ThreadPriority="+leafStr)

        x=""
        if self._myHasSleepMsec:
            x = "+"
        leafStr = str(self.sleepMsec)
        items.append(x + "SleepMsec="+leafStr)

        x=""
        if self._myHasCountersUpdateIntervalMsec:
            x = "+"
        leafStr = str(self.countersUpdateIntervalMsec)
        items.append(x + "CountersUpdateIntervalMsec="+leafStr)

        x=""
        if self._myHasThreadAffinity:
            x = "+"
        leafStr = str(self.threadAffinity)
        items.append(x + "ThreadAffinity="+leafStr)

        return "{HouseKeeperData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "HouseKeeperData", 
        "namespace": "house_keeper", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.dispatcher.house_keeper.house_keeper_data_gen import HouseKeeperData"
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
            "namespace": "dispatcher", 
            "isCurrent": false
        }, 
        {
            "namespace": "house_keeper", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "sleepMsec", 
            "yangName": "sleep-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "countersUpdateIntervalMsec", 
            "yangName": "counters-update-interval-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadAffinity", 
            "yangName": "thread-affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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


