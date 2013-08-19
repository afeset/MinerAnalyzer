


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

    # activeSeconds
    def requestActiveSeconds (self, requested):
        raise NotImplementedError()

    def isActiveSecondsRequested (self):
        raise NotImplementedError()

    def getActiveSeconds (self):
        raise NotImplementedError()

    def hasActiveSeconds (self):
        raise NotImplementedError()

    def setActiveSeconds (self, activeSeconds):
        raise NotImplementedError()

    # totalSeconds
    def requestTotalSeconds (self, requested):
        raise NotImplementedError()

    def isTotalSecondsRequested (self):
        raise NotImplementedError()

    def getTotalSeconds (self):
        raise NotImplementedError()

    def hasTotalSeconds (self):
        raise NotImplementedError()

    def setTotalSeconds (self, totalSeconds):
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

    # pollsMissed
    def requestPollsMissed (self, requested):
        raise NotImplementedError()

    def isPollsMissedRequested (self):
        raise NotImplementedError()

    def getPollsMissed (self):
        raise NotImplementedError()

    def hasPollsMissed (self):
        raise NotImplementedError()

    def setPollsMissed (self, pollsMissed):
        raise NotImplementedError()

    # pollLatencyWarnings
    def requestPollLatencyWarnings (self, requested):
        raise NotImplementedError()

    def isPollLatencyWarningsRequested (self):
        raise NotImplementedError()

    def getPollLatencyWarnings (self):
        raise NotImplementedError()

    def hasPollLatencyWarnings (self):
        raise NotImplementedError()

    def setPollLatencyWarnings (self, pollLatencyWarnings):
        raise NotImplementedError()

    # pollLatencyErrors
    def requestPollLatencyErrors (self, requested):
        raise NotImplementedError()

    def isPollLatencyErrorsRequested (self):
        raise NotImplementedError()

    def getPollLatencyErrors (self):
        raise NotImplementedError()

    def hasPollLatencyErrors (self):
        raise NotImplementedError()

    def setPollLatencyErrors (self, pollLatencyErrors):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.counters.counters_maapi_gen import CountersMaapi", 
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
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log", 
            "namespace": "log", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "housekeeper", 
            "namespace": "housekeeper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "housekeeper"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activeSeconds", 
            "yangName": "active-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "totalSeconds", 
            "yangName": "total-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "polls", 
            "yangName": "polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollsMissed", 
            "yangName": "polls-missed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarnings", 
            "yangName": "poll-latency-warnings", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyErrors", 
            "yangName": "poll-latency-errors", 
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
            "debug", 
            "qwilt_tech_log"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activeSeconds", 
            "yangName": "active-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "totalSeconds", 
            "yangName": "total-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "polls", 
            "yangName": "polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollsMissed", 
            "yangName": "polls-missed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarnings", 
            "yangName": "poll-latency-warnings", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyErrors", 
            "yangName": "poll-latency-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


