#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

import threading
import time
import re

import a.api.alarms.alarm.all_registered
import a.api.alarms.alarm.alarm_base

from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import AlarmNameType
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import TestAlarmReasonType

from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.alarms_data_gen import AlarmsData
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.thresholds.thresholds_data_gen import ThresholdsData
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.list.list_oper_data_gen import ListOperData
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.simulate.simulate_data_gen import SimulateData
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.counters.counters_oper_data_gen import CountersOperData
from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.summary.summary_oper_data_gen import SummaryOperData


from a.infra.basic.return_codes import ReturnCodes
import a.infra.time.monotonic_clock
import a.infra.time.elapsed_timer
import a.sys.mng.alarm.create_sources

from a.sys.mng.alarm.sources.source_base import AlarmSourceBase
from a.sys.mng.alarm.sources.source_base import AlarmSourceError

import a.sys.mng.alarm.alarm_blinky_adapter

# Bypass for PyChecker
if  __package__ is None:
    G_MODULE_NAME_ALARM_MANAGER                  = "unknown"
    G_GROUP_NAME_ALARM_MANAGER_SOURCES           = "unknown"
    G_GROUP_NAME_ALARM_MANAGER_CONFIGURATION     = "unknown"
    G_GROUP_NAME_ALARM_MANAGER_PROCESS           = "unknown"
    G_GROUP_NAME_ALARM_MANAGER_ALARMS            = "unknown"
    G_GROUP_NAME_ALARM_MANAGER_COUNTERS          = "unknown"
else:
    from . import G_MODULE_NAME_ALARM_MANAGER     
    from . import G_GROUP_NAME_ALARM_MANAGER_SOURCES
    from . import G_GROUP_NAME_ALARM_MANAGER_CONFIGURATION
    from . import G_GROUP_NAME_ALARM_MANAGER_PROCESS
    from . import G_GROUP_NAME_ALARM_MANAGER_ALARMS
    from . import G_GROUP_NAME_ALARM_MANAGER_COUNTERS


class AlarmManager:
    """ Manages the alarms in the system.
    
    Responsible to refresh the alarms table once every few seconds (configurable).

    """
    SLEEP_INTERVAL_SECONDS_WAIT_FOR_CONFIGURATION = 1 # TODO(shmulika): this might be configurable   
    REFRESH_OPER_ALARM_LIST_INTERVAL = 3 # TODO(shmulika): this might be configurable

    def __init__ (self, logger):        
        self._logConfiguration = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_CONFIGURATION)
        self._logProcess       = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_PROCESS)
        self._logSources       = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_SOURCES)
        self._logAlarms        = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_ALARMS)

        ### Configuration ###
        self._configurationLock = threading.RLock()

        self._runningSettings = AlarmsData()
        self._runningThresholds = ThresholdsData()
        self._runningSimulateList = _SimulateList(logger)        

        self._changedSettings = AlarmsData()
        self._changedThresholds = ThresholdsData()

        self._candidateSettings = AlarmsData()
        self._candidateThresholds = ThresholdsData()
        self._candidateSimulateList = _SimulateList(logger)

        self._configErrorMsgFunctor = lambda x: self._logConfiguration("config-error-msg").debug1("error-msg-functor not set yet, called with message: %s", x)

        ### Process ###        
        self._wasStopped = False
        self._wasConfigured = False
        self._pollTimer = None

        # TODO(shmulika): _shouldResetPollTimer is the result of not having "unset" method in BlinkyData.
        #   This is a configuration that can update itself only a-priori (not immediately), and not all values change immediately
        #   This method is responsible for updating the poll-intervalp; it uses _shouldResetPollTimer, but it should have used a BlinkyData called
        #   changedRunningSettings; and if it has a value for pollInterval, only then should this method reset the timer, and then "unset" the pollInterval value
        #   thus signalling to itself, that the change has already been taken care of....
        self._shouldResetPollTimer = True

        ### Alarms & Sources ###
        self._alarmSources = []
        self._activeAlarms = _AlarmTable(self._logAlarms)
        self._activeAlarmsLock = threading.RLock()
        self._registeredAlarms = _AlarmHash(self._logAlarms)

        self._timeoutSinglePollDuration  = _TimeElapsor(logger)
        self._timeoutOverallPollDuration = _TimeElapsor(logger)

        ### Counters ###
        self._counterPollLatencyError           = _Counter(logger, "poll-latency-error")
        self._counterPollLatencyWarning         = _Counter(logger, "poll-latency-warning")
        self._counterSinglePollDurationError    = _Counter(logger, "single-poll-duration-error")
        self._counterSinglePollDurationWarning  = _Counter(logger, "single-poll-duration-warning")
        self._counterOverallPollDurationError   = _Counter(logger, "overall-poll-duration-error")
        self._counterOverallPollDurationWarning = _Counter(logger, "overall-poll-duration-warning")
        self._counterPollError                  = _Counter(logger, "poll-error")
        self._counterAlarmNotSimulated          = _Counter(logger, "alarm-not-simulated")
        self._counterPolls                      = _Counter(logger, "polls")
        self._counterMissedPolls                = _Counter(logger, "missed-polls")

        # TODO(shmulika): these counters need to be added to blinky!
        self._counterTotalPollSeconds           = _Counter(logger, "total-poll-seconds")
        self._elapsorEnabledRunTime             = _TimeElapsor(logger)

        ### OPER ###
        self._alarmListOper = _AlarmOperListList(logger, lambda: self._getCopyActiveAlarms(), lambda: AlarmManager.REFRESH_OPER_ALARM_LIST_INTERVAL)       

###############################################################
# INIT
###############################################################

    def initializeAlarmsAndSources (self):
        """ Called to initialize all the alarms and sources handled by the alarm manager
        Must be called before attaching Blinky
        """
        self._logProcess("initialize-alarms-and-sources").debug1("initializing alarms-source and registered alarms")
        self._initRegisteredAlarms()        
        self._initAlarmSources()


    def _initAlarmSources (self):
        self._logProcess("init-alarm-sources").debug1("initializing all the alarm sources by calling a.sys.mng.alarm.create_sources.createSources")
        a.sys.mng.alarm.create_sources.createSources(self, self._logSources)        


    def addAlarmSource (self, alarmSource):
        """ Adds an AlarmSource that the manager works with """
        self._logProcess("add-alarm-source").debug1("alarms source (%s) called the add-alarm-source method", alarmSource.getInstanceName())
        self._alarmSources.append(alarmSource)
        alarmSource.initSupportedAlarmNames()


    def _initRegisteredAlarms (self):        
        # Add all the registered alarms from api, to our internal hash
        self._logAlarms("init-registered-alarms").debug1("initializing the registered alarms")
        registeredAlarmsList = self._getRegisteredAlarmsListFromApi()        
        for registeredAlarm in registeredAlarmsList:
            self._addRegisteredAlarm(registeredAlarm)

        # initialize the registered oper list
        self._initRegisteredAlarmsOperList()
        

    def _initRegisteredAlarmsOperList (self):
        self._registeredListOper = _AlarmOperListRegistered(self._logAlarms)
        self._registeredListOper.setAlarmsList(self._getOrderedCopyOfRegisteredAlarmsList(self._registeredAlarms.getAllAlarms()))
        self._logAlarms("init-registered-alarms-oper-list").debug2("initialized the registered-alarms-oper-list")


    def _getRegisteredAlarmsListFromApi (self):
        registeredAlarmsListCopy = a.api.alarms.alarm.alarm_base.RegisteredAlarms.s_getRegisteredAlarmsList()[:]
        self._logAlarms("get-registered-alarms-list-from-api").debug2("registered alarms list = %s", registeredAlarmsListCopy)
        return registeredAlarmsListCopy


    def _getOrderedCopyOfRegisteredAlarmsList (self, registeredAlarms):
        """ Notice: Contained RegisteredAlarm objects are the same, not copied. Only the list itself is copied """
        copyRegisteredAlarms = registeredAlarms[:]
        copyRegisteredAlarms.sort(key = lambda alarm: alarm.name)
        copyRegisteredAlarms.sort(key = lambda alarm: alarm.severity)
        return copyRegisteredAlarms

###############################################################
# REGISTERED ALARMS
###############################################################

    def _addRegisteredAlarm (self, registeredAlarm):
        """ Inserts the RegisteredOperData object into the collection of registered alarms """
        self._registeredAlarms.insertAlarm(name = registeredAlarm.name, entity = "none", simulated = False, alarmObject = registeredAlarm)
        self._logAlarms("add-registered-alarm").debug4("added registered alarm = %s", registeredAlarm)


    def _getRegisteredAlarm (self, alarmName):
        """ Gets the RegisteredOperData object according to name, or None if does not exist """
        return self._registeredAlarms.getAlarm(name = alarmName, entity = "none", simulated = False)


    def _isRegisteredAlarm (self, alarmName):
        """ Returns True if the given name is a registered alarm """
        return self._getRegisteredAlarm(alarmName) is not None

