# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from utils import Utils
from a.infra.misc.enum_with_value import EnumWithValue

import copy

class TrxPhase(object):
    # Dummy to satisfy pychecker
    _log=None

    @classmethod
    def setLogger(cls, logger):
        cls._log=logger.createLogger("sys-blinky", "trx-phase")

    class TrxConfdPhase(EnumWithValue):
        def __init__ (self, value, name):
            EnumWithValue.__init__(self, value, name)

    kPrepare=TrxConfdPhase(0,"kPrepare")
    kCommit=TrxConfdPhase(1, "kCommit")
    kAbort=TrxConfdPhase(2, "kAbort")
    kConfdLast=TrxConfdPhase(3, "kConfdLast")

    class TrxBlinkyPhase(EnumWithValue):
        def __init__ (self, value, name):
            EnumWithValue.__init__(self, value, name)

    kBlinky=TrxBlinkyPhase(0,"kBlinky")
    kPrivate=TrxBlinkyPhase(1,"kPrivate")
    kPublic=TrxBlinkyPhase(2,"kPublic")
    kBlinkyLast=TrxBlinkyPhase(3,"kBlinkyLast")

    def __init__ (self, confdPhase, blinkyPhase):
        Utils.fatalIfNotInstanceOf(confdPhase, self.TrxConfdPhase)
        Utils.fatalIfNotInstanceOf(blinkyPhase, self.TrxBlinkyPhase)
        self.myConfdPhase=copy.deepcopy(confdPhase)
        self.myBlinkyPhase=copy.deepcopy(blinkyPhase)

    def copyFrom (self, other):
        Utils.fatalIfNotInstanceOf(other, TrxPhase)
        self.myConfdPhase=copy.deepcopy(other.myConfdPhase)
        self.myBlinkyPhase=copy.deepcopy(other.myBlinkyPhase)

    def getConfdPhase (self):
        return self.myConfdPhase

    def getBlinkyPhase (self):
        return self.myBlinkyPhase

    def isPrepareBlinky (self):
        return (self.myConfdPhase == self.kPrepare) and (self.myBlinkyPhase == self.kBlinky)

    def isPreparePrivate (self):
        return (self.myConfdPhase == self.kPrepare) and (self.myBlinkyPhase == self.kPrivate)

    def isPreparePublic (self):
        return (self.myConfdPhase == self.kPrepare) and (self.myBlinkyPhase == self.kPublic)

    def isCommitBlinky (self):
        return (self.myConfdPhase == self.kCommit) and (self.myBlinkyPhase == self.kBlinky)

    def isCommitPrivate (self):
        return (self.myConfdPhase == self.kCommit) and (self.myBlinkyPhase == self.kPrivate)

    def isCommitPublic (self):
        return (self.myConfdPhase == self.kCommit) and (self.myBlinkyPhase == self.kPublic)

    def isAbortBlinky (self):
        return (self.myConfdPhase == self.kAbort) and (self.myBlinkyPhase == self.kBlinky)

    def isAbortPrivate (self):
        return (self.myConfdPhase == self.kAbort) and (self.myBlinkyPhase == self.kPrivate)

    def isAbortPublic (self):
        return (self.myConfdPhase == self.kAbort) and (self.myBlinkyPhase == self.kPublic)

    def gotoNextBlinkyPhase(self):
        if self.myConfdPhase == self.kPrepare:
            if self.myBlinkyPhase == self.kBlinky:
                self.myBlinkyPhase = self.kPrivate
            elif self.myBlinkyPhase == self.kPrivate:
                self.myBlinkyPhase = self.kPublic
            elif self.myBlinkyPhase == self.kPublic:
                self.myBlinkyPhase = self.kBlinkyLast
            else:
                self._log("goto-next-blinky-phase-prepare-illegal-blinky")\
                    .error("gotoNextBlinkyPhase - prepare - illegal blinky phase %s", self.myBlinkyPhase)
        elif self.myConfdPhase == self.kPrepare:
            pass
        elif (self.myConfdPhase == self.kCommit) or (self.myConfdPhase == self.kAbort):
            if self.myBlinkyPhase == self.kPublic:
                self.myBlinkyPhase = self.kPrivate
            elif self.myBlinkyPhase == self.kPrivate:
                self.myBlinkyPhase = self.kBlinky
            elif self.myBlinkyPhase == self.kBlinky:
                self.myBlinkyPhase = self.kBlinkyLast
            else:
                self._log("goto-next-blinky-phase-commit-abort-illegal-blinky")\
                    .error("gotoNextBlinkyPhase - commit-abort - illegal blinky phase %s", self.myBlinkyPhase)
        else:
            self._log("goto-next-blinky-phase-illegal-confd")\
                .error("gotoNextBlinkyPhase - illegal confd phase %s", self.myConfdPhase)

    def __str__ (self):
        return "{%s,%s}" % (self.myConfdPhase, self.myBlinkyPhase)

