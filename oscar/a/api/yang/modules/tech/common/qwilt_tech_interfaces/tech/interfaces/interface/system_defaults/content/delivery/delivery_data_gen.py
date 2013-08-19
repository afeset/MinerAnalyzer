


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

        self.enabled = False
        self._myHasEnabled=False
        

    def copyFrom (self, other):

        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
    # has...() methods

    def hasEnabled (self):
        return self._myHasEnabled


    # setHas...() methods

    def setHasEnabled (self):
        self._myHasEnabled=True


    def clearAllHas (self):

        self._myHasEnabled=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        return "{DeliveryData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DeliveryData", 
        "namespace": "delivery", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.content.delivery.delivery_data_gen import DeliveryData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "interfaces", 
            "isCurrent": false
        }, 
        {
            "namespace": "interface", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "content", 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "createTime": "2013"
}
"""


