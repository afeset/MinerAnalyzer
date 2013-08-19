#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: royr
# 

import shutil, time, os, platform, statvfs, subprocess, threading , re
import traceback
import a.infra.format.json
import a.infra.file.rotating_file_archiver

from a.content import KEY_LAST_ACCESS_TIME
from a.content import KEY_META_FILE_FULL_NAME_PATH
from a.content import KEY_META_FILE_RELATIVE_PATH
from a.content import KEY_DISK_NUM
from a.content import KEY_CGID 

G_NAME_MODULE_CONTENT_CLEANER = "content-cleaner"
G_NAME_GROUP_CONTENT_CLEANER_GENERAL = "general"
G_NAME_GROUP_CONTENT_CLEANER_CGID = "cgid-cleaner"
G_NAME_GROUP_CONTENT_CLEANER_IO = "io"


# Constants
DO_PERIODIC_WORK_INTERVAL_RECOREDS = 1000
MAX_ERRORS_TO_HANDLE = 100

NO_META = 'no_meta_file_found'
ERROR_READ_META = 'error_reading_meta_file'
ERROR_REMOVE_META = 'error_removing_meta_file'
ERROR_REMOVE_META_PERSISTENT = 'error_removing_meta_persistent_file'
NO_MEDIA = 'no_media_file_found'
ERROR_REMOVE_MEDIA = 'error_removing_media_file'
REMOVED_OK='meta_and_media_removed_ok'

DB_FILE_NAME = 'content_cleaner'
COUNTERS_FILE_NAME = 'content_cleaner_counters'
DB_FAILED_FILE_NAME = 'failed_to_remove'
DB_FILES_EXTENSTION = 'state'

# private keys
KEY_ERROR = 'error'
KEY_META_PERSISTENT_FILE_FULL_NAME_PATH = 'metaPersistentFileFullNamePath'
KEY_LAST_MODIFICATION_TIME = 'lastModificationTime'
KEY_LAST_BYTES_ON_DISK = 'lastBytesOnDisk'
KEY_WAS_COUNTED = 'wasCounted'

# counters ketys
NUM_TOTAL_USED_BYTES = 'numTotalUsedBytes'
NUM_TITLES = 'numTitles'
PREDICTION_TOKEN = 'Prediction'
TOTAL       = ''
YOUTUBE     = '_youtube'
NETFLIX     = '_netflix'
XVIDEOS     = '_xvideos'        
YOUPORN     = '_youporn'        
APPLE       = '_apple'          
FC2         = '_fc2'            
HULU        = '_hulu'   
DAILYMOTION = '_dailymotion'    
BBC         = '_bbc' 
NICOVIDEO   = '_nicovideo' 
SKY         = '_sky'
APPLE_SOFT  = '_apple-software'   
HULU_JP     = '_hulu-jp'  
DMM         = '_dmm'
REDTUBE     = '_redtube'  
VK          = '_vk'
SVT         = '_svt'
PORNHUB     = '_pornhub'
PHNCDN      = '_phncdn'
# MSP28
FACEBOOK    = '_facebook'
APPLE_APPS  = '_apple-software-apps'
YOUKU       = '_youku'
NAVER       = '_naver'
VIMEO       = '_vimeo'
GOOGLE_PLAY = '_android-apps'
UOL         = '_uol'
# MSP29
DAUM        = '_daum'
GLOBO       = '_globo'
RTVE        = '_rtve'
EYNY        = '_eyny'
RUTUBE      = '_rutube'
VNEXPRESS   = '_vnexpress'



class ContentCleanerCfg (object):
    """This struct holds the configuration data for the content cleaner and should be filled and then passed when creating an instance."""
    def __init__ (self):
        # Meta base (persistent) dir
        self.metaPersistentBaseDir = None
        # Meta ram base dir
        self.metaRamBaseDir = None
        # Media base dir
        self.mediaBaseDir = None
        # When reaching this disk usage percent we signal oscar to stop acquiring cid to this disk
        self.diskUsagePercentStopAcq = 90
        # Content clean will remove content only if disk usage is above this number
        self.diskUsagePercentTrigger = 80
        # Content clean will remove content until it reaches this disk usage
        self.diskUsagePercentTarget = 75
        # Max number of files to remove in each cycle. if == -1, files will be removed until reached the disk usage target.
        self.maxNumOfContentToRemove = -1
        # Files that their time since last access is lower then this wont be removed
        self.lastAccessThresholdMinutes = 120
        # Files that their time since last access is lower then this will be removed and will raise a warning
        self.lastAccessThresholdWarnMinutes = 240
        # Directory path for saving and loading db state
        self.dbFilesDir = None
        # Meta files suffix
        self.metaFilesExtension = None
        # Bad files extension
        self.badFilesExtension = None
        # Acquisition Prediction mode only
        self.metaPredictionFilesExtension = None
        self.isPrediction = False
        # Acq files extension
        self.acqFilesExtension = 'acq'
        # Should we remove content that are under the threshold
        self.shouldRemoveContentUnderThreshold = None
        # Modification check treshold
        self.modificationCheckThresholdMinutes = None
        # Max title count. Will remove content if below this regardless of diskUsage
        self.maxTitleCount = None
        # Num of titles to remove between each disk usage check
        self.numContentToRemoveEachIteration = None


        # archiving configuration
        self.shouldArchive = False
        self.archiverOutputDir = None
        self.archiverOutDirSizeLimitGb = None
        self.archiverOutFileSizeLimitMb = None
        self.archiverBufferDir = None
        self.archiverBufferDirSizeLimitMb = None
        self.archiverRotationTimeTresholdSeconds = None


    def __repr__ (self):
        configurationStr = "diskUsagePercentTrigger=" + str(self.diskUsagePercentTrigger) + \
                           ", diskUsagePercentTarget=" + str(self.diskUsagePercentTarget) + \
                           ", shouldRemoveContentUnderThreshold=" + str(self.shouldRemoveContentUnderThreshold) + \
                           ", shouldArchive=" + str(self.shouldArchive) +  \
                           ", archiverOutDirSizeLimitGb=" + str(self.archiverOutDirSizeLimitGb) + \
                           ", archiveSingleFileMaxSizeMb=" + str(self.archiverOutFileSizeLimitMb) + \
                           ", archiverBufferDirSizeLimitMb=" + str(self.archiverBufferDirSizeLimitMb) +  \
                           ", archiverRotationTimeTresholdSeconds=" + str(self.archiverRotationTimeTresholdSeconds) + \
                           ", maxTitleCountPerDisk=" + str(self.maxTitleCount)

        return configurationStr
        
        