###############################################################
# BLINKY, CONFIGURATION, OPER
###############################################################

    def attachToBlinky (self, blinkyAgent):
        """ Attaches this AlarmManager to the given BlinkyAgent
        Notice: this should be done after initializtion (specifically of the alarm sources)
        """
        self._logConfiguration("attach-to-blinky").debug1("attaching to blinky")
        self._alarmBlinkyAdapter = a.sys.mng.alarm.alarm_blinky_adapter.AlarmBlinkyAdapter(self._logConfiguration)
        self._alarmBlinkyAdapter.createDomainAndBlinkyAlarmAndAttach(blinkyAgent, self)
        self._setMaapiDomainToAlarmSources(self._alarmBlinkyAdapter.getMaapiDomain())


    def _setMaapiDomainToAlarmSources (self, maapiDomain):
        """ Sets the given MAAPI domain to all the alarm sources """
        for alarmSource in self._alarmSources:
            alarmSource.setMaapiDomain(maapiDomain)


    def setConfigMsgFunctor (self, functor):
        """ Sets the config error message functor - which will be used to report configuration error messages """
        def logAndCallFunctor (message):
            self._logConfiguration("config-error-msg").debug2("error-msg-functor called with message: %s", message)
            functor(message)

        self._logConfiguration("set-config-msg-functor").debug2("setting error msg functor to given functor %s", functor)
        self._configErrorMsgFunctor = logAndCallFunctor

    ######################
    # OPER
    ######################

    def getNextAlarmsList (self, dpTrxContext, key, nextKey, isCompleted):
        self._logConfiguration("get-next-alarms-list-called").debug3("called with dpTrxContext = %s, key = %s, nextKey = %s, isCompleted = %s", dpTrxContext, key, nextKey, isCompleted)
        rc, errMessage = self._alarmListOper.getNext(dpTrxContext, key, nextKey, isCompleted)        
        if rc != ReturnCodes.kOk:
            self._logConfiguration("get-next-alarms-list-error").debug1("call to alarmListOper.getNext(..) failed. error message: %s", errMessage)
            self._configErrorMsgFunctor(errMessage)
            return ReturnCodes.kGeneralError 

        self._logConfiguration("get-next-alarms-list-done").debug3("done")
        return ReturnCodes.kOk


    def getObjAlarmsList (self, dpTrxContext, key, operData):        
        self._logConfiguration("get-obj-alarms-list-called").debug3("called with dpTrxContext = %s, key = %s, operData = %s", dpTrxContext, key, operData)
        rc, errMessage = self._alarmListOper.getObj(dpTrxContext, key, operData)
        if rc != ReturnCodes.kOk:
            self._logConfiguration("get-obj-alarms-list-error").debug1("call to alarmListOper.getObj(..) failed. error message: %s", errMessage)
            self._configErrorMsgFunctor(errMessage)
            return ReturnCodes.kGeneralError 

        self._logConfiguration("get-obj-alarms-list-done").debug3("done")
        return ReturnCodes.kOk


    def getNextRegisteredList (self, dpTrxContext, key, nextKey, isCompleted):
        self._logConfiguration("get-next-registered-list-called").debug3("called with dpTrxContext = %s, key = %s, nextKey = %s, isCompleted = %s", dpTrxContext, key, nextKey, isCompleted)
        rc, errMessage = self._registeredListOper.getNext(dpTrxContext, key, nextKey, isCompleted)
        if rc != ReturnCodes.kOk:
            self._logConfiguration("get-next-registered-list-error").debug1("call to _registeredListOper.getNext(..) failed. error message: %s", errMessage)
            self._configErrorMsgFunctor(errMessage)
            return ReturnCodes.kGeneralError 

        self._logConfiguration("get-next-registered-list-done").debug3("done")
        return ReturnCodes.kOk


    def getObjRegisteredList (self, dpTrxContext, key, operData):        
        self._logConfiguration("get-obj-registered-list-called").debug3("called with dpTrxContext = %s, key = %s, operData = %s", dpTrxContext, key, operData)
        rc, errMessage = self._registeredListOper.getObj(dpTrxContext, key, operData)        
        if rc != ReturnCodes.kOk:
            self._logConfiguration("get-obj-registered-list-error").debug1("call to _registeredListOper.getObj(..) failed. error message: %s", errMessage)
            self._configErrorMsgFunctor(errMessage)
            return ReturnCodes.kGeneralError 

        self._logConfiguration("get-obj-registered-list-done").debug3("done")
        return ReturnCodes.kOk


    def getObjCountersOperData(self, trxContext, countersData):                
        self._logConfiguration("get-obj-counters-oper-data-called").debug3("called with trxContext = %s, countersData = %s", trxContext, countersData)
        countersData.setPolls(self._counterPolls.get())
        countersData.setPollLatencyWarning(self._counterPollLatencyWarning.get())
        countersData.setPollLatencyError(self._counterPollLatencyError.get())
        countersData.setSinglePollDurationWarning(self._counterSinglePollDurationWarning.get())
        countersData.setSinglePollDurationError(self._counterSinglePollDurationError.get())
        countersData.setOverallPollDurationWarning(self._counterOverallPollDurationWarning.get())
        countersData.setOverallPollDurationError(self._counterOverallPollDurationError.get())
        countersData.setAlarmsCreated(self._activeAlarms.getCountRaisedAlarms())
        countersData.setPollErrors(self._counterPollError.get())   
        countersData.setMissedPolls(self._counterMissedPolls.get())           
        countersData.setActiveSeconds(self._counterTotalPollSeconds.get())
        countersData.setTotalSeconds(int(self._elapsorEnabledRunTime.getElapsedSeconds()))

        self._logConfiguration("get-obj-counters-oper-data-done").debug3("returned counters-oper-data=%s", countersData)
        return ReturnCodes.kOk     


    def getObjSummaryOperData (self, trxContext, summaryData):
        self._logConfiguration("get-obj-summary-oper-data-called").debug3("called with trxContext = %s, summaryData = %s", trxContext, summaryData)
        errorCount     = 0
        emergencyCount = 0       
        criticalCount  = 0
        warningCount   = 0
        alertCount     = 0
        noticeCount    = 0

        alarms = self._getCopyActiveAlarms()
        for alarm in alarms:
            if alarm.severity == SeverityType.kError:
                errorCount = errorCount + 1
            elif alarm.severity == SeverityType.kEmergency:
                emergencyCount = emergencyCount + 1
            elif alarm.severity == SeverityType.kCritical:
                criticalCount = criticalCount + 1
            elif alarm.severity == SeverityType.kWarning:
                warningCount = warningCount + 1
            elif alarm.severity == SeverityType.kAlert:
                alertCount = alertCount + 1
            elif alarm.severity == SeverityType.kNotice:
                noticeCount = noticeCount + 1

        summaryData.setErrorCount(errorCount)
        summaryData.setEmergencyCount(emergencyCount)
        summaryData.setCriticalCount(criticalCount)
        summaryData.setWarningCount(warningCount)
        summaryData.setAlertCount(alertCount)
        summaryData.setNoticeCount(noticeCount)
        
        # find highest severity level
        highestSeverity = SeverityType.kNone
        if noticeCount > 0:
            highestSeverity = SeverityType.kNotice

        if warningCount > 0:
            highestSeverity = SeverityType.kWarning

        if errorCount > 0:
            highestSeverity = SeverityType.kError

        if criticalCount > 0:
            highestSeverity = SeverityType.kCritical

        if alertCount > 0:
            highestSeverity = SeverityType.kAlert

        if emergencyCount > 0:
            highestSeverity = SeverityType.kEmergency
        
        summaryData.setHighestSeverity(highestSeverity)
        self._logConfiguration("get-obj-summary-oper-data-done").debug3("returned summary-oper-data=%s", summaryData)
        return ReturnCodes.kOk


    def getObjAlarmOperData (self, trxContext, alarmData):
        self._logConfiguration("get-obj-alarm-oper-data-called").debug3("called with trxContext = %s, alarmData = %s", trxContext, alarmData)
        runningSettinsg = self.getRunningAlarmsData()
        if runningSettinsg.raiseTestAlarm:
            alarmData.setTestAlarm(True)
            alarmData.setTestAlarmReason(TestAlarmReasonType.kUserConfiguration)
        else:
            alarmData.setTestAlarm(False)
            alarmData.setTestAlarmReason(TestAlarmReasonType.kNone)

        self._logConfiguration("get-obj-alarm-oper-data-done").debug3("returned alarm-oper-data=%s", alarmData)
        return ReturnCodes.kOk

    ######################
    # ACTION
    ######################

    def actionClearCounters (self):
        self._counterPolls.clear()
        self._counterPollLatencyWarning.clear()
        self._counterPollLatencyError.clear()
        self._counterSinglePollDurationWarning.clear()
        self._counterSinglePollDurationError.clear()
        self._counterOverallPollDurationWarning.clear()
        self._counterOverallPollDurationError.clear()
        self._counterPollError.clear()
        self._counterMissedPolls.clear()
        self._counterTotalPollSeconds.clear()
        self._activeAlarms.clearCountRaisedAlarms()
        self._elapsorEnabledRunTime.clear()
        self._logConfiguration("action-clear-counters").debug1("counters cleared.")
        return (ReturnCodes.kOk, None)

    ######################
    # GETTERS
    ######################

    # TODO(shmulika): self-review: notice that getting the datas seperately means they might be inconsistent.
    # this maybe makes a different when considering poll interval which is referenced by both data (but only a weak connection between the references)
    # don't think I want to change it right now for that....

    def getRunningThresholdsData (self):
        """ Returns a copy of the running (configured) ThresholdsData """
        copyThresholdsData = ThresholdsData()
        with self._configurationLock:            
            copyThresholdsData.copyFrom(self._runningThresholds)
        self._logConfiguration("get-running-threshold-data").debug3("returned a copy of running threshold data=%s", copyThresholdsData)
        return copyThresholdsData


    def getRunningAlarmsData (self):
        """ Returns a copy of the running (configured) AlarmsData """
        copyAlarmsData = AlarmsData()
        with self._configurationLock:            
            copyAlarmsData.copyFrom(self._runningSettings)
        self._logConfiguration("get-running-alarms-data").debug3("returned a copy of running alarms data=%s", copyAlarmsData)
        return copyAlarmsData


    def _getConfiguredSimulatedAlarms (self):
        """ Returns a copy of the configured list of SimulatedAlarms
        Notice: the list is a copy, but the contained 
        """
        with self._configurationLock:            
            simulatedAlarms = self._runningSimulateList.getCopySimulatedDatas()
        self._logConfiguration("get-configured-simulated-alarms").debug3("returned a copy of configured simulated alarms list=%s", simulatedAlarms)
        return simulatedAlarms

    ######################
    # TRANSACTION
    ######################

    def configStartTransaction (self):
        self._logConfiguration("config-start-transaction").debug2("configuration transaction started")
        self._configResetCandidates()
        self._candidateSettings.copyFrom(self._runningSettings)
        self._candidateThresholds.copyFrom(self._runningThresholds)        
        self._candidateSimulateList.copyFrom(self._runningSimulateList)
        return ReturnCodes.kOk


    def preparePrivateAlarmData (self, blinkyAlarmData):        
        self._logConfiguration("prepare-private-alarm-data").debug2("got candidate alarm data = %s", blinkyAlarmData)
        self._copySetAlarmDataToFrom(self._candidateSettings, blinkyAlarmData)
        self._changedSettings.copyFrom(blinkyAlarmData)
        return ReturnCodes.kOk


    def preparePrivateThresholdsData (self, blinkyThresholdsData):
        self._logConfiguration("prepare-private-thresholds-data").debug2("got candidate alarm data = %s", blinkyThresholdsData)
        self._copySetThresholdsDataToFrom(self._candidateThresholds, blinkyThresholdsData)
        self._changedThresholds.copyFrom(blinkyThresholdsData)
        return ReturnCodes.kOk

    
    def preparePrivateSimulateListCreate(self, listKey):
        self._logConfiguration("prepare-private-simulate-list-create").debug2("create simulate, listKey = %s", listKey)
        if self._candidateSimulateList.hasSimulated(listKey):
            self._configErrorMsgFunctor("simulate already contains element with key %s"%listKey)
            return ReturnCodes.kGeneralError 
        # note: the element itself will be inserted in call to method preparePrivateSimulateData
        # note: I could have remembered the key, and make sure the data is created later on, but I simply trust blinky/confd on this
        #       anyway, nothing really bad happens if key was created here and data not inserted, or vice-versa
        return ReturnCodes.kOk
        

    def preparePrivateSimulateListDelete(self, listKey):
        self._logConfiguration("prepare-private-simulate-list-delete").debug2("delete simulate, listKey = %s", listKey)
        if not self._candidateSimulateList.hasSimulated(listKey):
            self._configErrorMsgFunctor("simulate does not contain element with key %s"%listKey)
            return ReturnCodes.kGeneralError 
        self._candidateSimulateList.removeSimulated(listKey)
        return ReturnCodes.kOk

    def preparePrivateSimulateData(self, listKey, simulateData):
        self._logConfiguration("prepare-private-simulate-data").debug2("got candidate simulate, listKey=%s, data=%s", listKey, simulateData)
        # note: this call will either insert a new key-data, or update an existing key-data
        # note: deleted elements are not called with this method, so they're not "re-inserted" by mistake
        self._candidateSimulateList.insertUpdateSimulated(listKey, simulateData)
        return ReturnCodes.kOk


    def configAbortTransaction (self):
        self._logConfiguration("config-abort-transaction").debug2("configuration transaction aborted")
        self._configResetCandidates()
        return ReturnCodes.kOk


    def configPreparePrivateAfter (self):
        self._logConfiguration("config-prepare-private-after").debug2("checking configuration validity")                
        
        rc, errMessage = self._checkCandidateAlarmData()
        if rc != ReturnCodes.kOk:
            self._configErrorMsgFunctor(errMessage)
            self._logConfiguration("config-prepare-private-after-error-alarm-data").error("candidate alarm data invalid: %s", errMessage)                
            return ReturnCodes.kGeneralError         
               
        rc, errMessage = self._checkCandidateThresholdsData()
        if rc != ReturnCodes.kOk:
            self._configErrorMsgFunctor(errMessage)
            self._logConfiguration("config-prepare-private-after-error-thresholds-data").error("candidate thresholds data invalid: %s", errMessage)                
            return ReturnCodes.kGeneralError         

        rc, errMessage = self._checkCandidateSimulateList()
        if rc != ReturnCodes.kOk:
            self._configErrorMsgFunctor(errMessage)
            self._logConfiguration("config-prepare-private-after-error-simulate-list").error("candidate simulate list invalid: %s", errMessage)                
            return ReturnCodes.kGeneralError         

        self._logConfiguration("config-prepare-private-after-done").debug1("candidate configuration is valid")                
        return ReturnCodes.kOk


    def configPreparePublicAfter (self):
        self._logConfiguration("config-prepare-public-after").debug2("doing nothing - already checked data in private")       
        return ReturnCodes.kOk


    def configCommitTransaction (self):
        self._logConfiguration("config-commit-transaction").debug2("configuration transaction commited")

        with self._configurationLock:            
            self._copySetAlarmDataToFrom(self._runningSettings, self._candidateSettings)
            self._copySetThresholdsDataToFrom(self._runningThresholds, self._candidateThresholds)
            self._runningSimulateList.copyFrom(self._candidateSimulateList)
            self._applyChangedConfiguration()
            self._configResetCandidates()

        self._wasConfigured = True
        return ReturnCodes.kOk

    ######################
    # CHECKERS
    ######################

    def _checkCandidateSimulateList (self):
        for key, simulateData in self._candidateSimulateList.getKeysAndSimulateDatas():
            rc, errMessage = self._checkSimulateData(simulateData)
            if rc != ReturnCodes.kOk:
                return (ReturnCodes.kGeneralError, errMessage%({"key" : key}))

        rc, errMessage = self._candidateSimulateList.checkDuplicatedSimulated()
        if rc != ReturnCodes.kOk:
            return (ReturnCodes.kGeneralError, "simulate contains duplicated elements (%s)"%errMessage)

        return (ReturnCodes.kOk, None)


    def _checkSimulateData (self, simulateData):
        if not simulateData.hasId():
            return (ReturnCodes.kGeneralError, "%(key)s has no id") 

        if not simulateData.hasName():
            return (ReturnCodes.kGeneralError, "%(key)s was not given a name") 

        if not simulateData.hasEntity():
            return (ReturnCodes.kGeneralError, "%(key)s was not given an entity") 

        if not self._isRegisteredAlarm(simulateData.name):
            return (ReturnCodes.kGeneralError, "%(key)s's" + " name is %s, which is not a registered alarm"%simulateData.name) 

        if simulateData.entity == "":
            return (ReturnCodes.kGeneralError, "%(key)s's entity is the empty-string, which is invalid") 

        if ''.join(simulateData.entity.split()) != simulateData.entity:
            return (ReturnCodes.kGeneralError, "%(key)s's entity contains whitespaces, which is invalid") 

        return (ReturnCodes.kOk, None)


    def _checkCandidateAlarmData (self):
        """ Checks the validity of the candidate AlarmData """
        if self._candidateSettings.pollInterval <= 0:
            return (ReturnCodes.kGeneralError, "poll-interval must be a positive value")

        return (ReturnCodes.kOk, None)

    
    def _checkCandidateThresholdsData (self):
        """Checks the validity of the candidate ThresholdsData """
        rc, errMessage = self._checkThresholdWarningErrorValues(self._candidateThresholds.pollLatencyWarningSeconds, self._candidateThresholds.pollLatencyErrorSeconds)
        if rc != ReturnCodes.kOk:
            return (ReturnCodes.kGeneralError, errMessage%({"errorThreshold" : "poll-latency-error-seconds", "warningThreshold" : "poll-latency-warning-seconds"}))

        rc, errMessage = self._checkThresholdWarningErrorValues(self._candidateThresholds.singlePollDurationWarningMsec, self._candidateThresholds.singlePollDurationErrorMsec)
        if rc != ReturnCodes.kOk:
            return (ReturnCodes.kGeneralError, errMessage%({"errorThreshold" : "single-poll-duration-error-msec", "warningThreshold" : "single-poll-duration-warning-msec"}))

        rc, errMessage = self._checkThresholdWarningErrorValues(self._candidateThresholds.overallPollDurationWarningMsec, self._candidateThresholds.overallPollDurationErrorMsec)
        if rc != ReturnCodes.kOk:
            return (ReturnCodes.kGeneralError, errMessage%({"errorThreshold" : "overall-poll-duration-error-msec", "warningThreshold" : "overall-poll-duration-warning-msec"}))

        return (ReturnCodes.kOk, None)


    def _checkThresholdWarningErrorValues (self, warningValue, errorValue):
        """ Checks warning-error thresholds pair validity """
        rc, errMessage = self._checkThresholdValue(warningValue)
        if rc != ReturnCodes.kOk:
            return (ReturnCodes.kGeneralError, errMessage%({"value" : "%(warningThreshold)s"}))

        rc, errMessage = self._checkThresholdValue(errorValue)
        if rc != ReturnCodes.kOk:
            return (ReturnCodes.kGeneralError, errMessage%({"value" : "%(errorThreshold)s"}))

        if warningValue > errorValue:
            return (ReturnCodes.kGeneralError, "%(warningThreshold)s must be smaller than or equal to %(errorThreshold)s")            

        return (ReturnCodes.kOk, None)


    def _checkThresholdValue (self, thresholdValue):
        if thresholdValue < 0:
            return (ReturnCodes.kGeneralError, "%(value)s must be a non-negative value")

        return (ReturnCodes.kOk, None)

    ######################
    # APPLIERS
    ######################

    def _applyChangedConfiguration (self):
        """ applies changed configurations that have immedaite effect on behavior """
        if self._changedSettings.hasPollInterval():
            self._applyPollIntervalConfiguration()


    def _applyPollIntervalConfiguration (self):
        # TODO(shmulika): _shouldResetPollTimer is the result of not having "unset" method in BlinkyData.
        #   This is a configuration that can update itself only a-priori (not immediately), and not all values change immediately
        #   This method is responsible for updating the poll-intervalp; it uses _shouldResetPollTimer, but it should have used a BlinkyData called
        #   changedRunningSettings; and if it has a value for pollInterval, only then should this method reset the timer, and then "unset" the pollInterval value
        #   thus signalling to itself, that the change has already been taken care of....
        self._shouldResetPollTimer = True        

    ######################
    # UTILS
    ######################

    # TODO(shmulika): replace all this terrible code with blinkyData.copySetFrom() when availabe at Blinky framework
    def _copySetAlarmDataToFrom (self, dest, source):
        if source.hasEnabled():
            dest.enabled = source.enabled
            dest.setHasEnabled()

        if source.hasPollInterval():
            dest.pollInterval = source.pollInterval
            dest.setHasPollInterval()

        if source.hasRaiseTestAlarm():
            dest.raiseTestAlarm = source.raiseTestAlarm
            dest.setHasRaiseTestAlarm()


    # TODO(shmulika): replace all this terrible code with blinkyData.copySetFrom() when availabe at Blinky framework
    def _copySetThresholdsDataToFrom (self, dest, source):
        if source.hasPollLatencyWarningSeconds():
            dest.pollLatencyWarningSeconds = source.pollLatencyWarningSeconds
            dest.setHasPollLatencyWarningSeconds()

        if source.hasPollLatencyErrorSeconds():
            dest.pollLatencyErrorSeconds = source.pollLatencyErrorSeconds
            dest.setHasPollLatencyErrorSeconds()

        if source.hasSinglePollDurationWarningMsec():
            dest.singlePollDurationWarningMsec = source.singlePollDurationWarningMsec
            dest.setHasSinglePollDurationWarningMsec()

        if source.hasSinglePollDurationErrorMsec():
            dest.singlePollDurationErrorMsec = source.singlePollDurationErrorMsec
            dest.setHasSinglePollDurationErrorMsec()

        if source.hasOverallPollDurationWarningMsec():
            dest.overallPollDurationWarningMsec = source.overallPollDurationWarningMsec
            dest.setHasOverallPollDurationWarningMsec()

        if source.hasOverallPollDurationErrorMsec():
            dest.overallPollDurationErrorMsec = source.overallPollDurationErrorMsec
            dest.setHasOverallPollDurationErrorMsec()


    def _configResetCandidates (self):
        self._logConfiguration("config-reset-candidates").debug3("resetting candidate variables")
        self._candidateSettings = AlarmsData()
        self._candidateThresholds = ThresholdsData()
        self._changedSettings = AlarmsData()
        self._changedThresholds = ThresholdsData()        

