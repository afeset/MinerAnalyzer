


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

from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.system_defaults.housekeeper.housekeeper_data_gen import HousekeeperData


from a.sys.log.housekeeper.blinky.tech.log.system_defaults.housekeeper.thresholds.blinky_thresholds_gen import BlinkyThresholds

from a.sys.log.housekeeper.blinky.tech.log.system_defaults.housekeeper.log_archiving.blinky_log_archiving_gen import BlinkyLogArchiving




class BlinkyHousekeeper(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"
    #leaves
    
    ourXmlTagEnabled="enabled"
    
    ourXmlTagPollInterval="poll-interval"
    

    #descendants
    
    ourXmlTagThresholds="thresholds"
    
    ourXmlTagLogArchiving="log-archiving"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    THRESHOLDS_CREATE_FUNCTOR = 'THRESHOLDS_CREATE_FUNCTOR'
    THRESHOLDS_DELETE_FUNCTOR = 'THRESHOLDS_DELETE_FUNCTOR'
    
    LOGARCHIVING_CREATE_FUNCTOR = 'LOGARCHIVING_CREATE_FUNCTOR'
    LOGARCHIVING_DELETE_FUNCTOR = 'LOGARCHIVING_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateThresholdsFunctor=None
        self.myDeleteThresholdsFunctor=None
        self.myThresholds=None
        
        self.myCreateLogArchivingFunctor=None
        self.myDeleteLogArchivingFunctor=None
        self.myLogArchiving=None
        
        self.myValueSetFunctor=None
        self.myCandidateData=None
        self.myRunningData=None
        self.isInDestroy = False
        
        self.validateRegistrationDone = False
        self.actionRegistrationDone=False
        
        

    @classmethod
    def s_create (cls, logger, 
                  
                  
                  
                  
                  
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkyhousekeeper').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyHousekeeper._validationPointId, BlinkyHousekeeper._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("housekeeper", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("log", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyHousekeeper(logger)
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

    
    def setCreateThresholdsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-thresholds-functor-active").errorFunc():
                logFunc("setCreateThresholdsFunctor() is illegal when blinky node is active")
        self.myCreateThresholdsFunctor = functor

    def setDeleteThresholdsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-thresholds-functor-active").errorFunc():
                logFunc("setDeleteThresholdsFunctor() is illegal when blinky node is active")
        self.myDeleteThresholdsFunctor = functor
    
    def setCreateLogArchivingFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-log-archiving-functor-active").errorFunc():
                logFunc("setCreateLogArchivingFunctor() is illegal when blinky node is active")
        self.myCreateLogArchivingFunctor = functor

    def setDeleteLogArchivingFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-log-archiving-functor-active").errorFunc():
                logFunc("setDeleteLogArchivingFunctor() is illegal when blinky node is active")
        self.myDeleteLogArchivingFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagEnabled)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.enabled = newValue.asBool()
                self.myCandidateData.setHasEnabled()
                
            else:
                self.setEnabledDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPollInterval)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.pollInterval = newValue.asInt64()
                self.myCandidateData.setHasPollInterval()
                
            else:
                self.setPollIntervalDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagThresholds)):
            return self.myThresholds
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagLogArchiving)):
            return self.myLogArchiving
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyhousekeeper').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.log.housekeeper.blinky.tech.log.system_defaults.housekeeper.blinky_housekeeper_gen import BlinkyHousekeeper', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagThresholds)):
                    keyPathRegistered = BlinkyThresholds.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagLogArchiving)):
                    keyPathRegistered = BlinkyLogArchiving.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagEnabled)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagPollInterval)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkyhousekeeper-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.log.housekeeper.blinky.tech.log.system_defaults.housekeeper.blinky_housekeeper_gen import BlinkyHousekeeper', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagThresholds)):
            if (self.myThresholds):
                for logFunc in self._log("prepare-my-blinky-node-thresholds-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myThresholds = BlinkyThresholds(self._log)
            self.myThresholds.setParent(self)
            self.myThresholds.setKeyPath(keyPath)
            self.myThresholds.setDomain(self.myDomain)

            return self.myThresholds
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLogArchiving)):
            if (self.myLogArchiving):
                for logFunc in self._log("prepare-my-blinky-node-logarchiving-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myLogArchiving = BlinkyLogArchiving(self._log)
            self.myLogArchiving.setParent(self)
            self.myLogArchiving.setKeyPath(keyPath)
            self.myLogArchiving.setDomain(self.myDomain)

            return self.myLogArchiving
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagThresholds)):
            self.myThresholds = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLogArchiving)):
            self.myLogArchiving = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagThresholds)):
                if (self.myCreateThresholdsFunctor):
                    if (not self.myThresholds):
                        for logFunc in self._log("handle-trx-element-create-thresholds-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): thresholds not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-thresholds-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.THRESHOLDS_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.THRESHOLDS_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateThresholdsFunctor(phase, self.myThresholds)
                    except:
                        for logFunc in self._log("handle-trx-element-create-thresholds-functor-exception").exceptionFunc():
                            logFunc("Thresholds's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateThresholdsFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-thresholds-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): thresholds functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-thresholds-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): thresholds functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLogArchiving)):
                if (self.myCreateLogArchivingFunctor):
                    if (not self.myLogArchiving):
                        for logFunc in self._log("handle-trx-element-create-logarchiving-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): logarchiving not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-logarchiving-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.LOGARCHIVING_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.LOGARCHIVING_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateLogArchivingFunctor(phase, self.myLogArchiving)
                    except:
                        for logFunc in self._log("handle-trx-element-create-logarchiving-functor-exception").exceptionFunc():
                            logFunc("LogArchiving's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateLogArchivingFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-logarchiving-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): logarchiving functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-logarchiving-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): logarchiving functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.myThresholds):
            self.myThresholds.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myLogArchiving):
            self.myLogArchiving.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagThresholds)):
                res = self.activateDeleteThresholdsFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-thresholds-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): thresholds functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-thresholds-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): thresholds functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLogArchiving)):
                res = self.activateDeleteLogArchivingFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-logarchiving-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): logarchiving functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-logarchiving-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): logarchiving functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeThresholds(self):
        self.myThresholds = None

    def activateDeleteThresholdsFunctor(self, phase):
        for logFunc in self._log("activate-delete-thresholds-functor").debug3Func(): logFunc("activateDeleteThresholdsFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteThresholdsFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-thresholds-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.THRESHOLDS_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.THRESHOLDS_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteThresholdsFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-thresholds-functor-exception").exceptionFunc():
                        logFunc("Thresholds's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteThresholdsFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-thresholds-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteThresholdsFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-thresholds-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteThresholdsFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeLogArchiving(self):
        self.myLogArchiving = None

    def activateDeleteLogArchivingFunctor(self, phase):
        for logFunc in self._log("activate-delete-logarchiving-functor").debug3Func(): logFunc("activateDeleteLogArchivingFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteLogArchivingFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-logarchiving-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.LOGARCHIVING_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.LOGARCHIVING_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteLogArchivingFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-logarchiving-functor-exception").exceptionFunc():
                        logFunc("LogArchiving's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteLogArchivingFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-logarchiving-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteLogArchivingFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-logarchiving-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteLogArchivingFunctor(): functor failed, phase=%s", phase)
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
        self.myCandidateData = HousekeeperData()
        
        res = self.setEnabledDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-enabled-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setEnabledDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setPollIntervalDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-pollinterval-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setPollIntervalDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setEnabledDefaultValue (self, setHas):
        for logFunc in self._log("set-enabled-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.enabled = False
            
        if setHas:
            self.myCandidateData.setHasEnabled()

        return ReturnCodes.kOk

    def setPollIntervalDefaultValue (self, setHas):
        for logFunc in self._log("set-pollinterval-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.pollInterval = 0
            
        if setHas:
            self.myCandidateData.setHasPollInterval()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = HousekeeperData()
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
        self.myRunningData = HousekeeperData()
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyhousekeeper-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyhousekeeper-failed").errorFunc():
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
                
                if (self.myThresholds):
                    res = self.myThresholds.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-thresholds-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-thresholds-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myLogArchiving):
                    res = self.myLogArchiving.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-logarchiving-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-logarchiving-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.myThresholds):
                    res = self.activateDeleteThresholdsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-thresholds-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteThresholdsFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myThresholds):
                    res = self.myThresholds.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-thresholds-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myThresholds.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myLogArchiving):
                    res = self.activateDeleteLogArchivingFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-logarchiving-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteLogArchivingFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myLogArchiving):
                    res = self.myLogArchiving.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-logarchiving-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myLogArchiving.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myThresholds):
                    res = self.myThresholds.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-thresholds-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myThresholds.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeThresholds()
                
                if (self.myLogArchiving):
                    res = self.myLogArchiving.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-logarchiving-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myLogArchiving.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeLogArchiving()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myThresholds):
                    res = self.myThresholds.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-thresholds-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myThresholds.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteThresholdsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-thresholds-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteThresholdsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteThresholdsFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myLogArchiving):
                    res = self.myLogArchiving.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-logarchiving-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myLogArchiving.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteLogArchivingFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-logarchiving-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteLogArchivingFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteLogArchivingFunctor failed in commit phase (private/public)")
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
                
                if (self.myThresholds):
                    res = self.myThresholds.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-thresholds-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myThresholds.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myLogArchiving):
                    res = self.myLogArchiving.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-logarchiving-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myLogArchiving.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myThresholds):
                    res = self.myThresholds.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-thresholds-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myThresholds.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myThresholds):
                    res = self.activateDeleteThresholdsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-thresholds-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteThresholdsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myLogArchiving):
                    res = self.myLogArchiving.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-logarchiving-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myLogArchiving.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myLogArchiving):
                    res = self.activateDeleteLogArchivingFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-logarchiving-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteLogArchivingFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.system_defaults.housekeeper.housekeeper_data_gen import HousekeeperData", 
        "moduleYangNamespacePrefix": "qt-log", 
        "validationPoint": null, 
        "yangName": "housekeeper", 
        "namespace": "housekeeper", 
        "logGroupName": "blinky-housekeeper", 
        "className": "BlinkyHousekeeper", 
        "logModuleName": "a-sys-log-housekeeper-blinky-tech-log-system-defaults-housekeeper-blinky-housekeeper-gen", 
        "importStatement": "from a.sys.log.housekeeper.blinky.tech.log.system_defaults.housekeeper.blinky_housekeeper_gen import BlinkyHousekeeper", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
        "dataClassName": "HousekeeperData", 
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
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log", 
            "namespace": "log", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "housekeeper", 
            "namespace": "housekeeper", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "housekeeper"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyThresholds", 
            "memberName": "Thresholds", 
            "yangName": "thresholds", 
            "importStatement": "from a.sys.log.housekeeper.blinky.tech.log.system_defaults.housekeeper.thresholds.blinky_thresholds_gen import BlinkyThresholds"
        }, 
        {
            "className": "BlinkyLogArchiving", 
            "memberName": "LogArchiving", 
            "yangName": "log-archiving", 
            "importStatement": "from a.sys.log.housekeeper.blinky.tech.log.system_defaults.housekeeper.log_archiving.blinky_log_archiving_gen import BlinkyLogArchiving"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "env": [
        "a", 
        "sys", 
        "log", 
        "housekeeper", 
        "blinky", 
        ""
    ], 
    "createTime": "2013"
}
"""

