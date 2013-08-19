


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class DestinationZoneData(object):

    def __init__ (self):

        self.zone = ""
        self._myHasZone=False
        

    def copyFrom (self, other):

        self.zone=other.zone
        self._myHasZone=other._myHasZone
        
    # has...() methods

    def hasZone (self):
        return self._myHasZone


    # setHas...() methods

    def setHasZone (self):
        self._myHasZone=True


    def clearAllHas (self):

        self._myHasZone=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasZone:
            x = "+"
        leafStr = str(self.zone)
        items.append(x + "Zone="+leafStr)

        return "{DestinationZoneData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DestinationZoneData", 
        "namespace": "destination_zone", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.destination_zone.destination_zone_data_gen import DestinationZoneData"
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
            "namespace": "policy", 
            "isCurrent": false
        }, 
        {
            "namespace": "rules", 
            "isCurrent": false
        }, 
        {
            "namespace": "rule", 
            "isCurrent": false
        }, 
        {
            "namespace": "destination_zone", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "zone", 
            "yangName": "zone", 
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
            "qwilt_tech_content"
        ]
    }, 
    "createTime": "2013"
}
"""


