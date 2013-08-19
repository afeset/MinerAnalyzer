


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class InterfaceMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , interface
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , interface
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # continuousCounters32Bit
    def newContinuousCounters32Bit (self):
        raise NotImplementedError()

    def setContinuousCounters32BitObj (self, obj):
        raise NotImplementedError()

    def getContinuousCounters32BitObj (self):
        raise NotImplementedError()

    def hasContinuousCounters32Bit (self):
        raise NotImplementedError()

    # management
    def newManagement (self):
        raise NotImplementedError()

    def setManagementObj (self, obj):
        raise NotImplementedError()

    def getManagementObj (self):
        raise NotImplementedError()

    def hasManagement (self):
        raise NotImplementedError()

    # content
    def newContent (self):
        raise NotImplementedError()

    def setContentObj (self, obj):
        raise NotImplementedError()

    def getContentObj (self):
        raise NotImplementedError()

    def hasContent (self):
        raise NotImplementedError()

    # ipv4
    def newIpv4 (self):
        raise NotImplementedError()

    def setIpv4Obj (self, obj):
        raise NotImplementedError()

    def getIpv4Obj (self):
        raise NotImplementedError()

    def hasIpv4 (self):
        raise NotImplementedError()

    # ipv6
    def newIpv6 (self):
        raise NotImplementedError()

    def setIpv6Obj (self, obj):
        raise NotImplementedError()

    def getIpv6Obj (self):
        raise NotImplementedError()

    def hasIpv6 (self):
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

    # status
    def newStatus (self):
        raise NotImplementedError()

    def setStatusObj (self, obj):
        raise NotImplementedError()

    def getStatusObj (self):
        raise NotImplementedError()

    def hasStatus (self):
        raise NotImplementedError()

    # connectivityCheck
    def newConnectivityCheck (self):
        raise NotImplementedError()

    def setConnectivityCheckObj (self, obj):
        raise NotImplementedError()

    def getConnectivityCheckObj (self):
        raise NotImplementedError()

    def hasConnectivityCheck (self):
        raise NotImplementedError()

    # link
    def newLink (self):
        raise NotImplementedError()

    def setLinkObj (self, obj):
        raise NotImplementedError()

    def getLinkObj (self):
        raise NotImplementedError()

    def hasLink (self):
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

    # device
    def newDevice (self):
        raise NotImplementedError()

    def setDeviceObj (self, obj):
        raise NotImplementedError()

    def getDeviceObj (self):
        raise NotImplementedError()

    def hasDevice (self):
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

    # ethernet
    def newEthernet (self):
        raise NotImplementedError()

    def setEthernetObj (self, obj):
        raise NotImplementedError()

    def getEthernetObj (self):
        raise NotImplementedError()

    def hasEthernet (self):
        raise NotImplementedError()

    # continuousCounters
    def newContinuousCounters (self):
        raise NotImplementedError()

    def setContinuousCountersObj (self, obj):
        raise NotImplementedError()

    def getContinuousCountersObj (self):
        raise NotImplementedError()

    def hasContinuousCounters (self):
        raise NotImplementedError()




    # config leaves

    # shutdown
    def requestShutdown (self, requested):
        raise NotImplementedError()

    def isShutdownRequested (self):
        raise NotImplementedError()

    def getShutdown (self):
        raise NotImplementedError()

    def hasShutdown (self):
        raise NotImplementedError()

    def setShutdown (self, shutdown):
        raise NotImplementedError()

    # muteReporting
    def requestMuteReporting (self, requested):
        raise NotImplementedError()

    def isMuteReportingRequested (self):
        raise NotImplementedError()

    def getMuteReporting (self):
        raise NotImplementedError()

    def hasMuteReporting (self):
        raise NotImplementedError()

    def setMuteReporting (self, muteReporting):
        raise NotImplementedError()

    # techMode
    def requestTechMode (self, requested):
        raise NotImplementedError()

    def isTechModeRequested (self):
        raise NotImplementedError()

    def getTechMode (self):
        raise NotImplementedError()

    def hasTechMode (self):
        raise NotImplementedError()

    def setTechMode (self, techMode):
        raise NotImplementedError()

    # description
    def requestDescription (self, requested):
        raise NotImplementedError()

    def isDescriptionRequested (self):
        raise NotImplementedError()

    def getDescription (self):
        raise NotImplementedError()

    def hasDescription (self):
        raise NotImplementedError()

    def setDescription (self, description):
        raise NotImplementedError()

    # configurationDelay
    def requestConfigurationDelay (self, requested):
        raise NotImplementedError()

    def isConfigurationDelayRequested (self):
        raise NotImplementedError()

    def getConfigurationDelay (self):
        raise NotImplementedError()

    def hasConfigurationDelay (self):
        raise NotImplementedError()

    def setConfigurationDelay (self, configurationDelay):
        raise NotImplementedError()

    # name
    def requestName (self, requested):
        raise NotImplementedError()

    def isNameRequested (self):
        raise NotImplementedError()

    def getName (self):
        raise NotImplementedError()

    def hasName (self):
        raise NotImplementedError()

    def setName (self, name):
        raise NotImplementedError()

    # sendGratuitousArp
    def requestSendGratuitousArp (self, requested):
        raise NotImplementedError()

    def isSendGratuitousArpRequested (self):
        raise NotImplementedError()

    def getSendGratuitousArp (self):
        raise NotImplementedError()

    def hasSendGratuitousArp (self):
        raise NotImplementedError()

    def setSendGratuitousArp (self, sendGratuitousArp):
        raise NotImplementedError()

    # mibIfIndex
    def requestMibIfIndex (self, requested):
        raise NotImplementedError()

    def isMibIfIndexRequested (self):
        raise NotImplementedError()

    def getMibIfIndex (self):
        raise NotImplementedError()

    def hasMibIfIndex (self):
        raise NotImplementedError()

    def setMibIfIndex (self, mibIfIndex):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "interface", 
        "namespace": "interface", 
        "className": "InterfaceMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.interface_maapi_gen import InterfaceMaapi", 
        "baseClassName": "InterfaceMaapiBase", 
        "baseModule": "interface_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": true, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "continuousCounters32Bit", 
            "yangName": "continuous-counters-32bit", 
            "className": "BlinkyContinuousCounters32BitMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.continuous_counters_32bit.continuous_counters_32bit_maapi_gen import BlinkyContinuousCounters32BitMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "management", 
            "yangName": "management", 
            "className": "BlinkyManagementMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.management.management_maapi_gen import BlinkyManagementMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "content", 
            "yangName": "content", 
            "className": "BlinkyContentMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.content.content_maapi_gen import BlinkyContentMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "ipv4", 
            "yangName": "ipv4", 
            "className": "BlinkyIpv4Maapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.ipv4.ipv4_maapi_gen import BlinkyIpv4Maapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "ipv6", 
            "yangName": "ipv6", 
            "className": "BlinkyIpv6Maapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.ipv6.ipv6_maapi_gen import BlinkyIpv6Maapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "connectivityCheck", 
            "yangName": "connectivity-check", 
            "className": "BlinkyConnectivityCheckMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.connectivity_check_maapi_gen import BlinkyConnectivityCheckMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "link", 
            "yangName": "link", 
            "className": "BlinkyLinkMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.link.link_maapi_gen import BlinkyLinkMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "device", 
            "yangName": "device", 
            "className": "BlinkyDeviceMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.device_maapi_gen import BlinkyDeviceMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "alarms", 
            "yangName": "alarms", 
            "className": "BlinkyAlarmsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.alarms.alarms_maapi_gen import BlinkyAlarmsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "ethernet", 
            "yangName": "ethernet", 
            "className": "BlinkyEthernetMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.ethernet.ethernet_maapi_gen import BlinkyEthernetMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "continuousCounters", 
            "yangName": "continuous-counters", 
            "className": "BlinkyContinuousCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.continuous_counters.continuous_counters_maapi_gen import BlinkyContinuousCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shutdown", 
            "yangName": "shutdown", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "techMode", 
            "yangName": "tech-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "configurationDelay", 
            "yangName": "configuration-delay", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "sendGratuitousArp", 
            "yangName": "send-gratuitous-arp", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "mibIfIndex", 
            "yangName": "mib-if-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shutdown", 
            "yangName": "shutdown", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "techMode", 
            "yangName": "tech-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "configurationDelay", 
            "yangName": "configuration-delay", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "sendGratuitousArp", 
            "yangName": "send-gratuitous-arp", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "mibIfIndex", 
            "yangName": "mib-if-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


