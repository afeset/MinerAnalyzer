
# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: amiry

# TODO(amiry) - This file should move to another namespace.

if  __package__ is None:
    G_NAME_GROUP_CDN_REPORTER = "unknown"
else:
    from . import G_NAME_GROUP_CDN_REPORTER


import time, os, glob, subprocess
import a.infra.format.json
from a.infra.file.rotating_file_size_enforcer import RotatingFileSizeEnforcer
import a.infra.file.rotating_file_archiver
import topper_record_utils
import a.infra.process
import a.api.user_log.msg.export

class CdnReporter (object):

    def __init__ (self, name):
        self._name = name
        self._enabled = False
        self._analytics = False
        self._logDir = None
        self._log = None
        self._tranRotatingFile = None
        self._tranFileName = None
        self._metaFileName = None
        self._tranFile = None
        self._fileOpenTime = None
        self._rotationSizeKB = None
        self._rotationTimeSec = None
        self._unsentQueueMaxSizeMB = None
        self._metaFlushIntervalSec = None
        self._lastTimeMetaUpdate = None
        self._urlTranslationEnabled = None

        self._unsentArchiveDir = None
        self._metaArchiveDir = None
        self._unsentArchiveMaxSizeGB = None
        self._metaArchiveMaxSizeGB = None
        self._unsentArchiver = None
        self._metaArchiver = None

        self._counters = {
            "cgid": {},
            "logDirSizeMB": 0
            }

        self._cgidCurrMeta = {}
        self._checkRotationCnt = 0


    def initLogger (self, logger):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_CDN_REPORTER)


    def init (self, cfg):
        if not self._updateConfig(cfg):
            self._log("error-init").warning("Error init CDN reporter %s", self._name)
            return False
        return True


    def disable (self):
        self._log("cfg-disable").notice("Disable CDN integration %s", self._name)
        self._closeTranAndMetaFile()
        self._clearOutQueue()
        self._stopArchivers()


    def terminate (self):
        self._log("terminate").notice("Terminate CDN integration %s", self._name)
        self._closeTranAndMetaFile()
        self._stopArchivers()


    def getCounters (self):
        self._getTotalDirSizeMB() # Update the "logDirSizeMB" counter
        return self._counters


    def _updateConfig (self, cfg):
        enabled = cfg.get("enabled")
        logDir = cfg.get("logdir")
        self._rotationTimeSec = cfg.get("rotationTimeSec")
        self._rotationSizeKB = cfg.get("rotationSizeKB")
        self._unsentQueueMaxSizeMB = cfg.get("unsentQueueMaxSizeMB")
        self._metaFlushIntervalSec = cfg.get("metaFlushIntervalSec")
        unsentArchiveDir = cfg.get("unsentArchiveDir")
        metaArchiveDir = cfg.get("metaArchiveDir")
        unsentArchiveMaxSizeGB = cfg.get("unsentArchiveMaxSizeGB")
        metaArchiveMaxSizeGB = cfg.get("metaArchiveMaxSizeGB")
        self._urlTranslationEnabled = cfg.get("urlTranslation")
        self._analytics = cfg.get("analytics")

        if self._analytics:
            self._log("analytics-mode").notice("CDN reporter %s running in analytics mode", self._name)

        if enabled:
            # Rename old tmp files (in case of crash recovery) before we open the new file
            self._handleOldTmpFiles(logDir)
    
            # Check if log dir changed. Need to create a new rotating file
            if self._logDir and self._logDir != logDir:
                self._log("log-dir-changed").notice("Log dir for CDN reporter %s changed", self._name)
    
                # Close and rename the currently opened file
                self._closeTranAndMetaFile()
                self._tranRotatingFile = None

            self._logDir = logDir
    
            if not self._tranRotatingFile:
                self._tranRotatingFile = RotatingFileSizeEnforcer(self._log, self._logDir, "tran-"+self._name+"-", ".log")
                self._tranRotatingFile.initFileRotatingPattern(
                    "%s.%s" % (RotatingFileSizeEnforcer.KICK_NUM_4, RotatingFileSizeEnforcer.EPOCH_SECONDS_10))
    
                # Instead of setting max size on the rotating file pattern, we enforce the size limit ourselves.
                # We will not write new log files if the filder size reaced max size.
                # Instead, we will pass the tmp fils directly into the unsent files archive.
                # This is because the unsent files may be opened and can't be deleted.
                self._tranRotatingFile.prepare()

            # Restart archivers if needed
            if unsentArchiveDir != self._unsentArchiveDir or \
                metaArchiveDir != self._metaArchiveDir or \
                unsentArchiveMaxSizeGB != self._unsentArchiveMaxSizeGB or \
                metaArchiveMaxSizeGB != self._metaArchiveMaxSizeGB:

                self._unsentArchiveDir = unsentArchiveDir
                self._metaArchiveDir = metaArchiveDir
                self._unsentArchiveMaxSizeGB = unsentArchiveMaxSizeGB
                self._metaArchiveMaxSizeGB = metaArchiveMaxSizeGB
                self._startArchivers()

        if self._enabled and not enabled:
            # Disable integration
            self.disable()
            self._enabled = False

        if not self._enabled and enabled:
            # Enable integration
            if self._rotateFile():
                self._log("cfg-enable").notice("Enabled CDN integration %s", self._name)
                self._enabled = True
            else:
                self._log("cfg-enable-error").notice("Error enabling CDN integration %s", self._name)

        return True


    def _openTranAndMetaFile (self):
        # Close the file if it was opened
        self._closeTranAndMetaFile()
        if self._tranFile:
            self._log("file-close-before-open-error").error("Can't open new transactoin log file. Error closing prev. Name %s", self._tranFileName)
            return False

        # Get the new file name
        self._tranRotatingFile.rotate()
        tranFileName = self._tranRotatingFile.getCurrentFileName() + ".tmp"
        metaFileName = tranFileName[:-8] + ".meta"
        self._cgidCurrMeta = {}

        try:
            self._tranFile = open(tranFileName, "wt", buffering=1)
        except IOError as ex:
            self._log("file-open-error").warning("Error opening transaction file %s. %s", tranFileName, ex)
            return False

        self._log("file-opened").notice("Transaction log file opened. Name %s, Meta %s", tranFileName, metaFileName)
        self._fileOpenTime = time.time()
        self._tranFileName = tranFileName
        self._metaFileName = metaFileName
        self._numTransactionsInCurrFile = 0
        return True


    def _closeTranAndMetaFile (self):

        closed = False

        try:
            if self._tranFile:
                self._tranFile.close()
                self._updateMetaFile()
                self._tranFile = None
                closed = True
        except IOError as ex:
            self._log("tran-ile-close-error").error("Error closing transaction file. Name %s. %s", self._tranFileName, ex)
            return

        if not closed:
            return

        # Check if we should push the file to the log queue. The total size includes the current file.
        totalSizeMB = self._getTotalDirSizeMB()
        if totalSizeMB < self._unsentQueueMaxSizeMB:
            self._log("file-closed").debug1("Transaction log file closed. Rename to %s", self._tranFileName[:-4])
            self._pushToOutQueue(self._tranFileName)
        else:
            # Archive file in unsent archive
            self._log("max-log-queue").notice("Log queue size limit exceeded. Unsent file %s archived. Unsent meta file %s archived", 
                                              self._tranFileName, self._metaFileName)
            a.infra.process.logUserMessage(a.api.user_log.msg.export.QueueFull(self._name, self._numTransactionsInCurrFile))
            self._archiveFile(self._tranFileName, self._unsentArchiver)

        # Archive meta file in meta archive
        self._archiveFile(self._metaFileName, self._metaArchiver)


    def _rotateFile (self):
        self._closeTranAndMetaFile()
        self._tranRotatingFile.rotate()
        if self._openTranAndMetaFile():
            return True
        return False


    def _shouldRotate (self):
        rotateBySize = None
        rotateByTime = None

        try:
            fileSize = os.path.getsize(self._tranFileName) / 1024
        except Exception as ex:
            self._log("getsize-error").error("Error getting tran file size. File %s. %s" % (self._tranFileName, ex))
            # Recover. Open a new file
            self._openTranAndMetaFile()
            return False

        if fileSize > self._rotationSizeKB:
            self._log("rotate-by-size").debug1("Should rotate by size. %d > %d" % (fileSize, self._rotationSizeKB))
            rotateBySize = True
        else:
            now = time.time()
            if now - self._fileOpenTime > self._rotationTimeSec:
                self._log("rotate-by-time").debug1("Should rotate by size. %d > %d" %(now - self._fileOpenTime, self._rotationTimeSec))
                rotateByTime = True

        return (rotateBySize or rotateByTime)


    def _getTotalDirSizeMB (self):
        totalSize = 0
        if not self._logDir or not os.path.exists(self._logDir):
            return 0

        for dirpath, dirnames, filenames in os.walk(self._logDir):
            for f in filenames:
                # We only want to count ".bz" files
                if len(f) > 4 and f[-4:] == '.bz2':
                    fp = os.path.join(dirpath, f)
                    totalSize += os.path.getsize(fp)
        totalSizeMB = totalSize / (1024.0*1024.0)
        self._counters["logDirSizeMB"] = int(totalSizeMB)
        return totalSizeMB


    def _updateStatsCounters (self, cgid, downloadedContentBytes):
        # Update the total stats counters
        self._updatePerCgidData(self._counters["cgid"], cgid, downloadedContentBytes)
        # Update the meta counters (reset per meta file)
        self._updatePerCgidData(self._cgidCurrMeta, cgid, downloadedContentBytes)

        # Update meta file once in a while
        currentTime = time.time()
        if (self._lastTimeMetaUpdate == None) or (currentTime - self._lastTimeMetaUpdate >= self._metaFlushIntervalSec):
            # Update time even if we fail. Don't want to try on every transaction
            self._lastTimeMetaUpdate = currentTime
            self._updateMetaFile()


    def _updatePerCgidData (self, aDict, cgid, volume):
        perCgidData = aDict.get(cgid)
        if perCgidData is None:
            aDict[cgid] = {"count":1, "volume":volume}
        else:
            aDict[cgid]["count"] += 1
            aDict[cgid]["volume"] += volume


    def _updateMetaFile (self):
        try:
            a.infra.format.json.writeToFile(self._log, self._cgidCurrMeta, self._metaFileName)
        except Exception as ex:
            self._log("error-update-mata").error("Error updating meta file %s. Data %s. %s" % (self._metaFileName, self._cgidCurrMeta, ex))


    def _handleOldTmpFiles (self, logDir):

        # TODO(amiry) - Since this is done very early in the init process, 
        # it is a little difficult to properly handle handle old tmp files properly. 
        # Currently we just delete them

        self._killPattern(logDir, "tran-*.log")
        self._killPattern(logDir, "tran-*.log.tmp")
        self._killPattern(logDir, "tran-*.log.meta")


    def _killPattern (self, logDir, pattern):
        fileList = glob.glob(os.path.join(logDir, pattern))
        for fileName in fileList:
            fileName = os.path.join(logDir, fileName)
            self._log("delete-old-tmp-file").debug1("Delete old tmp file %s" % fileName)
            try:
                os.unlink(fileName)
            except Exception as ex:
                self._log("error-delete").error("Error deleting file %s. %s" % (fileName, ex))


    def _clearOutQueue (self):

        # TODO(amiry) - It is possible that archiving will fail because logpusher sent this file already.

        fileList = glob.glob(os.path.join(self._logDir, "tran-*.log.bz2"))
        for fileName in fileList:
            self._log("clear-out-queue").notice("Clear log queue: archive unsent file %s" % fileName)
            self._archiveFile(fileName, self._unsentArchiver)


    def _pushToOutQueue (self, tmpFileName):

        logFileName = tmpFileName[:-4]

        try:
            # Remove the ".tmp" suffix
            os.rename(tmpFileName, logFileName) 
        except Exception as ex:
            self._log("rename-tmp-file-failed").error("Error renaming tmp file %s. %s" % (tmpFileName, ex))
            return

        # We compress the files ourselves instead of letting logpusher doing that.
        # This is bacause
        # 1. Logpusher's bad behaviour in case of connectivity problem. (Keeps finding and compressing the same 
        #    file over and over again)
        # 2. Maintain a smaller pickup queue. Do not assume that logpusher failed to compress.
        self._log("bzip-log-file").debug1("bzip2 %s" % logFileName)
        subprocess.call("bzip2 %s" % logFileName, shell=True)

        if os.path.exists(logFileName):
            self._log("bzip-error").warning("Error bzipping file %s. Delete file" % logFileName)
            os.unlink(logFileName)
        else:
            self._log("pushed").info("File pushed to log queue %s" % logFileName)

        """
        try:
            # And remove the log file
            os.unlink(logFileName)
        except Exception as ex:
            self._log("rename-tmp-file-failed").error("Error removing log file %s. %s" % (logFileName, ex))
        """


    def _archiveFile (self, fileName, archiver):

        shouldCheckIfExists = False
        shouldRemove = False

        try:
            if not archiver.archiveFile(fileName):
                shouldCheckIfExists = True
        except Exception as ex:
            self._log("failed-archive").error("Failed to archive file '%s'. exception %s", fileName, ex)
            shouldCheckIfExists = True

        if shouldCheckIfExists:
            if os.path.exists(fileName):
                shouldRemove = True 

        if shouldRemove:
            try:
                self._log("remove-file").debug1("Remove file '%s'", fileName)
                os.remove(fileName)
            except Exception as ex:
                self._log("failed-remove").error("Failed to remove file '%s'. exception %s", fileName, ex)


    def _startArchivers (self):

        # Start the unsent archiver

        if self._unsentArchiver:
            self._unsentArchiver.stop()
            self._unsentArchiver = None

        self._unsentArchiver = a.infra.file.rotating_file_archiver.Archiver(
            logger = self._log, inputDir = self._logDir, bufferDirSizeLimitInMB = 1024, outputDir = self._unsentArchiveDir, \
            bufferDir = "unsent_archiver_buffer")

        self._unsentArchiver.setUseFixedFileSize(4096)
        self._unsentArchiver.setOutputDirSizeLimitGB(self._unsentArchiveMaxSizeGB)
        self._unsentArchiver.setRotationTimeThersholdSeconds(60)
        self._unsentArchiver.start(self._archiverThreadExceptionCallBack)

        # Start the meta archiver

        if self._metaArchiver:
            self._metaArchiver.stop()
            self._metaArchiver = None

        self._metaArchiver = a.infra.file.rotating_file_archiver.Archiver(
            logger = self._log, inputDir = self._logDir, bufferDirSizeLimitInMB = 1024, outputDir = self._metaArchiveDir, \
            bufferDir = "meta_archiver_buffer")

        self._metaArchiver.setUseFixedFileSize(4096)
        self._metaArchiver.setOutputDirSizeLimitGB(self._metaArchiveMaxSizeGB)
        self._metaArchiver.setRotationTimeThersholdSeconds(60)
        self._metaArchiver.start(self._archiverThreadExceptionCallBack)


    def _stopArchivers (self):
        # Stop the unsent archiver
        if self._unsentArchiver:
            self._unsentArchiver.stop()

        # Stop the meta archiver
        if self._metaArchiver:
            self._metaArchiver.stop()


    def _archiverThreadExceptionCallBack (self, exception):
        self._log("archvier-thread-exception").error("Got exception '%s' from the archiver thread. Terminate reporter %s" % (exception, self._name))
        self.terminate()


    def enabled (self):
        return self._enabled or self._analytics


