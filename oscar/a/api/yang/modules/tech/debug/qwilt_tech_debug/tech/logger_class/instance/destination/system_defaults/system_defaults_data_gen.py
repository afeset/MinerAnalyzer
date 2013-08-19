


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


class SystemDefaultsData(object):

    def __init__ (self):

        self.minLevel = LogSeverity.kAny
        self._myHasMinLevel=False
        
        self.destinationType = DestinationType.kText
        self._myHasDestinationType=False
        
        self.enabled = True
        self._myHasEnabled=False
        

    def copyFrom (self, other):

        self.minLevel=other.minLevel
        self._myHasMinLevel=other._myHasMinLevel
        
        self.destinationType=other.destinationType
        self._myHasDestinationType=other._myHasDestinationType
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
    # has...() methods

    def hasMinLevel (self):
        return self._myHasMinLevel

    def hasDestinationType (self):
        return self._myHasDestinationType

    def hasEnabled (self):
        return self._myHasEnabled


    # setHas...() methods

    def setHasMinLevel (self):
        self._myHasMinLevel=True

    def setHasDestinationType (self):
        self._myHasDestinationType=True

    def setHasEnabled (self):
        self._myHasEnabled=True


    def clearAllHas (self):

        self._myHasMinLevel=False

        self._myHasDestinationType=False

        self._myHasEnabled=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasMinLevel:
            x = "+"
        leafStr = str(self.minLevel)
        items.append(x + "MinLevel="+leafStr)

        x=""
        if self._myHasDestinationType:
            x = "+"
        leafStr = str(self.destinationType)
        items.append(x + "DestinationType="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        return "{SystemDefaultsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemDefaultsData", 
        "namespace": "system_defaults", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.system_defaults_data_gen import SystemDefaultsData"
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
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "minLevel", 
            "yangName": "min-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "destinationType", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "text", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
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
            "debug", 
            "qwilt_tech_debug"
        ]
    }, 
    "createTime": "2013"
}
"""


