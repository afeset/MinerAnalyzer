


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogSeverity
from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import DestinationType


class DestinationData(object):

    def __init__ (self):

        self.description = ""
        self._myHasDescription=False
        
        self.minLevel = LogSeverity.kDebug1
        self._myHasMinLevel=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.destinationType = DestinationType.kTextCsv
        self._myHasDestinationType=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.minLevel=other.minLevel
        self._myHasMinLevel=other._myHasMinLevel
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.destinationType=other.destinationType
        self._myHasDestinationType=other._myHasDestinationType
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasDescription (self):
        return self._myHasDescription

    def hasMinLevel (self):
        return self._myHasMinLevel

    def hasEnabled (self):
        return self._myHasEnabled

    def hasDestinationType (self):
        return self._myHasDestinationType

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasMinLevel (self):
        self._myHasMinLevel=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasDestinationType (self):
        self._myHasDestinationType=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasDescription=False

        self._myHasMinLevel=False

        self._myHasEnabled=False

        self._myHasDestinationType=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDescription:
            x = "+"
        leafStr = str(self.description)
        items.append(x + "Description="+leafStr)

        x=""
        if self._myHasMinLevel:
            x = "+"
        leafStr = str(self.minLevel)
        items.append(x + "MinLevel="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasDestinationType:
            x = "+"
        leafStr = str(self.destinationType)
        items.append(x + "DestinationType="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{DestinationData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DestinationData", 
        "namespace": "destination", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.destination_data_gen import DestinationData"
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
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "minLevel", 
            "yangName": "min-level", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "destinationType", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
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
            "debug", 
            "qwilt_tech_debug"
        ]
    }, 
    "createTime": "2013"
}
"""


