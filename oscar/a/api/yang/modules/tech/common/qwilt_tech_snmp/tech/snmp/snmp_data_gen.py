


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SnmpData(object):

    def __init__ (self):

        self.enabled = False
        self._myHasEnabled=False
        
        self.contact = ""
        self._myHasContact=False
        
        self.location = ""
        self._myHasLocation=False
        

    def copyFrom (self, other):

        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.contact=other.contact
        self._myHasContact=other._myHasContact
        
        self.location=other.location
        self._myHasLocation=other._myHasLocation
        
    # has...() methods

    def hasEnabled (self):
        return self._myHasEnabled

    def hasContact (self):
        return self._myHasContact

    def hasLocation (self):
        return self._myHasLocation


    # setHas...() methods

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasContact (self):
        self._myHasContact=True

    def setHasLocation (self):
        self._myHasLocation=True


    def clearAllHas (self):

        self._myHasEnabled=False

        self._myHasContact=False

        self._myHasLocation=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasContact:
            x = "+"
        leafStr = str(self.contact)
        items.append(x + "Contact="+leafStr)

        x=""
        if self._myHasLocation:
            x = "+"
        leafStr = str(self.location)
        items.append(x + "Location="+leafStr)

        return "{SnmpData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SnmpData", 
        "namespace": "snmp", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.snmp_data_gen import SnmpData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "snmp", 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "contact", 
            "yangName": "contact", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
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


