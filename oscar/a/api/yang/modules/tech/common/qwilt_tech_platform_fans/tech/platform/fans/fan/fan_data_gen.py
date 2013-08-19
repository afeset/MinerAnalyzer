


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class FanData(object):

    def __init__ (self):

        self.name = ""
        self._myHasName=False
        
        self.muteReporting = False
        self._myHasMuteReporting=False
        
        self.location = ""
        self._myHasLocation=False
        

    def copyFrom (self, other):

        self.name=other.name
        self._myHasName=other._myHasName
        
        self.muteReporting=other.muteReporting
        self._myHasMuteReporting=other._myHasMuteReporting
        
        self.location=other.location
        self._myHasLocation=other._myHasLocation
        
    # has...() methods

    def hasName (self):
        return self._myHasName

    def hasMuteReporting (self):
        return self._myHasMuteReporting

    def hasLocation (self):
        return self._myHasLocation


    # setHas...() methods

    def setHasName (self):
        self._myHasName=True

    def setHasMuteReporting (self):
        self._myHasMuteReporting=True

    def setHasLocation (self):
        self._myHasLocation=True


    def clearAllHas (self):

        self._myHasName=False

        self._myHasMuteReporting=False

        self._myHasLocation=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasMuteReporting:
            x = "+"
        leafStr = str(self.muteReporting)
        items.append(x + "MuteReporting="+leafStr)

        x=""
        if self._myHasLocation:
            x = "+"
        leafStr = str(self.location)
        items.append(x + "Location="+leafStr)

        return "{FanData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "FanData", 
        "namespace": "fan", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.fan_data_gen import FanData"
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
            "namespace": "fans", 
            "isCurrent": false
        }, 
        {
            "namespace": "fan", 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
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
            "qwilt_tech_platform_fans"
        ]
    }, 
    "createTime": "2013"
}
"""


