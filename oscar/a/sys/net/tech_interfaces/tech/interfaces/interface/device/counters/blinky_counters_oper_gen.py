



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.counters.counters_oper_data_gen import CountersOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef









class BlinkyOperCounters(BlinkyOperNode):

    _kCallpointName = "tech-interfaces-interface-device-counters-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "tech-interfaces-interface-device-counters-callpoint"
        
        self.myGetObjectFunctor = None
        
        

    def getCallpointName (self):
        return self.kCallpointName

    def setParent (self, parentNode):
        for logFunc in self._log("set-parent").debug2Func(): logFunc("called")
        BlinkyOperNode.setParent(self, parentNode)

        

        return ReturnCodes.kOk

    def distributeConfigObjectToDescendants (self, configObj):
        for logFunc in self._log("distribute-config-object-to-descendants").debug3Func(): logFunc("called. configObj=%s", configObj)

        
        return ReturnCodes.kOk

    def getOperRelativePath (self, operRelativePath):
        for logFunc in self._log("get-oper-relative-path").debug3Func(): logFunc("called")
        
        val = Value()
        val.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        operRelativePath.addKeyPathPostfix(val)
        
        for logFunc in self._log("getOperRelativePath-done").debug3Func(): logFunc("done. operRelativePath=%s", operRelativePath)


    def setOperDataRequestedFields (self, operData, keyPath):
        __pychecker__="maxbranches=100 maxlines=500"
        for logFunc in self._log("set-oper-data-requested-fields").debug3Func(): logFunc("called. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
        flattenedSelfKeyPath = self.myKeyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        requestedKeyPath = keyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        
        if requestedKeyPath.isEqual(flattenedSelfKeyPath) or (requestedKeyPath.getLen() <= flattenedSelfKeyPath.getLen()):
        
            operData.setAllRequested()
        else:
            
            for logFunc in self._log("set-oper-data-requested-fields-checking-fields").debug3Func(): logFunc("requestedKeyPath=%s, flattenedSelfKeyPath=%s", requestedKeyPath, flattenedSelfKeyPath)
            if requestedKeyPath.getLen() > flattenedSelfKeyPath.getLen():
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "hw-rsc-flushed"):
                    for logFunc in self._log("set-oper-data-requested-fields-hwrscflushed-requested").debug3Func(): logFunc(
                        "hw-rsc-flushed requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setHwRscFlushedRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "lsc-int"):
                    for logFunc in self._log("set-oper-data-requested-fields-lscint-requested").debug3Func(): logFunc(
                        "lsc-int requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setLscIntRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "hw-rsc-aggregated"):
                    for logFunc in self._log("set-oper-data-requested-fields-hwrscaggregated-requested").debug3Func(): logFunc(
                        "hw-rsc-aggregated requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setHwRscAggregatedRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-long-length-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxlonglengtherrors-requested").debug3Func(): logFunc(
                        "rx-long-length-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxLongLengthErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "fdir-match"):
                    for logFunc in self._log("set-oper-data-requested-fields-fdirmatch-requested").debug3Func(): logFunc(
                        "fdir-match requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setFdirMatchRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-fcoe-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-txfcoepackets-requested").debug3Func(): logFunc(
                        "tx-fcoe-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxFcoePacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-short-length-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxshortlengtherrors-requested").debug3Func(): logFunc(
                        "rx-short-length-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxShortLengthErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-fcoe-dwords"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxfcoedwords-requested").debug3Func(): logFunc(
                        "rx-fcoe-dwords requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxFcoeDwordsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-bytes-nic"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxbytesnic-requested").debug3Func(): logFunc(
                        "rx-bytes-nic requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxBytesNicRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-fcoe-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxfcoepackets-requested").debug3Func(): logFunc(
                        "rx-fcoe-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxFcoePacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-fcoe-dwords"):
                    for logFunc in self._log("set-oper-data-requested-fields-txfcoedwords-requested").debug3Func(): logFunc(
                        "tx-fcoe-dwords requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxFcoeDwordsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-no-buffer-count"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxnobuffercount-requested").debug3Func(): logFunc(
                        "rx-no-buffer-count requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxNoBufferCountRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-fifo-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxfifoerrors-requested").debug3Func(): logFunc(
                        "rx-fifo-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxFifoErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "alloc-rx-page-failed"):
                    for logFunc in self._log("set-oper-data-requested-fields-allocrxpagefailed-requested").debug3Func(): logFunc(
                        "alloc-rx-page-failed requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setAllocRxPageFailedRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-busy"):
                    for logFunc in self._log("set-oper-data-requested-fields-txbusy-requested").debug3Func(): logFunc(
                        "tx-busy requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxBusyRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-aborted-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-txabortederrors-requested").debug3Func(): logFunc(
                        "tx-aborted-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxAbortedErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "collisions"):
                    for logFunc in self._log("set-oper-data-requested-fields-collisions-requested").debug3Func(): logFunc(
                        "collisions requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setCollisionsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-heartbeat-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-txheartbeaterrors-requested").debug3Func(): logFunc(
                        "tx-heartbeat-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxHeartbeatErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-missed-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxmissederrors-requested").debug3Func(): logFunc(
                        "rx-missed-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxMissedErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "non-eop-descs"):
                    for logFunc in self._log("set-oper-data-requested-fields-noneopdescs-requested").debug3Func(): logFunc(
                        "non-eop-descs requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setNonEopDescsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-flow-control-xon"):
                    for logFunc in self._log("set-oper-data-requested-fields-txflowcontrolxon-requested").debug3Func(): logFunc(
                        "tx-flow-control-xon requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxFlowControlXonRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-csum-offload-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxcsumoffloaderrors-requested").debug3Func(): logFunc(
                        "rx-csum-offload-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxCsumOffloadErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-crc-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxcrcerrors-requested").debug3Func(): logFunc(
                        "rx-crc-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxCrcErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-fifo-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-txfifoerrors-requested").debug3Func(): logFunc(
                        "tx-fifo-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxFifoErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-pkts-nic"):
                    for logFunc in self._log("set-oper-data-requested-fields-txpktsnic-requested").debug3Func(): logFunc(
                        "tx-pkts-nic requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxPktsNicRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-fcoe-dropped"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxfcoedropped-requested").debug3Func(): logFunc(
                        "rx-fcoe-dropped requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxFcoeDroppedRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-bytes-nic"):
                    for logFunc in self._log("set-oper-data-requested-fields-txbytesnic-requested").debug3Func(): logFunc(
                        "tx-bytes-nic requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxBytesNicRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "alloc-rx-buff-failed"):
                    for logFunc in self._log("set-oper-data-requested-fields-allocrxbufffailed-requested").debug3Func(): logFunc(
                        "alloc-rx-buff-failed requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setAllocRxBuffFailedRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "fcoe-bad-fccrc"):
                    for logFunc in self._log("set-oper-data-requested-fields-fcoebadfccrc-requested").debug3Func(): logFunc(
                        "fcoe-bad-fccrc requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setFcoeBadFccrcRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-flow-control-xoff"):
                    for logFunc in self._log("set-oper-data-requested-fields-txflowcontrolxoff-requested").debug3Func(): logFunc(
                        "tx-flow-control-xoff requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxFlowControlXoffRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-timeout-count"):
                    for logFunc in self._log("set-oper-data-requested-fields-txtimeoutcount-requested").debug3Func(): logFunc(
                        "tx-timeout-count requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxTimeoutCountRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-carrier-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-txcarriererrors-requested").debug3Func(): logFunc(
                        "tx-carrier-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxCarrierErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-flow-control-xoff"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxflowcontrolxoff-requested").debug3Func(): logFunc(
                        "rx-flow-control-xoff requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxFlowControlXoffRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "fdir-miss"):
                    for logFunc in self._log("set-oper-data-requested-fields-fdirmiss-requested").debug3Func(): logFunc(
                        "fdir-miss requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setFdirMissRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-no-dma-resources"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxnodmaresources-requested").debug3Func(): logFunc(
                        "rx-no-dma-resources requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxNoDmaResourcesRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-over-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxovererrors-requested").debug3Func(): logFunc(
                        "rx-over-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxOverErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-flow-control-xon"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxflowcontrolxon-requested").debug3Func(): logFunc(
                        "rx-flow-control-xon requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxFlowControlXonRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-restart-queue"):
                    for logFunc in self._log("set-oper-data-requested-fields-txrestartqueue-requested").debug3Func(): logFunc(
                        "tx-restart-queue requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setTxRestartQueueRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-frame-errors"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxframeerrors-requested").debug3Func(): logFunc(
                        "rx-frame-errors requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxFrameErrorsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-pkts-nic"):
                    for logFunc in self._log("set-oper-data-requested-fields-rxpktsnic-requested").debug3Func(): logFunc(
                        "rx-pkts-nic requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setRxPktsNicRequested()
                
            else:
                for logFunc in self._log("set-oper-data-requested-fields-bad-keypath").errorFunc(): logFunc(
                    "don't know how to handle this keyPath. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                return ReturnCodes.kGeneralError

        for logFunc in self._log("set-oper-data-requested-fields-done").debug3Func(): logFunc("done. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
        return ReturnCodes.kOk

    

    def fillTagValues (self, keyPath, tagValueList, operData):
        initialListSize = tagValueList.getLen()
        for logFunc in self._log("fill-tag-values").debug3Func(): logFunc("called. operData=%s, keyPath=%s, initialListSize=%d", operData.debugStr(True), keyPath, initialListSize)
        # fill tag values up to current
        if self.myKeyPath.isEqualLen(keyPath, keyPath.getLen()):
            i = keyPath.getLen()
            while i < self.myKeyPath.getLen():
                valBegin = Value()
                (tag, ns, prefix) = self.myKeyPath.getAt(i).asXmlTag()
                valBegin.setXmlBegin((tag, ns, prefix))
                tagValueList.push((tag, ns), valBegin)
                for logFunc in self._log("fill-tag-values-adding").debug3Func(): logFunc("adding xml begin. i=%d, valBegin=%s, self.myKeyPath.getLen()=%d", i, valBegin, self.myKeyPath.getLen())
                i+=1
        
        if operData.isHwRscFlushedRequested() and operData.hasHwRscFlushed():
            val = Value()
            val.setUint64(operData.hwRscFlushed)
            tagValueList.push(("hw-rsc-flushed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isLscIntRequested() and operData.hasLscInt():
            val = Value()
            val.setUint64(operData.lscInt)
            tagValueList.push(("lsc-int", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isHwRscAggregatedRequested() and operData.hasHwRscAggregated():
            val = Value()
            val.setUint64(operData.hwRscAggregated)
            tagValueList.push(("hw-rsc-aggregated", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxLongLengthErrorsRequested() and operData.hasRxLongLengthErrors():
            val = Value()
            val.setUint64(operData.rxLongLengthErrors)
            tagValueList.push(("rx-long-length-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isFdirMatchRequested() and operData.hasFdirMatch():
            val = Value()
            val.setUint64(operData.fdirMatch)
            tagValueList.push(("fdir-match", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxFcoePacketsRequested() and operData.hasTxFcoePackets():
            val = Value()
            val.setUint64(operData.txFcoePackets)
            tagValueList.push(("tx-fcoe-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxShortLengthErrorsRequested() and operData.hasRxShortLengthErrors():
            val = Value()
            val.setUint64(operData.rxShortLengthErrors)
            tagValueList.push(("rx-short-length-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxFcoeDwordsRequested() and operData.hasRxFcoeDwords():
            val = Value()
            val.setUint64(operData.rxFcoeDwords)
            tagValueList.push(("rx-fcoe-dwords", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxBytesNicRequested() and operData.hasRxBytesNic():
            val = Value()
            val.setUint64(operData.rxBytesNic)
            tagValueList.push(("rx-bytes-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxFcoePacketsRequested() and operData.hasRxFcoePackets():
            val = Value()
            val.setUint64(operData.rxFcoePackets)
            tagValueList.push(("rx-fcoe-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxFcoeDwordsRequested() and operData.hasTxFcoeDwords():
            val = Value()
            val.setUint64(operData.txFcoeDwords)
            tagValueList.push(("tx-fcoe-dwords", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxNoBufferCountRequested() and operData.hasRxNoBufferCount():
            val = Value()
            val.setUint64(operData.rxNoBufferCount)
            tagValueList.push(("rx-no-buffer-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxFifoErrorsRequested() and operData.hasRxFifoErrors():
            val = Value()
            val.setUint64(operData.rxFifoErrors)
            tagValueList.push(("rx-fifo-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isAllocRxPageFailedRequested() and operData.hasAllocRxPageFailed():
            val = Value()
            val.setUint64(operData.allocRxPageFailed)
            tagValueList.push(("alloc-rx-page-failed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxBusyRequested() and operData.hasTxBusy():
            val = Value()
            val.setUint64(operData.txBusy)
            tagValueList.push(("tx-busy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxAbortedErrorsRequested() and operData.hasTxAbortedErrors():
            val = Value()
            val.setUint64(operData.txAbortedErrors)
            tagValueList.push(("tx-aborted-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isCollisionsRequested() and operData.hasCollisions():
            val = Value()
            val.setUint64(operData.collisions)
            tagValueList.push(("collisions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxHeartbeatErrorsRequested() and operData.hasTxHeartbeatErrors():
            val = Value()
            val.setUint64(operData.txHeartbeatErrors)
            tagValueList.push(("tx-heartbeat-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxMissedErrorsRequested() and operData.hasRxMissedErrors():
            val = Value()
            val.setUint64(operData.rxMissedErrors)
            tagValueList.push(("rx-missed-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isNonEopDescsRequested() and operData.hasNonEopDescs():
            val = Value()
            val.setUint64(operData.nonEopDescs)
            tagValueList.push(("non-eop-descs", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxFlowControlXonRequested() and operData.hasTxFlowControlXon():
            val = Value()
            val.setUint64(operData.txFlowControlXon)
            tagValueList.push(("tx-flow-control-xon", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxCsumOffloadErrorsRequested() and operData.hasRxCsumOffloadErrors():
            val = Value()
            val.setUint64(operData.rxCsumOffloadErrors)
            tagValueList.push(("rx-csum-offload-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxCrcErrorsRequested() and operData.hasRxCrcErrors():
            val = Value()
            val.setUint64(operData.rxCrcErrors)
            tagValueList.push(("rx-crc-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxFifoErrorsRequested() and operData.hasTxFifoErrors():
            val = Value()
            val.setUint64(operData.txFifoErrors)
            tagValueList.push(("tx-fifo-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxPktsNicRequested() and operData.hasTxPktsNic():
            val = Value()
            val.setUint64(operData.txPktsNic)
            tagValueList.push(("tx-pkts-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxFcoeDroppedRequested() and operData.hasRxFcoeDropped():
            val = Value()
            val.setUint64(operData.rxFcoeDropped)
            tagValueList.push(("rx-fcoe-dropped", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxBytesNicRequested() and operData.hasTxBytesNic():
            val = Value()
            val.setUint64(operData.txBytesNic)
            tagValueList.push(("tx-bytes-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isAllocRxBuffFailedRequested() and operData.hasAllocRxBuffFailed():
            val = Value()
            val.setUint64(operData.allocRxBuffFailed)
            tagValueList.push(("alloc-rx-buff-failed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isFcoeBadFccrcRequested() and operData.hasFcoeBadFccrc():
            val = Value()
            val.setUint64(operData.fcoeBadFccrc)
            tagValueList.push(("fcoe-bad-fccrc", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxFlowControlXoffRequested() and operData.hasTxFlowControlXoff():
            val = Value()
            val.setUint64(operData.txFlowControlXoff)
            tagValueList.push(("tx-flow-control-xoff", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxTimeoutCountRequested() and operData.hasTxTimeoutCount():
            val = Value()
            val.setUint64(operData.txTimeoutCount)
            tagValueList.push(("tx-timeout-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxCarrierErrorsRequested() and operData.hasTxCarrierErrors():
            val = Value()
            val.setUint64(operData.txCarrierErrors)
            tagValueList.push(("tx-carrier-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxFlowControlXoffRequested() and operData.hasRxFlowControlXoff():
            val = Value()
            val.setUint64(operData.rxFlowControlXoff)
            tagValueList.push(("rx-flow-control-xoff", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isFdirMissRequested() and operData.hasFdirMiss():
            val = Value()
            val.setUint64(operData.fdirMiss)
            tagValueList.push(("fdir-miss", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxNoDmaResourcesRequested() and operData.hasRxNoDmaResources():
            val = Value()
            val.setUint64(operData.rxNoDmaResources)
            tagValueList.push(("rx-no-dma-resources", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxOverErrorsRequested() and operData.hasRxOverErrors():
            val = Value()
            val.setUint64(operData.rxOverErrors)
            tagValueList.push(("rx-over-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxFlowControlXonRequested() and operData.hasRxFlowControlXon():
            val = Value()
            val.setUint64(operData.rxFlowControlXon)
            tagValueList.push(("rx-flow-control-xon", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isTxRestartQueueRequested() and operData.hasTxRestartQueue():
            val = Value()
            val.setUint64(operData.txRestartQueue)
            tagValueList.push(("tx-restart-queue", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxFrameErrorsRequested() and operData.hasRxFrameErrors():
            val = Value()
            val.setUint64(operData.rxFrameErrors)
            tagValueList.push(("rx-frame-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isRxPktsNicRequested() and operData.hasRxPktsNic():
            val = Value()
            val.setUint64(operData.rxPktsNic)
            tagValueList.push(("rx-pkts-nic", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        
        if self.myKeyPath.isEqualLen(keyPath, keyPath.getLen()):
            i = self.myKeyPath.getLen() - 1
            while i >= keyPath.getLen():
                valEnd = Value()
                (tag, ns, prefix) = self.myKeyPath.getAt(i).asXmlTag()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
                i-=1

        for logFunc in self._log("fill-tag-values-ended").debug3Func(): logFunc("ended. operData=%s, keyPath=%s, initialListSize=%d, finalListSize=%d",
                                                  operData.debugStr(True), keyPath, initialListSize, tagValueList.getLen())
        return ReturnCodes.kOk

    def fillValue (self, value, keyPath, operData):
        __pychecker__="maxbranches=100 maxlines=500"
        for logFunc in self._log("fill-value").debug3Func(): logFunc("called. keyPath=%s, operData=%s", keyPath, operData.debugStr(True))
        flattenedSelfKeyPath = self.myKeyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        requestedKeyPath = keyPath.getKeyPathPostfixFlattened(self.myConfigNode.getKeyPath(), False)
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "hw-rsc-flushed"):
            if operData.isHwRscFlushedRequested():
                 if operData.hasHwRscFlushed():
                     value.setUint64(operData.hwRscFlushed)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "lsc-int"):
            if operData.isLscIntRequested():
                 if operData.hasLscInt():
                     value.setUint64(operData.lscInt)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "hw-rsc-aggregated"):
            if operData.isHwRscAggregatedRequested():
                 if operData.hasHwRscAggregated():
                     value.setUint64(operData.hwRscAggregated)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-long-length-errors"):
            if operData.isRxLongLengthErrorsRequested():
                 if operData.hasRxLongLengthErrors():
                     value.setUint64(operData.rxLongLengthErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "fdir-match"):
            if operData.isFdirMatchRequested():
                 if operData.hasFdirMatch():
                     value.setUint64(operData.fdirMatch)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-fcoe-packets"):
            if operData.isTxFcoePacketsRequested():
                 if operData.hasTxFcoePackets():
                     value.setUint64(operData.txFcoePackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-short-length-errors"):
            if operData.isRxShortLengthErrorsRequested():
                 if operData.hasRxShortLengthErrors():
                     value.setUint64(operData.rxShortLengthErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-fcoe-dwords"):
            if operData.isRxFcoeDwordsRequested():
                 if operData.hasRxFcoeDwords():
                     value.setUint64(operData.rxFcoeDwords)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-bytes-nic"):
            if operData.isRxBytesNicRequested():
                 if operData.hasRxBytesNic():
                     value.setUint64(operData.rxBytesNic)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-fcoe-packets"):
            if operData.isRxFcoePacketsRequested():
                 if operData.hasRxFcoePackets():
                     value.setUint64(operData.rxFcoePackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-fcoe-dwords"):
            if operData.isTxFcoeDwordsRequested():
                 if operData.hasTxFcoeDwords():
                     value.setUint64(operData.txFcoeDwords)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-no-buffer-count"):
            if operData.isRxNoBufferCountRequested():
                 if operData.hasRxNoBufferCount():
                     value.setUint64(operData.rxNoBufferCount)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-fifo-errors"):
            if operData.isRxFifoErrorsRequested():
                 if operData.hasRxFifoErrors():
                     value.setUint64(operData.rxFifoErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "alloc-rx-page-failed"):
            if operData.isAllocRxPageFailedRequested():
                 if operData.hasAllocRxPageFailed():
                     value.setUint64(operData.allocRxPageFailed)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-busy"):
            if operData.isTxBusyRequested():
                 if operData.hasTxBusy():
                     value.setUint64(operData.txBusy)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-aborted-errors"):
            if operData.isTxAbortedErrorsRequested():
                 if operData.hasTxAbortedErrors():
                     value.setUint64(operData.txAbortedErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "collisions"):
            if operData.isCollisionsRequested():
                 if operData.hasCollisions():
                     value.setUint64(operData.collisions)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-heartbeat-errors"):
            if operData.isTxHeartbeatErrorsRequested():
                 if operData.hasTxHeartbeatErrors():
                     value.setUint64(operData.txHeartbeatErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-missed-errors"):
            if operData.isRxMissedErrorsRequested():
                 if operData.hasRxMissedErrors():
                     value.setUint64(operData.rxMissedErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "non-eop-descs"):
            if operData.isNonEopDescsRequested():
                 if operData.hasNonEopDescs():
                     value.setUint64(operData.nonEopDescs)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-flow-control-xon"):
            if operData.isTxFlowControlXonRequested():
                 if operData.hasTxFlowControlXon():
                     value.setUint64(operData.txFlowControlXon)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-csum-offload-errors"):
            if operData.isRxCsumOffloadErrorsRequested():
                 if operData.hasRxCsumOffloadErrors():
                     value.setUint64(operData.rxCsumOffloadErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-crc-errors"):
            if operData.isRxCrcErrorsRequested():
                 if operData.hasRxCrcErrors():
                     value.setUint64(operData.rxCrcErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-fifo-errors"):
            if operData.isTxFifoErrorsRequested():
                 if operData.hasTxFifoErrors():
                     value.setUint64(operData.txFifoErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-pkts-nic"):
            if operData.isTxPktsNicRequested():
                 if operData.hasTxPktsNic():
                     value.setUint64(operData.txPktsNic)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-fcoe-dropped"):
            if operData.isRxFcoeDroppedRequested():
                 if operData.hasRxFcoeDropped():
                     value.setUint64(operData.rxFcoeDropped)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-bytes-nic"):
            if operData.isTxBytesNicRequested():
                 if operData.hasTxBytesNic():
                     value.setUint64(operData.txBytesNic)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "alloc-rx-buff-failed"):
            if operData.isAllocRxBuffFailedRequested():
                 if operData.hasAllocRxBuffFailed():
                     value.setUint64(operData.allocRxBuffFailed)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "fcoe-bad-fccrc"):
            if operData.isFcoeBadFccrcRequested():
                 if operData.hasFcoeBadFccrc():
                     value.setUint64(operData.fcoeBadFccrc)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-flow-control-xoff"):
            if operData.isTxFlowControlXoffRequested():
                 if operData.hasTxFlowControlXoff():
                     value.setUint64(operData.txFlowControlXoff)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-timeout-count"):
            if operData.isTxTimeoutCountRequested():
                 if operData.hasTxTimeoutCount():
                     value.setUint64(operData.txTimeoutCount)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-carrier-errors"):
            if operData.isTxCarrierErrorsRequested():
                 if operData.hasTxCarrierErrors():
                     value.setUint64(operData.txCarrierErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-flow-control-xoff"):
            if operData.isRxFlowControlXoffRequested():
                 if operData.hasRxFlowControlXoff():
                     value.setUint64(operData.rxFlowControlXoff)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "fdir-miss"):
            if operData.isFdirMissRequested():
                 if operData.hasFdirMiss():
                     value.setUint64(operData.fdirMiss)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-no-dma-resources"):
            if operData.isRxNoDmaResourcesRequested():
                 if operData.hasRxNoDmaResources():
                     value.setUint64(operData.rxNoDmaResources)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-over-errors"):
            if operData.isRxOverErrorsRequested():
                 if operData.hasRxOverErrors():
                     value.setUint64(operData.rxOverErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-flow-control-xon"):
            if operData.isRxFlowControlXonRequested():
                 if operData.hasRxFlowControlXon():
                     value.setUint64(operData.rxFlowControlXon)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "tx-restart-queue"):
            if operData.isTxRestartQueueRequested():
                 if operData.hasTxRestartQueue():
                     value.setUint64(operData.txRestartQueue)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-frame-errors"):
            if operData.isRxFrameErrorsRequested():
                 if operData.hasRxFrameErrors():
                     value.setUint64(operData.rxFrameErrors)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "rx-pkts-nic"):
            if operData.isRxPktsNicRequested():
                 if operData.hasRxPktsNic():
                     value.setUint64(operData.rxPktsNic)
                 else:
                     value.setEmpty()
        
        
        for logFunc in self._log("fill-value-ended").debug3Func(): logFunc("ended. keyPath=%s, operData=%s, value=%s", keyPath, operData.debugStr(True), value)
        return ReturnCodes.kOk


    def replyObject (self, dpTrxCtx, keyPath, operData):
        for logFunc in self._log("reply-object").debug3Func(): logFunc("called. dpTrxCtx=%s, operData=%s, keyPath=%s", dpTrxCtx, operData.debugStr(True), keyPath)
        tagValueList = TagValues()
        res = self.fillTagValues(keyPath, tagValueList, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-object-fill-tag-values-failed").errorFunc(): logFunc(
                "fillTagValues() failed. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
            return ReturnCodes.kGeneralError
        res = self.myDomain.sendTagValues(dpTrxCtx, tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-object-send-tag-values-failed").errorFunc(): logFunc(
                "myDomain.sendTagValues() failed. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def replyElement (self, dpTrxCtx, keyPath, operData):
        for logFunc in self._log("reply-element").debug3Func(): logFunc("called. dpTrxCtx=%s, operData=%s, keyPath=%s", dpTrxCtx, operData.debugStr(True), keyPath)
        val = Value()
        res = self.fillValue(val, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-element-fill-value-failed").errorFunc(): logFunc(
                "fillValue() failed. operData=%s, keyPath=%s", operData.debugStr(True), keyPath)
            return ReturnCodes.kGeneralError
        res = self.myDomain.sendValue(dpTrxCtx, val)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("reply-element-send-value-failed").errorFunc(): logFunc(
                "myDomain.sendValue() failed. operData=%s, keyPath=%s, value=%s", operData.debugStr(True), keyPath, val)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def getObject (self, trxContext, keyPath):
        for logFunc in self._log("get-object").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)
        operData = CountersOperData()

        res = self.handleGetRequest(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-object-handle-get-request-failed").errorFunc(): logFunc(
                "handleGetRequest() failed. operData=%s, keyPath=%s, trxContext=%s", operData.debugStr(True), keyPath, trxContext)
            return ReturnCodes.kGeneralError

        res = self.replyObject(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-object-reply-object-failed").errorFunc(): logFunc(
                "handleGetRequest() failed. operData=%s, keyPath=%s, trxContext=%s", operData.debugStr(True), keyPath, trxContext)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def handleGetRequest (self, trxContext, keyPath, operData):
        for logFunc in self._log("handle-get-request").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        

        res = self.setOperDataRequestedFields(operData, keyPath)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("handle-get-request-set-oper-data-requested-fields-failed").errorFunc(): logFunc(
                "setOperDataRequestedFields() failed. keyPath=%s, trxContext=%s", keyPath, trxContext)
            return ReturnCodes.kGeneralError

        if self.myIsActive:
            if self.myGetObjectFunctor:
                timeoutGuardName = str(self.myKeyPath) + "-" + "get-object-functor";
                timeoutGuard = TimeoutGuard(self._log, timeoutGuardName, 
                                            self.getFunctorTimeout(self.GET_OBJ_FUNCTOR), 
                                            self.getFunctorMildTimeout(self.GET_OBJ_FUNCTOR))
                
                
                
                
                
                
                
                res = self.myGetObjectFunctor(trxContext, 
                                              
                                              
                                              operData)
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myGetObjectFunctor.__name__)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("handle-get-request-functor-failed").errorFunc(): logFunc(
                        "functor failed. keyPath=%s, trxContext=%s", keyPath, trxContext)
                    return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def getElement (self, trxContext, keyPath):
        for logFunc in self._log("get-element").debug3Func(): logFunc("called. trxContext=%s, keyPath=%s", trxContext, keyPath)

        operData = CountersOperData()
        res = self.handleGetRequest(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-element-handle-get-request-failed").errorFunc(): logFunc(
                "handleGetRequest() failed. keyPath=%s, trxContext=%s, operData=%s", keyPath, trxContext, operData.debugStr(True))
            return ReturnCodes.kGeneralError

        res = self.replyElement(trxContext, keyPath, operData)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("get-element-reply-element-failed").errorFunc(): logFunc(
                "replyElement() failed. keyPath=%s, trxContext=%s, operData=%s", keyPath, trxContext, operData.debugStr(True))
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def setBasicFunctors (self, getObjFunctor):
        if self.myIsActive:
            for logFunc in self._log("set-basic-functor-active").errorFunc(): logFunc("illegal when blinky active.")
            return

        self.myGetObjectFunctor = getObjFunctor
        self.myFunctorsSet = True







"""
Extracted from the below data: 
{
    "node": {
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.counters.counters_oper_data_gen import CountersOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "qt-if", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "counters", 
        "namespace": "counters", 
        "logGroupName": "blinky-counters-oper", 
        "className": "BlinkyOperCounters", 
        "logModuleName": "a-sys-net-tech-interfaces-tech-interfaces-interface-device-counters-blinky-counters-oper-gen", 
        "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.device.counters.blinky_counters_oper_gen import BlinkyOperCounters", 
        "callpointName": "tech-interfaces-interface-device-counters-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
        "dataClassName": "CountersOperData", 
        "getObjArgsNum": 2, 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "isOper": false, 
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
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "device"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "counters"
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
    "env": [
        "a", 
        "sys", 
        "net", 
        "tech_interfaces"
    ], 
    "createTime": "2013"
}
"""


