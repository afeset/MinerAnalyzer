


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class DeliveryData(object):

    def __init__ (self):

        self.maxActiveConnections = 0
        self._myHasMaxActiveConnections=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.maxRedirectRate = 0
        self._myHasMaxRedirectRate=False
        

    def copyFrom (self, other):

        self.maxActiveConnections=other.maxActiveConnections
        self._myHasMaxActiveConnections=other._myHasMaxActiveConnections
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.maxRedirectRate=other.maxRedirectRate
        self._myHasMaxRedirectRate=other._myHasMaxRedirectRate
        
    # has...() methods

    def hasMaxActiveConnections (self):
        return self._myHasMaxActiveConnections

    def hasEnabled (self):
        return self._myHasEnabled

    def hasMaxRedirectRate (self):
        return self._myHasMaxRedirectRate


    # setHas...() methods

    def setHasMaxActiveConnections (self):
        self._myHasMaxActiveConnections=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasMaxRedirectRate (self):
        self._myHasMaxRedirectRate=True


    def clearAllHas (self):

        self._myHasMaxActiveConnections=False

        self._myHasEnabled=False

        self._myHasMaxRedirectRate=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasMaxActiveConnections:
            x = "+"
        leafStr = str(self.maxActiveConnections)
        items.append(x + "MaxActiveConnections="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasMaxRedirectRate:
            x = "+"
        leafStr = str(self.maxRedirectRate)
        items.append(x + "MaxRedirectRate="+leafStr)

        return "{DeliveryData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DeliveryData", 
        "namespace": "delivery", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.delivery.delivery_data_gen import DeliveryData"
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
            "namespace": "analyzer", 
            "isCurrent": false
        }, 
        {
            "namespace": "delivery", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxActiveConnections", 
            "yangName": "max-active-connections", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxRedirectRate", 
            "yangName": "max-redirect-rate", 
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


