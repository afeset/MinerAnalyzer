


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

from system_defaults_maapi_base_gen import SystemDefaultsMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.content.content_maapi_gen import BlinkyContentMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.connectivity_check_maapi_gen import BlinkyConnectivityCheckMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.management.management_maapi_gen import BlinkyManagementMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.link.link_maapi_gen import BlinkyLinkMaapi
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.device.device_maapi_gen import BlinkyDeviceMaapi



class BlinkySystemDefaultsMaapi(SystemDefaultsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-systemDefaults")
        self.domain = None

        
        self.contentObj = None
        
        self.connectivityCheckObj = None
        
        self.managementObj = None
        
        self.linkObj = None
        
        self.deviceObj = None
        

        
        self.configurationDelayRequested = False
        self.configurationDelay = None
        self.configurationDelaySet = False
        
        self.muteReportingRequested = False
        self.muteReporting = None
        self.muteReportingSet = False
        
        self.sendGratuitousArpRequested = False
        self.sendGratuitousArp = None
        self.sendGratuitousArpSet = False
        
        self.shutdownRequested = False
        self.shutdown = None
        self.shutdownSet = False
        
        self.techModeRequested = False
        self.techMode = None
        self.techModeSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestConfigurationDelay(True)
        
        self.requestMuteReporting(True)
        
        self.requestSendGratuitousArp(True)
        
        self.requestShutdown(True)
        
        self.requestTechMode(True)
        
        
        
        if not self.contentObj:
            self.contentObj = self.newContent()
            self.contentObj.requestConfigAndOper()
        
        if not self.connectivityCheckObj:
            self.connectivityCheckObj = self.newConnectivityCheck()
            self.connectivityCheckObj.requestConfigAndOper()
        
        if not self.managementObj:
            self.managementObj = self.newManagement()
            self.managementObj.requestConfigAndOper()
        
        if not self.linkObj:
            self.linkObj = self.newLink()
            self.linkObj.requestConfigAndOper()
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestConfigurationDelay(True)
        
        self.requestMuteReporting(True)
        
        self.requestSendGratuitousArp(True)
        
        self.requestShutdown(True)
        
        self.requestTechMode(True)
        
        
        
        if not self.contentObj:
            self.contentObj = self.newContent()
            self.contentObj.requestConfig()
        
        if not self.connectivityCheckObj:
            self.connectivityCheckObj = self.newConnectivityCheck()
            self.connectivityCheckObj.requestConfig()
        
        if not self.managementObj:
            self.managementObj = self.newManagement()
            self.managementObj.requestConfig()
        
        if not self.linkObj:
            self.linkObj = self.newLink()
            self.linkObj.requestConfig()
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestConfigurationDelay(False)
        
        self.requestMuteReporting(False)
        
        self.requestSendGratuitousArp(False)
        
        self.requestShutdown(False)
        
        self.requestTechMode(False)
        
        
        
        if not self.contentObj:
            self.contentObj = self.newContent()
            self.contentObj.requestOper()
        
        if not self.connectivityCheckObj:
            self.connectivityCheckObj = self.newConnectivityCheck()
            self.connectivityCheckObj.requestOper()
        
        if not self.managementObj:
            self.managementObj = self.newManagement()
            self.managementObj.requestOper()
        
        if not self.linkObj:
            self.linkObj = self.newLink()
            self.linkObj.requestOper()
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestConfigurationDelay(False)
        
        self.requestMuteReporting(False)
        
        self.requestSendGratuitousArp(False)
        
        self.requestShutdown(False)
        
        self.requestTechMode(False)
        
        
        
        if not self.contentObj:
            self.contentObj = self.newContent()
            self.contentObj.clearAllRequested()
        
        if not self.connectivityCheckObj:
            self.connectivityCheckObj = self.newConnectivityCheck()
            self.connectivityCheckObj.clearAllRequested()
        
        if not self.managementObj:
            self.managementObj = self.newManagement()
            self.managementObj.clearAllRequested()
        
        if not self.linkObj:
            self.linkObj = self.newLink()
            self.linkObj.clearAllRequested()
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setConfigurationDelay(None)
        self.configurationDelaySet = False
        
        self.setMuteReporting(None)
        self.muteReportingSet = False
        
        self.setSendGratuitousArp(None)
        self.sendGratuitousArpSet = False
        
        self.setShutdown(None)
        self.shutdownSet = False
        
        self.setTechMode(None)
        self.techModeSet = False
        
        
        if self.contentObj:
            self.contentObj.clearAllSet()
        
        if self.connectivityCheckObj:
            self.connectivityCheckObj.clearAllSet()
        
        if self.managementObj:
            self.managementObj.clearAllSet()
        
        if self.linkObj:
            self.linkObj.clearAllSet()
        
        if self.deviceObj:
            self.deviceObj.clearAllSet()
        

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.contentObj:
            self.contentObj._clearAllReadData()
        
        if self.connectivityCheckObj:
            self.connectivityCheckObj._clearAllReadData()
        
        if self.managementObj:
            self.managementObj._clearAllReadData()
        
        if self.linkObj:
            self.linkObj._clearAllReadData()
        
        if self.deviceObj:
            self.deviceObj._clearAllReadData()
        

        
        self.configurationDelay = 0
        self.configurationDelaySet = False
        
        self.muteReporting = 0
        self.muteReportingSet = False
        
        self.sendGratuitousArp = 0
        self.sendGratuitousArpSet = False
        
        self.shutdown = 0
        self.shutdownSet = False
        
        self.techMode = 0
        self.techModeSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
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

        
        if self.contentObj:
            res = self.contentObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-content-failed').errorFunc(): logFunc('contentObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.connectivityCheckObj:
            res = self.connectivityCheckObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-connectivity-check-failed').errorFunc(): logFunc('connectivityCheckObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.managementObj:
            res = self.managementObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-management-failed').errorFunc(): logFunc('managementObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.linkObj:
            res = self.linkObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-link-failed').errorFunc(): logFunc('linkObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.deviceObj:
            res = self.deviceObj._collectItemsToDelete(interface, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-device-failed').errorFunc(): logFunc('deviceObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasConfigurationDelay():
            valConfigurationDelay = Value()
            if self.configurationDelay is not None:
                valConfigurationDelay.setUint64(self.configurationDelay)
            else:
                valConfigurationDelay.setEmpty()
            tagValueList.push(("configuration-delay", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valConfigurationDelay)
        
        if self.hasMuteReporting():
            valMuteReporting = Value()
            if self.muteReporting is not None:
                valMuteReporting.setBool(self.muteReporting)
            else:
                valMuteReporting.setEmpty()
            tagValueList.push(("mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMuteReporting)
        
        if self.hasSendGratuitousArp():
            valSendGratuitousArp = Value()
            if self.sendGratuitousArp is not None:
                valSendGratuitousArp.setBool(self.sendGratuitousArp)
            else:
                valSendGratuitousArp.setEmpty()
            tagValueList.push(("send-gratuitous-arp", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valSendGratuitousArp)
        
        if self.hasShutdown():
            valShutdown = Value()
            if self.shutdown is not None:
                valShutdown.setBool(self.shutdown)
            else:
                valShutdown.setEmpty()
            tagValueList.push(("shutdown", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valShutdown)
        
        if self.hasTechMode():
            valTechMode = Value()
            if self.techMode is not None:
                valTechMode.setBool(self.techMode)
            else:
                valTechMode.setEmpty()
            tagValueList.push(("tech-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTechMode)
        

        
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
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isConfigurationDelayRequested():
            valConfigurationDelay = Value()
            valConfigurationDelay.setEmpty()
            tagValueList.push(("configuration-delay", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valConfigurationDelay)
        
        if self.isMuteReportingRequested():
            valMuteReporting = Value()
            valMuteReporting.setEmpty()
            tagValueList.push(("mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMuteReporting)
        
        if self.isSendGratuitousArpRequested():
            valSendGratuitousArp = Value()
            valSendGratuitousArp.setEmpty()
            tagValueList.push(("send-gratuitous-arp", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valSendGratuitousArp)
        
        if self.isShutdownRequested():
            valShutdown = Value()
            valShutdown.setEmpty()
            tagValueList.push(("shutdown", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valShutdown)
        
        if self.isTechModeRequested():
            valTechMode = Value()
            valTechMode.setEmpty()
            tagValueList.push(("tech-mode", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valTechMode)
        

        
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
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
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
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
        "baseClassName": "SystemDefaultsMaapiBase", 
        "baseModule": "system_defaults_maapi_base_gen"
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
            "isCurrent": false, 
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
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "content", 
            "yangName": "content", 
            "className": "BlinkyContentMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.content.content_maapi_gen import BlinkyContentMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "connectivityCheck", 
            "yangName": "connectivity-check", 
            "className": "BlinkyConnectivityCheckMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.connectivity_check_maapi_gen import BlinkyConnectivityCheckMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "management", 
            "yangName": "management", 
            "className": "BlinkyManagementMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.management.management_maapi_gen import BlinkyManagementMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "link", 
            "yangName": "link", 
            "className": "BlinkyLinkMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.link.link_maapi_gen import BlinkyLinkMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "device", 
            "yangName": "device", 
            "className": "BlinkyDeviceMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.device.device_maapi_gen import BlinkyDeviceMaapi", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "configurationDelay", 
            "yangName": "configuration-delay", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
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
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shutdown", 
            "yangName": "shutdown", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "techMode", 
            "yangName": "tech-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "configurationDelay", 
            "yangName": "configuration-delay", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
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
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shutdown", 
            "yangName": "shutdown", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "techMode", 
            "yangName": "tech-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


