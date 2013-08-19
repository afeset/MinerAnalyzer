


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

        self.getLogicalDiskStatus = 0
        self._myHasGetLogicalDiskStatus=False
        
        self.getPhysicalStatus = 0
        self._myHasGetPhysicalStatus=False
        
        self.activateLogicalDisk = 0
        self._myHasActivateLogicalDisk=False
        

    def copyFrom (self, other):

        self.getLogicalDiskStatus=other.getLogicalDiskStatus
        self._myHasGetLogicalDiskStatus=other._myHasGetLogicalDiskStatus
        
        self.getPhysicalStatus=other.getPhysicalStatus
        self._myHasGetPhysicalStatus=other._myHasGetPhysicalStatus
        
        self.activateLogicalDisk=other.activateLogicalDisk
        self._myHasActivateLogicalDisk=other._myHasActivateLogicalDisk
        
    # has...() methods

    def hasGetLogicalDiskStatus (self):
        return self._myHasGetLogicalDiskStatus

    def hasGetPhysicalStatus (self):
        return self._myHasGetPhysicalStatus

    def hasActivateLogicalDisk (self):
        return self._myHasActivateLogicalDisk


    # setHas...() methods

    def setHasGetLogicalDiskStatus (self):
        self._myHasGetLogicalDiskStatus=True

    def setHasGetPhysicalStatus (self):
        self._myHasGetPhysicalStatus=True

    def setHasActivateLogicalDisk (self):
        self._myHasActivateLogicalDisk=True


    def clearAllHas (self):

        self._myHasGetLogicalDiskStatus=False

        self._myHasGetPhysicalStatus=False

        self._myHasActivateLogicalDisk=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasGetLogicalDiskStatus:
            x = "+"
        leafStr = str(self.getLogicalDiskStatus)
        items.append(x + "GetLogicalDiskStatus="+leafStr)

        x=""
        if self._myHasGetPhysicalStatus:
            x = "+"
        leafStr = str(self.getPhysicalStatus)
        items.append(x + "GetPhysicalStatus="+leafStr)

        x=""
        if self._myHasActivateLogicalDisk:
            x = "+"
        leafStr = str(self.activateLogicalDisk)
        items.append(x + "ActivateLogicalDisk="+leafStr)

        return "{TimeoutsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "TimeoutsData", 
        "namespace": "timeouts", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.system_defaults.timeouts.timeouts_data_gen import TimeoutsData"
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
            "namespace": "controller", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
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
            "memberName": "getLogicalDiskStatus", 
            "yangName": "get-logical-disk-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "getPhysicalStatus", 
            "yangName": "get-physical-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "activateLogicalDisk", 
            "yangName": "activate-logical-disk", 
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
            "common", 
            "qwilt_tech_storage_controller"
        ]
    }, 
    "createTime": "2013"
}
"""


