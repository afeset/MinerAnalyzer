



# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperContainer
__pychecker__="no-classattr"

from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.counters.counters_oper_data_gen import CountersOperData
from a.sys.blinky.blinky_oper_node import BlinkyOperNode
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.tag_values import TagValues

from a.infra.misc.timeout_guard import TimeoutGuard
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.pass_by_ref import PassByRef









class BlinkyOperCounters(BlinkyOperNode):

    _kCallpointName = "tech-network-ipv6-application-initiated-discovery-counters-callpoint"

    GET_OBJ_FUNCTOR = 'GET_OBJ_FUNCTOR'

    


    def __init__ (self, logger):
        BlinkyOperNode.__init__(self, logger)
        self.kCallpointName = "tech-network-ipv6-application-initiated-discovery-counters-callpoint"
        
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
        val.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
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
            
                
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-entry-discards"):
                    for logFunc in self._log("set-oper-data-requested-fields-applicationentrydiscards-requested").debug3Func(): logFunc(
                        "application-entry-discards requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setApplicationEntryDiscardsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "neighbor-discovery-failures"):
                    for logFunc in self._log("set-oper-data-requested-fields-neighbordiscoveryfailures-requested").debug3Func(): logFunc(
                        "neighbor-discovery-failures requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setNeighborDiscoveryFailuresRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "neighbor-discovery-timeouts"):
                    for logFunc in self._log("set-oper-data-requested-fields-neighbordiscoverytimeouts-requested").debug3Func(): logFunc(
                        "neighbor-discovery-timeouts requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setNeighborDiscoveryTimeoutsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "neighbor-discovery-successes"):
                    for logFunc in self._log("set-oper-data-requested-fields-neighbordiscoverysuccesses-requested").debug3Func(): logFunc(
                        "neighbor-discovery-successes requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setNeighborDiscoverySuccessesRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "polls"):
                    for logFunc in self._log("set-oper-data-requested-fields-polls-requested").debug3Func(): logFunc(
                        "polls requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setPollsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-request-failures"):
                    for logFunc in self._log("set-oper-data-requested-fields-applicationrequestfailures-requested").debug3Func(): logFunc(
                        "application-request-failures requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setApplicationRequestFailuresRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-entry-updates"):
                    for logFunc in self._log("set-oper-data-requested-fields-applicationentryupdates-requested").debug3Func(): logFunc(
                        "application-entry-updates requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setApplicationEntryUpdatesRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "os-table-load-failures"):
                    for logFunc in self._log("set-oper-data-requested-fields-ostableloadfailures-requested").debug3Func(): logFunc(
                        "os-table-load-failures requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOsTableLoadFailuresRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-request-discards"):
                    for logFunc in self._log("set-oper-data-requested-fields-applicationrequestdiscards-requested").debug3Func(): logFunc(
                        "application-request-discards requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setApplicationRequestDiscardsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-request-blocks"):
                    for logFunc in self._log("set-oper-data-requested-fields-applicationrequestblocks-requested").debug3Func(): logFunc(
                        "application-request-blocks requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setApplicationRequestBlocksRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-requests"):
                    for logFunc in self._log("set-oper-data-requested-fields-applicationrequests-requested").debug3Func(): logFunc(
                        "application-requests requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setApplicationRequestsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "os-table-loads"):
                    for logFunc in self._log("set-oper-data-requested-fields-ostableloads-requested").debug3Func(): logFunc(
                        "os-table-loads requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setOsTableLoadsRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "neighbor-discovery-requests-sent"):
                    for logFunc in self._log("set-oper-data-requested-fields-neighbordiscoveryrequestssent-requested").debug3Func(): logFunc(
                        "neighbor-discovery-requests-sent requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setNeighborDiscoveryRequestsSentRequested()
                
                if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-entry-failures"):
                    for logFunc in self._log("set-oper-data-requested-fields-applicationentryfailures-requested").debug3Func(): logFunc(
                        "application-entry-failures requested. requestedKeyPath=%s, operData=%s", requestedKeyPath, operData.debugStr(True))
                    operData.setApplicationEntryFailuresRequested()
                
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
        
        if operData.isApplicationEntryDiscardsRequested() and operData.hasApplicationEntryDiscards():
            val = Value()
            val.setInt64(operData.applicationEntryDiscards)
            tagValueList.push(("application-entry-discards", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isNeighborDiscoveryFailuresRequested() and operData.hasNeighborDiscoveryFailures():
            val = Value()
            val.setInt64(operData.neighborDiscoveryFailures)
            tagValueList.push(("neighbor-discovery-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isNeighborDiscoveryTimeoutsRequested() and operData.hasNeighborDiscoveryTimeouts():
            val = Value()
            val.setInt64(operData.neighborDiscoveryTimeouts)
            tagValueList.push(("neighbor-discovery-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isNeighborDiscoverySuccessesRequested() and operData.hasNeighborDiscoverySuccesses():
            val = Value()
            val.setInt64(operData.neighborDiscoverySuccesses)
            tagValueList.push(("neighbor-discovery-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isPollsRequested() and operData.hasPolls():
            val = Value()
            val.setInt64(operData.polls)
            tagValueList.push(("polls", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isApplicationRequestFailuresRequested() and operData.hasApplicationRequestFailures():
            val = Value()
            val.setInt64(operData.applicationRequestFailures)
            tagValueList.push(("application-request-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isApplicationEntryUpdatesRequested() and operData.hasApplicationEntryUpdates():
            val = Value()
            val.setInt64(operData.applicationEntryUpdates)
            tagValueList.push(("application-entry-updates", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isOsTableLoadFailuresRequested() and operData.hasOsTableLoadFailures():
            val = Value()
            val.setInt64(operData.osTableLoadFailures)
            tagValueList.push(("os-table-load-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isApplicationRequestDiscardsRequested() and operData.hasApplicationRequestDiscards():
            val = Value()
            val.setInt64(operData.applicationRequestDiscards)
            tagValueList.push(("application-request-discards", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isApplicationRequestBlocksRequested() and operData.hasApplicationRequestBlocks():
            val = Value()
            val.setInt64(operData.applicationRequestBlocks)
            tagValueList.push(("application-request-blocks", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isApplicationRequestsRequested() and operData.hasApplicationRequests():
            val = Value()
            val.setInt64(operData.applicationRequests)
            tagValueList.push(("application-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isOsTableLoadsRequested() and operData.hasOsTableLoads():
            val = Value()
            val.setInt64(operData.osTableLoads)
            tagValueList.push(("os-table-loads", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isNeighborDiscoveryRequestsSentRequested() and operData.hasNeighborDiscoveryRequestsSent():
            val = Value()
            val.setInt64(operData.neighborDiscoveryRequestsSent)
            tagValueList.push(("neighbor-discovery-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        if operData.isApplicationEntryFailuresRequested() and operData.hasApplicationEntryFailures():
            val = Value()
            val.setInt64(operData.applicationEntryFailures)
            tagValueList.push(("application-entry-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), val)
        
        
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
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-entry-discards"):
            if operData.isApplicationEntryDiscardsRequested():
                 if operData.hasApplicationEntryDiscards():
                     value.setInt64(operData.applicationEntryDiscards)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "neighbor-discovery-failures"):
            if operData.isNeighborDiscoveryFailuresRequested():
                 if operData.hasNeighborDiscoveryFailures():
                     value.setInt64(operData.neighborDiscoveryFailures)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "neighbor-discovery-timeouts"):
            if operData.isNeighborDiscoveryTimeoutsRequested():
                 if operData.hasNeighborDiscoveryTimeouts():
                     value.setInt64(operData.neighborDiscoveryTimeouts)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "neighbor-discovery-successes"):
            if operData.isNeighborDiscoverySuccessesRequested():
                 if operData.hasNeighborDiscoverySuccesses():
                     value.setInt64(operData.neighborDiscoverySuccesses)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "polls"):
            if operData.isPollsRequested():
                 if operData.hasPolls():
                     value.setInt64(operData.polls)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-request-failures"):
            if operData.isApplicationRequestFailuresRequested():
                 if operData.hasApplicationRequestFailures():
                     value.setInt64(operData.applicationRequestFailures)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-entry-updates"):
            if operData.isApplicationEntryUpdatesRequested():
                 if operData.hasApplicationEntryUpdates():
                     value.setInt64(operData.applicationEntryUpdates)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "os-table-load-failures"):
            if operData.isOsTableLoadFailuresRequested():
                 if operData.hasOsTableLoadFailures():
                     value.setInt64(operData.osTableLoadFailures)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-request-discards"):
            if operData.isApplicationRequestDiscardsRequested():
                 if operData.hasApplicationRequestDiscards():
                     value.setInt64(operData.applicationRequestDiscards)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-request-blocks"):
            if operData.isApplicationRequestBlocksRequested():
                 if operData.hasApplicationRequestBlocks():
                     value.setInt64(operData.applicationRequestBlocks)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-requests"):
            if operData.isApplicationRequestsRequested():
                 if operData.hasApplicationRequests():
                     value.setInt64(operData.applicationRequests)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "os-table-loads"):
            if operData.isOsTableLoadsRequested():
                 if operData.hasOsTableLoads():
                     value.setInt64(operData.osTableLoads)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "neighbor-discovery-requests-sent"):
            if operData.isNeighborDiscoveryRequestsSentRequested():
                 if operData.hasNeighborDiscoveryRequestsSent():
                     value.setInt64(operData.neighborDiscoveryRequestsSent)
                 else:
                     value.setEmpty()
        
        if requestedKeyPath.isTagEqual(flattenedSelfKeyPath.getLen(), "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "application-entry-failures"):
            if operData.isApplicationEntryFailuresRequested():
                 if operData.hasApplicationEntryFailures():
                     value.setInt64(operData.applicationEntryFailures)
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.counters.counters_oper_data_gen import CountersOperData", 
        "callpointResponsible": true, 
        "moduleYangNamespacePrefix": "qt-net-ip6", 
        "validationPoint": null, 
        "getNextArgsNum": 4, 
        "yangName": "counters", 
        "namespace": "counters", 
        "logGroupName": "blinky-counters-oper", 
        "className": "BlinkyOperCounters", 
        "logModuleName": "a-sys-net-tech-network-ipv6-tech-network-ipv6-neighbors-application-initiated-discovery-counters-blinky-counters-oper-gen", 
        "importStatement": "from a.sys.net.tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.counters.blinky_counters_oper_gen import BlinkyOperCounters", 
        "callpointName": "tech-network-ipv6-application-initiated-discovery-counters-callpoint", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
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
            "moduleYangNamespacePrefix": "qt-net", 
            "yangName": "network", 
            "namespace": "network", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network", 
            "name": "network"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "ipv6", 
            "namespace": "ipv6", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "ipv6"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "neighbors", 
            "namespace": "neighbors", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "neighbors"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "application-initiated-discovery", 
            "namespace": "application_initiated_discovery", 
            "isCurrent": false, 
            "isList": false, 
            "isOper": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "application-initiated-discovery"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "isOper": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryDiscards", 
            "yangName": "application-entry-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryFailures", 
            "yangName": "neighbor-discovery-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryTimeouts", 
            "yangName": "neighbor-discovery-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoverySuccesses", 
            "yangName": "neighbor-discovery-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "polls", 
            "yangName": "polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestFailures", 
            "yangName": "application-request-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryUpdates", 
            "yangName": "application-entry-updates", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoadFailures", 
            "yangName": "os-table-load-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestDiscards", 
            "yangName": "application-request-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestBlocks", 
            "yangName": "application-request-blocks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequests", 
            "yangName": "application-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoads", 
            "yangName": "os-table-loads", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryRequestsSent", 
            "yangName": "neighbor-discovery-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryFailures", 
            "yangName": "application-entry-failures", 
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
        "tech_network_ipv6"
    ], 
    "createTime": "2013"
}
"""


