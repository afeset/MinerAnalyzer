


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class FormatMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , loggerClass
              , instance
              , destination
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , loggerClass
              , instance
              , destination
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       , destination
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # messageExtra
    def requestMessageExtra (self, requested):
        raise NotImplementedError()

    def isMessageExtraRequested (self):
        raise NotImplementedError()

    def getMessageExtra (self):
        raise NotImplementedError()

    def hasMessageExtra (self):
        raise NotImplementedError()

    def setMessageExtra (self, messageExtra):
        raise NotImplementedError()

    # messageBase
    def requestMessageBase (self, requested):
        raise NotImplementedError()

    def isMessageBaseRequested (self):
        raise NotImplementedError()

    def getMessageBase (self):
        raise NotImplementedError()

    def hasMessageBase (self):
        raise NotImplementedError()

    def setMessageBase (self, messageBase):
        raise NotImplementedError()

    # payload
    def requestPayload (self, requested):
        raise NotImplementedError()

    def isPayloadRequested (self):
        raise NotImplementedError()

    def getPayload (self):
        raise NotImplementedError()

    def hasPayload (self):
        raise NotImplementedError()

    def setPayload (self, payload):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "format", 
        "namespace": "format", 
        "className": "FormatMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.format.format_maapi_gen import FormatMaapi", 
        "baseClassName": "FormatMaapiBase", 
        "baseModule": "format_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "logger-class", 
            "namespace": "logger_class", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "loggerClass", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "logger-class"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "instance", 
            "namespace": "instance", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "instance", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "instance"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "destination", 
            "namespace": "destination", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "destination", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "destination"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "format", 
            "namespace": "format", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "format"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageExtra", 
            "yangName": "message-extra", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageBase", 
            "yangName": "message-base", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "payload", 
            "yangName": "payload", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "debug", 
            "qwilt_tech_debug"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageExtra", 
            "yangName": "message-extra", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageBase", 
            "yangName": "message-base", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "payload", 
            "yangName": "payload", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


