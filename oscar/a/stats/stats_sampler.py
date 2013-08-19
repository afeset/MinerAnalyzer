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
# This is the stats sampler object. Responsible of timing the sapling of the oscar counters
# The goal of the stats sampler is to periodicly sample the counters requested and Enqueue them
#                                                                                                                      #
########################################################################################################################

import tempfile
import threading
import time
import re
#import heapq
from stats_queue_objects import ValueObj, AggregationQueueValues, formatExceptionInfo
from enums import CommMethodTypes

#import google.yappi as profiler

# === Globals =====================================================================================
RATE_VALUE_TO_PARSE = 'lastSec'
RATE_NORMALIZE_MULT_VALUE = 1000
MIN_TIME_BETWEEN_SAMPLE_ERRORS = 3600
MIN_TIME_BETWEEN_DISCOVER_ERRORS = 3600
MAX_QUEUE_MESSAGES = 100
MAX_SAMPLING_TIME_SPAN = 60
REGEX_COUNTERS_DISCOVERY_INTERVAL = 60*3 # 3 minutes
# === Implementations =====================================================================================
class StatsSamplerPacer(threading.Thread):
    """
    This class is responsible of timing the samples
    """
    def __init__ (self):
        # We don't put it in init because we want to preserve this time between calls to init()
        now = abs(time.time())
        self.myNextDiscoveryTime = now
        self.myZeroTime = now - (now%3600) # The prev round hour time
        #We need a disctionary of counter names to check if discovered counters already exist
        self.myDiscoveredCounters = {}
        self.myNextSampleTime = None

    #counters - a dictionary containing all the counters key = counter id value = counter descriptor object
    #regexCounters - a dictionary containing regex counters
    #logger - dah
    #sampler - an instance of the Stats Sampler object
    def init (self, counters, regexCounters, logger, sampler):

        #These are used in the discovery process for new counters
        self.myRegexCounters = regexCounters

        self.myLogger = logger
        self.mySampler = sampler

        """
        #Build priority queue using a heap. The head of the heap is always the counter that its sample time is the closest
        self.myCountersPace = []
        now = abs(time.time())
        for counter in counters.values():
            nextSamplingTime = counter.mySamplingRate*(((now-self.myZeroTime) / counter.mySamplingRate) + 1) + self.myZeroTime 
            heapq.heappush(self.myCountersPace, (nextSamplingTime, counter))
        """
        self.myCounters = counters.values()

        self.myNewCounters = {}
        self.myDeletedCounters = {}

        self.myRunFlag = True
        threading.Thread.__init__(self)

    """
    def skipSample (self):
        self.myLogger.debug1("Entering skip counters")
        while(self.myCountersPace[0][0] <= time.time()):
            nextCounter = heapq.heappop(self.myCountersPace)
            #Update counter's next sampling time. 
            nextSamplingTime = nextCounter[1].mySamplingRate + nextCounter[0]
            self.myLogger.debug3("Counter " + self.myCountersPace[0][1].toString() + " time was " + str(nextCounter[0]) + " and changed to " + str(nextSamplingTime))
            #Insert the chosen counter back to the priority queue
            heapq.heappush(self.myCountersPace, (nextSamplingTime, nextCounter[1]))
        self.myLogger.debug3("Skip counters finished")
    """

    def run (self):

        self.myLogger.notice("Stats Sampler running")

        if self.myNextSampleTime is None:
            # One time initialization
            self.myNextSampleTime = time.time()
        else:
            # If we quit this thread due to discovering new counters, we need to sleep here before the next sample
            now = time.time()
            sleepTime = self.myNextSampleTime - now
            while sleepTime < 0:
                self.myNextSampleTime += 60
                sleepTime = self.myNextSampleTime - now

            self.myLogger.debug1("%d Compensation sleep %d sec (before loop)" % (int(now), int(sleepTime)))
            time.sleep(sleepTime)

        try:
            while (self.myRunFlag):

                # Sample counters
                startTime = time.time()
                self.myLogger.debug1("%d Start sampling counters" % int(startTime))
                self.__sampleValues()

                # Discover new regex counters
                if self.myNextDiscoveryTime - time.time() < 0:
                    self.myLogger.debug1("%d Start discover counters" % int(time.time()))
                    (self.myNewCounters, self.myDeletedCounters) = self.__discoverRegexCounters()
                    self.myNextDiscoveryTime = time.time() + REGEX_COUNTERS_DISCOVERY_INTERVAL
                    if self.myNewCounters or self.myDeletedCounters:
                        # If we discovered new counters we will exit the loop and re-initialize
                        self.myRunFlag = False

                endTime = time.time()
                self.myLogger.debug1("%d Finish sample/discover cycle. Elasped %d sec" % (int(endTime), int(endTime-startTime)))

                self.myNextSampleTime += 60
                sleepTime = self.myNextSampleTime - endTime
                while sleepTime < 0:
                    self.myNextSampleTime += 60
                    sleepTime = self.myNextSampleTime - endTime

                if self.myRunFlag:
                    # If we need to quit we will sleep when we come back
                    self.myLogger.debug1("%d Sleep %d sec" % (int(endTime), int(sleepTime)))
                    time.sleep(sleepTime)
        except:
            self.myLogger.error("Unexpected exception on Stats Sampler. Exception info: %s" % formatExceptionInfo())

        if self.myRunFlag:
            self.myLogger.notice("Stats Sampler thread ended enexpectedly")
        else:
            self.myLogger.notice("Stats Sampler thread ended")

        self.myRunFlag = False

    #Calls the sampler object
    #If in the future there is a need to sample multi-threaded a queue can be added here
    def __sampleValues (self):
        return self.mySampler.sample(self.myCounters)

    #Discover new regex counters
    def __discoverRegexCounters (self):

        #We will create a list of new counters based on the counters that we discovered
        newCounters = {}
        deletedCounters = []
        processInacessibleInLastDiscoveryCycle = {}

        self.myLogger.debug3("Discovering new counters")
        discoveredCounters = self.mySampler.discover(self.myRegexCounters, processInacessibleInLastDiscoveryCycle)
        tmpDiscoveredCounters = {}

        for (regexCounterId, realCounterName) in discoveredCounters:
            #Since the discovery process in on going. We always discover counters that we Already know of.
            fullName = self.myRegexCounters[regexCounterId].myCounterPath + "/" + realCounterName + "-" + str(self.myRegexCounters[regexCounterId].myCounterType)

            tmpDiscoveredCounters[fullName] = 1
            if fullName not in self.myDiscoveredCounters:
                #Discovered a new counter. Yeah!
                self.myLogger.debug1("Discovered new counter %s" % fullName)
                #Pinocchio becomes a real boy...
                newRealCounter = self.myRegexCounters[regexCounterId].cloneRealCounter(realCounterName)
                newCounters[newRealCounter.myCounterId] = newRealCounter
                self.myDiscoveredCounters[fullName] = newRealCounter


        #Now check if some counters were deleted
        namesToDelete = []

        for fullName in self.myDiscoveredCounters:
            if fullName not in tmpDiscoveredCounters:
                if self.myDiscoveredCounters[fullName].myCounterProcess not in processInacessibleInLastDiscoveryCycle:
                    deletedCounters.append(self.myDiscoveredCounters[fullName].myCounterId)
                    self.myLogger.notice("Deleted regex counter %s" % fullName)
                    namesToDelete.append(fullName)

        for nameToDelete in namesToDelete:
            del(self.myDiscoveredCounters[nameToDelete])

        return newCounters, deletedCounters

    #Is the thread still running? still alive?
    def isRunning (self):
        return self.myRunFlag

    def needUpdate (self):
        if self.myNewCounters or self.myDeletedCounters:
            return True
        return False

    def getNewAndDeletedCounters (self):
        return (self.myNewCounters, self.myDeletedCounters)

    #End the main thread loop - kill the thread
    def end (self):
        self.myLogger.notice("Stats Sampler request to end thread")
        self.myRunFlag = False

    def setLogger (self, logger):
        self.myLogger = None
        self.myLogger = logger
        self.mySampler.setLogger(logger)

