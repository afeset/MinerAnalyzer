


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class DpdkData(object):

    def __init__ (self):

        self.channelQueueSize = 0
        self._myHasChannelQueueSize=False
        
        self.memSize = 0
        self._myHasMemSize=False
        

    def copyFrom (self, other):

        self.channelQueueSize=other.channelQueueSize
        self._myHasChannelQueueSize=other._myHasChannelQueueSize
        
        self.memSize=other.memSize
        self._myHasMemSize=other._myHasMemSize
        
    # has...() methods

    def hasChannelQueueSize (self):
        return self._myHasChannelQueueSize

    def hasMemSize (self):
        return self._myHasMemSize


    # setHas...() methods

    def setHasChannelQueueSize (self):
        self._myHasChannelQueueSize=True

    def setHasMemSize (self):
        self._myHasMemSize=True


    def clearAllHas (self):

        self._myHasChannelQueueSize=False

        self._myHasMemSize=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasChannelQueueSize:
            x = "+"
        leafStr = str(self.channelQueueSize)
        items.append(x + "ChannelQueueSize="+leafStr)

        x=""
        if self._myHasMemSize:
            x = "+"
        leafStr = str(self.memSize)
        items.append(x + "MemSize="+leafStr)

        return "{DpdkData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DpdkData", 
        "namespace": "dpdk", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.dpdk.dpdk_data_gen import DpdkData"
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
            "namespace": "dpdk", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "channelQueueSize", 
            "yangName": "channel-queue-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "memSize", 
            "yangName": "mem-size", 
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


