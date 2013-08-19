#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import os
import sys
import a.infra.process
import a.sys.blinky.pearl

if  __package__ is None:
    G_NAME_MODULE_PROCESS_MANAGER = "unknown"
    G_NAME_GROUP_PROCESS_MANAGER_BLINKY_COPY = "unknown"
    G_NAME_GROUP_PROCESS_MANAGER_BLINKY_DATA = "unknown"
else:
    from . import G_NAME_MODULE_PROCESS_MANAGER 
    from . import G_NAME_GROUP_PROCESS_MANAGER_BLINKY_COPY
    from . import G_NAME_GROUP_PROCESS_MANAGER_BLINKY_DATA


class BlinkyKeyPath:
    MODULE_KEY_PATH = os.path.join("sys", "process-manager")
    PROCESS_TABLE_SUB_KEY_PATH = "processes"
    PROCESS_TABLE_KEY_PATH = os.path.join(MODULE_KEY_PATH, PROCESS_TABLE_SUB_KEY_PATH)

class SingleProcessBlinkyData:
    """ this class is simulating the module retrieving data from blinky"""

    ACTUAL_SUFFIX = "-actual"

    PROCESS_TYPE = "process-type"
    IS_BLOCKING = "is-blocking"


    #delayed fields
    EXECUTABLE = "executable"
    EXTRA_ARGS = "extra-args"
    CWD = "cwd"
    REDIRECT_DIR = "redirect-dir"
    OS_ENV = "os-env"
    CHROOT_DIR = "chroot-dir"
    INIT_PARAM_FILES_DIR = "init-param-files-dir"
    #immediate fields
    MAIN_LOOP_SLEEP_TIME = "main-loop-sleep-time"
    AFFINITY = "affinity"
    FAILURE_TERMINATION_SIGNAL = "failure-termination-signal"
    STATE_TRANSITION_TIMEOUT = "state-transition-timeout"
    STATE_TRANSITION_WARNING_THRESHOLD = "state-transition-warning-threshold"
    WATCHDOG_TIMEOUT = "watchdog-timeout"
    WATCHDOG_WARNING_THRESHOLD = "watchdog-warning-threshold"
    KILL_TIMEOUT = "kill-timeout"
    KILL_WARNING_THRESHOLD = "kill-warning-threshold"

    #operational. writen by PM/PM-Agent
    PID = "pid"
    ACTUAL_STATE = "actual-state"
    DESIRED_STATE = "desired-state"
    MACHINE_STATE = "machine-state"

    WATCHDOG_MARK = "watchdog-mark"
   

    def __init__ (self, processName, logger):
        self._log = logger.createLogger(G_NAME_MODULE_PROCESS_MANAGER, G_NAME_GROUP_PROCESS_MANAGER_BLINKY_DATA)
        self._managerToAgentBlinkyDataEngine = a.sys.blinky.pearl.BlinkyJsonDataEngine(self._log)
        self._processName=processName

    def initBlinky (self, blinky):
        self._blinkyOnOurPath = blinky.keyPath(BlinkyKeyPath.PROCESS_TABLE_KEY_PATH, self._processName)
        self._managerToAgentBlinkyDataEngine.initBlinky(self._blinkyOnOurPath)

    def removeFromBlinky (self):
        self._blinkyOnOurPath.remove()

    def isDefinedProcessType (self):
        fieldName = self.PROCESS_TYPE
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def readProcessType (self):
        fieldName = self.PROCESS_TYPE
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeProcessType (self, data):
        fieldName = self.PROCESS_TYPE
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data)

    def isDefinedIsBlocking (self):
        fieldName = self.IS_BLOCKING
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def readIsBlocking (self):
        fieldName = self.IS_BLOCKING
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeIsBlocking (self, data):
        fieldName = self.IS_BLOCKING
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data)

    def isDefinedExecutable (self):
        fieldName = self.EXECUTABLE
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultExecutable (self):
        fieldName = self.EXECUTABLE
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readExecutable (self):
        fieldName = self.EXECUTABLE
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeExecutableDefault (self, data):
        fieldName = self.EXECUTABLE
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    def writeExecutableActual (self, data):
        fieldName = self.EXECUTABLE
        fieldName = fieldName+self.ACTUAL_SUFFIX
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

    def isDefinedExtraArgs (self):
        fieldName = self.EXTRA_ARGS
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultExtraArgs (self):
        fieldName = self.EXTRA_ARGS
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readExtraArgs (self):
        fieldName = self.EXTRA_ARGS
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeExtraArgsDefault (self, data):
        fieldName = self.EXTRA_ARGS
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    def writeExtraArgsActual (self, data):
        fieldName = self.EXTRA_ARGS
        fieldName = fieldName+self.ACTUAL_SUFFIX
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

    def isDefinedCwd (self):
        fieldName = self.CWD
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultCwd (self):
        fieldName = self.CWD
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readCwd (self):
        fieldName = self.CWD
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeCwdDefault (self, data):
        fieldName = self.CWD
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    def writeCwdActual (self, data):
        fieldName = self.CWD
        fieldName = fieldName+self.ACTUAL_SUFFIX
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

    def isDefinedRedirectDir (self):
        fieldName = self.REDIRECT_DIR
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultRedirectDir (self):
        fieldName = self.REDIRECT_DIR
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readRedirectDir (self):
        fieldName = self.REDIRECT_DIR
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeRedirectDirDefault (self, data):
        fieldName = self.REDIRECT_DIR
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    def writeRedirectDirActual (self, data):
        fieldName = self.REDIRECT_DIR
        fieldName = fieldName+self.ACTUAL_SUFFIX
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

    def isDefinedOsEnv (self):
        fieldName = self.OS_ENV
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultOsEnv (self):
        fieldName = self.OS_ENV
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readOsEnv (self):
        fieldName = self.OS_ENV
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeOsEnvDefault (self, data):
        fieldName = self.OS_ENV
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    def writeOsEnvActual (self, data):
        fieldName = self.OS_ENV
        fieldName = fieldName+self.ACTUAL_SUFFIX
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

    def isDefinedChrootDir (self):
        fieldName = self.CHROOT_DIR
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultChrootDir (self):
        fieldName = self.CHROOT_DIR
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readChrootDir (self):
        fieldName = self.CHROOT_DIR
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeChrootDirDefault (self, data):
        fieldName = self.CHROOT_DIR
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    def writeChrootDirActual (self, data):
        fieldName = self.CHROOT_DIR
        fieldName = fieldName+self.ACTUAL_SUFFIX
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

    def isDefinedInitParamFilesDir (self):
        fieldName = self.INIT_PARAM_FILES_DIR
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultInitParamFilesDir (self):
        fieldName = self.INIT_PARAM_FILES_DIR
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readInitParamFilesDir (self):
        fieldName = self.INIT_PARAM_FILES_DIR
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeInitParamFilesDirDefault (self, data):
        fieldName = self.INIT_PARAM_FILES_DIR
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    def writeInitParamFilesDirActual (self, data):
        fieldName = self.CWD
        fieldName = fieldName+self.INIT_PARAM_FILES_DIR
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

    def isDefinedMainLoopSleepTime (self):
        fieldName = self.MAIN_LOOP_SLEEP_TIME
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultMainLoopSleepTime (self):
        fieldName = self.MAIN_LOOP_SLEEP_TIME
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readMainLoopSleepTime (self):
        fieldName = self.MAIN_LOOP_SLEEP_TIME
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeMainLoopSleepTimeDefault (self, data):
        fieldName = self.MAIN_LOOP_SLEEP_TIME
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    
    def isDefinedAffinity (self):
        fieldName = self.AFFINITY
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultAffinity (self):
        fieldName = self.AFFINITY
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readAffinity (self):
        fieldName = self.AFFINITY
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeAffinityDefault (self, data):
        fieldName = self.AFFINITY
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    
    def isDefinedStateTransitionTimeout (self):
        fieldName = self.STATE_TRANSITION_TIMEOUT
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultStateTransitionTimeout (self):
        fieldName = self.STATE_TRANSITION_TIMEOUT
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readStateTransitionTimeout (self):
        fieldName = self.STATE_TRANSITION_TIMEOUT
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeStateTransitionTimeoutDefault (self, data):
        fieldName = self.STATE_TRANSITION_TIMEOUT
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    
    def isDefinedStateTransitionWarningThreshold (self):
        fieldName = self.STATE_TRANSITION_WARNING_THRESHOLD
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultStateTransitionWarningThreshold (self):
        fieldName = self.STATE_TRANSITION_WARNING_THRESHOLD
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readStateTransitionWarningThreshold (self):
        fieldName = self.STATE_TRANSITION_WARNING_THRESHOLD
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeStateTransitionWarningThresholdDefault (self, data):
        fieldName = self.STATE_TRANSITION_WARNING_THRESHOLD
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    
    def isDefinedWatchdogTimeout (self):
        fieldName = self.WATCHDOG_TIMEOUT
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultWatchdogTimeout (self):
        fieldName = self.WATCHDOG_TIMEOUT
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readWatchdogTimeout (self):
        fieldName = self.WATCHDOG_TIMEOUT
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeWatchdogTimeoutDefault (self, data):
        fieldName = self.WATCHDOG_TIMEOUT
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    
    def isDefinedWatchdogWarningThreshold (self):
        fieldName = self.WATCHDOG_WARNING_THRESHOLD
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultWatchdogWarningThreshold (self):
        fieldName = self.WATCHDOG_WARNING_THRESHOLD
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readWatchdogWarningThreshold (self):
        fieldName = self.WATCHDOG_WARNING_THRESHOLD
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeWatchdogWarningThresholdDefault (self, data):
        fieldName = self.WATCHDOG_WARNING_THRESHOLD
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    
    def isDefinedKillTimeout (self):
        fieldName = self.KILL_TIMEOUT
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultKillTimeout (self):
        fieldName = self.KILL_TIMEOUT
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readKillTimeout (self):
        fieldName = self.KILL_TIMEOUT
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeKillTimeoutDefault (self, data):
        fieldName = self.KILL_TIMEOUT
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)
    
    def isDefinedKillWarningThreshold (self):
        fieldName = self.KILL_WARNING_THRESHOLD
        return self._managerToAgentBlinkyDataEngine.isExistsConfigurationField(fieldName)
    def isNonDefaultKillWarningThreshold (self):
        fieldName = self.KILL_WARNING_THRESHOLD
        return self._managerToAgentBlinkyDataEngine.isExistsNonDefaultConfigurationField(fieldName)
    def readKillWarningThreshold (self):
        fieldName = self.KILL_WARNING_THRESHOLD
        return self._managerToAgentBlinkyDataEngine.readConfigurationField(fieldName)
    def writeKillWarningThresholdDefault (self, data):
        fieldName = self.KILL_WARNING_THRESHOLD
        self._managerToAgentBlinkyDataEngine.writeConfigurationField(fieldName, data, isDefaultTwin=True)

    def isDefinedActualState (self):
        fieldName = self.ACTUAL_STATE
        return self._managerToAgentBlinkyDataEngine.isExistsOperationalVolatileField(fieldName)
    def readActualState (self):
        fieldName = self.ACTUAL_STATE
        return self._managerToAgentBlinkyDataEngine.readOperationalVolatileField(fieldName)
    def writeActualState (self, data):
        fieldName = self.ACTUAL_STATE
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)


    def isDefinedDesiredState (self):
        fieldName = self.DESIRED_STATE
        return self._managerToAgentBlinkyDataEngine.isExistsOperationalVolatileField(fieldName)
    def readDesiredState (self):
        fieldName = self.DESIRED_STATE
        return self._managerToAgentBlinkyDataEngine.readOperationalVolatileField(fieldName)
    def writeDesiredState (self, data):
        fieldName = self.DESIRED_STATE
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)


    def isDefinedMachineState (self):
        fieldName = self.MACHINE_STATE
        return self._managerToAgentBlinkyDataEngine.isExistsOperationalVolatileField(fieldName)
    def readMachineState (self):
        fieldName = self.MACHINE_STATE
        return self._managerToAgentBlinkyDataEngine.readOperationalVolatileField(fieldName)
    def writeMachineState (self, data):
        fieldName = self.MACHINE_STATE
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)


    def isDefinedPid (self):
        fieldName = self.PID
        return self._managerToAgentBlinkyDataEngine.isExistsOperationalVolatileField(fieldName)
    def readPid (self):
        fieldName = self.PID
        return self._managerToAgentBlinkyDataEngine.readOperationalVolatileField(fieldName)
    def writePid (self, data):
        fieldName = self.PID
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)


    def isDefinedWatchdogMark (self):
        fieldName = self.WATCHDOG_MARK
        return self._managerToAgentBlinkyDataEngine.isExistsOperationalVolatileField(fieldName)
    def readWatchdogMark (self):
        fieldName = self.WATCHDOG_MARK
        return self._managerToAgentBlinkyDataEngine.readOperationalVolatileField(fieldName)
    def writeWatchdogMark (self, data):
        fieldName = self.WATCHDOG_MARK
        self._managerToAgentBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

