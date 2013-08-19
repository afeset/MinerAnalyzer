


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class UnitData(object):

    def __init__ (self):

        self.threadPriority = ""
        self._myHasThreadPriority=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.name = ""
        self._myHasName=False
        
        self.threadAffinity = ""
        self._myHasThreadAffinity=False
        

    def copyFrom (self, other):

        self.threadPriority=other.threadPriority
        self._myHasThreadPriority=other._myHasThreadPriority
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.name=other.name
        self._myHasName=other._myHasName
        
        self.threadAffinity=other.threadAffinity
        self._myHasThreadAffinity=other._myHasThreadAffinity
        
    # has...() methods

    def hasThreadPriority (self):
        return self._myHasThreadPriority

    def hasEnabled (self):
        return self._myHasEnabled

    def hasName (self):
        return self._myHasName

    def hasThreadAffinity (self):
        return self._myHasThreadAffinity


    # setHas...() methods

    def setHasThreadPriority (self):
        self._myHasThreadPriority=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasName (self):
        self._myHasName=True

    def setHasThreadAffinity (self):
        self._myHasThreadAffinity=True


    def clearAllHas (self):

        self._myHasThreadPriority=False

        self._myHasEnabled=False

        self._myHasName=False

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
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasThreadAffinity:
            x = "+"
        leafStr = str(self.threadAffinity)
        items.append(x + "ThreadAffinity="+leafStr)

        return "{UnitData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "UnitData", 
        "namespace": "unit", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.unit.unit_data_gen import UnitData"
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
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadAffinity", 
            "yangName": "thread-affinity", 
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


