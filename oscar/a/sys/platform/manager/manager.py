# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 

import threading
import time

import a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.manager_data_gen #ManagerData

from a.infra.basic.return_codes import ReturnCodes
import a.infra.subprocess
import a.infra.time.poll_supervisor
import a.infra.time.monotonic_clock
import a.infra.time.elapsed_timer

# Bypass for PyChecker
if  __package__ is None:
    G_MODULE_NAME_PLATFORM_MANAGER                 = "unknown"
    G_GROUP_NAME_PLATFORM_MANAGER_PROCESS          = "unknown"
    G_GROUP_NAME_PLATFORM_MANAGER_CONFIGURATION    = "unknown"
    G_GROUP_NAME_PLATFORM_MANAGER_COUNTERS         = "unknown"
else:
    from . import G_MODULE_NAME_PLATFORM_MANAGER                  
    from . import G_GROUP_NAME_PLATFORM_MANAGER_PROCESS       
    from . import G_GROUP_NAME_PLATFORM_MANAGER_CONFIGURATION 
    from . import G_GROUP_NAME_PLATFORM_MANAGER_COUNTERS


class ConfigurationError(Exception):
    def __init__ (self, errMessage):
        Exception.__init__(self)
        self.errMessage = errMessage

    def getErrorMessage (self):
        return self.errMessage


class PlatformManager:
    SLEEP_INTERVAL_SECONDS_WAIT_FOR_CONFIGURATION = 1   # TODO(shmulika): this might be configurable   
    SLEEP_INTERVAL_SECONDS_BETWEEN_CHECK_POLLS    = 0.1 # TODO(shmulika): this might be configurable   

    MANAGED_ELEMENTS_SUPERVISOR_KEY = "managed-elements"
    REPORTERS_SUPERVISOR_KEY        = "reporters"


    def __init__ (self, logger):
        self._logConfiguration = logger.createLogger(G_MODULE_NAME_PLATFORM_MANAGER, G_GROUP_NAME_PLATFORM_MANAGER_CONFIGURATION)
        self._logProcess       = logger.createLogger(G_MODULE_NAME_PLATFORM_MANAGER, G_GROUP_NAME_PLATFORM_MANAGER_PROCESS)

        ### Configuration ###
        self._configErrorMsgFunctor = lambda x: self._logConfiguration("config-error-msg").debug1("error-msg-functor not set yet, called with message: %s", x)
        self._configLock = threading.RLock()
        self._runningSettings   = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.manager_data_gen.ManagerData()
        self._candidateSettings = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.manager_data_gen.ManagerData()
        self._changedSettings   = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.manager_data_gen.ManagerData()
        
        self._runningThresholds   = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.thresholds.thresholds_data_gen.ThresholdsData()
        self._candidateThresholds = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.thresholds.thresholds_data_gen.ThresholdsData()
        self._changedThresholds   = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.thresholds.thresholds_data_gen.ThresholdsData()
        


        #self._runningThresholds = TempThresholdsData()

        ### Process ###        
        self._wasStopped = False
        self._wasConfigured = False
        self._pollSupervisor = a.infra.time.poll_supervisor.PollSupervisor(self._logProcess, "platform-manager", "") # TODO(shmulika): check pollCycleLogString with nirs
        self._pollSupervisor.addPollElement([self.REPORTERS_SUPERVISOR_KEY], logString = "reporters-polling")
        self._pollSupervisor.addPollElement([self.MANAGED_ELEMENTS_SUPERVISOR_KEY], logString = "element-updating")
        self._isFirstRealPoll = True
        self._shouldForceStartPollSupervisor = False

        ### Logic ###
        self._reporters = []
        self._managedElements = []
        self._componentsUpdated = False
        

