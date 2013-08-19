


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

from status_maapi_base_gen import StatusMaapiBase




class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.applicationEntryCountRequested = False
        self.applicationEntryCount = None
        self.applicationEntryCountSet = False
        
        self.concurrentRequestsRequested = False
        self.concurrentRequests = None
        self.concurrentRequestsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestApplicationEntryCount(True)
        
        self.requestConcurrentRequests(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestApplicationEntryCount(False)
        
        self.requestConcurrentRequests(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestApplicationEntryCount(True)
        
        self.requestConcurrentRequests(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestApplicationEntryCount(False)
        
        self.requestConcurrentRequests(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(trxContext)

    def read (self
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  True,
                                  trxContext)



    def requestApplicationEntryCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-applicationentrycount').debug3Func(): logFunc('called. requested=%s', requested)
        self.applicationEntryCountRequested = requested
        self.applicationEntryCountSet = False

    def isApplicationEntryCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-applicationentrycount-requested').debug3Func(): logFunc('called. requested=%s', self.applicationEntryCountRequested)
        return self.applicationEntryCountRequested

    def getApplicationEntryCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-applicationentrycount').debug3Func(): logFunc('called. self.applicationEntryCountSet=%s, self.applicationEntryCount=%s', self.applicationEntryCountSet, self.applicationEntryCount)
        if self.applicationEntryCountSet:
            return self.applicationEntryCount
        return None

    def hasApplicationEntryCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-applicationentrycount').debug3Func(): logFunc('called. self.applicationEntryCountSet=%s, self.applicationEntryCount=%s', self.applicationEntryCountSet, self.applicationEntryCount)
        if self.applicationEntryCountSet:
            return True
        return False

    def setApplicationEntryCount (self, applicationEntryCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-applicationentrycount').debug3Func(): logFunc('called. applicationEntryCount=%s, old=%s', applicationEntryCount, self.applicationEntryCount)
        self.applicationEntryCountSet = True
        self.applicationEntryCount = applicationEntryCount

    def requestConcurrentRequests (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-concurrentrequests').debug3Func(): logFunc('called. requested=%s', requested)
        self.concurrentRequestsRequested = requested
        self.concurrentRequestsSet = False

    def isConcurrentRequestsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-concurrentrequests-requested').debug3Func(): logFunc('called. requested=%s', self.concurrentRequestsRequested)
        return self.concurrentRequestsRequested

    def getConcurrentRequests (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-concurrentrequests').debug3Func(): logFunc('called. self.concurrentRequestsSet=%s, self.concurrentRequests=%s', self.concurrentRequestsSet, self.concurrentRequests)
        if self.concurrentRequestsSet:
            return self.concurrentRequests
        return None

    def hasConcurrentRequests (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-concurrentrequests').debug3Func(): logFunc('called. self.concurrentRequestsSet=%s, self.concurrentRequests=%s', self.concurrentRequestsSet, self.concurrentRequests)
        if self.concurrentRequestsSet:
            return True
        return False

    def setConcurrentRequests (self, concurrentRequests):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-concurrentrequests').debug3Func(): logFunc('called. concurrentRequests=%s, old=%s', concurrentRequests, self.concurrentRequests)
        self.concurrentRequestsSet = True
        self.concurrentRequests = concurrentRequests


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.applicationEntryCount = 0
        self.applicationEntryCountSet = False
        
        self.concurrentRequests = 0
        self.concurrentRequestsSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("application-initiated-discovery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("neighbors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ipv6", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("network", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network", "qt-net"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       
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

        keyPath = self._getSelfKeyPath(
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

        
        if self.isApplicationEntryCountRequested():
            valApplicationEntryCount = Value()
            valApplicationEntryCount.setEmpty()
            tagValueList.push(("application-entry-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valApplicationEntryCount)
        
        if self.isConcurrentRequestsRequested():
            valConcurrentRequests = Value()
            valConcurrentRequests.setEmpty()
            tagValueList.push(("concurrent-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valConcurrentRequests)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isApplicationEntryCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "application-entry-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-applicationentrycount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "applicationEntryCount", "application-entry-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-application-entry-count-bad-value').infoFunc(): logFunc('applicationEntryCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setApplicationEntryCount(tempVar)
            for logFunc in self._log('read-tag-values-application-entry-count').debug3Func(): logFunc('read applicationEntryCount. applicationEntryCount=%s, tempValue=%s', self.applicationEntryCount, tempValue.getType())
        
        if self.isConcurrentRequestsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "concurrent-requests") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-concurrentrequests').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "concurrentRequests", "concurrent-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-concurrent-requests-bad-value').infoFunc(): logFunc('concurrentRequests not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setConcurrentRequests(tempVar)
            for logFunc in self._log('read-tag-values-concurrent-requests').debug3Func(): logFunc('read concurrentRequests. concurrentRequests=%s, tempValue=%s', self.concurrentRequests, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-net", 
            "yangName": "network", 
            "namespace": "network", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network", 
            "name": "network"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "ipv6", 
            "namespace": "ipv6", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "ipv6"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "neighbors", 
            "namespace": "neighbors", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "neighbors"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "application-initiated-discovery", 
            "namespace": "application_initiated_discovery", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "application-initiated-discovery"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryCount", 
            "yangName": "application-entry-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "concurrentRequests", 
            "yangName": "concurrent-requests", 
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
            "qwilt_tech_network_ipv6"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryCount", 
            "yangName": "application-entry-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "concurrentRequests", 
            "yangName": "concurrent-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


