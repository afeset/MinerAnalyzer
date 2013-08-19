


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class TimeoutsMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , controller
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , controller
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , controller
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # getLogicalDiskStatus
    def requestGetLogicalDiskStatus (self, requested):
        raise NotImplementedError()

    def isGetLogicalDiskStatusRequested (self):
        raise NotImplementedError()

    def getGetLogicalDiskStatus (self):
        raise NotImplementedError()

    def hasGetLogicalDiskStatus (self):
        raise NotImplementedError()

    def setGetLogicalDiskStatus (self, getLogicalDiskStatus):
        raise NotImplementedError()

    # getPhysicalStatus
    def requestGetPhysicalStatus (self, requested):
        raise NotImplementedError()

    def isGetPhysicalStatusRequested (self):
        raise NotImplementedError()

    def getGetPhysicalStatus (self):
        raise NotImplementedError()

    def hasGetPhysicalStatus (self):
        raise NotImplementedError()

    def setGetPhysicalStatus (self, getPhysicalStatus):
        raise NotImplementedError()

    # activateLogicalDisk
    def requestActivateLogicalDisk (self, requested):
        raise NotImplementedError()

    def isActivateLogicalDiskRequested (self):
        raise NotImplementedError()

    def getActivateLogicalDisk (self):
        raise NotImplementedError()

    def hasActivateLogicalDisk (self):
        raise NotImplementedError()

    def setActivateLogicalDisk (self, activateLogicalDisk):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "timeouts", 
        "namespace": "timeouts", 
        "className": "TimeoutsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_controller.tech.storage.controller.system_defaults.timeouts.timeouts_maapi_gen import TimeoutsMaapi", 
        "baseClassName": "TimeoutsMaapiBase", 
        "baseModule": "timeouts_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "isCurrent": false, 
            "yangName": "controller", 
            "namespace": "controller", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "keyLeaf": {
                "varName": "controller", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "controller"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "yangName": "timeouts", 
            "namespace": "timeouts", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "name": "timeouts"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "getLogicalDiskStatus", 
            "yangName": "get-logical-disk-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "getPhysicalStatus", 
            "yangName": "get-physical-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activateLogicalDisk", 
            "yangName": "activate-logical-disk", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
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
            "qwilt_tech_storage_controller"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "getLogicalDiskStatus", 
            "yangName": "get-logical-disk-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "getPhysicalStatus", 
            "yangName": "get-physical-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-controller", 
            "moduleYangNamespacePrefix": "qt-strg-ctrl", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activateLogicalDisk", 
            "yangName": "activate-logical-disk", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


