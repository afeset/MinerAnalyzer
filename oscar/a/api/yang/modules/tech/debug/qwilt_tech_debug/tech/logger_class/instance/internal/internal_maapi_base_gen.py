


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class InternalMaapiBase(object):
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
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , loggerClass
              , instance
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # burstLimits
    def newBurstLimits (self):
        raise NotImplementedError()

    def setBurstLimitsObj (self, obj):
        raise NotImplementedError()

    def getBurstLimitsObj (self):
        raise NotImplementedError()

    def hasBurstLimits (self):
        raise NotImplementedError()




    # config leaves

    # maxMessageRecursionDepth
    def requestMaxMessageRecursionDepth (self, requested):
        raise NotImplementedError()

    def isMaxMessageRecursionDepthRequested (self):
        raise NotImplementedError()

    def getMaxMessageRecursionDepth (self):
        raise NotImplementedError()

    def hasMaxMessageRecursionDepth (self):
        raise NotImplementedError()

    def setMaxMessageRecursionDepth (self, maxMessageRecursionDepth):
        raise NotImplementedError()

    # logMessageProcessing
    def requestLogMessageProcessing (self, requested):
        raise NotImplementedError()

    def isLogMessageProcessingRequested (self):
        raise NotImplementedError()

    def getLogMessageProcessing (self):
        raise NotImplementedError()

    def hasLogMessageProcessing (self):
        raise NotImplementedError()

    def setLogMessageProcessing (self, logMessageProcessing):
        raise NotImplementedError()

    # logAction
    def requestLogAction (self, requested):
        raise NotImplementedError()

    def isLogActionRequested (self):
        raise NotImplementedError()

    def getLogAction (self):
        raise NotImplementedError()

    def hasLogAction (self):
        raise NotImplementedError()

    def setLogAction (self, logAction):
        raise NotImplementedError()

    # maxMessageBodySize
    def requestMaxMessageBodySize (self, requested):
        raise NotImplementedError()

    def isMaxMessageBodySizeRequested (self):
        raise NotImplementedError()

    def getMaxMessageBodySize (self):
        raise NotImplementedError()

    def hasMaxMessageBodySize (self):
        raise NotImplementedError()

    def setMaxMessageBodySize (self, maxMessageBodySize):
        raise NotImplementedError()

    # maxImplicitMessages
    def requestMaxImplicitMessages (self, requested):
        raise NotImplementedError()

    def isMaxImplicitMessagesRequested (self):
        raise NotImplementedError()

    def getMaxImplicitMessages (self):
        raise NotImplementedError()

    def hasMaxImplicitMessages (self):
        raise NotImplementedError()

    def setMaxImplicitMessages (self, maxImplicitMessages):
        raise NotImplementedError()

    # messageRecursionWarningThreshold
    def requestMessageRecursionWarningThreshold (self, requested):
        raise NotImplementedError()

    def isMessageRecursionWarningThresholdRequested (self):
        raise NotImplementedError()

    def getMessageRecursionWarningThreshold (self):
        raise NotImplementedError()

    def hasMessageRecursionWarningThreshold (self):
        raise NotImplementedError()

    def setMessageRecursionWarningThreshold (self, messageRecursionWarningThreshold):
        raise NotImplementedError()

    # logMessageCreation
    def requestLogMessageCreation (self, requested):
        raise NotImplementedError()

    def isLogMessageCreationRequested (self):
        raise NotImplementedError()

    def getLogMessageCreation (self):
        raise NotImplementedError()

    def hasLogMessageCreation (self):
        raise NotImplementedError()

    def setLogMessageCreation (self, logMessageCreation):
        raise NotImplementedError()

    # maxLoggerShutdownTime
    def requestMaxLoggerShutdownTime (self, requested):
        raise NotImplementedError()

    def isMaxLoggerShutdownTimeRequested (self):
        raise NotImplementedError()

    def getMaxLoggerShutdownTime (self):
        raise NotImplementedError()

    def hasMaxLoggerShutdownTime (self):
        raise NotImplementedError()

    def setMaxLoggerShutdownTime (self, maxLoggerShutdownTime):
        raise NotImplementedError()

    # logConfiguration
    def requestLogConfiguration (self, requested):
        raise NotImplementedError()

    def isLogConfigurationRequested (self):
        raise NotImplementedError()

    def getLogConfiguration (self):
        raise NotImplementedError()

    def hasLogConfiguration (self):
        raise NotImplementedError()

    def setLogConfiguration (self, logConfiguration):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "internal", 
        "namespace": "internal", 
        "className": "InternalMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.internal.internal_maapi_gen import InternalMaapi", 
        "baseClassName": "InternalMaapiBase", 
        "baseModule": "internal_maapi_base_gen"
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
            "yangName": "internal", 
            "namespace": "internal", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "internal"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "memberName": "burstLimits", 
            "yangName": "burst-limits", 
            "className": "BlinkyBurstLimitsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.internal.burst_limits.burst_limits_maapi_gen import BlinkyBurstLimitsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxMessageRecursionDepth", 
            "yangName": "max-message-recursion-depth", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logMessageProcessing", 
            "yangName": "log-message-processing", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logAction", 
            "yangName": "log-action", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxMessageBodySize", 
            "yangName": "max-message-body-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxImplicitMessages", 
            "yangName": "max-implicit-messages", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "messageRecursionWarningThreshold", 
            "yangName": "message-recursion-warning-threshold", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logMessageCreation", 
            "yangName": "log-message-creation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxLoggerShutdownTime", 
            "yangName": "max-logger-shutdown-time", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logConfiguration", 
            "yangName": "log-configuration", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxMessageRecursionDepth", 
            "yangName": "max-message-recursion-depth", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logMessageProcessing", 
            "yangName": "log-message-processing", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logAction", 
            "yangName": "log-action", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxMessageBodySize", 
            "yangName": "max-message-body-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxImplicitMessages", 
            "yangName": "max-implicit-messages", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "messageRecursionWarningThreshold", 
            "yangName": "message-recursion-warning-threshold", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logMessageCreation", 
            "yangName": "log-message-creation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxLoggerShutdownTime", 
            "yangName": "max-logger-shutdown-time", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logConfiguration", 
            "yangName": "log-configuration", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


