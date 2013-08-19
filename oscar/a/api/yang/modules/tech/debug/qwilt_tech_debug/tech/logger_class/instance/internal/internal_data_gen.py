


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogSeverity


class InternalData(object):

    def __init__ (self):

        self.maxMessageRecursionDepth = 0
        self._myHasMaxMessageRecursionDepth=False
        
        self.logMessageProcessing = LogSeverity.kDebug1
        self._myHasLogMessageProcessing=False
        
        self.logAction = LogSeverity.kDebug1
        self._myHasLogAction=False
        
        self.maxMessageBodySize = 0
        self._myHasMaxMessageBodySize=False
        
        self.maxImplicitMessages = 0
        self._myHasMaxImplicitMessages=False
        
        self.messageRecursionWarningThreshold = 0
        self._myHasMessageRecursionWarningThreshold=False
        
        self.logMessageCreation = LogSeverity.kDebug1
        self._myHasLogMessageCreation=False
        
        self.maxLoggerShutdownTime = 0
        self._myHasMaxLoggerShutdownTime=False
        
        self.logConfiguration = LogSeverity.kDebug1
        self._myHasLogConfiguration=False
        

    def copyFrom (self, other):

        self.maxMessageRecursionDepth=other.maxMessageRecursionDepth
        self._myHasMaxMessageRecursionDepth=other._myHasMaxMessageRecursionDepth
        
        self.logMessageProcessing=other.logMessageProcessing
        self._myHasLogMessageProcessing=other._myHasLogMessageProcessing
        
        self.logAction=other.logAction
        self._myHasLogAction=other._myHasLogAction
        
        self.maxMessageBodySize=other.maxMessageBodySize
        self._myHasMaxMessageBodySize=other._myHasMaxMessageBodySize
        
        self.maxImplicitMessages=other.maxImplicitMessages
        self._myHasMaxImplicitMessages=other._myHasMaxImplicitMessages
        
        self.messageRecursionWarningThreshold=other.messageRecursionWarningThreshold
        self._myHasMessageRecursionWarningThreshold=other._myHasMessageRecursionWarningThreshold
        
        self.logMessageCreation=other.logMessageCreation
        self._myHasLogMessageCreation=other._myHasLogMessageCreation
        
        self.maxLoggerShutdownTime=other.maxLoggerShutdownTime
        self._myHasMaxLoggerShutdownTime=other._myHasMaxLoggerShutdownTime
        
        self.logConfiguration=other.logConfiguration
        self._myHasLogConfiguration=other._myHasLogConfiguration
        
    # has...() methods

    def hasMaxMessageRecursionDepth (self):
        return self._myHasMaxMessageRecursionDepth

    def hasLogMessageProcessing (self):
        return self._myHasLogMessageProcessing

    def hasLogAction (self):
        return self._myHasLogAction

    def hasMaxMessageBodySize (self):
        return self._myHasMaxMessageBodySize

    def hasMaxImplicitMessages (self):
        return self._myHasMaxImplicitMessages

    def hasMessageRecursionWarningThreshold (self):
        return self._myHasMessageRecursionWarningThreshold

    def hasLogMessageCreation (self):
        return self._myHasLogMessageCreation

    def hasMaxLoggerShutdownTime (self):
        return self._myHasMaxLoggerShutdownTime

    def hasLogConfiguration (self):
        return self._myHasLogConfiguration


    # setHas...() methods

    def setHasMaxMessageRecursionDepth (self):
        self._myHasMaxMessageRecursionDepth=True

    def setHasLogMessageProcessing (self):
        self._myHasLogMessageProcessing=True

    def setHasLogAction (self):
        self._myHasLogAction=True

    def setHasMaxMessageBodySize (self):
        self._myHasMaxMessageBodySize=True

    def setHasMaxImplicitMessages (self):
        self._myHasMaxImplicitMessages=True

    def setHasMessageRecursionWarningThreshold (self):
        self._myHasMessageRecursionWarningThreshold=True

    def setHasLogMessageCreation (self):
        self._myHasLogMessageCreation=True

    def setHasMaxLoggerShutdownTime (self):
        self._myHasMaxLoggerShutdownTime=True

    def setHasLogConfiguration (self):
        self._myHasLogConfiguration=True


    def clearAllHas (self):

        self._myHasMaxMessageRecursionDepth=False

        self._myHasLogMessageProcessing=False

        self._myHasLogAction=False

        self._myHasMaxMessageBodySize=False

        self._myHasMaxImplicitMessages=False

        self._myHasMessageRecursionWarningThreshold=False

        self._myHasLogMessageCreation=False

        self._myHasMaxLoggerShutdownTime=False

        self._myHasLogConfiguration=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasMaxMessageRecursionDepth:
            x = "+"
        leafStr = str(self.maxMessageRecursionDepth)
        items.append(x + "MaxMessageRecursionDepth="+leafStr)

        x=""
        if self._myHasLogMessageProcessing:
            x = "+"
        leafStr = str(self.logMessageProcessing)
        items.append(x + "LogMessageProcessing="+leafStr)

        x=""
        if self._myHasLogAction:
            x = "+"
        leafStr = str(self.logAction)
        items.append(x + "LogAction="+leafStr)

        x=""
        if self._myHasMaxMessageBodySize:
            x = "+"
        leafStr = str(self.maxMessageBodySize)
        items.append(x + "MaxMessageBodySize="+leafStr)

        x=""
        if self._myHasMaxImplicitMessages:
            x = "+"
        leafStr = str(self.maxImplicitMessages)
        items.append(x + "MaxImplicitMessages="+leafStr)

        x=""
        if self._myHasMessageRecursionWarningThreshold:
            x = "+"
        leafStr = str(self.messageRecursionWarningThreshold)
        items.append(x + "MessageRecursionWarningThreshold="+leafStr)

        x=""
        if self._myHasLogMessageCreation:
            x = "+"
        leafStr = str(self.logMessageCreation)
        items.append(x + "LogMessageCreation="+leafStr)

        x=""
        if self._myHasMaxLoggerShutdownTime:
            x = "+"
        leafStr = str(self.maxLoggerShutdownTime)
        items.append(x + "MaxLoggerShutdownTime="+leafStr)

        x=""
        if self._myHasLogConfiguration:
            x = "+"
        leafStr = str(self.logConfiguration)
        items.append(x + "LogConfiguration="+leafStr)

        return "{InternalData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "InternalData", 
        "namespace": "internal", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.internal.internal_data_gen import InternalData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "logger_class", 
            "isCurrent": false
        }, 
        {
            "namespace": "instance", 
            "isCurrent": false
        }, 
        {
            "namespace": "internal", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxMessageRecursionDepth", 
            "yangName": "max-message-recursion-depth", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logMessageProcessing", 
            "yangName": "log-message-processing", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logAction", 
            "yangName": "log-action", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxMessageBodySize", 
            "yangName": "max-message-body-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxImplicitMessages", 
            "yangName": "max-implicit-messages", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "messageRecursionWarningThreshold", 
            "yangName": "message-recursion-warning-threshold", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logMessageCreation", 
            "yangName": "log-message-creation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxLoggerShutdownTime", 
            "yangName": "max-logger-shutdown-time", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logConfiguration", 
            "yangName": "log-configuration", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "debug", 
            "qwilt_tech_debug"
        ]
    }, 
    "createTime": "2013"
}
"""


