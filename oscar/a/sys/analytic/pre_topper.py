
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: royr

import collections, glob, time, os, platform, statvfs, datetime
from operator import itemgetter 

import topper_record_utils
import a.infra.file.rotating_file 
import a.infra.file.utils
import a.infra.file.rotating_file_archiver
import a.infra.process
import a.infra.format.json
from a.stats.stats_comm_over_file_client import StatsCommOverFileClient
import cdn_reporter
import session_reporter

if  __package__ is None:
    G_NAME_MODULE_PRE_TOPPER = "unknown"
    G_NAME_GROUP_PRE_TOPPER_GENERAL = "unknown"
    G_NAME_GROUP_PRE_TOPPER_IO = "unknown"
else:
    from . import G_NAME_MODULE_PRE_TOPPER
    from . import G_NAME_GROUP_PRE_TOPPER_GENERAL
    from . import G_NAME_GROUP_PRE_TOPPER_IO

# Constants
RECORDS_COUNT_FOR_PERIODIC_CHECK = 1000
TIME_WAIT_FOR_PERIODIC_CHECK_SEC = 1
OUTPUT_FILE_PREFIX = "data"
MAX_LIST_SIZE = 500000
WARN_LIST_SIZE = 400000
MAX_DICT_SIZE = 500000
WARN_DICT_SIZE = 400000
FILES_TO_PROCESS_ON_BACK_LOG = 9

# Data structures health
DICT_OK = "dict_ok"
DICT_WARN = "dict_warn"
DICT_FULL = "dict_full"
LIST_OK = "list_ok"
LIST_WARN = "list_warn"
LIST_FULL = "list_full"

# Private keys
KEY_RECORD_TIME_STAMP = 'recordTimeStamp'
KEY_RECORD_ARRAY = 'recordArray'
KEY_FIRST_RECORD_TIME_STAMP = 'firstRecordTimeStamp' 
KEY_RECORD_TYPE = 'recordType'
KEY_FILE_NAME = 'fileName'
KEY_LINE_NUM = 'lineNum'
KEY_LINE = 'line'

CFG_UPDATE_FILE_NAME = "pre_topper.cfg"

# flaffen a nested dictionary
def flatten(d, parentKey=''):
    items = []
    for k, v in d.items():
        newKey = parentKey + '_' + k if parentKey else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, newKey).items())
        else:
            items.append((newKey, v))
    return dict(items)
    

class PreTopperCfg:
    """This struct holds the configuration data for the pretopper and should be filled and then passed when creating pretopper instance."""
    def __init__ (self):
        self.recordWritingIntervalSec = 2
        self.rotateFileIntervalSec = 30
        self.deltaTimeForAggregatingSec = 35
        self.deltaTimeStampForAggregatingSec = 35
        self.outputDirQuotaMB = 300
        self.percentOfQuotaToWarn = 90
        self.outPutFolder = None
        self.archiveFolder = None
        self.inputFileExtension = ".data"
        self.outputFileExtension = ".adata"
        self.inputScanRoot = ""
        self.fieldsSeperator = "\t"
        self.shouldAggregate = True
        self.systemStartTimeStamp = None
        self.maxInputDiskUsage = None
        self.rateReportingIntervalSec = 30
        self.ratePerSecTriggerForReporting = 200
        self.statsReportingIntervalSec = 60
        self.shouldCheckForBackLog = True
        self.enableSessionRecords = True

        self.sysCfgRunDir=""
        self.cfgUpdateCheckIntervalSec = 30

        # archiving configuration
        self.shouldArchive = False
        self.archiverOutputDir = None
        self.archiverOutDirSizeLimitGB = None
        self.archiverOutFileSizeLimitMB = None
        self.archiverOutFilePrefix = None
        self.archiverBufferDir = None
        self.archiverBufferDirSizeLimitMB = None
        self.archiverRotationTimeTresholdSeconds = None

        # CDN integration
        self.cdnIntegrationConfigFile = None
        self.cdnIntegrationConfigLoadingIntervalSec = None

        # Session bit-rate reporting
        self.sessionReportInterval = 5*60
        self.sessionSortDealy = 60
        self.sessionAgingTime = 2*60
        self.sessionTimeUntilAutoAdvance = 20
        self.sessionMinTransactionDurationMsec = 0
        self.sessionMinTransactionVolume = 0


    def __repr__ (self):
        configurationStr = "recordWritingIntervalSec=" + str(self.recordWritingIntervalSec) + \
                           ", rotateFileIntervalSec=" + str(self.rotateFileIntervalSec) + \
                           ", deltaTimeForAggregatingSec=" + str(self.deltaTimeForAggregatingSec) + \
                           ", deltaTimeStampForAggregatingSec=" + str(self.deltaTimeStampForAggregatingSec) +  \
                           ", outputDirQuotaMB=" + str(self.outputDirQuotaMB) + \
                           ", percentOfQuotaToWarn=" + str(self.percentOfQuotaToWarn) + \
                           ", shouldAggregate=" + str(self.shouldAggregate) + \
                           ", enableSessionRecords=" + str(self.enableSessionRecords) + \
                           ", maxInputDiskUsage=" + str(self.maxInputDiskUsage) + \
                           ", shouldCheckForBackLog=" + str(self.shouldCheckForBackLog) + \
                           ", shouldArchive=" + str(self.shouldArchive) + \
                           ", archiverOutDirSizeLimitGB=" + str(self.archiverOutDirSizeLimitGB) + \
                           ", archiverOutFileSizeLimitMB=" + str(self.archiverOutFileSizeLimitMB) + \
                           ", archiverBufferDirSizeLimitMB=" + str(self.archiverBufferDirSizeLimitMB) + \
                           ", archiverRotationTimeTresholdSeconds=" + str(self.archiverRotationTimeTresholdSeconds) + \
                           ", sessionReportInterval=" + str(self.sessionReportInterval) + \
                           ", sessionSortDealy=" + str(self.sessionSortDealy) + \
                           ", sessionAgingTime=" + str(self.sessionAgingTime) + \
                           ", sessionTimeUntilAutoAdvance=" + str(self.sessionTimeUntilAutoAdvance) + \
                           ", sessionMinTransactionDurationMsec=" + str(self.sessionMinTransactionDurationMsec) + \
                           ", sessionMinTransactionVolume=" + str(self.sessionMinTransactionVolume) + \
                           ", cfgUpdateCheckIntervalSec=" + str(self.cfgUpdateCheckIntervalSec)
                           
        return configurationStr


