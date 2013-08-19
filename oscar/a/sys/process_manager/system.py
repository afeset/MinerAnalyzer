#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 


import time
import a.infra.subprocess
import process_flex
import process_simple

import blinky_copy
import common
if  __package__ is None:
    G_NAME_MODULE_PROCESS_MANAGER = "unknown"
    G_NAME_GROUP_PROCESS_MANAGER_SYSTEM_STATE_MACHINE  = "unknown"
    G_NAME_GROUP_PROCESS_MANAGER_MANAGER  = "unknown"
else:
    from . import G_NAME_MODULE_PROCESS_MANAGER 
    from . import G_NAME_GROUP_PROCESS_MANAGER_SYSTEM_STATE_MACHINE
    from . import G_NAME_GROUP_PROCESS_MANAGER_MANAGER


class StateMachine:
    """This class hold implements the state machine for the system state"""

    #state machine inputs for every round
    INPUT_SYSTEM_DESIRED_STATE = "system-desired-state"
    INPUT_MIN_PROCESS_STATE = "min-process-state"
    INPUT_MAX_PROCESS_STATE = "max-process-state"
            
    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_PROCESS_MANAGER_SYSTEM_STATE_MACHINE)
        self._shallQuit = False
        self._systemDesiredState = None
        self._minProcessState = None
        self._maxProcessState = None


    def learnInitialState (self):
        """a function that has to be called before using the state machine - learning the initial state of the system"""
        #TODO(nirs) recover based on data from blinky. 
        self._state = common.SystemState.DOWN_TO_PASSIVE
        self._log("advance").debug1("system state machine initial state was learnd to be '%s'", self._state)


    def advance (self, inputDictionary):
        """this is the primay function of the state machine. 
        it gets a dictionary (with the "INPUT_***" keys) as an input and producess the outputs (to be reached using separate functions)"""

        self._log("advance").debug5("calling system state machine 'advance' function. input: '%s'", inputDictionary)

        systemDesiredState = inputDictionary[self.INPUT_SYSTEM_DESIRED_STATE]
        if self._systemDesiredState != systemDesiredState:
            self._log("system-desired-state-changed").notice("system desired state was changed: from '%s' to '%s'", self._systemDesiredState, systemDesiredState)
        self._systemDesiredState = systemDesiredState

        minProcessState = inputDictionary[self.INPUT_MIN_PROCESS_STATE]
        if self._minProcessState != minProcessState:
            self._log("min-process-state-changed").info("system min process state was changed: from '%s' to '%s'", self._minProcessState, minProcessState)
        self._minProcessState = minProcessState

        maxProcessState = inputDictionary[self.INPUT_MAX_PROCESS_STATE]
        if self._maxProcessState != maxProcessState:
            self._log("max-process-state-changed").info("system max process state was changed: from '%s' to '%s'", self._maxProcessState, maxProcessState)
        self._maxProcessState = maxProcessState

        #calling the right function according to our state
        (self.ourStateMachine[self._state])(self)
        self._log("advance-done").debug5("called system state machine 'advance' function resulted with. getSystemState: %s, getShallQuit: '%s'", 
                                         self.getSystemState(), self.getShallQuit())


    #state machine output functions
    def getSystemState (self):
        return self._state

    def getShallQuit (self):
        return self._shallQuit


    
    def _setState (self, state):
        if state != self._state:
            self._log("state-changed").notice("system state machine is changing state. from '%s', to '%s'", self._state, state)
            self._state = state

    def _calcNextStateGoingUp (self, processStateToWaitOn, nextSystemStateWhenAllGoesWell):
        if self._minProcessState == processStateToWaitOn: 
            #need to stay as is - the min process havent changed
            return self._state
        if self._minProcessState == common.ProcessState.DOWN: 
            #a process crashed
            return common.SystemState.DOWN_TO_PASSIVE
        currentIndex = common.ProcessState.s_getStableStateIndex (processStateToWaitOn)
        newIndex = common.ProcessState.s_getStableStateIndex (self._minProcessState)
        if currentIndex > newIndex:
            #really weird - process went states downward but is not down
            self._log("step-back").warning("min process state changed to '%s' while '%s' was expected", self._minProcessState, processStateToWaitOn)
            return common.SystemState.DOWN_TO_PASSIVE
        elif not nextSystemStateWhenAllGoesWell is None:#currentIndex < newIndex
            #going in the right direction
            return nextSystemStateWhenAllGoesWell
        else:
            a.infra.process.processFatal("Failed calculating next state on up - this shall never happen.")#TODO(nirs) system fatal

    def _calcNextStateGoingDown (self, processStateToWaitOn, nextSystemStateWhenAllGoesWell):
        if self._maxProcessState == processStateToWaitOn: 
            #need to stay as is - max process havent changed
            return self._state
        currentIndex = common.ProcessState.s_getStableStateIndex (processStateToWaitOn)
        newIndex = common.ProcessState.s_getStableStateIndex (self._maxProcessState)
        if currentIndex < newIndex:
            #really weird - process went states upward but is not down
            a.infra.process.processFatal("Failed calculating next state while going down - found a state which is to high." 
                                         "system state ='%s', max process state ='%s'.", self._state, self._maxProcessState)#TODO(nirs) system fatal
        else:#currentIndex > newIndex
            #well done, lets go the the next state
            return nextSystemStateWhenAllGoesWell
            
    def _advance_down (self):
        if self._systemDesiredState == common.SystemDesiredState.UP:
            self._shallQuit = False
            self._setState(common.SystemState.DOWN_TO_PASSIVE)
        else:
            self._shallQuit = True

    def _advance_downToPassive (self):
        if self._systemDesiredState == common.SystemDesiredState.UP:
            self._setState(self._calcNextStateGoingUp(common.ProcessState.DOWN, common.SystemState.PASSIVE_TO_ACTIVE))
        else:
            self._setState(common.SystemState.UP_TO_ACTIVE)

    def _advance_passiveToActive (self):
        if self._systemDesiredState == common.SystemDesiredState.UP:
            self._setState(self._calcNextStateGoingUp(common.ProcessState.PASSIVE, common.SystemState.ACTIVE_TO_UP))
        else:
            self._setState(common.SystemState.UP_TO_ACTIVE)

    def _advance_activeToUp (self):
        if self._systemDesiredState == common.SystemDesiredState.UP:
            self._setState(self._calcNextStateGoingUp(common.ProcessState.ACTIVE, common.SystemState.UP))
        else:
            self._setState(common.SystemState.UP_TO_ACTIVE)

    def _advance_up (self):
        if self._systemDesiredState == common.SystemDesiredState.UP:
            self._setState(self._calcNextStateGoingUp(common.ProcessState.UP, None))
        else:
            self._setState(common.SystemState.UP_TO_ACTIVE)


    def _advance_upToActive (self):
        if self._systemDesiredState == common.SystemDesiredState.UP:
            pass #when starting to go down - we go all the way and only then rise back
        else:
            self._setState(self._calcNextStateGoingDown(common.ProcessState.UP, common.SystemState.ACTIVE_TO_PASSIVE))

    def _advance_activeToPassive (self):
        if self._systemDesiredState == common.SystemDesiredState.UP:
            pass #when starting to go down - we go all the way and only then rise back
        else:
            self._setState(self._calcNextStateGoingDown(common.ProcessState.ACTIVE, common.SystemState.PASSIVE_TO_DOWN))

    def _advance_passiveToDown (self):
        if self._systemDesiredState == common.SystemDesiredState.UP:
            pass #when starting to go down - we go all the way and only then rise back
        else:
            self._setState(self._calcNextStateGoingDown(common.ProcessState.PASSIVE, common.SystemState.DOWN))


    ourStateMachine = {}
    ourStateMachine[common.SystemState.DOWN] = _advance_down
    ourStateMachine[common.SystemState.UP] = _advance_up
    ourStateMachine[common.SystemState.DOWN_TO_PASSIVE] = _advance_downToPassive
    ourStateMachine[common.SystemState.PASSIVE_TO_DOWN] = _advance_passiveToDown
    ourStateMachine[common.SystemState.PASSIVE_TO_ACTIVE] = _advance_passiveToActive
    ourStateMachine[common.SystemState.ACTIVE_TO_PASSIVE] = _advance_activeToPassive
    ourStateMachine[common.SystemState.ACTIVE_TO_UP] = _advance_activeToUp
    ourStateMachine[common.SystemState.UP_TO_ACTIVE] = _advance_upToActive
            