###############################################################
# BLINKY, CONFIGURATION, OPER
###############################################################
    
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
    
    def getObjCountersOperData(self, trxContext, countersData):                
        self._logConfiguration("get-obj-counters-oper-data-called").debug3("called with trxContext = %s, countersData = %s", trxContext, countersData)
        countersData.setPolls(self._pollSupervisor.getPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_POLLS))
        countersData.setMissedPolls(self._pollSupervisor.getPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_MISSED_POLLS))

        countersData.setPollLatencyWarning(self._pollSupervisor.getPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_LATENCY_WARNINGS))
        countersData.setPollLatencyError(self._pollSupervisor.getPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_LATENCY_ERRORS))

        countersData.setSinglePollDurationWarning(self._pollSupervisor.getElementPollCounter([self.REPORTERS_SUPERVISOR_KEY], a.infra.time.poll_supervisor.PollSupervisor.COUNTER_DURATION_WARNINGS))
        countersData.setSinglePollDurationError(self._pollSupervisor.getElementPollCounter([self.REPORTERS_SUPERVISOR_KEY], a.infra.time.poll_supervisor.PollSupervisor.COUNTER_DURATION_ERRORS))

        countersData.setOverallPollDurationWarning(self._pollSupervisor.getPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_DURATION_WARNINGS))
        countersData.setOverallPollDurationError(self._pollSupervisor.getPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_DURATION_ERRORS))

        countersData.setPollLatencyWarning(self._pollSupervisor.getPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_LATENCY_WARNINGS))
        countersData.setPollLatencyError(self._pollSupervisor.getPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_LATENCY_ERRORS))

        countersData.setTotalSeconds(self._pollSupervisor.getPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_TOTAL_NANO_SECONDS)/1000/1000/1000)
        countersData.setActiveSeconds(self._pollSupervisor.getPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_ACTIVE_NANO_SECONDS)/1000/1000/1000)


        self._logConfiguration("get-obj-counters-oper-data-done").debug3("returned counters-oper-data=%s", countersData)
        return ReturnCodes.kOk  


    def actionClearCounters (self):
        self._pollSupervisor.clearPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_POLLS)
        self._pollSupervisor.clearPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_MISSED_POLLS)
        self._pollSupervisor.clearPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_LATENCY_WARNINGS)
        self._pollSupervisor.clearPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_LATENCY_ERRORS)
        self._pollSupervisor.clearPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_TOTAL_NANO_SECONDS)
        self._pollSupervisor.clearPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_ACTIVE_NANO_SECONDS)
        self._pollSupervisor.clearPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_DURATION_ERRORS)
        self._pollSupervisor.clearPollCycleCounter(a.infra.time.poll_supervisor.PollSupervisor.COUNTER_DURATION_WARNINGS)

        self._pollSupervisor.clearElementPollCounter([self.REPORTERS_SUPERVISOR_KEY], a.infra.time.poll_supervisor.PollSupervisor.COUNTER_POLLS)
        self._pollSupervisor.clearElementPollCounter([self.REPORTERS_SUPERVISOR_KEY], a.infra.time.poll_supervisor.PollSupervisor.COUNTER_FAILURES)
        self._pollSupervisor.clearElementPollCounter([self.REPORTERS_SUPERVISOR_KEY], a.infra.time.poll_supervisor.PollSupervisor.COUNTER_DURATION_ERRORS)
        self._pollSupervisor.clearElementPollCounter([self.REPORTERS_SUPERVISOR_KEY], a.infra.time.poll_supervisor.PollSupervisor.COUNTER_DURATION_WARNINGS)        
        self._pollSupervisor.clearElementPollCounter([self.REPORTERS_SUPERVISOR_KEY], a.infra.time.poll_supervisor.PollSupervisor.COUNTER_TOTAL_NANO_SECONDS)        

        self._logConfiguration("action-clear-counters").debug1("counters cleared.")
        return (ReturnCodes.kOk, None)

    ######################
    # GETTERS
    ######################

    def getData (self):
        with self._configLock:
            copyData = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.manager_data_gen.ManagerData()
            copyData.copyFrom(self._runningSettings)
        return copyData


    def getThresholds (self):
        with self._configLock:
            copyData = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.thresholds.thresholds_data_gen.ThresholdsData()
            copyData.copyFrom(self._runningThresholds)
        return copyData

    ######################
    # TRANSACTION
    ######################

    def configStartTransaction (self):
        self._logConfiguration("config-start-transaction").debug2("configuration transaction started")

        with self._configLock:
            self._candidateSettings.copyFrom(self._runningSettings)
            self._changedSettings = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.manager_data_gen.ManagerData()

            self._candidateThresholds.copyFrom(self._runningThresholds)
            self._changedThresholds = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.thresholds.thresholds_data_gen.ThresholdsData()
            
            
        return ReturnCodes.kOk


    def preparePrivateData (self, blinkyData):        
        self._logConfiguration("prepare-private-data").debug2("got candidate data = %s", blinkyData)
        
        if blinkyData.hasPollIntervalSeconds():
            self._candidateSettings.pollIntervalSeconds = blinkyData.pollIntervalSeconds
            self._candidateSettings.setHasPollIntervalSeconds()

        if blinkyData.hasEnabled():
            self._candidateSettings.enabled = blinkyData.enabled
            self._candidateSettings.setHasEnabled()

        self._changedSettings.copyFrom(blinkyData)

        return ReturnCodes.kOk


    def preparePrivateThresholdsData (self, blinkyThresholdsData):
        self._logConfiguration("prepare-private-thresholds-data").debug2("got candidate alarm data = %s", blinkyThresholdsData)
        
        if blinkyThresholdsData.hasPollLatencyWarning():
            self._candidateThresholds.pollLatencyWarning = blinkyThresholdsData.pollLatencyWarning
            self._candidateThresholds.setHasPollLatencyWarning()

        if blinkyThresholdsData.hasPollLatencyError():
            self._candidateThresholds.pollLatencyError = blinkyThresholdsData.pollLatencyError
            self._candidateThresholds.setHasPollLatencyError()

        if blinkyThresholdsData.hasSinglePollDurationWarning():
            self._candidateThresholds.singlePollDurationWarning = blinkyThresholdsData.singlePollDurationWarning
            self._candidateThresholds.setHasSinglePollDurationWarning()

        if blinkyThresholdsData.hasSinglePollDurationError():
            self._candidateThresholds.singlePollDurationError = blinkyThresholdsData.singlePollDurationError
            self._candidateThresholds.setHasSinglePollDurationError()

        if blinkyThresholdsData.hasOverallPollDurationWarning():
            self._candidateThresholds.overallPollDurationWarning = blinkyThresholdsData.overallPollDurationWarning
            self._candidateThresholds.setHasOverallPollDurationWarning()

        if blinkyThresholdsData.hasOverallPollDurationError():
            self._candidateThresholds.overallPollDurationError = blinkyThresholdsData.overallPollDurationError
            self._candidateThresholds.setHasOverallPollDurationError()

        self._changedThresholds.copyFrom(blinkyThresholdsData)
        return ReturnCodes.kOk


    def configAbortTransaction (self):
        self._logConfiguration("config-abort-transaction").debug2("configuration transaction aborted")
        return ReturnCodes.kOk


    def configPreparePrivateAfter (self):
        self._logConfiguration("config-prepare-private-after").debug2("checking configuration validity")                        
        try:
            self._checkCandidateConfigurationData(self._candidateSettings)
            self._checkCandidateThresholdsData(self._candidateThresholds)
        except ConfigurationError as configurationError:
            self._logConfiguration("config-prepare-private-after-configuration-invalid").error("configuration invalid: %s", configurationError.getErrorMessage())
            self._configErrorMsgFunctor(configurationError.getErrorMessage())
            return ReturnCodes.kGeneralError
        else:
            self._logConfiguration("config-prepare-private-after-done").debug1("candidate configuration is valid")                
            return ReturnCodes.kOk


    def _checkCandidateConfigurationData (self, candidateSettings):        
        if not candidateSettings.hasEnabled():
            raise ConfigurationError("manager must be configured to either enabled or disabled")

        if not candidateSettings.hasPollIntervalSeconds():
            raise ConfigurationError("poll-interval-seconds must be configured")

        if candidateSettings.pollIntervalSeconds <= 0:
            raise ConfigurationError("poll-interval-seconds must be a positive value")


    def _checkCandidateThresholdsData (self, candidateThresholds):
        if not candidateThresholds.hasPollLatencyWarning():
            raise ConfigurationError("poll-latency-warning must be configured")
        if not candidateThresholds.hasPollLatencyError():
            raise ConfigurationError("poll-latency-error must be configured")
        if not candidateThresholds.hasSinglePollDurationWarning():
            raise ConfigurationError("single-poll-duration-warning must be configured")
        if not candidateThresholds.hasSinglePollDurationError():
            raise ConfigurationError("single-poll-duration-error must be configured")
        if not candidateThresholds.hasOverallPollDurationWarning():
            raise ConfigurationError("overall-poll-duration-warning must be configured")
        if not candidateThresholds.hasOverallPollDurationError():
            raise ConfigurationError("overall-poll-duration-error must be configured")

        self._checkCandidateWarningErrorThresholdsValues(candidateThresholds.pollLatencyWarning, candidateThresholds.pollLatencyError, "poll-latency-%s")
        self._checkCandidateWarningErrorThresholdsValues(candidateThresholds.singlePollDurationWarning, candidateThresholds.singlePollDurationError, "single-poll-duration-%s")
        self._checkCandidateWarningErrorThresholdsValues(candidateThresholds.overallPollDurationWarning, candidateThresholds.overallPollDurationError, "overall-poll-duration-%s")        

            
    def _checkCandidateWarningErrorThresholdsValues (self, warning, error, string):
        warningString = string % "warning"
        errorString = string % "error"
        self._checkCandidateThresholdValue(warning, warningString)
        self._checkCandidateThresholdValue(error, errorString)        
        if warning > error > 0:
            raise ConfigurationError("%s threshold must be smaller then or equal to %s" % (warningString, errorString))


    def _checkCandidateThresholdValue (self, thresholdValue, name):
        if thresholdValue < 0:
            raise ConfigurationError("%s threshold must be a non-negative value" % name)


    def configPreparePublicAfter (self):
        self._logConfiguration("config-prepare-public-after").debug2("doing nothing - already checked data in private")       
        return ReturnCodes.kOk


    def configCommitTransaction (self):        
        with self._configLock:
            self._runningSettings.copyFrom(self._candidateSettings)
            self.applyRunningConfiguration(self._changedSettings)

            self._runningThresholds.copyFrom(self._candidateThresholds)

        self._logConfiguration("config-commit-transaction").debug2("configuration transaction commited")
        self._wasConfigured = True
        return ReturnCodes.kOk


    def applyRunningConfiguration (self, changedSettings):
        if changedSettings.hasEnabled() and changedSettings.enabled:
            self._forceStartPollSupervisor()
        if changedSettings.hasEnabled() and not changedSettings.enabled:
            self._forceClearManagedComponents()
        if changedSettings.hasPollIntervalSeconds():
            self._forceStartPollSupervisor()


