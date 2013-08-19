


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

        self.queueThresholdLow = 0
        self._myHasQueueThresholdLow=False
        
        self.queueThresholdHigh = 0
        self._myHasQueueThresholdHigh=False
        
        self.queueSize = 0
        self._myHasQueueSize=False
        

    def copyFrom (self, other):

        self.queueThresholdLow=other.queueThresholdLow
        self._myHasQueueThresholdLow=other._myHasQueueThresholdLow
        
        self.queueThresholdHigh=other.queueThresholdHigh
        self._myHasQueueThresholdHigh=other._myHasQueueThresholdHigh
        
        self.queueSize=other.queueSize
        self._myHasQueueSize=other._myHasQueueSize
        
    # has...() methods

    def hasQueueThresholdLow (self):
        return self._myHasQueueThresholdLow

    def hasQueueThresholdHigh (self):
        return self._myHasQueueThresholdHigh

    def hasQueueSize (self):
        return self._myHasQueueSize


    # setHas...() methods

    def setHasQueueThresholdLow (self):
        self._myHasQueueThresholdLow=True

    def setHasQueueThresholdHigh (self):
        self._myHasQueueThresholdHigh=True

    def setHasQueueSize (self):
        self._myHasQueueSize=True


    def clearAllHas (self):

        self._myHasQueueThresholdLow=False

        self._myHasQueueThresholdHigh=False

        self._myHasQueueSize=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasQueueThresholdLow:
            x = "+"
        leafStr = str(self.queueThresholdLow)
        items.append(x + "QueueThresholdLow="+leafStr)

        x=""
        if self._myHasQueueThresholdHigh:
            x = "+"
        leafStr = str(self.queueThresholdHigh)
        items.append(x + "QueueThresholdHigh="+leafStr)

        x=""
        if self._myHasQueueSize:
            x = "+"
        leafStr = str(self.queueSize)
        items.append(x + "QueueSize="+leafStr)

        return "{SystemDefaultsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemDefaultsData", 
        "namespace": "system_defaults", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.queue_group.queue_.system_defaults.system_defaults_data_gen import SystemDefaultsData"
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdLow", 
            "yangName": "queue-threshold-low", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdHigh", 
            "yangName": "queue-threshold-high", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueSize", 
            "yangName": "queue-size", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "createTime": "2013"
}
"""


