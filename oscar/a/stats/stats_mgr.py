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
#                                                                                                                      #
# This is the module managment class. To use Stats, one should create this class with the proper configurations
#                                                                                                                      #
########################################################################################################################

import os, sys
import logging
import re
from Queue import Queue
from stats_aggregator import StatsAggregator
from stats_sampler import StatsSamplerPacer, StatsSampler
from stats_rrd_writer import StatsRrdWriter
from stats_queue_objects import formatExceptionInfo
from enums import AggregationConsolidationFunctionType, VariableTypes, AggregationCounterType, CommMethodTypes
from counter_descriptor import CounterDescriptor, CounterProperty, DataSetArchaive
from configuration_functions import *
import threading, time, datetime
from ConfigParser import ConfigParser
from stats_comm_over_file import StatsCommOverFile 
from a.infra.log.main_logger import MainLogger
import a.infra.process.captain
import a.infra.format.json
from event_report_limiter import EventReportLimiter

# === Globals =====================================================================================

RRDTOOL_EXE_PATH_CMD = "rrdtool/bin/rrdtool" 
RRDTOOL_WRAPPER_EXE_PATH_CMD = "rrdtool/bin/rrdtool_wrapper.py --file " 
OLD_DATA_PATH = "old"
PREV_RUN_PATH = "prev"
LOGGER_NAME = "stats"
COUNTERS_VARIABLE_TYPE = 'integer'
DATE_TIME_QSHELL_CHECK_INTERVAL = datetime.timedelta(0,40)

CFG_DEFAULT_ARCHAIVE_SAMPLING_RATE='sampling-rate'
CFG_DEFAULT_ARCHAIVE_ERROR_RATE='errors-precentage-allowed'
# Fisrst archaive - latest
CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_SPAN_LATEST='consolidation-span-latest-samples-archaive'
CFG_DEFAULT_ARCHAIVE_ROWS_TO_KEEP_LATEST='num-of-rows-latest-samples-archaive'
# Fisrst archaive - mid
CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_SPAN_MID='consolidation-span-mid-samples-archaive'
CFG_DEFAULT_ARCHAIVE_ROWS_TO_KEEP_MID='num-of-rows-mid-samples-archaive'
# Fisrst archaive - old
CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_SPAN_OLD='consolidation-span-old-samples-archaive'
CFG_DEFAULT_ARCHAIVE_ROWS_TO_KEEP_OLD='num-of-rows-old-samples-archaive'
CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_FUNCTION='consolidation-function'

CFG_PROCESS_NAME = 'process-name'
CFG_COMM_METHOD = 'comm-method'
CFG_REGEX = 'regex'
CFG_EXPERATION_TIME = 'experation-time'
CFG_COUNTER_TYPE = 'counter-types'
CFG_COUNTER_IS_RATE = 'is-rate'
CFG_COUNTER_RATE_ONLY = 'rate-only'
CFG_COUNTER_CONSOLIDATION_FUNCTION = 'consolidation-function'
CFG_COUNTER_DESCRIPTION = 'counter-description'
CFG_COUNTER_UNITS = 'APS_units'
CFG_GAUGE_UNITS = 'GAUGE_units'
CFG_RATE_UNITS = 'rate_units'
CFG_META_COUNTER__ARITHMETIC_EXPRESSION = 'meta-counter-expression'
CFG_META_RATE__ARITHMETIC_EXPRESSION = 'meta-rate-expression'
CFG_SHOULD_DEVIDE_COUNTERS_BY_SAMPLING_RATE = 'present-counters-per-second'
CFG_COUNTER_CUSTOM_ARCHAIVES = 'custom-archaives-list'
CFG_COUNTER_PROPERTIES = 'properties-list'
CFG_COUNTER_SAMPLING_RATE_CLASS = 'counter-sampling-rate-class'
CFG_DEFAULT_HIGH_SAMPLING_RATE_CLASS='high-sample-rate'
CFG_DEFAULT_SUPER_SAMPLING_RATE_CLASS='super-sample-rate'
CFG_DEFAULT_LEGAL_PROPERTIES = 'properties-enum'
CFG_COUNTERS_FILE = 'counters-file'
CFG_DEBUG_OUTPUT_PATH='output-path'
CFG_PROCESSES_WITH_Q_SHELL = "processes-with-qshell"
CFG_SHOULD_EXIT_ON_DB_ERROR = "exit-on-db-error"

CFG_WRITE_PERIOD='write-period'
CFG_RRD_UPDATE_BURST_COUNT='rrd-update-burst-count'
CFG_RRD_UPDATE_BURST_INTERVAL='rrd-update-burst-interval'
CFG_AGGR_UPDATE_BURST_COUNT='aggr-update-burst-count'
CFG_AGGR_UPDATE_BURST_INTERVAL_MSEC='aggr-update-burst-interval-msec'
CFG_STARTUP_GRACE_PERIOD='startup-grace-period'
CFG_ENABLE_RECOVERY='enable-recovery'

