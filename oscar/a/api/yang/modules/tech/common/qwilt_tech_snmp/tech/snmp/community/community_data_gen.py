


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.common.qwilt_types.qwilt_types_module_gen import Accessmodetype


class CommunityData(object):

    def __init__ (self):

        self.entryName = ""
        self._myHasEntryName=False
        
        self.accessMode = Accessmodetype.kReadOnly
        self._myHasAccessMode=False
        
        self.community = ""
        self._myHasCommunity=False
        

    def copyFrom (self, other):

        self.entryName=other.entryName
        self._myHasEntryName=other._myHasEntryName
        
        self.accessMode=other.accessMode
        self._myHasAccessMode=other._myHasAccessMode
        
        self.community=other.community
        self._myHasCommunity=other._myHasCommunity
        
    # has...() methods

    def hasEntryName (self):
        return self._myHasEntryName

    def hasAccessMode (self):
        return self._myHasAccessMode

    def hasCommunity (self):
        return self._myHasCommunity


    # setHas...() methods

    def setHasEntryName (self):
        self._myHasEntryName=True

    def setHasAccessMode (self):
        self._myHasAccessMode=True

    def setHasCommunity (self):
        self._myHasCommunity=True


    def clearAllHas (self):

        self._myHasEntryName=False

        self._myHasAccessMode=False

        self._myHasCommunity=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEntryName:
            x = "+"
        leafStr = str(self.entryName)
        items.append(x + "EntryName="+leafStr)

        x=""
        if self._myHasAccessMode:
            x = "+"
        leafStr = str(self.accessMode)
        items.append(x + "AccessMode="+leafStr)

        x=""
        if self._myHasCommunity:
            x = "+"
        leafStr = str(self.community)
        items.append(x + "Community="+leafStr)

        return "{CommunityData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "CommunityData", 
        "namespace": "community", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.community.community_data_gen import CommunityData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "snmp", 
            "isCurrent": false
        }, 
        {
            "namespace": "community", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "entryName", 
            "yangName": "entry-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "accessMode", 
            "yangName": "access-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "community", 
            "yangName": "community", 
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
            "common", 
            "qwilt_tech_snmp"
        ]
    }, 
    "createTime": "2013"
}
"""


