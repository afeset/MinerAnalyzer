


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SystemDefaultsData(object):

    def __init__ (self):

        self.configurationDelay = 0
        self._myHasConfigurationDelay=False
        
        self.muteReporting = False
        self._myHasMuteReporting=False
        
        self.sendGratuitousArp = True
        self._myHasSendGratuitousArp=False
        
        self.shutdown = True
        self._myHasShutdown=False
        
        self.techMode = False
        self._myHasTechMode=False
        

    def copyFrom (self, other):

        self.configurationDelay=other.configurationDelay
        self._myHasConfigurationDelay=other._myHasConfigurationDelay
        
        self.muteReporting=other.muteReporting
        self._myHasMuteReporting=other._myHasMuteReporting
        
        self.sendGratuitousArp=other.sendGratuitousArp
        self._myHasSendGratuitousArp=other._myHasSendGratuitousArp
        
        self.shutdown=other.shutdown
        self._myHasShutdown=other._myHasShutdown
        
        self.techMode=other.techMode
        self._myHasTechMode=other._myHasTechMode
        
    # has...() methods

    def hasConfigurationDelay (self):
        return self._myHasConfigurationDelay

    def hasMuteReporting (self):
        return self._myHasMuteReporting

    def hasSendGratuitousArp (self):
        return self._myHasSendGratuitousArp

    def hasShutdown (self):
        return self._myHasShutdown

    def hasTechMode (self):
        return self._myHasTechMode


    # setHas...() methods

    def setHasConfigurationDelay (self):
        self._myHasConfigurationDelay=True

    def setHasMuteReporting (self):
        self._myHasMuteReporting=True

    def setHasSendGratuitousArp (self):
        self._myHasSendGratuitousArp=True

    def setHasShutdown (self):
        self._myHasShutdown=True

    def setHasTechMode (self):
        self._myHasTechMode=True


    def clearAllHas (self):

        self._myHasConfigurationDelay=False

        self._myHasMuteReporting=False

        self._myHasSendGratuitousArp=False

        self._myHasShutdown=False

        self._myHasTechMode=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasConfigurationDelay:
            x = "+"
        leafStr = str(self.configurationDelay)
        items.append(x + "ConfigurationDelay="+leafStr)

        x=""
        if self._myHasMuteReporting:
            x = "+"
        leafStr = str(self.muteReporting)
        items.append(x + "MuteReporting="+leafStr)

        x=""
        if self._myHasSendGratuitousArp:
            x = "+"
        leafStr = str(self.sendGratuitousArp)
        items.append(x + "SendGratuitousArp="+leafStr)

        x=""
        if self._myHasShutdown:
            x = "+"
        leafStr = str(self.shutdown)
        items.append(x + "Shutdown="+leafStr)

        x=""
        if self._myHasTechMode:
            x = "+"
        leafStr = str(self.techMode)
        items.append(x + "TechMode="+leafStr)

        return "{SystemDefaultsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemDefaultsData", 
        "namespace": "system_defaults", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.system_defaults_data_gen import SystemDefaultsData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
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
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "configurationDelay", 
            "yangName": "configuration-delay", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "sendGratuitousArp", 
            "yangName": "send-gratuitous-arp", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shutdown", 
            "yangName": "shutdown", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "techMode", 
            "yangName": "tech-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "createTime": "2013"
}
"""