###############################################################
# ACTIVE ALARMS - MAIN LOGIC
###############################################################

    def _getCopyActiveAlarms (self):
        """ gets a copy of the active alarms list """
        with self._activeAlarmsLock:
            copyAlarms = self._activeAlarms.getCopyOfAlarms()        
        return copyAlarms


    def _checkAllAlarmsWereSimulated (self, configuredSimulatedAlarms):
        """ Checks that all the simulated alarms are actually in the table.
        Reports an error if not, and updates relevant counter
        """   
        self._logAlarms("check-all-alarms-were-simulated").debug3("checking that all simulated alarms were actually simulated")     

        for simulatedAlarm in configuredSimulatedAlarms:
            if not self._activeAlarms.hasAlarm(name = simulatedAlarm.name, entity = simulatedAlarm.entity, simulated = True):
                self._logAlarms("alarm-not-simulated").error("simulated alarm was not actually simulated. simulated-alarm-data = %s", simulatedAlarm)     
                self._counterAlarmNotSimulated.increment()

    
    def _updateActiveAlarms (self, alarms):
        """ updates the active alarms list """        
        with self._activeAlarmsLock:
            self._activeAlarms.updateFromList(alarms)
            self._logAlarms("update-active-alarms").debug2("updated the active alarms list")
            
        

    def _createAlarmDataFromAlarmInfo (self, alarmInfo):        
        """ Creates an AlarmData object from the given AlarmInfo object (according to appropriate registered alarm) """
        registeredAlarm = self._getRegisteredAlarm(alarmInfo.name)
        if registeredAlarm is None:
            self._logAlarms("create-alarm-data-from-alarm-info-not-registered").error("an alarm was issued (name=%s), but no appropriate alarm was registered in api", alarmInfo.name)
            return None

        alarmData = ListOperData()
        # setting the requested fields for logging, so str(alarmData) will contain all the fields
        alarmData.setNameRequested()
        alarmData.setEntityRequested()
        alarmData.setSeverityRequested()
        alarmData.setSimulatedRequested()
        alarmData.setSourceRequested()
        alarmData.setDescriptionRequested()
        
        alarmData.setName(alarmInfo.name)
        alarmData.setEntity(alarmInfo.entity)        
        alarmData.setSimulated(alarmInfo.simulated)
        alarmData.setSource(alarmInfo.source)
        alarmData.setSeverity(registeredAlarm.severity)

        # description needs to be parsed, because entity name should be placed inside it.        
        try:
            # TODO(shmulika): keeping the description pattern in separate hash is ugly, consider creating a wrapper to the registeredAlarm object containing both RegisteredData and descriptionPattern 
            descriptionPattern = a.api.alarms.alarm.alarm_base.RegisteredAlarms.s_getRegisteredAlarmDescriptionPattern(alarmInfo.name)
            alarmData.setDescription(descriptionPattern % ({a.api.alarms.alarm.alarm_base.ENTITY_KEY_STRING : alarmData.entity}))            
        except:  
            alarmData.setDescription(registeredAlarm.description)          
            self._logAlarms("create-alarm-data-from-alarm-info-fail-formatting").warning("failed formatting the alarm's description field. alarmData=%s, registeredAlarm=%s", alarmData, registeredAlarm)    
        
        self._logAlarms("create-alarm-data-from-alarm-info").debug3("created alarm data from alarm info. alarmInfo=%s, alarmData=%s, registeredAlarm=%s", alarmInfo, alarmData, registeredAlarm)    
        return alarmData


    def _createAlarmDataListFromAlarmInfoList (self, alarmInfos):
        """ Creates the alarm datas from the alarm infos, and returns as a list """
        alarmDatas = []
        for alarmInfo in alarmInfos:
            alarmData = self._createAlarmDataFromAlarmInfo(alarmInfo)
            if alarmData is not None:
                alarmDatas.append(alarmData)
        return alarmDatas


    def _checkAlarmsFromSourceAreSupportedAndRegistered (self, alarmInfos, alarmSource):
        """ Checks that all the alarms info from a source are supported by it and are registered; if not - log an error"""
        alarmSourceName = alarmSource.getInstanceName()
        for alarmInfo in alarmInfos:
            if not alarmSource.isSupportedAlarmName(alarmInfo.name):
                self._logAlarms("check-alarms-from-source-not-supported").error("source %s returned alarm=%s, but it does not support it", alarmSourceName, alarmInfo.name)

            if not self._isRegisteredAlarm(alarmInfo.name):
                self._logAlarms("check-alarms-from-source-not-registered").error("source %s returned alarm=%s, but it was not registered", alarmSourceName, alarmInfo.name)


    def _pollActiveAlarmsFromSources (self, configuredSimulatedAlarms):
        """ Goes through all AlarmSources and get the currently active alarms from them """        
        activeAlarmInfos = []
        runningThresholds = self.getRunningThresholdsData() # get all thresholds once, so they will all be consistent

        self._timeoutOverallPollDuration.set()        
        for alarmSource in self._alarmSources:
            alarmSourceName = alarmSource.getInstanceName()
            try:
                self._timeoutSinglePollDuration.set()
                self._logSources("refresh-alarms-call-source").debug2("polling active alarms from alarm source %s", alarmSourceName)
                alarmInfosFromSource = alarmSource.pollActiveAlarms(configuredSimulatedAlarms)
                self._logSources("refresh-alarms-return-source").debug2("polled active alarms from alarm source %s, after %s msecs", alarmSourceName, self._timeoutSinglePollDuration.getElapsedMsecs())
                self._logSources("refresh-alarms-alarms-from-source").debug3("source %s returned these alarms=%s", alarmSourceName, activeAlarmInfos)

                # TODO(shmulika): self-review: "unfair" to alarm-source to put this next check inside the timeout, but o.w. code will be uglier - aesthetics wins this for me
                # TODO(shmulika): ask gaash if should show unsupported or unregistered alarms...
                # TODO(shmulika): self-review: anyway might want to return check result for future implementation
                self._checkAlarmsFromSourceAreSupportedAndRegistered(alarmInfosFromSource, alarmSource)
                activeAlarmInfos.extend(alarmInfosFromSource)
                
            except AlarmSourceError:
                self._logSources("refresh-alarms-source-error").error("error polling active alarms from alarm-source", exc_info = 1)
                self._counterPollError.increment()
            finally:
                # check the single-poll duration
                elapsedMsec = self._timeoutSinglePollDuration.getElapsedMsecs()                
                self._counterTotalPollSeconds.incrementBy(self._timeoutSinglePollDuration.getElapsedSeconds())
                self._logSources("single-poll-duration").debug2("polling alarm source %s for active alarms took %s msec", alarmSourceName, elapsedMsec)
                if self._hasPassedThreshold(elapsedMsec, runningThresholds.singlePollDurationErrorMsec):
                    self._logSources("single-poll-duration-error").error("polling alarm source %s for active alarms took %s msec, passed error threshold %s", alarmSourceName, elapsedMsec, runningThresholds.singlePollDurationErrorMsec)
                    self._counterSinglePollDurationError.increment()
                elif self._hasPassedThreshold(elapsedMsec, runningThresholds.singlePollDurationWarningMsec):
                    self._logSources("single-poll-duration-warning").warning("polling alarm source %s for active alarms took %s msec, passed warning threshold %s", alarmSourceName, elapsedMsec, runningThresholds.singlePollDurationWarningMsec)
                    self._counterSinglePollDurationWarning.increment()

        # TODO(shmulika): self-review: all this elapsed-time checking is pretty repititive, could be nice to do it with a "with" clause        
        # check the overall-poll duration
        elapsedMsec = self._timeoutOverallPollDuration.getElapsedMsecs()        
        self._logSources("overall-poll-duration").debug2("overall polling took %s msec", elapsedMsec)        
        if self._hasPassedThreshold(elapsedMsec, runningThresholds.overallPollDurationErrorMsec):
            self._logSources("overall-poll-duration-error").error("overall polling took %s msec, passed error threshold %s", elapsedMsec, runningThresholds.overallPollDurationErrorMsec)
            self._counterOverallPollDurationError.increment()
        elif self._hasPassedThreshold(elapsedMsec, runningThresholds.overallPollDurationWarningMsec):
            self._logSources("overall-poll-duration-warning").warning("overall polling took %s msec, passed warning threshold", elapsedMsec, runningThresholds.overallPollDurationWarningMsec)
            self._counterOverallPollDurationWarning.increment()

        return activeAlarmInfos

        
    def _repollAlarms (self):
        """ Repoll all the alarm sources and update the alarm table """
        self._logAlarms("refresh-alarms").debug2("refreshing alarms-table")        
        configuredSimulatedAlarms = self._getConfiguredSimulatedAlarms()
        activeAlarmInfos = self._pollActiveAlarmsFromSources(configuredSimulatedAlarms)
        activeAlarmDatas = self._createAlarmDataListFromAlarmInfoList(activeAlarmInfos)
        self._updateActiveAlarms(activeAlarmDatas)
        self._checkAllAlarmsWereSimulated(configuredSimulatedAlarms)
        self._counterPolls.increment()
        self._logAlarms("refresh-alarms-done").debug2("done refreshing alarms")


    def _clearAlarms (self):
        """ Clears all alarms from the alarm table """
        self._logAlarms("clear-alarms").debug2("clearing alarms")
        self._updateActiveAlarms([]) # simply update with "no alarms" to clear the table


    def _refreshAlarms (self):
        """ Refresh the alarms table (either re-poll the alarms sources if enabled, or clear if disabled) """
        # refresh the alarms table, if the alarms are enabled
        runningSettings = self.getRunningAlarmsData()
        if runningSettings.enabled:
            self._elapsorEnabledRunTime.resume()
            self._repollAlarms()

        # if alarms are disabled - clear the alarms table (even immediately after 
        # refresh incase configuration changed in the middle - that's why not an "elif", and why we get the settings again)
        # notice: we're always clearing alarms-table if disabled (not only on change) - this simplifies logic of understanding the change at relatively low performance cost (KISS)
        runningSettings = self.getRunningAlarmsData()
        if not runningSettings.enabled:
            self._elapsorEnabledRunTime.pause()
            self._clearAlarms()