class SingleProcessBlinkyCopy:
    def __init__(self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_PROCESS_MANAGER, G_NAME_GROUP_PROCESS_MANAGER_BLINKY_COPY)
        self.clearCachedData()

    def initBlinkyData (self, blinkyData):
        self._blinkyData = blinkyData

    def clearCachedData (self):
        self._cachedData = {}

    def configuredToActual (self):
        self._blinkyData.writeExecutableActual (self.getExecutable())
        self._blinkyData.writeExtraArgsActual (self.getExtraArgs())
        self._blinkyData.writeCwdActual (self.getCwd())
        self._blinkyData.writeRedirectDirActual (self.getRedirectDir())
        self._blinkyData.writeOsEnvActual (self.getOsEnv())
        self._blinkyData.writeChrootDirActual (self.getChrootDir())
        self._blinkyData.writeInitParamFilesDirActual (self.getInitParamFilesDir())

    def _genericUpdateField (self, noneIfNoData = False):
        callingFunction = sys._getframe(1).f_code.co_name
        fieldString=callingFunction[len("_refresh"):] 
        isDefinedFunction = getattr(self._blinkyData, "isDefined"+fieldString)               
        isDefinded = isDefinedFunction()
        #TODO(nirs) a lock is needed between the "isDefined" and the "read"         
        if isDefinded:
            readFunction = getattr(self._blinkyData, "read"+fieldString)
            value = readFunction()            
            self._cachedData[fieldString] = value
        elif noneIfNoData:
            self._cachedData[fieldString] = None
        elif fieldString in self._cachedData:#removing already existing data when not defined
            self._cachedData.pop(fieldString)

    def _genericGetValue (self):
        callingFunction = sys._getframe(1).f_code.co_name
        fieldString=callingFunction[len("get"):] 
        return self._cachedData[fieldString]

    def _genericWriteValue (self,value):#used by operational volatile fields
        callingFunction = sys._getframe(1).f_code.co_name
        fieldString=callingFunction[len("write"):] 
        writeFunction = getattr(self._blinkyData, "write"+fieldString)
        self._cachedData[fieldString]=value
        writeFunction(self._cachedData[fieldString])

    def _refreshProcessType (self):
        self._genericUpdateField()
    def getProcessType (self):
        return self._genericGetValue()

    def _refreshIsBlocking (self):
        self._genericUpdateField()
    def getIsBlocking (self):
        return self._genericGetValue()

    def _refreshExecutable (self):
        self._genericUpdateField()
    def getExecutable (self):
        return self._genericGetValue()

    def _refreshExtraArgs (self):
        self._genericUpdateField()
    def getExtraArgs (self):
        return self._genericGetValue()

    def _refreshCwd (self):
        self._genericUpdateField()
    def getCwd (self):
        return self._genericGetValue()

    def _refreshRedirectDir (self):
        self._genericUpdateField()
    def getRedirectDir (self):
        return self._genericGetValue()

    def _refreshOsEnv (self):
        self._genericUpdateField()
    def getOsEnv (self):
        return self._genericGetValue()

    def _refreshChrootDir (self):
        self._genericUpdateField()
    def getChrootDir (self):
        return self._genericGetValue()

    def _refreshInitParamFilesDir (self):
        self._genericUpdateField()
    def getInitParamFilesDir (self):
        return self._genericGetValue()

    def _refreshMainLoopSleepTime (self):
        self._genericUpdateField()
    def getMainLoopSleepTime (self):
        return self._genericGetValue()
        
    def _refreshAffinity (self):
        self._genericUpdateField()
    def getAffinity (self):
        return self._genericGetValue()

    def _refreshStateTransitionTimeout (self):
        self._genericUpdateField()
    def getStateTransitionTimeout (self):
        return self._genericGetValue()

    def _refreshStateTransitionWarningThreshold (self):
        self._genericUpdateField()
    def getStateTransitionWarningThreshold (self):
        return self._genericGetValue()

    def _refreshWatchdogTimeout (self):
        self._genericUpdateField()
    def getWatchdogTimeout (self):
        return self._genericGetValue()

    def _refreshWatchdogWarningThreshold (self):
        self._genericUpdateField()
    def getWatchdogWarningThreshold (self):
        return self._genericGetValue()

    def _refreshKillTimeout (self):
        self._genericUpdateField()
    def getKillTimeout (self):
        return self._genericGetValue()

    def _refreshKillWarningThreshold (self):
        self._genericUpdateField()
    def getKillWarningThreshold (self):
        return self._genericGetValue()

    def _refreshActualState (self):
        self._genericUpdateField(noneIfNoData=True)#(noneIfNoData=True) for first round
    def getActualState (self):
        return self._genericGetValue()
    def writeActualState (self, data):
        self._genericWriteValue(data)

    def _refreshDesiredState (self):
        self._genericUpdateField(noneIfNoData=True)#(noneIfNoData=True) for first round
    def getDesiredState (self):
        return self._genericGetValue()
    def writeDesiredState (self, data):
        self._genericWriteValue(data)

    def _refreshMachineState (self):
        self._genericUpdateField(noneIfNoData=True)#(noneIfNoData=True) for first round
    def getMachineState (self):
        return self._genericGetValue()
    def writeMachineState (self, data):
        self._genericWriteValue(data)

    def _refreshPid (self):
        self._genericUpdateField(noneIfNoData=True)#(noneIfNoData=True) for first round
    def getPid (self):
        return self._genericGetValue()
    def writePid (self, data):
        self._genericWriteValue(data)

    def _refreshWatchdogMark (self):
        self._genericUpdateField(noneIfNoData=True)#(noneIfNoData=True) for first round
    def getWatchdogMark (self):
        return self._genericGetValue()
    def writeWatchdogMark (self, data):
        self._genericWriteValue(data)

    def refreshFromBlinky(self):
        self.clearCachedData()
        self._refreshProcessType()
        self._refreshIsBlocking()
        self._refreshExecutable()
        self._refreshExtraArgs()
        self._refreshCwd()
        self._refreshRedirectDir()
        self._refreshOsEnv()
        self._refreshChrootDir()
        self._refreshInitParamFilesDir()
        self._refreshMainLoopSleepTime()
        self._refreshAffinity()
        self._refreshStateTransitionTimeout()
        self._refreshStateTransitionWarningThreshold()
        self._refreshWatchdogTimeout()
        self._refreshWatchdogWarningThreshold()
        self._refreshKillTimeout()
        self._refreshKillWarningThreshold()
        self._refreshActualState()
        self._refreshDesiredState()
        self._refreshMachineState()
        self._refreshPid()
        self._refreshWatchdogMark()


