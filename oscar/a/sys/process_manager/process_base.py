#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import os
import signal
import datetime
import subprocess
import a.infra.process

if  __package__ is None:
    G_NAME_MODULE_PROCESS_MANAGER = "unknown"
    G_NAME_GROUP_PROCESS_MANAGER_PROCESS_TIMER = "unknown"
    G_NAME_GROUP_PROCESS_MANAGER_PROCESS_STATE_MACHINE = "unknown"
    G_NAME_GROUP_PROCESS_MANAGER_PROCESS = "unknown"
else:
    from . import G_NAME_MODULE_PROCESS_MANAGER 
    from . import G_NAME_GROUP_PROCESS_MANAGER_PROCESS_TIMER
    from . import G_NAME_GROUP_PROCESS_MANAGER_PROCESS_STATE_MACHINE
    from . import G_NAME_GROUP_PROCESS_MANAGER_PROCESS

import common

class TerminationTimer:
    """This class implements a 2 stage timer that monitors a process. 
    When the first reaches its timeout a "termination" function is called and the second timer starts
    When the second timer is running the timer can no longer be be used with the regulat operations. 
    when the second timer is reached a "kill" function is called"""
    _OUR_INFINIT_DELTA =  datetime.timedelta(365*1000) #~1K years. Quite enough

    def __init__ (self, name, logger):
        self._name = name
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_PROCESS_MANAGER_PROCESS_TIMER)
        self._startDescription = None
        self._reset()

    def _reset (self):
        self._log("reset").debug2("timer '%s' is being reset", self._name)

        self._startTime = None
        self._isTerminationWarningThresholdReached = False
        self._isTerminating = False

        self._secondPhaseStartTime = None
        self._isKillWarningThresholdReached = False
        self._isKilled = False
        

    def init (self, terminationFunction, terminationWarningFunction, killTimeout, killFunction, killWarningThreshold, killWarningFunction):
        self._log("init").debug1("timer '%s' is being init. params: killTimeout='%s', killWarningThreshold='%s'", 
                                 self._name, killTimeout, killWarningThreshold)

        self._reset()
        
        self._terminationFunction = terminationFunction
        self._terminationWarningFunction = terminationWarningFunction

        self._killTimeout = self._OUR_INFINIT_DELTA
        if not killTimeout is None:
            self._killTimeout = datetime.timedelta(0, killTimeout)
        self._killFunction = killFunction

        self._killWarningTimeout = self._OUR_INFINIT_DELTA
        if (not killTimeout is None) and (not killWarningThreshold is None):
            self._killWarningTimeout = datetime.timedelta(0, killWarningThreshold*killTimeout)        
        self._killWarningFunction = killWarningFunction

    def start (self, terminationTimeout, terminationWarningThreshold, description):
        """starting the timer"""
        if self._isTerminating:
            #already reached the first ("termination") timeout - not regular operations can be done
            self._log("start-discarded").debug1("starting timer '%s' - discarded (already terminating)", self._name)
            return#moved to second state - cannot go back

        self._log("start").debug1("starting timer '%s'. params: terminationTimeout='%s', terminationWarningThreshold='%s', description = '%s'", 
                                  self._name, terminationTimeout, terminationWarningThreshold, description)

        #reset for the case of "start" after "start" with no stop in the middle
        self._reset()

        self._startDescription = description
        self._terminationTimeout = self._OUR_INFINIT_DELTA
        if not terminationTimeout is None:
            self._terminationTimeout = datetime.timedelta(0, terminationTimeout)
        
        self._terminationWarningTimeout = self._OUR_INFINIT_DELTA
        if (not terminationTimeout is None) and (not terminationWarningThreshold is None):
            self._terminationWarningTimeout = datetime.timedelta(0, terminationWarningThreshold*terminationTimeout)        

        self._startTime = datetime.datetime.now()

    def getLastStartDescription (self):
        return self._startDescription

    def kick (self):        
        if self._isTerminating:
             #already reached the first ("termination") timeout - "kick" came to late....
            self._log("kick-discarded").debug4("kicking timer '%s' - discarded (already terminating)", self._name)
            return #moved to second state - cannot go back

        self._log("kick").debug5("kicking timer '%s' (start descriptions: '%s')", self._name, self._startDescription)
        self._isTerminationWarningThresholdReached = False
        self._startTime = datetime.datetime.now()

    
    def test (self):
        """Synchronic timer test"""
        if self._startTime is None: #timer was not started
            self._log("test-empty").debug5("cannot test timer '%s'. was not started", self._name)
            return #Nothing to do - was not started yet

        currentTime = datetime.datetime.now()

        #first phase
        if not self._isTerminating:
            delta = currentTime-self._startTime
            if not self._isTerminationWarningThresholdReached:
                if delta >= self._terminationWarningTimeout:
                    self._log("reached-termination-warning").debug1("Timer '%s' reached the termination warning threshold of '%s' (start descriptions: '%s')", 
                                                                    self._name, self._terminationWarningTimeout, self._startDescription)
                    self._isTerminationWarningThresholdReached = True
                    if self._terminationWarningFunction:
                        (self._terminationWarningFunction)()

            if delta >= self._terminationTimeout:
                self._log("reached-termination").debug1("Timer '%s' reached the termination timeout of '%s' (start descriptions: '%s')", 
                                                        self._name, self._terminationTimeout, self._startDescription)
                self.moveToTerminating()
            return#end of first phase. 

        #second phase
        if not self._isKilled:
            delta = currentTime-self._secondPhaseStartTime
            if not self._isKillWarningThresholdReached:
                if delta >= self._killWarningTimeout:
                    self._log("reached-kill-warning").debug1("Timer '%s' reached the kill warning threshold of '%s' (start descriptions: '%s')", 
                                                              self._name, self._killWarningTimeout, self._startDescription)
                    self._isKillWarningThresholdReached = True
                    if self._killWarningFunction:
                        (self._killWarningFunction)()
    
            if delta >= self._killTimeout:
                self._isKilled = True
                self._log("reached-kill").debug1("Timer '%s' reached the kill timeout of '%s' (start descriptions: '%s')", 
                                                  self._name, self._killWarningTimeout, self._startDescription)
                if self._killFunction:
                    (self._killFunction)()

    def moveToTerminating (self):
        if not self._isTerminating:
            self._log("moving-to-termination").debug1("Timer '%s' is moving to termination phase (start descriptions: '%s')", 
                                                  self._name, self._startDescription)
            self._isTerminating = True
            self._secondPhaseStartTime = datetime.datetime.now()
            if self._terminationFunction:
                (self._terminationFunction)()


    def fullReset (self):        
        self._log("stop").debug1("reset timer '%s' (start descriptions: '%s')", self._name, self._startDescription)
        self._reset()