###############################################################
# MANAGER - SET UP
###############################################################

    def addManagedElement (self, element):        
        self._managedElements.append(element)

    def addReporter (self, reporterer):
        self._reporters.append(reporterer)


###############################################################
# MANAGER - MAIN LOGIC
###############################################################

    def _updateManagedElements (self):
        self._logProcess("update-managed-elements").debug2("updating the managed elements")
        for element in self._managedElements:            
            self._logProcess("update-managed-element").debug3("updating managed element %s", element.getName())
            self._pollSupervisor.startElementPoll([self.MANAGED_ELEMENTS_SUPERVISOR_KEY], element.getName())
            element.updateOrClear(enabled = True)
            self._pollSupervisor.endElementPoll([self.MANAGED_ELEMENTS_SUPERVISOR_KEY], ReturnCodes.kOk)
        self._componentsUpdated = True  
        
    def _clearManagedElements (self):
        self._logProcess("clear-managed-elements").debug2("clearing the managed elements")
        for element in self._managedElements:            
            self._logProcess("clear-managed-element").debug3("clearing managed element %s", element.getName())
            self._pollSupervisor.startElementPoll([self.MANAGED_ELEMENTS_SUPERVISOR_KEY], element.getName())
            element.updateOrClear(enabled = False)
            self._pollSupervisor.endElementPoll([self.MANAGED_ELEMENTS_SUPERVISOR_KEY], ReturnCodes.kOk)
        self._componentsUpdated = False  

    def _pollReporters (self):
        self._logProcess("poll-reporter").debug2("polling the reporters for data")
        for reporterer in self._reporters:
            self._pollSupervisor.startElementPoll([self.REPORTERS_SUPERVISOR_KEY], reporterer.getName())
            returnCode = reporterer.poll()
            self._pollSupervisor.endElementPoll([self.REPORTERS_SUPERVISOR_KEY], returnCode)


    def _pollAndUpdate (self):
        self._logProcess("poll-and-update").debug2("polling reportes and updating managed elements")
        self._pollReporters()
        self._updateManagedElements()