class ManagerBlinkyData:
    """ this class is simulating the module retrieving data from blinky"""
    SYSTEM_DESIRED_STATE = "system-desired-state"
    SYSTEM_REQUESTED_STATE = "system-requested-state"
    SYSTEM_STATE = "system-state"

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_PROCESS_MANAGER, G_NAME_GROUP_PROCESS_MANAGER_BLINKY_DATA)
        self._managerModuleCentralBlinkyDataEngine = a.sys.blinky.pearl.BlinkyJsonDataEngine(self._log)
        self._perProcessBlinkyData = {}

    def initBlinky (self, blinky):
        self._blinky = blinky
        self._managerModuleCentralBlinkyDataEngine.initBlinky(blinky.keyPath(BlinkyKeyPath.MODULE_KEY_PATH))

    def isDefinedSystemDesiredState (self):
        fieldName = self.SYSTEM_DESIRED_STATE
        return self._managerModuleCentralBlinkyDataEngine.isExistsOperationalVolatileField(fieldName)
    def readSystemDesiredState (self):
        fieldName = self.SYSTEM_DESIRED_STATE
        return self._managerModuleCentralBlinkyDataEngine.readOperationalVolatileField(fieldName)
    def writeSystemDesiredState (self, data):
        fieldName = self.SYSTEM_DESIRED_STATE
        self._managerModuleCentralBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

    def isDefinedSystemRequestedState (self):
        fieldName = self.SYSTEM_REQUESTED_STATE
        return self._managerModuleCentralBlinkyDataEngine.isExistsOperationalVolatileField(fieldName)
    def readSystemRequestedState (self):
        fieldName = self.SYSTEM_REQUESTED_STATE
        return self._managerModuleCentralBlinkyDataEngine.readOperationalVolatileField(fieldName)
    def writeSystemRequestedState (self, data):
        fieldName = self.SYSTEM_REQUESTED_STATE
        self._managerModuleCentralBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

    def isDefinedSystemState (self):
        fieldName = self.SYSTEM_STATE
        return self._managerModuleCentralBlinkyDataEngine.isExistsOperationalVolatileField(fieldName)
    def readSystemState (self):
        fieldName = self.SYSTEM_STATE
        return self._managerModuleCentralBlinkyDataEngine.readOperationalVolatileField(fieldName)
    def writeSystemState (self, data):
        fieldName = self.SYSTEM_STATE
        self._managerModuleCentralBlinkyDataEngine.writeOperationalVolatileField(fieldName, data)

    def getSingleProcessBlinkyData (self, processName):
        if not processName in self._perProcessBlinkyData:
            self._perProcessBlinkyData[processName] = SingleProcessBlinkyData(processName, self._log)
            self._perProcessBlinkyData[processName].initBlinky(self._blinky)
        return self._perProcessBlinkyData[processName]        

    def getProcessesList (self):
        return self._blinky.keyPath(BlinkyKeyPath.PROCESS_TABLE_KEY_PATH).listDirectChildKeyPath()


