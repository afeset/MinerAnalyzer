


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.content.qwilt_tech_content_line.qwilt_tech_content_line_module_gen import AnalyzerUnitModeType


class SystemDefaultsData(object):

    def __init__ (self):

        self.threadAffinity = ""
        self._myHasThreadAffinity=False
        
        self.idleSleepMsec = 0
        self._myHasIdleSleepMsec=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.mode = AnalyzerUnitModeType.kProcessPackets
        self._myHasMode=False
        
        self.threadPriority = ""
        self._myHasThreadPriority=False
        

    def copyFrom (self, other):

        self.threadAffinity=other.threadAffinity
        self._myHasThreadAffinity=other._myHasThreadAffinity
        
        self.idleSleepMsec=other.idleSleepMsec
        self._myHasIdleSleepMsec=other._myHasIdleSleepMsec
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.mode=other.mode
        self._myHasMode=other._myHasMode
        
        self.threadPriority=other.threadPriority
        self._myHasThreadPriority=other._myHasThreadPriority
        
    # has...() methods

    def hasThreadAffinity (self):
        return self._myHasThreadAffinity

    def hasIdleSleepMsec (self):
        return self._myHasIdleSleepMsec

    def hasEnabled (self):
        return self._myHasEnabled

    def hasMode (self):
        return self._myHasMode

    def hasThreadPriority (self):
        return self._myHasThreadPriority


    # setHas...() methods

    def setHasThreadAffinity (self):
        self._myHasThreadAffinity=True

    def setHasIdleSleepMsec (self):
        self._myHasIdleSleepMsec=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasMode (self):
        self._myHasMode=True

    def setHasThreadPriority (self):
        self._myHasThreadPriority=True


    def clearAllHas (self):

        self._myHasThreadAffinity=False

        self._myHasIdleSleepMsec=False

        self._myHasEnabled=False

        self._myHasMode=False

        self._myHasThreadPriority=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasThreadAffinity:
            x = "+"
        leafStr = str(self.threadAffinity)
        items.append(x + "ThreadAffinity="+leafStr)

        x=""
        if self._myHasIdleSleepMsec:
            x = "+"
        leafStr = str(self.idleSleepMsec)
        items.append(x + "IdleSleepMsec="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasMode:
            x = "+"
        leafStr = str(self.mode)
        items.append(x + "Mode="+leafStr)

        x=""
        if self._myHasThreadPriority:
            x = "+"
        leafStr = str(self.threadPriority)
        items.append(x + "ThreadPriority="+leafStr)

        return "{SystemDefaultsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemDefaultsData", 
        "namespace": "system_defaults", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.system_defaults.system_defaults_data_gen import SystemDefaultsData"
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
            "namespace": "analyzer", 
            "isCurrent": false
        }, 
        {
            "namespace": "unit", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadAffinity", 
            "yangName": "thread-affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "idleSleepMsec", 
            "yangName": "idle-sleep-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mode", 
            "yangName": "mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "process-packets", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
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


