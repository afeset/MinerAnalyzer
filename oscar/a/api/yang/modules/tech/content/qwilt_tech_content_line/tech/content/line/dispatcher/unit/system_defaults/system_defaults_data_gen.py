


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SystemDefaultsData(object):

    def __init__ (self):

        self.threadPriority = ""
        self._myHasThreadPriority=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.threadAffinity = ""
        self._myHasThreadAffinity=False
        

    def copyFrom (self, other):

        self.threadPriority=other.threadPriority
        self._myHasThreadPriority=other._myHasThreadPriority
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.threadAffinity=other.threadAffinity
        self._myHasThreadAffinity=other._myHasThreadAffinity
        
    # has...() methods

    def hasThreadPriority (self):
        return self._myHasThreadPriority

    def hasEnabled (self):
        return self._myHasEnabled

    def hasThreadAffinity (self):
        return self._myHasThreadAffinity


    # setHas...() methods

    def setHasThreadPriority (self):
        self._myHasThreadPriority=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasThreadAffinity (self):
        self._myHasThreadAffinity=True


    def clearAllHas (self):

        self._myHasThreadPriority=False

        self._myHasEnabled=False

        self._myHasThreadAffinity=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasThreadPriority:
            x = "+"
        leafStr = str(self.threadPriority)
        items.append(x + "ThreadPriority="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasThreadAffinity:
            x = "+"
        leafStr = str(self.threadAffinity)
        items.append(x + "ThreadAffinity="+leafStr)

        return "{SystemDefaultsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemDefaultsData", 
        "namespace": "system_defaults", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.unit.system_defaults.system_defaults_data_gen import SystemDefaultsData"
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
            "namespace": "dispatcher", 
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
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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


