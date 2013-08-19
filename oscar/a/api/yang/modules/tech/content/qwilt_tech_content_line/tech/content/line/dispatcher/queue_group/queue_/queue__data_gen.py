


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class QueueData(object):

    def __init__ (self):

        self.queueThresholdLow = 0
        self._myHasQueueThresholdLow=False
        
        self.queueSize = 0
        self._myHasQueueSize=False
        
        self.queueThresholdHigh = 0
        self._myHasQueueThresholdHigh=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.queueThresholdLow=other.queueThresholdLow
        self._myHasQueueThresholdLow=other._myHasQueueThresholdLow
        
        self.queueSize=other.queueSize
        self._myHasQueueSize=other._myHasQueueSize
        
        self.queueThresholdHigh=other.queueThresholdHigh
        self._myHasQueueThresholdHigh=other._myHasQueueThresholdHigh
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasQueueThresholdLow (self):
        return self._myHasQueueThresholdLow

    def hasQueueSize (self):
        return self._myHasQueueSize

    def hasQueueThresholdHigh (self):
        return self._myHasQueueThresholdHigh

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasQueueThresholdLow (self):
        self._myHasQueueThresholdLow=True

    def setHasQueueSize (self):
        self._myHasQueueSize=True

    def setHasQueueThresholdHigh (self):
        self._myHasQueueThresholdHigh=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasQueueThresholdLow=False

        self._myHasQueueSize=False

        self._myHasQueueThresholdHigh=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasQueueThresholdLow:
            x = "+"
        leafStr = str(self.queueThresholdLow)
        items.append(x + "QueueThresholdLow="+leafStr)

        x=""
        if self._myHasQueueSize:
            x = "+"
        leafStr = str(self.queueSize)
        items.append(x + "QueueSize="+leafStr)

        x=""
        if self._myHasQueueThresholdHigh:
            x = "+"
        leafStr = str(self.queueThresholdHigh)
        items.append(x + "QueueThresholdHigh="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{QueueData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "QueueData", 
        "namespace": "queue_", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.queue_group.queue_.queue__data_gen import QueueData"
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
            "namespace": "queue_group", 
            "isCurrent": false
        }, 
        {
            "namespace": "queue_", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdLow", 
            "yangName": "queue-threshold-low", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueSize", 
            "yangName": "queue-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdHigh", 
            "yangName": "queue-threshold-high", 
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


