# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from trx_phase import TrxPhase
from utils import Utils
from a.infra.misc.enum_with_value import EnumWithValue

import copy

class TrxProgress(object):
    # Dummy to satisfy pychecker
    _log=None

    @classmethod
    def setLogger(cls, logger):
        cls._log=logger.createLogger("sys-blinky", "trx-progress")

    class TrxProgressStages(EnumWithValue):
        def __init__ (self, value, name):
            EnumWithValue.__init__(self, value, name)

    kBefore=TrxProgressStages(0,"kBefore")
    kAfter=TrxProgressStages(1, "kAfter")
    kProgressStagesLast=TrxProgressStages(2, "kProgressStagesLast")

    def __init__ (self, trxPhase, progressStage):
        Utils.fatalIfNotInstanceOf(progressStage, self.TrxProgressStages)
        self.myProgressStage=copy.deepcopy(progressStage)
        self.myTrxPhase=copy.deepcopy(trxPhase)

    def copyFrom (self, other):
        Utils.fatalIfNotInstanceOf(other, TrxProgress)
        self.myProgressStage=copy.deepcopy(other.myProgressStage)
        self.myTrxPhase=copy.deepcopy(other.myTrxPhase)

    def getProgressStage (self):
        return self.myProgressStage

    def getPrepareProgressStage (self):
        prepareStage = TrxProgress(TrxPhase(TrxPhase.kPrepare, self.myTrxPhase.getBlinkyPhase()), self.myProgressStage)
        return prepareStage

    def getTrxPhase (self):
        return self.myTrxPhase

    def isBlinky (self):
        return self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kBlinky

    def isPrepare (self):
        return self.myTrxPhase.myConfdPhase == self.myTrxPhase.kPrepare

    def isAbort (self):
        return self.myTrxPhase.myConfdPhase == self.myTrxPhase.kAbort

    def isPrepareBlinkyBefore (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kPrepare) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kBlinky) and (self.myProgressStage == self.kBefore)

    def isPrepareBlinkyAfter (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kPrepare) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kBlinky) and (self.myProgressStage == self.kAfter)

    def isPreparePrivateBefore (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kPrepare) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPrivate) and (self.myProgressStage == self.kBefore)

    def isPreparePrivateAfter (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kPrepare) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPrivate) and (self.myProgressStage == self.kAfter)

    def isPreparePublicBefore (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kPrepare) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPublic) and (self.myProgressStage == self.kBefore)

    def isPreparePublicAfter (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kPrepare) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPublic) and (self.myProgressStage == self.kAfter)

    def isCommitPrivateBefore (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kCommit) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPrivate) and (self.myProgressStage == self.kBefore)

    def isCommitPrivateAfter (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kCommit) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPrivate) and (self.myProgressStage == self.kAfter)

    def isCommitPublicBefore (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kCommit) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPublic) and (self.myProgressStage == self.kBefore)

    def isCommitPublicAfter (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kCommit) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPublic) and (self.myProgressStage == self.kAfter)

    def isAbortBlinkyBefore (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kAbort) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kBlinky) and (self.myProgressStage == self.kBefore)

    def isAbortBlinkyAfter (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kAbort) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.BlinkyNode) and (self.myProgressStage == self.kAfter)

    def isAbortPrivateBefore (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kAbort) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPrivate) and (self.myProgressStage == self.kBefore)

    def isAbortPrivateAfter (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kAbort) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPrivate) and (self.myProgressStage == self.kAfter)

    def isAbortPublicBefore (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kAbort) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPublic) and (self.myProgressStage == self.kBefore)

    def isAbortPublicAfter (self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kAbort) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kPublic) and (self.myProgressStage == self.kAfter)

    def isCommitBlinkyBefore(self):
        return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kCommit) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kBlinky) and (self.myProgressStage == self.kBefore)

    def isCommitBlinkyAfter (self):
       return (self.myTrxPhase.myConfdPhase  == self.myTrxPhase.kCommit) and (self.myTrxPhase.myBlinkyPhase == self.myTrxPhase.kBlinky) and (self.myProgressStage == self.kAfter)


    def __str__ (self):
        return "{%s,%s,%s}" % (self.myTrxPhase.myConfdPhase , self.myTrxPhase.myBlinkyPhase, self.myProgressStage)

