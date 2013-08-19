#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: royr
# 

import a.content.storage.content_cleaner , os, time, fnmatch, shutil
from a.stats.stats_comm_over_file_client import StatsCommOverFileClient

if  __package__ is None:
    G_NAME_MODULE_CONTENT_CLEANER_APP = "unknown"
    G_NAME_GROUP_CONTENT_CLEANER_APP_GENERAL = "unknown"
    G_NAME_GROUP_CONTENT_CLEANER_APP_IO = "unknown"
    G_NAME_GROUP_CONTENT_CLEANER_APP_CLEANERS = "unknown"
else:
    from . import G_NAME_MODULE_CONTENT_CLEANER_APP
    from . import G_NAME_GROUP_CONTENT_CLEANER_APP_GENERAL
    from . import G_NAME_GROUP_CONTENT_CLEANER_APP_IO
    from . import G_NAME_GROUP_CONTENT_CLEANER_APP_CLEANERS

# Configuration
SHOULD_REMOVE_CONTENT_UNDER_THRESHOLD=True
MAX_CONTINUOUS_MAIN_LOOP_EXCEPTIONS=1000

class ContentCleanerApp():

    # Consts use for the specificParams dictionary provided on "initspecificParams"
    SPECIFIC_PARAM_KEY_PERSISTENT_META_DIR = "persistent-meta-dir"
    SPECIFIC_PARAM_KEY_VOLATILE_META_BASE_DIR = "volatile-meta-base-dir"
    SPECIFIC_PARAM_KEY_MEDIA_BASE_DIR = "media-base-dir"
    SPECIFIC_PARAM_KEY_EVETS_UPDATES_DIR = "event-updates-dir"
    SPECIFIC_PARAM_KEY_DB_FILE_DIR = "db-file-dir"
    SPECIFIC_PARAM_KEY_META_FILES_EXTENSION = "meta-files-extension"
    SPECIFIC_PARAM_KEY_BAD_FILES_EXTENSION = "bad-files-extension"
    SPECIFIC_PARAM_KEY_PREDICTION_FILES_EXTENSION = "prediction-files-extension"
    SPECIFIC_PARAM_KEY_ACQ_FILES_EXTENSION = "acq-files-extension"
    SPECIFIC_PARAM_KEY_EVENTS_FILES_EXTENSION = "events-files-extension"
    SPECIFIC_PARAM_KEY_SHRED_REQUEST_FILE_NAME = "shred-request-file-name"
    SPECIFIC_PARAM_KEY_PREDICTION_MODE_FILE_NAME = "prediction-mode-file-name"
    SPECIFIC_PARAM_KEY_DELETED_META_ARCHIVE_DIR = "archive-dir"
    SPECIFIC_PARAM_KEY_ARCHIVER_BUFFER_DIR = SPECIFIC_PARAM_KEY_VOLATILE_META_BASE_DIR
    SPECIFIC_PARAM_KEY_DISK_LIST = "disk-list"
    SPECIFIC_PARAM_CLEAN_STATE_ON_LAUNCH = "clean-state-on-launch"
    SPECIFIC_PARAM_KEY_STATUS_RUN_DIR = "status-run-dir"
    # Path to place to write stored titles count to UI, updated once every 10 (?) seconds
    SPECIFIC_PARAM_KEY_STORED_TITLES_PATH = "stored-titles-path"
    # This parameter tells the content cleaner how many .meta files we in the ramdisks when oscar started
    SPECIFIC_PARAM_KEY_INITIAL_STORED_TITLES_COUNT = "initial-stored-titles-count"
    # Path to file where the line priodically updates the amount of .meta files added to the ramdisks
    # since Oscar was started. If file does not exist, it means that line did not start yet, consider it to be 0.
    SPECIFIC_PARAM_KEY_ADDED_STORED_TITLES_PATH = "added-stored-titles-path"


    # Consts for sections/fields names in sys-param
    CONFIG_SECTION_CONTENT_CLEANER_PARAMS = "content-cleaner-params"
    CONFIG_VAR_DISK_USAGE_PERCENT_STOP_ACQ = "disk-usage-percent-stop-acq"
    CONFIG_VAR_DISK_USAGE_PERCENT_TRIGGER = "disk-usage-percent-trigger"
    CONFIG_VAR_DISK_USAGE_PERCENT_TARGET = "disk-usage-percent-target"
    CONFIG_VAR_MAX_NUM_OF_CONTENT_TO_REMOVE = "max_num_of_content_to_remove"
    CONFIG_VAR_LAST_ACCESS_THRESHOLD_MINUTES = "last-access-threshold-minutes"
    CONFIG_VAR_LAST_ACCESS_THRESHOLD_WARN_MINUTES = "last-access-threshold-warn-minutes"
    CONFIG_VAR_CLEAN_CYCLE_INTERVAL_SEC = "clean-cycle-interval-sec"
    CONFIG_VAR_SCAN_NEW_CONTENT_INTERVAL_SEC = "scan-new-content-interval-sec"
    CONFIG_VAR_CLEANERS_STATE_INFO_LOGGING_INTERVAL_SEC = "cleaners-state-logging-interval-sec"
    CONFIG_VAR_STATS_UPDATES_INTERVAL_SEC = "stats-updates-interval-sec"
    CONFIG_VAR_SCAN_BAD_CONTENT_INTERVAL_SEC = "scan-bad-content-interval-sec"
    CONFIG_VAR_MAX_TITLE_COUNT_K = "max-title-count-k"
    CONFIG_VAR_NUM_CONTENT_TO_REMOVE_EACH_ITERATION = "num-content-to-remove-each-iteration"
    CONFIG_VAR_TITLE_STORED_UPDATE_INTERVAL_SEC = "title-stored-update-interval-sec"
    # Archiver 
    CONFIG_VAR_SHOULD_ARCHIVE_META_FILES = "archive-meta-files"
    CONFIG_VAR_ARCHIVE_TOTAL_SIZE_GB = "archive-total-size-gb"
    CONFIG_VAR_ARCHIVE_FILE_SIZE_MB = "archive-file-size-mb"
    CONFIG_VAR_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB = "archiver-buffer-dir-size-limit-mb"
    CONFIG_VAR_ARCHIVER_ROTATION_TRESHOLD_SECONDS = "archiver-rotation-threshold-seconds"

    # Default values for data in sys-param
    DEFAULT_DISK_USAGE_PERCENT_STOP_ACQ = 100
    DEFAULT_DISK_USAGE_PERCENT_TRIGGER = 95
    DEFAULT_DISK_USAGE_PERCENT_TARGET = 95
    DEFAULT_MAX_NUM_OF_CONTENT_TO_REMOVE = -1
    DEFAULT_LAST_ACCESS_THRESHOLD_MINUTES = 120
    DEFAULT_LAST_ACCESS_THRESHOLD_WARN_MINUTES = 240
    DEFAULT_CLEAN_CYCLE_INTERVAL_SEC = 10
    DEFAULT_SCAN_NEW_CONTENT_INTERVAL_SEC = 900
    DEFAULT_CLEANERS_STATE_INFO_LOGGING_INTERVAL_SEC = 0
    DEFAULT_STATS_UPDATES_INTERVAL_SEC = 60
    DEFAULT_SCAN_BAD_CONTENT_INTERVAL_SEC = 120
    DEFAULT_MAX_TITLE_COUNT_K = 1500
    DEFAULT_NUM_CONTENT_TO_REMOVE_EACH_ITERATION = 1
    DEFAULT_TITLE_STORED_UPDATE_INTERVAL_SEC = 5
    # Archiver 
    DEFAULT_SHOULD_ARCHIVE_META_FILES = True
    DEFAULT_ARCHIVE_TOTAL_SIZE_GB = 10
    DEFAULT_ARCHIVE_FILE_SIZE_MB = 10
    DEFAULT_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB = 30
    DEFAULT_ARCHIVER_ROTATION_TRESHOLD_SECONDS = 3600




    def __init__ (self):

        self._contentCleaners = a.content.storage.content_cleaner.ContentCleanerGroup(self.doPeriodicWork)
        self._wasContentCleanersInitialized = False
        self._keepRunning = True

        #-----------configuration--------------------------#
        self._diskList = None
        self._contentCleanerCfg = None
        self._predictionSignalFile = None
        self._shredRequestFileName = None
        self._shouldClearStateFilesOnLaunch = None
        self._totalMaxTitleCount = None

        # Interval in seconds for doing cleaning actions
        self._cleanCycleIntervalSec = None
        self._stateLoggingIntervalSec = None
        self._newContentScanIntervalSec = None
        self._badContentScanIntervalSec = None
        self._intervalForDumpingDictToFileMinutes = None
        self._updatingTitleStoredFileIntervalSec = None


        self._lastAccessUpdatesDir = None
        self._lastAccessEventsFilesPattern = None


        #------ Timing ----------#
        self._lastTimeScannedContent = None
        self._lastTimeScannedBad = None
        self._lastTimeDumpedDict = None
        self._lastTimeCleaned = None
        self._lastLoggedState = None
        self._lastTimeUpdatedTitlesStoredFile = None

        #------ Counters ----------#
        self.counters = {'numTotalEventFilesScanned':0}
        self.cleanIterationCounters = {'totalAvgRemovedPerDisk':0,
                                       'numOfIterations':0,
                                       'peakRemovedPerIterationPerDisk':0,
                                       'peakRemovedPerIteration':0,
                                       'totalRemoved':0}


        #--------Stats--------------#
        self._statsReportingIntervalSec = None
        self._stats = None 
        self._statsDir = None
        self._lastTimeSentStats = None
        self._lastTimeresetMaxUsageCounters = None

        #-------- per cgid deletion ----#
        self._perCgidCleanStatusFile = None
        self._cgidRequestedForDeletion = None
        self._prevNeedToBeMarkedBad = -1


        #-------- Title count updates ----#
        self._initialTitleCount = None
        self._storedTitlePath = None
        self._addedStoredTitlePath = None
        self._addedStoredTitlePathWasFound = False
        


    def daemonControlInitLogger(self, logger):
        """Init the class logger to be used.

        Init the logger. 
        This function shall be called before any other functions of the class

        Args:
            logger: a logger from which new loggers shall be created

        Returns:
            None

        Raises:
            None
        """

        self._logGeneral= logger.createLogger(G_NAME_MODULE_CONTENT_CLEANER_APP, G_NAME_GROUP_CONTENT_CLEANER_APP_GENERAL)
        self._logIo= logger.createLogger(G_NAME_MODULE_CONTENT_CLEANER_APP, G_NAME_GROUP_CONTENT_CLEANER_APP_IO)
        self._logContentCleaners = logger.createLogger(G_NAME_MODULE_CONTENT_CLEANER_APP, G_NAME_GROUP_CONTENT_CLEANER_APP_CLEANERS)
        self._contentCleaners.initLogger(self._logContentCleaners)



    def daemonControlInitExternalData(self, sysParamsCfg, specificParams):
        """Init the data provided from outside

        Init the data provided from outside - both from configuration and operational consts

        Args:
            sysParamsCfg: a contatiner holding the sys params base configuration (that are destined to move to blinky)
            specificParams: a dictionary holding the data under the "SPECIFIC_PARAM_KEY_..." keys defined at the begining of this class                                            

        Returns:
            None

        Raises:
            None
        """

        self._contentCleanerCfg = a.content.storage.content_cleaner.ContentCleanerCfg()
        self._contentCleanerCfg.metaPersistentBaseDir = specificParams[self.SPECIFIC_PARAM_KEY_PERSISTENT_META_DIR]
        self._contentCleanerCfg.metaRamBaseDir = specificParams[self.SPECIFIC_PARAM_KEY_VOLATILE_META_BASE_DIR]
        self._contentCleanerCfg.mediaBaseDir = specificParams[self.SPECIFIC_PARAM_KEY_MEDIA_BASE_DIR]
        

        self._lastAccessUpdatesDir = specificParams[self.SPECIFIC_PARAM_KEY_EVETS_UPDATES_DIR]
        self._contentCleanerCfg.dbFilesDir = specificParams[self.SPECIFIC_PARAM_KEY_DB_FILE_DIR]
        self._contentCleanerCfg.metaFilesExtension = specificParams[self.SPECIFIC_PARAM_KEY_META_FILES_EXTENSION] 
        self._contentCleanerCfg.badFilesExtension = specificParams[self.SPECIFIC_PARAM_KEY_BAD_FILES_EXTENSION]
        self._lastAccessEventsFilesPattern = '*.' + specificParams[self.SPECIFIC_PARAM_KEY_EVENTS_FILES_EXTENSION]
        self._predictionSignalFile = specificParams[self.SPECIFIC_PARAM_KEY_PREDICTION_MODE_FILE_NAME]
        self._contentCleanerCfg.isPrediction = os.path.exists(self._predictionSignalFile)
        self._shredRequestFileName = specificParams[self.SPECIFIC_PARAM_KEY_SHRED_REQUEST_FILE_NAME]
        self.__perCgidCleanStatusFile = os.path.join(specificParams[self.SPECIFIC_PARAM_KEY_STATUS_RUN_DIR],"cgid-clean-status")
        self._contentCleanerCfg.metaPredictionFilesExtension = specificParams[self.SPECIFIC_PARAM_KEY_PREDICTION_FILES_EXTENSION]
        self._contentCleanerCfg.acqFilesExtension = specificParams[self.SPECIFIC_PARAM_KEY_ACQ_FILES_EXTENSION]
        self._diskList = specificParams[self.SPECIFIC_PARAM_KEY_DISK_LIST]
        # Sanity check
        if len(self._diskList) == 0:
            raise Exception("can't start content cleaner for 0 disks.")
        self._initialTitleCount = specificParams[self.SPECIFIC_PARAM_KEY_INITIAL_STORED_TITLES_COUNT]
        self._storedTitlePath = specificParams[self.SPECIFIC_PARAM_KEY_STORED_TITLES_PATH]
        self._addedStoredTitlePath = specificParams[self.SPECIFIC_PARAM_KEY_ADDED_STORED_TITLES_PATH]
        self._shouldClearStateFilesOnLaunch = specificParams[self.SPECIFIC_PARAM_CLEAN_STATE_ON_LAUNCH]


        self._stateLoggingIntervalSec = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                            self.CONFIG_VAR_CLEANERS_STATE_INFO_LOGGING_INTERVAL_SEC, 
                                                            self.DEFAULT_CLEANERS_STATE_INFO_LOGGING_INTERVAL_SEC)

        self._contentCleanerCfg.diskUsagePercentStopAcq = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                              self.CONFIG_VAR_DISK_USAGE_PERCENT_STOP_ACQ, 
                                                                              self.DEFAULT_DISK_USAGE_PERCENT_STOP_ACQ)

        self._contentCleanerCfg.diskUsagePercentTrigger = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                              self.CONFIG_VAR_DISK_USAGE_PERCENT_TRIGGER, 
                                                                              self.DEFAULT_DISK_USAGE_PERCENT_TRIGGER)

        self._contentCleanerCfg.diskUsagePercentTarget = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                             self.CONFIG_VAR_DISK_USAGE_PERCENT_TARGET, 
                                                                             self.DEFAULT_DISK_USAGE_PERCENT_TARGET)

        self._contentCleanerCfg.maxNumOfContentToRemove = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                              self.CONFIG_VAR_MAX_NUM_OF_CONTENT_TO_REMOVE, 
                                                                              self.DEFAULT_MAX_NUM_OF_CONTENT_TO_REMOVE)
               
        self._contentCleanerCfg.lastAccessThresholdMinutes = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                                 self.CONFIG_VAR_LAST_ACCESS_THRESHOLD_MINUTES, 
                                                                                 self.DEFAULT_LAST_ACCESS_THRESHOLD_MINUTES)

        
        self._contentCleanerCfg.lastAccessThresholdWarnMinutes = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                                     self.CONFIG_VAR_LAST_ACCESS_THRESHOLD_WARN_MINUTES, 
                                                                                     self.DEFAULT_LAST_ACCESS_THRESHOLD_WARN_MINUTES)

        self._contentCleanerCfg.shouldRemoveContentUnderThreshold = SHOULD_REMOVE_CONTENT_UNDER_THRESHOLD

        self._cleanCycleIntervalSec = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                          self.CONFIG_VAR_CLEAN_CYCLE_INTERVAL_SEC, 
                                                          self.DEFAULT_CLEAN_CYCLE_INTERVAL_SEC)

        self._newContentScanIntervalSec = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                              self.CONFIG_VAR_SCAN_NEW_CONTENT_INTERVAL_SEC, 
                                                              self.DEFAULT_SCAN_NEW_CONTENT_INTERVAL_SEC)

        self._contentCleanerCfg.modificationCheckThresholdMinutes = int(self._newContentScanIntervalSec/60)

        self._statsReportingIntervalSec = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                              self.CONFIG_VAR_STATS_UPDATES_INTERVAL_SEC, 
                                                              self.DEFAULT_STATS_UPDATES_INTERVAL_SEC) 

        self._badContentScanIntervalSec = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                              self.CONFIG_VAR_SCAN_BAD_CONTENT_INTERVAL_SEC, 
                                                              self.DEFAULT_SCAN_BAD_CONTENT_INTERVAL_SEC)

        self._intervalForDumpingDictToFileMinutes = self._contentCleanerCfg.lastAccessThresholdMinutes / 4


        self._totalMaxTitleCount = 1000*sysParamsCfg.getFloat(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                            self.CONFIG_VAR_MAX_TITLE_COUNT_K, 
                                                            self.DEFAULT_MAX_TITLE_COUNT_K)

        self._contentCleanerCfg.maxTitleCount = int(self._totalMaxTitleCount / len(self._diskList))

        self._contentCleanerCfg.numContentToRemoveEachIteration = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                                      self.CONFIG_VAR_NUM_CONTENT_TO_REMOVE_EACH_ITERATION, 
                                                                                      self.DEFAULT_NUM_CONTENT_TO_REMOVE_EACH_ITERATION)

        self._updatingTitleStoredFileIntervalSec = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                       self.CONFIG_VAR_TITLE_STORED_UPDATE_INTERVAL_SEC, 
                                                                       self.DEFAULT_TITLE_STORED_UPDATE_INTERVAL_SEC)

        #-------------------------- Archiver config -------------------------------------------------------
   
        self._contentCleanerCfg.archiverOutputDir = specificParams[self.SPECIFIC_PARAM_KEY_DELETED_META_ARCHIVE_DIR]
        self._contentCleanerCfg.archiverBufferDir = specificParams[self.SPECIFIC_PARAM_KEY_ARCHIVER_BUFFER_DIR]

        self._contentCleanerCfg.shouldArchive = sysParamsCfg.getBool(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                     self.CONFIG_VAR_SHOULD_ARCHIVE_META_FILES, 
                                                                     self.DEFAULT_SHOULD_ARCHIVE_META_FILES)

        self._contentCleanerCfg.archiverOutDirSizeLimitGb = sysParamsCfg.getFloat(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                                  self.CONFIG_VAR_ARCHIVE_TOTAL_SIZE_GB, 
                                                                                  self.DEFAULT_ARCHIVE_TOTAL_SIZE_GB)

        self._contentCleanerCfg.archiverOutFileSizeLimitMb = sysParamsCfg.getFloat(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                                   self.CONFIG_VAR_ARCHIVE_FILE_SIZE_MB, 
                                                                                   self.DEFAULT_ARCHIVE_FILE_SIZE_MB)

        self._contentCleanerCfg.archiverBufferDirSizeLimitMb = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                                  self.CONFIG_VAR_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB, 
                                                                                  self.DEFAULT_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB)

        self._contentCleanerCfg.archiverRotationTimeTresholdSeconds = sysParamsCfg.getInt(self.CONFIG_SECTION_CONTENT_CLEANER_PARAMS, 
                                                                                          self.CONFIG_VAR_ARCHIVER_ROTATION_TRESHOLD_SECONDS, 
                                                                                          self.DEFAULT_ARCHIVER_ROTATION_TRESHOLD_SECONDS)
       

        self._contentCleaners.initCfg(self._contentCleanerCfg)

        if self._wasContentCleanersInitialized:
            self._updateCfg()

        self._wasContentCleanersInitialized = True






    def daemonControlInitStats(self, statsDir):
        """
        Init Stats Dir
        """
        self._statsDir = statsDir



    def _init(self):
        """Initializing the module

        Args:
            None

        Returns:
            None

        Raises:
            None
        """

        # Lets create the disksSetList
        disksSetList = []
        for diskNumStr in self._diskList:         
            disksSet = []                                            
            disksSet.append(int(diskNumStr))                                       
            disksSetList.append(disksSet)   
            
        self._logGeneral("cfg-on-launch").notice("starting with disksSetList: %s", disksSetList)

        self._contentCleaners.createAndInitContentCleaners(disksSetList)

        self._contentCleaners.startArchiver(self.archiverThreadExceptionCallBack)

        # Init the stats object
        self._stats = StatsCommOverFileClient("content_cleaner", self._logGeneral)
        self._stats.init(self._statsDir)

        self._logGeneral("cfg-on-launch").notice("Starting content cleaners. configuration:%s", self._contentCleanerCfg)
        self._logGeneral("archiver-dir-init-info").notice("base input dir given to content cleaners archiver is: %s" , self._contentCleanerCfg.archiverBufferDir)

        return True
            

    #-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStart(self):
        """launching the process"""
        if not self._init():
            a.infra.process.processFatal("Failed initializing content_cleaner")


    #-----------------------------------------------------------------------------------------------------------------------
    def daemonControlRun(self):
        """getting into the main loop"""
        if not self._mainLoop():
            self._logGeneral("done-error").error("process exited with error")
        else:
            self._logGeneral("done-ok").notice("process terminated")

    


    def daemonControlStop (self):
        """stopping the module

        This function is called from a context of signal handling. just set the stop flag or you will get into deep shit
        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self.stop()


    def stop (self):
        self._keepRunning = False
        self._contentCleaners.stop()


    def archiverThreadExceptionCallBack (self, exception):
        self._logGeneral("archiver-thread-exception").error("got exception '%s' from archiver thread. exiting", exception)
        self.stop()



    def doPeriodicWork (self):
        self._calculateAndUpdateTitleCountIfNeeded()
        self._sendStatsAndResetMaxCountersIfNeeded()



    def _sendStatsAndResetMaxCountersIfNeeded (self):
        currentTime = time.time()

        sendStats = False
        if (self._lastTimeSentStats == None) or (currentTime - self._lastTimeSentStats >= self._statsReportingIntervalSec):
            sendStats = True
            self._lastTimeSentStats = currentTime

        if sendStats:
            self._logGeneral("main-loop-stats").debug3("sending stats counters")
            aggregatedCounters = self._getAggregatedCounters()
            self._stats.send(aggregatedCounters)
            self._contentCleaners.resetMaxDiskUsageCounters()
            self.cleanIterationCounters['peakRemovedPerIterationPerDisk'] = 0
            self.cleanIterationCounters['peakRemovedPerIteration'] = 0

        
   

    def _mainLoop (self):

        # Maybe we need to clear the state on disk
        if self._shouldClearStateFilesOnLaunch:
            self._contentCleaners.clearStateOnDisk()
        elif self._keepRunning:
            self.doPeriodicWork()
            currentTime = time.time()
            # Load the dict from disk if exists
            try:
                self._logGeneral("start-loading-db").debug1("starting to load db")
                self._contentCleaners.loadFromDiskMultiThreaded()
                self._logGeneral("finished-loading-db").debug1("finished loading db. total time is: %.6f", time.time() - currentTime)
            except Exception as ex:
                self._logGeneral("save-db-error").error("error loading cleaners state. exception: %s", ex)
            self._removeOldDbTmpFiles()
        self._updatePerCgidCleanStatus("")
        
        continuousExceptionsCounter = 0
        
        while self._keepRunning:

            if continuousExceptionsCounter >= MAX_CONTINUOUS_MAIN_LOOP_EXCEPTIONS:
                self._logGeneral("too-many-exceptions").error("got %d exceptions", continuousExceptionsCounter)
                raise Exception("too many exceptions in main loop")

            try:
                # Do periodic work
                self.doPeriodicWork()
    
                currentTime = time.time()
                # Check whether or not to log cleaners state
                logState = False
                if self._stateLoggingIntervalSec != 0:
                    if (self._lastLoggedState == None) or (currentTime - self._lastLoggedState >= self._stateLoggingIntervalSec):
                        logState = True
                        self._lastLoggedState = currentTime
                
                if logState:
                    self._logCleanersState()
    
                # check for per cgid clean request before the check for content scan
                self._checkForPerCgidCleanRequests()
    
                currentTime = time.time()
                # Check whether or not to scan for content
                performCleaningAction = False
                if (self._lastTimeCleaned == None) or (currentTime - self._lastTimeCleaned >= self._cleanCycleIntervalSec):
                    performCleaningAction = True
                    self._lastTimeCleaned = currentTime
    
                if performCleaningAction :
                    self._cleanContent()
    
                # Maybe we have configuration changes
                self._checkForCfgChanges()
    
                # Maybe we need to shred all content
                self._checkForShredRequest()
    
                # Maybe we need to clean some content
                self._checkForPendingCgidToDelete ()
    
                # Sleep for 0.5 sec
                time.sleep(0.5)

                # No exception so far. We can reset the counter
                continuousExceptionsCounter = 0

            except Exception as ex:
                self._logGeneral("main-loop-error").error("got exception on main loop. exception: %s", ex)
                continuousExceptionsCounter += 1
                time.sleep(0.1)


        # We are going to exit the main loop. We dump the dict to file before we exit
        try:
            self._contentCleaners.saveToDiskMultiThreaded()
        except Exception as ex:
            self._logGeneral("save-db-error").error("error saving cleaners state. exception: %s", ex)
            return False

        return True


    def _checkForCfgChanges (self):
        hasCfgChanged = False

        # prediction mode change
        isPrediction = os.path.exists(self._predictionSignalFile)

        self._logContentCleaners("prediction-mode-signal").debug3("%s: prediction mode siganl - %s", 
                                                          self._predictionSignalFile, isPrediction)

        if (isPrediction != self._contentCleanerCfg.isPrediction):
            self._logContentCleaners("prediction-mode-update").info("prediction mode change notification")
            self._contentCleanerCfg.isPrediction = isPrediction
            hasCfgChanged = True

        # update configuration (if needed)
        if hasCfgChanged is True: 
            self._updateCfg()



    def _checkForShredRequest (self):
        if os.path.exists(self._shredRequestFileName):
            try:
                # First update title stored and get the current title count
                correntTitleCount = self._calculateAndUpdateTitleCountIfNeeded(True)
                self._contentCleaners.shredAll()
                # Update the numRemoved counter for title count
                self._updateNumRemoved(correntTitleCount)
                os.remove(self._shredRequestFileName)
            except Exception,e:
                self._logIo("shred-all-content").error("ShredAllContent() encountered an exception: %s", str(e))

    def _checkForPerCgidCleanRequests (self):
        perCgidFile="%s-cgid" % self._shredRequestFileName
        if os.path.exists(perCgidFile):
            try:
                fd=open(perCgidFile)
                if fd is not None:
                    cgidString=fd.readline().strip()
                    if len(cgidString) == 0:
                        self._logIo("clean-per-cgid-empty").error("cleanPerCgidContent() got empty cgid directive")
                    else:
                        self._logIo("clean-per-cgid-trigger").debug1("cleanPerCgidContent() triggered for %s",cgidString)
                        cgid=int(cgidString)
                        self._cgidRequestedForDeletion = cgid
                        #this should trigger a scan in the nearest round
                        self._lastTimeCleaned = None
                        self._lastTimeScannedContent = None
                    fd.close()
                os.remove(perCgidFile)
            except Exception,e:
                self._logIo("clean-per-cgid").error("cleanPerCgidContent() encountered an exception: %s", str(e))
                if os.path.exists(perCgidFile):
                    os.remove(perCgidFile)




    def _updatePerCgidCleanStatus (self,msg):
        tmpName = "%s-tmp" % self.__perCgidCleanStatusFile
        fd=open(tmpName ,"w")
        if fd is None:
            self._logIo("clean-per-cgid").error("_updatePerCgidCleanStatus failed to open %s for write", tmpName)
        else:
            fd.write("%s\n" % msg)
            fd.close()
            os.rename(tmpName,self.__perCgidCleanStatusFile)



    def _checkForPendingCgidToDelete (self):
        if self._cgidRequestedForDeletion is not None:
            self._prevNeedToBeMarkedBad = -1 # make it dirty so that we update the file
            self._contentCleaners.scanAndMarkCgidToClean(self._cgidRequestedForDeletion)
            #clear the cgid indication
            self._cgidRequestedForDeletion = None
        #start doing a portion of the work - maybe all of it
        self._contentCleaners.markBadPerCgidContent()
        needToBeMarkedBad = self._contentCleaners.getPerCgidDeletionStatus()
        msg=""
        soFar="So far deleted %d" % self._contentCleaners.totalMarkedBadByPerCgidContentClean
        if needToBeMarkedBad==0:
            msg="No site specific titles queued for deletion. %s" % soFar
        else:
            msg="%d site specific titles are currently queued for deletion. %s" % (needToBeMarkedBad , soFar)
            self._logIo("clean-per-cgid-active").debug1(msg) 
            # get the cleaner working also in the next round
            self._lastTimeCleaned = None
        #update file upon change
        if self._prevNeedToBeMarkedBad != needToBeMarkedBad:
            self._updatePerCgidCleanStatus(msg)
        self._prevNeedToBeMarkedBad = needToBeMarkedBad

            




    def _cleanContent (self):
        try:
            #### Scanning New files task ##################
            # Let's see if it's time to scan for new media. (maybe it's the first time)
            currentTime = time.time()
            scanForNewContent = False
            if (self._lastTimeScannedContent == None) or (currentTime - self._lastTimeScannedContent >= self._newContentScanIntervalSec):
                scanForNewContent = True
                self._lastTimeScannedContent = currentTime
                    
            # Scan for new media if necessary
            if scanForNewContent:
                self._logGeneral("start-scan").debug1("starting scanning for NEW content.")
                self._contentCleaners.scanContent()
                self._logGeneral("finished-scan").debug1("finished scanning for NEW content. total time is: %.6f", time.time() - currentTime)
    
    
            #### Scanning Bad files task ##################
            # Let's see if it's time to scan for BAD media. (maybe it's the first time)
            currentTime = time.time()
            scanForBadContent = False
            if (self._lastTimeScannedBad == None) or (currentTime - self._lastTimeScannedBad >= self._badContentScanIntervalSec):
                scanForBadContent = True
                self._lastTimeScannedBad = currentTime
                    
            # Scan for new media if necessary
            if scanForBadContent:
                self._logGeneral("start-scan-bad").debug1("starting scanning for BAD content.")
                self._contentCleaners.scanBadContent()
                self._logGeneral("finished-scan-bad").debug1("finished scanning for BAD content. total time is: %.6f", time.time() - currentTime)
            
    
            #### Load updates from muncher task ##################
            # Load lastAccessEvents and update the db
            if self._keepRunning :
                self._logGeneral("start-loading-events").debug1("starting loading events.")
                self._contentCleaners.loadEvents(self._loadEventsFromFiles())
                self._logGeneral("finished-loading-events").debug1("finished loading events. total time is: %.6f", time.time() - currentTime)
            else:
                return
            
            #### Remove content task ##################
            # Remove old content
            if self._keepRunning:
                self._logGeneral("start-removing-content").debug1("starting removing content.")
                numOfContentRemoved, numOfBadContentRemoved, numOfTotalContentRemoved, avgTotalContentRemovedPerDisk, peakTotalContentRemovedPerDisk = self._contentCleaners.removeContent()
                self.cleanIterationCounters['totalAvgRemovedPerDisk'] += avgTotalContentRemovedPerDisk
                self.cleanIterationCounters['numOfIterations'] += 1
                self.cleanIterationCounters['totalRemoved'] += numOfTotalContentRemoved
                if peakTotalContentRemovedPerDisk > self.cleanIterationCounters['peakRemovedPerIterationPerDisk']:
                    self.cleanIterationCounters['peakRemovedPerIterationPerDisk'] = peakTotalContentRemovedPerDisk
                if numOfTotalContentRemoved > self.cleanIterationCounters['peakRemovedPerIteration']:
                    self.cleanIterationCounters['peakRemovedPerIteration'] = numOfTotalContentRemoved
                self._logGeneral("finished-removing-content").debug1("finished removing content. total time is: %.6f", time.time() - currentTime)
                self.doPeriodicWork()
            else:
                return
            
    
            #### Save DB task ##################
            # Let's see if it's time to save db to file. (maybe it's the first time)
            currentTime = time.time()
            saveDb = False
            if self._lastTimeDumpedDict == None:
                self._lastTimeDumpedDict = currentTime
            elif currentTime - self._lastTimeDumpedDict >= self._intervalForDumpingDictToFileMinutes*60:
                self._lastTimeDumpedDict = currentTime
                saveDb = True
    
            # save db if necessary
            if saveDb and self._keepRunning:
                self._logGeneral("start-saving-db").debug1("starting saving db.")
                try:
                    self._contentCleaners.saveToDisk()
                except Exception as ex:
                    self._logGeneral("save-db-error").error("error saving cleaners state. exception: %s", ex)
                self._logGeneral("finished-saving-db").debug1("finished saving db. total time is: %.6f", time.time() - currentTime)

        except Exception as ex:
            self._logGeneral("clean-content-iteration-error").error("got exception trying to run a clean content iteration. exception: %s", ex)
            




    def _logCleanersState (self):
        self._contentCleaners.logCleanersState()


    def _removeOldDbTmpFiles (self):
        # Let's remove old tmp files if there are any
        for (currentRoot,dirNames,fileNames) in os.walk(self._contentCleanerCfg.dbFilesDir):
            # For each file (if there is any):
            for fileName in fnmatch.filter(fileNames, '*tmp*'):
                tmpFileFullNamePath = os.path.join(currentRoot, fileName)
                try:
                    os.remove(tmpFileFullNamePath)
                except Exception as ex:
                    self._logIo("error-remove-tmp").error("error removing tmp db file='%s'. exception=%s", tmpFileFullNamePath, ex)

 

    def _loadEventsFromFiles (self):
        
        # Holds the events
        # key: cid
        # value: {'lastAccessTime', 'metaFileFullPath', 'diskNum'}
        events = dict()

        # Walk in the directory tree
        for (currentRoot,dirNames,laeFileNames) in os.walk(self._lastAccessUpdatesDir):
           
            # sort the fileNames
            laeFileNames.sort()

            # Count total files scanned
            self.counters['numTotalEventFilesScanned'] += len(laeFileNames)
        
            # For each file (if there is any):
            for laeFileName in fnmatch.filter(laeFileNames, self._lastAccessEventsFilesPattern):
        
                eventFileFullNamePath = os.path.join(currentRoot,laeFileName)

                singleFileData = None
        
                # File should be in Json format. key = cid, 
                try:
                    singleFileData = a.infra.format.json.readFromFile(self._logIo, eventFileFullNamePath)
                except Exception as ex:
                    self._logIo("error-read-event-file").error("error reading event file='%s'. exception: %s", eventFileFullNamePath, ex)
                                                                 
                if singleFileData != None:
                    try:
                        events.update(singleFileData)
                    except Exception as ex:
                        self._logIo("error-update-events").error("error updating event file='%s'. exception: %s", eventFileFullNamePath, ex)
                
                self._handleEventsFile(eventFileFullNamePath)

        return events



    def _handleEventsFile (self, eventFileFullNamePath):
        self._logIo("remove-event-file").debug1("removing '%s'", eventFileFullNamePath)
        try:
            os.remove(eventFileFullNamePath)
        except Exception, e:
            self._logIo("failed-remove-file").error("Failed to remove '%s'. exception=%s", eventFileFullNamePath, str(e))


    def _getPathHead (self, pathName):
        head, tail = os.path.split(pathName)
        if tail == '':
            head, tail = os.path.split(head)
        return head

    def  _getAggregatedCounters(self):
        # Get the counters from the cleaners
        countersList, contentCountList, bytesUsedCountersList, numTitlesCountersList, diskUsageCountersList = self._contentCleaners.getCountersList()

        # Create the dict that is going to hold all the counters
        aggregatedCounters = dict()

        # All these counters are being aggregated
        for counters in countersList:
            for key in counters.keys():
                aggregatedCounters[key] = aggregatedCounters.get(key, 0) + counters.get(key, 0)

        for counters in bytesUsedCountersList:
            for key in counters.keys():
                aggregatedCounters[key] = aggregatedCounters.get(key, 0) + counters.get(key, 0)

        for counters in numTitlesCountersList:
            for key in counters.keys():
                aggregatedCounters[key] = aggregatedCounters.get(key, 0) + counters.get(key, 0)

        aggregatedCounters['contentCount'] = sum(contentCountList)

        # These counters are maxed
        isFirst = True
        for counters in diskUsageCountersList:
            if isFirst:
                isFirst = False
                for key in counters.keys():
                    aggregatedCounters[key] = int(counters.get(key, 0))
                continue

            for key in counters.keys():
                if int(counters.get(key, 0)) > aggregatedCounters.get(key, 0):
                    aggregatedCounters[key] = int(counters.get(key, 0))

        # We need to avarage the lifeTimeCounters
        if aggregatedCounters['numTotalContentRemoved'] == 0:
            aggregatedCounters['numTotalContentRemoved'] = 1
        aggregatedCounters['avgTitleLifeTimeSec'] = int(aggregatedCounters['numTotalTitleLifeTimeSec'] / aggregatedCounters['numTotalContentRemoved'])

        # Add counters aggregated by the app
        if self.cleanIterationCounters['numOfIterations'] == 0:
            self.cleanIterationCounters['numOfIterations'] = 1
        aggregatedCounters['avgRemovedPerIterationPerDisk'] = self.cleanIterationCounters['totalAvgRemovedPerDisk'] / self.cleanIterationCounters['numOfIterations']
        aggregatedCounters['avgRemovedPerIteration'] = self.cleanIterationCounters['totalRemoved'] / self.cleanIterationCounters['numOfIterations']
        aggregatedCounters['peakRemovedPerIterationPerDisk'] = self.cleanIterationCounters['peakRemovedPerIterationPerDisk']
        aggregatedCounters['peakRemovedPerIteration'] = self.cleanIterationCounters['peakRemovedPerIteration']
        

        return aggregatedCounters


    def _calculateAndUpdateTitleCountIfNeeded (self, force = False):

        currentTime = time.time()

        shouldUpdateTitleCount = False
        if (self._lastTimeUpdatedTitlesStoredFile == None) or (currentTime - self._lastTimeUpdatedTitlesStoredFile >= self._updatingTitleStoredFileIntervalSec):
            shouldUpdateTitleCount = True
            self._lastTimeUpdatedTitlesStoredFile = currentTime

        if (not force) and (not shouldUpdateTitleCount):
            return

        # First try to read how much new titles were added
        addedTitlesCount = 0
        fd = None
        try:
            fd = open(self._addedStoredTitlePath, "r")
        except Exception as ex:
            if self._addedStoredTitlePathWasFound:
                self._logIo("error-open-file").error("error trying to open the added title stored file. self._addedStoredTitlePath=%s. ex: %s", self._addedStoredTitlePath, ex)

        if fd is not None:
            self._addedStoredTitlePathWasFound = True
            try:
                # We limit the read to 1000 in size just in case
                addedTitlesCountStr = ""
                addedTitlesCountStr = fd.read(1000)
                addedTitlesCount = int(addedTitlesCountStr)
            except Exception as ex:
                self._logIo("error-convert-added").error("error reading and converting to string the added titles. addedTitlesCountStr=%s. ex: %s", addedTitlesCountStr, ex)
            finally:
                fd.close()

        

        # Calculate the current title stored number
        currentTitleCount = self._initialTitleCount + addedTitlesCount - self.cleanIterationCounters['totalRemoved']
        if currentTitleCount < 0 or self._contentCleanerCfg.isPrediction:
            currentTitleCount = 0

        # Write it to file
        tmpFile=self._storedTitlePath + "_"
        fd = None
        try:
            fd=open(tmpFile,"w")
        except Exception as ex:
            self._logIo("error-open-file").error("got exception trying to open %s for write. ex: %s", tmpFile, ex)

        if fd is not None:
            try:
                fd.write(str(currentTitleCount))
                # replace the old file atomicly
                shutil.move(tmpFile,self._storedTitlePath)
            except Exception as ex:
                self._logIo("error-writing-stored").error("got exception trying to write to titles-stored file.  ex: %s", ex)
            finally:
                fd.close()

        return currentTitleCount



    def _updateNumRemoved (self, numTitlesRemoved):
        self.cleanIterationCounters['totalRemoved'] += numTitlesRemoved


    def _updateCfg (self):
        # We update the configuration. This update may result moving to or out from prediction mode.
        # In that case we need to update the counters for the title stored
        numTitlesRemoved = self._contentCleaners.updateCleanersCfg(self._contentCleanerCfg)
        self._updateNumRemoved(numTitlesRemoved)
        
