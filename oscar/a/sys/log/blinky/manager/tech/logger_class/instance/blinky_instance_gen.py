


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

from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.instance_data_gen import InstanceData


from a.sys.log.blinky.manager.tech.logger_class.instance.internal.blinky_internal_gen import BlinkyInternal

from a.sys.log.blinky.manager.tech.logger_class.instance.destination.blinky_destination_list_gen import BlinkyDestinationList

from a.sys.log.blinky.manager.tech.logger_class.instance.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults

from a.sys.log.blinky.manager.tech.logger_class.instance.rule.blinky_rule_list_gen import BlinkyRuleList




class BlinkyInstance(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"
    #leaves
    
    ourXmlTagName="name"
    

    #descendants
    
    ourXmlTagInternal="internal"
    
    ourXmlTagDestinationList="destination"
    
    ourXmlTagSystemDefaults="system-defaults"
    
    ourXmlTagRuleList="rule"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    INTERNAL_CREATE_FUNCTOR = 'INTERNAL_CREATE_FUNCTOR'
    INTERNAL_DELETE_FUNCTOR = 'INTERNAL_DELETE_FUNCTOR'
    
    DESTINATIONLIST_CREATE_FUNCTOR = 'DESTINATIONLIST_CREATE_FUNCTOR'
    DESTINATIONLIST_DELETE_FUNCTOR = 'DESTINATIONLIST_DELETE_FUNCTOR'
    
    SYSTEMDEFAULTS_CREATE_FUNCTOR = 'SYSTEMDEFAULTS_CREATE_FUNCTOR'
    SYSTEMDEFAULTS_DELETE_FUNCTOR = 'SYSTEMDEFAULTS_DELETE_FUNCTOR'
    
    RULELIST_CREATE_FUNCTOR = 'RULELIST_CREATE_FUNCTOR'
    RULELIST_DELETE_FUNCTOR = 'RULELIST_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateInternalFunctor=None
        self.myDeleteInternalFunctor=None
        self.myInternal=None
        
        self.myCreateDestinationListFunctor=None
        self.myDeleteDestinationListFunctor=None
        self.myDestinationList=None
        
        self.myCreateSystemDefaultsFunctor=None
        self.myDeleteSystemDefaultsFunctor=None
        self.mySystemDefaults=None
        
        self.myCreateRuleListFunctor=None
        self.myDeleteRuleListFunctor=None
        self.myRuleList=None
        
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

        logger('s-create-blinkyinstance').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyInstance._validationPointId, BlinkyInstance._actionPointId)

        confd_key=KeyPath()
        
        
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
        
        newNode=BlinkyInstance(logger)
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

    
    def setCreateInternalFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-internal-functor-active").errorFunc():
                logFunc("setCreateInternalFunctor() is illegal when blinky node is active")
        self.myCreateInternalFunctor = functor

    def setDeleteInternalFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-internal-functor-active").errorFunc():
                logFunc("setDeleteInternalFunctor() is illegal when blinky node is active")
        self.myDeleteInternalFunctor = functor
    
    def setCreateDestinationListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-destination-functor-active").errorFunc():
                logFunc("setCreateDestinationListFunctor() is illegal when blinky node is active")
        self.myCreateDestinationListFunctor = functor

    def setDeleteDestinationListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-destination-functor-active").errorFunc():
                logFunc("setDeleteDestinationListFunctor() is illegal when blinky node is active")
        self.myDeleteDestinationListFunctor = functor
    
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
    
    def setCreateRuleListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-rule-functor-active").errorFunc():
                logFunc("setCreateRuleListFunctor() is illegal when blinky node is active")
        self.myCreateRuleListFunctor = functor

    def setDeleteRuleListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-rule-functor-active").errorFunc():
                logFunc("setDeleteRuleListFunctor() is illegal when blinky node is active")
        self.myDeleteRuleListFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagName)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.name = newValue.asString()
                self.myCandidateData.setHasName()
                
            else:
                self.setNameDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagInternal)):
            return self.myInternal
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagDestinationList)):
            return self.myDestinationList
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagSystemDefaults)):
            return self.mySystemDefaults
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagRuleList)):
            return self.myRuleList
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyinstance').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.log.blinky.manager.tech.logger_class.instance.blinky_instance_gen import BlinkyInstance', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagInternal)):
                    keyPathRegistered = BlinkyInternal.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagDestinationList)):
                    keyPathRegistered = BlinkyDestinationList.isKeyPathRegistered(logger, keyPath, keyDepth+1)
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
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagRuleList)):
                    keyPathRegistered = BlinkyRuleList.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagName)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkyinstance-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.log.blinky.manager.tech.logger_class.instance.blinky_instance_gen import BlinkyInstance', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagInternal)):
            if (self.myInternal):
                for logFunc in self._log("prepare-my-blinky-node-internal-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myInternal = BlinkyInternal(self._log)
            self.myInternal.setParent(self)
            self.myInternal.setKeyPath(keyPath)
            self.myInternal.setDomain(self.myDomain)

            return self.myInternal
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDestinationList)):
            if (self.myDestinationList):
                for logFunc in self._log("prepare-my-blinky-node-destinationlist-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myDestinationList = BlinkyDestinationList(self._log)
            self.myDestinationList.setParent(self)
            self.myDestinationList.setKeyPath(keyPath)
            self.myDestinationList.setDomain(self.myDomain)

            return self.myDestinationList
        
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
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagRuleList)):
            if (self.myRuleList):
                for logFunc in self._log("prepare-my-blinky-node-rulelist-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myRuleList = BlinkyRuleList(self._log)
            self.myRuleList.setParent(self)
            self.myRuleList.setKeyPath(keyPath)
            self.myRuleList.setDomain(self.myDomain)

            return self.myRuleList
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagInternal)):
            self.myInternal = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDestinationList)):
            self.myDestinationList = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSystemDefaults)):
            self.mySystemDefaults = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagRuleList)):
            self.myRuleList = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagInternal)):
                if (self.myCreateInternalFunctor):
                    if (not self.myInternal):
                        for logFunc in self._log("handle-trx-element-create-internal-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): internal not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-internal-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.INTERNAL_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.INTERNAL_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateInternalFunctor(phase, self.myInternal)
                    except:
                        for logFunc in self._log("handle-trx-element-create-internal-functor-exception").exceptionFunc():
                            logFunc("Internal's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateInternalFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-internal-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): internal functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-internal-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): internal functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDestinationList)):
                if (self.myCreateDestinationListFunctor):
                    if (not self.myDestinationList):
                        for logFunc in self._log("handle-trx-element-create-destinationlist-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): destinationlist not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-destinationlist-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.DESTINATIONLIST_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.DESTINATIONLIST_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateDestinationListFunctor(phase, self.myDestinationList)
                    except:
                        for logFunc in self._log("handle-trx-element-create-destinationlist-functor-exception").exceptionFunc():
                            logFunc("DestinationList's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateDestinationListFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-destinationlist-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): destinationlist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-destinationlist-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): destinationlist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagRuleList)):
                if (self.myCreateRuleListFunctor):
                    if (not self.myRuleList):
                        for logFunc in self._log("handle-trx-element-create-rulelist-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): rulelist not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-rulelist-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.RULELIST_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.RULELIST_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateRuleListFunctor(phase, self.myRuleList)
                    except:
                        for logFunc in self._log("handle-trx-element-create-rulelist-functor-exception").exceptionFunc():
                            logFunc("RuleList's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateRuleListFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-rulelist-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): rulelist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-rulelist-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): rulelist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.myInternal):
            self.myInternal.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myDestinationList):
            self.myDestinationList.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.mySystemDefaults):
            self.mySystemDefaults.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myRuleList):
            self.myRuleList.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagInternal)):
                res = self.activateDeleteInternalFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-internal-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): internal functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-internal-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): internal functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDestinationList)):
                res = self.activateDeleteDestinationListFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-destinationlist-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): destinationlist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-destinationlist-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): destinationlist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagRuleList)):
                res = self.activateDeleteRuleListFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-rulelist-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): rulelist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-rulelist-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): rulelist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeInternal(self):
        self.myInternal = None

    def activateDeleteInternalFunctor(self, phase):
        for logFunc in self._log("activate-delete-internal-functor").debug3Func(): logFunc("activateDeleteInternalFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteInternalFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-internal-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.INTERNAL_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.INTERNAL_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteInternalFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-internal-functor-exception").exceptionFunc():
                        logFunc("Internal's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteInternalFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-internal-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteInternalFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-internal-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteInternalFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeDestinationList(self):
        self.myDestinationList = None

    def activateDeleteDestinationListFunctor(self, phase):
        for logFunc in self._log("activate-delete-destinationlist-functor").debug3Func(): logFunc("activateDeleteDestinationListFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteDestinationListFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-destinationlist-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.DESTINATIONLIST_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.DESTINATIONLIST_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteDestinationListFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-destinationlist-functor-exception").exceptionFunc():
                        logFunc("DestinationList's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteDestinationListFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-destinationlist-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteDestinationListFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-destinationlist-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteDestinationListFunctor(): functor failed, phase=%s", phase)
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
    
    def removeRuleList(self):
        self.myRuleList = None

    def activateDeleteRuleListFunctor(self, phase):
        for logFunc in self._log("activate-delete-rulelist-functor").debug3Func(): logFunc("activateDeleteRuleListFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteRuleListFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-rulelist-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.RULELIST_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.RULELIST_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteRuleListFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-rulelist-functor-exception").exceptionFunc():
                        logFunc("RuleList's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteRuleListFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-rulelist-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteRuleListFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-rulelist-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteRuleListFunctor(): functor failed, phase=%s", phase)
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
        self.myCandidateData = InstanceData()
        
        res = self.setNameDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-name-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setNameDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setNameDefaultValue (self, setHas):
        for logFunc in self._log("set-name-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.name = ""
            
        if setHas:
            self.myCandidateData.setHasName()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = InstanceData()
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
        self.myRunningData = InstanceData()
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyinstance-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyinstance-failed").errorFunc():
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
                
                if (self.myInternal):
                    res = self.myInternal.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-internal-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-internal-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myDestinationList):
                    res = self.myDestinationList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-destinationlist-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-destinationlist-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-systemdefaults-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myRuleList):
                    res = self.myRuleList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-rulelist-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-rulelist-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.myInternal):
                    res = self.activateDeleteInternalFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-internal-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteInternalFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myInternal):
                    res = self.myInternal.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-internal-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myInternal.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myDestinationList):
                    res = self.activateDeleteDestinationListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-destinationlist-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteDestinationListFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myDestinationList):
                    res = self.myDestinationList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-destinationlist-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myDestinationList.handleInternalDestroy() failed, res=%s, phase=%s",
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
                
                if (self.myRuleList):
                    res = self.activateDeleteRuleListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-rulelist-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteRuleListFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myRuleList):
                    res = self.myRuleList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-rulelist-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myRuleList.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myInternal):
                    res = self.myInternal.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-internal-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myInternal.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeInternal()
                
                if (self.myDestinationList):
                    res = self.myDestinationList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-destinationlist-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myDestinationList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeDestinationList()
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeSystemDefaults()
                
                if (self.myRuleList):
                    res = self.myRuleList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-rulelist-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myRuleList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeRuleList()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myInternal):
                    res = self.myInternal.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-internal-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myInternal.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteInternalFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-internal-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteInternalFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteInternalFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myDestinationList):
                    res = self.myDestinationList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-destinationlist-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myDestinationList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteDestinationListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-destinationlist-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteDestinationListFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteDestinationListFunctor failed in commit phase (private/public)")
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
                
                if (self.myRuleList):
                    res = self.myRuleList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-rulelist-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myRuleList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteRuleListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-rulelist-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteRuleListFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteRuleListFunctor failed in commit phase (private/public)")
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
                
                if (self.myInternal):
                    res = self.myInternal.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-internal-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myInternal.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myDestinationList):
                    res = self.myDestinationList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-destinationlist-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myDestinationList.handleInternalDestroy() failed, res=%s, phase=%s",
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
                
                if (self.myRuleList):
                    res = self.myRuleList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-rulelist-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myRuleList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myInternal):
                    res = self.myInternal.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-internal-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myInternal.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myInternal):
                    res = self.activateDeleteInternalFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-internal-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteInternalFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myDestinationList):
                    res = self.myDestinationList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-destinationlist-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myDestinationList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myDestinationList):
                    res = self.activateDeleteDestinationListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-destinationlist-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteDestinationListFunctor() failed, res=%s, phase=%s",
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
                
                if (self.myRuleList):
                    res = self.myRuleList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-rulelist-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myRuleList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myRuleList):
                    res = self.activateDeleteRuleListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-rulelist-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteRuleListFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.instance_data_gen import InstanceData", 
        "moduleYangNamespacePrefix": "qt-debug", 
        "validationPoint": null, 
        "yangName": "instance", 
        "namespace": "instance", 
        "logGroupName": "blinky-instance", 
        "className": "BlinkyInstance", 
        "logModuleName": "a-sys-log-blinky-manager-tech-logger-class-instance-blinky-instance-gen", 
        "importStatement": "from a.sys.log.blinky.manager.tech.logger_class.instance.blinky_instance_gen import BlinkyInstance", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
        "dataClassName": "InstanceData", 
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
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyInternal", 
            "memberName": "Internal", 
            "yangName": "internal", 
            "importStatement": "from a.sys.log.blinky.manager.tech.logger_class.instance.internal.blinky_internal_gen import BlinkyInternal"
        }, 
        {
            "className": "BlinkyDestinationList", 
            "memberName": "DestinationList", 
            "yangName": "destination", 
            "importStatement": "from a.sys.log.blinky.manager.tech.logger_class.instance.destination.blinky_destination_list_gen import BlinkyDestinationList"
        }, 
        {
            "className": "BlinkySystemDefaults", 
            "memberName": "SystemDefaults", 
            "yangName": "system-defaults", 
            "importStatement": "from a.sys.log.blinky.manager.tech.logger_class.instance.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults"
        }, 
        {
            "className": "BlinkyRuleList", 
            "memberName": "RuleList", 
            "yangName": "rule", 
            "importStatement": "from a.sys.log.blinky.manager.tech.logger_class.instance.rule.blinky_rule_list_gen import BlinkyRuleList"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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

