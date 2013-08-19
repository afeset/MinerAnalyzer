


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

        self.deliveryInterfaceFailover = True
        self._myHasDeliveryInterfaceFailover=False
        

    def copyFrom (self, other):

        self.deliveryInterfaceFailover=other.deliveryInterfaceFailover
        self._myHasDeliveryInterfaceFailover=other._myHasDeliveryInterfaceFailover
        
    # has...() methods

    def hasDeliveryInterfaceFailover (self):
        return self._myHasDeliveryInterfaceFailover


    # setHas...() methods

    def setHasDeliveryInterfaceFailover (self):
        self._myHasDeliveryInterfaceFailover=True


    def clearAllHas (self):

        self._myHasDeliveryInterfaceFailover=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDeliveryInterfaceFailover:
            x = "+"
        leafStr = str(self.deliveryInterfaceFailover)
        items.append(x + "DeliveryInterfaceFailover="+leafStr)

        return "{DeliveryData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DeliveryData", 
        "namespace": "delivery", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.system_defaults.delivery.delivery_data_gen import DeliveryData"
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "deliveryInterfaceFailover", 
            "yangName": "delivery-interface-failover", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
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
            "qwilt_tech_content"
        ]
    }, 
    "createTime": "2013"
}
"""


