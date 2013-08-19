


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

from application_initiated_discovery_maapi_base_gen import ApplicationInitiatedDiscoveryMaapiBase




class BlinkyApplicationInitiatedDiscoveryMaapi(ApplicationInitiatedDiscoveryMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-applicationInitiatedDiscovery")
        self.domain = None

        

        
        self.maxApplicationEntriesRequested = False
        self.maxApplicationEntries = None
        self.maxApplicationEntriesSet = False
        
        self.requestCountRequested = False
        self.requestCount = None
        self.requestCountSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.maxPendingRequestsRequested = False
        self.maxPendingRequests = None
        self.maxPendingRequestsSet = False
        
        self.maxRequestRateRequested = False
        self.maxRequestRate = None
        self.maxRequestRateSet = False
        
        self.maxConcurrentRequestsRequested = False
        self.maxConcurrentRequests = None
        self.maxConcurrentRequestsSet = False
        
        self.requestTimeoutRequested = False
        self.requestTimeout = None
        self.requestTimeoutSet = False
        
        self.pollIntervalRequested = False
        self.pollInterval = None
        self.pollIntervalSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxApplicationEntries(True)
        
        self.requestRequestCount(True)
        
        self.requestEnabled(True)
        
        self.requestMaxPendingRequests(True)
        
        self.requestMaxRequestRate(True)
        
        self.requestMaxConcurrentRequests(True)
        
        self.requestRequestTimeout(True)
        
        self.requestPollInterval(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxApplicationEntries(True)
        
        self.requestRequestCount(True)
        
        self.requestEnabled(True)
        
        self.requestMaxPendingRequests(True)
        
        self.requestMaxRequestRate(True)
        
        self.requestMaxConcurrentRequests(True)
        
        self.requestRequestTimeout(True)
        
        self.requestPollInterval(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxApplicationEntries(False)
        
        self.requestRequestCount(False)
        
        self.requestEnabled(False)
        
        self.requestMaxPendingRequests(False)
        
        self.requestMaxRequestRate(False)
        
        self.requestMaxConcurrentRequests(False)
        
        self.requestRequestTimeout(False)
        
        self.requestPollInterval(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMaxApplicationEntries(False)
        
        self.requestRequestCount(False)
        
        self.requestEnabled(False)
        
        self.requestMaxPendingRequests(False)
        
        self.requestMaxRequestRate(False)
        
        self.requestMaxConcurrentRequests(False)
        
        self.requestRequestTimeout(False)
        
        self.requestPollInterval(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setMaxApplicationEntries(None)
        self.maxApplicationEntriesSet = False
        
        self.setRequestCount(None)
        self.requestCountSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setMaxPendingRequests(None)
        self.maxPendingRequestsSet = False
        
        self.setMaxRequestRate(None)
        self.maxRequestRateSet = False
        
        self.setMaxConcurrentRequests(None)
        self.maxConcurrentRequestsSet = False
        
        self.setRequestTimeout(None)
        self.requestTimeoutSet = False
        
        self.setPollInterval(None)
        self.pollIntervalSet = False
        
        

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



    def requestMaxApplicationEntries (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxapplicationentries').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxApplicationEntriesRequested = requested
        self.maxApplicationEntriesSet = False

    def isMaxApplicationEntriesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxapplicationentries-requested').debug3Func(): logFunc('called. requested=%s', self.maxApplicationEntriesRequested)
        return self.maxApplicationEntriesRequested

    def getMaxApplicationEntries (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxapplicationentries').debug3Func(): logFunc('called. self.maxApplicationEntriesSet=%s, self.maxApplicationEntries=%s', self.maxApplicationEntriesSet, self.maxApplicationEntries)
        if self.maxApplicationEntriesSet:
            return self.maxApplicationEntries
        return None

    def hasMaxApplicationEntries (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxapplicationentries').debug3Func(): logFunc('called. self.maxApplicationEntriesSet=%s, self.maxApplicationEntries=%s', self.maxApplicationEntriesSet, self.maxApplicationEntries)
        if self.maxApplicationEntriesSet:
            return True
        return False

    def setMaxApplicationEntries (self, maxApplicationEntries):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxapplicationentries').debug3Func(): logFunc('called. maxApplicationEntries=%s, old=%s', maxApplicationEntries, self.maxApplicationEntries)
        self.maxApplicationEntriesSet = True
        self.maxApplicationEntries = maxApplicationEntries

    def requestRequestCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-requestcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.requestCountRequested = requested
        self.requestCountSet = False

    def isRequestCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-requestcount-requested').debug3Func(): logFunc('called. requested=%s', self.requestCountRequested)
        return self.requestCountRequested

    def getRequestCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-requestcount').debug3Func(): logFunc('called. self.requestCountSet=%s, self.requestCount=%s', self.requestCountSet, self.requestCount)
        if self.requestCountSet:
            return self.requestCount
        return None

    def hasRequestCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-requestcount').debug3Func(): logFunc('called. self.requestCountSet=%s, self.requestCount=%s', self.requestCountSet, self.requestCount)
        if self.requestCountSet:
            return True
        return False

    def setRequestCount (self, requestCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-requestcount').debug3Func(): logFunc('called. requestCount=%s, old=%s', requestCount, self.requestCount)
        self.requestCountSet = True
        self.requestCount = requestCount

    def requestEnabled (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-enabled').debug3Func(): logFunc('called. requested=%s', requested)
        self.enabledRequested = requested
        self.enabledSet = False

    def isEnabledRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-enabled-requested').debug3Func(): logFunc('called. requested=%s', self.enabledRequested)
        return self.enabledRequested

    def getEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return self.enabled
        return None

    def hasEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return True
        return False

    def setEnabled (self, enabled):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-enabled').debug3Func(): logFunc('called. enabled=%s, old=%s', enabled, self.enabled)
        self.enabledSet = True
        self.enabled = enabled

    def requestMaxPendingRequests (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxpendingrequests').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxPendingRequestsRequested = requested
        self.maxPendingRequestsSet = False

    def isMaxPendingRequestsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxpendingrequests-requested').debug3Func(): logFunc('called. requested=%s', self.maxPendingRequestsRequested)
        return self.maxPendingRequestsRequested

    def getMaxPendingRequests (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxpendingrequests').debug3Func(): logFunc('called. self.maxPendingRequestsSet=%s, self.maxPendingRequests=%s', self.maxPendingRequestsSet, self.maxPendingRequests)
        if self.maxPendingRequestsSet:
            return self.maxPendingRequests
        return None

    def hasMaxPendingRequests (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxpendingrequests').debug3Func(): logFunc('called. self.maxPendingRequestsSet=%s, self.maxPendingRequests=%s', self.maxPendingRequestsSet, self.maxPendingRequests)
        if self.maxPendingRequestsSet:
            return True
        return False

    def setMaxPendingRequests (self, maxPendingRequests):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxpendingrequests').debug3Func(): logFunc('called. maxPendingRequests=%s, old=%s', maxPendingRequests, self.maxPendingRequests)
        self.maxPendingRequestsSet = True
        self.maxPendingRequests = maxPendingRequests

    def requestMaxRequestRate (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxrequestrate').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxRequestRateRequested = requested
        self.maxRequestRateSet = False

    def isMaxRequestRateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxrequestrate-requested').debug3Func(): logFunc('called. requested=%s', self.maxRequestRateRequested)
        return self.maxRequestRateRequested

    def getMaxRequestRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxrequestrate').debug3Func(): logFunc('called. self.maxRequestRateSet=%s, self.maxRequestRate=%s', self.maxRequestRateSet, self.maxRequestRate)
        if self.maxRequestRateSet:
            return self.maxRequestRate
        return None

    def hasMaxRequestRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxrequestrate').debug3Func(): logFunc('called. self.maxRequestRateSet=%s, self.maxRequestRate=%s', self.maxRequestRateSet, self.maxRequestRate)
        if self.maxRequestRateSet:
            return True
        return False

    def setMaxRequestRate (self, maxRequestRate):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxrequestrate').debug3Func(): logFunc('called. maxRequestRate=%s, old=%s', maxRequestRate, self.maxRequestRate)
        self.maxRequestRateSet = True
        self.maxRequestRate = maxRequestRate

    def requestMaxConcurrentRequests (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxconcurrentrequests').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxConcurrentRequestsRequested = requested
        self.maxConcurrentRequestsSet = False

    def isMaxConcurrentRequestsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxconcurrentrequests-requested').debug3Func(): logFunc('called. requested=%s', self.maxConcurrentRequestsRequested)
        return self.maxConcurrentRequestsRequested

    def getMaxConcurrentRequests (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxconcurrentrequests').debug3Func(): logFunc('called. self.maxConcurrentRequestsSet=%s, self.maxConcurrentRequests=%s', self.maxConcurrentRequestsSet, self.maxConcurrentRequests)
        if self.maxConcurrentRequestsSet:
            return self.maxConcurrentRequests
        return None

    def hasMaxConcurrentRequests (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxconcurrentrequests').debug3Func(): logFunc('called. self.maxConcurrentRequestsSet=%s, self.maxConcurrentRequests=%s', self.maxConcurrentRequestsSet, self.maxConcurrentRequests)
        if self.maxConcurrentRequestsSet:
            return True
        return False

    def setMaxConcurrentRequests (self, maxConcurrentRequests):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxconcurrentrequests').debug3Func(): logFunc('called. maxConcurrentRequests=%s, old=%s', maxConcurrentRequests, self.maxConcurrentRequests)
        self.maxConcurrentRequestsSet = True
        self.maxConcurrentRequests = maxConcurrentRequests

    def requestRequestTimeout (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-requesttimeout').debug3Func(): logFunc('called. requested=%s', requested)
        self.requestTimeoutRequested = requested
        self.requestTimeoutSet = False

    def isRequestTimeoutRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-requesttimeout-requested').debug3Func(): logFunc('called. requested=%s', self.requestTimeoutRequested)
        return self.requestTimeoutRequested

    def getRequestTimeout (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-requesttimeout').debug3Func(): logFunc('called. self.requestTimeoutSet=%s, self.requestTimeout=%s', self.requestTimeoutSet, self.requestTimeout)
        if self.requestTimeoutSet:
            return self.requestTimeout
        return None

    def hasRequestTimeout (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-requesttimeout').debug3Func(): logFunc('called. self.requestTimeoutSet=%s, self.requestTimeout=%s', self.requestTimeoutSet, self.requestTimeout)
        if self.requestTimeoutSet:
            return True
        return False

    def setRequestTimeout (self, requestTimeout):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-requesttimeout').debug3Func(): logFunc('called. requestTimeout=%s, old=%s', requestTimeout, self.requestTimeout)
        self.requestTimeoutSet = True
        self.requestTimeout = requestTimeout

    def requestPollInterval (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pollinterval').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollIntervalRequested = requested
        self.pollIntervalSet = False

    def isPollIntervalRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pollinterval-requested').debug3Func(): logFunc('called. requested=%s', self.pollIntervalRequested)
        return self.pollIntervalRequested

    def getPollInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pollinterval').debug3Func(): logFunc('called. self.pollIntervalSet=%s, self.pollInterval=%s', self.pollIntervalSet, self.pollInterval)
        if self.pollIntervalSet:
            return self.pollInterval
        return None

    def hasPollInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pollinterval').debug3Func(): logFunc('called. self.pollIntervalSet=%s, self.pollInterval=%s', self.pollIntervalSet, self.pollInterval)
        if self.pollIntervalSet:
            return True
        return False

    def setPollInterval (self, pollInterval):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pollinterval').debug3Func(): logFunc('called. pollInterval=%s, old=%s', pollInterval, self.pollInterval)
        self.pollIntervalSet = True
        self.pollInterval = pollInterval


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.maxApplicationEntries = 0
        self.maxApplicationEntriesSet = False
        
        self.requestCount = 0
        self.requestCountSet = False
        
        self.enabled = 0
        self.enabledSet = False
        
        self.maxPendingRequests = 0
        self.maxPendingRequestsSet = False
        
        self.maxRequestRate = 0
        self.maxRequestRateSet = False
        
        self.maxConcurrentRequests = 0
        self.maxConcurrentRequestsSet = False
        
        self.requestTimeout = 0
        self.requestTimeoutSet = False
        
        self.pollInterval = 0
        self.pollIntervalSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("application-initiated-discovery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("neighbors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
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

        
        if self.hasMaxApplicationEntries():
            valMaxApplicationEntries = Value()
            if self.maxApplicationEntries is not None:
                valMaxApplicationEntries.setInt64(self.maxApplicationEntries)
            else:
                valMaxApplicationEntries.setEmpty()
            tagValueList.push(("max-application-entries", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valMaxApplicationEntries)
        
        if self.hasRequestCount():
            valRequestCount = Value()
            if self.requestCount is not None:
                valRequestCount.setInt64(self.requestCount)
            else:
                valRequestCount.setEmpty()
            tagValueList.push(("request-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valRequestCount)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valEnabled)
        
        if self.hasMaxPendingRequests():
            valMaxPendingRequests = Value()
            if self.maxPendingRequests is not None:
                valMaxPendingRequests.setInt64(self.maxPendingRequests)
            else:
                valMaxPendingRequests.setEmpty()
            tagValueList.push(("max-pending-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valMaxPendingRequests)
        
        if self.hasMaxRequestRate():
            valMaxRequestRate = Value()
            if self.maxRequestRate is not None:
                valMaxRequestRate.setInt64(self.maxRequestRate)
            else:
                valMaxRequestRate.setEmpty()
            tagValueList.push(("max-request-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valMaxRequestRate)
        
        if self.hasMaxConcurrentRequests():
            valMaxConcurrentRequests = Value()
            if self.maxConcurrentRequests is not None:
                valMaxConcurrentRequests.setInt64(self.maxConcurrentRequests)
            else:
                valMaxConcurrentRequests.setEmpty()
            tagValueList.push(("max-concurrent-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valMaxConcurrentRequests)
        
        if self.hasRequestTimeout():
            valRequestTimeout = Value()
            if self.requestTimeout is not None:
                valRequestTimeout.setInt64(self.requestTimeout)
            else:
                valRequestTimeout.setEmpty()
            tagValueList.push(("request-timeout", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valRequestTimeout)
        
        if self.hasPollInterval():
            valPollInterval = Value()
            if self.pollInterval is not None:
                valPollInterval.setInt64(self.pollInterval)
            else:
                valPollInterval.setEmpty()
            tagValueList.push(("poll-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valPollInterval)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isMaxApplicationEntriesRequested():
            valMaxApplicationEntries = Value()
            valMaxApplicationEntries.setEmpty()
            tagValueList.push(("max-application-entries", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valMaxApplicationEntries)
        
        if self.isRequestCountRequested():
            valRequestCount = Value()
            valRequestCount.setEmpty()
            tagValueList.push(("request-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valRequestCount)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valEnabled)
        
        if self.isMaxPendingRequestsRequested():
            valMaxPendingRequests = Value()
            valMaxPendingRequests.setEmpty()
            tagValueList.push(("max-pending-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valMaxPendingRequests)
        
        if self.isMaxRequestRateRequested():
            valMaxRequestRate = Value()
            valMaxRequestRate.setEmpty()
            tagValueList.push(("max-request-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valMaxRequestRate)
        
        if self.isMaxConcurrentRequestsRequested():
            valMaxConcurrentRequests = Value()
            valMaxConcurrentRequests.setEmpty()
            tagValueList.push(("max-concurrent-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valMaxConcurrentRequests)
        
        if self.isRequestTimeoutRequested():
            valRequestTimeout = Value()
            valRequestTimeout.setEmpty()
            tagValueList.push(("request-timeout", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valRequestTimeout)
        
        if self.isPollIntervalRequested():
            valPollInterval = Value()
            valPollInterval.setEmpty()
            tagValueList.push(("poll-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valPollInterval)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isMaxApplicationEntriesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-application-entries") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxapplicationentries').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxApplicationEntries", "max-application-entries", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-application-entries-bad-value').infoFunc(): logFunc('maxApplicationEntries not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxApplicationEntries(tempVar)
            for logFunc in self._log('read-tag-values-max-application-entries').debug3Func(): logFunc('read maxApplicationEntries. maxApplicationEntries=%s, tempValue=%s', self.maxApplicationEntries, tempValue.getType())
        
        if self.isRequestCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "request-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-requestcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "requestCount", "request-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-request-count-bad-value').infoFunc(): logFunc('requestCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRequestCount(tempVar)
            for logFunc in self._log('read-tag-values-request-count').debug3Func(): logFunc('read requestCount. requestCount=%s, tempValue=%s', self.requestCount, tempValue.getType())
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-enabled-bad-value').infoFunc(): logFunc('enabled not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEnabled(tempVar)
            for logFunc in self._log('read-tag-values-enabled').debug3Func(): logFunc('read enabled. enabled=%s, tempValue=%s', self.enabled, tempValue.getType())
        
        if self.isMaxPendingRequestsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-pending-requests") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxpendingrequests').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxPendingRequests", "max-pending-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-pending-requests-bad-value').infoFunc(): logFunc('maxPendingRequests not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxPendingRequests(tempVar)
            for logFunc in self._log('read-tag-values-max-pending-requests').debug3Func(): logFunc('read maxPendingRequests. maxPendingRequests=%s, tempValue=%s', self.maxPendingRequests, tempValue.getType())
        
        if self.isMaxRequestRateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-request-rate") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxrequestrate').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxRequestRate", "max-request-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-request-rate-bad-value').infoFunc(): logFunc('maxRequestRate not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxRequestRate(tempVar)
            for logFunc in self._log('read-tag-values-max-request-rate').debug3Func(): logFunc('read maxRequestRate. maxRequestRate=%s, tempValue=%s', self.maxRequestRate, tempValue.getType())
        
        if self.isMaxConcurrentRequestsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-concurrent-requests") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxconcurrentrequests').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxConcurrentRequests", "max-concurrent-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-concurrent-requests-bad-value').infoFunc(): logFunc('maxConcurrentRequests not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxConcurrentRequests(tempVar)
            for logFunc in self._log('read-tag-values-max-concurrent-requests').debug3Func(): logFunc('read maxConcurrentRequests. maxConcurrentRequests=%s, tempValue=%s', self.maxConcurrentRequests, tempValue.getType())
        
        if self.isRequestTimeoutRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "request-timeout") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-requesttimeout').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "requestTimeout", "request-timeout", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-request-timeout-bad-value').infoFunc(): logFunc('requestTimeout not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRequestTimeout(tempVar)
            for logFunc in self._log('read-tag-values-request-timeout').debug3Func(): logFunc('read requestTimeout. requestTimeout=%s, tempValue=%s', self.requestTimeout, tempValue.getType())
        
        if self.isPollIntervalRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-interval") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pollinterval').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollInterval", "poll-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-interval-bad-value').infoFunc(): logFunc('pollInterval not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollInterval(tempVar)
            for logFunc in self._log('read-tag-values-poll-interval').debug3Func(): logFunc('read pollInterval. pollInterval=%s, tempValue=%s', self.pollInterval, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "applicationInitiatedDiscovery", 
        "namespace": "application_initiated_discovery", 
        "className": "ApplicationInitiatedDiscoveryMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.system_defaults.neighbors.application_initiated_discovery.application_initiated_discovery_maapi_gen import ApplicationInitiatedDiscoveryMaapi", 
        "baseClassName": "ApplicationInitiatedDiscoveryMaapiBase", 
        "baseModule": "application_initiated_discovery_maapi_base_gen"
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
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "system-defaults"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "application-initiated-discovery"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxApplicationEntries", 
            "yangName": "max-application-entries", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestCount", 
            "yangName": "request-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxPendingRequests", 
            "yangName": "max-pending-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxRequestRate", 
            "yangName": "max-request-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxConcurrentRequests", 
            "yangName": "max-concurrent-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestTimeout", 
            "yangName": "request-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
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
            "memberName": "maxApplicationEntries", 
            "yangName": "max-application-entries", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestCount", 
            "yangName": "request-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxPendingRequests", 
            "yangName": "max-pending-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxRequestRate", 
            "yangName": "max-request-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxConcurrentRequests", 
            "yangName": "max-concurrent-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestTimeout", 
            "yangName": "request-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


