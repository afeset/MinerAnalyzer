


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

        self.preferredDeliveryInterface = ""
        self._myHasPreferredDeliveryInterface=False
        

    def copyFrom (self, other):

        self.preferredDeliveryInterface=other.preferredDeliveryInterface
        self._myHasPreferredDeliveryInterface=other._myHasPreferredDeliveryInterface
        
    # has...() methods

    def hasPreferredDeliveryInterface (self):
        return self._myHasPreferredDeliveryInterface


    # setHas...() methods

    def setHasPreferredDeliveryInterface (self):
        self._myHasPreferredDeliveryInterface=True


    def clearAllHas (self):

        self._myHasPreferredDeliveryInterface=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasPreferredDeliveryInterface:
            x = "+"
        leafStr = str(self.preferredDeliveryInterface)
        items.append(x + "PreferredDeliveryInterface="+leafStr)

        return "{DeliveryData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DeliveryData", 
        "namespace": "delivery", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.system_defaults.delivery.delivery_data_gen import DeliveryData"
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
            "namespace": "delivery", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "preferredDeliveryInterface", 
            "yangName": "preferred-delivery-interface", 
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
            "content", 
            "qwilt_tech_content_interfaces"
        ]
    }, 
    "createTime": "2013"
}
"""


