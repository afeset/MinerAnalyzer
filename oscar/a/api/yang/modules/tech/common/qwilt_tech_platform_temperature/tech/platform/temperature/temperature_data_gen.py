


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class TemperatureData(object):

    def __init__ (self):

        self.muteReporting = False
        self._myHasMuteReporting=False
        
        self.enabled = False
        self._myHasEnabled=False
        

    def copyFrom (self, other):

        self.muteReporting=other.muteReporting
        self._myHasMuteReporting=other._myHasMuteReporting
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
    # has...() methods

    def hasMuteReporting (self):
        return self._myHasMuteReporting

    def hasEnabled (self):
        return self._myHasEnabled


    # setHas...() methods

    def setHasMuteReporting (self):
        self._myHasMuteReporting=True

    def setHasEnabled (self):
        self._myHasEnabled=True


    def clearAllHas (self):

        self._myHasMuteReporting=False

        self._myHasEnabled=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasMuteReporting:
            x = "+"
        leafStr = str(self.muteReporting)
        items.append(x + "MuteReporting="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        return "{TemperatureData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "TemperatureData", 
        "namespace": "temperature", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.temperature_data_gen import TemperatureData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "platform", 
            "isCurrent": false
        }, 
        {
            "namespace": "temperature", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
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
            "qwilt_tech_platform_temperature"
        ]
    }, 
    "createTime": "2013"
}
"""