configurationsDefaults = {
    CFG_DB_FILES_BASE_NAME:'Stats',
    CFG_JOBS_QUEUE_MAX_SIZE:3,
    CFG_SHOULD_EXIT_ON_DB_ERROR:True,
    
    #Default archaive - exists for each counter
    #DO NOT DELETE THIS COMMENT - CFG_DEFAULT_ARCHAIVE_SAMPLING_FACTOR:1, - must always remain 1. If any changes are needed change other defaults. - DO NOT DELETE THIS COMMENT
    CFG_DEFAULT_ARCHAIVE_SAMPLING_RATE:60,
    CFG_DEFAULT_HIGH_SAMPLING_RATE_CLASS:40,
    CFG_DEFAULT_SUPER_SAMPLING_RATE_CLASS:20,
    CFG_DEFAULT_ARCHAIVE_ERROR_RATE:0.5,

    # Fisrst archaive - latest
    CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_SPAN_LATEST:1,
    CFG_DEFAULT_ARCHAIVE_ROWS_TO_KEEP_LATEST:44640,

    # First archaive - mid
    CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_SPAN_MID:None,
    CFG_DEFAULT_ARCHAIVE_ROWS_TO_KEEP_MID:None,

    # Fisrst archaive - old
    CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_SPAN_OLD:None,
    CFG_DEFAULT_ARCHAIVE_ROWS_TO_KEEP_OLD:None,

    CFG_DEFAULT_LEGAL_PROPERTIES:"['Port', 'Process', 'Url']",
    CFG_PROCESSES_WITH_Q_SHELL:"['line']",
    CFG_COUNTERS_FILE:"stats/counters_configurations.cfg",
    CFG_META_COUNTER__ARITHMETIC_EXPRESSION:"",
    CFG_META_RATE__ARITHMETIC_EXPRESSION:"",
    CFG_COUNTER_UNITS:"",
    CFG_GAUGE_UNITS:"",
    CFG_RATE_UNITS:"",
    CFG_COUNTER_TYPE:"['%s','%s']" % (AggregationCounterType.GAUGE, AggregationCounterType.COUNTER),
    CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_FUNCTION:AggregationConsolidationFunctionType.AVERAGE,
    CFG_COUNTER_IS_RATE:False,
    CFG_COUNTER_RATE_ONLY:False,
    CFG_COUNTER_DESCRIPTION:None, 
    CFG_DEBUG_OUTPUT_PATH:None,
    CFG_SHOULD_DEVIDE_COUNTERS_BY_SAMPLING_RATE:True,

    CFG_COMM_METHOD:CommMethodTypes.QSHELL,
    CFG_EXPERATION_TIME:120,
    CFG_REGEX:False,

    CFG_WRITE_PERIOD:1200,
    CFG_RRD_UPDATE_BURST_COUNT:70,
    CFG_RRD_UPDATE_BURST_INTERVAL:3,
    CFG_AGGR_UPDATE_BURST_COUNT:1000,
    CFG_AGGR_UPDATE_BURST_INTERVAL_MSEC:100,
    CFG_STARTUP_GRACE_PERIOD:600,
    CFG_ENABLE_RECOVERY:True
}


# === Implementations =====================================================================================

