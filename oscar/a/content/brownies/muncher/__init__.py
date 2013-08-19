#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: royr
# 

import time, datetime, os, statvfs, platform, subprocess
import a.infra.format.json
import a.infra.file.rotating_file
from a.stats.stats_comm_over_file_client import StatsCommOverFileClient
import a.infra.file.rotating_file_archiver
from delivery_tracking import DeliveryTracking

from a.content import KEY_LAST_ACCESS_TIME
from a.content import KEY_META_FILE_FULL_NAME_PATH
from a.content import KEY_META_FILE_RELATIVE_PATH
from a.content import KEY_DISK_NUM

G_NAME_MODULE_MUNCHER = "muncher"
G_NAME_GROUP_MUNCHER_GENERAL = "general"
G_NAME_GROUP_MUNCHER_IO = "io"


QUOTA_MARGIN_PERCENT = 12.5

class MuncherCfg (object):
    """This struct holds the configuration data for the muncher and should be filled and then passed when creating an instance."""
    def __init__ (self):
        # Input directory for brownies
        self.browniesRootDir = None
        # Brownie files suffix
        self.brownieFilesExtension = None
        # Output directory for lastAccessTime updates
        self.lastAccessUpdatesOutputDir = None
        # Should we write lau files?
        self.shouldWriteLastAccessUpdates = False
        # Delta to add to expiration time in order to prevent racing conditions with the delivery
        self.expirationTimeDeltaSec = 0
        # Interval for processing brownies
        self.browniesProcessingIntervalSec = 0
        # Interval for dumping the updates and rotating the file
        self.updatesFileRotationIntervalSec = 0
        # Quota file name
        self.quotaFileName = None
        # Quota limit
        self.quotaLimit = None
        # Disk usage threshold for zero quota
        self.quotaZeroDiskUsagePercent = None
        # Disk usage threshold for normal quota
        self.quotaNormalDiskUsagePercent = None
        # Stats reporting interval
        self.statsReportingIntervalSec = 60
        # Directories
        self.dataDir = None
        self.confDir = None
        self.tempDir = None
        # Archiving configuration
        self.shouldArchive = False
        self.archiverOutputDir = None
        self.archiverOutDirSizeLimitGb = None
        self.archiverOutFileSizeLimitMb = None
        self.archiverBufferDir = None
        self.archiverBufferDirSizeLimitMb = None
        self.archiverRotationTimeTresholdSeconds = None
        # Delivery Tracking
        self.deliveryTrackingEnabled = None
        self.deliveryTrackingUpdatesToLineDir = None
        self.deliveryTrackingBlockTTLSec = None
        self.deliveryTrackingShortBlockTTLSec = None
        self.deliveryTrackingWhitelistFile = None
        self.deliveryTrackingNewSessionIgnorePeriod = None
        self.deliveryTrackingMaxSessionKeys = None
        self.deliveryTrackingMaxNoDeliveryTableSize = None
        self.deliveryTrackingDumpTablesIntervalSec = None
        self.deliveryTrackingWindowSizeSec = None
        self.deliveryTrackingWindowNumFrames = None
        self.deliveryTrackingFloodProtectionEnabled = None
        self.deliveryTrackingFloodProtectionWindowSizeSec = None
        self.deliveryTrackingFloodProtectionWindowNumFrames = None
        self.deliveryTrackingFloodProtectionRatio = None
        self.deliveryTrackingMinSessionsToAllowProtection = None
        # Delivery Tracking Archiving configuration
        self.shouldArchiveNoDeliveryTable = None
        self.shouldArchiveDeliveryTrackingUpdatesToLine = None
        self.deliveryTrackingArchiveTableInterval = None
        self.deliveryTrackingArchiverOutputDir = None
        self.deliveryTrackingArchiverOutDirSizeLimitGb = None
        self.deliveryTrackingArchiverOutFileSizeLimitMb = None
        self.deliveryTrackingArchiverBufferDir = None
        self.deliveryTrackingArchiverBufferDirSizeLimitMb = None
        self.deliveryTrackingArchiverRotationTimeTresholdSeconds = None

    def __repr__ (self):
        configurationStr = "shouldWriteLastAccessUpdates=" + str(self.shouldWriteLastAccessUpdates) + \
                           ", updatesFileRotationIntervalSec=" + str(self.updatesFileRotationIntervalSec) + \
                           ", expirationTimeDeltaSec=" + str(self.expirationTimeDeltaSec) + \
                           ", browniesProcessingIntervalSec=" + str(self.browniesProcessingIntervalSec) +  \
                           ", quotaLimit=" + str(self.quotaLimit) + \
                           ", quotaZeroDiskUsagePercent=" + str(self.quotaZeroDiskUsagePercent) + \
                           ", quotaNormalDiskUsagePercent=" + str(self.quotaNormalDiskUsagePercent) + \
                           ", shouldArchive=" + str(self.shouldArchive) + \
                           ", archiverOutDirSizeLimitGb=" + str(self.archiverOutDirSizeLimitGb) + \
                           ", archiverOutFileSizeLimitMb=" + str(self.archiverOutFileSizeLimitMb) + \
                           ", archiverBufferDirSizeLimitMb=" + str(self.archiverBufferDirSizeLimitMb) +  \
                           ", archiverRotationTimeTresholdSeconds=" + str(self.archiverRotationTimeTresholdSeconds) + \
                           ", shouldArchiveNoDeliveryTable=" + str(self.shouldArchiveNoDeliveryTable) + \
                           ", shouldArchiveDeliveryTrackingUpdatesToLine=" + str(self.shouldArchiveDeliveryTrackingUpdatesToLine) + \
                           ", deliveryTrackingArchiverOutDirSizeLimitGb=" + str(self.deliveryTrackingArchiverOutDirSizeLimitGb) + \
                           ", deliveryTrackingArchiverOutFileSizeLimitMb=" + str(self.deliveryTrackingArchiverOutFileSizeLimitMb) + \
                           ", deliveryTrackingArchiverBufferDirSizeLimitMb=" + str(self.deliveryTrackingArchiverBufferDirSizeLimitMb) +  \
                           ", deliveryTrackingArchiverRotationTimeTresholdSeconds=" + str(self.deliveryTrackingArchiverRotationTimeTresholdSeconds)

        return configurationStr


