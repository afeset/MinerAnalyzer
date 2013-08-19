#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import signal

import a.infra.process
import common

from process_base import ProcessBase, StateMachine

class ProcessSimple(ProcessBase):
    def __init__ (self, name, logger, isBlocking):#last args come from derived
        ProcessBase.__init__(self, name, logger)
        self._isBlocking = isBlocking
        self._actualState = common.ProcessState.DOWN
        self._desiredState = None


    def init (self, executable, extraArgs, redirectDir=None, cwd=None, osEnv=None, affinity = None, chrootDir = None, 
              stateTransitionTimeout=None, stateTransitionWarningThreshold = None, watchdogTimeout = None, watchdogWarningThreshold = None,
              killTimeout = None, killWarningThreshold = None):
        self._executable = executable
        self._extraArgs = extraArgs
        self._redirectDir = redirectDir
        self._cwd = cwd
        self._osEnv = osEnv
        self._affinity = affinity
        self._chrootDir = chrootDir
        self._stateTransitionTimeout = stateTransitionTimeout
        self._stateTransitionWarningThreshold = stateTransitionWarningThreshold
        self._watchdogTimeout = watchdogTimeout
        self._watchdogWarningThreshold = watchdogWarningThreshold
        self._killTimeout = killTimeout
        self._killWarningThreshold = killWarningThreshold
        self._log("init-simple").debug2("a simple process '%s' was init: "
                                        "executable = '%s', "
                                        "extraArgs = '%s', "
                                        "redirectDir = '%s', "
                                        "cwd = '%s', "
                                        "osEnv = '%s', "
                                        "affinity = '%s', "
                                        "chrootDir = '%s', "
                                        "stateTransitionTimeout = '%s', "
                                        "stateTransitionWarningThreshold = '%s', "
                                        "watchdogTimeout = '%s', "
                                        "watchdogWarningThreshold = '%s', "
                                        "killTimeout = '%s', "
                                        "killWarningThreshold = '%s', ",
                                        self.getName(), executable, extraArgs, redirectDir, cwd, osEnv, affinity, chrootDir,
                                        stateTransitionTimeout, stateTransitionWarningThreshold ,
                                        watchdogTimeout, watchdogWarningThreshold, killTimeout, killWarningThreshold)

    def launch (self):
        self._setDesiredState(common.ProcessState.PASSIVE)#simulating the state machine
        self._launch()
        if self.getIsBlocking():
            self._log("wait-for-simple-process").info("waiting for process '%s'", self.getName())
            self._waitPid()            
            rc = self._getReturnCode()
            self._log("simple-process-returned").info("process '%s' returned with code '%s'", self.getName(), rc)
            if rc != 0:
                self._log("failed-launching-blocking").error("Failed launching process '%s'", self.getName())
                return False                    
        else:# a non blocking process - we expect it to keep on living
            if not self._getIsRunning():
                self._log("failed-launching-non-blocking").error("Failed launching process '%s' - process is already down", self.getName())
                return False
        return True#success
                    
        

    def stop (self):  
        terminationSignal = signal.SIGTERM
        terminationTimeout = None
        if not self._getStateTransitionTimeout() is None:
            terminationTimeout = self._getStateTransitionTimeout()
        #TODO(nirs) when supporting getting down by the state machine, self._setDesiredState(common.ProcessState.Down) simulating the state machine      
        self._log("stopping-simple-process").notice("stopping process '%s'", self.getName())
        self._log("stopping-simple-process-debug").debug2("stopping process '%s', terminationSignal='%s', terminationTimeout='%s'", 
                                                          self.getName(), terminationSignal, terminationTimeout)
        self._stop(terminationTimeout, terminationSignal)
        self._log("simple-process-stopped").info("process '%s' was stopped", self.getName())

#---------------------------------------------------------------------------------------------
    def updateStatus (self):                
        self._prevActualState = self._actualState
        changeReason = ""
        if not self._getIsRunning():
            #process was found down
            self._log("simple-update-status-down").debug5("process '%s' is not running - setting actual state to down", self.getName())
            changeReason = "process is not running"
            self._actualState = common.ProcessState.DOWN            
        elif self._desiredState is not None:
            if self._desiredState == common.ProcessState.DOWN:
                #BUG - must not happen as we do not take such processes down
                a.infra.process.processFatal("desired state of simple process '%s' was found to be DOWN - it cannot be", self.getName())
            #simulating the actual state by the desired state
            self._actualState = self._desiredState
            changeReason = "process desired state was set"
        
        self._log("simple-update-status").debug5("process '%s' updateStatus resulted with actual-state = %s", self.getName(), self._actualState)
        if self._actualState!=self._prevActualState:
            self._log("simple-actual-state-changed").debug1("process '%s' actual state chnaged from '%s' to '%s' due to %s", 
                                                            self.getName(), self._prevActualState, self._actualState, changeReason)
        
        self._testWatchdog()

    def _testWatchdog (self):
        #just kick it - we have no information to work on
        self._log("simple-test-watchdog").debug5("process '%s' test watchdog - just kicking", self.getName())
        if self._actualState != common.ProcessState.DOWN:
            self._timer.kick()        

    def getDesiredState (self):        
        return self._desiredState

    def getActualState (self):
        return self._actualState

    def _getPrevActualState (self):
        return self._prevActualState

    def _getInitialMachineState (self):
        #TODO(nirs) recover in case of failures
        return StateMachine.s_processStateToMachineState(self.getActualState())


    def _setDesiredState (self, state):
        self._desiredState = state
        if state == common.ProcessState.DOWN and self._getIsRunning():
            a.infra.process.processFatal("Setting the desired state of the simple process '%s' to DOWN - not supported", self.getName())
            #TODO(nirs) when supporting simple processes that get be taken down by PM itself - take the process down in such cases            


    def getProcessType (self):
        return common.ProcessType.SIMPLE

    def getIsBlocking (self):
        return self._isBlocking

    def getMinLevelPmCanTakeDown (self):
        return common.ProcessState.PASSIVE

    def _getCommandLine (self):
        cmd = [self._getExecutable()]
        if self._getExtraArgs() is not None:
            cmd+=[self._getExtraArgs().split()]
        return cmd        
    def _getExecutable (self):
        return self._executable
    def _getExtraArgs (self):
        return self._extraArgs
    def _getRedirectDir (self):
        return self._redirectDir
    def _getCwd (self):
        return self._cwd
    def _getOsEnv (self):
        return self._osEnv
    def _getAffinity (self):
        return self._affinity
    def _getChrootDir (self):
        return self._chrootDir
    def _getStateTransitionTimeout (self):
        return self._stateTransitionTimeout
    def _getStateTransitionWarningThreshold (self):
        return self._stateTransitionWarningThreshold
    def _getWatchdogTimeout (self):
        return self._watchdogTimeout
    def _getWatchdogWarningThreshold (self):
        return self._watchdogWarningThreshold
    def _getKillTimeout (self):
        return self._killTimeout
    def _getKillWarningThreshold (self):
        return self._killWarningThreshold

    def _preExecute (self):        
        pass

    def _launch (self):
        if self._getIsRunning():
            a.infra.process.processFatal("Failed launching process '%s' - process is already running", self.getName())
        self._log("launching-simple-process").notice("launching process '%s'", self.getName())
        self._preExecute()
        self._actualState = common.ProcessState.DORMANT        
        self._run()        


