#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 


# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_POLL_SUPRERVISOR  = "unknown"
    G_GROUP_NAME_POLL_SUPRERVISOR_INTERNAL  = "unknown"

else:
    from . import G_GROUP_NAME_POLL_SUPRERVISOR
    from . import G_GROUP_NAME_POLL_SUPRERVISOR_INTERNAL

from a.infra.basic.return_codes import ReturnCodes
import monotonic_clock

class PollSupervisor:
    """ A class for supervisoring times things took
    """
    COUNTER_POLLS = "polls" #valid only for the pollCycle
    COUNTER_MISSED_POLLS = "missed-polls" #valid only for the pollCycle
    COUNTER_LATENCY_ERRORS = "latency-err" #valid only for the pollCycle
    COUNTER_LATENCY_WARNINGS = "latency-warn" #valid only for the pollCycle
    COUNTER_DURATION_ERRORS = "duration-err"
    COUNTER_DURATION_WARNINGS = "duration-warn"
    COUNTER_FAILURES = "failures" #not valid for the pollCycle
    COUNTER_SUCCESS = "success"   #not valid for the pollCycle
    COUNTER_TOTAL_NANO_SECONDS = "total-nano-seconds" #valid only for the pollCycle
    COUNTER_ACTIVE_NANO_SECONDS = "active-nano-seconds" #valid only for the pollCycle
    
    def __init__ (self, logger, name, pollCycleLogString):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_POLL_SUPRERVISOR, instance = name)        
        self._wasPollStarted = False
        self._pollCycleReporter = _Reporter(self._log, name+"-poll-cycle",  pollCycleLogString)    
        self._name = name
        self._tasksReporters = {}    
        self._tasksReporters[()] = self._pollCycleReporter

    def setPollCycleInterval (self, pollCycleInterval):
        self._pollCycleReporter.setRepeatInterval(pollCycleInterval)

    def setPollCycleLatencyThresholds (self, errorThreshold, warningThreshold):
        self._pollCycleReporter.setLatencyThreshold(errorThreshold, warningThreshold)

    def setPollCycleDurationThresholds (self, errorThreshold, warningThreshold):
        self._pollCycleReporter.setDurationThresholds(errorThreshold, warningThreshold)

    def addPollElement (self, elementKeyList, logString):
        if not isinstance(elementKeyList,list) or not elementKeyList:
            self._log("invalid-element").error("invalid poll key: %s", elementKeyList)
            return ReturnCodes.kGeneralError

        if len(elementKeyList) > 1:
            parentKey = elementKeyList[:-1]
            if not tuple(parentKey) in self._tasksReporters:
                self._log("no-parent").error("new element '%s' with parent element '%s' not existing: %s", 
                                             elementKeyList, parentKey)
                return ReturnCodes.kGeneralError

        self._tasksReporters[tuple(elementKeyList)] = _Reporter(self._log, 
                                                                self._name+"-"+"-".join(elementKeyList), 
                                                                logString)

    def setElementPollDurationThresholds (self, elementKeyList, errorThreshold, warningThreshold):
        if not tuple(elementKeyList) in self._tasksReporters:
            self._log("set-th-no-elem").error("trying to set thresholds for a non-existing element '%s'", elementKeyList)
            return ReturnCodes.kGeneralError

        self._tasksReporters[tuple(elementKeyList)].setDurationThresholds(errorThreshold, warningThreshold)

    def startPollCycle (self):
        if not self._wasPollStarted:
            self._pollCycleReporter.start(None)
            self._wasPollStarted = True
        else:
            self._pollCycleReporter.restart()

    def endPollCycle (self):
        self._pollCycleReporter.end(ReturnCodes.kOk)

    def isTimeToStartPollCycle (self):
        return self._pollCycleReporter.hasReachedRestartTime()

    def forceStart (self):
        self._pollCycleReporter.start(None)
        self._wasPollStarted = True

    def startElementPoll (self, elementKeyList, specificName):
        if not tuple(elementKeyList) in self._tasksReporters:
            self._log("start-no-elem").error("trying to set thresholds for a non-existing element '%s'", elementKeyList)
            return

        for partialKeyLen in range(0, len(elementKeyList)-1):
            parentKey = elementKeyList[:partialKeyLen]
            reporter = self._tasksReporters[tuple(parentKey)]
            if not reporter.isActive():
                self._log("start-parent-not").warning("starting element '%s(%s)' while parent '%s'  is not active", 
                                                      elementKeyList, specificName, parentKey)
            reporter.kickTimeCount()

        self._tasksReporters[tuple(elementKeyList)].start(specificName)        

    def endElementPoll (self, elementKeyList, returnCode = ReturnCodes.kOk):
        #the return code is of class "a.infra.basic.return_codes.ReturnCode"        
        if not tuple(elementKeyList) in self._tasksReporters:
            self._log("end-no-elem").error("trying to set thresholds for a non-existing element '%s'", elementKeyList)
            return

        self._tasksReporters[tuple(elementKeyList)].end(returnCode)

        for partialKeyLen in range(1, len(elementKeyList)):
            parentKey = elementKeyList[:partialKeyLen]
            reporter = self._tasksReporters[tuple(parentKey)]
            if not reporter.isActive():
                self._log("end-parent-not").warning("end element '%s' while parent '%s' is not active", 
                                                      elementKeyList, parentKey)
            reporter.kickTimeCount()


    def getPollCycleCounter (self, counterName):
        #counter name is one of the COUNTER_ constants in the begining of this class
        return self._pollCycleReporter.getCount(counterName)

    def clearPollCycleCounter (self, counterName):
        #counter name is one of the COUNTER_ constants in the begining of this class
        return self._pollCycleReporter.clearCount(counterName)

    def getElementPollCounter (self, elementKeyList, counterName):
        #counter name is one of the COUNTER_ constants in the begining of this class        
        if not tuple(elementKeyList) in self._tasksReporters:
            self._log("get-count-no-elem").error("trying to get counters for a non-existing element '%s'. return 0", elementKeyList)
            return 0
        return self._tasksReporters[tuple(elementKeyList)].getCount(counterName)

    def clearElementPollCounter (self, elementKeyList, counterName):
        #counter name is one of the COUNTER_ constants in the begining of this class
        if not tuple(elementKeyList) in self._tasksReporters:
            self._log("clear-count-no-elem").error("trying to clear counters for a non-existing element '%s'. return 0", elementKeyList)
            return 0
        return self._tasksReporters[tuple(elementKeyList)].clearCount(counterName)


    #####private stuff ######

