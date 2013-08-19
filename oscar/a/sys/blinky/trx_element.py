# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

# This Python class mimics the basic::ReturnCode class

from a.infra.misc.enum_with_value import EnumWithValue
import a.infra.process.captain
from a.sys.confd.pyconfdlib import pyconfdlib
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from utils import Utils
from trx_phase import TrxPhase

class TrxElement (object):

    class OpCode(EnumWithValue):
        def __init__ (self, value, name):
            EnumWithValue.__init__ (self, value, name)

    kValueSet = OpCode(0,"kValueSet")
    kCreate = OpCode(1,"kCreate")
    kDelete = OpCode(2,"kDelete")
    kMovedAfter = OpCode(3,"kMovedAfter")

    def __init__ (self, logger, keyPath, op, oldv, newv, subscriptionId):
        Utils.fatalIfNotInstanceOf(keyPath, KeyPath)
        Utils.fatalIfNotInstanceOf(op, pyconfdlib.ConfdIterOp)
        Utils.fatalIfNotInstanceOf(oldv, Value, allowNone=True)
        Utils.fatalIfNotInstanceOf(newv, Value, allowNone=True)
        Utils.fatalIfNotInstanceOf(subscriptionId, int)

        self._log=logger.createLogger("sys-blinky","trx-element")
        for logFunc in self._log('iterate-ctor').debug4Func(): logFunc('TrxElement Ctor - op=%s, keyPath=%s, newv=%s', str(op), str(keyPath), str(newv))
        self.myKeyPath=None
        if oldv:
            self.myOldVal = oldv
        else:
            self.myOldVal = None
        if newv:
            self.myNewVal = newv
        else:
            self.myNewVal = None
        self.myBlinkyNode=None
        self.myBlinkyNodeKeyDepth=0
        self.mySubscriptionId=subscriptionId
        # Create a list with 3 False values
        __pychecker__="no-local"   # x is not used
        self.myPreparePassed=[ False for x in range(TrxPhase.kBlinkyLast.getValue()) ]

        for logFunc in self._log("ctor").debug4Func(): logFunc("ctor. op=%s", op)
        self.myKeyPath=keyPath

        if op==pyconfdlib.MOP_CREATED:
            self.myOp=self.kCreate
            for logFunc in self._log("iterate-created").debug4Func(): logFunc("config node created")
        elif op==pyconfdlib.MOP_DELETED:
            self.myOp=self.kDelete
            for logFunc in self._log("iterate-deleted").debug4Func(): logFunc("config node deleted")
        elif op==pyconfdlib.MOP_VALUE_SET:
            self.myOp=self.kValueSet
            for logFunc in self._log("iterate-value-set").debug4Func(): logFunc("config node value set from %s to %s", oldv, newv)
        elif op==pyconfdlib.MOP_MODIFIED:
            pass
        elif op==pyconfdlib.MOP_MOVED_AFTER:
            self.myOp=self.kMovedAfter
            for logFunc in self._log("iterate-moved-after").debug4Func(): logFunc("config node moved-after")
            pass
        else:
            a.infra.process.processFatal("Got unexpected op %s in cdb_diff_iterate()" % op)

        for logFunc in self._log("ctor-ended").debug4Func(): logFunc("ctor-ended op=%s", op)
        
    def __str__ (self):
        return "{TrxElement: subscriptionId=%s, op=%s, keyPath=%s, oldv=%s, newv=%s, bnode=%s, bnodeKeyDepth=%s, pp=%s}" % \
            (self.mySubscriptionId, self.myOp, self.myKeyPath, self.myOldVal, self.myNewVal, self.myBlinkyNode, 
             self.myBlinkyNodeKeyDepth, self.myPreparePassed)

    def getNewVal (self):
        return self.myNewVal

    def getOldVal(self):
        return self.myOldVal

    def getOpCode(self):
        return self.myOp

    def getSubscriptionId(self):
        return self.mySubscriptionId

    def setKeyPath(self, keyPath):
        self.myKeyPath = keyPath

    def getKeyPath(self):
        return self.myKeyPath

    def setBlinkyNode(self, blinkyNode, blinkyNodeKeyDepth):
        for logFunc in self._log("set-blinky-node").debug4Func(): logFunc("setBlinkyNode(): called, blinkyNode=%s", blinkyNode)
        Utils.fatalIfNotInstanceOf(blinkyNodeKeyDepth, int)
        self.myBlinkyNode = blinkyNode
        self.myBlinkyNodeKeyDepth = blinkyNodeKeyDepth

    def getBlinkyNode(self):
        return self.myBlinkyNode

    def getBlinkyNodeKeyDepth(self):
        return self.myBlinkyNodeKeyDepth

    def setPreparePassedOn(self, phase):
        for logFunc in self._log("set-prepare-passed-on-keypath").debug2Func():
            logFunc("setPreparePassedOn - phases: phase=%s, prepare-blinky-passed=%s, prepare-private-passed=%s, prepare-public-passed=%s",
                    phase, self.myPreparePassed[TrxPhase.kBlinky.getValue()], self.myPreparePassed[TrxPhase.kPrivate.getValue()], 
                    self.myPreparePassed[TrxPhase.kPublic.getValue()])
        if (phase.getBlinkyPhase() >= TrxPhase.kBlinkyLast):
            for logFunc in self._log("set-prepare-passed-on-illegal-phase").errorFunc():
                logFunc("setPreparePassedOn - illegal blinky phase=%s, keyPath=%s", phase, self.myKeyPath)
        self.myPreparePassed[phase.getBlinkyPhase().getValue()] = True

    def hasPreparePassed(self, phase):
        for logFunc in self._log("has-prepare-passed-keypath").debug2Func():
            logFunc("hasPreparePassed - phases: phase=%s, prepare-blinky-passed=%s, prepare-private-passed=%s, prepare-public-passed=%s",
                    phase, self.myPreparePassed[TrxPhase.kBlinky.getValue()], self.myPreparePassed[TrxPhase.kPrivate.getValue()], 
                    self.myPreparePassed[TrxPhase.kPublic.getValue()])
        if (phase.getBlinkyPhase() >= TrxPhase.kBlinkyLast):
            for logFunc in self._log("has-prepare-passed-keypath-illegal-phase").errorFunc():
                logFunc("hasPreparePassed - illegal blinky phase=%s, keyPath=%s", phase, self.myKeyPath)
        return self.myPreparePassed[phase.getBlinkyPhase().getValue()]

    def isSystemDefault (self):
        for logFunc in self._log("is-system-default").debug4Func():
            logFunc("called: keyPath=%s", self.myKeyPath)
        i=0
        while i < self.myKeyPath.getLen():
            val = self.myKeyPath.getAt(i)
            if val.isXmlTag() and val.xmlTagAsStr() == "system-defaults":
                return True
            i += 1
        return False
