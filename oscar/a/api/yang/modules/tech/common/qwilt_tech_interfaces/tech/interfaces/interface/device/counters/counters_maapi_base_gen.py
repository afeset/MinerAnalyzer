


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class CountersMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , interface
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , interface
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # hwRscFlushed
    def requestHwRscFlushed (self, requested):
        raise NotImplementedError()

    def isHwRscFlushedRequested (self):
        raise NotImplementedError()

    def getHwRscFlushed (self):
        raise NotImplementedError()

    def hasHwRscFlushed (self):
        raise NotImplementedError()

    def setHwRscFlushed (self, hwRscFlushed):
        raise NotImplementedError()

    # lscInt
    def requestLscInt (self, requested):
        raise NotImplementedError()

    def isLscIntRequested (self):
        raise NotImplementedError()

    def getLscInt (self):
        raise NotImplementedError()

    def hasLscInt (self):
        raise NotImplementedError()

    def setLscInt (self, lscInt):
        raise NotImplementedError()

    # hwRscAggregated
    def requestHwRscAggregated (self, requested):
        raise NotImplementedError()

    def isHwRscAggregatedRequested (self):
        raise NotImplementedError()

    def getHwRscAggregated (self):
        raise NotImplementedError()

    def hasHwRscAggregated (self):
        raise NotImplementedError()

    def setHwRscAggregated (self, hwRscAggregated):
        raise NotImplementedError()

    # rxLongLengthErrors
    def requestRxLongLengthErrors (self, requested):
        raise NotImplementedError()

    def isRxLongLengthErrorsRequested (self):
        raise NotImplementedError()

    def getRxLongLengthErrors (self):
        raise NotImplementedError()

    def hasRxLongLengthErrors (self):
        raise NotImplementedError()

    def setRxLongLengthErrors (self, rxLongLengthErrors):
        raise NotImplementedError()

    # fdirMatch
    def requestFdirMatch (self, requested):
        raise NotImplementedError()

    def isFdirMatchRequested (self):
        raise NotImplementedError()

    def getFdirMatch (self):
        raise NotImplementedError()

    def hasFdirMatch (self):
        raise NotImplementedError()

    def setFdirMatch (self, fdirMatch):
        raise NotImplementedError()

    # txFcoePackets
    def requestTxFcoePackets (self, requested):
        raise NotImplementedError()

    def isTxFcoePacketsRequested (self):
        raise NotImplementedError()

    def getTxFcoePackets (self):
        raise NotImplementedError()

    def hasTxFcoePackets (self):
        raise NotImplementedError()

    def setTxFcoePackets (self, txFcoePackets):
        raise NotImplementedError()

    # rxShortLengthErrors
    def requestRxShortLengthErrors (self, requested):
        raise NotImplementedError()

    def isRxShortLengthErrorsRequested (self):
        raise NotImplementedError()

    def getRxShortLengthErrors (self):
        raise NotImplementedError()

    def hasRxShortLengthErrors (self):
        raise NotImplementedError()

    def setRxShortLengthErrors (self, rxShortLengthErrors):
        raise NotImplementedError()

    # rxFcoeDwords
    def requestRxFcoeDwords (self, requested):
        raise NotImplementedError()

    def isRxFcoeDwordsRequested (self):
        raise NotImplementedError()

    def getRxFcoeDwords (self):
        raise NotImplementedError()

    def hasRxFcoeDwords (self):
        raise NotImplementedError()

    def setRxFcoeDwords (self, rxFcoeDwords):
        raise NotImplementedError()

    # rxBytesNic
    def requestRxBytesNic (self, requested):
        raise NotImplementedError()

    def isRxBytesNicRequested (self):
        raise NotImplementedError()

    def getRxBytesNic (self):
        raise NotImplementedError()

    def hasRxBytesNic (self):
        raise NotImplementedError()

    def setRxBytesNic (self, rxBytesNic):
        raise NotImplementedError()

    # rxFcoePackets
    def requestRxFcoePackets (self, requested):
        raise NotImplementedError()

    def isRxFcoePacketsRequested (self):
        raise NotImplementedError()

    def getRxFcoePackets (self):
        raise NotImplementedError()

    def hasRxFcoePackets (self):
        raise NotImplementedError()

    def setRxFcoePackets (self, rxFcoePackets):
        raise NotImplementedError()

    # txFcoeDwords
    def requestTxFcoeDwords (self, requested):
        raise NotImplementedError()

    def isTxFcoeDwordsRequested (self):
        raise NotImplementedError()

    def getTxFcoeDwords (self):
        raise NotImplementedError()

    def hasTxFcoeDwords (self):
        raise NotImplementedError()

    def setTxFcoeDwords (self, txFcoeDwords):
        raise NotImplementedError()

    # rxNoBufferCount
    def requestRxNoBufferCount (self, requested):
        raise NotImplementedError()

    def isRxNoBufferCountRequested (self):
        raise NotImplementedError()

    def getRxNoBufferCount (self):
        raise NotImplementedError()

    def hasRxNoBufferCount (self):
        raise NotImplementedError()

    def setRxNoBufferCount (self, rxNoBufferCount):
        raise NotImplementedError()

    # rxFifoErrors
    def requestRxFifoErrors (self, requested):
        raise NotImplementedError()

    def isRxFifoErrorsRequested (self):
        raise NotImplementedError()

    def getRxFifoErrors (self):
        raise NotImplementedError()

    def hasRxFifoErrors (self):
        raise NotImplementedError()

    def setRxFifoErrors (self, rxFifoErrors):
        raise NotImplementedError()

    # allocRxPageFailed
    def requestAllocRxPageFailed (self, requested):
        raise NotImplementedError()

    def isAllocRxPageFailedRequested (self):
        raise NotImplementedError()

    def getAllocRxPageFailed (self):
        raise NotImplementedError()

    def hasAllocRxPageFailed (self):
        raise NotImplementedError()

    def setAllocRxPageFailed (self, allocRxPageFailed):
        raise NotImplementedError()

    # txBusy
    def requestTxBusy (self, requested):
        raise NotImplementedError()

    def isTxBusyRequested (self):
        raise NotImplementedError()

    def getTxBusy (self):
        raise NotImplementedError()

    def hasTxBusy (self):
        raise NotImplementedError()

    def setTxBusy (self, txBusy):
        raise NotImplementedError()

    # txAbortedErrors
    def requestTxAbortedErrors (self, requested):
        raise NotImplementedError()

    def isTxAbortedErrorsRequested (self):
        raise NotImplementedError()

    def getTxAbortedErrors (self):
        raise NotImplementedError()

    def hasTxAbortedErrors (self):
        raise NotImplementedError()

    def setTxAbortedErrors (self, txAbortedErrors):
        raise NotImplementedError()

    # collisions
    def requestCollisions (self, requested):
        raise NotImplementedError()

    def isCollisionsRequested (self):
        raise NotImplementedError()

    def getCollisions (self):
        raise NotImplementedError()

    def hasCollisions (self):
        raise NotImplementedError()

    def setCollisions (self, collisions):
        raise NotImplementedError()

    # txHeartbeatErrors
    def requestTxHeartbeatErrors (self, requested):
        raise NotImplementedError()

    def isTxHeartbeatErrorsRequested (self):
        raise NotImplementedError()

    def getTxHeartbeatErrors (self):
        raise NotImplementedError()

    def hasTxHeartbeatErrors (self):
        raise NotImplementedError()

    def setTxHeartbeatErrors (self, txHeartbeatErrors):
        raise NotImplementedError()

    # rxMissedErrors
    def requestRxMissedErrors (self, requested):
        raise NotImplementedError()

    def isRxMissedErrorsRequested (self):
        raise NotImplementedError()

    def getRxMissedErrors (self):
        raise NotImplementedError()

    def hasRxMissedErrors (self):
        raise NotImplementedError()

    def setRxMissedErrors (self, rxMissedErrors):
        raise NotImplementedError()

    # nonEopDescs
    def requestNonEopDescs (self, requested):
        raise NotImplementedError()

    def isNonEopDescsRequested (self):
        raise NotImplementedError()

    def getNonEopDescs (self):
        raise NotImplementedError()

    def hasNonEopDescs (self):
        raise NotImplementedError()

    def setNonEopDescs (self, nonEopDescs):
        raise NotImplementedError()

    # txFlowControlXon
    def requestTxFlowControlXon (self, requested):
        raise NotImplementedError()

    def isTxFlowControlXonRequested (self):
        raise NotImplementedError()

    def getTxFlowControlXon (self):
        raise NotImplementedError()

    def hasTxFlowControlXon (self):
        raise NotImplementedError()

    def setTxFlowControlXon (self, txFlowControlXon):
        raise NotImplementedError()

    # rxCsumOffloadErrors
    def requestRxCsumOffloadErrors (self, requested):
        raise NotImplementedError()

    def isRxCsumOffloadErrorsRequested (self):
        raise NotImplementedError()

    def getRxCsumOffloadErrors (self):
        raise NotImplementedError()

    def hasRxCsumOffloadErrors (self):
        raise NotImplementedError()

    def setRxCsumOffloadErrors (self, rxCsumOffloadErrors):
        raise NotImplementedError()

    # rxCrcErrors
    def requestRxCrcErrors (self, requested):
        raise NotImplementedError()

    def isRxCrcErrorsRequested (self):
        raise NotImplementedError()

    def getRxCrcErrors (self):
        raise NotImplementedError()

    def hasRxCrcErrors (self):
        raise NotImplementedError()

    def setRxCrcErrors (self, rxCrcErrors):
        raise NotImplementedError()

    # txFifoErrors
    def requestTxFifoErrors (self, requested):
        raise NotImplementedError()

    def isTxFifoErrorsRequested (self):
        raise NotImplementedError()

    def getTxFifoErrors (self):
        raise NotImplementedError()

    def hasTxFifoErrors (self):
        raise NotImplementedError()

    def setTxFifoErrors (self, txFifoErrors):
        raise NotImplementedError()

    # txPktsNic
    def requestTxPktsNic (self, requested):
        raise NotImplementedError()

    def isTxPktsNicRequested (self):
        raise NotImplementedError()

    def getTxPktsNic (self):
        raise NotImplementedError()

    def hasTxPktsNic (self):
        raise NotImplementedError()

    def setTxPktsNic (self, txPktsNic):
        raise NotImplementedError()

    # rxFcoeDropped
    def requestRxFcoeDropped (self, requested):
        raise NotImplementedError()

    def isRxFcoeDroppedRequested (self):
        raise NotImplementedError()

    def getRxFcoeDropped (self):
        raise NotImplementedError()

    def hasRxFcoeDropped (self):
        raise NotImplementedError()

    def setRxFcoeDropped (self, rxFcoeDropped):
        raise NotImplementedError()

    # txBytesNic
    def requestTxBytesNic (self, requested):
        raise NotImplementedError()

    def isTxBytesNicRequested (self):
        raise NotImplementedError()

    def getTxBytesNic (self):
        raise NotImplementedError()

    def hasTxBytesNic (self):
        raise NotImplementedError()

    def setTxBytesNic (self, txBytesNic):
        raise NotImplementedError()

    # allocRxBuffFailed
    def requestAllocRxBuffFailed (self, requested):
        raise NotImplementedError()

    def isAllocRxBuffFailedRequested (self):
        raise NotImplementedError()

    def getAllocRxBuffFailed (self):
        raise NotImplementedError()

    def hasAllocRxBuffFailed (self):
        raise NotImplementedError()

    def setAllocRxBuffFailed (self, allocRxBuffFailed):
        raise NotImplementedError()

    # fcoeBadFccrc
    def requestFcoeBadFccrc (self, requested):
        raise NotImplementedError()

    def isFcoeBadFccrcRequested (self):
        raise NotImplementedError()

    def getFcoeBadFccrc (self):
        raise NotImplementedError()

    def hasFcoeBadFccrc (self):
        raise NotImplementedError()

    def setFcoeBadFccrc (self, fcoeBadFccrc):
        raise NotImplementedError()

    # txFlowControlXoff
    def requestTxFlowControlXoff (self, requested):
        raise NotImplementedError()

    def isTxFlowControlXoffRequested (self):
        raise NotImplementedError()

    def getTxFlowControlXoff (self):
        raise NotImplementedError()

    def hasTxFlowControlXoff (self):
        raise NotImplementedError()

    def setTxFlowControlXoff (self, txFlowControlXoff):
        raise NotImplementedError()

    # txTimeoutCount
    def requestTxTimeoutCount (self, requested):
        raise NotImplementedError()

    def isTxTimeoutCountRequested (self):
        raise NotImplementedError()

    def getTxTimeoutCount (self):
        raise NotImplementedError()

    def hasTxTimeoutCount (self):
        raise NotImplementedError()

    def setTxTimeoutCount (self, txTimeoutCount):
        raise NotImplementedError()

    # txCarrierErrors
    def requestTxCarrierErrors (self, requested):
        raise NotImplementedError()

    def isTxCarrierErrorsRequested (self):
        raise NotImplementedError()

    def getTxCarrierErrors (self):
        raise NotImplementedError()

    def hasTxCarrierErrors (self):
        raise NotImplementedError()

    def setTxCarrierErrors (self, txCarrierErrors):
        raise NotImplementedError()

    # rxFlowControlXoff
    def requestRxFlowControlXoff (self, requested):
        raise NotImplementedError()

    def isRxFlowControlXoffRequested (self):
        raise NotImplementedError()

    def getRxFlowControlXoff (self):
        raise NotImplementedError()

    def hasRxFlowControlXoff (self):
        raise NotImplementedError()

    def setRxFlowControlXoff (self, rxFlowControlXoff):
        raise NotImplementedError()

    # fdirMiss
    def requestFdirMiss (self, requested):
        raise NotImplementedError()

    def isFdirMissRequested (self):
        raise NotImplementedError()

    def getFdirMiss (self):
        raise NotImplementedError()

    def hasFdirMiss (self):
        raise NotImplementedError()

    def setFdirMiss (self, fdirMiss):
        raise NotImplementedError()

    # rxNoDmaResources
    def requestRxNoDmaResources (self, requested):
        raise NotImplementedError()

    def isRxNoDmaResourcesRequested (self):
        raise NotImplementedError()

    def getRxNoDmaResources (self):
        raise NotImplementedError()

    def hasRxNoDmaResources (self):
        raise NotImplementedError()

    def setRxNoDmaResources (self, rxNoDmaResources):
        raise NotImplementedError()

    # rxOverErrors
    def requestRxOverErrors (self, requested):
        raise NotImplementedError()

    def isRxOverErrorsRequested (self):
        raise NotImplementedError()

    def getRxOverErrors (self):
        raise NotImplementedError()

    def hasRxOverErrors (self):
        raise NotImplementedError()

    def setRxOverErrors (self, rxOverErrors):
        raise NotImplementedError()

    # rxFlowControlXon
    def requestRxFlowControlXon (self, requested):
        raise NotImplementedError()

    def isRxFlowControlXonRequested (self):
        raise NotImplementedError()

    def getRxFlowControlXon (self):
        raise NotImplementedError()

    def hasRxFlowControlXon (self):
        raise NotImplementedError()

    def setRxFlowControlXon (self, rxFlowControlXon):
        raise NotImplementedError()

    # txRestartQueue
    def requestTxRestartQueue (self, requested):
        raise NotImplementedError()

    def isTxRestartQueueRequested (self):
        raise NotImplementedError()

    def getTxRestartQueue (self):
        raise NotImplementedError()

    def hasTxRestartQueue (self):
        raise NotImplementedError()

    def setTxRestartQueue (self, txRestartQueue):
        raise NotImplementedError()

    # rxFrameErrors
    def requestRxFrameErrors (self, requested):
        raise NotImplementedError()

    def isRxFrameErrorsRequested (self):
        raise NotImplementedError()

    def getRxFrameErrors (self):
        raise NotImplementedError()

    def hasRxFrameErrors (self):
        raise NotImplementedError()

    def setRxFrameErrors (self, rxFrameErrors):
        raise NotImplementedError()

    # rxPktsNic
    def requestRxPktsNic (self, requested):
        raise NotImplementedError()

    def isRxPktsNicRequested (self):
        raise NotImplementedError()

    def getRxPktsNic (self):
        raise NotImplementedError()

    def hasRxPktsNic (self):
        raise NotImplementedError()

    def setRxPktsNic (self, rxPktsNic):
        raise NotImplementedError()




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


