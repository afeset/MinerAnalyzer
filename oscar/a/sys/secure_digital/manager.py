# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: shmulika

from glob import iglob
import datetime
import distutils.dir_util
import os
import re
import shutil
import statvfs
import subprocess as originalsubprocess
import time

from a.infra.basic.return_codes import ReturnCodes
import a.infra.format.json
import a.infra.process
import a.infra.process.captain
import a.infra.subprocess
import a.sys.boot.utils
import a.sys.mng.bash_log.server
import a.sys.secure_digital.utils
import a.sys.vital.platform
import a.sys.vital.validity

import rfs_installer

# Bypass for PyChecker
if  __package__ is None:
    G_MODULE_NAME_SECURE_DIGITAL                  = "unknown"
    G_GROUP_NAME_SECURE_DIGITAL_MANAGER           = "unknown"
else:
    from . import G_MODULE_NAME_SECURE_DIGITAL      
    from . import G_GROUP_NAME_SECURE_DIGITAL_MANAGER 



class SdManagerError(Exception):
    def __init__ (self, msg):
        Exception.__init__(self, msg)

class SdManager(object):

    # TODO(shmulika): remove from code commented-out code like "rm -rf" and "cp -f", when sure of changes

    RPM_REMOVE_EXPECTED_ERR_MSG = "Stopping system message bus: [FAILED]"
    DEAFULT_KILL_TIMEOUT        = 180
    DEAFULT_WARNING_TIMEOUT     = 90

    RECOVERY_PACKAGE_FILENAME = "qb-secure-digital-recovery.qosp"
    INSTALL_RECOVERY_PACKAGE = "install/0/var/api/secure-digital-recovery-package/qb-secure-digital-recovery.qosp"
    KRUSTY_JSON_FILNAME =  "krusty.json"

    SLEEP_INTERVAL_BETWEEN_BLK_COMMANDS = 2 # seconds

    DEFAULT_CARD_READER_DEVICE_MODEL = "USB CARD READER"

#-----------------------------------------------------------------------------#

    ######################################
    # INITIALIZATION INTERFACE
    ######################################

    def __init__ (self, logger, isExternalSD = False, platformType = None, cardReaderDeviceModel = None):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_SECURE_DIGITAL_MANAGER)

        self._systemDiskVitalDir = a.infra.process.substitueSystemKnownPaths("%s"%a.infra.process.captain.Captain.PATH_SUBSITUTION_KEY_VITAL_PATH)

        self._krustyBaseDir      = a.infra.process.substitueSystemKnownPaths(os.path.join(a.infra.process.captain.Captain.PATH_SUBSITUTION_KEY_APPLICATIONS_PATH, "krusty_install"))
        self._krustyTarFilename  = os.path.join(self._krustyBaseDir, "krusty-sys.tar")

        self._availableKrustyJsonFilepath = os.path.join(self._krustyBaseDir, self.KRUSTY_JSON_FILNAME)
        self._installedKrustyJsonRelativeFilepath = os.path.join("sd-sys/krusty", self.KRUSTY_JSON_FILNAME)

        self._qbPackageFilename = a.infra.process.substitueSystemKnownPaths(os.path.join(a.infra.process.captain.Captain.PATH_SUBSITUTION_KEY_APPLICATION_SYS_PATH, self.INSTALL_RECOVERY_PACKAGE))
        
        self._lastErrMsg = ""

        self._isExternalSD = isExternalSD

        self._initUtils(isExternalSD, platformType, cardReaderDeviceModel)                
        self._initDone()


    def _initUtils (self, isExternalSD, platformType, cardReaderDeviceModel):
        if isExternalSD:
            self._log("init-utils").notice("initializing sd-utils and boot-utils for external secure digital, platformTypes=%s, cardReaderDeviceModel=%s:", platformType, cardReaderDeviceModel)
            sdUtils   = a.sys.secure_digital.utils.SdUtils(self._log)
            bootUtils = a.sys.boot.utils.BootUtils.s_getFromOsefOrCrash(a.infra.process.getOsef())            
            if cardReaderDeviceModel is None:
                cardReaderDeviceModel = self.DEFAULT_CARD_READER_DEVICE_MODEL
            self._sdUtils   = sdUtils.createSdUtilsForExternalDevice(platformType, cardReaderDeviceModel)
            self._bootUtils = bootUtils.createBootUtilsForExternalSecureDigital(self._sdUtils, self._sdUtils.getPlatformBasic())
        else:
            self._log("init-utils").notice("initializing sd-utils and boot-utils for internal secure digital:")
            self._sdUtils   = a.sys.secure_digital.utils.SdUtils(self._log)
            self._bootUtils = a.sys.boot.utils.BootUtils.s_getFromOsefOrCrash(a.infra.process.getOsef())

        self._rfsInstaller = rfs_installer.RfsInstaller(self._log, self._sdUtils)


    def _initDone (self):
        """ Called to after all initializations are done.
        """
        if self._sdUtils.isSdIdentified():
            self._partitionDiskNames = self._sdUtils.getPartitionDiskNames()
            self._sdDevice           = self._sdUtils.getSdDevice()
        else:
            self._partitionDiskNames = None
            self._sdDevice           = None