class LlnwdCdnReporter(CdnReporter):
    
    def __init__ (self, name):
        super(LlnwdCdnReporter, self).__init__(name)


    def reportTransaction (self, recordArray):

        if not self.enabled():
            return

        endTime = recordArray[topper_record_utils.FlowRecordOffsets.theTimeOfDayOffset.myVal]
        srcIp = recordArray[topper_record_utils.FlowRecordOffsets.theSrcIpOffset.myVal]
        duration = recordArray[topper_record_utils.FlowRecordOffsets.theTransactionDownloadTimeMsecOffset.myVal]

        downloadedContentBytesPort0 = recordArray[topper_record_utils.FlowRecordOffsets.theTransactionDownloadedContentBytesPort0Offset.myVal]
        downloadedContentBytesPort1 = recordArray[topper_record_utils.FlowRecordOffsets.theTransactionDownloadedContentBytesPort1Offset.myVal]
        downloadedContentBytes = int(downloadedContentBytesPort0) + int(downloadedContentBytesPort1)
        if downloadedContentBytes == 0:
            return

        cgid = recordArray[topper_record_utils.FlowRecordOffsets.theCgidOffset.myVal]

        reqPath = recordArray[topper_record_utils.FlowRecordOffsets.thePathOffset.myVal]
        lstPath = reqPath.split("/", 4)
        if not (len(lstPath) == 5 and lstPath[0] == ""):
            self._log("req-path-error").warning("Error Extracting request original path from delivery path %s", reqPath)
            return

        origPath = lstPath[4]
        origHostName = recordArray[topper_record_utils.FlowRecordOffsets.theOrigHostNameOffset.myVal]
        reqUrl = "http://" + origHostName + "/" + origPath

        # TODO(amiry) - POC hack. Need a constant for the id somewhere
        cdnId = recordArray[topper_record_utils.FlowRecordOffsets.theCdnIdOffset.myVal]
        isLLnwdTransaction = (cdnId == '1')

        # TODO(amiry) - POC hack. Only limelight urls are on the f-record
        llnwdLocation = recordArray[topper_record_utils.FlowRecordOffsets.theLlnwdLocationOffset.myVal]

        hasLlnwdLocation = True
        if (llnwdLocation == 'N'):
            hasLlnwdLocation = False

        # For limelight transactions we explicitly set the llnwdLocation to be the same as reqUrl.
        if isLLnwdTransaction:
            llnwdLocation = reqUrl

        # Simple "transaction filtering"
        writeTransaction = False
        if isLLnwdTransaction or (self._urlTranslationEnabled and hasLlnwdLocation):
            writeTransaction = True

        if self._analytics:
            # In analytics mode we only update stats counters
            if writeTransaction:
                self._updatePerCgidData(self._counters["cgid"], cgid, downloadedContentBytes)
            return

        if writeTransaction:
            # Rotate file if needed
            self._checkRotationCnt += 1
            if (self._checkRotationCnt % 5000 == 0) and self._shouldRotate():
                if not self._rotateFile():
                    # Failed to rotate
                    self._log("rotate-failed").warning("Rotation failed. Can't write transaction")
                    return

            # Write the transaction
            if self._tranFile:
                self._tranFile.write("%s %s %s %s %s %s\n" % (endTime, duration, srcIp, downloadedContentBytes, reqUrl, llnwdLocation))
                self._updateStatsCounters(cgid, downloadedContentBytes)
                self._numTransactionsInCurrFile += 1
            else:
                self._log("no-open-file").error("Can't write transaction. Log file is closed.")

