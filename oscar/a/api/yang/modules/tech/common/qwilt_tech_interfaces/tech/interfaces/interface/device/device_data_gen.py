


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import DeviceCountersClearEventType


class DeviceData(object):

    def __init__ (self):

        self.osName = ""
        self._myHasOsName=False
        
        self.pciDeviceId = ""
        self._myHasPciDeviceId=False
        
        self.pciVendorId = ""
        self._myHasPciVendorId=False
        
        self.postUpCommand = ""
        self._myHasPostUpCommand=False
        
        self.countersClearEvent = DeviceCountersClearEventType.kNone
        self._myHasCountersClearEvent=False
        
        self.pciIndex = 0
        self._myHasPciIndex=False
        
        self.postInitCommand = ""
        self._myHasPostInitCommand=False
        
        self.postDownCommand = ""
        self._myHasPostDownCommand=False
        

    def copyFrom (self, other):

        self.osName=other.osName
        self._myHasOsName=other._myHasOsName
        
        self.pciDeviceId=other.pciDeviceId
        self._myHasPciDeviceId=other._myHasPciDeviceId
        
        self.pciVendorId=other.pciVendorId
        self._myHasPciVendorId=other._myHasPciVendorId
        
        self.postUpCommand=other.postUpCommand
        self._myHasPostUpCommand=other._myHasPostUpCommand
        
        self.countersClearEvent=other.countersClearEvent
        self._myHasCountersClearEvent=other._myHasCountersClearEvent
        
        self.pciIndex=other.pciIndex
        self._myHasPciIndex=other._myHasPciIndex
        
        self.postInitCommand=other.postInitCommand
        self._myHasPostInitCommand=other._myHasPostInitCommand
        
        self.postDownCommand=other.postDownCommand
        self._myHasPostDownCommand=other._myHasPostDownCommand
        
    # has...() methods

    def hasOsName (self):
        return self._myHasOsName

    def hasPciDeviceId (self):
        return self._myHasPciDeviceId

    def hasPciVendorId (self):
        return self._myHasPciVendorId

    def hasPostUpCommand (self):
        return self._myHasPostUpCommand

    def hasCountersClearEvent (self):
        return self._myHasCountersClearEvent

    def hasPciIndex (self):
        return self._myHasPciIndex

    def hasPostInitCommand (self):
        return self._myHasPostInitCommand

    def hasPostDownCommand (self):
        return self._myHasPostDownCommand


    # setHas...() methods

    def setHasOsName (self):
        self._myHasOsName=True

    def setHasPciDeviceId (self):
        self._myHasPciDeviceId=True

    def setHasPciVendorId (self):
        self._myHasPciVendorId=True

    def setHasPostUpCommand (self):
        self._myHasPostUpCommand=True

    def setHasCountersClearEvent (self):
        self._myHasCountersClearEvent=True

    def setHasPciIndex (self):
        self._myHasPciIndex=True

    def setHasPostInitCommand (self):
        self._myHasPostInitCommand=True

    def setHasPostDownCommand (self):
        self._myHasPostDownCommand=True


    def clearAllHas (self):

        self._myHasOsName=False

        self._myHasPciDeviceId=False

        self._myHasPciVendorId=False

        self._myHasPostUpCommand=False

        self._myHasCountersClearEvent=False

        self._myHasPciIndex=False

        self._myHasPostInitCommand=False

        self._myHasPostDownCommand=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasOsName:
            x = "+"
        leafStr = str(self.osName)
        items.append(x + "OsName="+leafStr)

        x=""
        if self._myHasPciDeviceId:
            x = "+"
        leafStr = str(self.pciDeviceId)
        items.append(x + "PciDeviceId="+leafStr)

        x=""
        if self._myHasPciVendorId:
            x = "+"
        leafStr = str(self.pciVendorId)
        items.append(x + "PciVendorId="+leafStr)

        x=""
        if self._myHasPostUpCommand:
            x = "+"
        leafStr = str(self.postUpCommand)
        items.append(x + "PostUpCommand="+leafStr)

        x=""
        if self._myHasCountersClearEvent:
            x = "+"
        leafStr = str(self.countersClearEvent)
        items.append(x + "CountersClearEvent="+leafStr)

        x=""
        if self._myHasPciIndex:
            x = "+"
        leafStr = str(self.pciIndex)
        items.append(x + "PciIndex="+leafStr)

        x=""
        if self._myHasPostInitCommand:
            x = "+"
        leafStr = str(self.postInitCommand)
        items.append(x + "PostInitCommand="+leafStr)

        x=""
        if self._myHasPostDownCommand:
            x = "+"
        leafStr = str(self.postDownCommand)
        items.append(x + "PostDownCommand="+leafStr)

        return "{DeviceData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DeviceData", 
        "namespace": "device", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.device_data_gen import DeviceData"
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
            "namespace": "device", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "osName", 
            "yangName": "os-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciDeviceId", 
            "yangName": "pci-device-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciVendorId", 
            "yangName": "pci-vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "postUpCommand", 
            "yangName": "post-up-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "countersClearEvent", 
            "yangName": "counters-clear-event", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pciIndex", 
            "yangName": "pci-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "postInitCommand", 
            "yangName": "post-init-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "postDownCommand", 
            "yangName": "post-down-command", 
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