class ManagerBlinkyCopy:

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_PROCESS_MANAGER, G_NAME_GROUP_PROCESS_MANAGER_BLINKY_COPY)
        self._cachedData = {}
        self._perProcessBlinkyCopy = {}

    def initBlinkyData (self, blinkyData):
        self._blinkyData = blinkyData

    def clearCachedData (self):
        self._cachedData = {}
        self._perProcessBlinkyCopy = {}

    def _genericUpdateField (self, noneIfNoData = False):
        callingFunction = sys._getframe(1).f_code.co_name
        fieldString=callingFunction[len("_refresh"):] 
        isDefinedFunction = getattr(self._blinkyData, "isDefined"+fieldString)               
        isDefinded = isDefinedFunction()
        #TODO(nirs) a lock is needed between the "isDefined" and the "read"         
        if isDefinded:
            readFunction = getattr(self._blinkyData, "read"+fieldString)
            value = readFunction()
            self._cachedData[fieldString] = value
        elif noneIfNoData:
            self._cachedData[fieldString] = None
        elif fieldString in self._cachedData:#removing already existing data when not defined
            self._cachedData.pop(fieldString)

    def _genericGetValue (self):
        callingFunction = sys._getframe(1).f_code.co_name
        fieldString=callingFunction[len("get"):] 
        return self._cachedData[fieldString]

    def _genericWriteValue (self,value):
        callingFunction = sys._getframe(1).f_code.co_name
        fieldString=callingFunction[len("write"):] 
        self._cachedData[fieldString]=value
        writeFunction = getattr(self._blinkyData, "write"+fieldString)
        writeFunction(self._cachedData[fieldString])


    def _refreshSystemDesiredState (self):
        self._genericUpdateField(noneIfNoData=True)#(noneIfNoData=True) for first round
    def getSystemDesiredState (self):
        return self._genericGetValue()
    def writeSystemDesiredState (self, data):
        self._genericWriteValue(data)

    def _refreshSystemRequestedState (self):
        self._genericUpdateField()
    def getSystemRequestedState (self):
        return self._genericGetValue()
    def writeSystemRequestedState (self, data):
        self._genericWriteValue(data)

    def _refreshSystemState (self):
        self._genericUpdateField(noneIfNoData=True)#(noneIfNoData=True) for first round
    def getSystemState (self):
        return self._genericGetValue()
    def writeSystemState (self, data):
        self._genericWriteValue(data)


    def refreshFromBlinky (self):
        self._cachedData = {}
        self._refreshSystemDesiredState()
        self._refreshSystemRequestedState()
        self._refreshSystemState()
        knownProcessesList = self._blinkyData.getProcessesList()
        for processName in sorted(self._perProcessBlinkyCopy):
            if not processName in knownProcessesList:
                #fatal - not supported
                a.infra.process.processFatal("Process %s disappeared from blinky '%s'", processName)
        for processName in sorted(knownProcessesList):
            if not processName in sorted(self._perProcessBlinkyCopy):
                self._perProcessBlinkyCopy[processName] = SingleProcessBlinkyCopy(self._log)
                self._perProcessBlinkyCopy[processName].initBlinkyData(self._blinkyData.getSingleProcessBlinkyData(processName))
        for processName in sorted(self._perProcessBlinkyCopy):
            self._perProcessBlinkyCopy[processName].refreshFromBlinky()

    def getProcessesList (self):
        return sorted(self._perProcessBlinkyCopy)

    def getSingleProcessBlinkyCopy (self, processName):
        return self._perProcessBlinkyCopy[processName]





