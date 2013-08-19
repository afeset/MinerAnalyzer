# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: shmulika

import datetime
import fcntl
import os
import shutil
import subprocess as originalsubprocess

from   a.infra.basic.return_codes import ReturnCodes
import a.infra.format.json
import a.infra.process
import a.infra.subprocess

import a.sys.vital.validity

# Bypass for PyChecker
if  __package__ is None:
    G_MODULE_NAME_SECURE_DIGITAL                  = "unknown"
    G_GROUP_NAME_SECURE_DIGITAL_UTILS             = "unknown"
else:
    from . import G_MODULE_NAME_SECURE_DIGITAL      
    from . import G_GROUP_NAME_SECURE_DIGITAL_UTILS 


class SdUtilsError(Exception):
    def __init__ (self, msg):
        Exception.__init__(self, msg)


class SdUtils(object):
    """ The SD Utils class is responsible for:
     - Identifying (detecting) the SD device in the system.
     - Knowing the status of the SD (whether it's valid or invalid)
     - Mounting/unmounting its partitions
     - Provides a lock for accessing the SD

    Notice this class is also used by Pilot (via PilotServices), and thus is responsbile for maitaining backward-compatability.
    For this reason - Pilot has its own Interface methods, which are the methods that must maintain backward-compatability for Pilot.
    """

    # TODO(shmulika): remove from code commented-out code like "rm -rf" and "cp -f", when sure of changes

    DEAFULT_KILL_TIMEOUT    = 180
    DEAFULT_WARNING_TIMEOUT = 90

#-----------------------------------------------------------------------------#

    ######################################
    # INITIALIZATION INTERFACE
    ######################################
    
    BOOT_STATUS_FILE_SUFFIX           = "sd-boot.json"
    KRUSTY_INSTALLATION_FILE_SUFFIX   = "sd-sys/krusty/installation.json"
    KRUSTY_VERSION_FILE_SUFFIX        = "sd-sys/krusty/krusty.json"

    INSTALL_OPERATIONS_LOCK_FILE_SUFFIX = "install/0/run/lock"


    def __init__ (self, logger, platformBasic = None, sdDeviceModel = None, mountPointPrefix = None):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_SECURE_DIGITAL_UTILS)
        self._partitionOsDevice = {}
        self._lockFileName = a.infra.process.substitueSystemKnownPaths(os.path.join(a.infra.process.captain.Captain.PATH_SUBSITUTION_KEY_APPLICATION_SYS_PATH, self.INSTALL_OPERATIONS_LOCK_FILE_SUFFIX))
        
        if platformBasic is None:
            self._platformBasic = a.infra.process.getPlatformBasicDataOrCrash()
        else:
            self._platformBasic = platformBasic
            self._log("init").notice("configured to use platform-basic of platform type: %s", self._platformBasic.getPlatformType())            

        self._mountPointPrefix = mountPointPrefix        
        if self._mountPointPrefix is not None:
            self._log("init").notice("configured to use a mount-point prefix: %s", self._mountPointPrefix)

        self._sdDeviceModel = sdDeviceModel
        if self._sdDeviceModel is not None:
            self._log("init").notice("configured to find SD device model: %s", self._sdDeviceModel)

        self._initDone()
        
        
    def _initDone (self):
        try:
            self._identifySdDevices()
            self._wasSdIdentified = True
        except SdUtilsError:
            self._log("init-done-no-sd").notice("could not identify the SD device, assume no SD card in system")
            self._wasSdIdentified = False


