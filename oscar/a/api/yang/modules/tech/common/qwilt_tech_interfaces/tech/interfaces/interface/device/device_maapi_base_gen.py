


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class DeviceMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , interface
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , interface
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # status
    def newStatus (self):
        raise NotImplementedError()

    def setStatusObj (self, obj):
        raise NotImplementedError()

    def getStatusObj (self):
        raise NotImplementedError()

    def hasStatus (self):
        raise NotImplementedError()

    # counters
    def newCounters (self):
        raise NotImplementedError()

    def setCountersObj (self, obj):
        raise NotImplementedError()

    def getCountersObj (self):
        raise NotImplementedError()

    def hasCounters (self):
        raise NotImplementedError()




    # config leaves

    # osName
    def requestOsName (self, requested):
        raise NotImplementedError()

    def isOsNameRequested (self):
        raise NotImplementedError()

    def getOsName (self):
        raise NotImplementedError()

    def hasOsName (self):
        raise NotImplementedError()

    def setOsName (self, osName):
        raise NotImplementedError()

    # pciDeviceId
    def requestPciDeviceId (self, requested):
        raise NotImplementedError()

    def isPciDeviceIdRequested (self):
        raise NotImplementedError()

    def getPciDeviceId (self):
        raise NotImplementedError()

    def hasPciDeviceId (self):
        raise NotImplementedError()

    def setPciDeviceId (self, pciDeviceId):
        raise NotImplementedError()

    # pciVendorId
    def requestPciVendorId (self, requested):
        raise NotImplementedError()

    def isPciVendorIdRequested (self):
        raise NotImplementedError()

    def getPciVendorId (self):
        raise NotImplementedError()

    def hasPciVendorId (self):
        raise NotImplementedError()

    def setPciVendorId (self, pciVendorId):
        raise NotImplementedError()

    # postUpCommand
    def requestPostUpCommand (self, requested):
        raise NotImplementedError()

    def isPostUpCommandRequested (self):
        raise NotImplementedError()

    def getPostUpCommand (self):
        raise NotImplementedError()

    def hasPostUpCommand (self):
        raise NotImplementedError()

    def setPostUpCommand (self, postUpCommand):
        raise NotImplementedError()

    # countersClearEvent
    def requestCountersClearEvent (self, requested):
        raise NotImplementedError()

    def isCountersClearEventRequested (self):
        raise NotImplementedError()

    def getCountersClearEvent (self):
        raise NotImplementedError()

    def hasCountersClearEvent (self):
        raise NotImplementedError()

    def setCountersClearEvent (self, countersClearEvent):
        raise NotImplementedError()

    # pciIndex
    def requestPciIndex (self, requested):
        raise NotImplementedError()

    def isPciIndexRequested (self):
        raise NotImplementedError()

    def getPciIndex (self):
        raise NotImplementedError()

    def hasPciIndex (self):
        raise NotImplementedError()

    def setPciIndex (self, pciIndex):
        raise NotImplementedError()

    # postInitCommand
    def requestPostInitCommand (self, requested):
        raise NotImplementedError()

    def isPostInitCommandRequested (self):
        raise NotImplementedError()

    def getPostInitCommand (self):
        raise NotImplementedError()

    def hasPostInitCommand (self):
        raise NotImplementedError()

    def setPostInitCommand (self, postInitCommand):
        raise NotImplementedError()

    # postDownCommand
    def requestPostDownCommand (self, requested):
        raise NotImplementedError()

    def isPostDownCommandRequested (self):
        raise NotImplementedError()

    def getPostDownCommand (self):
        raise NotImplementedError()

    def hasPostDownCommand (self):
        raise NotImplementedError()

    def setPostDownCommand (self, postDownCommand):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "device", 
        "namespace": "device", 
        "className": "DeviceMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.device_maapi_gen import DeviceMaapi", 
        "baseClassName": "DeviceMaapiBase", 
        "baseModule": "device_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "device", 
            "namespace": "device", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "device"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "osName", 
            "yangName": "os-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciDeviceId", 
            "yangName": "pci-device-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciVendorId", 
            "yangName": "pci-vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postUpCommand", 
            "yangName": "post-up-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "countersClearEvent", 
            "yangName": "counters-clear-event", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pciIndex", 
            "yangName": "pci-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postInitCommand", 
            "yangName": "post-init-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postDownCommand", 
            "yangName": "post-down-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
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
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "osName", 
            "yangName": "os-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciDeviceId", 
            "yangName": "pci-device-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pciVendorId", 
            "yangName": "pci-vendor-id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postUpCommand", 
            "yangName": "post-up-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "countersClearEvent", 
            "yangName": "counters-clear-event", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pciIndex", 
            "yangName": "pci-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postInitCommand", 
            "yangName": "post-init-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "postDownCommand", 
            "yangName": "post-down-command", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


