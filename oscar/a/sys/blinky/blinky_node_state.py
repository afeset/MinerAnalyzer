# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from trx_phase import TrxPhase
from trx_progress import TrxProgress
from a.infra.basic.return_codes import ReturnCodes

class BlinkyNodeState(object):
    def __init__ (self, logger):
        self._log=logger  # Not creating a separate logger, will use instance of BlinkyContainer
        self.reset()

    def __del__ (self):
        self.reset()

    def __str__ (self):
        ret = "{BlinkyNodeState: "
        ret = ret+ "myPreparePrivateCalled="+str(self.myPreparePrivateCalled)
        ret = ret+",myPreparePublicCalled="+str(self.myPreparePublicCalled)
        ret = ret+",myCommitPrivateCalled="+str(self.myCommitPrivateCalled)
        ret = ret+",myCommitPublicCalled="+str(self.myCommitPublicCalled)
        ret = ret+",myCandidateActivated="+str(self.myCandidateActivated)
        ret = ret+"}"
        return ret
    
    def reset(self):
        self.myPreparePrivateCalled=False
        self.myPreparePublicCalled=False
        self.myCommitPrivateCalled=False
        self.myCommitPublicCalled=False
        self.myCandidateActivated=False
        self.myCalledStages = {
            str(TrxProgress.kBefore) : {
                str(TrxPhase.kPrepare) : {
                    str(TrxPhase.kBlinky) : False,
                    str(TrxPhase.kPrivate) : False,
                    str(TrxPhase.kPublic) : False,
                    },
                str(TrxPhase.kCommit) : {
                    str(TrxPhase.kBlinky) : False,
                    str(TrxPhase.kPrivate) : False,
                    str(TrxPhase.kPublic) : False,
                },
                str(TrxPhase.kAbort) : {
                    str(TrxPhase.kBlinky) : False,
                    str(TrxPhase.kPrivate) : False,
                    str(TrxPhase.kPublic) : False,
                }
            },
            str(TrxProgress.kAfter) : {
                str(TrxPhase.kPrepare) : {
                    str(TrxPhase.kBlinky) : False,
                    str(TrxPhase.kPrivate) : False,
                    str(TrxPhase.kPublic) : False,
                    },
                str(TrxPhase.kCommit) : {
                    str(TrxPhase.kBlinky) : False,
                    str(TrxPhase.kPrivate) : False,
                    str(TrxPhase.kPublic) : False,
                },
                str(TrxPhase.kAbort) : {
                    str(TrxPhase.kBlinky) : False,
                    str(TrxPhase.kPrivate) : False,
                    str(TrxPhase.kPublic) : False,
                }
            }
        }
    
    def setPhaseDone(self, phase):
        for logFunc in self._log("set-phase-done-before").debug3Func(): logFunc("setPhaseDone() called. state=%s, phase=%s", self, phase)
        if (phase.getConfdPhase() == TrxPhase.kPrepare):
            if (phase.getBlinkyPhase() == TrxPhase.kPrivate):
                self.myPreparePrivateCalled = True
            elif (phase.getBlinkyPhase() == TrxPhase.kPublic):
                self.myPreparePublicCalled = True
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                self.myCandidateActivated = True
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate):
                self.myCommitPrivateCalled = True
            elif (phase.getBlinkyPhase() == TrxPhase.kPublic):
                self.myCommitPublicCalled = True
        for logFunc in self._log("set-phase-done-after").debug3Func(): logFunc("setPhaseDone() called. state=%s, phase=%s", self, phase)

    def setStageDone (self, progress):
        for logFunc in self._log("set-stage-done-before").debug3Func(): logFunc("setStageDone() called. state before=%s, progress=%s", self, progress)
        self.myCalledStages[str(progress.getProgressStage())][str(progress.getTrxPhase().getConfdPhase())][str(progress.getTrxPhase().getBlinkyPhase())] = True
        for logFunc in self._log("set-stage-done-after").debug3Func(): logFunc("setStageDone() called. state before=%s, progress=%s", self, progress)
    
    def isPhaseDone(self, phase):
        for logFunc in self._log("is-phase-done").debug3Func(): logFunc("isPhaseDone() called. state=%s, phase=%s", self, phase)
        if (phase.getConfdPhase() == TrxPhase.kPrepare):
            if (phase.getBlinkyPhase() == TrxPhase.kPrivate):
                return self.myPreparePrivateCalled
            elif (phase.getBlinkyPhase() == TrxPhase.kPublic):
                return self.myPreparePublicCalled
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                return self.myCandidateActivated
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate):
                return self.myCommitPrivateCalled
            elif (phase.getBlinkyPhase() == TrxPhase.kPublic):
                return self.myCommitPublicCalled
        return False

    def isStageDone (self, progress):
        for logFunc in self._log("is-stage-done").debug3Func(): logFunc("isStageDone() called. state=%s, progress=%s", self, progress)
        return self.myCalledStages[str(progress.getProgressStage())][str(progress.getTrxPhase().getConfdPhase())][str(progress.getTrxPhase().getBlinkyPhase())]

