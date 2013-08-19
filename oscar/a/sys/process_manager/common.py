#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import a.infra.process

class ProcessState:
    """ A class of constants for specifying process state"""
    #stable states
    DOWN = "down"
    PASSIVE = "passive"
    ACTIVE = "active"
    UP = "up"

    #transinision states
    DORMANT = "dormant"
    DORMANT_TO_PASSIVE = "dormant-to-passive"
    PASSIVE_TO_DORMANT = "passive-to-dormant"
    PASSIVE_TO_ACTIVE = "passive-to-active"
    ACTIVE_TO_PASSIVE = "active-to-passive"
    ACTIVE_TO_UP = "active-to-up"
    UP_TO_ACTIVE = "up-to-active"

    PASSIVE_FAILED = "passive-failed"
    PASSIVE_FAILED_FREEZED = "passive-failed-freezed"
    ACTIVE_FAILED = "active-failed"
    ACTIVE_FAILED_FREEZED = "active-failed-freezed"
    UP_FAILED = "up-failed"
    UP_FAILED_FREEZED = "up-failed-freezed"

    ourStableStates        = [DOWN  , PASSIVE  , ACTIVE  , UP  ]

    ourTransitionStatesStableFloor =   {DORMANT: DOWN, 
                                        DORMANT_TO_PASSIVE:DOWN, 
                                        PASSIVE_TO_DORMANT:DOWN, 

                                        PASSIVE_TO_ACTIVE:PASSIVE, 
                                        ACTIVE_TO_PASSIVE:PASSIVE, 

                                        ACTIVE_TO_UP:ACTIVE, 
                                        UP_TO_ACTIVE:ACTIVE,

                                        PASSIVE_FAILED:DOWN,
                                        PASSIVE_FAILED_FREEZED:DOWN,
                                        ACTIVE_FAILED:DOWN,
                                        ACTIVE_FAILED_FREEZED:DOWN,
                                        UP_FAILED:DOWN,
                                        UP_FAILED_FREEZED:DOWN}

    ourTransitionStatesStableCeil =     {DORMANT: PASSIVE, 
                                         DORMANT_TO_PASSIVE:PASSIVE, 
                                         PASSIVE_TO_DORMANT:PASSIVE, 

                                         PASSIVE_TO_ACTIVE:ACTIVE, 
                                         ACTIVE_TO_PASSIVE:ACTIVE, 

                                         ACTIVE_TO_UP:UP, 
                                         UP_TO_ACTIVE:UP,

                                         PASSIVE_FAILED:PASSIVE,
                                         PASSIVE_FAILED_FREEZED:PASSIVE,
                                         ACTIVE_FAILED:ACTIVE,
                                         ACTIVE_FAILED_FREEZED:ACTIVE,
                                         UP_FAILED:UP,
                                         UP_FAILED_FREEZED:UP}

    @classmethod
    def s_getIsStableState (cls, state):
        return (state in cls.ourStableStates)

    @classmethod
    def s_getStableStateIndex (cls, state):
        if not state in cls.ourStableStates:
            a.infra.process.processFatal("source state '%s' is not a stabe state", state) 
        return cls.ourStableStates.index(state)

    @classmethod
    def s_getStateStableFloor (cls, state):
        if state in cls.ourStableStates:
            return state
        if not state in cls.ourTransitionStatesStableFloor:
            a.infra.process.processFatal("source state '%s' does not have infimum", state) 
        return cls.ourTransitionStatesStableFloor[state]

    @classmethod
    def s_getStateStableCeil (cls, state):
        if state in cls.ourStableStates:
            return state
        if not state in cls.ourTransitionStatesStableCeil:
            a.infra.process.processFatal("source state '%s' does not have infimum", state) 
        return cls.ourTransitionStatesStableCeil[state]


    @classmethod
    def s_getNextStableState(cls, sourceStableState, targetStableState):
        if sourceStableState == cls.DORMANT:#needed for the aent - this is the first state it sees 
                                            #but it is not in the stable list
            sourceStableState = cls.DOWN
        sourceIndex = cls.s_getStableStateIndex(sourceStableState)
        targetIndex = cls.s_getStableStateIndex(targetStableState)
        if sourceIndex > targetIndex:
            nextIndex = sourceIndex-1
        if sourceIndex < targetIndex:
            nextIndex = sourceIndex+1
        if sourceIndex == targetIndex:
            nextIndex = sourceIndex
        return cls.ourStableStates[nextIndex]


class SystemDesiredState:
    """ A class of constants for specifying the system state"""
    DOWN = "down"
    UP = "up"

class SystemState:
    #stable states
    DOWN = "down"
    UP = "up"
    #transinision states
    DOWN_TO_PASSIVE = "down-to-passive"
    PASSIVE_TO_DOWN = "passive-to-down"
    PASSIVE_TO_ACTIVE = "passive-to-active"
    ACTIVE_TO_PASSIVE = "active-to-passive"
    ACTIVE_TO_UP = "active-to-up"
    UP_TO_ACTIVE = "up-to-active"


class ProcessType:
    """ A class of constants for specifying the system state"""
    FLEX = "flex"
    SIMPLE = "simple"

