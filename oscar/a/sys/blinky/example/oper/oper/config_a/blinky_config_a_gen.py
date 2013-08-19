


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




from a.sys.blinky.example.oper.oper.config_a.op_l.blinky_op_l_gen import BlinkyOpL

from a.sys.blinky.example.oper.oper.config_a.config_q.blinky_config_q_gen import BlinkyConfigQ

from a.sys.blinky.example.oper.oper.config_a.config_p.blinky_config_p_list_gen import BlinkyConfigPList

from a.sys.blinky.example.oper.oper.config_a.config_u.blinky_config_u_list_gen import BlinkyConfigUList




class BlinkyConfigA(BlinkyContainer):
    ourNamespace="http://qwilt.com/model/oper"
    #leaves
    

    #descendants
    
    ourXmlTagOpL="op-l"
    
    ourXmlTagConfigQ="config-q"
    
    ourXmlTagConfigPList="config-p"
    
    ourXmlTagConfigUList="config-u"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    OPL_CREATE_FUNCTOR = 'OPL_CREATE_FUNCTOR'
    OPL_DELETE_FUNCTOR = 'OPL_DELETE_FUNCTOR'
    
    CONFIGQ_CREATE_FUNCTOR = 'CONFIGQ_CREATE_FUNCTOR'
    CONFIGQ_DELETE_FUNCTOR = 'CONFIGQ_DELETE_FUNCTOR'
    
    CONFIGPLIST_CREATE_FUNCTOR = 'CONFIGPLIST_CREATE_FUNCTOR'
    CONFIGPLIST_DELETE_FUNCTOR = 'CONFIGPLIST_DELETE_FUNCTOR'
    
    CONFIGULIST_CREATE_FUNCTOR = 'CONFIGULIST_CREATE_FUNCTOR'
    CONFIGULIST_DELETE_FUNCTOR = 'CONFIGULIST_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateOpLFunctor=None
        self.myDeleteOpLFunctor=None
        self.myOpL=None
        
        self.myCreateConfigQFunctor=None
        self.myDeleteConfigQFunctor=None
        self.myConfigQ=None
        
        self.myCreateConfigPListFunctor=None
        self.myDeleteConfigPListFunctor=None
        self.myConfigPList=None
        
        self.myCreateConfigUListFunctor=None
        self.myDeleteConfigUListFunctor=None
        self.myConfigUList=None
        
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

        logger('s-create-blinkyconfiga').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyConfigA._validationPointId, BlinkyConfigA._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("config-a", "http://qwilt.com/model/oper", "oper"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyConfigA(logger)
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

    
    def setCreateOpLFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-op-l-functor-active").errorFunc():
                logFunc("setCreateOpLFunctor() is illegal when blinky node is active")
        self.myCreateOpLFunctor = functor

    def setDeleteOpLFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-op-l-functor-active").errorFunc():
                logFunc("setDeleteOpLFunctor() is illegal when blinky node is active")
        self.myDeleteOpLFunctor = functor
    
    def setCreateConfigQFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-config-q-functor-active").errorFunc():
                logFunc("setCreateConfigQFunctor() is illegal when blinky node is active")
        self.myCreateConfigQFunctor = functor

    def setDeleteConfigQFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-config-q-functor-active").errorFunc():
                logFunc("setDeleteConfigQFunctor() is illegal when blinky node is active")
        self.myDeleteConfigQFunctor = functor
    
    def setCreateConfigPListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-config-p-functor-active").errorFunc():
                logFunc("setCreateConfigPListFunctor() is illegal when blinky node is active")
        self.myCreateConfigPListFunctor = functor

    def setDeleteConfigPListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-config-p-functor-active").errorFunc():
                logFunc("setDeleteConfigPListFunctor() is illegal when blinky node is active")
        self.myDeleteConfigPListFunctor = functor
    
    def setCreateConfigUListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-config-u-functor-active").errorFunc():
                logFunc("setCreateConfigUListFunctor() is illegal when blinky node is active")
        self.myCreateConfigUListFunctor = functor

    def setDeleteConfigUListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-config-u-functor-active").errorFunc():
                logFunc("setDeleteConfigUListFunctor() is illegal when blinky node is active")
        self.myDeleteConfigUListFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagOpL)):
            return self.myOpL
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagConfigQ)):
            return self.myConfigQ
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagConfigPList)):
            return self.myConfigPList
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagConfigUList)):
            return self.myConfigUList
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyconfiga').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.blinky.example.oper.oper.config_a.blinky_config_a_gen import BlinkyConfigA', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagOpL)):
                    keyPathRegistered = BlinkyOpL.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagConfigQ)):
                    keyPathRegistered = BlinkyConfigQ.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagConfigPList)):
                    keyPathRegistered = BlinkyConfigPList.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagConfigUList)):
                    keyPathRegistered = BlinkyConfigUList.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        logger('is-key-path-registered-blinkyconfiga-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.blinky.example.oper.oper.config_a.blinky_config_a_gen import BlinkyConfigA', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOpL)):
            if (self.myOpL):
                for logFunc in self._log("prepare-my-blinky-node-opl-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myOpL = BlinkyOpL(self._log)
            self.myOpL.setParent(self)
            self.myOpL.setKeyPath(keyPath)
            self.myOpL.setDomain(self.myDomain)

            return self.myOpL
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigQ)):
            if (self.myConfigQ):
                for logFunc in self._log("prepare-my-blinky-node-configq-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myConfigQ = BlinkyConfigQ(self._log)
            self.myConfigQ.setParent(self)
            self.myConfigQ.setKeyPath(keyPath)
            self.myConfigQ.setDomain(self.myDomain)

            return self.myConfigQ
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigPList)):
            if (self.myConfigPList):
                for logFunc in self._log("prepare-my-blinky-node-configplist-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myConfigPList = BlinkyConfigPList(self._log)
            self.myConfigPList.setParent(self)
            self.myConfigPList.setKeyPath(keyPath)
            self.myConfigPList.setDomain(self.myDomain)

            return self.myConfigPList
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigUList)):
            if (self.myConfigUList):
                for logFunc in self._log("prepare-my-blinky-node-configulist-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myConfigUList = BlinkyConfigUList(self._log)
            self.myConfigUList.setParent(self)
            self.myConfigUList.setKeyPath(keyPath)
            self.myConfigUList.setDomain(self.myDomain)

            return self.myConfigUList
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOpL)):
            self.myOpL = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigQ)):
            self.myConfigQ = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigPList)):
            self.myConfigPList = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigUList)):
            self.myConfigUList = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOpL)):
                if (self.myCreateOpLFunctor):
                    if (not self.myOpL):
                        for logFunc in self._log("handle-trx-element-create-opl-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): opl not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-opl-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.OPL_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.OPL_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateOpLFunctor(phase, self.myOpL)
                    except:
                        for logFunc in self._log("handle-trx-element-create-opl-functor-exception").exceptionFunc():
                            logFunc("OpL's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateOpLFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-opl-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): opl functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-opl-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): opl functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigQ)):
                if (self.myCreateConfigQFunctor):
                    if (not self.myConfigQ):
                        for logFunc in self._log("handle-trx-element-create-configq-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): configq not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-configq-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.CONFIGQ_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.CONFIGQ_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateConfigQFunctor(phase, self.myConfigQ)
                    except:
                        for logFunc in self._log("handle-trx-element-create-configq-functor-exception").exceptionFunc():
                            logFunc("ConfigQ's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateConfigQFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-configq-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): configq functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-configq-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): configq functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigPList)):
                if (self.myCreateConfigPListFunctor):
                    if (not self.myConfigPList):
                        for logFunc in self._log("handle-trx-element-create-configplist-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): configplist not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-configplist-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.CONFIGPLIST_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.CONFIGPLIST_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateConfigPListFunctor(phase, self.myConfigPList)
                    except:
                        for logFunc in self._log("handle-trx-element-create-configplist-functor-exception").exceptionFunc():
                            logFunc("ConfigPList's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateConfigPListFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-configplist-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): configplist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-configplist-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): configplist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigUList)):
                if (self.myCreateConfigUListFunctor):
                    if (not self.myConfigUList):
                        for logFunc in self._log("handle-trx-element-create-configulist-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): configulist not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-configulist-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.CONFIGULIST_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.CONFIGULIST_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateConfigUListFunctor(phase, self.myConfigUList)
                    except:
                        for logFunc in self._log("handle-trx-element-create-configulist-functor-exception").exceptionFunc():
                            logFunc("ConfigUList's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateConfigUListFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-configulist-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): configulist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-configulist-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): configulist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.myOpL):
            self.myOpL.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myConfigQ):
            self.myConfigQ.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myConfigPList):
            self.myConfigPList.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myConfigUList):
            self.myConfigUList.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOpL)):
                res = self.activateDeleteOpLFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-opl-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): opl functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-opl-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): opl functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigQ)):
                res = self.activateDeleteConfigQFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-configq-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): configq functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-configq-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): configq functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigPList)):
                res = self.activateDeleteConfigPListFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-configplist-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): configplist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-configplist-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): configplist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigUList)):
                res = self.activateDeleteConfigUListFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-configulist-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): configulist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-configulist-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): configulist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeOpL(self):
        self.myOpL = None

    def activateDeleteOpLFunctor(self, phase):
        for logFunc in self._log("activate-delete-opl-functor").debug3Func(): logFunc("activateDeleteOpLFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteOpLFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-opl-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.OPL_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.OPL_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteOpLFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-opl-functor-exception").exceptionFunc():
                        logFunc("OpL's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteOpLFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-opl-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteOpLFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-opl-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteOpLFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeConfigQ(self):
        self.myConfigQ = None

    def activateDeleteConfigQFunctor(self, phase):
        for logFunc in self._log("activate-delete-configq-functor").debug3Func(): logFunc("activateDeleteConfigQFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteConfigQFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-configq-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.CONFIGQ_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.CONFIGQ_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteConfigQFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-configq-functor-exception").exceptionFunc():
                        logFunc("ConfigQ's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteConfigQFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-configq-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteConfigQFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-configq-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteConfigQFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeConfigPList(self):
        self.myConfigPList = None

    def activateDeleteConfigPListFunctor(self, phase):
        for logFunc in self._log("activate-delete-configplist-functor").debug3Func(): logFunc("activateDeleteConfigPListFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteConfigPListFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-configplist-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.CONFIGPLIST_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.CONFIGPLIST_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteConfigPListFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-configplist-functor-exception").exceptionFunc():
                        logFunc("ConfigPList's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteConfigPListFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-configplist-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteConfigPListFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-configplist-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteConfigPListFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeConfigUList(self):
        self.myConfigUList = None

    def activateDeleteConfigUListFunctor(self, phase):
        for logFunc in self._log("activate-delete-configulist-functor").debug3Func(): logFunc("activateDeleteConfigUListFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteConfigUListFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-configulist-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.CONFIGULIST_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.CONFIGULIST_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteConfigUListFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-configulist-functor-exception").exceptionFunc():
                        logFunc("ConfigUList's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteConfigUListFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-configulist-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteConfigUListFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-configulist-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteConfigUListFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    

    

    
    
    def notifyWithCandidate(self, phase):
        for logFunc in self._log("notify-with-candidate").debug3Func(): logFunc("notifyWithCandidate(): called, candidate=%s, phase=%s",
                                                              self.myCandidateData, phase)
        return ReturnCodes.kOk
    
    def allocMyCandidate(self):
        for logFunc in self._log("alloc-my-candidate").debug3Func():
            logFunc("called")
        
        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            pass
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyconfiga-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyconfiga-failed").errorFunc():
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
                
                if (self.myOpL):
                    res = self.myOpL.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-opl-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-opl-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myConfigQ):
                    res = self.myConfigQ.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configq-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-configq-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myConfigPList):
                    res = self.myConfigPList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configplist-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-configplist-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myConfigUList):
                    res = self.myConfigUList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configulist-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-configulist-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.myOpL):
                    res = self.activateDeleteOpLFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-opl-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteOpLFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myOpL):
                    res = self.myOpL.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-opl-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myOpL.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myConfigQ):
                    res = self.activateDeleteConfigQFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configq-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConfigQFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myConfigQ):
                    res = self.myConfigQ.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configq-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigQ.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myConfigPList):
                    res = self.activateDeleteConfigPListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configplist-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConfigPListFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myConfigPList):
                    res = self.myConfigPList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configplist-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigPList.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myConfigUList):
                    res = self.activateDeleteConfigUListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configulist-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConfigUListFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myConfigUList):
                    res = self.myConfigUList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configulist-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigUList.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myOpL):
                    res = self.myOpL.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-opl-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myOpL.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeOpL()
                
                if (self.myConfigQ):
                    res = self.myConfigQ.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configq-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigQ.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeConfigQ()
                
                if (self.myConfigPList):
                    res = self.myConfigPList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configplist-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigPList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeConfigPList()
                
                if (self.myConfigUList):
                    res = self.myConfigUList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configulist-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigUList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeConfigUList()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myOpL):
                    res = self.myOpL.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-opl-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myOpL.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteOpLFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-opl-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteOpLFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteOpLFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myConfigQ):
                    res = self.myConfigQ.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configq-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigQ.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteConfigQFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configq-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConfigQFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteConfigQFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myConfigPList):
                    res = self.myConfigPList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configplist-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigPList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteConfigPListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configplist-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConfigPListFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteConfigPListFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myConfigUList):
                    res = self.myConfigUList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configulist-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigUList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteConfigUListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configulist-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConfigUListFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteConfigUListFunctor failed in commit phase (private/public)")
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
                
                if (self.myOpL):
                    res = self.myOpL.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-opl-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myOpL.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myConfigQ):
                    res = self.myConfigQ.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configq-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigQ.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myConfigPList):
                    res = self.myConfigPList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configplist-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigPList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myConfigUList):
                    res = self.myConfigUList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configulist-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigUList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myOpL):
                    res = self.myOpL.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-opl-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myOpL.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myOpL):
                    res = self.activateDeleteOpLFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-opl-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteOpLFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myConfigQ):
                    res = self.myConfigQ.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configq-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigQ.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myConfigQ):
                    res = self.activateDeleteConfigQFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configq-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConfigQFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myConfigPList):
                    res = self.myConfigPList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configplist-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigPList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myConfigPList):
                    res = self.activateDeleteConfigPListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configplist-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConfigPListFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myConfigUList):
                    res = self.myConfigUList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configulist-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConfigUList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myConfigUList):
                    res = self.activateDeleteConfigUListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-configulist-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConfigUListFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.sys.blinky.example.oper.oper.config_a.config_a_data_gen import ConfigAData", 
        "moduleYangNamespacePrefix": "oper", 
        "validationPoint": null, 
        "yangName": "config-a", 
        "namespace": "config_a", 
        "logGroupName": "blinky-config-a", 
        "className": "BlinkyConfigA", 
        "logModuleName": "a-sys-blinky-example-oper-oper-config-a-blinky-config-a-gen", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.blinky_config_a_gen import BlinkyConfigA", 
        "moduleYangNamespace": "http://qwilt.com/model/oper", 
        "dataClassName": "ConfigAData", 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "config-a", 
            "namespace": "config_a", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "config-a"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyOpL", 
            "memberName": "OpL", 
            "yangName": "op-l", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_l.blinky_op_l_gen import BlinkyOpL"
        }, 
        {
            "className": "BlinkyConfigQ", 
            "memberName": "ConfigQ", 
            "yangName": "config-q", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_q.blinky_config_q_gen import BlinkyConfigQ"
        }, 
        {
            "className": "BlinkyConfigPList", 
            "memberName": "ConfigPList", 
            "yangName": "config-p", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.blinky_config_p_list_gen import BlinkyConfigPList"
        }, 
        {
            "className": "BlinkyConfigUList", 
            "memberName": "ConfigUList", 
            "yangName": "config-u", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_u.blinky_config_u_list_gen import BlinkyConfigUList"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [], 
    "module": {}, 
    "env": [
        "a", 
        "sys", 
        "blinky", 
        "example", 
        "oper", 
        "oper"
    ], 
    "createTime": "2013"
}
"""

