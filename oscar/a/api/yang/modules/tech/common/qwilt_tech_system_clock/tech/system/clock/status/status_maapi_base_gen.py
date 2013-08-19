


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class StatusMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # localTimeString
    def requestLocalTimeString (self, requested):
        raise NotImplementedError()

    def isLocalTimeStringRequested (self):
        raise NotImplementedError()

    def getLocalTimeString (self):
        raise NotImplementedError()

    def hasLocalTimeString (self):
        raise NotImplementedError()

    def setLocalTimeString (self, localTimeString):
        raise NotImplementedError()

    # utcTimeString
    def requestUtcTimeString (self, requested):
        raise NotImplementedError()

    def isUtcTimeStringRequested (self):
        raise NotImplementedError()

    def getUtcTimeString (self):
        raise NotImplementedError()

    def hasUtcTimeString (self):
        raise NotImplementedError()

    def setUtcTimeString (self, utcTimeString):
        raise NotImplementedError()

    # daylightSavingTime
    def requestDaylightSavingTime (self, requested):
        raise NotImplementedError()

    def isDaylightSavingTimeRequested (self):
        raise NotImplementedError()

    def getDaylightSavingTime (self):
        raise NotImplementedError()

    def hasDaylightSavingTime (self):
        raise NotImplementedError()

    def setDaylightSavingTime (self, daylightSavingTime):
        raise NotImplementedError()

    # epoch
    def requestEpoch (self, requested):
        raise NotImplementedError()

    def isEpochRequested (self):
        raise NotImplementedError()

    def getEpoch (self):
        raise NotImplementedError()

    def hasEpoch (self):
        raise NotImplementedError()

    def setEpoch (self, epoch):
        raise NotImplementedError()

    # utcOffsetMinutes
    def requestUtcOffsetMinutes (self, requested):
        raise NotImplementedError()

    def isUtcOffsetMinutesRequested (self):
        raise NotImplementedError()

    def getUtcOffsetMinutes (self):
        raise NotImplementedError()

    def hasUtcOffsetMinutes (self):
        raise NotImplementedError()

    def setUtcOffsetMinutes (self, utcOffsetMinutes):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_clock.tech.system.clock.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "system", 
            "namespace": "system", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "yangName": "clock", 
            "namespace": "clock", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "name": "clock"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "localTimeString", 
            "yangName": "local-time-string", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "utcTimeString", 
            "yangName": "utc-time-string", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "daylightSavingTime", 
            "yangName": "daylight-saving-time", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "epoch", 
            "yangName": "epoch", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "utcOffsetMinutes", 
            "yangName": "utc-offset-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_system_clock"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "localTimeString", 
            "yangName": "local-time-string", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "utcTimeString", 
            "yangName": "utc-time-string", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "daylightSavingTime", 
            "yangName": "daylight-saving-time", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "epoch", 
            "yangName": "epoch", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-clock", 
            "moduleYangNamespacePrefix": "qt-sys-clock", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "utcOffsetMinutes", 
            "yangName": "utc-offset-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


