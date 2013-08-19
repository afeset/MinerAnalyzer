# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from trx_phase import TrxPhase
from trx_progress import TrxProgress
from blinky_node import BlinkyNode
from blinky_node_state import BlinkyNodeState
from a.infra.misc.timeout_guard import TimeoutGuard
import a.infra.process.captain
from a.infra.basic.return_codes import ReturnCodes

from a.sys.confd.pyconfdlib import pyconfdlib
from a.sys.confd.pyconfdlib.key_path import KeyPath

class BlinkyConfigNode(BlinkyNode): 

    TRX_PROGRESS_FUNCTOR = 'TRX_PROGRESS_FUNCTOR'

    def __init__ (self, logger):
        BlinkyNode.__init__(self, logger)
        self.myDestroySelfFunctor=None
        self.myConfigErrorStr=None
        self.myAttachedObject=None
        self.myNotifyTrxProgressFunctor = None
        self.myNotifyDescendantsModifications = False
        self.myNodesToProgressNotification = []
        self.myAllowNoDestroySelfFunctor = False
        self.myState = None
        self.myRegisteredOperNodes = []
        self.myPendingOperNodes = []

    def _myStr (self):
        if self.myConfigErrorStr != None:
            return (",myConfigErrorStr='%s'" % self.myConfigErrorStr)
        return ""


    def setKeyPath (self, keyPath):
        for logFunc in self._log("set-key-path").debug3Func(): logFunc("called. keyPath=%s", keyPath)
        self.internalSetKeyPath(keyPath)

    def setDomain (self, domain):
        for logFunc in self._log("set-domain").debug3Func(): logFunc("called. domain=%s", domain)

        self.internalSetDomain(domain)

        # every object is registered for trx notification of the trx it was created in
        self.myDomain.registerNodeToProgressNotification(self)

    def activate (self):
        for logFunc in self._log("activate-before").debug1Func(): logFunc("Called. myIsActive=%s", self.myIsActive)

        if not self.myDestroySelfFunctor and not self.myAllowNoDestroySelfFunctor:
            for logFunc in self._log("activate-activate-specific-null-destroy-self-functor").errorFunc(): logFunc("destroySelf functor was not set")
            return ReturnCodes.kGeneralError

        res = BlinkyNode.activate(self)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("activate-base-implementation-failed").errorFunc(): logFunc("BlinkyNode::activate() failed")
            return ReturnCodes.kGeneralError

        res = self.activateSpecific()
        if res != ReturnCodes.kOk:
            for logFunc in self._log("activate-activate-specific-failed").errorFunc(): logFunc("activateSpecific() failed")
            return ReturnCodes.kGeneralError

        for logFunc in self._log("activate-after").debug1Func(): logFunc("Done. myIsActive=%s", self.myIsActive)
        return ReturnCodes.kOk

    def deactivate (self):
        for logFunc in self._log("deactivate-before").debug1Func(): logFunc("Called. myIsActive=%s", self.myIsActive)

        res = self.deactivateSpecific()
        if res != ReturnCodes.kOk:
            for logFunc in self._log("deactivate-deactivate-specific-failed").errorFunc(): logFunc("deactivateSpecific() failed")
            return ReturnCodes.kGeneralError

        res = BlinkyNode.deactivate(self)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("deactivate-base-implementation-failed").errorFunc(): logFunc("BlinkyNode::deactivate() failed")
            return ReturnCodes.kGeneralError

        for logFunc in self._log("deactivate-after").debug1Func(): logFunc("Done. myIsActive=%s", self.myIsActive)
        return ReturnCodes.kOk


    def trxElementBegin(self):
        self.myState.reset()

    def trxElementEnd(self):
        pass

    def setDestroySelfFunctor(self, functor):
        if self.myIsActive:
            for logFunc in self._log("set-destroy-functor-active").errorFunc(): logFunc("setDestroySelfFunctor is illegal when blinky node is active")
        self.myDestroySelfFunctor=functor

    def setNotifyTrxProgressFunctor (self, functor, notifyDescendantsModifications):
        for logFunc in self._log("set-notify-trx-progress-functor").debug2Func(): logFunc("Called")
        if self.myIsActive:
            for logFunc in self._log("set-notify-trx-progress-functor-active").errorFunc(): logFunc("setNotifyTrxProgressFunctor is illegal when blinky node is active")
        self.myNotifyTrxProgressFunctor=functor
        self.myNotifyDescendantsModifications=notifyDescendantsModifications
        self.myDomain.registerNodeToProgressNotification(self)

    def activateDestroySelfFunctor(self, phase):
        for logFunc in self._log("activate-destroy-self-functor").debug2Func(): logFunc("Called, phase=%s", phase)
        if self.myIsActive:
            if self.myDestroySelfFunctor != None:
                timeoutGuard = TimeoutGuard(self._log, '%s-destroy-self-functor-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.DESTROY_SELF_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.DESTROY_SELF_FUNCTOR, phase))
                res = self.myDestroySelfFunctor(phase)
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDestroySelfFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() != TrxPhase.kPrepare):
                        for logFunc in self._log("activate-destroy-self-functor-failed-prepare").errorFunc():
                            logFunc("activateDestroySelfFunctor - functor failed - fatal. phase=%s, myConfigErrorStr=%s",
                                  phase, self.myConfigErrorStr)
                        a.infra.process.processFatal("destroy self functor failed during non-prepare phase")
                    for logFunc in self._log("activate-destroy-self-functor-failed").noticeFunc():
                        logFunc("activateDestroySelfFunctor - functor failed. phase=%s, myConfigErrorStr=%s",
                               phase, self.myConfigErrorStr)
                    self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    return ReturnCodes.kGeneralError
        for logFunc in self._log("activate-destroy-self-functor-done").debug2Func(): logFunc("Done, phase=%s", phase)
        return ReturnCodes.kOk

    def activateNotifyTrxProgressFunctor (self, progress):
        for logFunc in self._log("activate-notify-trx-progress-functor").debug2Func(): logFunc("Called, progress=%s", progress)
        if self.myIsActive:
            if self.myNotifyTrxProgressFunctor != None:
                timeoutGuard = TimeoutGuard(self._log, '%s-activate-notify-trx-progress-functor-%s' % (self.myKeyPath, progress), 
                                            self.getFunctorTimeoutForProgress(self.TRX_PROGRESS_FUNCTOR, progress), 
                                            self.getFunctorMildTimeoutForProgress(self.TRX_PROGRESS_FUNCTOR, progress))
                res = self.myNotifyTrxProgressFunctor(progress)
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myNotifyTrxProgressFunctor.__name__);
                if (res != ReturnCodes.kOk):
                    if (not progress.isPrepare()):
                        for logFunc in self._log("activate-notify-trx-progress-functor-failed-prepare").errorFunc():
                            logFunc("activateNotifyTrxProgressFunctor - functor failed - fatal. progress=%s, myConfigErrorStr=%s",
                                  progress, self.myConfigErrorStr)
                        a.infra.process.processFatal("notify trx progress functor failed during non-prepare progress")
                    for logFunc in self._log("activate-notify-trx-progress-functor-failed").noticeFunc():
                        logFunc("activateNotifyTrxProgressFunctor - functor failed. progress=%s, myConfigErrorStr=%s",
                               progress, self.myConfigErrorStr)
                    self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    return ReturnCodes.kGeneralError
        for logFunc in self._log("activate-notify-trx-progress-functor-done").debug2Func(): logFunc("Done, progress=%s", progress)
        return ReturnCodes.kOk


    def handleTrxProgressNotification (self, progress):
        for logFunc in self._log("handle-trx-progress-notification").debug3Func(): logFunc("Called, progress=%s, myState=%s", progress, self.myState)

        res = self.handleTrxProgressNotificationSpecific(progress)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("handle-trx-progress-notification-handle-specific-failed").errorFunc():
                logFunc("handleTrxProgressNotification(): handleTrxProgressNotificationSpecific() failed, trxProgress=%s", progress)
            return ReturnCodes.kGeneralError

        if (not self.myState or (not progress.isAbort() or self.myState.isStageDone(progress.getPrepareProgressStage()))):
            res = self.activateNotifyTrxProgressFunctor(progress)
            if (res != ReturnCodes.kOk):
                for logFunc in self._log("handle-trx-progress-notification-activate-failed").noticeFunc():
                    logFunc("handleTrxProgressNotification(): activateNotifyTrxProgressFunctor() failed, trxProgress=%s", progress)
                return ReturnCodes.kGeneralError

        if self.myState:
            self.myState.setStageDone(progress)

        return ReturnCodes.kOk

    def handleTrxProgressNotificationSpecific (self, progress):
        __pychecker__='no-argsused'
        return ReturnCodes.kOk

    def handleTrxElement(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element").debug1Func(): logFunc("handleTrxElement() called: phase=%s, trxElement=%s, keyDepth=%s",
                                               phase, trxElement, keyDepth)
        if (phase.getConfdPhase() == TrxPhase.kPrepare) and \
           (phase.getBlinkyPhase() == TrxPhase.kBlinky):
            self.myConfigErrorStr=""
            self.trxElementBegin()
            if self.myNotifyTrxProgressFunctor:
                self.myDomain.registerNodeToProgressNotification(self)
            for node in self.myNodesToProgressNotification:
                self.myDomain.registerNodeToProgressNotification(node)

        return self.trxElementHelper(trxElement, keyDepth, phase)

    def addNodesToProgressNotification (self, nodes):
        self.myNotifyDescendantsModifications=True
        for node in nodes:
            if node not in self.myNodesToProgressNotification:
                self.myNodesToProgressNotification.append(node)

    def findBlinkyNode(self, keyPath, keyDepth_PassByRef, foundAtKeyDepth_PassByRef):
        __pychecker__='no-argsused'
        raise NotImplementedError()

    def setConfigErrorStr(self, errorStr):
        for logFunc in self._log("set-config-error-str").debug1Func(): logFunc("setConfigErrorStr() called: errorStr=%s", errorStr)
        self.myConfigErrorStr = errorStr
        self.myDomain.setConfigErrorStr(errorStr)

    def isInTrigger (self):
        for logFunc in self._log("is-in-trigger").debug1Func(): logFunc("isInTrigger() called")
        return self.myDomain.isInTrigger()

    def setAttachedObject(self, attachedObject):
        if self.myAttachedObject:
            a.infra.process.processFatal("An object is already attached! "+str(self.myKeyPath))
        if not attachedObject:
            a.infra.process.processFatal("Trying to attach a NULL object! "+str(self.myKeyPath))
        self.myAttachedObject = attachedObject

    def activateCandidate (self):
        pass
    
    def getAttachedObject(self):
        return self.myAttachedObject
    
    def allocMyCandidate (self):
        raise NotImplementedError()

    def deleteMyCandidate (self):
        raise NotImplementedError()

    def internalInit(self):
        for logFunc in self._log("internal-init").debug2Func(): logFunc("internalInit(): called, myState=%s", self.myState)
        self.myState = BlinkyNodeState(self._log)
        res = self.allocMyCandidate()
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("internal-init-alloc-my-candidate-failed").errorFunc():
                logFunc("internalInit() - allocaMyCandidate() failed, myState=%s", self.myState)
            return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

    def internalFinalize(self):
        for logFunc in self._log("internal-finalize").debug2Func(): logFunc("internalFinalize(): Called, myState=%s", self.myState)
        if len(self.myRegisteredOperNodes):
            for logFunc in self._log("internal-finalize-oper-nodes-exist").warningFunc(): logFunc("a config object is being deleted but some of its oper nodes weren't deactivated. first oper path=%s",
                                                                    self.myRegisteredOperNodes[0].getKeyPath())
        self.deleteMyCandidate()
        self.myState = None

    def setTransError (self, tctx, error):
        for logFunc in self._log("set-trans-error").debug1Func(): logFunc("Called, tctx=%s, error=%s", tctx, error)
        self.myDomain.setDpErrorStr(tctx, error)

    def setActionError (self, userInfo, error):
        for logFunc in self._log("set-action-error").debug1Func(): logFunc("Called, userInfo=%s, error=%s", userInfo, error)
        self.myDomain.setActionErrorStr(userInfo, error)

    def trxElementHelper(self, trxElement, keyDepth, phase):
        for logFunc in self._log("trx-element-helper").errorFunc(): logFunc("NOT IMPLEMENTED")
        __pychecker__='no-argsused'
        raise NotImplementedError()

    def registerOperNode (self, operNode):
        for logFunc in self._log("register-oper-node").debug1Func(): logFunc("Called, operNode=%s", operNode)

        registrationAllowed = False
        trxPhase = self.myDomain.getTrxPhase()
        if trxPhase.isCommitPublic():
            registrationAllowed = True
        elif not self.myParentNode:
            # this is a top level object
            registrationAllowed = True
        if registrationAllowed:
            self.registerOperNodeToDomain(operNode)
        else:
            for logFunc in self._log("register-oper-node-registration-is-not-allowed").errorFunc(): logFunc("oper node registration is not allowed at this stage. operNode=%s, trxPhase=%s", operNode, trxPhase)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def unregisterOperNode (self, operNode):
        for logFunc in self._log("unregister-oper-node").debug1Func(): logFunc("Called, operNode=%s", operNode)

        unregistrationAllowed = False
        trxPhase = self.myDomain.getTrxPhase()
        if trxPhase.isCommitPublic():
            unregistrationAllowed = True
        if unregistrationAllowed:
            self.unregisterOperNodeFromDomain(operNode)
        else:
            for logFunc in self._log("unregister-oper-node-unregistration-is-not-allowed").errorFunc(): logFunc("oper node unregistration is not allowed at this stage. operNode=%s, trxPhase=%s", operNode, trxPhase)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def registerOperNodeToDomain (self, operNode):
        for logFunc in self._log("register-oper-node-to-domain").debug1Func(): logFunc("Called, operNode=%s", operNode)

        operRelativePath = KeyPath()
        operNode.getOperRelativePath(operRelativePath)

        callpointName = operNode.getCallpointName()

        res = operNode.getDomain().registerOperCallpoint(callpointName, self, operRelativePath, operNode)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("register-oper-node-to-domain-register-oper-callpoint-failed").errorFunc(): logFunc(
                "domain->registerOperCallpoint() failed. callpointName=%s, myKeyPath=%s, operRelativePath=%s, operNode=%s, res=%s", 
                callpointName, self.myKeyPath, operRelativePath, operNode, res)
            return ReturnCodes.kGeneralError

        self.myRegisteredOperNodes.append(operNode)

        for logFunc in self._log("register-oper-node-to-domain-done").debug1Func(): logFunc("Done, operNode=%s", operNode)

        return ReturnCodes.kOk

    def unregisterOperNodeFromDomain(self, operNode):
        for logFunc in self._log("unregister-oper-node-from-domain").debug1Func(): logFunc("Called, operNode=%s", operNode)


        self.myRegisteredOperNodes.remove(operNode)
        callpointName = operNode.getCallpointName()

        operRelativePath = KeyPath()
        operNode.getOperRelativePath(operRelativePath)

        res = operNode.getDomain().unregisterCallpoint(callpointName, self.getKeyPath(), operRelativePath)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("unregister-oper-node-from-domain-unregister-callpoint-failed").errorFunc(): logFunc("domain->unregisterCallpoint() failed. callpointName=%s, myKeyPath=%s, operRelativePath=%s, operNode=%s, res=%s",
                                                                                            callpointName, self.myKeyPath, operRelativePath, operNode, res)
            return ReturnCodes.kGeneralError

        for logFunc in self._log("unregister-oper-node-from-domain-done").debug1Func(): logFunc("Done, operNode=%s", operNode)

        return ReturnCodes.kOk

    def operGetElem (self, tctx, callpoint, keypath):
        __pychecker__='no-argsused'
        pass

    def operGetNext (self, tctx, callpoint, keypath, next):
        __pychecker__='no-argsused'
        pass