#-----------------------------------------------------------------------------#

    ######################################
    # GETTERS INTERFACE
    ######################################

    def createSdUtilsForExternalDevice (self, platformType, deviceModel):
        """ Creates and returns a sd-utils for an external secure-digital device.
        platformType - type of platform, e.g: a.sys.platform_basic.platform_base.PLATFORM_TYPE_QB_10B5
        deviceModel  - device model of the external device to look for, e.g.: " Storage Device"
        """
        platformBasic = self._platformBasic.createPlatformBasicForPlatformType(platformType)
        return SdUtils(self._log, platformBasic = platformBasic, sdDeviceModel = deviceModel, mountPointPrefix = "external-sd")


    ######################################
    # GETTERS INTERFACE
    ######################################

    def getPlatformBasic (self):
        return self._platformBasic


    def getPartitionDiskNames (self):
        return self._platformBasic.getPartitionsUnderDisk(self.getSdDiskName())


    def getSdDiskName (self):
        return self._platformBasic.DISK_NAME_SD_DISK


    def getBootPartitionDiskName (self):
        return self._platformBasic.DISK_NAME_SD_BOOT 


    def getFatPartitionDiskName (self):
        return self._platformBasic.DISK_NAME_SD_FAT  


    def getVitalPartitionDiskName (self):
        return self._platformBasic.DISK_NAME_SD_VITAL


    def getMainPartitionDiskName (self):
        return self._platformBasic.DISK_NAME_SD_MAIN      


    def getSdDevice (self):
        return self._sdDevice


    def getSdOsDeviceName (self):
        if self._sdDeviceModel is not None:
            # configured to use specific device model
            return None

        sdDiskOsDevice = self._platformBasic.getDiskProperty(self.getSdDiskName(), self._platformBasic.DISK_FIELD_OS_DEVICE)
        if self._platformBasic.isNoneValue(sdDiskOsDevice):
            return None
        return sdDiskOsDevice

    def getSdScsiDisk (self):        
        if self._sdDeviceModel is not None:
            # configured to use specific device model
            return None

        sdDiskScsiDisk = self._platformBasic.getDiskProperty(self.getSdDiskName(), self._platformBasic.DISK_FIELD_SCSI_DISK)
        if self._platformBasic.isNoneValue(sdDiskScsiDisk):
            return None
        return sdDiskScsiDisk

    def getSdDeviceModel (self):         
        if self._sdDeviceModel is not None:
            # configured to use specific device model
            return self._sdDeviceModel

        sdDiskDeviceModel = self._platformBasic.getDiskProperty(self.getSdDiskName(), self._platformBasic.DISK_FIELD_DEVICE_MODEL)
        if self._platformBasic.isNoneValue(sdDiskDeviceModel):
            return None
        return sdDiskDeviceModel

    def getPartitionOsDeviceName (self, partitionDiskName):
        osDevice = self._platformBasic.getDiskProperty(partitionDiskName, self._platformBasic.DISK_FIELD_OS_DEVICE)
        if self._platformBasic.isNoneValue(osDevice):
            return None
        return osDevice

    def getPartitionIndex (self, partitionDiskName):
        return self._platformBasic.getDiskProperty(partitionDiskName, self._platformBasic.DISK_FIELD_INDEX)


    def getPartitionDevice (self, partitionDiskName):
        return self._partitionOsDevice[partitionDiskName]    

    def getPartitionDevices (self):        
        return [self.getPartitionDevice(partitionDiskName) for partitionDiskName in self.getPartitionDiskNames()]        

    def getBootPartitionDevice (self):
        return self.getPartitionDevice(self.getBootPartitionDiskName())

    def getFatPartitionDevice (self):
        return self.getPartitionDevice(self.getFatPartitionDiskName())

    def getVitalPartitionDevice (self):
        return self.getPartitionDevice(self.getVitalPartitionDiskName())

    def getMainPartitionDevice (self):
        return self.getPartitionDevice(self.getMainPartitionDiskName())


    def isBootPartitionExist (self):
        return self._isDeviceExist(self.getBootPartitionDevice())

    def isFatPartitionExist (self):
        return self._isDeviceExist(self.getFatPartitionDevice())

    def isVitalPartitionExist (self):
        return self._isDeviceExist(self.getVitalPartitionDevice())

    def isMainPartitionExist (self):
        return self._isDeviceExist(self.getMainPartitionDevice())


    def getPartitionMountPoint (self, partitionDiskName, noPrefix = False):
        mountPoint = self._platformBasic.getDiskProperty(partitionDiskName, self._platformBasic.DISK_FIELD_MOUNT_POINT)
        if self._mountPointPrefix is not None and not noPrefix:
            if mountPoint[0] == '/':
                mountPoint = mountPoint[1:]                
            if self._mountPointPrefix[0] == '/':
                mountPoint = os.path.join(self._mountPointPrefix, mountPoint)
            else:
                mountPoint = os.path.join('/', self._mountPointPrefix, mountPoint)

        return mountPoint
                
    def getBootPartitionMountPoint (self, noPrefix = False):
        return self.getPartitionMountPoint(self.getBootPartitionDiskName(), noPrefix = noPrefix)

    def getFatPartitionMountPoint (self, noPrefix = False):
        return self.getPartitionMountPoint(self.getFatPartitionDiskName(), noPrefix = noPrefix)

    def getVitalPartitionMountPoint (self, noPrefix = False):
        return self.getPartitionMountPoint(self.getVitalPartitionDiskName(), noPrefix = noPrefix)

    def getMainPartitionMountPoint (self, noPrefix = False):
        return self.getPartitionMountPoint(self.getMainPartitionDiskName(), noPrefix = noPrefix)



    def getPartitionFileSystemLabel (self, partitionDiskName):
        return self._platformBasic.getDiskProperty(partitionDiskName, self._platformBasic.DISK_FIELD_FS_LABEL)
                
    def getBootPartitionFileSystemLabel (self):
        return self.getPartitionFileSystemLabel(self.getBootPartitionDiskName())

    def getFatPartitionFileSystemLabel (self):
        return self.getPartitionFileSystemLabel(self.getFatPartitionDiskName())

    def getVitalPartitionFileSystemLabel (self):
        return self.getPartitionFileSystemLabel(self.getVitalPartitionDiskName())

    def getMainPartitionFileSystemLabel (self):
        return self.getPartitionFileSystemLabel(self.getMainPartitionDiskName())
    

    def getPartitionFileSystemType (self, partitionDiskName):
        return self._platformBasic.getDiskProperty(partitionDiskName, self._platformBasic.DISK_FIELD_FS_TYPE)
                
    def getBootPartitionFileSystemType (self):
        return self.getPartitionFileSystemType(self.getBootPartitionDiskName())

    def getFatPartitionFileSystemType (self):
        return self.getPartitionFileSystemType(self.getFatPartitionDiskName())

    def getVitalPartitionFileSystemType (self):
        return self.getPartitionFileSystemType(self.getVitalPartitionDiskName())

    def getMainPartitionFileSystemType (self):
        return self.getPartitionFileSystemType(self.getMainPartitionDiskName())


    def getPartitionStart (self, partitionDiskName):
        return self._platformBasic.getDiskProperty(partitionDiskName, self._platformBasic.DISK_FIELD_PARTITION_START)

    def getPartitionEnd (self, partitionDiskName):
        return self._platformBasic.getDiskProperty(partitionDiskName, self._platformBasic.DISK_FIELD_PARTITION_END)

    def getPartitionType (self, partitionDiskName):
        partitionType = self._platformBasic.getDiskProperty(partitionDiskName, self._platformBasic.DISK_FIELD_PARTITION_TYPE)
        if self._platformBasic.isNoneValue(partitionType):
            return None
        return partitionType


    def isSdIdentified (self):
        return self._wasSdIdentified

    def isSdDefined (self):
        return self._isSdDeviceDefined()


    def isBootValid (self):
        """ Returns True if the SD boot partition is valid for usage
        """
        if not self._wasSdIdentified:
            self._log("is-boot-valid").notice("secure-digital was not identified, its boot partition is not valid.")
            return False

        if not self.isBootPartitionExist():
            self._log("is-boot-valid").notice("the secure-digital boot partition does not exist (not valid).")
            return False

        try:
            self.mountBootPartition()
        except:
            self._log("is-boot-valid").exception("failed mounting partition, partition is invalid")
            return False

        stateFile = self._getBootInstallationFilePath()
        isValid   = os.path.exists(stateFile)
        if isValid:
            self._log("is-boot-valid").notice("secure-digital boot partition's state file %s exists, the boot partitions is valid.", stateFile)
        else:
            self._log("is-boot-valid").notice("secure-digital boot partition's state file %s does not exist, the boot partitions is invalid.", stateFile)

        return isValid
        

    def isMainValid (self):
        """ Returns True if the SD main partition for is valid
        """
        if not self._wasSdIdentified:
            self._log("is-main-valid").notice("secure-digital was not identified, its main partition is not valid.")
            return False

        if not self.isMainPartitionExist():
            self._log("is-main-valid").notice("the secure-digital main partition does not exist (invalid).")
            return False

        try:
            self.mountMainPartition()
        except:
            self._log("is-main-valid").exception("failed mounting partition, partition is invalid")
            return False
        
        sdMainValidity = self._getMainValidityMarker()       
        isValid = sdMainValidity.isValid()
        if isValid:
            self._log("is-main-valid").notice("secure-digital main partition is valid.")
        else:
            self._log("is-main-valid").notice("secure-digital main partition is invalid.")

        return isValid


    def isKrustyValid (self):
        """ Returns True if the secure digital software (krusty) is valid for usage
        """
        if not self._wasSdIdentified:
            self._log("is-krusty-valid").notice("secure-digital was not identified, its software (krusty) is not valid.")
            return False

        if not self.isMainPartitionExist():
            self._log("is-krusty-valid").notice("the secure digital software does not exist (krusty invalid).")
            return False

        try:
            self.mountMainPartition()
        except:
            self._log("is-krusty-valid").exception("failed mounting partition, partition is invalid")
            return False

        stateFile = self._getKrustyInstallationFilePath()
        isValid   = os.path.exists(stateFile)
        if isValid:
            self._log("is-krusty-valid").notice("secure-digital krusty's state file %s exists, secure digital software  is valid.", stateFile)
        else:
            self._log("is-krusty-valid").notice("secure-digital krusty's state file %s does not exist, secure digital software  is invalid.", stateFile)

        return isValid


    def isVitalValid (self):
        """ Returns True if the SD vital partition for is valid
        """
        if not self._wasSdIdentified:
            self._log("is-vital-valid").notice("secure-digital was not identified, its vital partition is not valid.")
            return False

        if not self.isVitalPartitionExist():
            self._log("is-vital-valid").notice("the secure-digital vital partition does not exist (invalid).")
            return False
        
        try:
            self.mountVitalPartition()
        except:
            self._log("is-vital-valid").exception("failed mounting partition, partition is invalid")
            return False

        sdVitalValidity = self._getVitalValidityMarker()       
        isValid = sdVitalValidity.isValid()
        if isValid:
            self._log("is-vital-valid").notice("secure-digital vital partition is valid.")
        else:
            self._log("is-vital-valid").notice("secure-digital vital partition is invalid.")

        return isValid


    def getBootValidityDictionary (self):
        """ Returns dicitonary if boot validity file exists, o.w. None
        """
        if not self.isBootValid():
            return None

        stateFile = self._getBootInstallationFilePath()
        return self._readDictionaryFromJson(stateFile)


    def getMainValidityDictionary (self):
        """ Returns dictionary if main is valid, o.w. None
        """
        if not self.isMainValid():
            return None
            
        sdMainValidity = self._getMainValidityMarker()
        return sdMainValidity.getData()


    def getVitalValidityDictionary (self):
        """ Returns dictionary if vital is valid, o.w. None
        """
        if not self.isVitalValid():
            return None
            
        sdVitalValidity = self._getVitalValidityMarker()
        return sdVitalValidity.getData()


    def getKrustyValidityDictionary (self):
        """ Returns dicitonary if krusty validity file exists, o.w. None
        """
        if not self.isKrustyValid():
            return None

        stateFile = self._getKrustyInstallationFilePath()
        return self._readDictionaryFromJson(stateFile)


    def getKrustyVersionDictionary (self):
        """ Returns dicitonary if krusty validity file exists, o.w. None
        """
        if not self.isKrustyValid():
            return None

        stateFile = self._getKrustyVersionFilePath()
        return self._readDictionaryFromJson(stateFile)


        