###############################################################
# PROCESS
###############################################################

    def _checkShouldResetPollTimer (self):
        """ check if the poll timer should be resetted (at start of process, or due to configuration change at run-time)"""
        runningSettings = self.getRunningAlarmsData()        

        # TODO(shmulika): _shouldResetPollTimer is the result of not having "unset" method in BlinkyData.
        #   This is a configuration that can update itself only a-priori (not immediately), and not all values change immediately
        #   This method is responsible for updating the poll-intervalp; it uses _shouldResetPollTimer, but it should have used a BlinkyData called
        #   changedRunningSettings; and if it has a value for pollInterval, only then should this method reset the timer, and then "unset" the pollInterval value
        #   thus signalling to itself, that the change has already been taken care of....
        if self._shouldResetPollTimer:
            self._pollTimer = a.infra.time.elapsed_timer.ElapsedTimer(self._logProcess)
            self._pollTimer.initInterval(self._pollTimer.secondsToNanos(runningSettings.pollInterval))
            self._pollTimer.initRecurrence(isDriftless = True)
            self._pollTimer.start()
            self._shouldResetPollTimer = False

                    
    def _checkPollTimeoutAndRefreshAlarms (self):
        """ Check the refresh timeout - if it has expired (or not yet set) - it will refresh the alarms table and set the timeout for next time.
        """            
        self._checkShouldResetPollTimer() # poll timer might need reset (first run or change in configuration)

        # TODO(shmulika): self-review: might want to reverse the order - refresh first, then sleep.
        # sleep till next time to poll
        countIntervals, passedSeconds = self._pollTimer.sleepTillElapsedCountAndSeconds()        
        if countIntervals > 1:
            missedPolls = countIntervals - 1
            # TODO(shmulika): self-review: to nirs/gaash, maybe this should be notice?
            self._logProcess("missed-polls").debug1("missed %s polls during sleep between alarm table refreshes", missedPolls)
            self._counterMissedPolls.incrementBy(missedPolls)

        runningThresholds = self.getRunningThresholdsData()                                
        if self._hasPassedThreshold(passedSeconds, runningThresholds.pollLatencyErrorSeconds):
            self._logProcess("poll-latency-error").error("poll was delayed too much (slept too long), over %s seconds elapsed since last alarms-table refresh", passedSeconds)
            self._counterPollLatencyError.increment()
        elif self._hasPassedThreshold(passedSeconds, runningThresholds.pollLatencyWarningSeconds):
            self._logProcess("poll-latency-warning").warning("poll was delayed too much (slept too long), over %s seconds elapsed since last alarms-table refresh", passedSeconds)
            self._counterPollLatencyWarning.increment()

        self._refreshAlarms()


    def launch (self):
        """ Called by the Application to launch the alarm manager """
        self._logProcess("launch-go").debug1("alarm-manager was launched")

        self._waitForInitialConfigration()

        while not self._wasStopped:            
            self._checkPollTimeoutAndRefreshAlarms()

        self._logProcess("launch-stop").debug1("alarm-manager has stopped")


    def stop (self):
        """ Called by the Application to stop the alarm manager """
        self._logProcess("stop").debug1("alarm-manager asked to be stopped")
        self._wasStopped = True


    # TODO(shmulika): maybe Nirs does this for me in oscar; ask him...
    def _waitForInitialConfigration (self):
        """ Wait for the initial configuration to be done before running the process
        Running the process without configuration is a bad idea...
        """
        if self._wasConfigured:
            self._logProcess("wait-for-initial-configuration-already-configured").debug1("no need to wait. process is already configured")
            return

        self._logProcess("wait-for-initial-configuration-waiting").debug1("waiting for the initial configuration of the process to take place")
        while not self._wasConfigured:
            time.sleep(AlarmManager.SLEEP_INTERVAL_SECONDS_WAIT_FOR_CONFIGURATION)

        self._logProcess("wait-for-initial-configuration-done").debug1("initial configuration of the process was made")

