# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from trx_phase import TrxPhase
import a.infra.process.captain
from a.infra.basic.return_codes import ReturnCodes
from blinky_config_node import BlinkyConfigNode
from pass_by_ref import PassByRef
from trx_element import TrxElement

__pychecker__="no-classattr"

class BlinkyContainer(BlinkyConfigNode): 
    def __init__ (self, logger):
        BlinkyConfigNode.__init__(self, logger)

    def __str__ (self):
        return "{BlinkyContainer: myState=%s, {BlinkyConfigNode=%s}}" % (str(self.myState), BlinkyConfigNode.__str__(self))

    def handleTrxElementPrepareBlinkyValueSet(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-prepare-blinky-value-set-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        self.copyRunningToCandidate()
        self.trxElementUpdateCandidate(trxElement, keyDepth)
        return ReturnCodes.kOk

    def handleTrxElementPreparePrivateValueSet(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-prepare-private-value-set-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        phase=TrxPhase(TrxPhase.kPrepare, TrxPhase.kPrivate)
        res = self.notifyPhase(phase)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-element-prepare-private-value-set-failed").noticeFunc():
                logFunc("handle-trx-element-prepare-private-value-set-failed: element-key-path=%s, element-op-code=%s, keyDepth=%s, res=%s",
                        trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, res)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def handleTrxElementPreparePublicValueSet(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-prepare-public-value-set-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        phase=TrxPhase(TrxPhase.kPrepare, TrxPhase.kPublic)
        res = self.notifyPhase(phase)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-element-prepare-public-value-set-failed").noticeFunc():
                logFunc("handle-trx-prepare-public-value-set-failed: element-key-path=%s, element-op-code=%s, keyDepth=%s, res=%s",
                        trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, res)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
    def handleTrxElementCommitBlinkyValueSet(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-commit-blinky-value-set-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        self.activateCandidate()
        return ReturnCodes.kOk
    
    def handleTrxElementCommitPrivateValueSet(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-commit-private-value-set-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        phase=TrxPhase(TrxPhase.kCommit, TrxPhase.kPrivate)
        res = self.notifyPhase(phase);
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-element-commit-private-value-set-failed").errorFunc():
                logFunc("handle-trx-commit-private-value-set-failed: element-key-path=%s, element-op-code=%s, keyDepth=%s, res=%s",
                       trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, res)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
    def handleTrxElementCommitPublicValueSet(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-commit-public-value-set-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        phase=TrxPhase(TrxPhase.kCommit, TrxPhase.kPublic)
        res = self.notifyPhase(phase);
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-element-commit-public-value-set-failed").errorFunc():
                logFunc("handle-trx-commit-public-value-set-failed: element-key-path=%s, element-op-code=%s, keyDepth=%s, res=%s",
                       trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, res)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
    def handleTrxElementAbortBlinkyValueSet(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-abort-blinky-value-set-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        self.deleteMyCandidate()
        return ReturnCodes.kOk
    
    def handleTrxElementAbortPrivateValueSet(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-abort-private-value-set-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        phase=TrxPhase(TrxPhase.kAbort, TrxPhase.kPrivate)
        res = self.notifyPhase(phase);
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-element-abort-private-value-set-failed").errorFunc():
                logFunc("handle-trx-element-abort-private-value-set-failed - fatal: element-key-path=%s, "\
                       "element-op-code=%s, keyDepth=%s, res=%s", 
                       trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, res)
            a.infra.process.processFatal("abort private value set failed" )
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
    def handleTrxElementAbortPublicValueSet(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-abort-public-value-set-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        phase=TrxPhase(TrxPhase.kAbort, TrxPhase.kPublic)
        res = self.notifyPhase(phase)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-element-abort-public-value-set-failed").errorFunc():
                logFunc("handle-trx-abort-public-value-set-failed - fatal: element-key-path=%s, "\
                       "element-op-code=%s, keyDepth=%s, res=%s", 
                       trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, res)
            a.infra.process.processFatal("abort public value set failed" )
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
    def handleTrxElementPrepareBlinkyCreate(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-prepare-blinky-create-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        keyPath = trxElement.getKeyPath()
        newBlinkyNode = self.prepareMyBlinkyNode(keyPath, keyDepth)
        if not newBlinkyNode:
            for logFunc in self._log("handle-trx-element-prepare-blinky-create-blinky-node-not-created").errorFunc():
                logFunc("blinky node was not created: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                        trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
            a.infra.process.processFatal("blinky node was not created %s" % str(keyPath))
        res = newBlinkyNode.internalInit()
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-element-prepare-blinky-create-internal-init-failed").noticeFunc():
                logFunc("handleTrxElementPrepareBlinkyCreate - newBlinkyNode.internalInit() failed: "\
                        "element-key-path=%s, element-op-code=%s, keyDepth=%s, newBlinkyNode.getKeyPath()=%s", 
                        trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, newBlinkyNode.getKeyPath())
            self.abortMyBlinkyNode(keyPath, keyDepth)
            return ReturnCodes.kGeneralError

        nodes = self.myNodesToProgressNotification
        if self.myNotifyDescendantsModifications:
            nodes.append(self)
        newBlinkyNode.addNodesToProgressNotification(nodes)
    
        return ReturnCodes.kOk
    
    def handleTrxElementAbortBlinkyCreate(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-abort-blinky-create-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        keyPath = trxElement.getKeyPath()
        keyDepth_pbr=PassByRef(keyDepth)
        createdNode = self.getDescendant(keyPath, keyDepth_pbr)
        if (createdNode == None):
            for logFunc in self._log("handle-trx-element-abort-blinky-create-node-not-found").errorFunc():
                logFunc("node not found - fatal: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                       trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
            a.infra.process.processFatal("handle trx element abort blinky create - get descendant failed" )
        createdNode.internalFinalize()
        self.abortMyBlinkyNode(keyPath, keyDepth_pbr.value())
    
        return ReturnCodes.kOk
    
    def handleTrxElementAbortBlinkyDelete(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-abort-blinky-delete-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)

        return self.handleTrxElementAbortBlinkyValueSet(trxElement, keyDepth)

    def handleTrxElementCommitBlinkyCreate(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-commit-blinky-create-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        keyPath = trxElement.getKeyPath()
        keyDepth_pbr=PassByRef(keyDepth)
        createdNode = self.getDescendant(keyPath, keyDepth_pbr)
        if (createdNode == None):
            for logFunc in self._log("handle-trx-element-commit-blinky-create-node-not-found").errorFunc():
                logFunc("node not found - fatal: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                       trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
            a.infra.process.processFatal("handle trx element commit blinky create - get descendant failed" )
        createdNode.activateCandidate()
        return ReturnCodes.kOk
    
    def handleTrxElementCommitBlinkyDelete(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-commit-blinky-delete-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)
        keyPath = trxElement.getKeyPath()
        keyDepth_pbr=PassByRef(keyDepth)
        nodeToDelete = self.getDescendant(keyPath, keyDepth_pbr)
        if nodeToDelete:
            nodeToDelete.internalFinalize()

        self.deleteMyBlinkyNode(keyPath, keyDepth_pbr.value())

        return self.handleTrxElementCommitBlinkyValueSet(trxElement, keyDepth)

    def trxElementHelper(self, trxElement, keyDepth, phase):
        for logFunc in self._log("trx-element-helper-details").debug2Func():
            logFunc("trx-details: element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        keyPath = trxElement.getKeyPath()
    
        keyRemainderLen = keyPath.getLen() - keyDepth
        if (keyRemainderLen != 1):
            for logFunc in self._log("trx-element-helper-bad-path-len").errorFunc():
                logFunc("trx-helper, bad element key length, expected 1: phase=%s, keyPath=%s, keyPath.getLen()=%s, keyDepth=%s",
                       phase, keyPath, keyPath.getLen(), keyDepth)
            return ReturnCodes.kGeneralError
    
        res = ReturnCodes.kOk
    
        if trxElement.getOpCode() == TrxElement.kValueSet:
            if phase.getConfdPhase() == TrxPhase.kPrepare:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxElementPrepareBlinkyValueSet(trxElement, keyDepth)
                elif phase.getBlinkyPhase() == TrxPhase.kPrivate:
                    res = self.handleTrxElementPreparePrivateValueSet(trxElement, keyDepth)
                elif phase.getBlinkyPhase() == TrxPhase.kPublic:
                    res = self.handleTrxElementPreparePublicValueSet(trxElement, keyDepth)
                else:
                    for logFunc in self._log("trx-element-helper-value-set-illegal-trx-phase-prepare").errorFunc():
                        logFunc("trx-helper, illegal trx phase: phase=%s", phase)
                    return ReturnCodes.kGeneralError
            elif phase.getConfdPhase() == TrxPhase.kCommit:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxElementCommitBlinkyValueSet(trxElement, keyDepth)
                elif phase.getBlinkyPhase() == TrxPhase.kPrivate:
                    res = self.handleTrxElementCommitPrivateValueSet(trxElement, keyDepth)
                elif phase.getBlinkyPhase() == TrxPhase.kPublic:
                    res = self.handleTrxElementCommitPublicValueSet(trxElement, keyDepth)
                else:
                    for logFunc in self._log("trx-element-helper-value-set-illegal-trx-phase-commit").errorFunc():
                        logFunc("trx-helper, illegal trx phase: phase=%s", phase)
                    return ReturnCodes.kGeneralError
            elif phase.getConfdPhase() == TrxPhase.kAbort:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxElementAbortBlinkyValueSet(trxElement, keyDepth)
                elif phase.getBlinkyPhase() == TrxPhase.kPrivate:
                    res = self.handleTrxElementAbortPrivateValueSet(trxElement, keyDepth)
                elif phase.getBlinkyPhase() == TrxPhase.kPublic:
                    res = self.handleTrxElementAbortPublicValueSet(trxElement, keyDepth)
                else:
                    for logFunc in self._log("trx-element-helper-value-set-illegal-trx-phase-abort").errorFunc():
                        logFunc("trx-helper, illegal trx phase: phase=%s", phase)
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("trx-helper-value-set-illegal-trx-phase").errorFunc(): logFunc("trx-helper, illegal trx phase: phase=%s", phase)
                return ReturnCodes.kGeneralError

            if (res != ReturnCodes.kOk):
                if phase.getConfdPhase() == TrxPhase.kPrepare:
                    for logFunc in self._log("trx-element-helper-handle-value-set-failed-prepare").noticeFunc():
                        logFunc("trx-helper-handle-value-set-failed-prepare: element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                                trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
                else:
                    for logFunc in self._log("trx-element-helper-handle-value-set-failed").errorFunc():
                        logFunc("trx-helper-handle-value-set-failed: element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                               trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
                return ReturnCodes.kGeneralError

        elif trxElement.getOpCode() == TrxElement.kCreate:
            if phase.getConfdPhase() == TrxPhase.kPrepare:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxElementPrepareBlinkyCreate(trxElement, keyDepth)
                elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                     (phase.getBlinkyPhase() == TrxPhase.kPublic):
                    res = self.handleTrxElementCreate(trxElement, keyDepth, phase)
                else:
                    a.infra.process.processFatal("unknown blinky phase: %s" % phase)
                    return ReturnCodes.kGeneralError
            elif phase.getConfdPhase() == TrxPhase.kCommit:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxElementCommitBlinkyCreate(trxElement, keyDepth)
                elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                     (phase.getBlinkyPhase() == TrxPhase.kPublic):
                    res = self.handleTrxElementCreate(trxElement, keyDepth, phase)
                else:
                    a.infra.process.processFatal("unknown blinky phase: %s" % phase)
                    return ReturnCodes.kGeneralError
            elif phase.getConfdPhase() == TrxPhase.kAbort:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxElementAbortBlinkyCreate(trxElement, keyDepth)
                elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                     (phase.getBlinkyPhase() == TrxPhase.kPublic):
                    res = self.handleTrxElementCreate(trxElement, keyDepth, phase)
                else:
                    a.infra.process.processFatal("unknown blinky phase: %s" % phase)
                    return ReturnCodes.kGeneralError
            else:
                a.infra.process.processFatal("unknown confd phase: %s" % phase)
                return ReturnCodes.kGeneralError

            if (res != ReturnCodes.kOk):
                if phase.getConfdPhase() == TrxPhase.kPrepare:
                    for logFunc in self._log("trx-element-prepare-helper-handle-trx-create-failed-prepare").noticeFunc():
                        logFunc("trx-element-prepare-helper-handle-trx-create-failed-prepare: element-key-path=%s, "\
                                "element-op-code=%s, keyDepth=%s, phase=%s, res=%s", 
                                trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase, res)
                else:
                    for logFunc in self._log("trx-element-prepare-helper-handle-trx-create-failed").errorFunc():
                        logFunc("trx-element-prepare-helper-handle-trx-create-failed: element-key-path=%s, "\
                               "element-op-code=%s, keyDepth=%s, phase=%s, res=%s", 
                               trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase, res)

                return ReturnCodes.kGeneralError

        elif trxElement.getOpCode() == TrxElement.kDelete:
            if phase.getConfdPhase() == TrxPhase.kPrepare:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxElementPrepareBlinkyDelete(trxElement, keyDepth)
                elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                     (phase.getBlinkyPhase() == TrxPhase.kPublic):
                    res = self.handleTrxElementDelete(trxElement, keyDepth, phase)
                else:
                    a.infra.process.processFatal("unknown blinky phase: %s" % phase)
                    return ReturnCodes.kGeneralError
            elif phase.getConfdPhase() == TrxPhase.kCommit:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxElementCommitBlinkyDelete(trxElement, keyDepth)
                elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                     (phase.getBlinkyPhase() == TrxPhase.kPublic):
                    res = self.handleTrxElementDelete(trxElement, keyDepth, phase)
                else:
                    a.infra.process.processFatal("unknown blinky phase: %s" % phase)
                    return ReturnCodes.kGeneralError
            elif phase.getConfdPhase() == TrxPhase.kAbort:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxElementAbortBlinkyDelete(trxElement, keyDepth)
                elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                     (phase.getBlinkyPhase() == TrxPhase.kPublic):
                    res = self.handleTrxElementDelete(trxElement, keyDepth, phase)
                else:
                    a.infra.process.processFatal("unknown blinky phase: %s" % phase)
                    return ReturnCodes.kGeneralError
            else:
                a.infra.process.processFatal("unknown confd phase: %s" % phase)
                return ReturnCodes.kGeneralError

            if (res != ReturnCodes.kOk):
                if phase.getConfdPhase() == TrxPhase.kPrepare:
                    for logFunc in self._log("trx-element-prepare-helper-handle-trx-delete-failed-prepare").noticeFunc():
                        logFunc("trx-element-prepare-helper-handle-trx-delete-failed-prepare: element-key-path=%s, "\
                                "element-op-code=%s, keyDepth=%s, phase=%s, res=%s", 
                                trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase, res)
                else:
                    for logFunc in self._log("trx-element-prepare-helper-handle-trx-delete-failed").errorFunc():
                        logFunc("trx-element-prepare-helper-handle-trx-delete-failed: element-key-path=%s, "\
                               "element-op-code=%s, keyDepth=%s, phase=%s, res=%s", 
                               trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase, res)

                return ReturnCodes.kGeneralError

        else:
            for logFunc in self._log("trx-element-prepare-helper-illegal-op").errorFunc():
                logFunc("trx-element-prepare-helper-illegal-op: element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s, res=%s",
                       trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase, res)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
    
    def findBlinkyNode(self, keyPath, keyDepth_PBR, foundAtKeyDepth_PBR):
        for logFunc in self._log("find-blinky-node-details").debug2Func():
            logFunc("findBlinkyNode details: keyPath=%s, keyDepth=%s, foundAtKeyDepth=%s",
                    keyPath, keyDepth_PBR, foundAtKeyDepth_PBR)
        keyRemainderLen = keyPath.getLen() - keyDepth_PBR.value()
        if (keyRemainderLen < 1):
            for logFunc in self._log("find-blinky-node-path-too-short").noticeFunc():
                logFunc("findBlinkyNode too-short: keyPath=%s, key len=%s, keyDepth=%s",
                        keyPath, keyPath.getLen(), keyDepth_PBR)

            errStr = "Cannot delete this configuration element"
            self.setConfigErrorStr(errStr)
            return None

        if (keyRemainderLen > 1):
            for logFunc in self._log("find-blinky-node-getting-descendant").debug2Func():
                logFunc("find-blinky-node-getting-descendant: keyPath=%s, keyDepth=%s",
                        keyPath, keyDepth_PBR)
            descendant = self.getDescendant(keyPath, keyDepth_PBR)
            if (descendant == None):
                for logFunc in self._log("find-blinky-node-descendant-not-found").debug2Func():
                    logFunc("find-blinky-node-descendant-not-found: keyPath=%s, keyDepth=%s",
                            keyPath, keyDepth_PBR)
                foundAtKeyDepth_PBR.setValue(keyDepth_PBR.value())
                return self
            for logFunc in self._log("find-blinky-node-querying-descendant").debug2Func():
                logFunc("find-blinky-node-querying-descendant: keyPath=%s, keyDepth=%s",
                        keyPath, keyDepth_PBR)
            keyDepth_PBR.setValue(keyDepth_PBR.value() + 1)
            return descendant.findBlinkyNode(keyPath, keyDepth_PBR, foundAtKeyDepth_PBR)
        else:
            foundAtKeyDepth_PBR.setValue(keyDepth_PBR.value())
            return self
        return None
    
    def internalPreparePrivateCreate(self):
        for logFunc in self._log("internal-prepare-private-create").debug2Func(): logFunc("internalPreparePrivateCreate() called")
        return self.notifyPhase(TrxPhase(TrxPhase.kPrepare, TrxPhase.kPrivate))
    
    def internalPreparePublicCreate(self):
        for logFunc in self._log("internal-prepare-public-create").debug2Func(): logFunc("internalPreparePublicCreate() called")
        return self.notifyPhase(TrxPhase(TrxPhase.kPrepare, TrxPhase.kPublic))
    
    def internalCommitBlinkyCreate(self):
        for logFunc in self._log("internal-commit-blinky-create").debug2Func(): logFunc("internalCommitBlinkyCreate() called")
        self.activateCandidate()
    
    def internalCommitPrivateCreate(self):
        for logFunc in self._log("internal-commit-private-create").debug2Func(): logFunc("internalCommitPrivateCreate() called")
        return self.notifyPhase(TrxPhase(TrxPhase.kCommit, TrxPhase.kPrivate))
    
    def internalCommitPublicCreate(self):
        for logFunc in self._log("internal-commit-public-create").debug2Func(): logFunc("internalCommitPublicCreate() called")
        self.notifyPhase(TrxPhase(TrxPhase.kCommit, TrxPhase.kPublic))
    
    def internalAbortPrivateCreate(self):
        for logFunc in self._log("internal-abort-private-create").debug2Func(): logFunc("internalAbortPrivateCreate() called")
        return self.notifyPhase(TrxPhase(TrxPhase.kAbort, TrxPhase.kPrivate))
    
    def internalAbortPublicCreate(self):
        for logFunc in self._log("internal-abort-public-create").debug2Func(): logFunc("internalAbortPublicCreate() called")
        return self.notifyPhase(TrxPhase(TrxPhase.kAbort, TrxPhase.kPublic))
    
    def notifyPhase(self, phase):
        for logFunc in self._log("notify-phase").debug2Func(): logFunc("notifyPhase() called, phase=%s, phaseDone=%s",
                                         phase, self.myState.isPhaseDone(phase))
        if (not self.myState.isPhaseDone(phase)):
            res = self.notifyWithCandidate(phase)
            if (res != ReturnCodes.kOk):
                if (phase.getConfdPhase() == TrxPhase.kPrepare):
                    for logFunc in self._log("notify-phase-call-functor-failed-prepare").noticeFunc():
                        logFunc("notifyPhase() call-functor-failed-prepare, phase=%s, res=%s", phase, res)
                else:
                    for logFunc in self._log("notify-phase-call-functor-failed").errorFunc():
                        logFunc("notifyPhase() call-functor-failed, phase=%s, res=%s", phase, res)
                return ReturnCodes.kGeneralError
            self.myState.setPhaseDone(phase)
        return ReturnCodes.kOk
    
    def deactivateSpecific(self):
        return ReturnCodes.kOk

