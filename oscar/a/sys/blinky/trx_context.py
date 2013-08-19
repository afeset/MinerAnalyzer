# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.basic.return_codes import ReturnCodes
from trx_phase import TrxPhase
from trx_progress import TrxProgress
from trx_element import TrxElement
from utils import Utils

import copy

class TrxContext(object):

    # From here on, TrxContext methods
    def __init__(self, logger):
        self._log=logger.createLogger("sys-blinky", "trx-context")
        self.myTrxElements=[]
        self.myStatus = ReturnCodes.kOk
        self.myErrorText = ""
        self.myTrxId=None
        self.myNodesToProgressNotification=[]
        self.myTrxPhase = None
        self.myPreparePassed=[ [False for x in range(TrxProgress.kProgressStagesLast.getValue())] for x in range(TrxPhase.kBlinkyLast.getValue()) ]

        self._opElements = {
            TrxElement.kValueSet : 0,
            TrxElement.kCreate : 0,
            TrxElement.kDelete : 0,
            TrxElement.kMovedAfter : 0
            }

    def __str__ (self):
        return "{TrxContext: myTrxId=%s, myTrxElements=[%s], myErrorText=%s}" % \
            (self.myTrxId, ",".join(map(str, self.myTrxElements)), self.myErrorText)

    def setTrxId(self, trxId):
        self.myTrxId = trxId.clone()

    def getTrxId(self):
        return self.myTrxId

    def getTrxElements(self):
        return self.myTrxElements

    def getTrxElementsNum (self):
        return len(self.myTrxElements)

    def getTrxValueSetElementsNum (self):
        return self._opElements[TrxElement.kValueSet]

    def getTrxCreateElementsNum (self):
        return self._opElements[TrxElement.kCreate]

    def getTrxDeleteElementsNum (self):
        return self._opElements[TrxElement.kDelete]

    def getTrxMovedAfterElementsNum (self):
        return self._opElements[TrxElement.kMovedAfter]

    def getErrorText(self):
        return self.myErrorText

    def setTrxPhase (self, trxPhase):
        self.myTrxPhase = copy.deepcopy(trxPhase)

    def getTrxPhase (self):
        return self.myTrxPhase

    def removeElementAt (self, index):
        for logFunc in self._log("remove-trx-element-at").debug3Func(): logFunc("removing transaction element in: %d.", index)
        if index >= len(self.myTrxElements):
            for logFunc in self._log('remove-trx-element-bad-index').errorFunc(): logFunc("bad index: %d. there are only %d elements",
                                                            index, len(self.myTrxElements))
            return ReturnCodes.kGeneralError
        self._opElements[self.myTrxElements[index].getOpCode()] -= 1
        del self.myTrxElements[index]
        return ReturnCodes.kOk

    def addTrxElement(self, trxElement):
        for logFunc in self._log("add-trx-element").debug4Func(): logFunc("adding element '%s' to this: '%s'.", trxElement, self)
        self.myTrxElements.append(trxElement)
        self._opElements[trxElement.getOpCode()] += 1

    def insertTrxElement (self, trxElement, index):
        for logFunc in self._log("insert-trx-element").debug4Func(): logFunc("inserting element[%d] '%s' to this: '%s'.", index, trxElement, self)
        self.myTrxElements.insert(index, trxElement)
        self._opElements[trxElement.getOpCode()] += 1

    def registerNodeToProgressNotification (self, node):
        for logFunc in self._log("register-node-to-progress-notification").debug4Func(): logFunc("node: %s.", node)
        if node in self.myNodesToProgressNotification:
            for logFunc in self._log("register-node-to-progress-notification-skipping").debug4Func(): logFunc("skipping registration - node is already registered: %s.", node)
        else:
            for logFunc in self._log("register-node-to-progress-notification-registering").debug3Func(): logFunc("registering node: %s.", node)
            self.myNodesToProgressNotification.append(node)

    def getNodesToProgressNotification (self):
        for logFunc in self._log("get-nodes-to-ptogress-notification").debug3Func(): logFunc("getNodesToProgressNotification() called")
        return self.myNodesToProgressNotification

    def setPreparePassedOn (self, progress):
        for logFunc in self._log("set-prepare-passed-on-keypath").debug3Func(): logFunc("current=%s", progress)
        if progress.getProgressStage() >= progress.kProgressStagesLast:
            for logFunc in self._log("set-prepare-passed-on-illegal-stage").errorFunc(): logFunc("illegal progress stage=%s", progress.getProgressStage())
            return
        if progress.myTrxPhase.getBlinkyPhase() >= progress.myTrxPhase.kBlinkyLast:
            for logFunc in self._log("set-prepare-passed-on-illegal-phase").errorFunc(): logFunc("illegal blinky phase=%s", progress.myTrxPhase.getBlinkyPhase())
            return
        self.myPreparePassed[progress.myTrxPhase.getBlinkyPhase().getValue()][progress.getProgressStage().getValue()] = True

    def hasPreparePassed (self, progress):
        for logFunc in self._log("has-prepare-passed-keypath").debug3Func(): logFunc("current=%s", progress)
        if progress.getProgressStage() >= progress.kProgressStagesLast:
            for logFunc in self._log("has-prepare-passed-keypath-stage").errorFunc(): logFunc("illegal progress stage=%s", progress.getProgressStage())
            return
        if progress.myTrxPhase.getBlinkyPhase() >= progress.myTrxPhase.kBlinkyLast:
            for logFunc in self._log("has-prepare-passed-keypath-illegal-phase").errorFunc(): logFunc("illegal blinky phase=%s", progress.myTrxPhase.getBlinkyPhase())
            return
        return self.myPreparePassed[progress.myTrxPhase.getBlinkyPhase().getValue()][progress.getProgressStage().getValue()]


    def simpleUpdate(self, simpleTrxContext):
        if (simpleTrxContext.getStatus() != ReturnCodes.kOk):
            self.myStatus = simpleTrxContext.getStatus()
            self.myErrorText = self.myErrorText+simpleTrxContext.getErrorText()
        return ReturnCodes.kOk

    def logDetailed (self, logFuncIn):
        for logFunc in self._log("log-detailed-num").debug3Func(): logFunc("numOfElements=%d", len(self.myTrxElements))
        if logFuncIn:
            logFuncIn("numOfElements=%d", len(self.myTrxElements))
            for i, element in enumerate(self.myTrxElements):
                logFuncIn("i=%d, element=%s", i, element)


