# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz


if  __package__ is None:
    G_NAME_MODULE_STORAGE_DISK = "unknown"
    G_NAME_GROUP_STORAGE_DISK_CONTENT_DISK = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_DISK
    from . import G_NAME_GROUP_STORAGE_DISK_CONTENT_DISK


from a.infra.basic.return_codes import ReturnCodes
from a.storage.disk import logical_disk as ld, logical_disk_manager as ldm, file_system as fs, dell_raid_controller as drc
__pychecker__ = 'maxrefs=20'
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen #  impoting with 'as blinky_generated_enums' causes stupid pycheck warnings
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.disk_data_gen
blinky_generated_disk_data=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.disk_data_gen  
blinky_generated_enums=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen
import a.api.user_log.msg.storage
import a.infra.process
import os
import email.utils
import time
import shutil
import threading




class ContentDisk(object):
    """
    A class represnting a content disk
                     ________________
                    |                |
                    |  content disk  |
                    |________________|
                      /            \
             ________/______    ____\___________     
            |       |       |  |                | 
            |  LDM  |  PDM  |  |      FSM       |
            |_______|_______|  |________________|
                    |                  |
            ________|________    ______|_________
           |        |        |  |                |
           |logical |physical|  |  file system   |
           |________|________|  |________________|

    """

    # Status related constants
    DETAILED_STATUS_KEY_LOGICAL_DISK = "logiacl-disk"
    DETAILED_STATUS_KEY_FILE_SYSTEM  = "file-system"

    STATUS_SUMMARY_STATUS_DOWN_STRING = "Down"
    STATUS_SUMMARY_STATE_FAULT_STRING = "Fault"

    # user log related constant
    OPERATIVE_STATE_UP      = "up"
    OPERATIVE_STATE_DOWN    = "down"
    REASON_DISK_INITIALIZED = "disk was initialized"
    REASON_ABSENT           = "absent"
    REASON_DISK_ERROR       = "disk error"
    REASON_FOREIGN_DISK     = "foreign"

    # vital file constants
    VITAL_FILE_NAME                 = "vital"
    VITAL_FILE_KEY_INIT_DATE_EPOCH  = "init-date-epoch"
    VITAL_FILE_KEY_INIT_DATE_STRING = "init-date-string"
    VITAL_FILE_KEY_FORMAT_VERSION   = "format-version"
    VITAL_FILE_FORMAT_VERSION       = 11
    

    class ActivateData:

        def __init__ (self,mountingPoint,metaDir,mediaDir,vitalDir,expectedUuid,cleanDirs):

            # input params
            self.mountingPoint = mountingPoint
            self.metaDir = metaDir
            self.mediaDir = mediaDir
            self.vitalDir = vitalDir
            self.expectedUuid = expectedUuid
            self.cleanDirs = cleanDirs


        def __str__ (self):
            return str(self.__dict__)


    def __init__ (self,logicalDiskName,logicalDiskManager,physicalDiskManager,fileSystemManager,storageModuleManager,logger):

        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_DISK,G_NAME_GROUP_STORAGE_DISK_CONTENT_DISK)
        
        # identifier
        self._logicalDiskName     = logicalDiskName

        # cofiguration
        self._runningDiskConfig   = blinky_generated_disk_data.DiskData()
        self._candidateDiskConfig = blinky_generated_disk_data.DiskData()
        self._activeDiskConfig    = blinky_generated_disk_data.DiskData()
        self._lock                = threading.RLock()

        # managers
        self._logicalDiskManager      = logicalDiskManager
        self._physicalDiskManager     = physicalDiskManager
        self._fileSystemManager       = fileSystemManager
        self._storageModuleManager    = storageModuleManager

        # intermediate params
        self._blockDevice             = None

        # general
        self._activateData            = None

        # flags
        self._isActive = False

        # status
        self.statusEnum       = blinky_generated_enums.DiskOperationalStatusType.kUp
        self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kNone

        # alarms
        self.failureAlarm = False
        self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kNone

        # state (user log)
        self.state            = ContentDisk.OPERATIVE_STATE_UP
        self.reason           = ContentDisk.REASON_DISK_INITIALIZED
        self.prevState        = ContentDisk.OPERATIVE_STATE_UP
        self.prevReason       = ContentDisk.REASON_DISK_INITIALIZED


    def updateStateAndReason (self,newState,newReason):
        self.prevState  = self.state
        self.prevReason = self.reason
        self.state      = newState
        self.reason     = newReason

        if self._stateChanged():
            # content disk state was changed -> user log
            if (self.state == ContentDisk.OPERATIVE_STATE_UP) and (self.REASON_DISK_INITIALIZED):
                # content disk was initialized -> more user log
                a.infra.process.logUserMessage(a.api.user_log.msg.storage.ContentDiskInit(self._logicalDiskName))

            a.infra.process.logUserMessage(a.api.user_log.msg.storage.ContentDiskState(self._logicalDiskName,self.state,self.reason))


    ## Configuration related functions ##

    def _getDiskCandidateSubElements (self):
        physicalDisk = self._physicalDiskManager.getCandidatePhysicalDisk(self._logicalDiskName)
        logicalDisk  = self._logicalDiskManager.getCandidateLogicalDisk(self._logicalDiskName)
        fileSystem   = self._fileSystemManager.getCandidateFileSystem(self._logicalDiskName)

        subElements = [physicalDisk,logicalDisk,fileSystem]

        if (None in subElements):
            self._log("missing-subelements").error("content disk %s needs all the subelements [physicalDisk = %s,logicalDisk = %s,fileSystem = %s]",self._logicalDiskName,physicalDisk,logicalDisk,fileSystem)
            return subElements + [ReturnCodes.kGeneralError]

        self._log("missing-subelements").debug2("all subelements for content disk %s found [physicalDisk = %s,logicalDisk = %s,fileSystem = %s]",self._logicalDiskName,physicalDisk,logicalDisk,fileSystem)
        return subElements + [ReturnCodes.kOk]
        

    def diskTrxStart (self):
        self._log("disk-trx-start").debug3("diskTrxStart()  was called for content disk %s, running --> candidate",self._logicalDiskName)
        self._candidateDiskConfig.copyFrom(self._runningDiskConfig)
        
        physicalDisk,logicalDisk,fileSystem,rc = self._getDiskCandidateSubElements()
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        if ((physicalDisk.diskPhysicalTrxStart() == ReturnCodes.kOk) and
            (logicalDisk.diskRaidArrayTrxStart() == ReturnCodes.kOk) and
            (fileSystem.diskFileSystemTrxStart() == ReturnCodes.kOk)):
            return ReturnCodes.kOk

        self._log("disk-trx-start-fail").error("diskTrxStart() for content disk %s failed!",self._logicalDiskName)
        return ReturnCodes.kGeneralError


    def diskTrxCommit (self):
        self._log("disk-trx-commit").debug3("diskTrxCommit()  was called for content disk %s, candidate --> running",self._logicalDiskName)
        physicalDisk,logicalDisk,fileSystem,rc = self._getDiskCandidateSubElements()
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        with self._lock:
            
            self._runningDiskConfig.copyFrom(self._candidateDiskConfig)
            if ((physicalDisk.diskPhysicalTrxCommit() == ReturnCodes.kOk) and
                (logicalDisk.diskRaidArrayTrxCommit() == ReturnCodes.kOk) and
                (fileSystem.diskFileSystemTrxCommit() == ReturnCodes.kOk)):
                return ReturnCodes.kOk

        return ReturnCodes.kGeneralError


    def diskTrxAbort (self):
        self._log("disk-trx-abort").debug3("diskTrxAbort()  was called for content disk %s, None --> candidate",self._logicalDiskName)
        self._candidateDiskConfig = None
        physicalDisk,logicalDisk,fileSystem,rc = self._getDiskCandidateSubElements()
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
        
        if ((physicalDisk.diskPhysicalTrxAbort() == ReturnCodes.kOk) and
            (logicalDisk.diskRaidArrayTrxAbort() == ReturnCodes.kOk) and
            (fileSystem.diskFileSystemTrxAbort() == ReturnCodes.kOk)):
            return ReturnCodes.kOk

        return ReturnCodes.kGeneralError


    def diskValueSet (self,data):
        self._log("disk-value-set").debug3("diskValueSet(data=%s)  was called for content disk %s, data --> candidate",data,self._logicalDiskName)
        self._candidateDiskConfig.copyFrom(data)
        return ReturnCodes.kOk


    def diskPhysicalValueSet (self,data):
        physicalDisk = self._physicalDiskManager.getCandidatePhysicalDisk(self._logicalDiskName)
        
        # if no such physical disk is found - create it
        if (physicalDisk == None):
            physicalDisk = self._physicalDiskManager.createPhysicalDisk(self._logicalDiskName,data.implementation)
            if (physicalDisk == None):
                return ReturnCodes.kGeneralError
        
        # now the actual value set
        return physicalDisk.diskPhysicalValueSet(data)


    def diskRaidArrayValueSet (self,data):
        logicalDisk = self._logicalDiskManager.getCandidateLogicalDisk(self._logicalDiskName)
        
        # if no such logical disk is found - create it
        if (logicalDisk == None):
            logicalDisk = self._logicalDiskManager.createLogicalDisk(self._logicalDiskName,data.implementation)
            if (logicalDisk == None):
                return ReturnCodes.kGeneralError
        
        # now the actual value set
        return logicalDisk.diskRaidArrayValueSet(data)


    def diskFileSystemValueSet (self,data):
        fileSystem = self._fileSystemManager.getCandidateFileSystem(self._logicalDiskName)
        
        # if no such file system is found - create it
        if (fileSystem == None):
            fileSystem = self._fileSystemManager.createFileSystem(self._logicalDiskName,data.fileSystemType)
            if (fileSystem == None):
                return ReturnCodes.kGeneralError
        
        # now the actual value set
        return fileSystem.diskFileSystemValueSet(data)


    def diskFileSystemCommandsValueSet (self,data):
        fileSystem = self._fileSystemManager.getCandidateFileSystem(self._logicalDiskName)
        
        # if no such file system is found - create it
        if (fileSystem == None):
            self._log("no-file-system-for-calue-set").error("diskFileSystemCommandsValueSet(data=%s) for file system %s failed. no file system with that name",data,self._logicalDiskName)
            return ReturnCodes.kGeneralError
        
        # now the actual value set
        return fileSystem.diskFileSystemCommandsValueSet(data)


    def diskFileSystemTimeoutsValueSet (self,data):
        fileSystem = self._fileSystemManager.getCandidateFileSystem(self._logicalDiskName)

        # if no such file system is found - create it
        if (fileSystem == None):
            self._log("no-file-system-for-calue-set").error("diskFileSystemTimeoutsValueSet(data=%s) for file system %s failed. no file system with that name",data,self._logicalDiskName)
            return ReturnCodes.kGeneralError

        # now the actual value set
        return fileSystem.diskFileSystemTimeoutsValueSet(data)


    def pushRunningToActiveConfig (self):
        self._log("push-running-to-active").debug3("pushRunningToActiveConfig()  was called for content disk %s, running -- selective --> active",self._logicalDiskName)
        with self._lock:
            self._activeDiskConfig.copyFrom(self._runningDiskConfig)
            physicalDisk,logicalDisk,fileSystem,rc = self._getDiskCandidateSubElements()
            if (rc != ReturnCodes.kOk):
                self._log("missing-subelements").error("pushRunningToActiveConfig() failed! content disk %s failed to fetch its subelements",self._logicalDiskName)
                return ReturnCodes.kGeneralError
        
            if ((physicalDisk.pushRunningToActiveConfig() == ReturnCodes.kOk) and
                (logicalDisk.pushRunningToActiveConfig() == ReturnCodes.kOk) and
                (fileSystem.pushRunningToActiveConfig() == ReturnCodes.kOk)):
                return ReturnCodes.kOk

        self._log("push-running-to-active-failed").error("pushRunningToActiveConfig() failed! content disk %s subelemnts failed to push",self._logicalDiskName)
        return ReturnCodes.kGeneralError


    def isModuleEnabled (self):
        storageModuleName = self._activeDiskConfig.storageModule
        storageModule = self._storageModuleManager.getStorageModule(storageModuleName)
        if (storageModule == None):
            self._log("no-module-to-query").error("no module named '%s' found, assuming disk %s is disabled",storageModuleName,self._logicalDiskName)
            return False

        return storageModule.isEnabled()

