
#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: royr
# 

import a.content.brownies.muncher 
import a.infra.format.json
import a.infra.process
import os

if  __package__ is None:
    G_NAME_MODULE_MUNCHER_APP = "unknown"
    G_NAME_GROUP_MUNCHER_APP_GENERAL = "unknown"
else:
    from . import G_NAME_MODULE_MUNCHER_APP
    from . import G_NAME_GROUP_MUNCHER_APP_GENERAL

class MuncherApp():

    # Consts use for the specificParams dictionary provided on "initspecificParams"
    SPECIFIC_PARAM_KEY_BROWNIES_ROOT_DIR="brownies-root-dir"
    SPECIFIC_PARAM_KEY_BROWNIES_FILES_EXTENSION = "brownies-files-extension"
    SPECIFIC_PARAM_KEY_LAST_ACCESS_UPDATES_OUTPUT_DIR = "last-access-update-output-dir"
    SPECIFIC_PARAM_KEY_QUOTA_FILE_NAME = "qouta-file-name"
    SPECIFIC_PARAM_KEY_DATA_DIR = "data-dir"
    SPECIFIC_PARAM_KEY_CONF_DIR = "donf-dir"
    SPECIFIC_PARAM_KEY_TEMP_DIR = "temp-dir"
    SPECIFIC_PARAM_KEY_DELETED_BROWNIES_ARCHIVE_DIR = "archive-dir"
    SPECIFIC_PARAM_KEY_ARCHIVER_BUFFER_DIR = SPECIFIC_PARAM_KEY_BROWNIES_ROOT_DIR
    SPECIFIC_PARAM_KEY_DELIVERY_TRACKING_ARCHIVER_DIR = "delivery-tracking-archiver-dir"
    SPECIFIC_PARAM_KEY_DELIVERY_TRACKING_ARCHIVER_BUFFER_DIR = SPECIFIC_PARAM_KEY_TEMP_DIR
    SPECIFIC_PARAM_KEY_DELIVERY_TRACKING_UPDATES_TO_LINE_DIR = "delivery-tracking-updates-to-line-dir"

    # Consts for sections/fields names in sys-param
    CONFIG_SECTION_MUNCHER_PARAMS = "muncher-params"
    CONFIG_VAR_BROWNIES_PROCESSING_INTERVAL_SEC = "brownies-processing-interval-sec"
    CONFIG_VAR_EXPIRATION_TIME_DELTA_SEC ="expiration-time-delta-sec"
    CONFIG_VAR_LAST_ACCESS_UPDATES_FILE_ROTATION_INTERVAL_SEC ="last-access-updates-files-rotation-interval"
    CONFIG_VAR_SHOULD_WRITE_LAST_ACCESS_UPDATES="write-last-access-updates"
    CONFIG_VAR_QUOTA_LIMIT = "quota-limit"
    CONFIG_VAR_QUOTA_ZERO_DISK_USAGE_PERCENT = "quota-zero-disk-usage-percent"
    CONFIG_VAR_QUOTA_NORMAL_DISK_USAGE_PERCENT = "qouta-normal-disk-usage-percent"
    CONFIG_VAR_STATS_UPDATES_INTERVAL_SEC = "stats-updates-interval-sec"
    # Archiver 
    CONFIG_VAR_SHOULD_ARCHIVE_BROWNIE_FILES = "archive-brownie-files"
    CONFIG_VAR_ARCHIVE_TOTAL_SIZE_GB = "archive-total-size-gb"
    CONFIG_VAR_ARCHIVE_FILE_SIZE_MB = "archive-file-size-mb"
    CONFIG_VAR_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB = "archiver-buffer-dir-size-limit-mb"
    CONFIG_VAR_ARCHIVER_ROTATION_TRESHOLD_SECONDS = "archiver-rotation-threshold-seconds"

    # Consts for sections/fields names in sys-param for delivery tracking
    CONFIG_SECTION_DELIVERY_TRACKING_PARAMS = "delivery-tracking"
    CONFIG_VAR_DELIVERY_TRACKING_ENABLED = "enabled"
    CONFIG_VAR_DELIVERY_TRACKING_BLOCK_TTL_SEC = "ttl"
    CONFIG_VAR_DELIVERY_TRACKING_SHORT_BLOCK_TTL_SEC = "short-ttl"
    CONFIG_VAR_DELIVERY_TRACKING_NEW_SESSION_IGNORE_PERIOD = "new-session-ignore-period"
    CONFIG_VAR_DELIVERY_TRACKING_MAX_SESSION_KEYS = "max-session-keys"
    CONFIG_VAR_DELIVERY_TRACKING_MAX_NO_DELIVERY_TABLE_SIZE = "max-no-delivery-table-size"
    CONFIG_VAR_DELIVERY_TRACKING_DUMP_TABLES_INTERVAL_SEC = "dump-tables-interval-sec"
    CONFIG_VAR_DELIVERY_TRACKING_WINDOW_SIZE_SEC = "window-size-sec"
    CONFIG_VAR_DELIVERY_TRACKING_WINDOW_NUM_FRAMES = "window-num-frames"
    CONFIG_VAR_DELIVERY_TRACKING_FLOOD_PROTECTION_ENABLED = "flood-protection-enabled"
    CONFIG_VAR_DELIVERY_TRACKING_FLOOD_PROTECTION_WINDOW_SIZE_SEC = "flood-protection-window-size-sec"
    CONFIG_VAR_DELIVERY_TRACKING_FLOOD_PROTECTION_WINDOW_NUM_FRAMES = "flood-protection-window-num-frames"
    CONFIG_VAR_DELIVERY_TRACKING_FLOOD_PROTECTION_RATIO = "flood-protection-ratio"
    CONFIG_VAR_DELIVERY_TRACKING_FLOOD_PROTECTION_MIN_SESSIONS = "min-sessions-to-allow-protection"
    CONFIG_VAR_DELIVERY_TRACKING_WHITELIST_FILE = "whitelist-file"
    # Delivery Tracking Archiver 
    CONFIG_VAR_SHOULD_ARCHIVE_NO_DELIVERY_TABLE = "archive-no-delivery-table"
    CONFIG_VAR_SHOULD_ARCHIVE_DELIVERY_TRACKING_UPDATES_TO_LINE = "archive-delivery-tracking-updates-to-line"
    CONFIG_VAR_DELIVERY_TRACKING_ARCHIVE_TABLE_INTERVAL = "delivery-tracking-archive-table-interval"
    CONFIG_VAR_DELIVERY_TRACKING_ARCHIVE_TOTAL_SIZE_GB = "delivery-tracking-archive-total-size-gb"
    CONFIG_VAR_DELIVERY_TRACKING_ARCHIVE_FILE_SIZE_MB = "delivery-tracking-archive-file-size-mb"
    CONFIG_VAR_DELIVERY_TRACKING_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB = "delivery-tracking-archiver-buffer-dir-size-limit-mb"
    CONFIG_VAR_DELIVERY_TRACKING_ARCHIVER_ROTATION_TRESHOLD_SECONDS = "delivery-tracking-archiver-rotation-threshold-seconds"

    # Default values for data in sys-param
    DEFAULT_BROWNIES_PROCESSING_INTERVAL_SEC = 1 # Changed from 5 sec for delivery tracking !
    DEFAULT_EXPIRATION_TIME_DELTA_SEC = 2
    DEFAULT_LAST_ACCESS_UPDATES_FILE_ROTATION_INTERVAL_SEC = 10
    DEFAULT_SHOULD_WRITE_LAST_ACCESS_UPDATES = True
    DEFAULT_QUOTA_LIMIT = 80000
    DEFAULT_QUOTA_ZERO_DISK_USAGE_PERCENT = 80
    DEFAULT_QUOTA_NORMAL_DISK_USAGE_PERCENT = 70
    DEFAULT_STATS_UPDATES_INTERVAL_SEC = 60                                                                        
    # Archiver 
    DEFAULT_SHOULD_ARCHIVE_BROWNIE_FILES = True
    DEFAULT_ARCHIVE_TOTAL_SIZE_GB = 20
    DEFAULT_ARCHIVE_FILE_SIZE_MB = 10
    DEFAULT_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB = 30
    DEFAULT_ARCHIVER_ROTATION_TRESHOLD_SECONDS = 3600

    # Default values for data in sys-param for delivery tracking
    DEFAULT_DELIVERY_TRACKING_ENABLED = True
    DEFAULT_DELIVERY_TRACKING_BLOCK_TTL_SEC = 3600 * 3 # 3 hours
    DEFAULT_DELIVERY_TRACKING_SHORT_BLOCK_TTL_SEC = 60 * 5 # 5 minutes
    DEFAULT_DELIVERY_TRACKING_WHITELIST_FILE = None
    DEFAULT_DELIVERY_TRACKING_NEW_SESSION_IGNORE_PERIOD = 2000
    DEFAULT_DELIVERY_TRACKING_MAX_SESSION_KEYS = 150000
    DEFAULT_DELIVERY_TRACKING_MAX_NO_DELIVERY_TABLE_SIZE = 200000
    DEFAULT_DELIVERY_TRACKING_DUMP_TABLES_INTERVAL_SEC = 60
    DEFAULT_DELIVERY_TRACKING_WINDOW_SIZE_SEC = 120
    DEFAULT_DELIVERY_TRACKING_WINDOW_NUM_FRAMES = 5
    DEFAULT_DELIVERY_TRACKING_FLOOD_PROTECTION_ENABLED = True
    DEFAULT_DELIVERY_TRACKING_FLOOD_PROTECTION_WINDOW_SIZE_SEC = 5
    DEFAULT_DELIVERY_TRACKING_FLOOD_PROTECTION_WINDOW_NUM_FRAMES = 5
    DEFAULT_DELIVERY_TRACKING_FLOOD_PROTECTION_RATIO = 0
    DEFAULT_DELIVERY_TRACKING_FLOOD_PROTECTION_MIN_SESSIONS = 1000
    # Delivery Tracking Archiver 
    DEFAULT_SHOULD_ARCHIVE_NO_DELIVERY_TABLE = True
    DEFAULT_SHOULD_ARCHIVE_DELIVERY_TRACKING_UPDATES_TO_LINE = True
    DEFAULT_DELIVERY_TRACKING_ARCHIVE_TOTAL_SIZE_GB = 1
    DEFAULT_DELIVERY_TRACKING_ARCHIVE_FILE_SIZE_MB = 10
    DEFAULT_DELIVERY_TRACKING_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB = 30
    DEFAULT_DELIVERY_TRACKING_ARCHIVER_ROTATION_TRESHOLD_SECONDS = 3600
    DEFAULT_DELIVERY_TRACKING_ARCHIVE_TABLE_INTERVAL = 3600

    def __init__ (self):
        self._muncher = a.content.brownies.muncher.Muncher()
        self._muncherCfg = None


    def _loadSpecificParams (self, specificParams, cfg):
        cfg.browniesRootDir = specificParams[self.SPECIFIC_PARAM_KEY_BROWNIES_ROOT_DIR]
        cfg.brownieFilesExtension = specificParams[self.SPECIFIC_PARAM_KEY_BROWNIES_FILES_EXTENSION]
        cfg.quotaFileName = specificParams[self.SPECIFIC_PARAM_KEY_QUOTA_FILE_NAME]
        cfg.lastAccessUpdatesOutputDir = specificParams[self.SPECIFIC_PARAM_KEY_LAST_ACCESS_UPDATES_OUTPUT_DIR]
        cfg.dataDir = specificParams[self.SPECIFIC_PARAM_KEY_DATA_DIR]
        cfg.confDir = specificParams[self.SPECIFIC_PARAM_KEY_CONF_DIR]
        cfg.tempDir = specificParams[self.SPECIFIC_PARAM_KEY_TEMP_DIR]
        cfg.archiveOutputDir = specificParams[self.SPECIFIC_PARAM_KEY_DELETED_BROWNIES_ARCHIVE_DIR]
        cfg.archiverBufferDir = specificParams[self.SPECIFIC_PARAM_KEY_ARCHIVER_BUFFER_DIR]

        # Delivery Tracking
        cfg.deliveryTrackingUpdatesToLineDir = specificParams[self.SPECIFIC_PARAM_KEY_DELIVERY_TRACKING_UPDATES_TO_LINE_DIR]
        cfg.deliveryTrackingArchiverOutputDir = specificParams[self.SPECIFIC_PARAM_KEY_DELIVERY_TRACKING_ARCHIVER_DIR]
        cfg.deliveryTrackingArchiverBufferDir = specificParams[self.SPECIFIC_PARAM_KEY_DELIVERY_TRACKING_ARCHIVER_BUFFER_DIR]

    def _loadSysParamsCfg (self, sysParamsCfg, cfg):

        cfg.shouldWriteLastAccessUpdates = sysParamsCfg.getBool(self.CONFIG_SECTION_MUNCHER_PARAMS,
                                                                self.CONFIG_VAR_SHOULD_WRITE_LAST_ACCESS_UPDATES,
                                                                self.DEFAULT_SHOULD_WRITE_LAST_ACCESS_UPDATES)

        cfg.quotaLimit = sysParamsCfg.getInt(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                             self.CONFIG_VAR_QUOTA_LIMIT, 
                                             self.DEFAULT_QUOTA_LIMIT)

        cfg.quotaZeroDiskUsagePercent = sysParamsCfg.getInt(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                            self.CONFIG_VAR_QUOTA_ZERO_DISK_USAGE_PERCENT, 
                                                            self.DEFAULT_QUOTA_ZERO_DISK_USAGE_PERCENT)

        cfg.quotaNormalDiskUsagePercent = sysParamsCfg.getInt(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                              self.CONFIG_VAR_QUOTA_NORMAL_DISK_USAGE_PERCENT, 
                                                              self.DEFAULT_QUOTA_NORMAL_DISK_USAGE_PERCENT)

        cfg.browniesProcessingIntervalSec = sysParamsCfg.getInt(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                                self.CONFIG_VAR_BROWNIES_PROCESSING_INTERVAL_SEC, 
                                                                self.DEFAULT_BROWNIES_PROCESSING_INTERVAL_SEC)

        cfg.expirationTimeDeltaSec = sysParamsCfg.getInt(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                         self.CONFIG_VAR_EXPIRATION_TIME_DELTA_SEC,  
                                                         self.DEFAULT_EXPIRATION_TIME_DELTA_SEC)

        cfg.eventsFileRotationIntervalSec = sysParamsCfg.getInt(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                                self.CONFIG_VAR_LAST_ACCESS_UPDATES_FILE_ROTATION_INTERVAL_SEC, 
                                                                self.DEFAULT_LAST_ACCESS_UPDATES_FILE_ROTATION_INTERVAL_SEC)

        cfg.statsReportingIntervalSec = sysParamsCfg.getInt(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                            self.CONFIG_VAR_STATS_UPDATES_INTERVAL_SEC, 
                                                            self.DEFAULT_STATS_UPDATES_INTERVAL_SEC)

        #-------------------------- Archiver config --------------------------------------------------------------------
      
        cfg.shouldArchive = sysParamsCfg.getBool(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                 self.CONFIG_VAR_SHOULD_ARCHIVE_BROWNIE_FILES, 
                                                 self.DEFAULT_SHOULD_ARCHIVE_BROWNIE_FILES)

        cfg.archiverOutDirSizeLimitGb = sysParamsCfg.getFloat(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                              self.CONFIG_VAR_ARCHIVE_TOTAL_SIZE_GB, 
                                                              self.DEFAULT_ARCHIVE_TOTAL_SIZE_GB)
       
        cfg.archiverOutFileSizeLimitMb = sysParamsCfg.getFloat(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                               self.CONFIG_VAR_ARCHIVE_FILE_SIZE_MB, 
                                                               self.DEFAULT_ARCHIVE_FILE_SIZE_MB)

        cfg.archiverBufferDirSizeLimitMb = sysParamsCfg.getInt(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                               self.CONFIG_VAR_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB, 
                                                               self.DEFAULT_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB)

        cfg.archiverRotationTimeTresholdSeconds = sysParamsCfg.getInt(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                                      self.CONFIG_VAR_ARCHIVER_ROTATION_TRESHOLD_SECONDS, 
                                                                      self.DEFAULT_ARCHIVER_ROTATION_TRESHOLD_SECONDS)

        #-------------------------- Delivery Tracking config -----------------------------------------------------------

        cfg.deliveryTrackingEnabled = sysParamsCfg.getBool(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                           self.CONFIG_VAR_DELIVERY_TRACKING_ENABLED, 
                                                           self.DEFAULT_DELIVERY_TRACKING_ENABLED)

        cfg.deliveryTrackingBlockTTLSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                              self.CONFIG_VAR_DELIVERY_TRACKING_BLOCK_TTL_SEC, 
                                                              self.DEFAULT_DELIVERY_TRACKING_BLOCK_TTL_SEC)

        cfg.deliveryTrackingShortBlockTTLSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                   self.CONFIG_VAR_DELIVERY_TRACKING_SHORT_BLOCK_TTL_SEC, 
                                                                   self.DEFAULT_DELIVERY_TRACKING_SHORT_BLOCK_TTL_SEC)

        cfg.deliveryTrackingWhitelistFile = sysParamsCfg.getString(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                   self.CONFIG_VAR_DELIVERY_TRACKING_WHITELIST_FILE, 
                                                                   self.DEFAULT_DELIVERY_TRACKING_WHITELIST_FILE)

        # The sys params container doesn't handle None values correctly
        if cfg.deliveryTrackingWhitelistFile == 'None':
            cfg.deliveryTrackingWhitelistFile = None

        cfg.deliveryTrackingNewSessionIgnorePeriod = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                         self.CONFIG_VAR_DELIVERY_TRACKING_NEW_SESSION_IGNORE_PERIOD, 
                                                                         self.DEFAULT_DELIVERY_TRACKING_NEW_SESSION_IGNORE_PERIOD)

        cfg.deliveryTrackingMaxSessionKeys = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                 self.CONFIG_VAR_DELIVERY_TRACKING_MAX_SESSION_KEYS, 
                                                                 self.DEFAULT_DELIVERY_TRACKING_MAX_SESSION_KEYS)

        cfg.deliveryTrackingMaxNoDeliveryTableSize = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                         self.CONFIG_VAR_DELIVERY_TRACKING_MAX_NO_DELIVERY_TABLE_SIZE, 
                                                                         self.DEFAULT_DELIVERY_TRACKING_MAX_NO_DELIVERY_TABLE_SIZE)

        cfg.deliveryTrackingDumpTablesIntervalSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                         self.CONFIG_VAR_DELIVERY_TRACKING_DUMP_TABLES_INTERVAL_SEC, 
                                                                         self.DEFAULT_DELIVERY_TRACKING_DUMP_TABLES_INTERVAL_SEC)

        cfg.deliveryTrackingWindowSizeSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                self.CONFIG_VAR_DELIVERY_TRACKING_WINDOW_SIZE_SEC, 
                                                                self.DEFAULT_DELIVERY_TRACKING_WINDOW_SIZE_SEC)

        cfg.deliveryTrackingWindowNumFrames = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                  self.CONFIG_VAR_DELIVERY_TRACKING_WINDOW_NUM_FRAMES, 
                                                                  self.DEFAULT_DELIVERY_TRACKING_WINDOW_NUM_FRAMES)

        cfg.deliveryTrackingFloodProtectionEnabled = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                         self.CONFIG_VAR_DELIVERY_TRACKING_FLOOD_PROTECTION_ENABLED, 
                                                                         self.DEFAULT_DELIVERY_TRACKING_FLOOD_PROTECTION_ENABLED)

        cfg.deliveryTrackingFloodProtectionWindowSizeSec = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                               self.CONFIG_VAR_DELIVERY_TRACKING_FLOOD_PROTECTION_WINDOW_SIZE_SEC, 
                                                                               self.DEFAULT_DELIVERY_TRACKING_FLOOD_PROTECTION_WINDOW_SIZE_SEC)

        cfg.deliveryTrackingFloodProtectionWindowNumFrames = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                                 self.CONFIG_VAR_DELIVERY_TRACKING_FLOOD_PROTECTION_WINDOW_NUM_FRAMES, 
                                                                                 self.DEFAULT_DELIVERY_TRACKING_FLOOD_PROTECTION_WINDOW_NUM_FRAMES)

        cfg.deliveryTrackingFloodProtectionRatio = sysParamsCfg.getFloat(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                         self.CONFIG_VAR_DELIVERY_TRACKING_FLOOD_PROTECTION_RATIO, 
                                                                         self.DEFAULT_DELIVERY_TRACKING_FLOOD_PROTECTION_RATIO)

        cfg.deliveryTrackingMinSessionsToAllowProtection = sysParamsCfg.getFloat(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                                 self.CONFIG_VAR_DELIVERY_TRACKING_FLOOD_PROTECTION_MIN_SESSIONS, 
                                                                                 self.DEFAULT_DELIVERY_TRACKING_FLOOD_PROTECTION_MIN_SESSIONS)

        #-------------------------- Delivery Tracking Archiver config --------------------------------------------------

        cfg.shouldArchiveNoDeliveryTable = sysParamsCfg.getBool(self.CONFIG_SECTION_MUNCHER_PARAMS, 
                                                 self.CONFIG_VAR_SHOULD_ARCHIVE_NO_DELIVERY_TABLE, 
                                                 self.DEFAULT_SHOULD_ARCHIVE_NO_DELIVERY_TABLE)

        cfg.shouldArchiveDeliveryTrackingUpdatesToLine = sysParamsCfg.getBool(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                              self.CONFIG_VAR_SHOULD_ARCHIVE_DELIVERY_TRACKING_UPDATES_TO_LINE,
                                                                              self.DEFAULT_SHOULD_ARCHIVE_DELIVERY_TRACKING_UPDATES_TO_LINE)

        # Fix a problem with mal-formed user-param template.
        tmpString = sysParamsCfg.getString(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                           self.CONFIG_VAR_DELIVERY_TRACKING_ARCHIVE_TABLE_INTERVAL,
                                           None)
        if tmpString == "<int>":
            cfg.deliveryTrackingArchiveTableInterval = self.DEFAULT_DELIVERY_TRACKING_ARCHIVE_TABLE_INTERVAL
        else:
            cfg.deliveryTrackingArchiveTableInterval = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                           self.CONFIG_VAR_DELIVERY_TRACKING_ARCHIVE_TABLE_INTERVAL,
                                                                           self.DEFAULT_DELIVERY_TRACKING_ARCHIVE_TABLE_INTERVAL)

        cfg.deliveryTrackingArchiverOutDirSizeLimitGb = sysParamsCfg.getFloat(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                              self.CONFIG_VAR_DELIVERY_TRACKING_ARCHIVE_TOTAL_SIZE_GB, 
                                                                              self.DEFAULT_DELIVERY_TRACKING_ARCHIVE_TOTAL_SIZE_GB)

        cfg.deliveryTrackingArchiverOutFileSizeLimitMb = sysParamsCfg.getFloat(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                               self.CONFIG_VAR_DELIVERY_TRACKING_ARCHIVE_FILE_SIZE_MB, 
                                                                               self.DEFAULT_DELIVERY_TRACKING_ARCHIVE_FILE_SIZE_MB)

        cfg.deliveryTrackingArchiverBufferDirSizeLimitMb = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                               self.CONFIG_VAR_DELIVERY_TRACKING_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB, 
                                                                               self.DEFAULT_DELIVERY_TRACKING_ARCHIVER_BUFFER_DIR_SIZE_LIMIT_MB)

        cfg.deliveryTrackingArchiverRotationTimeTresholdSeconds = sysParamsCfg.getInt(self.CONFIG_SECTION_DELIVERY_TRACKING_PARAMS, 
                                                                                      self.CONFIG_VAR_DELIVERY_TRACKING_ARCHIVER_ROTATION_TRESHOLD_SECONDS, 
                                                                                      self.DEFAULT_DELIVERY_TRACKING_ARCHIVER_ROTATION_TRESHOLD_SECONDS)

                                 

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

        self._logGeneral=logger.createLogger(G_NAME_MODULE_MUNCHER_APP, G_NAME_GROUP_MUNCHER_APP_GENERAL)
        self._muncher.initLogger(self._logGeneral)


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
        
        cfg = a.content.brownies.muncher.MuncherCfg()
        self._loadSpecificParams(specificParams, cfg)
        self._loadSysParamsCfg(sysParamsCfg, cfg)
        self._muncher.initCfg(cfg)
        self._muncherCfg = cfg


    def  daemonControlInitStats(self, statsDir):
        """
        Init Stats Dir
        """

        self._muncher.initStatsDir(statsDir)



    #-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStart(self):
        """launching the process"""
        if not self._muncher.init():
            a.infra.process.processFatal("Failed initializing muncher")

    #-----------------------------------------------------------------------------------------------------------------------
    def daemonControlRun(self):
        """getting into the main loop"""
        if not self._muncher.run():
            self._logGeneral("main-loop-false").error("muncher main loop returned false")
        else:
            self._logGeneral("done2").notice("process terminated")


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
        self._muncher.stop()


    def daemonControlCreateUpdateData (self, updateDir, sysParamsCfg, logger):
        """reload configuration

        This function is called in the context of oscar core before sending a SIGHUP so the process.
        It is responsible to create the update information (taken from sys params) and store it in a file
        accessible to the process
         
        Args:
            sysParamsCfg: a contatiner holding the sys params base configuration (that are destined to move to blinky)

        Returns:
            None

        Raises:
            None
        """

        # TODO(amiry) - The logger that oscar_core give us is currently a dummy logger,
        #               so no logging will be done until a logger is available in oscar_core

        cfg = a.content.brownies.muncher.MuncherCfg()
        self._loadSysParamsCfg(sysParamsCfg, cfg)

        try:
            filename = os.path.join(updateDir, "muncher.cfg")
            a.infra.format.json.writeToFile(logger, cfg.__dict__, filename)
        except (IOError, TypeError) as ex:
            logger("error-write-cfg").error("Error in write configuration file %s. %s", filename, ex)
        


    def daemonControlUpdate (self):
        """reload configuration

        This function is called from a context of signal handling. just set a flag to reload configuration
        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self._muncher.update()