#-----------------------------------------------------------------------------#

    ######################################
    # FUNCTIONALITY INTERFACE
    ######################################

    def lock (self):
        """ Locks secure-digital and software install
        """
        self._createLockFileIfNeeded()
        self._lockHandle=open(self._lockFileName, "r")
        fcntl.flock(self._lockHandle, fcntl.LOCK_EX)


    def unlock (self):
        """ Unlocks secure-digital and software install
        """
        fcntl.flock(self._lockHandle, fcntl.LOCK_UN)
        self._lockHandle.close()


    def invalidateBoot (self):
        """ Invalidates the SD boot partition for usage
        """
        if self.isBootValid():            
            self.mountBootPartition()
            installFilePath = self._getBootInstallationFilePath()
            if os.path.exists(installFilePath):
                os.remove(installFilePath)

            #self._runCommandRaiseIfFail("rm -rf %s" % (self._getBootInstallationFilePath()))
            self._log("invalidate-boot").notice("boot partition is invalidated")
        else:
            self._log("invalidate-boot").notice("boot partition is already invalid")


    def validateBoot (self):
        """ Validates the SD boot partition for usage
        """
        self.mountBootPartition()
        stateDictionary = self._createBootInstallationDictionary()
        self._writeDictionaryAsJson(stateDictionary, self._getBootInstallationFilePath())
        self._log("validate-boot").notice("boot partition is validated")


    def invalidateMain (self):
        """ Invalidates the SD main partition for usage
        """
        if self.isMainValid():
            self.mountMainPartition()
            sdMainValidity = self._getMainValidityMarker()
            sdMainValidity.markInvalid()
            self._log("invalidate-main").notice("main partition is invalidated")
        else:
            self._log("invalidate-main").notice("main partition is already invalid")


    def validateMain (self):
        """ Validates the SD main partition for usage by putting the installation marker file in it.
        """
        self.mountMainPartition()
        sdMainValidity = self._getMainValidityMarker()       
        sdMainValidity.markValid(self._getOscarVersionString())
        self._log("validate-main").notice("main partition is validated")


    def invalidateKrusty (self):
        """ Invalidates the SD krusty (SD software) for usage
        """
        if self.isKrustyValid():
            self.mountMainPartition()

            installFilePath = self._getKrustyInstallationFilePath()
            if os.path.exists(installFilePath):
                os.remove(installFilePath)
            #self._runCommandRaiseIfFail("rm -rf %s" % (self._getKrustyInstallationFilePath()))

            self._log("invalidate-krusty").notice("secure digital software (krusty) is invalidated")
        else:
            self._log("invalidate-krusty").notice("secure digital software (krusty) is already invalid")


    def validateKrusty (self):
        """ Validates the SD krusty partition for usage by putting the installation file in it.
        """
        self.mountMainPartition()
        installDictionary = self._createKrustyInstallationDictionary()
        self._writeDictionaryAsJson(installDictionary, self._getKrustyInstallationFilePath())
        self._log("validate-krusty").notice("secure digital software (krusty) is validated")


    def invalidateVital (self):
        """ Invalidates the SD vital partition for usage
        """
        if self.isVitalValid():
            self.mountVitalPartition()
            sdVitalValidity = self._getVitalValidityMarker()
            sdVitalValidity.markInvalid()
            self._log("invalidate-vital").notice("vital partition is invalidated")
        else:
            self._log("invalidate-vital").notice("vital partition is already invalid")


    def validateVital (self):
        """ Validates the SD vital partition for usage by putting the installation marker file in it.
        """
        self.mountMainPartition()
        sdVitalValidity = self._getVitalValidityMarker()       
        sdVitalValidity.markValid(self._getOscarVersionString())
        self._log("validate-vital").notice("vital partition is validated")

            
    # NOTE for the next unmount methods: When allMountPoints == True, then all the mount-points found for the device will be unmounted
    def mountAllPartitions (self):        
        for partitionDiskName in self.getPartitionDiskNames():
            self._mountPartitionByDiskName(partitionDiskName) 


    def unmountAllPartitions (self, allMountPoints = True):
        for partitionDiskName in self.getPartitionDiskNames():
            self._unmountPartitionByDiskName(partitionDiskName, allMountPoints) 


    def mountBootPartition (self):
        self._mountPartitionByDiskName(self.getBootPartitionDiskName())


    def unmountBootPartition (self, allMountPoints = True):
        self._unmountPartitionByDiskName(self.getBootPartitionDiskName(), allMountPoints)


    def mountFatPartition (self):
        self._mountPartitionByDiskName(self.getFatPartitionDiskName())


    def unmountFatPartition (self, allMountPoints = True):
        self._unmountPartitionByDiskName(self.getFatPartitionDiskName(), allMountPoints)


    def mountVitalPartition (self):
        self._mountPartitionByDiskName(self.getVitalPartitionDiskName())


    def unmountVitalPartition (self, allMountPoints = True):
        self._unmountPartitionByDiskName(self.getVitalPartitionDiskName(), allMountPoints)


    def mountMainPartition (self):
        self._mountPartitionByDiskName(self.getMainPartitionDiskName())


    def unmountMainPartition (self, allMountPoints = True):
        self._unmountPartitionByDiskName(self.getMainPartitionDiskName(), allMountPoints)