class StateMachine:
    """This class hold implements the state machine for the process"""

    #state machine inputs for every round
    INPUT_SYSTEM_STATE = "system-state"
    INPUT_PROCESS_ACTUAL_STATE = "process-actual-state"

    ####Machine states
    #stable states
    DOWN = "down"
    PASSIVE = "passive"
    ACTIVE = "active"
    UP = "up"
    ourStableStates = [DOWN, PASSIVE, ACTIVE, UP]
    #transinision states
    DOWN_TO_PASSIVE = "down-to-passive"
    PASSIVE_TO_DOWN = "passive-to-down"
    PASSIVE_TO_ACTIVE = "passive-to-active"
    ACTIVE_TO_PASSIVE = "active-to-passive"
    ACTIVE_TO_UP = "active-to-up"
    UP_TO_ACTIVE = "up-to-active"

    #allowed transitions
    ourGoingUpStates = [DOWN, DOWN_TO_PASSIVE, PASSIVE, PASSIVE_TO_ACTIVE, ACTIVE, ACTIVE_TO_UP, UP]
    ourGoingDownStates = [UP, UP_TO_ACTIVE, ACTIVE, ACTIVE_TO_PASSIVE, PASSIVE, PASSIVE_TO_DOWN, DOWN]

    ourFollowingDesiredState = {DOWN:common.ProcessState.DOWN,
                                PASSIVE:common.ProcessState.PASSIVE,
                                ACTIVE:common.ProcessState.ACTIVE,
                                UP:common.ProcessState.UP,
                                DOWN_TO_PASSIVE:common.ProcessState.PASSIVE,                                
                                PASSIVE_TO_ACTIVE:common.ProcessState.ACTIVE,
                                ACTIVE_TO_UP:common.ProcessState.UP,
                                UP_TO_ACTIVE:common.ProcessState.ACTIVE,
                                ACTIVE_TO_PASSIVE:common.ProcessState.PASSIVE,
                                PASSIVE_TO_DOWN:common.ProcessState.DOWN}

    def __init__ (self, processName, lastProcessStateWhenGoingDown, logger):
        self._processName = processName
        self._lastMachineStateWhenGoingDown = self.s_processStateToMachineState(lastProcessStateWhenGoingDown)
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_PROCESS_MANAGER_PROCESS_STATE_MACHINE)
        self._state = None
        self._systemState = None
        self._processActualState = None
        self._processNextDesiredState = None
                

    def setInitialState (self, machineState):
        """a function that has to be called before using the state machine - learning the initial state of the system"""
        if machineState is None:
            self._log("initial-state-default").debug1("setting initial state for process process '%s' got 'None'. will Use the default 'DOWN' value", self._processName)
            machineState = self.DOWN
        self._setState(machineState)
        self._processNextDesiredState = self.ourFollowingDesiredState[machineState] #for consistency
    
    def advance (self, inputDictionary):     
        """this is the primay function of the state machine. 
        it gets a dictionary (with the "INPUT_***" keys) as an input and producess the outputs (to be reached using separate functions)"""

        #reading the input
        systemState = inputDictionary[self.INPUT_SYSTEM_STATE]
        if self._systemState != systemState:
            self._log("system-state-changed").debug1("system state was changed: from '%s' to '%s'", self._systemState, systemState)
        self._systemState = systemState

        processActualState = inputDictionary[self.INPUT_PROCESS_ACTUAL_STATE]
        if self._processActualState != processActualState:
            self._log("process-actual-state-changed").debug1("process actual state was changed: from '%s' to '%s'", self._processActualState, processActualState)
        self._processActualState = processActualState

        self._inputDictionary = inputDictionary

        self._log("advance").debug5("calling state machine of process '%s'. newState='%s', processActualState='%s', systemState='%s'",
                                    self._processName, self._state, self._processActualState, self._systemState)

        #clean outputs
        self._shallStartTimer = False
        self._shallResetTimer = False
        self._shallTerminateProcess = False
        #common state machine advace
        if self._doAllStates():
            self._log("do-on-all").debug1("doAllStates return True, skipping main state machine")
        else:
            #specific state machine pass
            self.ourStateMachine[self._state](self)

        self._log("advance-done").debug5("called state machine of process '%s'. currentState='%s', nextDesiredState='%s', shallStartTimer='%s', shallResetTimer='%s', shallTerminateProcess = '%s'",
                                         self._processName, self._state, self._processNextDesiredState, self._shallStartTimer, self._shallResetTimer, self._shallTerminateProcess)

    #state machine outputs
    def getState (self):
        return self._state

    def getIsInStableState (self):
        return self._state in self.ourStableStates

    def getProcessNextDesiredState (self):
        return self._processNextDesiredState

    def getShallStartTimer (self):
        return self._shallStartTimer

    def getShallResetTimer (self):
        return self._shallResetTimer

    def getShallTerminateProcess (self):
        return self._shallTerminateProcess


    @classmethod
    def s_processStateToMachineState (cls, processState):
        if   processState == common.ProcessState.DOWN              : return cls.DOWN             
        elif processState == common.ProcessState.PASSIVE           : return cls.PASSIVE          
        elif processState == common.ProcessState.ACTIVE            : return cls.ACTIVE           
        elif processState == common.ProcessState.UP                : return cls.UP               
        elif processState == common.ProcessState.DORMANT           : return cls.DOWN_TO_PASSIVE         
        elif processState == common.ProcessState.DORMANT_TO_PASSIVE: return cls.DOWN_TO_PASSIVE  
        elif processState == common.ProcessState.PASSIVE_TO_DORMANT: return cls.PASSIVE_TO_DOWN  
        elif processState == common.ProcessState.PASSIVE_TO_ACTIVE : return cls.PASSIVE_TO_ACTIVE
        elif processState == common.ProcessState.ACTIVE_TO_PASSIVE : return cls.ACTIVE_TO_PASSIVE
        elif processState == common.ProcessState.ACTIVE_TO_UP      : return cls.ACTIVE_TO_UP     
        elif processState == common.ProcessState.UP_TO_ACTIVE      : return cls.UP_TO_ACTIVE     
        else:
            a.infra.process.processFatal("Failed calculating next state. Invalid process state: '%s'", processState)

    def _setState (self, state):
        self._log("state-changed").debug1("changing state. from '%s', to '%s'", self._state, state)
        self._state = state

    def _setProcessNextDesiredState (self, processNextDesiredState):
        self._log("setting-next-desired-state").debug2("setting process next desired state to to '%s'", processNextDesiredState)
        self._processNextDesiredState = processNextDesiredState

    def _doAllStates (self):                
        if self._state != self.DOWN and self._processActualState == common.ProcessState.DOWN:
            #found the process to be down while it was not expected to
            self._setState(self.DOWN) 
            if self.getProcessNextDesiredState() != common.ProcessState.DOWN:
                self._log("process-down").warning("process %s was found to be down due to %s", self._processName, "XYZ") #TODONOW(nirs) log on failure reason
            self._setProcessNextDesiredState(common.ProcessState.DOWN)#for consistency            
            self._shallResetTimer = True
            return True

        #found the process not down but in an unexpected state 
        if self._processActualState != self._processNextDesiredState and self.s_processStateToMachineState(self._processActualState) != self._state:
            #something really bad happend - inconsistency. let kill the process                       
            self._log("state-inconsistency").warning("process %s was found to be in an inconsitent state and shall be terminated."
                                                     "self._processActualState=%s; self._processNextDesiredState=%s; "
                                                     "self.s_processStateToMachineState(self._processActualState)=%s; self._state=%s", 
                                                     self._processName, self._processActualState, self._processNextDesiredState,
                                                     self.s_processStateToMachineState(self._processActualState), self._state) 
            self._shallTerminateProcess = True
            return True

        return False

    def _shallAvoidTransitionWhenGoingDown (self):
        return (self.ourGoingDownStates.index(self.getState()) >= self.ourGoingDownStates.index(self._lastMachineStateWhenGoingDown))

    def _advance_down (self):
        if self._systemState == common.SystemState.DOWN_TO_PASSIVE:
            self._setProcessNextDesiredState(self.ourFollowingDesiredState[self._systemState])#(common.ProcessState.PASSIVE)
            self._setState(self.DOWN_TO_PASSIVE)
            self._shallStartTimer = True

    def _advance_passive (self):
        if self._systemState == common.SystemState.PASSIVE_TO_ACTIVE:
            self._setProcessNextDesiredState(self.ourFollowingDesiredState[self._systemState])#(common.ProcessState.ACTIVE)
            self._setState(self.PASSIVE_TO_ACTIVE)
            self._shallStartTimer = True
        if self._systemState == common.SystemState.PASSIVE_TO_DOWN:
            if not self._shallAvoidTransitionWhenGoingDown():
                self._setProcessNextDesiredState(self.ourFollowingDesiredState[self._systemState])#(common.ProcessState.DOWN)
                self._setState(self.PASSIVE_TO_DOWN)
                self._shallStartTimer = True
            else:
                self._log("skip-transition").debug4("process '%s' ignoring system state '%s' due to min machine state '%s' (current machine state '%s')", 
                                                    self._processName, self._systemState, self._lastMachineStateWhenGoingDown, self.getState())


    def _advance_active (self):
        if self._systemState == common.SystemState.ACTIVE_TO_UP:
            self._setProcessNextDesiredState(self.ourFollowingDesiredState[self._systemState])#(common.ProcessState.UP)
            self._setState(self.ACTIVE_TO_UP)
            self._shallStartTimer = True
        if self._systemState == common.SystemState.ACTIVE_TO_PASSIVE:
            if not self._shallAvoidTransitionWhenGoingDown():
                self._setProcessNextDesiredState(self.ourFollowingDesiredState[self._systemState])#(common.ProcessState.PASSIVE)
                self._setState(self.ACTIVE_TO_PASSIVE)
                self._shallStartTimer = True
            else:
                self._log("skip-transition").debug1("process '%s' ignoring system state '%s' due to min machine state '%s' (current machine state '%s')", 
                                                    self._processName, self._systemState, self._lastMachineStateWhenGoingDown, self.getState())
            

    def _advance_up (self):
        if self._systemState == common.SystemState.UP_TO_ACTIVE:
            if not self._shallAvoidTransitionWhenGoingDown():
                self._setProcessNextDesiredState(self.ourFollowingDesiredState[self._systemState])#(common.ProcessState.ACTIVE)
                self._setState(self.UP_TO_ACTIVE)
                self._shallStartTimer = True
            else:
                self._log("skip-transition").debug1("process '%s' ignoring system state '%s' due to min machine state '%s' (current machine state '%s')", 
                                                    self._processName, self._systemState, self._lastMachineStateWhenGoingDown, self.getState())

    def _advance_downToPassive (self):
        if self._processActualState == common.ProcessState.PASSIVE:
            self._setState(self.PASSIVE)
            self._shallStartTimer = True
        
    def _advance_passiveToActive (self):
        if self._processActualState == common.ProcessState.ACTIVE:
            self._setState(self.ACTIVE)
            self._shallStartTimer = True

    def _advance_activeToUp (self):
        if self._processActualState == common.ProcessState.UP:
            self._setState(self.UP)
            self._shallStartTimer = True

    def _advance_upToActive (self):
        if self._processActualState == common.ProcessState.ACTIVE:
            self._setState(self.ACTIVE)
            self._shallStartTimer = True

    def _advance_activeToPassive (self):
        if self._processActualState == common.ProcessState.PASSIVE:
            self._setState(self.PASSIVE)
            self._shallStartTimer = True

    def _advance_passiveToDown (self):
        pass #wating to the process to get down



    ourStateMachine = {}
    ourStateMachine[DOWN] = _advance_down
    ourStateMachine[PASSIVE] = _advance_passive
    ourStateMachine[ACTIVE] = _advance_active
    ourStateMachine[UP] = _advance_up
    ourStateMachine[DOWN_TO_PASSIVE] = _advance_downToPassive
    ourStateMachine[PASSIVE_TO_DOWN] = _advance_passiveToDown
    ourStateMachine[PASSIVE_TO_ACTIVE] = _advance_passiveToActive
    ourStateMachine[ACTIVE_TO_PASSIVE] = _advance_activeToPassive
    ourStateMachine[ACTIVE_TO_UP] = _advance_activeToUp
    ourStateMachine[UP_TO_ACTIVE] = _advance_upToActive