class StatsMgr(object):

    def __init__ (self):
        self.statsInitOK = False
        self.myValuesDbLock = threading.Lock()
    
    #pocessesDict - Dictionary. key = process name value = 'StatsDaemonInfo' object that handeks q0shell connections and queris
    #statsParamsCfg = Stats configurations file
    #descriptionDbFilesPath = The output path for the SQLite files
    #dbFilesOutputPath = The output path for the RRD files
    def init (self, processesDict, dataRunDirPath, descriptionDbFilesPath, dbFilesOutputPath, statsDataRootDir, 
              kickNumber, logPath, logLevel, logFileSize, logTotalSize, logConfigurationFile, logConfigurationLoadPeriod, 
              systemParamsCfg, systemConstDir, processCommFileGlobPattern, lineRunningCfgFile):

        #initialize memeber variables
        self.myStatsConfigurations = systemParamsCfg
        self.systemConstDir = systemConstDir
        self.myCountersListFilePath = os.path.join(systemConstDir, getSysParamOrDefault(systemParamsCfg, CFG_SECTION, CFG_COUNTERS_FILE, configurationsDefaults))
        self.myDbFilesOutputPath = dbFilesOutputPath
        self.myDescriptionDbFilesPath = descriptionDbFilesPath
        self.myDataRunDirPath = dataRunDirPath
        self.myKickNumber = kickNumber
        self.myLogPath = logPath
        self.myLogFileSize = logFileSize
        self.myLogTotalSize = logTotalSize
        self.myLogConfigurationFile = logConfigurationFile
        self.myLogConfigurationLoadPeriod = logConfigurationLoadPeriod
        self.myProcessesDictionary = processesDict
        self.myStatsDataRootDir = statsDataRootDir
        self.processCommFileGlobPattern = processCommFileGlobPattern
        self._logLevel = logLevel
        self.myPacer = None
        self.mylineRunningCfgFile = lineRunningCfgFile
        self.myGracePeriodEnded = False

    def postStartInit (self):
        #Enables us to replace the counters if needed
        #TODO(galm) - this is not relevant to you output, only to you inputs - please separate the outpt
        alternativeOutputPath = getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEBUG_OUTPUT_PATH, configurationsDefaults)
        if alternativeOutputPath:
            self.myDescriptionDbFilesPath = alternativeOutputPath
        
            #Create the output dir if doesn't exist
            if not self.__makeDirsIfNeeded(self.myDescriptionDbFilesPath):
                self.myLogger.error("Couldn't create db's output directory - aborts. Dir path: %s" % self.myDescriptionDbFilesPath)
                return 8349


        #TEMP till we have a captain
        self.captain = a.infra.process.captain.Captain()
        self.captain._initKickNumber(self.myKickNumber)
        a.infra.process.setGlobalCaptain(self.captain)
        #TEMP END
        self._mainLogger = MainLogger(processName = "Stats")
        self._baseLogger = self._mainLogger.getLoggerManager().createLogger("Stats", "Stats")
        self._mainLogger.initLoggerToUse(self._baseLogger)
        self._mainLogger.init(initialLogLevel=self._logLevel, logDir = self.myLogPath, 
                              logFileSize = self.myLogFileSize, logTotalSize = self.myLogTotalSize,
                              pearlConfigurationFilesFullName = self.myLogConfigurationFile, 
                              pearlConfigurationLoadPeriodInSeconds = self.myLogConfigurationLoadPeriod)
        self.myLogger = self._baseLogger("stats-msg")
        self.myLogger.info("Stats Script - Starting...")
        
        #The next code block checks that the q-shell of the sampled processes is responding. This solves the problem of sampling the q-shell too soon
        allProcesses = self.myProcessesDictionary.keys()
        processesWithQShell = getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_PROCESSES_WITH_Q_SHELL, configurationsDefaults)
        successes = 0
        hasQshellProcess = False
        try:
            for process_key in allProcesses:
                if not process_key in processesWithQShell:
                    continue

                hasQshellProcess = True

                # Given that line might take a lot of time to start, try a few times before giving up.
                maxRetries=20
                warnThreshold=3
                retryIndex=0
                processStarted=False
                while (not processStarted) and (retryIndex < maxRetries):
                    retryIndex += 1
                    self.myLogger.debug5("Waiting for process %s to start, attempt %s out of %s" % (process_key, retryIndex, maxRetries))
                    if self.myProcessesDictionary[process_key].waitForQshellRunningIndicationOrTimeout(process_key, datetime.datetime.now()+DATE_TIME_QSHELL_CHECK_INTERVAL):
                        processStarted = True # Terminate loop
                    else:
                        if retryIndex >= warnThreshold:
                            self.myLogger.warning("Process %s q-shell is not responding after %s attempts" % (process_key, retryIndex))

                if processStarted:
                    successes += 1
                    self.myLogger.notice("Process %s started, attempt %s out of %s" % (process_key, retryIndex, maxRetries))
                else:
                    self.myLogger.notice("Process %s q-shell is not responding" % process_key)
        except:
            self.myLogger.error("Unknown Exception in stats init - aborts. Exception info: %s" % (formatExceptionInfo()))
            return 69403
        
        #There is no logic for stats to run if there are no responding processes
        if (not allProcesses):
            self.myLogger.error("Stats initialized with zero processes - aborts")
            return 69401

        if (hasQshellProcess and successes == 0):
            self.myLogger.error("Stats initialized with zero processes running - aborts")
            return 69402
        
        # At this point, the line configuration file must exist.
        self.__readLineRunningCfg()

        #Create consumer design pattern Queue
        self.myJobsQueue = Queue()
        self.myLogger.debug1("StatsMgr queues created")
        
        #Load counters configurations 
        (self.myCountersDBInfo, self.myRegexCounters, self.myCommChanDict) = self.loadCountersConfigurations()
        if not self.myCountersDBInfo and not self.myRegexCounters:
            #No counters were found? Nothing to do - die
            self.myLogger.error("StatsMgr zero counters were found in counter configurations file. File path: %s" % self.myCountersListFilePath)
            return 548731

        #Check that the properties names are unique.
        #We need to combine the 2 counter dictionaries to one.
        #Since the dict keys are derived from a config file section names, 
        #it is safe to assume that there will be no overlapping keys
        tempCountersDict = dict(self.myCountersDBInfo)
        tempCountersDict.update(self.myRegexCounters)
        errFlag = self.__validateProperties(tempCountersDict)
        if errFlag:
            return 787544

        self.myLogger.debug1("StatsMgr counters configuration loaded")
        self.myMaxJobsQueueSize = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_JOBS_QUEUE_MAX_SIZE, configurationsDefaults))

        self.myNumHistoryFiles = self.__calcNumHistoryFiles(self.myWritePeriod + self.myStartupGracePeriod)
        self.myLogger.notice("StatsMgr: Grace period started, keeping %s history files", self.myNumHistoryFiles)
        self.myAggrHistory = AggrHistory(self.myLogger)
        self.myAggrHistory.setMaxHistoryEntries(self.myNumHistoryFiles * 2)

        self.__initWorkers()

        # Now, the aggregator is already created. We want to tell him to load its prev-run files
        # Into the newly created aggrHistory object
        self.myAggregator.loadHistoryFiles()

        self.myRrdWriter = StatsRrdWriter()
        self.myRrdWriter.init(self.myLogger, self, self.myAggrHistory, self.myWritePeriod, self.myRrdUpdateBurstCount, 
                              self.myRrdUpdateBurstInterval, self.myStartupGracePeriod)
        self.myRrdWriter.start()

        self.myLogger.info("Stats Script - Launched")
        self.myLogger.closeLog()
        self.statsInitOK = True
        return 0

    # RRD writer thread calls this function once the first loop is done, to tell this manager to reduce the amount
    # of history files it needs to keep
    def notifyNoMoreGrace (self):
        if not self.myGracePeriodEnded:
            self.myGracePeriodEnded = True
            self.myNumHistoryFiles = self.__calcNumHistoryFiles(self.myWritePeriod)
            self.myLogger.notice("StatsMgr: Grace period is over, keeping %s history files from now on", self.myNumHistoryFiles)
            self.myAggregator.setNumHistoryFiles(self.myNumHistoryFiles)
            # We do not update the AggrHistory max entries to avoid some boundray conditions when it is suddenly
            # decreaced due to grace period finished.

    def start (self):
        self.postStartInit()
        self.myLogger.info("Stats mgr - thread started")

        if not self.statsInitOK:
            self.myLogger.error("StatsMgr starting before proper initialization - crashing")
            return 2112

        try:
            self.myLogger.debug1("StatsMgr starting all threads")
            #Set logger must be called since Oscar launches Stats as a process with 'fork'. If the counter is not
            #created again in the child process then a collision will occur. The logger is thread-safe BUT NOT process-safe
            self.myAggregator.start()
            self.myPacer.start()
            self.myLogger.debug1("StatsMgr threads started")
    
            # This loop makes sure that if a thread dies all the module dies with it

            reloadCounters = False

            while(True):

                abort = False

                if not self.myAggregator.isRunning():
                    if not reloadCounters:
                        #Aggregator really died
                        self.myLogger.error("Stats aggregator thread died - script aborts")
                        abort = True
                        #Kill other thread
                        self.myPacer.end()
                    else:
                        # rebuild the database and restart the threads
                        (newCounters, deletedCounters) = self.myPacer.getNewAndDeletedCounters()
                        if newCounters or deletedCounters:
                            self.myLogger.notice("Stats reloading new counters (%d new. %d deleted)" % (len(newCounters), len(deletedCounters)))
                            self.myCountersDBInfo.update(newCounters)
                            for key in deletedCounters:
                                del(self.myCountersDBInfo[key])
                            self.__initWorkers()
                            self.myAggregator.start()
                            self.myPacer.start()
                            self.myLogger.notice("Stats reloaded with %d new counters", len(newCounters))
                        else:
                            self.myLogger.error("Asked to load new counters but list is empty")

                        reloadCounters = False

                if not self.myPacer.isRunning() and not abort:

                    if not reloadCounters and self.myPacer.needUpdate():
                        #Pacer discovered new regex counters and need to re-initialize
                        self.myLogger.notice("Stats discovered new counters - Ask to reload")
                        self.myAggregator.end()
                        reloadCounters = True

                    if not reloadCounters:
                        #Pacer really died
                        abort = True
                        self.myLogger.error("Stats sampler-pacer thread died - Script aborts")
                        #Kill other thread
                        self.myAggregator.end()
    
                if not reloadCounters:
                    #We want the script to die if one of its threads dies but it is not urgent
                    time.sleep(3)
                
                #Shut down
                if abort:
                    self.myLogger.notice("Stats main thread finished and is shutting down")
                    return 10101010
        except:
            self.myLogger.notice("Exception in main thread. Exception details: %s" % (formatExceptionInfo()))
            self.myLogger.debug2("Killing sampler-pacer thread")
            self.myPacer.end()
            self.myLogger.debug2("Killing aggregation thread")
            self.myAggregator.end()
            self.myLogger.debug2("Killing rrd writer thread")
            self.myRrdWriter.end()
            return 8873

        self.myLogger.notice("Stats main thread finished and is shutting down")
        return 0

    def loadCountersConfigurations (self):
        countersConfig = ConfigParser()
        try:
            countersConfig.read(self.myCountersListFilePath)
        except:
            self.myLogger.error("Couldn't open counters configuration file. Path: %s. Exception details: %s" % (self.myCountersListFilePath, formatExceptionInfo()))
            return (None, None)

        #deserialize
        return self.__createDBInfoObject(countersConfig)

    #If the path contains a regex number range indication - generates path for each step of the range
    def getCounterVariations(self, counterPath):

        notDone = [counterPath]
        result = []

        while len(notDone):
            counterToPermutate = notDone.pop(0)
            startIndex = counterToPermutate.find('(')
            if startIndex > -1:
                endIndex = counterToPermutate.find(')')
                pathRange = counterToPermutate[startIndex+1:endIndex]
                delimiterIndex = pathRange.find('-')
                rangeMin = int(pathRange[:delimiterIndex])
                rangeMax = int(pathRange[delimiterIndex+1:])+1
            else:
                startIndex = counterToPermutate.find('{')
                if startIndex > -1:
                    endIndex = counterToPermutate.find('}')
                    specialToken = counterToPermutate[startIndex+1:endIndex]
                    rangeMin = 0
                    rangeMax = self.myLineCfg.get(specialToken)
                    if rangeMax is None:
                        self.myLogger.error("Got unknown special token %s. Ignore %s" % (specialToken, counterToPermutate))
                        continue
                    if rangeMax == 0:
                        # If the variable value is 0, there should be no such counters
                        self.myLogger.notice("Skip %s. %s is 0" % (counterToPermutate, specialToken))
                        continue
                else:
                    result.append(counterToPermutate)
                    continue

            counterPathPrefix = counterToPermutate[:startIndex]
            counterPathSuffix = counterToPermutate[endIndex+1:]

            for i in range(rangeMin, rangeMax):
                newPath = ''.join([counterPathPrefix, str(i), counterPathSuffix])
                if newPath.find('(') > -1 or newPath.find('{') > -1:
                    notDone.append(newPath)
                else:
                    result.append(newPath)

        return result


    def __calcNumHistoryFiles (self, delaySeconds):
        return (delaySeconds/60) * 2


    def __readLineRunningCfg (self):

        try:
            self.myLogger.debug1("Reading line running cfg from %s" % self.mylineRunningCfgFile)
            self.myLineCfg = a.infra.format.json.readFromFile(self._baseLogger, self.mylineRunningCfgFile)
            self.myLogger.notice("Read line running cfg: %s" % self.myLineCfg)
        except Exception as ex:
            self.myLogger.warning("Can't read line cfg from file %s. %s" % (self.mylineRunningCfgFile, ex))
            self.myLineCfg = {}


    # Receives the configurations and 'deserialize' it
    def __createDBInfoObject (self, countersConfig):

        __pychecker__ = 'maxlocals=60'

        defaultSamplingRate = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_ARCHAIVE_SAMPLING_RATE, configurationsDefaults))
        defaultArchaiveErrorRate = float(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_ARCHAIVE_ERROR_RATE, configurationsDefaults))
        # defaultConsolidationFunction = getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_FUNCTION, configurationsDefaults)

        #Version 1.0: In order to prevent property hell. Each property has to be defined here first. Later, this will happen at the processes side
        legalProperties = getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_LEGAL_PROPERTIES, configurationsDefaults)            

        defaultSamplingRate = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_ARCHAIVE_SAMPLING_RATE, configurationsDefaults))

        self.myWritePeriod = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_WRITE_PERIOD, configurationsDefaults))
        self.myRrdUpdateBurstCount = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_RRD_UPDATE_BURST_COUNT, configurationsDefaults))
        self.myRrdUpdateBurstInterval = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_RRD_UPDATE_BURST_INTERVAL, configurationsDefaults))
        self.myAggrUpdateBurstCount = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_AGGR_UPDATE_BURST_COUNT, configurationsDefaults))
        self.myAggrUpdateBurstIntervalMsec = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_AGGR_UPDATE_BURST_INTERVAL_MSEC, configurationsDefaults))
        self.myStartupGracePeriod = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_STARTUP_GRACE_PERIOD, configurationsDefaults))
        enableRecoveryString = str(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_ENABLE_RECOVERY, configurationsDefaults)).lower()
        self.myEnableRecovery = (enableRecoveryString == 'true')

        #Get all counter names - also sections
        configSectionsList = countersConfig.sections()
        
        #Counters list - function output
        counters = {}
        regexCounters = {}
        ProcessCommChannel = {}
        
        for counterSection in configSectionsList:
            lastSlashIndex = counterSection.rfind('/')
            counterPath = counterSection[:lastSlashIndex]
            counterName = counterSection[lastSlashIndex+1:]
            processName = getSysParamOrExit(countersConfig, counterSection, CFG_PROCESS_NAME, self.myLogger)

            countersToAdd = self.getCounterVariations(counterName)
            for counterName in countersToAdd:

                #Is it a regex counter?
                #We can't identify it ourselves becasue some counter names contain special characters
                isRegex = getSysParamOrDefault(countersConfig, counterSection, CFG_REGEX, configurationsDefaults)
                if isRegex:
                    try:
                        re.compile(counterName)
                    except re.error:
                        self.myLogger.error("Regex counter can't be compiled (ignored) \"%s/%s\" in process%s" % (counterPath, counterName, processName))
                        continue
    
                counterPathsToAdd = self.getCounterVariations(counterPath)
                for counterPathVariation in counterPathsToAdd:

                    self.myLogger.debug1("Adding counter [%s] %s/%s" % (processName, counterPathVariation, counterName))
    
                    archaives = []
                    properties = []
        
                    #Set default values
                    #Check if this counter has defined a different consolidation function other than 'AVARAGE'
                    countersConsilidationFunction = getSysParamOrDefault(countersConfig, counterSection, CFG_COUNTER_CONSOLIDATION_FUNCTION, configurationsDefaults)
                    countersSamplingRate = defaultSamplingRate
                    countersArchaiveError = defaultArchaiveErrorRate
        
                    #Default consolidations
                    countersConsolidationSpanLatest = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_SPAN_LATEST, configurationsDefaults))
                    countersConsolidationSpanMid = getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_SPAN_MID, configurationsDefaults)
                    if countersConsolidationSpanMid:
                        countersConsolidationSpanMid = int(countersConsolidationSpanMid)
                    countersConsolidationSpanOld = getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_ARCHAIVE_CONSOLIDATION_SPAN_OLD, configurationsDefaults)
                    if countersConsolidationSpanOld:
                        countersConsolidationSpanOld = int(countersConsolidationSpanOld)
                    
                    #Default rows to keep
                    countersRowsToKeepLatest = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_ARCHAIVE_ROWS_TO_KEEP_LATEST, configurationsDefaults))
                    countersRowsToKeepMid = getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_ARCHAIVE_ROWS_TO_KEEP_MID, configurationsDefaults)
                    if countersRowsToKeepMid:
                        countersRowsToKeepMid = int(countersRowsToKeepMid)
                    countersRowsToKeepOld = getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_ARCHAIVE_ROWS_TO_KEEP_OLD, configurationsDefaults)
                    if countersRowsToKeepOld:
                        countersRowsToKeepOld = int(countersRowsToKeepOld)
        
                    archaivesSamplingFactor = 1 #Must be 1
                    #Check if this counter has defined a different sampling rate class other than 'Normal'
                    if hasNoneEmptyOption(countersConfig, counterSection, CFG_COUNTER_SAMPLING_RATE_CLASS):
                        samplingRateClass = countersConfig.get(counterSection, CFG_COUNTER_SAMPLING_RATE_CLASS)
        
                        if samplingRateClass == samplingRateClassEnum.HIGH:
                            highSamplingRate = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_HIGH_SAMPLING_RATE_CLASS, configurationsDefaults))
                            archaivesSamplingFactor = countersSamplingRate/highSamplingRate
                            countersSamplingRate = highSamplingRate
                        if samplingRateClass == samplingRateClassEnum.SUPER:
                            superSamplingRate = int(getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DEFAULT_SUPER_SAMPLING_RATE_CLASS, configurationsDefaults))
                            archaivesSamplingFactor = countersSamplingRate/superSamplingRate
                            countersSamplingRate = superSamplingRate
        
                        if archaivesSamplingFactor<1:
                            self.myLogger.error("Sampling rate classes where defined incorrectly")
                            return None
        
                    #Default archaive - latest
                    archObj1 = DataSetArchaive()
                    archObj1.init(countersConsilidationFunction, countersArchaiveError, countersConsolidationSpanLatest*archaivesSamplingFactor, countersRowsToKeepLatest)
                    archaives.append(archObj1)
                    #Default archaive - mid
                    if countersConsolidationSpanMid:
                        archObj2 = DataSetArchaive()
                        archObj2.init(countersConsilidationFunction, countersArchaiveError, countersConsolidationSpanMid*archaivesSamplingFactor, countersRowsToKeepMid)
                        archaives.append(archObj2)
                    #Default archaive - old
                    if countersConsolidationSpanOld:
                        archObj3 = DataSetArchaive()
                        archObj3.init(countersConsilidationFunction, countersArchaiveError, countersConsolidationSpanOld*archaivesSamplingFactor, countersRowsToKeepOld)
                        archaives.append(archObj3)
        
                    #Custom Archaives
                    countersCustomArchaives = getSysParamOrDefault(countersConfig, counterSection, CFG_COUNTER_CUSTOM_ARCHAIVES, configurationsDefaults)
                    if countersCustomArchaives:
                        for customArchaive in countersCustomArchaives:
                            #Archaive tuple format: [('Archaive Consilidation Function', Error Rate, Consilidation Span, Rows To Keep)]
                            archObj = DataSetArchaive()
                            archObj.init(customArchaive[0], customArchaive[1], customArchaive[2],customArchaive[3])
                            archaives.append(archObj)
            
                    #Properties
                    countersProperties = getSysParamOrDefault(countersConfig, counterSection, CFG_COUNTER_PROPERTIES, configurationsDefaults)            
                    if countersProperties:
                        #Properties tuple format: [('Property Name', Variable Type - integer/string only, Value)]
                        for prop in countersProperties:
                            if not prop[0] in legalProperties:
                                self.myLogger.error("Property name: %s is ilegal. Only use the defined property names" % prop[0])
                                return None
            
                            propObj = CounterProperty()
                            propObj.init(prop[0], prop[1], prop[2])
                            properties.append(propObj)
        
                    #Check if the process communication is over file
                    commMethod = getSysParamOrDefault(countersConfig, counterSection, CFG_COMM_METHOD, configurationsDefaults)
                    experation = int(getSysParamOrDefault(countersConfig, counterSection, CFG_EXPERATION_TIME, configurationsDefaults))
                    if commMethod == CommMethodTypes.FILE:
                        if processName not in ProcessCommChannel.keys():
                            self.myLogger.info("Creating comm object for process %s" % processName)
                            commObj = StatsCommOverFile(processName, self._baseLogger)
                            commObj.init(self.processCommFileGlobPattern, experation)
                            ProcessCommChannel[processName] = commObj
        
                    #TODO galm validate configuration values
                    isRateField = str(getSysParamOrDefault(countersConfig, counterSection, CFG_COUNTER_IS_RATE, configurationsDefaults)).lower()
                    isRateOnlyField = str(getSysParamOrDefault(countersConfig, counterSection, CFG_COUNTER_RATE_ONLY, configurationsDefaults)).lower()
                    if ("true" == isRateField or "true" == isRateOnlyField):
                        newCounter = CounterDescriptor()
                        rateUnitsStr = str(getSysParamOrDefault(countersConfig, counterSection, CFG_RATE_UNITS, configurationsDefaults))
                        #This means that two counter objects should be created. One for the counter and one for the rate.
                        newCounter.init(countersSamplingRate, 
                              counterPathVariation,
                              processName,
                              counterName, 
                              AggregationCounterType.GAUGE, #It has to be gauge - no dought!
                              COUNTERS_VARIABLE_TYPE,
                              True, #isRate
                              getSysParamOrDefault(countersConfig, counterSection, CFG_COUNTER_DESCRIPTION, configurationsDefaults), 
                              archaives, 
                              properties,
                              getSysParamOrDefault(countersConfig, counterSection, CFG_META_RATE__ARITHMETIC_EXPRESSION, configurationsDefaults),
                              commMethod, False, rateUnitsStr, experation)
                        if not isRegex:
                            counters[newCounter.myCounterId] = newCounter
                        else:
                            regexCounters[newCounter.myCounterId] = newCounter
    
                    if ("false" == isRateOnlyField):
                        counterTypes = getSysParamOrDefault(countersConfig, counterSection, CFG_COUNTER_TYPE, configurationsDefaults)
                        for typeOfCounter in counterTypes:
                            if typeOfCounter== str(AggregationCounterType.COUNTER):
                                shouldPresentCounterAsDefault = getSysParamOrDefault(countersConfig, counterSection, CFG_SHOULD_DEVIDE_COUNTERS_BY_SAMPLING_RATE, configurationsDefaults)
                                counterUnitsStr = str(getSysParamOrDefault(countersConfig, counterSection, CFG_COUNTER_UNITS, configurationsDefaults))
                            else:
                                shouldPresentCounterAsDefault=False
                                if typeOfCounter== str(AggregationCounterType.GAUGE):
                                    counterUnitsStr = str(getSysParamOrDefault(countersConfig, counterSection, CFG_GAUGE_UNITS, configurationsDefaults))
                                else:
                                    counterUnitsStr = ""
                            newCounter = CounterDescriptor()
                            newCounter.init(countersSamplingRate, 
                                      counterPathVariation,
                                      processName,
                                      counterName, 
                                      typeOfCounter.upper(),
                                      COUNTERS_VARIABLE_TYPE,
                                      False, #NOT Rate
                                      getSysParamOrDefault(countersConfig, counterSection, CFG_COUNTER_DESCRIPTION, configurationsDefaults), 
                                      archaives, 
                                      properties,
                                      getSysParamOrDefault(countersConfig, counterSection, CFG_META_COUNTER__ARITHMETIC_EXPRESSION, configurationsDefaults),
                                      commMethod, shouldPresentCounterAsDefault, counterUnitsStr, experation)
                            if not isRegex:
                                counters[newCounter.myCounterId] = newCounter
                            else:
                                regexCounters[newCounter.myCounterId] = newCounter

        return counters, regexCounters, ProcessCommChannel    

    # We need to protect the RRD writer thread from using a DB while the aggr thread is initializing it.
    def getAndLockValuesDb (self):
        self._lockValuesDb()
        return self.myAggregator.myValuesDB

    def unlockValuesDb (self):
        self.myLogger.debug4("Before release values db" )
        self.myValuesDbLock.release()

    def _lockValuesDb (self):
        self.myLogger.debug4("Before lock values db" )
        self.myValuesDbLock.acquire()
        self.myLogger.debug4("After lock values db" )

    def __initWorkers (self):

        # Take values DB lock - now we can destory the aggregator object and create a new one
        self._lockValuesDb()

        #Create stats aggregator
        self.myAggregator = StatsAggregator()
        errFlag = self.myAggregator.init(self.myCountersDBInfo, 
                                         self.myJobsQueue, self.myLogger, self._baseLogger, self.myDataRunDirPath, 
                                         self.myDescriptionDbFilesPath, self.myDbFilesOutputPath, 
                                         getSysParamOrDefault(self.myStatsConfigurations, CFG_SECTION, CFG_DB_FILES_BASE_NAME, configurationsDefaults), 
                                         os.path.join(self.systemConstDir, RRDTOOL_EXE_PATH_CMD),
                                         os.path.join(self.systemConstDir, RRDTOOL_WRAPPER_EXE_PATH_CMD),
                                         os.path.join(self.myStatsDataRootDir, OLD_DATA_PATH),
                                         os.path.join(self.myStatsDataRootDir, PREV_RUN_PATH),
                                         self.myAggrUpdateBurstCount, 
                                         self.myAggrUpdateBurstIntervalMsec,
                                         self.myEnableRecovery)

        # Release values DB lock
        self.unlockValuesDb()

        if errFlag:
            return errFlag

        self.myAggregator.setAggrHistory(self.myAggrHistory)
        self.myAggregator.setNumHistoryFiles(self.myNumHistoryFiles)

        self.myLogger.debug1("StatsMgr aggregator created")   

        # Before starting - get counter's descriptions from the q-shell
        # TODO(amiry) - DO WE REALLY GET COUNTER'S DESCRIPTIONS FROM Q-SHELL ?!?

        sampler = StatsSampler()
        sampler.init(self.myProcessesDictionary, self.myJobsQueue, self.myLogger, self.myMaxJobsQueueSize, self.myCommChanDict)
        if self.myPacer is None:
            self.myPacer = StatsSamplerPacer()
        self.myPacer.init(self.myCountersDBInfo, self.myRegexCounters, self.myLogger, sampler)

    def __makeDirsIfNeeded (self, dirPath):
        try:
            if os.path.exists(dirPath):
                if os.path.isdir(dirPath):
                    return True
                else:
                    return False
            else:
                    oldUmask = os.umask(0)
                    os.makedirs(dirPath)
                    os.umask(oldUmask)
                    return True
        except:
            return False


    #Check that the properties names are unique
    def __validateProperties(self, countersDBInfo):

        propsTypesByNames = {}
        
        for counter in countersDBInfo.values():
            for prop in counter.myProperties:
                if not prop.myName in propsTypesByNames.keys():
                    propsTypesByNames[prop.myName] = prop.myVariableType
                else:
                    if prop.myVariableType != propsTypesByNames[prop.myName]:
                        #ERROR
                        self.myLogger.error("Ambiguous property definition. It is ilegal to have properties with the same name and different type. PropName=%s, Type1=%s, Type2=%s" % (prop.myName, prop.myVariableType, propsTypesByNames[prop.myName]))
                        return 1

        return 0