class Manager:
    """The manager is the one to test the state of all the processes and decide what to do using the state machine"""
    SLEEP_TIME = 0.1#TODO(nirs) move to blinky
    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_PROCESS_MANAGER, G_NAME_GROUP_PROCESS_MANAGER_MANAGER)
        self._processes = {}
        self._stateMachine = StateMachine(self._log)
        self._systemDesiredState = None

    def initBlinky (self, blinky):
        """this function must be called before using the class"""
        self._blinky = blinky
        self._blinkyData = blinky_copy.ManagerBlinkyData(self._log)
        self._blinkyData.initBlinky(self._blinky)
        self._blinkyCopy = blinky_copy.ManagerBlinkyCopy(self._log)
        self._blinkyCopy.initBlinkyData(self._blinkyData)        

    def executeProcess (self, processSimple):
        """launchiung a simple process"""
        if not isinstance(processSimple, process_simple.ProcessSimple):
            a.infra.process.processFatal("Failed launching process '%s' - invalid type", processSimple.getName())

        processSimple.initManager(self)
                
        if not processSimple.getIsBlocking():
            if processSimple.getName() in self._processes:
                #this is really weird - or a bug of the developer that will be found on simple tests. Or PM bug.
                #Not smart to proceed
                a.infra.process.processFatal("Re-adding process with name '%s'", processSimple.getName())
            self._log("adding-simple").debug1("adding a new simple process '%s' to the processes list", processSimple.getName())
            self._processes[processSimple.getName()] = processSimple

        self._log("execute").notice("executing process %s", processSimple.getName())
        return processSimple.launch()


    def stopProcess (self, processName):
        """stopping a simple process"""
        if not processName in self._processes:
            self._log("terminate-process-not-found").error("Trying to terminate process '%s' - no such process held", processName)
            return
        processSimple = self._processes[processName]
        if processSimple.getProcessType()!=common.ProcessType.SIMPLE:
            a.infra.process.processFatal("Failed stopping process '%s' - invalid type", processSimple.getName())

        self._log("removing-simple").debug1("removing a simple process '%s' from the processes list", processSimple.getName())
        self._processes.pop(processName)
        self._log("stop").notice("stopping process %s", processSimple.getName())
        processSimple.stop()
        self._log("stop-done").info("process %s is now down", processSimple.getName())

    def getSystemState (self):
        return self._stateMachine.getSystemState()        
            
    def _initAndAddToBlinkyExistingSimpleProcesses (self):    
        for processName in self._processes:
            process = self._processes[processName]
            if process.getProcessType()!=common.ProcessType.SIMPLE:
                a.infra.process.processFatal("Adding to blinky as simple process a none simple process '%s' ", process.getName())
            process.learnInitialMachineState()
            process.fullyStartTimer()
            self._log("add-simple-to-blinky").info("adding a simple process '%s' to the blinky list", process.getName())
            processBlinkyData = self._blinkyData.getSingleProcessBlinkyData(process.getName())
            processBlinkyData.writePid(process.getPid())
            processBlinkyData.writeActualState(process.getActualState())
            processBlinkyData.writeDesiredState(process.getDesiredState())
            processBlinkyData.writeMachineState(process.getMachineState())

    def _scanForNewFlexProcesses (self):
        for processName in self._blinkyCopy.getProcessesList():
            if not processName in self._processes:
                #a new process or an existing proces after PM crash
                blinkyCopy = self._blinkyCopy.getSingleProcessBlinkyCopy(processName)
                if blinkyCopy.getIsBlocking():
                    continue#not a managed process
                if blinkyCopy.getProcessType() != common.ProcessType.FLEX:
                    a.infra.process.processFatal("A non 'flex' process was added to blinky - process name '%s'", processName)
                self._log("new-in-blinky").notice("found a new process '%s' in the blinky list", processName)
                newProcess = process_flex.ManagedFlexProcess(processName, self._log)
                newProcess.initManager(self)
                newProcess.initBlinky(self._blinky, self._blinkyData.getSingleProcessBlinkyData(processName), blinkyCopy)
                newProcess.learnInitialMachineState()
                self._processes[processName] = newProcess


    def _updateStatus (self):
        self._log("update-status").debug5("update status was called")
        self._calcSystemDesiredState()
        self._learnProcessesStatus()
        

    def _calcSystemDesiredState (self):
        newSystemDesiredState = self._blinkyCopy.getSystemRequestedState()
        self._log("calc-desired-state").debug5("desired state was calced to be %s", newSystemDesiredState)
        if newSystemDesiredState!= self._systemDesiredState:
            self._log("system-desired-change").notice("system desired state is changed from '%s' to '%s'", 
                                                      self._systemDesiredState, newSystemDesiredState)
            self._systemDesiredState = newSystemDesiredState        


    def _learnProcessesStatus (self):
        self._minProcessState = common.ProcessState.UP
        self._maxProcessState = common.ProcessState.DOWN
        for processName in sorted(self._processes):
            process = self._processes[processName]

            actualStateFloor = process.getActualStateStableFloorForStateMachine ()
            actualStateFloorIndex = common.ProcessState.s_getStableStateIndex(actualStateFloor)
            minStateIndex = common.ProcessState.s_getStableStateIndex(self._minProcessState)
            if actualStateFloorIndex < minStateIndex:
                self._minProcessState = actualStateFloor

            actualStateCeil = process.getActualStateStableCeilForStateMachine ()
            actualStateCeilIndex = common.ProcessState.s_getStableStateIndex(actualStateCeil)
            actualStatePmCanReach = process.getMinLevelPmCanTakeDown()
            actualStatePmCanReachIndex = common.ProcessState.s_getStableStateIndex(actualStatePmCanReach)
            if actualStateCeilIndex > actualStatePmCanReachIndex:
                maxStateIndex = common.ProcessState.s_getStableStateIndex(self._maxProcessState)
                if actualStateCeilIndex > maxStateIndex:
                    self._maxProcessState = actualStateCeil

        self._log("learn-process-status").debug5("discover that minProcessState='%s' and maxProcessState='%s'", 
                                                 self._minProcessState, self._maxProcessState)

    def _advance (self):      
        stateMachineInput = {}
        stateMachineInput[StateMachine.INPUT_SYSTEM_DESIRED_STATE] = self._systemDesiredState
        stateMachineInput[StateMachine.INPUT_MIN_PROCESS_STATE] = self._minProcessState
        stateMachineInput[StateMachine.INPUT_MAX_PROCESS_STATE] = self._maxProcessState
        self._stateMachine.advance(stateMachineInput)

        self._log("advance").debug5("at the end of the state machine: systemState='%s'", self._stateMachine.getSystemState())

        if self._blinkyCopy.getSystemState()!=self._stateMachine.getSystemState():
            self._blinkyCopy.writeSystemState(self._stateMachine.getSystemState())
        if self._blinkyCopy.getSystemDesiredState()!=self._systemDesiredState:
            self._blinkyCopy.writeSystemDesiredState(self._systemDesiredState)
        

    def _writeAdditionaProcessesInfoToBlinky (self):
        """writing data to blinky per process. 
        flex processes might have been able to write this data on their own but simple would not be able to"""
        for processName in self._processes:
            process = self._processes[processName]
            blinkyCopy = self._blinkyCopy.getSingleProcessBlinkyCopy(processName)
            if blinkyCopy.getPid() != process.getPid():
                blinkyCopy.writePid(process.getPid())
            if blinkyCopy.getActualState() != process.getActualState():
                #This is sensitive as also the agent writes to the blinky data.
                #If the actual state has changed by us, thi means that it is changed to "down" and the
                #agent is not alive.
                #The way back is also sensitive: this code is called after the process is launched
                #so what we write might overun data writen by agent. 
                #In such cases the state is already writen when the process is launched by the flex process
                if blinkyCopy.getProcessType() == common.ProcessType.FLEX and process.getActualState() != common.ProcessState.DOWN:
                    self._log("race-with-agent").error("A bug! for some reason the process manager is trying to write to blinky the actual state when the flex process is up")
                else:
                    blinkyCopy.writeActualState(process.getActualState())
            if blinkyCopy.getDesiredState() != process.getDesiredState():
                blinkyCopy.writeDesiredState(process.getDesiredState())
            if blinkyCopy.getMachineState() != process.getMachineState():
                blinkyCopy.writeMachineState(process.getMachineState())


    def run (self):
        """main manager function"""

        #add already existing processes to blinky
        self._initAndAddToBlinkyExistingSimpleProcesses()
        #TODO(nirs) gather data from confd for state machine recovery
        self._stateMachine.learnInitialState()

        while True:
            self._log("new-round").debug5("new round")

            #gathering data
            self._blinkyCopy.refreshFromBlinky()

            self._scanForNewFlexProcesses()

            for processName in sorted(self._processes):
                self._processes[processName].updateStatus()
            self._updateStatus()

            #Doing the work
            self._advance()
            for processName in sorted(self._processes):
                self._processes[processName].advance()

            self._writeAdditionaProcessesInfoToBlinky()#TODO(nirs) late night solution - re think

            if self._stateMachine.getShallQuit():
                self._log("quit").notice("process-manager main loop ended")
                break

            time.sleep(self.SLEEP_TIME)