###############################################################
# UTILITIES
###############################################################
    
    def _hasPassedThreshold (self, value, threshold):
        return value > threshold and threshold > 0

            
###############################################################
# INTERNAL CLASSES
###############################################################

#TODO(shmulika): this commented implementation is better, and more generic for operList;
# replace it someday, when there's time - or for my next operList somewhere...
#
#class _OperList:
#    """ This implements a general oper list
#    """
#    ERR_MESSAGE_INVALID_REQUESTED = "error while retrieving list"
#    ERR_MESSAGE_LIST_CHANGED      = "error while retrieving list, try again soon"
#
#    DEFAULT_INTERVAL_SECONDS_REFRESH_FROM_LAST_GET = 2
#
#    INDEX_KEY_FIRST   = -1
#    INDEX_KEY_NO_MORE = -2
#
#    def __init__ (self, logger, intervalRefreshSinceLastGet = DEFAULT_INTERVAL_SECONDS_REFRESH_FROM_LAST_GET):
#        self._log = logger.createLoggerSameModule(G_GROUP_NAME_OMREPORT_OPER_LIST)
#        self.intervalRefreshSinceLastGet = intervalRefreshSinceLastGet
#
#        self.lastRefreshTime = _TimeElapsor(self._log)
#        self.lastGetTime     = _TimeElapsor(self._log)
#
#        self._defaultIndexKeyToObject       = {}        
#        self._defaultIndexKeyToNextIndexKey = {}        
#
#        self._dictionaryObjectToObjectKey = {}
#        self._dictionaryObjectKeyToObject = {}
#
#        self.updatedList = None
#        self.runningList = None
#
#        self.wasRefreshedDuringGets = False
#    
#
#    def objectToObjectKey (self, anObject):
#        """ Needs to implemented by specific extension class """
#        __pychecker__ = "unusednames=anObject"
#        return None
#
#
#    def update (self, orderedList):
#        """ Updates the list.
#        Notice that the "gotten oper list" is not immediately changed, but only after the fixed time interval has passed since last get oper 
#
#        Arguments:
#            orderedList - list that will be gotten by the oper list, in desired order of elements.
#        Returns: None
#        Raises: None 
#        """
#        self._log("update").debug2("updating the list to %s (might take some time before applied to oper gets operations)", orderedList)
#        self.updatedList = orderedList
#
#
#    def _refresh (self):
#        if self.updatedList is None:
#            self._log("refresh-no-update").debug3("no updated list")
#            return
#
#        self._log("refresh").debug3("refreshing running list (was=%s) with updated list (is=%s)", self.runningList, self.updatedList)        
#        self.runningList = self.updatedList
#        self.updatedList = None
#        self.wasRefreshedDuringGets = True
#        self._createKeyHashes()
#
#
#    def _checkRefreshFromUpdateList (self):
#        if not self.lastGetTime.wasSet() or self.lastGetTime.getElapsedSeconds() > self.intervalRefreshSinceLastGet:
#            self._log("check-refresh-from-update-list-refreshing").debug2("more than %s seconds elapsed since last oper get. refreshing.", self.intervalRefreshSinceLastGet)
#            self._refresh()
#        else:
#            self._log("check-refresh-from-update-list-not-refrehing").debug2("less than %s seconds elapsed since last oper get. not refreshing.", self.intervalRefreshSinceLastGet)
#
#        self.lastGetTime.set()
#
#
#    def getNext (self, dpTrxContext, key, nextKey, isCompleted):
#        self._log("get-next-called").debug3("get-next called with dpTrxContext=%s, key=%s, nextKey=%s, isCompleted=%s", dpTrxContext, key, nextKey, isCompleted)        
#        self._checkRefreshFromUpdateList()
#
#        indexKeyValue = nextKey.value()            
#        if not self._hasIndexKeyToObject(indexKeyValue):
#            self._log("get-next-don't-have-key").error("oper get-next requested unrecognized key-index=%s", indexKeyValue)
#            return (ReturnCodes.kGeneralError, _OperList.ERR_MESSAGE_INVALID_REQUESTED)
#
#        if indexKeyValue == _OperList.INDEX_KEY_FIRST:
#            self._log("get-next-first-key").debug3("get next completed with last key-index=%s", indexKeyValue)
#            self.wasRefreshedDuringGets = False
#
#        anObject = self._indexKeyToObject(indexKeyValue)
#        if anObject is None:
#            self._log("get-next-completed").debug3("get next completed with last key-index=%s", indexKeyValue)
#            isCompleted.setValue(True)
#            return (ReturnCodes.kOk, None)
#
#        if not self._hasIndexKeyToNextIndexKey(indexKeyValue):
#            self._log("get-next-no-next-key").debug1("can't find next-key-index for key-index=%s, list probably changed between get-next calls", indexKeyValue)
#            return (ReturnCodes.kGeneralError, _OperList.ERR_MESSAGE_LIST_CHANGED)
#        
#        isCompleted.setValue(False)
#        key.setValue(self._objectToObjectKey(anObject))
#        nextKey.setValue(self._indexKeyToNextIndexKey(indexKeyValue))
#        self._log("get-next-success").debug3("get-next set values key=%s, nextKey=%s", key, nextKey)
#        return (ReturnCodes.kOk, None)
#
#
#    def getObj (self, dpTrxContext, key, operData):
#        self._log("get-obj-called").debug3("called with (dpTrxContext = %s, key = %s, operData = %s)", dpTrxContext, key, operData)        
#        self._checkRefreshFromUpdateList()
#
#        if not self._hasObjectKeyToObject(key):
#            self._log("get-obj-number-not-in-hash").debug1("requested object key=%s is not found, list probably changed between get-obj calls", key)
#            print "here: ", key, self._dictionaryObjectKeyToObject, self._dictionaryObjectKeyToObject[key]
#            return (ReturnCodes.kGeneralError, _OperList.ERR_MESSAGE_LIST_CHANGED)
#    
#        anObject = self._objectKeyToObject(key)
#        operData.copyFrom(anObject)
#
#        self._log("get-obj-done").debug3("done with (dpTrxContext = %s, key = %s, operData = %s)", dpTrxContext, key, operData)
#        return (ReturnCodes.kOk, None)
#
#    ###############################
#    # UTILITY FOR MAKING THE HASHES 
#    ###############################
#
#    def _listOfIndexKeys (self):
#        if len(self.runningList) == 0:
#            return [_OperList.INDEX_KEY_FIRST]
#
#        listIndexKey = [_OperList.INDEX_KEY_FIRST]        
#        listIndexKey.extend(range(len(self.runningList) - 1))
#        listIndexKey.append(_OperList.INDEX_KEY_NO_MORE)
#
#        return listIndexKey
#
#    def _listOfObjects (self):
#        listObjects = self.runningList[:]
#        listObjects.append(None)
#
#        return listObjects
#
#    def _listOfNextIndexKeys (self):
#        if len(self.runningList) == 0:
#            return []
#
#        listNextIndexKey = range(len(self.runningList) - 1)
#        listNextIndexKey.append(_OperList.INDEX_KEY_NO_MORE)
#        return listNextIndexKey
#
#    def _createKeyHashes (self):
#        self._defaultIndexKeyToObject       = {}        
#        self._defaultIndexKeyToNextIndexKey = {}        
#
#        self._dictionaryObjectToObjectKey = {}
#        self._dictionaryObjectKeyToObject = {}
#        
#        listIndexKeys = self._listOfIndexKeys()
#        for indexKey, anObject in zip(listIndexKeys, self._listOfObjects()):
#            self._defaultIndexKeyToObject[indexKey] = anObject
#
#        for indexKey, nextIndexKey in zip(listIndexKeys[:-1], self._listOfNextIndexKeys()):
#            self._defaultIndexKeyToNextIndexKey[indexKey] = nextIndexKey
#
#        for anObject in self.runningList:
#            objectKey = self.objectToObjectKey(anObject)
#            self._dictionaryObjectToObjectKey[anObject] = objectKey
#            self._dictionaryObjectKeyToObject[objectKey] = anObject
#
#
#    def _hasIndexKeyToObject (self, indexKey):
#        return indexKey in self._defaultIndexKeyToObject    
#
#    def _indexKeyToObject (self, indexKey):
#        return self._defaultIndexKeyToObject[indexKey]
#
#
#    def _hasIndexKeyToNextIndexKey (self, indexKey):
#        return indexKey in self._defaultIndexKeyToNextIndexKey
#
#    def _indexKeyToNextIndexKey (self, indexKey):
#        return self._defaultIndexKeyToNextIndexKey[indexKey]
#
#
#    def _hasObjectToObjectKey (self, anObject):        
#        return anObject in self._dictionaryObjectToObjectKey
#
#    def _objectToObjectKey (self, anObject):        
#        return self._dictionaryObjectToObjectKey[anObject]
#    
#
#    def _hasObjectKeyToObject (self, objectKey):
#        return objectKey in self._dictionaryObjectKeyToObject
#
#    def _objectKeyToObject (self, objectKey):
#        return self._dictionaryObjectKeyToObject[objectKey]