class ContentCleaner (object):
    """ContentCleaner is in-charge of cleaning old content from disk. It is ment to used on one disk or disksSet."""

    #---- Ctor -----------------------------------#
    def __init__ (self, instanceName = None):

        self._keepRunning = True

        self._logGeneral = None
        self._logIo = None

        self._instanceName = '00'
        if instanceName != None:
            self._instanceName = instanceName
    
        #------ Data structures -----------------------------#
        # This dict holds the updated last access times of all content on disk
        # Key : CID
        # Value: {KEY_LAST_ACCESS_TIME, KEY_META_FILE_FULL_NAME_PATH, KEY_DISK_NUM}
        self._cidLastAccessTimeDict = dict()

        # This dict holds the CIDs which we got error trying to remove
        # Key : CID
        # Value: {KEY_LAST_ACCESS_TIME, KEY_META_FILE_FULL_NAME_PATH, KEY_DISK_NUM, KEY_ERROR}
        #self._cidFailedToRemoveDict = dict()

        
        # This dict holds the CIDs which we got error trying to remove
        # Key : CID
        # Value: {KEY_LAST_ACCESS_TIME, KEY_META_FILE_FULL_NAME_PATH, KEY_DISK_NUM, KEY_ERROR}
        self._badContentList = []

        # per cgid deletion
        self._cidsToBeMarkedBad = dict()

        # This deque 

        #------ Configuration ----------#
        self._cfg = None
        self._metaFilesPattern = None
        self._metaPredictionFilesPattern = None
        # Holds list of content directories in case we are using diskSet (one for each disk)
        self._disksSet = []
        self._dbFileFullNamePath = None
        self._dbFailedToRemoveFileFullNamePath = None
        self._metaFilesPattern = None
        self._badFilesPattern = None
        self._isPrediction = False
        self._isFirstScan = True
        self._archiveCallBack = None
        self._periodicWorkCallBack = None
        
        

        #------ Counters ---------------#
        self.counters = {'numErrorNoMetaFiles':0,
                         'numErrorReadingMetaFiles':0,
                         'numErrorRemovingMetaFiles':0,
                         'numErrorNoMediaFiles':0,
                         'numErrorRemovingMediaFiles':0, 
                         'numNotRemovedBelowLastAccessThreshold':0,
                         'numGoodContentRemoved':0,
                         'numNotRemovedDueToError':0,
                         'numRemovedBelowLastAccessThresholdWarn':0,
                         'numTotalMetaFilesScanned':0,
                         'numTotalNewFilesAdded':0,
                         'numErrorNoMediaPathInMeta':0,
                         'numTotalLastAccessUpdates':0,
                         'numTotalLastAccessUpdatesForNewCID':0,
                         'numTotalBadContentFound':0,
                         'numErrorRemovingBadFiles':0,
                         'numBadContentRemoved':0,
                         'numErrorReadingBadFiles':0,
                         'numErrorRemovingMetaPersistentFiles':0,
                         'numTotalBadWithNoMetaFound':0,
                         'numTotalBadWithNoMetaRemoved':0,
                         'numJunkContentEntriesRemoved':0,
                         'numTotalPredictionRemovedBytes':0,
                         'numTotalContentRemoved':0,
                         'numTotalBytesRemoved':0,
                         'numTotalTitleLifeTimeSec':0,
                         'numMediaNoMetaRemoveErrors':0,
                         'numMediaNoMetaRemoved':0}

        # Content cleaner group max these values bteween all the content_cleaners
        self.diskUsageCounters = {'maxDiskUsagePercent':0}

        self._initCgidCounters()


        


    def _initCgidCounters (self):

        self.cgidToNameMap = {0:TOTAL,
                              2:YOUTUBE,
                              3:NETFLIX,
                              5:XVIDEOS,
                              7:YOUPORN,
                              10:APPLE,
                              61:FC2,
                              20:HULU,
                              14:DAILYMOTION,
                              11:BBC,
                              38:NICOVIDEO,
                              30:SKY,
                              52:APPLE_SOFT,
                              65:DMM,
                              86:HULU_JP,
                              6:PORNHUB,
                              71:PHNCDN,
                              62:REDTUBE,
                              44:VK,
                              87:SVT,
                              56:FACEBOOK,
                              110:APPLE_APPS,
                              88:YOUKU,
                              115:NAVER,
                              12:VIMEO,
                              114:GOOGLE_PLAY,
                              119:UOL,
                              124:DAUM,
                              120:GLOBO,
                              135:RTVE,
                              133:EYNY,
                              134:RUTUBE,
                              130:VNEXPRESS}
         


        self.bytesUsedCounters = {NUM_TOTAL_USED_BYTES + TOTAL:0,
                                  NUM_TOTAL_USED_BYTES + YOUTUBE:0,
                                  NUM_TOTAL_USED_BYTES + NETFLIX:0,       
                                  NUM_TOTAL_USED_BYTES + XVIDEOS:0,
                                  NUM_TOTAL_USED_BYTES + YOUPORN:0, 
                                  NUM_TOTAL_USED_BYTES + APPLE:0,          
                                  NUM_TOTAL_USED_BYTES + FC2:0,
                                  NUM_TOTAL_USED_BYTES + HULU:0,
                                  NUM_TOTAL_USED_BYTES + DAILYMOTION:0,
                                  NUM_TOTAL_USED_BYTES + BBC:0,
                                  NUM_TOTAL_USED_BYTES + NICOVIDEO:0,
                                  NUM_TOTAL_USED_BYTES + SKY:0,
                                  NUM_TOTAL_USED_BYTES + APPLE_SOFT:0,
                                  NUM_TOTAL_USED_BYTES + HULU_JP:0,
                                  NUM_TOTAL_USED_BYTES + DMM:0,
                                  NUM_TOTAL_USED_BYTES + REDTUBE:0,
                                  NUM_TOTAL_USED_BYTES + VK:0,
                                  NUM_TOTAL_USED_BYTES + SVT:0,
                                  NUM_TOTAL_USED_BYTES + PORNHUB:0,
                                  NUM_TOTAL_USED_BYTES + PHNCDN:0,
                                  NUM_TOTAL_USED_BYTES + FACEBOOK:0,
                                  NUM_TOTAL_USED_BYTES + APPLE_APPS:0,
                                  NUM_TOTAL_USED_BYTES + YOUKU:0,
                                  NUM_TOTAL_USED_BYTES + NAVER:0,
                                  NUM_TOTAL_USED_BYTES + VIMEO:0,
                                  NUM_TOTAL_USED_BYTES + GOOGLE_PLAY:0,
                                  NUM_TOTAL_USED_BYTES + UOL:0,
                                  NUM_TOTAL_USED_BYTES + DAUM:0,
                                  NUM_TOTAL_USED_BYTES + GLOBO:0,
                                  NUM_TOTAL_USED_BYTES + RTVE:0,
                                  NUM_TOTAL_USED_BYTES + EYNY:0,
                                  NUM_TOTAL_USED_BYTES + RUTUBE:0,
                                  NUM_TOTAL_USED_BYTES + VNEXPRESS:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + TOTAL:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + YOUTUBE:0,                  
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + NETFLIX:0,                  
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + XVIDEOS:0,                  
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + YOUPORN:0,                  
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + APPLE:0,                    
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + FC2:0,                      
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + HULU:0,                     
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + DAILYMOTION:0,              
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + BBC:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + NICOVIDEO:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + SKY:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + APPLE_SOFT:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + HULU_JP:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + DMM:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + REDTUBE:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + PORNHUB:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + PHNCDN:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + VK:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + SVT:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + FACEBOOK:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + APPLE_APPS:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + YOUKU:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + NAVER:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + VIMEO:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + GOOGLE_PLAY:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + UOL:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + DAUM:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + GLOBO:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + RTVE:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + EYNY:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + RUTUBE:0,
                                  NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + VNEXPRESS:0}
                        
        self.numTitlesCounters = {NUM_TITLES + TOTAL:0, 
                                  NUM_TITLES + YOUTUBE:0,
                                  NUM_TITLES + NETFLIX:0,       
                                  NUM_TITLES + XVIDEOS:0,
                                  NUM_TITLES + YOUPORN:0, 
                                  NUM_TITLES + APPLE:0,          
                                  NUM_TITLES + FC2:0,
                                  NUM_TITLES + HULU:0,
                                  NUM_TITLES + DAILYMOTION:0,
                                  NUM_TITLES + BBC:0,
                                  NUM_TITLES + NICOVIDEO:0,
                                  NUM_TITLES + SKY:0,
                                  NUM_TITLES + APPLE_SOFT:0,
                                  NUM_TITLES + HULU_JP:0,
                                  NUM_TITLES + DMM:0,
                                  NUM_TITLES + REDTUBE:0,
                                  NUM_TITLES + PORNHUB:0,
                                  NUM_TITLES + PHNCDN:0,
                                  NUM_TITLES + VK:0,
                                  NUM_TITLES + SVT:0,
                                  NUM_TITLES + FACEBOOK:0,
                                  NUM_TITLES + APPLE_APPS:0,
                                  NUM_TITLES + YOUKU:0,
                                  NUM_TITLES + NAVER:0,
                                  NUM_TITLES + VIMEO:0,
                                  NUM_TITLES + GOOGLE_PLAY:0,
                                  NUM_TITLES + UOL:0,
                                  NUM_TITLES + DAUM:0,
                                  NUM_TITLES + GLOBO:0,
                                  NUM_TITLES + RTVE:0,
                                  NUM_TITLES + EYNY:0,
                                  NUM_TITLES + RUTUBE:0,
                                  NUM_TITLES + VNEXPRESS:0,
                                  NUM_TITLES + PREDICTION_TOKEN + TOTAL:0,
                                  NUM_TITLES + PREDICTION_TOKEN + YOUTUBE:0,                  
                                  NUM_TITLES + PREDICTION_TOKEN + NETFLIX:0,                  
                                  NUM_TITLES + PREDICTION_TOKEN + XVIDEOS:0,                  
                                  NUM_TITLES + PREDICTION_TOKEN + YOUPORN:0,                  
                                  NUM_TITLES + PREDICTION_TOKEN + APPLE:0,                    
                                  NUM_TITLES + PREDICTION_TOKEN + FC2:0,                      
                                  NUM_TITLES + PREDICTION_TOKEN + HULU:0,                     
                                  NUM_TITLES + PREDICTION_TOKEN + DAILYMOTION:0,              
                                  NUM_TITLES + PREDICTION_TOKEN + BBC:0,
                                  NUM_TITLES + PREDICTION_TOKEN + NICOVIDEO:0,
                                  NUM_TITLES + PREDICTION_TOKEN + SKY:0,
                                  NUM_TITLES + PREDICTION_TOKEN + APPLE_SOFT:0,
                                  NUM_TITLES + PREDICTION_TOKEN + HULU_JP:0,
                                  NUM_TITLES + PREDICTION_TOKEN + DMM:0,
                                  NUM_TITLES + PREDICTION_TOKEN + REDTUBE:0,
                                  NUM_TITLES + PREDICTION_TOKEN + PORNHUB:0,
                                  NUM_TITLES + PREDICTION_TOKEN + PHNCDN:0,
                                  NUM_TITLES + PREDICTION_TOKEN + VK:0,
                                  NUM_TITLES + PREDICTION_TOKEN + SVT:0,
                                  NUM_TITLES + PREDICTION_TOKEN + FACEBOOK:0,
                                  NUM_TITLES + PREDICTION_TOKEN + APPLE_APPS:0,
                                  NUM_TITLES + PREDICTION_TOKEN + YOUKU:0,
                                  NUM_TITLES + PREDICTION_TOKEN + NAVER:0,
                                  NUM_TITLES + PREDICTION_TOKEN + VIMEO:0,
                                  NUM_TITLES + PREDICTION_TOKEN + GOOGLE_PLAY:0,
                                  NUM_TITLES + PREDICTION_TOKEN + UOL:0,
                                  NUM_TITLES + PREDICTION_TOKEN + DAUM:0,
                                  NUM_TITLES + PREDICTION_TOKEN + GLOBO:0,
                                  NUM_TITLES + PREDICTION_TOKEN + RTVE:0,
                                  NUM_TITLES + PREDICTION_TOKEN + EYNY:0,
                                  NUM_TITLES + PREDICTION_TOKEN + RUTUBE:0,
                                  NUM_TITLES + PREDICTION_TOKEN + VNEXPRESS:0}



    
    def initLogger (self, logger):
        """Init the logger.

        Init the logger. 
        This function shall be called before any other functions of the class

        Args:
            logger: a logger from which new loggers shall be created

        Returns:
            None

        Raises:
            None
        """
        self._logGeneral=logger.createLogger(G_NAME_MODULE_CONTENT_CLEANER, G_NAME_GROUP_CONTENT_CLEANER_GENERAL, self._instanceName)
        self._logIo=logger.createLogger(G_NAME_MODULE_CONTENT_CLEANER, G_NAME_GROUP_CONTENT_CLEANER_IO, self._instanceName)


    def initCfg (self, cfg):
        numTitlesRemoved = 0
        if self._cfg is not None:
            if self._isPrediction != cfg.isPrediction:
                # clear current content before changing modes
                numTitlesRemoved = self.clearAllContent()

                self._isPrediction = cfg.isPrediction
                self._logGeneral("prediction-mode").notice("prediction mode was changed to %s", self._isPrediction)

        # Init configuration
        self._cfg = cfg

        return numTitlesRemoved


    def initArchiveCallBack (self, callBack):
        self._archiveCallBack = callBack

    def initPeriodicWorkCallBack (self, callBack):
        self._periodicWorkCallBack = callBack


    def init (self, disksSet):
        """Init the content cleaner.

        Init the content cleaner. 
        This function shall be called before any other functions of the class

        Args:
            configuration: a configuration object specified in this object.
            disksSet: a list of disks to work on.

        Returns:
            None

        Raises:
            None
        """
        self._disksSet = disksSet
        self._metaFilesPattern = '*.' + self._cfg.metaFilesExtension
        self._metaPredictionFilesPattern = self._metaFilesPattern + '.' + self._cfg.metaPredictionFilesExtension
        self._badFilesPattern = self._metaFilesPattern + '.' + self._cfg.badFilesExtension
        self._dbFileFullNamePath = os.path.join(self._cfg.dbFilesDir, DB_FILE_NAME + '_' + self._instanceName + "." + DB_FILES_EXTENSTION)
        self._dbFailedToRemoveFileFullNamePath = os.path.join(self._cfg.dbFilesDir, DB_FAILED_FILE_NAME + '_' + self._instanceName + "." + DB_FILES_EXTENSTION)
        self._countersFileFullNamePath = os.path.join(self._cfg.dbFilesDir, COUNTERS_FILE_NAME + '_' + self._instanceName + "." + DB_FILES_EXTENSTION)
        self._isPrediction = self._cfg.isPrediction


        # Sanity check
        errorSites = []
        raiseException = False
        for value in self.cgidToNameMap.values():
            if ((NUM_TOTAL_USED_BYTES + value) not in self.bytesUsedCounters) \
               or ((NUM_TOTAL_USED_BYTES + PREDICTION_TOKEN + value) not in self.bytesUsedCounters) \
               or ((NUM_TITLES + value) not in self.numTitlesCounters) \
               or ((NUM_TITLES + PREDICTION_TOKEN +value) not in self.numTitlesCounters):
                raiseException = True
                errorSites.append(value)

        if raiseException:
            raise Exception("initError","error init counters for sites %s", errorSites)
                



    def stop (self):
        self._logGeneral("stop-content-cleaner").notice("Content Cleaner stop has been called")
        self._keepRunning = False




    def scanForNewContent (self):
        """Scan the content's meta directory.

        Scan the content's meta directory.
        This function scans the meta directory for new content.

        Args:
            None

        Returns:
            int: Number of new content files found

        Raises:
            None
        """

        self._logGeneral('scan-new-content-starting').debug2('starting to scan for new content')
        
        totalMetaFilesScanned = 0
        totalNewFilesAdded = 0

        metaFilesPattern = None
        if self._isPrediction is False:
            metaFilesPattern = self._metaFilesPattern
        else:
            metaFilesPattern = self._metaPredictionFilesPattern

        mminParam = self._cfg.modificationCheckThresholdMinutes
        if mminParam != None and mminParam == 0:
            mminParam = 1

        findCommand = "find -L . -type f -name '%(filePattern)s'" % {'filePattern':metaFilesPattern}
        if not self._isFirstScan and (mminParam != None):
            findCommand = "find -L . -mmin -%(minutes)s -type f -name '%(filePattern)s'" % {'minutes':str(mminParam), 'filePattern':metaFilesPattern}
        findCommand += " | xargs --no-run-if-empty stat -c '%n %Y'"

        self._logGeneral('new-content-find-command').debug2('going to search for new files. command: %s', findCommand)

        # We have set of meta file directories. go over each directory.
        for disk in self._disksSet:
            self._logGeneral('scan-new-files-starting-in-disk').debug3('starting to scan for new content in disk %02u', disk)

            metaRamRootDir = os.path.join(self._cfg.metaRamBaseDir, "%02u" % disk)
            metaPersistentRootDir = os.path.join(self._cfg.metaPersistentBaseDir, "%02u" % disk)
            data = None
            try:
                process = subprocess.Popen(findCommand, shell=True, stdout=subprocess.PIPE, cwd=metaRamRootDir, bufsize=65536)
                data = process.communicate()[0]
            except Exception as ex:
                self._logGeneral("cant-run-find").error("error trying to run 'find' command. exception: %s", ex)
                continue
                
            if data == None:
                self._logGeneral("no-output-data").error("data from 'find' command is None.")
                continue

            for line in data.split('\n'):
                if len(line)==0:
                    break              

                # Split the output line to the relative path and the modification time
                # Relative path is: aa/bb/aabbsdaa12231.meta / aa/bb/aabbsdaa12231.meta.prd
                splittedLine = line.split(" ")
                metaFileRelativePath = splittedLine[0]
                modificationTime = int(splittedLine[1])

                # Get the full meta path
                metaFileFullNamePath = os.path.join(metaRamRootDir, metaFileRelativePath)

                # Get only the meta file name: aabbsdaa12231.meta / aabbsdaa12231.meta.prd
                metaFileName = os.path.split(metaFileRelativePath)[1]
                # Get the cid
                cid = metaFileName.split('.')[0]

                # Get the meta persistent full name path
                metaPersistentFileFullNamePath = os.path.join(metaPersistentRootDir, metaFileRelativePath)
                
                # We check if self._keepRunning is up before we scan the next folder
                if not self._keepRunning:
                    return totalMetaFilesScanned, totalNewFilesAdded

                # Count total files scanned
                self.counters['numTotalMetaFilesScanned'] += 1
                totalMetaFilesScanned += 1

                if (totalMetaFilesScanned % DO_PERIODIC_WORK_INTERVAL_RECOREDS) == 0:
                    self._periodicWorkCallBack()

                updateLastAccess = False
                updateLastModificationTime = False
                isCounted = True
                isExist = False

                # If in dict, check if updates are needed
                if cid in self._cidLastAccessTimeDict:
                    isExist = True
                    # We check if we need to update modification time and bytes acquired.
                    if KEY_LAST_MODIFICATION_TIME in self._cidLastAccessTimeDict[cid]:
                        cidLastModificationTime = self._cidLastAccessTimeDict[cid][KEY_LAST_MODIFICATION_TIME]
                        if modificationTime > cidLastModificationTime:
                            updateLastModificationTime = True
                    else:
                        updateLastModificationTime = True

                    if KEY_WAS_COUNTED not in self._cidLastAccessTimeDict[cid]:
                        isCounted = False
                        self._cidLastAccessTimeDict[cid][KEY_WAS_COUNTED] = 1

                    cidCurrentLastAccessTime = self._cidLastAccessTimeDict[cid][KEY_LAST_ACCESS_TIME]
                    if  cidCurrentLastAccessTime < modificationTime:
                        self._logGeneral('in-dict-update').debug2('cid=%s already exists in dict. updating its lastAccessTime from %d to %d', cid, cidCurrentLastAccessTime, modificationTime)
                        updateLastModificationTime = True
                    else:
                        self._logGeneral('in-dict-no-update').debug2('cid=%s already exists in dict. no need to update lastAccessTime', cid)


                # If not exists or we need to update the modification time - we need to look for the bytes acquired inside the meta.
                bytesDiskSize = 0
                cgid = -1
                
                if (not isExist) or updateLastModificationTime or not isCounted or self._isFirstScan:
                    (cgid, bytesDiskSize) = self._getCgidAndBytesUsed(cid, metaFileFullNamePath)               

                # Update or insert to data base
                updateBytes = False
                bytesToAdd = 0;
                updateNumTitle = False
                if isExist:
                    if not isCounted:
                        updateNumTitle = True
                        self._cidLastAccessTimeDict[cid][KEY_CGID]=cgid
                    if updateLastModificationTime:
                        updateBytes = True
                        if KEY_LAST_BYTES_ON_DISK in self._cidLastAccessTimeDict[cid]:
                            bytesToAdd = bytesDiskSize - self._cidLastAccessTimeDict[cid][KEY_LAST_BYTES_ON_DISK]
                        else:
                            bytesToAdd = bytesDiskSize
                        self._cidLastAccessTimeDict[cid][KEY_LAST_BYTES_ON_DISK] = bytesDiskSize
                        self._cidLastAccessTimeDict[cid][KEY_LAST_MODIFICATION_TIME] = modificationTime

                    if updateLastAccess:
                        self._cidLastAccessTimeDict[cid][KEY_LAST_ACCESS_TIME] = modificationTime
                else:
                    bytesToAdd = bytesDiskSize
                    updateBytes = True
                    updateNumTitle = True
                    self._cidLastAccessTimeDict[cid] = {KEY_LAST_ACCESS_TIME:modificationTime, KEY_META_FILE_FULL_NAME_PATH:metaFileFullNamePath,\
                                                        KEY_META_PERSISTENT_FILE_FULL_NAME_PATH:metaPersistentFileFullNamePath, KEY_DISK_NUM:disk, \
                                                        KEY_LAST_MODIFICATION_TIME:modificationTime, KEY_LAST_BYTES_ON_DISK: bytesDiskSize, KEY_WAS_COUNTED:1, \
                                                        KEY_CGID:cgid}
                    self._logGeneral('new-content').debug2('new content has been found. cid=%s, metaFileFullNamePath="%s"', cid, metaFileFullNamePath)
                    self.counters['numTotalNewFilesAdded'] += 1
                    totalNewFilesAdded += 1
                    
                if self._isFirstScan:
                    updateBytes = True
                    bytesToAdd = bytesDiskSize;
                    updateNumTitle = True

                # Update counters
                self._incrCounters(updateBytes, updateNumTitle, cgid, bytesToAdd)

        
        if self._isFirstScan:
            if len(self._cidLastAccessTimeDict) > totalMetaFilesScanned:
                self._logGeneral('meta-count-too-large').notice('number meta on disk is less then on dict. going to remove junk entries. totalMetaFilesScanned=%d, len(Dict)=%d', totalMetaFilesScanned, len(self._cidLastAccessTimeDict))
                self._scanLastAccessDictForJunk()
            self._isFirstScan = False

        return totalMetaFilesScanned, totalNewFilesAdded 




    def scanForBadContent (self):

        self._logGeneral('scan-bad-files-starting').debug2('starting to scan for bad content')

        totalBadFilesScanned = 0

        # We have set of meta file directories. go over each directory.
        for disk in self._disksSet:
            self._logGeneral('scan-bad-files-starting-in-disk').debug3('starting to scan for bad content in disk %02u', disk)

            metaRamRootDir = os.path.join(self._cfg.metaRamBaseDir, "%02u" % disk)
            metaPersistentRootDir = os.path.join(self._cfg.metaPersistentBaseDir, "%02u" % disk)
          
            findCommand = "find -L . -type f -name '%(filePattern)s'" % {'filePattern':self._badFilesPattern}
            self._logGeneral('find-command').debug2('going to search for bad files. command: %s', findCommand)
            data = None
            try:
                process = subprocess.Popen(findCommand, shell=True, stdout=subprocess.PIPE, cwd=metaRamRootDir, bufsize=65536)
                data = process.communicate()[0]
            except Exception as ex:
                self._logGeneral("cant-run-find").error("error trying to run 'find' command. exception: %s", ex)
                continue
                
            if data == None:
                self._logGeneral("no-output-data").error("data from 'find' command is None.")
                continue
          
            for line in data.split('\n'):
                if len(line)==0:
                    self._logGeneral('end-of-data').debug4('len(line)==0. probebly got to the end of the data')
                    break

                if not self._keepRunning:
                    return totalBadFilesScanned

                # Split the output line to the relative path and the modification time
                # Relative path is: aa/bb/aabbsdaa12231.meta / aa/bb/aabbsdaa12231.meta.prd
                badFileRelativePath = line
                metaFileRelativePath = os.path.splitext(badFileRelativePath)[0]
                
                # Get the full meta path
                metaFileFullNamePath = os.path.join(metaRamRootDir, metaFileRelativePath)
                # Get the bad file full name path
                badFileFullNamePath = os.path.join(metaRamRootDir, badFileRelativePath)
                
                if not os.path.exists(metaFileFullNamePath):
                    # No meta. insert to bad list with cid 0
                    self._badContentList.append((badFileFullNamePath, 0))

                    # Update counters
                    self.counters['numTotalBadWithNoMetaFound'] += 1
                    totalBadFilesScanned += 1
                    self._logGeneral('scan-bad-files-bad-no-meta').debug4('found bad file without meta. badFileFullNamePath=%s, metaFileFullNamePath=%s', \
                                                                          badFileFullNamePath, metaFileFullNamePath)
                else:
                    # Get the full persistent meta path
                    metaPersistentFileFullNamePath = os.path.join(metaPersistentRootDir, metaFileRelativePath)
                    # Get only the meta file name: aabbsdaa12231.meta / aabbsdaa12231.meta.prd
                    metaFileName = os.path.split(metaFileRelativePath)[1]
                    # Get the cid
                    cid = metaFileName.split('.')[0]

                    # Append it to the list
                    self._badContentList.append((badFileFullNamePath, cid, {KEY_META_FILE_FULL_NAME_PATH:metaFileFullNamePath, KEY_META_PERSISTENT_FILE_FULL_NAME_PATH:metaPersistentFileFullNamePath, KEY_DISK_NUM:disk}))

                    # Update counters
                    self.counters['numTotalBadContentFound'] += 1
                    totalBadFilesScanned += 1
                    self._logGeneral('scan-bad-files-bad-no-meta').debug4('found bad file. badFileFullNamePath=%s, cid=%s, metaFileFullNamePath=%s, metaPersistentFileFullNamePath', \
                                                                          badFileFullNamePath, cid, metaFileFullNamePath, metaPersistentFileFullNamePath)
          
        return totalBadFilesScanned


    def _getCgidAndBytesUsed (self, cid, metaFileFullNamePath):
        bytesDiskSize = 0
        cgid = -1
        metaData = None
        try:
            metaData = a.infra.format.json.readFromFile(self._logIo, metaFileFullNamePath)
        except Exception as ex:
            self._logGeneral("error-reading-bad-file").error("can't get meta data from file='%s'. cid=%s. exception=%s", metaFileFullNamePath, cid, ex)
        if metaData != None:
            if ('bytesDiskSize' in metaData) and ('siteId' in metaData):
                bytesDiskSize = metaData['bytesDiskSize']
                cgid = metaData['siteId']
            else:
                self._logGeneral("no-mandatory-keys").debug3("no mandatory keys 'bytesDiskSize' & 'siteId' in file='%s'. cid=%s", metaFileFullNamePath, cid)
        else:
            self._logGeneral("cant-load-meta").warning("can't load meta data for updating counters for file='%s'. cid=%s", metaFileFullNamePath, cid)

        return (cgid, bytesDiskSize)



    def _incrCounters(self, shouldUpdateBytes, shouldUpdateNumTitle, cgid, bytesToAdd):
        isKnownCgid = cgid in self.cgidToNameMap
        if shouldUpdateBytes or shouldUpdateNumTitle:
            baseCounterKey = ''
            if self._isPrediction:
                baseCounterKey = PREDICTION_TOKEN
            if shouldUpdateBytes:
                self.bytesUsedCounters[NUM_TOTAL_USED_BYTES + baseCounterKey + self.cgidToNameMap[0]] += bytesToAdd
                if isKnownCgid:
                    self.bytesUsedCounters[NUM_TOTAL_USED_BYTES + baseCounterKey + self.cgidToNameMap[cgid]] += bytesToAdd
            if shouldUpdateNumTitle:
                self.numTitlesCounters[NUM_TITLES + baseCounterKey + self.cgidToNameMap[0]] += 1
                if isKnownCgid:
                    self.numTitlesCounters[NUM_TITLES + baseCounterKey + self.cgidToNameMap[cgid]] += 1


    def _scanLastAccessDictForJunk(self):
        contentList = self._cidLastAccessTimeDict.items()    
        for cid,data in contentList:
            if not self._keepRunning:
                return
            removeEntry = True
            try:
                if not os.path.exists(data[KEY_META_FILE_FULL_NAME_PATH]):
                    self._logGeneral('junk-meta').debug1('meta in dict not exists. removig from dict. cid=%s, metaFileFullNamePath="%s", diskNum=%d', cid, data[KEY_META_FILE_FULL_NAME_PATH], data[KEY_DISK_NUM])
                elif len(cid) <= 12:
                    self._logGeneral('junk-meta2').debug1('old cid format. removig from dict. cid=%s, metaFileFullNamePath="%s", diskNum=%d', cid, data[KEY_META_FILE_FULL_NAME_PATH], data[KEY_DISK_NUM])
                elif data[KEY_DISK_NUM] not in self._disksSet:
                    self._logGeneral('junk-meta3').debug1('disk num is wrong. removig from dict. cid=%s, metaFileFullNamePath="%s", diskNum=%d', cid, data[KEY_META_FILE_FULL_NAME_PATH], data[KEY_DISK_NUM])
                elif int(data[KEY_META_FILE_FULL_NAME_PATH].split(os.sep)[-4]) not in self._disksSet:
                    self._logGeneral('junk-meta4').debug1('meta is not on this disk. removig from dict. cid=%s, metaFileFullNamePath="%s", diskNum=%d', cid, data[KEY_META_FILE_FULL_NAME_PATH], data[KEY_DISK_NUM])
                elif KEY_META_PERSISTENT_FILE_FULL_NAME_PATH not in data:
                    # This is for backward comptability
                    metaRamFileFullNamePath = data[KEY_META_FILE_FULL_NAME_PATH]
                    metaRamFileFullNamePathSplitted = metaRamFileFullNamePath.split(os.sep)
                    metaRelativePath =os.path.join(metaRamFileFullNamePathSplitted[-4], metaRamFileFullNamePathSplitted[-3], \
                                                                  metaRamFileFullNamePathSplitted[-2], metaRamFileFullNamePathSplitted[-1])

                    metaPersistentFileFullNamePath = os.path.join(self._cfg.metaPersistentBaseDir, metaRelativePath)
                    metaRamFileFullNamePath = os.path.join(self._cfg.metaRamBaseDir, metaRelativePath)

                    self._cidLastAccessTimeDict[cid] = {KEY_LAST_ACCESS_TIME:data[KEY_LAST_ACCESS_TIME],\
                                                        KEY_META_FILE_FULL_NAME_PATH:metaRamFileFullNamePath,\
                                                        KEY_META_PERSISTENT_FILE_FULL_NAME_PATH:metaPersistentFileFullNamePath,\
                                                        KEY_DISK_NUM:data[KEY_DISK_NUM]}

                    self._logGeneral('junk-meta5').debug1('record missing meta persistent path. generating path. cid=%s, metaFileFullNamePath="%s", diskNum=%d, generatedPersistentMetaPath=%s',\
                                                           cid, metaRamFileFullNamePath, data[KEY_DISK_NUM], metaPersistentFileFullNamePath)
                    removeEntry = False
                else:
                    removeEntry = False
            except ValueError:
                self._logGeneral('junk-meta5').debug1('wrong meta dir structure on disk. removig from dict. cid=%s, metaFileFullNamePath="%s", diskNum=%d', cid, data[KEY_META_FILE_FULL_NAME_PATH], data[KEY_DISK_NUM])


            if removeEntry:
                self.counters['numJunkContentEntriesRemoved'] += 1
                self._cidLastAccessTimeDict.pop(cid,0)





    def _removeBadContent (self, shouldIgnoreAcq = False):

        numOfBadContentRemoved = 0

        for badContentEntry in self._badContentList:
            # First remove the content and then the bad file.
 
            badMetaFileFullNamePath = badContentEntry[0]
            cid = badContentEntry[1]
            data = None
            if cid != 0:
                data = badContentEntry[2]
            

            if (cid != 0) and (not shouldIgnoreAcq):
                if self._isInAcquisition(data[KEY_META_FILE_FULL_NAME_PATH]):
                    self._logGeneral("bad-content-in-acq-not-removed").debug3("bad content candidate for removel is in acquisition and won't be removed. cid=%s, metaFileFullNamePath=%s", cid, data[KEY_META_FILE_FULL_NAME_PATH])
                    continue

            # Load the bad file content
            badFileData = None
            try:
                badFileData = a.infra.format.json.readFromFile(self._logIo, badMetaFileFullNamePath)
            except Exception as ex:
                self.counters['numErrorReadingBadFiles'] += 1
                self._logGeneral("error-reading-bad-file").debug3("can't get bad data from file='%s'. cid=%s. exception=%s", badMetaFileFullNamePath, cid, ex)

            mediaFileFullNamePath = None
            if badFileData != None:
                self._logGeneral("bad-file-content").notice("cid=%s. bad file content for file=%s:\n%s", cid, badMetaFileFullNamePath, badFileData)
                if ('brownie' in badFileData) and ('contentFile' in badFileData['brownie']):
                    mediaFileFullNamePath = os.path.join(self._cfg.mediaBaseDir ,badFileData['brownie']['contentFile'])
            else:
                self._logGeneral("bad-file-no-content").notice("cid=%s. could not get bad file content for file=%s", cid, badMetaFileFullNamePath)

            if cid == 0:
                try:
                    os.remove(badMetaFileFullNamePath) 
                    self._logGeneral("bad-file-content-no-meta").notice("cid=%s. bad file with no meta. removing bad file=%s", cid, badMetaFileFullNamePath)
                    self.counters['numTotalBadWithNoMetaRemoved'] += 1
                except Exception as ex:
                    self.counters['numErrorRemovingBadFiles'] += 1
                    self._logGeneral("error-remove-bad-with-no-meta").error("bad file with no meta. error removing bad file='%s'. cid=%s. exception=%s", badMetaFileFullNamePath,cid, ex)
                self._tryToRemoveMediaIfNoMeta(badMetaFileFullNamePath)
                continue
        
            # Load the meta content
            metaData = None
            try:
                metaData = a.infra.format.json.readFromFile(self._logIo, data[KEY_META_FILE_FULL_NAME_PATH])
            except Exception as ex:
                self._logGeneral("error-reading-meta-data").error("can't get meta data from file='%s'. cid=%s. exception=%s", data[KEY_META_FILE_FULL_NAME_PATH], cid, ex)
            

            if metaData!= None:
                self._logGeneral("meta-file-content").notice("cid=%s. meta file content for file=%s:\n%s", cid, data[KEY_META_FILE_FULL_NAME_PATH], metaData)

            metaRemoved = True
            metaPersistentRemoved = True
            mediaRemoved = True

            shouldUpdateCounters = False
            if cid in self._cidLastAccessTimeDict:
                shouldUpdateCounters = KEY_WAS_COUNTED in self._cidLastAccessTimeDict[cid]
                # Pop the cid from the dict. 
                self._cidLastAccessTimeDict.pop(cid,0)

            # Try to remove the content
            rc = self._removeContent(cid, data, shouldUpdateCounters)
            
            if (rc == REMOVED_OK):
                # If file was removed
                self.counters['numBadContentRemoved'] +=1
                numOfBadContentRemoved +=1
                self._logGeneral("bad-content-removed").debug2("bad content has been removed. cid=%s, metaFileFullNamePath=%s", cid, data[KEY_META_FILE_FULL_NAME_PATH])
            else:          
                # Let's try archiving and removing the meta anyway
                if (rc == ERROR_READ_META) or (rc == ERROR_REMOVE_META):
                    metaRemoved = self._archiveCallBack(data[KEY_META_FILE_FULL_NAME_PATH])

                # Let's try removing the meta persistent file anyway
                if (rc == ERROR_REMOVE_META_PERSISTENT):
                    try:
                        os.remove(data[KEY_META_PERSISTENT_FILE_FULL_NAME_PATH])    
                    except Exception as ex:
                        metaPersistentRemoved = False
                        self._logIo("error-remove-bad-meta-persistent").error("error removing bad meta persistent file='%s'. exception: %s", data[KEY_META_PERSISTENT_FILE_FULL_NAME_PATH], ex)

                # No meta was found or error reading/removing it. lets try removing the content if we have the path and if it exists 
                if (mediaFileFullNamePath != None) and (os.path.exists(mediaFileFullNamePath)):
                    try:
                        os.remove(mediaFileFullNamePath)
                    except Exception as ex:
                        mediaRemoved = False
                        self._logIo("error-remove-bad-media").error("error removing bad media file='%s'. exception: %s", mediaFileFullNamePath, ex)
                else:
                    mediaRemoved = False
            

            # Remove the '.bad' file only if meta was removed. We don't want the leave bad meta without the bad file
            if metaRemoved:
                if os.path.exists(badMetaFileFullNamePath):
                    try:
                        os.remove(badMetaFileFullNamePath)
                    except Exception as ex:
                        self.counters['numErrorRemovingBadFiles'] += 1
                        self._logGeneral("error-remove-bad").error("error removing bad file='%s'. cid=%s. exception=%s", badMetaFileFullNamePath,cid, ex)
            else:
               self._logGeneral("meta-and-bad-not-removed").warning("bad file=%s not removed because meta file=%s could not be removed. mediaRemoved=%s, metaPersistentRemoved=%s", badMetaFileFullNamePath, data[KEY_META_FILE_FULL_NAME_PATH], mediaRemoved, metaPersistentRemoved)


        self._badContentList[:] = []
        return numOfBadContentRemoved;


    def clearAllContent(self):
        # scan for bad content (before clearing all)
        totalBadFilesScanned = self.scanForBadContent()
        self._logGeneral("clear-all-content-bad-prescan").info("bad content was scanned before clear: totalBadFilesScanned=%s", totalBadFilesScanned)

        # scan for new content (before clearing all)
        totalMetaFilesScanned, totalNewFilesAdded = self.scanForNewContent()
        self._logGeneral("clear-all-content-prescan").info("content was scanned before clear: totalMetaFilesScanned=%s, totalNewFilesAdded=%s", 
                                                     totalMetaFilesScanned, totalNewFilesAdded)
        # clear all content
        numOfContentRemoved, numOfBadContentRemoved = self.removeOldContent(shouldCleanAll=True) 
        self._logGeneral("clear-all-content").notice("all content was cleared: numOfContentRemoved=%s, numOfBadContentRemoved=%s", 
                                                     numOfContentRemoved, numOfBadContentRemoved)

        # We return the total num of titles removed
        numTitlesRemoved = numOfContentRemoved + numOfBadContentRemoved
        return numTitlesRemoved




    def removeOldContent (self, shouldCleanAll=False):
        """Remove old content.

        Remove old content.
        This function sorts it's content DB and removes old content according to the configuration.

        Args:
            None

        Returns:
            int: Number of content removed

        Raises:
            None
        """

        # First, remove bad content
        numOfBadContentRemoved = self._removeBadContent(shouldCleanAll)

        diskUsagePercentTrigger = self._cfg.diskUsagePercentTrigger
        diskUsagePercentTarget = self._cfg.diskUsagePercentTarget
        lastAccessThresholdMinutes = self._cfg.lastAccessThresholdMinutes
        lastAccessThresholdWarnMinutes = self._cfg.lastAccessThresholdWarnMinutes
        numContentToRemove = self._cfg.maxNumOfContentToRemove

        if shouldCleanAll is True:
            diskUsagePercentTrigger = 0 
            diskUsagePercentTarget = 0 
            lastAccessThresholdMinutes = 0      
            lastAccessThresholdWarnMinutes = 0
            numContentToRemove = -1
            
        diskUsage = self.getDiskUsage()
        if diskUsage > self.diskUsageCounters['maxDiskUsagePercent']:
            self.diskUsageCounters['maxDiskUsagePercent'] = diskUsage
        self._logGeneral("remove-content-disk-usage").debug3("current disk usage: %s", str(diskUsage))

        # If we are below the disk usage percent trigger - return
        if  diskUsage < diskUsagePercentTrigger and len(self._cidLastAccessTimeDict) <= self._cfg.maxTitleCount:
            return 0, numOfBadContentRemoved

        # Generate a list of the enteries        
        contentList = self._cidLastAccessTimeDict.items()
        self._logGeneral("remove-content-cid-dict").debug3("current cid dictionary: %s", self._cidLastAccessTimeDict)

        # This lambda will give us access to the last access time in each entry - for sorting
        lastAccessLambda = lambda k:k[1][KEY_LAST_ACCESS_TIME]

        # Sort the list according to the lastAccessTime (the first entry for the value of the key)
        contentList.sort(key=lastAccessLambda)

        if numContentToRemove == -1:
            numContentToRemove = len(contentList)


        contentListIndex = 0
        currentTime = time.time()
        numOfContentRemoved = 0
        numOfContentFailedToRemove = 0

        shouldBreakOuterLoop = False
        # While we didn't get to the disk usage target and we haven't reached our max number of content to remove
        while self._shouldKeepRemoving(diskUsage, diskUsagePercentTarget) and (contentListIndex < numContentToRemove):
            currentIterationCount = 0
            if shouldBreakOuterLoop:
                break
            while (currentIterationCount < self._cfg.numContentToRemoveEachIteration) and (contentListIndex < numContentToRemove):
                
                currentIterationCount +=1

                # If we have too many errors we stop the loop
                if numOfContentFailedToRemove >= MAX_ERRORS_TO_HANDLE:
                    self._logGeneral("too-many-failed").warning("got too many failed to remove. stopping the cleaning iteration. MAX_ERRORS_TO_HANDLE=%d", MAX_ERRORS_TO_HANDLE)
                    shouldBreakOuterLoop = True
                    break
    
                # Get the entry info
                cid = contentList[contentListIndex][0]
                data = contentList[contentListIndex][1]
                timeSinceLastAccessed = currentTime - data[KEY_LAST_ACCESS_TIME]
                
                shouldRemove = True
                # Check thresholds and remove if needed
                if timeSinceLastAccessed < lastAccessThresholdMinutes*60:
                    # We are below the threshold - check cfg if we want to remove it or not
                    self.counters['numNotRemovedBelowLastAccessThreshold'] +=1
                    self._logGeneral("below-threshold").warning("time sinced last accessed is below threshold. cid=%s, timeSinceLastAccessedSec=%f, lastAccessThresholdSec=%f", cid, timeSinceLastAccessed, lastAccessThresholdMinutes*60)
                    if not self._cfg.shouldRemoveContentUnderThreshold:
                        shouldRemove = False
                else:
                    if timeSinceLastAccessed < lastAccessThresholdWarnMinutes*60:
                        # We are below the warn threshold - count and log
                        self._logGeneral("below-threshold").notice("time sinced last accessed is below warn threshold. cid=%s, timeSinceLastAccessedSec=%f, lastAccessThresholdWarnSec=%f", cid, timeSinceLastAccessed, lastAccessThresholdWarnMinutes*60)
                        self.counters['numRemovedBelowLastAccessThresholdWarn'] +=1
                        
    
                if shouldRemove:             
                    if (not shouldCleanAll) and self._isInAcquisition(data[KEY_META_FILE_FULL_NAME_PATH]):
                        self._logGeneral("content-in-acq-not-removed").debug2("content candidate for removel is in acquisition and won't be removed. cid=%s, timeSinceLastAccessed=%f, metaFileFullNamePath=%s", cid, timeSinceLastAccessed, data[KEY_META_FILE_FULL_NAME_PATH])
                        contentListIndex += 1
                        continue 


                    shouldUpdateCounters = False
                    if cid in self._cidLastAccessTimeDict:
                        shouldUpdateCounters = KEY_WAS_COUNTED in self._cidLastAccessTimeDict[cid]
                        # Pop the cid from the dict. 
                        self._cidLastAccessTimeDict.pop(cid,0)

                    # Remove the content
                    rc = self._removeContent(cid, data, shouldUpdateCounters)
    
                    if rc == REMOVED_OK:
                        # if file was removed
                        self.counters['numGoodContentRemoved'] +=1
                        numOfContentRemoved +=1
                        self._logGeneral("content-removed-ok").debug3("content has been removed. cid=%s, timeSinceLastAccessed=%f, metaFileFullNamePath=%s", cid, timeSinceLastAccessed, data[KEY_META_FILE_FULL_NAME_PATH])
                    else:
                        # We got error trying remove the content. We log it and count it. 
                        self.counters['numNotRemovedDueToError'] +=1
                        numOfContentFailedToRemove +=1
                        self._logGeneral("content-removed-error").debug3("content has failed pn remove. cid=%s, timeSinceLastAccessed=%f, metaFileFullNamePath=%s", cid, timeSinceLastAccessed, data[KEY_META_FILE_FULL_NAME_PATH])
           
                contentListIndex += 1


            diskUsage = self.getDiskUsage()
            if diskUsage > self.diskUsageCounters['maxDiskUsagePercent']:
                self.diskUsageCounters['maxDiskUsagePercent'] = diskUsage


        self._logGeneral("remove-old-content").debug2("old content was removed: numOfContentRemoved=%s, numOfBadContentRemoved=%s", 
                                                     numOfContentRemoved, numOfBadContentRemoved)
        return numOfContentRemoved, numOfBadContentRemoved




    def _shouldKeepRemoving (self, diskUsage, diskUsagePercentTarget):
        return (diskUsage > diskUsagePercentTarget) or (len(self._cidLastAccessTimeDict) > self._cfg.maxTitleCount)




    def shredAllContent (self):
        self._logIo("shred-started").debug1("starting to shred all content on disk")
        # We have set of meta file directories. go over each directory.
        for disk in self._disksSet:

            metaRamRootDir = os.path.join(self._cfg.metaRamBaseDir, "%02u" % disk)
            metaPersistentRootDir = os.path.join(self._cfg.metaPersistentBaseDir, "%02u" % disk)
            mediaRootDir = os.path.join(self._cfg.mediaBaseDir, "%02u" % disk)

            # Shred the meta ram dir
            self._logIo("shred-meta").info("shreding meta files on ram")
            actualPath = os.path.realpath(metaRamRootDir)
            try:
                self._deleteSubDirsAndContent(actualPath)
            except Exception as ex:
                self._logIo("error-shred-meta").error("error shreding meta ram. metaRamRootDir=%s, actualPath=%s. exception=%s", metaRamRootDir, actualPath, ex)

            # Shred the meta dir
            self._logIo("shred-meta").info("shreding meta persistent files")
            actualPath = os.path.realpath(metaPersistentRootDir)
            try:
                self._deleteSubDirsAndContent(actualPath)
            except Exception as ex:
                self._logIo("error-shred-meta").error("error shreding meta. metaPersistentRootDir=%s, actualPath=%s. exception=%s", metaPersistentRootDir, actualPath, ex)

            # Shred the media dir
            self._logIo("shred-media").info("shreding media files")
            actualPath = os.path.realpath(mediaRootDir)
            try:
                self._deleteSubDirsAndContent(actualPath)
            except Exception as ex:
                self._logIo("error-shred-meta").error("error shreding meta. mediaRootDir=%s, actualPath=%s. exception=%s", mediaRootDir, actualPath, ex)

            ## notify remove all bytes on prediction mode
            #if self._isPrediction is True:
            #    diskData = self.getVirtualDiskData(disk)
            #
            #    if diskData is not None:
            #        totalUsedBytes = diskData["totalUsedBytes"]
            #        self.counters['numTotalPredictionRemovedBytes'] += totalUsedBytes

        # Now let's remove the content from the db
        self._cidLastAccessTimeDict.clear()

        # Let's clear the counters 
        for key in self.numTitlesCounters:
            self.numTitlesCounters[key] = 0

        for key in self.bytesUsedCounters:
            self.bytesUsedCounters[key] = 0

        self.counters['numTotalPredictionRemovedBytes'] = 0

        # Clear state on disk
        if os.path.exists(self._dbFileFullNamePath):
            try:
                os.remove(self._dbFileFullNamePath)
            except Exception as ex:
                self._logIo("error-remove-db-file").error("error removing db file='%s'. exception: %s", self._dbFileFullNamePath, ex)

        if os.path.exists(self._countersFileFullNamePath):
            try:
                os.remove(self._countersFileFullNamePath)
            except Exception as ex:
                self._logIo("error-remove-db-file").error("error removing counters file='%s'. exception: %s", self._countersFileFullNamePath, ex)





    def loadAndUpdateEvents (self, allDisksLastAccessTimeUpdates):
        """Updates the last access time dictionary.

        Updates the last access time dictionary. 
        This function reads lastTimeAccessUpdates from files

        Args:
            lastAccessTimeUpdates: Dict which holds updates for the last access time of CIDs.
                                   Key: CID
                                   Value: lastAccessTime

        Returns:
            None

        Raises:
            None
        """
        lastAccessTimeUpdates = dict()

        for disk in self._disksSet:
            if disk in allDisksLastAccessTimeUpdates:
                lastAccessTimeUpdates.update(allDisksLastAccessTimeUpdates[disk])

        numOfupdates = 0
        numOfNewCid = 0

        # We don't manipulate the dict so we can use iterator
        for cid, data in lastAccessTimeUpdates.iteritems():

            if cid in self._cidLastAccessTimeDict:
                self._logGeneral("update-cid").debug2("proccessing a last access time update for cid=%s", cid)
                if self._cidLastAccessTimeDict[cid][KEY_LAST_ACCESS_TIME] < data[KEY_LAST_ACCESS_TIME]:
                    self._logGeneral("updating-cid").debug2("updating last access time update for cid=%s, from=%d to=%d", cid, self._cidLastAccessTimeDict[cid][KEY_LAST_ACCESS_TIME], data[KEY_LAST_ACCESS_TIME])
                    self._cidLastAccessTimeDict[cid][KEY_LAST_ACCESS_TIME] = data[KEY_LAST_ACCESS_TIME]
                    numOfupdates +=1
                    self.counters['numTotalLastAccessUpdates'] += 1
            else:
                if cid in [entry[1] for entry in self._badContentList]:
                    self._logGeneral("update-to-bad-cid").debug2("got a last access time update for bad cid. not updating. cid=%s",cid)
                    continue
                else:
                    self._logGeneral("update-to-non-existing-cid").debug2("got a last access time update for cid not in db. cid=%s",cid)
                    self.counters['numTotalLastAccessUpdatesForNewCID'] += 1
                    numOfNewCid += 1
                    self._cidLastAccessTimeDict[cid] = {KEY_LAST_ACCESS_TIME:data[KEY_LAST_ACCESS_TIME], KEY_META_FILE_FULL_NAME_PATH:data[KEY_META_FILE_FULL_NAME_PATH], KEY_META_PERSISTENT_FILE_FULL_NAME_PATH:data[KEY_META_PERSISTENT_FILE_FULL_NAME_PATH], KEY_DISK_NUM:data[KEY_DISK_NUM]}


        return numOfupdates, numOfNewCid



    def saveDbToDisk (self):
        """Saves the db to disk.

        Saves the db to disk. 
        This function saves the db to the disk.
        Each record in the file will be in a new line and each record field will be saperated with \t.
        Record's fields:
        cid, lastAccessTime, metaFileFullPath, diskNum, error(optional)

        Args:
            None

        Returns:
            None

        Raises:
            None
        """

        currentThread=threading.currentThread()
        self._logIo("save-db-to-disk").debug1("starting to save db for instance %s. thread-id=%d", self._instanceName, currentThread.ident)

        # We dump the dict to Json format
        try:
            a.infra.format.json.writeToFile(self._logIo, self._cidLastAccessTimeDict, self._dbFileFullNamePath)
        except Exception as ex:
            self._logIo("error-write-db-file").error("error writing db to file='%s'. exception: %s", self._dbFileFullNamePath, ex)

        # We dump prediction counters for presistency
        try:
            a.infra.format.json.writeToFile(self._logIo, self.counters, self._countersFileFullNamePath)
        except Exception as ex:
            self._logIo("error-write-counters-file").error("error writing counters to file='%s'. exception: %s", self._countersFileFullNamePath, ex)
                 
        return self._dbFileFullNamePath, self._dbFailedToRemoveFileFullNamePath





    def loadDbFromDisk (self):
        """Loads the db from disk.

        Loads the db from disk. 
        This function loads the db into the dict.
        This should only be used when luanching the content cleaner.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        currentThread=threading.currentThread()
        self._logIo("load-db-from-disk").debug1("starting to load db. thread-id=%d", currentThread.ident)

        startLoadingTime = time.time()
        if os.path.exists(self._dbFileFullNamePath):
            try:
                self._cidLastAccessTimeDict = a.infra.format.json.readFromFile(self._logIo, self._dbFileFullNamePath)
                self._logIo("read-db-from-disk").debug1("loading db - reading from file time is: %.6f", time.time() - startLoadingTime)
                startValidatingTime = time.time()
                self._scanLastAccessDictForJunk()
                self._logIo("validate-db").debug1("loading db - validating data time is: %.6f", time.time() - startValidatingTime)
            except Exception as ex:
                self._logIo("error-read-db-file").error("error reading db file='%s'. exception: %s", self._dbFileFullNamePath, ex)

        if os.path.exists(self._countersFileFullNamePath):
            try:
                countersData = a.infra.format.json.readFromFile(self._logIo, self._countersFileFullNamePath)
                
                # load prediction counters for presistency
                self.counters['numTotalPredictionRemovedBytes'] = countersData['numTotalPredictionRemovedBytes']
            except Exception as ex:
                self._logIo("error-read-counters-file").error("error reading counters file='%s'. exception: %s", self._countersFileFullNamePath, ex)
        self._logIo("read-db-from-disk").debug1("loading db - total time is: %.6f", time.time() - startLoadingTime)


    def logState (self):
        self._logGeneral("state").notice("Cleaner current state: %s. current content count:%d", self.counters, self.getContentCount())


    def getContentCount (self):
        return len(self._cidLastAccessTimeDict)
        

    def _deleteSubDirsAndContent (self, dirName):
        for fileOrDirName in os.listdir(dirName):
            fileOrDirNamePath = os.path.join(dirName, fileOrDirName)
            try:
                if os.path.isfile(fileOrDirNamePath):
                    self._logIo("remove-file").debug2("removing file '%s'" , fileOrDirNamePath)
                    os.remove(fileOrDirNamePath)
                else:
                    self._logIo("remove-tree").debug2("removing the directory tree at '%s'" , fileOrDirNamePath)
                    shutil.rmtree(fileOrDirNamePath)
            except Exception as ex:
                self._logIo("delete-sub-dirs-and-content").error("got exception trying to remove '%s'. exception: %s" % (fileOrDirNamePath, ex))


    def _tryToRemoveMediaIfNoMeta (self,badOrMetaFilePath):
        #assume the path of the media according to the meta or bad filename
        # this is a huristic holding water only as long as we use relative media and meta paths
        notBad = re.sub(r"\.bad$","",badOrMetaFilePath)
        notMeta = re.sub(r"\.meta$","",notBad)
        mediaPath = re.sub(r".*/meta/", "%s/" % self._cfg.mediaBaseDir ,notMeta)
        
        self._logIo("assume-orphan-media").debug2("assuming orphan file '%s' deduced from '%s'" , mediaPath , badOrMetaFilePath)
        if os.path.exists(mediaPath):
            self._logIo("remove-orphan-media").warning("removing orphan media file '%s' deduced from '%s'" , mediaPath , badOrMetaFilePath)
            try:
                os.remove(mediaPath)
                self.counters['numMediaNoMetaRemoved'] += 1
            except Exception as ex:
                self.counters['numMediaNoMetaRemoveErrors'] += 1
                self._logGeneral("error-remove-orphan").error("error removing orphan media file='%s' exception=%s", mediaPath, ex)

        


    def _removeContent (self, cid, data, shouldUpdateCounters):
        # First let's get the meta content
        metaData = None
        metaFileFullNamePath = data[KEY_META_FILE_FULL_NAME_PATH]
        metaPersistentFileFullNamePath = data[KEY_META_PERSISTENT_FILE_FULL_NAME_PATH]
        if not (os.path.exists(metaFileFullNamePath) and os.path.isfile(metaFileFullNamePath)):
            self.counters['numErrorNoMetaFiles'] += 1
            self._logGeneral("no-meta-file").error("no meta file='%s'. cid=%s" , metaFileFullNamePath, cid)
            self._tryToRemoveMediaIfNoMeta(metaFileFullNamePath)
            return NO_META
        else:
            try:
                metaData = a.infra.format.json.readFromFile(self._logIo, metaFileFullNamePath)
            except Exception as ex:
                self.counters['numErrorReadingMetaFiles'] += 1
                self._logGeneral("error-reading-meta").error("can't get meta data from file='%s'. cid=%s. exception=%s", metaFileFullNamePath, cid, ex)
                return  ERROR_READ_META

        # Get the media path
        mediaFileFullNamePath = None
        if 'mediaRelativeFilePath' in metaData:
            mediaFileFullNamePath = os.path.join(self._cfg.mediaBaseDir, metaData['mediaRelativeFilePath'])
        else:
            self.counters['numErrorNoMediaPathInMeta'] += 1
            self._logGeneral("error-reading-media-path").error("no media path in file='%s'. cid=%s. metaData=%s", metaFileFullNamePath, cid, metaData)
            return  ERROR_READ_META

        # Check that media exists
        mediaFound = True
        if not (os.path.exists(mediaFileFullNamePath) and os.path.isfile(mediaFileFullNamePath)):
             self._logGeneral("error-finding-media").error("can't find media. looking for media file='%s'. going to delete meta file=%s", mediaFileFullNamePath, metaFileFullNamePath)
             self.counters['numErrorNoMediaFiles'] += 1
             mediaFound = False

        # Now archive if needed and remove the meta (before the content)
        if not self._archiveCallBack(metaFileFullNamePath):
            self.counters['numErrorRemovingMetaFiles'] += 1
            return ERROR_REMOVE_META

        # Now remove the meta persistent file
        try:
            os.remove(metaPersistentFileFullNamePath)
        except Exception as ex:
            self.counters['numErrorRemovingMetaPersistentFiles'] += 1
            self._logGeneral("error-remove-meta-persistent").error("error removing meta file='%s'. cid=%s. exception=%s", metaPersistentFileFullNamePath,cid, ex)
            return ERROR_REMOVE_META_PERSISTENT

        # Remove the media file
        if mediaFound:
            try:
                os.remove(mediaFileFullNamePath)
            except Exception as ex:
                self.counters['numErrorRemovingMediaFiles'] += 1
                self._logGeneral("error-remove-media").error("error removing media file='%s'. cid=%s. exception=%s", mediaFileFullNamePath,cid, ex)
                return ERROR_REMOVE_MEDIA
            
            # let's try to read the disk usage of the file
            byteSize = 0;
            cgid = -1
            if (metaData != None) and ('bytesDiskSize' in metaData) and ('siteId' in metaData):
                byteSize = metaData['bytesDiskSize']
                cgid = metaData['siteId']
            if self._isPrediction is True:     
                self.counters['numTotalPredictionRemovedBytes'] += byteSize

            if shouldUpdateCounters:
                self._decrCounters(cgid, byteSize)

        else:
            return NO_MEDIA    
        
        if metaData!= None:
            # Count total content removed (including bad content)
            self.counters['numTotalContentRemoved'] +=1
    
            # Count total bytes removed (including bad content)
            if 'bytesDiskSize' in metaData:
                self.counters['numTotalBytesRemoved'] += metaData['bytesDiskSize']
    
            # Count total titles lifeTime
            if 'creationTime' in metaData:
                creationTime = metaData['creationTime'].split(" ")[0]
                contentLifeTimesec = time.time() - int(creationTime)
                self.counters['numTotalTitleLifeTimeSec'] += int(contentLifeTimesec)

        return REMOVED_OK



    def _decrCounters(self, cgid, bytesToDecrement):
        isKnownCgid = cgid in self.cgidToNameMap
        baseCounterKey = ''
        if self._isPrediction:
            baseCounterKey = PREDICTION_TOKEN

        self.bytesUsedCounters[NUM_TOTAL_USED_BYTES + baseCounterKey + self.cgidToNameMap[0]] -= bytesToDecrement
        if isKnownCgid:
            self.bytesUsedCounters[NUM_TOTAL_USED_BYTES + baseCounterKey + self.cgidToNameMap[cgid]] -= bytesToDecrement
        self.numTitlesCounters[NUM_TITLES + baseCounterKey + self.cgidToNameMap[0]] -= 1
        if isKnownCgid:
            self.numTitlesCounters[NUM_TITLES + baseCounterKey + self.cgidToNameMap[cgid]] -= 1


    def _isInAcquisition (self, metaFileFullNamePath):
        acqFileName = metaFileFullNamePath + "." + self._cfg.acqFilesExtension
        return os.path.exists(acqFileName)




#------------------Public for UT ---------------------------------------#
    def getDiskUsage (self, disksSet = None):
        """
            Get the disk usage for the fileSystem of the given directory list.
            The assumption is that each directory is on different disk.
            We sum the used blocks and the total blocks and get the final "disk" usage.
            Works only for linux.
       
            Returns:
                float: diskUsage in precentage
        """
        if disksSet == None:
            disksSet = self._disksSet

        if platform.system() == "Linux":
       
            totalBlocks = 0
            totalUsedBlocks = 0

            if len(disksSet)==0:
                return 0
   
            for disk in disksSet:

                if self._isPrediction is False:
                    mediaRootDir = os.path.join(self._cfg.mediaBaseDir, "%02u" % disk)
                    actualPath = os.path.realpath(mediaRootDir)
                    # Get the statistics for the file system
                    statistics = os.statvfs(actualPath)
                    # Sum used and total blocks
                    totalUsedBlocks += float(statistics[statvfs.F_BLOCKS]) - float(statistics[statvfs.F_BFREE])
                    totalBlocks += float(statistics[statvfs.F_BLOCKS])
                else:

                    diskData = self.getVirtualDiskData(disk)

                    if diskData is not None:
                        totalUsedBlocks += float(diskData["totalUsedBytes"])
                        totalBlocks += float(diskData["totalDiskBytes"])
                    else:
                        totalBlocks+=1.0

        
            # Calculate the "disk" usage 
            diskUsage = 100*(totalUsedBlocks/totalBlocks)

        else:
            self._logGeneral().error("not on linux. can't calculate disk usage")
            raise Exception("platformError","not linux")
       
        self._logGeneral("disk-usage").debug2("diskUsage=%s", diskUsage)
        return diskUsage



    def getVirtualDiskData (self, disk):
        self._logGeneral("perdiction-virtual-disk-data").debug2("disk %s: get virtual disk data", disk)

        # Load the disk usage data file
        diskData = None
        diskUsageFile = os.path.join(self._cfg.mediaBaseDir, "%02u" % disk, "du.txt")
       
        if os.path.exists(diskUsageFile) is True:
            try:
                diskData = a.infra.format.json.readFromFile(self._logIo, diskUsageFile)
            except Exception as ex:
                self._logIo("error-reading-perdiction-du-file").debug1("can't get disk data from file='%s'. exception=%s", diskUsageFile, ex)
        else:
            self._logGeneral("error-perdiction-du-get").debug3("failed retrieving disk data from file='%s'", diskUsageFile)

        if diskData is not None:
            totalRemovedBytes = self.counters['numTotalPredictionRemovedBytes']

            # update used bytes
            self._logGeneral("perdiction-du-removed-bytes").debug1("disk %s: already removed total bytes of %s", 
                                                                   disk, totalRemovedBytes)
            diskData["totalUsedBytes"]-=totalRemovedBytes

        return diskData


    def scanAndMarkCgid(self,cgid):                
    
        for cid,data in self._cidLastAccessTimeDict.iteritems():
            titleCgid = 0
            try:
                titleCgid = int(self._cidLastAccessTimeDict[cid][KEY_CGID])
            except Exception,ex:
                self._logGeneral("cgid-clean-scan").debug1("cid %s has old format. %s",cid,str(ex))
            if cid not in self._cidsToBeMarkedBad and cgid == titleCgid:  
                self._cidsToBeMarkedBad[cid]=(cgid,self._cidLastAccessTimeDict[cid][KEY_META_FILE_FULL_NAME_PATH])
            else:
                self._logGeneral("cgid-clean-scan").debug1("cid %s in-db=%s cgid=%d titleCgid=%d",cid,(cid not in self._cidsToBeMarkedBad),cgid,titleCgid)
        return len(self._cidsToBeMarkedBad)
        


    def createBadFilesPerCgidCleanContent(self):
        startTime = time.time()
        isMarking = True
        remains = dict()
        counter=0
        for cid,data in self._cidsToBeMarkedBad.iteritems():
            if isMarking:# create bad file
                counter += 1
                badFile = "%s%s" % (data[1],".bad")
                fd=open(badFile,"w")
                if fd is not None:
                    fd.write('{ "reason" : "per cgid deletion" }\n')
                    fd.close()
                else:
                    self._logGeneral("cgid-generate-bad").error("failed to open bad file %s for write",badFile)
                currTime=time.time()
                if (currTime - startTime) > 3:
                    isMarking = False
            else:
                remains[cid]=data
        if counter > 0:
            self._logGeneral("cgid-generate-bad").debug1("generated %s bad files",counter)
        self._cidsToBeMarkedBad = remains
        return counter

    
    def getPerCgidNumMarkedForDeletion (self):
        """
        Get per cgid count of pending items for deletion
        """
        total = dict()
        for cid,cgid in self._cidsToBeMarkedBad.iteritems():
            if cgid not in total:
                total[cgid]=0
            num=total[cgid]
            total[cgid]=num+1
        return total



#   def scanAndMarkCgid(self,cgid):
#       # Walk in the directory tree
#       metaFilesPattern=self._metaFilesPattern
#
#       markedBad=0
#       filesNotMarked=0
#       metaOpenErrors=0
#
#       for disk in self._disksSet:
#           metaRamRootDir = os.path.join(self._cfg.metaRamBaseDir, "%02u" % disk)
#           for (currentRoot,dirNames,FileNames) in os.walk(metaRamRootDir):
#               # For each file (if there is any):
#               for metaFileName in fnmatch.filter(FileNames, metaFilesPattern):
#                   # Get the meta file full name path
#                   metaFileFullNamePath = os.path.join(currentRoot,metaFileName)
#
#                   # Check if Bad exists
#                   badMetaFileFullNamePath = metaFileFullNamePath + "." + self._cfg.badFilesExtension
#
#                   if os.path.exists(badMetaFileFullNamePath):
#                       # No need to process it. It will be deleted
#                       continue
#                   try:
#                       metaData = a.infra.format.json.readFromFile(self._logIo, metaFileFullNamePath)
#                   except Exception as ex:
#                       self._logGeneral("cgid-cleaner-error-reading-meta").error("cgid-cleaner can't get meta data from file='%s'. exception=%s", metaFileFullNamePath, ex)
#                       metaOpenErrors +=1
#                   if metaData != None:
#                       if 'siteId' in metaData:
#                           fromFile=metaData['siteId']
#                           if fromFile == cgid:
#                               # this does 'touch' and closes fd as it has no references
#                               open(badMetaFileFullNamePath,"w")
#                               markedBad += 1
#                           else:
#                               self._logGeneral("cgid-cleaner-skip").debug4("desired=%s found=%s",cgid,fromFile)
#                               filesNotMarked += 1
#                       else:
#                           self._logGeneral("cgid-cleaner-no-site-id").error("cgid-cleaner- no 'siteId' in file='%s'.", metaFileFullNamePath)
#                           metaOpenErrors +=1
#                   else:
#                       self._logGeneral("cgid-cleaner-meta-is-none").warning("cgid-cleaner can't load meta data for updating counters for file='%s'", metaFileFullNamePath)
#                       metaOpenErrors +=1
#           self._logGeneral("cgid-cleaner-done").notice("cgid-cleaner done. marked %d files , skipped %d and had %d meta read errors.", markedBad,filesNotMarked,metaOpenErrors)



class ContentCleanerGroup (object):

    #---- Ctor -----------------------------------#
    def __init__ (self, periodicWorkCallBack):
        self.contentCleanersList = []
        self.metaRamBaseDir = None
        self.metaPersistentBaseDir = None
        self.periodicWorkCallBack = periodicWorkCallBack
        self._archiver = None
        self._wasArchiverClosed = False
        self._cfg = None
        self._logGeneral = None
        self.totalMarkedBadByPerCgidContentClean = 0


    def initLogger (self, logger):
        self._logGeneral = logger

    def initCfg (self, cfg):
        self._cfg = cfg


    def init (self):
        # Init the archiver
        if self._cfg.shouldArchive:
            # Let's create directory for this instance
            bufferDir = os.path.realpath(self._cfg.archiverBufferDir)

            self._logGeneral("archiver-dirs").debug1("bufferDir=%s, archiverDir=%s", bufferDir, self._cfg.archiverOutputDir)
            self._archiver = a.infra.file.rotating_file_archiver.Archiver(logger=self._logGeneral,\
                                                                          inputDir=bufferDir, \
                                                                          bufferDirSizeLimitInMB=self._cfg.archiverBufferDirSizeLimitMb, \
                                                                          outputDir=self._cfg.archiverOutputDir)

            self._archiver.setUseFixedFileSize(4096)
            self._archiver.setFileSizeThresholdMB(self._cfg.archiverOutFileSizeLimitMb)
            self._archiver.setOutputDirSizeLimitGB(self._cfg.archiverOutDirSizeLimitGb)
            


    def createAndInitContentCleaners (self, disksSetList):
        self.init()
        self.metaRamBaseDir = self._cfg.metaRamBaseDir
        self.metaPersistentBaseDir = self._cfg.metaPersistentBaseDir
        for disksSet in disksSetList:

            if len(disksSet) >= 1:
                instanceName = ("%02u" % disksSet[0])
                if len(disksSet) > 1:
                 instanceName += "-" + ("%02u" % disksSet[len(disksSet)-1])
            else:
                raise Exception("disksSet is empty")

            contentCleanInstance = ContentCleaner(instanceName)
            contentCleanInstance.initLogger(self._logGeneral)
            contentCleanInstance.initCfg(self._cfg)
            contentCleanInstance.initArchiveCallBack(self.removeAndArchiveMetaFileifNeededCallBack)
            contentCleanInstance.initPeriodicWorkCallBack(self.periodicWorkCallBack)
            contentCleanInstance.init(disksSet)
            self.contentCleanersList.append(contentCleanInstance)


    def updateCleanersCfg (self, cfg):
        numTitleRemoved = 0
        for contentCleaner in self.contentCleanersList:
            numTitleRemoved += contentCleaner.initCfg(cfg)
        return  numTitleRemoved


    def scanContent (self):
        totalMetaFilesScanned = 0
        totalNewFilesAdded = 0
        for contentCleaner in self.contentCleanersList:
            filesScanned, newFilesAdded = contentCleaner.scanForNewContent()
            totalMetaFilesScanned += filesScanned
            totalNewFilesAdded += newFilesAdded
            self.periodicWorkCallBack()
        return totalMetaFilesScanned, totalNewFilesAdded


    def scanBadContent (self):
        totalBadFilesScanned = 0
        for contentCleaner in self.contentCleanersList:
            badFilesScanned = contentCleaner.scanForBadContent()
            totalBadFilesScanned += badFilesScanned
        return totalBadFilesScanned


    def loadEvents (self, lastAccessTimeUpdates):
        numOfupdates = 0
        numOfNewCid = 0
        allDisksLastAccessTimeUpdates = dict()
        for cid, value in lastAccessTimeUpdates.items():
            if (KEY_LAST_ACCESS_TIME in value) and (KEY_META_FILE_RELATIVE_PATH in value) and (KEY_META_FILE_RELATIVE_PATH in value) and (KEY_DISK_NUM in value):
                if value[KEY_DISK_NUM] not in allDisksLastAccessTimeUpdates:
                    allDisksLastAccessTimeUpdates[value[KEY_DISK_NUM]] = dict()
                
                allDisksLastAccessTimeUpdates[value[KEY_DISK_NUM]][cid] = {KEY_LAST_ACCESS_TIME:value[KEY_LAST_ACCESS_TIME], \
                                                                           KEY_META_FILE_FULL_NAME_PATH:os.path.join(self.metaRamBaseDir, value[KEY_META_FILE_RELATIVE_PATH]), \
                                                                           KEY_META_PERSISTENT_FILE_FULL_NAME_PATH:os.path.join(self.metaPersistentBaseDir, value[KEY_META_FILE_RELATIVE_PATH]), \
                                                                           KEY_DISK_NUM:value[KEY_DISK_NUM]}
            else:
                self._logGeneral("bad-event").error("missing mandatory data in last access event. value=%s", value)

        for contentCleaner in self.contentCleanersList:
            numUpdates, numNewCid = contentCleaner.loadAndUpdateEvents(allDisksLastAccessTimeUpdates)
            numOfupdates += numUpdates
            numOfNewCid += numNewCid

        return numOfupdates, numOfNewCid

    def removeContent (self):
        numOfContentRemoved = 0
        numOfBadContentRemoved = 0
        numOfTotalContentRemoved = 0
        avgTotalContentRemovedPerDisk = 0
        peakTotalContentRemovedPerDisk = 0
        for contentCleaner in self.contentCleanersList:
            numRemoved, numBadRemoved = contentCleaner.removeOldContent()
            numOfContentRemoved += numRemoved
            numOfBadContentRemoved += numBadRemoved
            totalremoved = numRemoved + numBadRemoved
            numOfTotalContentRemoved += totalremoved
            if totalremoved > peakTotalContentRemovedPerDisk:
                peakTotalContentRemovedPerDisk = totalremoved
        avgTotalContentRemovedPerDisk = numOfTotalContentRemoved / len(self.contentCleanersList)
        return numOfContentRemoved, numOfBadContentRemoved, numOfTotalContentRemoved, avgTotalContentRemovedPerDisk, peakTotalContentRemovedPerDisk



    def loadFromDiskMultiThreaded (self):
        threadList = []
        for contentCleaner in self.contentCleanersList:
            t = threading.Thread(target=contentCleaner.loadDbFromDisk)
            t.start()
            threadList.append(t)
        for t in threadList:
            t.join()


    def saveToDiskMultiThreaded (self):
        threadList = []
        for contentCleaner in self.contentCleanersList:
            t = threading.Thread(target=contentCleaner.saveDbToDisk)
            t.start()
            threadList.append(t)
        for t in threadList:
            t.join()


    def saveToDisk (self):
        for contentCleaner in self.contentCleanersList:
            contentCleaner.saveDbToDisk()


    def shredAll (self):
        for contentCleaner in self.contentCleanersList:
            contentCleaner.shredAllContent()
        self.clearStateOnDisk()


    def clearStateOnDisk (self):
        if os.path.exists(self._cfg.dbFilesDir):
            for fileOrDirName in os.listdir(self._cfg.dbFilesDir):
                fileOrDirNamePath = os.path.join(self._cfg.dbFilesDir, fileOrDirName)
                try:
                    if os.path.isfile(fileOrDirNamePath):
                        os.remove(fileOrDirNamePath)
                    else:
                        shutil.rmtree(fileOrDirNamePath)
                except Exception as ex:
                    self._logGeneral("clear-state-disk-error").error("exception trying to remove %s. exception: %s", fileOrDirNamePath, ex)
                

    def scanAndMarkCgidToClean (self,cgid):
        currentTime = time.time()
        self._logGeneral("cgid-clean-start-scan").debug1("cgid %s start scan t=%s",cgid,currentTime)
        total=0
        try:
            for contentCleaner in self.contentCleanersList:
                total += contentCleaner.scanAndMarkCgid(cgid)
            currentTime = time.time()
            self._logGeneral("cgid-clean-end-scan").debug1("cgid %s end scan count=%d t=%d",cgid,total,currentTime)
        except Exception as ex:
            self._logGeneral("scan-for-marking-bad").error("Error scanning for marking bad %s", str(ex))
        

    def markBadPerCgidContent (self):
        try:
            for contentCleaner in self.contentCleanersList:
                self.totalMarkedBadByPerCgidContentClean += contentCleaner.createBadFilesPerCgidCleanContent()
        except Exception as ex:
            self._logGeneral("error-marking-for-bad").error("Error marking for bad %s\n%s", str(ex),traceback.format_exc())


    def getPerCgidDeletionStatus(self):
        total = dict()
        totalNum = 0
        for contentCleaner in self.contentCleanersList:
            subResult = contentCleaner.getPerCgidNumMarkedForDeletion()
            for cgid,num in subResult.iteritems():
                if cgid not in total:
                    total[cgid]=0
                total[cgid] = total[cgid] + num
                totalNum += num
        #todo - arnon: use dict result to display per cgid progress?
        return totalNum         


    def startArchiver (self, archiverThreadExceptionCallBack):
        #Start the archiver with the exception callback
        if self._cfg.shouldArchive and self._archiver != None:
            self._archiver.start(archiverThreadExceptionCallBack)


    def stop (self):
        for contentCleaner in self.contentCleanersList:
            contentCleaner.stop()
        self._closeArchiver()


    def logCleanersState (self):
        for contentCleaner in self.contentCleanersList:
            contentCleaner.logState()


    def getCountersList(self):
        countersList = []
        contentCountList = []
        bytesUsedCountersList = []
        numTitlesCountersList = []
        diskUsageCountersList = []
        for contentCleaner in self.contentCleanersList:
            countersList.append(contentCleaner.counters)
            contentCountList.append(contentCleaner.getContentCount())
            bytesUsedCountersList.append(contentCleaner.bytesUsedCounters) 
            numTitlesCountersList.append(contentCleaner.numTitlesCounters)
            diskUsageCountersList.append(contentCleaner.diskUsageCounters)


        return countersList, contentCountList, bytesUsedCountersList, numTitlesCountersList, diskUsageCountersList


    def resetMaxDiskUsageCounters(self):
        for contentCleaner in self.contentCleanersList:
            contentCleaner.diskUsageCounters['maxDiskUsagePercent'] = 0


    def _closeArchiver (self):
        if self._archiver != None:
            self._wasArchiverClosed = True
            self._archiver.stop()


    def removeAndArchiveMetaFileifNeededCallBack (self, metaFileFullNamePath):
        shouldRemove = True
        shouldCheckIfExists = False

        if self._cfg.shouldArchive and self._archiver != None and not self._wasArchiverClosed:
            self._logGeneral("archive-brownie").debug1("archiving file='%s'", metaFileFullNamePath)
            shouldRemove = False
            try:
                if not self._archiver.archiveFile(metaFileFullNamePath):
                    shouldCheckIfExists = True
            except Exception as ex:
                self._logGeneral("failed-archive-brownie").error("failed to archive file='%s'. exception=%s", metaFileFullNamePath, ex)
                shouldCheckIfExists = True
                

        if shouldCheckIfExists:
            if os.path.exists(metaFileFullNamePath):
                shouldRemove = True

        if shouldRemove:
            try:
                os.remove(metaFileFullNamePath)    
            except Exception as ex:
                self._logGeneral("error-remove-bad-meta-ram").error("error removing meta ram file='%s'. exception: %s", metaFileFullNamePath, ex)
                return False

        return True



    ########## FOR UT ##############################
    def initArchiveCallBacks (self, callBack):
        for contentCleaner in self.contentCleanersList:
            contentCleaner.initArchiveCallBack(callBack)


