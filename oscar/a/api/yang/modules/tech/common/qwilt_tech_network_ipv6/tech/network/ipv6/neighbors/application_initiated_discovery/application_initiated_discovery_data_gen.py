


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ApplicationInitiatedDiscoveryData(object):

    def __init__ (self):

        self.maxApplicationEntries = 0
        self._myHasMaxApplicationEntries=False
        
        self.maxConcurrentRequests = 0
        self._myHasMaxConcurrentRequests=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.maxPendingRequests = 0
        self._myHasMaxPendingRequests=False
        
        self.maxRequestRate = 0
        self._myHasMaxRequestRate=False
        
        self.requestCount = 0
        self._myHasRequestCount=False
        
        self.requestTimeout = 0
        self._myHasRequestTimeout=False
        
        self.pollInterval = 0
        self._myHasPollInterval=False
        

    def copyFrom (self, other):

        self.maxApplicationEntries=other.maxApplicationEntries
        self._myHasMaxApplicationEntries=other._myHasMaxApplicationEntries
        
        self.maxConcurrentRequests=other.maxConcurrentRequests
        self._myHasMaxConcurrentRequests=other._myHasMaxConcurrentRequests
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.maxPendingRequests=other.maxPendingRequests
        self._myHasMaxPendingRequests=other._myHasMaxPendingRequests
        
        self.maxRequestRate=other.maxRequestRate
        self._myHasMaxRequestRate=other._myHasMaxRequestRate
        
        self.requestCount=other.requestCount
        self._myHasRequestCount=other._myHasRequestCount
        
        self.requestTimeout=other.requestTimeout
        self._myHasRequestTimeout=other._myHasRequestTimeout
        
        self.pollInterval=other.pollInterval
        self._myHasPollInterval=other._myHasPollInterval
        
    # has...() methods

    def hasMaxApplicationEntries (self):
        return self._myHasMaxApplicationEntries

    def hasMaxConcurrentRequests (self):
        return self._myHasMaxConcurrentRequests

    def hasEnabled (self):
        return self._myHasEnabled

    def hasMaxPendingRequests (self):
        return self._myHasMaxPendingRequests

    def hasMaxRequestRate (self):
        return self._myHasMaxRequestRate

    def hasRequestCount (self):
        return self._myHasRequestCount

    def hasRequestTimeout (self):
        return self._myHasRequestTimeout

    def hasPollInterval (self):
        return self._myHasPollInterval


    # setHas...() methods

    def setHasMaxApplicationEntries (self):
        self._myHasMaxApplicationEntries=True

    def setHasMaxConcurrentRequests (self):
        self._myHasMaxConcurrentRequests=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasMaxPendingRequests (self):
        self._myHasMaxPendingRequests=True

    def setHasMaxRequestRate (self):
        self._myHasMaxRequestRate=True

    def setHasRequestCount (self):
        self._myHasRequestCount=True

    def setHasRequestTimeout (self):
        self._myHasRequestTimeout=True

    def setHasPollInterval (self):
        self._myHasPollInterval=True


    def clearAllHas (self):

        self._myHasMaxApplicationEntries=False

        self._myHasMaxConcurrentRequests=False

        self._myHasEnabled=False

        self._myHasMaxPendingRequests=False

        self._myHasMaxRequestRate=False

        self._myHasRequestCount=False

        self._myHasRequestTimeout=False

        self._myHasPollInterval=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasMaxApplicationEntries:
            x = "+"
        leafStr = str(self.maxApplicationEntries)
        items.append(x + "MaxApplicationEntries="+leafStr)

        x=""
        if self._myHasMaxConcurrentRequests:
            x = "+"
        leafStr = str(self.maxConcurrentRequests)
        items.append(x + "MaxConcurrentRequests="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasMaxPendingRequests:
            x = "+"
        leafStr = str(self.maxPendingRequests)
        items.append(x + "MaxPendingRequests="+leafStr)

        x=""
        if self._myHasMaxRequestRate:
            x = "+"
        leafStr = str(self.maxRequestRate)
        items.append(x + "MaxRequestRate="+leafStr)

        x=""
        if self._myHasRequestCount:
            x = "+"
        leafStr = str(self.requestCount)
        items.append(x + "RequestCount="+leafStr)

        x=""
        if self._myHasRequestTimeout:
            x = "+"
        leafStr = str(self.requestTimeout)
        items.append(x + "RequestTimeout="+leafStr)

        x=""
        if self._myHasPollInterval:
            x = "+"
        leafStr = str(self.pollInterval)
        items.append(x + "PollInterval="+leafStr)

        return "{ApplicationInitiatedDiscoveryData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ApplicationInitiatedDiscoveryData", 
        "namespace": "application_initiated_discovery", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.application_initiated_discovery_data_gen import ApplicationInitiatedDiscoveryData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "network", 
            "isCurrent": false
        }, 
        {
            "namespace": "ipv6", 
            "isCurrent": false
        }, 
        {
            "namespace": "neighbors", 
            "isCurrent": false
        }, 
        {
            "namespace": "application_initiated_discovery", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxApplicationEntries", 
            "yangName": "max-application-entries", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxConcurrentRequests", 
            "yangName": "max-concurrent-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxPendingRequests", 
            "yangName": "max-pending-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxRequestRate", 
            "yangName": "max-request-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestCount", 
            "yangName": "request-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestTimeout", 
            "yangName": "request-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "qwilt_tech_network_ipv6"
        ]
    }, 
    "createTime": "2013"
}
"""


