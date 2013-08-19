


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class InstancesData(object):

    def __init__ (self):

        self.warnTotalRecordCount = 0
        self._myHasWarnTotalRecordCount=False
        
        self.periodicWorkRecordCount = 0
        self._myHasPeriodicWorkRecordCount=False
        
        self.aggregationPeriod = 0
        self._myHasAggregationPeriod=False
        
        self.maxTotalRecordCount = 0
        self._myHasMaxTotalRecordCount=False
        
        self.periodicWorkInterval = 0
        self._myHasPeriodicWorkInterval=False
        
        self.warnSessionIdCount = 0
        self._myHasWarnSessionIdCount=False
        
        self.instance = ""
        self._myHasInstance=False
        
        self.maxSessionIdCount = 0
        self._myHasMaxSessionIdCount=False
        
        self.rotateFileInterval = 0
        self._myHasRotateFileInterval=False
        
        self.recordWriteInterval = 0
        self._myHasRecordWriteInterval=False
        
        self.archive = False
        self._myHasArchive=False
        

    def copyFrom (self, other):

        self.warnTotalRecordCount=other.warnTotalRecordCount
        self._myHasWarnTotalRecordCount=other._myHasWarnTotalRecordCount
        
        self.periodicWorkRecordCount=other.periodicWorkRecordCount
        self._myHasPeriodicWorkRecordCount=other._myHasPeriodicWorkRecordCount
        
        self.aggregationPeriod=other.aggregationPeriod
        self._myHasAggregationPeriod=other._myHasAggregationPeriod
        
        self.maxTotalRecordCount=other.maxTotalRecordCount
        self._myHasMaxTotalRecordCount=other._myHasMaxTotalRecordCount
        
        self.periodicWorkInterval=other.periodicWorkInterval
        self._myHasPeriodicWorkInterval=other._myHasPeriodicWorkInterval
        
        self.warnSessionIdCount=other.warnSessionIdCount
        self._myHasWarnSessionIdCount=other._myHasWarnSessionIdCount
        
        self.instance=other.instance
        self._myHasInstance=other._myHasInstance
        
        self.maxSessionIdCount=other.maxSessionIdCount
        self._myHasMaxSessionIdCount=other._myHasMaxSessionIdCount
        
        self.rotateFileInterval=other.rotateFileInterval
        self._myHasRotateFileInterval=other._myHasRotateFileInterval
        
        self.recordWriteInterval=other.recordWriteInterval
        self._myHasRecordWriteInterval=other._myHasRecordWriteInterval
        
        self.archive=other.archive
        self._myHasArchive=other._myHasArchive
        
    # has...() methods

    def hasWarnTotalRecordCount (self):
        return self._myHasWarnTotalRecordCount

    def hasPeriodicWorkRecordCount (self):
        return self._myHasPeriodicWorkRecordCount

    def hasAggregationPeriod (self):
        return self._myHasAggregationPeriod

    def hasMaxTotalRecordCount (self):
        return self._myHasMaxTotalRecordCount

    def hasPeriodicWorkInterval (self):
        return self._myHasPeriodicWorkInterval

    def hasWarnSessionIdCount (self):
        return self._myHasWarnSessionIdCount

    def hasInstance (self):
        return self._myHasInstance

    def hasMaxSessionIdCount (self):
        return self._myHasMaxSessionIdCount

    def hasRotateFileInterval (self):
        return self._myHasRotateFileInterval

    def hasRecordWriteInterval (self):
        return self._myHasRecordWriteInterval

    def hasArchive (self):
        return self._myHasArchive


    # setHas...() methods

    def setHasWarnTotalRecordCount (self):
        self._myHasWarnTotalRecordCount=True

    def setHasPeriodicWorkRecordCount (self):
        self._myHasPeriodicWorkRecordCount=True

    def setHasAggregationPeriod (self):
        self._myHasAggregationPeriod=True

    def setHasMaxTotalRecordCount (self):
        self._myHasMaxTotalRecordCount=True

    def setHasPeriodicWorkInterval (self):
        self._myHasPeriodicWorkInterval=True

    def setHasWarnSessionIdCount (self):
        self._myHasWarnSessionIdCount=True

    def setHasInstance (self):
        self._myHasInstance=True

    def setHasMaxSessionIdCount (self):
        self._myHasMaxSessionIdCount=True

    def setHasRotateFileInterval (self):
        self._myHasRotateFileInterval=True

    def setHasRecordWriteInterval (self):
        self._myHasRecordWriteInterval=True

    def setHasArchive (self):
        self._myHasArchive=True


    def clearAllHas (self):

        self._myHasWarnTotalRecordCount=False

        self._myHasPeriodicWorkRecordCount=False

        self._myHasAggregationPeriod=False

        self._myHasMaxTotalRecordCount=False

        self._myHasPeriodicWorkInterval=False

        self._myHasWarnSessionIdCount=False

        self._myHasInstance=False

        self._myHasMaxSessionIdCount=False

        self._myHasRotateFileInterval=False

        self._myHasRecordWriteInterval=False

        self._myHasArchive=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasWarnTotalRecordCount:
            x = "+"
        leafStr = str(self.warnTotalRecordCount)
        items.append(x + "WarnTotalRecordCount="+leafStr)

        x=""
        if self._myHasPeriodicWorkRecordCount:
            x = "+"
        leafStr = str(self.periodicWorkRecordCount)
        items.append(x + "PeriodicWorkRecordCount="+leafStr)

        x=""
        if self._myHasAggregationPeriod:
            x = "+"
        leafStr = str(self.aggregationPeriod)
        items.append(x + "AggregationPeriod="+leafStr)

        x=""
        if self._myHasMaxTotalRecordCount:
            x = "+"
        leafStr = str(self.maxTotalRecordCount)
        items.append(x + "MaxTotalRecordCount="+leafStr)

        x=""
        if self._myHasPeriodicWorkInterval:
            x = "+"
        leafStr = str(self.periodicWorkInterval)
        items.append(x + "PeriodicWorkInterval="+leafStr)

        x=""
        if self._myHasWarnSessionIdCount:
            x = "+"
        leafStr = str(self.warnSessionIdCount)
        items.append(x + "WarnSessionIdCount="+leafStr)

        x=""
        if self._myHasInstance:
            x = "+"
        leafStr = str(self.instance)
        items.append(x + "Instance="+leafStr)

        x=""
        if self._myHasMaxSessionIdCount:
            x = "+"
        leafStr = str(self.maxSessionIdCount)
        items.append(x + "MaxSessionIdCount="+leafStr)

        x=""
        if self._myHasRotateFileInterval:
            x = "+"
        leafStr = str(self.rotateFileInterval)
        items.append(x + "RotateFileInterval="+leafStr)

        x=""
        if self._myHasRecordWriteInterval:
            x = "+"
        leafStr = str(self.recordWriteInterval)
        items.append(x + "RecordWriteInterval="+leafStr)

        x=""
        if self._myHasArchive:
            x = "+"
        leafStr = str(self.archive)
        items.append(x + "Archive="+leafStr)

        return "{InstancesData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "InstancesData", 
        "namespace": "instances", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_pre_topper.tech.content.pre_topper.instances.instances_data_gen import InstancesData"
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
            "namespace": "pre_topper", 
            "isCurrent": false
        }, 
        {
            "namespace": "instances", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnTotalRecordCount", 
            "yangName": "warn-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkRecordCount", 
            "yangName": "periodic-work-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "aggregationPeriod", 
            "yangName": "aggregation-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxTotalRecordCount", 
            "yangName": "max-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkInterval", 
            "yangName": "periodic-work-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnSessionIdCount", 
            "yangName": "warn-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "instance", 
            "yangName": "instance", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessionIdCount", 
            "yangName": "max-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rotateFileInterval", 
            "yangName": "rotate-file-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "recordWriteInterval", 
            "yangName": "record-write-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "archive", 
            "yangName": "archive", 
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
            "content", 
            "qwilt_tech_content_pre_topper"
        ]
    }, 
    "createTime": "2013"
}
"""


