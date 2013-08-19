#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# ver 1.0 
#
# Author: galm
#
########################################################################################################################
# 
# This file defines the data structures used to hold the counters information
#                                                                                                                      
########################################################################################################################

from my_hash import myHash
from UserString import MutableString
from enums import VariableTypes
from copy import copy

# This object describes a stats counter
class CounterDescriptor(object):
    def __init__(self):
        pass

    def init (self, samplingRate, counterPath, counterProcess, counterName, counterType, variableType, isRate,
              counterShortDescriptionString, archaives, properties, metaCounterExpression, commMethod, 
              presentCounterPerSecond, measuredUnits, minHeartbeat):

        #Sampling rate in seconds
        self.mySamplingRate = samplingRate
        #The path of the counter in the processes tree - just path not counter name. i.e. its PO path
        self.myCounterPath = counterPath
        #The name of the counter's process
        self.myCounterProcess = counterProcess
        # The method in which the couter is read from the process currently we support qshell and file methods
        self.myCommMethod = commMethod
        #The time of the counter. i.e. GAUGE/COUNTER/ABSOLUTE etc
        self.myCounterType = counterType    
        #Is this counter represent rate? should stats retrieve the rate value of this counter? True - Rate is fetched. False - Value is fetched.
        self.myIsRate = isRate
        self.myArchaives = archaives
        self.myProperties = properties
        #A very short description of the counter
        self.myCounterShortDescriptionString = counterShortDescriptionString
        #Expression that represents the arithmetic operations that needs to be done when **presenting** the counter - the cuonter is saved with original value!
        self.myMetaCounterExpression = metaCounterExpression
        #Indicated if the description of this counter was overriden by the configurations
        self.myCounterDescriptionIsOverride = False
        #Enum VariableTypes
        self.myVariableType = variableType
        self.myPresentCounterPerSecond = presentCounterPerSecond
        self.myMeasuredUnits = measuredUnits
        #RRD heartbeat
        self.myMinHeartbeat = minHeartbeat
        #Name based properties
        self.__initName(counterName)


    def toString (self):
        result = MutableString()

        result.append("Process name: %s " % self.myCounterProcess)
        result.append("Counter path: %s " % self.myCounterPath)
        result.append("Counter name: %s " % self.myCounterName)
        result.append("Counter name: %s " % self.myCounterSamplingName)
        result.append("Sampling rate: %s " % self.mySamplingRate)
        result.append("Counter Type: %s " % self.myCounterType)
        result.append("Counter Units: %s " % self.myMeasuredUnits)
        result.append("Counter present per second is: %s " % str(self.myPresentCounterPerSecond))
        result.append("Counter Id: %d " % self.myCounterId)
        result.append("Is rate? %s" % str(self.myIsRate))
        result.append("Counter short description: %s " % self.myCounterShortDescriptionString)
        result.append("Counter short description override flag: %s " % str(self.myCounterDescriptionIsOverride))
        result.append("Counter value variable type: %s " % self.myVariableType)
        result.append("Meta-Counter arithmetic expression: %s " % self.myMetaCounterExpression)
        result.append("Communication method: %s " % self.myCommMethod)
        result.append("RRD min heartbeat: %s " % self.myMinHeartbeat)

        for arch in self.myArchaives:
            result.append(arch.toString())

        for prop in self.myProperties:
            result.append(prop.toString())

        return result.data

    def __cmp__ (self, other):
        # Validate that the counter wasn't changed - this is a comparison of all the counters fields
        #
        # Note that myMinHeartbeat is not a part of the comparison because we do not want to take 
        # the chance that modifying the heartbeat will result with a new RRD file.
        # We explicitly write code to tune the RRD file.

        if self.mySamplingRate == other.mySamplingRate:
            if self.myCounterName == other.myCounterName:
                if self.myCounterSamplingName == other.myCounterSamplingName:
                    if self.myCounterPath == other.myCounterPath:
                        if self.myCounterProcess == other.myCounterProcess:
                            if self.myCounterType == other.myCounterType:
                                if self.myIsRate == other.myIsRate:
                                    if self.myVariableType == other.myVariableType:
                                        if self.myProperties == other.myProperties:
                                            if self.myArchaives == other.myArchaives:
                                                if self.myCommMethod == other.myCommMethod:
                                                    #If arrived here - success - everything is the same
                                                    return 0

        if self.myCounterId < other.myCounterId:
            return -1 
        return 1

    def setValuesBoundaries(self, minValue, maxValue):
        self.myMinValue = minValue
        self.myMaxValue = maxValue

    def getMinStr (self):
        if hasattr(self, 'myMinValue'):
            return str(self.myMinValue)
        return "U"

    def getMaxStr (self):
        if hasattr(self, 'myMaxValue'):
            return str(self.myMaxValue)
        return "U"

    def getMinHeartbeat (self):
        return self.myMinHeartbeat

    def cloneRealCounter (self, realCounterName):
        newCounter = copy(self) # Shallow copy
        #Recompute new values based on the new name
        newCounter.__initName(realCounterName)
        return newCounter

    def __initName (self, realCounterName):
        self.myCounterName = realCounterName+'_('+self.myCounterType+')'
        self.myCounterSamplingName = realCounterName
        #Communication and Aggregation will use counterID that equals a murmur3 hash on its path
        self.myCounterId = abs(myHash(self.myCounterPath+self.myCounterName+str(self.myIsRate)))

# This object describes an rrdtool archaive
class DataSetArchaive(object):
    def __init__(self):
        pass

    def init (self, archaiveType, errorsAllowed, consolidationSpan, rowsToKeep):
        self.myArchaiveType = archaiveType
        self.myErrorsAllowed = errorsAllowed
        self.myConsolidationSpan = consolidationSpan
        self.myRowsToKeep = rowsToKeep

    def toString (self):
        result = MutableString()
        result.append("Archaive type: %s" % self.myArchaiveType)
        result.append("Archaive errors allowed: %s" % self.myErrorsAllowed)
        result.append("Archaive consolidation span: %d" % self.myConsolidationSpan)
        result.append("Archaive rows to keep: %d" % self.myRowsToKeep)
        return result.data

    def __cmp__ (self, other):
        if self.myArchaiveType == other.myArchaiveType:
            if self.myErrorsAllowed == other.myErrorsAllowed:
                if self.myConsolidationSpan == other.myConsolidationSpan:
                    if self.myRowsToKeep == other.myRowsToKeep:
                        #If arrived here - success - everything is the same
                        return 0

        #If you got here it means that a diff was found
        if self.myConsolidationSpan < other.myConsolidationSpan:
            return -1
        return 1

# This object describes a counter property
class CounterProperty(object):
    def __init__(self):
        pass

    def init (self, propName, propVariableType, propValue):
        self.myName = propName
        self.myVariableType = propVariableType
        self.myValue = propValue

    def toString (self):
        result = MutableString()
        result.append("Property name: %s" % self.myName)
        result.append("Property variable type: %s" % self.myVariableType)
        #Get the correct format according to the variable type
        frmt = "Property value: %s" % VariableTypes.FORMAT_BY_NAMES[self.myVariableType]
        result.append(frmt % self.myValue)
        return result.data

    def __cmp__ (self, other):
        if self.myName == other.myName:
            if self.myVariableType == other.myVariableType:
                if self.myValue == other.myValue:
                    #If arrived here - success - everything is the same
                    return 0
                else:
                    return self.myValue-other.myValue

        #If you got here it means that a diff was found
        if self.myName < other.myName:
            return -1
        return 1

