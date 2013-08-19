


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
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # applicationEntryDiscards
    def requestApplicationEntryDiscards (self, requested):
        raise NotImplementedError()

    def isApplicationEntryDiscardsRequested (self):
        raise NotImplementedError()

    def getApplicationEntryDiscards (self):
        raise NotImplementedError()

    def hasApplicationEntryDiscards (self):
        raise NotImplementedError()

    def setApplicationEntryDiscards (self, applicationEntryDiscards):
        raise NotImplementedError()

    # neighborDiscoveryFailures
    def requestNeighborDiscoveryFailures (self, requested):
        raise NotImplementedError()

    def isNeighborDiscoveryFailuresRequested (self):
        raise NotImplementedError()

    def getNeighborDiscoveryFailures (self):
        raise NotImplementedError()

    def hasNeighborDiscoveryFailures (self):
        raise NotImplementedError()

    def setNeighborDiscoveryFailures (self, neighborDiscoveryFailures):
        raise NotImplementedError()

    # neighborDiscoveryTimeouts
    def requestNeighborDiscoveryTimeouts (self, requested):
        raise NotImplementedError()

    def isNeighborDiscoveryTimeoutsRequested (self):
        raise NotImplementedError()

    def getNeighborDiscoveryTimeouts (self):
        raise NotImplementedError()

    def hasNeighborDiscoveryTimeouts (self):
        raise NotImplementedError()

    def setNeighborDiscoveryTimeouts (self, neighborDiscoveryTimeouts):
        raise NotImplementedError()

    # neighborDiscoverySuccesses
    def requestNeighborDiscoverySuccesses (self, requested):
        raise NotImplementedError()

    def isNeighborDiscoverySuccessesRequested (self):
        raise NotImplementedError()

    def getNeighborDiscoverySuccesses (self):
        raise NotImplementedError()

    def hasNeighborDiscoverySuccesses (self):
        raise NotImplementedError()

    def setNeighborDiscoverySuccesses (self, neighborDiscoverySuccesses):
        raise NotImplementedError()

    # polls
    def requestPolls (self, requested):
        raise NotImplementedError()

    def isPollsRequested (self):
        raise NotImplementedError()

    def getPolls (self):
        raise NotImplementedError()

    def hasPolls (self):
        raise NotImplementedError()

    def setPolls (self, polls):
        raise NotImplementedError()

    # applicationRequestFailures
    def requestApplicationRequestFailures (self, requested):
        raise NotImplementedError()

    def isApplicationRequestFailuresRequested (self):
        raise NotImplementedError()

    def getApplicationRequestFailures (self):
        raise NotImplementedError()

    def hasApplicationRequestFailures (self):
        raise NotImplementedError()

    def setApplicationRequestFailures (self, applicationRequestFailures):
        raise NotImplementedError()

    # applicationEntryUpdates
    def requestApplicationEntryUpdates (self, requested):
        raise NotImplementedError()

    def isApplicationEntryUpdatesRequested (self):
        raise NotImplementedError()

    def getApplicationEntryUpdates (self):
        raise NotImplementedError()

    def hasApplicationEntryUpdates (self):
        raise NotImplementedError()

    def setApplicationEntryUpdates (self, applicationEntryUpdates):
        raise NotImplementedError()

    # osTableLoadFailures
    def requestOsTableLoadFailures (self, requested):
        raise NotImplementedError()

    def isOsTableLoadFailuresRequested (self):
        raise NotImplementedError()

    def getOsTableLoadFailures (self):
        raise NotImplementedError()

    def hasOsTableLoadFailures (self):
        raise NotImplementedError()

    def setOsTableLoadFailures (self, osTableLoadFailures):
        raise NotImplementedError()

    # applicationRequestDiscards
    def requestApplicationRequestDiscards (self, requested):
        raise NotImplementedError()

    def isApplicationRequestDiscardsRequested (self):
        raise NotImplementedError()

    def getApplicationRequestDiscards (self):
        raise NotImplementedError()

    def hasApplicationRequestDiscards (self):
        raise NotImplementedError()

    def setApplicationRequestDiscards (self, applicationRequestDiscards):
        raise NotImplementedError()

    # applicationRequestBlocks
    def requestApplicationRequestBlocks (self, requested):
        raise NotImplementedError()

    def isApplicationRequestBlocksRequested (self):
        raise NotImplementedError()

    def getApplicationRequestBlocks (self):
        raise NotImplementedError()

    def hasApplicationRequestBlocks (self):
        raise NotImplementedError()

    def setApplicationRequestBlocks (self, applicationRequestBlocks):
        raise NotImplementedError()

    # applicationRequests
    def requestApplicationRequests (self, requested):
        raise NotImplementedError()

    def isApplicationRequestsRequested (self):
        raise NotImplementedError()

    def getApplicationRequests (self):
        raise NotImplementedError()

    def hasApplicationRequests (self):
        raise NotImplementedError()

    def setApplicationRequests (self, applicationRequests):
        raise NotImplementedError()

    # osTableLoads
    def requestOsTableLoads (self, requested):
        raise NotImplementedError()

    def isOsTableLoadsRequested (self):
        raise NotImplementedError()

    def getOsTableLoads (self):
        raise NotImplementedError()

    def hasOsTableLoads (self):
        raise NotImplementedError()

    def setOsTableLoads (self, osTableLoads):
        raise NotImplementedError()

    # neighborDiscoveryRequestsSent
    def requestNeighborDiscoveryRequestsSent (self, requested):
        raise NotImplementedError()

    def isNeighborDiscoveryRequestsSentRequested (self):
        raise NotImplementedError()

    def getNeighborDiscoveryRequestsSent (self):
        raise NotImplementedError()

    def hasNeighborDiscoveryRequestsSent (self):
        raise NotImplementedError()

    def setNeighborDiscoveryRequestsSent (self, neighborDiscoveryRequestsSent):
        raise NotImplementedError()

    # applicationEntryFailures
    def requestApplicationEntryFailures (self, requested):
        raise NotImplementedError()

    def isApplicationEntryFailuresRequested (self):
        raise NotImplementedError()

    def getApplicationEntryFailures (self):
        raise NotImplementedError()

    def hasApplicationEntryFailures (self):
        raise NotImplementedError()

    def setApplicationEntryFailures (self, applicationEntryFailures):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.counters.counters_maapi_gen import CountersMaapi", 
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
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryDiscards", 
            "yangName": "application-entry-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryFailures", 
            "yangName": "neighbor-discovery-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryTimeouts", 
            "yangName": "neighbor-discovery-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoverySuccesses", 
            "yangName": "neighbor-discovery-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "polls", 
            "yangName": "polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestFailures", 
            "yangName": "application-request-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryUpdates", 
            "yangName": "application-entry-updates", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoadFailures", 
            "yangName": "os-table-load-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestDiscards", 
            "yangName": "application-request-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestBlocks", 
            "yangName": "application-request-blocks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequests", 
            "yangName": "application-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoads", 
            "yangName": "os-table-loads", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryRequestsSent", 
            "yangName": "neighbor-discovery-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
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
            "memberName": "applicationEntryDiscards", 
            "yangName": "application-entry-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryFailures", 
            "yangName": "neighbor-discovery-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryTimeouts", 
            "yangName": "neighbor-discovery-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoverySuccesses", 
            "yangName": "neighbor-discovery-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "polls", 
            "yangName": "polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestFailures", 
            "yangName": "application-request-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryUpdates", 
            "yangName": "application-entry-updates", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoadFailures", 
            "yangName": "os-table-load-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestDiscards", 
            "yangName": "application-request-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestBlocks", 
            "yangName": "application-request-blocks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequests", 
            "yangName": "application-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoads", 
            "yangName": "os-table-loads", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryRequestsSent", 
            "yangName": "neighbor-discovery-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryFailures", 
            "yangName": "application-entry-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


