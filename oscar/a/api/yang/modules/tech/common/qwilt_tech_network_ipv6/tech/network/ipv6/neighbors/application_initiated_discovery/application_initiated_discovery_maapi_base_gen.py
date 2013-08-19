


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ApplicationInitiatedDiscoveryMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # status
    def newStatus (self):
        raise NotImplementedError()

    def setStatusObj (self, obj):
        raise NotImplementedError()

    def getStatusObj (self):
        raise NotImplementedError()

    def hasStatus (self):
        raise NotImplementedError()

    # counters
    def newCounters (self):
        raise NotImplementedError()

    def setCountersObj (self, obj):
        raise NotImplementedError()

    def getCountersObj (self):
        raise NotImplementedError()

    def hasCounters (self):
        raise NotImplementedError()




    # config leaves

    # maxApplicationEntries
    def requestMaxApplicationEntries (self, requested):
        raise NotImplementedError()

    def isMaxApplicationEntriesRequested (self):
        raise NotImplementedError()

    def getMaxApplicationEntries (self):
        raise NotImplementedError()

    def hasMaxApplicationEntries (self):
        raise NotImplementedError()

    def setMaxApplicationEntries (self, maxApplicationEntries):
        raise NotImplementedError()

    # maxConcurrentRequests
    def requestMaxConcurrentRequests (self, requested):
        raise NotImplementedError()

    def isMaxConcurrentRequestsRequested (self):
        raise NotImplementedError()

    def getMaxConcurrentRequests (self):
        raise NotImplementedError()

    def hasMaxConcurrentRequests (self):
        raise NotImplementedError()

    def setMaxConcurrentRequests (self, maxConcurrentRequests):
        raise NotImplementedError()

    # enabled
    def requestEnabled (self, requested):
        raise NotImplementedError()

    def isEnabledRequested (self):
        raise NotImplementedError()

    def getEnabled (self):
        raise NotImplementedError()

    def hasEnabled (self):
        raise NotImplementedError()

    def setEnabled (self, enabled):
        raise NotImplementedError()

    # maxPendingRequests
    def requestMaxPendingRequests (self, requested):
        raise NotImplementedError()

    def isMaxPendingRequestsRequested (self):
        raise NotImplementedError()

    def getMaxPendingRequests (self):
        raise NotImplementedError()

    def hasMaxPendingRequests (self):
        raise NotImplementedError()

    def setMaxPendingRequests (self, maxPendingRequests):
        raise NotImplementedError()

    # maxRequestRate
    def requestMaxRequestRate (self, requested):
        raise NotImplementedError()

    def isMaxRequestRateRequested (self):
        raise NotImplementedError()

    def getMaxRequestRate (self):
        raise NotImplementedError()

    def hasMaxRequestRate (self):
        raise NotImplementedError()

    def setMaxRequestRate (self, maxRequestRate):
        raise NotImplementedError()

    # requestCount
    def requestRequestCount (self, requested):
        raise NotImplementedError()

    def isRequestCountRequested (self):
        raise NotImplementedError()

    def getRequestCount (self):
        raise NotImplementedError()

    def hasRequestCount (self):
        raise NotImplementedError()

    def setRequestCount (self, requestCount):
        raise NotImplementedError()

    # requestTimeout
    def requestRequestTimeout (self, requested):
        raise NotImplementedError()

    def isRequestTimeoutRequested (self):
        raise NotImplementedError()

    def getRequestTimeout (self):
        raise NotImplementedError()

    def hasRequestTimeout (self):
        raise NotImplementedError()

    def setRequestTimeout (self, requestTimeout):
        raise NotImplementedError()

    # pollInterval
    def requestPollInterval (self, requested):
        raise NotImplementedError()

    def isPollIntervalRequested (self):
        raise NotImplementedError()

    def getPollInterval (self):
        raise NotImplementedError()

    def hasPollInterval (self):
        raise NotImplementedError()

    def setPollInterval (self, pollInterval):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "applicationInitiatedDiscovery", 
        "namespace": "application_initiated_discovery", 
        "className": "ApplicationInitiatedDiscoveryMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.application_initiated_discovery_maapi_gen import ApplicationInitiatedDiscoveryMaapi", 
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
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"
        }
    ], 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxConcurrentRequests", 
            "yangName": "max-concurrent-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxPendingRequests", 
            "yangName": "max-pending-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxRequestRate", 
            "yangName": "max-request-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestCount", 
            "yangName": "request-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestTimeout", 
            "yangName": "request-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxConcurrentRequests", 
            "yangName": "max-concurrent-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxPendingRequests", 
            "yangName": "max-pending-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxRequestRate", 
            "yangName": "max-request-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestCount", 
            "yangName": "request-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "requestTimeout", 
            "yangName": "request-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


