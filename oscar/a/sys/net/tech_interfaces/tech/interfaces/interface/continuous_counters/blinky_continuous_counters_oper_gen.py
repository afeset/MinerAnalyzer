



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.continuous_counters.continuous_counters_oper_data_gen import ContinuousCountersOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef









class BlinkyOperContinuousCounters(BlinkyOperNode):

    _kCallpointName = "tech-interfaces-interface-continuous-counters-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "tech-interfaces-interface-continuous-counters-callpoint"
        
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
        val.setXmlTag(("continuous-counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-gratuitous-arp-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-outgratuitousarppackets-requested").debug3Func(): logFunc(
                        "out-gratuitous-arp-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOutGratuitousArpPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-unicast-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-outunicastpackets-requested").debug3Func(): logFunc(
                        "out-unicast-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOutUnicastPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-unknown-protocol-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-inunknownprotocolpackets-requested").debug3Func(): logFunc(
                        "in-unknown-protocol-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInUnknownProtocolPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-discard-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-outdiscardpackets-requested").debug3Func(): logFunc(
                        "out-discard-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOutDiscardPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-octets"):
                    for logFunc in self._log("set-oper-data-requested-fields-inoctets-requested").debug3Func(): logFunc(
                        "in-octets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInOctetsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-error-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-inerrorpackets-requested").debug3Func(): logFunc(
                        "in-error-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInErrorPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-packets-rate"):
                    for logFunc in self._log("set-oper-data-requested-fields-inpacketsrate-requested").debug3Func(): logFunc(
                        "in-packets-rate requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInPacketsRateRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-outpackets-requested").debug3Func(): logFunc(
                        "out-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOutPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-discard-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-indiscardpackets-requested").debug3Func(): logFunc(
                        "in-discard-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInDiscardPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-multicast-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-inmulticastpackets-requested").debug3Func(): logFunc(
                        "in-multicast-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInMulticastPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-broadcast-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-outbroadcastpackets-requested").debug3Func(): logFunc(
                        "out-broadcast-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOutBroadcastPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-octets"):
                    for logFunc in self._log("set-oper-data-requested-fields-outoctets-requested").debug3Func(): logFunc(
                        "out-octets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOutOctetsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-multicast-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-outmulticastpackets-requested").debug3Func(): logFunc(
                        "out-multicast-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOutMulticastPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-unicast-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-inunicastpackets-requested").debug3Func(): logFunc(
                        "in-unicast-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInUnicastPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-error-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-outerrorpackets-requested").debug3Func(): logFunc(
                        "out-error-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOutErrorPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-packets-rate"):
                    for logFunc in self._log("set-oper-data-requested-fields-outpacketsrate-requested").debug3Func(): logFunc(
                        "out-packets-rate requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOutPacketsRateRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-inpackets-requested").debug3Func(): logFunc(
                        "in-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInPacketsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "operational-status-changes"):
                    for logFunc in self._log("set-oper-data-requested-fields-operationalstatuschanges-requested").debug3Func(): logFunc(
                        "operational-status-changes requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOperationalStatusChangesRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-bits-rate"):
                    for logFunc in self._log("set-oper-data-requested-fields-inbitsrate-requested").debug3Func(): logFunc(
                        "in-bits-rate requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInBitsRateRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-bits-rate"):
                    for logFunc in self._log("set-oper-data-requested-fields-outbitsrate-requested").debug3Func(): logFunc(
                        "out-bits-rate requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOutBitsRateRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-broadcast-packets"):
                    for logFunc in self._log("set-oper-data-requested-fields-inbroadcastpackets-requested").debug3Func(): logFunc(
                        "in-broadcast-packets requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setInBroadcastPacketsRequested()
                
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
        
        if operData.isOutGratuitousArpPacketsRequested() and operData.hasOutGratuitousArpPackets():
            val = Value()
            val.setUint64(operData.outGratuitousArpPackets)
            tagValueList.push(("out-gratuitous-arp-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isOutUnicastPacketsRequested() and operData.hasOutUnicastPackets():
            val = Value()
            val.setUint64(operData.outUnicastPackets)
            tagValueList.push(("out-unicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isInUnknownProtocolPacketsRequested() and operData.hasInUnknownProtocolPackets():
            val = Value()
            val.setUint64(operData.inUnknownProtocolPackets)
            tagValueList.push(("in-unknown-protocol-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isOutDiscardPacketsRequested() and operData.hasOutDiscardPackets():
            val = Value()
            val.setUint64(operData.outDiscardPackets)
            tagValueList.push(("out-discard-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isInOctetsRequested() and operData.hasInOctets():
            val = Value()
            val.setUint64(operData.inOctets)
            tagValueList.push(("in-octets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isInErrorPacketsRequested() and operData.hasInErrorPackets():
            val = Value()
            val.setUint64(operData.inErrorPackets)
            tagValueList.push(("in-error-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isInPacketsRateRequested() and operData.hasInPacketsRate():
            val = Value()
            val.setUint64(operData.inPacketsRate)
            tagValueList.push(("in-packets-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isOutPacketsRequested() and operData.hasOutPackets():
            val = Value()
            val.setUint64(operData.outPackets)
            tagValueList.push(("out-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isInDiscardPacketsRequested() and operData.hasInDiscardPackets():
            val = Value()
            val.setUint64(operData.inDiscardPackets)
            tagValueList.push(("in-discard-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isInMulticastPacketsRequested() and operData.hasInMulticastPackets():
            val = Value()
            val.setUint64(operData.inMulticastPackets)
            tagValueList.push(("in-multicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isOutBroadcastPacketsRequested() and operData.hasOutBroadcastPackets():
            val = Value()
            val.setUint64(operData.outBroadcastPackets)
            tagValueList.push(("out-broadcast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isOutOctetsRequested() and operData.hasOutOctets():
            val = Value()
            val.setUint64(operData.outOctets)
            tagValueList.push(("out-octets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isOutMulticastPacketsRequested() and operData.hasOutMulticastPackets():
            val = Value()
            val.setUint64(operData.outMulticastPackets)
            tagValueList.push(("out-multicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isInUnicastPacketsRequested() and operData.hasInUnicastPackets():
            val = Value()
            val.setUint64(operData.inUnicastPackets)
            tagValueList.push(("in-unicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isOutErrorPacketsRequested() and operData.hasOutErrorPackets():
            val = Value()
            val.setUint64(operData.outErrorPackets)
            tagValueList.push(("out-error-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isOutPacketsRateRequested() and operData.hasOutPacketsRate():
            val = Value()
            val.setUint64(operData.outPacketsRate)
            tagValueList.push(("out-packets-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isInPacketsRequested() and operData.hasInPackets():
            val = Value()
            val.setUint64(operData.inPackets)
            tagValueList.push(("in-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isOperationalStatusChangesRequested() and operData.hasOperationalStatusChanges():
            val = Value()
            val.setUint64(operData.operationalStatusChanges)
            tagValueList.push(("operational-status-changes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isInBitsRateRequested() and operData.hasInBitsRate():
            val = Value()
            val.setUint64(operData.inBitsRate)
            tagValueList.push(("in-bits-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isOutBitsRateRequested() and operData.hasOutBitsRate():
            val = Value()
            val.setUint64(operData.outBitsRate)
            tagValueList.push(("out-bits-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        if operData.isInBroadcastPacketsRequested() and operData.hasInBroadcastPackets():
            val = Value()
            val.setUint64(operData.inBroadcastPackets)
            tagValueList.push(("in-broadcast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), val)
        
        
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
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-gratuitous-arp-packets"):
            if operData.isOutGratuitousArpPacketsRequested():
                 if operData.hasOutGratuitousArpPackets():
                     value.setUint64(operData.outGratuitousArpPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-unicast-packets"):
            if operData.isOutUnicastPacketsRequested():
                 if operData.hasOutUnicastPackets():
                     value.setUint64(operData.outUnicastPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-unknown-protocol-packets"):
            if operData.isInUnknownProtocolPacketsRequested():
                 if operData.hasInUnknownProtocolPackets():
                     value.setUint64(operData.inUnknownProtocolPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-discard-packets"):
            if operData.isOutDiscardPacketsRequested():
                 if operData.hasOutDiscardPackets():
                     value.setUint64(operData.outDiscardPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-octets"):
            if operData.isInOctetsRequested():
                 if operData.hasInOctets():
                     value.setUint64(operData.inOctets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-error-packets"):
            if operData.isInErrorPacketsRequested():
                 if operData.hasInErrorPackets():
                     value.setUint64(operData.inErrorPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-packets-rate"):
            if operData.isInPacketsRateRequested():
                 if operData.hasInPacketsRate():
                     value.setUint64(operData.inPacketsRate)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-packets"):
            if operData.isOutPacketsRequested():
                 if operData.hasOutPackets():
                     value.setUint64(operData.outPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-discard-packets"):
            if operData.isInDiscardPacketsRequested():
                 if operData.hasInDiscardPackets():
                     value.setUint64(operData.inDiscardPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-multicast-packets"):
            if operData.isInMulticastPacketsRequested():
                 if operData.hasInMulticastPackets():
                     value.setUint64(operData.inMulticastPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-broadcast-packets"):
            if operData.isOutBroadcastPacketsRequested():
                 if operData.hasOutBroadcastPackets():
                     value.setUint64(operData.outBroadcastPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-octets"):
            if operData.isOutOctetsRequested():
                 if operData.hasOutOctets():
                     value.setUint64(operData.outOctets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-multicast-packets"):
            if operData.isOutMulticastPacketsRequested():
                 if operData.hasOutMulticastPackets():
                     value.setUint64(operData.outMulticastPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-unicast-packets"):
            if operData.isInUnicastPacketsRequested():
                 if operData.hasInUnicastPackets():
                     value.setUint64(operData.inUnicastPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-error-packets"):
            if operData.isOutErrorPacketsRequested():
                 if operData.hasOutErrorPackets():
                     value.setUint64(operData.outErrorPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-packets-rate"):
            if operData.isOutPacketsRateRequested():
                 if operData.hasOutPacketsRate():
                     value.setUint64(operData.outPacketsRate)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-packets"):
            if operData.isInPacketsRequested():
                 if operData.hasInPackets():
                     value.setUint64(operData.inPackets)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "operational-status-changes"):
            if operData.isOperationalStatusChangesRequested():
                 if operData.hasOperationalStatusChanges():
                     value.setUint64(operData.operationalStatusChanges)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-bits-rate"):
            if operData.isInBitsRateRequested():
                 if operData.hasInBitsRate():
                     value.setUint64(operData.inBitsRate)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "out-bits-rate"):
            if operData.isOutBitsRateRequested():
                 if operData.hasOutBitsRate():
                     value.setUint64(operData.outBitsRate)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "in-broadcast-packets"):
            if operData.isInBroadcastPacketsRequested():
                 if operData.hasInBroadcastPackets():
                     value.setUint64(operData.inBroadcastPackets)
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
        operData = ContinuousCountersOperData()

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

        operData = ContinuousCountersOperData()
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.continuous_counters.continuous_counters_oper_data_gen import ContinuousCountersOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "qt-if", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "continuous-counters", 
        "namespace": "continuous_counters", 
        "logGroupName": "blinky-continuous-counters-oper", 
        "className": "BlinkyOperContinuousCounters", 
        "logModuleName": "a-sys-net-tech-interfaces-tech-interfaces-interface-continuous-counters-blinky-continuous-counters-oper-gen", 
        "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.continuous_counters.blinky_continuous_counters_oper_gen import BlinkyOperContinuousCounters", 
        "callpointName": "tech-interfaces-interface-continuous-counters-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
        "dataClassName": "ContinuousCountersOperData", 
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
            "yangName": "continuous-counters", 
            "namespace": "continuous_counters", 
            "isCurrent": true, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "continuous-counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outGratuitousArpPackets", 
            "yangName": "out-gratuitous-arp-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outUnicastPackets", 
            "yangName": "out-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnknownProtocolPackets", 
            "yangName": "in-unknown-protocol-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outDiscardPackets", 
            "yangName": "out-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inOctets", 
            "yangName": "in-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inErrorPackets", 
            "yangName": "in-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPacketsRate", 
            "yangName": "in-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPackets", 
            "yangName": "out-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inDiscardPackets", 
            "yangName": "in-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inMulticastPackets", 
            "yangName": "in-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBroadcastPackets", 
            "yangName": "out-broadcast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outOctets", 
            "yangName": "out-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outMulticastPackets", 
            "yangName": "out-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnicastPackets", 
            "yangName": "in-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outErrorPackets", 
            "yangName": "out-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPacketsRate", 
            "yangName": "out-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPackets", 
            "yangName": "in-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "operationalStatusChanges", 
            "yangName": "operational-status-changes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBitsRate", 
            "yangName": "in-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBitsRate", 
            "yangName": "out-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBroadcastPackets", 
            "yangName": "in-broadcast-packets", 
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


