


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

from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.system_defaults_data_gen import SystemDefaultsData


from a.sys.log.blinky.manager.tech.logger_class.instance.destination.system_defaults.output.blinky_output_gen import BlinkyOutput

from a.sys.log.blinky.manager.tech.logger_class.instance.destination.system_defaults.format.blinky_format_gen import BlinkyFormat


from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogSeverity
from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import DestinationType


class BlinkySystemDefaults(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
    #leaves
    
    ourXmlTagMinLevel="min-level"
    
    ourXmlTagDestinationType="type"
    
    ourXmlTagEnabled="enabled"
    

    #descendants
    
    ourXmlTagOutput="output"
    
    ourXmlTagFormat="format"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    OUTPUT_CREATE_FUNCTOR = 'OUTPUT_CREATE_FUNCTOR'
    OUTPUT_DELETE_FUNCTOR = 'OUTPUT_DELETE_FUNCTOR'
    
    FORMAT_CREATE_FUNCTOR = 'FORMAT_CREATE_FUNCTOR'
    FORMAT_DELETE_FUNCTOR = 'FORMAT_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateOutputFunctor=None
        self.myDeleteOutputFunctor=None
        self.myOutput=None
        
        self.myCreateFormatFunctor=None
        self.myDeleteFormatFunctor=None
        self.myFormat=None
        
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
                  destination, 
                  
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkysystemdefaults').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkySystemDefaults._validationPointId, BlinkySystemDefaults._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(destination);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("destination", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
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
        
        newNode=BlinkySystemDefaults(logger)
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

    
    def setCreateOutputFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-output-functor-active").errorFunc():
                logFunc("setCreateOutputFunctor() is illegal when blinky node is active")
        self.myCreateOutputFunctor = functor

    def setDeleteOutputFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-output-functor-active").errorFunc():
                logFunc("setDeleteOutputFunctor() is illegal when blinky node is active")
        self.myDeleteOutputFunctor = functor
    
    def setCreateFormatFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-format-functor-active").errorFunc():
                logFunc("setCreateFormatFunctor() is illegal when blinky node is active")
        self.myCreateFormatFunctor = functor

    def setDeleteFormatFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-format-functor-active").errorFunc():
                logFunc("setDeleteFormatFunctor() is illegal when blinky node is active")
        self.myDeleteFormatFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMinLevel)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not LogSeverity.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-minlevel-failed")\
                        .error("illegal enum value %s for minLevel", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.minLevel = LogSeverity.getByValue(newValue.asEnum())
                self.myCandidateData.setHasMinLevel()
                
            else:
                self.setMinLevelDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDestinationType)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not DestinationType.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-destinationtype-failed")\
                        .error("illegal enum value %s for destinationType", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.destinationType = DestinationType.getByValue(newValue.asEnum())
                self.myCandidateData.setHasDestinationType()
                
            else:
                self.setDestinationTypeDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagEnabled)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.enabled = newValue.asBool()
                self.myCandidateData.setHasEnabled()
                
            else:
                self.setEnabledDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagOutput)):
            return self.myOutput
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagFormat)):
            return self.myFormat
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkysystemdefaults').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.log.blinky.manager.tech.logger_class.instance.destination.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagOutput)):
                    keyPathRegistered = BlinkyOutput.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagFormat)):
                    keyPathRegistered = BlinkyFormat.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMinLevel)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagDestinationType)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagEnabled)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkysystemdefaults-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.log.blinky.manager.tech.logger_class.instance.destination.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOutput)):
            if (self.myOutput):
                for logFunc in self._log("prepare-my-blinky-node-output-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myOutput = BlinkyOutput(self._log)
            self.myOutput.setParent(self)
            self.myOutput.setKeyPath(keyPath)
            self.myOutput.setDomain(self.myDomain)

            return self.myOutput
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFormat)):
            if (self.myFormat):
                for logFunc in self._log("prepare-my-blinky-node-format-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myFormat = BlinkyFormat(self._log)
            self.myFormat.setParent(self)
            self.myFormat.setKeyPath(keyPath)
            self.myFormat.setDomain(self.myDomain)

            return self.myFormat
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOutput)):
            self.myOutput = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFormat)):
            self.myFormat = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOutput)):
                if (self.myCreateOutputFunctor):
                    if (not self.myOutput):
                        for logFunc in self._log("handle-trx-element-create-output-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): output not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-output-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.OUTPUT_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.OUTPUT_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateOutputFunctor(phase, self.myOutput)
                    except:
                        for logFunc in self._log("handle-trx-element-create-output-functor-exception").exceptionFunc():
                            logFunc("Output's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateOutputFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-output-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): output functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-output-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): output functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFormat)):
                if (self.myCreateFormatFunctor):
                    if (not self.myFormat):
                        for logFunc in self._log("handle-trx-element-create-format-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): format not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-format-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.FORMAT_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.FORMAT_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateFormatFunctor(phase, self.myFormat)
                    except:
                        for logFunc in self._log("handle-trx-element-create-format-functor-exception").exceptionFunc():
                            logFunc("Format's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateFormatFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-format-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): format functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-format-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): format functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.myOutput):
            self.myOutput.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myFormat):
            self.myFormat.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOutput)):
                res = self.activateDeleteOutputFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-output-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): output functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-output-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): output functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFormat)):
                res = self.activateDeleteFormatFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-format-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): format functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-format-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): format functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeOutput(self):
        self.myOutput = None

    def activateDeleteOutputFunctor(self, phase):
        for logFunc in self._log("activate-delete-output-functor").debug3Func(): logFunc("activateDeleteOutputFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteOutputFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-output-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.OUTPUT_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.OUTPUT_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteOutputFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-output-functor-exception").exceptionFunc():
                        logFunc("Output's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteOutputFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-output-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteOutputFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-output-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteOutputFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeFormat(self):
        self.myFormat = None

    def activateDeleteFormatFunctor(self, phase):
        for logFunc in self._log("activate-delete-format-functor").debug3Func(): logFunc("activateDeleteFormatFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteFormatFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-format-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.FORMAT_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.FORMAT_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteFormatFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-format-functor-exception").exceptionFunc():
                        logFunc("Format's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteFormatFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-format-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteFormatFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-format-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteFormatFunctor(): functor failed, phase=%s", phase)
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
        self.myCandidateData = SystemDefaultsData()
        
        res = self.setMinLevelDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-minlevel-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMinLevelDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setDestinationTypeDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-destinationtype-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setDestinationTypeDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setEnabledDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-enabled-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setEnabledDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setMinLevelDefaultValue (self, setHas):
        for logFunc in self._log("set-minlevel-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.minLevel = LogSeverity.kAny
            
        if setHas:
            self.myCandidateData.setHasMinLevel()

        return ReturnCodes.kOk

    def setDestinationTypeDefaultValue (self, setHas):
        for logFunc in self._log("set-destinationtype-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.destinationType = DestinationType.kText
            
        if setHas:
            self.myCandidateData.setHasDestinationType()

        return ReturnCodes.kOk

    def setEnabledDefaultValue (self, setHas):
        for logFunc in self._log("set-enabled-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.enabled = True
            
        if setHas:
            self.myCandidateData.setHasEnabled()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = SystemDefaultsData()
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
        self.myRunningData = SystemDefaultsData()
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkysystemdefaults-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkysystemdefaults-failed").errorFunc():
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
                
                if (self.myOutput):
                    res = self.myOutput.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-output-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-output-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myFormat):
                    res = self.myFormat.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-format-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-format-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.myOutput):
                    res = self.activateDeleteOutputFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-output-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteOutputFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myOutput):
                    res = self.myOutput.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-output-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myOutput.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myFormat):
                    res = self.activateDeleteFormatFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-format-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteFormatFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myFormat):
                    res = self.myFormat.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-format-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myFormat.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myOutput):
                    res = self.myOutput.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-output-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myOutput.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeOutput()
                
                if (self.myFormat):
                    res = self.myFormat.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-format-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myFormat.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeFormat()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myOutput):
                    res = self.myOutput.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-output-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myOutput.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteOutputFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-output-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteOutputFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteOutputFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myFormat):
                    res = self.myFormat.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-format-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myFormat.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteFormatFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-format-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteFormatFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteFormatFunctor failed in commit phase (private/public)")
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
                
                if (self.myOutput):
                    res = self.myOutput.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-output-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myOutput.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myFormat):
                    res = self.myFormat.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-format-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myFormat.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myOutput):
                    res = self.myOutput.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-output-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myOutput.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myOutput):
                    res = self.activateDeleteOutputFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-output-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteOutputFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myFormat):
                    res = self.myFormat.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-format-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myFormat.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myFormat):
                    res = self.activateDeleteFormatFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-format-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteFormatFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.destination.system_defaults.system_defaults_data_gen import SystemDefaultsData", 
        "moduleYangNamespacePrefix": "qt-debug", 
        "validationPoint": null, 
        "yangName": "system-defaults", 
        "namespace": "system_defaults", 
        "logGroupName": "blinky-system-defaults", 
        "className": "BlinkySystemDefaults", 
        "logModuleName": "a-sys-log-blinky-manager-tech-logger-class-instance-destination-system-defaults-blinky-system-defaults-gen", 
        "importStatement": "from a.sys.log.blinky.manager.tech.logger_class.instance.destination.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
        "dataClassName": "SystemDefaultsData", 
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyOutput", 
            "memberName": "Output", 
            "yangName": "output", 
            "importStatement": "from a.sys.log.blinky.manager.tech.logger_class.instance.destination.system_defaults.output.blinky_output_gen import BlinkyOutput"
        }, 
        {
            "className": "BlinkyFormat", 
            "memberName": "Format", 
            "yangName": "format", 
            "importStatement": "from a.sys.log.blinky.manager.tech.logger_class.instance.destination.system_defaults.format.blinky_format_gen import BlinkyFormat"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "minLevel", 
            "yangName": "min-level", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "destinationType", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "text", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
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

