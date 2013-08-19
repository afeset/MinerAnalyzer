


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ManagerData(object):

    def __init__ (self):

        self.enabled = False
        self._myHasEnabled=False
        
        self.pollIntervalSeconds = 0
        self._myHasPollIntervalSeconds=False
        

    def copyFrom (self, other):

        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.pollIntervalSeconds=other.pollIntervalSeconds
        self._myHasPollIntervalSeconds=other._myHasPollIntervalSeconds
        
    # has...() methods

    def hasEnabled (self):
        return self._myHasEnabled

    def hasPollIntervalSeconds (self):
        return self._myHasPollIntervalSeconds


    # setHas...() methods

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasPollIntervalSeconds (self):
        self._myHasPollIntervalSeconds=True


    def clearAllHas (self):

        self._myHasEnabled=False

        self._myHasPollIntervalSeconds=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasPollIntervalSeconds:
            x = "+"
        leafStr = str(self.pollIntervalSeconds)
        items.append(x + "PollIntervalSeconds="+leafStr)

        return "{ManagerData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ManagerData", 
        "namespace": "manager", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.manager_data_gen import ManagerData"
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollIntervalSeconds", 
            "yangName": "poll-interval-seconds", 
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
            "qwilt_tech_platform_manager"
        ]
    }, 
    "createTime": "2013"
}
"""


