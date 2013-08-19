# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

import copy

from a.infra.basic.return_codes import ReturnCodes

from a.sys.confd.pyconfdlib import pyconfdlib
from a.sys.confd.pyconfdlib.key_path import KeyPath

class BlinkyNode(object): 

    DESTROY_SELF_FUNCTOR = 'DESTROY_SELF_FUNCTOR'

    def __init__ (self, logger):
        self._log=logger.createLogger("sys-blinky", "blinky-node")
        self.myParentNode = None
        self.myIsActive = False
        self.myDomain = None
        self.myKeyPath = None
        self.myDestroySelfFunctor = None
        self.myAllowNoDestroySelfFunctor = False

        self.defaultFunctorTimeout = 5000
        self.functorTimeouts = {}
        self.functorMildTimeouts = {}

    def __str__ (self):
        ret="{BlinkyNode: myKeyPath=%s, myDomain=%s" % (self.myKeyPath, self.myDomain)
        ret+=self._myStr()
        ret=ret+"}"
        return ret

    def _myStr (self):
        raise NotImplementedError()

    def _makeKeyFromFunctorNameAndPhase (self, functorName, phase):
        return "%s-%s-%s" % (functorName, str(phase.getConfdPhase()), str(phase.getBlinkyPhase()))

    def _makeKeyFromFunctorNameAndProgress (self, functorName, progress):
        return "%s-%s-%s-%s" % (functorName, str(progress.getProgressStage()), str(progress.getTrxPhase().getConfdPhase()), str(progress.getTrxPhase().getBlinkyPhase()))

    def setFunctorTimeout (self, functorName, timeout):
        self.functorTimeouts[functorName] = timeout

    def setFunctorMildTimeout (self, functorName, timeout):
        self.functorMildTimeouts[functorName] = timeout

    def setFunctorTimeoutForPhase (self, functorName, phase, timeout):
        keyStr = self._makeKeyFromFunctorNameAndPhase(functorName, phase)
        self.functorTimeouts[keyStr] = timeout

    def setFunctorMildTimeoutForPhase (self, functorName, phase, timeout):
        keyStr = self._makeKeyFromFunctorNameAndPhase(functorName, phase)
        self.functorMildTimeouts[keyStr] = timeout

    def setFunctorTimeoutForProgress (self, functorName, progress, timeout):
        keyStr = self._makeKeyFromFunctorNameAndProgress(functorName, progress)
        self.functorTimeouts[keyStr] = timeout

    def setFunctorMildTimeoutForProgress (self, functorName, progress, timeout):
        keyStr = self._makeKeyFromFunctorNameAndProgress(functorName, progress)
        self.functorMildTimeouts[keyStr] = timeout

    def getFunctorTimeout (self, functorName):
        if functorName in self.functorTimeouts:
            return self.functorTimeouts[functorName]
        return self.defaultFunctorTimeout

    def getFunctorMildTimeout (self, functorName):
        if functorName in self.functorMildTimeouts:
            return self.functorMildTimeouts[functorName]
        return self.getFunctorTimeout(functorName)/2

    def getFunctorTimeoutForPhase (self, functorName, phase):
        keyStr = self._makeKeyFromFunctorNameAndPhase(functorName, phase)
        if keyStr in self.functorTimeouts:
            return self.functorTimeouts[keyStr]
        return self.defaultFunctorTimeout

    def getFunctorMildTimeoutForPhase (self, functorName, phase):
        keyStr = self._makeKeyFromFunctorNameAndPhase(functorName, phase)
        if keyStr in self.functorMildTimeouts:
            return self.functorMildTimeouts[keyStr]
        return self.getFunctorTimeoutForPhase(functorName, phase)/2

    def getFunctorTimeoutForProgress (self, functorName, progress):
        keyStr = self._makeKeyFromFunctorNameAndProgress(functorName, progress)
        if keyStr in self.functorTimeouts:
            return self.functorTimeouts[keyStr]
        return self.defaultFunctorTimeout

    def getFunctorMildTimeoutForProgress (self, functorName, progress):
        keyStr = self._makeKeyFromFunctorNameAndProgress(functorName, progress)
        if keyStr in self.functorMildTimeouts:
            return self.functorMildTimeouts[keyStr]
        return self.getFunctorTimeoutForProgress(functorName, progress)/2

    def setParent (self, parentNode):
        for logFunc in self._log("set-parent").debug3Func(): logFunc("called. parentNode=%s", parentNode)
        self.myParentNode = parentNode

    def activate (self):
        for logFunc in self._log("activate").debug2Func(): logFunc("activate() called")
        if not self.myDestroySelfFunctor and not self.myAllowNoDestroySelfFunctor:
            for logFunc in self._log("activate-no-destroy-self-functor").errorFunc(): logFunc("destroy-self functor was not set")
            return ReturnCodes.kGeneralError
        self.myIsActive=True
        res = self.activateSpecific()
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("activate-activate-specific-failed").errorFunc(): logFunc("activate-activate-specific-failed")
            return ReturnCodes.kGeneralError
        for logFunc in self._log("activate").debug2Func(): logFunc("activate() done")
        return ReturnCodes.kOk

    def deactivate (self):
        for logFunc in self._log("deactivate").debug2Func(): logFunc("deactivate() called")
        res = self.deactivateSpecific()
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("deactivate-deactivate-specific-failed").errorFunc(): logFunc("deactivate-deactivate-specific-failed")
            return ReturnCodes.kGeneralError
        self.myIsActive=False
        for logFunc in self._log("deactivate").debug2Func(): logFunc("deactivate() done")
        return ReturnCodes.kOk

    def getKeyPath(self):
        return self.myKeyPath

    def getKeyPathStr (self):
        return str(self.myKeyPath)

    def getParentNode (self):
        return self.myParentNode

    def internalSetKeyPath (self, keyPath):
        for logFunc in self._log("internal-set-keypath").debug1Func(): logFunc("called. keyPath=%s", keyPath)
        self.myKeyPath = copy.deepcopy(keyPath)
        self._log.setInstance(str(keyPath))

    def internalSetDomain (self, domain):
        for logFunc in self._log("internal-set-domain").debug1Func(): logFunc("called. domain=%s", domain)
        self.myDomain = domain

    def getDomain (self):
        return self.myDomain

    def activateSpecific(self):
        raise NotImplementedError()

    def deactivateSpecific(self):
        raise NotImplementedError()

