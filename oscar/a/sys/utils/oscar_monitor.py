#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import datetime
import os
import sys
import time
import subprocess
import a.api.user_log.msg.sys
import a.infra.process
import a.infra.format.json
import a.infra.time.monotonic_clock

if  __package__ is None:
    G_NAME_MODULE_OSCAR_MONITOR = "unknown"
    G_NAME_GROUP_OSCAR_MONITOR_GENERAL = "unknown"
    G_NAME_GROUP_OSCAR_MONITOR_DAEMONS = "unknown"
    G_NAME_GROUP_OSCAR_MONITOR_CONTENT_DISKS = "unknown"
else:
    from . import G_NAME_MODULE_OSCAR_MONITOR
    from . import G_NAME_GROUP_OSCAR_MONITOR_GENERAL
    from . import G_NAME_GROUP_OSCAR_MONITOR_DAEMONS
    from . import G_NAME_GROUP_OSCAR_MONITOR_CONTENT_DISKS


class OscarMonitor:   
    """Oscar Monitor is the daemon in-charge of actively monitoring the overall QB100 system status.
    It detects and reacts upon a few kinds of system's failures such as processes crash."""
    
    #consts for sections/fields names in sys-param
    CONFIG_SECTION_OSCAR_MONITOR_PARAMS = "oscar-monitor-params"
    CONFIG_VAR_RESTARTS_TILL_RECOVERY = "restarts-till-recovery"
    CONFIG_VAR_TIME_INTERVAL_FOR_RESTARTS_TILL_RECOVERY = "time-interval-for-restarts-till-recovery"
    CONFIG_VAR_SLEEP_TIME_BEFORE_DISKS_TEST = "sleep-time-before-disks-test"
    CONFIG_VAR_SLEEP_TIME = "sleep-time"
    CONFIG_VAR_STOP_FAILURE_REBOOT_TIMEOUT = "stop-failure-reboot-timeout"
    CONFIG_VAR_NO_RESTART = "no-restart"
    CONFIG_VAR_AUTO_DAILY_STOP_ENABLE = "auto-daily-stop-enable"
    CONFIG_VAR_AUTO_DAILY_STOP_HOUR = "auto-daily-stop-hour"
    CONFIG_VAR_DELAY_RESTART = "delay-restart"

    CONFIG_SECTION_OSCAR_MONITOR_DONT_MONITOR = "oscar-monitor-dont-monitor"
    CONFIG_VAR_OSCAR_MONITOR_DONT_MONITOR_CONTENT_DISKS = "content-disks"
    CONFIG_VAR_OSCAR_MONITOR_DONT_MONITOR_PROCESSES = "all-processes"

    CONFIG_SECTION_OSCAR_MONITOR_IS_UP_ALLOWED_FAILURE_INTERVAL = "oscar-monitor-is-up-allowed-failure-interval"
    CONFIG_VAR_OSCAR_MONITOR_IS_UP_ALLOWED_FAILURE_INTERVAL_DEFAULT = "default"

    CONFIG_SECTION_OSCAR_MONITOR_IS_ACTIVE_ALLOWED_FAILURE_INTERVAL = "oscar-monitor-is-active-allowed-failure-interval"
    CONFIG_VAR_OSCAR_MONITOR_IS_ACTIVE_ALLOWED_FAILURE_INTERVAL_DEFAULT = "default"

    #default values for data in sys-param
    DEFAULT_RESTARTS_TILL_RECOVERY = 3
    DEFAULT_TIME_INTERVAL_FOR_RESTARTS_TILL_RECOVERY = 2*60*60#2 hours
    DEFAULT_SLEEP_TIME_BEFORE_DISKS_TEST = 3
    DEFAULT_SLEEP_TIME = 2
    DEFAULT_STOP_FAILURE_REBOOT_TIMEOUT = 10*60+10 #10 min (the line launch timeout) + 10 seconds (safety margin)
    DEFAULT_AUTO_DAILY_STOP_HOUR = 3

    #consts use for the specificParams dictionary provided on "initspecificParams"
    SPECIFIC_PARAM_KEY_DAEMONS_TABLE="daemons-table"
    SPECIFIC_PARAM_KEY_SYSTEM_CONTROL="system-control"
    SPECIFIC_PARAM_KEY_TEST_CONTENT_DISKS = "test-content-disks-function"
    SPECIFIC_PARAM_KEY_OSCAR_MONITOR_DAEMON_NAME="oscar-monitor-daemon-name"    
    SPECIFIC_PARAM_KEY_RESTARTS_DATA_DIR="restarts-data-dir"    
    SPECIFIC_PARAM_KEY_WRITE_NO_START_REASON_FUNCTION = "no-restart-reason-function"
    

    #private consts
    RESTARTS_FILE_NAME = "monitored-restarts.json"

    class DaemonInfo:
        def __init__ (self, name, isDisabledFunc, isUpFunc, isActiveFunc):
            """
            Args:
                name: daemon name
                isDisabledFunc: boolean function - is the process disabled and therefore shall not be tested
                isUpFunc: boolean function - is the process up
                isActiveFunc: function that says if the process is active and configurable. returns (bool isactive, bool isInFirstGracePeriod, info-string)
            """
            self.name = name
            self.isDisabledFunc = isDisabledFunc
            self.isUpFunc = isUpFunc
            self.isActiveFunc = isActiveFunc

            self._isUpFailures = 0            
            self._isUpFirstFailureTime = None
            self._isActiveFailures = 0
            self._isActiveFirstFailureTime = None
            self._isActiveTestWasInFirstGracePeriod = True

        def getName (self):
            return self.name
        def isDisabled (self):
            return (self.isDisabledFunc)()

        def isUp (self):
            if self._isUpAllowedFailureInterval < 0:
                (isUp, msg) = (True, "test-disabled")
            else:
                (isUp, msg) = ((self.isUpFunc)(), "tested")

            isUpToReturn = True
            if not isUp:
                now = a.infra.time.monotonic_clock.monotonicTimeSeconds()
                if self._isUpFirstFailureTime is None:
                    self._isUpFirstFailureTime = now
                self._isUpFailures += 1
                if (now-self._isUpFirstFailureTime) >= self._isUpAllowedFailureInterval:
                    self._log("daemon-down").error("daemon %s is down for %f seconds (%d tests). Threshold is %d seconds. need to restart the system: %s",
                                                   self.name, now-self._isUpFirstFailureTime,
                                                   self._isUpFailures, self._isUpAllowedFailureInterval, msg)
                    isUpToReturn = False
                else:
                    self._log("daemon-down-retry").warning("daemon %s is down for %f seconds (%d tests). Threshold is %d seconds: %s",
                                                           self.name,  now-self._isUpFirstFailureTime,
                                                           self._isUpFailures, self._isUpAllowedFailureInterval, msg)
            else:
                self._log("daemon-up").debug4("daemon %s is up", self.name)
                self._isUpFailures = 0
                self._isUpFirstFailureTime = None

            return isUpToReturn

        def isActive (self):
            if self._isActiveAllowedFailureInterval < 0:
                (isActive, isInFirstGracePeriod, msg) = (True, False, "test-disabled")
            else:
                (isActive, isInFirstGracePeriod, msg) = (self.isActiveFunc)()

            isActiveToReturn = True
            if (not isActive) and (not isInFirstGracePeriod):                
                now = a.infra.time.monotonic_clock.monotonicTimeSeconds()
                if self._isActiveFirstFailureTime is None:
                    self._isActiveFirstFailureTime = now
                self._isActiveFailures += 1
                if (now-self._isActiveFirstFailureTime) >= self._isActiveAllowedFailureInterval:
                    self._log("daemon-inactive").error("daemon %s is not active for %f seconds (%d tests). Threshold is %d seconds. need to restart the system: %s",
                                                       self.name, now-self._isActiveFirstFailureTime,
                                                       self._isActiveFailures, self._isActiveAllowedFailureInterval, msg)
                    isActiveToReturn = False
                elif self._isActiveTestWasInFirstGracePeriod:#first time "get out of grace" period. we fail "is-active" to keep oscar launch time as is in 3.0
                    self._log("daemon-inactive-grace").error("daemon %s is not active (first round after grace). need to restart the system: %s",
                                                             self.name, msg)
                    isActiveToReturn = False
                else:
                    self._log("daemon-inactive-retry").warning("daemon %s is not active for %f seconds (%d tests). Threshold is %d seconds: %s",
                                                               self.name, now-self._isActiveFirstFailureTime,
                                                               self._isActiveFailures, self._isActiveAllowedFailureInterval, msg)
            else:
                self._log("daemon-ok").debug4("daemon %s is ok", self.name)
                self._isActiveFailures = 0
                self._isActiveFirstFailureTime = None

            isConfigurableToReturn = isActiveToReturn
            if isInFirstGracePeriod:
                if not self._isActiveTestWasInFirstGracePeriod:
                    self._log("re-entered-grace").notice("re-entered daemon %s grace period", self.name)
                self._isActiveTestWasInFirstGracePeriod = True
                isConfigurableToReturn = False
                self._log("daemon-non-configurable").debug2("daemon %s is not configurable: %s", self.name, msg)
            else:
                self._isActiveTestWasInFirstGracePeriod = False

            return (isActiveToReturn, isConfigurableToReturn)

        def initLogger (self, logger):
            self._log = logger.createLogger(G_NAME_MODULE_OSCAR_MONITOR, 
                                            G_NAME_GROUP_OSCAR_MONITOR_DAEMONS, 
                                            instance = self.name)

        def initIsUpAllowedFailureInterval (self, seconds):
            self._isUpAllowedFailureInterval = seconds
            if self._isUpAllowedFailureInterval<0:
                self._log("no-up-test").notice("daemon %s up test is disabled", self.name)
            else:
                self._log("up-test-times").debug1("daemon %s up test allows %d seconds failure interval", self.name, self._isUpAllowedFailureInterval)


        def initIsActiveAllowedFailureInterval (self, number):
            self._isActiveAllowedFailureInterval = number
            if self._isActiveAllowedFailureInterval<0:
                self._log("no-active-test").notice("daemon %s active test is disabled", self.name)
            else:
                self._log("active-test-times").debug1("daemon %s active test allows %d seconds failure interval", self.name, self._isActiveAllowedFailureInterval)


    class SystemControl:
        def __init__ (self, startSystemFunc, stopSystemFunc, 
                      coldRebootSystemFunc, signalConfigurationIsAllowedFunc,
                      isSystemInTransitionFunc):
            """
            Args:
                startSystemFunc: function to start the system. return True on sucess
                stopSystemFunc: function to stop the system. get reason to stop and is shutdown, return True on sucess
                coldRebootSystemFunc: function to cold reboot the system. get reason to stop and reason to reboot, returns nothing
                signalConfigurationIsAllowedFunc: function that get a bool that say if we allow or disallow configuration. return error msg in case of failure
                isSystemInTransitionFunc: function that gets no input and return True if the system is in transision phase (stop/start)
            """
            self.startSystemFunc = startSystemFunc
            self.stopSystemFunc = stopSystemFunc
            self.coldRebootSystemFunc = coldRebootSystemFunc
            self.signalConfigurationIsAllowedFunc = signalConfigurationIsAllowedFunc
            self.isSystemInTransitionFunc = isSystemInTransitionFunc

        def startSystem (self):
            return (self.startSystemFunc)()
        def stopSystem (self, stopReason, isShutdown):
            return (self.stopSystemFunc)(stopReason, isShutdown)
        def coldRebootSystem (self, rebootReason):
            return (self.coldRebootSystemFunc)(rebootReason)
        def signalConfigurationIsAllowed (self, isAllowed):
            return (self.signalConfigurationIsAllowedFunc)(isAllowed)
        def isSystemInTransition (self):
            return (self.isSystemInTransitionFunc)()

    def __init__ (self):
        self._doNothing = False
        self._debugRestartFromNewProcess = True
        self._wasConfigurationAllowed = None #None and not "false" - operaration will take place anyhow at first round
        self._lastSeenHourForAutoDailyStop = datetime.datetime.now().hour

    def initLogger(self, logger):
        """Init the class logger to be used.

        Init the logger. 
        This function shall be called before any other functions of the class

        Args:
            logger: a logger from which new loggers shall be created

        Returns:
            None

        Raises:
            None
        """
        self._logGeneral=logger.createLogger(G_NAME_MODULE_OSCAR_MONITOR, G_NAME_GROUP_OSCAR_MONITOR_GENERAL)
        self._logDaemonMonitor=logger.createLogger(G_NAME_MODULE_OSCAR_MONITOR, G_NAME_GROUP_OSCAR_MONITOR_DAEMONS)
        self._logContentDisks=logger.createLogger(G_NAME_MODULE_OSCAR_MONITOR, G_NAME_GROUP_OSCAR_MONITOR_CONTENT_DISKS)

    def initExternalData(self, sysParamsCfg, specificParams):
        """Init the data provided from outside

        Init the data provided from outside - both from configuration and operational consts

        Args:
            sysParamsCfg: a contatiner holding the sys params base configuration (that are destined to move to blinky)
            specificParams: a dictionary holding the data under the "SPECIFIC_PARAM_KEY_..." keys defined at the begining of this class                                            

        Returns:
            None

        Raises:
            None
        """

        self._daemonsTable = specificParams[self.SPECIFIC_PARAM_KEY_DAEMONS_TABLE]        
        self._oscarMonitorDaemonName = specificParams[self.SPECIFIC_PARAM_KEY_OSCAR_MONITOR_DAEMON_NAME]
        self._testContetnDisksFunction = specificParams[self.SPECIFIC_PARAM_KEY_TEST_CONTENT_DISKS]        
        self._restartsDataDir = specificParams[self.SPECIFIC_PARAM_KEY_RESTARTS_DATA_DIR]                
        self._logGeneral("restarts-dir").debug1("restarts-dir: '%s'", self._restartsDataDir)
        self._restartsFileName = os.path.join(self._restartsDataDir, self.RESTARTS_FILE_NAME)
        self._logGeneral("restarts-file").debug1("restarts-file: '%s'", self._restartsFileName)
        self._restartRounds = []
        if os.path.exists(self._restartsFileName):
            self._restartRounds = a.infra.format.json.readFromFile(self._logGeneral, self._restartsFileName)
        self._logGeneral("prev-restarts-data").info("previouse monitored restarts times: '%s'", self._restartRounds)
        self._systemControl = specificParams[self.SPECIFIC_PARAM_KEY_SYSTEM_CONTROL]  
        self._writeNoRestartReasonFunction = specificParams[self.SPECIFIC_PARAM_KEY_WRITE_NO_START_REASON_FUNCTION]  

        self._restartsTillRecovery = sysParamsCfg.getInt(self.CONFIG_SECTION_OSCAR_MONITOR_PARAMS, 
                                                         self.CONFIG_VAR_RESTARTS_TILL_RECOVERY, 
                                                         self.DEFAULT_RESTARTS_TILL_RECOVERY)
        self._logGeneral("restarts-till-recovery-value").debug1("the number of restart rounds till recovery was set to '%d'", 
                                                                self._restartsTillRecovery)

        self._timeIntervalForRestartsTillRecovery = sysParamsCfg.getFloat(self.CONFIG_SECTION_OSCAR_MONITOR_PARAMS, 
                                                                          self.CONFIG_VAR_TIME_INTERVAL_FOR_RESTARTS_TILL_RECOVERY, 
                                                                          self.DEFAULT_TIME_INTERVAL_FOR_RESTARTS_TILL_RECOVERY)
        self._logGeneral("period-till-recovery-value").debug1("the time period for restarts till recovery was set to '%f'", 
                                                              self._timeIntervalForRestartsTillRecovery)

        self._sleepTimeBeforeDisksTest = sysParamsCfg.getFloat(self.CONFIG_SECTION_OSCAR_MONITOR_PARAMS, 
                                                               self.CONFIG_VAR_SLEEP_TIME_BEFORE_DISKS_TEST, 
                                                               self.DEFAULT_SLEEP_TIME_BEFORE_DISKS_TEST)
        self._logGeneral("sleep-time-before-disks-value").debug1("sleep time before disks test was set to '%f'", self._sleepTimeBeforeDisksTest)

        self._sleepTime = sysParamsCfg.getFloat(self.CONFIG_SECTION_OSCAR_MONITOR_PARAMS, 
                                                self.CONFIG_VAR_SLEEP_TIME, 
                                                self.DEFAULT_SLEEP_TIME)
        self._logGeneral("sleep-time-value").debug1("sleep time was set to '%f'", self._sleepTime)

        self._stopFailureRebootTimeout = sysParamsCfg.getFloat(self.CONFIG_SECTION_OSCAR_MONITOR_PARAMS, 
                                                               self.CONFIG_VAR_STOP_FAILURE_REBOOT_TIMEOUT, 
                                                               self.DEFAULT_STOP_FAILURE_REBOOT_TIMEOUT)
        self._logGeneral("stop-failure-reboot-timeout").debug1("stop failure reboot timeout was set to '%f'", self._stopFailureRebootTimeout)


        self._noRestart = sysParamsCfg.getBool(self.CONFIG_SECTION_OSCAR_MONITOR_PARAMS, 
                                               self.CONFIG_VAR_NO_RESTART, 
                                               False)
        self._logGeneral("no-restart-value").debug1("no restart was set to '%s'", self._noRestart)

        self._autoDailyStopEnable = sysParamsCfg.getBool(self.CONFIG_SECTION_OSCAR_MONITOR_PARAMS, 
                                                         self.CONFIG_VAR_AUTO_DAILY_STOP_ENABLE, 
                                                         False)
        self._autoDailyStopHour = sysParamsCfg.getInt(self.CONFIG_SECTION_OSCAR_MONITOR_PARAMS, 
                                                      self.CONFIG_VAR_AUTO_DAILY_STOP_HOUR, 
                                                      self.DEFAULT_AUTO_DAILY_STOP_HOUR)
        self._logGeneral("auto-daily-stop-value").debug1("auto-daily-stop-enable %s (at %d)", self._autoDailyStopEnable, self._autoDailyStopHour)

        if self._autoDailyStopEnable:
            self._logGeneral("auto-daily-stop-enable").notice("The system will stop automatically at %d:00 (configuration)", self._autoDailyStopHour)

        self._delayRestart = sysParamsCfg.getFloat(self.CONFIG_SECTION_OSCAR_MONITOR_PARAMS, 
                                                   self.CONFIG_VAR_DELAY_RESTART, 
                                                   0)
        self._logGeneral("delay-restart-value").debug1("delay restart value was set to '%f'", self._delayRestart)

        #complicated example - use with care
        self._daemonsToSkipStaticTable = {}
        for daemon in self._daemonsTable:
            daemon.initLogger(self._logDaemonMonitor)
            dontMonitorProcess = sysParamsCfg.getBool(self.CONFIG_SECTION_OSCAR_MONITOR_DONT_MONITOR, 
                                                      self.CONFIG_VAR_OSCAR_MONITOR_DONT_MONITOR_PROCESSES,
                                                      False)
            dontMonitorProcess = sysParamsCfg.getBool(self.CONFIG_SECTION_OSCAR_MONITOR_DONT_MONITOR, 
                                                      daemon.getName(), dontMonitorProcess)
            self._daemonsToSkipStaticTable[daemon.getName()] = dontMonitorProcess
            self._logGeneral("skip-daemon-value").debug1("skip daemon '%s' was set to '%s'", daemon.getName(), 
                                                         self._daemonsToSkipStaticTable[daemon.getName()])
            if dontMonitorProcess:
                 self._logGeneral("skip-daemons").notice("daemons '%s' will not be monitored (configuration)", daemon.getName())


            isUpAllowedFailureInterval = sysParamsCfg.getInt(self.CONFIG_SECTION_OSCAR_MONITOR_IS_UP_ALLOWED_FAILURE_INTERVAL, 
                                                      self.CONFIG_VAR_OSCAR_MONITOR_IS_UP_ALLOWED_FAILURE_INTERVAL_DEFAULT,
                                                      0)
            isUpAllowedFailureInterval = sysParamsCfg.getInt(self.CONFIG_SECTION_OSCAR_MONITOR_IS_UP_ALLOWED_FAILURE_INTERVAL, 
                                                      daemon.getName(), isUpAllowedFailureInterval)
            daemon.initIsUpAllowedFailureInterval(isUpAllowedFailureInterval)

            isActiveAllowedFailureInterval = sysParamsCfg.getInt(self.CONFIG_SECTION_OSCAR_MONITOR_IS_ACTIVE_ALLOWED_FAILURE_INTERVAL, 
                                                          self.CONFIG_VAR_OSCAR_MONITOR_IS_ACTIVE_ALLOWED_FAILURE_INTERVAL_DEFAULT,
                                                          0)
            isActiveAllowedFailureInterval = sysParamsCfg.getInt(self.CONFIG_SECTION_OSCAR_MONITOR_IS_ACTIVE_ALLOWED_FAILURE_INTERVAL, 
                                                      daemon.getName(), isActiveAllowedFailureInterval)
            daemon.initIsActiveAllowedFailureInterval(isActiveAllowedFailureInterval)

        self._skipContentDisksTest = sysParamsCfg.getBool(self.CONFIG_SECTION_OSCAR_MONITOR_DONT_MONITOR, 
                                                          self.CONFIG_VAR_OSCAR_MONITOR_DONT_MONITOR_CONTENT_DISKS,
                                                          False)
        self._logGeneral("skip-content-disks-value").debug1("skip content disks test value was set to '%s'", 
                                                            self._skipContentDisksTest)
        if self._skipContentDisksTest:
            self._logGeneral("skip-content-disks").notice("content disks status will not be monitored (configuration)")
        

    def launch(self):
        """launching the module

        do our thing:) and keep on doing so until the stop command is called
        This function may sys.exit upon failure

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        while not a.infra.process.getWasStopped():
            self._test()
            time.sleep(self._sleepTime)

        if self._wasConfigurationAllowed:#blocking configuration - just so nobody will be abl to do stupid things
            self._logGeneral("block-configuration").notice("blocking configuration as the system is not monitored")
            failureStr = self._systemControl.signalConfigurationIsAllowed(False)            
            if failureStr is not None:
               self._logGeneral("failed-block-configuration").error("Failed to signal configuration is blocked: %s", failureStr)
               #########################################################################################
               # we better restart the system now, but I dont want to deal with it at 3.0.0.0 last mile
               # the whole mechanism need to be oscar monitor crash proff as well...
               #########################################################################################

        self._logGeneral("done").notice("process terminated")

    def debugDontLaunchNewProcessForRestart (self):
        self._debugRestartFromNewProcess = False

    ###private functions
    def _test (self):

        if self._doNothing:#this test need to be in the calling function, 
                                    #it is here so people will not get confused when using this code as reference
            return
        
        testStartTime = datetime.datetime.now()
        self._logGeneral("test-start").debug4("starting a test")
        rebootReason = None   
        restartReason = None   
        needToAllowConfiguration = True   
        for daemon in self._daemonsTable:
            self._logDaemonMonitor("reached-daemon").debug4("reached daemon %s", daemon.getName())
            if self._daemonsToSkipStaticTable[daemon.getName()]:
                self._logDaemonMonitor("daemon-skipped").debug3("daemon %s is skipped by configuration", daemon.getName())
                continue
            if daemon.getName() == self._oscarMonitorDaemonName:
                self._logDaemonMonitor("daemon-oscar-monitor").debug4("oscar monitor daemon is skipped")
                continue #not monitoring ourselve
            if not daemon.isDisabled():                
                if not daemon.isUp():                    
                    needToAllowConfiguration = False
                    restartReason = 'application failure'
                else:
                    (isActive, isConfigurable) = daemon.isActive()
                    if not isActive:
                        restartReason = 'application failure'
                    if not isConfigurable:
                        needToAllowConfiguration = False
            else:
                self._logDaemonMonitor("daemon-disabled").debug3("daemon %s is disabled and therefore not monitored", daemon.getName())


        if self._skipContentDisksTest:
            self._logContentDisks("test-content-disks-disabled").debug3("testing the status of the content disks is disabled - assuming \"Up\" by default")
        else:
            time.sleep(self._sleepTimeBeforeDisksTest)#sleep used allow linux to figure out disks are down. this comes to avoid a scenario in which a disk went down, 
                                                      #a process crashed as a result, but the disk status test passes. If this happens we will restart oscar instead of reboot. not good
            errors = self._testContetnDisksFunction()
            if errors:
                self._logContentDisks("content-disk-down").error("content disks are down, need to reboot the system: %s", ",".join(errors))
                needToAllowConfiguration = False
                rebootReason = 'content disk problem'

        if self._systemControl.isSystemInTransition():
            self._logGeneral("system-in-transision-non-configurable").debug2("system is in transition and therefore is not configurable")
            needToAllowConfiguration = False
        
        autoDailyStop = False
        if (not restartReason) and (not rebootReason) and self._autoDailyStopEnable:
            if datetime.datetime.now().hour == self._autoDailyStopHour and self._lastSeenHourForAutoDailyStop != self._autoDailyStopHour:
                self._logGeneral("auto-daily-stop").notice("The system will stop automatically due to the auto daily stop")
                needToAllowConfiguration = False
                restartReason = 'daily stop'
                autoDailyStop = True

        ###ACTIONS TIME

        if needToAllowConfiguration!=self._wasConfigurationAllowed:
            self._logDaemonMonitor("need-to-allow-configuration").debug1("needToAllowConfiguration!=self._wasConfigurationAllowed (%s!=%s)", 
                                                                   needToAllowConfiguration, self._wasConfigurationAllowed)
            failureStr = self._systemControl.signalConfigurationIsAllowed(needToAllowConfiguration)            
            if failureStr is None:
               self._logGeneral("success-to-allow-configuration").notice("signal configuration allowed state = %s", needToAllowConfiguration)
               self._wasConfigurationAllowed = needToAllowConfiguration
            else:
               self._logGeneral("failed-to-allow-configuration").error("Failed to signal configuration allowed state = %s. error:%s. need to restart the system", 
                                                                             needToAllowConfiguration, failureStr)
               restartReason = 'application failure'

        if rebootReason:
            self._restartSystem(testStartTime, rebootReason, coldReboot = True, isAutoDailyStop = autoDailyStop)
            return

        if restartReason:
            self._restartSystem(testStartTime, restartReason, isAutoDailyStop = autoDailyStop)
            return 

       
    def _restartSystem(self, testStartTime, reason, coldReboot=False, isAutoDailyStop = False):
        #fork - so the the stop command we are about to call will not kill us
        #we could have use the same process and call "execve", but then, we will create many processes 
        #one create the other....        
        if coldReboot:
            self._logGeneral("system-reboot").notice("cold reboot the system - issues were found at the test started at %s", testStartTime.strftime("%Y%m%d-%H%M%S.%f"))
        else:
            self._logGeneral("system-restart").notice("restarting the system - issues were found at the test started at %s", testStartTime.strftime("%Y%m%d-%H%M%S.%f"))

        if self._noRestart and not isAutoDailyStop:
            self._logGeneral("no-system-restart").notice("not really restarting the system due to the no restarts flag. Stop working")
            self._doNothing = True
            return

        if self._delayRestart > 0:
            self._logGeneral("delay-restart").notice("sleeping for %f seconds before restarting oscar", self._delayRestart)
            time.sleep(self._delayRestart)

        #gathering information on the system load
        subprocess.call("ps -e o pid,user,%cpu,cputime,%mem,rss,vsz,comm,cmd", shell=True)

        sys.stdout.flush() 
        sys.stderr.flush() 
        if self._debugRestartFromNewProcess:
            pid=os.fork()
        else:
            pid=0
        if pid==0:  
            #cannot use the logger... - we are in another process
            #child process
            if coldReboot:
                self._systemControl.coldRebootSystem(reason)
                sys.exit(1)

            
            now = time.time()
            self._restartRounds += [str(time.time())]
            givingUp = False
            if len(self._restartRounds) >= self._restartsTillRecovery:
                firstStart = float(self._restartRounds[0])
                if (now-firstStart) < self._timeIntervalForRestartsTillRecovery:
                    givingUp = True
                    applicationShutdownReason = 'persistent application failure'
                    print "Restart number",len(self._restartRounds),"in",(now-firstStart),"seconds. Thershold is", self._timeIntervalForRestartsTillRecovery,"seconds. Giving up"
                    self._writeNoRestartReasonFunction(["Reached restarts threshold"])
                    
            if isAutoDailyStop:
                givingUp = True
                applicationShutdownReason = 'persistent application failure'
                print "Auto daily stop"
                self._writeNoRestartReasonFunction(["Auto daily stop"]) 

        
            stopRebootTimeout = datetime.datetime.now()+datetime.timedelta(seconds=self._stopFailureRebootTimeout)
            reasonToSignal = reason
            if givingUp:
                reasonToSignal = applicationShutdownReason

            while datetime.datetime.now() < stopRebootTimeout:
                if self._systemControl.isSystemInTransition():
                    print datetime.datetime.now().strftime("%Y%m%d-%H%M%S.%f")+": Cannot stop the system: system is in transition"
                elif self._systemControl.stopSystem(reasonToSignal, givingUp):
                    break
                else:
                    print datetime.datetime.now().strftime("%Y%m%d-%H%M%S.%f")+": failed to stop the system"#we actually need to reboot here or something like this, 
                                                     #as we failed even though the system is not in transision
                                                     #BUT I dont want to make such a change in 3.0.0 end

                reasonToSignal = None                
                time.sleep(5)
            else:
                if not self._systemControl.stopSystem(reasonToSignal, False):
                    print "failed to stop the system - moving to reboot"
                    self._systemControl.coldRebootSystem('OS problem')
                    sys.exit(1)

            if givingUp:
                if self._debugRestartFromNewProcess:
                    sys.exit(1)
                else:
                    return 1    

            if len(self._restartRounds)>=self._restartsTillRecovery:
                self._restartRounds = self._restartRounds[(-self._restartsTillRecovery+1):]

            a.infra.format.json.writeToFile(None, self._restartRounds, self._restartsFileName, indent=4)        

            subprocess.call("ps -lf -u `whoami`", shell=True)

            if not self._systemControl.startSystem():
                print "failed to restart the system"
                if self._debugRestartFromNewProcess:
                    sys.exit(1)
                else:
                    return 1    

            if self._debugRestartFromNewProcess:
                sys.exit(0)
            else:
                return 0  
                
    
        else:
            # parent
            #stop working as we dont want to restart the system twice. 
            self._logGeneral("stop-operating").info("marking the process to wait to be terminated")
            self._doNothing = True