#-----------------------------------------------------------------------------#

    ######################################
    # FUNCTIONALITY INTERFACE
    ######################################

    def getLastErrorMsg (self):
        return self._lastErrMsg

    ### BOOT ACTIONS
    def setBootSystemDisk (self, progressOut):        
        self._log("set-boot-system-disk").notice("about to set system disk as the boot device:")
        rc = self._makeSureValid(sdIdentified = False, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:            
            if not self._bootUtils.isBootDeviceSettable():
                self._log("set-boot-system-disk").notice("boot device is not settable (probably running on a virtual machine).")
                self._setErrorMsg("Boot device cannot be set, must be set manually. See http://wiki.it.qwilt.com/display/dev/Secure+Digital+Installation+and+Recvoery#SecureDigitalInstallationandRecvoery-ChangingBootDevicetoSystemDisk")
                return ReturnCodes.kGeneralError
            else:
                self._writeProgress("* setting system disk as boot device: ", newLine = False ,progressOut = progressOut)
                self._bootUtils.setBootFromSystemDisk()
                self._writeProgress("done.", newLine = True ,progressOut = progressOut)
        except Exception:
            self._log("set-boot-system-disk").exception("exception raised while setting system disk as boot device, operation failed.")
            self._setErrorMsg("failed.")
            return ReturnCodes.kGeneralError
                
        self._log("set-boot-system-disk").notice("successfuly set system disk as the boot device.")        
        return ReturnCodes.kOk


    def setBootSecureDigital (self, progressOut):
        self._log("set-boot-secure-digital").notice("about to set secure digital as the boot device:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = True, bootPartitionValid = True, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            self._sdUtils.lock()
            if not self._bootUtils.isBootDeviceSettable():
                self._log("set-boot-system-disk").notice("boot device is not settable (probably running on a virtual machine).")
                self._setErrorMsg("Boot device cannot be set, must be set manually. See http://wiki.it.qwilt.com/display/dev/Secure+Digital+Installation+and+Recvoery#SecureDigitalInstallationandRecvoery-ChangingBootDevicetoSecureDigital")
                self._sdUtils.unlock()
                return ReturnCodes.kGeneralError
            else:
                self._writeProgress("* setting recovery media as boot device: ", newLine = False ,progressOut = progressOut)
                self._bootUtils.setBootFromSd() 
                self._writeProgress("done.", newLine = True ,progressOut = progressOut)
        except Exception:
            self._sdUtils.unlock()
            self._log("set-boot-secure-digital").exception("exception raised while setting secure digital as boot device, operation failed.")
            self._setErrorMsg("failed.")
            return ReturnCodes.kGeneralError
               
        self._sdUtils.unlock() 
        self._log("set-boot-secure-digital").notice("successfuly set recovery media as the boot device.")        
        return ReturnCodes.kOk


    def dumpBootMethodStatus(self, progressOut):
        # dump current boot device
        rc = self._makeSureValid(sdIdentified = False, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc

        if self._bootUtils.isSecureDigialBootDevice():
            msg = "The recovery media is the boot device"
        elif self._bootUtils.isSystemDiskBootDevice():
            msg = "The system disk is the boot device"
        else:
            msg = "Unable to determine boot device"

        self._log("dump-boot-method-status").notice(msg)
        self._writeProgress(msg, newLine = True ,progressOut = progressOut)

        if not self._bootUtils.isBootDeviceSettable():
            msg = "Notice: unable to set boot device in this platform"
            self._log("dump-boot-method-status").notice(msg)
            self._writeProgress(msg, newLine = True ,progressOut = progressOut)
        
        return ReturnCodes.kOk


    def setSecureDigitalRecoveryOnBoot (self, progressOut, manualRecovery = False):        
        self._log("secure-digital-recovery-on-boot").notice("about to set next boot to be in recovery mode:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = True, bootPartitionValid = True, mainPartitionExist = False, mainPartitionValid = True, krustyValid = True, systemVital = False, vitalPartitionExist = True, vitalPartitionValid = True, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc

        rc = ReturnCodes.kOk
        if not self._bootUtils.isBootDeviceSettable():
            self._log("set-secure-digital-recovery-on-boot").notice("boot device is not settable (probably running on a virtual machine).")
            warningMsg = "Warning: Boot device cannot be set, must be set manually. See http://wiki.it.qwilt.com/display/dev/Secure+Digital+Installation+and+Recvoery#SecureDigitalInstallationandRecvoery-ChangingBootDevicetoSecureDigital."
            self._writeProgress(warningMsg, newLine = True ,progressOut = progressOut)
        else:
            rc = self.setBootSecureDigital(progressOut)
            if rc != ReturnCodes.kOk:
                self._setErrorMsg("failed setting recovery media as boot device.")
                return rc

        try:
            if manualRecovery:
                bootOptionTag = "krusty_manual"
                bootOnce = True                
                progressMsg = "* setting next boot to manual Recovery & Installation mode: "
            else:
                bootOptionTag = "krusty_automatic"
                bootOnce = False
                progressMsg = "* setting next boot to automatic system restoration to factory default: "
            
            self._writeProgress(progressMsg, newLine = False ,progressOut = progressOut)
            if bootOnce:
                # when booting once - first make sure the default boot is the normal Oscar option
                # because after the "once" boot, the system will boot the previously default option (we don't want that to be Krusty obviously...)
                self._bootUtils.updateSecureDigitalGrubConf(allowKrustyBootOptions = True)
            self._bootUtils.updateSecureDigitalGrubConf(allowKrustyBootOptions = True, defaultBootOptionTag = bootOptionTag, bootOnce = bootOnce)
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)
        except Exception:
            self._log("set-secure-digital-recovery-on-boot").exception("exception raised while setting secure digital recovery on next boot, operation failed.")
            self._setErrorMsg("failed.")
            return ReturnCodes.kGeneralError
                
        self._log("set-secure-digital-recovery-on-boot").notice("successfuly set secure digital recovery on next boot.")        
        return rc


    def unsetSecureDigitalRecoveryOnBoot (self, progressOut):        
        self._log("unset-secure-digital-recovery-on-boot").notice("about to un-set next boot from being recovery mode:")
        rc = self._makeSureValid(sdIdentified = False, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc

        try:
            self._writeProgress(" * setting next boot to normal QB system launch", newLine = False ,progressOut = progressOut)
            self._bootUtils.updateSecureDigitalGrubConf(allowKrustyBootOptions = True)
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)
        except Exception:
            self._log("unset-secure-digital-recovery-on-boot").exception("exception raised while unsetting secure digital recovery on next boot, operation failed.")
            self._setErrorMsg("failed.")
            return ReturnCodes.kGeneralError
                
        self._log("unset-secure-digital-recovery-on-boot").notice("successfuly unset secure digital recovery on next boot (will boot normally).")        
        return ReturnCodes.kOk

    ### RECOVERY MEDIA ACTIONS - FOR TECH USER

    def reInstallEntireSecureDigital (self, progressOut):
        self._log("reinstall-sd").notice("about to re-install the contents of the recovery media. All existing content will be deleted:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = True, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            self._sdUtils.lock()

            # Read logs/history of (possibly) existing secure digital 
            self._readLogsAndHistoryFromSecureDigital()
            
            # Reformat the entire SD
            self._writeProgress("* wiping any existing content from recovery media, recreating partitions: ", newLine = False ,progressOut = progressOut)
            self._invalidateAndWipeSecureDigital()
            self._createAndMkfsSdPartitions()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)
    
            # Rebuild the boot partition
            self._writeProgress("* installing the boot partition: ", newLine = False ,progressOut = progressOut)
            self._installBootPartitionAndSet(allowKrustyBootOptions = False)
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)           
    
            # Rebuild the vital partition
            self._installSdVital(progressOut)
    
            # Rebuid the main (Krusty) partition
            self._writeProgress("* installing the main partition (recovery media software): ", newLine = False ,progressOut = progressOut)                
            self._installMainAndKrusty(progressOut = progressOut)
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)           

            # Save old logs/history of (possibly) prior existing secure digital in the re-built secure digital
            self._saveOldLogsAndHistoryToSecureDigital()


        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("reinstall-sd").exception("exception raised during sd installation, operation failed. unmounting all the sd partitions.")
            self._setErrorMsg("recovery media installation failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("reinstall-sd").notice("successfuly re-installed the contents of the recovery media.")        
        return ReturnCodes.kOk


    def reInstallEntireExternalSecureDigital (self, progressOut, packageFilename):
        self._log("reinstall-external-sd").notice("about to re-install the contents of an external recovery media. All existing content will be deleted:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = True, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = False, externalSd = True)
        if rc != ReturnCodes.kOk:
            return rc

        if packageFilename is None:
            self._log("reinstall-external-sd").warning("package filename was not specified for re-installation of an external recovery media, cannot continue.")
            self._setErrorMsg("software package filename must be specified.")
            return ReturnCodes.kGeneralError
        
        try:
            # Reformat the entire SD
            self._writeProgress("* wiping any existing content from external recovery media, recreating partitions: ", newLine = False ,progressOut = progressOut)
            self._invalidateAndWipeExternalSecureDigital()
            self._createAndMkfsSdPartitions()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)
                
            # Rebuild the vital partition
            self._installUniqueSdVital(progressOut)
    
            # Rebuid the main (Krusty) partition
            self._writeProgress("* installing the main partition (recovery media software): ", newLine = False ,progressOut = progressOut)                
            self._installMainAndKrusty(progressOut = progressOut, packageFilename = packageFilename)
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)           

            # Rebuild the boot partition
            self._writeProgress("* installing the boot partition: ", newLine = False ,progressOut = progressOut)
            self._installBootPartition(allowKrustyBootOptions = True, allowOscarBootOptions = False, defaultBootOptionTag = "krusty_automatic")            
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)           

            # Let system sync, to make sure everything is written on secure digital
            self._writeProgress("* making external recovery media safe to remove: ", newLine = False ,progressOut = progressOut)
            self._sdUtils.unmountAllPartitions()
            self._runCommandRaiseIfFail("sync", killTimeout = 900)
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)           

        except Exception:
            self._sdUtils.unmountAllPartitions()
            self._log("reinstall-external-sd").exception("exception raised during sd installation, operation failed. unmounting all the sd partitions.")
            self._setErrorMsg("recovery media installation failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unmountAllPartitions()
        self._log("reinstall-external-sd").notice("successfuly re-installed the contents of the recovery media.")        
        return ReturnCodes.kOk


    def invalidateEntireSecureDigital (self, progressOut):
        self._log("invalidate-entire-secure-digital").notice("about to invalidate the entire secure digital:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)        
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            self._sdUtils.lock()
            self._writeProgress("* invalidating the recovery media: ", newLine = False ,progressOut = progressOut)
            self._bootUtils.setBootFromSystemDisk()
            self._invalidateAllSecureDigital()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)

        except Exception:
            self._sdUtils.unlock()            
            self._sdUtils.unmountAllPartitions()
            self._log("invalidate-entire-secure-digital").exception("exception raised during sd wipe, operation failed. unmounting all the sd partitions.")
            self._setErrorMsg("recovery media invalidation failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("invalidate-entire-secure-digital").notice("successfuly wiped the contents of the recovery media.")        
        return ReturnCodes.kOk


    def invalidateEntireExternalSecureDigital (self, progressOut):
        self._log("invalidate-entire-external-secure-digital").notice("about to invalidate the entire external secure digital:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = False, externalSd = True)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            self._writeProgress("* invalidating the external recovery media: ", newLine = False ,progressOut = progressOut)
            self._invalidateAllSecureDigital()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)

        except Exception:
            self._sdUtils.unmountAllPartitions()
            self._log("invalidate-entire-external-secure-digital").exception("exception raised during external sd wipe, operation failed. unmounting all the external sd partitions.")
            self._setErrorMsg("recovery media invalidation failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unmountAllPartitions()
        self._log("invalidate-entire-external-secure-digital").notice("successfuly wiped the contents of the external recovery media.")        
        return ReturnCodes.kOk


    def reInstallMain (self, progressOut):
        """ reformats the main partition, and re-installs the recovery software (krusty) 
        """
        self._log("re-install-krusty").notice("about to re-install krusty on SD's main partition:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = True, mainPartitionValid = False, krustyValid = False, systemVital = True, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            # Disable Krusty (main partition)
            self._sdUtils.lock()
            self._invalidateAndReInstallMainAndKrusty(progressOut = progressOut)

        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("re-install-krusty").exception("exception raised during krusty installation, operation failed. ")
            self._setErrorMsg("recovery media recovery software installation failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("re-install-krusty").notice("successfuly re-installed krusty.")        
        return ReturnCodes.kOk


    def checkAndUpdateMain (self, progressOut):
        """ checks for major updates for Krusty, and if available - re-install main.
        """
        self._log("check-and-update-main").notice("searching if a new major version of krusty is available:")
        rc = self._makeSureValid(sdIdentified = False, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc

        if not self._sdUtils.isSdDefined():
            self._log("check-and-update-main").notice("secure digital is not available on this platform, nothing to update.")
            return ReturnCodes.kOk

        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = True, mainPartitionValid = True, krustyValid = False, systemVital = True, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:            
            self._sdUtils.lock()            
            if self._isKrustyUpdateRequired():
                self._log("check-and-update-main").notice("krusty upgrade is required - re installing the main partition:")
                self._writeProgress("* major update available, re-installing: ", newLine = True ,progressOut = progressOut)
                self._invalidateAndReInstallMainAndKrusty(progressOut = progressOut)

        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("check-and-update-main").exception("exception raised during krusty check for updates, operation failed. ")
            self._setErrorMsg("recovery media recovery software check-for-updates failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("check-and-update-main").notice("successfuly check-and-updated krusty.")        
        return ReturnCodes.kOk



    def invalidateMain (self, progressOut):
        self._log("invalidate-krusty").notice("about to invalidate krusty on SD's main partition:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = True, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            # Disable Krusty (main partition)
            self._sdUtils.lock()
            self._writeProgress("* invalidating the recovery media software: ", newLine = False ,progressOut = progressOut)                
            self._bootUtils.updateSecureDigitalGrubConf(allowKrustyBootOptions = False)
            self._sdUtils.invalidateKrusty()
            self._sdUtils.invalidateMain()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)           

        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("invalidate-krusty").exception("exception raised during krusty invalidation, operation failed. ")
            self._setErrorMsg("recovery media software invalidation failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("invalidate-krusty").notice("successfuly invalidated krusty.")        
        return ReturnCodes.kOk


    def copyRecoveryPackage (self, progressOut, packageFilename):
        self._log("copy-recovery-package").notice("about to copy recovery qosp package to sceure digital:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = True, mainPartitionValid = True, krustyValid = True, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            self._sdUtils.lock()
            self._writeProgress("* updating recovery software package: ", newLine = False ,progressOut = progressOut)                
            self._copyQbPackageFile(progressOut, packageFilename)
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)

        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("copy-recovery-package").exception("exception raised during while copying recovery software-package file.")
            self._setErrorMsg("failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("copy-recovery-package").notice("successfuly copied recovery package.")        
        return ReturnCodes.kOk


    def invalidateRecoveryPackage (self, progressOut):
        self._log("copy-recovery-package").notice("about to invalidate recovery qosp package on sceure digital:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = True, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            self._sdUtils.lock()
            self._writeProgress("* invalidating recovery software package: ", newLine = False ,progressOut = progressOut)                
            self._sdUtils.mountMainPartition()
            packageValidity = self._getSecureDigitalRecoveryPackageValidity()
            packageValidity.markInvalid()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)

        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("copy-recovery-package").exception("exception raised during while copying invalidating package file.")
            self._setErrorMsg("failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("copy-recovery-package").notice("successfuly copied recovery package.")        
        return ReturnCodes.kOk


    def reInstallVital (self, progressOut):
        self._log("re-install-vital").notice("about to re-install secure digital vital partition:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = True, vitalPartitionExist = True, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            # Disable Krusty (main partition)
            self._sdUtils.lock()
            self._writeProgress("* re-installing the recovery media vital partition: ", newLine = False ,progressOut = progressOut)                
            self._installSdVital(progressOut)
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)           

        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("re-install-vital").exception("exception raised during vital re-install, operation failed.")
            self._setErrorMsg("failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("re-install-vital").notice("successfuly re-installed secure digital vital.")        
        return ReturnCodes.kOk


    def invalidateVital (self, progressOut):
        self._log("invalidate-vital").notice("about to invalidate secure digital vital partition:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = True, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            # Disable Krusty (main partition)
            self._sdUtils.lock()
            self._writeProgress("* invalidating the recovery media vital partition: ", newLine = False ,progressOut = progressOut)                
            self._sdUtils.invalidateVital()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)           

        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("invalidate-vital").exception("exception raised during vital invalidation, operation failed.")
            self._setErrorMsg("failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("invalidate-vital").notice("successfuly invalidated secure digital vital.")        
        return ReturnCodes.kOk


    def dumpSecureDigitalStatus (self, progressOut):
        # Check if Secure digital was identified
        if not self._sdUtils.isSdDefined():
            self._log("check-sd").notice("secure digital is not available on this platform.")
            self._writeProgress("The recovery media device is not supported on this platform", newLine = True ,progressOut = progressOut)
            return ReturnCodes.kOk

        if not self._sdUtils.isSdIdentified():
            self._log("check-sd").notice("SD device was not identified in the system.")
            self._writeProgress("The recovery media device cannot be identified", newLine = True ,progressOut = progressOut)
            return ReturnCodes.kOk

        # dump the linux device
        sdDevice = self._sdUtils.getSdDevice()
        msg = "The recovery media device is: %s" % sdDevice
        self._log("check-sd").notice(msg)
        self._writeProgress(msg, newLine = True ,progressOut = progressOut)
        
        # dump boot partition status
        msg = "The recovery media boot partition is invalid"
        try:
            if self._sdUtils.isBootValid():
                msg = "The recovery media boot partition is valid"                
        except:
            self._log("check-sd").exception("caught exception while trying to check secure digital boot partition")

        self._log("check-sd").notice(msg)
        self._writeProgress(msg, newLine = True ,progressOut = progressOut)

        # dump vital partition status 
        msg = "The recovery media vital partition is invalid"
        try:
            if self._sdUtils.isVitalValid():
                msg = "The recovery media vital partition is valid"
        except:
            self._log("check-sd").exception("caught exception while trying to check secure digital vital partition")

        self._log("check-sd").notice(msg)
        self._writeProgress(msg, newLine = True ,progressOut = progressOut)                

        # dump main partition status 
        mainValid = False
        msg = "The recovery media main partition is invalid"
        try:
            if self._sdUtils.isMainValid():
                mainValid = True
                msg = "The recovery media main partition is valid"
        except:
            self._log("check-sd").exception("caught exception while trying to check secure digital main partition")

        self._log("check-sd").notice(msg)
        self._writeProgress(msg, newLine = True ,progressOut = progressOut)                

        if mainValid:
            # dump recovery package status 
            msg = "Recovery software package is invalid"
            recoveryPackageValidity = self._getSecureDigitalRecoveryPackageValidity()
            if recoveryPackageValidity.isValid():
                msg = "Recovery software package is valid"
    
            self._log("check-sd").notice(msg)
            self._writeProgress(msg, newLine = True ,progressOut = progressOut)

        # dump validity files information
        self._writeDictionaryProgress(newLine = True,  progressOut = progressOut, dictionary = self._sdUtils.getBootValidityDictionary(),   headerMessage = "recovery media boot information:")
        self._writeDictionaryProgress(newLine = False, progressOut = progressOut, dictionary = self._sdUtils.getKrustyVersionDictionary(),  headerMessage = "recovery media software information:")
        self._writeDictionaryProgress(newLine = True,  progressOut = progressOut, dictionary = self._sdUtils.getKrustyValidityDictionary(), headerMessage = None)
        if mainValid:
            self._writeDictionaryProgress(newLine = True, progressOut = progressOut, dictionary = self._getSecureDigitalRecoveryPackageValidityDictionary(), headerMessage = "recovery media software package information:")

        if self._sdUtils.isBootPartitionExist():
            self._sdUtils.mountBootPartition()
            self._writeProgress ("Boot partition usage:  ", newLine = False ,progressOut = progressOut)
            self._writeDirectoryStatvfs(self._sdUtils.getBootPartitionMountPoint(), newLine = True, progressOut = progressOut)

        if self._sdUtils.isFatPartitionExist():
            self._sdUtils.mountFatPartition()
            self._writeProgress ("Fat partition usage:   ", newLine = False ,progressOut = progressOut)
            self._writeDirectoryStatvfs(self._sdUtils.getFatPartitionMountPoint(), newLine = True, progressOut = progressOut)

        if self._sdUtils.isVitalPartitionExist():
            self._sdUtils.mountVitalPartition()
            self._writeProgress ("Vital partition usage: ", newLine = False ,progressOut = progressOut)
            self._writeDirectoryStatvfs(self._sdUtils.getVitalPartitionMountPoint(), newLine = True, progressOut = progressOut)

        if self._sdUtils.isMainPartitionExist():
            self._sdUtils.mountMainPartition()
            self._writeProgress ("Main partition usage:  ", newLine = False ,progressOut = progressOut)
            self._writeDirectoryStatvfs(self._sdUtils.getMainPartitionMountPoint(), newLine = True, progressOut = progressOut)

        self._sdUtils.unmountAllPartitions()
        return ReturnCodes.kOk


    def mountAllPartitions (self, progressOut):
        self._log("mount-all-partitions").notice("about to mount all partitions:")        
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = False, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc

        try:
            self._sdUtils.mountBootPartition()
            msg = "mounted boot partition."
        except Exception:
            msg = "failed mounting boot partition."
        self._log("mount-all-partitions").notice(msg)
        self._writeProgress(msg, newLine = True ,progressOut = progressOut)

        try:
            self._sdUtils.mountFatPartition()
            msg = "mounted fat partition."
        except Exception:
            msg = "failed mounting fat partition."
        self._log("mount-all-partitions").notice(msg)
        self._writeProgress(msg, newLine = True ,progressOut = progressOut)

        try:
            self._sdUtils.mountVitalPartition()
            msg = "mounted vital partition."
        except Exception:
            msg = "failed mounting vital partition."
        self._log("mount-all-partitions").notice(msg)
        self._writeProgress(msg, newLine = True ,progressOut = progressOut)

        try:
            self._sdUtils.mountMainPartition()
            msg = "mounted main partition."
        except Exception:
            msg = "failed mounting main partition."
        self._log("mount-all-partitions").notice(msg)
        self._writeProgress(msg, newLine = True ,progressOut = progressOut)

        return ReturnCodes.kOk


    def umountAllPartitions (self, progressOut):
        __pychecker__  = 'unusednames=progressOut'
        self._log("umount-all-partitions").notice("about to umount all partitions:")        
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = False, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        self._sdUtils.unmountAllPartitions()    
        self._log("umount-all-partitions").notice("successfuly umounted all partitions.")        
        return ReturnCodes.kOk
    

    def wipeEntireSd (self, progressOut):
        """ Completely Wipes the entire secure digital, and does not re-install it.
        All content is deleted, nothing remains
        """

        self._log("wipe-sd").notice("about to wipe the contents of the SD device. All existing content will be deleted:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            self._sdUtils.lock()
            self._writeProgress("* erasing any existing content from recovery media: ", newLine = False ,progressOut = progressOut)
            self._invalidateAndWipeSecureDigital()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)

        except Exception:
            self._sdUtils.unlock()            
            self._sdUtils.unmountAllPartitions()
            self._log("wipe-sd").exception("exception raised during sd wipe, operation failed. unmounting all the sd partitions.")
            self._setErrorMsg("recovery media wipe failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("wipe-sd").notice("successfuly wiped the contents of the SD device.")        
        return ReturnCodes.kOk


    def wipeEntireExternalSd (self, progressOut):
        """ Completely Wipes the entire extneral secure digital, and does not re-install it.
        All content is deleted, nothing remains
        """
        self._log("wipe-external-sd").notice("about to wipe the contents of the external SD device. All existing content will be deleted:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = False, externalSd = True)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            self._writeProgress("* erasing any existing content from external recovery media: ", newLine = False ,progressOut = progressOut)
            self._invalidateAndWipeExternalSecureDigital()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)

        except Exception:
            self._sdUtils.unmountAllPartitions()
            self._log("wipe-external-sd").exception("exception raised during external sd wipe, operation failed. unmounting all the sd partitions.")
            self._setErrorMsg("recovery media wipe failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unmountAllPartitions()
        self._log("wipe-external-sd").notice("successfuly wiped the contents of the external SD device.")        
        return ReturnCodes.kOk


    def dumpBashHistory (self, progressOut):
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = True, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        self._sdUtils.mountMainPartition()
        mainMountPoint = self._sdUtils.getMainPartitionMountPoint()        
        bashHistorySourceDirectory    = os.path.join(mainMountPoint, "sd-data/krusty/data/history/bash")

        if not os.path.exists(bashHistorySourceDirectory):
            self._log("dump-bash-history").notice("directory %s does not exist, faild dumping bash history of the recovery media", bashHistorySourceDirectory)
            self._sdUtils.unmountAllPartitions()
            return ReturnCodes.kGeneralError

        self._log("dump-bash-history").notice("dumping bash history of the recovery media:")        
        self._bashLogServer = a.sys.mng.bash_log.server.Server(self._log)
        self._bashLogServer.initInputFilesDir(bashHistorySourceDirectory)
        self._bashLogServer.initOutputFd(progressOut)
        success = self._bashLogServer.viewLog()
        self._sdUtils.unmountAllPartitions()
        if not success:
            self._log("dump-bash-history").notice("faild dumping bash history of the recovery media")            
            return ReturnCodes.kGeneralError

        self._log("dump-bash-history").notice("successfuly dumped bash history of the recovery media")        
        return ReturnCodes.kOk


    def dumpVarLogMessages (self, progressOut):
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = True, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        self._sdUtils.mountMainPartition()
        mainMountPoint = self._sdUtils.getMainPartitionMountPoint()        
        varLogMessagesSourceGlob = os.path.join(mainMountPoint, "var/log/messages-*")
        varLogMessagesFile       = os.path.join(mainMountPoint, "var/log/messages")

        historyMessagesFiles = [filename for filename in iglob(varLogMessagesSourceGlob)]
        historyMessagesFiles.sort()

        self._log("dump-var-log-messages").notice("dumping content of history files /var/log/messages-*: %s", historyMessagesFiles)
        for filename in historyMessagesFiles:
            self._log("dump-var-log-messages").notice("dumping content of history file %s", filename)
            with open(filename, 'r') as fileIn:
                progressOut.write(fileIn.read())

        if not os.path.exists(varLogMessagesFile):
            self._log("dump-var-log-messages").notice("failed dumping %s, file does not exist", varLogMessagesFile)
        else:
            self._log("dump-var-log-messages").notice("dumping content of messages file %s", varLogMessagesFile)
            with open(varLogMessagesFile, 'r') as fileIn:
                progressOut.write(fileIn.read())

        self._sdUtils.unmountAllPartitions()
        self._log("dump-var-log-messages").notice("successfuly dumped /var/log/messages of the recovery media")        
        return ReturnCodes.kOk


    ### RECOVERY MEDIA ACTIONS - FOR DEBUG USAGE ONLY

    def reInstallPartitions (self, progressOut):
        self._log("reinstall-partitions").notice("about to re-install the sd partitions. Any existing content will be deleted:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = False, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            self._sdUtils.lock()

            # Read logs/history of (possibly) existing secure digital 
            self._readLogsAndHistoryFromSecureDigital()
            
            # Reformat the entire SD
            self._writeProgress("* wiping any existing content from recovery media, recreating partitions: ", newLine = False ,progressOut = progressOut)
            self._invalidateAndWipeSecureDigital()
            self._createAndMkfsSdPartitions()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)

            # Save old logs/history of (possibly) prior existing secure digital in the re-built secure digital
            self._saveOldLogsAndHistoryToSecureDigital()

        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("reinstall-partitions").exception("exception raised during sd partitions installation, operation failed. unmounting all the sd partitions.")
            self._setErrorMsg("recovery media partitions installation failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("reinstall-partitions").notice("successfuly re-installed the SD partitions.")        
        return ReturnCodes.kOk

    
    def invalidateBoot (self, progressOut):
        self._log("invalidate-boot").notice("about to invalidate the SD boot partition:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = True, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            # Disable the SD boot
            self._sdUtils.lock()
            self._writeProgress("* invalidating the boot partition, setting system disk as boot device: ", newLine = False ,progressOut = progressOut)                
            self._bootUtils.setBootFromSystemDisk()
            self._sdUtils.invalidateBoot()
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)           

        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("invalidate-boot").exception("exception raised during sd boot invalidation, operation failed. unmounting the sd boot partition.")
            self._setErrorMsg("recovery media boot partition invalidation failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("invalidate-boot").notice("successfuly invalidated SD boot partition.")        
        return ReturnCodes.kOk


    def reInstallBoot (self, progressOut):
        self._log("reinstall-boot").notice("about to re-install the SD boot partition. Any existing content will be deleted:")
        rc = self._makeSureValid(sdIdentified = True, bootPartitionExist = True, bootPartitionValid = False, mainPartitionExist = False, mainPartitionValid = False, krustyValid = False, systemVital = False, vitalPartitionExist = False, vitalPartitionValid = False, internalSd = True, externalSd = False)
        if rc != ReturnCodes.kOk:
            return rc
        
        try:
            # Disable the SD boot
            self._sdUtils.lock()
            self._bootUtils.setBootFromSystemDisk()
            self._sdUtils.invalidateBoot()
            self._sdUtils.unmountBootPartition()

            # Reformat and rebuild the SD boot partition
            self._writeProgress("* re-installing the boot partition (existing content lost): ", newLine = False ,progressOut = progressOut)
            self._mkfsSdBootPartition()
            self._installBootPartitionAndSet(allowKrustyBootOptions = self._sdUtils.isKrustyValid())
            self._writeProgress("done.", newLine = True ,progressOut = progressOut)

        except Exception:
            self._sdUtils.unlock()
            self._sdUtils.unmountAllPartitions()
            self._log("reinstall-boot").exception("exception raised during sd boot partition installation, operation failed. unmounting the sd boot partition.")
            self._setErrorMsg("recovery media boot partition installation failed.")
            return ReturnCodes.kGeneralError
                
        self._sdUtils.unlock()
        self._sdUtils.unmountAllPartitions()
        self._log("reinstall-boot").notice("successfuly re-installed the SD boot partition.")        
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------#
    ######################################
    # MAIN LOGIC PRIVATE
    ######################################

    def _assertIsExternalSd (self):
        if not self._isExternalSD:
            self._log("assert-is-external-sd").error("manager instance not inteded for external Secure Digital, cannot continue.")
            raise SdManagerError("Manager instance not intended for external Secure Digital")

    def _assertIsInternalSd (self):
        if self._isExternalSD:
            self._log("assert-is-internal-sd").error("manager instance not inteded for internal Secure Digital, cannot continue.")
            raise SdManagerError("Manager instance not intended for internal Secure Digital")

    def _makeSureValid (self, sdIdentified, bootPartitionExist, bootPartitionValid, mainPartitionExist, mainPartitionValid, krustyValid, systemVital, vitalPartitionExist, vitalPartitionValid, internalSd, externalSd):
        msg     = None
        isValid = True

        if internalSd and self._isExternalSD:
            msg = "manager instance configured for operations on external secure-digital (not for internal), cannot continue."
            isValid = False

        elif externalSd and not self._isExternalSD:
            msg = "manager instance configured for operations on internal secure-digital (not for external), cannot continue."
            isValid = False

        elif sdIdentified and not self._sdUtils.isSdIdentified():
            msg = "recovery media device was not identified/detected in the system, cannot continue."
            isValid = False

        elif bootPartitionExist and not self._sdUtils.isBootPartitionExist():
            msg = "recovery media boot partition does not exist, cannot continue."
            isValid = False

        elif bootPartitionValid and not self._sdUtils.isBootValid():
            msg = "recovery media boot partition is invalid, cannot continue."
            isValid = False
            
        elif mainPartitionExist and not self._sdUtils.isMainPartitionExist():
            msg = "recovery media main partition does not exist, cannot contiune."
            isValid = False

        elif mainPartitionValid and not self._sdUtils.isMainValid():
            msg = "recovery media main partition is invalid, cannot contiune."
            isValid = False

        elif krustyValid and not self._sdUtils.isKrustyValid():
            msg = "recovery media software is invalid, cannot contiune."
            isValid = False    

        elif systemVital and not a.sys.vital.validity.SysVital(self._log, self._systemDiskVitalDir).isValid():
            msg = "system-disk's vital partition is invalid, cannot continue."
            isValid = False

        if vitalPartitionExist and not self._sdUtils.isVitalPartitionExist():
            msg = "recovery media vital partition does not exist, cannot continue."
            isValid = False

        elif vitalPartitionValid and not self._sdUtils.isVitalValid():
            msg = "recovery media vital partition is invalid, cannot continue."
            isValid = False

        if not isValid:
            self._log("make-sure-valid").notice(msg)
            self._setErrorMsg(msg)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def _setErrorMsg (self, msg):
        self._log("set-error-msg").notice("Error message set to: %s", msg)
        self._lastErrMsg = msg


    def _readLogsAndHistoryFromSecureDigital (self):
        if self._sdUtils.isMainPartitionExist():
            self._sdUtils.mountMainPartition()
            mainMountPoint = self._sdUtils.getMainPartitionMountPoint()        
            tmpDirectory      = "/tmp/secure_digital/previous-installations" # TODO(shmulika): replace this with a directory that nirs will give me
            previousDirectory = os.path.join(mainMountPoint, "sd-data/krusty/data/history/previous-installations")
    
            dateTime                   = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")        
            newSubDirectory            = os.path.join(tmpDirectory, dateTime)
    
            bashHistoryDestDirectory    = os.path.join(newSubDirectory, "bash-history")
            varLogMessagesDestDirectory = os.path.join(newSubDirectory, "var/log")
            #varLogMessagesDestFilename  = os.path.join(newSubDirectory, "var-log-messages")            
    
            bashHistorySourceDirectory    = os.path.join(mainMountPoint, "sd-data/krusty/data/history/bash")            
            varLogMessagesSourceGlob = os.path.join(mainMountPoint, "var/log/messages*")
            #varLogMessagesSourceFilename = os.path.join(mainMountPoint, "var/log/messages")
        
            self._removeAndCreateDir(tmpDirectory)
    
            if os.path.exists(previousDirectory):
                distutils.dir_util.copy_tree(previousDirectory, tmpDirectory, preserve_symlinks = 1)
            
            os.makedirs(newSubDirectory)        
            os.makedirs(varLogMessagesDestDirectory)
    
            if os.path.exists(bashHistorySourceDirectory):
                distutils.dir_util.copy_tree(bashHistorySourceDirectory, bashHistoryDestDirectory, preserve_symlinks = 1)            

            for sourceFilepath in iglob(varLogMessagesSourceGlob):
                dirpath, filename = os.path.split(sourceFilepath)
                destFilepath = os.path.join(varLogMessagesDestDirectory, filename)
                shutil.copyfile(sourceFilepath, destFilepath)

#            if os.path.exists(varLogMessagesSourceFilename):
#                shutil.copyfile(varLogMessagesSourceFilename, varLogMessagesDestFilename)


    def _saveOldLogsAndHistoryToSecureDigital (self):
        self._sdUtils.mountMainPartition()
        mainMountPoint = self._sdUtils.getMainPartitionMountPoint()        
        tmpDirectory      = "/tmp/secure_digital/previous-installations" # TODO(shmulika): replace this with a directory that nirs will give me
        newDirectory = os.path.join(mainMountPoint, "sd-data/krusty/data/history/previous-installations")

        if os.path.exists(tmpDirectory):
            os.makedirs(newDirectory)
    
            distutils.dir_util.copy_tree(tmpDirectory, newDirectory, preserve_symlinks = 1)
    
            shutil.rmtree(tmpDirectory)
    

    def _invalidateAndWipeSecureDigital (self):
        self._log("invalidate-and-wipe-secure-digital").notice("invalidating and wiping secure digital:")        
        self._log("invalidate-and-wipe-secure-digital").notice("setting system disk as boot device:")
        self._bootUtils.setBootFromSystemDisk()
        self._invalidateAllSecureDigital()    
        self._wipeSdDevice() # Reformat the entire SD
        self._log("invalidate-and-wipe-secure-digital").notice("succesfully invalidated and wiped secure digital:")        


    def _invalidateAndWipeExternalSecureDigital (self):
        self._log("invalidate-and-wipe-secure-digital").notice("invalidating and wiping secure digital:")        
        self._invalidateAllSecureDigital()    
        self._wipeSdDevice() # Reformat the entire SD
        self._log("invalidate-and-wipe-secure-digital").notice("succesfully invalidated and wiped secure digital:")        


    def _invalidateAllSecureDigital (self):
        self._log("invalidate-all-secure-digital").notice("invalidating all SD's partitions and directories:")        
        self._sdUtils.invalidateMain()
        self._sdUtils.invalidateKrusty()
        self._sdUtils.invalidateBoot()
        self._sdUtils.invalidateVital()
        self._sdUtils.unmountAllPartitions()
        self._log("invalidate-all-secure-digital").notice("succesfully invalidated all SD's partitions and directories.")        


    def _wipeSdDevice (self):
        self._log("wipe-sd-device").notice("about to wipe (format) the SD device:")                
        self._wipeDevice(self._sdDevice)
        self._runCommandAndUdevSettle("parted %s mklabel msdos --script" % (self._sdDevice))         # recreate the sys-disk label
        self._log("wipe-sd-device").notice("successfuly wiped the SD device.")


    def _wipeSdMainPartition (self):
        self._log("wipe-sd-device").notice("about to wipe (format) the SD's  main partition:")
        mainPartitionDevice = self._sdUtils.getMainPartitionDevice()
        self._sdUtils.unmountMainPartition()
        self._wipeDevice(mainPartitionDevice)
        self._log("wipe-sd-device").notice("successfuly wiped the SD's  main partition.")


    def _wipeDevice (self, device, countBlocks = 20480):
        # Wipe first blocks of a device (default is 20480 blocks of 512B = 10MB)
        self._log("wipe-device").notice("about to wipe device %s:" % device)
        self._runCommandAndUdevSettle("dd if=/dev/zero of=%s bs=512 count=%s" % (device, countBlocks)) # clear 10MB of device
        self._runCommandAndUdevSettle("blockdev --rereadpt %s" % (device))                             # make the system re-read the partition table of the device (so it notices its wiped)
        self._log("wipe-device").notice("successfuly wiped device %s." % device)


    def _createAndMkfsSdPartitions (self):
        self._createSdPartitions()
        self._mkfsSdPartitions()


    def _getSdPartitionsDiskNames (self):
        return self._sdUtils.getPartitionDiskNames()


    def _createSdPartitions (self):
        self._log("create-sd-partitions").notice("about to create the partitions of the SD:")
        for partitionDiskName in self._getSdPartitionsDiskNames():
            partitionStart = self._sdUtils.getPartitionStart(partitionDiskName)
            partitionEnd   = self._sdUtils.getPartitionEnd(partitionDiskName)
            partitionType  = self._sdUtils.getPartitionType(partitionDiskName)
                
            time.sleep(self.SLEEP_INTERVAL_BETWEEN_BLK_COMMANDS)
            if partitionType is None:
                self._runCommandAndUdevSettle("parted %s mkpart primary %s %s --script" % (self._sdDevice, partitionStart, partitionEnd)) 
            else:
                self._runCommandAndUdevSettle("parted %s mkpart primary %s %s %s --script" % (self._sdDevice, partitionType, partitionStart, partitionEnd)) 

            time.sleep(self.SLEEP_INTERVAL_BETWEEN_BLK_COMMANDS)
            
        self._log("create-sd-partitions").notice("successfuly created the partitions of the SD.")
        

    def _mkfsSdPartitions (self):
        self._log("mkfs-sd-partitions").notice("about to format (mkfs) the partitions of the SD:")
        for partitionDiskName in self._getSdPartitionsDiskNames():
            self._mkfsSdPartitionByDiskName(partitionDiskName)
        self._log("mkfs-sd-partitions").notice("successfuly formatted (mkfs) the partitions of the SD.")


    def _mkfsSdBootPartition (self):
        self._mkfsSdPartitionByDiskName(self._sdUtils.getBootPartitionDiskName())


    def _mkfsSdMainPartition (self):
        self._mkfsSdPartitionByDiskName(self._sdUtils.getMainPartitionDiskName())


    def _mkfsSdPartitionByDiskName (self, partitionDiskName):
        self._log("mkfs-sd-partition-by-disk-name").notice("about to format (mkfs) SD's partition %s:", partitionDiskName)
        partitionDevice       = self._sdUtils.getPartitionDevice(partitionDiskName)
        partitionFilesystem   = self._sdUtils.getPartitionFileSystemType(partitionDiskName)
        partitionLabel        = self._sdUtils.getPartitionFileSystemLabel(partitionDiskName)
        self._createMkfsOnDevice(partitionDevice, partitionFilesystem, partitionLabel)            
        self._log("mkfs-sd-partition-by-disk-name").notice("successfuly formatted (mkfs) SD's partition %s.", partitionDiskName)


    def _installSdVital (self, progressOut):
        self._log("install-sd-vital").notice("about to install SD's vital:")
        self._sdUtils.mountVitalPartition()
        sdVitalMountPoint = self._sdUtils.getVitalPartitionMountPoint()

        if not self._sdUtils.isVitalValid():
            distutils.dir_util.copy_tree(self._systemDiskVitalDir, sdVitalMountPoint, preserve_symlinks = 1)
            # remove the validity file that was copied from HDD
            a.sys.vital.validity.SysVital(self._log, sdVitalMountPoint).markInvalid()
            self._sdUtils.validateVital()  
        else:
            self._writeProgress("vital already valid, not overwriting it (invalidate it first to overwrite). ", newLine = False ,progressOut = progressOut)
            
        self._log("install-sd-vital").notice("successfuly installed SD's vital.")          


    def _installUniqueSdVital (self, progressOut):
        """ installs a unique vital on the Secure Digital (not a copy of this machine's) """
        __pychecker__  = 'unusednames=progressOut'

        self._log("install-unique-sd-vital").notice("about to install unique SD's vital:")
        self._sdUtils.mountVitalPartition()
        sdVitalMountPoint = self._sdUtils.getVitalPartitionMountPoint()
        platformType = self._sdUtils.getPlatformBasic().getPlatformType()
        
        # Installing the platform-vital subdirectory        
        platformDirectory = a.sys.vital.platform.VitalPlatformData.s_getDirectory(sdVitalMountPoint)
        legacyDirectory   = a.sys.vital.platform.VitalPlatformData.s_getLegacyDirectory(sdVitalMountPoint)
        platformVitalData = a.sys.vital.platform.VitalPlatformData()
        os.makedirs(platformDirectory)
        os.makedirs(legacyDirectory)

        # TODO(shmulika): replace with constants, once I know where constants should sit (probably platform basic)
        if platformType == "qb-6b2": 
            platformVitalData.loadAsQb6B2()
        elif platformType == "qb-10b5":
            platformVitalData.loadAsQb10B5()
        else:
            self._log("install-uniqe-sd-vital").notice("vitals of platform type %s not supported. cannot continue", platformType)
            raise SdManagerError("Creating unique vital not supported from platform of type %s" % platformType)

        self._log("install-uniqe-sd-vital").notice("installing platform-vitals of platform type %s on sd:", platformType)
        platformVitalData.saveToFile(a.sys.vital.platform.VitalPlatformData.s_getDefaultFileName(sdVitalMountPoint))
        platformVitalData.saveToLegacyFile(a.sys.vital.platform.VitalPlatformData.s_getLegacyDefaultFileName(sdVitalMountPoint))        

        # Installing the system-vital subdirectory        
        self._log("install-uniqe-sd-vital").notice("installing system-vitals on sd:", platformType)
        systemDirectorySuffix = "system/0/var/sshd" # TODO(shmulika): move functionality to a.sys.vital.* when we know exactly how we want this to look
        systemDirectory = os.path.join(sdVitalMountPoint, systemDirectorySuffix)
        os.makedirs(systemDirectory)

        # TODO(shmulika): move functionality to a.sys.vital.* when we know exactly how we want this to look
        sshdConfigFileSuffix = "sshd_config"
        systemSshdConfigFile = os.path.join(self._systemDiskVitalDir, systemDirectorySuffix, sshdConfigFileSuffix)
        sdSshdConfigFile = os.path.join(systemDirectory, sshdConfigFileSuffix)

        dsaFilePrefix = os.path.join(systemDirectory, "ssh_host_dsa_key")
        rsaFilePrefix = os.path.join(systemDirectory, "ssh_host_rsa_key")
        ver1FilePrefix = os.path.join(systemDirectory, "ssh_host_key")

        shutil.copyfile(systemSshdConfigFile, sdSshdConfigFile) # take the config file as it is.
        allowOverwrite = "y\n" # forces the ssh-keygen to overwrite existing files        
        self._runCommandRaiseIfFail(["ssh-keygen", "-f" ,ver1FilePrefix ,"-t" ,"rsa1", "-N", ""], input=allowOverwrite, killTimeout = 30)
        self._runCommandRaiseIfFail(["ssh-keygen", "-f" ,rsaFilePrefix  ,"-t" ,"rsa", "-N", ""], input=allowOverwrite, killTimeout = 30)
        self._runCommandRaiseIfFail(["ssh-keygen", "-f" ,dsaFilePrefix  ,"-t" ,"dsa", "-N", ""], input=allowOverwrite, killTimeout = 30)

        self._sdUtils.validateVital()

        self._log("install-sd-vital").notice("successfuly installed SD's vital.")          


    def _invalidateAndReInstallMainAndKrusty (self, progressOut):
        self._invalidateMainAndKrusty(progressOut = progressOut)                                
        self._writeProgress("* installing the main partition (recovery media software): ", newLine = False ,progressOut = progressOut)                
        self._mkfsSdMainPartition()
        self._installMainAndKrusty(progressOut = progressOut)
        self._writeProgress("done.", newLine = True ,progressOut = progressOut)           


    def _invalidateMainAndKrusty (self, progressOut):
        __pychecker__  = 'unusednames=progressOut'
        if self._sdUtils.isBootValid():
            self._bootUtils.updateSecureDigitalGrubConf(allowKrustyBootOptions = False)
        self._sdUtils.invalidateMain()
        self._sdUtils.invalidateKrusty()
        self._sdUtils.unmountMainPartition()


    def _installMainAndKrusty (self, progressOut, packageFilename = None):
        self._log("install-sd-main-and-krusty").notice("about to install SD's main partition and application (krusty):")
        self._extractRfs(progressOut = progressOut)
        self._copyKrustyContent()
        self._copyQbPackageFile(progressOut, packageFilename)
        self._sdUtils.validateKrusty()
        self._sdUtils.validateMain()
        if self._sdUtils.isBootValid():
            self._bootUtils.updateSecureDigitalGrubConf(allowKrustyBootOptions = True)
        self._log("install-sd-main-and-krusty").notice("successfuly installed SD's main partition and application (krusty).")


    def _isKrustyUpdateRequired (self):
        availableKrustyVersion = self._getAvailableKrustyMajorVersion()
        installedKrustyVersion = self._getInstalledKrustyMajorVersion()

        if availableKrustyVersion > installedKrustyVersion:
            self._log("is-krusty-update-required").notice("installed krusty major version: %s, available krusty major version: %s; update is required", installedKrustyVersion, availableKrustyVersion)
            return True
        else:
            self._log("is-krusty-update-required").notice("installed krusty major version: %s, available krusty major version: %s; update not required", installedKrustyVersion, availableKrustyVersion)
            return False


    def _getInstalledKrustyMajorVersion (self):
        self._sdUtils.mountMainPartition()
        mountPoint = self._sdUtils.getMainPartitionMountPoint()
        fullKrustyJsonPath = os.path.join(mountPoint, self._installedKrustyJsonRelativeFilepath)
        return self._getKrustyMajorVersionFromJson(fullKrustyJsonPath)


    def _getAvailableKrustyMajorVersion (self):
        return self._getKrustyMajorVersionFromJson(self._availableKrustyJsonFilepath)


    def _getKrustyMajorVersionFromJson (self, filepath):
        krustyData = a.infra.format.json.readFromFile(self._log, filepath)
        fullVersionNumber = int(krustyData["version"])        
        majorVersion = fullVersionNumber // 100
        self._log("get-krusty-major-version-from-json").notice("read version: file %s, version=%s, major=%s" , filepath, fullVersionNumber, majorVersion)
        return majorVersion


    def _extractRfs (self, progressOut):
        self._sdUtils.mountMainPartition()
        sdMainMountPoint = self._sdUtils.getMainPartitionMountPoint()

        self._rfsInstaller.initTargetRfsPath(sdMainMountPoint)
        self._rfsInstaller.initProgressOut(progressOut)
        self._rfsInstaller.install()
        

    def _copyKrustyContent (self):
        self._sdUtils.mountMainPartition()
        sdMainMountPoint    = self._sdUtils.getMainPartitionMountPoint()
        krustyBaseDir       = os.path.join(sdMainMountPoint, "sd-sys")

        #self._runCommandRaiseIfFail("mkdir -p %s" % (krustyBaseDir))
        os.makedirs(krustyBaseDir)        
        self._runCommandRaiseIfFail("tar -xf %s -C %s" % (self._krustyTarFilename, krustyBaseDir), killTimeout = 240)
    

    def _copyQbPackageFile (self, progressOut, packageFilename = None):        
        self._sdUtils.mountMainPartition()
        target = self._getSecureDigitalRecoveryPackageFilename()
        manuallyChosen = True
        if packageFilename is None:
            manuallyChosen = False
            packageFilename = self._qbPackageFilename        

        if not os.path.exists(packageFilename):
            if manuallyChosen:
                msg = "file %s does not exist, cannot update package file. " % packageFilename
            else:
                msg = "no recovery software package prepared for update, cannot continue. "
            self._writeProgress(msg, newLine = False ,progressOut = progressOut)
            self._logErrorAndRaise("package file %s is not a qosp qb-package, cannot continue." % packageFilename)

        packageValidity = self._getSecureDigitalRecoveryPackageValidity()
        
        versionBuild = self._getRecoveryPackageVersion(packageFilename)
        if versionBuild is not None:
            packageValidity.setSoftwareVersionBuild(versionBuild)
            self._log("copy-qb-package-file").notice("version & build of package = %s", versionBuild)

        if not self._isPackageQosp(packageFilename):
            self._logErrorAndRaise("package file %s is not a qosp qb-package, cannot continue." % packageFilename)

        packageValidity.markInvalid()        
        self._runCommandRaiseIfFail("sync", killTimeout = 900)
        self._log("copy-qb-package-file").notice("copying the secure-digital recovery package %s to the secure-digital in %s:" % (packageFilename, target))
        shutil.copyfile(packageFilename, target) #self._runCommandRaiseIfFail("cp -f %s %s" % (packageFilename, target))
        self._runCommandRaiseIfFail("sync", killTimeout = 900)
        packageValidity.markValid(self._getOscarVersionString())


    def _installBootPartitionAndSet (self, allowKrustyBootOptions):
        """ Installs the secure digital's boot partition and set it as the boot device
        """
        self._installBootPartition(allowKrustyBootOptions)
        self._log("install-boot-partition-and-set").notice("setting secure digital as boot device:")
        self._bootUtils.setBootFromSd() 


    def _installBootPartition (self, allowKrustyBootOptions, allowOscarBootOptions = True, defaultBootOptionTag = None):
        """ Installs the secure digital's boot partition and set it as the boot device
        """
        self._log("install-boot-partition").notice("about to install the secure digital's boot partition:")
        self._installGrub()                 
        self._bootUtils.updateSecureDigitalGrubConfOriginal(allowKrustyBootOptions = allowKrustyBootOptions, allowOscarBootOptions = allowOscarBootOptions, defaultBootOptionTag = defaultBootOptionTag)            
        self._bootUtils.updateSecureDigitalGrubConf(allowKrustyBootOptions = allowKrustyBootOptions, allowOscarBootOptions = allowOscarBootOptions, defaultBootOptionTag = defaultBootOptionTag)            
        self._sdUtils.validateBoot()


    def _installGrub (self):
        self._bootUtils.installSecureDigitalGrub()


    def _createMkfsOnDevice (self, device, filesystem, label = None):
        self._log("create-mkfs-on-device").notice("trying to make %s on device %s with label %s:" % (filesystem, device, label))

        self._runCommandRaiseIfFail("sync", killTimeout = 900)
        self._runCommandAndUdevSettle("mke2fs -t %s %s" % (filesystem, device))
        self._runCommandAndUdevSettle("tune2fs -c0 -i0 -ouser_xattr,acl %s" % (device))
        if label is not None:
            self._runCommandAndUdevSettle("e2label %s %s" % (device, label))
        self._runCommandRaiseIfFail("sync", killTimeout = 900)


    def _getSecureDigitalRecoveryPackageVersion (self):
        """ Returns: (version, build) if package file exists and valid, o.w. returns None
        """
        self._sdUtils.mountMainPartition()
        filename = self._getSecureDigitalRecoveryPackageFilename()
        return self._getRecoveryPackageVersion(filename)


    def _getSecureDigitalRecoveryPackageValidityDictionary (self):
        packageValidity = self._getSecureDigitalRecoveryPackageValidity()
        if packageValidity.isValid():
            return packageValidity.getData()
        else:
            return None


    def _getSecureDigitalRecoveryPackageValidity (self):
        packageValidity = SdSoftwarePackageValidity(self._log, self._getSecureDigitalRecoveryPackageDirectory())
        return packageValidity


    def _getSecureDigitalRecoveryPackageFilename (self):
        return os.path.join(self._getSecureDigitalRecoveryPackageDirectory(), self.RECOVERY_PACKAGE_FILENAME)


    def _getSecureDigitalRecoveryPackageDirectory (self):
        sdMainMountPoint = self._sdUtils.getMainPartitionMountPoint()
        return os.path.join(sdMainMountPoint, "sd-tech/package")
        

    def _getRecoveryPackageVersion (self, filename):
        """ Returns: version if package file exists and valid, o.w. returns None
        """
        if not os.path.exists(filename):
            return None
            
        (rpmOut, rpmErr) = self._runCommandRaiseIfFail("rpm -qp %s" % filename)
        return rpmOut.rstrip('\n')


    def _isPackageQosp (self, packageFilePath):
        """ Returns: True when package is a qosp package (False o.w.)
        Method:
        Runs rpm on the package file, to determine whether theres an RFS package inside it.
        If there is - it is a qosp package, if not - it's not.
        """
        (rpmOut, rpmErr) = self._runCommandRaiseIfFail("rpm -qlp %s" % packageFilePath)

        rpmLines = rpmOut.splitlines()

        for rpmLine in rpmLines:
            if re.search("^/rfs-", rpmLine) is not None:
                self._log("is-package-qosp").notice("package-file %s is a qosp, contains the following rfs package: %s" % (packageFilePath, rpmLine))
                return True

        self._log("is-package-qosp").notice("package-file %s contains no rfs package, thus not a qosp." % (packageFilePath))
        return False
    

    def _getOscarVersionString (self):
        oscarVersion = a.infra.process.getApplicationVersionUnsafe()
        if oscarVersion is None:
            oscarVersion = "unknown"
        oscarVersionString = "Oscar-%s" % oscarVersion
        return oscarVersionString


#-----------------------------------------------------------------------------#
    ######################################
    # SUB PROCESS PRIVATE UTILS
    ######################################

    # TODO(shmulika): use python interface instead!
    def _removeAndCreateDir(self, dirName):
        if os.path.exists(dirName):
            shutil.rmtree(dirName) #self._runCommandRaiseIfFail("rm -rf %s" % dirName)
        os.makedirs(dirName)   #self._runCommandRaiseIfFail("mkdir -p %s" % dirName)


    def _runCommandAndUdevSettle (self, cmd):
        self._runCommand("udevadm settle")
        self._runCommand("udevadm settle")
        self._runCommand("udevadm settle")
        self._runCommandRaiseIfFail(cmd)


    def _runCommand (self, cmd, killTimeout = DEAFULT_KILL_TIMEOUT, warningTimeout = DEAFULT_WARNING_TIMEOUT, shell = False, input = None):
        subprocess = a.infra.subprocess.Subprocess("secure-digital-manager", self._log)
        args = cmd
        if not shell and not isinstance(args, list):
            args = cmd.split()        
        try:
            self._log("run-command").notice("running command, args=%s", args)

            if input is None:
                stdin = None
            else:
                stdin = originalsubprocess.PIPE

            subprocess.start(args, stdin = stdin, stdout = originalsubprocess.PIPE, stderr = originalsubprocess.PIPE, shell = shell)
            omreportStdout, omreportStderr = subprocess.communicate(input = input, killTimeOut = killTimeout, warningTimeOut = warningTimeout)
            self._log("run-command").notice("command stdout = %s, stderr = %s", omreportStdout, omreportStderr)
        except Exception as exception:
            self._log("run-command").error("Failed executing cmd %s, error=%s", args, exception, exc_info = 1)
            return (1, "", "")
        
        returnCode = subprocess.getReturnCode()                
        self._log("run-command").notice("command rc = %s", returnCode)
        return (returnCode, omreportStdout, omreportStderr)
    

    def _runCommandRaiseIfFail (self, command, killTimeout = DEAFULT_KILL_TIMEOUT, warningTimeout = DEAFULT_WARNING_TIMEOUT, shell=False, input = None):
        """Returns a tuple (outText,errText)"""
        (rc,outText,errText) = self._runCommand(command, killTimeout = killTimeout, warningTimeout = warningTimeout, shell = shell, input = input)
        if rc != 0:            
            self._log("run-command-raising").warning("Command returned '%s', raising exception", rc)
            raise SdManagerError("Failed running command %s" % command)
        return (outText,errText)


#-----------------------------------------------------------------------------#
    ######################################
    # MISC PRIVATE UTILS
    ######################################

    def _writeDirectoryStatvfs (self, path_, newLine = True, progressOut = None):
        statResult = os.statvfs(path_)
        availBytes = statResult[statvfs.F_BAVAIL] * statResult[statvfs.F_BSIZE]
        totalBytes = statResult[statvfs.F_BLOCKS] * statResult[statvfs.F_BSIZE]        
        availMB = availBytes / 1048576.0
        totalMB = totalBytes / 1048576.0
        self._writeProgress("%.2fMB available, out of total %.2fMB" % (availMB, totalMB), newLine = newLine ,progressOut = progressOut)




    def _writeDictionaryProgress (self, newLine = False, progressOut = None, dictionary = None, headerMessage = None):
        if dictionary is not None:
            if headerMessage is not None:
                self._writeProgress(headerMessage, newLine = True ,progressOut = progressOut)
                                                                                                 
            if 'version' in dictionary:                                                          
                self._writeProgress("Version:             %s" % dictionary['version'],           newLine = True ,progressOut = progressOut)
                                                                                                 
            if 'format-version' in dictionary:
                self._writeProgress("Format version:      %s" % dictionary['format-version'],    newLine = True ,progressOut = progressOut)

            if 'creation-date-utc' in dictionary:
                self._writeProgress("Creation date (UTC): %s" % dictionary['creation-date-utc'], newLine = True ,progressOut = progressOut)

            if 'creator' in dictionary:
                self._writeProgress("Creator:             %s" % dictionary['creator'],           newLine = True ,progressOut = progressOut)

            if newLine:
                self._writeProgress("", newLine = True ,progressOut = progressOut)


    def _writeProgress (self, message, newLine ,progressOut = None):
        if progressOut is not None:
            progressOut.write(message)
            if newLine:
                progressOut.write("\n")
            progressOut.flush()


    def _logErrorAndRaise (self, msg):        
        msg = "sd-manager error occured: %s" % msg
        self._log("log-error-and-raise").error(msg)
        raise SdManagerError(msg) 


    def _removeRootFromPath (self, pathString):
        if len(pathString) == 0:
            return pathString
        if pathString[0] == "/":
            return pathString[1:]
        else:
            return pathString


#-----------------------------------------------------------------------------#
    ######################################
    # UTILITY CLASSES
    ######################################

class SdSoftwarePackageValidity(a.infra.misc.marker_file.ValidityMarker):
    def __init__ (self, logger, directory):
        a.infra.misc.marker_file.ValidityMarker.__init__(self, logger, os.path.join(directory, "software-package.json"), instance="sd-software-package")
        self._version = "unknown"

    def setSoftwareVersionBuild (self, version):
        self._version  = version


    def getVersion (self):
        return self._version

    def getData (self):
        data = a.infra.misc.marker_file.ValidityMarker.getData(self)
        self._version  = data['version'] 
        return data

    def _createData (self, creatorString):
        baseDictionary = a.infra.misc.marker_file.ValidityMarker._createData(self, creatorString)
        baseDictionary['version']  = self._version  
        return baseDictionary

        