#-----------------------------------------------------------------------------#

    ###################################################################################
    # PILOT INTERFACE
    # 
    # Important Note:
    #    This interface must always remain backward compatible,
    #    since there is no strict correspondence between Pilot version & Oscar version.
    #    All pilots must see the same backward-compatible API,
    #    The API can only be expanded - never changed!
    #    If SdUtils functionality is changed, this interface must wrap it and
    #    preserve backward compatability.
    ###################################################################################

    def pilotIsBootValid (self):
        """ Returns True if the SD is valid for usage
        """
        return self.isBootValid()

    def pilotInvalidateBoot (self):
        """ Invalidates the SD for usage
        """
        return self.invalidateBoot()

    def pilotValidateBoot (self):
        """ Validates the SD for usage
        """
        return self.validateBoot()
        
    def pilotLock (self):
        """ Locks the SD (for synchronization)
        """
        return self.unlock()

    def pilotUnlock (self):
        """ Unlocks the SD (for synchronization)
        """
        return self.unlock()

    def pilotMountBootPartition (self):
        self.mountBootPartition()

    def pilotGetBootPartitionMountPoint (self):
        return self.getBootPartitionMountPoint()



#-----------------------------------------------------------------------------#
    ######################################
    # MAIN LOGIC PRIVATE
    ######################################

    def _identifySdDevices (self):
        self._findSdDevice()
        self._findSdPartitionDevice()


    def _isSdDeviceDefined (self):
        # returns true if the SD is defined for this platform           
        sdDiskOsDevice    = self.getSdOsDeviceName()
        sdDiskScsiDisk    = self.getSdScsiDisk()
        sdDiskDeviceModel = self.getSdDeviceModel()

        isSdOsDeviceDefined = sdDiskOsDevice is not None
        isSdScsiDefined   = sdDiskScsiDisk is not None   
        isSdModelDefined  = sdDiskDeviceModel is not None

        self._log("is-sd-device-defined").notice("definition of SD for this platform: sdDiskOsDevice=%s, sdDiskScsiDisk=%s, sdDiskDeviceModel=%s", sdDiskOsDevice, sdDiskScsiDisk, sdDiskDeviceModel)
        
        sdDefinedOnPlatform = isSdOsDeviceDefined or isSdScsiDefined or isSdModelDefined
        if sdDefinedOnPlatform:
            self._log("is-sd-device-defined").notice("secure digital is defined for this platform")
            return True
        else:
            self._log("is-sd-device-defined").notice("secure digital is not defined for this platform")
            return False


    def _findSdDevice (self):
        # find the sd by the SCSI disk if was defined, otherwise by device model.
        sdDiskOsDevice    = self.getSdOsDeviceName()
        sdDiskScsiDisk    = self.getSdScsiDisk()
        sdDiskDeviceModel = self.getSdDeviceModel()

        isSdOsDeviceDefined = sdDiskOsDevice is not None
        isSdScsiDefined = sdDiskScsiDisk is not None   
        isSdModelDefined = sdDiskDeviceModel is not None

        self._log("find-sd-device").notice("definition of SD for this platform: sdDiskOsDevice=%s, sdDiskScsiDisk=%s, sdDiskDeviceModel=%s", sdDiskOsDevice, sdDiskScsiDisk, sdDiskDeviceModel)

        sdDevice = None

        if isSdOsDeviceDefined:
            # The device was specifically given to us in the platform data
            sdDevice = sdDiskOsDevice
            self._log("find-sd-device").notice("SD device %s was given directly in platform_basic data" % sdDevice)

        # The device was not given - need to find it using other information that was given (scsi disk or device model)
        elif isSdScsiDefined:
            sdDevice = self._findDeviceWithScsiDisk(sdDiskScsiDisk)
            if sdDevice is not None:
                sdDevice = "/dev/%s" % sdDevice
                self._log("find-sd-device").notice("SD device %s was deduced from platform_basic data (scsi-disk=%s)" % (sdDevice, sdDiskScsiDisk))

        # Identification by device model is second priority (scsi-disk is stronger if known by platform data)
        elif isSdModelDefined:
            possibleDevices = self._findDevicesWithModel(sdDiskDeviceModel)
            if len(possibleDevices) == 0:
                self._logErrorAndRaise("No SD device detected with the expected device model: %s" % sdDiskDeviceModel)
            elif len(possibleDevices) > 1:
                self._logErrorAndRaise("Found more than one SD device with the expected device model: %s, devices are: %s" % (sdDiskDeviceModel, possibleDevices))
            sdDevice = possibleDevices[0]
            if sdDevice is not None:
                sdDevice = "/dev/%s" % sdDevice
                self._log("find-sd-device").notice("SD device %s was deduced from platform_basic data (device-model=%s)" % (sdDevice, sdDiskDeviceModel))

        else:
            self._logNoticeAndRaise("Cannot find SD - no data (SCSI-disk or device-model) was defined for this platform to enable identifying the device.")

        if sdDevice is None:
            self._logNoticeAndRaise("Failed finding SD device.")

        [notUsed, sdDeviceName] = os.path.split(sdDevice)
        if not self._isDeviceReadyForUse(sdDeviceName):
            self._logNoticeAndRaise("SD device is not ready for use.")

        self._sdDevice = sdDevice


    def _findSdPartitionDevice (self):
        """ this method "calculates" the OS device of the partitions, which may not be known from the platform data
        """
        for partitionDiskName in self.getPartitionDiskNames():
            partitionOsDevice = self.getPartitionOsDeviceName(partitionDiskName)
            partitionIndex    = self.getPartitionIndex(partitionDiskName)

            if partitionOsDevice is None:
                # not given - need to "calculate" it from the sd device and index
                partitionOsDevice = self.getSdDevice() + str(int(partitionIndex) + 1)

            self._log("find-sd-partition-device").notice("found SD partition %s as os device %s", partitionDiskName, partitionOsDevice)
            self._partitionOsDevice[partitionDiskName] = partitionOsDevice

    