class SingleProcessBlinkyInitCfgWriter(a.sys.blinky.pearl.BlinkyInitCfgWriter):
    def __init__(self,logger):
        a.sys.blinky.pearl.BlinkyInitCfgWriter.__init__(self,logger)

    def _refreshExecutable (self):
        self._genericUpdateField()
    def getExecutable (self):
        return self._genericGetValue()
    def setDefaultExecutable (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultExecutable (self):
        self._genericCommitDefault()

    def _refreshExtraArgs (self):
        self._genericUpdateField()
    def getExtraArgs (self):
        return self._genericGetValue()
    def setDefaultExtraArgs (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultExtraArgs (self):
        self._genericCommitDefault()

    def _refreshCwd (self):
        self._genericUpdateField()
    def getCwd (self):
        return self._genericGetValue()
    def setDefaultCwd (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultCwd (self):
        self._genericCommitDefault()

    def _refreshRedirectDir (self):
        self._genericUpdateField()
    def getRedirectDir (self):
        return self._genericGetValue()
    def setDefaultRedirectDir (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultRedirectDir (self):
        self._genericCommitDefault()

    def _refreshOsEnv (self):
        self._genericUpdateField()
    def getOsEnv (self):
        return self._genericGetValue()
    def setDefaultOsEnv (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultOsEnv (self):
        self._genericCommitDefault()

    def _refreshChrootDir (self):
        self._genericUpdateField()
    def getChrootDir (self):
        return self._genericGetValue()
    def setDefaultChrootDir (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultChrootDir (self):
        self._genericCommitDefault()

    def _refreshInitParamFilesDir (self):
        self._genericUpdateField()
    def getInitParamFilesDir (self):
        return self._genericGetValue()
    def setDefaultInitParamFilesDir (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultInitParamFilesDir (self):
        self._genericCommitDefault()

    def _refreshMainLoopSleepTime (self):
        self._genericUpdateField()
    def getMainLoopSleepTime (self):
        return self._genericGetValue()
    def setDefaultMainLoopSleepTime (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultMainLoopSleepTime (self):
        self._genericCommitDefault()

    def _refreshAffinity (self):
        self._genericUpdateField()
    def getAffinity (self):
        return self._genericGetValue()
    def setDefaultAffinity (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultAffinity (self):
        self._genericCommitDefault()

    def _refreshStateTransitionTimeout (self):
        self._genericUpdateField()
    def getStateTransitionTimeout (self):
        return self._genericGetValue()
    def setDefaultStateTransitionTimeout (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultStateTransitionTimeout (self):
        self._genericCommitDefault()

    def _refreshStateTransitionWarningThreshold (self):
        self._genericUpdateField()
    def getStateTransitionWarningThreshold (self):
        return self._genericGetValue()
    def setDefaultStateTransitionWarningThreshold (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultStateTransitionWarningThreshold (self):
        self._genericCommitDefault()

    def _refreshWatchdogTimeout (self):
        self._genericUpdateField()
    def getWatchdogTimeout (self):
        return self._genericGetValue()
    def setDefaultWatchdogTimeout (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultWatchdogTimeout (self):
        self._genericCommitDefault()

    def _refreshWatchdogWarningThreshold (self):
        self._genericUpdateField()
    def getWatchdogWarningThreshold (self):
        return self._genericGetValue()
    def setDefaultWatchdogWarningThreshold (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultWatchdogWarningThreshold (self):
        self._genericCommitDefault()

    def _refreshKillTimeout (self):
        self._genericUpdateField()
    def getKillTimeout (self):
        return self._genericGetValue()
    def setDefaultKillTimeout (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultKillTimeout (self):
        self._genericCommitDefault()

    def _refreshKillWarningThreshold (self):
        self._genericUpdateField()
    def getKillWarningThreshold (self):
        return self._genericGetValue()
    def setDefaultKillWarningThreshold (self,value):
        self._genericSetDefaultValue(value)
    def _commitDefaultKillWarningThreshold (self):
        self._genericCommitDefault()

    def refreshFromBlinky(self):
        self.clearCachedData()
        self._refreshExecutable()
        self._refreshExtraArgs()
        self._refreshCwd()
        self._refreshRedirectDir()
        self._refreshOsEnv()
        self._refreshChrootDir()
        self._refreshInitParamFilesDir()
        self._refreshMainLoopSleepTime()
        self._refreshAffinity()
        self._refreshStateTransitionTimeout()
        self._refreshStateTransitionWarningThreshold()
        self._refreshWatchdogTimeout()
        self._refreshWatchdogWarningThreshold()
        self._refreshKillTimeout()
        self._refreshKillWarningThreshold()

    def commitAllDefaults (self):
        self._commitDefaultExecutable()
        self._commitDefaultExtraArgs()
        self._commitDefaultCwd()
        self._commitDefaultRedirectDir()
        self._commitDefaultOsEnv()
        self._commitDefaultChrootDir()
        self._commitDefaultInitParamFilesDir()
        self._commitDefaultMainLoopSleepTime()
        self._commitDefaultAffinity()
        self._commitDefaultStateTransitionTimeout()
        self._commitDefaultStateTransitionWarningThreshold()
        self._commitDefaultWatchdogTimeout()
        self._commitDefaultWatchdogWarningThreshold()
        self._commitDefaultKillTimeout()
        self._commitDefaultKillWarningThreshold()





