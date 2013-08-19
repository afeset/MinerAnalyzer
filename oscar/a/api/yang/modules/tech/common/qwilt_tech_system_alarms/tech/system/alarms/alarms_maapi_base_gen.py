


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class AlarmsMaapiBase(object):
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

    # thresholds
    def newThresholds (self):
        raise NotImplementedError()

    def setThresholdsObj (self, obj):
        raise NotImplementedError()

    def getThresholdsObj (self):
        raise NotImplementedError()

    def hasThresholds (self):
        raise NotImplementedError()

    # listList
    def newListList (self):
        raise NotImplementedError()

    def setListListObj (self, obj):
        raise NotImplementedError()

    def getListListObj (self):
        raise NotImplementedError()

    def hasListList (self):
        raise NotImplementedError()

    # summary
    def newSummary (self):
        raise NotImplementedError()

    def setSummaryObj (self, obj):
        raise NotImplementedError()

    def getSummaryObj (self):
        raise NotImplementedError()

    def hasSummary (self):
        raise NotImplementedError()

    # systemDefaults
    def newSystemDefaults (self):
        raise NotImplementedError()

    def setSystemDefaultsObj (self, obj):
        raise NotImplementedError()

    def getSystemDefaultsObj (self):
        raise NotImplementedError()

    def hasSystemDefaults (self):
        raise NotImplementedError()

    # simulateList
    def newSimulateList (self):
        raise NotImplementedError()

    def setSimulateListObj (self, obj):
        raise NotImplementedError()

    def getSimulateListObj (self):
        raise NotImplementedError()

    def hasSimulateList (self):
        raise NotImplementedError()

    # alarms
    def newAlarms (self):
        raise NotImplementedError()

    def setAlarmsObj (self, obj):
        raise NotImplementedError()

    def getAlarmsObj (self):
        raise NotImplementedError()

    def hasAlarms (self):
        raise NotImplementedError()

    # registeredList
    def newRegisteredList (self):
        raise NotImplementedError()

    def setRegisteredListObj (self, obj):
        raise NotImplementedError()

    def getRegisteredListObj (self):
        raise NotImplementedError()

    def hasRegisteredList (self):
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

    # raiseTestAlarm
    def requestRaiseTestAlarm (self, requested):
        raise NotImplementedError()

    def isRaiseTestAlarmRequested (self):
        raise NotImplementedError()

    def getRaiseTestAlarm (self):
        raise NotImplementedError()

    def hasRaiseTestAlarm (self):
        raise NotImplementedError()

    def setRaiseTestAlarm (self, raiseTestAlarm):
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
        "name": "alarms", 
        "namespace": "alarms", 
        "className": "AlarmsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.alarms_maapi_gen import AlarmsMaapi", 
        "baseClassName": "AlarmsMaapiBase", 
        "baseModule": "alarms_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "alarms"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "memberName": "thresholds", 
            "yangName": "thresholds", 
            "className": "BlinkyThresholdsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.thresholds.thresholds_maapi_gen import BlinkyThresholdsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "memberName": "listList", 
            "yangName": "list", 
            "className": "BlinkyListMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.list.list_maapi_list_gen import BlinkyListMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "memberName": "summary", 
            "yangName": "summary", 
            "className": "BlinkySummaryMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.summary.summary_maapi_gen import BlinkySummaryMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "memberName": "simulateList", 
            "yangName": "simulate", 
            "className": "BlinkySimulateMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.simulate.simulate_maapi_list_gen import BlinkySimulateMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "memberName": "alarms", 
            "yangName": "alarms", 
            "className": "BlinkyAlarmsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.alarms.alarms_maapi_gen import BlinkyAlarmsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "memberName": "registeredList", 
            "yangName": "registered", 
            "className": "BlinkyRegisteredMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.registered.registered_maapi_list_gen import BlinkyRegisteredMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "raiseTestAlarm", 
            "yangName": "raise-test-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
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
            "qwilt_tech_system_alarms"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "raiseTestAlarm", 
            "yangName": "raise-test-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
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