#-----------------------------------------------------------------------------#
    ######################################
    # DEVICE IDENTIFICATION PRIVATE UTILS
    ######################################

    def _findDevicesWithModel (self, model):        
        return [device for device in self._getAllBlockDevices() if self._isDeviceOfModel(device, model)]


    def _findDeviceWithScsiDisk (self, scsiDisk):
        for device in self._getAllBlockDevices():
            if self._isDeviceScsiDisk(device, scsiDisk):
                return device
        return None


    def _isDeviceOfModel (self, device, model):        
        deviceModel = self._getBlockDeviceModel(device)
        # TODO(shmulika): perhaps rfind is not the best way to compare file content, think reg-exp
        if deviceModel is not None:
            return deviceModel.rfind(model) > -1
        return False


    def _isDeviceScsiDisk (self, device, scsiDisk):
        deviceScsiDisk = self._getBlockScsiDisk(device)
        # TODO(shmulika): perhaps rfind is not the best way to compare file content, think reg-exp
        if deviceScsiDisk is not None:
            return deviceScsiDisk.rfind(scsiDisk) > -1
        return False


    def _isDeviceReadyForUse (self, device):
        deviceSize = self._getBlockDeviceSize(device)
        self._log("is-device-ready-for-use").notice("device %s size is: %s [sectors, 512B]", device, deviceSize)
        if deviceSize is None or int(deviceSize) < 1: # TODO(shmulika): if this is the method we want, parse the deviceSize string with re.
            self._log("is-device-ready-for-use").notice("device %s is not ready for use", device)
            return False
            
        self._log("is-device-ready-for-use").notice("device %s is ready for use", device)
        return True


    def _getBlockDeviceSize (self, device):
        sizePath = os.path.join("/sys/block", device, "size")
        try:
            with open(sizePath, "r") as fileInput:
                return fileInput.read()
        except:
            return None


    def _getBlockDeviceModel (self, device):
        modelPath = os.path.join("/sys/block", device, "device/model")
        try:
            with open(modelPath, "r") as fileInput:
                return fileInput.read()
        except:
            return None


    def _getBlockScsiDisk (self, device):
        scsiPath = os.path.join("/sys/block", device, "device/scsi_disk")
        scsiDisk = []
        
        try:
            scsiDisk = os.listdir(scsiPath)
        except:
            pass

        if len(scsiDisk) != 1:
            return None

        return scsiDisk[0]


    def _getAllBlockDevices (self):
        return os.listdir("/sys/block")


