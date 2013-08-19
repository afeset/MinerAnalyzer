


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class MatchMaapiBase(object):
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
              , rule
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , loggerClass
              , instance
              , rule
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       , rule
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # minSeverity
    def requestMinSeverity (self, requested):
        raise NotImplementedError()

    def isMinSeverityRequested (self):
        raise NotImplementedError()

    def getMinSeverity (self):
        raise NotImplementedError()

    def hasMinSeverity (self):
        raise NotImplementedError()

    def setMinSeverity (self, minSeverity):
        raise NotImplementedError()

    # function
    def requestFunction (self, requested):
        raise NotImplementedError()

    def isFunctionRequested (self):
        raise NotImplementedError()

    def getFunction (self):
        raise NotImplementedError()

    def hasFunction (self):
        raise NotImplementedError()

    def setFunction (self, function):
        raise NotImplementedError()

    # messageName
    def requestMessageName (self, requested):
        raise NotImplementedError()

    def isMessageNameRequested (self):
        raise NotImplementedError()

    def getMessageName (self):
        raise NotImplementedError()

    def hasMessageName (self):
        raise NotImplementedError()

    def setMessageName (self, messageName):
        raise NotImplementedError()

    # group
    def requestGroup (self, requested):
        raise NotImplementedError()

    def isGroupRequested (self):
        raise NotImplementedError()

    def getGroup (self):
        raise NotImplementedError()

    def hasGroup (self):
        raise NotImplementedError()

    def setGroup (self, group):
        raise NotImplementedError()

    # maxLine
    def requestMaxLine (self, requested):
        raise NotImplementedError()

    def isMaxLineRequested (self):
        raise NotImplementedError()

    def getMaxLine (self):
        raise NotImplementedError()

    def hasMaxLine (self):
        raise NotImplementedError()

    def setMaxLine (self, maxLine):
        raise NotImplementedError()

    # minLine
    def requestMinLine (self, requested):
        raise NotImplementedError()

    def isMinLineRequested (self):
        raise NotImplementedError()

    def getMinLine (self):
        raise NotImplementedError()

    def hasMinLine (self):
        raise NotImplementedError()

    def setMinLine (self, minLine):
        raise NotImplementedError()

    # module
    def requestModule (self, requested):
        raise NotImplementedError()

    def isModuleRequested (self):
        raise NotImplementedError()

    def getModule (self):
        raise NotImplementedError()

    def hasModule (self):
        raise NotImplementedError()

    def setModule (self, module):
        raise NotImplementedError()

    # file
    def requestFile (self, requested):
        raise NotImplementedError()

    def isFileRequested (self):
        raise NotImplementedError()

    def getFile (self):
        raise NotImplementedError()

    def hasFile (self):
        raise NotImplementedError()

    def setFile (self, file):
        raise NotImplementedError()

    # conditional
    def requestConditional (self, requested):
        raise NotImplementedError()

    def isConditionalRequested (self):
        raise NotImplementedError()

    def getConditional (self):
        raise NotImplementedError()

    def hasConditional (self):
        raise NotImplementedError()

    def setConditional (self, conditional):
        raise NotImplementedError()

    # maxSeverity
    def requestMaxSeverity (self, requested):
        raise NotImplementedError()

    def isMaxSeverityRequested (self):
        raise NotImplementedError()

    def getMaxSeverity (self):
        raise NotImplementedError()

    def hasMaxSeverity (self):
        raise NotImplementedError()

    def setMaxSeverity (self, maxSeverity):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "match", 
        "namespace": "match", 
        "className": "MatchMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.rule.match.match_maapi_gen import MatchMaapi", 
        "baseClassName": "MatchMaapiBase", 
        "baseModule": "match_maapi_base_gen"
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
            "yangName": "rule", 
            "namespace": "rule", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "rule", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "rule"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "match", 
            "namespace": "match", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "match"
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "minSeverity", 
            "yangName": "min-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "function", 
            "yangName": "function", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageName", 
            "yangName": "message-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "group", 
            "yangName": "group", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxLine", 
            "yangName": "max-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minLine", 
            "yangName": "min-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "module", 
            "yangName": "module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "file", 
            "yangName": "file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "conditional", 
            "yangName": "conditional", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "maxSeverity", 
            "yangName": "max-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "minSeverity", 
            "yangName": "min-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "function", 
            "yangName": "function", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageName", 
            "yangName": "message-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "group", 
            "yangName": "group", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxLine", 
            "yangName": "max-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minLine", 
            "yangName": "min-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "module", 
            "yangName": "module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "file", 
            "yangName": "file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "conditional", 
            "yangName": "conditional", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "maxSeverity", 
            "yangName": "max-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


