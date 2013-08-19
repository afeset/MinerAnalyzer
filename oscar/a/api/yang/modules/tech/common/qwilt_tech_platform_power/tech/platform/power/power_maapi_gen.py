


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

from power_maapi_base_gen import PowerMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.status.status_maapi_gen import BlinkyStatusMaapi
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.power_supply_maapi_list_gen import BlinkyPowerSupplyMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.alarm.alarm_maapi_gen import BlinkyAlarmMaapi
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.simulation.simulation_maapi_gen import BlinkySimulationMaapi
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi



class BlinkyPowerMaapi(PowerMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-power")
        self.domain = None

        
        self.statusObj = None
        
        self.powerSupplyListObj = None
        
        self.alarmObj = None
        
        self.simulationObj = None
        
        self.systemDefaultsObj = None
        

        
        self.muteReportingRequested = False
        self.muteReporting = None
        self.muteReportingSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMuteReporting(True)
        
        self.requestEnabled(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        
        if not self.powerSupplyListObj:
            self.powerSupplyListObj = self.newPowerSupplyList()
            self.powerSupplyListObj.requestConfigAndOper()
        
        if not self.alarmObj:
            self.alarmObj = self.newAlarm()
            self.alarmObj.requestConfigAndOper()
        
        if not self.simulationObj:
            self.simulationObj = self.newSimulation()
            self.simulationObj.requestConfigAndOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMuteReporting(True)
        
        self.requestEnabled(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        
        if not self.powerSupplyListObj:
            self.powerSupplyListObj = self.newPowerSupplyList()
            self.powerSupplyListObj.requestConfig()
        
        if not self.alarmObj:
            self.alarmObj = self.newAlarm()
            self.alarmObj.requestConfig()
        
        if not self.simulationObj:
            self.simulationObj = self.newSimulation()
            self.simulationObj.requestConfig()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMuteReporting(False)
        
        self.requestEnabled(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        
        if not self.powerSupplyListObj:
            self.powerSupplyListObj = self.newPowerSupplyList()
            self.powerSupplyListObj.requestOper()
        
        if not self.alarmObj:
            self.alarmObj = self.newAlarm()
            self.alarmObj.requestOper()
        
        if not self.simulationObj:
            self.simulationObj = self.newSimulation()
            self.simulationObj.requestOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMuteReporting(False)
        
        self.requestEnabled(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        
        if not self.powerSupplyListObj:
            self.powerSupplyListObj = self.newPowerSupplyList()
            self.powerSupplyListObj.clearAllRequested()
        
        if not self.alarmObj:
            self.alarmObj = self.newAlarm()
            self.alarmObj.clearAllRequested()
        
        if not self.simulationObj:
            self.simulationObj = self.newSimulation()
            self.simulationObj.clearAllRequested()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setMuteReporting(None)
        self.muteReportingSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        
        if self.powerSupplyListObj:
            self.powerSupplyListObj.clearAllSet()
        
        if self.alarmObj:
            self.alarmObj.clearAllSet()
        
        if self.simulationObj:
            self.simulationObj.clearAllSet()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        

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

    def newPowerSupplyList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-powersupplylist').debug3Func(): logFunc('called.')
        powerSupplyList = BlinkyPowerSupplyMaapiList(self._log)
        powerSupplyList.init(self.domain)
        return powerSupplyList

    def setPowerSupplyListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-powersupplylist').debug3Func(): logFunc('called. obj=%s', obj)
        self.powerSupplyListObj = obj

    def getPowerSupplyListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-powersupplylist').debug3Func(): logFunc('called. self.powerSupplyListObj=%s', self.powerSupplyListObj)
        return self.powerSupplyListObj

    def hasPowerSupplyList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-powersupplylist').debug3Func(): logFunc('called. self.powerSupplyListObj=%s', self.powerSupplyListObj)
        if self.powerSupplyListObj:
            return True
        return False

    def newAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-alarm').debug3Func(): logFunc('called.')
        alarm = BlinkyAlarmMaapi(self._log)
        alarm.init(self.domain)
        return alarm

    def setAlarmObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-alarm').debug3Func(): logFunc('called. obj=%s', obj)
        self.alarmObj = obj

    def getAlarmObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-alarm').debug3Func(): logFunc('called. self.alarmObj=%s', self.alarmObj)
        return self.alarmObj

    def hasAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-alarm').debug3Func(): logFunc('called. self.alarmObj=%s', self.alarmObj)
        if self.alarmObj:
            return True
        return False

    def newSimulation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-simulation').debug3Func(): logFunc('called.')
        simulation = BlinkySimulationMaapi(self._log)
        simulation.init(self.domain)
        return simulation

    def setSimulationObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-simulation').debug3Func(): logFunc('called. obj=%s', obj)
        self.simulationObj = obj

    def getSimulationObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-simulation').debug3Func(): logFunc('called. self.simulationObj=%s', self.simulationObj)
        return self.simulationObj

    def hasSimulation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-simulation').debug3Func(): logFunc('called. self.simulationObj=%s', self.simulationObj)
        if self.simulationObj:
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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        
        if self.powerSupplyListObj:
            self.powerSupplyListObj._clearAllReadData()
        
        if self.alarmObj:
            self.alarmObj._clearAllReadData()
        
        if self.simulationObj:
            self.simulationObj._clearAllReadData()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        

        
        self.muteReporting = 0
        self.muteReportingSet = False
        
        self.enabled = 0
        self.enabledSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("power", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("platform", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", "qt-pltf"))
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

        
        if self.statusObj:
            res = self.statusObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-failed').errorFunc(): logFunc('statusObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.powerSupplyListObj:
            res = self.powerSupplyListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-power-supply-failed').errorFunc(): logFunc('powerSupplyListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.alarmObj:
            res = self.alarmObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-alarm-failed').errorFunc(): logFunc('alarmObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.simulationObj:
            res = self.simulationObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-simulation-failed').errorFunc(): logFunc('simulationObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasMuteReporting():
            valMuteReporting = Value()
            if self.muteReporting is not None:
                valMuteReporting.setBool(self.muteReporting)
            else:
                valMuteReporting.setEmpty()
            tagValueList.push(("mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valMuteReporting)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valEnabled)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr")
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
        
        if self.powerSupplyListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("power-supply" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.powerSupplyListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-power-supply-failed').errorFunc(): logFunc('powerSupplyListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.alarmObj:
            valBegin = Value()
            (tag, ns, prefix) = ("alarm" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.alarmObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-alarm-failed').errorFunc(): logFunc('alarmObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.simulationObj:
            valBegin = Value()
            (tag, ns, prefix) = ("simulation" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.simulationObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-simulation-failed').errorFunc(): logFunc('simulationObj._fillWriteTagValues() failed. PARAMS')
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
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr")
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
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isMuteReportingRequested():
            valMuteReporting = Value()
            valMuteReporting.setEmpty()
            tagValueList.push(("mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valMuteReporting)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valEnabled)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr")
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
        
        if self.powerSupplyListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("power-supply" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.powerSupplyListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-power-supply-failed').errorFunc(): logFunc('powerSupplyListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.alarmObj:
            valBegin = Value()
            (tag, ns, prefix) = ("alarm" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.alarmObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-alarm-failed').errorFunc(): logFunc('alarmObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.simulationObj:
            valBegin = Value()
            (tag, ns, prefix) = ("simulation" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.simulationObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-simulation-failed').errorFunc(): logFunc('simulationObj._fillReadTagValues() failed. PARAMS')
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
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr")
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
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isMuteReportingRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mute-reporting") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mutereporting').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "muteReporting", "mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
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
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
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
        

        
        if self.statusObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", Value.kXmlBegin,
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.powerSupplyListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "power-supply") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "power-supply", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.powerSupplyListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-power-supply-failed').errorFunc(): logFunc('powerSupplyListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "power-supply") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "power-supply", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.alarmObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "alarm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.alarmObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-alarm-failed').errorFunc(): logFunc('alarmObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "alarm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.simulationObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "simulation") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "simulation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.simulationObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-simulation-failed').errorFunc(): logFunc('simulationObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "simulation") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "simulation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", Value.kXmlBegin,
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "power", 
        "namespace": "power", 
        "className": "PowerMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_maapi_gen import PowerMaapi", 
        "baseClassName": "PowerMaapiBase", 
        "baseModule": "power_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-pltf", 
            "yangName": "platform", 
            "namespace": "platform", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", 
            "name": "platform"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "yangName": "power", 
            "namespace": "power", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "power"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "memberName": "powerSupplyList", 
            "yangName": "power-supply", 
            "className": "BlinkyPowerSupplyMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.power_supply_maapi_list_gen import BlinkyPowerSupplyMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "memberName": "alarm", 
            "yangName": "alarm", 
            "className": "BlinkyAlarmMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.alarm.alarm_maapi_gen import BlinkyAlarmMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "memberName": "simulation", 
            "yangName": "simulation", 
            "className": "BlinkySimulationMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.simulation.simulation_maapi_gen import BlinkySimulationMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
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
            "qwilt_tech_platform_power"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


