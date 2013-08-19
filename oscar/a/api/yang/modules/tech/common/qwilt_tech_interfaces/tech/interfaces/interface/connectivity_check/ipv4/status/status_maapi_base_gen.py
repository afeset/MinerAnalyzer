


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

    # actualMethod
    def requestActualMethod (self, requested):
        raise NotImplementedError()

    def isActualMethodRequested (self):
        raise NotImplementedError()

    def getActualMethod (self):
        raise NotImplementedError()

    def hasActualMethod (self):
        raise NotImplementedError()

    def setActualMethod (self, actualMethod):
        raise NotImplementedError()

    # operationalStatus
    def requestOperationalStatus (self, requested):
        raise NotImplementedError()

    def isOperationalStatusRequested (self):
        raise NotImplementedError()

    def getOperationalStatus (self):
        raise NotImplementedError()

    def hasOperationalStatus (self):
        raise NotImplementedError()

    def setOperationalStatus (self, operationalStatus):
        raise NotImplementedError()

    # operationalStatusReason
    def requestOperationalStatusReason (self, requested):
        raise NotImplementedError()

    def isOperationalStatusReasonRequested (self):
        raise NotImplementedError()

    def getOperationalStatusReason (self):
        raise NotImplementedError()

    def hasOperationalStatusReason (self):
        raise NotImplementedError()

    def setOperationalStatusReason (self, operationalStatusReason):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.status.status_maapi_gen import StatusMaapi", 
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
            "yangName": "connectivity-check", 
            "namespace": "connectivity_check", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "connectivity-check"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "ipv4", 
            "namespace": "ipv4", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "ipv4"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "actualMethod", 
            "yangName": "actual-method", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
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
            "memberName": "actualMethod", 
            "yangName": "actual-method", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


