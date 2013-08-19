


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from counters_maapi_base_gen import CountersMaapiBase




class BlinkyCountersMaapi(CountersMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-counters")
        self.domain = None

        

        
        self.hwRscFlushedRequested = False
        self.hwRscFlushed = None
        self.hwRscFlushedSet = False
        
        self.lscIntRequested = False
        self.lscInt = None
        self.lscIntSet = False
        
        self.hwRscAggregatedRequested = False
        self.hwRscAggregated = None
        self.hwRscAggregatedSet = False
        
        self.rxLongLengthErrorsRequested = False
        self.rxLongLengthErrors = None
        self.rxLongLengthErrorsSet = False
        
        self.fdirMatchRequested = False
        self.fdirMatch = None
        self.fdirMatchSet = False
        
        self.txFcoePacketsRequested = False
        self.txFcoePackets = None
        self.txFcoePacketsSet = False
        
        self.rxShortLengthErrorsRequested = False
        self.rxShortLengthErrors = None
        self.rxShortLengthErrorsSet = False
        
        self.rxFcoeDwordsRequested = False
        self.rxFcoeDwords = None
        self.rxFcoeDwordsSet = False
        
        self.rxBytesNicRequested = False
        self.rxBytesNic = None
        self.rxBytesNicSet = False
        
        self.rxFcoePacketsRequested = False
        self.rxFcoePackets = None
        self.rxFcoePacketsSet = False
        
        self.txFcoeDwordsRequested = False
        self.txFcoeDwords = None
        self.txFcoeDwordsSet = False
        
        self.rxNoBufferCountRequested = False
        self.rxNoBufferCount = None
        self.rxNoBufferCountSet = False
        
        self.rxFifoErrorsRequested = False
        self.rxFifoErrors = None
        self.rxFifoErrorsSet = False
        
        self.allocRxPageFailedRequested = False
        self.allocRxPageFailed = None
        self.allocRxPageFailedSet = False
        
        self.txBusyRequested = False
        self.txBusy = None
        self.txBusySet = False
        
        self.txAbortedErrorsRequested = False
        self.txAbortedErrors = None
        self.txAbortedErrorsSet = False
        
        self.collisionsRequested = False
        self.collisions = None
        self.collisionsSet = False
        
        self.txHeartbeatErrorsRequested = False
        self.txHeartbeatErrors = None
        self.txHeartbeatErrorsSet = False
        
        self.rxMissedErrorsRequested = False
        self.rxMissedErrors = None
        self.rxMissedErrorsSet = False
        
        self.nonEopDescsRequested = False
        self.nonEopDescs = None
        self.nonEopDescsSet = False
        
        self.txFlowControlXonRequested = False
        self.txFlowControlXon = None
        self.txFlowControlXonSet = False
        
        self.rxCsumOffloadErrorsRequested = False
        self.rxCsumOffloadErrors = None
        self.rxCsumOffloadErrorsSet = False
        
        self.rxCrcErrorsRequested = False
        self.rxCrcErrors = None
        self.rxCrcErrorsSet = False
        
        self.txFifoErrorsRequested = False
        self.txFifoErrors = None
        self.txFifoErrorsSet = False
        
        self.txPktsNicRequested = False
        self.txPktsNic = None
        self.txPktsNicSet = False
        
        self.rxFcoeDroppedRequested = False
        self.rxFcoeDropped = None
        self.rxFcoeDroppedSet = False
        
        self.txBytesNicRequested = False
        self.txBytesNic = None
        self.txBytesNicSet = False
        
        self.allocRxBuffFailedRequested = False
        self.allocRxBuffFailed = None
        self.allocRxBuffFailedSet = False
        
        self.fcoeBadFccrcRequested = False
        self.fcoeBadFccrc = None
        self.fcoeBadFccrcSet = False
        
        self.txFlowControlXoffRequested = False
        self.txFlowControlXoff = None
        self.txFlowControlXoffSet = False
        
        self.txTimeoutCountRequested = False
        self.txTimeoutCount = None
        self.txTimeoutCountSet = False
        
        self.txCarrierErrorsRequested = False
        self.txCarrierErrors = None
        self.txCarrierErrorsSet = False
        
        self.rxFlowControlXoffRequested = False
        self.rxFlowControlXoff = None
        self.rxFlowControlXoffSet = False
        
        self.fdirMissRequested = False
        self.fdirMiss = None
        self.fdirMissSet = False
        
        self.rxNoDmaResourcesRequested = False
        self.rxNoDmaResources = None
        self.rxNoDmaResourcesSet = False
        
        self.rxOverErrorsRequested = False
        self.rxOverErrors = None
        self.rxOverErrorsSet = False
        
        self.rxFlowControlXonRequested = False
        self.rxFlowControlXon = None
        self.rxFlowControlXonSet = False
        
        self.txRestartQueueRequested = False
        self.txRestartQueue = None
        self.txRestartQueueSet = False
        
        self.rxFrameErrorsRequested = False
        self.rxFrameErrors = None
        self.rxFrameErrorsSet = False
        
        self.rxPktsNicRequested = False
        self.rxPktsNic = None
        self.rxPktsNicSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestHwRscFlushed(True)
        
        self.requestLscInt(True)
        
        self.requestHwRscAggregated(True)
        
        self.requestRxLongLengthErrors(True)
        
        self.requestFdirMatch(True)
        
        self.requestTxFcoePackets(True)
        
        self.requestRxShortLengthErrors(True)
        
        self.requestRxFcoeDwords(True)
        
        self.requestRxBytesNic(True)
        
        self.requestRxFcoePackets(True)
        
        self.requestTxFcoeDwords(True)
        
        self.requestRxNoBufferCount(True)
        
        self.requestRxFifoErrors(True)
        
        self.requestAllocRxPageFailed(True)
        
        self.requestTxBusy(True)
        
        self.requestTxAbortedErrors(True)
        
        self.requestCollisions(True)
        
        self.requestTxHeartbeatErrors(True)
        
        self.requestRxMissedErrors(True)
        
        self.requestNonEopDescs(True)
        
        self.requestTxFlowControlXon(True)
        
        self.requestRxCsumOffloadErrors(True)
        
        self.requestRxCrcErrors(True)
        
        self.requestTxFifoErrors(True)
        
        self.requestTxPktsNic(True)
        
        self.requestRxFcoeDropped(True)
        
        self.requestTxBytesNic(True)
        
        self.requestAllocRxBuffFailed(True)
        
        self.requestFcoeBadFccrc(True)
        
        self.requestTxFlowControlXoff(True)
        
        self.requestTxTimeoutCount(True)
        
        self.requestTxCarrierErrors(True)
        
        self.requestRxFlowControlXoff(True)
        
        self.requestFdirMiss(True)
        
        self.requestRxNoDmaResources(True)
        
        self.requestRxOverErrors(True)
        
        self.requestRxFlowControlXon(True)
        
        self.requestTxRestartQueue(True)
        
        self.requestRxFrameErrors(True)
        
        self.requestRxPktsNic(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestHwRscFlushed(False)
        
        self.requestLscInt(False)
        
        self.requestHwRscAggregated(False)
        
        self.requestRxLongLengthErrors(False)
        
        self.requestFdirMatch(False)
        
        self.requestTxFcoePackets(False)
        
        self.requestRxShortLengthErrors(False)
        
        self.requestRxFcoeDwords(False)
        
        self.requestRxBytesNic(False)
        
        self.requestRxFcoePackets(False)
        
        self.requestTxFcoeDwords(False)
        
        self.requestRxNoBufferCount(False)
        
        self.requestRxFifoErrors(False)
        
        self.requestAllocRxPageFailed(False)
        
        self.requestTxBusy(False)
        
        self.requestTxAbortedErrors(False)
        
        self.requestCollisions(False)
        
        self.requestTxHeartbeatErrors(False)
        
        self.requestRxMissedErrors(False)
        
        self.requestNonEopDescs(False)
        
        self.requestTxFlowControlXon(False)
        
        self.requestRxCsumOffloadErrors(False)
        
        self.requestRxCrcErrors(False)
        
        self.requestTxFifoErrors(False)
        
        self.requestTxPktsNic(False)
        
        self.requestRxFcoeDropped(False)
        
        self.requestTxBytesNic(False)
        
        self.requestAllocRxBuffFailed(False)
        
        self.requestFcoeBadFccrc(False)
        
        self.requestTxFlowControlXoff(False)
        
        self.requestTxTimeoutCount(False)
        
        self.requestTxCarrierErrors(False)
        
        self.requestRxFlowControlXoff(False)
        
        self.requestFdirMiss(False)
        
        self.requestRxNoDmaResources(False)
        
        self.requestRxOverErrors(False)
        
        self.requestRxFlowControlXon(False)
        
        self.requestTxRestartQueue(False)
        
        self.requestRxFrameErrors(False)
        
        self.requestRxPktsNic(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestHwRscFlushed(True)
        
        self.requestLscInt(True)
        
        self.requestHwRscAggregated(True)
        
        self.requestRxLongLengthErrors(True)
        
        self.requestFdirMatch(True)
        
        self.requestTxFcoePackets(True)
        
        self.requestRxShortLengthErrors(True)
        
        self.requestRxFcoeDwords(True)
        
        self.requestRxBytesNic(True)
        
        self.requestRxFcoePackets(True)
        
        self.requestTxFcoeDwords(True)
        
        self.requestRxNoBufferCount(True)
        
        self.requestRxFifoErrors(True)
        
        self.requestAllocRxPageFailed(True)
        
        self.requestTxBusy(True)
        
        self.requestTxAbortedErrors(True)
        
        self.requestCollisions(True)
        
        self.requestTxHeartbeatErrors(True)
        
        self.requestRxMissedErrors(True)
        
        self.requestNonEopDescs(True)
        
        self.requestTxFlowControlXon(True)
        
        self.requestRxCsumOffloadErrors(True)
        
        self.requestRxCrcErrors(True)
        
        self.requestTxFifoErrors(True)
        
        self.requestTxPktsNic(True)
        
        self.requestRxFcoeDropped(True)
        
        self.requestTxBytesNic(True)
        
        self.requestAllocRxBuffFailed(True)
        
        self.requestFcoeBadFccrc(True)
        
        self.requestTxFlowControlXoff(True)
        
        self.requestTxTimeoutCount(True)
        
        self.requestTxCarrierErrors(True)
        
        self.requestRxFlowControlXoff(True)
        
        self.requestFdirMiss(True)
        
        self.requestRxNoDmaResources(True)
        
        self.requestRxOverErrors(True)
        
        self.requestRxFlowControlXon(True)
        
        self.requestTxRestartQueue(True)
        
        self.requestRxFrameErrors(True)
        
        self.requestRxPktsNic(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestHwRscFlushed(False)
        
        self.requestLscInt(False)
        
        self.requestHwRscAggregated(False)
        
        self.requestRxLongLengthErrors(False)
        
        self.requestFdirMatch(False)
        
        self.requestTxFcoePackets(False)
        
        self.requestRxShortLengthErrors(False)
        
        self.requestRxFcoeDwords(False)
        
        self.requestRxBytesNic(False)
        
        self.requestRxFcoePackets(False)
        
        self.requestTxFcoeDwords(False)
        
        self.requestRxNoBufferCount(False)
        
        self.requestRxFifoErrors(False)
        
        self.requestAllocRxPageFailed(False)
        
        self.requestTxBusy(False)
        
        self.requestTxAbortedErrors(False)
        
        self.requestCollisions(False)
        
        self.requestTxHeartbeatErrors(False)
        
        self.requestRxMissedErrors(False)
        
        self.requestNonEopDescs(False)
        
        self.requestTxFlowControlXon(False)
        
        self.requestRxCsumOffloadErrors(False)
        
        self.requestRxCrcErrors(False)
        
        self.requestTxFifoErrors(False)
        
        self.requestTxPktsNic(False)
        
        self.requestRxFcoeDropped(False)
        
        self.requestTxBytesNic(False)
        
        self.requestAllocRxBuffFailed(False)
        
        self.requestFcoeBadFccrc(False)
        
        self.requestTxFlowControlXoff(False)
        
        self.requestTxTimeoutCount(False)
        
        self.requestTxCarrierErrors(False)
        
        self.requestRxFlowControlXoff(False)
        
        self.requestFdirMiss(False)
        
        self.requestRxNoDmaResources(False)
        
        self.requestRxOverErrors(False)
        
        self.requestRxFlowControlXon(False)
        
        self.requestTxRestartQueue(False)
        
        self.requestRxFrameErrors(False)
        
        self.requestRxPktsNic(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , interface
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(interface, trxContext)

    def read (self
              , interface
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  True,
                                  trxContext)



    def requestHwRscFlushed (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-hwrscflushed').debug3Func(): logFunc('called. requested=%s', requested)
        self.hwRscFlushedRequested = requested
        self.hwRscFlushedSet = False

    def isHwRscFlushedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-hwrscflushed-requested').debug3Func(): logFunc('called. requested=%s', self.hwRscFlushedRequested)
        return self.hwRscFlushedRequested

    def getHwRscFlushed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-hwrscflushed').debug3Func(): logFunc('called. self.hwRscFlushedSet=%s, self.hwRscFlushed=%s', self.hwRscFlushedSet, self.hwRscFlushed)
        if self.hwRscFlushedSet:
            return self.hwRscFlushed
        return None

    def hasHwRscFlushed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-hwrscflushed').debug3Func(): logFunc('called. self.hwRscFlushedSet=%s, self.hwRscFlushed=%s', self.hwRscFlushedSet, self.hwRscFlushed)
        if self.hwRscFlushedSet:
            return True
        return False

    def setHwRscFlushed (self, hwRscFlushed):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-hwrscflushed').debug3Func(): logFunc('called. hwRscFlushed=%s, old=%s', hwRscFlushed, self.hwRscFlushed)
        self.hwRscFlushedSet = True
        self.hwRscFlushed = hwRscFlushed

    def requestLscInt (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-lscint').debug3Func(): logFunc('called. requested=%s', requested)
        self.lscIntRequested = requested
        self.lscIntSet = False

    def isLscIntRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-lscint-requested').debug3Func(): logFunc('called. requested=%s', self.lscIntRequested)
        return self.lscIntRequested

    def getLscInt (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-lscint').debug3Func(): logFunc('called. self.lscIntSet=%s, self.lscInt=%s', self.lscIntSet, self.lscInt)
        if self.lscIntSet:
            return self.lscInt
        return None

    def hasLscInt (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-lscint').debug3Func(): logFunc('called. self.lscIntSet=%s, self.lscInt=%s', self.lscIntSet, self.lscInt)
        if self.lscIntSet:
            return True
        return False

    def setLscInt (self, lscInt):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-lscint').debug3Func(): logFunc('called. lscInt=%s, old=%s', lscInt, self.lscInt)
        self.lscIntSet = True
        self.lscInt = lscInt

    def requestHwRscAggregated (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-hwrscaggregated').debug3Func(): logFunc('called. requested=%s', requested)
        self.hwRscAggregatedRequested = requested
        self.hwRscAggregatedSet = False

    def isHwRscAggregatedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-hwrscaggregated-requested').debug3Func(): logFunc('called. requested=%s', self.hwRscAggregatedRequested)
        return self.hwRscAggregatedRequested

    def getHwRscAggregated (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-hwrscaggregated').debug3Func(): logFunc('called. self.hwRscAggregatedSet=%s, self.hwRscAggregated=%s', self.hwRscAggregatedSet, self.hwRscAggregated)
        if self.hwRscAggregatedSet:
            return self.hwRscAggregated
        return None

    def hasHwRscAggregated (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-hwrscaggregated').debug3Func(): logFunc('called. self.hwRscAggregatedSet=%s, self.hwRscAggregated=%s', self.hwRscAggregatedSet, self.hwRscAggregated)
        if self.hwRscAggregatedSet:
            return True
        return False

    def setHwRscAggregated (self, hwRscAggregated):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-hwrscaggregated').debug3Func(): logFunc('called. hwRscAggregated=%s, old=%s', hwRscAggregated, self.hwRscAggregated)
        self.hwRscAggregatedSet = True
        self.hwRscAggregated = hwRscAggregated

    def requestRxLongLengthErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxlonglengtherrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxLongLengthErrorsRequested = requested
        self.rxLongLengthErrorsSet = False

    def isRxLongLengthErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxlonglengtherrors-requested').debug3Func(): logFunc('called. requested=%s', self.rxLongLengthErrorsRequested)
        return self.rxLongLengthErrorsRequested

    def getRxLongLengthErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxlonglengtherrors').debug3Func(): logFunc('called. self.rxLongLengthErrorsSet=%s, self.rxLongLengthErrors=%s', self.rxLongLengthErrorsSet, self.rxLongLengthErrors)
        if self.rxLongLengthErrorsSet:
            return self.rxLongLengthErrors
        return None

    def hasRxLongLengthErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxlonglengtherrors').debug3Func(): logFunc('called. self.rxLongLengthErrorsSet=%s, self.rxLongLengthErrors=%s', self.rxLongLengthErrorsSet, self.rxLongLengthErrors)
        if self.rxLongLengthErrorsSet:
            return True
        return False

    def setRxLongLengthErrors (self, rxLongLengthErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxlonglengtherrors').debug3Func(): logFunc('called. rxLongLengthErrors=%s, old=%s', rxLongLengthErrors, self.rxLongLengthErrors)
        self.rxLongLengthErrorsSet = True
        self.rxLongLengthErrors = rxLongLengthErrors

    def requestFdirMatch (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-fdirmatch').debug3Func(): logFunc('called. requested=%s', requested)
        self.fdirMatchRequested = requested
        self.fdirMatchSet = False

    def isFdirMatchRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-fdirmatch-requested').debug3Func(): logFunc('called. requested=%s', self.fdirMatchRequested)
        return self.fdirMatchRequested

    def getFdirMatch (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-fdirmatch').debug3Func(): logFunc('called. self.fdirMatchSet=%s, self.fdirMatch=%s', self.fdirMatchSet, self.fdirMatch)
        if self.fdirMatchSet:
            return self.fdirMatch
        return None

    def hasFdirMatch (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-fdirmatch').debug3Func(): logFunc('called. self.fdirMatchSet=%s, self.fdirMatch=%s', self.fdirMatchSet, self.fdirMatch)
        if self.fdirMatchSet:
            return True
        return False

    def setFdirMatch (self, fdirMatch):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-fdirmatch').debug3Func(): logFunc('called. fdirMatch=%s, old=%s', fdirMatch, self.fdirMatch)
        self.fdirMatchSet = True
        self.fdirMatch = fdirMatch

    def requestTxFcoePackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txfcoepackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.txFcoePacketsRequested = requested
        self.txFcoePacketsSet = False

    def isTxFcoePacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txfcoepackets-requested').debug3Func(): logFunc('called. requested=%s', self.txFcoePacketsRequested)
        return self.txFcoePacketsRequested

    def getTxFcoePackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txfcoepackets').debug3Func(): logFunc('called. self.txFcoePacketsSet=%s, self.txFcoePackets=%s', self.txFcoePacketsSet, self.txFcoePackets)
        if self.txFcoePacketsSet:
            return self.txFcoePackets
        return None

    def hasTxFcoePackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txfcoepackets').debug3Func(): logFunc('called. self.txFcoePacketsSet=%s, self.txFcoePackets=%s', self.txFcoePacketsSet, self.txFcoePackets)
        if self.txFcoePacketsSet:
            return True
        return False

    def setTxFcoePackets (self, txFcoePackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txfcoepackets').debug3Func(): logFunc('called. txFcoePackets=%s, old=%s', txFcoePackets, self.txFcoePackets)
        self.txFcoePacketsSet = True
        self.txFcoePackets = txFcoePackets

    def requestRxShortLengthErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxshortlengtherrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxShortLengthErrorsRequested = requested
        self.rxShortLengthErrorsSet = False

    def isRxShortLengthErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxshortlengtherrors-requested').debug3Func(): logFunc('called. requested=%s', self.rxShortLengthErrorsRequested)
        return self.rxShortLengthErrorsRequested

    def getRxShortLengthErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxshortlengtherrors').debug3Func(): logFunc('called. self.rxShortLengthErrorsSet=%s, self.rxShortLengthErrors=%s', self.rxShortLengthErrorsSet, self.rxShortLengthErrors)
        if self.rxShortLengthErrorsSet:
            return self.rxShortLengthErrors
        return None

    def hasRxShortLengthErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxshortlengtherrors').debug3Func(): logFunc('called. self.rxShortLengthErrorsSet=%s, self.rxShortLengthErrors=%s', self.rxShortLengthErrorsSet, self.rxShortLengthErrors)
        if self.rxShortLengthErrorsSet:
            return True
        return False

    def setRxShortLengthErrors (self, rxShortLengthErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxshortlengtherrors').debug3Func(): logFunc('called. rxShortLengthErrors=%s, old=%s', rxShortLengthErrors, self.rxShortLengthErrors)
        self.rxShortLengthErrorsSet = True
        self.rxShortLengthErrors = rxShortLengthErrors

    def requestRxFcoeDwords (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxfcoedwords').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxFcoeDwordsRequested = requested
        self.rxFcoeDwordsSet = False

    def isRxFcoeDwordsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxfcoedwords-requested').debug3Func(): logFunc('called. requested=%s', self.rxFcoeDwordsRequested)
        return self.rxFcoeDwordsRequested

    def getRxFcoeDwords (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxfcoedwords').debug3Func(): logFunc('called. self.rxFcoeDwordsSet=%s, self.rxFcoeDwords=%s', self.rxFcoeDwordsSet, self.rxFcoeDwords)
        if self.rxFcoeDwordsSet:
            return self.rxFcoeDwords
        return None

    def hasRxFcoeDwords (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxfcoedwords').debug3Func(): logFunc('called. self.rxFcoeDwordsSet=%s, self.rxFcoeDwords=%s', self.rxFcoeDwordsSet, self.rxFcoeDwords)
        if self.rxFcoeDwordsSet:
            return True
        return False

    def setRxFcoeDwords (self, rxFcoeDwords):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxfcoedwords').debug3Func(): logFunc('called. rxFcoeDwords=%s, old=%s', rxFcoeDwords, self.rxFcoeDwords)
        self.rxFcoeDwordsSet = True
        self.rxFcoeDwords = rxFcoeDwords

    def requestRxBytesNic (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxbytesnic').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxBytesNicRequested = requested
        self.rxBytesNicSet = False

    def isRxBytesNicRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxbytesnic-requested').debug3Func(): logFunc('called. requested=%s', self.rxBytesNicRequested)
        return self.rxBytesNicRequested

    def getRxBytesNic (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxbytesnic').debug3Func(): logFunc('called. self.rxBytesNicSet=%s, self.rxBytesNic=%s', self.rxBytesNicSet, self.rxBytesNic)
        if self.rxBytesNicSet:
            return self.rxBytesNic
        return None

    def hasRxBytesNic (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxbytesnic').debug3Func(): logFunc('called. self.rxBytesNicSet=%s, self.rxBytesNic=%s', self.rxBytesNicSet, self.rxBytesNic)
        if self.rxBytesNicSet:
            return True
        return False

    def setRxBytesNic (self, rxBytesNic):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxbytesnic').debug3Func(): logFunc('called. rxBytesNic=%s, old=%s', rxBytesNic, self.rxBytesNic)
        self.rxBytesNicSet = True
        self.rxBytesNic = rxBytesNic

    def requestRxFcoePackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxfcoepackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxFcoePacketsRequested = requested
        self.rxFcoePacketsSet = False

    def isRxFcoePacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxfcoepackets-requested').debug3Func(): logFunc('called. requested=%s', self.rxFcoePacketsRequested)
        return self.rxFcoePacketsRequested

    def getRxFcoePackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxfcoepackets').debug3Func(): logFunc('called. self.rxFcoePacketsSet=%s, self.rxFcoePackets=%s', self.rxFcoePacketsSet, self.rxFcoePackets)
        if self.rxFcoePacketsSet:
            return self.rxFcoePackets
        return None

    def hasRxFcoePackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxfcoepackets').debug3Func(): logFunc('called. self.rxFcoePacketsSet=%s, self.rxFcoePackets=%s', self.rxFcoePacketsSet, self.rxFcoePackets)
        if self.rxFcoePacketsSet:
            return True
        return False

    def setRxFcoePackets (self, rxFcoePackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxfcoepackets').debug3Func(): logFunc('called. rxFcoePackets=%s, old=%s', rxFcoePackets, self.rxFcoePackets)
        self.rxFcoePacketsSet = True
        self.rxFcoePackets = rxFcoePackets

    def requestTxFcoeDwords (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txfcoedwords').debug3Func(): logFunc('called. requested=%s', requested)
        self.txFcoeDwordsRequested = requested
        self.txFcoeDwordsSet = False

    def isTxFcoeDwordsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txfcoedwords-requested').debug3Func(): logFunc('called. requested=%s', self.txFcoeDwordsRequested)
        return self.txFcoeDwordsRequested

    def getTxFcoeDwords (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txfcoedwords').debug3Func(): logFunc('called. self.txFcoeDwordsSet=%s, self.txFcoeDwords=%s', self.txFcoeDwordsSet, self.txFcoeDwords)
        if self.txFcoeDwordsSet:
            return self.txFcoeDwords
        return None

    def hasTxFcoeDwords (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txfcoedwords').debug3Func(): logFunc('called. self.txFcoeDwordsSet=%s, self.txFcoeDwords=%s', self.txFcoeDwordsSet, self.txFcoeDwords)
        if self.txFcoeDwordsSet:
            return True
        return False

    def setTxFcoeDwords (self, txFcoeDwords):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txfcoedwords').debug3Func(): logFunc('called. txFcoeDwords=%s, old=%s', txFcoeDwords, self.txFcoeDwords)
        self.txFcoeDwordsSet = True
        self.txFcoeDwords = txFcoeDwords

    def requestRxNoBufferCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxnobuffercount').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxNoBufferCountRequested = requested
        self.rxNoBufferCountSet = False

    def isRxNoBufferCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxnobuffercount-requested').debug3Func(): logFunc('called. requested=%s', self.rxNoBufferCountRequested)
        return self.rxNoBufferCountRequested

    def getRxNoBufferCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxnobuffercount').debug3Func(): logFunc('called. self.rxNoBufferCountSet=%s, self.rxNoBufferCount=%s', self.rxNoBufferCountSet, self.rxNoBufferCount)
        if self.rxNoBufferCountSet:
            return self.rxNoBufferCount
        return None

    def hasRxNoBufferCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxnobuffercount').debug3Func(): logFunc('called. self.rxNoBufferCountSet=%s, self.rxNoBufferCount=%s', self.rxNoBufferCountSet, self.rxNoBufferCount)
        if self.rxNoBufferCountSet:
            return True
        return False

    def setRxNoBufferCount (self, rxNoBufferCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxnobuffercount').debug3Func(): logFunc('called. rxNoBufferCount=%s, old=%s', rxNoBufferCount, self.rxNoBufferCount)
        self.rxNoBufferCountSet = True
        self.rxNoBufferCount = rxNoBufferCount

    def requestRxFifoErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxfifoerrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxFifoErrorsRequested = requested
        self.rxFifoErrorsSet = False

    def isRxFifoErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxfifoerrors-requested').debug3Func(): logFunc('called. requested=%s', self.rxFifoErrorsRequested)
        return self.rxFifoErrorsRequested

    def getRxFifoErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxfifoerrors').debug3Func(): logFunc('called. self.rxFifoErrorsSet=%s, self.rxFifoErrors=%s', self.rxFifoErrorsSet, self.rxFifoErrors)
        if self.rxFifoErrorsSet:
            return self.rxFifoErrors
        return None

    def hasRxFifoErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxfifoerrors').debug3Func(): logFunc('called. self.rxFifoErrorsSet=%s, self.rxFifoErrors=%s', self.rxFifoErrorsSet, self.rxFifoErrors)
        if self.rxFifoErrorsSet:
            return True
        return False

    def setRxFifoErrors (self, rxFifoErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxfifoerrors').debug3Func(): logFunc('called. rxFifoErrors=%s, old=%s', rxFifoErrors, self.rxFifoErrors)
        self.rxFifoErrorsSet = True
        self.rxFifoErrors = rxFifoErrors

    def requestAllocRxPageFailed (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-allocrxpagefailed').debug3Func(): logFunc('called. requested=%s', requested)
        self.allocRxPageFailedRequested = requested
        self.allocRxPageFailedSet = False

    def isAllocRxPageFailedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-allocrxpagefailed-requested').debug3Func(): logFunc('called. requested=%s', self.allocRxPageFailedRequested)
        return self.allocRxPageFailedRequested

    def getAllocRxPageFailed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-allocrxpagefailed').debug3Func(): logFunc('called. self.allocRxPageFailedSet=%s, self.allocRxPageFailed=%s', self.allocRxPageFailedSet, self.allocRxPageFailed)
        if self.allocRxPageFailedSet:
            return self.allocRxPageFailed
        return None

    def hasAllocRxPageFailed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-allocrxpagefailed').debug3Func(): logFunc('called. self.allocRxPageFailedSet=%s, self.allocRxPageFailed=%s', self.allocRxPageFailedSet, self.allocRxPageFailed)
        if self.allocRxPageFailedSet:
            return True
        return False

    def setAllocRxPageFailed (self, allocRxPageFailed):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-allocrxpagefailed').debug3Func(): logFunc('called. allocRxPageFailed=%s, old=%s', allocRxPageFailed, self.allocRxPageFailed)
        self.allocRxPageFailedSet = True
        self.allocRxPageFailed = allocRxPageFailed

    def requestTxBusy (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txbusy').debug3Func(): logFunc('called. requested=%s', requested)
        self.txBusyRequested = requested
        self.txBusySet = False

    def isTxBusyRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txbusy-requested').debug3Func(): logFunc('called. requested=%s', self.txBusyRequested)
        return self.txBusyRequested

    def getTxBusy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txbusy').debug3Func(): logFunc('called. self.txBusySet=%s, self.txBusy=%s', self.txBusySet, self.txBusy)
        if self.txBusySet:
            return self.txBusy
        return None

    def hasTxBusy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txbusy').debug3Func(): logFunc('called. self.txBusySet=%s, self.txBusy=%s', self.txBusySet, self.txBusy)
        if self.txBusySet:
            return True
        return False

    def setTxBusy (self, txBusy):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txbusy').debug3Func(): logFunc('called. txBusy=%s, old=%s', txBusy, self.txBusy)
        self.txBusySet = True
        self.txBusy = txBusy

    def requestTxAbortedErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txabortederrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.txAbortedErrorsRequested = requested
        self.txAbortedErrorsSet = False

    def isTxAbortedErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txabortederrors-requested').debug3Func(): logFunc('called. requested=%s', self.txAbortedErrorsRequested)
        return self.txAbortedErrorsRequested

    def getTxAbortedErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txabortederrors').debug3Func(): logFunc('called. self.txAbortedErrorsSet=%s, self.txAbortedErrors=%s', self.txAbortedErrorsSet, self.txAbortedErrors)
        if self.txAbortedErrorsSet:
            return self.txAbortedErrors
        return None

    def hasTxAbortedErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txabortederrors').debug3Func(): logFunc('called. self.txAbortedErrorsSet=%s, self.txAbortedErrors=%s', self.txAbortedErrorsSet, self.txAbortedErrors)
        if self.txAbortedErrorsSet:
            return True
        return False

    def setTxAbortedErrors (self, txAbortedErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txabortederrors').debug3Func(): logFunc('called. txAbortedErrors=%s, old=%s', txAbortedErrors, self.txAbortedErrors)
        self.txAbortedErrorsSet = True
        self.txAbortedErrors = txAbortedErrors

    def requestCollisions (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-collisions').debug3Func(): logFunc('called. requested=%s', requested)
        self.collisionsRequested = requested
        self.collisionsSet = False

    def isCollisionsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-collisions-requested').debug3Func(): logFunc('called. requested=%s', self.collisionsRequested)
        return self.collisionsRequested

    def getCollisions (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-collisions').debug3Func(): logFunc('called. self.collisionsSet=%s, self.collisions=%s', self.collisionsSet, self.collisions)
        if self.collisionsSet:
            return self.collisions
        return None

    def hasCollisions (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-collisions').debug3Func(): logFunc('called. self.collisionsSet=%s, self.collisions=%s', self.collisionsSet, self.collisions)
        if self.collisionsSet:
            return True
        return False

    def setCollisions (self, collisions):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-collisions').debug3Func(): logFunc('called. collisions=%s, old=%s', collisions, self.collisions)
        self.collisionsSet = True
        self.collisions = collisions

    def requestTxHeartbeatErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txheartbeaterrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.txHeartbeatErrorsRequested = requested
        self.txHeartbeatErrorsSet = False

    def isTxHeartbeatErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txheartbeaterrors-requested').debug3Func(): logFunc('called. requested=%s', self.txHeartbeatErrorsRequested)
        return self.txHeartbeatErrorsRequested

    def getTxHeartbeatErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txheartbeaterrors').debug3Func(): logFunc('called. self.txHeartbeatErrorsSet=%s, self.txHeartbeatErrors=%s', self.txHeartbeatErrorsSet, self.txHeartbeatErrors)
        if self.txHeartbeatErrorsSet:
            return self.txHeartbeatErrors
        return None

    def hasTxHeartbeatErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txheartbeaterrors').debug3Func(): logFunc('called. self.txHeartbeatErrorsSet=%s, self.txHeartbeatErrors=%s', self.txHeartbeatErrorsSet, self.txHeartbeatErrors)
        if self.txHeartbeatErrorsSet:
            return True
        return False

    def setTxHeartbeatErrors (self, txHeartbeatErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txheartbeaterrors').debug3Func(): logFunc('called. txHeartbeatErrors=%s, old=%s', txHeartbeatErrors, self.txHeartbeatErrors)
        self.txHeartbeatErrorsSet = True
        self.txHeartbeatErrors = txHeartbeatErrors

    def requestRxMissedErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxmissederrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxMissedErrorsRequested = requested
        self.rxMissedErrorsSet = False

    def isRxMissedErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxmissederrors-requested').debug3Func(): logFunc('called. requested=%s', self.rxMissedErrorsRequested)
        return self.rxMissedErrorsRequested

    def getRxMissedErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxmissederrors').debug3Func(): logFunc('called. self.rxMissedErrorsSet=%s, self.rxMissedErrors=%s', self.rxMissedErrorsSet, self.rxMissedErrors)
        if self.rxMissedErrorsSet:
            return self.rxMissedErrors
        return None

    def hasRxMissedErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxmissederrors').debug3Func(): logFunc('called. self.rxMissedErrorsSet=%s, self.rxMissedErrors=%s', self.rxMissedErrorsSet, self.rxMissedErrors)
        if self.rxMissedErrorsSet:
            return True
        return False

    def setRxMissedErrors (self, rxMissedErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxmissederrors').debug3Func(): logFunc('called. rxMissedErrors=%s, old=%s', rxMissedErrors, self.rxMissedErrors)
        self.rxMissedErrorsSet = True
        self.rxMissedErrors = rxMissedErrors

    def requestNonEopDescs (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-noneopdescs').debug3Func(): logFunc('called. requested=%s', requested)
        self.nonEopDescsRequested = requested
        self.nonEopDescsSet = False

    def isNonEopDescsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-noneopdescs-requested').debug3Func(): logFunc('called. requested=%s', self.nonEopDescsRequested)
        return self.nonEopDescsRequested

    def getNonEopDescs (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-noneopdescs').debug3Func(): logFunc('called. self.nonEopDescsSet=%s, self.nonEopDescs=%s', self.nonEopDescsSet, self.nonEopDescs)
        if self.nonEopDescsSet:
            return self.nonEopDescs
        return None

    def hasNonEopDescs (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-noneopdescs').debug3Func(): logFunc('called. self.nonEopDescsSet=%s, self.nonEopDescs=%s', self.nonEopDescsSet, self.nonEopDescs)
        if self.nonEopDescsSet:
            return True
        return False

    def setNonEopDescs (self, nonEopDescs):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-noneopdescs').debug3Func(): logFunc('called. nonEopDescs=%s, old=%s', nonEopDescs, self.nonEopDescs)
        self.nonEopDescsSet = True
        self.nonEopDescs = nonEopDescs

    def requestTxFlowControlXon (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txflowcontrolxon').debug3Func(): logFunc('called. requested=%s', requested)
        self.txFlowControlXonRequested = requested
        self.txFlowControlXonSet = False

    def isTxFlowControlXonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txflowcontrolxon-requested').debug3Func(): logFunc('called. requested=%s', self.txFlowControlXonRequested)
        return self.txFlowControlXonRequested

    def getTxFlowControlXon (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txflowcontrolxon').debug3Func(): logFunc('called. self.txFlowControlXonSet=%s, self.txFlowControlXon=%s', self.txFlowControlXonSet, self.txFlowControlXon)
        if self.txFlowControlXonSet:
            return self.txFlowControlXon
        return None

    def hasTxFlowControlXon (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txflowcontrolxon').debug3Func(): logFunc('called. self.txFlowControlXonSet=%s, self.txFlowControlXon=%s', self.txFlowControlXonSet, self.txFlowControlXon)
        if self.txFlowControlXonSet:
            return True
        return False

    def setTxFlowControlXon (self, txFlowControlXon):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txflowcontrolxon').debug3Func(): logFunc('called. txFlowControlXon=%s, old=%s', txFlowControlXon, self.txFlowControlXon)
        self.txFlowControlXonSet = True
        self.txFlowControlXon = txFlowControlXon

    def requestRxCsumOffloadErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxcsumoffloaderrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxCsumOffloadErrorsRequested = requested
        self.rxCsumOffloadErrorsSet = False

    def isRxCsumOffloadErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxcsumoffloaderrors-requested').debug3Func(): logFunc('called. requested=%s', self.rxCsumOffloadErrorsRequested)
        return self.rxCsumOffloadErrorsRequested

    def getRxCsumOffloadErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxcsumoffloaderrors').debug3Func(): logFunc('called. self.rxCsumOffloadErrorsSet=%s, self.rxCsumOffloadErrors=%s', self.rxCsumOffloadErrorsSet, self.rxCsumOffloadErrors)
        if self.rxCsumOffloadErrorsSet:
            return self.rxCsumOffloadErrors
        return None

    def hasRxCsumOffloadErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxcsumoffloaderrors').debug3Func(): logFunc('called. self.rxCsumOffloadErrorsSet=%s, self.rxCsumOffloadErrors=%s', self.rxCsumOffloadErrorsSet, self.rxCsumOffloadErrors)
        if self.rxCsumOffloadErrorsSet:
            return True
        return False

    def setRxCsumOffloadErrors (self, rxCsumOffloadErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxcsumoffloaderrors').debug3Func(): logFunc('called. rxCsumOffloadErrors=%s, old=%s', rxCsumOffloadErrors, self.rxCsumOffloadErrors)
        self.rxCsumOffloadErrorsSet = True
        self.rxCsumOffloadErrors = rxCsumOffloadErrors

    def requestRxCrcErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxcrcerrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxCrcErrorsRequested = requested
        self.rxCrcErrorsSet = False

    def isRxCrcErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxcrcerrors-requested').debug3Func(): logFunc('called. requested=%s', self.rxCrcErrorsRequested)
        return self.rxCrcErrorsRequested

    def getRxCrcErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxcrcerrors').debug3Func(): logFunc('called. self.rxCrcErrorsSet=%s, self.rxCrcErrors=%s', self.rxCrcErrorsSet, self.rxCrcErrors)
        if self.rxCrcErrorsSet:
            return self.rxCrcErrors
        return None

    def hasRxCrcErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxcrcerrors').debug3Func(): logFunc('called. self.rxCrcErrorsSet=%s, self.rxCrcErrors=%s', self.rxCrcErrorsSet, self.rxCrcErrors)
        if self.rxCrcErrorsSet:
            return True
        return False

    def setRxCrcErrors (self, rxCrcErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxcrcerrors').debug3Func(): logFunc('called. rxCrcErrors=%s, old=%s', rxCrcErrors, self.rxCrcErrors)
        self.rxCrcErrorsSet = True
        self.rxCrcErrors = rxCrcErrors

    def requestTxFifoErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txfifoerrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.txFifoErrorsRequested = requested
        self.txFifoErrorsSet = False

    def isTxFifoErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txfifoerrors-requested').debug3Func(): logFunc('called. requested=%s', self.txFifoErrorsRequested)
        return self.txFifoErrorsRequested

    def getTxFifoErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txfifoerrors').debug3Func(): logFunc('called. self.txFifoErrorsSet=%s, self.txFifoErrors=%s', self.txFifoErrorsSet, self.txFifoErrors)
        if self.txFifoErrorsSet:
            return self.txFifoErrors
        return None

    def hasTxFifoErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txfifoerrors').debug3Func(): logFunc('called. self.txFifoErrorsSet=%s, self.txFifoErrors=%s', self.txFifoErrorsSet, self.txFifoErrors)
        if self.txFifoErrorsSet:
            return True
        return False

    def setTxFifoErrors (self, txFifoErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txfifoerrors').debug3Func(): logFunc('called. txFifoErrors=%s, old=%s', txFifoErrors, self.txFifoErrors)
        self.txFifoErrorsSet = True
        self.txFifoErrors = txFifoErrors

    def requestTxPktsNic (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txpktsnic').debug3Func(): logFunc('called. requested=%s', requested)
        self.txPktsNicRequested = requested
        self.txPktsNicSet = False

    def isTxPktsNicRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txpktsnic-requested').debug3Func(): logFunc('called. requested=%s', self.txPktsNicRequested)
        return self.txPktsNicRequested

    def getTxPktsNic (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txpktsnic').debug3Func(): logFunc('called. self.txPktsNicSet=%s, self.txPktsNic=%s', self.txPktsNicSet, self.txPktsNic)
        if self.txPktsNicSet:
            return self.txPktsNic
        return None

    def hasTxPktsNic (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txpktsnic').debug3Func(): logFunc('called. self.txPktsNicSet=%s, self.txPktsNic=%s', self.txPktsNicSet, self.txPktsNic)
        if self.txPktsNicSet:
            return True
        return False

    def setTxPktsNic (self, txPktsNic):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txpktsnic').debug3Func(): logFunc('called. txPktsNic=%s, old=%s', txPktsNic, self.txPktsNic)
        self.txPktsNicSet = True
        self.txPktsNic = txPktsNic

    def requestRxFcoeDropped (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxfcoedropped').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxFcoeDroppedRequested = requested
        self.rxFcoeDroppedSet = False

    def isRxFcoeDroppedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxfcoedropped-requested').debug3Func(): logFunc('called. requested=%s', self.rxFcoeDroppedRequested)
        return self.rxFcoeDroppedRequested

    def getRxFcoeDropped (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxfcoedropped').debug3Func(): logFunc('called. self.rxFcoeDroppedSet=%s, self.rxFcoeDropped=%s', self.rxFcoeDroppedSet, self.rxFcoeDropped)
        if self.rxFcoeDroppedSet:
            return self.rxFcoeDropped
        return None

    def hasRxFcoeDropped (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxfcoedropped').debug3Func(): logFunc('called. self.rxFcoeDroppedSet=%s, self.rxFcoeDropped=%s', self.rxFcoeDroppedSet, self.rxFcoeDropped)
        if self.rxFcoeDroppedSet:
            return True
        return False

    def setRxFcoeDropped (self, rxFcoeDropped):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxfcoedropped').debug3Func(): logFunc('called. rxFcoeDropped=%s, old=%s', rxFcoeDropped, self.rxFcoeDropped)
        self.rxFcoeDroppedSet = True
        self.rxFcoeDropped = rxFcoeDropped

    def requestTxBytesNic (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txbytesnic').debug3Func(): logFunc('called. requested=%s', requested)
        self.txBytesNicRequested = requested
        self.txBytesNicSet = False

    def isTxBytesNicRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txbytesnic-requested').debug3Func(): logFunc('called. requested=%s', self.txBytesNicRequested)
        return self.txBytesNicRequested

    def getTxBytesNic (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txbytesnic').debug3Func(): logFunc('called. self.txBytesNicSet=%s, self.txBytesNic=%s', self.txBytesNicSet, self.txBytesNic)
        if self.txBytesNicSet:
            return self.txBytesNic
        return None

    def hasTxBytesNic (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txbytesnic').debug3Func(): logFunc('called. self.txBytesNicSet=%s, self.txBytesNic=%s', self.txBytesNicSet, self.txBytesNic)
        if self.txBytesNicSet:
            return True
        return False

    def setTxBytesNic (self, txBytesNic):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txbytesnic').debug3Func(): logFunc('called. txBytesNic=%s, old=%s', txBytesNic, self.txBytesNic)
        self.txBytesNicSet = True
        self.txBytesNic = txBytesNic

    def requestAllocRxBuffFailed (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-allocrxbufffailed').debug3Func(): logFunc('called. requested=%s', requested)
        self.allocRxBuffFailedRequested = requested
        self.allocRxBuffFailedSet = False

    def isAllocRxBuffFailedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-allocrxbufffailed-requested').debug3Func(): logFunc('called. requested=%s', self.allocRxBuffFailedRequested)
        return self.allocRxBuffFailedRequested

    def getAllocRxBuffFailed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-allocrxbufffailed').debug3Func(): logFunc('called. self.allocRxBuffFailedSet=%s, self.allocRxBuffFailed=%s', self.allocRxBuffFailedSet, self.allocRxBuffFailed)
        if self.allocRxBuffFailedSet:
            return self.allocRxBuffFailed
        return None

    def hasAllocRxBuffFailed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-allocrxbufffailed').debug3Func(): logFunc('called. self.allocRxBuffFailedSet=%s, self.allocRxBuffFailed=%s', self.allocRxBuffFailedSet, self.allocRxBuffFailed)
        if self.allocRxBuffFailedSet:
            return True
        return False

    def setAllocRxBuffFailed (self, allocRxBuffFailed):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-allocrxbufffailed').debug3Func(): logFunc('called. allocRxBuffFailed=%s, old=%s', allocRxBuffFailed, self.allocRxBuffFailed)
        self.allocRxBuffFailedSet = True
        self.allocRxBuffFailed = allocRxBuffFailed

    def requestFcoeBadFccrc (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-fcoebadfccrc').debug3Func(): logFunc('called. requested=%s', requested)
        self.fcoeBadFccrcRequested = requested
        self.fcoeBadFccrcSet = False

    def isFcoeBadFccrcRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-fcoebadfccrc-requested').debug3Func(): logFunc('called. requested=%s', self.fcoeBadFccrcRequested)
        return self.fcoeBadFccrcRequested

    def getFcoeBadFccrc (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-fcoebadfccrc').debug3Func(): logFunc('called. self.fcoeBadFccrcSet=%s, self.fcoeBadFccrc=%s', self.fcoeBadFccrcSet, self.fcoeBadFccrc)
        if self.fcoeBadFccrcSet:
            return self.fcoeBadFccrc
        return None

    def hasFcoeBadFccrc (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-fcoebadfccrc').debug3Func(): logFunc('called. self.fcoeBadFccrcSet=%s, self.fcoeBadFccrc=%s', self.fcoeBadFccrcSet, self.fcoeBadFccrc)
        if self.fcoeBadFccrcSet:
            return True
        return False

    def setFcoeBadFccrc (self, fcoeBadFccrc):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-fcoebadfccrc').debug3Func(): logFunc('called. fcoeBadFccrc=%s, old=%s', fcoeBadFccrc, self.fcoeBadFccrc)
        self.fcoeBadFccrcSet = True
        self.fcoeBadFccrc = fcoeBadFccrc

    def requestTxFlowControlXoff (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txflowcontrolxoff').debug3Func(): logFunc('called. requested=%s', requested)
        self.txFlowControlXoffRequested = requested
        self.txFlowControlXoffSet = False

    def isTxFlowControlXoffRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txflowcontrolxoff-requested').debug3Func(): logFunc('called. requested=%s', self.txFlowControlXoffRequested)
        return self.txFlowControlXoffRequested

    def getTxFlowControlXoff (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txflowcontrolxoff').debug3Func(): logFunc('called. self.txFlowControlXoffSet=%s, self.txFlowControlXoff=%s', self.txFlowControlXoffSet, self.txFlowControlXoff)
        if self.txFlowControlXoffSet:
            return self.txFlowControlXoff
        return None

    def hasTxFlowControlXoff (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txflowcontrolxoff').debug3Func(): logFunc('called. self.txFlowControlXoffSet=%s, self.txFlowControlXoff=%s', self.txFlowControlXoffSet, self.txFlowControlXoff)
        if self.txFlowControlXoffSet:
            return True
        return False

    def setTxFlowControlXoff (self, txFlowControlXoff):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txflowcontrolxoff').debug3Func(): logFunc('called. txFlowControlXoff=%s, old=%s', txFlowControlXoff, self.txFlowControlXoff)
        self.txFlowControlXoffSet = True
        self.txFlowControlXoff = txFlowControlXoff

    def requestTxTimeoutCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txtimeoutcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.txTimeoutCountRequested = requested
        self.txTimeoutCountSet = False

    def isTxTimeoutCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txtimeoutcount-requested').debug3Func(): logFunc('called. requested=%s', self.txTimeoutCountRequested)
        return self.txTimeoutCountRequested

    def getTxTimeoutCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txtimeoutcount').debug3Func(): logFunc('called. self.txTimeoutCountSet=%s, self.txTimeoutCount=%s', self.txTimeoutCountSet, self.txTimeoutCount)
        if self.txTimeoutCountSet:
            return self.txTimeoutCount
        return None

    def hasTxTimeoutCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txtimeoutcount').debug3Func(): logFunc('called. self.txTimeoutCountSet=%s, self.txTimeoutCount=%s', self.txTimeoutCountSet, self.txTimeoutCount)
        if self.txTimeoutCountSet:
            return True
        return False

    def setTxTimeoutCount (self, txTimeoutCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txtimeoutcount').debug3Func(): logFunc('called. txTimeoutCount=%s, old=%s', txTimeoutCount, self.txTimeoutCount)
        self.txTimeoutCountSet = True
        self.txTimeoutCount = txTimeoutCount

    def requestTxCarrierErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txcarriererrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.txCarrierErrorsRequested = requested
        self.txCarrierErrorsSet = False

    def isTxCarrierErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txcarriererrors-requested').debug3Func(): logFunc('called. requested=%s', self.txCarrierErrorsRequested)
        return self.txCarrierErrorsRequested

    def getTxCarrierErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txcarriererrors').debug3Func(): logFunc('called. self.txCarrierErrorsSet=%s, self.txCarrierErrors=%s', self.txCarrierErrorsSet, self.txCarrierErrors)
        if self.txCarrierErrorsSet:
            return self.txCarrierErrors
        return None

    def hasTxCarrierErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txcarriererrors').debug3Func(): logFunc('called. self.txCarrierErrorsSet=%s, self.txCarrierErrors=%s', self.txCarrierErrorsSet, self.txCarrierErrors)
        if self.txCarrierErrorsSet:
            return True
        return False

    def setTxCarrierErrors (self, txCarrierErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txcarriererrors').debug3Func(): logFunc('called. txCarrierErrors=%s, old=%s', txCarrierErrors, self.txCarrierErrors)
        self.txCarrierErrorsSet = True
        self.txCarrierErrors = txCarrierErrors

    def requestRxFlowControlXoff (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxflowcontrolxoff').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxFlowControlXoffRequested = requested
        self.rxFlowControlXoffSet = False

    def isRxFlowControlXoffRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxflowcontrolxoff-requested').debug3Func(): logFunc('called. requested=%s', self.rxFlowControlXoffRequested)
        return self.rxFlowControlXoffRequested

    def getRxFlowControlXoff (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxflowcontrolxoff').debug3Func(): logFunc('called. self.rxFlowControlXoffSet=%s, self.rxFlowControlXoff=%s', self.rxFlowControlXoffSet, self.rxFlowControlXoff)
        if self.rxFlowControlXoffSet:
            return self.rxFlowControlXoff
        return None

    def hasRxFlowControlXoff (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxflowcontrolxoff').debug3Func(): logFunc('called. self.rxFlowControlXoffSet=%s, self.rxFlowControlXoff=%s', self.rxFlowControlXoffSet, self.rxFlowControlXoff)
        if self.rxFlowControlXoffSet:
            return True
        return False

    def setRxFlowControlXoff (self, rxFlowControlXoff):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxflowcontrolxoff').debug3Func(): logFunc('called. rxFlowControlXoff=%s, old=%s', rxFlowControlXoff, self.rxFlowControlXoff)
        self.rxFlowControlXoffSet = True
        self.rxFlowControlXoff = rxFlowControlXoff

    def requestFdirMiss (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-fdirmiss').debug3Func(): logFunc('called. requested=%s', requested)
        self.fdirMissRequested = requested
        self.fdirMissSet = False

    def isFdirMissRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-fdirmiss-requested').debug3Func(): logFunc('called. requested=%s', self.fdirMissRequested)
        return self.fdirMissRequested

    def getFdirMiss (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-fdirmiss').debug3Func(): logFunc('called. self.fdirMissSet=%s, self.fdirMiss=%s', self.fdirMissSet, self.fdirMiss)
        if self.fdirMissSet:
            return self.fdirMiss
        return None

    def hasFdirMiss (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-fdirmiss').debug3Func(): logFunc('called. self.fdirMissSet=%s, self.fdirMiss=%s', self.fdirMissSet, self.fdirMiss)
        if self.fdirMissSet:
            return True
        return False

    def setFdirMiss (self, fdirMiss):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-fdirmiss').debug3Func(): logFunc('called. fdirMiss=%s, old=%s', fdirMiss, self.fdirMiss)
        self.fdirMissSet = True
        self.fdirMiss = fdirMiss

    def requestRxNoDmaResources (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxnodmaresources').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxNoDmaResourcesRequested = requested
        self.rxNoDmaResourcesSet = False

    def isRxNoDmaResourcesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxnodmaresources-requested').debug3Func(): logFunc('called. requested=%s', self.rxNoDmaResourcesRequested)
        return self.rxNoDmaResourcesRequested

    def getRxNoDmaResources (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxnodmaresources').debug3Func(): logFunc('called. self.rxNoDmaResourcesSet=%s, self.rxNoDmaResources=%s', self.rxNoDmaResourcesSet, self.rxNoDmaResources)
        if self.rxNoDmaResourcesSet:
            return self.rxNoDmaResources
        return None

    def hasRxNoDmaResources (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxnodmaresources').debug3Func(): logFunc('called. self.rxNoDmaResourcesSet=%s, self.rxNoDmaResources=%s', self.rxNoDmaResourcesSet, self.rxNoDmaResources)
        if self.rxNoDmaResourcesSet:
            return True
        return False

    def setRxNoDmaResources (self, rxNoDmaResources):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxnodmaresources').debug3Func(): logFunc('called. rxNoDmaResources=%s, old=%s', rxNoDmaResources, self.rxNoDmaResources)
        self.rxNoDmaResourcesSet = True
        self.rxNoDmaResources = rxNoDmaResources

    def requestRxOverErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxovererrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxOverErrorsRequested = requested
        self.rxOverErrorsSet = False

    def isRxOverErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxovererrors-requested').debug3Func(): logFunc('called. requested=%s', self.rxOverErrorsRequested)
        return self.rxOverErrorsRequested

    def getRxOverErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxovererrors').debug3Func(): logFunc('called. self.rxOverErrorsSet=%s, self.rxOverErrors=%s', self.rxOverErrorsSet, self.rxOverErrors)
        if self.rxOverErrorsSet:
            return self.rxOverErrors
        return None

    def hasRxOverErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxovererrors').debug3Func(): logFunc('called. self.rxOverErrorsSet=%s, self.rxOverErrors=%s', self.rxOverErrorsSet, self.rxOverErrors)
        if self.rxOverErrorsSet:
            return True
        return False

    def setRxOverErrors (self, rxOverErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxovererrors').debug3Func(): logFunc('called. rxOverErrors=%s, old=%s', rxOverErrors, self.rxOverErrors)
        self.rxOverErrorsSet = True
        self.rxOverErrors = rxOverErrors

    def requestRxFlowControlXon (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxflowcontrolxon').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxFlowControlXonRequested = requested
        self.rxFlowControlXonSet = False

    def isRxFlowControlXonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxflowcontrolxon-requested').debug3Func(): logFunc('called. requested=%s', self.rxFlowControlXonRequested)
        return self.rxFlowControlXonRequested

    def getRxFlowControlXon (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxflowcontrolxon').debug3Func(): logFunc('called. self.rxFlowControlXonSet=%s, self.rxFlowControlXon=%s', self.rxFlowControlXonSet, self.rxFlowControlXon)
        if self.rxFlowControlXonSet:
            return self.rxFlowControlXon
        return None

    def hasRxFlowControlXon (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxflowcontrolxon').debug3Func(): logFunc('called. self.rxFlowControlXonSet=%s, self.rxFlowControlXon=%s', self.rxFlowControlXonSet, self.rxFlowControlXon)
        if self.rxFlowControlXonSet:
            return True
        return False

    def setRxFlowControlXon (self, rxFlowControlXon):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxflowcontrolxon').debug3Func(): logFunc('called. rxFlowControlXon=%s, old=%s', rxFlowControlXon, self.rxFlowControlXon)
        self.rxFlowControlXonSet = True
        self.rxFlowControlXon = rxFlowControlXon

    def requestTxRestartQueue (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-txrestartqueue').debug3Func(): logFunc('called. requested=%s', requested)
        self.txRestartQueueRequested = requested
        self.txRestartQueueSet = False

    def isTxRestartQueueRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-txrestartqueue-requested').debug3Func(): logFunc('called. requested=%s', self.txRestartQueueRequested)
        return self.txRestartQueueRequested

    def getTxRestartQueue (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-txrestartqueue').debug3Func(): logFunc('called. self.txRestartQueueSet=%s, self.txRestartQueue=%s', self.txRestartQueueSet, self.txRestartQueue)
        if self.txRestartQueueSet:
            return self.txRestartQueue
        return None

    def hasTxRestartQueue (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-txrestartqueue').debug3Func(): logFunc('called. self.txRestartQueueSet=%s, self.txRestartQueue=%s', self.txRestartQueueSet, self.txRestartQueue)
        if self.txRestartQueueSet:
            return True
        return False

    def setTxRestartQueue (self, txRestartQueue):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-txrestartqueue').debug3Func(): logFunc('called. txRestartQueue=%s, old=%s', txRestartQueue, self.txRestartQueue)
        self.txRestartQueueSet = True
        self.txRestartQueue = txRestartQueue

    def requestRxFrameErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxframeerrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxFrameErrorsRequested = requested
        self.rxFrameErrorsSet = False

    def isRxFrameErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxframeerrors-requested').debug3Func(): logFunc('called. requested=%s', self.rxFrameErrorsRequested)
        return self.rxFrameErrorsRequested

    def getRxFrameErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxframeerrors').debug3Func(): logFunc('called. self.rxFrameErrorsSet=%s, self.rxFrameErrors=%s', self.rxFrameErrorsSet, self.rxFrameErrors)
        if self.rxFrameErrorsSet:
            return self.rxFrameErrors
        return None

    def hasRxFrameErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxframeerrors').debug3Func(): logFunc('called. self.rxFrameErrorsSet=%s, self.rxFrameErrors=%s', self.rxFrameErrorsSet, self.rxFrameErrors)
        if self.rxFrameErrorsSet:
            return True
        return False

    def setRxFrameErrors (self, rxFrameErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxframeerrors').debug3Func(): logFunc('called. rxFrameErrors=%s, old=%s', rxFrameErrors, self.rxFrameErrors)
        self.rxFrameErrorsSet = True
        self.rxFrameErrors = rxFrameErrors

    def requestRxPktsNic (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rxpktsnic').debug3Func(): logFunc('called. requested=%s', requested)
        self.rxPktsNicRequested = requested
        self.rxPktsNicSet = False

    def isRxPktsNicRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rxpktsnic-requested').debug3Func(): logFunc('called. requested=%s', self.rxPktsNicRequested)
        return self.rxPktsNicRequested

    def getRxPktsNic (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rxpktsnic').debug3Func(): logFunc('called. self.rxPktsNicSet=%s, self.rxPktsNic=%s', self.rxPktsNicSet, self.rxPktsNic)
        if self.rxPktsNicSet:
            return self.rxPktsNic
        return None

    def hasRxPktsNic (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rxpktsnic').debug3Func(): logFunc('called. self.rxPktsNicSet=%s, self.rxPktsNic=%s', self.rxPktsNicSet, self.rxPktsNic)
        if self.rxPktsNicSet:
            return True
        return False

    def setRxPktsNic (self, rxPktsNic):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rxpktsnic').debug3Func(): logFunc('called. rxPktsNic=%s, old=%s', rxPktsNic, self.rxPktsNic)
        self.rxPktsNicSet = True
        self.rxPktsNic = rxPktsNic


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.hwRscFlushed = 0
        self.hwRscFlushedSet = False
        
        self.lscInt = 0
        self.lscIntSet = False
        
        self.hwRscAggregated = 0
        self.hwRscAggregatedSet = False
        
        self.rxLongLengthErrors = 0
        self.rxLongLengthErrorsSet = False
        
        self.fdirMatch = 0
        self.fdirMatchSet = False
        
        self.txFcoePackets = 0
        self.txFcoePacketsSet = False
        
        self.rxShortLengthErrors = 0
        self.rxShortLengthErrorsSet = False
        
        self.rxFcoeDwords = 0
        self.rxFcoeDwordsSet = False
        
        self.rxBytesNic = 0
        self.rxBytesNicSet = False
        
        self.rxFcoePackets = 0
        self.rxFcoePacketsSet = False
        
        self.txFcoeDwords = 0
        self.txFcoeDwordsSet = False
        
        self.rxNoBufferCount = 0
        self.rxNoBufferCountSet = False
        
        self.rxFifoErrors = 0
        self.rxFifoErrorsSet = False
        
        self.allocRxPageFailed = 0
        self.allocRxPageFailedSet = False
        
        self.txBusy = 0
        self.txBusySet = False
        
        self.txAbortedErrors = 0
        self.txAbortedErrorsSet = False
        
        self.collisions = 0
        self.collisionsSet = False
        
        self.txHeartbeatErrors = 0
        self.txHeartbeatErrorsSet = False
        
        self.rxMissedErrors = 0
        self.rxMissedErrorsSet = False
        
        self.nonEopDescs = 0
        self.nonEopDescsSet = False
        
        self.txFlowControlXon = 0
        self.txFlowControlXonSet = False
        
        self.rxCsumOffloadErrors = 0
        self.rxCsumOffloadErrorsSet = False
        
        self.rxCrcErrors = 0
        self.rxCrcErrorsSet = False
        
        self.txFifoErrors = 0
        self.txFifoErrorsSet = False
        
        self.txPktsNic = 0
        self.txPktsNicSet = False
        
        self.rxFcoeDropped = 0
        self.rxFcoeDroppedSet = False
        
        self.txBytesNic = 0
        self.txBytesNicSet = False
        
        self.allocRxBuffFailed = 0
        self.allocRxBuffFailedSet = False
        
        self.fcoeBadFccrc = 0
        self.fcoeBadFccrcSet = False
        
        self.txFlowControlXoff = 0
        self.txFlowControlXoffSet = False
        
        self.txTimeoutCount = 0
        self.txTimeoutCountSet = False
        
        self.txCarrierErrors = 0
        self.txCarrierErrorsSet = False
        
        self.rxFlowControlXoff = 0
        self.rxFlowControlXoffSet = False
        
        self.fdirMiss = 0
        self.fdirMissSet = False
        
        self.rxNoDmaResources = 0
        self.rxNoDmaResourcesSet = False
        
        self.rxOverErrors = 0
        self.rxOverErrorsSet = False
        
        self.rxFlowControlXon = 0
        self.rxFlowControlXonSet = False
        
        self.txRestartQueue = 0
        self.txRestartQueueSet = False
        
        self.rxFrameErrors = 0
        self.rxFrameErrorsSet = False
        
        self.rxPktsNic = 0
        self.rxPktsNicSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(interface);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interfaces", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        interface, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(interface, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       interface, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               interface, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isHwRscFlushedRequested():
            valHwRscFlushed = Value()
            valHwRscFlushed.setEmpty()
            tagValueList.push(("hw-rsc-flushed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valHwRscFlushed)
        
        if self.isLscIntRequested():
            valLscInt = Value()
            valLscInt.setEmpty()
            tagValueList.push(("lsc-int", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valLscInt)
        
        if self.isHwRscAggregatedRequested():
            valHwRscAggregated = Value()
            valHwRscAggregated.setEmpty()
            tagValueList.push(("hw-rsc-aggregated", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valHwRscAggregated)
        
        if self.isRxLongLengthErrorsRequested():
            valRxLongLengthErrors = Value()
            valRxLongLengthErrors.setEmpty()
            tagValueList.push(("rx-long-length-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxLongLengthErrors)
        
        if self.isFdirMatchRequested():
            valFdirMatch = Value()
            valFdirMatch.setEmpty()
            tagValueList.push(("fdir-match", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valFdirMatch)
        
        if self.isTxFcoePacketsRequested():
            valTxFcoePackets = Value()
            valTxFcoePackets.setEmpty()
            tagValueList.push(("tx-fcoe-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxFcoePackets)
        
        if self.isRxShortLengthErrorsRequested():
            valRxShortLengthErrors = Value()
            valRxShortLengthErrors.setEmpty()
            tagValueList.push(("rx-short-length-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxShortLengthErrors)
        
        if self.isRxFcoeDwordsRequested():
            valRxFcoeDwords = Value()
            valRxFcoeDwords.setEmpty()
            tagValueList.push(("rx-fcoe-dwords", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxFcoeDwords)
        
        if self.isRxBytesNicRequested():
            valRxBytesNic = Value()
            valRxBytesNic.setEmpty()
            tagValueList.push(("rx-bytes-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxBytesNic)
        
        if self.isRxFcoePacketsRequested():
            valRxFcoePackets = Value()
            valRxFcoePackets.setEmpty()
            tagValueList.push(("rx-fcoe-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxFcoePackets)
        
        if self.isTxFcoeDwordsRequested():
            valTxFcoeDwords = Value()
            valTxFcoeDwords.setEmpty()
            tagValueList.push(("tx-fcoe-dwords", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxFcoeDwords)
        
        if self.isRxNoBufferCountRequested():
            valRxNoBufferCount = Value()
            valRxNoBufferCount.setEmpty()
            tagValueList.push(("rx-no-buffer-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxNoBufferCount)
        
        if self.isRxFifoErrorsRequested():
            valRxFifoErrors = Value()
            valRxFifoErrors.setEmpty()
            tagValueList.push(("rx-fifo-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxFifoErrors)
        
        if self.isAllocRxPageFailedRequested():
            valAllocRxPageFailed = Value()
            valAllocRxPageFailed.setEmpty()
            tagValueList.push(("alloc-rx-page-failed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valAllocRxPageFailed)
        
        if self.isTxBusyRequested():
            valTxBusy = Value()
            valTxBusy.setEmpty()
            tagValueList.push(("tx-busy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxBusy)
        
        if self.isTxAbortedErrorsRequested():
            valTxAbortedErrors = Value()
            valTxAbortedErrors.setEmpty()
            tagValueList.push(("tx-aborted-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxAbortedErrors)
        
        if self.isCollisionsRequested():
            valCollisions = Value()
            valCollisions.setEmpty()
            tagValueList.push(("collisions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valCollisions)
        
        if self.isTxHeartbeatErrorsRequested():
            valTxHeartbeatErrors = Value()
            valTxHeartbeatErrors.setEmpty()
            tagValueList.push(("tx-heartbeat-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxHeartbeatErrors)
        
        if self.isRxMissedErrorsRequested():
            valRxMissedErrors = Value()
            valRxMissedErrors.setEmpty()
            tagValueList.push(("rx-missed-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxMissedErrors)
        
        if self.isNonEopDescsRequested():
            valNonEopDescs = Value()
            valNonEopDescs.setEmpty()
            tagValueList.push(("non-eop-descs", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valNonEopDescs)
        
        if self.isTxFlowControlXonRequested():
            valTxFlowControlXon = Value()
            valTxFlowControlXon.setEmpty()
            tagValueList.push(("tx-flow-control-xon", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxFlowControlXon)
        
        if self.isRxCsumOffloadErrorsRequested():
            valRxCsumOffloadErrors = Value()
            valRxCsumOffloadErrors.setEmpty()
            tagValueList.push(("rx-csum-offload-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxCsumOffloadErrors)
        
        if self.isRxCrcErrorsRequested():
            valRxCrcErrors = Value()
            valRxCrcErrors.setEmpty()
            tagValueList.push(("rx-crc-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxCrcErrors)
        
        if self.isTxFifoErrorsRequested():
            valTxFifoErrors = Value()
            valTxFifoErrors.setEmpty()
            tagValueList.push(("tx-fifo-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxFifoErrors)
        
        if self.isTxPktsNicRequested():
            valTxPktsNic = Value()
            valTxPktsNic.setEmpty()
            tagValueList.push(("tx-pkts-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxPktsNic)
        
        if self.isRxFcoeDroppedRequested():
            valRxFcoeDropped = Value()
            valRxFcoeDropped.setEmpty()
            tagValueList.push(("rx-fcoe-dropped", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxFcoeDropped)
        
        if self.isTxBytesNicRequested():
            valTxBytesNic = Value()
            valTxBytesNic.setEmpty()
            tagValueList.push(("tx-bytes-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxBytesNic)
        
        if self.isAllocRxBuffFailedRequested():
            valAllocRxBuffFailed = Value()
            valAllocRxBuffFailed.setEmpty()
            tagValueList.push(("alloc-rx-buff-failed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valAllocRxBuffFailed)
        
        if self.isFcoeBadFccrcRequested():
            valFcoeBadFccrc = Value()
            valFcoeBadFccrc.setEmpty()
            tagValueList.push(("fcoe-bad-fccrc", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valFcoeBadFccrc)
        
        if self.isTxFlowControlXoffRequested():
            valTxFlowControlXoff = Value()
            valTxFlowControlXoff.setEmpty()
            tagValueList.push(("tx-flow-control-xoff", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxFlowControlXoff)
        
        if self.isTxTimeoutCountRequested():
            valTxTimeoutCount = Value()
            valTxTimeoutCount.setEmpty()
            tagValueList.push(("tx-timeout-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxTimeoutCount)
        
        if self.isTxCarrierErrorsRequested():
            valTxCarrierErrors = Value()
            valTxCarrierErrors.setEmpty()
            tagValueList.push(("tx-carrier-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxCarrierErrors)
        
        if self.isRxFlowControlXoffRequested():
            valRxFlowControlXoff = Value()
            valRxFlowControlXoff.setEmpty()
            tagValueList.push(("rx-flow-control-xoff", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxFlowControlXoff)
        
        if self.isFdirMissRequested():
            valFdirMiss = Value()
            valFdirMiss.setEmpty()
            tagValueList.push(("fdir-miss", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valFdirMiss)
        
        if self.isRxNoDmaResourcesRequested():
            valRxNoDmaResources = Value()
            valRxNoDmaResources.setEmpty()
            tagValueList.push(("rx-no-dma-resources", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxNoDmaResources)
        
        if self.isRxOverErrorsRequested():
            valRxOverErrors = Value()
            valRxOverErrors.setEmpty()
            tagValueList.push(("rx-over-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxOverErrors)
        
        if self.isRxFlowControlXonRequested():
            valRxFlowControlXon = Value()
            valRxFlowControlXon.setEmpty()
            tagValueList.push(("rx-flow-control-xon", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxFlowControlXon)
        
        if self.isTxRestartQueueRequested():
            valTxRestartQueue = Value()
            valTxRestartQueue.setEmpty()
            tagValueList.push(("tx-restart-queue", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTxRestartQueue)
        
        if self.isRxFrameErrorsRequested():
            valRxFrameErrors = Value()
            valRxFrameErrors.setEmpty()
            tagValueList.push(("rx-frame-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxFrameErrors)
        
        if self.isRxPktsNicRequested():
            valRxPktsNic = Value()
            valRxPktsNic.setEmpty()
            tagValueList.push(("rx-pkts-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valRxPktsNic)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isHwRscFlushedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "hw-rsc-flushed") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-hwrscflushed').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "hwRscFlushed", "hw-rsc-flushed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-hw-rsc-flushed-bad-value').infoFunc(): logFunc('hwRscFlushed not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHwRscFlushed(tempVar)
            for logFunc in self._log('read-tag-values-hw-rsc-flushed').debug3Func(): logFunc('read hwRscFlushed. hwRscFlushed=%s, tempValue=%s', self.hwRscFlushed, tempValue.getType())
        
        if self.isLscIntRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "lsc-int") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-lscint').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "lscInt", "lsc-int", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-lsc-int-bad-value').infoFunc(): logFunc('lscInt not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLscInt(tempVar)
            for logFunc in self._log('read-tag-values-lsc-int').debug3Func(): logFunc('read lscInt. lscInt=%s, tempValue=%s', self.lscInt, tempValue.getType())
        
        if self.isHwRscAggregatedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "hw-rsc-aggregated") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-hwrscaggregated').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "hwRscAggregated", "hw-rsc-aggregated", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-hw-rsc-aggregated-bad-value').infoFunc(): logFunc('hwRscAggregated not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHwRscAggregated(tempVar)
            for logFunc in self._log('read-tag-values-hw-rsc-aggregated').debug3Func(): logFunc('read hwRscAggregated. hwRscAggregated=%s, tempValue=%s', self.hwRscAggregated, tempValue.getType())
        
        if self.isRxLongLengthErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-long-length-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxlonglengtherrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxLongLengthErrors", "rx-long-length-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-long-length-errors-bad-value').infoFunc(): logFunc('rxLongLengthErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxLongLengthErrors(tempVar)
            for logFunc in self._log('read-tag-values-rx-long-length-errors').debug3Func(): logFunc('read rxLongLengthErrors. rxLongLengthErrors=%s, tempValue=%s', self.rxLongLengthErrors, tempValue.getType())
        
        if self.isFdirMatchRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "fdir-match") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-fdirmatch').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fdirMatch", "fdir-match", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-fdir-match-bad-value').infoFunc(): logFunc('fdirMatch not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFdirMatch(tempVar)
            for logFunc in self._log('read-tag-values-fdir-match').debug3Func(): logFunc('read fdirMatch. fdirMatch=%s, tempValue=%s', self.fdirMatch, tempValue.getType())
        
        if self.isTxFcoePacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-fcoe-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txfcoepackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txFcoePackets", "tx-fcoe-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-fcoe-packets-bad-value').infoFunc(): logFunc('txFcoePackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxFcoePackets(tempVar)
            for logFunc in self._log('read-tag-values-tx-fcoe-packets').debug3Func(): logFunc('read txFcoePackets. txFcoePackets=%s, tempValue=%s', self.txFcoePackets, tempValue.getType())
        
        if self.isRxShortLengthErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-short-length-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxshortlengtherrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxShortLengthErrors", "rx-short-length-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-short-length-errors-bad-value').infoFunc(): logFunc('rxShortLengthErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxShortLengthErrors(tempVar)
            for logFunc in self._log('read-tag-values-rx-short-length-errors').debug3Func(): logFunc('read rxShortLengthErrors. rxShortLengthErrors=%s, tempValue=%s', self.rxShortLengthErrors, tempValue.getType())
        
        if self.isRxFcoeDwordsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-fcoe-dwords") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxfcoedwords').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxFcoeDwords", "rx-fcoe-dwords", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-fcoe-dwords-bad-value').infoFunc(): logFunc('rxFcoeDwords not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxFcoeDwords(tempVar)
            for logFunc in self._log('read-tag-values-rx-fcoe-dwords').debug3Func(): logFunc('read rxFcoeDwords. rxFcoeDwords=%s, tempValue=%s', self.rxFcoeDwords, tempValue.getType())
        
        if self.isRxBytesNicRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-bytes-nic") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxbytesnic').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxBytesNic", "rx-bytes-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-bytes-nic-bad-value').infoFunc(): logFunc('rxBytesNic not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxBytesNic(tempVar)
            for logFunc in self._log('read-tag-values-rx-bytes-nic').debug3Func(): logFunc('read rxBytesNic. rxBytesNic=%s, tempValue=%s', self.rxBytesNic, tempValue.getType())
        
        if self.isRxFcoePacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-fcoe-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxfcoepackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxFcoePackets", "rx-fcoe-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-fcoe-packets-bad-value').infoFunc(): logFunc('rxFcoePackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxFcoePackets(tempVar)
            for logFunc in self._log('read-tag-values-rx-fcoe-packets').debug3Func(): logFunc('read rxFcoePackets. rxFcoePackets=%s, tempValue=%s', self.rxFcoePackets, tempValue.getType())
        
        if self.isTxFcoeDwordsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-fcoe-dwords") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txfcoedwords').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txFcoeDwords", "tx-fcoe-dwords", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-fcoe-dwords-bad-value').infoFunc(): logFunc('txFcoeDwords not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxFcoeDwords(tempVar)
            for logFunc in self._log('read-tag-values-tx-fcoe-dwords').debug3Func(): logFunc('read txFcoeDwords. txFcoeDwords=%s, tempValue=%s', self.txFcoeDwords, tempValue.getType())
        
        if self.isRxNoBufferCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-no-buffer-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxnobuffercount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxNoBufferCount", "rx-no-buffer-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-no-buffer-count-bad-value').infoFunc(): logFunc('rxNoBufferCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxNoBufferCount(tempVar)
            for logFunc in self._log('read-tag-values-rx-no-buffer-count').debug3Func(): logFunc('read rxNoBufferCount. rxNoBufferCount=%s, tempValue=%s', self.rxNoBufferCount, tempValue.getType())
        
        if self.isRxFifoErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-fifo-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxfifoerrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxFifoErrors", "rx-fifo-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-fifo-errors-bad-value').infoFunc(): logFunc('rxFifoErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxFifoErrors(tempVar)
            for logFunc in self._log('read-tag-values-rx-fifo-errors').debug3Func(): logFunc('read rxFifoErrors. rxFifoErrors=%s, tempValue=%s', self.rxFifoErrors, tempValue.getType())
        
        if self.isAllocRxPageFailedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "alloc-rx-page-failed") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-allocrxpagefailed').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "allocRxPageFailed", "alloc-rx-page-failed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-alloc-rx-page-failed-bad-value').infoFunc(): logFunc('allocRxPageFailed not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAllocRxPageFailed(tempVar)
            for logFunc in self._log('read-tag-values-alloc-rx-page-failed').debug3Func(): logFunc('read allocRxPageFailed. allocRxPageFailed=%s, tempValue=%s', self.allocRxPageFailed, tempValue.getType())
        
        if self.isTxBusyRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-busy") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txbusy').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txBusy", "tx-busy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-busy-bad-value').infoFunc(): logFunc('txBusy not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxBusy(tempVar)
            for logFunc in self._log('read-tag-values-tx-busy').debug3Func(): logFunc('read txBusy. txBusy=%s, tempValue=%s', self.txBusy, tempValue.getType())
        
        if self.isTxAbortedErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-aborted-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txabortederrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txAbortedErrors", "tx-aborted-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-aborted-errors-bad-value').infoFunc(): logFunc('txAbortedErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxAbortedErrors(tempVar)
            for logFunc in self._log('read-tag-values-tx-aborted-errors').debug3Func(): logFunc('read txAbortedErrors. txAbortedErrors=%s, tempValue=%s', self.txAbortedErrors, tempValue.getType())
        
        if self.isCollisionsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "collisions") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-collisions').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "collisions", "collisions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-collisions-bad-value').infoFunc(): logFunc('collisions not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCollisions(tempVar)
            for logFunc in self._log('read-tag-values-collisions').debug3Func(): logFunc('read collisions. collisions=%s, tempValue=%s', self.collisions, tempValue.getType())
        
        if self.isTxHeartbeatErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-heartbeat-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txheartbeaterrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txHeartbeatErrors", "tx-heartbeat-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-heartbeat-errors-bad-value').infoFunc(): logFunc('txHeartbeatErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxHeartbeatErrors(tempVar)
            for logFunc in self._log('read-tag-values-tx-heartbeat-errors').debug3Func(): logFunc('read txHeartbeatErrors. txHeartbeatErrors=%s, tempValue=%s', self.txHeartbeatErrors, tempValue.getType())
        
        if self.isRxMissedErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-missed-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxmissederrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxMissedErrors", "rx-missed-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-missed-errors-bad-value').infoFunc(): logFunc('rxMissedErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxMissedErrors(tempVar)
            for logFunc in self._log('read-tag-values-rx-missed-errors').debug3Func(): logFunc('read rxMissedErrors. rxMissedErrors=%s, tempValue=%s', self.rxMissedErrors, tempValue.getType())
        
        if self.isNonEopDescsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "non-eop-descs") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-noneopdescs').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "nonEopDescs", "non-eop-descs", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-non-eop-descs-bad-value').infoFunc(): logFunc('nonEopDescs not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNonEopDescs(tempVar)
            for logFunc in self._log('read-tag-values-non-eop-descs').debug3Func(): logFunc('read nonEopDescs. nonEopDescs=%s, tempValue=%s', self.nonEopDescs, tempValue.getType())
        
        if self.isTxFlowControlXonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-flow-control-xon") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txflowcontrolxon').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txFlowControlXon", "tx-flow-control-xon", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-flow-control-xon-bad-value').infoFunc(): logFunc('txFlowControlXon not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxFlowControlXon(tempVar)
            for logFunc in self._log('read-tag-values-tx-flow-control-xon').debug3Func(): logFunc('read txFlowControlXon. txFlowControlXon=%s, tempValue=%s', self.txFlowControlXon, tempValue.getType())
        
        if self.isRxCsumOffloadErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-csum-offload-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxcsumoffloaderrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxCsumOffloadErrors", "rx-csum-offload-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-csum-offload-errors-bad-value').infoFunc(): logFunc('rxCsumOffloadErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxCsumOffloadErrors(tempVar)
            for logFunc in self._log('read-tag-values-rx-csum-offload-errors').debug3Func(): logFunc('read rxCsumOffloadErrors. rxCsumOffloadErrors=%s, tempValue=%s', self.rxCsumOffloadErrors, tempValue.getType())
        
        if self.isRxCrcErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-crc-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxcrcerrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxCrcErrors", "rx-crc-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-crc-errors-bad-value').infoFunc(): logFunc('rxCrcErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxCrcErrors(tempVar)
            for logFunc in self._log('read-tag-values-rx-crc-errors').debug3Func(): logFunc('read rxCrcErrors. rxCrcErrors=%s, tempValue=%s', self.rxCrcErrors, tempValue.getType())
        
        if self.isTxFifoErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-fifo-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txfifoerrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txFifoErrors", "tx-fifo-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-fifo-errors-bad-value').infoFunc(): logFunc('txFifoErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxFifoErrors(tempVar)
            for logFunc in self._log('read-tag-values-tx-fifo-errors').debug3Func(): logFunc('read txFifoErrors. txFifoErrors=%s, tempValue=%s', self.txFifoErrors, tempValue.getType())
        
        if self.isTxPktsNicRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-pkts-nic") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txpktsnic').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txPktsNic", "tx-pkts-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-pkts-nic-bad-value').infoFunc(): logFunc('txPktsNic not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxPktsNic(tempVar)
            for logFunc in self._log('read-tag-values-tx-pkts-nic').debug3Func(): logFunc('read txPktsNic. txPktsNic=%s, tempValue=%s', self.txPktsNic, tempValue.getType())
        
        if self.isRxFcoeDroppedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-fcoe-dropped") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxfcoedropped').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxFcoeDropped", "rx-fcoe-dropped", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-fcoe-dropped-bad-value').infoFunc(): logFunc('rxFcoeDropped not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxFcoeDropped(tempVar)
            for logFunc in self._log('read-tag-values-rx-fcoe-dropped').debug3Func(): logFunc('read rxFcoeDropped. rxFcoeDropped=%s, tempValue=%s', self.rxFcoeDropped, tempValue.getType())
        
        if self.isTxBytesNicRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-bytes-nic") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txbytesnic').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txBytesNic", "tx-bytes-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-bytes-nic-bad-value').infoFunc(): logFunc('txBytesNic not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxBytesNic(tempVar)
            for logFunc in self._log('read-tag-values-tx-bytes-nic').debug3Func(): logFunc('read txBytesNic. txBytesNic=%s, tempValue=%s', self.txBytesNic, tempValue.getType())
        
        if self.isAllocRxBuffFailedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "alloc-rx-buff-failed") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-allocrxbufffailed').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "allocRxBuffFailed", "alloc-rx-buff-failed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-alloc-rx-buff-failed-bad-value').infoFunc(): logFunc('allocRxBuffFailed not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAllocRxBuffFailed(tempVar)
            for logFunc in self._log('read-tag-values-alloc-rx-buff-failed').debug3Func(): logFunc('read allocRxBuffFailed. allocRxBuffFailed=%s, tempValue=%s', self.allocRxBuffFailed, tempValue.getType())
        
        if self.isFcoeBadFccrcRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "fcoe-bad-fccrc") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-fcoebadfccrc').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fcoeBadFccrc", "fcoe-bad-fccrc", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-fcoe-bad-fccrc-bad-value').infoFunc(): logFunc('fcoeBadFccrc not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFcoeBadFccrc(tempVar)
            for logFunc in self._log('read-tag-values-fcoe-bad-fccrc').debug3Func(): logFunc('read fcoeBadFccrc. fcoeBadFccrc=%s, tempValue=%s', self.fcoeBadFccrc, tempValue.getType())
        
        if self.isTxFlowControlXoffRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-flow-control-xoff") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txflowcontrolxoff').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txFlowControlXoff", "tx-flow-control-xoff", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-flow-control-xoff-bad-value').infoFunc(): logFunc('txFlowControlXoff not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxFlowControlXoff(tempVar)
            for logFunc in self._log('read-tag-values-tx-flow-control-xoff').debug3Func(): logFunc('read txFlowControlXoff. txFlowControlXoff=%s, tempValue=%s', self.txFlowControlXoff, tempValue.getType())
        
        if self.isTxTimeoutCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-timeout-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txtimeoutcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txTimeoutCount", "tx-timeout-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-timeout-count-bad-value').infoFunc(): logFunc('txTimeoutCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxTimeoutCount(tempVar)
            for logFunc in self._log('read-tag-values-tx-timeout-count').debug3Func(): logFunc('read txTimeoutCount. txTimeoutCount=%s, tempValue=%s', self.txTimeoutCount, tempValue.getType())
        
        if self.isTxCarrierErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-carrier-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txcarriererrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txCarrierErrors", "tx-carrier-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-carrier-errors-bad-value').infoFunc(): logFunc('txCarrierErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxCarrierErrors(tempVar)
            for logFunc in self._log('read-tag-values-tx-carrier-errors').debug3Func(): logFunc('read txCarrierErrors. txCarrierErrors=%s, tempValue=%s', self.txCarrierErrors, tempValue.getType())
        
        if self.isRxFlowControlXoffRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-flow-control-xoff") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxflowcontrolxoff').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxFlowControlXoff", "rx-flow-control-xoff", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-flow-control-xoff-bad-value').infoFunc(): logFunc('rxFlowControlXoff not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxFlowControlXoff(tempVar)
            for logFunc in self._log('read-tag-values-rx-flow-control-xoff').debug3Func(): logFunc('read rxFlowControlXoff. rxFlowControlXoff=%s, tempValue=%s', self.rxFlowControlXoff, tempValue.getType())
        
        if self.isFdirMissRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "fdir-miss") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-fdirmiss').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fdirMiss", "fdir-miss", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-fdir-miss-bad-value').infoFunc(): logFunc('fdirMiss not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFdirMiss(tempVar)
            for logFunc in self._log('read-tag-values-fdir-miss').debug3Func(): logFunc('read fdirMiss. fdirMiss=%s, tempValue=%s', self.fdirMiss, tempValue.getType())
        
        if self.isRxNoDmaResourcesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-no-dma-resources") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxnodmaresources').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxNoDmaResources", "rx-no-dma-resources", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-no-dma-resources-bad-value').infoFunc(): logFunc('rxNoDmaResources not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxNoDmaResources(tempVar)
            for logFunc in self._log('read-tag-values-rx-no-dma-resources').debug3Func(): logFunc('read rxNoDmaResources. rxNoDmaResources=%s, tempValue=%s', self.rxNoDmaResources, tempValue.getType())
        
        if self.isRxOverErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-over-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxovererrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxOverErrors", "rx-over-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-over-errors-bad-value').infoFunc(): logFunc('rxOverErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxOverErrors(tempVar)
            for logFunc in self._log('read-tag-values-rx-over-errors').debug3Func(): logFunc('read rxOverErrors. rxOverErrors=%s, tempValue=%s', self.rxOverErrors, tempValue.getType())
        
        if self.isRxFlowControlXonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-flow-control-xon") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxflowcontrolxon').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxFlowControlXon", "rx-flow-control-xon", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-flow-control-xon-bad-value').infoFunc(): logFunc('rxFlowControlXon not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxFlowControlXon(tempVar)
            for logFunc in self._log('read-tag-values-rx-flow-control-xon').debug3Func(): logFunc('read rxFlowControlXon. rxFlowControlXon=%s, tempValue=%s', self.rxFlowControlXon, tempValue.getType())
        
        if self.isTxRestartQueueRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tx-restart-queue") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-txrestartqueue').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "txRestartQueue", "tx-restart-queue", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tx-restart-queue-bad-value').infoFunc(): logFunc('txRestartQueue not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTxRestartQueue(tempVar)
            for logFunc in self._log('read-tag-values-tx-restart-queue').debug3Func(): logFunc('read txRestartQueue. txRestartQueue=%s, tempValue=%s', self.txRestartQueue, tempValue.getType())
        
        if self.isRxFrameErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-frame-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxframeerrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxFrameErrors", "rx-frame-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-frame-errors-bad-value').infoFunc(): logFunc('rxFrameErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxFrameErrors(tempVar)
            for logFunc in self._log('read-tag-values-rx-frame-errors').debug3Func(): logFunc('read rxFrameErrors. rxFrameErrors=%s, tempValue=%s', self.rxFrameErrors, tempValue.getType())
        
        if self.isRxPktsNicRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rx-pkts-nic") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rxpktsnic').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rxPktsNic", "rx-pkts-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rx-pkts-nic-bad-value').infoFunc(): logFunc('rxPktsNic not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRxPktsNic(tempVar)
            for logFunc in self._log('read-tag-values-rx-pkts-nic').debug3Func(): logFunc('read rxPktsNic. rxPktsNic=%s, tempValue=%s', self.rxPktsNic, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "device", 
            "namespace": "device", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "device"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "hwRscFlushed", 
            "yangName": "hw-rsc-flushed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "lscInt", 
            "yangName": "lsc-int", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "hwRscAggregated", 
            "yangName": "hw-rsc-aggregated", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxLongLengthErrors", 
            "yangName": "rx-long-length-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fdirMatch", 
            "yangName": "fdir-match", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFcoePackets", 
            "yangName": "tx-fcoe-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxShortLengthErrors", 
            "yangName": "rx-short-length-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFcoeDwords", 
            "yangName": "rx-fcoe-dwords", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxBytesNic", 
            "yangName": "rx-bytes-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFcoePackets", 
            "yangName": "rx-fcoe-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFcoeDwords", 
            "yangName": "tx-fcoe-dwords", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxNoBufferCount", 
            "yangName": "rx-no-buffer-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFifoErrors", 
            "yangName": "rx-fifo-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "allocRxPageFailed", 
            "yangName": "alloc-rx-page-failed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txBusy", 
            "yangName": "tx-busy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txAbortedErrors", 
            "yangName": "tx-aborted-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "collisions", 
            "yangName": "collisions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txHeartbeatErrors", 
            "yangName": "tx-heartbeat-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxMissedErrors", 
            "yangName": "rx-missed-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "nonEopDescs", 
            "yangName": "non-eop-descs", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFlowControlXon", 
            "yangName": "tx-flow-control-xon", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxCsumOffloadErrors", 
            "yangName": "rx-csum-offload-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxCrcErrors", 
            "yangName": "rx-crc-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFifoErrors", 
            "yangName": "tx-fifo-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txPktsNic", 
            "yangName": "tx-pkts-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFcoeDropped", 
            "yangName": "rx-fcoe-dropped", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txBytesNic", 
            "yangName": "tx-bytes-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "allocRxBuffFailed", 
            "yangName": "alloc-rx-buff-failed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fcoeBadFccrc", 
            "yangName": "fcoe-bad-fccrc", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFlowControlXoff", 
            "yangName": "tx-flow-control-xoff", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txTimeoutCount", 
            "yangName": "tx-timeout-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txCarrierErrors", 
            "yangName": "tx-carrier-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFlowControlXoff", 
            "yangName": "rx-flow-control-xoff", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fdirMiss", 
            "yangName": "fdir-miss", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxNoDmaResources", 
            "yangName": "rx-no-dma-resources", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxOverErrors", 
            "yangName": "rx-over-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFlowControlXon", 
            "yangName": "rx-flow-control-xon", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txRestartQueue", 
            "yangName": "tx-restart-queue", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFrameErrors", 
            "yangName": "rx-frame-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxPktsNic", 
            "yangName": "rx-pkts-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "hwRscFlushed", 
            "yangName": "hw-rsc-flushed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "lscInt", 
            "yangName": "lsc-int", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "hwRscAggregated", 
            "yangName": "hw-rsc-aggregated", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxLongLengthErrors", 
            "yangName": "rx-long-length-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fdirMatch", 
            "yangName": "fdir-match", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFcoePackets", 
            "yangName": "tx-fcoe-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxShortLengthErrors", 
            "yangName": "rx-short-length-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFcoeDwords", 
            "yangName": "rx-fcoe-dwords", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxBytesNic", 
            "yangName": "rx-bytes-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFcoePackets", 
            "yangName": "rx-fcoe-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFcoeDwords", 
            "yangName": "tx-fcoe-dwords", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxNoBufferCount", 
            "yangName": "rx-no-buffer-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFifoErrors", 
            "yangName": "rx-fifo-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "allocRxPageFailed", 
            "yangName": "alloc-rx-page-failed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txBusy", 
            "yangName": "tx-busy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txAbortedErrors", 
            "yangName": "tx-aborted-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "collisions", 
            "yangName": "collisions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txHeartbeatErrors", 
            "yangName": "tx-heartbeat-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxMissedErrors", 
            "yangName": "rx-missed-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "nonEopDescs", 
            "yangName": "non-eop-descs", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFlowControlXon", 
            "yangName": "tx-flow-control-xon", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxCsumOffloadErrors", 
            "yangName": "rx-csum-offload-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxCrcErrors", 
            "yangName": "rx-crc-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFifoErrors", 
            "yangName": "tx-fifo-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txPktsNic", 
            "yangName": "tx-pkts-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFcoeDropped", 
            "yangName": "rx-fcoe-dropped", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txBytesNic", 
            "yangName": "tx-bytes-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "allocRxBuffFailed", 
            "yangName": "alloc-rx-buff-failed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fcoeBadFccrc", 
            "yangName": "fcoe-bad-fccrc", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFlowControlXoff", 
            "yangName": "tx-flow-control-xoff", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txTimeoutCount", 
            "yangName": "tx-timeout-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txCarrierErrors", 
            "yangName": "tx-carrier-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFlowControlXoff", 
            "yangName": "rx-flow-control-xoff", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fdirMiss", 
            "yangName": "fdir-miss", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxNoDmaResources", 
            "yangName": "rx-no-dma-resources", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxOverErrors", 
            "yangName": "rx-over-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFlowControlXon", 
            "yangName": "rx-flow-control-xon", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "txRestartQueue", 
            "yangName": "tx-restart-queue", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFrameErrors", 
            "yangName": "rx-frame-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxPktsNic", 
            "yangName": "rx-pkts-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


