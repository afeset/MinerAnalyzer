#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: effiz
# 

from a.infra.basic.return_codes import ReturnCodes
from a.storage.disk import content_disk,content_disk_manager,storage_module_manager,logical_disk_manager,physical_disk_manager,file_system_manager,controller_manager,disk
import a.storage.blinky.disk
import a.sys.blinky.domain_priority
import a.infra.process
import time
import os
import shutil
import storage_control_app_utils


if  __package__ is None:
    G_NAME_MODULE_STORAGE_CONTROL_APP = "unknown"
    G_NAME_GROUP_STORAGE_CONTROL_APP_GENERAL = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_CONTROL_APP
    from . import G_NAME_GROUP_STORAGE_CONTROL_APP_GENERAL


class StorageControlApp:

    # Consts used for the specificParams dictionary
    SPECIFIC_PARAM_KEY_STORAGE_CONTROL_CONFIGURATION_DIR  = "storage-control-cfg-dir"
    SPECIFIC_PARAM_KEY_CONTENT_DISK_MANAGER_STATE_DIR     = "content-disk-manager-state-dir"
    SPECIFIC_PARAM_KEY_APP_STATUS_DIR                     = "app-status-dir"
    SPECIFIC_PARAM_KEY_CLEAN_CONTENT                      = "clean-content"
    SPECIFIC_PARAM_KEY_CLEAN_CONTENT_RM                   = "clean-content-rm"
                                                         
    # Consts used for per-content-disk-specification
    CONTENT_DISK_SPEC_KEY_MOUNT_POINT = "mount-point"
    CONTENT_DISK_SPEC_KEY_META_DIR    = "meta-dir"
    CONTENT_DISK_SPEC_KEY_MEDIA_DIR   = "media-dir"
    CONTENT_DISK_SPEC_KEY_VITAL_DIR   = "vital-dir"

    # Consts for sections/fields-names/defaults in sys-param
    CONFIG_SECTION_STORAGE_CONTROL_PARAMS = "storage-control-params"
    CONFIG_VAR_MAX_CONTENT_DISK_COUNT     = "max-active-content-disk-count"
    CONFIG_VAR_MIN_CONTENT_DISK_COUNT     = "min-active-content-disk-count"
    CONFIG_VAR_BLOCK_DEVICE_READAHEAD     = "block-device-readahead"
    CONFIG_VAR_ACCEPT_ANY_UUID            = "accept-any-uuid"
    CONFIG_VAR_DISABLE_AUTO_INIT          = "disable-auto-init"
    CONFIG_VAR_FORCE_INIT                 = "force-init"
    CONFIG_VAR_DISABLE_REMOVE_LVM         = "disable-remove-lvm"
    CONFIG_VAR_USER_DEFINED_CFG_DIR       = "user-defined-cfg-dir"


    # Default values for data in sys-param
    DEFAULT_MAX_CONTENT_DISK_COUNT = 6
    DEFAULT_MIN_CONTENT_DISK_COUNT = 6
    DEFAULT_BLOCK_DEVICE_READAHEAD = 256
    DEFAULT_ACCEPT_ANY_UUID        = False
    DEFAULT_DISABLE_AUTO_INIT      = False
    DEFAULT_FORCE_INIT             = ""
    DEFAULT_DISABLE_REMOVE_LVM     = False
    DEFAULT_USER_DEFINED_CFG_DIR   = ""

                                 
    # Consts for internal objects use
    _DISK_CONTROLLER_CONFIGURATION_FILE_NAME             = "disk_controller_cfg.json"
    _PDISK_CONFIGURATION_FILE_NAME                       = "pdisks_cfg.json"
    _LOGICAL_DISK_CONFIGURATION_FILE_NAME                = "logical_disks_cfg.json"
    _FILE_SYSTEMS_CONFIGURATION_FILE_NAME                = "file_systems_cfg.json"
    _CONTENT_DISKS_CONFIGURATION_FILE_NAME               = "content_disks_cfg.json"
    _CONTENT_DISK_MANAGER_CONFIGURATION_FILE_NAME        = "content_disk_manager_cfg.json"

    def __init__ (self):
        self._contentDiskManager   = None
        self._diskMapper           = None
        self._blinkyAgent          = None
        self._storageBlinkyAdapter = None
        self._keepOnRunningFlag    = True

    def daemonControlInitBlinky (self,blinkyAgent):
        self._domain = blinkyAgent.createConfigDomain("storage-control", a.sys.blinky.domain_priority.DomainPriority.kApplicationDefault)
        self._storageBlinkyAdapter.initBlinky(self._domain,self._diskMapper,self._storageModuleManager)
        self._domain.registrationDone()
        self._storageBlinkyAdapter.triggerBlinky()

    def initContentDiskSpecification (self, dictionaryDiskNameToSpecDictionary):
        self._contentDisksSpecification = dictionaryDiskNameToSpecDictionary

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

        self._logGeneral = logger.createLogger(G_NAME_MODULE_STORAGE_CONTROL_APP, G_NAME_GROUP_STORAGE_CONTROL_APP_GENERAL)
        self._controllerManager   = controller_manager.ControllerkManager(logger)
        physicalDiskManager = physical_disk_manager.PhysicalDiskManager(logger,self._controllerManager)
        logicalDiskManager  = logical_disk_manager.LogicalDiskManager(logger,physicalDiskManager)
        fileSystemManager   = file_system_manager.FileSystemManager(logger)
        self._storageModuleManager = storage_module_manager.StorageModuleManager(logger,self._controllerManager)
        self._contentDiskManager = content_disk_manager.ContentDiskManager(logicalDiskManager,physicalDiskManager,fileSystemManager,self._storageModuleManager,logger)
        self._diskMapper = disk.DiskMapper(self._contentDiskManager,logicalDiskManager,physicalDiskManager,fileSystemManager,logger)
        self._storageBlinkyAdapter = a.storage.blinky.disk.StorageBlinkyAdaptor(logger)


    def daemonControlInitExternalData (self,sysParamsCfg,specificParams):
        """Init the data provided from outside

        Init the data provided from outside - both from configuration and operational consts

        Args:
            sysParamsCfg: a contatiner holding the sys params base configuration (that are destined to move to blinky)
            specificParams: a dictionary holding the data under the "SPECIFIC_PARAM_KEY_..." keys defined at the begining of this class                                            

        Returns:
            None

        Raises:
            None (but may Fatal)
        """       
        
        self._appStatusDir = specificParams[self.SPECIFIC_PARAM_KEY_APP_STATUS_DIR] # not persistant (application use)
        self._storageControlCfgDir = sysParamsCfg.getString(self.CONFIG_SECTION_STORAGE_CONTROL_PARAMS,self.CONFIG_VAR_USER_DEFINED_CFG_DIR,self.DEFAULT_USER_DEFINED_CFG_DIR)
        if not self._storageControlCfgDir:
            self._storageControlCfgDir = specificParams[self.SPECIFIC_PARAM_KEY_STORAGE_CONTROL_CONFIGURATION_DIR]


        # Wrap necessary params in a cfg object
        self._contentDiskManagerExternalCfg = content_disk_manager.ContentDiskManagerExternalCfg()
        self._contentDiskManagerExternalCfg.diskControllersCfg    = os.path.join(self._storageControlCfgDir,self._DISK_CONTROLLER_CONFIGURATION_FILE_NAME)
        self._contentDiskManagerExternalCfg.pdisksCfg             = os.path.join(self._storageControlCfgDir,self._PDISK_CONFIGURATION_FILE_NAME)
        self._contentDiskManagerExternalCfg.logicalDisksCfg       = os.path.join(self._storageControlCfgDir,self._LOGICAL_DISK_CONFIGURATION_FILE_NAME)
        self._contentDiskManagerExternalCfg.fssCfg                = os.path.join(self._storageControlCfgDir,self._FILE_SYSTEMS_CONFIGURATION_FILE_NAME)
        self._contentDiskManagerExternalCfg.contentDisksCfg       = os.path.join(self._storageControlCfgDir,self._CONTENT_DISKS_CONFIGURATION_FILE_NAME)
        self._contentDiskManagerExternalCfg.contentDiskManagerCfg = os.path.join(self._storageControlCfgDir,self._CONTENT_DISK_MANAGER_CONFIGURATION_FILE_NAME)
        self._contentDiskManagerExternalCfg.stateDir              = specificParams[self.SPECIFIC_PARAM_KEY_CONTENT_DISK_MANAGER_STATE_DIR] # persistant (internal use)    
        self._contentDiskManagerExternalCfg.doCleanContent        = specificParams[self.SPECIFIC_PARAM_KEY_CLEAN_CONTENT]
        self._contentDiskManagerExternalCfg.doCleanContentRm      = specificParams[self.SPECIFIC_PARAM_KEY_CLEAN_CONTENT_RM]

        # include sys-params in cfg object
        self._contentDiskManagerExternalCfg.maxDiskCount         = sysParamsCfg.getInt(self.CONFIG_SECTION_STORAGE_CONTROL_PARAMS,self.CONFIG_VAR_MAX_CONTENT_DISK_COUNT,self.DEFAULT_MAX_CONTENT_DISK_COUNT)
        self._contentDiskManagerExternalCfg.minDiskCount         = sysParamsCfg.getInt(self.CONFIG_SECTION_STORAGE_CONTROL_PARAMS,self.CONFIG_VAR_MIN_CONTENT_DISK_COUNT,self.DEFAULT_MIN_CONTENT_DISK_COUNT)
        self._contentDiskManagerExternalCfg.blockDeviceReadahead = sysParamsCfg.getInt(self.CONFIG_SECTION_STORAGE_CONTROL_PARAMS,self.CONFIG_VAR_BLOCK_DEVICE_READAHEAD,self.DEFAULT_BLOCK_DEVICE_READAHEAD)
        self._contentDiskManagerExternalCfg.acceptAnyUuid        = sysParamsCfg.getBool(self.CONFIG_SECTION_STORAGE_CONTROL_PARAMS,self.CONFIG_VAR_ACCEPT_ANY_UUID,self.DEFAULT_ACCEPT_ANY_UUID)
        self._contentDiskManagerExternalCfg.disableRemoveLvm     = sysParamsCfg.getBool(self.CONFIG_SECTION_STORAGE_CONTROL_PARAMS,self.CONFIG_VAR_DISABLE_REMOVE_LVM,self.DEFAULT_DISABLE_REMOVE_LVM)
        self._contentDiskManagerExternalCfg.disableAutoInit      = sysParamsCfg.getBool(self.CONFIG_SECTION_STORAGE_CONTROL_PARAMS,self.CONFIG_VAR_DISABLE_AUTO_INIT,self.DEFAULT_DISABLE_AUTO_INIT)
                    
        rc = self._contentDiskManager.init(self._contentDiskManagerExternalCfg)
        rc = self._controllerManager.init(self._contentDiskManagerExternalCfg.diskControllersCfg)


        if (rc != ReturnCodes.kOk):
            a.infra.process.processFatal("failed to init content disk manager external data: %s", rc.getName())
        

    def daemonControlSystemInit(self):

        # prepare per content data for activation
        activationData = {}
        for name,diskSpec in self._contentDisksSpecification.items():
            activationData[name] = content_disk.ContentDiskActivationExternalData(diskSpec[self.CONTENT_DISK_SPEC_KEY_MOUNT_POINT],\
                                                                                  diskSpec[self.CONTENT_DISK_SPEC_KEY_META_DIR],\
                                                                                  diskSpec[self.CONTENT_DISK_SPEC_KEY_MEDIA_DIR],\
                                                                                  diskSpec[self.CONTENT_DISK_SPEC_KEY_VITAL_DIR])

        rc = self._contentDiskManager.activateAllDisks(activationData)
        isStorageInUnsupportedState = False
        if (rc != ReturnCodes.kOk):
            if (rc == ReturnCodes.kUnSupported):
                isStorageInUnsupportedState = True
            else:
                a.infra.process.processFatal("failed to activate all disks: %s", rc.getName())

        # after activation is done, update app status file
        dataDict = {}
        dataDict[storage_control_app_utils.StorageControlAppUtils._STATUS_FILE_KEY_STATUS_SUMMARY_STRING]     = self._contentDiskManager.getStatusSummaryString()
        dataDict[storage_control_app_utils.StorageControlAppUtils._STATUS_FILE_KEY_DETAILED_STATUS_STRING]    = self._contentDiskManager.getDetailedStatusString()
        dataDict[storage_control_app_utils.StorageControlAppUtils._STATUS_FILE_KEY_SHELL_STATUS_STRING]       = self._contentDiskManager.getSystemStatusString()
        dataDict[storage_control_app_utils.StorageControlAppUtils._STATUS_FILE_KEY_ACTIVE_DISKS_LIST]         = self._contentDiskManager.getActiveDisksList()
        dataDict[storage_control_app_utils.StorageControlAppUtils._STATUS_FILE_KEY_IS_QSM_ENABLED]            = self._contentDiskManager.isQsmEnabled()
        dataDict[storage_control_app_utils.StorageControlAppUtils._STATUS_FILE_KEY_STORAGE_ERROR_STATUS]      = isStorageInUnsupportedState

        statusFileName = os.path.join(self._appStatusDir, storage_control_app_utils.StorageControlAppUtils._STATUS_FILE_NAME)
        try:
            a.infra.format.json.writeToFile(self._logGeneral, dataDict, statusFileName, indent=4)
        except:
            a.infra.process.processFatal("failed to write status file %s", statusFileName)


    def daemonControlRun(self):
        while self._keepOnRunningFlag:
            time.sleep(0.1)
        self._logGeneral("about-to-stop").debug1("about to shut-down storage control")
        self._contentDiskManager.shutDown()
        self._logGeneral("shut-down").debug1("storage control is now down")
        
    def daemonControlStop (self):        
        self._logGeneral("got-stop-sig").notice("process is about to stop")
        self._keepOnRunningFlag = False
        statusFileName = os.path.join(self._appStatusDir, storage_control_app_utils.StorageControlAppUtils._STATUS_FILE_NAME)
        try:
            shutil.copyfile(statusFileName,statusFileName+".old")
            os.remove(statusFileName)
        except Exception,e:
            self._logGeneral("failed-to-delete").error("failed to delete status file %s or copy it to .old! exception = ",statusFileName,e)


