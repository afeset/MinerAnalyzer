


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ThresholdsMaapiBase(object):
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





    # config leaves

    # singlePollDurationWarningMsec
    def requestSinglePollDurationWarningMsec (self, requested):
        raise NotImplementedError()

    def isSinglePollDurationWarningMsecRequested (self):
        raise NotImplementedError()

    def getSinglePollDurationWarningMsec (self):
        raise NotImplementedError()

    def hasSinglePollDurationWarningMsec (self):
        raise NotImplementedError()

    def setSinglePollDurationWarningMsec (self, singlePollDurationWarningMsec):
        raise NotImplementedError()

    # pollLatencyErrorSeconds
    def requestPollLatencyErrorSeconds (self, requested):
        raise NotImplementedError()

    def isPollLatencyErrorSecondsRequested (self):
        raise NotImplementedError()

    def getPollLatencyErrorSeconds (self):
        raise NotImplementedError()

    def hasPollLatencyErrorSeconds (self):
        raise NotImplementedError()

    def setPollLatencyErrorSeconds (self, pollLatencyErrorSeconds):
        raise NotImplementedError()

    # singlePollDurationErrorMsec
    def requestSinglePollDurationErrorMsec (self, requested):
        raise NotImplementedError()

    def isSinglePollDurationErrorMsecRequested (self):
        raise NotImplementedError()

    def getSinglePollDurationErrorMsec (self):
        raise NotImplementedError()

    def hasSinglePollDurationErrorMsec (self):
        raise NotImplementedError()

    def setSinglePollDurationErrorMsec (self, singlePollDurationErrorMsec):
        raise NotImplementedError()

    # overallPollDurationErrorMsec
    def requestOverallPollDurationErrorMsec (self, requested):
        raise NotImplementedError()

    def isOverallPollDurationErrorMsecRequested (self):
        raise NotImplementedError()

    def getOverallPollDurationErrorMsec (self):
        raise NotImplementedError()

    def hasOverallPollDurationErrorMsec (self):
        raise NotImplementedError()

    def setOverallPollDurationErrorMsec (self, overallPollDurationErrorMsec):
        raise NotImplementedError()

    # pollLatencyWarningSeconds
    def requestPollLatencyWarningSeconds (self, requested):
        raise NotImplementedError()

    def isPollLatencyWarningSecondsRequested (self):
        raise NotImplementedError()

    def getPollLatencyWarningSeconds (self):
        raise NotImplementedError()

    def hasPollLatencyWarningSeconds (self):
        raise NotImplementedError()

    def setPollLatencyWarningSeconds (self, pollLatencyWarningSeconds):
        raise NotImplementedError()

    # overallPollDurationWarningMsec
    def requestOverallPollDurationWarningMsec (self, requested):
        raise NotImplementedError()

    def isOverallPollDurationWarningMsecRequested (self):
        raise NotImplementedError()

    def getOverallPollDurationWarningMsec (self):
        raise NotImplementedError()

    def hasOverallPollDurationWarningMsec (self):
        raise NotImplementedError()

    def setOverallPollDurationWarningMsec (self, overallPollDurationWarningMsec):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "thresholds", 
        "namespace": "thresholds", 
        "className": "ThresholdsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.system_defaults.thresholds.thresholds_maapi_gen import ThresholdsMaapi", 
        "baseClassName": "ThresholdsMaapiBase", 
        "baseModule": "thresholds_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "system", 
            "namespace": "system", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "thresholds", 
            "namespace": "thresholds", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "thresholds"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationWarningMsec", 
            "yangName": "single-poll-duration-warning-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyErrorSeconds", 
            "yangName": "poll-latency-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationErrorMsec", 
            "yangName": "single-poll-duration-error-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationErrorMsec", 
            "yangName": "overall-poll-duration-error-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarningSeconds", 
            "yangName": "poll-latency-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationWarningMsec", 
            "yangName": "overall-poll-duration-warning-msec", 
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
            "qwilt_tech_system_alarms"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationWarningMsec", 
            "yangName": "single-poll-duration-warning-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyErrorSeconds", 
            "yangName": "poll-latency-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationErrorMsec", 
            "yangName": "single-poll-duration-error-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationErrorMsec", 
            "yangName": "overall-poll-duration-error-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarningSeconds", 
            "yangName": "poll-latency-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationWarningMsec", 
            "yangName": "overall-poll-duration-warning-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


