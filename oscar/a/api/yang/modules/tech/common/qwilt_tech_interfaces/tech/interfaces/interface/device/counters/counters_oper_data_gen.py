


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperData
__pychecker__="no-classattr"

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket





class CountersOperData (object):

    def __init__ (self):

        self.hwRscFlushed = 0
        self._myHasHwRscFlushed=False
        self._myHwRscFlushedRequested=False
        
        self.lscInt = 0
        self._myHasLscInt=False
        self._myLscIntRequested=False
        
        self.hwRscAggregated = 0
        self._myHasHwRscAggregated=False
        self._myHwRscAggregatedRequested=False
        
        self.rxLongLengthErrors = 0
        self._myHasRxLongLengthErrors=False
        self._myRxLongLengthErrorsRequested=False
        
        self.fdirMatch = 0
        self._myHasFdirMatch=False
        self._myFdirMatchRequested=False
        
        self.txFcoePackets = 0
        self._myHasTxFcoePackets=False
        self._myTxFcoePacketsRequested=False
        
        self.rxShortLengthErrors = 0
        self._myHasRxShortLengthErrors=False
        self._myRxShortLengthErrorsRequested=False
        
        self.rxFcoeDwords = 0
        self._myHasRxFcoeDwords=False
        self._myRxFcoeDwordsRequested=False
        
        self.rxBytesNic = 0
        self._myHasRxBytesNic=False
        self._myRxBytesNicRequested=False
        
        self.rxFcoePackets = 0
        self._myHasRxFcoePackets=False
        self._myRxFcoePacketsRequested=False
        
        self.txFcoeDwords = 0
        self._myHasTxFcoeDwords=False
        self._myTxFcoeDwordsRequested=False
        
        self.rxNoBufferCount = 0
        self._myHasRxNoBufferCount=False
        self._myRxNoBufferCountRequested=False
        
        self.rxFifoErrors = 0
        self._myHasRxFifoErrors=False
        self._myRxFifoErrorsRequested=False
        
        self.allocRxPageFailed = 0
        self._myHasAllocRxPageFailed=False
        self._myAllocRxPageFailedRequested=False
        
        self.txBusy = 0
        self._myHasTxBusy=False
        self._myTxBusyRequested=False
        
        self.txAbortedErrors = 0
        self._myHasTxAbortedErrors=False
        self._myTxAbortedErrorsRequested=False
        
        self.collisions = 0
        self._myHasCollisions=False
        self._myCollisionsRequested=False
        
        self.txHeartbeatErrors = 0
        self._myHasTxHeartbeatErrors=False
        self._myTxHeartbeatErrorsRequested=False
        
        self.rxMissedErrors = 0
        self._myHasRxMissedErrors=False
        self._myRxMissedErrorsRequested=False
        
        self.nonEopDescs = 0
        self._myHasNonEopDescs=False
        self._myNonEopDescsRequested=False
        
        self.txFlowControlXon = 0
        self._myHasTxFlowControlXon=False
        self._myTxFlowControlXonRequested=False
        
        self.rxCsumOffloadErrors = 0
        self._myHasRxCsumOffloadErrors=False
        self._myRxCsumOffloadErrorsRequested=False
        
        self.rxCrcErrors = 0
        self._myHasRxCrcErrors=False
        self._myRxCrcErrorsRequested=False
        
        self.txFifoErrors = 0
        self._myHasTxFifoErrors=False
        self._myTxFifoErrorsRequested=False
        
        self.txPktsNic = 0
        self._myHasTxPktsNic=False
        self._myTxPktsNicRequested=False
        
        self.rxFcoeDropped = 0
        self._myHasRxFcoeDropped=False
        self._myRxFcoeDroppedRequested=False
        
        self.txBytesNic = 0
        self._myHasTxBytesNic=False
        self._myTxBytesNicRequested=False
        
        self.allocRxBuffFailed = 0
        self._myHasAllocRxBuffFailed=False
        self._myAllocRxBuffFailedRequested=False
        
        self.fcoeBadFccrc = 0
        self._myHasFcoeBadFccrc=False
        self._myFcoeBadFccrcRequested=False
        
        self.txFlowControlXoff = 0
        self._myHasTxFlowControlXoff=False
        self._myTxFlowControlXoffRequested=False
        
        self.txTimeoutCount = 0
        self._myHasTxTimeoutCount=False
        self._myTxTimeoutCountRequested=False
        
        self.txCarrierErrors = 0
        self._myHasTxCarrierErrors=False
        self._myTxCarrierErrorsRequested=False
        
        self.rxFlowControlXoff = 0
        self._myHasRxFlowControlXoff=False
        self._myRxFlowControlXoffRequested=False
        
        self.fdirMiss = 0
        self._myHasFdirMiss=False
        self._myFdirMissRequested=False
        
        self.rxNoDmaResources = 0
        self._myHasRxNoDmaResources=False
        self._myRxNoDmaResourcesRequested=False
        
        self.rxOverErrors = 0
        self._myHasRxOverErrors=False
        self._myRxOverErrorsRequested=False
        
        self.rxFlowControlXon = 0
        self._myHasRxFlowControlXon=False
        self._myRxFlowControlXonRequested=False
        
        self.txRestartQueue = 0
        self._myHasTxRestartQueue=False
        self._myTxRestartQueueRequested=False
        
        self.rxFrameErrors = 0
        self._myHasRxFrameErrors=False
        self._myRxFrameErrorsRequested=False
        
        self.rxPktsNic = 0
        self._myHasRxPktsNic=False
        self._myRxPktsNicRequested=False
        


    def copyFrom (self, other):

        self.hwRscFlushed=other.hwRscFlushed
        self._myHasHwRscFlushed=other._myHasHwRscFlushed
        self._myHwRscFlushedRequested=other._myHwRscFlushedRequested
        
        self.lscInt=other.lscInt
        self._myHasLscInt=other._myHasLscInt
        self._myLscIntRequested=other._myLscIntRequested
        
        self.hwRscAggregated=other.hwRscAggregated
        self._myHasHwRscAggregated=other._myHasHwRscAggregated
        self._myHwRscAggregatedRequested=other._myHwRscAggregatedRequested
        
        self.rxLongLengthErrors=other.rxLongLengthErrors
        self._myHasRxLongLengthErrors=other._myHasRxLongLengthErrors
        self._myRxLongLengthErrorsRequested=other._myRxLongLengthErrorsRequested
        
        self.fdirMatch=other.fdirMatch
        self._myHasFdirMatch=other._myHasFdirMatch
        self._myFdirMatchRequested=other._myFdirMatchRequested
        
        self.txFcoePackets=other.txFcoePackets
        self._myHasTxFcoePackets=other._myHasTxFcoePackets
        self._myTxFcoePacketsRequested=other._myTxFcoePacketsRequested
        
        self.rxShortLengthErrors=other.rxShortLengthErrors
        self._myHasRxShortLengthErrors=other._myHasRxShortLengthErrors
        self._myRxShortLengthErrorsRequested=other._myRxShortLengthErrorsRequested
        
        self.rxFcoeDwords=other.rxFcoeDwords
        self._myHasRxFcoeDwords=other._myHasRxFcoeDwords
        self._myRxFcoeDwordsRequested=other._myRxFcoeDwordsRequested
        
        self.rxBytesNic=other.rxBytesNic
        self._myHasRxBytesNic=other._myHasRxBytesNic
        self._myRxBytesNicRequested=other._myRxBytesNicRequested
        
        self.rxFcoePackets=other.rxFcoePackets
        self._myHasRxFcoePackets=other._myHasRxFcoePackets
        self._myRxFcoePacketsRequested=other._myRxFcoePacketsRequested
        
        self.txFcoeDwords=other.txFcoeDwords
        self._myHasTxFcoeDwords=other._myHasTxFcoeDwords
        self._myTxFcoeDwordsRequested=other._myTxFcoeDwordsRequested
        
        self.rxNoBufferCount=other.rxNoBufferCount
        self._myHasRxNoBufferCount=other._myHasRxNoBufferCount
        self._myRxNoBufferCountRequested=other._myRxNoBufferCountRequested
        
        self.rxFifoErrors=other.rxFifoErrors
        self._myHasRxFifoErrors=other._myHasRxFifoErrors
        self._myRxFifoErrorsRequested=other._myRxFifoErrorsRequested
        
        self.allocRxPageFailed=other.allocRxPageFailed
        self._myHasAllocRxPageFailed=other._myHasAllocRxPageFailed
        self._myAllocRxPageFailedRequested=other._myAllocRxPageFailedRequested
        
        self.txBusy=other.txBusy
        self._myHasTxBusy=other._myHasTxBusy
        self._myTxBusyRequested=other._myTxBusyRequested
        
        self.txAbortedErrors=other.txAbortedErrors
        self._myHasTxAbortedErrors=other._myHasTxAbortedErrors
        self._myTxAbortedErrorsRequested=other._myTxAbortedErrorsRequested
        
        self.collisions=other.collisions
        self._myHasCollisions=other._myHasCollisions
        self._myCollisionsRequested=other._myCollisionsRequested
        
        self.txHeartbeatErrors=other.txHeartbeatErrors
        self._myHasTxHeartbeatErrors=other._myHasTxHeartbeatErrors
        self._myTxHeartbeatErrorsRequested=other._myTxHeartbeatErrorsRequested
        
        self.rxMissedErrors=other.rxMissedErrors
        self._myHasRxMissedErrors=other._myHasRxMissedErrors
        self._myRxMissedErrorsRequested=other._myRxMissedErrorsRequested
        
        self.nonEopDescs=other.nonEopDescs
        self._myHasNonEopDescs=other._myHasNonEopDescs
        self._myNonEopDescsRequested=other._myNonEopDescsRequested
        
        self.txFlowControlXon=other.txFlowControlXon
        self._myHasTxFlowControlXon=other._myHasTxFlowControlXon
        self._myTxFlowControlXonRequested=other._myTxFlowControlXonRequested
        
        self.rxCsumOffloadErrors=other.rxCsumOffloadErrors
        self._myHasRxCsumOffloadErrors=other._myHasRxCsumOffloadErrors
        self._myRxCsumOffloadErrorsRequested=other._myRxCsumOffloadErrorsRequested
        
        self.rxCrcErrors=other.rxCrcErrors
        self._myHasRxCrcErrors=other._myHasRxCrcErrors
        self._myRxCrcErrorsRequested=other._myRxCrcErrorsRequested
        
        self.txFifoErrors=other.txFifoErrors
        self._myHasTxFifoErrors=other._myHasTxFifoErrors
        self._myTxFifoErrorsRequested=other._myTxFifoErrorsRequested
        
        self.txPktsNic=other.txPktsNic
        self._myHasTxPktsNic=other._myHasTxPktsNic
        self._myTxPktsNicRequested=other._myTxPktsNicRequested
        
        self.rxFcoeDropped=other.rxFcoeDropped
        self._myHasRxFcoeDropped=other._myHasRxFcoeDropped
        self._myRxFcoeDroppedRequested=other._myRxFcoeDroppedRequested
        
        self.txBytesNic=other.txBytesNic
        self._myHasTxBytesNic=other._myHasTxBytesNic
        self._myTxBytesNicRequested=other._myTxBytesNicRequested
        
        self.allocRxBuffFailed=other.allocRxBuffFailed
        self._myHasAllocRxBuffFailed=other._myHasAllocRxBuffFailed
        self._myAllocRxBuffFailedRequested=other._myAllocRxBuffFailedRequested
        
        self.fcoeBadFccrc=other.fcoeBadFccrc
        self._myHasFcoeBadFccrc=other._myHasFcoeBadFccrc
        self._myFcoeBadFccrcRequested=other._myFcoeBadFccrcRequested
        
        self.txFlowControlXoff=other.txFlowControlXoff
        self._myHasTxFlowControlXoff=other._myHasTxFlowControlXoff
        self._myTxFlowControlXoffRequested=other._myTxFlowControlXoffRequested
        
        self.txTimeoutCount=other.txTimeoutCount
        self._myHasTxTimeoutCount=other._myHasTxTimeoutCount
        self._myTxTimeoutCountRequested=other._myTxTimeoutCountRequested
        
        self.txCarrierErrors=other.txCarrierErrors
        self._myHasTxCarrierErrors=other._myHasTxCarrierErrors
        self._myTxCarrierErrorsRequested=other._myTxCarrierErrorsRequested
        
        self.rxFlowControlXoff=other.rxFlowControlXoff
        self._myHasRxFlowControlXoff=other._myHasRxFlowControlXoff
        self._myRxFlowControlXoffRequested=other._myRxFlowControlXoffRequested
        
        self.fdirMiss=other.fdirMiss
        self._myHasFdirMiss=other._myHasFdirMiss
        self._myFdirMissRequested=other._myFdirMissRequested
        
        self.rxNoDmaResources=other.rxNoDmaResources
        self._myHasRxNoDmaResources=other._myHasRxNoDmaResources
        self._myRxNoDmaResourcesRequested=other._myRxNoDmaResourcesRequested
        
        self.rxOverErrors=other.rxOverErrors
        self._myHasRxOverErrors=other._myHasRxOverErrors
        self._myRxOverErrorsRequested=other._myRxOverErrorsRequested
        
        self.rxFlowControlXon=other.rxFlowControlXon
        self._myHasRxFlowControlXon=other._myHasRxFlowControlXon
        self._myRxFlowControlXonRequested=other._myRxFlowControlXonRequested
        
        self.txRestartQueue=other.txRestartQueue
        self._myHasTxRestartQueue=other._myHasTxRestartQueue
        self._myTxRestartQueueRequested=other._myTxRestartQueueRequested
        
        self.rxFrameErrors=other.rxFrameErrors
        self._myHasRxFrameErrors=other._myHasRxFrameErrors
        self._myRxFrameErrorsRequested=other._myRxFrameErrorsRequested
        
        self.rxPktsNic=other.rxPktsNic
        self._myHasRxPktsNic=other._myHasRxPktsNic
        self._myRxPktsNicRequested=other._myRxPktsNicRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isHwRscFlushedRequested():
            self.hwRscFlushed=other.hwRscFlushed
            self._myHasHwRscFlushed=other._myHasHwRscFlushed
            self._myHwRscFlushedRequested=other._myHwRscFlushedRequested
        
        if self.isLscIntRequested():
            self.lscInt=other.lscInt
            self._myHasLscInt=other._myHasLscInt
            self._myLscIntRequested=other._myLscIntRequested
        
        if self.isHwRscAggregatedRequested():
            self.hwRscAggregated=other.hwRscAggregated
            self._myHasHwRscAggregated=other._myHasHwRscAggregated
            self._myHwRscAggregatedRequested=other._myHwRscAggregatedRequested
        
        if self.isRxLongLengthErrorsRequested():
            self.rxLongLengthErrors=other.rxLongLengthErrors
            self._myHasRxLongLengthErrors=other._myHasRxLongLengthErrors
            self._myRxLongLengthErrorsRequested=other._myRxLongLengthErrorsRequested
        
        if self.isFdirMatchRequested():
            self.fdirMatch=other.fdirMatch
            self._myHasFdirMatch=other._myHasFdirMatch
            self._myFdirMatchRequested=other._myFdirMatchRequested
        
        if self.isTxFcoePacketsRequested():
            self.txFcoePackets=other.txFcoePackets
            self._myHasTxFcoePackets=other._myHasTxFcoePackets
            self._myTxFcoePacketsRequested=other._myTxFcoePacketsRequested
        
        if self.isRxShortLengthErrorsRequested():
            self.rxShortLengthErrors=other.rxShortLengthErrors
            self._myHasRxShortLengthErrors=other._myHasRxShortLengthErrors
            self._myRxShortLengthErrorsRequested=other._myRxShortLengthErrorsRequested
        
        if self.isRxFcoeDwordsRequested():
            self.rxFcoeDwords=other.rxFcoeDwords
            self._myHasRxFcoeDwords=other._myHasRxFcoeDwords
            self._myRxFcoeDwordsRequested=other._myRxFcoeDwordsRequested
        
        if self.isRxBytesNicRequested():
            self.rxBytesNic=other.rxBytesNic
            self._myHasRxBytesNic=other._myHasRxBytesNic
            self._myRxBytesNicRequested=other._myRxBytesNicRequested
        
        if self.isRxFcoePacketsRequested():
            self.rxFcoePackets=other.rxFcoePackets
            self._myHasRxFcoePackets=other._myHasRxFcoePackets
            self._myRxFcoePacketsRequested=other._myRxFcoePacketsRequested
        
        if self.isTxFcoeDwordsRequested():
            self.txFcoeDwords=other.txFcoeDwords
            self._myHasTxFcoeDwords=other._myHasTxFcoeDwords
            self._myTxFcoeDwordsRequested=other._myTxFcoeDwordsRequested
        
        if self.isRxNoBufferCountRequested():
            self.rxNoBufferCount=other.rxNoBufferCount
            self._myHasRxNoBufferCount=other._myHasRxNoBufferCount
            self._myRxNoBufferCountRequested=other._myRxNoBufferCountRequested
        
        if self.isRxFifoErrorsRequested():
            self.rxFifoErrors=other.rxFifoErrors
            self._myHasRxFifoErrors=other._myHasRxFifoErrors
            self._myRxFifoErrorsRequested=other._myRxFifoErrorsRequested
        
        if self.isAllocRxPageFailedRequested():
            self.allocRxPageFailed=other.allocRxPageFailed
            self._myHasAllocRxPageFailed=other._myHasAllocRxPageFailed
            self._myAllocRxPageFailedRequested=other._myAllocRxPageFailedRequested
        
        if self.isTxBusyRequested():
            self.txBusy=other.txBusy
            self._myHasTxBusy=other._myHasTxBusy
            self._myTxBusyRequested=other._myTxBusyRequested
        
        if self.isTxAbortedErrorsRequested():
            self.txAbortedErrors=other.txAbortedErrors
            self._myHasTxAbortedErrors=other._myHasTxAbortedErrors
            self._myTxAbortedErrorsRequested=other._myTxAbortedErrorsRequested
        
        if self.isCollisionsRequested():
            self.collisions=other.collisions
            self._myHasCollisions=other._myHasCollisions
            self._myCollisionsRequested=other._myCollisionsRequested
        
        if self.isTxHeartbeatErrorsRequested():
            self.txHeartbeatErrors=other.txHeartbeatErrors
            self._myHasTxHeartbeatErrors=other._myHasTxHeartbeatErrors
            self._myTxHeartbeatErrorsRequested=other._myTxHeartbeatErrorsRequested
        
        if self.isRxMissedErrorsRequested():
            self.rxMissedErrors=other.rxMissedErrors
            self._myHasRxMissedErrors=other._myHasRxMissedErrors
            self._myRxMissedErrorsRequested=other._myRxMissedErrorsRequested
        
        if self.isNonEopDescsRequested():
            self.nonEopDescs=other.nonEopDescs
            self._myHasNonEopDescs=other._myHasNonEopDescs
            self._myNonEopDescsRequested=other._myNonEopDescsRequested
        
        if self.isTxFlowControlXonRequested():
            self.txFlowControlXon=other.txFlowControlXon
            self._myHasTxFlowControlXon=other._myHasTxFlowControlXon
            self._myTxFlowControlXonRequested=other._myTxFlowControlXonRequested
        
        if self.isRxCsumOffloadErrorsRequested():
            self.rxCsumOffloadErrors=other.rxCsumOffloadErrors
            self._myHasRxCsumOffloadErrors=other._myHasRxCsumOffloadErrors
            self._myRxCsumOffloadErrorsRequested=other._myRxCsumOffloadErrorsRequested
        
        if self.isRxCrcErrorsRequested():
            self.rxCrcErrors=other.rxCrcErrors
            self._myHasRxCrcErrors=other._myHasRxCrcErrors
            self._myRxCrcErrorsRequested=other._myRxCrcErrorsRequested
        
        if self.isTxFifoErrorsRequested():
            self.txFifoErrors=other.txFifoErrors
            self._myHasTxFifoErrors=other._myHasTxFifoErrors
            self._myTxFifoErrorsRequested=other._myTxFifoErrorsRequested
        
        if self.isTxPktsNicRequested():
            self.txPktsNic=other.txPktsNic
            self._myHasTxPktsNic=other._myHasTxPktsNic
            self._myTxPktsNicRequested=other._myTxPktsNicRequested
        
        if self.isRxFcoeDroppedRequested():
            self.rxFcoeDropped=other.rxFcoeDropped
            self._myHasRxFcoeDropped=other._myHasRxFcoeDropped
            self._myRxFcoeDroppedRequested=other._myRxFcoeDroppedRequested
        
        if self.isTxBytesNicRequested():
            self.txBytesNic=other.txBytesNic
            self._myHasTxBytesNic=other._myHasTxBytesNic
            self._myTxBytesNicRequested=other._myTxBytesNicRequested
        
        if self.isAllocRxBuffFailedRequested():
            self.allocRxBuffFailed=other.allocRxBuffFailed
            self._myHasAllocRxBuffFailed=other._myHasAllocRxBuffFailed
            self._myAllocRxBuffFailedRequested=other._myAllocRxBuffFailedRequested
        
        if self.isFcoeBadFccrcRequested():
            self.fcoeBadFccrc=other.fcoeBadFccrc
            self._myHasFcoeBadFccrc=other._myHasFcoeBadFccrc
            self._myFcoeBadFccrcRequested=other._myFcoeBadFccrcRequested
        
        if self.isTxFlowControlXoffRequested():
            self.txFlowControlXoff=other.txFlowControlXoff
            self._myHasTxFlowControlXoff=other._myHasTxFlowControlXoff
            self._myTxFlowControlXoffRequested=other._myTxFlowControlXoffRequested
        
        if self.isTxTimeoutCountRequested():
            self.txTimeoutCount=other.txTimeoutCount
            self._myHasTxTimeoutCount=other._myHasTxTimeoutCount
            self._myTxTimeoutCountRequested=other._myTxTimeoutCountRequested
        
        if self.isTxCarrierErrorsRequested():
            self.txCarrierErrors=other.txCarrierErrors
            self._myHasTxCarrierErrors=other._myHasTxCarrierErrors
            self._myTxCarrierErrorsRequested=other._myTxCarrierErrorsRequested
        
        if self.isRxFlowControlXoffRequested():
            self.rxFlowControlXoff=other.rxFlowControlXoff
            self._myHasRxFlowControlXoff=other._myHasRxFlowControlXoff
            self._myRxFlowControlXoffRequested=other._myRxFlowControlXoffRequested
        
        if self.isFdirMissRequested():
            self.fdirMiss=other.fdirMiss
            self._myHasFdirMiss=other._myHasFdirMiss
            self._myFdirMissRequested=other._myFdirMissRequested
        
        if self.isRxNoDmaResourcesRequested():
            self.rxNoDmaResources=other.rxNoDmaResources
            self._myHasRxNoDmaResources=other._myHasRxNoDmaResources
            self._myRxNoDmaResourcesRequested=other._myRxNoDmaResourcesRequested
        
        if self.isRxOverErrorsRequested():
            self.rxOverErrors=other.rxOverErrors
            self._myHasRxOverErrors=other._myHasRxOverErrors
            self._myRxOverErrorsRequested=other._myRxOverErrorsRequested
        
        if self.isRxFlowControlXonRequested():
            self.rxFlowControlXon=other.rxFlowControlXon
            self._myHasRxFlowControlXon=other._myHasRxFlowControlXon
            self._myRxFlowControlXonRequested=other._myRxFlowControlXonRequested
        
        if self.isTxRestartQueueRequested():
            self.txRestartQueue=other.txRestartQueue
            self._myHasTxRestartQueue=other._myHasTxRestartQueue
            self._myTxRestartQueueRequested=other._myTxRestartQueueRequested
        
        if self.isRxFrameErrorsRequested():
            self.rxFrameErrors=other.rxFrameErrors
            self._myHasRxFrameErrors=other._myHasRxFrameErrors
            self._myRxFrameErrorsRequested=other._myRxFrameErrorsRequested
        
        if self.isRxPktsNicRequested():
            self.rxPktsNic=other.rxPktsNic
            self._myHasRxPktsNic=other._myHasRxPktsNic
            self._myRxPktsNicRequested=other._myRxPktsNicRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasHwRscFlushed():
            self.hwRscFlushed=other.hwRscFlushed
            self._myHasHwRscFlushed=other._myHasHwRscFlushed
            self._myHwRscFlushedRequested=other._myHwRscFlushedRequested
        
        if other.hasLscInt():
            self.lscInt=other.lscInt
            self._myHasLscInt=other._myHasLscInt
            self._myLscIntRequested=other._myLscIntRequested
        
        if other.hasHwRscAggregated():
            self.hwRscAggregated=other.hwRscAggregated
            self._myHasHwRscAggregated=other._myHasHwRscAggregated
            self._myHwRscAggregatedRequested=other._myHwRscAggregatedRequested
        
        if other.hasRxLongLengthErrors():
            self.rxLongLengthErrors=other.rxLongLengthErrors
            self._myHasRxLongLengthErrors=other._myHasRxLongLengthErrors
            self._myRxLongLengthErrorsRequested=other._myRxLongLengthErrorsRequested
        
        if other.hasFdirMatch():
            self.fdirMatch=other.fdirMatch
            self._myHasFdirMatch=other._myHasFdirMatch
            self._myFdirMatchRequested=other._myFdirMatchRequested
        
        if other.hasTxFcoePackets():
            self.txFcoePackets=other.txFcoePackets
            self._myHasTxFcoePackets=other._myHasTxFcoePackets
            self._myTxFcoePacketsRequested=other._myTxFcoePacketsRequested
        
        if other.hasRxShortLengthErrors():
            self.rxShortLengthErrors=other.rxShortLengthErrors
            self._myHasRxShortLengthErrors=other._myHasRxShortLengthErrors
            self._myRxShortLengthErrorsRequested=other._myRxShortLengthErrorsRequested
        
        if other.hasRxFcoeDwords():
            self.rxFcoeDwords=other.rxFcoeDwords
            self._myHasRxFcoeDwords=other._myHasRxFcoeDwords
            self._myRxFcoeDwordsRequested=other._myRxFcoeDwordsRequested
        
        if other.hasRxBytesNic():
            self.rxBytesNic=other.rxBytesNic
            self._myHasRxBytesNic=other._myHasRxBytesNic
            self._myRxBytesNicRequested=other._myRxBytesNicRequested
        
        if other.hasRxFcoePackets():
            self.rxFcoePackets=other.rxFcoePackets
            self._myHasRxFcoePackets=other._myHasRxFcoePackets
            self._myRxFcoePacketsRequested=other._myRxFcoePacketsRequested
        
        if other.hasTxFcoeDwords():
            self.txFcoeDwords=other.txFcoeDwords
            self._myHasTxFcoeDwords=other._myHasTxFcoeDwords
            self._myTxFcoeDwordsRequested=other._myTxFcoeDwordsRequested
        
        if other.hasRxNoBufferCount():
            self.rxNoBufferCount=other.rxNoBufferCount
            self._myHasRxNoBufferCount=other._myHasRxNoBufferCount
            self._myRxNoBufferCountRequested=other._myRxNoBufferCountRequested
        
        if other.hasRxFifoErrors():
            self.rxFifoErrors=other.rxFifoErrors
            self._myHasRxFifoErrors=other._myHasRxFifoErrors
            self._myRxFifoErrorsRequested=other._myRxFifoErrorsRequested
        
        if other.hasAllocRxPageFailed():
            self.allocRxPageFailed=other.allocRxPageFailed
            self._myHasAllocRxPageFailed=other._myHasAllocRxPageFailed
            self._myAllocRxPageFailedRequested=other._myAllocRxPageFailedRequested
        
        if other.hasTxBusy():
            self.txBusy=other.txBusy
            self._myHasTxBusy=other._myHasTxBusy
            self._myTxBusyRequested=other._myTxBusyRequested
        
        if other.hasTxAbortedErrors():
            self.txAbortedErrors=other.txAbortedErrors
            self._myHasTxAbortedErrors=other._myHasTxAbortedErrors
            self._myTxAbortedErrorsRequested=other._myTxAbortedErrorsRequested
        
        if other.hasCollisions():
            self.collisions=other.collisions
            self._myHasCollisions=other._myHasCollisions
            self._myCollisionsRequested=other._myCollisionsRequested
        
        if other.hasTxHeartbeatErrors():
            self.txHeartbeatErrors=other.txHeartbeatErrors
            self._myHasTxHeartbeatErrors=other._myHasTxHeartbeatErrors
            self._myTxHeartbeatErrorsRequested=other._myTxHeartbeatErrorsRequested
        
        if other.hasRxMissedErrors():
            self.rxMissedErrors=other.rxMissedErrors
            self._myHasRxMissedErrors=other._myHasRxMissedErrors
            self._myRxMissedErrorsRequested=other._myRxMissedErrorsRequested
        
        if other.hasNonEopDescs():
            self.nonEopDescs=other.nonEopDescs
            self._myHasNonEopDescs=other._myHasNonEopDescs
            self._myNonEopDescsRequested=other._myNonEopDescsRequested
        
        if other.hasTxFlowControlXon():
            self.txFlowControlXon=other.txFlowControlXon
            self._myHasTxFlowControlXon=other._myHasTxFlowControlXon
            self._myTxFlowControlXonRequested=other._myTxFlowControlXonRequested
        
        if other.hasRxCsumOffloadErrors():
            self.rxCsumOffloadErrors=other.rxCsumOffloadErrors
            self._myHasRxCsumOffloadErrors=other._myHasRxCsumOffloadErrors
            self._myRxCsumOffloadErrorsRequested=other._myRxCsumOffloadErrorsRequested
        
        if other.hasRxCrcErrors():
            self.rxCrcErrors=other.rxCrcErrors
            self._myHasRxCrcErrors=other._myHasRxCrcErrors
            self._myRxCrcErrorsRequested=other._myRxCrcErrorsRequested
        
        if other.hasTxFifoErrors():
            self.txFifoErrors=other.txFifoErrors
            self._myHasTxFifoErrors=other._myHasTxFifoErrors
            self._myTxFifoErrorsRequested=other._myTxFifoErrorsRequested
        
        if other.hasTxPktsNic():
            self.txPktsNic=other.txPktsNic
            self._myHasTxPktsNic=other._myHasTxPktsNic
            self._myTxPktsNicRequested=other._myTxPktsNicRequested
        
        if other.hasRxFcoeDropped():
            self.rxFcoeDropped=other.rxFcoeDropped
            self._myHasRxFcoeDropped=other._myHasRxFcoeDropped
            self._myRxFcoeDroppedRequested=other._myRxFcoeDroppedRequested
        
        if other.hasTxBytesNic():
            self.txBytesNic=other.txBytesNic
            self._myHasTxBytesNic=other._myHasTxBytesNic
            self._myTxBytesNicRequested=other._myTxBytesNicRequested
        
        if other.hasAllocRxBuffFailed():
            self.allocRxBuffFailed=other.allocRxBuffFailed
            self._myHasAllocRxBuffFailed=other._myHasAllocRxBuffFailed
            self._myAllocRxBuffFailedRequested=other._myAllocRxBuffFailedRequested
        
        if other.hasFcoeBadFccrc():
            self.fcoeBadFccrc=other.fcoeBadFccrc
            self._myHasFcoeBadFccrc=other._myHasFcoeBadFccrc
            self._myFcoeBadFccrcRequested=other._myFcoeBadFccrcRequested
        
        if other.hasTxFlowControlXoff():
            self.txFlowControlXoff=other.txFlowControlXoff
            self._myHasTxFlowControlXoff=other._myHasTxFlowControlXoff
            self._myTxFlowControlXoffRequested=other._myTxFlowControlXoffRequested
        
        if other.hasTxTimeoutCount():
            self.txTimeoutCount=other.txTimeoutCount
            self._myHasTxTimeoutCount=other._myHasTxTimeoutCount
            self._myTxTimeoutCountRequested=other._myTxTimeoutCountRequested
        
        if other.hasTxCarrierErrors():
            self.txCarrierErrors=other.txCarrierErrors
            self._myHasTxCarrierErrors=other._myHasTxCarrierErrors
            self._myTxCarrierErrorsRequested=other._myTxCarrierErrorsRequested
        
        if other.hasRxFlowControlXoff():
            self.rxFlowControlXoff=other.rxFlowControlXoff
            self._myHasRxFlowControlXoff=other._myHasRxFlowControlXoff
            self._myRxFlowControlXoffRequested=other._myRxFlowControlXoffRequested
        
        if other.hasFdirMiss():
            self.fdirMiss=other.fdirMiss
            self._myHasFdirMiss=other._myHasFdirMiss
            self._myFdirMissRequested=other._myFdirMissRequested
        
        if other.hasRxNoDmaResources():
            self.rxNoDmaResources=other.rxNoDmaResources
            self._myHasRxNoDmaResources=other._myHasRxNoDmaResources
            self._myRxNoDmaResourcesRequested=other._myRxNoDmaResourcesRequested
        
        if other.hasRxOverErrors():
            self.rxOverErrors=other.rxOverErrors
            self._myHasRxOverErrors=other._myHasRxOverErrors
            self._myRxOverErrorsRequested=other._myRxOverErrorsRequested
        
        if other.hasRxFlowControlXon():
            self.rxFlowControlXon=other.rxFlowControlXon
            self._myHasRxFlowControlXon=other._myHasRxFlowControlXon
            self._myRxFlowControlXonRequested=other._myRxFlowControlXonRequested
        
        if other.hasTxRestartQueue():
            self.txRestartQueue=other.txRestartQueue
            self._myHasTxRestartQueue=other._myHasTxRestartQueue
            self._myTxRestartQueueRequested=other._myTxRestartQueueRequested
        
        if other.hasRxFrameErrors():
            self.rxFrameErrors=other.rxFrameErrors
            self._myHasRxFrameErrors=other._myHasRxFrameErrors
            self._myRxFrameErrorsRequested=other._myRxFrameErrorsRequested
        
        if other.hasRxPktsNic():
            self.rxPktsNic=other.rxPktsNic
            self._myHasRxPktsNic=other._myHasRxPktsNic
            self._myRxPktsNicRequested=other._myRxPktsNicRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.hwRscFlushed=other.hwRscFlushed
        self._myHasHwRscFlushed=other._myHasHwRscFlushed
        
        self.lscInt=other.lscInt
        self._myHasLscInt=other._myHasLscInt
        
        self.hwRscAggregated=other.hwRscAggregated
        self._myHasHwRscAggregated=other._myHasHwRscAggregated
        
        self.rxLongLengthErrors=other.rxLongLengthErrors
        self._myHasRxLongLengthErrors=other._myHasRxLongLengthErrors
        
        self.fdirMatch=other.fdirMatch
        self._myHasFdirMatch=other._myHasFdirMatch
        
        self.txFcoePackets=other.txFcoePackets
        self._myHasTxFcoePackets=other._myHasTxFcoePackets
        
        self.rxShortLengthErrors=other.rxShortLengthErrors
        self._myHasRxShortLengthErrors=other._myHasRxShortLengthErrors
        
        self.rxFcoeDwords=other.rxFcoeDwords
        self._myHasRxFcoeDwords=other._myHasRxFcoeDwords
        
        self.rxBytesNic=other.rxBytesNic
        self._myHasRxBytesNic=other._myHasRxBytesNic
        
        self.rxFcoePackets=other.rxFcoePackets
        self._myHasRxFcoePackets=other._myHasRxFcoePackets
        
        self.txFcoeDwords=other.txFcoeDwords
        self._myHasTxFcoeDwords=other._myHasTxFcoeDwords
        
        self.rxNoBufferCount=other.rxNoBufferCount
        self._myHasRxNoBufferCount=other._myHasRxNoBufferCount
        
        self.rxFifoErrors=other.rxFifoErrors
        self._myHasRxFifoErrors=other._myHasRxFifoErrors
        
        self.allocRxPageFailed=other.allocRxPageFailed
        self._myHasAllocRxPageFailed=other._myHasAllocRxPageFailed
        
        self.txBusy=other.txBusy
        self._myHasTxBusy=other._myHasTxBusy
        
        self.txAbortedErrors=other.txAbortedErrors
        self._myHasTxAbortedErrors=other._myHasTxAbortedErrors
        
        self.collisions=other.collisions
        self._myHasCollisions=other._myHasCollisions
        
        self.txHeartbeatErrors=other.txHeartbeatErrors
        self._myHasTxHeartbeatErrors=other._myHasTxHeartbeatErrors
        
        self.rxMissedErrors=other.rxMissedErrors
        self._myHasRxMissedErrors=other._myHasRxMissedErrors
        
        self.nonEopDescs=other.nonEopDescs
        self._myHasNonEopDescs=other._myHasNonEopDescs
        
        self.txFlowControlXon=other.txFlowControlXon
        self._myHasTxFlowControlXon=other._myHasTxFlowControlXon
        
        self.rxCsumOffloadErrors=other.rxCsumOffloadErrors
        self._myHasRxCsumOffloadErrors=other._myHasRxCsumOffloadErrors
        
        self.rxCrcErrors=other.rxCrcErrors
        self._myHasRxCrcErrors=other._myHasRxCrcErrors
        
        self.txFifoErrors=other.txFifoErrors
        self._myHasTxFifoErrors=other._myHasTxFifoErrors
        
        self.txPktsNic=other.txPktsNic
        self._myHasTxPktsNic=other._myHasTxPktsNic
        
        self.rxFcoeDropped=other.rxFcoeDropped
        self._myHasRxFcoeDropped=other._myHasRxFcoeDropped
        
        self.txBytesNic=other.txBytesNic
        self._myHasTxBytesNic=other._myHasTxBytesNic
        
        self.allocRxBuffFailed=other.allocRxBuffFailed
        self._myHasAllocRxBuffFailed=other._myHasAllocRxBuffFailed
        
        self.fcoeBadFccrc=other.fcoeBadFccrc
        self._myHasFcoeBadFccrc=other._myHasFcoeBadFccrc
        
        self.txFlowControlXoff=other.txFlowControlXoff
        self._myHasTxFlowControlXoff=other._myHasTxFlowControlXoff
        
        self.txTimeoutCount=other.txTimeoutCount
        self._myHasTxTimeoutCount=other._myHasTxTimeoutCount
        
        self.txCarrierErrors=other.txCarrierErrors
        self._myHasTxCarrierErrors=other._myHasTxCarrierErrors
        
        self.rxFlowControlXoff=other.rxFlowControlXoff
        self._myHasRxFlowControlXoff=other._myHasRxFlowControlXoff
        
        self.fdirMiss=other.fdirMiss
        self._myHasFdirMiss=other._myHasFdirMiss
        
        self.rxNoDmaResources=other.rxNoDmaResources
        self._myHasRxNoDmaResources=other._myHasRxNoDmaResources
        
        self.rxOverErrors=other.rxOverErrors
        self._myHasRxOverErrors=other._myHasRxOverErrors
        
        self.rxFlowControlXon=other.rxFlowControlXon
        self._myHasRxFlowControlXon=other._myHasRxFlowControlXon
        
        self.txRestartQueue=other.txRestartQueue
        self._myHasTxRestartQueue=other._myHasTxRestartQueue
        
        self.rxFrameErrors=other.rxFrameErrors
        self._myHasRxFrameErrors=other._myHasRxFrameErrors
        
        self.rxPktsNic=other.rxPktsNic
        self._myHasRxPktsNic=other._myHasRxPktsNic
        


    def setAllNumericToZero (self):
        
        self.hwRscFlushed=0
        self.setHasHwRscFlushed()
        self.lscInt=0
        self.setHasLscInt()
        self.hwRscAggregated=0
        self.setHasHwRscAggregated()
        self.rxLongLengthErrors=0
        self.setHasRxLongLengthErrors()
        self.fdirMatch=0
        self.setHasFdirMatch()
        self.txFcoePackets=0
        self.setHasTxFcoePackets()
        self.rxShortLengthErrors=0
        self.setHasRxShortLengthErrors()
        self.rxFcoeDwords=0
        self.setHasRxFcoeDwords()
        self.rxBytesNic=0
        self.setHasRxBytesNic()
        self.rxFcoePackets=0
        self.setHasRxFcoePackets()
        self.txFcoeDwords=0
        self.setHasTxFcoeDwords()
        self.rxNoBufferCount=0
        self.setHasRxNoBufferCount()
        self.rxFifoErrors=0
        self.setHasRxFifoErrors()
        self.allocRxPageFailed=0
        self.setHasAllocRxPageFailed()
        self.txBusy=0
        self.setHasTxBusy()
        self.txAbortedErrors=0
        self.setHasTxAbortedErrors()
        self.collisions=0
        self.setHasCollisions()
        self.txHeartbeatErrors=0
        self.setHasTxHeartbeatErrors()
        self.rxMissedErrors=0
        self.setHasRxMissedErrors()
        self.nonEopDescs=0
        self.setHasNonEopDescs()
        self.txFlowControlXon=0
        self.setHasTxFlowControlXon()
        self.rxCsumOffloadErrors=0
        self.setHasRxCsumOffloadErrors()
        self.rxCrcErrors=0
        self.setHasRxCrcErrors()
        self.txFifoErrors=0
        self.setHasTxFifoErrors()
        self.txPktsNic=0
        self.setHasTxPktsNic()
        self.rxFcoeDropped=0
        self.setHasRxFcoeDropped()
        self.txBytesNic=0
        self.setHasTxBytesNic()
        self.allocRxBuffFailed=0
        self.setHasAllocRxBuffFailed()
        self.fcoeBadFccrc=0
        self.setHasFcoeBadFccrc()
        self.txFlowControlXoff=0
        self.setHasTxFlowControlXoff()
        self.txTimeoutCount=0
        self.setHasTxTimeoutCount()
        self.txCarrierErrors=0
        self.setHasTxCarrierErrors()
        self.rxFlowControlXoff=0
        self.setHasRxFlowControlXoff()
        self.fdirMiss=0
        self.setHasFdirMiss()
        self.rxNoDmaResources=0
        self.setHasRxNoDmaResources()
        self.rxOverErrors=0
        self.setHasRxOverErrors()
        self.rxFlowControlXon=0
        self.setHasRxFlowControlXon()
        self.txRestartQueue=0
        self.setHasTxRestartQueue()
        self.rxFrameErrors=0
        self.setHasRxFrameErrors()
        self.rxPktsNic=0
        self.setHasRxPktsNic()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasHwRscFlushed():
            if other.hasHwRscFlushed():
                self.hwRscFlushed -= other.hwRscFlushed
        
        if self.hasLscInt():
            if other.hasLscInt():
                self.lscInt -= other.lscInt
        
        if self.hasHwRscAggregated():
            if other.hasHwRscAggregated():
                self.hwRscAggregated -= other.hwRscAggregated
        
        if self.hasRxLongLengthErrors():
            if other.hasRxLongLengthErrors():
                self.rxLongLengthErrors -= other.rxLongLengthErrors
        
        if self.hasFdirMatch():
            if other.hasFdirMatch():
                self.fdirMatch -= other.fdirMatch
        
        if self.hasTxFcoePackets():
            if other.hasTxFcoePackets():
                self.txFcoePackets -= other.txFcoePackets
        
        if self.hasRxShortLengthErrors():
            if other.hasRxShortLengthErrors():
                self.rxShortLengthErrors -= other.rxShortLengthErrors
        
        if self.hasRxFcoeDwords():
            if other.hasRxFcoeDwords():
                self.rxFcoeDwords -= other.rxFcoeDwords
        
        if self.hasRxBytesNic():
            if other.hasRxBytesNic():
                self.rxBytesNic -= other.rxBytesNic
        
        if self.hasRxFcoePackets():
            if other.hasRxFcoePackets():
                self.rxFcoePackets -= other.rxFcoePackets
        
        if self.hasTxFcoeDwords():
            if other.hasTxFcoeDwords():
                self.txFcoeDwords -= other.txFcoeDwords
        
        if self.hasRxNoBufferCount():
            if other.hasRxNoBufferCount():
                self.rxNoBufferCount -= other.rxNoBufferCount
        
        if self.hasRxFifoErrors():
            if other.hasRxFifoErrors():
                self.rxFifoErrors -= other.rxFifoErrors
        
        if self.hasAllocRxPageFailed():
            if other.hasAllocRxPageFailed():
                self.allocRxPageFailed -= other.allocRxPageFailed
        
        if self.hasTxBusy():
            if other.hasTxBusy():
                self.txBusy -= other.txBusy
        
        if self.hasTxAbortedErrors():
            if other.hasTxAbortedErrors():
                self.txAbortedErrors -= other.txAbortedErrors
        
        if self.hasCollisions():
            if other.hasCollisions():
                self.collisions -= other.collisions
        
        if self.hasTxHeartbeatErrors():
            if other.hasTxHeartbeatErrors():
                self.txHeartbeatErrors -= other.txHeartbeatErrors
        
        if self.hasRxMissedErrors():
            if other.hasRxMissedErrors():
                self.rxMissedErrors -= other.rxMissedErrors
        
        if self.hasNonEopDescs():
            if other.hasNonEopDescs():
                self.nonEopDescs -= other.nonEopDescs
        
        if self.hasTxFlowControlXon():
            if other.hasTxFlowControlXon():
                self.txFlowControlXon -= other.txFlowControlXon
        
        if self.hasRxCsumOffloadErrors():
            if other.hasRxCsumOffloadErrors():
                self.rxCsumOffloadErrors -= other.rxCsumOffloadErrors
        
        if self.hasRxCrcErrors():
            if other.hasRxCrcErrors():
                self.rxCrcErrors -= other.rxCrcErrors
        
        if self.hasTxFifoErrors():
            if other.hasTxFifoErrors():
                self.txFifoErrors -= other.txFifoErrors
        
        if self.hasTxPktsNic():
            if other.hasTxPktsNic():
                self.txPktsNic -= other.txPktsNic
        
        if self.hasRxFcoeDropped():
            if other.hasRxFcoeDropped():
                self.rxFcoeDropped -= other.rxFcoeDropped
        
        if self.hasTxBytesNic():
            if other.hasTxBytesNic():
                self.txBytesNic -= other.txBytesNic
        
        if self.hasAllocRxBuffFailed():
            if other.hasAllocRxBuffFailed():
                self.allocRxBuffFailed -= other.allocRxBuffFailed
        
        if self.hasFcoeBadFccrc():
            if other.hasFcoeBadFccrc():
                self.fcoeBadFccrc -= other.fcoeBadFccrc
        
        if self.hasTxFlowControlXoff():
            if other.hasTxFlowControlXoff():
                self.txFlowControlXoff -= other.txFlowControlXoff
        
        if self.hasTxTimeoutCount():
            if other.hasTxTimeoutCount():
                self.txTimeoutCount -= other.txTimeoutCount
        
        if self.hasTxCarrierErrors():
            if other.hasTxCarrierErrors():
                self.txCarrierErrors -= other.txCarrierErrors
        
        if self.hasRxFlowControlXoff():
            if other.hasRxFlowControlXoff():
                self.rxFlowControlXoff -= other.rxFlowControlXoff
        
        if self.hasFdirMiss():
            if other.hasFdirMiss():
                self.fdirMiss -= other.fdirMiss
        
        if self.hasRxNoDmaResources():
            if other.hasRxNoDmaResources():
                self.rxNoDmaResources -= other.rxNoDmaResources
        
        if self.hasRxOverErrors():
            if other.hasRxOverErrors():
                self.rxOverErrors -= other.rxOverErrors
        
        if self.hasRxFlowControlXon():
            if other.hasRxFlowControlXon():
                self.rxFlowControlXon -= other.rxFlowControlXon
        
        if self.hasTxRestartQueue():
            if other.hasTxRestartQueue():
                self.txRestartQueue -= other.txRestartQueue
        
        if self.hasRxFrameErrors():
            if other.hasRxFrameErrors():
                self.rxFrameErrors -= other.rxFrameErrors
        
        if self.hasRxPktsNic():
            if other.hasRxPktsNic():
                self.rxPktsNic -= other.rxPktsNic
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasHwRscFlushed():
            if other.hasHwRscFlushed():
                self.hwRscFlushed += other.hwRscFlushed
        
        if self.hasLscInt():
            if other.hasLscInt():
                self.lscInt += other.lscInt
        
        if self.hasHwRscAggregated():
            if other.hasHwRscAggregated():
                self.hwRscAggregated += other.hwRscAggregated
        
        if self.hasRxLongLengthErrors():
            if other.hasRxLongLengthErrors():
                self.rxLongLengthErrors += other.rxLongLengthErrors
        
        if self.hasFdirMatch():
            if other.hasFdirMatch():
                self.fdirMatch += other.fdirMatch
        
        if self.hasTxFcoePackets():
            if other.hasTxFcoePackets():
                self.txFcoePackets += other.txFcoePackets
        
        if self.hasRxShortLengthErrors():
            if other.hasRxShortLengthErrors():
                self.rxShortLengthErrors += other.rxShortLengthErrors
        
        if self.hasRxFcoeDwords():
            if other.hasRxFcoeDwords():
                self.rxFcoeDwords += other.rxFcoeDwords
        
        if self.hasRxBytesNic():
            if other.hasRxBytesNic():
                self.rxBytesNic += other.rxBytesNic
        
        if self.hasRxFcoePackets():
            if other.hasRxFcoePackets():
                self.rxFcoePackets += other.rxFcoePackets
        
        if self.hasTxFcoeDwords():
            if other.hasTxFcoeDwords():
                self.txFcoeDwords += other.txFcoeDwords
        
        if self.hasRxNoBufferCount():
            if other.hasRxNoBufferCount():
                self.rxNoBufferCount += other.rxNoBufferCount
        
        if self.hasRxFifoErrors():
            if other.hasRxFifoErrors():
                self.rxFifoErrors += other.rxFifoErrors
        
        if self.hasAllocRxPageFailed():
            if other.hasAllocRxPageFailed():
                self.allocRxPageFailed += other.allocRxPageFailed
        
        if self.hasTxBusy():
            if other.hasTxBusy():
                self.txBusy += other.txBusy
        
        if self.hasTxAbortedErrors():
            if other.hasTxAbortedErrors():
                self.txAbortedErrors += other.txAbortedErrors
        
        if self.hasCollisions():
            if other.hasCollisions():
                self.collisions += other.collisions
        
        if self.hasTxHeartbeatErrors():
            if other.hasTxHeartbeatErrors():
                self.txHeartbeatErrors += other.txHeartbeatErrors
        
        if self.hasRxMissedErrors():
            if other.hasRxMissedErrors():
                self.rxMissedErrors += other.rxMissedErrors
        
        if self.hasNonEopDescs():
            if other.hasNonEopDescs():
                self.nonEopDescs += other.nonEopDescs
        
        if self.hasTxFlowControlXon():
            if other.hasTxFlowControlXon():
                self.txFlowControlXon += other.txFlowControlXon
        
        if self.hasRxCsumOffloadErrors():
            if other.hasRxCsumOffloadErrors():
                self.rxCsumOffloadErrors += other.rxCsumOffloadErrors
        
        if self.hasRxCrcErrors():
            if other.hasRxCrcErrors():
                self.rxCrcErrors += other.rxCrcErrors
        
        if self.hasTxFifoErrors():
            if other.hasTxFifoErrors():
                self.txFifoErrors += other.txFifoErrors
        
        if self.hasTxPktsNic():
            if other.hasTxPktsNic():
                self.txPktsNic += other.txPktsNic
        
        if self.hasRxFcoeDropped():
            if other.hasRxFcoeDropped():
                self.rxFcoeDropped += other.rxFcoeDropped
        
        if self.hasTxBytesNic():
            if other.hasTxBytesNic():
                self.txBytesNic += other.txBytesNic
        
        if self.hasAllocRxBuffFailed():
            if other.hasAllocRxBuffFailed():
                self.allocRxBuffFailed += other.allocRxBuffFailed
        
        if self.hasFcoeBadFccrc():
            if other.hasFcoeBadFccrc():
                self.fcoeBadFccrc += other.fcoeBadFccrc
        
        if self.hasTxFlowControlXoff():
            if other.hasTxFlowControlXoff():
                self.txFlowControlXoff += other.txFlowControlXoff
        
        if self.hasTxTimeoutCount():
            if other.hasTxTimeoutCount():
                self.txTimeoutCount += other.txTimeoutCount
        
        if self.hasTxCarrierErrors():
            if other.hasTxCarrierErrors():
                self.txCarrierErrors += other.txCarrierErrors
        
        if self.hasRxFlowControlXoff():
            if other.hasRxFlowControlXoff():
                self.rxFlowControlXoff += other.rxFlowControlXoff
        
        if self.hasFdirMiss():
            if other.hasFdirMiss():
                self.fdirMiss += other.fdirMiss
        
        if self.hasRxNoDmaResources():
            if other.hasRxNoDmaResources():
                self.rxNoDmaResources += other.rxNoDmaResources
        
        if self.hasRxOverErrors():
            if other.hasRxOverErrors():
                self.rxOverErrors += other.rxOverErrors
        
        if self.hasRxFlowControlXon():
            if other.hasRxFlowControlXon():
                self.rxFlowControlXon += other.rxFlowControlXon
        
        if self.hasTxRestartQueue():
            if other.hasTxRestartQueue():
                self.txRestartQueue += other.txRestartQueue
        
        if self.hasRxFrameErrors():
            if other.hasRxFrameErrors():
                self.rxFrameErrors += other.rxFrameErrors
        
        if self.hasRxPktsNic():
            if other.hasRxPktsNic():
                self.rxPktsNic += other.rxPktsNic
        
        
        pass


    # has...() methods

    def hasHwRscFlushed (self):
        return self._myHasHwRscFlushed

    def hasLscInt (self):
        return self._myHasLscInt

    def hasHwRscAggregated (self):
        return self._myHasHwRscAggregated

    def hasRxLongLengthErrors (self):
        return self._myHasRxLongLengthErrors

    def hasFdirMatch (self):
        return self._myHasFdirMatch

    def hasTxFcoePackets (self):
        return self._myHasTxFcoePackets

    def hasRxShortLengthErrors (self):
        return self._myHasRxShortLengthErrors

    def hasRxFcoeDwords (self):
        return self._myHasRxFcoeDwords

    def hasRxBytesNic (self):
        return self._myHasRxBytesNic

    def hasRxFcoePackets (self):
        return self._myHasRxFcoePackets

    def hasTxFcoeDwords (self):
        return self._myHasTxFcoeDwords

    def hasRxNoBufferCount (self):
        return self._myHasRxNoBufferCount

    def hasRxFifoErrors (self):
        return self._myHasRxFifoErrors

    def hasAllocRxPageFailed (self):
        return self._myHasAllocRxPageFailed

    def hasTxBusy (self):
        return self._myHasTxBusy

    def hasTxAbortedErrors (self):
        return self._myHasTxAbortedErrors

    def hasCollisions (self):
        return self._myHasCollisions

    def hasTxHeartbeatErrors (self):
        return self._myHasTxHeartbeatErrors

    def hasRxMissedErrors (self):
        return self._myHasRxMissedErrors

    def hasNonEopDescs (self):
        return self._myHasNonEopDescs

    def hasTxFlowControlXon (self):
        return self._myHasTxFlowControlXon

    def hasRxCsumOffloadErrors (self):
        return self._myHasRxCsumOffloadErrors

    def hasRxCrcErrors (self):
        return self._myHasRxCrcErrors

    def hasTxFifoErrors (self):
        return self._myHasTxFifoErrors

    def hasTxPktsNic (self):
        return self._myHasTxPktsNic

    def hasRxFcoeDropped (self):
        return self._myHasRxFcoeDropped

    def hasTxBytesNic (self):
        return self._myHasTxBytesNic

    def hasAllocRxBuffFailed (self):
        return self._myHasAllocRxBuffFailed

    def hasFcoeBadFccrc (self):
        return self._myHasFcoeBadFccrc

    def hasTxFlowControlXoff (self):
        return self._myHasTxFlowControlXoff

    def hasTxTimeoutCount (self):
        return self._myHasTxTimeoutCount

    def hasTxCarrierErrors (self):
        return self._myHasTxCarrierErrors

    def hasRxFlowControlXoff (self):
        return self._myHasRxFlowControlXoff

    def hasFdirMiss (self):
        return self._myHasFdirMiss

    def hasRxNoDmaResources (self):
        return self._myHasRxNoDmaResources

    def hasRxOverErrors (self):
        return self._myHasRxOverErrors

    def hasRxFlowControlXon (self):
        return self._myHasRxFlowControlXon

    def hasTxRestartQueue (self):
        return self._myHasTxRestartQueue

    def hasRxFrameErrors (self):
        return self._myHasRxFrameErrors

    def hasRxPktsNic (self):
        return self._myHasRxPktsNic




    # setHas...() methods

    def setHasHwRscFlushed (self):
        self._myHasHwRscFlushed=True

    def setHasLscInt (self):
        self._myHasLscInt=True

    def setHasHwRscAggregated (self):
        self._myHasHwRscAggregated=True

    def setHasRxLongLengthErrors (self):
        self._myHasRxLongLengthErrors=True

    def setHasFdirMatch (self):
        self._myHasFdirMatch=True

    def setHasTxFcoePackets (self):
        self._myHasTxFcoePackets=True

    def setHasRxShortLengthErrors (self):
        self._myHasRxShortLengthErrors=True

    def setHasRxFcoeDwords (self):
        self._myHasRxFcoeDwords=True

    def setHasRxBytesNic (self):
        self._myHasRxBytesNic=True

    def setHasRxFcoePackets (self):
        self._myHasRxFcoePackets=True

    def setHasTxFcoeDwords (self):
        self._myHasTxFcoeDwords=True

    def setHasRxNoBufferCount (self):
        self._myHasRxNoBufferCount=True

    def setHasRxFifoErrors (self):
        self._myHasRxFifoErrors=True

    def setHasAllocRxPageFailed (self):
        self._myHasAllocRxPageFailed=True

    def setHasTxBusy (self):
        self._myHasTxBusy=True

    def setHasTxAbortedErrors (self):
        self._myHasTxAbortedErrors=True

    def setHasCollisions (self):
        self._myHasCollisions=True

    def setHasTxHeartbeatErrors (self):
        self._myHasTxHeartbeatErrors=True

    def setHasRxMissedErrors (self):
        self._myHasRxMissedErrors=True

    def setHasNonEopDescs (self):
        self._myHasNonEopDescs=True

    def setHasTxFlowControlXon (self):
        self._myHasTxFlowControlXon=True

    def setHasRxCsumOffloadErrors (self):
        self._myHasRxCsumOffloadErrors=True

    def setHasRxCrcErrors (self):
        self._myHasRxCrcErrors=True

    def setHasTxFifoErrors (self):
        self._myHasTxFifoErrors=True

    def setHasTxPktsNic (self):
        self._myHasTxPktsNic=True

    def setHasRxFcoeDropped (self):
        self._myHasRxFcoeDropped=True

    def setHasTxBytesNic (self):
        self._myHasTxBytesNic=True

    def setHasAllocRxBuffFailed (self):
        self._myHasAllocRxBuffFailed=True

    def setHasFcoeBadFccrc (self):
        self._myHasFcoeBadFccrc=True

    def setHasTxFlowControlXoff (self):
        self._myHasTxFlowControlXoff=True

    def setHasTxTimeoutCount (self):
        self._myHasTxTimeoutCount=True

    def setHasTxCarrierErrors (self):
        self._myHasTxCarrierErrors=True

    def setHasRxFlowControlXoff (self):
        self._myHasRxFlowControlXoff=True

    def setHasFdirMiss (self):
        self._myHasFdirMiss=True

    def setHasRxNoDmaResources (self):
        self._myHasRxNoDmaResources=True

    def setHasRxOverErrors (self):
        self._myHasRxOverErrors=True

    def setHasRxFlowControlXon (self):
        self._myHasRxFlowControlXon=True

    def setHasTxRestartQueue (self):
        self._myHasTxRestartQueue=True

    def setHasRxFrameErrors (self):
        self._myHasRxFrameErrors=True

    def setHasRxPktsNic (self):
        self._myHasRxPktsNic=True




    # isRequested...() methods

    def isHwRscFlushedRequested (self):
        return self._myHwRscFlushedRequested

    def isLscIntRequested (self):
        return self._myLscIntRequested

    def isHwRscAggregatedRequested (self):
        return self._myHwRscAggregatedRequested

    def isRxLongLengthErrorsRequested (self):
        return self._myRxLongLengthErrorsRequested

    def isFdirMatchRequested (self):
        return self._myFdirMatchRequested

    def isTxFcoePacketsRequested (self):
        return self._myTxFcoePacketsRequested

    def isRxShortLengthErrorsRequested (self):
        return self._myRxShortLengthErrorsRequested

    def isRxFcoeDwordsRequested (self):
        return self._myRxFcoeDwordsRequested

    def isRxBytesNicRequested (self):
        return self._myRxBytesNicRequested

    def isRxFcoePacketsRequested (self):
        return self._myRxFcoePacketsRequested

    def isTxFcoeDwordsRequested (self):
        return self._myTxFcoeDwordsRequested

    def isRxNoBufferCountRequested (self):
        return self._myRxNoBufferCountRequested

    def isRxFifoErrorsRequested (self):
        return self._myRxFifoErrorsRequested

    def isAllocRxPageFailedRequested (self):
        return self._myAllocRxPageFailedRequested

    def isTxBusyRequested (self):
        return self._myTxBusyRequested

    def isTxAbortedErrorsRequested (self):
        return self._myTxAbortedErrorsRequested

    def isCollisionsRequested (self):
        return self._myCollisionsRequested

    def isTxHeartbeatErrorsRequested (self):
        return self._myTxHeartbeatErrorsRequested

    def isRxMissedErrorsRequested (self):
        return self._myRxMissedErrorsRequested

    def isNonEopDescsRequested (self):
        return self._myNonEopDescsRequested

    def isTxFlowControlXonRequested (self):
        return self._myTxFlowControlXonRequested

    def isRxCsumOffloadErrorsRequested (self):
        return self._myRxCsumOffloadErrorsRequested

    def isRxCrcErrorsRequested (self):
        return self._myRxCrcErrorsRequested

    def isTxFifoErrorsRequested (self):
        return self._myTxFifoErrorsRequested

    def isTxPktsNicRequested (self):
        return self._myTxPktsNicRequested

    def isRxFcoeDroppedRequested (self):
        return self._myRxFcoeDroppedRequested

    def isTxBytesNicRequested (self):
        return self._myTxBytesNicRequested

    def isAllocRxBuffFailedRequested (self):
        return self._myAllocRxBuffFailedRequested

    def isFcoeBadFccrcRequested (self):
        return self._myFcoeBadFccrcRequested

    def isTxFlowControlXoffRequested (self):
        return self._myTxFlowControlXoffRequested

    def isTxTimeoutCountRequested (self):
        return self._myTxTimeoutCountRequested

    def isTxCarrierErrorsRequested (self):
        return self._myTxCarrierErrorsRequested

    def isRxFlowControlXoffRequested (self):
        return self._myRxFlowControlXoffRequested

    def isFdirMissRequested (self):
        return self._myFdirMissRequested

    def isRxNoDmaResourcesRequested (self):
        return self._myRxNoDmaResourcesRequested

    def isRxOverErrorsRequested (self):
        return self._myRxOverErrorsRequested

    def isRxFlowControlXonRequested (self):
        return self._myRxFlowControlXonRequested

    def isTxRestartQueueRequested (self):
        return self._myTxRestartQueueRequested

    def isRxFrameErrorsRequested (self):
        return self._myRxFrameErrorsRequested

    def isRxPktsNicRequested (self):
        return self._myRxPktsNicRequested




    # setRequested...() methods

    def setHwRscFlushedRequested (self):
        self._myHwRscFlushedRequested=True

    def setLscIntRequested (self):
        self._myLscIntRequested=True

    def setHwRscAggregatedRequested (self):
        self._myHwRscAggregatedRequested=True

    def setRxLongLengthErrorsRequested (self):
        self._myRxLongLengthErrorsRequested=True

    def setFdirMatchRequested (self):
        self._myFdirMatchRequested=True

    def setTxFcoePacketsRequested (self):
        self._myTxFcoePacketsRequested=True

    def setRxShortLengthErrorsRequested (self):
        self._myRxShortLengthErrorsRequested=True

    def setRxFcoeDwordsRequested (self):
        self._myRxFcoeDwordsRequested=True

    def setRxBytesNicRequested (self):
        self._myRxBytesNicRequested=True

    def setRxFcoePacketsRequested (self):
        self._myRxFcoePacketsRequested=True

    def setTxFcoeDwordsRequested (self):
        self._myTxFcoeDwordsRequested=True

    def setRxNoBufferCountRequested (self):
        self._myRxNoBufferCountRequested=True

    def setRxFifoErrorsRequested (self):
        self._myRxFifoErrorsRequested=True

    def setAllocRxPageFailedRequested (self):
        self._myAllocRxPageFailedRequested=True

    def setTxBusyRequested (self):
        self._myTxBusyRequested=True

    def setTxAbortedErrorsRequested (self):
        self._myTxAbortedErrorsRequested=True

    def setCollisionsRequested (self):
        self._myCollisionsRequested=True

    def setTxHeartbeatErrorsRequested (self):
        self._myTxHeartbeatErrorsRequested=True

    def setRxMissedErrorsRequested (self):
        self._myRxMissedErrorsRequested=True

    def setNonEopDescsRequested (self):
        self._myNonEopDescsRequested=True

    def setTxFlowControlXonRequested (self):
        self._myTxFlowControlXonRequested=True

    def setRxCsumOffloadErrorsRequested (self):
        self._myRxCsumOffloadErrorsRequested=True

    def setRxCrcErrorsRequested (self):
        self._myRxCrcErrorsRequested=True

    def setTxFifoErrorsRequested (self):
        self._myTxFifoErrorsRequested=True

    def setTxPktsNicRequested (self):
        self._myTxPktsNicRequested=True

    def setRxFcoeDroppedRequested (self):
        self._myRxFcoeDroppedRequested=True

    def setTxBytesNicRequested (self):
        self._myTxBytesNicRequested=True

    def setAllocRxBuffFailedRequested (self):
        self._myAllocRxBuffFailedRequested=True

    def setFcoeBadFccrcRequested (self):
        self._myFcoeBadFccrcRequested=True

    def setTxFlowControlXoffRequested (self):
        self._myTxFlowControlXoffRequested=True

    def setTxTimeoutCountRequested (self):
        self._myTxTimeoutCountRequested=True

    def setTxCarrierErrorsRequested (self):
        self._myTxCarrierErrorsRequested=True

    def setRxFlowControlXoffRequested (self):
        self._myRxFlowControlXoffRequested=True

    def setFdirMissRequested (self):
        self._myFdirMissRequested=True

    def setRxNoDmaResourcesRequested (self):
        self._myRxNoDmaResourcesRequested=True

    def setRxOverErrorsRequested (self):
        self._myRxOverErrorsRequested=True

    def setRxFlowControlXonRequested (self):
        self._myRxFlowControlXonRequested=True

    def setTxRestartQueueRequested (self):
        self._myTxRestartQueueRequested=True

    def setRxFrameErrorsRequested (self):
        self._myRxFrameErrorsRequested=True

    def setRxPktsNicRequested (self):
        self._myRxPktsNicRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myHwRscFlushedRequested:
            x = "+HwRscFlushed="
            if self._myHasHwRscFlushed:
                leafStr = str(self.hwRscFlushed)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myLscIntRequested:
            x = "+LscInt="
            if self._myHasLscInt:
                leafStr = str(self.lscInt)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myHwRscAggregatedRequested:
            x = "+HwRscAggregated="
            if self._myHasHwRscAggregated:
                leafStr = str(self.hwRscAggregated)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxLongLengthErrorsRequested:
            x = "+RxLongLengthErrors="
            if self._myHasRxLongLengthErrors:
                leafStr = str(self.rxLongLengthErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFdirMatchRequested:
            x = "+FdirMatch="
            if self._myHasFdirMatch:
                leafStr = str(self.fdirMatch)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxFcoePacketsRequested:
            x = "+TxFcoePackets="
            if self._myHasTxFcoePackets:
                leafStr = str(self.txFcoePackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxShortLengthErrorsRequested:
            x = "+RxShortLengthErrors="
            if self._myHasRxShortLengthErrors:
                leafStr = str(self.rxShortLengthErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxFcoeDwordsRequested:
            x = "+RxFcoeDwords="
            if self._myHasRxFcoeDwords:
                leafStr = str(self.rxFcoeDwords)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxBytesNicRequested:
            x = "+RxBytesNic="
            if self._myHasRxBytesNic:
                leafStr = str(self.rxBytesNic)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxFcoePacketsRequested:
            x = "+RxFcoePackets="
            if self._myHasRxFcoePackets:
                leafStr = str(self.rxFcoePackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxFcoeDwordsRequested:
            x = "+TxFcoeDwords="
            if self._myHasTxFcoeDwords:
                leafStr = str(self.txFcoeDwords)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxNoBufferCountRequested:
            x = "+RxNoBufferCount="
            if self._myHasRxNoBufferCount:
                leafStr = str(self.rxNoBufferCount)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxFifoErrorsRequested:
            x = "+RxFifoErrors="
            if self._myHasRxFifoErrors:
                leafStr = str(self.rxFifoErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myAllocRxPageFailedRequested:
            x = "+AllocRxPageFailed="
            if self._myHasAllocRxPageFailed:
                leafStr = str(self.allocRxPageFailed)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxBusyRequested:
            x = "+TxBusy="
            if self._myHasTxBusy:
                leafStr = str(self.txBusy)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxAbortedErrorsRequested:
            x = "+TxAbortedErrors="
            if self._myHasTxAbortedErrors:
                leafStr = str(self.txAbortedErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myCollisionsRequested:
            x = "+Collisions="
            if self._myHasCollisions:
                leafStr = str(self.collisions)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxHeartbeatErrorsRequested:
            x = "+TxHeartbeatErrors="
            if self._myHasTxHeartbeatErrors:
                leafStr = str(self.txHeartbeatErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxMissedErrorsRequested:
            x = "+RxMissedErrors="
            if self._myHasRxMissedErrors:
                leafStr = str(self.rxMissedErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNonEopDescsRequested:
            x = "+NonEopDescs="
            if self._myHasNonEopDescs:
                leafStr = str(self.nonEopDescs)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxFlowControlXonRequested:
            x = "+TxFlowControlXon="
            if self._myHasTxFlowControlXon:
                leafStr = str(self.txFlowControlXon)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxCsumOffloadErrorsRequested:
            x = "+RxCsumOffloadErrors="
            if self._myHasRxCsumOffloadErrors:
                leafStr = str(self.rxCsumOffloadErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxCrcErrorsRequested:
            x = "+RxCrcErrors="
            if self._myHasRxCrcErrors:
                leafStr = str(self.rxCrcErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxFifoErrorsRequested:
            x = "+TxFifoErrors="
            if self._myHasTxFifoErrors:
                leafStr = str(self.txFifoErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxPktsNicRequested:
            x = "+TxPktsNic="
            if self._myHasTxPktsNic:
                leafStr = str(self.txPktsNic)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxFcoeDroppedRequested:
            x = "+RxFcoeDropped="
            if self._myHasRxFcoeDropped:
                leafStr = str(self.rxFcoeDropped)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxBytesNicRequested:
            x = "+TxBytesNic="
            if self._myHasTxBytesNic:
                leafStr = str(self.txBytesNic)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myAllocRxBuffFailedRequested:
            x = "+AllocRxBuffFailed="
            if self._myHasAllocRxBuffFailed:
                leafStr = str(self.allocRxBuffFailed)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFcoeBadFccrcRequested:
            x = "+FcoeBadFccrc="
            if self._myHasFcoeBadFccrc:
                leafStr = str(self.fcoeBadFccrc)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxFlowControlXoffRequested:
            x = "+TxFlowControlXoff="
            if self._myHasTxFlowControlXoff:
                leafStr = str(self.txFlowControlXoff)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxTimeoutCountRequested:
            x = "+TxTimeoutCount="
            if self._myHasTxTimeoutCount:
                leafStr = str(self.txTimeoutCount)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxCarrierErrorsRequested:
            x = "+TxCarrierErrors="
            if self._myHasTxCarrierErrors:
                leafStr = str(self.txCarrierErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxFlowControlXoffRequested:
            x = "+RxFlowControlXoff="
            if self._myHasRxFlowControlXoff:
                leafStr = str(self.rxFlowControlXoff)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFdirMissRequested:
            x = "+FdirMiss="
            if self._myHasFdirMiss:
                leafStr = str(self.fdirMiss)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxNoDmaResourcesRequested:
            x = "+RxNoDmaResources="
            if self._myHasRxNoDmaResources:
                leafStr = str(self.rxNoDmaResources)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxOverErrorsRequested:
            x = "+RxOverErrors="
            if self._myHasRxOverErrors:
                leafStr = str(self.rxOverErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxFlowControlXonRequested:
            x = "+RxFlowControlXon="
            if self._myHasRxFlowControlXon:
                leafStr = str(self.rxFlowControlXon)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTxRestartQueueRequested:
            x = "+TxRestartQueue="
            if self._myHasTxRestartQueue:
                leafStr = str(self.txRestartQueue)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxFrameErrorsRequested:
            x = "+RxFrameErrors="
            if self._myHasRxFrameErrors:
                leafStr = str(self.rxFrameErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRxPktsNicRequested:
            x = "+RxPktsNic="
            if self._myHasRxPktsNic:
                leafStr = str(self.rxPktsNic)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{CountersOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+HwRscFlushed="
        if self._myHasHwRscFlushed:
            leafStr = str(self.hwRscFlushed)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myHwRscFlushedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+LscInt="
        if self._myHasLscInt:
            leafStr = str(self.lscInt)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myLscIntRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+HwRscAggregated="
        if self._myHasHwRscAggregated:
            leafStr = str(self.hwRscAggregated)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myHwRscAggregatedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxLongLengthErrors="
        if self._myHasRxLongLengthErrors:
            leafStr = str(self.rxLongLengthErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxLongLengthErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FdirMatch="
        if self._myHasFdirMatch:
            leafStr = str(self.fdirMatch)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFdirMatchRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxFcoePackets="
        if self._myHasTxFcoePackets:
            leafStr = str(self.txFcoePackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxFcoePacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxShortLengthErrors="
        if self._myHasRxShortLengthErrors:
            leafStr = str(self.rxShortLengthErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxShortLengthErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxFcoeDwords="
        if self._myHasRxFcoeDwords:
            leafStr = str(self.rxFcoeDwords)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxFcoeDwordsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxBytesNic="
        if self._myHasRxBytesNic:
            leafStr = str(self.rxBytesNic)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxBytesNicRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxFcoePackets="
        if self._myHasRxFcoePackets:
            leafStr = str(self.rxFcoePackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxFcoePacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxFcoeDwords="
        if self._myHasTxFcoeDwords:
            leafStr = str(self.txFcoeDwords)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxFcoeDwordsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxNoBufferCount="
        if self._myHasRxNoBufferCount:
            leafStr = str(self.rxNoBufferCount)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxNoBufferCountRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxFifoErrors="
        if self._myHasRxFifoErrors:
            leafStr = str(self.rxFifoErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxFifoErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+AllocRxPageFailed="
        if self._myHasAllocRxPageFailed:
            leafStr = str(self.allocRxPageFailed)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myAllocRxPageFailedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxBusy="
        if self._myHasTxBusy:
            leafStr = str(self.txBusy)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxBusyRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxAbortedErrors="
        if self._myHasTxAbortedErrors:
            leafStr = str(self.txAbortedErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxAbortedErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Collisions="
        if self._myHasCollisions:
            leafStr = str(self.collisions)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCollisionsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxHeartbeatErrors="
        if self._myHasTxHeartbeatErrors:
            leafStr = str(self.txHeartbeatErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxHeartbeatErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxMissedErrors="
        if self._myHasRxMissedErrors:
            leafStr = str(self.rxMissedErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxMissedErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+NonEopDescs="
        if self._myHasNonEopDescs:
            leafStr = str(self.nonEopDescs)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNonEopDescsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxFlowControlXon="
        if self._myHasTxFlowControlXon:
            leafStr = str(self.txFlowControlXon)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxFlowControlXonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxCsumOffloadErrors="
        if self._myHasRxCsumOffloadErrors:
            leafStr = str(self.rxCsumOffloadErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxCsumOffloadErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxCrcErrors="
        if self._myHasRxCrcErrors:
            leafStr = str(self.rxCrcErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxCrcErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxFifoErrors="
        if self._myHasTxFifoErrors:
            leafStr = str(self.txFifoErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxFifoErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxPktsNic="
        if self._myHasTxPktsNic:
            leafStr = str(self.txPktsNic)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxPktsNicRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxFcoeDropped="
        if self._myHasRxFcoeDropped:
            leafStr = str(self.rxFcoeDropped)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxFcoeDroppedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxBytesNic="
        if self._myHasTxBytesNic:
            leafStr = str(self.txBytesNic)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxBytesNicRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+AllocRxBuffFailed="
        if self._myHasAllocRxBuffFailed:
            leafStr = str(self.allocRxBuffFailed)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myAllocRxBuffFailedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FcoeBadFccrc="
        if self._myHasFcoeBadFccrc:
            leafStr = str(self.fcoeBadFccrc)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFcoeBadFccrcRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxFlowControlXoff="
        if self._myHasTxFlowControlXoff:
            leafStr = str(self.txFlowControlXoff)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxFlowControlXoffRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxTimeoutCount="
        if self._myHasTxTimeoutCount:
            leafStr = str(self.txTimeoutCount)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxTimeoutCountRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxCarrierErrors="
        if self._myHasTxCarrierErrors:
            leafStr = str(self.txCarrierErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxCarrierErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxFlowControlXoff="
        if self._myHasRxFlowControlXoff:
            leafStr = str(self.rxFlowControlXoff)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxFlowControlXoffRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FdirMiss="
        if self._myHasFdirMiss:
            leafStr = str(self.fdirMiss)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFdirMissRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxNoDmaResources="
        if self._myHasRxNoDmaResources:
            leafStr = str(self.rxNoDmaResources)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxNoDmaResourcesRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxOverErrors="
        if self._myHasRxOverErrors:
            leafStr = str(self.rxOverErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxOverErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxFlowControlXon="
        if self._myHasRxFlowControlXon:
            leafStr = str(self.rxFlowControlXon)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxFlowControlXonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TxRestartQueue="
        if self._myHasTxRestartQueue:
            leafStr = str(self.txRestartQueue)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTxRestartQueueRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxFrameErrors="
        if self._myHasRxFrameErrors:
            leafStr = str(self.rxFrameErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxFrameErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RxPktsNic="
        if self._myHasRxPktsNic:
            leafStr = str(self.rxPktsNic)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRxPktsNicRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setHwRscFlushedRequested()
        self.setLscIntRequested()
        self.setHwRscAggregatedRequested()
        self.setRxLongLengthErrorsRequested()
        self.setFdirMatchRequested()
        self.setTxFcoePacketsRequested()
        self.setRxShortLengthErrorsRequested()
        self.setRxFcoeDwordsRequested()
        self.setRxBytesNicRequested()
        self.setRxFcoePacketsRequested()
        self.setTxFcoeDwordsRequested()
        self.setRxNoBufferCountRequested()
        self.setRxFifoErrorsRequested()
        self.setAllocRxPageFailedRequested()
        self.setTxBusyRequested()
        self.setTxAbortedErrorsRequested()
        self.setCollisionsRequested()
        self.setTxHeartbeatErrorsRequested()
        self.setRxMissedErrorsRequested()
        self.setNonEopDescsRequested()
        self.setTxFlowControlXonRequested()
        self.setRxCsumOffloadErrorsRequested()
        self.setRxCrcErrorsRequested()
        self.setTxFifoErrorsRequested()
        self.setTxPktsNicRequested()
        self.setRxFcoeDroppedRequested()
        self.setTxBytesNicRequested()
        self.setAllocRxBuffFailedRequested()
        self.setFcoeBadFccrcRequested()
        self.setTxFlowControlXoffRequested()
        self.setTxTimeoutCountRequested()
        self.setTxCarrierErrorsRequested()
        self.setRxFlowControlXoffRequested()
        self.setFdirMissRequested()
        self.setRxNoDmaResourcesRequested()
        self.setRxOverErrorsRequested()
        self.setRxFlowControlXonRequested()
        self.setTxRestartQueueRequested()
        self.setRxFrameErrorsRequested()
        self.setRxPktsNicRequested()
        
        


    def setHwRscFlushed (self, hwRscFlushed):
        self.hwRscFlushed = hwRscFlushed
        self.setHasHwRscFlushed()

    def setLscInt (self, lscInt):
        self.lscInt = lscInt
        self.setHasLscInt()

    def setHwRscAggregated (self, hwRscAggregated):
        self.hwRscAggregated = hwRscAggregated
        self.setHasHwRscAggregated()

    def setRxLongLengthErrors (self, rxLongLengthErrors):
        self.rxLongLengthErrors = rxLongLengthErrors
        self.setHasRxLongLengthErrors()

    def setFdirMatch (self, fdirMatch):
        self.fdirMatch = fdirMatch
        self.setHasFdirMatch()

    def setTxFcoePackets (self, txFcoePackets):
        self.txFcoePackets = txFcoePackets
        self.setHasTxFcoePackets()

    def setRxShortLengthErrors (self, rxShortLengthErrors):
        self.rxShortLengthErrors = rxShortLengthErrors
        self.setHasRxShortLengthErrors()

    def setRxFcoeDwords (self, rxFcoeDwords):
        self.rxFcoeDwords = rxFcoeDwords
        self.setHasRxFcoeDwords()

    def setRxBytesNic (self, rxBytesNic):
        self.rxBytesNic = rxBytesNic
        self.setHasRxBytesNic()

    def setRxFcoePackets (self, rxFcoePackets):
        self.rxFcoePackets = rxFcoePackets
        self.setHasRxFcoePackets()

    def setTxFcoeDwords (self, txFcoeDwords):
        self.txFcoeDwords = txFcoeDwords
        self.setHasTxFcoeDwords()

    def setRxNoBufferCount (self, rxNoBufferCount):
        self.rxNoBufferCount = rxNoBufferCount
        self.setHasRxNoBufferCount()

    def setRxFifoErrors (self, rxFifoErrors):
        self.rxFifoErrors = rxFifoErrors
        self.setHasRxFifoErrors()

    def setAllocRxPageFailed (self, allocRxPageFailed):
        self.allocRxPageFailed = allocRxPageFailed
        self.setHasAllocRxPageFailed()

    def setTxBusy (self, txBusy):
        self.txBusy = txBusy
        self.setHasTxBusy()

    def setTxAbortedErrors (self, txAbortedErrors):
        self.txAbortedErrors = txAbortedErrors
        self.setHasTxAbortedErrors()

    def setCollisions (self, collisions):
        self.collisions = collisions
        self.setHasCollisions()

    def setTxHeartbeatErrors (self, txHeartbeatErrors):
        self.txHeartbeatErrors = txHeartbeatErrors
        self.setHasTxHeartbeatErrors()

    def setRxMissedErrors (self, rxMissedErrors):
        self.rxMissedErrors = rxMissedErrors
        self.setHasRxMissedErrors()

    def setNonEopDescs (self, nonEopDescs):
        self.nonEopDescs = nonEopDescs
        self.setHasNonEopDescs()

    def setTxFlowControlXon (self, txFlowControlXon):
        self.txFlowControlXon = txFlowControlXon
        self.setHasTxFlowControlXon()

    def setRxCsumOffloadErrors (self, rxCsumOffloadErrors):
        self.rxCsumOffloadErrors = rxCsumOffloadErrors
        self.setHasRxCsumOffloadErrors()

    def setRxCrcErrors (self, rxCrcErrors):
        self.rxCrcErrors = rxCrcErrors
        self.setHasRxCrcErrors()

    def setTxFifoErrors (self, txFifoErrors):
        self.txFifoErrors = txFifoErrors
        self.setHasTxFifoErrors()

    def setTxPktsNic (self, txPktsNic):
        self.txPktsNic = txPktsNic
        self.setHasTxPktsNic()

    def setRxFcoeDropped (self, rxFcoeDropped):
        self.rxFcoeDropped = rxFcoeDropped
        self.setHasRxFcoeDropped()

    def setTxBytesNic (self, txBytesNic):
        self.txBytesNic = txBytesNic
        self.setHasTxBytesNic()

    def setAllocRxBuffFailed (self, allocRxBuffFailed):
        self.allocRxBuffFailed = allocRxBuffFailed
        self.setHasAllocRxBuffFailed()

    def setFcoeBadFccrc (self, fcoeBadFccrc):
        self.fcoeBadFccrc = fcoeBadFccrc
        self.setHasFcoeBadFccrc()

    def setTxFlowControlXoff (self, txFlowControlXoff):
        self.txFlowControlXoff = txFlowControlXoff
        self.setHasTxFlowControlXoff()

    def setTxTimeoutCount (self, txTimeoutCount):
        self.txTimeoutCount = txTimeoutCount
        self.setHasTxTimeoutCount()

    def setTxCarrierErrors (self, txCarrierErrors):
        self.txCarrierErrors = txCarrierErrors
        self.setHasTxCarrierErrors()

    def setRxFlowControlXoff (self, rxFlowControlXoff):
        self.rxFlowControlXoff = rxFlowControlXoff
        self.setHasRxFlowControlXoff()

    def setFdirMiss (self, fdirMiss):
        self.fdirMiss = fdirMiss
        self.setHasFdirMiss()

    def setRxNoDmaResources (self, rxNoDmaResources):
        self.rxNoDmaResources = rxNoDmaResources
        self.setHasRxNoDmaResources()

    def setRxOverErrors (self, rxOverErrors):
        self.rxOverErrors = rxOverErrors
        self.setHasRxOverErrors()

    def setRxFlowControlXon (self, rxFlowControlXon):
        self.rxFlowControlXon = rxFlowControlXon
        self.setHasRxFlowControlXon()

    def setTxRestartQueue (self, txRestartQueue):
        self.txRestartQueue = txRestartQueue
        self.setHasTxRestartQueue()

    def setRxFrameErrors (self, rxFrameErrors):
        self.rxFrameErrors = rxFrameErrors
        self.setHasRxFrameErrors()

    def setRxPktsNic (self, rxPktsNic):
        self.rxPktsNic = rxPktsNic
        self.setHasRxPktsNic()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.counters.counters_oper_data_gen import CountersOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "interfaces", 
            "isCurrent": false
        }, 
        {
            "namespace": "interface", 
            "isCurrent": false
        }, 
        {
            "namespace": "device", 
            "isCurrent": false
        }, 
        {
            "namespace": "counters", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "hwRscFlushed", 
            "yangName": "hw-rsc-flushed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "lscInt", 
            "yangName": "lsc-int", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "hwRscAggregated", 
            "yangName": "hw-rsc-aggregated", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxLongLengthErrors", 
            "yangName": "rx-long-length-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "fdirMatch", 
            "yangName": "fdir-match", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFcoePackets", 
            "yangName": "tx-fcoe-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxShortLengthErrors", 
            "yangName": "rx-short-length-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFcoeDwords", 
            "yangName": "rx-fcoe-dwords", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxBytesNic", 
            "yangName": "rx-bytes-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFcoePackets", 
            "yangName": "rx-fcoe-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFcoeDwords", 
            "yangName": "tx-fcoe-dwords", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxNoBufferCount", 
            "yangName": "rx-no-buffer-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFifoErrors", 
            "yangName": "rx-fifo-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "allocRxPageFailed", 
            "yangName": "alloc-rx-page-failed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txBusy", 
            "yangName": "tx-busy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txAbortedErrors", 
            "yangName": "tx-aborted-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "collisions", 
            "yangName": "collisions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txHeartbeatErrors", 
            "yangName": "tx-heartbeat-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxMissedErrors", 
            "yangName": "rx-missed-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "nonEopDescs", 
            "yangName": "non-eop-descs", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFlowControlXon", 
            "yangName": "tx-flow-control-xon", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxCsumOffloadErrors", 
            "yangName": "rx-csum-offload-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxCrcErrors", 
            "yangName": "rx-crc-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFifoErrors", 
            "yangName": "tx-fifo-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txPktsNic", 
            "yangName": "tx-pkts-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFcoeDropped", 
            "yangName": "rx-fcoe-dropped", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txBytesNic", 
            "yangName": "tx-bytes-nic", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "allocRxBuffFailed", 
            "yangName": "alloc-rx-buff-failed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "fcoeBadFccrc", 
            "yangName": "fcoe-bad-fccrc", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txFlowControlXoff", 
            "yangName": "tx-flow-control-xoff", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txTimeoutCount", 
            "yangName": "tx-timeout-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txCarrierErrors", 
            "yangName": "tx-carrier-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFlowControlXoff", 
            "yangName": "rx-flow-control-xoff", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "fdirMiss", 
            "yangName": "fdir-miss", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxNoDmaResources", 
            "yangName": "rx-no-dma-resources", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxOverErrors", 
            "yangName": "rx-over-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFlowControlXon", 
            "yangName": "rx-flow-control-xon", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "txRestartQueue", 
            "yangName": "tx-restart-queue", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rxFrameErrors", 
            "yangName": "rx-frame-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
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
    "createTime": "2013"
}
"""


