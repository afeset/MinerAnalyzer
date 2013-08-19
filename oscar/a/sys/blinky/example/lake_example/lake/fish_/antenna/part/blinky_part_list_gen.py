


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyContainer
__pychecker__="no-classattr"

from a.infra.basic.return_codes import ReturnCodes
import a.infra.process.captain
from a.infra.misc.timeout_guard import TimeoutGuard
from a.sys.blinky.blinky_list import BlinkyList
from a.sys.blinky.trx_element import TrxElement
from a.sys.blinky.trx_phase import TrxPhase
from a.sys.confd.pyconfdlib import pyconfdlib
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value

from a.sys.blinky.example.lake_example.lake.fish_.antenna.part.blinky_part_gen import BlinkyPart

class BlinkyPartList(BlinkyList):

    CREATE_FUNCTOR = 'CREATE_FUNCTOR'
    DELETE_FUNCTOR = 'DELETE_FUNCTOR'
    MOVE_AFTER_FUNCTOR = 'MOVE_AFTER_FUNCTOR'

    @classmethod
    def s_create(cls, logger, 
                 
                 
                 
                 fish_, 
                 lake, 
                 domain):

        __pychecker__="no-argsused" # cls is not used
        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("parts", "http://qwilt.com/model/lake-example", "lake-example"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("antenna", "http://qwilt.com/model/lake-example", "lake-example"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(fish_);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fish", "http://qwilt.com/model/lake-example", "lake-example"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(lake);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("lake", "http://qwilt.com/model/lake-example", "lake-example"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyPartList(logger)
        logger("s-create-key-path").debug3("confd_key=%s.", confd_key)
        newNode.setParent(None)
        newNode.setKeyPath(confd_key)
        newNode.setDomain(domain)
        res = newNode.internalInit()
        if res != ReturnCodes.kOk:
            logger("s-create-internal-init-failed").error("internalInit() failed.")
            return None
        logger("s-create-done").debug3("newNode=%s. newNode.id()=%s, newNode.getKeyPath().id=%s", newNode.getKeyPath(), id(newNode), id(newNode.getKeyPath()))
        return newNode

    def __init__ (self, logger):
        BlinkyList.__init__(self, logger)
        self.myCreateFunctor = None
        self.myDeleteFunctor = None
        
        self.myContainersMap = {}
        

    def __str__ (self):
        ret="{BlinkyPartList: self.myContainersMap=%s, BlinkyList=%s}" % \
            (self.myContainersMap, BlinkyList.__str__(self))
        return ret

    @classmethod    
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__ = "unusednames=cls"
        logger('is-key-path-registered-blinkypartlist').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am list of: from a.sys.blinky.example.lake_example.lake.fish_.antenna.part.blinky_part_gen import BlinkyPart', keyPath, keyDepth)
        keyPathRegistered = False
        if keyPath.getLen() > keyDepth+1:
            keyPathRegistered = BlinkyPart.isKeyPathRegistered(logger, keyPath, keyDepth+1)
        else:
            keyPathRegistered = True
        logger('is-key-path-registered-blinkypartlist-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am list of: from a.sys.blinky.example.lake_example.lake.fish_.antenna.part.blinky_part_gen import BlinkyPart', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def setCreateFunctor(self, functor):
        if self.myIsActive:
            for logFunc in self._log("set-create-functor-not-active").errorFunc(): logFunc("setCreateFunctor is illegal when blinky-part-list is active.")
        self.myCreateFunctor=functor

    def setDeleteFunctor(self, functor):
        if self.myIsActive:
            for logFunc in self._log("set-delete-functor-not-active").errorFunc(): logFunc("setDeleteFunctor is illegal when blinky-part-list is active.")
        self.myDeleteFunctor=functor

    

    def findBlinkyNode (self, keyPath, keyDepth_PBR, foundAtkeyDepth_PBR):
        for logFunc in self._log("find-blinky-node-details").debug1Func(): logFunc("findBlinkyNode() called. keyPath=%s, keyDepth=%s, foundAtKeyDepth=%s",
                                                     keyPath, keyDepth_PBR, foundAtkeyDepth_PBR)

        res = ReturnCodes.kOk
        keyRemainderLen = keyPath.getLen() - keyDepth_PBR.value()
        if keyRemainderLen<1:
            for logFunc in self._log("find-blinky-node-path-too-short").noticeFunc(): logFunc("findBlinkyNode(): key length too short. keyPath=%s, keyDepth=%s",
                                                                keyPath, keyDepth_PBR)
            errStr = "Cannot delete this configuration element"
            self.setConfigErrorStr(errStr)
            return None

        if keyRemainderLen==1:
            for logFunc in self._log("find-blinky-node-handle-blinky-part").debug1Func(): logFunc("findBlinkyNode(): handling BlinkyPartList. keyPath=%s, keyDepth=%s",
                                                         keyPath, keyDepth_PBR)
            foundAtkeyDepth_PBR.setValue(keyDepth_PBR.value())
            return self

        if keyRemainderLen>1:
            val = keyPath.getAt(keyDepth_PBR.value())
        listKey=None
        listKey = val.asString()
        if res != ReturnCodes.kOk:
            return None
        for logFunc in self._log("find-blinky-node-getting-blinky-part").debug1Func(): logFunc("findBlinkyNode(): getting BlinkyPart. listKey=%s, self=%s", listKey, self)
        blinkyContainer = self.getBlinkyPart(listKey)
        if blinkyContainer==None:
            for logFunc in self._log("find-blinky-node-blinky-part-not-found").debug1Func(): logFunc("findBlinkyNode(): BlinkyPart not found. listKey=%s", listKey)
            foundAtkeyDepth_PBR.setValue(keyDepth_PBR.value())
            return self
        for logFunc in self._log("find-blinky-node-querying-blinky-part").debug1Func(): logFunc("findBlinkyNode(): querying BlinkyPart. keyPath=%s, keyDepth=%s, blinkyContainer=%s",
                                                           keyPath, keyDepth_PBR, blinkyContainer)
        keyDepth_PBR.setValue(keyDepth_PBR.value()+1)
        return blinkyContainer.findBlinkyNode(keyPath, keyDepth_PBR, foundAtkeyDepth_PBR)

        return None

    def getBlinkyPart(self, key):
        for logFunc in self._log("get-blinky-blinky-part").debug1Func(): logFunc("getBlinkyPart(): key=%s", key)
        keyString=str(key)
        if keyString in self.myContainersMap:
            return self.myContainersMap[keyString]
        else:
            return None

    def handleTrxPrepareBlinkyCreate(self, keyPath, listKey, blinkyContainer):
        for logFunc in self._log("handle-trx-prepare-blinky-create-details").debug1Func(): logFunc("handleTrxPrepareBlinkyCreate(): trx-details: keyPath=%s, listKey=%s, blinkyContainer=%s",
                                                                          keyPath, listKey, blinkyContainer)
        if blinkyContainer != None:
            for logFunc in self._log("handle-trx-prepare-blinky-create-already-exist").errorFunc(): logFunc("handleTrxPrepareBlinkyCreate(): already-exist: keyPath=%s, listKey=%s",
                                                                                   keyPath, listKey)
            return ReturnCodes.kGeneralError

        self.copyRunningToCandidate()
        newBlinkyNode=BlinkyPart(self._log)
        newBlinkyNode.setParent(self)
        newBlinkyNode.setKeyPath(keyPath)
        newBlinkyNode.setDomain(self.myDomain)

        res=newBlinkyNode.internalInit()
        if res != ReturnCodes.kOk:
            for logFunc in self._log("handle-trx-prepare-blinky-create-internal-init-failed").errorFunc(): logFunc("handleTrxPrepareBlinkyCreate(): internal-init-failed: keyPath=%s, listKey=%s",
                                                                                   keyPath, listKey)
            return ReturnCodes.kGeneralError

        nodes = self.myNodesToProgressNotification
        if self.myNotifyDescendantsModifications:
            nodes.append(self)
        newBlinkyNode.addNodesToProgressNotification(nodes)

        self.myContainersMap[str(listKey)] = newBlinkyNode
        

        for logFunc in self._log("handle-trx-prepare-blinky-create-added").debug4Func(): logFunc("handleTrxPrepareBlinkyCreate(): added. Now I am: %s", self)
        return ReturnCodes.kOk

    def removeByKey (self, listKey, blinkyToRemove):
        __pychecker__ = 'no-shadowbuiltin'
        for logFunc in self._log("remove-by-key").debug1Func(): logFunc("removeByKey(): details: listKey=%s, blinkyToRemove=%s",
                                          listKey, blinkyToRemove)

        keyString=str(listKey)
        if keyString not in self.myContainersMap:
            for logFunc in self._log("remove-by-key-not-found").errorFunc(): logFunc("key not found. listKey=%s, blinkyToRemove=%s",
                                              listKey, blinkyToRemove)
            return ReturnCodes.kGeneralError

        

        del self.myContainersMap[keyString]
        return ReturnCodes.kOk

    def handleTrxAbortBlinkyCreate(self, keyPath, listKey, blinkyContainer):
        for logFunc in self._log("handle-trx-abort-blinky-create-details").debug1Func(): logFunc("handleTrxAbortBlinkyCreate(): trx-details: keyPath=%s, listKey=%s, blinkyContainer=%s",
                                                                   keyPath, listKey, blinkyContainer)
        if blinkyContainer == None:
            for logFunc in self._log("handle-trx-abort-blinky-create-doesnt-exist").errorFunc(): logFunc("handleTrxAbortBlinkyCreate(): doesnt-exist: keyPath=%s, listKey=%s",
                                                                           keyPath, listKey)
            a.infra.process.processFatal("abort blinky create - item deosn't exist" )

        phase = TrxPhase(TrxPhase.kAbort, TrxPhase.kBlinky)
        res = blinkyContainer.handleInternalDestroy(phase)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("handle-trx-abort-blinky-create-handle-internal-destroy-failed").errorFunc(): logFunc("handleInternalDestroy() failed: keyPath=%s, listKey=%s, phase=%s",
                      keyPath, listKey, phase)
            a.infra.process.processFatal("abort blinky create failed - blinkyContainer.handleInternalDestroy(%s)", phase)

        res = self.removeByKey(listKey, blinkyContainer)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("handle-trx-abort-blinky-create-remove-by-key-failed").errorFunc(): logFunc("removeByKey() failed: keyPath=%s, listKey=%s",
                                                                           keyPath, listKey)
            a.infra.process.processFatal("abort blinky create - remove by key failed" )

        return ReturnCodes.kOk

    def activateCreateFunctor(self, phase, listKey, blinkyContainer):
        for logFunc in self._log("activate-create-functor-details").debug1Func(): logFunc("activateCreateFunctor(): trx-details: phase=%s, listKey=%s, blinkyContainer=%s",
                                                            phase, listKey, blinkyContainer)
        if self.myIsActive:
            if self.myCreateFunctor:
                timeoutGuard = TimeoutGuard(self._log, '%s-create-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.CREATE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.CREATE_FUNCTOR, phase))
                try:
                    res=self.myCreateFunctor(phase, listKey, blinkyContainer)
                except:
                    for logFunc in self._log("activate-create-functot-functor-exception").exceptionFunc():
                        logFunc("functor raised an exception. phase=%s, key=%s, blinkyContainer=%s", phase, listKey, blinkyContainer)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateFunctor.__name__)
                if res != ReturnCodes.kOk:
                    if phase.getConfdPhase() == TrxPhase.kPrepare:
                        for logFunc in self._log("activate-create-functor-functor-failed-prepare").noticeFunc(): logFunc("activateCreateFunctor(): functor failed during prepare: phase=%s, listKey=%s",
                                                                                            phase, listKey)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-create-functor-functor-failed").errorFunc(): logFunc("activateCreateFunctor(): functor failed: phase=%s, listKey=%s",
                                                                                    phase, listKey)
                    return ReturnCodes.kGeneralError

        self.myState.setPhaseDone(phase)
        return ReturnCodes.kOk

    def activateDeleteFunctor(self, phase, listKey):
        for logFunc in self._log("activate-delete-functor-details").debug1Func(): logFunc("activateDeleteFunctor(): details: phase=%s, listKey=%s",
                                                            phase, listKey)
        if self.myIsActive:
            if self.myDeleteFunctor:
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.DELETE_FUNCTOR, phase))
                try:
                    res=self.myDeleteFunctor(phase, listKey)
                except:
                    for logFunc in self._log("activate-delete-functor-functor-exception").exceptionFunc():
                        logFunc("functor raised an exception. phase=%s, key=%s", phase, listKey)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteFunctor.__name__)
                if res != ReturnCodes.kOk:
                    if phase.getConfdPhase() == TrxPhase.kPrepare:
                        for logFunc in self._log("activate-delete-functor-functor-failed-prepare").noticeFunc(): logFunc("activateDeleteFunctor(): functor failed during prepare: phase=%s, listKey=%s",
                                                                                            phase, listKey)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-functor-functor-failed").errorFunc(): logFunc("activateDeleteFunctor(): functor failed: phase=%s, listKey=%s",
                                                                                    phase, listKey)
                    return ReturnCodes.kGeneralError

        self.myState.setPhaseDone(phase)
        return ReturnCodes.kOk

    

    def handleTrxPreparePrivateCreate(self, listKey, blinkyContainer):
        for logFunc in self._log("handle-trx-prepare-private-create-details").debug1Func(): logFunc("handleTrxPreparePrivateCreate(): details: listKey=%s, blinkyContainer=%s",
                                                                      listKey, blinkyContainer)
        res=self.activateCreateFunctor(TrxPhase(TrxPhase.kPrepare, TrxPhase.kPrivate), listKey, blinkyContainer)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("handle-trx-prepare-private-create-activate-functor-failed").noticeFunc(): logFunc("handleTrxPreparePrivateCreate(): functor failed: listKey=%s",
                                                                                          listKey)
            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
            return ReturnCodes.kGeneralError

        res = blinkyContainer.internalPreparePrivateCreate()
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-prepare-private-create-internal-prepare-private-create-failed").noticeFunc(): logFunc("handleTrxPreparePrivateCreate(): internalPreparePrivateCreate failed. listKey=%s",
                                                                                                         listKey)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def handleTrxAbortPrivateCreate(self, listKey, blinkyContainer):
        for logFunc in self._log("handle-trx-abort-private-create-details").debug1Func(): logFunc("handleTrxAbortPrivateCreate(): details: listKey=%s, blinkyContainer=%s",
                                                                      listKey, blinkyContainer)
        res = blinkyContainer.internalAbortPrivateCreate()
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-abort-private-create-internal-abort-failed").errorFunc(): logFunc("handleTrxAbortPrivateCreate(): internalAbortPrivateCreate failed. listKey=%s",
                                                                                     listKey)
            a.infra.process.processFatal("abort private create failed - blinkyContainer.internalAbortPrivateCreate()" )
    
        phase = TrxPhase(TrxPhase.kAbort, TrxPhase.kPrivate)
        res = blinkyContainer.handleInternalDestroy(phase)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("handle-trx-abort-private-create-handle-internal-destroy-failed").errorFunc(): logFunc("handleInternalDestroy() failed: listKey=%s, phase=%s",
                      listKey, phase)
            a.infra.process.processFatal("abort private create failed - blinkyContainer.handleInternalDestroy(%s)" % phase )

        res = self.activateCreateFunctor(phase, listKey, blinkyContainer)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-abort-private-create-functor-failed").errorFunc(): logFunc("handleTrxAbortPrivateCreate(): functor failed. listKey=%s",
                                                                              listKey)
            a.infra.process.processFatal("abort private create - functor failed" )

        return ReturnCodes.kOk

    def handleTrxPreparePublicCreate(self, listKey, blinkyContainer):
        for logFunc in self._log("handle-trx-prepare-public-create-details").debug1Func(): logFunc("handleTrxPreparePublicCreate(): details: listKey=%s, blinkyContainer=%s",
                                                                      listKey, blinkyContainer)

        res = self.activateCreateFunctor(TrxPhase(TrxPhase.kPrepare, TrxPhase.kPublic), listKey, blinkyContainer)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-prepare-public-create-functor-failed").noticeFunc(): logFunc("handleTrxPreparePublicCreate(): functor failed: listKey=%s",
                                                                                listKey)
            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
            return ReturnCodes.kGeneralError

        res = blinkyContainer.internalPreparePublicCreate()
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-prepare-public-create-internal-abort-failed").noticeFunc(): logFunc("handleTrxPreparePublicCreate(): internalPreparePublicCreate() failed: listKey=%s",
                                                                                       listKey)
            return ReturnCodes.kOk

        return ReturnCodes.kOk

    def handleTrxAbortPublicCreate(self, listKey, blinkyContainer):
        for logFunc in self._log("handle-trx-abort-public-create-details").debug1Func(): logFunc("handleTrxAbortPublicCreate(): details: listKey=%s, blinkyContainer=%s",
                                                                      listKey, blinkyContainer)
        res = blinkyContainer.internalAbortPublicCreate()
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-abort-public-create-internal-abort-failed").errorFunc(): logFunc("handleTrxAbortPublicCreate(): internalAbortPublicCreate: listKey=%s",
                                                                                    listKey)
            a.infra.process.processFatal("abort public create failed - blinkyContainer.internalAbortPublicCreate()" )

        phase = TrxPhase(TrxPhase.kAbort, TrxPhase.kPublic)
        res = blinkyContainer.handleInternalDestroy(phase)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("handle-trx-abort-public-create-handle-internal-destroy-failed").errorFunc(): logFunc("handleInternalDestroy() failed: listKey=%s, phase=%s",
                      listKey, phase)
            a.infra.process.processFatal("abort public create failed - blinkyContainer.handleInternalDestroy(%s)" % phase )

        res = self.activateCreateFunctor(phase, listKey, blinkyContainer)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-abort-public-create-functor-failed").errorFunc(): logFunc("handleTrxAbortPublicCreate(): activateCreateFunctor failed: listKey=%s",
                                                                             listKey)
            a.infra.process.processFatal("abort public create failed - activateCreateFunctor()" )
    
        return ReturnCodes.kOk

    def handleTrxCommitBlinkyCreate(self, listKey, blinkyContainer):
        for logFunc in self._log("handle-trx-commit-blinky-create-details").debug1Func(): logFunc("handleTrxCommitBlinkyCreate(): trx-details: listKey=%s, blinkyContainer=%s",
                                                                   listKey, blinkyContainer)
        self.activateCandidate()
        blinkyContainer.internalCommitBlinkyCreate();
        return ReturnCodes.kOk

    def handleTrxCommitPrivateCreate(self, listKey, blinkyContainer):
        for logFunc in self._log("handle-trx-commit-private-create-details").debug1Func(): logFunc("handleTrxCommitPrivateCreate(): trx-details: listKey=%s, blinkyContainer=%s",
                                                                   listKey, blinkyContainer)
    
        res = self.activateCreateFunctor(TrxPhase(TrxPhase.kCommit, TrxPhase.kPrivate), listKey, blinkyContainer)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-commit-private-create-functor-failed").errorFunc(): logFunc("handleTrxCommitPrivateCreate(): trx-details: listKey=%s",
                                                                               listKey)
            a.infra.process.processFatal("commit private create failed" )
            return ReturnCodes.kGeneralError
    
        blinkyContainer.internalCommitPrivateCreate()
    
        return ReturnCodes.kOk

    def handleTrxCommitPublicCreate(self, listKey, blinkyContainer):
        for logFunc in self._log("handle-trx-commit-public-create-details").debug1Func(): logFunc("handleTrxCommitPublicCreate(): trx-details: listKey=%s, blinkyContainer=%s",
                                                                   listKey, blinkyContainer)
    
        res = self.activateCreateFunctor(TrxPhase(TrxPhase.kCommit, TrxPhase.kPublic), listKey, blinkyContainer)
        if (res != ReturnCodes.kOk):
            for logFunc in self._log("handle-trx-commit-public-create-functor-failed").errorFunc(): logFunc("handleTrxCommitPublicCreate(): functor failed: listKey=%s",
                                                                              listKey)
            a.infra.process.processFatal("commit public create failed" )
            return ReturnCodes.kGeneralError
    
        blinkyContainer.internalCommitPublicCreate()
    
        return ReturnCodes.kOk

    

    def notifyDescendantsPrepareBlinkyDelete(self):
        for logFunc in self._log("notify-descendants-prepare-blinky-delete-called").debug2Func(): logFunc("called")

        self.myDomain.registerNodeToProgressNotification(self)

        for childKey, child in self.myContainersMap.iteritems():
            child.notifyDescendantsPrepareBlinkyDelete()

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def trxElementHelper(self, trxElement, keyDepth, phase):

        __pychecker__="maxreturns=50 maxlines=500" # This function has a lot of return statements

        for logFunc in self._log("trx-element-helper-details").debug1Func(): logFunc("trxElementHelper(): trx-details: phase=%s, trxElement=%s, keyDepth=%s", phase, trxElement, keyDepth)
        keyPath = trxElement.getKeyPath()
        keyRemainderLen = keyPath.getLen() - keyDepth
        if (keyRemainderLen != 1):
            for logFunc in self._log("trx-element-helper-bad-path-len").errorFunc(): logFunc("trxElementHelper(): bad key path length: keyPath=%s, keyDepth=%s", keyPath, keyDepth)
            return ReturnCodes.kGeneralError
    
        res = ReturnCodes.kOk
        val = keyPath.getAt(keyDepth)
        listKey=None
        listKey = val.asString()
        if res != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError
        blinkyContainer = self.getBlinkyPart(listKey)
        if (blinkyContainer == None):
            if (not ((phase.getConfdPhase() == TrxPhase.kPrepare) and (phase.getBlinkyPhase() == TrxPhase.kBlinky)) ):
                for logFunc in self._log("trx-element-helper-blinky-part-not-exist").errorFunc(): logFunc("trxElementHelper(): BlinkyPart-not-exist: phase=%s, listKey=%s", phase, listKey)
                return ReturnCodes.kGeneralError
    
        res = ReturnCodes.kOk
        if trxElement.getOpCode() == TrxElement.kCreate:
            if phase.getConfdPhase() == TrxPhase.kPrepare:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxPrepareBlinkyCreate(keyPath, listKey, blinkyContainer)
                elif phase.getBlinkyPhase() == TrxPhase.kPrivate:
                    res = self.handleTrxPreparePrivateCreate(listKey, blinkyContainer)
                elif phase.getBlinkyPhase() == TrxPhase.kPublic:
                    res = self.handleTrxPreparePublicCreate(listKey, blinkyContainer)
                else:
                    for logFunc in self._log("trx-element-helper-prepare-illegal-blinky").errorFunc(): logFunc("trxElementHelper(): prepare - illegal blinky phase: phase=%s, listKey=%s", phase, listKey)
                    a.infra.process.processFatal("trxElementHelper():  prepare - illegal blinky phase %s" % phase )
                    return ReturnCodes.kGeneralError

                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("trx-element-helper-prepare-create-handle-failed").noticeFunc(): logFunc("trxElementHelper(): prepare-create-handle-failed - phase=%s, keyPath=%s, keyDepth=%s, listKey=%s",
                                                                                        phase, keyPath, keyDepth, listKey)
                    return ReturnCodes.kGeneralError

            elif phase.getConfdPhase() == TrxPhase.kCommit:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxCommitBlinkyCreate(listKey, blinkyContainer)
                elif phase.getBlinkyPhase() == TrxPhase.kPrivate:
                    res = self.handleTrxCommitPrivateCreate(listKey, blinkyContainer)
                elif phase.getBlinkyPhase() == TrxPhase.kPublic:
                    res = self.handleTrxCommitPublicCreate(listKey, blinkyContainer)
                else:
                    for logFunc in self._log("trx-element-helper-commit-illegal-blinky").errorFunc(): logFunc("trxElementHelper(): commit - illegal blinky phase: phase=%s, listKey=%s", phase, listKey)
                    a.infra.process.processFatal("trxElementHelper():  commit - illegal blinky phase %s" % phase )
                    return ReturnCodes.kGeneralError

            elif phase.getConfdPhase() == TrxPhase.kAbort:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = self.handleTrxAbortBlinkyCreate(keyPath, listKey, blinkyContainer)
                    self.deleteMyCandidate()
                elif phase.getBlinkyPhase() == TrxPhase.kPrivate:
                    res = self.handleTrxAbortPrivateCreate(listKey, blinkyContainer)
                elif phase.getBlinkyPhase() == TrxPhase.kPublic:
                    res = self.handleTrxAbortPublicCreate(listKey, blinkyContainer)
                else:
                    for logFunc in self._log("trx-element-helper-abort-illegal-blinky").errorFunc(): logFunc("trxElementHelper(): abort - illegal blinky phase: phase=%s, listKey=%s", phase, listKey)
                    a.infra.process.processFatal("trxElementHelper():  abort - illegal blinky phase %s" % phase )
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("trx-element-helper-abort-illegal-confd").errorFunc(): logFunc("trxElementHelper(): abort - illegal confd phase: phase=%s, listKey=%s", phase, listKey)
                a.infra.process.processFatal("trxElementHelper():  prepare - illegal confd phase %s" % phase )
                return ReturnCodes.kGeneralError

            if (res != ReturnCodes.kOk):
                for logFunc in self._log("trx-element-helper-create-handle-failed").errorFunc(): logFunc("trxElementHelper(): create-handle-failed: phase=%s, keyPath=%s, keyDepth=%s, listKey=%s",
                                                                           phase, keyPath, keyDepth, listKey)
                return ReturnCodes.kGeneralError

        elif trxElement.getOpCode() == TrxElement.kDelete:
            if (blinkyContainer == None):
                for logFunc in self._log("trx-element-helper-delete-no-entry").errorFunc(): logFunc("trxElementHelper(): delete-no-entry: phase=%s, keyPath=%s, keyDepth=%s, listKey=%s",
                                                                           phase, keyPath, keyDepth, listKey)
                return ReturnCodes.kGeneralError

            if phase.getConfdPhase() == TrxPhase.kPrepare:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    self.copyRunningToCandidate()
                    blinkyContainer.notifyDescendantsPrepareBlinkyDelete()
                    res = blinkyContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("trx-element-helper-delete-prepare-blinky-internal-destroy-failed").errorFunc(): logFunc("trxElementHelper(): delete prepare blinky - internalDestroy failed: keyPath=%s, listKey=%s",
                                                                                                            keyPath, listKey)
                        return ReturnCodes.kGeneralError
                elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                     (phase.getBlinkyPhase() == TrxPhase.kPublic):
                    res = self.activateDeleteFunctor(phase, listKey)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("trx-element-helper-delete-prepare-private-public-functor-failed").errorFunc(): logFunc("trxElementHelper(): delete prepare private-public - activateFunctor failed: phase=%s, keyPath=%s, listKey=%s",
                                                                                                           phase, keyPath, listKey)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                    res = blinkyContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("trx-element-helper-delete-prepare-private-public-internal-destroy-failed").errorFunc(): logFunc("trxElementHelper(): delete prepare blinky - internalDestroy failed: phase=%s, keyPath=%s, listKey=%s",
                                                                                                           phase, keyPath, listKey)
                        return ReturnCodes.kGeneralError
                else:
                    for logFunc in self._log("trx-element-helper-delete-prepare-illegal-blinky-phase").errorFunc(): logFunc("trxElementHelper(): delete prepare blinky - illegal blinky phase: phase=%s, keyPath=%s, listKey=%s",
                                                                                              phase, keyPath, listKey)
                    return ReturnCodes.kGeneralError

            elif phase.getConfdPhase() == TrxPhase.kCommit:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = blinkyContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("trx-element-helper-delete-commit-blinky-internal-destroy-failed").errorFunc(): logFunc("trxElementHelper(): delete commit blinky - internalDestroy failed: phase=%s, keyPath=%s, listKey=%s",
                                                                                                  phase, keyPath, listKey)
                        return ReturnCodes.kGeneralError
                    res = self.removeByKey(listKey, blinkyContainer)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("trx-element-helper-delete-commit-blinky-remove-by-key-failed").errorFunc(): logFunc("trxElementHelper(): removeByKey failed: phase=%s, keyPath=%s, listKey=%s",
                                                                                                        phase, keyPath, listKey)
                        return ReturnCodes.kGeneralError
                        self.activateCandidate()

                elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                     (phase.getBlinkyPhase() == TrxPhase.kPublic):
                    res = blinkyContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("trx-element-helper-delete-commit-private-public-internal-destroy-failed").errorFunc(): logFunc("trxElementHelper(): delete commit private-public - internalDestroy failed: phase=%s, keyPath=%s, listKey=%s",
                                                                                                  phase, keyPath, listKey)
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteFunctor(phase, listKey)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("trx-element-helper-delete-commit-private-public-functor-failed").errorFunc(): logFunc("trxElementHelper(): delete commit private-public - functor failed: phase=%s, keyPath=%s, listKey=%s",
                                                                                                  phase, keyPath, listKey)
                        a.infra.process.processFatal("trxElementHelper():  commit delete functor failed" )
                        return ReturnCodes.kGeneralError
                else:
                    for logFunc in self._log("trx-element-helper-delete-commit-illegal-blinky-phase").errorFunc(): logFunc("trxElementHelper(): delete commit blinky - illegal blinky phase: phase=%s, keyPath=%s, listKey=%s",
                                                                                              phase, keyPath, listKey)
                    return ReturnCodes.kGeneralError

            elif phase.getConfdPhase() == TrxPhase.kAbort:
                if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                    res = blinkyContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("trx-element-helper-delete-abort-blinky-internal-destroy-failed").errorFunc(): logFunc("trxElementHelper(): delete abort blinky - internalDestroy failed: phase=%s, keyPath=%s, listKey=%s",
                                                                                                  phase, keyPath, listKey)
                        return ReturnCodes.kGeneralError
                    self.deleteMyCandidate()

                elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                     (phase.getBlinkyPhase() == TrxPhase.kPublic):
                    res = blinkyContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("trx-element-helper-delete-abort-blinky-internal-destroy-failed").errorFunc(): logFunc("trxElementHelper(): delete abort blinky - internalDestroy failed: phase=%s, keyPath=%s, listKey=%s",
                                                                                                  phase, keyPath, listKey)
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteFunctor(phase, listKey)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("trx-element-helper-delete-abort-private-public-blinky-functor-failed").errorFunc(): logFunc("trxElementHelper(): delete abort private public - functor failed: phase=%s, keyPath=%s, listKey=%s",
                                                                                                  phase, keyPath, listKey)
                        a.infra.process.processFatal("trxElementHelper():  delete abort functor failed" )
                        return ReturnCodes.kGeneralError
                else:
                    for logFunc in self._log("trx-element-helper-delete-abort-illegal-blinky-phase").errorFunc(): logFunc("trxElementHelper(): delete abort blinky - illegal blinky phase: phase=%s, keyPath=%s, listKey=%s",
                                                                                              phase, keyPath, listKey)
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("trx-element-helper-delete-illegal-confd-phase").errorFunc(): logFunc("trxElementHelper(): delete - illegal confd phase: phase=%s, keyPath=%s, listKey=%s",
                                                                                          phase, keyPath, listKey)
                return ReturnCodes.kGeneralError

        
        else:
            for logFunc in self._log("trx-element-helper-illegal-op-code").errorFunc(): logFunc("trxElementHelper(): illegal op code: trxElement=%s, keyPath=%s, listKey=%s",
                                                                  trxElement, keyPath, listKey)
            return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug2Func(): logFunc("getDescendant() called: keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        res = ReturnCodes.kOk
        val = keyPath.getAt(keyDepth_PBR.value())
        listKey=None
        listKey = val.asString()
        if res != ReturnCodes.kOk:
            return None
        descendant = self.getBlinkyPart(listKey)
        return descendant


    def handleInternalDestroy(self, phase):
        for logFunc in self._log("internal-prepare-destroy-helper").debug1Func(): logFunc("handleInternalDestroy() called, phase=%s", phase)
        res = ReturnCodes.kOk
        if phase.getConfdPhase() == TrxPhase.kPrepare:
            if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                self.copyRunningToCandidate()
                for childKey, child in self.myContainersMap.iteritems():
                    for logFunc in self._log("handle-internal-destroy-iterating-prepare-blinky").debug2Func(): logFunc("handleInternalDestroy - iterating children, childKey=%s, phase=%s", childKey, phase)
                    res = child.handleInternalDestroy(phase)
                    if res != ReturnCodes.kOk:
                        for logFunc in self._log("handle-internal-destroy-prepare-blinky-child-failed").errorFunc(): logFunc("handleInternalDestroy - child.handleInternalDestroy, childKey=%s, phase=%s", childKey, phase)
                        return ReturnCodes.kGeneralError
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-prepare-blinky-destroy-self-functor-failed").errorFunc(): logFunc("handleInternalDestroy - destroySelfFunctor failed, myKeyPath=%s, phase=%s",
                                                                                                          self.myKeyPath(), phase)
                    self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    return ReturnCodes.kGeneralError
                for childKey, child in self.myContainersMap.iteritems():
                    for logFunc in self._log("handle-internal-destroy-iterating-prepare-private-public").debug2Func(): logFunc("handleInternalDestroy - iterating children, childKey=%s, phase=%s", childKey, phase)
                    res = self.activateDeleteFunctor(phase, childKey)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-prepare-blinky-functor-failed").noticeFunc(): logFunc("handleInternalDestroy - functor failed, childKey=%s, phase=%s", childKey, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                    res = child.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-prepare-child-failed").errorFunc(): logFunc("handleInternalDestroy - child.handleInternalDestroy() failed, childKey=%s, phase=%s", childKey, phase)
                        return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("handle-internal-destroy-prepare-illegal-blinky").errorFunc(): logFunc("handleInternalDestroy - illegal blinky phase, myKeyPath=%s, phase=%s", self.myKeyPath, phase)
                return ReturnCodes.kGeneralError

        elif phase.getConfdPhase() == TrxPhase.kCommit:
            if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                # Use keys() to allow changing the dictionary during iteration
                while len(self.myContainersMap):
                    childKey = self.myContainersMap.keys()[0]
                    for logFunc in self._log("handle-internal-destroy-iterating-commit-blinky").debug2Func(): logFunc("handleInternalDestroy - iterating children, childKey=%s, phase=%s", childKey, phase)
                    res = self.myContainersMap[childKey].handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-commit-blinky-child-failed").errorFunc(): logFunc("handleInternalDestroy - child->internalDestroy() failed, childKey=%s, phase=%s", childKey, phase)
                        return ReturnCodes.kGeneralError
                    del self.myContainersMap[childKey]
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                while len(self.myContainersMap):
                    childKey, child = self.myContainersMap.iteritems().next()
                    for logFunc in self._log("handle-internal-destroy-iterating-commit-private-public").debug2Func(): logFunc("handleInternalDestroy - iterating children, childKey=%s, phase=%s", childKey, phase)
                    res = child.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-commit-private-public-child-failed").errorFunc(): logFunc("handleInternalDestroy - child.handleInternalDestroy() failed, childKey=%s, phase=%s", childKey, phase)
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteFunctor(phase, child.getKeyPath())
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-commit-private-public-functor-failed").errorFunc(): logFunc("handleInternalDestroy - functor failed, childKey=%s, phase=%s", childKey, phase)
                        a.infra.process.processFatal("handleInternalDestroy():  delete commit functor failed" )
                        return ReturnCodes.kGeneralError
                    res = self.removeByKey(childKey, child)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-commit-private-public-remove-by-key-failed").errorFunc(): logFunc("handleInternalDestroy - removeByKey() failed, childKey=%s, phase=%s", childKey, phase)
                        return ReturnCodes.kGeneralError
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-commit-private-public-self-destroy-functor-failed").errorFunc(): logFunc("handleInternalDestroy - self-destroy-functor-failed, myKeyPath=%s, phase=%s", self.myKeyPath, phase)
                    a.infra.process.processFatal("handleInternalDestroy():  delete self destroy functor failed" )
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("handle-internal-destroy-commit-illegal-blinky").errorFunc(): logFunc("handleInternalDestroy - illegal blinky phase, myKeyPath=%s, phase=%s", self.myKeyPath, phase)
                return ReturnCodes.kGeneralError

        elif phase.getConfdPhase() == TrxPhase.kAbort:
            if phase.getBlinkyPhase() == TrxPhase.kBlinky:
                for childKey, child in self.myContainersMap.iteritems():
                    for logFunc in self._log("handle-internal-destroy-iterating-abort-blinky").debug2Func(): logFunc("handleInternalDestroy - abort, iterating children, childKey=%s, phase=%s", childKey, phase)
                    res = child.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-abort-blinky-child-failed").errorFunc(): logFunc("handleInternalDestroy - abort, child.handleInternalDestroy() failed, childKey=%s, phase=%s", childKey, phase)
                        return ReturnCodes.kGeneralError
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                for childKey, child in self.myContainersMap.iteritems():
                    for logFunc in self._log("handle-internal-destroy-iterating-abort-private-public").debug2Func(): logFunc("handleInternalDestroy - abort, iterating children, childKey=%s, phase=%s", childKey, phase)
                    res = child.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-abort-private-public-blinky").errorFunc(): logFunc("handleInternalDestroy - abort, child.handleInternalDestroy() failed, childKey=%s, phase=%s", childKey, phase)
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteFunctor(phase, child.getKeyPath())
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-abort-private-public-functor-failed").errorFunc(): logFunc("handleInternalDestroy - abort, functor failed, childKey=%s, phase=%s", childKey, phase)
                        return ReturnCodes.kGeneralError
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-abort-private-public").errorFunc(): logFunc("handleInternalDestroy - abort, self destroy functor failed, myKeyPath=%s, phase=%s", self.myKeyPath, phase)
                    a.infra.process.processFatal("handleInternalDestroy():  abort, destroySelf functor failed" )
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("handle-internal-destroy-abort-illegal-blinky").errorFunc(): logFunc("handleInternalDestroy - illegal blinky phase, myKeyPath=%s, phase=%s", self.myKeyPath, phase)
                return ReturnCodes.kGeneralError

        else:
            for logFunc in self._log("handle-internal-destroy-illegal-confd").errorFunc(): logFunc("handleInternalDestroy - illegal-confd phase, myKeyPath=%s, phase=%s", self.myKeyPath, phase)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk


    def allocMyCandidate (self):
        for logFunc in self._log("alloc-my-candidate").debug2Func(): logFunc("called")
        
        return ReturnCodes.kOk

    def deleteMyCandidate (self):
        for logFunc in self._log("delete-my-candidate").debug2Func(): logFunc("called")
        
        return ReturnCodes.kOk

    def activateCandidate (self):
        phase = TrxPhase(TrxPhase.kCommit, TrxPhase.kBlinky)
        for logFunc in self._log("activate-candidate").debug2Func(): logFunc("called: phaseDone=%s", self.myState.isPhaseDone(phase))
        if self.myState.isPhaseDone(phase):
            # running config already updated - skip
            return

        

        self.myState.setPhaseDone(phase)
        for logFunc in self._log("activate-candidate-done").debug2Func(): logFunc("done: phaseDone=%s", self.myState.isPhaseDone(phase))
        return ReturnCodes.kOk

    def copyRunningToCandidate (self):
        for logFunc in self._log("copy-running-to-candidate").debug2Func(): logFunc("called")
        

        


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyPart", 
        "containerLogGroupName": "blinky-part", 
        "namespace": "part", 
        "containerImportStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.part.blinky_part_gen import BlinkyPart", 
        "logGroupName": "blinky-part-list", 
        "className": "BlinkyPartList", 
        "logModuleName": "a-sys-blinky-example-lake-example-lake-fish--antenna-part-blinky-part-list-gen", 
        "keyLeaf": {
            "varName": "part", 
            "typeHandler": "handler: StringHandler"
        }
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "lake", 
            "namespace": "lake", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "lake", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lake"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "fish", 
            "namespace": "fish_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "fish_", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fish_"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "antenna", 
            "namespace": "antenna", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "antenna"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": true, 
            "yangName": "parts", 
            "namespace": "part", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "part", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "part"
        }
    ], 
    "orderedByUser": false, 
    "conditionalDebugName": null, 
    "leaves": null, 
    "module": {}, 
    "env": {}, 
    "createTime": "2013"
}
"""

