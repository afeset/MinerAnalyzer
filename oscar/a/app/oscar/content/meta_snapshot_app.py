
#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: royr
# 
import time, os, fnmatch

if  __package__ is None:
    G_NAME_MODULE_META_SNAPSHOT_APP = "unknown"
    G_NAME_GROUP_META_SNAPSHOT_APP_GENERAL = "unknown"
    G_NAME_GROUP_META_SNAPSHOT_APP_IO = "unknown"
else:
    from . import G_NAME_MODULE_META_SNAPSHOT_APP
    from . import G_NAME_GROUP_META_SNAPSHOT_APP_GENERAL
    from . import G_NAME_GROUP_META_SNAPSHOT_APP_IO 

import a.infra.file.rotating_file_size_enforcer


#--- Constants---------#
SNAPSHOT_ARCHIVE_SUFFIX = ".tar.gz"
SNAPSHOT_ARCHIVE_PREFIX = "snapshot-"


class MetaSnapshotApp():

    # Consts use for the specificParams dictionary provided on "initspecificParams"
    SPECIFIC_PARAM_KEY_VOLATILE_META_BASE_DIR="volatile-meta-base-dir"
    SPECIFIC_PARAM_KEY_SNAPSHOTS_OUTPUT_DIR="snapshots-output-dir"


    # Consts for sections/fields names in sys-param
    CONFIG_SECTION_META_SNAPSHOT_PARAMS = "meta-snapshot-params"
    CONFIG_VAR_SNAPSHOTS_TOTAL_SIZE_LIMIT_GB = "snapshots-total-size-limit-gb"
    CONFIG_VAR_SNAPSHOTS_INTERVAL_MINUTES = "snapshots-interval-minutes"
    CONFIG_VAR_SHOULD_TAKE_SNAPSHOTS = "take-snapshots"

 
                                                         
    # Default values for data in sys-param
    DEFAULT_SNAPSHOTS_TOTAL_SIZE_LIMIT_GB = 20
    DEFAULT_SNAPSHOTS_INTERVAL_MINUTES = 240
    DEFAULT_SHOULD_TAKE_SNAPSHOTS = True
                                                                        


    def __init__ (self):
        #--------Log--------------
        self._logGeneral = None

        #------Configuration-------
        self._volatileMetaDir = None
        self._globalSnapshotDir = None
        self._globalSnapshotDirSizeLimit = None
        self._snapshotsIntervalSec = None
        self._shouldTakeSnapshots = None

        #------Control------------
        self._keepRunning = None

        #------File naming and size limit enforcers
        self._globalSnapshotDirSizeEnforcer = None

        self._currentSnapshotsDir = None
        self._lastTimeMadeSnapshotSec = None
        self._currentSnapshotArchiveFileNamePath = None

        #-------Counters-----------
        self.counters = {'numOldTmpRemoved':0,
                         'numOldTmpFound':0,
                         'numSnapshotsOk':0,
                         'numSnapshotsFailed':0}


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

        self._logGeneral=logger.createLogger(G_NAME_MODULE_META_SNAPSHOT_APP, G_NAME_GROUP_META_SNAPSHOT_APP_GENERAL)
        self._logIo=logger.createLogger(G_NAME_MODULE_META_SNAPSHOT_APP, G_NAME_GROUP_META_SNAPSHOT_APP_IO)



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

        self._volatileMetaDir = specificParams[self.SPECIFIC_PARAM_KEY_VOLATILE_META_BASE_DIR]
        self._globalSnapshotDir = specificParams[self.SPECIFIC_PARAM_KEY_SNAPSHOTS_OUTPUT_DIR]
        
        self._globalSnapshotDirSizeLimit = 1024*1024*1024*sysParamsCfg.getFloat(self.CONFIG_SECTION_META_SNAPSHOT_PARAMS, 
                                                                              self.CONFIG_VAR_SNAPSHOTS_TOTAL_SIZE_LIMIT_GB, 
                                                                              self.DEFAULT_SNAPSHOTS_TOTAL_SIZE_LIMIT_GB)

        self._snapshotsIntervalSec = 60*sysParamsCfg.getInt(self.CONFIG_SECTION_META_SNAPSHOT_PARAMS, 
                                                           self.CONFIG_VAR_SNAPSHOTS_INTERVAL_MINUTES, 
                                                           self.DEFAULT_SNAPSHOTS_INTERVAL_MINUTES)

        self._shouldTakeSnapshots = sysParamsCfg.getBool(self.CONFIG_SECTION_META_SNAPSHOT_PARAMS, 
                                                           self.CONFIG_VAR_SHOULD_TAKE_SNAPSHOTS, 
                                                           self.DEFAULT_SHOULD_TAKE_SNAPSHOTS)
        
        

    #-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStart(self):
        """launching the process"""
        if not self._init():
            a.infra.process.processFatal("Failed initializing meta_snapshot")

        self._keepRunning = True

        numOfTmpsFound, numOfTmpsRemoved = self._clearOldTemps()
        self._logIo("remove-old-tmp-files").debug1("found %d old tmp files. removed %d old tmp files", numOfTmpsFound, numOfTmpsRemoved)
        self.counters['numOldTmpFound'] += numOfTmpsFound
        self.counters['numOldTmpRemoved'] += numOfTmpsRemoved



    #-----------------------------------------------------------------------------------------------------------------------
    def daemonControlRun(self):
        """getting into the main loop"""
        if not self._mainLoop():
            self._logGeneral("done-error").error("process exited with error")
        else:
            self._logGeneral("done-ok").notice("process terminated")



    def _mainLoop (self):

        while self._keepRunning:

            makeSnapShot = False
            currentTime = time.time()
            if (self._lastTimeMadeSnapshotSec == None) or (currentTime - self._lastTimeMadeSnapshotSec >= self._snapshotsIntervalSec):
                self._lastTimeMadeSnapshotSec = currentTime
                makeSnapShot = True

            if self._shouldTakeSnapshots and makeSnapShot:
                if self._makeSnapshot():
                    self._logIo("make-snapshot-ok").debug1("finished taking meta snapshot")
                    self.counters['numSnapshotsOk'] += 1    
                else:
                    self._logIo("make-snapshot-error").error("_makeSnapshot() returned with error")
                    self.counters['numSnapshotsFailed'] += 1

                if self._keepRunning:
                    try:
                        self._logIo("enforce-size-limit").debug2("enforcing size limit of %d bytes on %s", self._globalSnapshotDirSizeLimit, self._globalSnapshotDir)
                        self._globalSnapshotDirSizeEnforcer.enforceSize()
                    except Exception as ex:
                        self._logIo("cant-enforce").error("error trying to enforce global dir size. exception %s. proccess will terminate", ex)
                        return False

                    numOfEmptyDirsRemoved = self._removeOldEmptyDirs()
                    self._logIo("remove-old-empty-dirs").debug1("removed %d old empty directories", numOfEmptyDirsRemoved)

            if self._keepRunning:
                time.sleep(60)

        return True


    def _makeSnapshot (self):
        tmpfileName = self._currentSnapshotArchiveFileNamePath + ".tmp"
        try:
            os.system("cd %s; nice -n 19 tar -czf %s *" % (self._volatileMetaDir, tmpfileName)) # send file to archive
        except Exception as ex:
            self._logIo("failed-compressing").error("failed compressing to  %s. exception:%s", tmpfileName, ex)
            return False

        if os.path.exists(tmpfileName):
            try:
                os.rename(tmpfileName, self._currentSnapshotArchiveFileNamePath)
                self._logGeneral("make-snapshot-done").debug1("snapshot was archived to file %s", self._currentSnapshotArchiveFileNamePath)
            except Exception as ex:
                self._logIo("failed-renaming").error("failed renaming %s to %s. exception:%s", tmpfileName, self._currentSnapshotArchiveFileNamePath, ex)
                return False
        else:
            self._logIo("tmp-not-found").error("tmp archive file %s not found ", self._currentSnapshotArchiveFileNamePath)
            return False

        try:
            self._globalSnapshotDirSizeEnforcer.rotate()
            self._currentSnapshotArchiveFileNamePath = self._globalSnapshotDirSizeEnforcer.getCurrentFileName()
        except Exception as ex:
            self._logIo("cant-rotate-file").error("error rotating file. exception %s", ex)
            return False

        return True


    def _clearOldTemps (self):

        numOfTmpsFound = 0
        numOfTmpsRemoved = 0

        for (currentRoot,dirNames,fileNames) in os.walk(self._globalSnapshotDir):
            if self._keepRunning:
                # For each tmp file
                for tmpFile in fnmatch.filter(fileNames, "*.tmp"):
                    numOfTmpsFound += 1
                    tmpFileFullNamePath = os.path.join(currentRoot, tmpFile)
                    try:
                        os.remove(tmpFileFullNamePath)
                        self._logIo("remove-old-tmp-file").debug2("removed old tmp file %s", tmpFileFullNamePath)
                        numOfTmpsRemoved += 1
                    except Exception as ex:
                        self._logIo("error-remove-old-tmp-file").error("error removing tmp file %s. exception %s", tmpFileFullNamePath, ex)

        return numOfTmpsFound, numOfTmpsRemoved



    def _removeOldEmptyDirs (self):

        numOfEmptyDirsRemoved = 0

        for (currentRoot,dirNames,fileNames) in os.walk(self._globalSnapshotDir):
            for directory in dirNames:    
                try:
                    os.rmdir(os.path.join(currentRoot, directory))
                    numOfEmptyDirsRemoved += 1
                except Exception:
                    pass

        return numOfEmptyDirsRemoved



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
        self._keepRunning = False
        


    def _init (self):        

        self._globalSnapshotDirSizeEnforcer = a.infra.file.rotating_file_size_enforcer.RotatingFileSizeEnforcer(self._logIo, self._globalSnapshotDir, SNAPSHOT_ARCHIVE_PREFIX, SNAPSHOT_ARCHIVE_SUFFIX)
        self._globalSnapshotDirSizeEnforcer.setTotalSize(self._globalSnapshotDirSizeLimit)

        self._globalSnapshotDirSizeEnforcer.prepare()
        self._currentSnapshotArchiveFileNamePath = self._globalSnapshotDirSizeEnforcer.getCurrentFileName()

        return True
