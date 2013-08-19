#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import time
import datetime
import a.infra.process
import a.sys.blinky.pearl

import blinky_copy
from common import ProcessState
if  __package__ is None:
    G_NAME_MODULE_PROCESS_MANAGER = "unknown"
    G_NAME_GROUP_PROCESS_MANAGER_AGENT = "unknown"
else:
    from . import G_NAME_MODULE_PROCESS_MANAGER 
    from . import G_NAME_GROUP_PROCESS_MANAGER_AGENT

class Agent(object):
    _ourStateTransitionFunctionTable = {}

    def init (self, captain):
        """Init the process manager agent.

        An init funnction that must be called before using the PmAgent

        Args:
            captain: An application specific captain. Must inherit from "captain"

        Returns:
            None

        Raises:
            None
        """
        self._captain = captain

    def _setActualState (self, state):
        self._log("actual-state-change").debug1("changing the actual state from '%s' tp '%s'", self._actualState, state)
        self._actualState = state
        self._blinkData.writeActualState(self._actualState)

    def _dormant2Passive (self):
        self._setActualState(ProcessState.DORMANT_TO_PASSIVE)

        #TODO(nirs) maybe move to captain
        affinity = self._blinkData.readAffinity()
        if affinity is not None:
            #TODO(nirs) implement
            a.infra.process.processFatal("Affinity is set to '%s'. not supported", affinity)

        #TODO(nirs) maybe move to captain
        osEnv = self._blinkData.readOsEnv()
        if osEnv is not None:
            #TODO(nirs) implement
            a.infra.process.processFatal("OS-env is set to '%s'. not supported", osEnv)

        #TODO(nirs) maybe move to captain
        rootDir = self._blinkData.readChrootDir()
        if rootDir is not None:
            #TODO(nirs) implement
            a.infra.process.processFatal("Root-dir is set to '%s'. not supported", rootDir)
                
        self._captain.dormant2Passive()
        self._setActualState(ProcessState.PASSIVE)
    _ourStateTransitionFunctionTable[(ProcessState.DORMANT,ProcessState.PASSIVE)]=_dormant2Passive

    def _passive2Active (self):
        self._setActualState(ProcessState.PASSIVE_TO_ACTIVE)
        self._captain.passive2Active()
        self._setActualState(ProcessState.ACTIVE)
    _ourStateTransitionFunctionTable[(ProcessState.PASSIVE,ProcessState.ACTIVE)]=_passive2Active

    def _active2Up (self):
        self._setActualState(ProcessState.ACTIVE_TO_UP)
        self._captain.active2Up()
        self._setActualState(ProcessState.UP)        
    _ourStateTransitionFunctionTable[(ProcessState.ACTIVE,ProcessState.UP)]=_active2Up

    def _up2Active (self):
        self._setActualState(ProcessState.UP_TO_ACTIVE)
        self._captain.up2Active()
        self._setActualState(ProcessState.ACTIVE)        
    _ourStateTransitionFunctionTable[(ProcessState.UP,ProcessState.ACTIVE)]=_up2Active

    def _active2Passive (self):
        self._setActualState(ProcessState.ACTIVE_TO_PASSIVE)
        self._captain.active2Passive()
        self._setActualState(ProcessState.PASSIVE)        
    _ourStateTransitionFunctionTable[(ProcessState.ACTIVE,ProcessState.PASSIVE)]=_active2Passive

    def _passive2Dormant (self):
        self._setActualState(ProcessState.PASSIVE_TO_DORMANT)
        self._captain.passive2Dormant()
        self._setActualState(ProcessState.DORMANT)
    _ourStateTransitionFunctionTable[(ProcessState.PASSIVE,ProcessState.DOWN)]=_passive2Dormant

    def _getMainLoopSleepTime (self):
        return self._blinkData.readMainLoopSleepTime()

    def run (self):
        a.infra.process.setGlobalCaptain(self._captain)        
        self._captain.earlyInit() 
        mainLoggerManager = a.infra.log.main_logger.MainLogger.s_getFromOsefOrCrash(self._captain.getOsef()).getLoggerManager()
        self._log = mainLoggerManager.createLogger(G_NAME_MODULE_PROCESS_MANAGER, G_NAME_GROUP_PROCESS_MANAGER_AGENT)
        self._osef = self._captain.getOsef()

        processName = self._captain.getProcessName()
        self._blinkData = blinky_copy.SingleProcessBlinkyData(processName, self._log)#TODO(nirs) move to blinky data
        self._blinkData.initBlinky(self._osef[a.sys.blinky.pearl.Blinky.OSEF_KEY])

        """starting the application and mediate between it and the process manager"""
        self._actualState = self._blinkData.readActualState()
        self._log("reading-initial-state").debug1('initial state is %s', self._actualState)

        
        while True:
            self._captain.checkOk()
            self._blinkData.writeWatchdogMark(str(datetime.datetime.now()))
            desiredState = self._blinkData.readDesiredState()
            if self._actualState == desiredState:
                #in the desired state, can rest
                self._log("waiting-on-state").debug5("waiting on state: '%s'", desiredState)
                time.sleep(self._getMainLoopSleepTime())
                continue;

            #moving between states            
            nextState = ProcessState.s_getNextStableState(self._actualState, desiredState)
            self._log("move-between-states").notice('Moving from state %s to state %s aiming state %s',self._actualState, nextState, desiredState)

            if (self._actualState, nextState) in self._ourStateTransitionFunctionTable:
                self._ourStateTransitionFunctionTable[(self._actualState, nextState)](self)
            else:
                a.infra.process.processFatal("Transition between states is not defined. from: '%s', to '%s'", self._actualState, nextState)

            if self._actualState == ProcessState.DORMANT:                
                self._log("reached-dormant").notice('Process reached dormant state, end of process manager agent loop')
                self._captain.lateShutdown()
                return 0