class PreTopperTime:
    """This struct holds time snapshot for calculating time elapsed for writing records and file rotation"""
     
    def init (self):
        current = time.time()
        self.lastRecordWritingTime = current
        self.lastRotatingFileTime = current


class PreTopper (object):
    """Pre topper module is in-charge of aggregating F records and write them to file. Any other record types will be left as is.
    Output records are guaranteed to be sorted by the record time-stamp field."""

    #---- Ctor -----------------------------------#
    def __init__ (self):

        self._logGeneral = None
        self._logIo = None

        # 'Turn on' the keepRunning flag
        self._keepRunning = True
         # Quota exceeded flag
        self._quotaExceeded = False
    
        #------ Data structures --------#
        # Holds aggregated records
        self._sortedAggregatedList = collections.deque()
        # The session Id dictionary
        self._sessionDict = dict()
        # Holds the records to write
        self._linesToWriteList = []
      
        #------ Configuration ----------#
        self._cfg = None
        self._lastCfgCheckTime = None

        #------ Other data members -----#
        # Time snapShot
        self._time = PreTopperTime()
        # This object validates the records
        self._rawDataValidator = None
        # The rotating file to write the aggregated records to
        self._rotatingFile = None
        # The archive directory
        self._archiveFolder = None
        # This is the index of the aggregation key
        self._aggregationKeyIndex = None
        # List of record indexes to aggregate 
        self._tokensIndexesToAggregate = None
        # List of record indexes to overwrite 
        self._tokensIndexesToOverwrite = None
        self._recordsHeaderFileNamePath = ""
        self._pathForDiskUsageCalculation = ""

        # Rate
        self._lastTimeReportedRateLimit = 0
        self._deltaNumOfRecords = 0

        # Stats
        self._lastTimeSentStats = None
        self._statsDir = None
        self._statsDir = None

        #Archiver
        self._archiver = None

        # S records
        self._sessionReporter = session_reporter.SessionReporter()

        #------ Counters ---------------#
        self.counters = {'loopCount':0,
                         'numFoldersScaned':0,
                         'numFilesProcessed':0,
                         'numLinesLoaded':0,
                         'numLinesFailedToLoadDueToException':0,
                         'numLinesFailedOnlyNewLine':0,
                         'numLinesFailedBelowMinimumFields':0,
                         'numLinesFailedNoRecordType':0,
                         'numLinesFailedNotValidated':0,
                         'numRecordsProcessed':0,
                         'numFRecProcessed':0,
                         'numFRecSentForAggregation':0,
                         'numFRecAddedToDict':0,
                         'numRecordsAddedToList':0,
                         'numRecordsWritenToDisk':0,
                         'numSessonRecordsWritenToDisk':0,
                         'numFRecRemovedFromDict':0,
                         'numFileRotated':0,
                         'numTimesTriedWritingToDisk':0,
                         'numRecordListSizeZero':0,
                         'numRecordsDiscardedReachedMaxSessionId':0, 
                         'currentSessionIdCount':0,
                         'numRecordsDiscardedReachedMaxRecords':0,
                         'currentRecordsCount':0,
                         'numRecordsAppendedForWriting':0,
                         'numRecordFilesDiscarded':0,
                         'numOfInpurRecordsDropedDueToQuotaWarn':0,
                         'numOfInpurRecordsDropedDueToQuota':0,
                         'numOfOutputRecordsDropedDueToQuota':0}

        #------ Status ---------------#
        self.status = {'sessionIdDictStatus': 'Ok',
                       'recordsListStatus': 'Ok'}

        #------ CDN integration ---------------#
        self._cdnIntegrations = {}
        self._lastTimeLoadCdnIntegrationConfig = None


    #---- Public -----------------------------------#

    def initLogger (self, logger):
        """Init the logger.

        Init the pre topper. 
        This function shall be called before any other functions of the class

        Args:
            logger: a logger from which new loggers shall be created

        Returns:
            None

        Raises:
            None
        """
        self._logGeneral=logger.createLogger(G_NAME_MODULE_PRE_TOPPER, G_NAME_GROUP_PRE_TOPPER_GENERAL)
        self._logIo = logger.createLogger(G_NAME_MODULE_PRE_TOPPER, G_NAME_GROUP_PRE_TOPPER_IO)

        self._sessionReporter.initLogger(self._logGeneral)

    def initCfg (self, cfg):
        # Init configuration
        self._cfg = cfg

        self._sessionReporter.initCfg(self._cfg)


    def initStatsDir(self, directory):
        self._statsDir = directory


    def initRecordsHeaderFileNamePath (self, recordHeaderFileNamePath):
        self._recordsHeaderFileNamePath = recordHeaderFileNamePath


    def shouldKeepRunning (self):
        return self._keepRunning
        

    def start (self):
        """Start the pre topper.

        Start the pre topper. 
        This function starts the main loop until keepRuning flag is turned off.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """

        if not self.init():
            return False
        
        # Start the archiver
        if self._cfg.shouldArchive and self._archiver.start != None:
            self._archiver.start(self.archiverThreadExceptionCallBack)

        # 'Money time' - Run the main loop 
        return self._mainLoop()



    def stop (self):
        """Stop the pre topper.

        Stop the pre topper. 
        This function stops the main loop by setting keepRuning flag to False.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self._keepRunning = False


                                   
    def processRecords (self):
        """Process the records.

        Process the records. 
        This function is public only for UT use.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """

        __pychecker__ = 'maxlines=300'

        if not self._keepRunning:
            return True

        reachedQuotaWarn = self._checkOutputDirQouta()

        # Get the records fileNames
        fileNames = self._getFileNames()
        
        # Load record entries from the files. Each entry is a dict={KEY_RECORD_TIME_STAMP:recordTimeStamp, KEY_RECORD_TYPE:recordType, KEY_RECORD_ARRAY:recordArray}'
        recordList = self._loadFiles(fileNames)

        # Now let's calculate the record rate (if we need)
        currentTime = time.time()
        try:
            self._deltaNumOfRecords += len(recordList)
            if (self._lastTimeReportedRateLimit == None):
                self._lastTimeReportedRateLimit = currentTime
            elif (currentTime - self._lastTimeReportedRateLimit >= self._cfg.rateReportingIntervalSec):
                rate = int(self._deltaNumOfRecords / (currentTime - self._lastTimeReportedRateLimit))
                self._lastTimeReportedRateLimit = currentTime
                self._deltaNumOfRecords = 0
                if (rate >= self._cfg.ratePerSecTriggerForReporting):
                    self._logGeneral("records-rate").debug1("records rate is %d/sec", rate)
        except Exception as ex:
            self._logGeneral("error-parsing-time-stamp-for-rate-limit").error("got exception %s while while calculating records rate", ex)      

        # If no records where found or quota exceeded, sleep and then do periodic work if needed. Then continue to the next loop.
        if (not (len(recordList) > 0)) or reachedQuotaWarn or self._quotaExceeded:
            if len(recordList) > 0:
                if reachedQuotaWarn:
                    self.counters['numOfInpurRecordsDropedDueToQuotaWarn'] += len(recordList)
                else:
                    self.counters['numOfInpurRecordsDropedDueToQuota'] += len(recordList)
            else:
                self.counters['numRecordListSizeZero'] += 1
            time.sleep(TIME_WAIT_FOR_PERIODIC_CHECK_SEC)
            if self._keepRunning:
                if not self._doPeriodicWorkIfNeeded():
                    self._logGeneral("failed-periodic-work").error("_doPeriodicWorkIfNeeded returned False")
                    return False
            return True

        # Sort the records entries 
        recordList.sort(key=itemgetter(KEY_RECORD_TIME_STAMP))

        dictState = DICT_OK
        listState = LIST_OK
        recordsLostDictFull = 0
        recordsLostListFull = 0
        recordsCount = 0

        # Start processing the records
        if self._keepRunning:
            # For each recordEntry
            for recordEntry in recordList:

                recordsCount += 1

                # Increment counters
                self.counters['numRecordsProcessed'] += 1

                # Get the type and the array of the record
                recordArray = recordEntry[KEY_RECORD_ARRAY]
                recordType = recordEntry[KEY_RECORD_TYPE]
                fileName = recordEntry[KEY_FILE_NAME]
                lineNum = recordEntry[KEY_LINE_NUM]
                recordTimeStamp = ""

                try:
                    recordTimeStamp = int(recordEntry[KEY_RECORD_TIME_STAMP])
                except Exception as ex:
                    self._logGeneral("error-parsing-time-stamp").error("got exception %s while parsing time stamp to int for record:%s, fileName=%s, line=%d", ex, recordArray, fileName, lineNum)
                    continue

                # CDN Integration
                if self._cdnIntegrations:
                    if recordType == 'F':
                        isDeliveryRecord = (recordArray[topper_record_utils.FlowRecordOffsets.theIsDeliveredIndicator.myVal] == '1')
                        isTransactionLastRecord = topper_record_utils.FlowRecordOffsets.isTransactionLastRecord(recordArray)
                        if isDeliveryRecord and isTransactionLastRecord:
                            for cdnReporter in self._cdnIntegrations.values():
                                cdnReporter.reportTransaction(recordArray)

                # The default is to append the record to the list
                appendToList = True
                appendToDict = False

                # If record is 'F' record - Aggregate if exists or just append it to the list if not exists in the dict
                if recordType == 'F' and (self._cfg.shouldAggregate or self._cfg.enableSessionRecords):
                    # Make record ready for aggregation 
                    if not self._makeAggregationIndexesInt(recordArray):
                        self._logGeneral("error-parsing-indexs").error("error parsing aggregation indexes to int for record:%s, fileName=%s, line=%d", recordArray, fileName, lineNum)
                        continue

                    # Counter
                    self.counters['numFRecProcessed'] += 1

                    if self._cfg.enableSessionRecords:
                        self._sessionReporter.processFRecord(recordArray, currentTime)

                    if self._cfg.shouldAggregate:
                        # We append F records to dict
                        appendToDict = True

                        # Get the session id
                        sessionId = recordArray[self._aggregationKeyIndex]    
                                     
                        # If session Id key already exists, aggregate the record data - don't append again to list and to dict
                        if sessionId in self._sessionDict:
                            # We check that the records time stamp didn't pass the deltaTimeForAggregatingSec. take this sessionId 
                            # out of the dict. It will get into the dict and list as a new record.
                            if (recordTimeStamp - self._sessionDict[sessionId][KEY_FIRST_RECORD_TIME_STAMP] > self._cfg.deltaTimeStampForAggregatingSec) \
                                or ((int(recordTimeStamp)/60) > (int(self._sessionDict[sessionId][KEY_FIRST_RECORD_TIME_STAMP])/60)):
                                self._sessionDict.pop(sessionId,0)
                            else:
                                self.counters['numFRecSentForAggregation'] += 1
                                if not self._aggregateRecords(self._sessionDict[sessionId][KEY_RECORD_ARRAY], recordArray):
                                    self._logGeneral("error-parsing-indexs").error("error aggregating record:%s, fileName=%s, line=%d", recordArray, fileName, lineNum)
                                    continue
                                appendToList = False
                                appendToDict = False
                else:
                    if self._cfg.enableSessionRecords and recordType == 'V':
                        # we use V records as keep alive packets for the sessions mechanism
                        self._sessionReporter.keepAlive(recordTimeStamp, currentTime)
    
                # If appendToDisk flag is up, his is a new entry - Append to list and also insert into the dict - Check dict size thresholds before
                if appendToDict:
                    if len(self._sessionDict) >= MAX_DICT_SIZE:
                        self._logGeneral("reached-dict-max-size").debug1("sessionId dict reached the max threshold. record will be discarded")
                        recordsLostDictFull += 1 
                        dictState = DICT_FULL
                        # Don't append to list
                        appendToList = False
                    else:
                        if len(self._sessionDict) >= WARN_DICT_SIZE:
                            dictState = DICT_WARN
                            self._logGeneral("reached-dict-warn-size").debug1("sessionId dict reached the warnning threshold")
                        
                        # We didn't pass the max - insert into the dict
                        self.counters['numFRecAddedToDict'] += 1
                        self._sessionDict[sessionId] = {KEY_FIRST_RECORD_TIME_STAMP:recordTimeStamp , KEY_RECORD_ARRAY:recordArray}
                        

                # Append to list if necessary
                if appendToList:
                    if len(self._sortedAggregatedList) >= MAX_LIST_SIZE:
                        self._logGeneral("reached-list-max-size").debug1("records list reached the max threshold. records will be discarded")
                        recordsLostListFull += 1
                        listState = LIST_FULL
                        # If it's F record and we are trying to insert to list then it might be also in the dict. Lets try to remove it
                        # Get the session id
                        sessionId = recordArray[self._aggregationKeyIndex]
                        if (recordType == 'F') and (sessionId in self._sessionDict):
                            self._sessionDict.pop(sessionId)
                    else:
                        if len(self._sessionDict) >= WARN_LIST_SIZE:
                            listState = LIST_WARN
                            self._logGeneral("reached-list-warn-size").debug1("records list reached the warnning threshold")

                        # We didn't pass the max - insert record to list
                        self.counters['numRecordsAddedToList'] += 1
                        self._sortedAggregatedList.append({KEY_RECORD_TIME_STAMP:recordTimeStamp, 'preTopperTimeStamp':time.time(), KEY_RECORD_TYPE:recordType, KEY_RECORD_ARRAY:recordArray})


                # After each X records, do periodic work if needed
                if (recordsCount % RECORDS_COUNT_FOR_PERIODIC_CHECK) == 0:
                    if self._keepRunning:
                        if not self._doPeriodicWorkIfNeeded():
                            self._logGeneral("failed-periodic-work2").error("_doPeriodicWorkIfNeeded returned False")
                            return False                                               

            if dictState != DICT_OK:
                if dictState == DICT_WARN:
                    self.status['sessionIdDictStatus'] = "Warn"
                    self._logGeneral("dict-in-warn-state").warning("sessionId dict is in warn state. dict size is %d" % len(self._sessionDict))
                else:
                    self.status['sessionIdDictStatus'] = "Full"
                    self.counters['numRecordsDiscardedReachedMaxSessionId'] += recordsLostDictFull
                    self._logGeneral("dict-in-full-state").error("sessionId dict is in full state. %d records were discarded" % recordsLostDictFull)
            else:
                self.status['sessionIdDictStatus'] = "Ok"


            if listState != LIST_OK:
                if listState == LIST_WARN:
                    self.status['recordsListStatus'] = "Warn"
                    self._logGeneral("list-in-warn-state").warning("records list is in warn state. list size is %d" % len(self._sortedAggregatedList))
                else:
                    self.status['recordsListStatus'] = "Full"
                    self.counters['numRecordsDiscardedReachedMaxRecords'] += recordsLostListFull
                    self._logGeneral("list-in-full-state").error("records list is in full state. %d records were discarded" % recordsLostListFull)
            else:
                self.status['recordsListStatus'] = "Ok"

            if len(recordList) < RECORDS_COUNT_FOR_PERIODIC_CHECK:
                if self._keepRunning:
                    if not self._doPeriodicWorkIfNeeded():
                        self._logGeneral("failed-periodic-work3").error("_doPeriodicWorkIfNeeded returned False")
                        return False

        return True


    #---- Public for UT ------------------------------------#
    def init (self):

        # Create the rotating file
        self._rotatingFile = a.infra.file.rotating_file.RotatingFile(self._logGeneral, self._cfg.outPutFolder, OUTPUT_FILE_PREFIX, a.infra.file.rotating_file.NO_ROTATE, 0, self._cfg.outputFileExtension)
        if not self._rotatingFile.open():
            self._logGeneral("open-rotating-file").error("Failed to open rotating file at path '%s' - Can't start pre topper", self._cfg.outPutFolder)
            return False

        # Get the run pattern
        self._runPattern=os.path.basename(self._cfg.inputScanRoot)

        # Init the record headers
        self.initRecordTypesFromHeader()

        # Init the time object
        self._time.init()

        # Create the path for calculating disk usage
        self._pathForDiskUsageCalculation = os.path.realpath(os.path.join(self._cfg.inputScanRoot, "video-analyzer", "00"))
        if not os.path.exists(self._pathForDiskUsageCalculation):
            return False

        # Init the stats object
        if self._statsDir!= None:
            self._stats = StatsCommOverFileClient("pre_topper", self._logGeneral)
            self._stats.init(self._statsDir)

        # Init the archiver
        if self._cfg.shouldArchive:
            ## WORKAROUND
            tmpDir = os.path.join(self._cfg.archiverBufferDir, "video-analyzer", "00")
            actualDir = os.path.realpath(tmpDir)
            head, tail = os.path.split(actualDir)
            archiveBufferDir, tail = os.path.split(head)
            ## END Of woraround
            self._logGeneral("archiver-dir-init-info").notice("input dir given to archiver is: %s" , archiveBufferDir)
            self._archiver = a.infra.file.rotating_file_archiver.Archiver(logger=self._logGeneral,\
                                                                          inputDir=archiveBufferDir, \
                                                                          bufferDirSizeLimitInMB=self._cfg.archiverBufferDirSizeLimitMB, \
                                                                          outputDir=self._cfg.archiverOutputDir,\
                                                                          archiveFilePrefix=self._cfg.archiverOutFilePrefix)

            self._archiver.setFileSizeThresholdMB(self._cfg.archiverOutFileSizeLimitMB)
            self._archiver.setOutputDirSizeLimitGB(self._cfg.archiverOutDirSizeLimitGB)
            self._archiver.setRotationTimeThersholdSeconds(self._cfg.archiverRotationTimeTresholdSeconds)

        return True


    def initTime (self):
        self._time.init()

    def currentDictSize (self):
        return len(self._sessionDict)

    def closeRotatingFile (self):
        return self._rotatingFile.close()

    def setAggregationKeyIndex (self, keyIndex):
        self._aggregationKeyIndex = keyIndex

    def initRecordTypesFromHeader (self):
        # Init the records types
        topper_record_utils.RawDataRecordValidator.initRecordTypes(self._recordsHeaderFileNamePath, self._logGeneral("init-record-types"))

        # Get the index of the aggregation key
        self._aggregationKeyIndex = topper_record_utils.FlowRecordOffsets.getAggregationKeyIndex()

        # Get the tokens indexes to aggregate
        self._tokensIndexesToAggregate = topper_record_utils.FlowRecordOffsets.getTokensIndexesToAggregate()

        # Get the tokens indexes to aggregate
        self._tokensIndexesToParseToInt = topper_record_utils.FlowRecordOffsets.getTokensIndexesToParseToInt()

        # Get the tokens indexes to overwrite
        self._tokensIndexesToOverwrite = topper_record_utils.FlowRecordOffsets.getTokensIndexesToOverwrite()

        self._tokenTransactionSegmentIndex = topper_record_utils.FlowRecordOffsets.getTransactionSegmentTokenIndex()

        self._tokensContentLengthIndex = topper_record_utils.FlowRecordOffsets.getContentLengthTokenIndex()

        # Init the record validator
        self._rawDataValidator = topper_record_utils.RawDataRecordValidator(self._logGeneral("raw-data-validator"))


    def archiverThreadExceptionCallBack (self, exception):
        self._logGeneral("archiver-exception").error("got exception '%s' from archiver thread. exiting.", exception)
        self.stop()


    #---- Private -----------------------------------#
    def _mainLoop (self):

        # Endless loop until 'keepRunning' flag is turned off
        while self._keepRunning:

            self.counters['loopCount'] += 1
            currentTime = time.time()

            # update config if needed
            if (self._lastCfgCheckTime == None) or (currentTime - self._lastCfgCheckTime >= self._cfg.cfgUpdateCheckIntervalSec):
                self._lastCfgCheckTime = currentTime
                self._doUpdateConfiguration()


            # Send stats if needed
            sendStats = False
            if (self._lastTimeSentStats == None) or (currentTime - self._lastTimeSentStats >= self._cfg.statsReportingIntervalSec):
                sendStats = True
                self._lastTimeSentStats = currentTime

            # Load CDN integration config if needed
            loadCdnIntegrationConfig = False
            if (self._lastTimeLoadCdnIntegrationConfig == None) or (currentTime - self._lastTimeLoadCdnIntegrationConfig >= self._cfg.cdnIntegrationConfigLoadingIntervalSec):
                loadCdnIntegrationConfig = True
            
            if loadCdnIntegrationConfig:
                self._logGeneral("main-loop-load-cdn-integration-config").debug3("loading-cdn-integration-config")
                self._loadCdnIntegrationConfig()

            if sendStats:
                self._logGeneral("main-loop-stats").debug3("sending stats counters")

                allCdnStats = { "cdnIntegration": {}}
                for cdnName, cdnReporter in self._cdnIntegrations.items():
                    allCdnStats["cdnIntegration"][cdnName] = cdnReporter.getCounters()

                # TODO(amiry) - append this to the stats dictionary
                self.counters.update(flatten(allCdnStats))

                mergedCounters = dict(self.counters.items() + self._sessionReporter.getCounters().__dict__.items())
                self._stats.send(mergedCounters)

            if not self.processRecords():
                self._logGeneral("failed-periodic-work3").error("processRecords returned False")
                return False

        if not self._rotatingFile.close():
            self._logIo("failed-closing-rotate-file").error("failed to close the rotating file")
            return False

        if self._archiver != None:
            self._archiver.stop()

        for cdnReporter in self._cdnIntegrations.values():
            cdnReporter.terminate()

        return True


    def _checkOutputDirQouta (self):
        reachedQuotaWarn = False
        dirQuota = self._cfg.outputDirQuotaMB*1024*1024
        # Check disk space -  if you are above the quota, raise the apropriate flag
        try:
            self._quotaExceeded,currentSize = a.infra.file.utils.isDirectorySizeAboveLimitSafe(self._cfg.outPutFolder,True,dirQuota)
        except Exception as ex:
            self._logGeneral("output-dir-error-calculating").error("isDirectorySizeAboveLimitSafe() raised exception %s for file: '%s'" , ex, self._cfg.outPutFolder)
        if self._quotaExceeded:
            self._logGeneral("output-dir-above-quota").error("_quotaExceeded is True. reached the limit of %dMB. no record write or file rotating will be done. going to discard new input records" , self._cfg.outputDirQuotaMB)
        else:
            if currentSize > (float(self._cfg.percentOfQuotaToWarn)/100)*dirQuota:
                reachedQuotaWarn = True
                self._logGeneral("output-dir-approaching-quota").warning("approaching quota of %dMB output. directory's size is %dMB. going to discard new input records" , self._cfg.outputDirQuotaMB, ((currentSize/1024)/1024))
        
        return reachedQuotaWarn



    def _getFileNames (self):
        filesInAllFolders = []

        # Go over all the VAs and Deliverys cores
        VApattern = os.path.join(self._cfg.inputScanRoot, "video-analyzer", "[0-9][0-9]", topper_record_utils.DATA_SUB_FOLDER_AND_HEADER_NAME)
        LDpattern = os.path.join(self._cfg.inputScanRoot, "delivery", "[0-9][0-9]", topper_record_utils.DATA_SUB_FOLDER_AND_HEADER_NAME)

        # Sort the folders 
        folders = sorted(glob.glob(VApattern) + glob.glob(LDpattern))
        
        # Get the filenames
        for folder in folders: # iterate all per-core folders
            self.counters['numFoldersScaned'] += 1
            pattern = os.path.join(folder , "*" + self._cfg.inputFileExtension)
            filesInFolder = glob.glob(pattern) # find all data files per that core
            filesInAllFolders.extend(filesInFolder)

        return filesInAllFolders
   

                 
    def _loadFiles (self, fileNames):
        fileNames.sort()
        recordList = []
        
        fileNamesToProcess = fileNames
        fileNamesLeftOvers = []
        # Let's check if pre-topper is lagging behind.
        # If so we will process only the last 9 files (8 from line and 1 from delivery) 
        if self._cfg.maxInputDiskUsage == None: 
            raise Exception("maxInputDiskUsage == None")
        if (self._cfg.shouldCheckForBackLog) and (self.getDiskUsage(self._pathForDiskUsageCalculation) > self._cfg.maxInputDiskUsage):
            fileNamesToProcess = fileNames[-FILES_TO_PROCESS_ON_BACK_LOG:]
            fileNamesLeftOvers = fileNames[:-FILES_TO_PROCESS_ON_BACK_LOG]
            self.counters['numRecordFilesDiscarded'] += len(fileNamesLeftOvers)
            self._logGeneral("high-disk-usage").warning("disk usage is higher then %d precent. total %d files found. old files will be discarded" ,self._cfg.maxInputDiskUsage, len(fileNames))
            self._logGeneral("file-to-process-and-discard").debug1("file to process:%s, files to discard:%s", fileNamesToProcess, fileNamesLeftOvers)

        for fileName in fileNamesToProcess:
            self.counters['numFilesProcessed'] += 1
            fileDescriptor = self._openFileForRead(fileName) 
            if fileDescriptor==None:
                continue

            localLine = 0
            try:
                for line in fileDescriptor:
                    if self._loadLine(line, recordList, fileName, localLine + 1):
                        localLine += 1
                        self.counters['numLinesLoaded'] += 1
            except Exception as ex:
                self._logGeneral("line-read-error").error("got exception %s reading line=%d, fileName=%s", ex, localLine, fileName)
                self.counters['numLinesFailedToLoadDueToException'] += 1
                raise

            fileDescriptor.close()
            self._handleProcessedFile(fileName)

        # Handle the left over files
        for fileName in fileNamesLeftOvers:
            self._handleProcessedFile(fileName)

        return recordList



    def _loadLine(self, line, recordList, fileName, lineNum):
        recordArray = line.split(self._cfg.fieldsSeperator)
        recordArrayLength = len(recordArray)

        if recordArrayLength==1 and recordArray[0]=="\n":
            self.counters['numLinesFailedOnlyNewLine'] += 1
            return False

        if  recordArrayLength < topper_record_utils.MIN_FIELDS_IN_RECORD:
            self.counters['numLinesFailedBelowMinimumFields'] += 1
            self._logGeneral("bad-input-line1").error("Bad input line - " + line)
            return False

        recordType = recordArray[0]
        if len(recordType) != 1:
            self.counters['numLinesFailedNoRecordType'] += 1
            self._logGeneral("bad-input-line2").error("Bad input line - " + line)
            return False

        if self._rawDataValidator.verifyData(recordArray):
            recordTimeStamp = recordArray[topper_record_utils.FlowRecordOffsets.theTimeOfDayOffset.myVal]
            recordList.append({KEY_RECORD_TIME_STAMP:recordTimeStamp, KEY_RECORD_TYPE:recordType, KEY_RECORD_ARRAY:recordArray, KEY_FILE_NAME:fileName, KEY_LINE_NUM:lineNum}) 
            return True

        self.counters['numLinesFailedNotValidated'] += 1
        return False
        


    def _doPeriodicWorkIfNeeded (self):
        # Get the current time
        currentTime = time.time()

        # Check if it's time to 'rotate' the file
        if not self._quotaExceeded:
            if (currentTime - self._time.lastRotatingFileTime) > self._cfg.rotateFileIntervalSec:     
                self._time.lastRotatingFileTime = currentTime
                if not self._rotatingFile.rotateNow():
                    self._logGeneral("error-rotate-now").error("rotateNow returned false")
                    return False
                else:
                    self.counters['numFileRotated'] += 1

      
        # Check if it's time to write records to file
        if (currentTime - self._time.lastRecordWritingTime) > self._cfg.recordWritingIntervalSec:
            self._time.lastRecordWritingTime = currentTime
            timeToRemoveBefore = currentTime - self._cfg.deltaTimeForAggregatingSec
            if not self._writeRecordsToFile(timeToRemoveBefore):
                self._logGeneral("error-writing-to-file").error("writeRecordsToFile() returned false")
                return False
            else:
                self.counters['numTimesTriedWritingToDisk'] += 1

        # do sessions periodic work
        self._sessionReporter.doPeriodicWork(currentTime)

        dictSize = len(self._sessionDict)
        ListSize = len(self._sortedAggregatedList)

        if  dictSize >= WARN_DICT_SIZE:
            if dictSize >= MAX_DICT_SIZE:
                self.status['sessionIdDictStatus'] = "Full"
            else:
                self.status['sessionIdDictStatus'] = "Warn"
        else:
            self.status['sessionIdDictStatus'] = "Ok"

        if  ListSize >= WARN_LIST_SIZE:
            if dictSize >= MAX_LIST_SIZE:
                self.status['recordsListStatus'] = "Full"
            else:
                self.status['recordsListStatus'] = "Warn"
        else:
            self.status['recordsListStatus'] = "Ok"

        self.counters['currentSessionIdCount'] = dictSize
        self.counters['currentRecordsCount'] = ListSize

        return True



    def _writeRecordsToFile (self, timeToRemoveBefore):

        loopCounter = 0
        listSize = len(self._sortedAggregatedList)
        
        # We are not really going over the indexes (we need to pop during the loop).
        while loopCounter < listSize:

            loopCounter += 1

            # Check that we should keep running
            if not self._keepRunning:
                break

            # Check if the record timestamp is older then timeToRemoveBefore
            if self._sortedAggregatedList[0]['preTopperTimeStamp'] < timeToRemoveBefore:
                self.counters['numRecordsAppendedForWriting'] += 1
                # Pop the entry (the first one)
                recordEntry = self._sortedAggregatedList.popleft()
                
                # Get the record array
                recordArray = recordEntry[KEY_RECORD_ARRAY]
                # Get the record time stamp
                recordTimeStamp = recordEntry[KEY_RECORD_TIME_STAMP]
                # If this is An F record, lets change the fields back to str
                if recordEntry[KEY_RECORD_TYPE] == 'F':
                    if not self._makeAggregationIndexesStr(recordArray):
                        self._logGeneral("error-parsing-indexs-str").error("error parsing aggregatin indexes bak to str for record:%s", recordArray)
                        continue
                # Create the line 
                lineToWrite = self._cfg.fieldsSeperator.join(recordArray)      
                # Append to lines to write list
                self._linesToWriteList.append({KEY_RECORD_TIME_STAMP:recordTimeStamp, KEY_LINE:lineToWrite})

                ## Write to file
                #self._rotatingFile.write(lineToWrite)

                # If this is F record, we must remove it from the sessionDict
                if recordEntry[KEY_RECORD_TYPE] == 'F':
                    sessionId = recordArray[self._aggregationKeyIndex]
                    if sessionId in self._sessionDict:
                        self.counters['numFRecRemovedFromDict'] += 1
                        self._sessionDict.pop(sessionId)
            else:
                # The invariant is that the records are time based sorted. 
                # If this record is not "old" enough then the rest won't be. Lets break out of here.
                break

        # If quota was not exceeded you may right
        if not self._quotaExceeded:
            # Sort the lines by record time stamp and write them to file
            # For efficency we sort in reverse order and pop from the end 
            self._linesToWriteList.sort(key=itemgetter(KEY_RECORD_TIME_STAMP), reverse = True)
            while len(self._linesToWriteList) > 0:
                self._rotatingFile.write(self._linesToWriteList.pop()[KEY_LINE])
                self.counters['numRecordsWritenToDisk'] += 1

            sRecordArray = self._sessionReporter.getOutputSRecords()
            while len(sRecordArray) > 0:
                self._rotatingFile.write(sRecordArray.popleft())
                self.counters['numRecordsWritenToDisk'] += 1
                self.counters['numSessonRecordsWritenToDisk'] += 1
        else:
            # Quota was exceeded - drop the records
            self.counters['numOfOutputRecordsDropedDueToQuota'] += len(self._linesToWriteList)
            self._linesToWriteList = []


        return True


    def _aggregateRecords (self, aggregatedRecord, newRecord):
        # Agregate fields
        for i in self._tokensIndexesToAggregate:
            aggregatedRecord[i] += newRecord[i] 

        # Overwrite fields
        for i in self._tokensIndexesToOverwrite:
            try:
                aggregatedRecord[i] = newRecord[i]
            except Exception as ex:
                self._logGeneral("error-accessing-field").error("got exception %s while trying to access field index %d in record:\n%s", ex, i, newRecord)
                return False

        # Handle the contentLength field
        try:
            if topper_record_utils.FlowRecordOffsets.isTransactionFirstRecord(newRecord):
                aggregatedRecord[self._tokensContentLengthIndex] += newRecord[self._tokensContentLengthIndex]
        except Exception as ex:
                self._logGeneral("error-accessing-field2").error("got exception %s while trying to access contentLength field index (%d) for record:\n%s", ex, self._tokensContentLengthIndex, newRecord)
                return False

        return True


    def _makeAggregationIndexesInt (self, record):
        for i in self._tokensIndexesToParseToInt:
            try:
                record[i] = int(record[i])
            except Exception as ex:
                self._logGeneral("error-parsing-to-int").error("got exception %s while trying to parse to int field index %d in record:%s", ex, i, record)
                return False
        return True



    def _makeAggregationIndexesStr (self, record):
        for i in self._tokensIndexesToParseToInt:
            try:
                record[i] = str(record[i])
            except Exception as ex:
                self._logGeneral("error-parsing-to-str").error("got exception %s while trying to parse to string field index %d in record:%s", ex, i, record)
                return False 
        return True
   

    def _handleProcessedFile (self, fileNamePath):
        shouldRemove = True
        shouldCheckIfExists = False
        # First rename for archiving
        # Get the process and the instance
        proccesFolder = os.path.dirname(os.path.dirname(fileNamePath))
        instanceName = os.path.basename(proccesFolder)
        processName = os.path.basename(os.path.dirname(proccesFolder))

        # Add them to the file name
        dirName = os.path.dirname(fileNamePath)
        fileName = os.path.basename(fileNamePath)
        preffix, suffix = os.path.splitext(fileName)
        preffix = preffix + "_" + processName + "_" + instanceName
        newFileNamePath = os.path.join(dirName, preffix + suffix)
        try:
            os.rename(fileNamePath, newFileNamePath)
        except Exception:
            newFileNamePath = fileNamePath
            
        if self._cfg.shouldArchive and self._archiver != None:
            self._logIo("archive-record-file").debug1("archiving file='%s'", newFileNamePath)
            shouldRemove = False
            try:
                if not self._archiver.archiveFile(newFileNamePath):
                    shouldCheckIfExists = True
            except Exception as ex:
                self._logGeneral("failed-archiving").error("Failed using archiver on: %s. exception:%s. trying to remove manually", newFileNamePath, ex)
                shouldCheckIfExists = True

        if shouldCheckIfExists:
            if os.path.exists(newFileNamePath):
                    shouldRemove = True

        # This in case the archiver had troubles. Lets check if it's exists and remove
        if shouldRemove:
            try:
                os.remove(newFileNamePath)
            except Exception as ex:
                self._logIo("failed-remove-file").error("got exception trying to remove '%s'. exception: %s ", newFileNamePath, ex)
            

    def _openFileForRead (self, filename, openMode="r"):
        try:
            fileDescriptor= open(filename,openMode)
            return fileDescriptor
        except Exception, e:
            self._logGeneral("open-file-for-read").error("Failed to open '%s' for read - %s ", filename, str(e))
            return None


    def getDiskUsage (self, workDir):
        """
        Get the disk usage for the fileSystem of the given workDirectory. Works only for linux.
        Returns -1 if not linux
        returns:
            -float: diskUsage in precentage 
        """

        if platform.system() == "Linux":
            # Get the statistics for the file system
            st = os.statvfs(workDir)
            # Calculate the current disk usage and compare to the diskUsageLimit argument
            DiskUsage = 100*(1-(float(st[statvfs.F_BAVAIL])/st[statvfs.F_BLOCKS]))
        else:
            raise Exception("Not running on linux platform")
    
        return DiskUsage


    def _loadCdnIntegrationConfig (self):

        newConfig = {}
        renameOk = False
        readOk = False

        self._logGeneral("load-cfg").debug3("Load CDN integration configuration file %s", self._cfg.cdnIntegrationConfigFile)

        if not os.path.exists(self._cfg.cdnIntegrationConfigFile):
            return

        self._lastTimeLoadCdnIntegrationConfig = time.time()

        try:
            tempFilename = self._cfg.cdnIntegrationConfigFile + ".tmp." + datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")
            os.rename(self._cfg.cdnIntegrationConfigFile, tempFilename)
            renameOk = True
            if renameOk:
                newConfig = a.infra.format.json.readFromFile(self._logGeneral, tempFilename)
                readOk = True
        except (IOError, ValueError) as ex:
            self._logGeneral("error-load-cfg").error("Error in load configuration file %s. %s", tempFilename, ex)

        if renameOk:
            try:
                os.remove(tempFilename)
            except Exception as ex:
                self._logGeneral("error-remove-cfg").warning("Error in remove configuration file %s. %s", tempFilename, ex)

        if not readOk:
            return

        self._logGeneral("update-cfg").notice("Update CDN configuration from file %s. %s", 
                                              self._cfg.cdnIntegrationConfigFile,
                                              newConfig)

        # Update existing integrations
        for cdnName, cdnReporter in self._cdnIntegrations.items():
            cdnConfig = newConfig.get(cdnName)
            if cdnConfig:
                cdnReporter.init(cdnConfig)
                if not cdnReporter.enabled():
                    # Already disabled
                    del(self._cdnIntegrations[cdnName])
            else:
                # CDN was deleted from configuration
                cdnReporter.disable()
                del(self._cdnIntegrations[cdnName])

        # And create new integrations
        for cdnName, cdnConfig in newConfig.items():
            integrationType = cdnConfig.get("type")
            if integrationType == "kLimelight":
                cdnReporter = cdn_reporter.LlnwdCdnReporter(cdnName)
            else:
                self._logGeneral("bad-name").warning("Unknown integration type %s in configuration. Ignore.", integrationType)
                continue

            cdnReporter.initLogger(self._logGeneral)
            cdnReporter.init(cdnConfig)
            if cdnReporter.enabled():
                self._cdnIntegrations[cdnName] = cdnReporter;

    def _doUpdateConfiguration(self):

        filename = os.path.join(self._cfg.sysCfgRunDir, CFG_UPDATE_FILE_NAME)
        if not os.path.exists(filename):
            return

        try:
            tempFilename = filename + ".tmp." + datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")
            os.rename(filename, tempFilename)
            newCfg = a.infra.format.json.readFromFile(self._logGeneral, tempFilename)
        except (IOError, ValueError) as ex:
            self._logGeneral("error-load-cfg").error("Error in load configuration file %s. %s", tempFilename, ex)
            return
        finally:
            try:
                os.remove(tempFilename)
            except Exception as ex:
                self._logGeneral("error-remove-cfg").error("Error in remove configuration file %s. %s", tempFilename, ex)

        self._logGeneral("update-cfg").notice("Updating configuration from file %s", filename)

        # update only specific config params
        if "enableSessionRecords" in newCfg:
            self._cfg.enableSessionRecords = newCfg["enableSessionRecords"]

        self._logGeneral("update-cfg-new-cfg").notice("Updated configuration %s", self._cfg)

