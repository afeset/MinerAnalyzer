


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

        self.pciDeviceId = ""
        self._myHasPciDeviceId=False
        
        self.countersClearEvent = DeviceCountersClearEventType.kNone
        self._myHasCountersClearEvent=False
        
        self.pciVendorId = ""
        self._myHasPciVendorId=False
        
        self.pciIndex = 0
        self._myHasPciIndex=False
        
        self.osName = ""
        self._myHasOsName=False
        

    def copyFrom (self, other):

        self.pciDeviceId=other.pciDeviceId
        self._myHasPciDeviceId=other._myHasPciDeviceId
        
        self.countersClearEvent=other.countersClearEvent
        self._myHasCountersClearEvent=other._myHasCountersClearEvent
        
        self.pciVendorId=other.pciVendorId
        self._myHasPciVendorId=other._myHasPciVendorId
        
        self.pciIndex=other.pciIndex
        self._myHasPciIndex=other._myHasPciIndex
        
        self.osName=other.osName
        self._myHasOsName=other._myHasOsName
        
    # has...() methods

    def hasPciDeviceId (self):
        return self._myHasPciDeviceId

    def hasCountersClearEvent (self):
        return self._myHasCountersClearEvent

    def hasPciVendorId (self):
        return self._myHasPciVendorId

    def hasPciIndex (self):
        return self._myHasPciIndex

    def hasOsName (self):
        return self._myHasOsName


    # setHas...() methods

    def setHasPciDeviceId (self):
        self._myHasPciDeviceId=True

    def setHasCountersClearEvent (self):
        self._myHasCountersClearEvent=True

    def setHasPciVendorId (self):
        self._myHasPciVendorId=True

    def setHasPciIndex (self):
        self._myHasPciIndex=True

    def setHasOsName (self):
        self._myHasOsName=True


    def clearAllHas (self):

        self._myHasPciDeviceId=False

        self._myHasCountersClearEvent=False

        self._myHasPciVendorId=False

        self._myHasPciIndex=False

        self._myHasOsName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasPciDeviceId:
            x = "+"
        leafStr = str(self.pciDeviceId)
        items.append(x + "PciDeviceId="+leafStr)

        x=""
        if self._myHasCountersClearEvent:
            x = "+"
        leafStr = str(self.countersClearEvent)
        items.append(x + "CountersClearEvent="+leafStr)

        x=""
        if self._myHasPciVendorId:
            x = "+"
        leafStr = str(self.pciVendorId)
        items.append(x + "PciVendorId="+leafStr)

        x=""
        if self._myHasPciIndex:
            x = "+"
        leafStr = str(self.pciIndex)
        items.append(x + "PciIndex="+leafStr)

        x=""
        if self._myHasOsName:
            x = "+"
        leafStr = str(self.osName)
        items.append(x + "OsName="+leafStr)

        return "{DeviceData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DeviceData", 
        "namespace": "device", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.device.device_data_gen import DeviceData"
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
            "memberName": "pciDeviceId", 
            "yangName": "pci-device-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "countersClearEvent", 
            "yangName": "counters-clear-event", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciVendorId", 
            "yangName": "pci-vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pciIndex", 
            "yangName": "pci-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "osName", 
            "yangName": "os-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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