#-----------------------------------------------------------------------------#
    ######################################
    # VALIDITY/INFO FILES PRIVATE UTILS 
    ######################################

    def _getVitalValidityMarker (self):
        self.mountVitalPartition()
        sdVitalMountPoint = self.getVitalPartitionMountPoint()
        sdVitalValidity = a.sys.vital.validity.SdVital(self._log, sdVitalMountPoint)
        return sdVitalValidity


    def _getMainValidityMarker (self):
        self.mountMainPartition()
        sdMainMountPoint = self.getMainPartitionMountPoint()
        validityFilename = os.path.join(sdMainMountPoint, "sd-main.json")
        sdMainValidity = a.infra.misc.marker_file.ValidityMarker(self._log, validityFilename, instance='sd-main')
        return sdMainValidity
        

    def _getBootInstallationFilePath (self):
        return os.path.join(self.getBootPartitionMountPoint(), self.BOOT_STATUS_FILE_SUFFIX)


    def _getKrustyInstallationFilePath (self):
        return os.path.join(self.getMainPartitionMountPoint(), self.KRUSTY_INSTALLATION_FILE_SUFFIX)

    def _getKrustyVersionFilePath (self):
        return os.path.join(self.getMainPartitionMountPoint(), self.KRUSTY_VERSION_FILE_SUFFIX)


    def _createBootInstallationDictionary (self):
        dictionary = self._createInstallationDictionary()
        dictionary["version"]        = 100  # Hard-coded, this is the only creator of this file
        dictionary["format-version"] = 100
        return dictionary


    def _createKrustyInstallationDictionary (self):
        return self._createInstallationDictionary()


    def _createInstallationDictionary (self):
        oscarVersionString = self._getOscarVersionString()
        dateTime           = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")

        return {"creator"           : oscarVersionString,
                "creation-date-utc" : dateTime}


    def _getOscarVersionString (self):
        oscarVersion = a.infra.process.getApplicationVersionUnsafe()
        if oscarVersion is None:
            oscarVersion = "unknown"
        oscarVersionString = "Oscar-%s" % oscarVersion
        return oscarVersionString
                  

