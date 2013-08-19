


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_snmp.qwilt_tech_snmp_module_gen import SnmpNotificationTypeType
from a.api.yang.modules.tech.common.qwilt_tech_snmp.qwilt_tech_snmp_module_gen import SnmpNotificationVersionType


class DestinationData(object):

    def __init__ (self):

        self.name = ""
        self._myHasName=False
        
        self.destination = ""
        self._myHasDestination=False
        
        self.community = ""
        self._myHasCommunity=False
        
        self.version = SnmpNotificationVersionType.kV1
        self._myHasVersion=False
        
        self.type_ = SnmpNotificationTypeType.kTrap
        self._myHasType_=False
        
        self.port = 162
        self._myHasPort=False
        

    def copyFrom (self, other):

        self.name=other.name
        self._myHasName=other._myHasName
        
        self.destination=other.destination
        self._myHasDestination=other._myHasDestination
        
        self.community=other.community
        self._myHasCommunity=other._myHasCommunity
        
        self.version=other.version
        self._myHasVersion=other._myHasVersion
        
        self.type_=other.type_
        self._myHasType_=other._myHasType_
        
        self.port=other.port
        self._myHasPort=other._myHasPort
        
    # has...() methods

    def hasName (self):
        return self._myHasName

    def hasDestination (self):
        return self._myHasDestination

    def hasCommunity (self):
        return self._myHasCommunity

    def hasVersion (self):
        return self._myHasVersion

    def hasType_ (self):
        return self._myHasType_

    def hasPort (self):
        return self._myHasPort


    # setHas...() methods

    def setHasName (self):
        self._myHasName=True

    def setHasDestination (self):
        self._myHasDestination=True

    def setHasCommunity (self):
        self._myHasCommunity=True

    def setHasVersion (self):
        self._myHasVersion=True

    def setHasType_ (self):
        self._myHasType_=True

    def setHasPort (self):
        self._myHasPort=True


    def clearAllHas (self):

        self._myHasName=False

        self._myHasDestination=False

        self._myHasCommunity=False

        self._myHasVersion=False

        self._myHasType_=False

        self._myHasPort=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasDestination:
            x = "+"
        leafStr = str(self.destination)
        items.append(x + "Destination="+leafStr)

        x=""
        if self._myHasCommunity:
            x = "+"
        leafStr = str(self.community)
        items.append(x + "Community="+leafStr)

        x=""
        if self._myHasVersion:
            x = "+"
        leafStr = str(self.version)
        items.append(x + "Version="+leafStr)

        x=""
        if self._myHasType_:
            x = "+"
        leafStr = str(self.type_)
        items.append(x + "Type_="+leafStr)

        x=""
        if self._myHasPort:
            x = "+"
        leafStr = str(self.port)
        items.append(x + "Port="+leafStr)

        return "{DestinationData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DestinationData", 
        "namespace": "destination", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.notifications.destination.destination_data_gen import DestinationData"
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
            "namespace": "notifications", 
            "isCurrent": false
        }, 
        {
            "namespace": "destination", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "destination", 
            "yangName": "destination", 
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
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "version", 
            "yangName": "version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "v1", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "type_", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "trap", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "port", 
            "yangName": "port", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "162", 
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


