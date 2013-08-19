#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import threading
import os
from a.infra.basic.return_codes import ReturnCodes
from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogArchiveModeType
from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import DestinationType
import a.infra.file.std_archiver
from a.infra.time.poll_supervisor import PollSupervisor
from a.infra.file.rotating_file_size_enforcer import RotatingFileSizeEnforcer

if  __package__ is None:
    G_NAME_MODULE_SYS_LOG_HOUSEKEEPER = "unknown"
    G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_DESTINATION_ARCHIVER_ACT = "unknown"
    G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_DESTINATION_ARCHIVER_CFG = "unknown"
    G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_MASTER = "unknown"
    G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_COLLECTION = "unknown"
    G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_CFG = "unknown"
else:
    from . import G_NAME_MODULE_SYS_LOG_HOUSEKEEPER
    from . import G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_DESTINATION_ARCHIVER_ACT
    from . import G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_DESTINATION_ARCHIVER_CFG
    from . import G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_MASTER
    from . import G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_COLLECTION
    from . import G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_CFG



class InfraLoggerDestinationArchiver(object):
    _FILE_STD_STRUCTORE_MARKER = "%(rotation)s" #temprarily here, till python logger will need it also

    def __init__ (self, logger, destinationName):
        self._logAct=logger.createLogger(G_NAME_MODULE_SYS_LOG_HOUSEKEEPER, 
                                      G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_DESTINATION_ARCHIVER_ACT, 
                                      instance=destinationName)
        self._logCfg=logger.createLogger(G_NAME_MODULE_SYS_LOG_HOUSEKEEPER, 
                                         G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_DESTINATION_ARCHIVER_CFG, 
                                         instance=destinationName)
        self._destinationName = destinationName
        self._configurationLock = threading.RLock()
        self._configErrorMsgFunctor = None
        self._destinationData = None
        self._destinationOutputData = None
        self._runningDestinationData = None
        self._runningDestinationOutputData = None
        self._candidateDestinationData = None
        self._candidateDestinationOutputData = None
        self._shallStopFunctor = None

    def initConfigMsgFunctor(self, configErrorMsgFunctor):
        self._configErrorMsgFunctor = configErrorMsgFunctor

    def initStopFlagFunctor (self, shallStopFunctor):
        self._shallStopFunctor = shallStopFunctor

    def getDestinationName (self):
        return self._destinationName

    def configStartTransaction (self):
        self._logCfg("config-start-transaction").debug2("called")
        self._candidateDestinationData = self._runningDestinationData
        self._candidateDestinationOutputData = self._runningDestinationOutputData
        return ReturnCodes.kOk

    def preparePrivateLoggerDestinationValueSet(self, destinationData):
        self._logCfg("prepare-private").debug2("called, data=%s", destinationData) 
        self._candidateDestinationData = destinationData   
        return ReturnCodes.kOk

    def preparePrivateLoggerDestinationOutputValueSet(self, outputData):
        self._logCfg("prepare-private").debug2("called, data=%s", outputData)  
        self._candidateDestinationOutputData = outputData
        return ReturnCodes.kOk

    def configPreparePrivateAfter (self):
        fileNamePrefix = self._candidateDestinationOutputData.fileBaseName
        splitted = fileNamePrefix.split(self._FILE_STD_STRUCTORE_MARKER)
        if len(splitted) > 2:
            self._cfgError("File base name can include maximum one '%s' segment", self._FILE_STD_STRUCTORE_MARKER)
            return ReturnCodes.kGeneralError
        if (self._candidateDestinationOutputData.archiveMode != LogArchiveModeType.kNone) and (len(splitted) < 2):
            self._cfgError("File base name does include a '%s' segment - this is required for archive method which is not 'none", 
                           self._FILE_STD_STRUCTORE_MARKER)
            return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

    def configCommitTransaction (self):
        self._logCfg("config-commit-transaction").debug2("called")
        with self._configurationLock:            
            self._runningDestinationData = self._candidateDestinationData
            self._runningDestinationOutputData = self._candidateDestinationOutputData
        self._candidateDestinationData = None
        self._candidateDestinationOutputData = None
        return ReturnCodes.kOk

    def configAbortTransaction (self):
        self._logCfg("config-abort-transaction").debug2("called")
        self._candidateDestinationData = None
        self._candidateDestinationOutputData = None
        return ReturnCodes.kOk

    def commitPrivateLoggerDestinationOutputValueSet(self, outputData):        
        self._logCfg("commit-private").debug2("called, data=%s", outputData)
        self._runningDestinationOutputData = outputData
        return ReturnCodes.kOk

    def abortPrivateLoggerDestinationOutputValueSet(self, outputData):        
        self._logCfg("abort-private").debug2("called, data=%s", outputData)
        return ReturnCodes.kOk

    def archive(self, doBeforeEachFile, doAfterEachFile):
        #return an error class in case of failure, retrun code will be the number of archived files o.w.
        with self._configurationLock:     
            self._destinationData = self._runningDestinationData
            self._destinationOutputData = self._runningDestinationOutputData      

        if self._destinationData is None:
            self._logAct("archive-no-data").error("Archive function is called but destination data was not set")
            return ReturnCodes.kGeneralError
        if self._destinationOutputData is None:
            self._logAct("archive-no-data").error("Archive function is called but destination output data was not set")
            return ReturnCodes.kGeneralError

        compressionMethod = None
        if self._destinationOutputData.archiveMode == LogArchiveModeType.kNone:
            self._logAct("nothing-to-do").debug1("Archive mode is none. nothing to do")
            return ReturnCodes.kOk
        elif self._destinationOutputData.archiveMode == LogArchiveModeType.kNoCompression:
            compressionMethod = a.infra.file.std_archiver.StdArchiver.COMPRESSION_METHOD_NONE
        elif self._destinationOutputData.archiveMode == LogArchiveModeType.kGzipStandard:
            compressionMethod = a.infra.file.std_archiver.StdArchiver.COMPRESSION_METHOD_GZIP
        elif self._destinationOutputData.archiveMode == LogArchiveModeType.kGzipBest:
            compressionMethod = a.infra.file.std_archiver.StdArchiver.COMPRESSION_METHOD_GZIP_BEST
        elif self._destinationOutputData.archiveMode == LogArchiveModeType.kGzipFast:
            compressionMethod = a.infra.file.std_archiver.StdArchiver.COMPRESSION_METHOD_GZIP_FAST
        elif self._destinationOutputData.archiveMode == LogArchiveModeType.kBz2Standard:
            compressionMethod = a.infra.file.std_archiver.StdArchiver.COMPRESSION_METHOD_BZ2
        elif self._destinationOutputData.archiveMode == LogArchiveModeType.kBz2Best:
            compressionMethod = a.infra.file.std_archiver.StdArchiver.COMPRESSION_METHOD_BZ2_BEST
        elif self._destinationOutputData.archiveMode == LogArchiveModeType.kBz2Fast:
            compressionMethod = a.infra.file.std_archiver.StdArchiver.COMPRESSION_METHOD_BZ2_FAST
    
        if compressionMethod == None:
            self._logAct("unknown-archive-mode").error("Unknown archive mode: %s", self._destinationOutputData.archiveMode)
            return ReturnCodes.kGeneralError

        fileNameSuffix = None
        if self._destinationData.destinationType   == DestinationType.kText:
            fileNameSuffix = ".txt"
        elif self._destinationData.destinationType == DestinationType.kTextCsv:
            fileNameSuffix = ".csv"
        elif self._destinationData.destinationType == DestinationType.kTextSingleLine:
            fileNameSuffix = ".txt"
        elif self._destinationData.destinationType == DestinationType.kBinary:
            fileNameSuffix = ".qbl"

        if fileNameSuffix == None:
            self._logAct("unknown-destination-type").error("Unknown destination type mode: %s", self._destinationData.destinationType)
            return ReturnCodes.kGeneralError

        fileDirectory = self._destinationOutputData.fileDirectory
        fileNamePrefix = self._destinationOutputData.fileBaseName
        splitted = fileNamePrefix.split(self._FILE_STD_STRUCTORE_MARKER)
        if len(splitted)!=2:
            self._logAct("invlalid-file-name").error("Invalid file name: '%s'. not supporting phases", 
                                                  self._destinationData.destinatiofileNamePrefix)

        fileNamePrefix = splitted[0]
        fileNameSuffix = splitted[1]+fileNameSuffix

        fileBaseNamePattern = RotatingFileSizeEnforcer.s_getDefaultBaseNamePattern(fileNamePrefix, fileNameSuffix, True)
        fileBaseNameGlobPattern = RotatingFileSizeEnforcer.s_calcFilesGlobPattern(fileBaseNamePattern, RotatingFileSizeEnforcer.PHASE_PENDING)

        def renameFunc (fileBaseName):
            ret = RotatingFileSizeEnforcer.s_getFileNameRemovePhase(fileBaseNamePattern, fileBaseName)
            if ret is None:
                self._logAct("failed-translate-file").error("Failed to remove the phase from file name %s",  fileBaseName)
                return fileBaseName#best we can do
            return ret

        
        archiver = a.infra.file.std_archiver.StdArchiver(self._logAct, fileDirectory, fileBaseNameGlobPattern)
        rc = archiver.initTargetFileNameConversion(renameFunc)
        if not rc.success():
            self._logAct("failed-init-archiver-nc").error("Failed to init the archiver name conversion")
            return ReturnCodes.kGeneralError
        rc = archiver.initCompression(compressionMethod, True)
        if not rc.success():
            self._logAct("failed-init-archiver-c").error("Failed to init the archiver compression method")
            return ReturnCodes.kGeneralError
        rc = archiver.initDeleteEmptyFiles()
        if not rc.success():
            self._logAct("failed-init-archiver-de").error("Failed to init the archiver empty files deletion")
            return ReturnCodes.kGeneralError

        archiver.setStopFlagFunctor(self._shallStopFunctor)
        rc = archiver.initDone()
        if not rc.success():
            self._logAct("failed-init-archiver-do").error("Failed to init done the archiver")
            return ReturnCodes.kGeneralError

        rc = archiver.archive(doBeforeEachFile=doBeforeEachFile, doAfterEachFile=doAfterEachFile)
        if not rc.success():
            self._logAct("failed-archive").error("Failed to archive the files")
            return ReturnCodes.kGeneralError

        return rc#also holds the number of archived files

    def _cfgError (self, msg, *args):
        self._logCfg("cfg-errot").debug2(msg, args)
        try:
            self._configErrorMsgFunctor(msg%args)
        except:
            self._logCfg("failed-error-msg").exception("Failed ot send the error message to the user")