class Muncher (object):
    """Muncher is in-charge of cleaning brownies from disk."""

     #---- Ctor -----------------------------------#
    def __init__ (self):

        self._logGeneral = None
        self._logIo = None
        self._keepRunning = True
#        self._updateConfiguration = False

        #------ Data structures -----------------------------#
        # Key: brownie id (brownie's file name)
        # Value: {'expiration', 'cid'}
        self._browniesDict = dict()

        # A list holding new las access time for content (used by the ContentCleaner)
        # Key: cid
        # Value: expiration
        self._lastAccessTimeUpdatesDict = dict()
       
        #------ Configuration ----------#
        self._cfg = None
        self._brownieFilesExtensionPattern = None

        #------ Timing -----------------#
        self._lastTimeRotatedFile = None
        self._lastTimeProccessedBrownies = None
        self._lastTimeStartedToScanForNewBrownies = None

        #------ Io ---------------------#
        self._rotatingUpdatesFile = None
        self._archiver = None
        self._deliveryTrackingArchiver = None

        #------ State ------------------#
        self._reachedDiskUsageThreshold = False
        
        #------ Stats ------------------#
        self._stats = None 
        self._statsDir = None
        self._lastTimeSentStats = None

        #------ Delivery Tracking ------#
        self._deliveryTracking = None
        self._lastTimeDumpDeliveryTrackingTables = time.time() # Don't dump on sturtup

        #------ Counters ---------------#
        self.counters = {'numTotalBrowniesScanned':0,
                         'numTotalNewBrowniesAdded':0,
                         'numErrorReadingBrownieFiles':0,
                         'numMissingDataInBrownie':0,
                         'numMissingDataForUpdate':0,
                         'numCurrentBrowniesInDb':0,
                         'numErrorRemovingBrownie':0,
                         'numTotalBrowniesRemoved':0,
                         'numTotalLaeInDb':0,
                         'numTotalLaeUpdated':0,
                         'numReachedDiskUsageThreshold':0,
                         'numTotalUnusedExpairedBrownies':0,
                         # Delivery Tracking counters
                         'deliveryTrackingNumKeys':0,
                         'deliveryTrackingNoDeliveryTableSize':0,
                         'deliveryTrackingNumSessionsBornInWaitState':0,
                         'deliveryTrackingNumSessionsBornInActiveState':0,
                         'deliveryTrackingNumSessionsBornInIgnoredRedirectState':0,
                         'deliveryTrackingNumSessionsBecomeActiveState':0,
                         'deliveryTrackingNumSessionsBecomeIgnoredRedirectState':0,
                         'deliveryTrackingNumInvalidKeySessions':0,
                         'deliveryTrackingNumInvalidStateSessions':0,
                         'deliveryTrackingNumDeltaWritesSucceeded':0,
                         'deliveryTrackingNumDeltaWritesFailed':0,
                         'deliveryTrackingNumDeltaWritesNothingToDo':0,
                         'deliveryTrackingNumDeltaLinesWritten':0,
                         'deliveryTrackingAvgDeltaWriteTime':0,
                         'deliveryTrackingNumBlocked':0,
                         'deliveryTrackingNumSessionsBlockedInFloodProtection':0,
                         'deliveryTrackingNumSessionsBlockedOverSizeLimit':0,
                         'deliveryTrackingNumSessionsWhitelisted':0,
                         }