class ProcessBase:
    def __init__ (self, name, logger):
        self._name = name
        self._log = logger.createLogger(G_NAME_MODULE_PROCESS_MANAGER, G_NAME_GROUP_PROCESS_MANAGER_PROCESS, instance = self._name)
        self._subprocess = a.infra.subprocess.Subprocess(self._name, self._log)
        self._stateMachine = StateMachine(self._name, self.getMinLevelPmCanTakeDown(), self._log)
        self._timer = TerminationTimer(self._name, self._log)
    
    #base public functions
    def getName (self):
        return self._name

    def initManager (self, manager):
        self._manager = manager

    def getMachineState (self):
        return self._stateMachine.getState()

    def advance (self):
        """using the already gathered data to advance the state machine"""

        #the timer tests what ever needed
        self._timer.test()

        #Doing whatever needed to be done when actual state was changed
        if self._getPrevActualState() != self.getActualState():
            self._log("do-on-actual-state-change").debug3("calling to _doAfterActualStateChange")
            self._doAfterActualStateChange(self._getPrevActualState(), self.getActualState())

        #moving the state machine
        stateMachineInput = {}
        stateMachineInput[StateMachine.INPUT_SYSTEM_STATE] = self._manager.getSystemState()
        stateMachineInput[StateMachine.INPUT_PROCESS_ACTUAL_STATE] = self.getActualState()
        self._stateMachine.advance(stateMachineInput)
        
        #using the calculated data and acting upon it
        nextDesiredState = self._stateMachine.getProcessNextDesiredState()
        if self.getDesiredState() != nextDesiredState:
            self._log("desired-state-change").info("changing the desired state from '%s' to '%s'", 
                                                    self.getDesiredState(), nextDesiredState)
            self._doBeforeDesiredStateChange(self.getDesiredState(), nextDesiredState, self.getActualState())
            self._setDesiredState(nextDesiredState)
        if self.getActualState() == common.ProcessState.DOWN and self.getDesiredState() != common.ProcessState.DOWN:
            self._log("launching-due-to-state").notice("process is down and launched due to desired state '%s'", 
                                                     self.getDesiredState())
            self._launch()
            self._initTimer()


        if self._stateMachine.getShallResetTimer():
            self._log("full-reset-timer").debug1("process '%s' full reset the timer (start description: '%s')", 
                                                 self._name, self._timer.getLastStartDescription())
            self._timer.fullReset()

        if self._stateMachine.getShallStartTimer():
            self._startTimer()

        if self._stateMachine.getShallTerminateProcess():
            self._log("terminating-on-machine-request").notice("process '%s' is being terminated on the state-machine request", self._name)
            self._log("terminating-on-machine-request-debug").debug1("process '%s' is being terminated on the machine request. actual state: '%s', machine state: '%s'", 
                                                                     self._name, self.getActualState(), self._stateMachine.getState())
            self._timer.moveToTerminating()


    def learnInitialMachineState (self):        
        state = self._getInitialMachineState()
        self._log("learning-initial-state").debug1("process '%s' learned the initial machine state to be: '%s'", 
                                                   self._name, state)
        self._stateMachine.setInitialState(state)

    def _launch (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")


    def _initTimer (self):
        self._log("init-timer").debug1("process '%s' re-init the timer", self._name)

        #the function used to terminate the process
        def failureTerminationFunction ():            
            self._log("terminating-process").error("Terminating process '%s' (start description: %s)", 
                                                     self.getName(), self._timer.getLastStartDescription())
            self._log("terminating-process-more").debug1("reached termination timeout of process '%s' (start description: %s). current state '%s'", 
                                                     self.getName(), self._timer.getLastStartDescription(), self._stateMachine.getState())
            self._subprocess.terminate(terminationSignal = signal.SIGTERM)

        #the function emmiting when terminating the process is near
        def terminationWarningFunction ():
            self._log("termination-process-th").warning("reached termination warning threshold of process '%s' (start description: %s)", 
                                                        self.getName(), self._timer.getLastStartDescription())

        #the function used to kill the process
        def killFunction ():
            self._log("killing-process").error("reached kill timeout of process '%s' (start description: %s)", 
                                               self.getName(), self._timer.getLastStartDescription())
            self._log("killing-process-more").debug1("reached kill timeout of process '%s' (start description: %s). current state '%s'", 
                                                     self.getName(), self._timer.getLastStartDescription(), self._stateMachine.getState())
            self._subprocess.kill()

        #the function emmiting when killing the process is near
        def killWarningFunction ():
            self._log("killing-process-th").warning("reached kill warning threshold of process '%s' (start description: %s)", 
                                                    self.getName(), self._timer.getLastStartDescription())


        self._timer.init(terminationFunction = failureTerminationFunction, 
                         terminationWarningFunction = terminationWarningFunction, 
                         killTimeout = self._getKillTimeout(), 
                         killFunction = killFunction, 
                         killWarningThreshold = self._getKillWarningThreshold(), 
                         killWarningFunction=killWarningFunction)


    def _doAfterActualStateChange (self, prevState, newState):
        self._log("do-after-actual-state-change").debug1("process '%s' called 'doAfterActualStateChange(%s,%s)' empty implementation", 
                                                         self.getName(), prevState, newState)

    def _doBeforeDesiredStateChange (self, fromState, toState, actualState):
        self._log("do-before-desired-state-change").debug1("process '%s' called '_doBeforeDesiredStateChange()%s,%s,%s' empty implementation", 
                                                           self.getName(), fromState, toState, actualState)

    #functions managing operational data
    def updateStatus (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")

    def fullyStartTimer (self):
        self._initTimer()
        self._startTimer()
    
    def getDesiredState (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")

    def getActualState (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")

    def _getPrevActualState (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")

    def getActualStateStableFloorForStateMachine (self):
        return common.ProcessState.s_getStateStableFloor(self.getActualState())

    def getActualStateStableCeilForStateMachine (self):
        return common.ProcessState.s_getStateStableCeil(self.getActualState())

    def _getInitialMachineState (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")

    def _setActualState (self, state):
        self._pycheckerDummy = state
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")

    def _setDesiredState (self, state):
        self._pycheckerDummy = state
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")

    #functions for bringing configuration data
    def getProcessType (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def getIsBlocking (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def getMinLevelPmCanTakeDown (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")

    #functions for bringing configuration data for internal use
    def _getCommandLine (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getExecutable (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getExtraArgs (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getRedirectDir (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getCwd (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getOsEnv (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getAffinity (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getChrootDir (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getStateTransitionTimeout (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getStateTransitionWarningThreshold (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getWatchdogTimeout (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getWatchdogWarningThreshold (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getKillTimeout (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")
    def _getKillWarningThreshold (self):
        a.infra.process.processFatal("Running function dummy implementation (real implementaion need to reside at child class)")


    #Common infra functions
    def _startTimer (self):
        if self._stateMachine.getIsInStableState():
            timeout = self._getWatchdogTimeout()
            warnTh  = self._getWatchdogWarningThreshold()
            description = "watchdog timeout of '%s' seconds for stable state %s"%(timeout, self._stateMachine.getState())
        else:
            timeout = self._getStateTransitionTimeout()
            warnTh  = self._getStateTransitionWarningThreshold()
            description = "state transition timeout of '%s' seconds for transition state %s"%(timeout, self._stateMachine.getState())
        self._log("starting-the-timer").debug1("process '%s' starts the timer with the parameters: timeout: '%s', warnTh: '%s', description: '%s'", 
                                            self._name, timeout, warnTh, description)
        self._timer.start(timeout, warnTh, description)

    def _run (self):
        #running the process
        self._log("run").debug1("process '%s' called its '_run' command", self.getName())
        if self._getIsRunning():
            a.infra.process.processFatal("trying to launch an living process '%s' (pid = '%d')", self.getName(), self._subprocess.getPid())

        stdoutFileName = None
        stderr=None
        if self._getRedirectDir() != None:
            a.infra.file.utils.makeDirs(self._getRedirectDir(), reuseExisting=True)
            stdoutFileName = os.path.join(self._getRedirectDir(),'stdout'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S.%f")+'.txt')
            stderr = subprocess.STDOUT

        cwd = None
        if self._getCwd() != None:
            cwd = self._getCwd()

        env = None
        if self._getOsEnv() != None:
            env = self._getOsEnv()

        #affinity = None #TODO(nirs) fill up
        if self._getAffinity() != None:
            self._log("affinity-not-supported").error("trying to launch process '%s' and setting its affinity to '%s'. Not implemented yet", self.getName(), self._getAffinity())

        #chrootDir = None #TODO(nirs) fill up
        if self._getChrootDir() != None:
            self._log("root-dir-not-supported").error("trying to launch process '%s' and setting its root-dir to '%s'. Not implemented yet", self.getName(), self._getChrootDir())

        self._log("launch-params").debug1("process '%s' is being launched. commandLine='%s'; stdoutFileName='%s'; cwd='%s'; env='%s'", 
                                          self.getName(), self._getCommandLine(), stdoutFileName, cwd, env)
        
        self._subprocess.start(self._getCommandLine(), stdoutFileName = stdoutFileName, stderr = stderr, cwd = cwd, env = env)
        self._log("launched").info("process '%s' is launched. pid='%s'", self.getName(), self.getPid())

    def _waitPid (self):
        self._subprocess.waitPid()

    def getPid (self):
        return self._subprocess.getPid()

    def _getReturnCode (self):
        return self._subprocess.getReturnCode()

    def _getIsRunning (self):
        return self._subprocess.isUp()

    def _stop (self, terminationTimeout, terminationSignal):
        self._subprocess.stop(terminationTimeout, terminationSignal)



