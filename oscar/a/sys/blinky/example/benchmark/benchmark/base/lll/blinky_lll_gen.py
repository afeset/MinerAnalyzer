


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

from a.sys.blinky.example.benchmark.benchmark.base.lll.lll_data_gen import LllData


from a.sys.blinky.example.benchmark.benchmark.base.lll.aaa.blinky_aaa_gen import BlinkyAaa

from a.sys.blinky.example.benchmark.benchmark.base.lll.ccc.blinky_ccc_gen import BlinkyCcc

from a.sys.blinky.example.benchmark.benchmark.base.lll.bbb.blinky_bbb_gen import BlinkyBbb


from a.sys.blinky.example.benchmark.benchmark.benchmark_module_gen import ColorT


class BlinkyLll(BlinkyContainer):
    ourNamespace="http://qwilt.com/model/benchmark"
    #leaves
    
    ourXmlTagColor="color"
    
    ourXmlTagName="name"
    

    #descendants
    
    ourXmlTagAaa="aaa"
    
    ourXmlTagCcc="ccc"
    
    ourXmlTagBbb="bbb"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    AAA_CREATE_FUNCTOR = 'AAA_CREATE_FUNCTOR'
    AAA_DELETE_FUNCTOR = 'AAA_DELETE_FUNCTOR'
    
    CCC_CREATE_FUNCTOR = 'CCC_CREATE_FUNCTOR'
    CCC_DELETE_FUNCTOR = 'CCC_DELETE_FUNCTOR'
    
    BBB_CREATE_FUNCTOR = 'BBB_CREATE_FUNCTOR'
    BBB_DELETE_FUNCTOR = 'BBB_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateAaaFunctor=None
        self.myDeleteAaaFunctor=None
        self.myAaa=None
        
        self.myCreateCccFunctor=None
        self.myDeleteCccFunctor=None
        self.myCcc=None
        
        self.myCreateBbbFunctor=None
        self.myDeleteBbbFunctor=None
        self.myBbb=None
        
        self.myValueSetFunctor=None
        self.myCandidateData=None
        self.myRunningData=None
        self.isInDestroy = False
        
        self.validateRegistrationDone = False
        self.actionRegistrationDone=False
        
        

    @classmethod
    def s_create (cls, logger, 
                  
                  
                  lll, 
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkylll').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyLll._validationPointId, BlinkyLll._actionPointId)

        confd_key=KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(lll);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("lll", "http://qwilt.com/model/benchmark", "bnch"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("base", "http://qwilt.com/model/benchmark", "bnch"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyLll(logger)
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

    
    def setCreateAaaFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-aaa-functor-active").errorFunc():
                logFunc("setCreateAaaFunctor() is illegal when blinky node is active")
        self.myCreateAaaFunctor = functor

    def setDeleteAaaFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-aaa-functor-active").errorFunc():
                logFunc("setDeleteAaaFunctor() is illegal when blinky node is active")
        self.myDeleteAaaFunctor = functor
    
    def setCreateCccFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-ccc-functor-active").errorFunc():
                logFunc("setCreateCccFunctor() is illegal when blinky node is active")
        self.myCreateCccFunctor = functor

    def setDeleteCccFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-ccc-functor-active").errorFunc():
                logFunc("setDeleteCccFunctor() is illegal when blinky node is active")
        self.myDeleteCccFunctor = functor
    
    def setCreateBbbFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-bbb-functor-active").errorFunc():
                logFunc("setCreateBbbFunctor() is illegal when blinky node is active")
        self.myCreateBbbFunctor = functor

    def setDeleteBbbFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-bbb-functor-active").errorFunc():
                logFunc("setDeleteBbbFunctor() is illegal when blinky node is active")
        self.myDeleteBbbFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagColor)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not ColorT.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-color-failed")\
                        .error("illegal enum value %s for color", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.color = ColorT.getByValue(newValue.asEnum())
                self.myCandidateData.setHasColor()
                
            else:
                self.setColorDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagName)):
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
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagAaa)):
            return self.myAaa
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagCcc)):
            return self.myCcc
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagBbb)):
            return self.myBbb
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkylll').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.blinky.example.benchmark.benchmark.base.lll.blinky_lll_gen import BlinkyLll', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagAaa)):
                    keyPathRegistered = BlinkyAaa.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagCcc)):
                    keyPathRegistered = BlinkyCcc.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagBbb)):
                    keyPathRegistered = BlinkyBbb.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagColor)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagName)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkylll-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.blinky.example.benchmark.benchmark.base.lll.blinky_lll_gen import BlinkyLll', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAaa)):
            if (self.myAaa):
                for logFunc in self._log("prepare-my-blinky-node-aaa-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myAaa = BlinkyAaa(self._log)
            self.myAaa.setParent(self)
            self.myAaa.setKeyPath(keyPath)
            self.myAaa.setDomain(self.myDomain)

            return self.myAaa
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagCcc)):
            if (self.myCcc):
                for logFunc in self._log("prepare-my-blinky-node-ccc-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myCcc = BlinkyCcc(self._log)
            self.myCcc.setParent(self)
            self.myCcc.setKeyPath(keyPath)
            self.myCcc.setDomain(self.myDomain)

            return self.myCcc
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagBbb)):
            if (self.myBbb):
                for logFunc in self._log("prepare-my-blinky-node-bbb-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myBbb = BlinkyBbb(self._log)
            self.myBbb.setParent(self)
            self.myBbb.setKeyPath(keyPath)
            self.myBbb.setDomain(self.myDomain)

            return self.myBbb
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAaa)):
            self.myAaa = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagCcc)):
            self.myCcc = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagBbb)):
            self.myBbb = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAaa)):
                if (self.myCreateAaaFunctor):
                    if (not self.myAaa):
                        for logFunc in self._log("handle-trx-element-create-aaa-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): aaa not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-aaa-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.AAA_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.AAA_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateAaaFunctor(phase, self.myAaa)
                    except:
                        for logFunc in self._log("handle-trx-element-create-aaa-functor-exception").exceptionFunc():
                            logFunc("Aaa's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateAaaFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-aaa-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): aaa functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-aaa-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): aaa functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagCcc)):
                if (self.myCreateCccFunctor):
                    if (not self.myCcc):
                        for logFunc in self._log("handle-trx-element-create-ccc-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): ccc not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-ccc-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.CCC_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.CCC_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateCccFunctor(phase, self.myCcc)
                    except:
                        for logFunc in self._log("handle-trx-element-create-ccc-functor-exception").exceptionFunc():
                            logFunc("Ccc's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateCccFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-ccc-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): ccc functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-ccc-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): ccc functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagBbb)):
                if (self.myCreateBbbFunctor):
                    if (not self.myBbb):
                        for logFunc in self._log("handle-trx-element-create-bbb-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): bbb not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-bbb-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.BBB_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.BBB_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateBbbFunctor(phase, self.myBbb)
                    except:
                        for logFunc in self._log("handle-trx-element-create-bbb-functor-exception").exceptionFunc():
                            logFunc("Bbb's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateBbbFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-bbb-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): bbb functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-bbb-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): bbb functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.myAaa):
            self.myAaa.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myCcc):
            self.myCcc.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myBbb):
            self.myBbb.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAaa)):
                res = self.activateDeleteAaaFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-aaa-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): aaa functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-aaa-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): aaa functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagCcc)):
                res = self.activateDeleteCccFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-ccc-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): ccc functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-ccc-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): ccc functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagBbb)):
                res = self.activateDeleteBbbFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-bbb-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): bbb functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-bbb-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): bbb functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeAaa(self):
        self.myAaa = None

    def activateDeleteAaaFunctor(self, phase):
        for logFunc in self._log("activate-delete-aaa-functor").debug3Func(): logFunc("activateDeleteAaaFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteAaaFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-aaa-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.AAA_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.AAA_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteAaaFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-aaa-functor-exception").exceptionFunc():
                        logFunc("Aaa's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteAaaFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-aaa-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteAaaFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-aaa-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteAaaFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeCcc(self):
        self.myCcc = None

    def activateDeleteCccFunctor(self, phase):
        for logFunc in self._log("activate-delete-ccc-functor").debug3Func(): logFunc("activateDeleteCccFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteCccFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-ccc-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.CCC_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.CCC_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteCccFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-ccc-functor-exception").exceptionFunc():
                        logFunc("Ccc's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteCccFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-ccc-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteCccFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-ccc-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteCccFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeBbb(self):
        self.myBbb = None

    def activateDeleteBbbFunctor(self, phase):
        for logFunc in self._log("activate-delete-bbb-functor").debug3Func(): logFunc("activateDeleteBbbFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteBbbFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-bbb-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.BBB_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.BBB_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteBbbFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-bbb-functor-exception").exceptionFunc():
                        logFunc("Bbb's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteBbbFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-bbb-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteBbbFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-bbb-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteBbbFunctor(): functor failed, phase=%s", phase)
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
        self.myCandidateData = LllData()
        
        res = self.setColorDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-color-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setColorDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setNameDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-name-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setNameDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setColorDefaultValue (self, setHas):
        for logFunc in self._log("set-color-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.color = ColorT.kRed
            
        if setHas:
            self.myCandidateData.setHasColor()

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
            self.myCandidateData = LllData()
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
        self.myRunningData = LllData()
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkylll-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkylll-failed").errorFunc():
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
                
                if (self.myAaa):
                    res = self.myAaa.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-aaa-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-aaa-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myCcc):
                    res = self.myCcc.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ccc-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-ccc-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myBbb):
                    res = self.myBbb.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-bbb-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-bbb-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.myAaa):
                    res = self.activateDeleteAaaFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-aaa-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAaaFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myAaa):
                    res = self.myAaa.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-aaa-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAaa.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myCcc):
                    res = self.activateDeleteCccFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ccc-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteCccFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myCcc):
                    res = self.myCcc.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ccc-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myCcc.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myBbb):
                    res = self.activateDeleteBbbFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-bbb-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteBbbFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myBbb):
                    res = self.myBbb.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-bbb-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myBbb.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myAaa):
                    res = self.myAaa.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-aaa-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myAaa.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeAaa()
                
                if (self.myCcc):
                    res = self.myCcc.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ccc-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myCcc.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeCcc()
                
                if (self.myBbb):
                    res = self.myBbb.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-bbb-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myBbb.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeBbb()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myAaa):
                    res = self.myAaa.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-aaa-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAaa.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteAaaFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-aaa-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAaaFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteAaaFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myCcc):
                    res = self.myCcc.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ccc-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myCcc.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteCccFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ccc-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteCccFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteCccFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myBbb):
                    res = self.myBbb.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-bbb-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myBbb.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteBbbFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-bbb-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteBbbFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteBbbFunctor failed in commit phase (private/public)")
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
                
                if (self.myAaa):
                    res = self.myAaa.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-aaa-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myAaa.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myCcc):
                    res = self.myCcc.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ccc-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myCcc.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myBbb):
                    res = self.myBbb.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-bbb-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myBbb.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myAaa):
                    res = self.myAaa.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-aaa-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAaa.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myAaa):
                    res = self.activateDeleteAaaFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-aaa-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAaaFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myCcc):
                    res = self.myCcc.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ccc-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myCcc.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myCcc):
                    res = self.activateDeleteCccFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ccc-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteCccFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myBbb):
                    res = self.myBbb.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-bbb-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myBbb.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myBbb):
                    res = self.activateDeleteBbbFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-bbb-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteBbbFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.lll_data_gen import LllData", 
        "moduleYangNamespacePrefix": "bnch", 
        "validationPoint": null, 
        "yangName": "lll", 
        "namespace": "lll", 
        "logGroupName": "blinky-lll", 
        "className": "BlinkyLll", 
        "logModuleName": "a-sys-blinky-example-benchmark-benchmark-base-lll-blinky-lll-gen", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.blinky_lll_gen import BlinkyLll", 
        "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
        "dataClassName": "LllData", 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "bnch", 
            "yangName": "base", 
            "namespace": "base", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "base"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "isCurrent": true, 
            "yangName": "lll", 
            "namespace": "lll", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "keyLeaf": {
                "varName": "lll", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lll"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyAaa", 
            "memberName": "Aaa", 
            "yangName": "aaa", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.aaa.blinky_aaa_gen import BlinkyAaa"
        }, 
        {
            "className": "BlinkyCcc", 
            "memberName": "Ccc", 
            "yangName": "ccc", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.ccc.blinky_ccc_gen import BlinkyCcc"
        }, 
        {
            "className": "BlinkyBbb", 
            "memberName": "Bbb", 
            "yangName": "bbb", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.bbb.blinky_bbb_gen import BlinkyBbb"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
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
        "blinky", 
        "example", 
        "benchmark", 
        "benchmark"
    ], 
    "createTime": "2013"
}
"""

