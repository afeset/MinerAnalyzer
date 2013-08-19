


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.content.qwilt_tech_content_line.qwilt_tech_content_line_module_gen import AnalyzerUnitModeType


class UnitData(object):

    def __init__ (self):

        self.threadAffinity = ""
        self._myHasThreadAffinity=False
        
        self.name = ""
        self._myHasName=False
        
        self.idleSleepMsec = 0
        self._myHasIdleSleepMsec=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.threadPriority = ""
        self._myHasThreadPriority=False
        
        self.mode = AnalyzerUnitModeType.kProcessPackets
        self._myHasMode=False
        

    def copyFrom (self, other):

        self.threadAffinity=other.threadAffinity
        self._myHasThreadAffinity=other._myHasThreadAffinity
        
        self.name=other.name
        self._myHasName=other._myHasName
        
        self.idleSleepMsec=other.idleSleepMsec
        self._myHasIdleSleepMsec=other._myHasIdleSleepMsec
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.threadPriority=other.threadPriority
        self._myHasThreadPriority=other._myHasThreadPriority
        
        self.mode=other.mode
        self._myHasMode=other._myHasMode
        
    # has...() methods

    def hasThreadAffinity (self):
        return self._myHasThreadAffinity

    def hasName (self):
        return self._myHasName

    def hasIdleSleepMsec (self):
        return self._myHasIdleSleepMsec

    def hasEnabled (self):
        return self._myHasEnabled

    def hasThreadPriority (self):
        return self._myHasThreadPriority

    def hasMode (self):
        return self._myHasMode


    # setHas...() methods

    def setHasThreadAffinity (self):
        self._myHasThreadAffinity=True

    def setHasName (self):
        self._myHasName=True

    def setHasIdleSleepMsec (self):
        self._myHasIdleSleepMsec=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasThreadPriority (self):
        self._myHasThreadPriority=True

    def setHasMode (self):
        self._myHasMode=True


    def clearAllHas (self):

        self._myHasThreadAffinity=False

        self._myHasName=False

        self._myHasIdleSleepMsec=False

        self._myHasEnabled=False

        self._myHasThreadPriority=False

        self._myHasMode=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasThreadAffinity:
            x = "+"
        leafStr = str(self.threadAffinity)
        items.append(x + "ThreadAffinity="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

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
        if self._myHasThreadPriority:
            x = "+"
        leafStr = str(self.threadPriority)
        items.append(x + "ThreadPriority="+leafStr)

        x=""
        if self._myHasMode:
            x = "+"
        leafStr = str(self.mode)
        items.append(x + "Mode="+leafStr)

        return "{UnitData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "UnitData", 
        "namespace": "unit", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.unit_data_gen import UnitData"
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "idleSleepMsec", 
            "yangName": "idle-sleep-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mode", 
            "yangName": "mode", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "createTime": "2013"
}
"""