# TODO(shmulika): discuss with Nirs/gaash if we need to use the alarm.number for nextKey, or just for key
class _AlarmOperList:
    ERR_MESSAGE_LIST_CHANGED = "alarm list was changed during get operations, try again"
    NEXT_KEY_NO_MORE = -2
    NEXT_KEY_FIRST = -1

    def __init__ (self, logger):
        self._log  = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_ALARMS)
        self._changeLock = threading.RLock()

        self.setAlarmsList([]) # init to empty oper list


    def getNext (self, dpTrxContext, key, nextKey, isCompleted):
        self._log("get-next-called").debug3("called with (dpTrxContext = %s, key = %s, nextKey = %s, isCompleted = %s)", dpTrxContext, key, nextKey, isCompleted)
        with self._changeLock:
            # check if it's the first nexy ket blinky is asking for
            isCompleted.setValue(False)
            if nextKey.value() == _AlarmOperList.NEXT_KEY_FIRST:
                self._hookBeforeOperGetNext(first = True)
                currentNextKeyValue = self._firstNextKeyInHash
            else:
                self._hookBeforeOperGetNext(first = False)
                currentNextKeyValue = nextKey.value()
    
            # if we got "next_key_no_more", it means that we've already given the last key the iteration before
            if currentNextKeyValue == _AlarmOperList.NEXT_KEY_NO_MORE:
                isCompleted.setValue(True)
                self._log("get-next-no-more").debug3("no more keys. (dpTrxContext = %s, key = %s, nextKey = %s, isCompleted = %s)", dpTrxContext, key, nextKey, isCompleted)
                return (ReturnCodes.kOk, None)
    
            # if next key is not in hash - something went wrong during the "get transaction", probably table was refreshed during 
            if currentNextKeyValue not in self._nextKeyToAlarmAndNextNextKey:
                self._log("get-next-number-not-in-hash").debug1("requested key is not in hash, list probably changed during the oper operation")
                return (ReturnCodes.kGeneralError, _AlarmOperList.ERR_MESSAGE_LIST_CHANGED)
    
            # set the current key, and the next key (for next iteration)
            currentAlarm, nextNextKeyValue = self._nextKeyToAlarmAndNextNextKey[currentNextKeyValue]        
            key.setValue(self._getObjKeyFromAlarm(currentAlarm))
            nextKey.setValue(nextNextKeyValue)
                
            self._log("get-next-done").debug3("done with (dpTrxContext = %s, key = %s, nextKey = %s, isCompleted = %s)", dpTrxContext, key, nextKey, isCompleted)
            return (ReturnCodes.kOk, None)


    def getObj (self, dpTrxContext, key, operData):
        self._log("get-obj-called").debug3("called with (dpTrxContext = %s, key = %s, operData = %s)", dpTrxContext, key, operData)        

        with self._changeLock:
            self._hookBeforeOperGetObj()

            if key not in self._ObjkeyToAlarm:
                self._log("get-obj-number-not-in-hash").debug1("requested key=%s is not in hash, list probably changed during the oper operation", key)
                return (ReturnCodes.kGeneralError, _AlarmOperList.ERR_MESSAGE_LIST_CHANGED)
    
            alarm = self._ObjkeyToAlarm[key]
            operData.copyFrom(alarm)
    
            self._log("get-obj-done").debug3("done with (dpTrxContext = %s, key = %s, operData = %s)", dpTrxContext, key, operData)
            return (ReturnCodes.kOk, None)


    def setAlarmsList (self, alarms):
        """ This should be called to update the oper list, either by the checkRefreshAlarmList, or external update """
        with self._changeLock:
            self._createNextKeyHash(alarms)
        self._log("refresh-alarm-list").debug3("refreshed oper alarm list = %s", alarms)


    def _createNextKeyHash (self, alarms):
        """ Creates a "next-key" has table, in which each "next-key" entry is translated to the proper alarm, and the next key for the next iteration 
        """
        self._firstNextKeyInHash = _AlarmOperList.NEXT_KEY_NO_MORE
        self._nextKeyToAlarmAndNextNextKey = {}
        self._ObjkeyToAlarm = {}

        lastAlarm = None
        for alarm in alarms:
            self._ObjkeyToAlarm[self._getObjKeyFromAlarm(alarm)] = alarm

            if lastAlarm is not None:
                self._nextKeyToAlarmAndNextNextKey[self._getNextKeyOfAlarm(lastAlarm)] = (lastAlarm, self._getNextKeyOfAlarm(alarm))
            else:
                self._firstNextKeyInHash = self._getNextKeyOfAlarm(alarm)

            lastAlarm = alarm

        if lastAlarm is not None:
            self._nextKeyToAlarmAndNextNextKey[self._getNextKeyOfAlarm(lastAlarm)] = (lastAlarm, _AlarmOperList.NEXT_KEY_NO_MORE)


    def _hookBeforeOperGetObj (self):
        """ This should be overwritten by extension classes for special functionality before oper-get-obj method """
        pass

    def _hookBeforeOperGetNext (self, first):
        """ This should be overwritten by extension classes for special functionality before oper-get-next method
        first is True, when Blinky is asking for the first key in the table (reasonable place to refresh list maybe)
        """
        __pychecker__ = "unusednames=first"
        pass

    def _getObjKeyFromAlarm (self, alarm):
        __pychecker__ = "unusednames=alarm"
        self._log("get-key-from-alarm").error("this function must be implemented by an extension class")
        return None

    def _getNextKeyOfAlarm (self, alarm):
        __pychecker__ = "unusednames=alarm"
        self._log("get-key-from-alarm").error("this function must be implemented by an extension class")
        return None

