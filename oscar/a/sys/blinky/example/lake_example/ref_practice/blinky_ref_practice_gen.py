


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

from a.sys.blinky.example.lake_example.ref_practice.ref_practice_data_gen import RefPracticeData


from a.sys.blinky.example.lake_example.ref_practice.some_list.blinky_some_list_list_gen import BlinkySomeListList




class BlinkyRefPractice(BlinkyContainer):
    ourNamespace="http://qwilt.com/model/lake-example"
    #leaves
    
    ourXmlTagSomeLeafRef="some-leaf-ref"
    

    #descendants
    
    ourXmlTagSomeListList="some-list"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    SOMELISTLIST_CREATE_FUNCTOR = 'SOMELISTLIST_CREATE_FUNCTOR'
    SOMELISTLIST_DELETE_FUNCTOR = 'SOMELISTLIST_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateSomeListListFunctor=None
        self.myDeleteSomeListListFunctor=None
        self.mySomeListList=None
        
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

        logger('s-create-blinkyrefpractice').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyRefPractice._validationPointId, BlinkyRefPractice._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ref-practice", "http://qwilt.com/model/lake-example", "lake-example"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyRefPractice(logger)
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

    
    def setCreateSomeListListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-some-list-functor-active").errorFunc():
                logFunc("setCreateSomeListListFunctor() is illegal when blinky node is active")
        self.myCreateSomeListListFunctor = functor

    def setDeleteSomeListListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-some-list-functor-active").errorFunc():
                logFunc("setDeleteSomeListListFunctor() is illegal when blinky node is active")
        self.myDeleteSomeListListFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSomeLeafRef)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.someLeafRef = newValue.asString()
                self.myCandidateData.setHasSomeLeafRef()
                
            else:
                self.setSomeLeafRefDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagSomeListList)):
            return self.mySomeListList
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyrefpractice').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.blinky.example.lake_example.ref_practice.blinky_ref_practice_gen import BlinkyRefPractice', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagSomeListList)):
                    keyPathRegistered = BlinkySomeListList.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagSomeLeafRef)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkyrefpractice-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.blinky.example.lake_example.ref_practice.blinky_ref_practice_gen import BlinkyRefPractice', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSomeListList)):
            if (self.mySomeListList):
                for logFunc in self._log("prepare-my-blinky-node-somelistlist-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.mySomeListList = BlinkySomeListList(self._log)
            self.mySomeListList.setParent(self)
            self.mySomeListList.setKeyPath(keyPath)
            self.mySomeListList.setDomain(self.myDomain)

            return self.mySomeListList
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSomeListList)):
            self.mySomeListList = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSomeListList)):
                if (self.myCreateSomeListListFunctor):
                    if (not self.mySomeListList):
                        for logFunc in self._log("handle-trx-element-create-somelistlist-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): somelistlist not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-somelistlist-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.SOMELISTLIST_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.SOMELISTLIST_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateSomeListListFunctor(phase, self.mySomeListList)
                    except:
                        for logFunc in self._log("handle-trx-element-create-somelistlist-functor-exception").exceptionFunc():
                            logFunc("SomeListList's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateSomeListListFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-somelistlist-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): somelistlist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-somelistlist-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): somelistlist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.mySomeListList):
            self.mySomeListList.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSomeListList)):
                res = self.activateDeleteSomeListListFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-somelistlist-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): somelistlist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-somelistlist-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): somelistlist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeSomeListList(self):
        self.mySomeListList = None

    def activateDeleteSomeListListFunctor(self, phase):
        for logFunc in self._log("activate-delete-somelistlist-functor").debug3Func(): logFunc("activateDeleteSomeListListFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteSomeListListFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-somelistlist-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.SOMELISTLIST_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.SOMELISTLIST_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteSomeListListFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-somelistlist-functor-exception").exceptionFunc():
                        logFunc("SomeListList's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteSomeListListFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-somelistlist-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteSomeListListFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-somelistlist-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteSomeListListFunctor(): functor failed, phase=%s", phase)
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
        self.myCandidateData = RefPracticeData()
        
        res = self.setSomeLeafRefDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-someleafref-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setSomeLeafRefDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setSomeLeafRefDefaultValue (self, setHas):
        for logFunc in self._log("set-someleafref-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.someLeafRef = ""
            
        if setHas:
            self.myCandidateData.setHasSomeLeafRef()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = RefPracticeData()
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
        self.myRunningData = RefPracticeData()
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyrefpractice-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyrefpractice-failed").errorFunc():
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
                
                if (self.mySomeListList):
                    res = self.mySomeListList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-somelistlist-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-somelistlist-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.mySomeListList):
                    res = self.activateDeleteSomeListListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-somelistlist-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSomeListListFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.mySomeListList):
                    res = self.mySomeListList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-somelistlist-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySomeListList.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.mySomeListList):
                    res = self.mySomeListList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-somelistlist-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySomeListList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeSomeListList()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.mySomeListList):
                    res = self.mySomeListList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-somelistlist-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySomeListList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteSomeListListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-somelistlist-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSomeListListFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteSomeListListFunctor failed in commit phase (private/public)")
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
                
                if (self.mySomeListList):
                    res = self.mySomeListList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-somelistlist-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySomeListList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.mySomeListList):
                    res = self.mySomeListList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-somelistlist-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySomeListList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.mySomeListList):
                    res = self.activateDeleteSomeListListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-somelistlist-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSomeListListFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.sys.blinky.example.lake_example.ref_practice.ref_practice_data_gen import RefPracticeData", 
        "moduleYangNamespacePrefix": "lake-example", 
        "validationPoint": null, 
        "yangName": "ref-practice", 
        "namespace": "ref_practice", 
        "logGroupName": "blinky-ref-practice", 
        "className": "BlinkyRefPractice", 
        "logModuleName": "a-sys-blinky-example-lake-example-ref-practice-blinky-ref-practice-gen", 
        "importStatement": "from a.sys.blinky.example.lake_example.ref_practice.blinky_ref_practice_gen import BlinkyRefPractice", 
        "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
        "dataClassName": "RefPracticeData", 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "ref-practice", 
            "namespace": "ref_practice", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "ref-practice"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkySomeListList", 
            "memberName": "SomeListList", 
            "yangName": "some-list", 
            "importStatement": "from a.sys.blinky.example.lake_example.ref_practice.some_list.blinky_some_list_list_gen import BlinkySomeListList"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "someLeafRef", 
            "yangName": "some-leaf-ref", 
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
        "blinky", 
        "example", 
        "lake_example"
    ], 
    "createTime": "2013"
}
"""