class StatsSampler():
    """
    This class is responsible of sampling the other processes
    """
    def __init__ (self):        
        # Compile some static regexps 
        self.errorRegex = re.compile("^Error:")
        self.squareBracketsRegex = re.compile("\[(.*)\]")
        self.counterResponseRegex = re.compile('Qwilt>(?:\x07)?(.*?)\n\n', re.IGNORECASE | re.DOTALL)
        self.counterDescriptionRegex = re.compile('desc=(.*?)\n', re.IGNORECASE | re.DOTALL)
        self.counterValueRateRegex = re.compile(RATE_VALUE_TO_PARSE+'=([0-9.]+)', re.IGNORECASE | re.DOTALL)
        self.counterValueRegex = re.compile('value=([0-9]+)', re.IGNORECASE | re.DOTALL)

    #processesDictionary
    #outputJobsQueue
    #logger
    #maxJobsQueueSize
    #systemBaseDirectory
    def init (self, processesDictionary, outputJobsQueue, logger, maxJobsQueueSize, commChanDict):
        #Initialize memeber variables
        self.myOutputJobsQueue = outputJobsQueue
        self.myLogger = logger
        self.myMaxJobsQueueSize = maxJobsQueueSize
        self.myProcessesDictionary = processesDictionary
        self.lastSampleErrorMsg = time.time() - 2*MIN_TIME_BETWEEN_SAMPLE_ERRORS
        self.lastDiscoverErrorMsg = time.time() - 2*MIN_TIME_BETWEEN_DISCOVER_ERRORS
        self._commChanDict = commChanDict
        self.myLogger.debug2("StatsSampler initialized")

    #Sample and parse all the file based counters
    def _fileSample (self, counterDescList, errorMessages, sampleResults):

        processList = []
        errorsPerProcess = {}

        for counterDesc in counterDescList:
            #If this is the first counter we encountered from this process, create a new entry in the dictionary
            if counterDesc.myCounterProcess not in processList:
                if counterDesc.myCounterProcess in self._commChanDict.keys():
                    self.myLogger.debug3("Sample: About to receive counters from process %s" % (counterDesc.myCounterProcess)) 
                    self._commChanDict[counterDesc.myCounterProcess].receive()
                    self.myLogger.debug3("Sample: Receiving counters from process %s" % (counterDesc.myCounterProcess)) 
                else:
                    errorMessages.append("Process (%s) communication channel is missing for counter %s" % (counterDesc.myCounterProcess, counterDesc.myCounterName))
                    continue

                processList.append(counterDesc.myCounterProcess)
          
            valuesDict = self._commChanDict[counterDesc.myCounterProcess].getData()
            valuesTime = self._commChanDict[counterDesc.myCounterProcess].getTime()

            if valuesDict:
                self.myLogger.debug3("Sample: Got %s counters" % (len(valuesDict))) 
                if counterDesc.myCounterSamplingName in valuesDict.keys():
                    val = str(valuesDict[counterDesc.myCounterSamplingName])
                    sampleResults.append(ValueObj(counterDesc.myCounterId, valuesTime, val, counterDesc.myCounterSamplingName))
                    self.myLogger.debug4("Sampled counter %s(%s) read successfully. Val=%s(%s)  Time=%s(%s) ", counterDesc.myCounterSamplingName, counterDesc.myCounterId, val, type(val), valuesTime, type(valuesTime))
                else:
                    sampleResults.append(ValueObj(counterDesc.myCounterId, valuesTime, 0, counterDesc.myCounterSamplingName))
                    #errorMessages.append("Counter %s is missing" % (counterDesc.myCounterName)) 
                    self.myLogger.debug4("Counter %s is missing" % (counterDesc.myCounterName))
            else:
                sampleResults.append(ValueObj(counterDesc.myCounterId, valuesTime, 0, counterDesc.myCounterSamplingName))
                if counterDesc.myCounterProcess not in errorsPerProcess:
                    errorMessages.append("Unable to read counters from process %s" % (counterDesc.myCounterProcess))
                    errorsPerProcess[counterDesc.myCounterProcess]=1
        return 0

    #Sample and parse all the qshell counters 
    def _qShellSample (self, counterDescList, errorMessages, sampleResults):

        #This is a dictionary to hold the mega query for each process. i.e. We collect all the counters in one q-shell connection.
        megaQueryPerProcess = {}
        
        #Build all q-shell queries. Concat them according to the right process
        for counterDesc in counterDescList:
            #If this is the first counter we encountered from this process, create a new entry in the dictionary
            if counterDesc.myCounterProcess not in megaQueryPerProcess.keys():
                megaQueryPerProcess[counterDesc.myCounterProcess] = ''
            #Add a new command to the mega command
            if counterDesc.myIsRate:
                qShellFunc = "getRate"
            else:
                qShellFunc = "get"
            megaQueryPerProcess[counterDesc.myCounterProcess] += "%s/%s.%s[%s](actual=true)\n" % (counterDesc.myCounterProcess, counterDesc.myCounterPath, qShellFunc, counterDesc.myCounterSamplingName)

        #Run each mega command indevidually
        for process_key in megaQueryPerProcess.keys():

            outFile = tempfile.TemporaryFile()

            #Execute command using oscar_process_q_shell_connect.py
            self.myLogger.debug3("StatsSampler sends q-shell query for process %s - time = %s" % (str(process_key), str(time.time())))
            if process_key in self.myProcessesDictionary.keys():
                self.myLogger.debug4("StatsSampler sends q-shell query for process %s - query = %s" % (str(process_key), str(megaQueryPerProcess[process_key])))
                self.myProcessesDictionary[process_key].runShellCmd(megaQueryPerProcess[process_key], outFile)
                self.myLogger.debug3("StatsSampler Done")
            else:
                errorMessages.append("Process %s doesn't exist in the processes dictionary - sample skipped" % process_key)
                continue

            outFile.seek(0)

            numCounters = 0
            for match in re.finditer(self.counterResponseRegex, outFile.read()):
                response = match.group(1)

                isRate = response.find(RATE_VALUE_TO_PARSE) > -1
                #Get the counters value
                val = self.__parseValue(response, isRate)
                #Get its description string - it is free
                if not isRate:
                    desc = self.__parseDescription(response)
                else:
                    desc = "Rate of type: %s for counter %s/%s/%s" % (qShellFunc, counterDesc.myCounterProcess, counterDesc.myCounterPath, counterDesc.myCounterName)
                if val and desc:
                    #If all OK - create the val obj 
                    sampleResults.append(ValueObj(counterDescList[numCounters].myCounterId, time.time(), val, desc[0]))
                    #self.myLogger.debug1("Sampled counter parsed successfully. Value=%s, Description=%s" % (val, desc)) 
                else:
                    #If parsing failed - log
                    errMsg = "Sampled counter could not be parsed - might happen if sampled process is down. Counter response: %s." % (response)
                    self.myLogger.warning(errMsg) 
                
                numCounters += 1

            outFile.close()

            if numCounters == 0:
                errMsg = "StatsSampler - No response received during q-shell execution - wierd. time = %s" % str(time.time())
                errorMessages.append(errMsg)
                return 5731877

            self.myLogger.debug2("Parsed %s counters" % numCounters)

        return 0

    # Discover new regex counters for file based counters
    def _fileDiscover (self, counterDescList, errorMessages, discoveredCounters, processInacessibleInLastDiscoveryCycle):

        processList = []
        errorsPerProcess = {}

        self.myLogger.debug3("Discover counters called for file comm method (%d regex counters)" % len(counterDescList)) 

        for counterDesc in counterDescList:

            #If this is the first counter we encountered from this process, create a new entry in the dictionary
            if counterDesc.myCounterProcess not in processList:
                if counterDesc.myCounterProcess in self._commChanDict.keys():
                    self.myLogger.debug3("Discover: About to receiving counters from process %s" % (counterDesc.myCounterProcess)) 
                    self._commChanDict[counterDesc.myCounterProcess].receive()
                    self.myLogger.debug3("Discover: Receiving counters from process %s" % (counterDesc.myCounterProcess)) 
                else:
                    errorMessages.append("Discover: Process (%s) communication channel is missing for counter %s" % (counterDesc.myCounterProcess, counterDesc.myCounterName))
                    continue

                processList.append(counterDesc.myCounterProcess)

            valuesDict = self._commChanDict[counterDesc.myCounterProcess].getData()

            if valuesDict:
                self.myLogger.debug3("Discover: Got %s counters" % (len(valuesDict))) 
                #Any "real" counter can match to more than one regex (for rate counters)
                counterRegex = re.compile("^"+counterDesc.myCounterSamplingName+"$")
                for counterName in valuesDict.keys():
                    if counterRegex.match(counterName):
                        self.myLogger.debug4("Discovered counter %s, Regex %s, IsRate %s (file)" % (counterName, counterDesc.myCounterName, counterDesc.myIsRate))
                        discoveredCounters.append((counterDesc.myCounterId, counterName))
                self.myLogger.debug3("Discover: Finished parsing") 
            else:
                if counterDesc.myCounterProcess not in errorsPerProcess:
                    errorMessages.append("Discover: Unable to read counters from process %s" % (counterDesc.myCounterProcess))
                    errorsPerProcess[counterDesc.myCounterProcess]=1
                    processInacessibleInLastDiscoveryCycle[counterDesc.myCounterProcess]=1



    # Discover new regex counters for qshell based counters
    def _qShellDiscover (self, counterDescList, errorMessages, discoveredCounters, processInacessibleInLastDiscoveryCycle):

        #This is a dictionary to hold the discover query for each process (query the whole counters container)
        #We collect all the counters in one q-shell connection.
        queryPerProcess = {}

        self.myLogger.debug3("Discover counters called for qshell comm method (%d regex counters)" % len(counterDescList)) 

        #Build all q-shell queries. Concat them according to the right process
        for counterDesc in counterDescList:
            #If this is the first counter we encountered from this process, create a new entry in the dictionary
            if counterDesc.myCounterProcess not in queryPerProcess:
                queryPerProcess[counterDesc.myCounterProcess] = {}
            #Add a new command to the discover command. The values are the counterDesc objects that relate to this container
            containerName = "%s/%s" % (counterDesc.myCounterProcess, counterDesc.myCounterPath)
            if containerName not in queryPerProcess[counterDesc.myCounterProcess]:
                queryPerProcess[counterDesc.myCounterProcess][containerName] = []
            queryPerProcess[counterDesc.myCounterProcess][containerName].append(counterDesc)

        #For each process we run each discover command
        for processKey, processContainers in queryPerProcess.iteritems():
            # This list holds the containers in the process in the same order in which we query them
            containersList = []
            cmdPerProcess = ""
            for container in queryPerProcess[processKey]:
                cmdPerProcess += container + ".values()\n"
                containersList.append(container)
            
            self.myLogger.debug3("Discover: StatsSampler sends q-shell query for process %s" % (str(processKey)))
            #Execute command using oscar_process_q_shell_connect.py
            if processKey in self.myProcessesDictionary:
                self.myLogger.debug5("Discover: StatsSampler sends q-shell query for process %s - query = %s" % (str(processKey), str(cmdPerProcess)))
                commandResult = self.myProcessesDictionary[processKey].runShellCmd(cmdPerProcess)
            else:
                errorMessages.append("Discover: Process %s doesn't exist in the processes dictionary - sample skipped" % processKey)
                continue

            #We set a flag to mask the errors so there won't be any data to use in commandResult[0]
            commandResult = commandResult[1]
            if commandResult == None:
                errMsg = "Discover: StatsSampler - No response received during q-shell execution - wierd"
                errorMessages.append(errMsg)
                processInacessibleInLastDiscoveryCycle[processKey]=1
                return 5731878

            self.myLogger.debug3("Discover: StatsSampler - q-shell request returned succesfully.")
            #We received many responses from many counters sampled with our mega query - seperate them, the result is a list where each slot is an independent resopnse
            countersResponses = self.__seperateCounters(commandResult)
            #If we failed it is a big problem
            if not countersResponses:
                self.myLogger.warning("Discover: No response recieved from q-shell query. Query: %s" % cmdPerProcess) 
                return 5731879

            self.myLogger.debug3("Discover: Separated %s responses" % len(countersResponses))

            if len(containersList) != len(countersResponses):
                self.myLogger.warning("Discover: Mismatched response recieved from q-shell query. Asked about %s containers, got %s responses. Query: %s" % \
                                      (len(containersList), len(countersResponses), cmdPerProcess) )
                return 5837453

            #Parse the sample responses and collect all counters in the process to a single list
            for i in range(0, len(countersResponses)):

                allCountersInContainer = []

                response = countersResponses[i]
                queriedContainerName = containersList[i]
                counters = response.split("\n")
                
                if len(counters) >= 2: # There should be at least 2 lines here. 
                                       # First line is always the name of the container.
                                       # Second can be an error
                    tmpList = counters[0].split(".values()")
                    if tmpList:
                        container = tmpList[0]
                        if queriedContainerName != container:
                            self.myLogger.warning("Discover: Mismatched container name from q-shell query. Asked about %s, got %s. Query: %s" % \
                                                  (queriedContainerName, container, cmdPerProcess) )
                        for j in range (1, len(counters)):
                            if self.errorRegex.match(counters[j]):
                                #errorMessages.append(counters[j])
                                self.myLogger.debug1(counters[j]) 
                            else:
                                counterNameList = self.squareBracketsRegex.findall(counters[j])
                                if counterNameList:
                                    allCountersInContainer.append(counterNameList[0])
                                else:
                                    errMsg = "Discover: StatsSampler - Error parsing counter response from q-shell. [%s]" % (counters[j])
                                    errorMessages.append(errMsg)
                                    continue  
                    else:
                        errMsg = "Discover: StatsSampler - Error parsing counters line 0 response from q-shell. [%s]" % (counters[0])
                        errorMessages.append(errMsg)
                        continue  
                else:
                    response_len = len(response)
                    chars_to_print = min(100, response_len)
                    errMsg = "Discover: StatsSampler - Error parsing response from q-shell. First %d chars (of %d) [%s]" % \
                        (chars_to_print, response_len, response[:chars_to_print])
                    errorMessages.append(errMsg)
                    continue        

                # At this point we have a list of all "real" counters in the container.
                # Match them against all descriptions of this container
                for counterDesc in processContainers[queriedContainerName]:
                    counterRegex = re.compile("^"+counterDesc.myCounterSamplingName+"$")
                    #Any "real" counter can match to more than one regex (for rate counters)
                    for counterName in allCountersInContainer:
                        if counterRegex.match(counterName):
                            self.myLogger.debug4("Discovered counter %s, Regex %s, IsRate %s (file)" % (counterName, counterDesc.myCounterName, counterDesc.myIsRate))
                            discoveredCounters.append((counterDesc.myCounterId, counterName))
    
            self.myLogger.debug3("Discover: Finished, discovered %s counters" % len(discoveredCounters))

        return 0


    def sample (self, counterDescList):
        qShellCntrList = []
        fileCntrList = []
        for cntr in counterDescList:
            if cntr.myCommMethod == CommMethodTypes.FILE:
                fileCntrList.append(cntr)
            else:
                qShellCntrList.append(cntr)

        errorMessages = []
        sampleResults = []

        self.myLogger.info("Calling sample file")
        # currently retVal for _fileSample is not relevant as it is always 0
        retVal = self._fileSample(fileCntrList, errorMessages, sampleResults)
        retVal = self._qShellSample(qShellCntrList, errorMessages, sampleResults)

        if errorMessages and time.time()-self.lastSampleErrorMsg>MIN_TIME_BETWEEN_SAMPLE_ERRORS:
            for msg in errorMessages:
                self.myLogger.error(msg)
            self.lastSampleErrorMsg = time.time()

        #Enquque the values in the jobs queue in order for it to be stored in the DB
        if self.myOutputJobsQueue._qsize() > MAX_QUEUE_MESSAGES:
            self.myLogger.warning("StatsSampler job queue size exceeds max size - dropping newest sample. Q_SIZE=%d, MAX_SIZE=%d" % (self.myOutputJobsQueue._qsize(), MAX_QUEUE_MESSAGES));
            retVal = 748456
        else:
            #profiler.start()
            self.myOutputJobsQueue.put(AggregationQueueValues(sampleResults))
            #profiler.print_stats()
            #profiler.stop()
            #profiler.clear_stats()
            #print "=================================================="
            self.myLogger.debug1("StatsSampler job queue size is: %d" % self.myOutputJobsQueue._qsize())
            retVal = 0

        return retVal

    def discover (self, regexCounters, processInacessibleInLastDiscoveryCycle):

        qShellCntrList = []
        fileCntrList = []

        for cntr in regexCounters.values():
            if cntr.myCommMethod == CommMethodTypes.FILE:
                fileCntrList.append(cntr)
            else:
                qShellCntrList.append(cntr)

        errorMessages = []
        discoveredCounters = []

        self._fileDiscover(fileCntrList, errorMessages, discoveredCounters, processInacessibleInLastDiscoveryCycle)
        self._qShellDiscover(qShellCntrList, errorMessages, discoveredCounters, processInacessibleInLastDiscoveryCycle)

        if errorMessages and time.time()-self.lastDiscoverErrorMsg>MIN_TIME_BETWEEN_DISCOVER_ERRORS:
            for msg in errorMessages:
                self.myLogger.error(msg)
            self.lastDiscoverErrorMsg = time.time()

        return discoveredCounters


    #This function gets long strings containing many q-shell responses and splits it
    #Returns a list where each entry is an independent counter query
    def __seperateCounters(self, qshellQueryResponse):
        counterResponses = self.counterResponseRegex.findall(qshellQueryResponse)
        return counterResponses
        
    #Receives a counter q-shell response and retrieves the counter's description
    def __parseDescription (self, counterSampleResponse):
        counterDescription = self.counterDescriptionRegex.findall(counterSampleResponse)        
        if len(counterDescription) !=1:
            return None
        return counterDescription

    def setLogger (self, logger):
        self.myLogger = None
        self.myLogger = logger

    #Receives a counter q-shell response and retrieves the counter's value
    def __parseValue (self, countersShellOutput, isRate):
    
        if isRate:
            counterValue = self.counterValueRateRegex.findall(countersShellOutput)
            if len(counterValue) == 1:            
                return str(round(float(counterValue[0])*RATE_NORMALIZE_MULT_VALUE))
        else:
            counterValue = self.counterValueRegex.findall(countersShellOutput)
            if len(counterValue) == 1:            
                return counterValue[0]

        self.myLogger.debug4("Counter shell output could not be parsed. Output: %s. Length: %d" % (countersShellOutput, len(counterValue)))
        return None

