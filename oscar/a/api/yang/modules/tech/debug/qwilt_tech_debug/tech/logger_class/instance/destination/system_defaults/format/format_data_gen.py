


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class FormatData(object):

    def __init__ (self):

        self.messageExtra = ""
        self._myHasMessageExtra=False
        
        self.messageBase = ""
        self._myHasMessageBase=False
        
        self.payload = ""
        self._myHasPayload=False
        

    def copyFrom (self, other):

        self.messageExtra=other.messageExtra
        self._myHasMessageExtra=other._myHasMessageExtra
        
        self.messageBase=other.messageBase
        self._myHasMessageBase=other._myHasMessageBase
        
        self.payload=other.payload
        self._myHasPayload=other._myHasPayload
        
    # has...() methods

    def hasMessageExtra (self):
        return self._myHasMessageExtra

    def hasMessageBase (self):
        return self._myHasMessageBase

    def hasPayload (self):
        return self._myHasPayload


    # setHas...() methods

    def setHasMessageExtra (self):
        self._myHasMessageExtra=True

    def setHasMessageBase (self):
        self._myHasMessageBase=True

    def setHasPayload (self):
        self._myHasPayload=True


    def clearAllHas (self):

        self._myHasMessageExtra=False

        self._myHasMessageBase=False

        self._myHasPayload=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasMessageExtra:
            x = "+"
        leafStr = str(self.messageExtra)
        items.append(x + "MessageExtra="+leafStr)

        x=""
        if self._myHasMessageBase:
            x = "+"
        leafStr = str(self.messageBase)
        items.append(x + "MessageBase="+leafStr)

        x=""
        if self._myHasPayload:
            x = "+"
        leafStr = str(self.payload)
        items.append(x + "Payload="+leafStr)

        return "{FormatData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "FormatData", 
        "namespace": "format", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.format.format_data_gen import FormatData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "logger_class", 
            "isCurrent": false
        }, 
        {
            "namespace": "instance", 
            "isCurrent": false
        }, 
        {
            "namespace": "destination", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "format", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageExtra", 
            "yangName": "message-extra", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageBase", 
            "yangName": "message-base", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "payload", 
            "yangName": "payload", 
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
            "debug", 
            "qwilt_tech_debug"
        ]
    }, 
    "createTime": "2013"
}
"""