#-----------------------------------------------------------------------------#
   
class _AlarmOperListList(_AlarmOperList):
    """ The alarm-list (type of oper-list) checks before each oper-get, whether the table has changed in the last refresh interval...
    """
    def __init__ (self, logger, functorGetAlarmsList, functorGetRefreshInterval):
        _AlarmOperList.__init__(self, logger)
        self._log  = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_ALARMS)
        self._afterReset = True        

        self._functorGetAlarmsList = functorGetAlarmsList
        self._refreshTimeout = _Timeout(logger, functorGetRefreshInterval)


    def _hookBeforeOperGetObj (self):
        """ This should be overwritten by extension classes for special functionality before oper-get-obj method """
        self._hookBeforeOperGet()


    def _hookBeforeOperGetNext (self, first):
        """ This should be overwritten by extension classes for special functionality before oper-get-next method
        first is True, when Blinky is asking for the first key in the table (reasonable place to refresh list maybe)
        """
        __pychecker__ = "unusednames=first"
        self._hookBeforeOperGet()


    def _hookBeforeOperGet (self):
        needRefresh = False
        if self._afterReset:
            self._log("check-refresh-alarm-list-after-reset").debug4("we're after list reset. refreshing oper list")
            self._afterReset = False
            needRefresh = True            
        elif self._refreshTimeout.hasFullExpired():
            self._log("check-refresh-alarm-list-timeout").debug4("refresh timeout expired. refreshing oper list")
            needRefresh = True

        if needRefresh:
            self._refreshAlarmList()

        self._refreshTimeout.set()


    def _refreshAlarmList (self):
        self.setAlarmsList(self._functorGetAlarmsList())


    def _getObjKeyFromAlarm (self, alarm):
        return alarm.number

    def _getNextKeyOfAlarm (self, alarm):
        return alarm.number

#-----------------------------------------------------------------------------#

class _AlarmOperListRegistered(_AlarmOperList):
    def __init__ (self, logger):
        _AlarmOperList.__init__(self, logger)
        self._log  = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_ALARMS)
        self._alarmDictionary = {}

    def setAlarmsList (self, alarms):
        nextNumber = 0
        for alarm in alarms:
            self._alarmDictionary[alarm] = nextNumber
            nextNumber = nextNumber + 1

        _AlarmOperList.setAlarmsList(self, alarms)


    def _getObjKeyFromAlarm (self, alarm):
        return alarm.name

    def _getNextKeyOfAlarm (self, alarm):
        return self._alarmDictionary[alarm]        
        
#-----------------------------------------------------------------------------#

class _AlarmTable:
    """ Utility class to maintain an alarm table
    """
    def __init__ (self, logger):
        self._log  = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_ALARMS)
        self._alarmsHash = _AlarmHash(logger)
        self._nextSeqNumber = 0
        self._counterRaisedAlarms = _Counter(logger, "raised-alarms")

    ####################################        
    # FUNCTIONAL MODIFIERS
    ####################################

    def updateFromList (self, alarms):
        self._log("update-from-list").debug3("table is updated from given alarms list. alarms = %s", alarms)
        self.updateFromHash(self._createAlarmHashFromList(alarms))


    def updateFromHash (self, udpatedHash):        
        # keep alarms that are still in the updated table
        alarms = self._alarmsHash.alarmsIn(udpatedHash)
        self._log("update-from-hash-old-alarms").debug3("these alarms are still on from last time - keeping them. alarms = %s", alarms)

        # log about alarms that are removed
        removedAlarms = self._alarmsHash.alarmsNotIn(udpatedHash)
        for removedAlarm in removedAlarms:
            self._log("removed-alarm").notice("an alarm was removed from the alarms table = %s", removedAlarm)

        # add alarms that are new in the updated table
        newAlarms = udpatedHash.alarmsNotIn(self._alarmsHash)
        self._orderListOfAlarms(newAlarms)
        self._log("update-from-hash-new-alarms").debug3("these are new alarms to be added. alarms = %s", alarms)

        for newAlarm in newAlarms:            
            copyNewAlarm = ListOperData()
            copyNewAlarm.copyFrom(newAlarm)
            copyNewAlarm.number = self._nextSeqNumber
            copyNewAlarm.setHasNumber()
            copyNewAlarm.setNumberRequested()
            self._log("update-from-hash-new-alarm").debug4("adding new alarm to table. alarm = %s", copyNewAlarm)
            self._log("new-alarm").notice("new alarm added to the alarms table = %s", copyNewAlarm)
            self._nextSeqNumber = self._nextSeqNumber + 1
            self._counterRaisedAlarms.increment()
            alarms.append(copyNewAlarm)
        
        self._log("update-from-hash-alarms").debug3("updating hash with these alarms = %s", alarms)        
        self._alarmsHash = self._createAlarmHashFromList(alarms)


    def _createAlarmHashFromList (self, alarms):
        alarmHash = _AlarmHash(self._log)
        for alarm in alarms:
            alarmHash.insertAlarm(alarm.name, alarm.entity, alarm.simulated, alarm)

        return alarmHash

    ####################################        
    # FUNCTIONAL GETTERS
    ####################################

    def hasAlarm (self, name, entity, simulated):
        return self._alarmsHash.hasAlarm(name, entity, simulated)

    def getAlarm (self, name, entity, simulated):
        return self._alarmsHash.getAlarm(name, entity, simulated)

    def getCopyOfAlarms (self):
        copyAlarms = []
        #for alarm in self._alarmsDictionary.itervalues():
        for alarm in self._alarmsHash.getAllAlarms():
            copyAlarm = ListOperData()
            copyAlarm.copyFrom(alarm)
            copyAlarms.append(copyAlarm)            
            self._orderListOfAlarms(copyAlarms)

        self._log("get-copy-of-alarms").debug5("returning a list of copies of the alarms. alarms = %s", copyAlarms)
        return copyAlarms


    def _orderListOfAlarms (self, alarms):
        alarms.sort(key = lambda alarm: alarm.entity, cmp = compareStringsLexiNumerical)
        alarms.sort(key = lambda alarm: alarm.name)
        alarms.sort(key = lambda alarm: alarm.severity)

    ####################################        
    # OPER GETTERS
    ####################################

    def getCountRaisedAlarms (self):
        return self._counterRaisedAlarms.get()

    ####################################        
    # ACTION
    ####################################

    def clearCountRaisedAlarms (self):
        return self._counterRaisedAlarms.clear()


    def __str__ (self):
        return "{_AlarmTable: (" + self._alarmsHash.__str__() + ")}"        


#-----------------------------------------------------------------------------#

# TODO(shmulika): we might want to take this to infra!!!!
def compareStringsLexiNumerical (a, b):
    """ Returns: positive when a > b, zero when a == b, negative when a < b """
    aSplitted = splitDecimalSubstrings(str(a))
    bSplitted = splitDecimalSubstrings(str(b))
    
    for aSubString, bSubString in zip(aSplitted, bSplitted):
        try:
            aKey = int(aSubString)
            bKey = int(bSubString)            
        except:
            aKey = aSubString
            bKey = bSubString
        finally:
            if aKey > bKey:
                return 1
            if aKey < bKey:
                return -1

    if len(aSplitted) > len(bSplitted):
        return 1

    if len(aSplitted) < len(bSplitted):
        return -1

    return 0
    

