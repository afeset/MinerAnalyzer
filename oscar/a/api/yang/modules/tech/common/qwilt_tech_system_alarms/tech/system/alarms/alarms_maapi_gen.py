


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

from alarms_maapi_base_gen import AlarmsMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.thresholds.thresholds_maapi_gen import BlinkyThresholdsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.list.list_maapi_list_gen import BlinkyListMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.summary.summary_maapi_gen import BlinkySummaryMaapi
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.simulate.simulate_maapi_list_gen import BlinkySimulateMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.alarms.alarms_maapi_gen import BlinkyAlarmsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.registered.registered_maapi_list_gen import BlinkyRegisteredMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.counters.counters_maapi_gen import BlinkyCountersMaapi



class BlinkyAlarmsMaapi(AlarmsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-alarms")
        self.domain = None

        
        self.thresholdsObj = None
        
        self.listListObj = None
        
        self.summaryObj = None
        
        self.systemDefaultsObj = None
        
        self.simulateListObj = None
        
        self.alarmsObj = None
        
        self.registeredListObj = None
        
        self.countersObj = None
        

        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.raiseTestAlarmRequested = False
        self.raiseTestAlarm = None
        self.raiseTestAlarmSet = False
        
        self.pollIntervalRequested = False
        self.pollInterval = None
        self.pollIntervalSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(True)
        
        self.requestRaiseTestAlarm(True)
        
        self.requestPollInterval(True)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestConfigAndOper()
        
        if not self.listListObj:
            self.listListObj = self.newListList()
            self.listListObj.requestConfigAndOper()
        
        if not self.summaryObj:
            self.summaryObj = self.newSummary()
            self.summaryObj.requestConfigAndOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        
        if not self.simulateListObj:
            self.simulateListObj = self.newSimulateList()
            self.simulateListObj.requestConfigAndOper()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.requestConfigAndOper()
        
        if not self.registeredListObj:
            self.registeredListObj = self.newRegisteredList()
            self.registeredListObj.requestConfigAndOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(True)
        
        self.requestRaiseTestAlarm(True)
        
        self.requestPollInterval(True)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestConfig()
        
        if not self.listListObj:
            self.listListObj = self.newListList()
            self.listListObj.requestConfig()
        
        if not self.summaryObj:
            self.summaryObj = self.newSummary()
            self.summaryObj.requestConfig()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        
        if not self.simulateListObj:
            self.simulateListObj = self.newSimulateList()
            self.simulateListObj.requestConfig()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.requestConfig()
        
        if not self.registeredListObj:
            self.registeredListObj = self.newRegisteredList()
            self.registeredListObj.requestConfig()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(False)
        
        self.requestRaiseTestAlarm(False)
        
        self.requestPollInterval(False)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestOper()
        
        if not self.listListObj:
            self.listListObj = self.newListList()
            self.listListObj.requestOper()
        
        if not self.summaryObj:
            self.summaryObj = self.newSummary()
            self.summaryObj.requestOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        
        if not self.simulateListObj:
            self.simulateListObj = self.newSimulateList()
            self.simulateListObj.requestOper()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.requestOper()
        
        if not self.registeredListObj:
            self.registeredListObj = self.newRegisteredList()
            self.registeredListObj.requestOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(False)
        
        self.requestRaiseTestAlarm(False)
        
        self.requestPollInterval(False)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.clearAllRequested()
        
        if not self.listListObj:
            self.listListObj = self.newListList()
            self.listListObj.clearAllRequested()
        
        if not self.summaryObj:
            self.summaryObj = self.newSummary()
            self.summaryObj.clearAllRequested()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        
        if not self.simulateListObj:
            self.simulateListObj = self.newSimulateList()
            self.simulateListObj.clearAllRequested()
        
        if not self.alarmsObj:
            self.alarmsObj = self.newAlarms()
            self.alarmsObj.clearAllRequested()
        
        if not self.registeredListObj:
            self.registeredListObj = self.newRegisteredList()
            self.registeredListObj.clearAllRequested()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setRaiseTestAlarm(None)
        self.raiseTestAlarmSet = False
        
        self.setPollInterval(None)
        self.pollIntervalSet = False
        
        
        if self.thresholdsObj:
            self.thresholdsObj.clearAllSet()
        
        if self.listListObj:
            self.listListObj.clearAllSet()
        
        if self.summaryObj:
            self.summaryObj.clearAllSet()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        
        if self.simulateListObj:
            self.simulateListObj.clearAllSet()
        
        if self.alarmsObj:
            self.alarmsObj.clearAllSet()
        
        if self.registeredListObj:
            self.registeredListObj.clearAllSet()
        
        if self.countersObj:
            self.countersObj.clearAllSet()
        

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

    def newThresholds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-thresholds').debug3Func(): logFunc('called.')
        thresholds = BlinkyThresholdsMaapi(self._log)
        thresholds.init(self.domain)
        return thresholds

    def setThresholdsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-thresholds').debug3Func(): logFunc('called. obj=%s', obj)
        self.thresholdsObj = obj

    def getThresholdsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-thresholds').debug3Func(): logFunc('called. self.thresholdsObj=%s', self.thresholdsObj)
        return self.thresholdsObj

    def hasThresholds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-thresholds').debug3Func(): logFunc('called. self.thresholdsObj=%s', self.thresholdsObj)
        if self.thresholdsObj:
            return True
        return False

    def newListList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-listlist').debug3Func(): logFunc('called.')
        listList = BlinkyListMaapiList(self._log)
        listList.init(self.domain)
        return listList

    def setListListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-listlist').debug3Func(): logFunc('called. obj=%s', obj)
        self.listListObj = obj

    def getListListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-listlist').debug3Func(): logFunc('called. self.listListObj=%s', self.listListObj)
        return self.listListObj

    def hasListList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-listlist').debug3Func(): logFunc('called. self.listListObj=%s', self.listListObj)
        if self.listListObj:
            return True
        return False

    def newSummary (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-summary').debug3Func(): logFunc('called.')
        summary = BlinkySummaryMaapi(self._log)
        summary.init(self.domain)
        return summary

    def setSummaryObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-summary').debug3Func(): logFunc('called. obj=%s', obj)
        self.summaryObj = obj

    def getSummaryObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-summary').debug3Func(): logFunc('called. self.summaryObj=%s', self.summaryObj)
        return self.summaryObj

    def hasSummary (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-summary').debug3Func(): logFunc('called. self.summaryObj=%s', self.summaryObj)
        if self.summaryObj:
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

    def newSimulateList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-simulatelist').debug3Func(): logFunc('called.')
        simulateList = BlinkySimulateMaapiList(self._log)
        simulateList.init(self.domain)
        return simulateList

    def setSimulateListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-simulatelist').debug3Func(): logFunc('called. obj=%s', obj)
        self.simulateListObj = obj

    def getSimulateListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-simulatelist').debug3Func(): logFunc('called. self.simulateListObj=%s', self.simulateListObj)
        return self.simulateListObj

    def hasSimulateList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-simulatelist').debug3Func(): logFunc('called. self.simulateListObj=%s', self.simulateListObj)
        if self.simulateListObj:
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

    def newRegisteredList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-registeredlist').debug3Func(): logFunc('called.')
        registeredList = BlinkyRegisteredMaapiList(self._log)
        registeredList.init(self.domain)
        return registeredList

    def setRegisteredListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-registeredlist').debug3Func(): logFunc('called. obj=%s', obj)
        self.registeredListObj = obj

    def getRegisteredListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-registeredlist').debug3Func(): logFunc('called. self.registeredListObj=%s', self.registeredListObj)
        return self.registeredListObj

    def hasRegisteredList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-registeredlist').debug3Func(): logFunc('called. self.registeredListObj=%s', self.registeredListObj)
        if self.registeredListObj:
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

    def requestRaiseTestAlarm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-raisetestalarm').debug3Func(): logFunc('called. requested=%s', requested)
        self.raiseTestAlarmRequested = requested
        self.raiseTestAlarmSet = False

    def isRaiseTestAlarmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-raisetestalarm-requested').debug3Func(): logFunc('called. requested=%s', self.raiseTestAlarmRequested)
        return self.raiseTestAlarmRequested

    def getRaiseTestAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-raisetestalarm').debug3Func(): logFunc('called. self.raiseTestAlarmSet=%s, self.raiseTestAlarm=%s', self.raiseTestAlarmSet, self.raiseTestAlarm)
        if self.raiseTestAlarmSet:
            return self.raiseTestAlarm
        return None

    def hasRaiseTestAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-raisetestalarm').debug3Func(): logFunc('called. self.raiseTestAlarmSet=%s, self.raiseTestAlarm=%s', self.raiseTestAlarmSet, self.raiseTestAlarm)
        if self.raiseTestAlarmSet:
            return True
        return False

    def setRaiseTestAlarm (self, raiseTestAlarm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-raisetestalarm').debug3Func(): logFunc('called. raiseTestAlarm=%s, old=%s', raiseTestAlarm, self.raiseTestAlarm)
        self.raiseTestAlarmSet = True
        self.raiseTestAlarm = raiseTestAlarm

    def requestPollInterval (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pollinterval').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollIntervalRequested = requested
        self.pollIntervalSet = False

    def isPollIntervalRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pollinterval-requested').debug3Func(): logFunc('called. requested=%s', self.pollIntervalRequested)
        return self.pollIntervalRequested

    def getPollInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pollinterval').debug3Func(): logFunc('called. self.pollIntervalSet=%s, self.pollInterval=%s', self.pollIntervalSet, self.pollInterval)
        if self.pollIntervalSet:
            return self.pollInterval
        return None

    def hasPollInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pollinterval').debug3Func(): logFunc('called. self.pollIntervalSet=%s, self.pollInterval=%s', self.pollIntervalSet, self.pollInterval)
        if self.pollIntervalSet:
            return True
        return False

    def setPollInterval (self, pollInterval):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pollinterval').debug3Func(): logFunc('called. pollInterval=%s, old=%s', pollInterval, self.pollInterval)
        self.pollIntervalSet = True
        self.pollInterval = pollInterval


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.thresholdsObj:
            self.thresholdsObj._clearAllReadData()
        
        if self.listListObj:
            self.listListObj._clearAllReadData()
        
        if self.summaryObj:
            self.summaryObj._clearAllReadData()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        
        if self.simulateListObj:
            self.simulateListObj._clearAllReadData()
        
        if self.alarmsObj:
            self.alarmsObj._clearAllReadData()
        
        if self.registeredListObj:
            self.registeredListObj._clearAllReadData()
        
        if self.countersObj:
            self.countersObj._clearAllReadData()
        

        
        self.enabled = 0
        self.enabledSet = False
        
        self.raiseTestAlarm = 0
        self.raiseTestAlarmSet = False
        
        self.pollInterval = 0
        self.pollIntervalSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
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

        
        if self.thresholdsObj:
            res = self.thresholdsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-thresholds-failed').errorFunc(): logFunc('thresholdsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.listListObj:
            res = self.listListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-list-failed').errorFunc(): logFunc('listListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.summaryObj:
            res = self.summaryObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-summary-failed').errorFunc(): logFunc('summaryObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.simulateListObj:
            res = self.simulateListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-simulate-failed').errorFunc(): logFunc('simulateListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.alarmsObj:
            res = self.alarmsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-alarms-failed').errorFunc(): logFunc('alarmsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.registeredListObj:
            res = self.registeredListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-registered-failed').errorFunc(): logFunc('registeredListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            res = self.countersObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-counters-failed').errorFunc(): logFunc('countersObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valEnabled)
        
        if self.hasRaiseTestAlarm():
            valRaiseTestAlarm = Value()
            if self.raiseTestAlarm is not None:
                valRaiseTestAlarm.setBool(self.raiseTestAlarm)
            else:
                valRaiseTestAlarm.setEmpty()
            tagValueList.push(("raise-test-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valRaiseTestAlarm)
        
        if self.hasPollInterval():
            valPollInterval = Value()
            if self.pollInterval is not None:
                valPollInterval.setInt64(self.pollInterval)
            else:
                valPollInterval.setEmpty()
            tagValueList.push(("poll-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valPollInterval)
        

        
        if self.thresholdsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("thresholds" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.thresholdsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-thresholds-failed').errorFunc(): logFunc('thresholdsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.listListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("list" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.listListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-list-failed').errorFunc(): logFunc('listListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.summaryObj:
            valBegin = Value()
            (tag, ns, prefix) = ("summary" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.summaryObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-summary-failed').errorFunc(): logFunc('summaryObj._fillWriteTagValues() failed. PARAMS')
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
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
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
        
        if self.simulateListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("simulate" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.simulateListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-simulate-failed').errorFunc(): logFunc('simulateListObj._fillWriteTagValues() failed. PARAMS')
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
            (tag, ns, prefix) = ("alarms" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
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
        
        if self.registeredListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("registered" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.registeredListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-registered-failed').errorFunc(): logFunc('registeredListObj._fillWriteTagValues() failed. PARAMS')
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
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
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
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valEnabled)
        
        if self.isRaiseTestAlarmRequested():
            valRaiseTestAlarm = Value()
            valRaiseTestAlarm.setEmpty()
            tagValueList.push(("raise-test-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valRaiseTestAlarm)
        
        if self.isPollIntervalRequested():
            valPollInterval = Value()
            valPollInterval.setEmpty()
            tagValueList.push(("poll-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valPollInterval)
        

        
        if self.thresholdsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("thresholds" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.thresholdsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-thresholds-failed').errorFunc(): logFunc('thresholdsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.listListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("list" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.listListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-list-failed').errorFunc(): logFunc('listListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.summaryObj:
            valBegin = Value()
            (tag, ns, prefix) = ("summary" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.summaryObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-summary-failed').errorFunc(): logFunc('summaryObj._fillReadTagValues() failed. PARAMS')
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
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
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
        
        if self.simulateListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("simulate" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.simulateListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-simulate-failed').errorFunc(): logFunc('simulateListObj._fillReadTagValues() failed. PARAMS')
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
            (tag, ns, prefix) = ("alarms" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
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
        
        if self.registeredListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("registered" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.registeredListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-registered-failed').errorFunc(): logFunc('registeredListObj._fillReadTagValues() failed. PARAMS')
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
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms")
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
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
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
        
        if self.isRaiseTestAlarmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "raise-test-alarm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-raisetestalarm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "raiseTestAlarm", "raise-test-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-raise-test-alarm-bad-value').infoFunc(): logFunc('raiseTestAlarm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRaiseTestAlarm(tempVar)
            for logFunc in self._log('read-tag-values-raise-test-alarm').debug3Func(): logFunc('read raiseTestAlarm. raiseTestAlarm=%s, tempValue=%s', self.raiseTestAlarm, tempValue.getType())
        
        if self.isPollIntervalRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-interval") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pollinterval').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollInterval", "poll-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-interval-bad-value').infoFunc(): logFunc('pollInterval not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollInterval(tempVar)
            for logFunc in self._log('read-tag-values-poll-interval').debug3Func(): logFunc('read pollInterval. pollInterval=%s, tempValue=%s', self.pollInterval, tempValue.getType())
        

        
        if self.thresholdsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "thresholds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.thresholdsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-thresholds-failed').errorFunc(): logFunc('thresholdsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "thresholds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.listListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "list") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "list", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.listListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-list-failed').errorFunc(): logFunc('listListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "list") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "list", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.summaryObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "summary") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "summary", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.summaryObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-summary-failed').errorFunc(): logFunc('summaryObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "summary") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "summary", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlBegin,
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.simulateListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "simulate") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "simulate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.simulateListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-simulate-failed').errorFunc(): logFunc('simulateListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "simulate") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "simulate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.alarmsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "alarms") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlBegin,
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.registeredListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "registered") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "registered", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.registeredListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-registered-failed').errorFunc(): logFunc('registeredListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "registered") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "registered", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlBegin,
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



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