################################################################
## PROCESS
################################################################

    def _configurePollSupervisor (self, settings, thresholds):
        """ Configures the poll supervisor, can be called before each poll - even if configuration didn't change """
        self._pollSupervisor.setPollCycleInterval(settings.pollIntervalSeconds)
        self._pollSupervisor.setPollCycleLatencyThresholds(errorThreshold = thresholds.pollLatencyError, warningThreshold = thresholds.pollLatencyWarning)
        self._pollSupervisor.setPollCycleDurationThresholds(errorThreshold = thresholds.overallPollDurationError, warningThreshold = thresholds.overallPollDurationWarning)
        self._pollSupervisor.setElementPollDurationThresholds([self.MANAGED_ELEMENTS_SUPERVISOR_KEY], errorThreshold = thresholds.singlePollDurationError, warningThreshold = thresholds.singlePollDurationWarning) 
        self._pollSupervisor.setElementPollDurationThresholds([self.REPORTERS_SUPERVISOR_KEY], errorThreshold = thresholds.singlePollDurationError, warningThreshold = thresholds.singlePollDurationWarning) 


    def _forceStartPollSupervisor (self):
        """ Force the poll supervisor  """
        if not self._isFirstRealPoll:
            self._shouldForceStartPollSupervisor = True


    def _forceClearManagedComponents (self):
        self._shouldClearManagedComponents = True


    def _hasPollCycleStarted (self, settings, thresholds):
        """ Checks with the poll-supervisor, if should start the poll cycle - and if so, starts it.
        Returns: True - if poll cycle was started
        """
        self._configurePollSupervisor(settings, thresholds)

        # first poll / force start cases
        if self._isFirstRealPoll:
            self._isFirstRealPoll = False
            self._pollSupervisor.startPollCycle()
        elif self._shouldForceStartPollSupervisor:
            self._logProcess("poll-supervisor-force-started").debug2("restarting the poll-supervisor")
            self._pollSupervisor.forceStart()
            self._shouldForceStartPollSupervisor = False
        # normal cases
        elif self._pollSupervisor.isTimeToStartPollCycle():
            self._pollSupervisor.startPollCycle()
        else:            
            self._logProcess("has-poll-cycle-started-not-yet").debug4("not yet time to start poll cycle")
            return False

        self._logProcess("has-poll-cycle-started").debug3("poll cycle has started")
        return True


    def _checkPollSupervisorPollAndUpdate (self):
        settings = self.getData()
        thresholds = self.getThresholds()

        if not settings.enabled:
            self._logProcess("check-poll-supervisor-and-poll").debug3("poll disabled - not polling")            
            if self._componentsUpdated:
                self._clearManagedElements()
            return
        if not self._hasPollCycleStarted(settings, thresholds):            
            return

        self._pollAndUpdate()
        self._pollSupervisor.endPollCycle()
        self._logProcess("poll-cycle-finished").debug3("poll cycle is over")


    def launch (self):
        """ Called by the Application to launch the reporter manager """
        self._logProcess("launch-go").debug1("reporter-manager was launched")

        self._waitForInitialConfigration()
        while not self.wasStopped():            
            self._checkPollSupervisorPollAndUpdate()
            time.sleep(self.SLEEP_INTERVAL_SECONDS_BETWEEN_CHECK_POLLS)

        self._logProcess("launch-stop").debug1("reporter-manager has stopped")


    def wasStopped (self):
        return self._wasStopped


    def stop (self):
        """ Called by the Application to stop the reporter manager """
        self._logProcess("stop").debug1("reporter-manager asked to be stopped")
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
            time.sleep(PlatformManager.SLEEP_INTERVAL_SECONDS_WAIT_FOR_CONFIGURATION)

        self._logProcess("wait-for-initial-configuration-done").debug1("initial configuration of the process was made")
