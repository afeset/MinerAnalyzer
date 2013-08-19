


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from internal_maapi_base_gen import InternalMaapiBase

from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.internal.burst_limits.burst_limits_maapi_gen import BlinkyBurstLimitsMaapi

from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogSeverity


class BlinkyInternalMaapi(InternalMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-internal")
        self.domain = None

        
        self.burstLimitsObj = None
        

        
        self.maxMessageRecursionDepthRequested = False
        self.maxMessageRecursionDepth = None
        self.maxMessageRecursionDepthSet = False
        
        self.logMessageProcessingRequested = False
        self.logMessageProcessing = None
        self.logMessageProcessingSet = False
        
        self.logActionRequested = False
        self.logAction = None
        self.logActionSet = False
        
        self.maxMessageBodySizeRequested = False
        self.maxMessageBodySize = None
        self.maxMessageBodySizeSet = False
        
        self.maxImplicitMessagesRequested = False
        self.maxImplicitMessages = None
        self.maxImplicitMessagesSet = False
        
        self.messageRecursionWarningThresholdRequested = False
        self.messageRecursionWarningThreshold = None
        self.messageRecursionWarningThresholdSet = False
        
        self.logMessageCreationRequested = False
        self.logMessageCreation = None
        self.logMessageCreationSet = False
        
        self.maxLoggerShutdownTimeRequested = False
        self.maxLoggerShutdownTime = None
        self.maxLoggerShutdownTimeSet = False
        
        self.logConfigurationRequested = False
        self.logConfiguration = None
        self.logConfigurationSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxMessageRecursionDepth(True)
        
        self.requestLogMessageProcessing(True)
        
        self.requestLogAction(True)
        
        self.requestMaxMessageBodySize(True)
        
        self.requestMaxImplicitMessages(True)
        
        self.requestMessageRecursionWarningThreshold(True)
        
        self.requestLogMessageCreation(True)
        
        self.requestMaxLoggerShutdownTime(True)
        
        self.requestLogConfiguration(True)
        
        
        
        if not self.burstLimitsObj:
            self.burstLimitsObj = self.newBurstLimits()
            self.burstLimitsObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxMessageRecursionDepth(True)
        
        self.requestLogMessageProcessing(True)
        
        self.requestLogAction(True)
        
        self.requestMaxMessageBodySize(True)
        
        self.requestMaxImplicitMessages(True)
        
        self.requestMessageRecursionWarningThreshold(True)
        
        self.requestLogMessageCreation(True)
        
        self.requestMaxLoggerShutdownTime(True)
        
        self.requestLogConfiguration(True)
        
        
        
        if not self.burstLimitsObj:
            self.burstLimitsObj = self.newBurstLimits()
            self.burstLimitsObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxMessageRecursionDepth(False)
        
        self.requestLogMessageProcessing(False)
        
        self.requestLogAction(False)
        
        self.requestMaxMessageBodySize(False)
        
        self.requestMaxImplicitMessages(False)
        
        self.requestMessageRecursionWarningThreshold(False)
        
        self.requestLogMessageCreation(False)
        
        self.requestMaxLoggerShutdownTime(False)
        
        self.requestLogConfiguration(False)
        
        
        
        if not self.burstLimitsObj:
            self.burstLimitsObj = self.newBurstLimits()
            self.burstLimitsObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxMessageRecursionDepth(False)
        
        self.requestLogMessageProcessing(False)
        
        self.requestLogAction(False)
        
        self.requestMaxMessageBodySize(False)
        
        self.requestMaxImplicitMessages(False)
        
        self.requestMessageRecursionWarningThreshold(False)
        
        self.requestLogMessageCreation(False)
        
        self.requestMaxLoggerShutdownTime(False)
        
        self.requestLogConfiguration(False)
        
        
        
        if not self.burstLimitsObj:
            self.burstLimitsObj = self.newBurstLimits()
            self.burstLimitsObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setMaxMessageRecursionDepth(None)
        self.maxMessageRecursionDepthSet = False
        
        self.setLogMessageProcessing(None)
        self.logMessageProcessingSet = False
        
        self.setLogAction(None)
        self.logActionSet = False
        
        self.setMaxMessageBodySize(None)
        self.maxMessageBodySizeSet = False
        
        self.setMaxImplicitMessages(None)
        self.maxImplicitMessagesSet = False
        
        self.setMessageRecursionWarningThreshold(None)
        self.messageRecursionWarningThresholdSet = False
        
        self.setLogMessageCreation(None)
        self.logMessageCreationSet = False
        
        self.setMaxLoggerShutdownTime(None)
        self.maxLoggerShutdownTimeSet = False
        
        self.setLogConfiguration(None)
        self.logConfigurationSet = False
        
        
        if self.burstLimitsObj:
            self.burstLimitsObj.clearAllSet()
        

    def write (self
              , loggerClass
              , instance
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(loggerClass, instance, trxContext)

    def read (self
              , loggerClass
              , instance
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, 
                                  True,
                                  trxContext)

    def newBurstLimits (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-burstlimits').debug3Func(): logFunc('called.')
        burstLimits = BlinkyBurstLimitsMaapi(self._log)
        burstLimits.init(self.domain)
        return burstLimits

    def setBurstLimitsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-burstlimits').debug3Func(): logFunc('called. obj=%s', obj)
        self.burstLimitsObj = obj

    def getBurstLimitsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-burstlimits').debug3Func(): logFunc('called. self.burstLimitsObj=%s', self.burstLimitsObj)
        return self.burstLimitsObj

    def hasBurstLimits (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-burstlimits').debug3Func(): logFunc('called. self.burstLimitsObj=%s', self.burstLimitsObj)
        if self.burstLimitsObj:
            return True
        return False



    def requestMaxMessageRecursionDepth (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxmessagerecursiondepth').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxMessageRecursionDepthRequested = requested
        self.maxMessageRecursionDepthSet = False

    def isMaxMessageRecursionDepthRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxmessagerecursiondepth-requested').debug3Func(): logFunc('called. requested=%s', self.maxMessageRecursionDepthRequested)
        return self.maxMessageRecursionDepthRequested

    def getMaxMessageRecursionDepth (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxmessagerecursiondepth').debug3Func(): logFunc('called. self.maxMessageRecursionDepthSet=%s, self.maxMessageRecursionDepth=%s', self.maxMessageRecursionDepthSet, self.maxMessageRecursionDepth)
        if self.maxMessageRecursionDepthSet:
            return self.maxMessageRecursionDepth
        return None

    def hasMaxMessageRecursionDepth (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxmessagerecursiondepth').debug3Func(): logFunc('called. self.maxMessageRecursionDepthSet=%s, self.maxMessageRecursionDepth=%s', self.maxMessageRecursionDepthSet, self.maxMessageRecursionDepth)
        if self.maxMessageRecursionDepthSet:
            return True
        return False

    def setMaxMessageRecursionDepth (self, maxMessageRecursionDepth):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxmessagerecursiondepth').debug3Func(): logFunc('called. maxMessageRecursionDepth=%s, old=%s', maxMessageRecursionDepth, self.maxMessageRecursionDepth)
        self.maxMessageRecursionDepthSet = True
        self.maxMessageRecursionDepth = maxMessageRecursionDepth

    def requestLogMessageProcessing (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-logmessageprocessing').debug3Func(): logFunc('called. requested=%s', requested)
        self.logMessageProcessingRequested = requested
        self.logMessageProcessingSet = False

    def isLogMessageProcessingRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-logmessageprocessing-requested').debug3Func(): logFunc('called. requested=%s', self.logMessageProcessingRequested)
        return self.logMessageProcessingRequested

    def getLogMessageProcessing (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-logmessageprocessing').debug3Func(): logFunc('called. self.logMessageProcessingSet=%s, self.logMessageProcessing=%s', self.logMessageProcessingSet, self.logMessageProcessing)
        if self.logMessageProcessingSet:
            return self.logMessageProcessing
        return None

    def hasLogMessageProcessing (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-logmessageprocessing').debug3Func(): logFunc('called. self.logMessageProcessingSet=%s, self.logMessageProcessing=%s', self.logMessageProcessingSet, self.logMessageProcessing)
        if self.logMessageProcessingSet:
            return True
        return False

    def setLogMessageProcessing (self, logMessageProcessing):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-logmessageprocessing').debug3Func(): logFunc('called. logMessageProcessing=%s, old=%s', logMessageProcessing, self.logMessageProcessing)
        self.logMessageProcessingSet = True
        self.logMessageProcessing = logMessageProcessing

    def requestLogAction (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-logaction').debug3Func(): logFunc('called. requested=%s', requested)
        self.logActionRequested = requested
        self.logActionSet = False

    def isLogActionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-logaction-requested').debug3Func(): logFunc('called. requested=%s', self.logActionRequested)
        return self.logActionRequested

    def getLogAction (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-logaction').debug3Func(): logFunc('called. self.logActionSet=%s, self.logAction=%s', self.logActionSet, self.logAction)
        if self.logActionSet:
            return self.logAction
        return None

    def hasLogAction (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-logaction').debug3Func(): logFunc('called. self.logActionSet=%s, self.logAction=%s', self.logActionSet, self.logAction)
        if self.logActionSet:
            return True
        return False

    def setLogAction (self, logAction):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-logaction').debug3Func(): logFunc('called. logAction=%s, old=%s', logAction, self.logAction)
        self.logActionSet = True
        self.logAction = logAction

    def requestMaxMessageBodySize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxmessagebodysize').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxMessageBodySizeRequested = requested
        self.maxMessageBodySizeSet = False

    def isMaxMessageBodySizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxmessagebodysize-requested').debug3Func(): logFunc('called. requested=%s', self.maxMessageBodySizeRequested)
        return self.maxMessageBodySizeRequested

    def getMaxMessageBodySize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxmessagebodysize').debug3Func(): logFunc('called. self.maxMessageBodySizeSet=%s, self.maxMessageBodySize=%s', self.maxMessageBodySizeSet, self.maxMessageBodySize)
        if self.maxMessageBodySizeSet:
            return self.maxMessageBodySize
        return None

    def hasMaxMessageBodySize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxmessagebodysize').debug3Func(): logFunc('called. self.maxMessageBodySizeSet=%s, self.maxMessageBodySize=%s', self.maxMessageBodySizeSet, self.maxMessageBodySize)
        if self.maxMessageBodySizeSet:
            return True
        return False

    def setMaxMessageBodySize (self, maxMessageBodySize):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxmessagebodysize').debug3Func(): logFunc('called. maxMessageBodySize=%s, old=%s', maxMessageBodySize, self.maxMessageBodySize)
        self.maxMessageBodySizeSet = True
        self.maxMessageBodySize = maxMessageBodySize

    def requestMaxImplicitMessages (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maximplicitmessages').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxImplicitMessagesRequested = requested
        self.maxImplicitMessagesSet = False

    def isMaxImplicitMessagesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maximplicitmessages-requested').debug3Func(): logFunc('called. requested=%s', self.maxImplicitMessagesRequested)
        return self.maxImplicitMessagesRequested

    def getMaxImplicitMessages (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maximplicitmessages').debug3Func(): logFunc('called. self.maxImplicitMessagesSet=%s, self.maxImplicitMessages=%s', self.maxImplicitMessagesSet, self.maxImplicitMessages)
        if self.maxImplicitMessagesSet:
            return self.maxImplicitMessages
        return None

    def hasMaxImplicitMessages (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maximplicitmessages').debug3Func(): logFunc('called. self.maxImplicitMessagesSet=%s, self.maxImplicitMessages=%s', self.maxImplicitMessagesSet, self.maxImplicitMessages)
        if self.maxImplicitMessagesSet:
            return True
        return False

    def setMaxImplicitMessages (self, maxImplicitMessages):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maximplicitmessages').debug3Func(): logFunc('called. maxImplicitMessages=%s, old=%s', maxImplicitMessages, self.maxImplicitMessages)
        self.maxImplicitMessagesSet = True
        self.maxImplicitMessages = maxImplicitMessages

    def requestMessageRecursionWarningThreshold (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-messagerecursionwarningthreshold').debug3Func(): logFunc('called. requested=%s', requested)
        self.messageRecursionWarningThresholdRequested = requested
        self.messageRecursionWarningThresholdSet = False

    def isMessageRecursionWarningThresholdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-messagerecursionwarningthreshold-requested').debug3Func(): logFunc('called. requested=%s', self.messageRecursionWarningThresholdRequested)
        return self.messageRecursionWarningThresholdRequested

    def getMessageRecursionWarningThreshold (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-messagerecursionwarningthreshold').debug3Func(): logFunc('called. self.messageRecursionWarningThresholdSet=%s, self.messageRecursionWarningThreshold=%s', self.messageRecursionWarningThresholdSet, self.messageRecursionWarningThreshold)
        if self.messageRecursionWarningThresholdSet:
            return self.messageRecursionWarningThreshold
        return None

    def hasMessageRecursionWarningThreshold (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-messagerecursionwarningthreshold').debug3Func(): logFunc('called. self.messageRecursionWarningThresholdSet=%s, self.messageRecursionWarningThreshold=%s', self.messageRecursionWarningThresholdSet, self.messageRecursionWarningThreshold)
        if self.messageRecursionWarningThresholdSet:
            return True
        return False

    def setMessageRecursionWarningThreshold (self, messageRecursionWarningThreshold):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-messagerecursionwarningthreshold').debug3Func(): logFunc('called. messageRecursionWarningThreshold=%s, old=%s', messageRecursionWarningThreshold, self.messageRecursionWarningThreshold)
        self.messageRecursionWarningThresholdSet = True
        self.messageRecursionWarningThreshold = messageRecursionWarningThreshold

    def requestLogMessageCreation (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-logmessagecreation').debug3Func(): logFunc('called. requested=%s', requested)
        self.logMessageCreationRequested = requested
        self.logMessageCreationSet = False

    def isLogMessageCreationRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-logmessagecreation-requested').debug3Func(): logFunc('called. requested=%s', self.logMessageCreationRequested)
        return self.logMessageCreationRequested

    def getLogMessageCreation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-logmessagecreation').debug3Func(): logFunc('called. self.logMessageCreationSet=%s, self.logMessageCreation=%s', self.logMessageCreationSet, self.logMessageCreation)
        if self.logMessageCreationSet:
            return self.logMessageCreation
        return None

    def hasLogMessageCreation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-logmessagecreation').debug3Func(): logFunc('called. self.logMessageCreationSet=%s, self.logMessageCreation=%s', self.logMessageCreationSet, self.logMessageCreation)
        if self.logMessageCreationSet:
            return True
        return False

    def setLogMessageCreation (self, logMessageCreation):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-logmessagecreation').debug3Func(): logFunc('called. logMessageCreation=%s, old=%s', logMessageCreation, self.logMessageCreation)
        self.logMessageCreationSet = True
        self.logMessageCreation = logMessageCreation

    def requestMaxLoggerShutdownTime (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxloggershutdowntime').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxLoggerShutdownTimeRequested = requested
        self.maxLoggerShutdownTimeSet = False

    def isMaxLoggerShutdownTimeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxloggershutdowntime-requested').debug3Func(): logFunc('called. requested=%s', self.maxLoggerShutdownTimeRequested)
        return self.maxLoggerShutdownTimeRequested

    def getMaxLoggerShutdownTime (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxloggershutdowntime').debug3Func(): logFunc('called. self.maxLoggerShutdownTimeSet=%s, self.maxLoggerShutdownTime=%s', self.maxLoggerShutdownTimeSet, self.maxLoggerShutdownTime)
        if self.maxLoggerShutdownTimeSet:
            return self.maxLoggerShutdownTime
        return None

    def hasMaxLoggerShutdownTime (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxloggershutdowntime').debug3Func(): logFunc('called. self.maxLoggerShutdownTimeSet=%s, self.maxLoggerShutdownTime=%s', self.maxLoggerShutdownTimeSet, self.maxLoggerShutdownTime)
        if self.maxLoggerShutdownTimeSet:
            return True
        return False

    def setMaxLoggerShutdownTime (self, maxLoggerShutdownTime):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxloggershutdowntime').debug3Func(): logFunc('called. maxLoggerShutdownTime=%s, old=%s', maxLoggerShutdownTime, self.maxLoggerShutdownTime)
        self.maxLoggerShutdownTimeSet = True
        self.maxLoggerShutdownTime = maxLoggerShutdownTime

    def requestLogConfiguration (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-logconfiguration').debug3Func(): logFunc('called. requested=%s', requested)
        self.logConfigurationRequested = requested
        self.logConfigurationSet = False

    def isLogConfigurationRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-logconfiguration-requested').debug3Func(): logFunc('called. requested=%s', self.logConfigurationRequested)
        return self.logConfigurationRequested

    def getLogConfiguration (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-logconfiguration').debug3Func(): logFunc('called. self.logConfigurationSet=%s, self.logConfiguration=%s', self.logConfigurationSet, self.logConfiguration)
        if self.logConfigurationSet:
            return self.logConfiguration
        return None

    def hasLogConfiguration (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-logconfiguration').debug3Func(): logFunc('called. self.logConfigurationSet=%s, self.logConfiguration=%s', self.logConfigurationSet, self.logConfiguration)
        if self.logConfigurationSet:
            return True
        return False

    def setLogConfiguration (self, logConfiguration):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-logconfiguration').debug3Func(): logFunc('called. logConfiguration=%s, old=%s', logConfiguration, self.logConfiguration)
        self.logConfigurationSet = True
        self.logConfiguration = logConfiguration


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.burstLimitsObj:
            self.burstLimitsObj._clearAllReadData()
        

        
        self.maxMessageRecursionDepth = 0
        self.maxMessageRecursionDepthSet = False
        
        self.logMessageProcessing = 0
        self.logMessageProcessingSet = False
        
        self.logAction = 0
        self.logActionSet = False
        
        self.maxMessageBodySize = 0
        self.maxMessageBodySizeSet = False
        
        self.maxImplicitMessages = 0
        self.maxImplicitMessagesSet = False
        
        self.messageRecursionWarningThreshold = 0
        self.messageRecursionWarningThresholdSet = False
        
        self.logMessageCreation = 0
        self.logMessageCreationSet = False
        
        self.maxLoggerShutdownTime = 0
        self.maxLoggerShutdownTimeSet = False
        
        self.logConfiguration = 0
        self.logConfigurationSet = False
        

    def _getSelfKeyPath (self, loggerClass
                         , instance
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("internal", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(instance);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(loggerClass);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        loggerClass, 
                        instance, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(loggerClass, 
                                         instance, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       loggerClass, 
                       instance, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               loggerClass, 
                               instance, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.burstLimitsObj:
            res = self.burstLimitsObj._collectItemsToDelete(loggerClass, 
                                                                          instance, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-burst-limits-failed').errorFunc(): logFunc('burstLimitsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasMaxMessageRecursionDepth():
            valMaxMessageRecursionDepth = Value()
            if self.maxMessageRecursionDepth is not None:
                valMaxMessageRecursionDepth.setInt64(self.maxMessageRecursionDepth)
            else:
                valMaxMessageRecursionDepth.setEmpty()
            tagValueList.push(("max-message-recursion-depth", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxMessageRecursionDepth)
        
        if self.hasLogMessageProcessing():
            valLogMessageProcessing = Value()
            if self.logMessageProcessing is not None:
                valLogMessageProcessing.setEnum(self.logMessageProcessing.getValue())
            else:
                valLogMessageProcessing.setEmpty()
            tagValueList.push(("log-message-processing", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLogMessageProcessing)
        
        if self.hasLogAction():
            valLogAction = Value()
            if self.logAction is not None:
                valLogAction.setEnum(self.logAction.getValue())
            else:
                valLogAction.setEmpty()
            tagValueList.push(("log-action", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLogAction)
        
        if self.hasMaxMessageBodySize():
            valMaxMessageBodySize = Value()
            if self.maxMessageBodySize is not None:
                valMaxMessageBodySize.setInt64(self.maxMessageBodySize)
            else:
                valMaxMessageBodySize.setEmpty()
            tagValueList.push(("max-message-body-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxMessageBodySize)
        
        if self.hasMaxImplicitMessages():
            valMaxImplicitMessages = Value()
            if self.maxImplicitMessages is not None:
                valMaxImplicitMessages.setInt64(self.maxImplicitMessages)
            else:
                valMaxImplicitMessages.setEmpty()
            tagValueList.push(("max-implicit-messages", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxImplicitMessages)
        
        if self.hasMessageRecursionWarningThreshold():
            valMessageRecursionWarningThreshold = Value()
            if self.messageRecursionWarningThreshold is not None:
                valMessageRecursionWarningThreshold.setInt64(self.messageRecursionWarningThreshold)
            else:
                valMessageRecursionWarningThreshold.setEmpty()
            tagValueList.push(("message-recursion-warning-threshold", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMessageRecursionWarningThreshold)
        
        if self.hasLogMessageCreation():
            valLogMessageCreation = Value()
            if self.logMessageCreation is not None:
                valLogMessageCreation.setEnum(self.logMessageCreation.getValue())
            else:
                valLogMessageCreation.setEmpty()
            tagValueList.push(("log-message-creation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLogMessageCreation)
        
        if self.hasMaxLoggerShutdownTime():
            valMaxLoggerShutdownTime = Value()
            if self.maxLoggerShutdownTime is not None:
                valMaxLoggerShutdownTime.setInt64(self.maxLoggerShutdownTime)
            else:
                valMaxLoggerShutdownTime.setEmpty()
            tagValueList.push(("max-logger-shutdown-time", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxLoggerShutdownTime)
        
        if self.hasLogConfiguration():
            valLogConfiguration = Value()
            if self.logConfiguration is not None:
                valLogConfiguration.setEnum(self.logConfiguration.getValue())
            else:
                valLogConfiguration.setEmpty()
            tagValueList.push(("log-configuration", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLogConfiguration)
        

        
        if self.burstLimitsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("burst-limits" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.burstLimitsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-burst-limits-failed').errorFunc(): logFunc('burstLimitsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isMaxMessageRecursionDepthRequested():
            valMaxMessageRecursionDepth = Value()
            valMaxMessageRecursionDepth.setEmpty()
            tagValueList.push(("max-message-recursion-depth", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxMessageRecursionDepth)
        
        if self.isLogMessageProcessingRequested():
            valLogMessageProcessing = Value()
            valLogMessageProcessing.setEmpty()
            tagValueList.push(("log-message-processing", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLogMessageProcessing)
        
        if self.isLogActionRequested():
            valLogAction = Value()
            valLogAction.setEmpty()
            tagValueList.push(("log-action", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLogAction)
        
        if self.isMaxMessageBodySizeRequested():
            valMaxMessageBodySize = Value()
            valMaxMessageBodySize.setEmpty()
            tagValueList.push(("max-message-body-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxMessageBodySize)
        
        if self.isMaxImplicitMessagesRequested():
            valMaxImplicitMessages = Value()
            valMaxImplicitMessages.setEmpty()
            tagValueList.push(("max-implicit-messages", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxImplicitMessages)
        
        if self.isMessageRecursionWarningThresholdRequested():
            valMessageRecursionWarningThreshold = Value()
            valMessageRecursionWarningThreshold.setEmpty()
            tagValueList.push(("message-recursion-warning-threshold", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMessageRecursionWarningThreshold)
        
        if self.isLogMessageCreationRequested():
            valLogMessageCreation = Value()
            valLogMessageCreation.setEmpty()
            tagValueList.push(("log-message-creation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLogMessageCreation)
        
        if self.isMaxLoggerShutdownTimeRequested():
            valMaxLoggerShutdownTime = Value()
            valMaxLoggerShutdownTime.setEmpty()
            tagValueList.push(("max-logger-shutdown-time", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valMaxLoggerShutdownTime)
        
        if self.isLogConfigurationRequested():
            valLogConfiguration = Value()
            valLogConfiguration.setEmpty()
            tagValueList.push(("log-configuration", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLogConfiguration)
        

        
        if self.burstLimitsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("burst-limits" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.burstLimitsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-burst-limits-failed').errorFunc(): logFunc('burstLimitsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isMaxMessageRecursionDepthRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-message-recursion-depth") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxmessagerecursiondepth').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxMessageRecursionDepth", "max-message-recursion-depth", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-message-recursion-depth-bad-value').infoFunc(): logFunc('maxMessageRecursionDepth not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxMessageRecursionDepth(tempVar)
            for logFunc in self._log('read-tag-values-max-message-recursion-depth').debug3Func(): logFunc('read maxMessageRecursionDepth. maxMessageRecursionDepth=%s, tempValue=%s', self.maxMessageRecursionDepth, tempValue.getType())
        
        if self.isLogMessageProcessingRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "log-message-processing") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-logmessageprocessing').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "logMessageProcessing", "log-message-processing", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-log-message-processing-bad-value').infoFunc(): logFunc('logMessageProcessing not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLogMessageProcessing(tempVar)
            for logFunc in self._log('read-tag-values-log-message-processing').debug3Func(): logFunc('read logMessageProcessing. logMessageProcessing=%s, tempValue=%s', self.logMessageProcessing, tempValue.getType())
        
        if self.isLogActionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "log-action") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-logaction').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "logAction", "log-action", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-log-action-bad-value').infoFunc(): logFunc('logAction not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLogAction(tempVar)
            for logFunc in self._log('read-tag-values-log-action').debug3Func(): logFunc('read logAction. logAction=%s, tempValue=%s', self.logAction, tempValue.getType())
        
        if self.isMaxMessageBodySizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-message-body-size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxmessagebodysize').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxMessageBodySize", "max-message-body-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-message-body-size-bad-value').infoFunc(): logFunc('maxMessageBodySize not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxMessageBodySize(tempVar)
            for logFunc in self._log('read-tag-values-max-message-body-size').debug3Func(): logFunc('read maxMessageBodySize. maxMessageBodySize=%s, tempValue=%s', self.maxMessageBodySize, tempValue.getType())
        
        if self.isMaxImplicitMessagesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-implicit-messages") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maximplicitmessages').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxImplicitMessages", "max-implicit-messages", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-implicit-messages-bad-value').infoFunc(): logFunc('maxImplicitMessages not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxImplicitMessages(tempVar)
            for logFunc in self._log('read-tag-values-max-implicit-messages').debug3Func(): logFunc('read maxImplicitMessages. maxImplicitMessages=%s, tempValue=%s', self.maxImplicitMessages, tempValue.getType())
        
        if self.isMessageRecursionWarningThresholdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "message-recursion-warning-threshold") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-messagerecursionwarningthreshold').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "messageRecursionWarningThreshold", "message-recursion-warning-threshold", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-message-recursion-warning-threshold-bad-value').infoFunc(): logFunc('messageRecursionWarningThreshold not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMessageRecursionWarningThreshold(tempVar)
            for logFunc in self._log('read-tag-values-message-recursion-warning-threshold').debug3Func(): logFunc('read messageRecursionWarningThreshold. messageRecursionWarningThreshold=%s, tempValue=%s', self.messageRecursionWarningThreshold, tempValue.getType())
        
        if self.isLogMessageCreationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "log-message-creation") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-logmessagecreation').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "logMessageCreation", "log-message-creation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-log-message-creation-bad-value').infoFunc(): logFunc('logMessageCreation not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLogMessageCreation(tempVar)
            for logFunc in self._log('read-tag-values-log-message-creation').debug3Func(): logFunc('read logMessageCreation. logMessageCreation=%s, tempValue=%s', self.logMessageCreation, tempValue.getType())
        
        if self.isMaxLoggerShutdownTimeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-logger-shutdown-time") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxloggershutdowntime').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxLoggerShutdownTime", "max-logger-shutdown-time", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-logger-shutdown-time-bad-value').infoFunc(): logFunc('maxLoggerShutdownTime not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxLoggerShutdownTime(tempVar)
            for logFunc in self._log('read-tag-values-max-logger-shutdown-time').debug3Func(): logFunc('read maxLoggerShutdownTime. maxLoggerShutdownTime=%s, tempValue=%s', self.maxLoggerShutdownTime, tempValue.getType())
        
        if self.isLogConfigurationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "log-configuration") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-logconfiguration').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "logConfiguration", "log-configuration", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-log-configuration-bad-value').infoFunc(): logFunc('logConfiguration not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLogConfiguration(tempVar)
            for logFunc in self._log('read-tag-values-log-configuration').debug3Func(): logFunc('read logConfiguration. logConfiguration=%s, tempValue=%s', self.logConfiguration, tempValue.getType())
        

        
        if self.burstLimitsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "burst-limits") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "burst-limits", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.burstLimitsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-burst-limits-failed').errorFunc(): logFunc('burstLimitsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "burst-limits") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "burst-limits", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



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