def splitDecimalSubstrings (string):
    phase1 = re.sub("(\D)(\d)", "\g<1> \g<2>", string)
    phase2 = re.sub("(\d)(\D)", "\g<1> \g<2>", phase1)
    return phase2.split()


#-----------------------------------------------------------------------------#

class _AlarmHash:
    DELIMITER_ALARM_UNIQUE_ID = "::"

    def __init__ (self, logger):
        self._log  = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_ALARMS)
        self._alarmsDictionary = {}


    def insertAlarm (self, name, entity, simulated, alarmObject):
        """ Inserts a new alarm object into the hash, or replaces an old one with same name and entity
        """
        self._log("insert-alarm").debug4("inserted alarm object under name = %s, entity = %s, simulated = %s; object = %s", name, entity, simulated, alarmObject)
        self._alarmsDictionary[self._createAlarmUniqeId(name, entity, simulated)] = alarmObject


    def hasAlarm (self, name, entity, simulated):
        """ Returns True if hash contains an object with given name & entity
        """
        return self._createAlarmUniqeId(name, entity, simulated) in self._alarmsDictionary


    def getAlarm (self, name, entity, simulated):
        """ Returns the alarm object if exists in dictionary, or None if not """
        if not self.hasAlarm(name, entity, simulated):
            self._log("get-alarm-none").debug4("no alarm object with name = %s, entity = %s", name, entity)
            return None

        alarmObject = self._alarmsDictionary[self._createAlarmUniqeId(name, entity, simulated)]
        self._log("get-alarm").debug4("returning alarm object under name = %s, entity = %s; object = %s", name, entity, alarmObject)
        return alarmObject

    def getAllAlarms (self):
        """ Returns an iterator over all the alarm objects in the hash """
        return self._alarmsDictionary.values()


    def alarmsIn (self, other):
        """ Returns a list of all the alarm objects that are also contained (same name,entity,simulated) in the other hash """
        alarmObjects = []
        for alarmId, alarmObject in self._alarmsDictionary.iteritems():
            if alarmId in other._alarmsDictionary:
                alarmObjects.append(alarmObject)

        return alarmObjects

    def alarmsNotIn (self, other):
        """ Return a list of all the alarm objects that are not contained (same name,entity,simulated) in the other hash """
        alarmObjects = []
        for alarmId, alarmObject in self._alarmsDictionary.iteritems():
            if alarmId not in other._alarmsDictionary:
                alarmObjects.append(alarmObject)

        return alarmObjects


    def _createAlarmUniqeId (self, name, entity, simulated):
        return _AlarmHash.DELIMITER_ALARM_UNIQUE_ID.join([name.getName(), entity, str(simulated)])


    def __str__ (self):
        objectStrings = []
        for alarmId, alarmObject in self._alarmsDictionary.iteritems():
            objectStrings.append(alarmId + " : " + alarmObject.__str__())

        return "{_AlarmHash: (" + ", ".join(objectStrings) + ")}"

#-----------------------------------------------------------------------------#

class _SimulateList:
    """ Utility for holding the list of simulated alarms """

    def __init__ (self, logger):
        self._log  = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_ALARMS)
        self._simulated = {}

    def insertUpdateSimulated (self, key, simulateData):
        if self.hasSimulated(key):
            self._log("update-simulated").debug3("update simulate %s. old_value=%s, new_value=%s", key, self._simulated[key], simulateData)
            self._copySetSimulateDataToFrom(self._simulated[key], simulateData)
        else:
            self._log("insert-simulated").debug3("insert simulate %s. value=%s", key, simulateData)
            self._simulated[key] = simulateData

    def getKeysAndSimulateDatas (self):
        return self._simulated.iteritems()

    def getSimulatedDatas (self):
        """ Returns a copy of the list of simulated alarm (SimulatedData), contained elements are the original - not copied """
        return self._simulated.values()

    def getCopySimulatedDatas (self):
        """ Returns a copy of the list of simulated alarm (SimulatedData), contained elements are also copied """
        copySimualtedDatas = []
        for simulateData in self.getSimulatedDatas():
            copySimulateData = SimulateData()
            copySimulateData.copyFrom(simulateData)
            copySimualtedDatas.append(copySimulateData)

        return copySimualtedDatas


    def removeSimulated (self, key):
        self._log("remove-simulated").debug3("remove simulate %s. value_was=%s", key, self._simulated[key])
        del self._simulated[key]

    def hasSimulated (self, key):
        return key in self._simulated


    def checkDuplicatedSimulated (self):
        alarms = _AlarmHash(self._log)
        for simulateData in self.getSimulatedDatas():
            if alarms.hasAlarm(name = simulateData.name, entity = simulateData.entity, simulated = True):
                self._log("has-duplicated-simulated-true").debug1("simulated list contains duplicated simulated alarms name = %s, entity = %s", simulateData.name, simulateData.entity)
                return (ReturnCodes.kGeneralError, "name = %s, entity = %s"%(simulateData.name, simulateData.entity))
            alarms.insertAlarm(name = simulateData.name, entity = simulateData.entity, simulated = True, alarmObject = simulateData)
        self._log("has-duplicated-simulated-false").debug3("simulated list does not contain duplicated simulated alarms")
        return (ReturnCodes.kOk, None)


    def copyFrom (self, other):
        self._log("copy-from").debug3("copying list=%s", other)
        self._simulated = {}
        for key, simulateData in other._simulated.iteritems():
            copySimulateData = SimulateData()
            copySimulateData.copyFrom(simulateData)
            self._simulated[key] = copySimulateData

    def _copySetSimulateDataToFrom (self, dest, source):
        self._log("copy-set").debug3("from=%s, to=%s", source, dest)
        if source.hasId():
            dest.id = source.id
            dest.setHasId()

        if source.hasEntity():
            dest.entity = source.entity
            dest.setHasEntity()

        if source.hasName():
            dest.name = source.name
            dest.setHasName()

#-----------------------------------------------------------------------------#

class _Counter:
    """ Utility for maintaining a counter
    Note: could have simply be an int, but feels like there would have been code replication
    """

    def __init__ (self, logger, instanceName):
        self._log = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_COUNTERS, instance = instanceName)
        self._value = 0
        self._clearBase = 0
        self._instanceName = instanceName

    def increment (self):
        self._value = self._value + 1
        self._log("counter-increment").debug4("counter %s was incremented to value %s", self._instanceName, self._value)        

    def incrementBy (self, addition):
        self._value = self._value + addition
        self._log("counter-increment").debug4("counter %s was incremented by %s to value %s", self._instanceName, addition, self._value)        

    def get (self):
        value = int(self._value - self._clearBase)
        self._log("counter-get").debug3("returning counter %s value %s", self._instanceName, value)
        return value

    def getUncleared (self):
        value = int(self._value)
        self._log("counter-get").debug3("returning counter %s uncleared value %s", self._instanceName, value)
        return value

    def clear (self):
        self._clearBase = self._value
        self._log("counter-clear").debug2("clearing counter %s, clear-base-value=%s", self._instanceName, self._clearBase)
        
    def __str__ (self):
        return "{counter %s: (value = %s, uncleared-value=%s}"%(self._instanceName, self.get(), self.getUncleared())

#-----------------------------------------------------------------------------#
              
class _TimeElapsor:
    """ Convenient time counter utility, that simply tells you how much time has elapsed since setting it """
    def __init__ (self, logger):
        self._log = logger.createLogger(G_MODULE_NAME_ALARM_MANAGER, G_GROUP_NAME_ALARM_MANAGER_COUNTERS)

        self._startTime = None
        self._pauseTime = None
        self._totalPauseNanos = 0
        self._clearedNanos = 0

    def _secondsToNano (self, seconds):
        return 1000000000 * seconds

    def _nanoToSeconds (self, nanos):
        return float(nanos) / 1000000000.0

    def _nanoToMsecs (self, nanos):
        return float(nanos) / 1000000.0


    def _now (self):
        return a.infra.time.monotonic_clock.monotonicTimeNano()

    def set(self):
        self._startTime = self._now()        
        self._pauseTime = None
        self._totalPauseNanos = 0
        self._clearedNanos = 0

    def pause (self):
        self._pauseTime = self._now()

        
    def resume (self):
        if not self.wasSet():
            self.set()
        elif self._pauseTime is not None:
            self._totalPauseNanos = self._totalPauseNanos + self._now() - self._pauseTime
            self._pauseTime = None


    def getStartTimeNanos (self):
        return self._startTime

    def wasSet (self):
        return self._startTime is not None


    def getElapsedNanosUncleared (self):
        if not self.wasSet():
            return 0

        if self._pauseTime is not None:
            refernceTime = self._pauseTime
        else:
            refernceTime = self._now()

        elapsed = refernceTime - self._startTime - self._totalPauseNanos
        return elapsed


    def getElapsedNanos (self):
        if not self.wasSet():
            return 0
        return self.getElapsedNanosUncleared() - self._clearedNanos

    def getElapsedSeconds (self):        
        return self._nanoToSeconds(self.getElapsedNanos())

    def getElapsedMsecs (self):        
        return self._nanoToMsecs(self.getElapsedNanos())

    def clear (self):
        if self.wasSet():
            self._clearedNanos = self.getElapsedNanosUncleared()


#-----------------------------------------------------------------------------#

class _Timeout(_TimeElapsor):
    """ Convenient timeout class, that uses functors to always get the updated interval which might change during timer is on due to configuration """
    def __init__ (self, logger, functorGetInterval):
        _TimeElapsor.__init__(self, logger)
        self._functorGetInterval = functorGetInterval

    def hasFullExpired (self):        
        interval = self._secondsToNano(self._functorGetInterval())
        elapsed = self.getElapsedNanos()

        return elapsed >= interval