#-----------------------------------------------------------------------------#
    ######################################
    # MOUNT & FS PRIVATE UTILS
    ######################################

    def _isDeviceExist (self, device):
        return os.path.exists(device)


    def _mountPartitionByDiskName (self, partitionDiskName):
        partitionDevice     = self.getPartitionDevice(partitionDiskName)
        partitionMountPoint = self.getPartitionMountPoint(partitionDiskName)
        
        if self._isDeviceMounted(partitionDevice, partitionMountPoint):
            self._log("mount-partition-by-disk-name").notice("partition %s (device=%s) is already mounted - nothing to do", partitionDiskName, partitionDevice)
            return

        self._mountToDirectory(partitionDevice, partitionMountPoint)


    def _unmountPartitionByDiskName (self, partitionDiskName, allMountPoints = True):
        partitionDevice     = self.getPartitionDevice(partitionDiskName)
        partitionMountPoint = self.getPartitionMountPoint(partitionDiskName)

        if allMountPoints:
            if not self._isDeviceMounted(partitionDevice):
                self._log("unmount-partition-by-disk-name").notice("partition %s (device=%s) is not mounted - nothing to do", partitionDiskName, partitionDevice)
                return
                
            self._unmountDevice(partitionDevice)
        else:
            if not self._isDeviceMounted(partitionDevice, mountPoint = partitionMountPoint, singleMountPoint = True):
                self._log("unmount-partition-by-disk-name").notice("partition %s (device=%s) is not mounted on %s - nothing to do", partitionDiskName, partitionDevice, partitionMountPoint)
                return
            
            self._unmountDirectory(partitionMountPoint)


    def _isDeviceMounted (self, device, mountPoint = None, singleMountPoint = False):
        mounts = self._getMountsByDeviceOrDirectory(device = device)
        mountPoints = [mountPoint for (mountDevice, mountPoint) in mounts]

        if len(mounts) == 0:
            self._log("is-device-mounted").notice("device %s is not mounted", device)
            return False

        if mountPoint is None:
            self._log("is-device-mounted").notice("device %s is mounted on these mount-points: %s", device, mountPoints)
            return True
        
        if mountPoint not in mountPoints:
            self._log("is-device-mounted").notice("device %s is not mounted on %s, but on these mount-points: %s", device, mountPoint, mountPoints)
            return False            

        if singleMountPoint and len(mounts) > 1:
            self._log("is-device-mounted").notice("device %s is mounted not only on %s, but on several mount-points: %s", device, mountPoint, mountPoints)
            return False

        self._log("is-device-mounted").notice("device %s is mounted on %s, and on these mount-points: %s", device, mountPoint, mountPoints)
        return True


    def _unmountDevice (self, device):
        mounts = self._getMountsByDeviceOrDirectory(device = device)
        self._log("unmount-device").notice("unmounting all mount-points of device %s, mounts-points = %s", device, mounts)
        for (mountDevice, mountPoint) in mounts:
            self._unmountDirectory(mountPoint)


    def _getMountsByDeviceOrDirectory (self, device = None, directory = None):
        mountList = []
        for (mountDevice, mountPoint) in self._getMountList():
            if (device is not None and mountDevice == device) or (directory is not None and mountPoint == directory):
                mountList.append((mountDevice, mountPoint))

        return mountList


    def _getMountList (self):        
        mountText = self._getMountText()
        mountLines = mountText.splitlines()

        mountList = []
        for line in mountLines:
            words = line.split()
            mountList.append((words[0], words[1]))

        return mountList


    def _getMountText (self):
        with open("/proc/mounts", "r") as fileInput:
            return fileInput.read()


    def _mountToDirectory (self, device, directory):
        if not os.path.exists(directory):
            self._removeAndCreateDir(directory)
        self._runCommandRaiseIfFail("mount %s %s" % (device, directory))


    def _unmountDirectory (self, directory):
        self._runCommand("umount %s" % (directory))


    def _createMkfsOnDevice (self, device, filesystem):
        self._runCommandAndUdevSettle("mke2fs -t %s %s" % (filesystem, device))
        self._runCommandAndUdevSettle("tune2fs -c0 -i0 -ouser_xattr,acl %s" % (device))


    def _removeAndCreateDir(self, dirName):
        if os.path.exists(dirName):
            shutil.rmtree(dirName) #self._runCommandRaiseIfFail("rm -rf %s" % dirName)
        os.makedirs(dirName)   #self._runCommandRaiseIfFail("mkdir -p %s" % dirName)