class InfraLoggerHousekeeper(object):

    _SCAN_DIRS_POLL_SUPERVISOR_KEY = "scan-dir"
    _ARCHIVE_FILE_POLL_SUPERVISOR_KEY = "archive-file"

    def __init__ (self, logger):
        self._logCollection=logger.createLogger(G_NAME_MODULE_SYS_LOG_HOUSEKEEPER, 
                                                G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_COLLECTION)
        self._logMaster=logger.createLogger(G_NAME_MODULE_SYS_LOG_HOUSEKEEPER, 
                                             G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_COLLECTION)
        self._logCfg=logger.createLogger(G_NAME_MODULE_SYS_LOG_HOUSEKEEPER, 
                                         G_NAME_GROUP_SYS_LOG_HOUSEKEEPER_CFG)
        self._pollSupervisor = PollSupervisor(self._logMaster, "house-keeper", pollCycleLogString="poll cycle")
        self._pollSupervisor.addPollElement([self._SCAN_DIRS_POLL_SUPERVISOR_KEY], "directory-scan")
        self._pollSupervisor.addPollElement([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY], 
                                            "file archiving")
        self._configurationLock = threading.RLock()        
        self._runningHousekeeperData = None
        self._runningHousekeeperThresholdData = None
        self._runningArchivingData = None
        self._runningArchivingThresholdData = None
        self._runningDestinationArchivers = {}
        self._candidateHousekeeperData = None
        self._candidateHousekeeperThresholdData = None
        self._candidateArchivingData = None
        self._candidateArchivingThresholdData = None
        self._candidateDestinationArchivers = None
        self._actualHousekeeperData = None
        self._actualHousekeeperThresholdData = None
        self._actualArchivingThresholdData = None
        self._actualDestinationArchivers = None
        self._singlePengingFileCount = 0
        self._singlePengingFileCountCheckpoint = 0
        self._pengingFilesCountWarnings = 0
        self._pengingFilesCountWarningsCheckpoint = 0
        self._pengingFilesCountErrors = 0
        self._pengingFilesCountErrorsCheckpoint = 0
        self._isFirstRealPoll = True
        self._wasDisabled = True

    def initConfigMsgFunctor(self, configErrorMsgFunctor):
        self._configErrorMsgFunctor = configErrorMsgFunctor

    def initStopFlagFunctor (self, shallStopFunctor):
        """provide a functor that we will stop our operation if it returned True or failed
        """
        self._shallStopFunctor = shallStopFunctor

    def _cfgError (self, msg, *args):
        self._logCfg("cfg-errot").debug2(msg, args)
        try:
            self._configErrorMsgFunctor(msg%args)
        except:
            self._logCfg("failed-error-msg").exception("Failed ot send the error message to the user")


    def configStartTransaction (self):
        self._logCfg("config-start-transaction").debug2("called")
        self._candidateHousekeeperData = self._runningHousekeeperData
        self._candidateHousekeeperThresholdData = self._runningHousekeeperThresholdData
        self._candidateArchivingData = self._runningArchivingData
        self._candidateArchivingThresholdData = self._runningArchivingThresholdData
        self._candidateDestinationArchivers = self._runningDestinationArchivers
        for destArchiver in self._candidateDestinationArchivers:
            self._candidateDestinationArchivers[destArchiver].configStartTransaction()
        return ReturnCodes.kOk


    def preparePrivateHousekeeperData (self, housekeeperData):        
        self._logCfg("prepare-private-housekeeper-data").debug2("got candidate housekeeper data = %s", 
                                                                housekeeperData)
        self._candidateHousekeeperData = housekeeperData
        return ReturnCodes.kOk

    def preparePrivateHousekeeperThresholdData (self, housekeeperThData):        
        self._logCfg("prepare-private-housekeeper-th-data").debug2("got candidate housekeeper threshold data = %s", 
                                                                   housekeeperThData)
        self._candidateHousekeeperThresholdData = housekeeperThData
        return ReturnCodes.kOk

    def preparePrivateArchivingData (self, archivingData):        
        self._logCfg("prepare-private-archiving-housekeeper-data").debug2("got candidate archiving data = %s", 
                                                                          archivingData)
        self._candidateArchivingData = archivingData
        return ReturnCodes.kOk

    def preparePrivateArchivingThresholdData (self, archivingThData):        
        self._logCfg("prepare-private-archiving-th-data").debug2("got candidate archiving threshold data = %s", 
                                                                 archivingThData)
        self._candidateArchivingThresholdData = archivingThData
        return ReturnCodes.kOk


    def preparePrivateDestinationArchiversListCreate(self, loggerClass, loggerInstance, loggerDestination):
        self._logCfg("prepare-private-dest-list-create").debug2("create destination archiver, listKey = (%s, %s, %s)", 
                                                                loggerClass, loggerInstance, loggerDestination)
        destArchiver = InfraLoggerDestinationArchiver(self._logCfg, 
                                                      "/".join([loggerClass, loggerInstance, loggerDestination]))
        destArchiver.initConfigMsgFunctor(self._configErrorMsgFunctor)
        destArchiver.initStopFlagFunctor(self._shallStopFunctor)
        self._candidateDestinationArchivers[(loggerClass, loggerInstance, loggerDestination)] = destArchiver
        return destArchiver

    def preparePrivateDestinationArchiversListDelete(self, loggerClass, loggerInstance, loggerDestination):
        self._logCfg("prepare-private-dest-list-delete").debug2("delete destination archiver, listKey = (%s, %s, %s)", 
                                                                loggerClass, loggerInstance, loggerDestination)
        if not (loggerClass, loggerInstance, loggerDestination) in self._candidateDestinationArchivers:
            self._logCfg("delete-no-exists").warning("removing a none existing destingation (%s, %s, %s)",
                                                     loggerClass, loggerInstance, loggerDestination)
        else:
            self._candidateDestinationArchivers.pop((loggerClass, loggerInstance, loggerDestination))
        return ReturnCodes.kOk

    def configAbortTransaction (self):
        self._logCfg("config-abort-transaction").debug2("configuration transaction aborted")
        self._candidateHousekeeperData = None
        self._candidateHousekeeperThresholdData = None
        self._candidateArchivingData = None
        self._candidateArchivingThresholdData = None
        for destArchiver in self._candidateDestinationArchivers:
            self._candidateDestinationArchivers[destArchiver].configAbortTransaction()
        self._candidateDestinationArchivers = {}
        return ReturnCodes.kOk


    def configPreparePrivateAfter (self):
        self._logCfg("config-prepare-private-after").debug2("called")      
        __pychecker__="no-maxreturns=25"
        if self._candidateHousekeeperData is None:
            self._cfgError("missing houskeeper data")
            return ReturnCodes.kGeneralError

        if self._candidateHousekeeperThresholdData is None:
            self._cfgError("missing houskeeper threshold data")
            return ReturnCodes.kGeneralError

        if self._candidateArchivingData is None:
            self._cfgError("missing log archiving data")
            return ReturnCodes.kGeneralError

        if self._candidateArchivingThresholdData is None:
            self._cfgError("missing log archiving threshold data")
            return ReturnCodes.kGeneralError

        if self._candidateHousekeeperData.pollInterval<0:
            self._cfgError("poll interval '%d' is invalid. must not be negative", 
                          self._candidateHousekeeperData.pollInterval)
            return ReturnCodes.kGeneralError

        if self._candidateHousekeeperThresholdData.pollLatencyErrorSeconds<0:
            self._cfgError("poll latency error threshold '%d' is invalid. cannot be negative", 
                          self._candidateHousekeeperThresholdData.pollLatencyErrorSeconds)
            return ReturnCodes.kGeneralError

        if self._candidateHousekeeperThresholdData.pollLatencyWarningSeconds<0:
            self._cfgError("poll latency warning threshold '%d' is invalid. cannot be negative", 
                          self._candidateHousekeeperThresholdData.pollLatencyWarningSeconds)
            return ReturnCodes.kGeneralError

        if self._candidateHousekeeperThresholdData.pollLatencyErrorSeconds != 0 and \
            self._candidateHousekeeperThresholdData.pollLatencyWarningSeconds != 0 and\
            self._candidateHousekeeperThresholdData.pollLatencyWarningSeconds >= self._candidateHousekeeperThresholdData.pollLatencyErrorSeconds:
            self._cfgError("poll latency warning threshold '%d' is not smaller than the error threshold '%d'", 
                           self._candidateHousekeeperThresholdData.pollLatencyWarningSeconds,
                           self._candidateHousekeeperThresholdData.pollLatencyErrorSeconds)
            return ReturnCodes.kGeneralError

        if self._candidateHousekeeperData.pollInterval > 0 and \
            self._candidateHousekeeperThresholdData.pollLatencyErrorSeconds != 0 and \
            self._candidateHousekeeperThresholdData.pollLatencyErrorSeconds > self._candidateHousekeeperData.pollInterval:
            self._cfgError("poll latency error threshold '%d' is larger than the poll interval threshold '%d'", 
                           self._candidateHousekeeperThresholdData.pollLatencyErrorSeconds,
                           self._candidateHousekeeperData.pollInterval)
            return ReturnCodes.kGeneralError

        if self._candidateHousekeeperData.pollInterval > 0 and \
            self._candidateHousekeeperThresholdData.pollLatencyWarningSeconds != 0 and \
            self._candidateHousekeeperThresholdData.pollLatencyWarningSeconds > self._candidateHousekeeperData.pollInterval:
            self._cfgError("poll latency warning threshold '%d' is larger than the poll interval threshold '%d'", 
                           self._candidateHousekeeperThresholdData.pollLatencyWarningSeconds,
                           self._candidateHousekeeperData.pollInterval)
            return ReturnCodes.kGeneralError

        
        if self._candidateArchivingThresholdData.pendingFileCountError<0:
            self._cfgError("pending files count error threshold '%d' is invalid. cannot be negative", 
                          self._candidateArchivingThresholdData.pendingFileCountError)
            return ReturnCodes.kGeneralError

        if self._candidateArchivingThresholdData.pendingFileCountWarning<0:
            self._cfgError("pending files count warning threshold '%d' is invalid. cannot be negative", 
                          self._candidateArchivingThresholdData.pendingFileCountWarning)
            return ReturnCodes.kGeneralError

        if self._candidateArchivingThresholdData.pendingFileCountError != 0 and \
            self._candidateArchivingThresholdData.pendingFileCountWarning != 0 and\
            self._candidateArchivingThresholdData.pendingFileCountWarning >= self._candidateArchivingThresholdData.pendingFileCountError:
            self._cfgError("pending files count warning threshold '%d' is not smaller than the error threshold '%d'", 
                           self._candidateArchivingThresholdData.pendingFileCountWarning,
                           self._candidateArchivingThresholdData.pendingFileCountError)
            return ReturnCodes.kGeneralError

        if self._candidateArchivingThresholdData.fileArchiveDurationErrorSeconds<0:
            self._cfgError("file archive duration error threshold '%d' is invalid. cannot be negative", 
                          self._candidateArchivingThresholdData.fileArchiveDurationErrorSeconds)
            return ReturnCodes.kGeneralError

        if self._candidateArchivingThresholdData.fileArchiveDurationWarningSeconds<0:
            self._cfgError("file archive duration warning threshold '%d' is invalid. cannot be negative", 
                          self._candidateArchivingThresholdData.fileArchiveDurationWarningSeconds)
            return ReturnCodes.kGeneralError

        if self._candidateArchivingThresholdData.fileArchiveDurationErrorSeconds != 0 and \
            self._candidateArchivingThresholdData.fileArchiveDurationWarningSeconds != 0 and\
            self._candidateArchivingThresholdData.fileArchiveDurationWarningSeconds >= self._candidateArchivingThresholdData.fileArchiveDurationErrorSeconds:
            self._cfgError("file archive duration warning threshold '%d' is not smaller than the error threshold '%d'", 
                           self._candidateArchivingThresholdData.fileArchiveDurationWarningSeconds,
                           self._candidateArchivingThresholdData.fileArchiveDurationErrorSeconds)
            return ReturnCodes.kGeneralError

        if self._candidateArchivingThresholdData.overallArchiveDurationErrorSeconds<0:
            self._cfgError("overall archive duration error threshold '%d' is invalid. cannot be negative", 
                          self._candidateArchivingThresholdData.overallArchiveDurationErrorSeconds)
            return ReturnCodes.kGeneralError

        if self._candidateArchivingThresholdData.overallArchiveDurationWarningSeconds<0:
            self._cfgError("overall archive duration warning threshold '%d' is invalid. cannot be negative", 
                          self._candidateArchivingThresholdData.overallArchiveDurationWarningSeconds)
            return ReturnCodes.kGeneralError

        if self._candidateArchivingThresholdData.overallArchiveDurationErrorSeconds != 0 and \
            self._candidateArchivingThresholdData.overallArchiveDurationWarningSeconds != 0 and\
            self._candidateArchivingThresholdData.overallArchiveDurationWarningSeconds >= self._candidateArchivingThresholdData.overallArchiveDurationErrorSeconds:
            self._cfgError("overall archive duration warning threshold '%d' is not smaller than the error threshold '%d'", 
                           self._candidateArchivingThresholdData.overallArchiveDurationWarningSeconds,
                           self._candidateArchivingThresholdData.overallArchiveDurationErrorSeconds)
            return ReturnCodes.kGeneralError

        for destArchiver in self._candidateDestinationArchivers:
            rc = self._candidateDestinationArchivers[destArchiver].configPreparePrivateAfter()
            if not rc.success():
                self._logCfg("dest-config-prepare-private-after-fail").debug1("failure in destination")                
                return rc
        self._logCfg("config-prepare-private-after-done").debug1("Done")                
        return ReturnCodes.kOk


    def configPreparePublicAfter (self):
        self._logCfg("config-prepare-public-after").debug2("called")       
        return ReturnCodes.kOk


    def configCommitTransaction (self):
        self._logCfg("config-commit-transaction").debug2("called")
        with self._configurationLock:            
            self._runningHousekeeperData = self._candidateHousekeeperData
            self._runningHousekeeperThresholdData = self._candidateHousekeeperThresholdData
            self._runningArchivingData = self._candidateArchivingData
            self._runningArchivingThresholdData = self._candidateArchivingThresholdData
            for destArchiver in self._candidateDestinationArchivers:
                self._candidateDestinationArchivers[destArchiver].configCommitTransaction()
            self._runningDestinationArchivers = self._candidateDestinationArchivers
            self._candidateHousekeeperData = None
            self._candidateHousekeeperThresholdData = None
            self._candidateArchivingThresholdData = None
            self._candidateDestinationArchivers = None
        return ReturnCodes.kOk

    def getHousekeeperCountersOperData(self, trxContext, countersData):                
        self._logCfg("get-housekeeper-counters-oper-data-called").debug3("called with trxContext = %s, countersData = %s", trxContext, countersData)
        countersData.setPolls(self._pollSupervisor.getPollCycleCounter(PollSupervisor.COUNTER_POLLS))
        countersData.setPollsMissed(self._pollSupervisor.getPollCycleCounter(PollSupervisor.COUNTER_MISSED_POLLS))
        countersData.setPollLatencyWarnings(self._pollSupervisor.getPollCycleCounter(PollSupervisor.COUNTER_LATENCY_WARNINGS))
        countersData.setPollLatencyErrors(self._pollSupervisor.getPollCycleCounter(PollSupervisor.COUNTER_LATENCY_ERRORS))
        countersData.setTotalSeconds(self._pollSupervisor.getPollCycleCounter(PollSupervisor.COUNTER_TOTAL_NANO_SECONDS)/1000/1000/1000)
        countersData.setActiveSeconds(self._pollSupervisor.getPollCycleCounter(PollSupervisor.COUNTER_ACTIVE_NANO_SECONDS)/1000/1000/1000)
        self._logCfg("get-housekeeper-counters-oper-data-done").debug3("returned counters-oper-data=%s", countersData)
        return ReturnCodes.kOk     

    def getArchivingCountersOperData(self, trxContext, countersData):                
        self._logCfg("get-archiving-counters-oper-data-called").debug3("called with trxContext = %s, countersData = %s", trxContext, countersData)
        countersData.setArchivedFiles (self._pollSupervisor.getElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_SUCCESS))
        countersData.setArchivedErrors (self._pollSupervisor.getElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_FAILURES))
        countersData.setFileArchiveDurationErrors (self._pollSupervisor.getElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_DURATION_ERRORS))
        countersData.setFileArchiveDurationWarning (self._pollSupervisor.getElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_DURATION_WARNINGS))        
        countersData.setOverallArchiveDurationErrors (self._pollSupervisor.getPollCycleCounter(PollSupervisor.COUNTER_DURATION_ERRORS))
        countersData.setOverallArchiveDurationWarning (self._pollSupervisor.getPollCycleCounter(PollSupervisor.COUNTER_DURATION_WARNINGS))
        countersData.setPendingFileCountErrors (self._pengingFilesCountErrors - self._pengingFilesCountErrorsCheckpoint)
        countersData.setPendingFileCountWarning (self._pengingFilesCountWarnings - self._pengingFilesCountWarningsCheckpoint)
        countersData.setOnePendingFile (self._singlePengingFileCount - self._singlePengingFileCountCheckpoint)
        countersData.setDirScans (self._pollSupervisor.getElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_POLLS))
        countersData.setDirScansErrors (self._pollSupervisor.getElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_FAILURES))
        countersData.setActiveSeconds(self._pollSupervisor.getElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_ACTIVE_NANO_SECONDS)/1000/1000/1000)

        self._logCfg("get-archiving-counters-oper-data-done").debug3("returned counters-oper-data=%s", countersData)
        return ReturnCodes.kOk     

    def clearHousekeeperCounters(self):                
        self._logCfg("clear-housekeeper-counters").debug1("clear housekeeper counters")
        self._pollSupervisor.clearPollCycleCounter(PollSupervisor.COUNTER_POLLS)
        self._pollSupervisor.clearPollCycleCounter(PollSupervisor.COUNTER_MISSED_POLLS)
        self._pollSupervisor.clearPollCycleCounter(PollSupervisor.COUNTER_LATENCY_WARNINGS)
        self._pollSupervisor.clearPollCycleCounter(PollSupervisor.COUNTER_LATENCY_ERRORS)
        self._pollSupervisor.clearPollCycleCounter(PollSupervisor.COUNTER_TOTAL_NANO_SECONDS)
        self._pollSupervisor.clearPollCycleCounter(PollSupervisor.COUNTER_ACTIVE_NANO_SECONDS)
        return ReturnCodes.kOk     

    def clearArchivingCounters(self):                
        self._logCfg("clear-archiving-counters").debug1("clear archiving counters")
        self._pollSupervisor.clearElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_SUCCESS)
        self._pollSupervisor.clearElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_FAILURES)
        self._pollSupervisor.clearElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_DURATION_ERRORS)
        self._pollSupervisor.clearElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_DURATION_WARNINGS)
        self._pollSupervisor.clearPollCycleCounter(PollSupervisor.COUNTER_DURATION_ERRORS)
        self._pollSupervisor.clearPollCycleCounter(PollSupervisor.COUNTER_DURATION_WARNINGS)
        self._pengingFilesCountErrorsCheckpoint = self._pengingFilesCountErrors
        self._pengingFilesCountWarningsCheckpoint = self._pengingFilesCountWarnings
        self._singlePengingFileCountCheckpoint = self._singlePengingFileCount 
        self._pollSupervisor.clearElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_POLLS)
        self._pollSupervisor.clearElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_FAILURES)
        self._pollSupervisor.clearElementPollCounter([self._SCAN_DIRS_POLL_SUPERVISOR_KEY], PollSupervisor.COUNTER_TOTAL_NANO_SECONDS)        
        return ReturnCodes.kOk     


    def poll (self):
        self._logMaster("poll").debug5("poll")
        with self._configurationLock:
            if self._runningHousekeeperData is None:
                #configuration is yet to be loaded
                self._logMaster("no-cfg").debug3("configuration is yet to be loaded")
                return

            pollRateChanged = False
            if not self._isFirstRealPoll:
                pollRateChanged = self._actualHousekeeperData.pollInterval!=self._runningHousekeeperData.pollInterval

            self._actualHousekeeperData = self._runningHousekeeperData
            self._actualHousekeeperThresholdData = self._runningHousekeeperThresholdData
            self._actualThresholdData = self._runningArchivingData
            self._actualArchivingThresholdData = self._runningArchivingThresholdData
            self._actualDestinationArchivers = self._runningDestinationArchivers
            
        if not self._actualHousekeeperData.enabled:
            self._wasDisabled = True
            self._logMaster("disabled").debug4("poll skipped - is disabled")
            return 

        if self._actualHousekeeperData.pollInterval == 0:
            self._wasDisabled = True
            self._logMaster("disabled2").debug4("poll skipped - interval is 0")
            return 

        wasDisabled = self._wasDisabled
        self._wasDisabled = False

        #configuring the poll rest of the supervisor data anyhow, it is built to it
        self._pollSupervisor.setPollCycleInterval(self._actualHousekeeperData.pollInterval)
        self._pollSupervisor.setPollCycleLatencyThresholds(self._actualHousekeeperThresholdData.pollLatencyErrorSeconds,
                                                           self._actualHousekeeperThresholdData.pollLatencyWarningSeconds)
        self._pollSupervisor.setPollCycleDurationThresholds(self._actualArchivingThresholdData.overallArchiveDurationErrorSeconds,
                                                            self._actualArchivingThresholdData.overallArchiveDurationWarningSeconds)
        self._pollSupervisor.setElementPollDurationThresholds(
            [self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY], 
            self._actualArchivingThresholdData.fileArchiveDurationErrorSeconds,
            self._actualArchivingThresholdData.fileArchiveDurationWarningSeconds)

        if self._isFirstRealPoll:
            self._isFirstRealPoll = False
            self._pollSupervisor.startPollCycle()
        elif wasDisabled or pollRateChanged:
            self._logMaster("restarting-time").debug2("restarting the interval timer")
            self._pollSupervisor.forceStart()
        elif not self._pollSupervisor.isTimeToStartPollCycle():#normal state
            self._logMaster("not-time-yet").debug4("skipp poll - time has not come")
            return
        else:
            self._pollSupervisor.startPollCycle()

        self._logMaster("working-time").debug2("working time!")
        
        for destinationArchiverKey in self._actualDestinationArchivers:
            destinationArchiver = self._actualDestinationArchivers[destinationArchiverKey]
            if self._shallStopFunctor is not None:
                try:
                    shallStop = self._shallStopFunctor()
                    if shallStop:
                        self._logMaster("shall-stop").debug1("The stop funcor returned True. stopping")
                        break
                except:
                    self._logMaster("shall-stop-fail").exception("The shall stop functor failed. stopping")
                    break

            self._pollSupervisor.startElementPoll([self._SCAN_DIRS_POLL_SUPERVISOR_KEY], str(destinationArchiverKey))
            def doBeforeArchive (sourceDir, sourceFileName, targetDir, targetFileName):
                self._logMaster("do-before").debug4("called doBeforeArchive on destination '%s': %s, %s, %s, %s",
                                                    destinationArchiver.getDestinationName(), 
                                                    sourceDir, sourceFileName, targetDir, targetFileName)
                self._pollSupervisor.startElementPoll([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY],
                                                     os.path.join(sourceDir, sourceFileName))

            def doAfterArchive (returnCode):
                self._logMaster("do-after").debug4("called doAfterArchive on destination '%s': %s",
                                                   str(destinationArchiverKey), 
                                                   returnCode)
                self._pollSupervisor.endElementPoll([self._SCAN_DIRS_POLL_SUPERVISOR_KEY, self._ARCHIVE_FILE_POLL_SUPERVISOR_KEY],
                                                    returnCode)

            self._logMaster("working-dest").debug3("working on destination %s", 
                                                   str(destinationArchiverKey))

            rc = destinationArchiver.archive(doBeforeEachFile=doBeforeArchive, doAfterEachFile=doAfterArchive)
            self._pollSupervisor.endElementPoll([self._SCAN_DIRS_POLL_SUPERVISOR_KEY], rc)

            if rc.getValue() == 1:
                self._singlePengingFileCount += 1

            if self._actualArchivingThresholdData.pendingFileCountError!=0 and \
                rc.getValue() >= self._actualArchivingThresholdData.pendingFileCountError:
                self._logMaster("pending-file-count-e").error("Archiver dealt with many files at once (%d) when working on %s", 
                                                              rc.getValue(), str(destinationArchiverKey))
                self._pengingFilesCountErrors += 1

            elif self._actualArchivingThresholdData.pendingFileCountWarning!=0 and \
                rc.getValue() >= self._actualArchivingThresholdData.pendingFileCountWarning:
                self._logMaster("pending-file-count-w").warning("Archiver dealt with many files at once (%d) when working on %s", 
                                                                rc.getValue(), str(destinationArchiverKey))
                self._pengingFilesCountWarnings += 1

        self._pollSupervisor.endPollCycle()
        self._logMaster("round-done").debug2("round done")