###################################################################

    def _stateChanged (self):
        return ((self.state != self.prevState) or (self.reason != self.prevReason))

    def _createMetaAndMediaDirs (self,mountingPoint,metaDir,mediaDir,cleanDirs):
        metaDirFullPath  = os.path.join(mountingPoint,metaDir)
        mediaDirFullPath = os.path.join(mountingPoint,mediaDir)

        try:
            # remove dirs for fast clean content on small amounts of files
            if cleanDirs:
                if os.path.exists(metaDirFullPath):
                    shutil.rmtree(metaDirFullPath)
                if os.path.exists(mediaDirFullPath):
                    shutil.rmtree(mediaDirFullPath)            

            # create dirs if needed
            if not os.path.isdir(metaDirFullPath):
                os.makedirs(metaDirFullPath)
            if not os.path.isdir(mediaDirFullPath):
                os.makedirs(mediaDirFullPath)

            return ReturnCodes.kOk

        except Exception,e:
            self._log("failed-creating-meta-media").error("failed to create metaDir='%s' or mediaDir='%s' (logicalDiskName='%s') or to clean content. exception = '%s'",metaDirFullPath,mediaDirFullPath,self._logicalDiskName,e)
            return ReturnCodes.kGeneralError


    # this function should be called in final phase of activation only!
    def _createVitalDirAndFileIfNeeded (self,mountingPoint,vitalDir):
        
        vitalDirFullPath  = os.path.join(mountingPoint,vitalDir)
        vitalFileFullPath = os.path.join(vitalDirFullPath,self.VITAL_FILE_NAME)

        try:
            if not os.path.exists(vitalFileFullPath):
                
                # create vital dir
                self._log("not-vital-file-found").debug1("no vital file '%s' found (logicalDiskName='%s') -> need to create",vitalFileFullPath,self._logicalDiskName)

                if not os.path.isdir(vitalDirFullPath):
                    os.makedirs(vitalDirFullPath)
                    self._log("vital-dir-created").debug2("vital dir '%s' was created (logicalDiskName='%s')",vitalDirFullPath,self._logicalDiskName)
                
                # create vital file
                vitalContent = {self.VITAL_FILE_KEY_INIT_DATE_EPOCH  : int(time.time()),\
                                self.VITAL_FILE_KEY_INIT_DATE_STRING : email.utils.formatdate(localtime=True),\
                                self.VITAL_FILE_KEY_FORMAT_VERSION   : self.VITAL_FILE_FORMAT_VERSION}
    
                a.infra.format.json.writeToFile(self._log,vitalContent,vitalFileFullPath,indent=4)
                self._log("vital-file-created").debug1("vital file for '%s' was created in %s, (vital data is %s)",self._logicalDiskName,vitalFileFullPath,vitalContent)

            return ReturnCodes.kOk

        except Exception,e:
            self._log("fail-to-write-vital-file").exception("failed to write vital file '%s'! exception = '%s'",vitalFileFullPath,e)
            return ReturnCodes.kGeneralError


    # Important Note:
    def setInitialActivationParams (self,mountingPoint,metaDir,mediaDir,vitalDir,expectedUuid,cleanDirs):
        self._log("enter-phase0").debug2("entering phase0. activateData = %s",self._activateData)

        # prepare activation data to be used throughout the activation process
        self._activateData = ContentDisk.ActivateData(mountingPoint,metaDir,mediaDir,vitalDir,expectedUuid,cleanDirs)

        # setInitialActivationParams() of FileSystem
        forceInit = self._activeDiskConfig.tmpForceInit
        self._fileSystemManager.setInitialActivationParams(self._logicalDiskName,mountingPoint,expectedUuid,forceInit)

        return ReturnCodes.kOk

        
    def activatePhase0 (self):
        # disabled disks die here
        self._log("enter-phase0").debug2("entering phase0. activateData = %s",self._activateData)
        
        if self.isModuleEnabled():
            self._log("content-disk-enabled").debug2("content disk '%s' is enabled in the QSM level",self._logicalDiskName)
            return ReturnCodes.kOk
        else:
            self._log("content-disk-disabled").debug1("content disk '%s' is disabled in the QSM level",self._logicalDiskName)
            return ReturnCodes.kBadState
        

    def activatePhase1 (self):
        self._log("enter-phase1").debug2("entering phase1. activateData = %s",self._activateData)

        # activate the logical disk and fetch block device
        self._log("content-disk-pre-activate-logical-disk").debug2("attempting to activate logical disk '%s'",self._logicalDiskName)
        forceInit = self._activeDiskConfig.tmpForceInit
        self._blockDevice,rc = self._logicalDiskManager.activateLogicalDisk(self._logicalDiskName,forceInit=forceInit)
        if (rc == ReturnCodes.kOk):
            # disk was actually build in raid level -> initializing disk, state is down until file system is built
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_FOREIGN_DISK)

        elif (rc == ReturnCodes.kNotFound):
            # disk is absent
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_ABSENT)
            self.statusEnum = blinky_generated_enums.DiskOperationalStatusType.kDown
            self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kAbsent
            self.failureAlarm = True
            self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kAbsent
            return rc

        elif (rc == ReturnCodes.kBadState):
            # disk is bad physical state
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_DISK_ERROR)
            self.statusEnum = blinky_generated_enums.DiskOperationalStatusType.kDown
            self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kPhysicalError
            self.failureAlarm = True
            self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kPhysicalError
            return rc

        elif (rc != ReturnCodes.kAlreadyExists):
            # disk does exists but was not successfully built
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_DISK_ERROR)
            self.statusEnum = blinky_generated_enums.DiskOperationalStatusType.kDown
            self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kRaidError
            self.failureAlarm = True
            self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kRaidError
            
            self._log("activate-logical-disk-failed").error("activation of logical disk '%s' failed!",self._logicalDiskName)
            return rc

        self._log("activate-logical-disk-success").debug2("activation of logical disk '%s' succeeded! (blockDevice=%s)",self._logicalDiskName,self._blockDevice)
        
        # setIntermediateActivationParams() of file system
        self._fileSystemManager.setIntermediateActivationParams(self._logicalDiskName,self._blockDevice)

        # activatePhaseX (1<X<4) of FileSystem may fail (so check the return code)
        rc = self._fileSystemManager.activatePhase1(self._logicalDiskName)
        if (rc != ReturnCodes.kOk):
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_DISK_ERROR)
            self.statusEnum = blinky_generated_enums.DiskOperationalStatusType.kDown
            self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kFileSystemError
            self.failureAlarm = True
            self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kFileSystemError
            self._log("activate-logical-disk-failed").error("activation of logical disk '%s' failed!",self._logicalDiskName)
            return rc

        return ReturnCodes.kOk

    def activatePhase2 (self):
        self._log("enter-phase2").debug2("entering phase2. activateData = %s",self._activateData)
        rc = self._fileSystemManager.activatePhase2(self._logicalDiskName)
        if (rc == ReturnCodes.kOk):
            # disk was found foreign -> file system work is being done
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_FOREIGN_DISK)

        elif (rc != ReturnCodes.kAlreadyExists):
            # file system was not built successfully
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_DISK_ERROR)
            self.statusEnum = blinky_generated_enums.DiskOperationalStatusType.kDown
            self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kFileSystemError
            self.failureAlarm = True
            self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kFileSystemError
            self._log("activate-file-system-failed").error("activation of file system for '%s' failed!",self._logicalDiskName)
            return rc

        return ReturnCodes.kOk

    def activatePhase3 (self):
        self._log("enter-phase3").debug2("entering phase3. activateData = %s",self._activateData)
        rc = self._fileSystemManager.activatePhase3(self._logicalDiskName)
        if (rc != ReturnCodes.kOk):
            # file system was not built successfully
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_DISK_ERROR)
            self.statusEnum = blinky_generated_enums.DiskOperationalStatusType.kDown
            self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kFileSystemError
            self.failureAlarm = True
            self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kFileSystemError
            self._log("activate-file-system-failed").error("activation of file system for '%s' failed!",self._logicalDiskName)

        return rc


    def activatePhase4 (self):
        self._log("enter-phase4").debug2("entering phase4. activateData = %s",self._activateData)
        rc = self._fileSystemManager.activatePhase4(self._logicalDiskName)
        if (rc != ReturnCodes.kOk):
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_DISK_ERROR)
            self.statusEnum = blinky_generated_enums.DiskOperationalStatusType.kDown
            self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kFileSystemError
            self.failureAlarm = True
            self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kFileSystemError
            self._log("activate-file-system-failed").error("activation of file system for '%s' failed!",self._logicalDiskName)
            return rc
        
        # create meta and media directories (file-system is mounted by now)
        mountingPoint = self._activateData.mountingPoint
        metaDir  = self._activateData.metaDir
        mediaDir = self._activateData.mediaDir
        cleanDirs = self._activateData.cleanDirs

        rc = self._createMetaAndMediaDirs(mountingPoint,metaDir,mediaDir,cleanDirs)
        if (rc != ReturnCodes.kOk):
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_DISK_ERROR)
            self.statusEnum = blinky_generated_enums.DiskOperationalStatusType.kDown
            self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kOther
            self.failureAlarm = True
            self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kOther
            self._log("fail-to-create-media-meta").error("failed to create meta and/or media dirs for '%s'"%self._logicalDiskName)
            return rc

        # create vital file and directory if needed
        vitalDir = self._activateData.vitalDir
        rc = self._createVitalDirAndFileIfNeeded(mountingPoint,vitalDir)
        if (rc != ReturnCodes.kOk):
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_DOWN,ContentDisk.REASON_DISK_ERROR)
            self.statusEnum = blinky_generated_enums.DiskOperationalStatusType.kDown
            self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kOther
            self.failureAlarm = True
            self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kOther
            self._log("fail-to-create-vital").error("failed to create vital file for '%s'"%self._logicalDiskName)
        else:
            self.updateStateAndReason(ContentDisk.OPERATIVE_STATE_UP,ContentDisk.REASON_DISK_INITIALIZED)
            self.statusEnum = blinky_generated_enums.DiskOperationalStatusType.kUp
            self.statusReasonEnum = blinky_generated_enums.DiskOperationalStatusReasonType.kNone
            self.failureAlarm = False
            self.failureAlarmReason = blinky_generated_enums.ContentDiskFailureReasonType.kNone
            self._log("full-success").debug2("full activation of content disk '%s' ended successfully!",self._logicalDiskName)
            self._isActive = True

        return rc

    def activateGetCurrentUuid (self):
        return self._fileSystemManager.activateGetCurrentUuid(self._logicalDiskName)


    def getDetailedStatus (self):

        logicalDiskStatus,rc1 = self._logicalDiskManager.getLogicalDiskDetailedStatus(self._logicalDiskName)
        fileSystemStatus,rc2 = self._fileSystemManager.getFileSystemDetailedStatus(self._logicalDiskName)

        if ((rc1 == ReturnCodes.kOk) and (rc2 == ReturnCodes.kOk)):
            statusDict = {self.DETAILED_STATUS_KEY_LOGICAL_DISK : logicalDiskStatus, self.DETAILED_STATUS_KEY_FILE_SYSTEM : fileSystemStatus}
            self._log("get-content-disk-detailed-status-success").debug3("getDetailedStatus() for content-disk '%s' succeded! statusDistionary=%s",self._logicalDiskName,statusDict)
            return statusDict,ReturnCodes.kOk

        else:
            self._log("get-content-disk-detailed-status-failed").error("getDetailedStatus() for content-disk '%s' failed!",self._logicalDiskName)
            return None,ReturnCodes.kGeneralError


    def getStatus (self):

        logicalDiskStatus,rc = self._logicalDiskManager.getLogicalDiskStatus(self._logicalDiskName)
        if (rc != ReturnCodes.kOk):
            self._log("content-disk-get-status-failed").error("could not get content disk '%s' status",self._logicalDiskName)
            return None,rc
        
        # update values according to isActive flag - if the logical disk part is 
        # active but the content disk as a whole is not active -> state should be faulty
        if ((logicalDiskStatus[ld.LogicalDisk.STATUS_KEY_STATE] == ld.LogicalDisk.STATE_ACTIVE_STRING) and (not self._isActive)):
            logicalDiskStatus[ld.LogicalDisk.STATUS_KEY_STATUS] = self.STATUS_SUMMARY_STATUS_DOWN_STRING
            logicalDiskStatus[ld.LogicalDisk.STATUS_KEY_STATE]  = self.STATUS_SUMMARY_STATE_FAULT_STRING

        return logicalDiskStatus,ReturnCodes.kOk
        
    def getFileSystemStatus(self,operData):
        return self._fileSystemManager.getFileSystemStatus(self._logicalDiskName,operData)

    # for testing only - do not use without review
    def activate (self,mountingPoint,metaDir,mediaDir,vitalDir,expectedUuid,cleanDirs):
        """
        Activate the content disk. Includes activation of the relevant logical disk and file system

        returns the current uuid and return code
        """
        self.setInitialActivationParams(mountingPoint,metaDir,mediaDir,vitalDir,expectedUuid,cleanDirs)
        for func in [self.activatePhase1,self.activatePhase2,self.activatePhase3,self.activatePhase4]:
            if (func() != ReturnCodes.kOk):
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


class ContentDiskActivationExternalData:
    """
    Struct for passing external data from Application
    """
    def __init__ (self,mountingPoint,metaDir,mediaDir,vitalDir):
        self.mountingPoint = mountingPoint
        self.metaDir       = metaDir
        self.mediaDir      = mediaDir
        self.vitalDir      = vitalDir



