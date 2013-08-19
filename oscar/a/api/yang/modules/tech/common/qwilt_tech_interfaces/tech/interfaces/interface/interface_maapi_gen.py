


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

from interface_maapi_base_gen import InterfaceMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.continuous_counters_32bit.continuous_counters_32bit_maapi_gen import BlinkyContinuousCounters32BitMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.management.management_maapi_gen import BlinkyManagementMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.content.content_maapi_gen import BlinkyContentMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.ipv4.ipv4_maapi_gen import BlinkyIpv4Maapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.ipv6.ipv6_maapi_gen import BlinkyIpv6Maapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.counters.counters_maapi_gen import BlinkyCountersMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.status.status_maapi_gen import BlinkyStatusMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.connectivity_check_maapi_gen import BlinkyConnectivityCheckMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.link.link_maapi_gen import BlinkyLinkMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.device_maapi_gen import BlinkyDeviceMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.alarms.alarms_maapi_gen import BlinkyAlarmsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.ethernet.ethernet_maapi_gen import BlinkyEthernetMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.continuous_counters.continuous_counters_maapi_gen import BlinkyContinuousCountersMaapi



class BlinkyInterfaceMaapi(InterfaceMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-interface")
        self.domain = None

        
        self.continuousCounters32BitObj = None
        
        self.managementObj = None
        
        self.contentObj = None
        
        self.ipv4Obj = None
        
        self.ipv6Obj = None
        
        self.countersObj = None
        
        self.statusObj = None
        
        self.connectivityCheckObj = None
        
        self.linkObj = None
        
        self.systemDefaultsObj = None
        
        self.deviceObj = None
        
        self.alarmsObj = None
        
        self.ethernetObj = None
        
        self.continuousCountersObj = None
        

        
        self.shutdownRequested = False
        self.shutdown = None
        self.shutdownSet = False
        
        self.muteReportingRequested = False
        self.muteReporting = None
        self.muteReportingSet = False
        
        self.techModeRequested = False
        self.techMode = None
        self.techModeSet = False
        
        self.descriptionRequested = False
        self.description = None
        self.descriptionSet = False
        
        self.configurationDelayRequested = False
        self.configurationDelay = None
        self.configurationDelaySet = False
        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        
        self.sendGratuitousArpRequested = False
        self.sendGratuitousArp = None
        self.sendGratuitousArpSet = False
        
        self.mibIfIndexRequested = False
        self.mibIfIndex = None
        self.mibIfIndexSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestShutdown(True)
        
        self.requestMuteReporting(True)
        
        self.requestTechMode(True)
        
        self.requestDescription(True)
        
        self.requestConfigurationDelay(True)
        
        self.requestName(True)
        
        self.requestSendGratuitousArp(True)
        
        self.requestMibIfIndex(True)
        
        
        
        if not self.continuousCounters32BitObj:
            self.continuousCounters32BitObj = self.newContinuousCounters32Bit()
            self.continuousCounters32BitObj.requestConfigAndOper()
        
        if not self.managementObj:
            self.managementObj = self.newManagement()
            self.managementObj.requestConfigAndOper()
        
        if not self.contentObj:
            self.contentObj = self.newContent()
            self.contentObj.requestConfigAndOper()
        
        if not self.ipv4Obj:
            self.ipv4Obj = self.newIpv4()
            self.ipv4Obj.requestConfigAndOper()
        
        if not self.ipv6Obj:
            self.ipv6Obj = self.newIpv6()
            self.ipv6Obj.requestConfigAndOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfigAndOper()
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        
        if not self.connectivityCheckObj:
            self.connectivityCheckObj = self.newConnectivityCheck()
            self.connectivityCheckObj.requestConfigAndOper()
        
        if not self.linkObj:
            self.linkObj = self.newLink()
            self.linkObj.requestConfigAndOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.requestConfigAndOper()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.requestConfigAndOper()
        
        if not self.ethernetObj:
            self.ethernetObj = self.newEthernet()
            self.ethernetObj.requestConfigAndOper()
        
        if not self.continuousCountersObj:
            self.continuousCountersObj = self.newContinuousCounters()
            self.continuousCountersObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestShutdown(True)
        
        self.requestMuteReporting(True)
        
        self.requestTechMode(True)
        
        self.requestDescription(True)
        
        self.requestConfigurationDelay(True)
        
        self.requestName(True)
        
        self.requestSendGratuitousArp(True)
        
        self.requestMibIfIndex(True)
        
        
        
        if not self.continuousCounters32BitObj:
            self.continuousCounters32BitObj = self.newContinuousCounters32Bit()
            self.continuousCounters32BitObj.requestConfig()
        
        if not self.managementObj:
            self.managementObj = self.newManagement()
            self.managementObj.requestConfig()
        
        if not self.contentObj:
            self.contentObj = self.newContent()
            self.contentObj.requestConfig()
        
        if not self.ipv4Obj:
            self.ipv4Obj = self.newIpv4()
            self.ipv4Obj.requestConfig()
        
        if not self.ipv6Obj:
            self.ipv6Obj = self.newIpv6()
            self.ipv6Obj.requestConfig()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfig()
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        
        if not self.connectivityCheckObj:
            self.connectivityCheckObj = self.newConnectivityCheck()
            self.connectivityCheckObj.requestConfig()
        
        if not self.linkObj:
            self.linkObj = self.newLink()
            self.linkObj.requestConfig()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.requestConfig()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.requestConfig()
        
        if not self.ethernetObj:
            self.ethernetObj = self.newEthernet()
            self.ethernetObj.requestConfig()
        
        if not self.continuousCountersObj:
            self.continuousCountersObj = self.newContinuousCounters()
            self.continuousCountersObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestShutdown(False)
        
        self.requestMuteReporting(False)
        
        self.requestTechMode(False)
        
        self.requestDescription(False)
        
        self.requestConfigurationDelay(False)
        
        self.requestName(False)
        
        self.requestSendGratuitousArp(False)
        
        self.requestMibIfIndex(False)
        
        
        
        if not self.continuousCounters32BitObj:
            self.continuousCounters32BitObj = self.newContinuousCounters32Bit()
            self.continuousCounters32BitObj.requestOper()
        
        if not self.managementObj:
            self.managementObj = self.newManagement()
            self.managementObj.requestOper()
        
        if not self.contentObj:
            self.contentObj = self.newContent()
            self.contentObj.requestOper()
        
        if not self.ipv4Obj:
            self.ipv4Obj = self.newIpv4()
            self.ipv4Obj.requestOper()
        
        if not self.ipv6Obj:
            self.ipv6Obj = self.newIpv6()
            self.ipv6Obj.requestOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestOper()
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        
        if not self.connectivityCheckObj:
            self.connectivityCheckObj = self.newConnectivityCheck()
            self.connectivityCheckObj.requestOper()
        
        if not self.linkObj:
            self.linkObj = self.newLink()
            self.linkObj.requestOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.requestOper()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.requestOper()
        
        if not self.ethernetObj:
            self.ethernetObj = self.newEthernet()
            self.ethernetObj.requestOper()
        
        if not self.continuousCountersObj:
            self.continuousCountersObj = self.newContinuousCounters()
            self.continuousCountersObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestShutdown(False)
        
        self.requestMuteReporting(False)
        
        self.requestTechMode(False)
        
        self.requestDescription(False)
        
        self.requestConfigurationDelay(False)
        
        self.requestName(False)
        
        self.requestSendGratuitousArp(False)
        
        self.requestMibIfIndex(False)
        
        
        
        if not self.continuousCounters32BitObj:
            self.continuousCounters32BitObj = self.newContinuousCounters32Bit()
            self.continuousCounters32BitObj.clearAllRequested()
        
        if not self.managementObj:
            self.managementObj = self.newManagement()
            self.managementObj.clearAllRequested()
        
        if not self.contentObj:
            self.contentObj = self.newContent()
            self.contentObj.clearAllRequested()
        
        if not self.ipv4Obj:
            self.ipv4Obj = self.newIpv4()
            self.ipv4Obj.clearAllRequested()
        
        if not self.ipv6Obj:
            self.ipv6Obj = self.newIpv6()
            self.ipv6Obj.clearAllRequested()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.clearAllRequested()
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        
        if not self.connectivityCheckObj:
            self.connectivityCheckObj = self.newConnectivityCheck()
            self.connectivityCheckObj.clearAllRequested()
        
        if not self.linkObj:
            self.linkObj = self.newLink()
            self.linkObj.clearAllRequested()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.clearAllRequested()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.clearAllRequested()
        
        if not self.ethernetObj:
            self.ethernetObj = self.newEthernet()
            self.ethernetObj.clearAllRequested()
        
        if not self.continuousCountersObj:
            self.continuousCountersObj = self.newContinuousCounters()
            self.continuousCountersObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setShutdown(None)
        self.shutdownSet = False
        
        self.setMuteReporting(None)
        self.muteReportingSet = False
        
        self.setTechMode(None)
        self.techModeSet = False
        
        self.setDescription(None)
        self.descriptionSet = False
        
        self.setConfigurationDelay(None)
        self.configurationDelaySet = False
        
        self.setName(None)
        self.nameSet = False
        
        self.setSendGratuitousArp(None)
        self.sendGratuitousArpSet = False
        
        self.setMibIfIndex(None)
        self.mibIfIndexSet = False
        
        
        if self.continuousCounters32BitObj:
            self.continuousCounters32BitObj.clearAllSet()
        
        if self.managementObj:
            self.managementObj.clearAllSet()
        
        if self.contentObj:
            self.contentObj.clearAllSet()
        
        if self.ipv4Obj:
            self.ipv4Obj.clearAllSet()
        
        if self.ipv6Obj:
            self.ipv6Obj.clearAllSet()
        
        if self.countersObj:
            self.countersObj.clearAllSet()
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        
        if self.connectivityCheckObj:
            self.connectivityCheckObj.clearAllSet()
        
        if self.linkObj:
            self.linkObj.clearAllSet()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        
        if self.deviceObj:
            self.deviceObj.clearAllSet()
        
        if self.alarmsObj:
            self.alarmsObj.clearAllSet()
        
        if self.ethernetObj:
            self.ethernetObj.clearAllSet()
        
        if self.continuousCountersObj:
            self.continuousCountersObj.clearAllSet()
        

    def write (self
              , interface
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(interface, trxContext)

    def read (self
              , interface
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  True,
                                  trxContext)

    def newContinuousCounters32Bit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-continuouscounters32bit').debug3Func(): logFunc('called.')
        continuousCounters32Bit = BlinkyContinuousCounters32BitMaapi(self._log)
        continuousCounters32Bit.init(self.domain)
        return continuousCounters32Bit

    def setContinuousCounters32BitObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-continuouscounters32bit').debug3Func(): logFunc('called. obj=%s', obj)
        self.continuousCounters32BitObj = obj

    def getContinuousCounters32BitObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-continuouscounters32bit').debug3Func(): logFunc('called. self.continuousCounters32BitObj=%s', self.continuousCounters32BitObj)
        return self.continuousCounters32BitObj

    def hasContinuousCounters32Bit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-continuouscounters32bit').debug3Func(): logFunc('called. self.continuousCounters32BitObj=%s', self.continuousCounters32BitObj)
        if self.continuousCounters32BitObj:
            return True
        return False

    def newManagement (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-management').debug3Func(): logFunc('called.')
        management = BlinkyManagementMaapi(self._log)
        management.init(self.domain)
        return management

    def setManagementObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-management').debug3Func(): logFunc('called. obj=%s', obj)
        self.managementObj = obj

    def getManagementObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-management').debug3Func(): logFunc('called. self.managementObj=%s', self.managementObj)
        return self.managementObj

    def hasManagement (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-management').debug3Func(): logFunc('called. self.managementObj=%s', self.managementObj)
        if self.managementObj:
            return True
        return False

    def newContent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-content').debug3Func(): logFunc('called.')
        content = BlinkyContentMaapi(self._log)
        content.init(self.domain)
        return content

    def setContentObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-content').debug3Func(): logFunc('called. obj=%s', obj)
        self.contentObj = obj

    def getContentObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-content').debug3Func(): logFunc('called. self.contentObj=%s', self.contentObj)
        return self.contentObj

    def hasContent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-content').debug3Func(): logFunc('called. self.contentObj=%s', self.contentObj)
        if self.contentObj:
            return True
        return False

    def newIpv4 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-ipv4').debug3Func(): logFunc('called.')
        ipv4 = BlinkyIpv4Maapi(self._log)
        ipv4.init(self.domain)
        return ipv4

    def setIpv4Obj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ipv4').debug3Func(): logFunc('called. obj=%s', obj)
        self.ipv4Obj = obj

    def getIpv4Obj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ipv4').debug3Func(): logFunc('called. self.ipv4Obj=%s', self.ipv4Obj)
        return self.ipv4Obj

    def hasIpv4 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ipv4').debug3Func(): logFunc('called. self.ipv4Obj=%s', self.ipv4Obj)
        if self.ipv4Obj:
            return True
        return False

    def newIpv6 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-ipv6').debug3Func(): logFunc('called.')
        ipv6 = BlinkyIpv6Maapi(self._log)
        ipv6.init(self.domain)
        return ipv6

    def setIpv6Obj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ipv6').debug3Func(): logFunc('called. obj=%s', obj)
        self.ipv6Obj = obj

    def getIpv6Obj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ipv6').debug3Func(): logFunc('called. self.ipv6Obj=%s', self.ipv6Obj)
        return self.ipv6Obj

    def hasIpv6 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ipv6').debug3Func(): logFunc('called. self.ipv6Obj=%s', self.ipv6Obj)
        if self.ipv6Obj:
            return True
        return False

    def newCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-counters').debug3Func(): logFunc('called.')
        counters = BlinkyCountersMaapi(self._log)
        counters.init(self.domain)
        return counters

    def setCountersObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-counters').debug3Func(): logFunc('called. obj=%s', obj)
        self.countersObj = obj

    def getCountersObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-counters').debug3Func(): logFunc('called. self.countersObj=%s', self.countersObj)
        return self.countersObj

    def hasCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-counters').debug3Func(): logFunc('called. self.countersObj=%s', self.countersObj)
        if self.countersObj:
            return True
        return False

    def newStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-status').debug3Func(): logFunc('called.')
        status = BlinkyStatusMaapi(self._log)
        status.init(self.domain)
        return status

    def setStatusObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. obj=%s', obj)
        self.statusObj = obj

    def getStatusObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        return self.statusObj

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        if self.statusObj:
            return True
        return False

    def newConnectivityCheck (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-connectivitycheck').debug3Func(): logFunc('called.')
        connectivityCheck = BlinkyConnectivityCheckMaapi(self._log)
        connectivityCheck.init(self.domain)
        return connectivityCheck

    def setConnectivityCheckObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-connectivitycheck').debug3Func(): logFunc('called. obj=%s', obj)
        self.connectivityCheckObj = obj

    def getConnectivityCheckObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-connectivitycheck').debug3Func(): logFunc('called. self.connectivityCheckObj=%s', self.connectivityCheckObj)
        return self.connectivityCheckObj

    def hasConnectivityCheck (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-connectivitycheck').debug3Func(): logFunc('called. self.connectivityCheckObj=%s', self.connectivityCheckObj)
        if self.connectivityCheckObj:
            return True
        return False

    def newLink (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-link').debug3Func(): logFunc('called.')
        link = BlinkyLinkMaapi(self._log)
        link.init(self.domain)
        return link

    def setLinkObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-link').debug3Func(): logFunc('called. obj=%s', obj)
        self.linkObj = obj

    def getLinkObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-link').debug3Func(): logFunc('called. self.linkObj=%s', self.linkObj)
        return self.linkObj

    def hasLink (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-link').debug3Func(): logFunc('called. self.linkObj=%s', self.linkObj)
        if self.linkObj:
            return True
        return False

    def newSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-systemdefaults').debug3Func(): logFunc('called.')
        systemDefaults = BlinkySystemDefaultsMaapi(self._log)
        systemDefaults.init(self.domain)
        return systemDefaults

    def setSystemDefaultsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemdefaults').debug3Func(): logFunc('called. obj=%s', obj)
        self.systemDefaultsObj = obj

    def getSystemDefaultsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        return self.systemDefaultsObj

    def hasSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        if self.systemDefaultsObj:
            return True
        return False

    def newDevice (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-device').debug3Func(): logFunc('called.')
        device = BlinkyDeviceMaapi(self._log)
        device.init(self.domain)
        return device

    def setDeviceObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-device').debug3Func(): logFunc('called. obj=%s', obj)
        self.deviceObj = obj

    def getDeviceObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-device').debug3Func(): logFunc('called. self.deviceObj=%s', self.deviceObj)
        return self.deviceObj

    def hasDevice (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-device').debug3Func(): logFunc('called. self.deviceObj=%s', self.deviceObj)
        if self.deviceObj:
            return True
        return False

    def newAlarms (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-alarms').debug3Func(): logFunc('called.')
        alarms = BlinkyAlarmsMaapi(self._log)
        alarms.init(self.domain)
        return alarms

    def setAlarmsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-alarms').debug3Func(): logFunc('called. obj=%s', obj)
        self.alarmsObj = obj

    def getAlarmsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-alarms').debug3Func(): logFunc('called. self.alarmsObj=%s', self.alarmsObj)
        return self.alarmsObj

    def hasAlarms (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-alarms').debug3Func(): logFunc('called. self.alarmsObj=%s', self.alarmsObj)
        if self.alarmsObj:
            return True
        return False

    def newEthernet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-ethernet').debug3Func(): logFunc('called.')
        ethernet = BlinkyEthernetMaapi(self._log)
        ethernet.init(self.domain)
        return ethernet

    def setEthernetObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ethernet').debug3Func(): logFunc('called. obj=%s', obj)
        self.ethernetObj = obj

    def getEthernetObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ethernet').debug3Func(): logFunc('called. self.ethernetObj=%s', self.ethernetObj)
        return self.ethernetObj

    def hasEthernet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ethernet').debug3Func(): logFunc('called. self.ethernetObj=%s', self.ethernetObj)
        if self.ethernetObj:
            return True
        return False

    def newContinuousCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-continuouscounters').debug3Func(): logFunc('called.')
        continuousCounters = BlinkyContinuousCountersMaapi(self._log)
        continuousCounters.init(self.domain)
        return continuousCounters

    def setContinuousCountersObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-continuouscounters').debug3Func(): logFunc('called. obj=%s', obj)
        self.continuousCountersObj = obj

    def getContinuousCountersObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-continuouscounters').debug3Func(): logFunc('called. self.continuousCountersObj=%s', self.continuousCountersObj)
        return self.continuousCountersObj

    def hasContinuousCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-continuouscounters').debug3Func(): logFunc('called. self.continuousCountersObj=%s', self.continuousCountersObj)
        if self.continuousCountersObj:
            return True
        return False



    def requestShutdown (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-shutdown').debug3Func(): logFunc('called. requested=%s', requested)
        self.shutdownRequested = requested
        self.shutdownSet = False

    def isShutdownRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-shutdown-requested').debug3Func(): logFunc('called. requested=%s', self.shutdownRequested)
        return self.shutdownRequested

    def getShutdown (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-shutdown').debug3Func(): logFunc('called. self.shutdownSet=%s, self.shutdown=%s', self.shutdownSet, self.shutdown)
        if self.shutdownSet:
            return self.shutdown
        return None

    def hasShutdown (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-shutdown').debug3Func(): logFunc('called. self.shutdownSet=%s, self.shutdown=%s', self.shutdownSet, self.shutdown)
        if self.shutdownSet:
            return True
        return False

    def setShutdown (self, shutdown):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-shutdown').debug3Func(): logFunc('called. shutdown=%s, old=%s', shutdown, self.shutdown)
        self.shutdownSet = True
        self.shutdown = shutdown

    def requestMuteReporting (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mutereporting').debug3Func(): logFunc('called. requested=%s', requested)
        self.muteReportingRequested = requested
        self.muteReportingSet = False

    def isMuteReportingRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mutereporting-requested').debug3Func(): logFunc('called. requested=%s', self.muteReportingRequested)
        return self.muteReportingRequested

    def getMuteReporting (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mutereporting').debug3Func(): logFunc('called. self.muteReportingSet=%s, self.muteReporting=%s', self.muteReportingSet, self.muteReporting)
        if self.muteReportingSet:
            return self.muteReporting
        return None

    def hasMuteReporting (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mutereporting').debug3Func(): logFunc('called. self.muteReportingSet=%s, self.muteReporting=%s', self.muteReportingSet, self.muteReporting)
        if self.muteReportingSet:
            return True
        return False

    def setMuteReporting (self, muteReporting):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mutereporting').debug3Func(): logFunc('called. muteReporting=%s, old=%s', muteReporting, self.muteReporting)
        self.muteReportingSet = True
        self.muteReporting = muteReporting

    def requestTechMode (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-techmode').debug3Func(): logFunc('called. requested=%s', requested)
        self.techModeRequested = requested
        self.techModeSet = False

    def isTechModeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-techmode-requested').debug3Func(): logFunc('called. requested=%s', self.techModeRequested)
        return self.techModeRequested

    def getTechMode (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-techmode').debug3Func(): logFunc('called. self.techModeSet=%s, self.techMode=%s', self.techModeSet, self.techMode)
        if self.techModeSet:
            return self.techMode
        return None

    def hasTechMode (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-techmode').debug3Func(): logFunc('called. self.techModeSet=%s, self.techMode=%s', self.techModeSet, self.techMode)
        if self.techModeSet:
            return True
        return False

    def setTechMode (self, techMode):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-techmode').debug3Func(): logFunc('called. techMode=%s, old=%s', techMode, self.techMode)
        self.techModeSet = True
        self.techMode = techMode

    def requestDescription (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-description').debug3Func(): logFunc('called. requested=%s', requested)
        self.descriptionRequested = requested
        self.descriptionSet = False

    def isDescriptionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-description-requested').debug3Func(): logFunc('called. requested=%s', self.descriptionRequested)
        return self.descriptionRequested

    def getDescription (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-description').debug3Func(): logFunc('called. self.descriptionSet=%s, self.description=%s', self.descriptionSet, self.description)
        if self.descriptionSet:
            return self.description
        return None

    def hasDescription (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-description').debug3Func(): logFunc('called. self.descriptionSet=%s, self.description=%s', self.descriptionSet, self.description)
        if self.descriptionSet:
            return True
        return False

    def setDescription (self, description):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-description').debug3Func(): logFunc('called. description=%s, old=%s', description, self.description)
        self.descriptionSet = True
        self.description = description

    def requestConfigurationDelay (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-configurationdelay').debug3Func(): logFunc('called. requested=%s', requested)
        self.configurationDelayRequested = requested
        self.configurationDelaySet = False

    def isConfigurationDelayRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-configurationdelay-requested').debug3Func(): logFunc('called. requested=%s', self.configurationDelayRequested)
        return self.configurationDelayRequested

    def getConfigurationDelay (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-configurationdelay').debug3Func(): logFunc('called. self.configurationDelaySet=%s, self.configurationDelay=%s', self.configurationDelaySet, self.configurationDelay)
        if self.configurationDelaySet:
            return self.configurationDelay
        return None

    def hasConfigurationDelay (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-configurationdelay').debug3Func(): logFunc('called. self.configurationDelaySet=%s, self.configurationDelay=%s', self.configurationDelaySet, self.configurationDelay)
        if self.configurationDelaySet:
            return True
        return False

    def setConfigurationDelay (self, configurationDelay):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-configurationdelay').debug3Func(): logFunc('called. configurationDelay=%s, old=%s', configurationDelay, self.configurationDelay)
        self.configurationDelaySet = True
        self.configurationDelay = configurationDelay

    def requestName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-name').debug3Func(): logFunc('called. requested=%s', requested)
        self.nameRequested = requested
        self.nameSet = False

    def isNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-name-requested').debug3Func(): logFunc('called. requested=%s', self.nameRequested)
        return self.nameRequested

    def getName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return self.name
        return None

    def hasName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return True
        return False

    def setName (self, name):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-name').debug3Func(): logFunc('called. name=%s, old=%s', name, self.name)
        self.nameSet = True
        self.name = name

    def requestSendGratuitousArp (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-sendgratuitousarp').debug3Func(): logFunc('called. requested=%s', requested)
        self.sendGratuitousArpRequested = requested
        self.sendGratuitousArpSet = False

    def isSendGratuitousArpRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-sendgratuitousarp-requested').debug3Func(): logFunc('called. requested=%s', self.sendGratuitousArpRequested)
        return self.sendGratuitousArpRequested

    def getSendGratuitousArp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-sendgratuitousarp').debug3Func(): logFunc('called. self.sendGratuitousArpSet=%s, self.sendGratuitousArp=%s', self.sendGratuitousArpSet, self.sendGratuitousArp)
        if self.sendGratuitousArpSet:
            return self.sendGratuitousArp
        return None

    def hasSendGratuitousArp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-sendgratuitousarp').debug3Func(): logFunc('called. self.sendGratuitousArpSet=%s, self.sendGratuitousArp=%s', self.sendGratuitousArpSet, self.sendGratuitousArp)
        if self.sendGratuitousArpSet:
            return True
        return False

    def setSendGratuitousArp (self, sendGratuitousArp):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-sendgratuitousarp').debug3Func(): logFunc('called. sendGratuitousArp=%s, old=%s', sendGratuitousArp, self.sendGratuitousArp)
        self.sendGratuitousArpSet = True
        self.sendGratuitousArp = sendGratuitousArp

    def requestMibIfIndex (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mibifindex').debug3Func(): logFunc('called. requested=%s', requested)
        self.mibIfIndexRequested = requested
        self.mibIfIndexSet = False

    def isMibIfIndexRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mibifindex-requested').debug3Func(): logFunc('called. requested=%s', self.mibIfIndexRequested)
        return self.mibIfIndexRequested

    def getMibIfIndex (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mibifindex').debug3Func(): logFunc('called. self.mibIfIndexSet=%s, self.mibIfIndex=%s', self.mibIfIndexSet, self.mibIfIndex)
        if self.mibIfIndexSet:
            return self.mibIfIndex
        return None

    def hasMibIfIndex (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mibifindex').debug3Func(): logFunc('called. self.mibIfIndexSet=%s, self.mibIfIndex=%s', self.mibIfIndexSet, self.mibIfIndex)
        if self.mibIfIndexSet:
            return True
        return False

    def setMibIfIndex (self, mibIfIndex):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mibifindex').debug3Func(): logFunc('called. mibIfIndex=%s, old=%s', mibIfIndex, self.mibIfIndex)
        self.mibIfIndexSet = True
        self.mibIfIndex = mibIfIndex


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.continuousCounters32BitObj:
            self.continuousCounters32BitObj._clearAllReadData()
        
        if self.managementObj:
            self.managementObj._clearAllReadData()
        
        if self.contentObj:
            self.contentObj._clearAllReadData()
        
        if self.ipv4Obj:
            self.ipv4Obj._clearAllReadData()
        
        if self.ipv6Obj:
            self.ipv6Obj._clearAllReadData()
        
        if self.countersObj:
            self.countersObj._clearAllReadData()
        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        
        if self.connectivityCheckObj:
            self.connectivityCheckObj._clearAllReadData()
        
        if self.linkObj:
            self.linkObj._clearAllReadData()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        
        if self.deviceObj:
            self.deviceObj._clearAllReadData()
        
        if self.alarmsObj:
            self.alarmsObj._clearAllReadData()
        
        if self.ethernetObj:
            self.ethernetObj._clearAllReadData()
        
        if self.continuousCountersObj:
            self.continuousCountersObj._clearAllReadData()
        

        
        self.shutdown = 0
        self.shutdownSet = False
        
        self.muteReporting = 0
        self.muteReportingSet = False
        
        self.techMode = 0
        self.techModeSet = False
        
        self.description = 0
        self.descriptionSet = False
        
        self.configurationDelay = 0
        self.configurationDelaySet = False
        
        self.name = 0
        self.nameSet = False
        
        self.sendGratuitousArp = 0
        self.sendGratuitousArpSet = False
        
        self.mibIfIndex = 0
        self.mibIfIndexSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(interface);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interfaces", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        interface, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(interface, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       interface, 
                       
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

        keyPath = self._getSelfKeyPath(interface, 
                                       
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
                               interface, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.continuousCounters32BitObj:
            res = self.continuousCounters32BitObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-continuous-counters-32bit-failed').errorFunc(): logFunc('continuousCounters32BitObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.managementObj:
            res = self.managementObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-management-failed').errorFunc(): logFunc('managementObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.contentObj:
            res = self.contentObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-content-failed').errorFunc(): logFunc('contentObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.ipv4Obj:
            res = self.ipv4Obj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-ipv4-failed').errorFunc(): logFunc('ipv4Obj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.ipv6Obj:
            res = self.ipv6Obj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-ipv6-failed').errorFunc(): logFunc('ipv6Obj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            res = self.countersObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-counters-failed').errorFunc(): logFunc('countersObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.statusObj:
            res = self.statusObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-failed').errorFunc(): logFunc('statusObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.connectivityCheckObj:
            res = self.connectivityCheckObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-connectivity-check-failed').errorFunc(): logFunc('connectivityCheckObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.linkObj:
            res = self.linkObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-link-failed').errorFunc(): logFunc('linkObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.deviceObj:
            res = self.deviceObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-device-failed').errorFunc(): logFunc('deviceObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.alarmsObj:
            res = self.alarmsObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-alarms-failed').errorFunc(): logFunc('alarmsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.ethernetObj:
            res = self.ethernetObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-ethernet-failed').errorFunc(): logFunc('ethernetObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.continuousCountersObj:
            res = self.continuousCountersObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-continuous-counters-failed').errorFunc(): logFunc('continuousCountersObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasShutdown():
            valShutdown = Value()
            if self.shutdown is not None:
                valShutdown.setBool(self.shutdown)
            else:
                valShutdown.setEmpty()
            tagValueList.push(("shutdown", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valShutdown)
        
        if self.hasMuteReporting():
            valMuteReporting = Value()
            if self.muteReporting is not None:
                valMuteReporting.setBool(self.muteReporting)
            else:
                valMuteReporting.setEmpty()
            tagValueList.push(("mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMuteReporting)
        
        if self.hasTechMode():
            valTechMode = Value()
            if self.techMode is not None:
                valTechMode.setBool(self.techMode)
            else:
                valTechMode.setEmpty()
            tagValueList.push(("tech-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTechMode)
        
        if self.hasDescription():
            valDescription = Value()
            if self.description is not None:
                valDescription.setString(self.description)
            else:
                valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valDescription)
        
        if self.hasConfigurationDelay():
            valConfigurationDelay = Value()
            if self.configurationDelay is not None:
                valConfigurationDelay.setUint64(self.configurationDelay)
            else:
                valConfigurationDelay.setEmpty()
            tagValueList.push(("configuration-delay", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valConfigurationDelay)
        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valName)
        
        if self.hasSendGratuitousArp():
            valSendGratuitousArp = Value()
            if self.sendGratuitousArp is not None:
                valSendGratuitousArp.setBool(self.sendGratuitousArp)
            else:
                valSendGratuitousArp.setEmpty()
            tagValueList.push(("send-gratuitous-arp", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valSendGratuitousArp)
        
        if self.hasMibIfIndex():
            valMibIfIndex = Value()
            if self.mibIfIndex is not None:
                valMibIfIndex.setInt32(self.mibIfIndex)
            else:
                valMibIfIndex.setEmpty()
            tagValueList.push(("mib-if-index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMibIfIndex)
        

        
        if self.continuousCounters32BitObj:
            valBegin = Value()
            (tag, ns, prefix) = ("continuous-counters-32bit" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.continuousCounters32BitObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-continuous-counters-32bit-failed').errorFunc(): logFunc('continuousCounters32BitObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.managementObj:
            valBegin = Value()
            (tag, ns, prefix) = ("management" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.managementObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-management-failed').errorFunc(): logFunc('managementObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.contentObj:
            valBegin = Value()
            (tag, ns, prefix) = ("content" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.contentObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-content-failed').errorFunc(): logFunc('contentObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.ipv4Obj:
            valBegin = Value()
            (tag, ns, prefix) = ("ipv4" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.ipv4Obj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-ipv4-failed').errorFunc(): logFunc('ipv4Obj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.ipv6Obj:
            valBegin = Value()
            (tag, ns, prefix) = ("ipv6" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.ipv6Obj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-ipv6-failed').errorFunc(): logFunc('ipv6Obj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.countersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.countersObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-counters-failed').errorFunc(): logFunc('countersObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.connectivityCheckObj:
            valBegin = Value()
            (tag, ns, prefix) = ("connectivity-check" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.connectivityCheckObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-connectivity-check-failed').errorFunc(): logFunc('connectivityCheckObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.linkObj:
            valBegin = Value()
            (tag, ns, prefix) = ("link" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.linkObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-link-failed').errorFunc(): logFunc('linkObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.deviceObj:
            valBegin = Value()
            (tag, ns, prefix) = ("device" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.deviceObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-device-failed').errorFunc(): logFunc('deviceObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.alarmsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("alarms" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.alarmsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-alarms-failed').errorFunc(): logFunc('alarmsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.ethernetObj:
            valBegin = Value()
            (tag, ns, prefix) = ("ethernet" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.ethernetObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-ethernet-failed').errorFunc(): logFunc('ethernetObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.continuousCountersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("continuous-counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.continuousCountersObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-continuous-counters-failed').errorFunc(): logFunc('continuousCountersObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isShutdownRequested():
            valShutdown = Value()
            valShutdown.setEmpty()
            tagValueList.push(("shutdown", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valShutdown)
        
        if self.isMuteReportingRequested():
            valMuteReporting = Value()
            valMuteReporting.setEmpty()
            tagValueList.push(("mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMuteReporting)
        
        if self.isTechModeRequested():
            valTechMode = Value()
            valTechMode.setEmpty()
            tagValueList.push(("tech-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTechMode)
        
        if self.isDescriptionRequested():
            valDescription = Value()
            valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valDescription)
        
        if self.isConfigurationDelayRequested():
            valConfigurationDelay = Value()
            valConfigurationDelay.setEmpty()
            tagValueList.push(("configuration-delay", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valConfigurationDelay)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valName)
        
        if self.isSendGratuitousArpRequested():
            valSendGratuitousArp = Value()
            valSendGratuitousArp.setEmpty()
            tagValueList.push(("send-gratuitous-arp", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valSendGratuitousArp)
        
        if self.isMibIfIndexRequested():
            valMibIfIndex = Value()
            valMibIfIndex.setEmpty()
            tagValueList.push(("mib-if-index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMibIfIndex)
        

        
        if self.continuousCounters32BitObj:
            valBegin = Value()
            (tag, ns, prefix) = ("continuous-counters-32bit" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.continuousCounters32BitObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-continuous-counters-32bit-failed').errorFunc(): logFunc('continuousCounters32BitObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.managementObj:
            valBegin = Value()
            (tag, ns, prefix) = ("management" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.managementObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-management-failed').errorFunc(): logFunc('managementObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.contentObj:
            valBegin = Value()
            (tag, ns, prefix) = ("content" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.contentObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-content-failed').errorFunc(): logFunc('contentObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.ipv4Obj:
            valBegin = Value()
            (tag, ns, prefix) = ("ipv4" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.ipv4Obj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-ipv4-failed').errorFunc(): logFunc('ipv4Obj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.ipv6Obj:
            valBegin = Value()
            (tag, ns, prefix) = ("ipv6" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.ipv6Obj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-ipv6-failed').errorFunc(): logFunc('ipv6Obj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.countersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.countersObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-counters-failed').errorFunc(): logFunc('countersObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.connectivityCheckObj:
            valBegin = Value()
            (tag, ns, prefix) = ("connectivity-check" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.connectivityCheckObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-connectivity-check-failed').errorFunc(): logFunc('connectivityCheckObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.linkObj:
            valBegin = Value()
            (tag, ns, prefix) = ("link" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.linkObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-link-failed').errorFunc(): logFunc('linkObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.deviceObj:
            valBegin = Value()
            (tag, ns, prefix) = ("device" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.deviceObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-device-failed').errorFunc(): logFunc('deviceObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.alarmsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("alarms" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.alarmsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-alarms-failed').errorFunc(): logFunc('alarmsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.ethernetObj:
            valBegin = Value()
            (tag, ns, prefix) = ("ethernet" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.ethernetObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-ethernet-failed').errorFunc(): logFunc('ethernetObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.continuousCountersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("continuous-counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.continuousCountersObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-continuous-counters-failed').errorFunc(): logFunc('continuousCountersObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isShutdownRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "shutdown") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-shutdown').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "shutdown", "shutdown", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-shutdown-bad-value').infoFunc(): logFunc('shutdown not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setShutdown(tempVar)
            for logFunc in self._log('read-tag-values-shutdown').debug3Func(): logFunc('read shutdown. shutdown=%s, tempValue=%s', self.shutdown, tempValue.getType())
        
        if self.isMuteReportingRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mute-reporting") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mutereporting').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "muteReporting", "mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mute-reporting-bad-value').infoFunc(): logFunc('muteReporting not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMuteReporting(tempVar)
            for logFunc in self._log('read-tag-values-mute-reporting').debug3Func(): logFunc('read muteReporting. muteReporting=%s, tempValue=%s', self.muteReporting, tempValue.getType())
        
        if self.isTechModeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "tech-mode") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-techmode').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "techMode", "tech-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-tech-mode-bad-value').infoFunc(): logFunc('techMode not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTechMode(tempVar)
            for logFunc in self._log('read-tag-values-tech-mode').debug3Func(): logFunc('read techMode. techMode=%s, tempValue=%s', self.techMode, tempValue.getType())
        
        if self.isDescriptionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "description") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-description').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "description", "description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-description-bad-value').infoFunc(): logFunc('description not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDescription(tempVar)
            for logFunc in self._log('read-tag-values-description').debug3Func(): logFunc('read description. description=%s, tempValue=%s', self.description, tempValue.getType())
        
        if self.isConfigurationDelayRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "configuration-delay") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-configurationdelay').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "configurationDelay", "configuration-delay", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-configuration-delay-bad-value').infoFunc(): logFunc('configurationDelay not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setConfigurationDelay(tempVar)
            for logFunc in self._log('read-tag-values-configuration-delay').debug3Func(): logFunc('read configurationDelay. configurationDelay=%s, tempValue=%s', self.configurationDelay, tempValue.getType())
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-name-bad-value').infoFunc(): logFunc('name not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setName(tempVar)
            for logFunc in self._log('read-tag-values-name').debug3Func(): logFunc('read name. name=%s, tempValue=%s', self.name, tempValue.getType())
        
        if self.isSendGratuitousArpRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "send-gratuitous-arp") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-sendgratuitousarp').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "sendGratuitousArp", "send-gratuitous-arp", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-send-gratuitous-arp-bad-value').infoFunc(): logFunc('sendGratuitousArp not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSendGratuitousArp(tempVar)
            for logFunc in self._log('read-tag-values-send-gratuitous-arp').debug3Func(): logFunc('read sendGratuitousArp. sendGratuitousArp=%s, tempValue=%s', self.sendGratuitousArp, tempValue.getType())
        
        if self.isMibIfIndexRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mib-if-index") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mibifindex').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mibIfIndex", "mib-if-index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt32()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mib-if-index-bad-value').infoFunc(): logFunc('mibIfIndex not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMibIfIndex(tempVar)
            for logFunc in self._log('read-tag-values-mib-if-index').debug3Func(): logFunc('read mibIfIndex. mibIfIndex=%s, tempValue=%s', self.mibIfIndex, tempValue.getType())
        

        
        if self.continuousCounters32BitObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "continuous-counters-32bit") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "continuous-counters-32bit", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.continuousCounters32BitObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-continuous-counters-32bit-failed').errorFunc(): logFunc('continuousCounters32BitObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "continuous-counters-32bit") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "continuous-counters-32bit", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.managementObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "management") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "management", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.managementObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-management-failed').errorFunc(): logFunc('managementObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "management") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "management", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.contentObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "content") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.contentObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-content-failed').errorFunc(): logFunc('contentObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "content") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.ipv4Obj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "ipv4") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "ipv4", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.ipv4Obj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-ipv4-failed').errorFunc(): logFunc('ipv4Obj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "ipv4") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "ipv4", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.ipv6Obj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "ipv6") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "ipv6", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.ipv6Obj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-ipv6-failed').errorFunc(): logFunc('ipv6Obj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "ipv6") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "ipv6", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.countersObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-counters-failed').errorFunc(): logFunc('countersObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.statusObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.statusObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-status-failed').errorFunc(): logFunc('statusObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.connectivityCheckObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "connectivity-check") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "connectivity-check", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.connectivityCheckObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-connectivity-check-failed').errorFunc(): logFunc('connectivityCheckObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "connectivity-check") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "connectivity-check", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.linkObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "link") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "link", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.linkObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-link-failed').errorFunc(): logFunc('linkObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "link") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "link", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.systemDefaultsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.deviceObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "device") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.deviceObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-device-failed').errorFunc(): logFunc('deviceObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "device") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.alarmsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "alarms") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.alarmsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-alarms-failed').errorFunc(): logFunc('alarmsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "alarms") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.ethernetObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "ethernet") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "ethernet", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.ethernetObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-ethernet-failed').errorFunc(): logFunc('ethernetObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "ethernet") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "ethernet", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.continuousCountersObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "continuous-counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "continuous-counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.continuousCountersObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-continuous-counters-failed').errorFunc(): logFunc('continuousCountersObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "continuous-counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "continuous-counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



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