#-----------------------------------------------------------------------------#
    ######################################
    # LOCKS PRIVATE
    ######################################
    # Note: These are the same locks as those InstallOperations (qb-install/pilot) uses.
    # The shared locks assure us that software install and secure-digital changes aren't done simultanousely
    # (we want to assure it, because they both access the secure-digital's boot partition (grub.conf)
    ######################################

    def _createLockFileIfNeeded (self):
        if not os.path.exists(self._lockFileName):
            self._log("create-lock-file").notice("createLockFileIfNeeded(): Needed. Creating lock file %s." % self._lockFileName)
            f=open(self._lockFileName, "w")
            f.close()



#-----------------------------------------------------------------------------#
    ######################################
    # SUB PROCESS PRIVATE UTILS
    ######################################

    def _runCommandAndUdevSettle (self, cmd):
        self._runCommand("udevadm settle")
        self._runCommandRaiseIfFail(cmd)


  
    def _runCommand (self, cmd, killTimeout = DEAFULT_KILL_TIMEOUT, warningTimeout = DEAFULT_WARNING_TIMEOUT, shell = False):
        subprocess = a.infra.subprocess.Subprocess("boot-utils", self._log)
        args = cmd
        if not shell:
            args = cmd.split()
        
        try:
            subprocess.start(args, stdout = originalsubprocess.PIPE, stderr = originalsubprocess.PIPE, shell = shell)
            omreportStdout, omreportStderr = subprocess.communicate(killTimeOut = killTimeout, warningTimeOut = warningTimeout)
        except Exception as exception:
            self._log("run-command").error("Failed executing cmd %s, error=%s", args, exception, exc_info = 1)
            return (1, "", "")
        
        returnCode = subprocess.getReturnCode()                
        return (returnCode, omreportStdout, omreportStderr)



    def _runCommandRaiseIfFail (self, command, killTimeout = DEAFULT_KILL_TIMEOUT, warningTimeout = DEAFULT_WARNING_TIMEOUT, shell=False):
        """Returns a tuple (outText,errText)"""
        (rc,outText,errText) = self._runCommand(command, killTimeout = killTimeout, warningTimeout = warningTimeout, shell = shell)
        if rc != 0:
            self._log("run-command-raising").warning("Command returned '%s', raising exception", rc)
            raise SdUtilsError("Failed running command %s" % command)
        return (outText,errText)


#-----------------------------------------------------------------------------#
    ######################################
    # MISC PRIVATE UTILS
    ######################################

    def _logErrorAndRaise (self, msg):
        msg = "sd-utils error occured: %s" % msg
        self._log("log-error-and-raise").error(msg)
        raise SdUtilsError(msg) 

    def _logNoticeAndRaise (self, msg):
        self._log("log-notice-and-raise").notice(msg)
        raise SdUtilsError(msg) 


    def _writeDictionaryAsJson (self, dictionary, filename):
        a.infra.format.json.writeToFile(self._log, dictionary, filename, indent=4)


    def _readDictionaryFromJson (self, filename):
        return a.infra.format.json.readFromFile(self._log, filename)

