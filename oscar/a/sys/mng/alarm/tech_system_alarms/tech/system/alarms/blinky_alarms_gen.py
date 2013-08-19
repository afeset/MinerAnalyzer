


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

from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.alarms_data_gen import AlarmsData


from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.thresholds.blinky_thresholds_gen import BlinkyThresholds

from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults

from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.simulate.blinky_simulate_list_gen import BlinkySimulateList




class BlinkyAlarms(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"
    #leaves
    
    ourXmlTagEnabled="enabled"
    
    ourXmlTagRaiseTestAlarm="raise-test-alarm"
    
    ourXmlTagPollInterval="poll-interval"
    

    #descendants
    
    ourXmlTagThresholds="thresholds"
    
    ourXmlTagSystemDefaults="system-defaults"
    
    ourXmlTagSimulateList="simulate"
    

    _validationPointId=None
    
    _actionPointId=None
    _actionPointId="tech-system-alarms-clear-counters-actionpoint"

    
    THRESHOLDS_CREATE_FUNCTOR = 'THRESHOLDS_CREATE_FUNCTOR'
    THRESHOLDS_DELETE_FUNCTOR = 'THRESHOLDS_DELETE_FUNCTOR'
    
    SYSTEMDEFAULTS_CREATE_FUNCTOR = 'SYSTEMDEFAULTS_CREATE_FUNCTOR'
    SYSTEMDEFAULTS_DELETE_FUNCTOR = 'SYSTEMDEFAULTS_DELETE_FUNCTOR'
    
    SIMULATELIST_CREATE_FUNCTOR = 'SIMULATELIST_CREATE_FUNCTOR'
    SIMULATELIST_DELETE_FUNCTOR = 'SIMULATELIST_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateThresholdsFunctor=None
        self.myDeleteThresholdsFunctor=None
        self.myThresholds=None
        
        self.myCreateSystemDefaultsFunctor=None
        self.myDeleteSystemDefaultsFunctor=None
        self.mySystemDefaults=None
        
        self.myCreateSimulateListFunctor=None
        self.myDeleteSimulateListFunctor=None
        self.mySimulateList=None
        
        self.myValueSetFunctor=None
        self.myCandidateData=None
        self.myRunningData=None
        self.isInDestroy = False
        
        self.validateRegistrationDone = False
        self.actionRegistrationDone=False
        
        
        self.doActionFunctor = None
        

    @classmethod
    def s_create (cls, logger, 
                  
                  
                  
                  
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkyalarms').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyAlarms._validationPointId, BlinkyAlarms._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyAlarms(logger)
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
    
    def setCreateSystemDefaultsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-system-defaults-functor-active").errorFunc():
                logFunc("setCreateSystemDefaultsFunctor() is illegal when blinky node is active")
        self.myCreateSystemDefaultsFunctor = functor

    def setDeleteSystemDefaultsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-system-defaults-functor-active").errorFunc():
                logFunc("setDeleteSystemDefaultsFunctor() is illegal when blinky node is active")
        self.myDeleteSystemDefaultsFunctor = functor
    
    def setCreateSimulateListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-simulate-functor-active").errorFunc():
                logFunc("setCreateSimulateListFunctor() is illegal when blinky node is active")
        self.myCreateSimulateListFunctor = functor

    def setDeleteSimulateListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-simulate-functor-active").errorFunc():
                logFunc("setDeleteSimulateListFunctor() is illegal when blinky node is active")
        self.myDeleteSimulateListFunctor = functor
    

    

    
    def setDoActionFunctor(self, functor):
        if self.myIsActive:
            for logFunc in self._log("set-do-action-functor-active").errorFunc():
                logFunc("illegal when blinky node is active")
        self.doActionFunctor = functor
    

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
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagRaiseTestAlarm)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.raiseTestAlarm = newValue.asBool()
                self.myCandidateData.setHasRaiseTestAlarm()
                
            else:
                self.setRaiseTestAlarmDefaultValue(True)
            
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
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagSystemDefaults)):
            return self.mySystemDefaults
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagSimulateList)):
            return self.mySimulateList
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyalarms').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.blinky_alarms_gen import BlinkyAlarms', keyPath, keyDepth)
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
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagSystemDefaults)):
                    keyPathRegistered = BlinkySystemDefaults.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagSimulateList)):
                    keyPathRegistered = BlinkySimulateList.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagEnabled)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagRaiseTestAlarm)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagPollInterval)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkyalarms-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.blinky_alarms_gen import BlinkyAlarms', keyPathRegistered, keyPath, keyDepth)
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
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSystemDefaults)):
            if (self.mySystemDefaults):
                for logFunc in self._log("prepare-my-blinky-node-systemdefaults-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.mySystemDefaults = BlinkySystemDefaults(self._log)
            self.mySystemDefaults.setParent(self)
            self.mySystemDefaults.setKeyPath(keyPath)
            self.mySystemDefaults.setDomain(self.myDomain)

            return self.mySystemDefaults
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSimulateList)):
            if (self.mySimulateList):
                for logFunc in self._log("prepare-my-blinky-node-simulatelist-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.mySimulateList = BlinkySimulateList(self._log)
            self.mySimulateList.setParent(self)
            self.mySimulateList.setKeyPath(keyPath)
            self.mySimulateList.setDomain(self.myDomain)

            return self.mySimulateList
        
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
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSystemDefaults)):
            self.mySystemDefaults = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSimulateList)):
            self.mySimulateList = None
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
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSystemDefaults)):
                if (self.myCreateSystemDefaultsFunctor):
                    if (not self.mySystemDefaults):
                        for logFunc in self._log("handle-trx-element-create-systemdefaults-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): systemdefaults not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-systemdefaults-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.SYSTEMDEFAULTS_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.SYSTEMDEFAULTS_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateSystemDefaultsFunctor(phase, self.mySystemDefaults)
                    except:
                        for logFunc in self._log("handle-trx-element-create-systemdefaults-functor-exception").exceptionFunc():
                            logFunc("SystemDefaults's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateSystemDefaultsFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-systemdefaults-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): systemdefaults functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-systemdefaults-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): systemdefaults functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSimulateList)):
                if (self.myCreateSimulateListFunctor):
                    if (not self.mySimulateList):
                        for logFunc in self._log("handle-trx-element-create-simulatelist-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): simulatelist not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-simulatelist-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.SIMULATELIST_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.SIMULATELIST_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateSimulateListFunctor(phase, self.mySimulateList)
                    except:
                        for logFunc in self._log("handle-trx-element-create-simulatelist-functor-exception").exceptionFunc():
                            logFunc("SimulateList's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateSimulateListFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-simulatelist-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): simulatelist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-simulatelist-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): simulatelist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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
        
        if (self.mySystemDefaults):
            self.mySystemDefaults.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.mySimulateList):
            self.mySimulateList.notifyDescendantsPrepareBlinkyDelete()
        

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
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSystemDefaults)):
                res = self.activateDeleteSystemDefaultsFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-systemdefaults-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): systemdefaults functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-systemdefaults-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): systemdefaults functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSimulateList)):
                res = self.activateDeleteSimulateListFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-simulatelist-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): simulatelist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-simulatelist-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): simulatelist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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
    
    def removeSystemDefaults(self):
        self.mySystemDefaults = None

    def activateDeleteSystemDefaultsFunctor(self, phase):
        for logFunc in self._log("activate-delete-systemdefaults-functor").debug3Func(): logFunc("activateDeleteSystemDefaultsFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteSystemDefaultsFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-systemdefaults-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.SYSTEMDEFAULTS_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.SYSTEMDEFAULTS_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteSystemDefaultsFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-systemdefaults-functor-exception").exceptionFunc():
                        logFunc("SystemDefaults's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteSystemDefaultsFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-systemdefaults-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteSystemDefaultsFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-systemdefaults-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteSystemDefaultsFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeSimulateList(self):
        self.mySimulateList = None

    def activateDeleteSimulateListFunctor(self, phase):
        for logFunc in self._log("activate-delete-simulatelist-functor").debug3Func(): logFunc("activateDeleteSimulateListFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteSimulateListFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-simulatelist-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.SIMULATELIST_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.SIMULATELIST_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteSimulateListFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-simulatelist-functor-exception").exceptionFunc():
                        logFunc("SimulateList's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteSimulateListFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-simulatelist-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteSimulateListFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-simulatelist-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteSimulateListFunctor(): functor failed, phase=%s", phase)
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
        self.myCandidateData = AlarmsData()
        
        res = self.setEnabledDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-enabled-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setEnabledDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setRaiseTestAlarmDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-raisetestalarm-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setRaiseTestAlarmDefaultValue failed. res=%s",
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

    def setRaiseTestAlarmDefaultValue (self, setHas):
        for logFunc in self._log("set-raisetestalarm-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.raiseTestAlarm = False
            
        if setHas:
            self.myCandidateData.setHasRaiseTestAlarm()

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
            self.myCandidateData = AlarmsData()
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
        self.myRunningData = AlarmsData()
        self.myRunningData.copyFrom(self.myCandidateData)
        self.myCandidateData = None
        self.myState.setPhaseDone(phase)
        for logFunc in self._log("activate-candidate-done").debug3Func(): logFunc("activateCandidate(): done, candidate=%s, running=%s, isPhaseDone()=%s",
                                                    self.myCandidateData, self.myRunningData, self.myState.isPhaseDone(phase))

    

    
    def doAction (self, userInfo, actionPoint, actionName, keypath, params, nParams):
        for logFunc in self._log("do-action").debug3Func(): logFunc("called. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
        if self.myIsActive:
            if self.doActionFunctor:
                timeoutGuard = TimeoutGuard(self._log, '%s-do-action-functor-%s' % (keypath, actionPoint), 
                                            self.getFunctorTimeout(self.DO_ACTION_FUNCTOR), 
                                            self.getFunctorMildTimeout(self.DO_ACTION_FUNCTOR))
                try:
                    res = self.doActionFunctor(userInfo, actionPoint, actionName, params, nParams)
                except:
                    for logFunc in self._log("do-action-functor-exception").exceptionFunc():
                        logFunc("functor raised an exception. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.doActionFunctor.__name__)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("do-action-functor-failed").errorFunc(): logFunc("functor failed. res=%s, userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", res, userInfo, actionPoint, actionName, keypath, params, nParams)
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("do-action-functor-unset").debug3Func(): logFunc("no do-action functor set. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
            return ReturnCodes.kOk
        else:
            #TODO (naamas) - add error string
            for logFunc in self._log("d-action-inactive").errorFunc(): logFunc("Blinky node is inactive. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
            return ReturnCodes.kGeneralError
    

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
                
                if self.doActionFunctor:
                    res = self.myDomain.registerActionPoint(self._actionPointId, self)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("activate-specitic-register-action-point-failed").errorFunc():
                            logFunc("activateSpecific(): registerActionPoint(%s) failed",  self._actionPointId)
                        return None
                
        return ReturnCodes.kOk

    def handleTrxProgressNotificationSpecific (self, progress):
        for logFunc in self._log("handle-trx-progress-notification-specific").debug3Func(): logFunc("called. progress=%s, isInDestroy=%s", progress, self.isInDestroy)
        if progress.isCommitBlinkyBefore() or progress.isAbortBlinkyBefore():
            if self.isInDestroy:
                if self._validationPointId and self.validateRegistrationDone:
                    res = self.myDomain.unregisterValidationPoint(self._validationPointId, self)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyalarms-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyalarms-failed").errorFunc():
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
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-systemdefaults-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.mySimulateList):
                    res = self.mySimulateList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulatelist-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-simulatelist-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.mySystemDefaults):
                    res = self.activateDeleteSystemDefaultsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSystemDefaultsFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.mySimulateList):
                    res = self.activateDeleteSimulateListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulatelist-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSimulateListFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.mySimulateList):
                    res = self.mySimulateList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulatelist-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySimulateList.handleInternalDestroy() failed, res=%s, phase=%s",
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
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeSystemDefaults()
                
                if (self.mySimulateList):
                    res = self.mySimulateList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulatelist-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySimulateList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeSimulateList()
                
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
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteSystemDefaultsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSystemDefaultsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteSystemDefaultsFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.mySimulateList):
                    res = self.mySimulateList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulatelist-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySimulateList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteSimulateListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulatelist-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSimulateListFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteSimulateListFunctor failed in commit phase (private/public)")
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
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.mySimulateList):
                    res = self.mySimulateList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulatelist-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySimulateList.handleInternalDestroy() failed, res=%s, phase=%s",
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
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.mySystemDefaults):
                    res = self.activateDeleteSystemDefaultsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSystemDefaultsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.mySimulateList):
                    res = self.mySimulateList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulatelist-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySimulateList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.mySimulateList):
                    res = self.activateDeleteSimulateListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulatelist-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSimulateListFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.alarms_data_gen import AlarmsData", 
        "moduleYangNamespacePrefix": "qt-sys-alarms", 
        "validationPoint": null, 
        "yangName": "alarms", 
        "namespace": "alarms", 
        "logGroupName": "blinky-alarms", 
        "className": "BlinkyAlarms", 
        "logModuleName": "a-sys-mng-alarm-tech-system-alarms-tech-system-alarms-blinky-alarms-gen", 
        "importStatement": "from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.blinky_alarms_gen import BlinkyAlarms", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
        "dataClassName": "AlarmsData", 
        "actionPoint": "tech-system-alarms-clear-counters-actionpoint"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "alarms"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyThresholds", 
            "memberName": "Thresholds", 
            "yangName": "thresholds", 
            "importStatement": "from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.thresholds.blinky_thresholds_gen import BlinkyThresholds"
        }, 
        {
            "className": "BlinkySystemDefaults", 
            "memberName": "SystemDefaults", 
            "yangName": "system-defaults", 
            "importStatement": "from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults"
        }, 
        {
            "className": "BlinkySimulateList", 
            "memberName": "SimulateList", 
            "yangName": "simulate", 
            "importStatement": "from a.sys.mng.alarm.tech_system_alarms.tech.system.alarms.simulate.blinky_simulate_list_gen import BlinkySimulateList"
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "raiseTestAlarm", 
            "yangName": "raise-test-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "module": {}, 
    "env": [
        "a", 
        "sys", 
        "mng", 
        "alarm", 
        "tech_system_alarms"
    ], 
    "createTime": "2013"
}
"""