class _Counter:
    def __init__ (self):
        self._count = 0
        self._clearCheckpointCount = 0

    def clear (self):
        self._clearCheckpointCount = self._count

    def getMonotonic (self):
        return self._count

    def getClearable (self):
        return self._count-self._clearCheckpointCount

    def inc (self, num=1):
        self._count += num

class _Reporter:
    def __init__ (self, logger, instanceName, logString):
        self._startCounter = _Counter()
        self._missCounter  = _Counter()
        self._durationErrorCounter = _Counter()
        self._durationWarningCounter = _Counter()
        self._latencyErrorCounter = _Counter()
        self._latencyWarningCounter = _Counter()
        self._failuresCounter = _Counter()
        self._successCounter = _Counter()
        self._totalNanoSecondsCounter = _Counter()
        self._activeNanoSecondsCounter = _Counter()
        self._reportingLog = logger.createLoggerSameModule(G_GROUP_NAME_POLL_SUPRERVISOR, instance = instanceName)
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_POLL_SUPRERVISOR_INTERNAL, instance = instanceName)    
        self._isWorking = False
        self._logString = logString    
        self._interval = None
        self._durationErrorThresholdNanoSeconds = 0
        self._durationWarningThresholdNanoSeconds = 0
        self._latencyErrorThresholdNanoSeconds = 0
        self._latencyWarningThresholdNanoSeconds = 0
        self._clearStart()


    def setDurationThresholds (self, errorThreshold, warningThreshold):             
        self._durationErrorThresholdNanoSeconds = int(errorThreshold * 1000 * 1000 * 1000)
        self._durationWarningThresholdNanoSeconds = int(warningThreshold * 1000 * 1000 * 1000)
        self._log("set-duration-th").debug3("setting a duration threshold: error: '%d', warning: '%d'", 
                                            self._durationErrorThresholdNanoSeconds,
                                            self._durationWarningThresholdNanoSeconds)            

    def setRepeatInterval (self, interval):
        if interval <= 0:
            self._log("invalid-interval").error("setting a repeated mode with invalid interval '%d'", 
                                                interval)            
        self._interval = int(interval * 1000 * 1000 * 1000)
        self._log("set-repeated").debug3("setting a repeated mode, with interval '%d'", self._interval)   
        
    def setLatencyThreshold (self, errorThreshold, warningThreshold):
        self._latencyErrorThresholdNanoSeconds = int(errorThreshold * 1000 * 1000 * 1000)
        self._latencyWarningThresholdNanoSeconds = int(warningThreshold * 1000 * 1000 * 1000)
        self._log("set-latency-th").debug3("setting a latency threshold: error: '%d', warning: '%d'", 
                                            self._latencyErrorThresholdNanoSeconds,
                                            self._latencyWarningThresholdNanoSeconds) 

    def start (self, name):        
        self._isWorking = True
        self._realStartTime = monotonic_clock.monotonicTimeNano()
        self._alignedStartTime = self._realStartTime
        self._totalNanoSecondsCounterRefernenceTime = self._realStartTime        
        self._activeNanoSecondsCounterRefernenceTime = self._realStartTime        
        self._specificName = name
        self._startCounter.inc()
        #no kickTimeCount as we just starting or getting out of "disabled"
        self._log("start").debug5("start. time '%d', name %s", self._realStartTime, self._specificName)            

    def restart (self):            
        self._log("start-again").debug5("start-again") 
        name = self._specificName
        if name is None:
            name = ""
        else:
            name = "(%s)"%name

        if self._alignedStartTime is None:
            self._log("start-again-start").error("called the 'restart' function with no 'start' function call")
            return

        if self._interval is None:
            self._log("start-again-no-interval").error("calling start-again with no repeatition set")            
            return

        self._startCounter.inc()        
        now = monotonic_clock.monotonicTimeNano()

        deltaT = now - self._alignedStartTime
        if self._latencyErrorThresholdNanoSeconds > 0 and (deltaT-self._interval) >= self._latencyErrorThresholdNanoSeconds:
            self._reportingLog("latency-error-th-reached").error("Reached the latency error threshold for %s%s: total time passed: %.03f sec >= %.03f sec",
                                                                 self._logString, name, 
                                                                 deltaT*1.0/1000/1000/1000,  
                                                                 self._latencyErrorThresholdNanoSeconds*1.0/1000/1000/1000)
            self._latencyErrorCounter.inc()

        elif self._latencyWarningThresholdNanoSeconds > 0 and (deltaT-self._interval) >= self._latencyWarningThresholdNanoSeconds:
            self._reportingLog("latency-warning-th-reached").warning("Reached the latency warning threshold for %s%s: total time passed: %.03f sec >= %.03f sec",
                                                                     self._logString, name, 
                                                                     deltaT*1.0/1000/1000/1000,
                                                                     self._latencyWarningThresholdNanoSeconds*1.0/1000/1000/1000)
            self._latencyWarningCounter.inc()
        
        passCycles = int(deltaT/self._interval)
        if passCycles > 1:
            self._reportingLog("miss").warning("Missed %d cycles", passCycles-1)
            self._missCounter.inc(passCycles-1)                
        self.kickTimeCount(now)#before changing _isWorking to True  as it uses it
        self._isWorking = True
        self._alignedStartTime = self._alignedStartTime + passCycles*self._interval
        self._realStartTime = now
        self._log("restart").debug5("started again - new base time %d", self._alignedStartTime)                        


    def hasReachedRestartTime (self):
        if self._alignedStartTime is None:
            self._log("try-reach-no-start").error("called the 'hasReachedRestartTime' function with no 'start' function call")
            return False

        if self._interval is None:
            self._log("try-reach-no-interval").error("calling 'hasReachedRestartTime' with no interval set")            
            return False

        now = monotonic_clock.monotonicTimeNano()
        #update the total time counter here for the "smoothness' of the counter.
        #We do not do it on the "get counter" as we don't have enough information maybe we are disabled)
        #and we are maybe in another thread...
        self.kickTimeCount(now)
        return now >= self._alignedStartTime+self._interval


    def end (self, returnCode):
        now = monotonic_clock.monotonicTimeNano()
        name = self._specificName
        if name is None:
            name = ""
        else:
            name = "(%s)"%name

        if not self._isWorking:
            self._log("end-no-start").error("called the 'end' function with no 'start' function call")
            return

        if not returnCode.success():
            self._reportingLog("failure").error("Failure in %s%s: %s",
                                                self._logString, name, returnCode)
            self._failuresCounter.inc()

        else:
            self._successCounter.inc()

        deltaT = now - self._realStartTime

        if self._durationErrorThresholdNanoSeconds > 0 and deltaT >= self._durationErrorThresholdNanoSeconds:
            self._reportingLog("dur-error-th-reached").error("Reached the duration error threshold for %s%s: total time passed: %.03f sec >= %.03f sec",
                                                             self._logString, name, 
                                                             deltaT*1.0/1000/1000/1000,
                                                             self._durationErrorThresholdNanoSeconds*1.0/1000/1000/1000)
            self._durationErrorCounter.inc()

        elif self._durationWarningThresholdNanoSeconds > 0 and deltaT >= self._durationWarningThresholdNanoSeconds:
            self._reportingLog("dur-warning-th-reached").warning("Reached the duration warning threshold for %s%s: total time passed: %.03f sec >= %.03f sec",
                                                                 self._logString, name, 
                                                                 deltaT*1.0/1000/1000/1000,
                                                                 self._durationWarningThresholdNanoSeconds*1.0/1000/1000/1000)
            self._durationWarningCounter.inc()

        self.kickTimeCount(now)#before changing _isWorking to False as it uses it
        self._isWorking = False
        self._realStartTime = None

        if self._interval is None:
            self._log("end").debug5("end")            
            self._clearStart()

    def kickTimeCount (self, now = None):
        if now is None:
            now = monotonic_clock.monotonicTimeNano()
        #update the total time counter here for the "smoothness' of the counter.
        #We do not do it on the "get counter" as we don't have enough information maybe we are disabled)
        #and we are maybe in another thread...
        self._totalNanoSecondsCounter.inc(now-self._totalNanoSecondsCounterRefernenceTime)
        self._totalNanoSecondsCounterRefernenceTime = now

        if self._isWorking:
            self._activeNanoSecondsCounter.inc(now-self._activeNanoSecondsCounterRefernenceTime)
        self._activeNanoSecondsCounterRefernenceTime = now


    def isActive (self):
        return self._isWorking

    def _clearStart (self):
        self._alignedStartTime = None        
        self._specificName = None

    def _getCounter (self, counterName):
        if counterName == PollSupervisor.COUNTER_POLLS:
            return self._startCounter
        elif counterName == PollSupervisor.COUNTER_MISSED_POLLS:
            return self._missCounter
        elif counterName == PollSupervisor.COUNTER_LATENCY_ERRORS:
            return self._latencyErrorCounter
        elif counterName == PollSupervisor.COUNTER_LATENCY_WARNINGS:
            return self._latencyWarningCounter
        elif counterName == PollSupervisor.COUNTER_DURATION_ERRORS:
            return self._durationErrorCounter
        elif counterName == PollSupervisor.COUNTER_DURATION_WARNINGS:
            return self._durationWarningCounter
        elif counterName == PollSupervisor.COUNTER_FAILURES:
            return self._failuresCounter
        elif counterName == PollSupervisor.COUNTER_SUCCESS:
            return self._successCounter
        elif counterName == PollSupervisor.COUNTER_TOTAL_NANO_SECONDS:
            return self._totalNanoSecondsCounter
        elif counterName == PollSupervisor.COUNTER_ACTIVE_NANO_SECONDS:
            return self._activeNanoSecondsCounter
        else:
            self._log("invalid-counter").error("requesting an invalid counter '%s'", counterName) 
            return None      

    def getCount (self, counterName):
        counter = self._getCounter(counterName)
        if counter is None:
            return 0
        return counter.getClearable()

    def clearCount (self, counterName):
        counter = self._getCounter(counterName)
        if counter is None:
            return
        counter.clear()

