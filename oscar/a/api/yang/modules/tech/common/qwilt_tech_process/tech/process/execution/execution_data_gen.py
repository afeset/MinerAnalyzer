


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ExecutionData(object):

    def __init__ (self):

        self.priority = ""
        self._myHasPriority=False
        
        self.umask = 0
        self._myHasUmask=False
        
        self.affinity = ""
        self._myHasAffinity=False
        

    def copyFrom (self, other):

        self.priority=other.priority
        self._myHasPriority=other._myHasPriority
        
        self.umask=other.umask
        self._myHasUmask=other._myHasUmask
        
        self.affinity=other.affinity
        self._myHasAffinity=other._myHasAffinity
        
    # has...() methods

    def hasPriority (self):
        return self._myHasPriority

    def hasUmask (self):
        return self._myHasUmask

    def hasAffinity (self):
        return self._myHasAffinity


    # setHas...() methods

    def setHasPriority (self):
        self._myHasPriority=True

    def setHasUmask (self):
        self._myHasUmask=True

    def setHasAffinity (self):
        self._myHasAffinity=True


    def clearAllHas (self):

        self._myHasPriority=False

        self._myHasUmask=False

        self._myHasAffinity=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasPriority:
            x = "+"
        leafStr = str(self.priority)
        items.append(x + "Priority="+leafStr)

        x=""
        if self._myHasUmask:
            x = "+"
        leafStr = str(self.umask)
        items.append(x + "Umask="+leafStr)

        x=""
        if self._myHasAffinity:
            x = "+"
        leafStr = str(self.affinity)
        items.append(x + "Affinity="+leafStr)

        return "{ExecutionData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ExecutionData", 
        "namespace": "execution", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.execution_data_gen import ExecutionData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "process", 
            "isCurrent": false
        }, 
        {
            "namespace": "execution", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "priority", 
            "yangName": "priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "umask", 
            "yangName": "umask", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "affinity", 
            "yangName": "affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "qwilt_tech_process"
        ]
    }, 
    "createTime": "2013"
}
"""


