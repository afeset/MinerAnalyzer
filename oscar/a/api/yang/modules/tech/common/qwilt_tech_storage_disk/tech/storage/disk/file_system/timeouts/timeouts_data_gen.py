


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class TimeoutsData(object):

    def __init__ (self):

        self.activate = 0
        self._myHasActivate=False
        
        self.getStatus = 0
        self._myHasGetStatus=False
        

    def copyFrom (self, other):

        self.activate=other.activate
        self._myHasActivate=other._myHasActivate
        
        self.getStatus=other.getStatus
        self._myHasGetStatus=other._myHasGetStatus
        
    # has...() methods

    def hasActivate (self):
        return self._myHasActivate

    def hasGetStatus (self):
        return self._myHasGetStatus


    # setHas...() methods

    def setHasActivate (self):
        self._myHasActivate=True

    def setHasGetStatus (self):
        self._myHasGetStatus=True


    def clearAllHas (self):

        self._myHasActivate=False

        self._myHasGetStatus=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasActivate:
            x = "+"
        leafStr = str(self.activate)
        items.append(x + "Activate="+leafStr)

        x=""
        if self._myHasGetStatus:
            x = "+"
        leafStr = str(self.getStatus)
        items.append(x + "GetStatus="+leafStr)

        return "{TimeoutsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "TimeoutsData", 
        "namespace": "timeouts", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.timeouts.timeouts_data_gen import TimeoutsData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "storage", 
            "isCurrent": false
        }, 
        {
            "namespace": "disk", 
            "isCurrent": false
        }, 
        {
            "namespace": "file_system", 
            "isCurrent": false
        }, 
        {
            "namespace": "timeouts", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "activate", 
            "yangName": "activate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "getStatus", 
            "yangName": "get-status", 
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
            "qwilt_tech_storage_disk"
        ]
    }, 
    "createTime": "2013"
}
"""