#--------------Public -------------------------------------------------------------------#   
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
        self._logGeneral = logger.createLogger(G_NAME_MODULE_MUNCHER, G_NAME_GROUP_MUNCHER_GENERAL)
        self._logIo =logger.createLogger(G_NAME_MODULE_MUNCHER, G_NAME_GROUP_MUNCHER_IO)


    
    def initCfg (self, cfg):
        """Init the muncher configuration.

        Init the muncher configuration. 
        This function shall be called before any other functions of the class

        Args:
            configuration: a configuration object specified in this module

        Returns:
            None

        Raises:
            None
        """
        self._cfg = cfg


    def initStatsDir(self, directory):
        """Init the muncher stats directory.

        Init the muncher stats directory.

        Args:
            directory: the processes stats directory

        Returns:
            None

        Raises:
            None
        """
        self._statsDir = directory


    def run (self):
        """Runs the munching process - the main loop.

        Runs the munching process.
        This function starts the muncher main loop.

        Args:
            None

        Returns:
            int: Number of new content files found

        Raises:
            None
        """
        return self._mainLoop()


    def stop(self):
        """Stops the muncher.

        Stops the muncher.
        This function will cause the muncher main loop to exit

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self._keepRunning = False


    def update(self):
        """Reload configuration.

        This function will cause the muncher to reload its configuration

        Args:
            None

        Returns:
            None

        Raises:
            None
        """

        """
        # Well - This is usually called from context of oscar_core, that curently don't have a logger.
        # It is usefull for UT env, and hopefully to oscar_core in the future.
        self._logGeneral("update-signal").notice("Got update signal")
        self._updateConfiguration = True
        """
        pass



#--------------Public for UT----------------------------------------------------------#

    def init (self):

        self._lastTimeStartedToScanForNewBrownies = time.time()
        self._brownieFilesExtensionPattern = '*.' + self._cfg.brownieFilesExtension
        self._quotaFileFullNamePath = os.path.join(self._cfg.browniesRootDir, self._cfg.quotaFileName)

        # Init the stats object
        if self._statsDir != None:
            self._stats = StatsCommOverFileClient("muncher", self._logGeneral)
            self._stats.init(self._statsDir)
        
        # Create the rotating file
        if self._cfg.shouldWriteLastAccessUpdates:
            self._rotatingUpdatesFile = a.infra.file.rotating_file.RotatingFile(self._logIo, self._cfg.lastAccessUpdatesOutputDir, "lau", a.infra.file.rotating_file.NO_ROTATE, 0, ".lau")
            if not self._rotatingUpdatesFile.open():
                self._logGeneral("open-rotating-file").error("failed to open rotating file at path '%s' - can't start the Muncher", self._cfg.lastAccessUpdatesOutputDir)
                return False

        """
        # In relax mode (i.e. on mini) we do not create archivers, since archivers take too much CPU.
        if a.infra.process.getIsRelaxMode():
            self._cfg.shouldArchive = False
            self._cfg.shouldArchiveNoDeliveryTable = False
            self._cfg.shouldArchiveDeliveryTrackingUpdatesToLine = False
            self._logGeneral("disable-all-archivers").notice("disable all archives due to relax mode (archivers take too much CPU)")
        """

        # Init the archiver
        if self._cfg.shouldArchive:
            # This is work-around for the buffer dir
            archiveBufferDir = os.path.realpath(self._cfg.archiverBufferDir)
            self._logGeneral("archiver-dir-init-info").notice("input dir given to archiver is: %s" , archiveBufferDir)
            self._archiver = a.infra.file.rotating_file_archiver.Archiver(
                logger=self._logIo,\
                inputDir=archiveBufferDir, \
                bufferDirSizeLimitInMB=self._cfg.archiverBufferDirSizeLimitMb, \
                outputDir=self._cfg.archiveOutputDir)

            self._archiver.setUseFixedFileSize(4096)
            self._archiver.setFileSizeThresholdMB(self._cfg.archiverOutFileSizeLimitMb)
            self._archiver.setOutputDirSizeLimitGB(self._cfg.archiverOutDirSizeLimitGb)
            self._archiver.setRotationTimeThersholdSeconds(self._cfg.archiverRotationTimeTresholdSeconds)

        # Create the delivery tracking archiver
        if self._cfg.shouldArchiveNoDeliveryTable or self._cfg.shouldArchiveDeliveryTrackingUpdatesToLine:
            archiveBufferDir = os.path.realpath(self._cfg.deliveryTrackingArchiverBufferDir)
            self._logGeneral("delivery-tracking-archiver-dir-init-info").notice("input dir given to delivery-tracking archiver is: %s. Output dir is %s" , \
                                                                                archiveBufferDir,
                                                                                self._cfg.deliveryTrackingArchiverOutputDir)
            self._deliveryTrackingArchiver = a.infra.file.rotating_file_archiver.Archiver(
                logger=self._logIo,\
                inputDir=archiveBufferDir, \
                bufferDirSizeLimitInMB=self._cfg.deliveryTrackingArchiverBufferDirSizeLimitMb, \
                outputDir=self._cfg.deliveryTrackingArchiverOutputDir)

        self.startArchivers()

        # Init the delivery tracking module
        self._deliveryTracking = DeliveryTracking(
            self._cfg.deliveryTrackingUpdatesToLineDir, 
            self._cfg.dataDir, self._cfg.confDir, self._cfg.tempDir, 
            self.counters, self._logGeneral, 
            self._deliveryTrackingArchiver)

        self.updateDeliveryTrackingConfig(startup=True)

        return True


    def updateDeliveryTrackingConfig (self, startup=False):

        # Update the configuration.
        # We need ot update the configuration even if the feature is disabled becasue we need to be 
        # able to call sendClearNoDeliveryTableCommand()
        # 
        self._deliveryTracking.updateConfig(
            self._cfg.deliveryTrackingWindowSizeSec,
            self._cfg.deliveryTrackingWindowNumFrames,
            self._cfg.deliveryTrackingMaxSessionKeys,
            self._cfg.deliveryTrackingMaxNoDeliveryTableSize,
            self._cfg.deliveryTrackingBlockTTLSec,
            self._cfg.deliveryTrackingShortBlockTTLSec,
            self._cfg.deliveryTrackingWhitelistFile,
            self._cfg.deliveryTrackingNewSessionIgnorePeriod,
            self._cfg.deliveryTrackingFloodProtectionEnabled,
            self._cfg.deliveryTrackingFloodProtectionWindowSizeSec,
            self._cfg.deliveryTrackingFloodProtectionWindowNumFrames,
            self._cfg.deliveryTrackingFloodProtectionRatio,
            self._cfg.deliveryTrackingMinSessionsToAllowProtection,
            self._cfg.shouldArchiveNoDeliveryTable,
            self._cfg.shouldArchiveDeliveryTrackingUpdatesToLine,
            self._cfg.deliveryTrackingArchiveTableInterval)


        if self._cfg.deliveryTrackingEnabled:

            if self._deliveryTrackingArchiver:
                # Init the delivery tracking archiver.
                self._deliveryTrackingArchiver.setUseFixedFileSize(4096)
                self._deliveryTrackingArchiver.setFileSizeThresholdMB(self._cfg.deliveryTrackingArchiverOutFileSizeLimitMb)
                self._deliveryTrackingArchiver.setOutputDirSizeLimitGB(self._cfg.deliveryTrackingArchiverOutDirSizeLimitGb)
                self._deliveryTrackingArchiver.setRotationTimeThersholdSeconds(self._cfg.deliveryTrackingArchiverRotationTimeTresholdSeconds)

            self._deliveryTracking.enable(startup)

        else:
            # If feature is disabled, we send a clear table command to Line
            self._logGeneral('delivery-tracking-disabled').info('Delivery tracking is disabled')
            self._deliveryTracking.disable()


    def loadNewBrownies (self):
        browniesLoadedCount = 0
        currentTime = time.time()
        
        # Walk in the directory tree
        mminParam = ((currentTime - self._lastTimeStartedToScanForNewBrownies) / 60) + 1
        findCommand = "find -L . -mmin -%(minutes)s -type f -name '%(filePattern)s'" % {'minutes':str(mminParam), 'filePattern':self._brownieFilesExtensionPattern}
        self._logGeneral('new-content-find-command').debug2('going to search for new files. command: %s', findCommand)

        self._lastTimeStartedToScanForNewBrownies = currentTime

        data = None
        try:
            process = subprocess.Popen(findCommand, shell=True, stdout=subprocess.PIPE, cwd=self._cfg.browniesRootDir, bufsize=65536)
            data = process.communicate()[0]
        except Exception as ex:
            self._logGeneral("cant-run-find").error("error trying to run 'find' command. exception: %s", ex)
            return 0
            
        if data == None:
            self._logGeneral("no-output-data").error("data from 'find' command is None.")
            return 0
      
        for brownieRelativeFileName in data.split('\n'):
            if len(brownieRelativeFileName)==0:
                self._logGeneral('end-of-data').debug4('len(line)==0. probebly got to the end of the data')
                break

            self.counters['numTotalBrowniesScanned'] += 1

            # Get the full file name path
            brownieFileFullNamePath = os.path.join(self._cfg.browniesRootDir,brownieRelativeFileName)
            brownieFileName = os.path.basename(brownieRelativeFileName)

            # Brownie id is the fileName itself without it's extension.
            brownieId = brownieFileName.split(".")[0]
      
            # Lets check if we already have this brownie id. if so don't do nothing - continue to the next brownie
            if brownieId in self._browniesDict:
                continue

            self.counters['numTotalNewBrowniesAdded'] += 1
            browniesLoadedCount +=1

            # Load the json and get the expiration time
            try:
                brownieData = a.infra.format.json.readFromFile(self._logIo, brownieFileFullNamePath)
            except Exception as ex:
                self.counters['numErrorReadingBrownieFiles'] += 1
                self._logGeneral("error-reading-brownie").error("can't get brownie data from file='%s'. exception=%s" , brownieFileFullNamePath, ex)
                self._logCorruptedBrownie(brownieFileFullNamePath)
                # This is a corrupted brownie. Let's remove it.
                try:
                    os.remove(brownieFileFullNamePath)
                except Exception as ex:
                    self._logIo("failed-remove-brownie1").error("failed to remove '%s'. exception=%s", brownieFileFullNamePath, ex)
                continue

            # Insert to disk the file's expiration time, cid
            if ('expireTimeSeconds' in brownieData) and ('contentFile' in brownieData):

                expiration = brownieData['expireTimeSeconds']
                cid = brownieData['contentFile']

                # We need the cid without the disk and the directories preffixes
                cid = cid.split(os.sep)[-1]

                # Delivery Tracking
                sessionState = None
                creationTimeSeconds = None
                if self._cfg.deliveryTrackingEnabled:

                    # Ignore acquisition brownies
                    acquisitionBrownie = False
                    creationTimeSeconds = brownieData.get('creationTimeSeconds')
                    if creationTimeSeconds is None:
                        if brownieData.get('isInvalid'):
                            # This is an acquisition brownie
                            acquisitionBrownie = True
                        else:
                            self._logGeneral("bad-brownie").error("Invalid brownie. No creation time but not an acquisition brownie. Brownie data %s", brownieData)

                    if not acquisitionBrownie and self._deliveryTracking.isUpdateNeeded(None, creationTimeSeconds):
                        sessionState = self._deliveryTracking.handleSession(brownieData, None)

                # Insert to the brownies dict
                self._browniesDict[brownieId] = {'expiration':expiration, 'cid':cid, 'brownieFileFullNamePath':brownieFileFullNamePath, 'sessionState':sessionState, 'creationTimeSeconds':creationTimeSeconds}
                self.counters['numCurrentBrowniesInDb'] += 1

                # Create an update if necessary
                if (self._cfg.shouldWriteLastAccessUpdates):
                    if ('metaFile' in brownieData) and ('diskNumber' in brownieData):
                       
                        # Insert new entry to the evet list if necessary
                        # If we already seen a brownie for this cid with later expiration time - don't update
                        shouldInsertOrUpdateToUpdatesDict = True
                        isUpdate = False
                        if cid in self._lastAccessTimeUpdatesDict:
                            isUpdate = True
                            if self._lastAccessTimeUpdatesDict[cid][KEY_LAST_ACCESS_TIME] >= expiration:
                                shouldInsertOrUpdateToUpdatesDict = False
                   
                        if shouldInsertOrUpdateToUpdatesDict:
                            # TODO - check with arnon what metaFile we get from brownie
                            self._lastAccessTimeUpdatesDict[cid] = {KEY_LAST_ACCESS_TIME:expiration, KEY_META_FILE_RELATIVE_PATH:brownieData['metaFile'], KEY_DISK_NUM:brownieData['diskNumber']}
                            if isUpdate:
                                self.counters['numTotalLaeUpdated'] += 1
                            else:
                                self.counters['numTotalLaeInDb'] += 1
                   
                    else:
                        self.counters['numMissingDataForUpdate'] += 1
                        self._logGeneral("error-reading-brownie").error("missing necessary brownie data for creating latsAccess update. file='%s'. brownieData:\n%s" % (brownieFileFullNamePath,brownieData))      

                    
            else:
                self.counters['numMissingDataInBrownie'] += 1
                self._logGeneral("error-reading-brownie").error("missing necessary brownie data. file='%s'. brownieData:\n%s" % (brownieFileFullNamePath,brownieData))               
 
        return browniesLoadedCount                



    def processBrownies(self):
        """ Process the brownies and remove the expired ones

        Returns:
            None

        Raises:
            None

        """
        browniesDeletedCount = 0
       
        currentTime = time.time()
        for brownieId, value in self._browniesDict.items():

            updateDeliveryTracking = False
            if self._cfg.deliveryTrackingEnabled:
                prevState = value['sessionState']
                creationTimeSeconds = value['creationTimeSeconds']
                updateDeliveryTracking = self._deliveryTracking.isUpdateNeeded(prevState, creationTimeSeconds)

            isExpired =  (currentTime > value['expiration'] + self._cfg.expirationTimeDeltaSec)

            if updateDeliveryTracking or isExpired:
                # Reload the json and see if expiration time has changed or it wait-state has changes
                brownieFileFullNamePath = value['brownieFileFullNamePath']

                brownieData = None
                try:
                    brownieData = a.infra.format.json.readFromFile(self._logIo, brownieFileFullNamePath)
                except Exception as ex:
                    self.counters['numErrorReadingBrownieFiles'] += 1
                    self._logIo("error-reading-brownie").error("can't get brownie data from file='%s'. exception=%s" ,brownieFileFullNamePath, ex)
                    self._logCorruptedBrownie(brownieFileFullNamePath)
                    # This is a corrupted brownie. Let's remove it.
                    try:
                        os.remove(brownieFileFullNamePath)
                    except Exception as ex:
                        self._logIo("failed-remove-brownie2").error("failed to remove '%s'. exception=%s", brownieFileFullNamePath, ex)
                    continue    

                if brownieData == None:
                    self._logIo("no-brownie-data").error("brownieData is None. file is %s", brownieFileFullNamePath)
                    continue

            # Delivery Tracking
            if updateDeliveryTracking:
                # If the delivery tracking told us that this session needs an update (basically - 
                # if it's still in wait-state), we pass it again to delivary tracking
                currState = self._deliveryTracking.handleSession(brownieData, prevState)
                value['sessionState'] = currState


            # Handle all the expired brownie
            if isExpired:
                cid = value['cid']                        
                shouldRemoveBrownie = False
                shouldSendLastAccessUpdate = False
                # Lets check if expiration time has changed
                brownieNewExpiration = brownieData['expireTimeSeconds']
                if brownieNewExpiration > value['expiration']:
                    shouldSendLastAccessUpdate = True
                    # Maybe even if it's changed, it's still expired
                    if currentTime > brownieNewExpiration + self._cfg.expirationTimeDeltaSec:
                        shouldRemoveBrownie = True
                    else:
                        # Not expired - we only update the db
                        self._browniesDict[brownieId]['expiration'] = brownieNewExpiration
                else:
                    shouldRemoveBrownie = True

                if (self._cfg.shouldWriteLastAccessUpdates and shouldSendLastAccessUpdate):
                    # TODO - check with arnon what metaFile we get from brownie
                    self._lastAccessTimeUpdatesDict[cid] = {KEY_LAST_ACCESS_TIME:brownieNewExpiration, KEY_META_FILE_RELATIVE_PATH:brownieData['metaFile'], KEY_DISK_NUM:brownieData['diskNumber']}

                if shouldRemoveBrownie:
                    # It's time to remove the brownie
                    # If broniw doesn't have the 'cid' key then it's an acquisition brownie which we don't want to archive. we just want to delete it.
                    shouldOnlyRemove = 'cid' not in brownieData
                    if self._handleExpiredBrownie(brownieFileFullNamePath, shouldOnlyRemove):
                        if ('wasUsed' in brownieData) and not (brownieData['wasUsed']):
                            # Log unused brownies
                            self._logGeneral("not-used-expaired-brownie").debug3("expaired brownie was not used. brownie content: %s", brownieData)
                            self.counters['numTotalUnusedExpairedBrownies'] += 1
                        self._browniesDict.pop(brownieId,0)
                        self.counters['numCurrentBrowniesInDb'] -= 1
                        self.counters['numTotalBrowniesRemoved'] += 1
                        browniesDeletedCount += 1
                    else:
                        self._logIo("failed-removing-brownie").error("failed removing brownie. brownieId=%s, file=%s, cid=%s" \
                                                                     % (brownieId, brownieFileFullNamePath, cid))
                        self.counters['numErrorRemovingBrownie'] += 1

        return browniesDeletedCount



    def writeUpdatesToFileAndRotateIfNeeded (self):
        
        currentTime = time.time()
        if self._lastTimeRotatedFile == None:
            self._lastTimeRotatedFile = currentTime
        else:
            if currentTime - self._lastTimeRotatedFile >= self._cfg.updatesFileRotationIntervalSec:
                self._lastTimeRotatedFile = currentTime            
                if self._cfg.shouldWriteLastAccessUpdates and (len(self._lastAccessTimeUpdatesDict) > 0):
                    rotate = False
                    if self._rotatingUpdatesFile.writeJsonFormat(self._lastAccessTimeUpdatesDict):
                        rotate = True 
                    else:
                        self._logIo("failed-dumping-updates").error("writeJsonFormat returned 'False'. updates will be discarded")
                    lauUpdatesDictSize = len(self._lastAccessTimeUpdatesDict)
                    self._lastAccessTimeUpdatesDict.clear()
                    self.counters['numTotalLaeInDb'] -= lauUpdatesDictSize
                    if rotate:
                        if not self._rotatingUpdatesFile.rotateNow():
                            self._logIo("failed-rotating-file").error("failed to rotate file")



    def updateQuota (self):

        # Get the file temp name
        quotaFileTempName = self._quotaFileFullNamePath + '.tmp'
        # Get the disk usage
        diskUsagePercent = self.getDiskUsage(self._cfg.browniesRootDir)

        # Calculate the quota
        currentQuota = 0
        # If we reached the threshold we need to check that we are below the lower threshold
        if self._reachedDiskUsageThreshold:
            if diskUsagePercent <= self._cfg.quotaNormalDiskUsagePercent:
                currentQuota = self._calcualteQuota()
                self._reachedDiskUsageThreshold = False
        else:
            if diskUsagePercent <= self._cfg.quotaZeroDiskUsagePercent:
                currentQuota = self._calcualteQuota()
            else:
                self._reachedDiskUsageThreshold = True
                self.counters['numReachedDiskUsageThreshold'] += 1
                self._logGeneral("reached-disk-threshold").warning("reached disk usage threshold. current=%s, threshold=%s" % (str(diskUsagePercent), str(self._cfg.quotaZeroDiskUsagePercent)))

        if currentQuota < 0:
            currentQuota = 0


        try:
            fileDescriptor = open(quotaFileTempName, 'w')
            fileDescriptor.write(str(currentQuota))
            fileDescriptor.close()
            os.rename(quotaFileTempName, self._quotaFileFullNamePath)
        except Exception as ex:
            self._logIo("error-writing-quota").error("error writing quota file='%s'. exception=%s", self._quotaFileFullNamePath, ex)

        return currentQuota, diskUsagePercent


    def _calcualteQuota (self):
        quota = self._cfg.quotaLimit - len(self._browniesDict) - int((QUOTA_MARGIN_PERCENT/100)*self._cfg.quotaLimit)
        return quota


    def getDiskUsage (self, workDirectory):
        """
        Get the disk usage for the fileSystem of the given workDirectory. Works only for linux.
        Raises exception if not linux
        returns:
            -float: diskUsage in precentage
        """

        if platform.system() == "Linux":
            # Get the statistics for the file system
            st = os.statvfs(workDirectory)
            # Calculate the current disk usage and compare to the diskUsageLimit argument
            DiskUsage = 100*(1-(float(st[statvfs.F_BAVAIL])/st[statvfs.F_BLOCKS]))
        else:
            self._logGeneral().error("not on linux. can't calculate disk usage")
            raise Exception("platformError","not linux")

        return DiskUsage


    def archiverThreadExceptionCallBack (self, exception):
        self._logGeneral("archvier-thread-exception").error("got exception '%s' from the archiver thread. exiting", exception)
        self.stop()
    

#--------------Only for UT-----------------------------------------------------------------------#                               
    def closeRotatingFile (self):
        if self._cfg.shouldWriteLastAccessUpdates:
            self._rotatingUpdatesFile.close()

    def initlastTimeRotatedFile (self):
        self._lastTimeRotatedFile = time.time()

    def getDeliveryTrackingForUnitTest (self):
        return self._deliveryTracking

#--------------Private-----------------------------------------------------------------------#
    def _mainLoop(self):

        while self._keepRunning:

            currentTime = time.time()
           
            # Send stats if needed
            sendStats = False
            if (self._lastTimeSentStats == None) or (currentTime - self._lastTimeSentStats >= self._cfg.statsReportingIntervalSec):
                sendStats = True
                self._lastTimeSentStats = currentTime
            
            if sendStats and self._keepRunning:
                self._logGeneral("main-loop-stats").debug3("sending stats counters")
                if self._cfg.deliveryTrackingEnabled and self._deliveryTracking:
                    self.counters['deliveryTrackingNumKeys'] = self._deliveryTracking.getNumKeys()
                    self.counters['deliveryTrackingNoDeliveryTableSize'] = self._deliveryTracking.getNoDeliveryTableSize()
                self._stats.send(self.counters)
            
            currentTime = time.time()

            # Dump Delivery Tracking table to disk
            if self._cfg.deliveryTrackingEnabled and self._keepRunning:
                # Save no delivery table to disk
                if (currentTime - self._lastTimeDumpDeliveryTrackingTables >= self._cfg.deliveryTrackingDumpTablesIntervalSec):
                    self._deliveryTracking.saveNoDeliveryTable()
                    self._lastTimeDumpDeliveryTrackingTables = currentTime

            currentTime = time.time()

            # Process brownies if needed
            proccessBrownies = False
            if (self._lastTimeProccessedBrownies == None) or (currentTime - self._lastTimeProccessedBrownies >= self._cfg.browniesProcessingIntervalSec):
                proccessBrownies = True
                self._lastTimeProccessedBrownies = currentTime
                
            if proccessBrownies and self._keepRunning:
                self._proccessBrownies()

            """
            if self._updateConfiguration and self._keepRunning:
            """
            # This is called on every loop interval. Interval depends on the sleep() interval
            if self._keepRunning:
                self._doUpdateConfiguration()
#                self._updateConfiguration = False

            if self._keepRunning and self._cfg.deliveryTrackingEnabled and self._deliveryTracking:
                self._doOscarCoreCommand()

            if self._keepRunning:
                time.sleep(0.5)

        self.closeRotatingFile()

        # Dump Delivery Tracking table to disk
        if self._cfg.deliveryTrackingEnabled:
            self._deliveryTracking.saveNoDeliveryTable()

        self.stopArchivers()
        return True


    def _doUpdateConfiguration (self):

        ok = True

        filename = os.path.join(self._cfg.tempDir, "muncher.cfg")
        if not os.path.exists(filename):
            return

        try:
            tempFilename = filename + ".tmp." + datetime.datetime.now().strftime("%Y%m%d-%H%M%S-%f")
            os.rename(filename, tempFilename)
            newCfg = a.infra.format.json.readFromFile(self._logGeneral, tempFilename)
        except (IOError, ValueError) as ex:
            self._logGeneral("error-load-cfg").error("Error in load configuration file %s. %s", tempFilename, ex)
            ok = False

        try:
            os.remove(tempFilename)
        except Exception as ex:
            self._logGeneral("error-remove-cfg").error("Error in remove configuration file %s. %s", tempFilename, ex)

        if not ok:
            return

        self._logGeneral("update-cfg").notice("Updating configuration from file %s", filename)

        # Merge the existing configuration with the new configuration
        for key in self._cfg.__dict__:
            if key in newCfg and newCfg[key] is not None:
                self._cfg.__dict__[key] = newCfg[key]

        # Re-initialize delivery tracking when we update configuration
        self.updateDeliveryTrackingConfig()


    def _proccessBrownies(self):
        # Load new brownies
        self.loadNewBrownies()

        # Proccess (and delete if necessary) brownies
        self.processBrownies()

        # Write last access time updates to file and rotate if needed
        self.writeUpdatesToFileAndRotateIfNeeded()

        # Write Delivery Tracking delta
        if self._cfg.deliveryTrackingEnabled:
            self._deliveryTracking.checkFloodProtection()
            self._deliveryTracking.writeNoDeliveryDelta()

        # Update the quota
        self.updateQuota()


    def startArchivers (self):
        #Start the archiver
        if self._cfg.shouldArchive and self._archiver:
            self._archiver.start(self.archiverThreadExceptionCallBack)

        #Start the delivery tracking archiver
        if (self._cfg.shouldArchiveNoDeliveryTable or self._cfg.shouldArchiveDeliveryTrackingUpdatesToLine) and self._deliveryTrackingArchiver:
            self._deliveryTrackingArchiver.start(self.archiverThreadExceptionCallBack)


    def stopArchivers (self):
        #Stop the archiver
        if self._archiver:
            self._archiver.stop()

        #Stop the delivery tracking archiver
        if self._deliveryTrackingArchiver:
            self._deliveryTrackingArchiver.stop()


    def _doOscarCoreCommand (self):
        filename = os.path.join(self._cfg.tempDir, "oscar-core-command")
        if os.path.exists(filename):
            try:
                data = a.infra.format.json.readFromFile(self._logIo, filename)
            except Exception as ex:
                self._logGeneral("read-oscar-command-error").error("Error in read oscar command file. %s", ex)

            os.remove(filename)

            command = data.get("command")
            if command and command == "clear":
                self._deliveryTracking.clearNoDeliveryTable()
            elif command and command == "remove-key":
                key = data.get("key")
                self._deliveryTracking.removeKey(key)
            else:
                self._logGeneral("oscar-command-error").error("Wrong syntax in oscar command file. %s", data)
    

    def _handleExpiredBrownie (self, brownieFileFullNamePath, shouldOnlyRemove):
        shouldRemove = True
        shouldCheckIfExists = False

        if not shouldOnlyRemove:
            if self._cfg.shouldArchive and self._archiver != None:
                shouldRemove = False
                self._logIo("archive-brownie").debug1("archiving file='%s'", brownieFileFullNamePath)
                try:
                    if not self._archiver.archiveFile(brownieFileFullNamePath):
                        shouldCheckIfExists = True
                except Exception as ex:
                    self._logIo("failed-archive-brownie").error("failed to archive file='%s'. exception=%s", brownieFileFullNamePath, ex)
                    shouldCheckIfExists = True

        if shouldCheckIfExists:
            if os.path.exists(brownieFileFullNamePath):
                shouldRemove = True 

        if shouldRemove:
            try:
                self._logIo("remove-brownie").debug1("removing file='%s'", brownieFileFullNamePath)
                os.remove(brownieFileFullNamePath)
            except Exception as ex:
                self._logIo("failed-remove-brownie").error("failed to remove file='%s'. exception=%s", brownieFileFullNamePath, ex)
                return False

        return True


    def _logCorruptedBrownie (self, brownieFileFullNamePath):
        # We will try to read a log this corrupted brownie
        brownieContent = ""
        try:
            brownieFD = open(brownieFileFullNamePath, 'r')
            # We will read max of 50000 chars from the file
            brownieContent = brownieFD.read(50000)
            self._logIo("log-corrupted-brownie-msg").notice("logging corrupted brownie. file='%s' content=%s", brownieFileFullNamePath, brownieContent)
        except Exception as ex:
            self._logIo("log-corrupted-brownie-fail").error("failed to read corrupted file='%s'. exception=%s", brownieFileFullNamePath, ex)
            return brownieContent

        return brownieContent

    
    

