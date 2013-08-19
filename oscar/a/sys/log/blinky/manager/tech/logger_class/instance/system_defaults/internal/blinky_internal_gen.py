


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyContainer
__pychecker__="no-classattr"

from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.timeout_guard import TimeoutGuard
import a.infra.process.captain
from a.sys.blinky.blinky_container import BlinkyContainer
from a.sys.blinky.trx_phase import TrxPhase
from a.sys.confd.pyconfdlib import pyconfdlib
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
import copy

from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.system_defaults.internal.internal_data_gen import InternalData


from a.sys.log.blinky.manager.tech.logger_class.instance.system_defaults.internal.burst_limits.blinky_burst_limits_gen import BlinkyBurstLimits


from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogSeverity


class BlinkyInternal(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
    #leaves
    
    ourXmlTagMaxMessageRecursionDepth="max-message-recursion-depth"
    
    ourXmlTagLogMessageProcessing="log-message-processing"
    
    ourXmlTagLogAction="log-action"
    
    ourXmlTagMaxMessageBodySize="max-message-body-size"
    
    ourXmlTagMaxImplicitMessages="max-implicit-messages"
    
    ourXmlTagMessageRecursionWarningThreshold="message-recursion-warning-threshold"
    
    ourXmlTagLogMessageCreation="log-message-creation"
    
    ourXmlTagMaxLoggerShutdownTime="max-logger-shutdown-time"
    
    ourXmlTagLogConfiguration="log-configuration"
    

    #descendants
    
    ourXmlTagBurstLimits="burst-limits"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    BURSTLIMITS_CREATE_FUNCTOR = 'BURSTLIMITS_CREATE_FUNCTOR'
    BURSTLIMITS_DELETE_FUNCTOR = 'BURSTLIMITS_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateBurstLimitsFunctor=None
        self.myDeleteBurstLimitsFunctor=None
        self.myBurstLimits=None
        
        self.myValueSetFunctor=None
        self.myCandidateData=None
        self.myRunningData=None
        self.isInDestroy = False
        
        self.validateRegistrationDone = False
        self.actionRegistrationDone=False
        
        

    @classmethod
    def s_create (cls, logger, 
                  
                  
                  loggerClass, 
                  instance, 
                  
                  
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkyinternal').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyInternal._validationPointId, BlinkyInternal._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("internal", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(instance);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(loggerClass);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyInternal(logger)
        logger("s-create-keypath").info("confd_key=%s", confd_key)
        newNode.setParent(None)
        newNode.setKeyPath(confd_key)
        newNode.setDomain(domain)
        res = newNode.internalInit()
        if (res != ReturnCodes.kOk):
            logger("s-create-internal-init-failed")\
                .error("internalInit() failed. confd_key=%s", confd_key)

        if newNode._validationPointId:
            res = domain.registerValidationPoint(newNode._validationPointId, newNode)
            if (res != ReturnCodes.kOk):
                logger("s-create-register-validation-node--failed")\
                    .error("registerValidationNode(%s) failed",  newNode._validationPointId)
                return None
        newNode.validateRegistrationDone = True
        if newNode._actionPointId:
            res = domain.registerActionPoint(newNode._actionPointId, newNode)
            if (res != ReturnCodes.kOk):
                logger("s-create-register-action-node--failed")\
                    .error("registerActionNode(%s) failed",  newNode._actionPointId)
                return None
        newNode.actionRegistrationDone = True

        return newNode

    
    def setCreateBurstLimitsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-burst-limits-functor-active").errorFunc():
                logFunc("setCreateBurstLimitsFunctor() is illegal when blinky node is active")
        self.myCreateBurstLimitsFunctor = functor

    def setDeleteBurstLimitsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-burst-limits-functor-active").errorFunc():
                logFunc("setDeleteBurstLimitsFunctor() is illegal when blinky node is active")
        self.myDeleteBurstLimitsFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMaxMessageRecursionDepth)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.maxMessageRecursionDepth = newValue.asInt64()
                self.myCandidateData.setHasMaxMessageRecursionDepth()
                
            else:
                self.setMaxMessageRecursionDepthDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLogMessageProcessing)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not LogSeverity.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-logmessageprocessing-failed")\
                        .error("illegal enum value %s for logMessageProcessing", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.logMessageProcessing = LogSeverity.getByValue(newValue.asEnum())
                self.myCandidateData.setHasLogMessageProcessing()
                
            else:
                self.setLogMessageProcessingDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLogAction)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not LogSeverity.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-logaction-failed")\
                        .error("illegal enum value %s for logAction", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.logAction = LogSeverity.getByValue(newValue.asEnum())
                self.myCandidateData.setHasLogAction()
                
            else:
                self.setLogActionDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMaxMessageBodySize)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.maxMessageBodySize = newValue.asInt64()
                self.myCandidateData.setHasMaxMessageBodySize()
                
            else:
                self.setMaxMessageBodySizeDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMaxImplicitMessages)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.maxImplicitMessages = newValue.asInt64()
                self.myCandidateData.setHasMaxImplicitMessages()
                
            else:
                self.setMaxImplicitMessagesDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMessageRecursionWarningThreshold)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.messageRecursionWarningThreshold = newValue.asInt64()
                self.myCandidateData.setHasMessageRecursionWarningThreshold()
                
            else:
                self.setMessageRecursionWarningThresholdDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLogMessageCreation)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not LogSeverity.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-logmessagecreation-failed")\
                        .error("illegal enum value %s for logMessageCreation", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.logMessageCreation = LogSeverity.getByValue(newValue.asEnum())
                self.myCandidateData.setHasLogMessageCreation()
                
            else:
                self.setLogMessageCreationDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMaxLoggerShutdownTime)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.maxLoggerShutdownTime = newValue.asInt64()
                self.myCandidateData.setHasMaxLoggerShutdownTime()
                
            else:
                self.setMaxLoggerShutdownTimeDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLogConfiguration)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not LogSeverity.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-logconfiguration-failed")\
                        .error("illegal enum value %s for logConfiguration", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.logConfiguration = LogSeverity.getByValue(newValue.asEnum())
                self.myCandidateData.setHasLogConfiguration()
                
            else:
                self.setLogConfigurationDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagBurstLimits)):
            return self.myBurstLimits
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyinternal').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.log.blinky.manager.tech.logger_class.instance.system_defaults.internal.blinky_internal_gen import BlinkyInternal', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagBurstLimits)):
                    keyPathRegistered = BlinkyBurstLimits.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMaxMessageRecursionDepth)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagLogMessageProcessing)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagLogAction)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMaxMessageBodySize)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMaxImplicitMessages)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMessageRecursionWarningThreshold)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagLogMessageCreation)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMaxLoggerShutdownTime)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagLogConfiguration)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkyinternal-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.log.blinky.manager.tech.logger_class.instance.system_defaults.internal.blinky_internal_gen import BlinkyInternal', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagBurstLimits)):
            if (self.myBurstLimits):
                for logFunc in self._log("prepare-my-blinky-node-burstlimits-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myBurstLimits = BlinkyBurstLimits(self._log)
            self.myBurstLimits.setParent(self)
            self.myBurstLimits.setKeyPath(keyPath)
            self.myBurstLimits.setDomain(self.myDomain)

            return self.myBurstLimits
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagBurstLimits)):
            self.myBurstLimits = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagBurstLimits)):
                if (self.myCreateBurstLimitsFunctor):
                    if (not self.myBurstLimits):
                        for logFunc in self._log("handle-trx-element-create-burstlimits-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): burstlimits not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-burstlimits-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.BURSTLIMITS_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.BURSTLIMITS_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateBurstLimitsFunctor(phase, self.myBurstLimits)
                    except:
                        for logFunc in self._log("handle-trx-element-create-burstlimits-functor-exception").exceptionFunc():
                            logFunc("BurstLimits's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateBurstLimitsFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-burstlimits-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): burstlimits functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-burstlimits-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): burstlimits functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            pass
        return ReturnCodes.kOk
    
    def handleTrxElementPrepareBlinkyDelete(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-prepare-blinky-delete-called").debug2Func():
            logFunc("called: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)

        self.notifyDescendantsPrepareBlinkyDelete()

        # if deleted item is a leaf - clear it in the data
        return self.handleTrxElementPrepareBlinkyValueSet(trxElement, keyDepth)

    def notifyDescendantsPrepareBlinkyDelete(self):
        for logFunc in self._log("notify-descendants-prepare-blinky-delete-called").debug2Func(): logFunc("called")

        self.myDomain.registerNodeToProgressNotification(self)

        
        if (self.myBurstLimits):
            self.myBurstLimits.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagBurstLimits)):
                res = self.activateDeleteBurstLimitsFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-burstlimits-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): burstlimits functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-burstlimits-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): burstlimits functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeBurstLimits(self):
        self.myBurstLimits = None

    def activateDeleteBurstLimitsFunctor(self, phase):
        for logFunc in self._log("activate-delete-burstlimits-functor").debug3Func(): logFunc("activateDeleteBurstLimitsFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteBurstLimitsFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-burstlimits-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.BURSTLIMITS_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.BURSTLIMITS_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteBurstLimitsFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-burstlimits-functor-exception").exceptionFunc():
                        logFunc("BurstLimits's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteBurstLimitsFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-burstlimits-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteBurstLimitsFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-burstlimits-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteBurstLimitsFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    

    

    def setValueSetFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-value-set-functor-not-active").errorFunc():
                logFunc("setValueSetFunctor(): is illegal when blinky container is active")
        self.myValueSetFunctor = functor
    
    def activateValueSetFunctor(self, phase, data):
        for logFunc in self._log("activate-value-set-functor").debug3Func():
            logFunc("activateValueSetFunctor(): called, myIsActive=%s, phase=%s, data=%s, candidate=%s, running=%s, functor=%s",
                   self.myIsActive, phase, data, self.myCandidateData, self.myRunningData, self.myValueSetFunctor)
        res = ReturnCodes.kOk
        if (self.myIsActive):
            if (self.myValueSetFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-value-set-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.VALUE_SET_FUNCTOR, phase),
                                            self.getFunctorMildTimeoutForPhase(self.VALUE_SET_FUNCTOR, phase))
                try:
                    res = self.myValueSetFunctor(phase, data)
                except:
                    for logFunc in self._log("activate-value-set-functor-functor-exception").exceptionFunc():
                        logFunc("functor raised an exception. phase=%s, data=%s", phase, data)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myValueSetFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-value-set-functor-failed-prepare").noticeFunc():
                            logFunc("activateValueSetFunctor(): functor failed, phase=%s, data=%s, res=%s",
                                   phase, data, res)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-value-set-functor-failed").errorFunc():
                            logFunc("activateValueSetFunctor(): functor failed, phase=%s, data=%s, res=%s",
                                  phase, data, res)
                    return ReturnCodes.kGeneralError
        return res
    
    def notifyWithCandidate(self, phase):
        for logFunc in self._log("notify-with-candidate").debug3Func(): logFunc("notifyWithCandidate(): called, candidate=%s, phase=%s",
                                                              self.myCandidateData, phase)
        return self.activateValueSetFunctor(phase, self.myCandidateData)
    
    def allocMyCandidate(self):
        for logFunc in self._log("alloc-my-candidate").debug3Func():
            logFunc("called")
        self.myCandidateData = InternalData()
        
        res = self.setMaxMessageRecursionDepthDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-maxmessagerecursiondepth-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMaxMessageRecursionDepthDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setLogMessageProcessingDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-logmessageprocessing-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setLogMessageProcessingDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setLogActionDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-logaction-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setLogActionDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setMaxMessageBodySizeDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-maxmessagebodysize-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMaxMessageBodySizeDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setMaxImplicitMessagesDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-maximplicitmessages-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMaxImplicitMessagesDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setMessageRecursionWarningThresholdDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-messagerecursionwarningthreshold-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMessageRecursionWarningThresholdDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setLogMessageCreationDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-logmessagecreation-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setLogMessageCreationDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setMaxLoggerShutdownTimeDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-maxloggershutdowntime-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMaxLoggerShutdownTimeDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setLogConfigurationDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-logconfiguration-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setLogConfigurationDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setMaxMessageRecursionDepthDefaultValue (self, setHas):
        for logFunc in self._log("set-maxmessagerecursiondepth-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.maxMessageRecursionDepth = 0
            
        if setHas:
            self.myCandidateData.setHasMaxMessageRecursionDepth()

        return ReturnCodes.kOk

    def setLogMessageProcessingDefaultValue (self, setHas):
        for logFunc in self._log("set-logmessageprocessing-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.logMessageProcessing = LogSeverity.kNone
            
        if setHas:
            self.myCandidateData.setHasLogMessageProcessing()

        return ReturnCodes.kOk

    def setLogActionDefaultValue (self, setHas):
        for logFunc in self._log("set-logaction-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.logAction = LogSeverity.kNone
            
        if setHas:
            self.myCandidateData.setHasLogAction()

        return ReturnCodes.kOk

    def setMaxMessageBodySizeDefaultValue (self, setHas):
        for logFunc in self._log("set-maxmessagebodysize-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.maxMessageBodySize = 0
            
        if setHas:
            self.myCandidateData.setHasMaxMessageBodySize()

        return ReturnCodes.kOk

    def setMaxImplicitMessagesDefaultValue (self, setHas):
        for logFunc in self._log("set-maximplicitmessages-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.maxImplicitMessages = 0
            
        if setHas:
            self.myCandidateData.setHasMaxImplicitMessages()

        return ReturnCodes.kOk

    def setMessageRecursionWarningThresholdDefaultValue (self, setHas):
        for logFunc in self._log("set-messagerecursionwarningthreshold-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.messageRecursionWarningThreshold = 0
            
        if setHas:
            self.myCandidateData.setHasMessageRecursionWarningThreshold()

        return ReturnCodes.kOk

    def setLogMessageCreationDefaultValue (self, setHas):
        for logFunc in self._log("set-logmessagecreation-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.logMessageCreation = LogSeverity.kNone
            
        if setHas:
            self.myCandidateData.setHasLogMessageCreation()

        return ReturnCodes.kOk

    def setMaxLoggerShutdownTimeDefaultValue (self, setHas):
        for logFunc in self._log("set-maxloggershutdowntime-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.maxLoggerShutdownTime = 0
            
        if setHas:
            self.myCandidateData.setHasMaxLoggerShutdownTime()

        return ReturnCodes.kOk

    def setLogConfigurationDefaultValue (self, setHas):
        for logFunc in self._log("set-logconfiguration-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.logConfiguration = LogSeverity.kNone
            
        if setHas:
            self.myCandidateData.setHasLogConfiguration()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = InternalData()
            self.myCandidateData.copyFrom(self.myRunningData)
            
        else:
            for logFunc in self._log("copy-running-to-candidate-no-running").debug3Func(): logFunc("copyRunningToCandidate(): myRunningData is None")
            res = self.allocMyCandidate()
            if res != ReturnCodes.kOk:
                for logFunc in self._log("copy-running-to-candidate-alloc-my-candidate-failed").errorFunc(): logFunc("copyRunningToCandidate(): myRunningData is None and allocMyCandidate() failed. aborting")
                a.infra.process.processFatal("copyRunningToCandidate(): myRunningData is None and allocMyCandidate() failed")
    
    def deleteMyCandidate(self):
        for logFunc in self._log("delete-my-candidate").debug3Func(): logFunc("deleteMyCandidate(): called, candidate=%s, running=%s",
                                                     self.myCandidateData, self.myRunningData)
        self.myCandidateData = None
    
    def activateCandidate(self):
        phase=TrxPhase(TrxPhase.kCommit, TrxPhase.kBlinky)
        for logFunc in self._log("activate-candidate").debug3Func(): logFunc("activateCandidate(): called, candidate=%s, running=%s, isPhaseDone()=%s",
                                               self.myCandidateData, self.myRunningData, self.myState.isPhaseDone(phase))
        if (self.myState.isPhaseDone(phase)):
            # running config already updated - skip
            return
        self.myRunningData = InternalData()
        self.myRunningData.copyFrom(self.myCandidateData)
        self.myCandidateData = None
        self.myState.setPhaseDone(phase)
        for logFunc in self._log("activate-candidate-done").debug3Func(): logFunc("activateCandidate(): done, candidate=%s, running=%s, isPhaseDone()=%s",
                                                    self.myCandidateData, self.myRunningData, self.myState.isPhaseDone(phase))

    

    

    def getRunningCfgData (self):
        if self.myRunningData:
            return copy.copy(self.myRunningData)
        elif self.myCandidateData:
            # running is not yet initialized. getting the candidate that will soon be running
            return copy.copy(self.myCandidateData)
        for logFunc in self._log("get-running-cfg-data").errorFunc(): logFunc("both running and candidate data are none")
        return None

    def getCandidateCfgData (self):
        if self.myCandidateData:
            # when there is no active transaction, there will be no candidate configuration - give the running instead
            if not self.myRunningData:
                for logFunc in self._log("get-candidate-cfg-data").errorFunc(): logFunc("no running and no candidate")
                return None
            return copy.copy(self.myRunningData)
        else:
            # running is not yet initialized. getting the candidate that will soon be running
            return copy.copy(self.myCandidateData)

    def activateSpecific(self):
        for logFunc in self._log("activate-specific").debug3Func(): logFunc("called")
        if self._actionPointId:
            if not self.actionRegistrationDone:
                
                pass
                
        return ReturnCodes.kOk

    def handleTrxProgressNotificationSpecific (self, progress):
        for logFunc in self._log("handle-trx-progress-notification-specific").debug3Func(): logFunc("called. progress=%s, isInDestroy=%s", progress, self.isInDestroy)
        if progress.isCommitBlinkyBefore() or progress.isAbortBlinkyBefore():
            if self.isInDestroy:
                if self._validationPointId and self.validateRegistrationDone:
                    res = self.myDomain.unregisterValidationPoint(self._validationPointId, self)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyinternal-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyinternal-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterActionPoint(%s) failed, progress=%s",  self._actionPointId, progress)
                        return ReturnCodes.kGeneralError
        return ReturnCodes.kOk


    def handleInternalDestroy(self, phase):
        __pychecker__ = 'maxreturns=100 maxlines=1000 maxbranches=100'
        for logFunc in self._log("internal-prepare-destroy-helper").debug3Func(): logFunc("handleInternalDestroy(): called, phase=%s", phase)
        res = ReturnCodes.kOk
        self.isInDestroy = True
        if (phase.getConfdPhase() == TrxPhase.kPrepare):
            self.myDomain.registerNodeToProgressNotification(self)
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myBurstLimits):
                    res = self.myBurstLimits.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-burstlimits-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-burstlimits-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-delete-destroy-self-functor-failed-prepare").noticeFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                               res, phase)
                    self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    return ReturnCodes.kGeneralError
                
                if (self.myBurstLimits):
                    res = self.activateDeleteBurstLimitsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-burstlimits-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteBurstLimitsFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myBurstLimits):
                    res = self.myBurstLimits.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-burstlimits-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myBurstLimits.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myBurstLimits):
                    res = self.myBurstLimits.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-burstlimits-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myBurstLimits.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeBurstLimits()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myBurstLimits):
                    res = self.myBurstLimits.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-burstlimits-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myBurstLimits.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteBurstLimitsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-burstlimits-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteBurstLimitsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteBurstLimitsFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-delete-destroy-self-functor-failed-commit").errorFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                              res, phase)
                    a.infra.process.processFatal("destroy self functor failed in commit")
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("handle-internal-destroy-delete-commit-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): commit-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kAbort):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myBurstLimits):
                    res = self.myBurstLimits.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-burstlimits-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myBurstLimits.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myBurstLimits):
                    res = self.myBurstLimits.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-burstlimits-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myBurstLimits.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myBurstLimits):
                    res = self.activateDeleteBurstLimitsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-burstlimits-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteBurstLimitsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-activate-destroy-self-functor-failed-abort").errorFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                              res, phase)
                    a.infra.process.processFatal("destroy self functor failed in abort")
                    return ReturnCodes.kOk
            else:
                for logFunc in self._log("handle-internal-destroy-delete-abort-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): abort-illegal-blinky, res=%s, phase=%s", res, phase)
                return ReturnCodes.kGeneralError
        else:
            for logFunc in self._log("handle-internal-destroy-delete-illegal-confd").noticeFunc():
                logFunc("handleInternalDestroy(): illegal-confd, res=%s, phase=%s", res, phase)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
"""
Extracted from the below data: 
{
    "node": {
        "dataImportStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.system_defaults.internal.internal_data_gen import InternalData", 
        "moduleYangNamespacePrefix": "qt-debug", 
        "validationPoint": null, 
        "yangName": "internal", 
        "namespace": "internal", 
        "logGroupName": "blinky-internal", 
        "className": "BlinkyInternal", 
        "logModuleName": "a-sys-log-blinky-manager-tech-logger-class-instance-system-defaults-internal-blinky-internal-gen", 
        "importStatement": "from a.sys.log.blinky.manager.tech.logger_class.instance.system_defaults.internal.blinky_internal_gen import BlinkyInternal", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
        "dataClassName": "InternalData", 
        "actionPoint": null
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
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "system-defaults"
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
            "className": "BlinkyBurstLimits", 
            "memberName": "BurstLimits", 
            "yangName": "burst-limits", 
            "importStatement": "from a.sys.log.blinky.manager.tech.logger_class.instance.system_defaults.internal.burst_limits.blinky_burst_limits_gen import BlinkyBurstLimits"
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
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logMessageProcessing", 
            "yangName": "log-message-processing", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logAction", 
            "yangName": "log-action", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxMessageBodySize", 
            "yangName": "max-message-body-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxImplicitMessages", 
            "yangName": "max-implicit-messages", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "messageRecursionWarningThreshold", 
            "yangName": "message-recursion-warning-threshold", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logMessageCreation", 
            "yangName": "log-message-creation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxLoggerShutdownTime", 
            "yangName": "max-logger-shutdown-time", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logConfiguration", 
            "yangName": "log-configuration", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "env": [
        "a", 
        "sys", 
        "log", 
        "blinky", 
        "manager"
    ], 
    "createTime": "2013"
}
"""

