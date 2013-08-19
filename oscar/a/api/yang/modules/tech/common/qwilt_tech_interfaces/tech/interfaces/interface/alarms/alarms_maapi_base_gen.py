


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class AlarmsMaapiBase(object):
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







    # oper leaves

    # interfaceFailureReason
    def requestInterfaceFailureReason (self, requested):
        raise NotImplementedError()

    def isInterfaceFailureReasonRequested (self):
        raise NotImplementedError()

    def getInterfaceFailureReason (self):
        raise NotImplementedError()

    def hasInterfaceFailureReason (self):
        raise NotImplementedError()

    def setInterfaceFailureReason (self, interfaceFailureReason):
        raise NotImplementedError()

    # interfaceIpv6ConnectivityFailureAlarm
    def requestInterfaceIpv6ConnectivityFailureAlarm (self, requested):
        raise NotImplementedError()

    def isInterfaceIpv6ConnectivityFailureAlarmRequested (self):
        raise NotImplementedError()

    def getInterfaceIpv6ConnectivityFailureAlarm (self):
        raise NotImplementedError()

    def hasInterfaceIpv6ConnectivityFailureAlarm (self):
        raise NotImplementedError()

    def setInterfaceIpv6ConnectivityFailureAlarm (self, interfaceIpv6ConnectivityFailureAlarm):
        raise NotImplementedError()

    # interfaceFailureAlarm
    def requestInterfaceFailureAlarm (self, requested):
        raise NotImplementedError()

    def isInterfaceFailureAlarmRequested (self):
        raise NotImplementedError()

    def getInterfaceFailureAlarm (self):
        raise NotImplementedError()

    def hasInterfaceFailureAlarm (self):
        raise NotImplementedError()

    def setInterfaceFailureAlarm (self, interfaceFailureAlarm):
        raise NotImplementedError()

    # interfaceIpv4ConnectivityFailureAlarm
    def requestInterfaceIpv4ConnectivityFailureAlarm (self, requested):
        raise NotImplementedError()

    def isInterfaceIpv4ConnectivityFailureAlarmRequested (self):
        raise NotImplementedError()

    def getInterfaceIpv4ConnectivityFailureAlarm (self):
        raise NotImplementedError()

    def hasInterfaceIpv4ConnectivityFailureAlarm (self):
        raise NotImplementedError()

    def setInterfaceIpv4ConnectivityFailureAlarm (self, interfaceIpv4ConnectivityFailureAlarm):
        raise NotImplementedError()

    # interfaceIpv4ConnectivityFailureReason
    def requestInterfaceIpv4ConnectivityFailureReason (self, requested):
        raise NotImplementedError()

    def isInterfaceIpv4ConnectivityFailureReasonRequested (self):
        raise NotImplementedError()

    def getInterfaceIpv4ConnectivityFailureReason (self):
        raise NotImplementedError()

    def hasInterfaceIpv4ConnectivityFailureReason (self):
        raise NotImplementedError()

    def setInterfaceIpv4ConnectivityFailureReason (self, interfaceIpv4ConnectivityFailureReason):
        raise NotImplementedError()

    # interfaceIpv6ConnectivityFailureReason
    def requestInterfaceIpv6ConnectivityFailureReason (self, requested):
        raise NotImplementedError()

    def isInterfaceIpv6ConnectivityFailureReasonRequested (self):
        raise NotImplementedError()

    def getInterfaceIpv6ConnectivityFailureReason (self):
        raise NotImplementedError()

    def hasInterfaceIpv6ConnectivityFailureReason (self):
        raise NotImplementedError()

    def setInterfaceIpv6ConnectivityFailureReason (self, interfaceIpv6ConnectivityFailureReason):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "alarms", 
        "namespace": "alarms", 
        "className": "AlarmsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.alarms.alarms_maapi_gen import AlarmsMaapi", 
        "baseClassName": "AlarmsMaapiBase", 
        "baseModule": "alarms_maapi_base_gen"
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
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "alarms"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceFailureReason", 
            "yangName": "interface-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceIpv6ConnectivityFailureAlarm", 
            "yangName": "interface-ipv6-connectivity-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceFailureAlarm", 
            "yangName": "interface-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceIpv4ConnectivityFailureAlarm", 
            "yangName": "interface-ipv4-connectivity-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceIpv4ConnectivityFailureReason", 
            "yangName": "interface-ipv4-connectivity-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceIpv6ConnectivityFailureReason", 
            "yangName": "interface-ipv6-connectivity-failure-reason", 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceFailureReason", 
            "yangName": "interface-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceIpv6ConnectivityFailureAlarm", 
            "yangName": "interface-ipv6-connectivity-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceFailureAlarm", 
            "yangName": "interface-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceIpv4ConnectivityFailureAlarm", 
            "yangName": "interface-ipv4-connectivity-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceIpv4ConnectivityFailureReason", 
            "yangName": "interface-ipv4-connectivity-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceIpv6ConnectivityFailureReason", 
            "yangName": "interface-ipv6-connectivity-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