# === StatsDaemonInfo Class =====================================================================================

# Used to connect to q-shell
class StatsDaemonInfo(object):

    def __init__ (self, aQshellConnectionObject=None, aPid=None):
        self.myqShellObj = aQshellConnectionObject
        self.myPid = aPid
        #Unique to stats script
        #Run in early log mode - otherwise it takes too much time since the logger makes each call last at least one second
        self.myqShellObj.myEarlyLogEnable = True 
        #Masks q-shell errors from stats to make q-shell response parsing easier
        self.myqShellObj.myStderrMask = True

    def getPid(self):
        return self.myPid

    def isUp (self):
        if self.myPid != None:
            return True
        return False

    def runShellCmd(self, command):
        if self.myqShellObj != None:
            return self.myqShellObj.runShellCmd(command)
        else:
            return ("Process qShell object is none", "")

    def toString (self, processName):
        result = "Process name: %s" % processName
        if self.isUp():
            result += "Process up status is: %s" % 'Up'
            result += "Process up status is: %s. Pid: %s" % ('Up', str(self.getPid()))
        else:
            result += "Process up status is: %s" % 'Down'

        if self.myqShellObj:
            result += "Process qshell object received - not None"
        else:
            result += "Process qshell is None"

        return result

########################################################################################################################
class AggrHistory(object):

    def __init__(self, logger):
        self._log = logger
        self._dict = {}
        self._dictLock = threading.Lock()
        self._maxHistoryEntries = 0
        self._reportLimiter = EventReportLimiter(3600)


    def setMaxHistoryEntries(self, maxHistoryEntries):
        self._maxHistoryEntries = maxHistoryEntries


    def getMaxHistoryEntries(self):
        return self._maxHistoryEntries


    def getLock (self):
        """For use with 'with' """
        return self._dictLock


    def lock (self):
        self._log.debug4("Before lock aggr history" )
        self._dictLock.acquire()
        self._log.debug4("After lock aggr history" )


    def unlock (self):
        self._log.debug4("Before release aggr history" )
        self._dictLock.release()


    def keys (self):
        return self._dict.keys()


    def update (self, name, value, valueType, timestamp):

        lst = self._dict.get(name)

        if not lst:
            self._dict[name] = [(value, timestamp, valueType)]
        else:
            if len(lst) < self._maxHistoryEntries:
                lst.append((value, timestamp, valueType))
            else:
                (shouldReport, numEvents) = self._reportLimiter.shouldReport()
                if shouldReport:
                    self._log.error("Aggregator history entry is too long, update discarded (name=%s. size=%s). (Occured %s times since last reported)" % 
                                    (name, len(lst), numEvents))

        self._log.debug5("Update counter id %s values %s" % (name, self._dict[name]))


    def getAndClear (self, name):
        lst = self._dict.get(name, [])
        self._dict[name] = []
        return lst

