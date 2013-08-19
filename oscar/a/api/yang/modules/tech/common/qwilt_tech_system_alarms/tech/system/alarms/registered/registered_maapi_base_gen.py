


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class RegisteredMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , registered
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , registered
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , registered
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # description
    def requestDescription (self, requested):
        raise NotImplementedError()

    def isDescriptionRequested (self):
        raise NotImplementedError()

    def getDescription (self):
        raise NotImplementedError()

    def hasDescription (self):
        raise NotImplementedError()

    def setDescription (self, description):
        raise NotImplementedError()

    # devComment
    def requestDevComment (self, requested):
        raise NotImplementedError()

    def isDevCommentRequested (self):
        raise NotImplementedError()

    def getDevComment (self):
        raise NotImplementedError()

    def hasDevComment (self):
        raise NotImplementedError()

    def setDevComment (self, devComment):
        raise NotImplementedError()

    # softwareVersion
    def requestSoftwareVersion (self, requested):
        raise NotImplementedError()

    def isSoftwareVersionRequested (self):
        raise NotImplementedError()

    def getSoftwareVersion (self):
        raise NotImplementedError()

    def hasSoftwareVersion (self):
        raise NotImplementedError()

    def setSoftwareVersion (self, softwareVersion):
        raise NotImplementedError()

    # name
    def requestName (self, requested):
        raise NotImplementedError()

    def isNameRequested (self):
        raise NotImplementedError()

    def getName (self):
        raise NotImplementedError()

    def hasName (self):
        raise NotImplementedError()

    def setName (self, name):
        raise NotImplementedError()

    # source
    def requestSource (self, requested):
        raise NotImplementedError()

    def isSourceRequested (self):
        raise NotImplementedError()

    def getSource (self):
        raise NotImplementedError()

    def hasSource (self):
        raise NotImplementedError()

    def setSource (self, source):
        raise NotImplementedError()

    # state
    def requestState (self, requested):
        raise NotImplementedError()

    def isStateRequested (self):
        raise NotImplementedError()

    def getState (self):
        raise NotImplementedError()

    def hasState (self):
        raise NotImplementedError()

    def setState (self, state):
        raise NotImplementedError()

    # severity
    def requestSeverity (self, requested):
        raise NotImplementedError()

    def isSeverityRequested (self):
        raise NotImplementedError()

    def getSeverity (self):
        raise NotImplementedError()

    def hasSeverity (self):
        raise NotImplementedError()

    def setSeverity (self, severity):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "registered", 
        "namespace": "registered", 
        "className": "RegisteredMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.registered.registered_maapi_gen import RegisteredMaapi", 
        "baseClassName": "RegisteredMaapiBase", 
        "baseModule": "registered_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "isCurrent": true, 
            "yangName": "registered", 
            "namespace": "registered", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "keyLeaf": {
                "varName": "registered", 
                "defaultVal": null, 
                "typeHandler": "handler: EnumHandlerPy"
            }, 
            "name": "registered"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "devComment", 
            "yangName": "dev-comment", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "softwareVersion", 
            "yangName": "software-version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "source", 
            "yangName": "source", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "severity", 
            "yangName": "severity", 
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
            "qwilt_tech_system_alarms"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "devComment", 
            "yangName": "dev-comment", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "softwareVersion", 
            "yangName": "software-version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "source", 
            "yangName": "source", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "state", 
            "yangName": "state", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "severity", 
            "yangName": "severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


