


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class InterfaceData(object):

    def __init__ (self):

        self.shutdown = False
        self._myHasShutdown=False
        
        self.muteReporting = False
        self._myHasMuteReporting=False
        
        self.techMode = False
        self._myHasTechMode=False
        
        self.description = ""
        self._myHasDescription=False
        
        self.configurationDelay = 0
        self._myHasConfigurationDelay=False
        
        self.name = ""
        self._myHasName=False
        
        self.sendGratuitousArp = False
        self._myHasSendGratuitousArp=False
        
        self.mibIfIndex = 0
        self._myHasMibIfIndex=False
        

    def copyFrom (self, other):

        self.shutdown=other.shutdown
        self._myHasShutdown=other._myHasShutdown
        
        self.muteReporting=other.muteReporting
        self._myHasMuteReporting=other._myHasMuteReporting
        
        self.techMode=other.techMode
        self._myHasTechMode=other._myHasTechMode
        
        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.configurationDelay=other.configurationDelay
        self._myHasConfigurationDelay=other._myHasConfigurationDelay
        
        self.name=other.name
        self._myHasName=other._myHasName
        
        self.sendGratuitousArp=other.sendGratuitousArp
        self._myHasSendGratuitousArp=other._myHasSendGratuitousArp
        
        self.mibIfIndex=other.mibIfIndex
        self._myHasMibIfIndex=other._myHasMibIfIndex
        
    # has...() methods

    def hasShutdown (self):
        return self._myHasShutdown

    def hasMuteReporting (self):
        return self._myHasMuteReporting

    def hasTechMode (self):
        return self._myHasTechMode

    def hasDescription (self):
        return self._myHasDescription

    def hasConfigurationDelay (self):
        return self._myHasConfigurationDelay

    def hasName (self):
        return self._myHasName

    def hasSendGratuitousArp (self):
        return self._myHasSendGratuitousArp

    def hasMibIfIndex (self):
        return self._myHasMibIfIndex


    # setHas...() methods

    def setHasShutdown (self):
        self._myHasShutdown=True

    def setHasMuteReporting (self):
        self._myHasMuteReporting=True

    def setHasTechMode (self):
        self._myHasTechMode=True

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasConfigurationDelay (self):
        self._myHasConfigurationDelay=True

    def setHasName (self):
        self._myHasName=True

    def setHasSendGratuitousArp (self):
        self._myHasSendGratuitousArp=True

    def setHasMibIfIndex (self):
        self._myHasMibIfIndex=True


    def clearAllHas (self):

        self._myHasShutdown=False

        self._myHasMuteReporting=False

        self._myHasTechMode=False

        self._myHasDescription=False

        self._myHasConfigurationDelay=False

        self._myHasName=False

        self._myHasSendGratuitousArp=False

        self._myHasMibIfIndex=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasShutdown:
            x = "+"
        leafStr = str(self.shutdown)
        items.append(x + "Shutdown="+leafStr)

        x=""
        if self._myHasMuteReporting:
            x = "+"
        leafStr = str(self.muteReporting)
        items.append(x + "MuteReporting="+leafStr)

        x=""
        if self._myHasTechMode:
            x = "+"
        leafStr = str(self.techMode)
        items.append(x + "TechMode="+leafStr)

        x=""
        if self._myHasDescription:
            x = "+"
        leafStr = str(self.description)
        items.append(x + "Description="+leafStr)

        x=""
        if self._myHasConfigurationDelay:
            x = "+"
        leafStr = str(self.configurationDelay)
        items.append(x + "ConfigurationDelay="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasSendGratuitousArp:
            x = "+"
        leafStr = str(self.sendGratuitousArp)
        items.append(x + "SendGratuitousArp="+leafStr)

        x=""
        if self._myHasMibIfIndex:
            x = "+"
        leafStr = str(self.mibIfIndex)
        items.append(x + "MibIfIndex="+leafStr)

        return "{InterfaceData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "InterfaceData", 
        "namespace": "interface", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.interface_data_gen import InterfaceData"
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
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shutdown", 
            "yangName": "shutdown", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "techMode", 
            "yangName": "tech-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "configurationDelay", 
            "yangName": "configuration-delay", 
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
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "sendGratuitousArp", 
            "yangName": "send-gratuitous-arp", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "mibIfIndex", 
            "yangName": "mib-if-index", 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "createTime": "2013"
}
"""


