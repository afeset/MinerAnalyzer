# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz

from threading  import Thread
import a.infra.format.json
from a.infra.basic.return_codes import ReturnCodes
from a.storage.disk import common
import os
import random
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen #  impoting with 'as blinky_generated_enums' causes stupid pycheck warnings
blinky_generated_enums=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen  

__pychecker__ = 'maxrefs=20'
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.file_system_data_gen
blinky_generated_disk_file_system_data=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.file_system_data_gen
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.commands.commands_data_gen
blinky_generated_disk_file_system_commands_data=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.commands.commands_data_gen
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.timeouts.timeouts_data_gen
blinky_generated_disk_file_system_timeouts_data=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.file_system.timeouts.timeouts_data_gen


if  __package__ is None:
    G_NAME_MODULE_STORAGE_DISK = "unknown"
    G_NAME_GROUP_STORAGE_DISK_FILE_SYSTEM = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_DISK
    from . import G_NAME_GROUP_STORAGE_DISK_FILE_SYSTEM


class FileSystem(object):

    # constants
    UUID_ACCEPT_ANY = "any"

    class ActivateData:

        def __init__ (self,mountingPoint,blockDevice,expectedUuid,autoInit,forceInit,blockDeviceReadahead,terminateTimeOut):

            # input params
            self.mountingPoint = mountingPoint
            self.blockDevice = blockDevice
            self.expectedUuid = expectedUuid
            self.autoInit = autoInit
            self.forceInit = forceInit
            self.blockDeviceReadahead = blockDeviceReadahead
            self.timer = common.Timer(terminateTimeOut)

            # intermidiate objects
            self.foundUuid = None
            self.currentUuid = None
            self.shouldUpdateCurrentUuid = False


        def __str__ (self):
            statusDict = {}
            for k,v in self.__dict__.items():
                statusDict[k] = str(v)
            return str(statusDict)


    def __init__ (self,logicalDiskName,logger):

        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_DISK,G_NAME_GROUP_STORAGE_DISK_FILE_SYSTEM)
        self._logicalDiskName = logicalDiskName
        
        # configuration
        self._runningFileSystemConfig   = blinky_generated_disk_file_system_data.FileSystemData() 
        self._candidateFileSystemConfig = blinky_generated_disk_file_system_data.FileSystemData() 
        self._activeFileSystemConfig    = blinky_generated_disk_file_system_data.FileSystemData() 

        self._runningCommandsConfig   = blinky_generated_disk_file_system_commands_data.CommandsData() 
        self._candidateCommandsConfig = blinky_generated_disk_file_system_commands_data.CommandsData() 
        self._activeCommandsConfig    = blinky_generated_disk_file_system_commands_data.CommandsData() 
        
        self._runningTimeoutsConfig   = blinky_generated_disk_file_system_timeouts_data.TimeoutsData()
        self._candidateTimeoutsConfig = blinky_generated_disk_file_system_timeouts_data.TimeoutsData()
        self._activeTimeoutsConfig    = blinky_generated_disk_file_system_timeouts_data.TimeoutsData()

        # state and status
        self._activateData = None
        self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kNone
        self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kNoDevice
        self.fsRawType = ""
        self.fsType = blinky_generated_enums.FileSystemTypeType.kNone



    ## Configuration related functions ##
    
    def diskFileSystemTrxStart (self):
        self._log("disk-file-system-trx-start").debug3("diskFileSystemTrxStart()  was called for file-system %s, running --> candidate",self._logicalDiskName)
        self._candidateFileSystemConfig.copyFrom(self._runningFileSystemConfig)
        self._candidateCommandsConfig.copyFrom(self._runningCommandsConfig)
        self._candidateTimeoutsConfig.copyFrom(self._runningTimeoutsConfig)
        return ReturnCodes.kOk

    def diskFileSystemValueSet (self,data):
        self._log("disk-file-system-value-set").debug3("diskFileSystemValueSet(data=%s)  was called for file-system %s, data --> candidate",data,self._logicalDiskName)
        self._candidateFileSystemConfig.copyFrom(data)
        return ReturnCodes.kOk

    def diskFileSystemCommandsValueSet (self,data):
        self._log("disk-file-system-commands-value-set").debug3("diskFileSystemCommandsValueSet(data=%s)  was called for file-system %s, data --> candidate",data,self._logicalDiskName)
        self._candidateCommandsConfig.copyFrom(data)
        return ReturnCodes.kOk

    def diskFileSystemTimeoutsValueSet (self,data):
        self._log("disk-file-system-timeouts-value-set").debug3("diskFileSystemTimeoutsValueSet(data=%s)  was called for file-system %s, data --> candidate",data,self._logicalDiskName)
        self._candidateTimeoutsConfig.copyFrom(data)
        return ReturnCodes.kOk

    def diskFileSystemTrxCommit (self):
        self._log("disk-file-system-trx-commit").debug3("diskFileSystemTrxCommit()  was called for file-system %s, candidate --> running",self._logicalDiskName)
        self._runningFileSystemConfig.copyFrom(self._candidateFileSystemConfig)
        self._runningCommandsConfig.copyFrom(self._candidateCommandsConfig)
        self._runningTimeoutsConfig.copyFrom(self._candidateTimeoutsConfig)
        return ReturnCodes.kOk

    def diskFileSystemTrxAbort (self):
        self._log("disk-file-system-trx-abort").debug3("diskFileSystemTrxAbort()  was called for file-system %s, None --> candidate",self._logicalDiskName)
        self._candidateFileSystemConfig = None
        self._candidateCommandsConfig   = None
        self._candidateTimeoutsConfig   = None
        return ReturnCodes.kOk


    ## Periodic-work related functions #### Periodic-work related functions ##

    def pushRunningToActiveConfig (self):
        self._log("push-running-to-active").debug3("pushRunningToActiveConfig()  was called for file-system %s, running -- selective --> active",self._logicalDiskName)
        self._activeFileSystemConfig.copyFrom(self._runningFileSystemConfig) # TODO: in future should be selective
        self._activeCommandsConfig.copyFrom(self._runningCommandsConfig) # TODO: in future should be selective
        self._activeTimeoutsConfig.copyFrom(self._runningTimeoutsConfig) # TODO: in future should be selective
        return ReturnCodes.kOk

    def _runCommand (self,cmdString,timer):
        """
        Run a general filesystem related command. 
        """
        return common.runCommand (self._log,cmdString,timer)

    def setInitialActivationParams (self,mountingPoint,expectedUuid,forceInit):
        pass

    def setIntermediateActivationParams (self,blockDevice):
        pass

    def unmount (self):
        pass

    def activatePhase1 (self):
        pass

    def activatePhase2 (self):
        pass

    def activatePhase3 (self):
        pass

    def activatePhase4 (self):
        pass

    def activateGetCurrentUuid (self):
        pass

    def getDetailedStatus (self):
        pass

    def getStatus (self,operData):
        operData.setOperationalStatus(self.operationalStatus)
        operData.setOperationalStatusReason(self.operationalStatusReason)

        operData.setFileSystemType(self.fsType)
        if self.fsRawType:
            operData.setFileSystemTypeRaw(self.fsRawType)

        
        if (self._activateData != None):
            if self._activateData.currentUuid:
                operData.setUuid(str(self._activateData.currentUuid))

            if self._activateData.expectedUuid:
                operData.setExpectedUuid(str(self._activateData.expectedUuid))

        return ReturnCodes.kOk



class ExtFileSystem(FileSystem):
    """
    A class representing a file system
    """

    # mkfs and mount commands params
    BLOCK_DEVICE_COMMAND_ELEMENT = "blockDevice"
    TYPE_COMMAND_ELEMENT = "type"
    MOUNTING_POINT_COMMAND_ELEMENT = "mountingPoint"
    SECTORS_COMMAND_ELEMENT = "sectors"

    class ActivateData(FileSystem.ActivateData):
        
        def __init__ (self,mountingPoint,blockDevice,expectedUuid,autoInit,forceInit,blockDeviceReadahead,terminateTimeOut):
            FileSystem.ActivateData.__init__(self,mountingPoint,blockDevice,expectedUuid,autoInit,forceInit,blockDeviceReadahead,terminateTimeOut)
            
            # mkfs process handle
            self.mkfsThread = None
            self.mkfsRc = None


    def __init__ (self,logicalDiskName,logger):

        # init base class
        FileSystem.__init__(self,logicalDiskName,logger)

        # status
        self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kNone
        self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kNoDevice
        self.fsRawType = ""
        self.fsType = blinky_generated_enums.FileSystemTypeType.kNone


    def _getBlockDeviceUuid (self,blockDevice,timer):
        """
        get the block devices that hold a file system in the form of a dictionary {block_device:fs_uuid}
        """
        endOfBlockDeviceIndicator = ":"
        uuidAttributeIndicator = "UUID=\""
        uuidOffsetFromIndicator = len(uuidAttributeIndicator)
        fsTypeAttributeIndicator = "TYPE=\""
        fsTypeOffsetFromIndicator = len(uuidAttributeIndicator)
        cmdString = "blkid %s"%blockDevice
        stdout,stderr,rc = self._runCommand(cmdString,timer)

        if (rc == 0):
            self._log("blikd-success").debug3("successfully excuted command '%s',\noutput is '%s'",cmdString,stdout)
            line = stdout.strip()
            
            #parse line and get blockDevice and UUID (example line -> /dev/sda1: UUID="995c41e5-4c9d-4d2d-8802-0116bdfd5857" TYPE="ext3")
            endOfBlockDeviceIndex = line.find(endOfBlockDeviceIndicator)
            startOfUuidIndex = line.find(uuidAttributeIndicator) + uuidOffsetFromIndicator
            startOfFsTypeIndex = line.find(fsTypeAttributeIndicator) + fsTypeOffsetFromIndicator
            if ((endOfBlockDeviceIndex != -1) and (startOfUuidIndex != -1)):
                blockDevice = line[:endOfBlockDeviceIndex]
                endOfUuidIndex = line.find("\"",startOfUuidIndex +1)
                uuid = line[startOfUuidIndex:endOfUuidIndex]
                self.fsRawType = ""

                if (startOfFsTypeIndex != -1):
                    endOfFsTypeIndex = line.find("\"",startOfFsTypeIndex +1)
                    self.fsRawType = line[startOfFsTypeIndex:endOfFsTypeIndex]
                    if (self.fsRawType == "ext4"):
                        self.fsType = blinky_generated_enums.FileSystemTypeType.kExt4
                    elif (self.fsRawType == "ext3"):
                        self.fsType = blinky_generated_enums.FileSystemTypeType.kExt3
                    else:
                        self.fsType = blinky_generated_enums.FileSystemTypeType.kOther

                else: # fs type could not be retrieved
                    self.fsType = blinky_generated_enums.FileSystemTypeType.kUnknown

                self._log("parsed-block-device").debug3("block device '%s', UUID='%s' and TYPE='%s' were parsed from line '%s'",blockDevice,uuid,self.fsRawType,line)
                return uuid,ReturnCodes.kOk
            else:
                self._log("bad-output-line-blkid").debug3("line '%s' is non conventional output for '%s' command (skipping it). (endOfBlockDeviceIndex=%d, startOfUuidIndex=%d)",line,cmdString,endOfBlockDeviceIndex,startOfUuidIndex)
                return None,ReturnCodes.kGeneralError

        elif (rc == 2):
            self._log("blikd-success-not-found").debug3("successfully excuted command '%s',no UUID found for block device '%s'",cmdString,blockDevice)
            return None,ReturnCodes.kOk

        else:
            self._log("blikd-fail").error("function _getBlockDeviceUuid('%s') failed --> command '%s' failed!",blockDevice,cmdString)
            return None,ReturnCodes.kGeneralError
    

    def _umount (self,mountingPoint,timer):
        """
        unmount a block device (via mountingPoint)
        """
        cmdString = "umount %s"%mountingPoint

        stdout,stderr,rc = self._runCommand(cmdString,timer)
        if (rc != 0):
            # this may not be bad, if this device was not mounted we are still cool
            acceptableError = "%s: not mounted"%mountingPoint
            if acceptableError in stderr:
                self._log("unneeded-unmount").debug3("unmount for mounting point '%s' was not needed (already not mounted)",mountingPoint)
            else:
                self._log("unmount-failed").error("unmount for mounting point '%s' failed! stderr=%s",mountingPoint,stderr)
                return ReturnCodes.kGeneralError
                
        self._log("unmount-success").debug3("unmount for '%s' succeeded!",mountingPoint)                    
        return ReturnCodes.kOk


    def __joinCmdStringWithExtras (self,cmdString,extras):
        """
        private function for preparing command string with extras
        """
        if (extras != ""):
            self._log("joining-extras").debug4("joining cmd '%s' with extra params '%s'",cmdString,extras)
            cmdString += " " + extras
        return cmdString


    
    def _setReservedBlockPercentage (self,blockDevice,percentage,timer):
        """
        set the reserved block percentage parameter
        """
        if not (0 <= percentage <= 100):
            self._log("bad-param-for-set-reserved").error("%s is no a valid parameter for setting reserved block percentage!",percentage)
            return ReturnCodes.kGeneralError

        setReservedBlockPercentageCmd = "tune2fs -m %d %s"%(percentage,blockDevice)
        stdout,stderr,rc = self._runCommand(setReservedBlockPercentageCmd,timer)
        if (rc != 0):
            self._log("set-reserved-cmd-fail").error("set-reserved-block command '%s' failed! stderr=%s",setReservedBlockPercentageCmd,stderr)
            return ReturnCodes.kGeneralError

        self._log("set-reserved-success").debug2("set-reserved-block ('%s') was successful!",setReservedBlockPercentageCmd)
        return ReturnCodes.kOk


    def _mount (self,blockDevice,mountingPoint,blockDeviceReadahead,timer):
        """
        entire mounting sequence with pre and post commands
        """

        # pre-mount command
        preMountCmd = self._activeCommandsConfig.preMount
        preMountCmdExtras = self._activeCommandsConfig.preMountExtras
        preMountCmdString = self.__joinCmdStringWithExtras(preMountCmd,preMountCmdExtras)
        if (preMountCmdString != ""):
            stdout,stderr,rc = self._runCommand(preMountCmdString,timer)
            if (rc != 0):
                self._log("pre-mount-cmd-fail").error("pre-mount command '%s' failed! stderr=%s",preMountCmdString,stderr)
                return ReturnCodes.kGeneralError

        # mount command
        mountCmd = self._activeCommandsConfig.mount
        mountCmdExtras = self._activeCommandsConfig.mountExtras
        mountCmdString = mountCmd%{self.MOUNTING_POINT_COMMAND_ELEMENT:mountingPoint,self.BLOCK_DEVICE_COMMAND_ELEMENT:blockDevice}
        mountCmdString = self.__joinCmdStringWithExtras(mountCmdString,mountCmdExtras)
        stdout,stderr,rc = self._runCommand(mountCmdString,timer)
        if (rc != 0):
            self._log("mount-cmd-fail").error("mount command '%s' failed! stderr=%s",mountCmdString,stderr)
            # TODO: consider insertion os pre and post commands cancelation commands - since we don't know what they do...
            return ReturnCodes.kGeneralError

        # post-mount command
        postMountCmd = self._activeCommandsConfig.preMount
        postMountCmdExtras = self._activeCommandsConfig.preMountExtras
        postMountCmdString = postMountCmd%{self.BLOCK_DEVICE_COMMAND_ELEMENT:blockDevice,self.SECTORS_COMMAND_ELEMENT:blockDeviceReadahead}
        postMountCmdString = self.__joinCmdStringWithExtras(postMountCmdString,postMountCmdExtras)
        if (postMountCmdString != ""):
            stdout,stderr,rc = self._runCommand(postMountCmdString,timer)
            if (rc != 0):
                self._log("post-mount-cmd-fail").error("post-mount command '%s' failed! stderr=%s",postMountCmdString,stderr)
                return ReturnCodes.kGeneralError

        # full success
        self._log("mount-sequence-success").debug2("full mount sequence was successful!")
        return ReturnCodes.kOk


    def _mkfs (self,blockDevice,timer):
        """
        create the file system on the block device. 
        """
        # build command string
        fsTypeString = None
        if (self._activeFileSystemConfig.fileSystemType == blinky_generated_enums.FileSystemTypeType.kExt3):
            fsTypeString = "ext3"
        if (self._activeFileSystemConfig.fileSystemType == blinky_generated_enums.FileSystemTypeType.kExt4):
            fsTypeString = "ext4"
        else:
            self._log("unsupported-fs-type").error("file system %s doesn't support type %s",self._activeFileSystemConfig.fileSystemType)
            return ReturnCodes.kGeneralError
        
        mkfsCmd = self._activeCommandsConfig.mkfs
        mkfsCmdExtras = self._activeCommandsConfig.mkfsExtras
        cmdString = mkfsCmd%{self.BLOCK_DEVICE_COMMAND_ELEMENT:blockDevice,self.TYPE_COMMAND_ELEMENT:fsTypeString}

        # update with extra parameters
        cmdString = self.__joinCmdStringWithExtras(cmdString,mkfsCmdExtras)

        # run
        stdout,stderr,rc = self._runCommand(cmdString,timer)
        
        if (rc == 0):
            self._log("fs-created").debug2("file system was successfully created on block device '%s'",blockDevice)
            return ReturnCodes.kOk
        else:
            self._log("fs-creation-failed").error("file system creation on block device '%s' failed! stderr=%s",blockDevice,stderr)
            return ReturnCodes.kGeneralError

    def _mkfsWraper (self,blockDevice,timer,rcPointer):
        try:
            # wrap rc in pointer and hand in as input param (since thread object has no return value)
            rcPointer[0] = self._mkfs(blockDevice,timer)

        except Exception,e:
            self._log("mkfs-wraper-fail").error("_mkfsWraper() failed! activateData = %s, exception = '%s'",self._activateData,e)
            rcPointer[0] = ReturnCodes.kGeneralError


    def _mkfsLaunchOnly (self,blockDevice,timer):

        rcPointer = [None]
        mkfsThread = Thread(target=self._mkfsWraper, args=(blockDevice,timer,rcPointer))
        mkfsThread.daemon = True
        mkfsThread.start()
        self._activateData.mkfsThread = mkfsThread
        self._activateData.mkfsRc = rcPointer
        

    def _mkfsWaitOnly (self):
        
        mkfsThread = self._activateData.mkfsThread
        mkfsThread.join()
        rc = self._activateData.mkfsRc[0]
        return rc

    def _tune2fs (self,blockDevice,timer):
        
        cmdString = "tune2fs -l %s"%blockDevice
        stdout,stderr,rc = self._runCommand(cmdString,timer)

        if (rc == 0):
            statusDictionary = {}
            self._log("tune2fs-success").debug4("successfully excuted command '%s',\noutput is '%s'",cmdString,stdout)
            lines = stdout.split("\n")
            for line in lines:
                keyValueSplitIndex = line.find(":")
                if (keyValueSplitIndex != -1):
                    key = line[:keyValueSplitIndex].strip()
                    value = line[keyValueSplitIndex+1:].strip()
                    statusDictionary[key] = value
                    self._log("adding-key-value-to-status-dict").debug3("updating status dictionary for block device '%s'-> statusDictionary['%s'] = '%s'",blockDevice,key,value)

            return statusDictionary,ReturnCodes.kOk
            
        elif (rc==1): # not found (no file system or no such device)
            self._log("tune2fs-cannot-retrieve").debug2("command '%s' could not retrieve data. \nstdout='%s'\nstderr='%s'",cmdString,stdout,stderr)
            return None,ReturnCodes.kOk

        else:
            self._log("tune2fs-fail").debug2("command '%s' failed. \nstdout='%s'\nstderr='%s'",cmdString,stdout,stderr)
            return None,ReturnCodes.kGeneralError


    def setInitialActivationParams (self,mountingPoint,expectedUuid,forceInit):

        # stuff to take from config
        autoInit = self._activeFileSystemConfig.autoInit
        blockDeviceReadahead = self._activeFileSystemConfig.readAhead
        activateTerminateTimeOut = self._activeTimeoutsConfig.activate
        if not self._activeFileSystemConfig.checkUuid:
            expectedUuid = self.UUID_ACCEPT_ANY

        self._activateData = self.ActivateData(mountingPoint,None,expectedUuid,autoInit,forceInit,blockDeviceReadahead,activateTerminateTimeOut)
        self._log("set-initial-activeation-params").debug2("setInitialActivationParams() called for '%s'. activateData = %s",self._logicalDiskName,self._activateData)
        return ReturnCodes.kOk

    def setIntermediateActivationParams (self,blockDevice):
        self._activateData.blockDevice = blockDevice
        self._log("set-intermidiate-activeation-params").debug2("setIntermediateActivationParams() called for '%s'. activateData = %s",self._logicalDiskName,self._activateData)
        self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
        self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kOk
        return ReturnCodes.kOk

    def unmount (self):
        try:
            self._log("unmount").debug3("unmount(). activateData = %s",self._activateData)
            mountingPoint = self._activateData.mountingPoint
            timer = self._activateData.timer
            rc = self._umount(mountingPoint,timer)
            if (rc != ReturnCodes.kOk):
                self._log("fail-on-unmount").error("failed to unmount! activateData = %s",self._activateData)
                self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
                self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kMountError
            return rc

        except Exception,e:
            self._log("unmount-exception").error("unmount() failed! activateData = %s, exception = '%s'",self._activateData,e)
            self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
            self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kUnknown
            return ReturnCodes.kGeneralError


    def activatePhase1 (self):
        
        try:
            # entering phase 1
            self._log("enter-phase1").debug2("entering phase1 for '%s'. activateData = %s",self._logicalDiskName,self._activateData)
            
            blockDevice = self._activateData.blockDevice
            timer = self._activateData.timer

            # check if the block device holds a file system
            foundUuid,rc = self._getBlockDeviceUuid(blockDevice,timer)
            if (rc != ReturnCodes.kOk):
                self._log("failed-blkid").error("activatePhase1() failed to obtain uuids! activateData = %s",self._activateData)
                self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
                self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kUuidError
                return rc
            
            # block device may hold a file system or 'None' will be returned from _getBlockDeviceUuid() ('None' means no fs on this block device)
            self._log("block-device-uuid-found").debug2("for block device '%s' foundUuid is '%s'",blockDevice,foundUuid)

            self._activateData.foundUuid = foundUuid
            self._activateData.currentUuid = foundUuid
            return ReturnCodes.kOk

        except Exception,e:
            self._log("activate-fs-phase1-exception").error("activatePhase1() failed! activateData = %s, exception = '%s'",self._activateData,e)
            self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
            self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kUnknown
            return ReturnCodes.kGeneralError

    # non blocking phase
    # mkfs if needed
    def activatePhase2 (self):
        """
        Non blocking phase (mkfs if needed)
        two only ways to get out of this phase alive is to launch a mkfs process or to have no need in creating a new fs
        """
        try:
            # entering phase 2
            self._log("enter-phase2").debug2("entering phase2 for '%s'. activateData = %s",self._logicalDiskName,self._activateData)

            foundUuid = self._activateData.foundUuid
            expectedUuid = self._activateData.expectedUuid
            blockDevice = self._activateData.blockDevice
            timer = self._activateData.timer
            autoInit = self._activateData.autoInit
            forceInit = self._activateData.forceInit

            if (expectedUuid == self.UUID_ACCEPT_ANY):
                if (foundUuid == None):
                    self._log("cannot-accept-any").error("cannot accepet any UUID for block device '%s', as found UUID is 'None'",blockDevice)
                    self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
                    self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kUuidError
                    return ReturnCodes.kGeneralError
                else:
                    self._log("accept-any").error("accepeting UUID '%s' ('accept any' flag was used) for block device '%s'",foundUuid,blockDevice)
                    self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
                    self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kOk
                    return ReturnCodes.kAlreadyExists

            else: # usual scenario ('accept any' was not used)
                if ((foundUuid != expectedUuid) or (foundUuid == None) or forceInit):
                    # mismatch of uuids
                    self._log("block-device-exists-init-required").debug2("block device '%s' found UUID='%s', expected UUID is'%s', forceInit='%s' - need to initialize",blockDevice,foundUuid,expectedUuid,forceInit)
                    self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
                    self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kUuidMismatch
    
                    if autoInit:
                        # rebuild file system on device
                        self._mkfsLaunchOnly(blockDevice,timer)
                        return ReturnCodes.kOk
                    else:
                        # found and expected mismatch but no permission to initialize
                        self._log("block-device-init-required-no-init-permission").error("block device '%s' needs a new fs but was not allowed to be initialized (autoInit=%s)",blockDevice,autoInit)
                        return ReturnCodes.kGeneralError

                else: 
                    # foundUuid == expectedUuid (!=None)
                    self._log("block-device-uuids-match").debug2("block device '%s' holds fs with UUID='%s' and expected UUID is '%s' (this is ok)",blockDevice,foundUuid,expectedUuid)
                    self._activateData.mkfsThread = None
                    self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
                    self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kOk
                    return ReturnCodes.kAlreadyExists

        except Exception,e:
            self._log("activate-fs-phase2-exception").error("activatePhase2() failed! activateData = %s, exception = '%s'",self._activateData,e)
            self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
            self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kUnknown
            return ReturnCodes.kGeneralError

    
    def activatePhase3 (self):
        """
        Block till mkfs is done - dummy phase
        """
        try:
            # entering phase 3
            self._log("enter-phase3").debug2("entering phase3 for '%s'. activateData = %s",self._logicalDiskName,self._activateData)
            
            mkfsThread = self._activateData.mkfsThread

            if (mkfsThread != None):
                rc = self._mkfsWaitOnly()
                if (rc != ReturnCodes.kOk):
                    self._log("activate-fail-on-mkfs").error("activatePhase3() failed creating a file system! activateData = %s",self._activateData)
                    self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
                    self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kFileSystemError
                    return rc
                self._activateData.shouldUpdateCurrentUuid = True

            self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
            self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kOk
            return ReturnCodes.kOk

        except Exception,e:
            self._log("activate-fs-phase3-exception").error("activatePhase3() failed! activateData = %s, exception = '%s'",self._activateData,e)
            self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
            self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kUnknown
            return ReturnCodes.kGeneralError
            
    def activatePhase4 (self):
        """
        Rest of work goes here (mount etc')
        """
        try:
            # entering phase 4
            self._log("enter-phase4").debug2("entering phase4 for '%s'. activateData = %s",self._logicalDiskName,self._activateData)
            
            shouldUpdateCurrentUuid = self._activateData.shouldUpdateCurrentUuid
            blockDevice = self._activateData.blockDevice
            timer = self._activateData.timer
            mountingPoint = self._activateData.mountingPoint
            blockDeviceReadahead = self._activateData.blockDeviceReadahead
            currentUuid = self._activateData.currentUuid

            # if needed, update current uuid after new file system was created
            if shouldUpdateCurrentUuid:
                currentUuid,rc = self._getBlockDeviceUuid(blockDevice,timer)
                if ((rc != ReturnCodes.kOk) or (currentUuid == None)):
                    self._log("failed-blkid2").error("activatePhase4() failed to obtain uuids! activateData = %s",self._activateData)
                    self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
                    self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kUuidError
                    return rc

                self._log("fs-created-on-block-device").debug2("new file system (UUID='%s') was created on block device '%s'",currentUuid,blockDevice)
                self._activateData.currentUuid = currentUuid
                self._activateData.shouldUpdateCurrentUuid = False
            
            # before mounting
            rc = self._setReservedBlockPercentage(blockDevice,0,timer)
            if (rc != ReturnCodes.kOk):
                self._log("activate-fail-on-setting-reserved-block-percentage").error("activatePhase4() failed on setting reserved blocks parameter! activateData = %s",self._activateData)
                self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
                self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kUnknown
                return rc

            # mount
            rc = self._mount(blockDevice,mountingPoint,blockDeviceReadahead,timer)
            if (rc != ReturnCodes.kOk):
                self._log("activate-fail-on-mount").error("activatePhase4() failed on mount! activateData = %s",self._activateData)
                self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
                self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kMountError
                return rc

            # full success - since this is the final stage
            self._log("activate-success").debug2("activation succeeded! activateData = %s",self._activateData)
            self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kUp
            self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kOk

            return ReturnCodes.kOk

        except Exception,e:
            self._log("activate-fs-phase4-exception").error("activatePhase4() failed! activateData = %s, exception = '%s'",self._activateData,e)
            self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kDown
            self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kUnknown
            return ReturnCodes.kGeneralError

    def activateGetCurrentUuid (self):
        if (self._activateData != None):
            return self._activateData.currentUuid
        return None


    def getDetailedStatus (self):
        """
        Fetch file system status
        """
        try:
            if ((self._activateData == None) or (self._activateData.blockDevice == None)):
                self._log("no-block-device-no-status").debug2("no block device was found for file system '%s'",self._logicalDiskName)
                return None,ReturnCodes.kOk

            else:
                terminateTimeOut = self._activeTimeoutsConfig.getStatus
                timer = common.Timer(terminateTimeOut)
                blockDevice = self._activateData.blockDevice
                statusDisctionary,rc = self._tune2fs(blockDevice,timer)
                
                if (rc != ReturnCodes.kOk):
                    self._log("get-status-failed").error("getDetailedStatus() for file system '%s' failed!",self._logicalDiskName)
                    return None,ReturnCodes.kGeneralError

                if (statusDisctionary == None):
                    self._log("have-block-but-no-status").debug2("block device '%s' for file system '%s' - could not fins file-system status",blockDevice,self._logicalDiskName)
                else:
                    self._log("status-found").debug2("block device '%s' for file system '%s' - status found!",blockDevice,self._logicalDiskName)

                return statusDisctionary,rc

        except Exception,e:
            self._log("get-file-system-status-exception").error("getDetailedStatus(terminateTimeOut=%.2f) faild! exception = '%s'",terminateTimeOut,e)
            return None,ReturnCodes.kGeneralError
        

       
       
class DirectoryFileSystem(FileSystem):
    """
    File system class to support mini platform
    """
    INTERNAL_DIRECTORY_RELATIVE_PATH = "file_system"
    INTERNALS_JSON_FILE_NAME = "internal.json"
    BAD_FILE_NAME = "bad"
    INTERNALS_KEY_UUID = "uuid"

    def __init__ (self,logicalDiskName,logger):

        # init base class
        FileSystem.__init__(self,logicalDiskName,logger)

        self._internalDirectoryPath = None
        self._internalsJsonFilePath = None
        self._badFilePath           = None

        # state and status
        self.operationalStatus = blinky_generated_enums.FileSystemOperationalStatusType.kUp
        self.operationalStatusReason = blinky_generated_enums.FileSystemOperationalStatusReasonType.kOk
        self.fsRawType = "directory-fs"
        self.fsType = blinky_generated_enums.FileSystemTypeType.kDirectory


    def _shouldFailActivation (self):
        if (self._badFilePath == None):
            # activation haven't begun
            return False
        
        if (os.path.exists(self._badFilePath)):
            return True
        return False

    def _fakeMkfs (self,mountingPoint,timer):

        withinMountingPointPath = os.path.join(mountingPoint,"*")

        # build command string 
        cmdString = "rm -rf %s"%withinMountingPointPath

        # run
        stdout,stderr,rc = self._runCommand(cmdString,timer)
        
        if (rc == 0):
            self._log("fs-created").debug2("file system '%s' was successfully created",self._logicalDiskName)
            return ReturnCodes.kOk
        else:
            self._log("fs-creation-failed").error("file system '%s' creation failed! stderr=%s",self._logicalDiskName,stderr)
            return ReturnCodes.kGeneralError
        

    def _getNewUuid (self):
        return str(random.random())


    def setInitialActivationParams (self,mountingPoint,expectedUuid,forceInit):
        # stuff to take from config
        autoInit = self._activeFileSystemConfig.autoInit
        blockDeviceReadahead = self._activeFileSystemConfig.readAhead
        activateTerminateTimeOut = self._activeTimeoutsConfig.activate
        if not self._activeFileSystemConfig.checkUuid:
            expectedUuid = self.UUID_ACCEPT_ANY

        self._activateData = self.ActivateData(mountingPoint,None,expectedUuid,autoInit,forceInit,blockDeviceReadahead,activateTerminateTimeOut)
        self._log("set-initial-activeation-params").debug2("setInitialActivationParams() called. activateData = %s",self._activateData)
        return ReturnCodes.kOk


    def setIntermediateActivationParams (self,blockDevice):
        self._activateData.blockDevice = blockDevice
        self._log("set-intermidiate-activeation-params").debug2("setIntermediateActivationParams() called. activateData = %s",self._activateData)
        return ReturnCodes.kOk


    def unmount (self):
        self._log("unmount").debug2("unmounted file system '%s'",self._logicalDiskName)
        return ReturnCodes.kOk


    def activatePhase1 (self):
        try:
            # entering phase 1
            self._log("enter-phase1").debug2("entering phase1 (the obtain current UUID phase). activateData = %s",self._activateData)

            mountingPoint = self._activateData.mountingPoint
            self._internalDirectoryPath = os.path.join(mountingPoint,self.INTERNAL_DIRECTORY_RELATIVE_PATH)
            self._internalsJsonFilePath = os.path.join(self._internalDirectoryPath,self.INTERNALS_JSON_FILE_NAME)
            self._badFilePath           = os.path.join(self._internalDirectoryPath,self.BAD_FILE_NAME)

            foundUuid = None

            if os.path.exists(self._internalsJsonFilePath):
                self._log("fs-internals-found").debug3("internals for DirectoryFileSystem '%s' are in %s",self._logicalDiskName,self._internalsJsonFilePath)
                internals = a.infra.format.json.readFromFile(self._log,self._internalsJsonFilePath)
                self._log("fs-internals-obtained").debug3("internals for DirectoryFileSystem '%s' are %s",self._logicalDiskName,internals)
                foundUuid = internals[self.INTERNALS_KEY_UUID]

            self._activateData.foundUuid = foundUuid
            self._activateData.currentUuid = foundUuid
            return ReturnCodes.kOk

        except Exception,e:
            self._log("activate-fs-phase1-exception").error("activatePhase1() failed! activateData = %s, exception = '%s'",self._activateData,e)
            return ReturnCodes.kGeneralError


    def activatePhase2 (self):
        """
        mkfs phase
        """
        try:
            # entering phase 2
            self._log("enter-phase2").debug2("entering phase2 (the mkfs phase). activateData = %s",self._activateData)

            foundUuid = self._activateData.foundUuid
            expectedUuid = self._activateData.expectedUuid
            mountingPoint = self._activateData.mountingPoint
            timer = self._activateData.timer
            autoInit = self._activateData.autoInit
            forceInit = self._activateData.forceInit

            if (expectedUuid == self.UUID_ACCEPT_ANY):
                if (foundUuid == None):
                    self._log("cannot-accept-any").error("cannot accepet any UUID for '%s', as found UUID is 'None'",self._logicalDiskName)
                    return ReturnCodes.kGeneralError
                else:
                    self._log("accept-any").error("accepeting UUID '%s' ('accept any' flag was used) for '%s'",foundUuid,self._logicalDiskName)
                    return ReturnCodes.kAlreadyExists

            else: # usual scenario ('accept any' was not used)
                if ((foundUuid != expectedUuid) or (foundUuid == None) or forceInit):
                    # mismatch of uuids
                    self._log("block-device-exists-init-required").debug2("'%s' found UUID='%s',expected UUID is'%s', forceInit='%s' need to initialize",self._logicalDiskName,foundUuid,expectedUuid,forceInit)
    
                    if autoInit:
                        rc = self._fakeMkfs(mountingPoint,timer)
                        if (rc == ReturnCodes.kOk):
                            self._activateData.shouldUpdateCurrentUuid = True
                        return rc
                    else:
                        # found and expected mismatch but no permission to initialize
                        self._log("block-device-init-required-no-init-permission").error("'%s' needs a new fs but was not allowed to be initialized (autoInit=%s)",self._logicalDiskName,autoInit)
                        return ReturnCodes.kGeneralError

                else: 
                    # foundUuid == expectedUuid (!=None)
                    self._log("block-device-uuids-match").debug2("'%s' holds fs with UUID='%s' and expected UUID is '%s' (this is ok)",self._logicalDiskName,foundUuid,expectedUuid)
                    return ReturnCodes.kAlreadyExists

        except Exception,e:
            self._log("activate-fs-phase2-exception").error("activatePhase2() failed! activateData = %s, exception = '%s'",self._activateData,e)
            return ReturnCodes.kGeneralError


    def activatePhase3 (self):
        try:
            # entering phase 3
            self._log("enter-phase3").debug2("entering phase3 (the do nothing phase). activateData = %s",self._activateData)
            return ReturnCodes.kOk

        except Exception,e:
            self._log("activate-fs-phase3-exception").error("activatePhase3() failed! activateData = %s, exception = '%s'",self._activateData,e)
            return ReturnCodes.kGeneralError


    def activatePhase4 (self):
        try:
            # entering phase 4
            self._log("enter-phase4").debug2("entering phase4 (update UUID if needed phase). activateData = %s",self._activateData)
            
            shouldUpdateCurrentUuid = self._activateData.shouldUpdateCurrentUuid

            # if needed, update current uuid after new file system was created
            if shouldUpdateCurrentUuid:
                currentUuid = self._getNewUuid()

                # burn UUID on file-system
                internals = {}
                internals[self.INTERNALS_KEY_UUID] = currentUuid
                if not os.path.exists(self._internalDirectoryPath):
                    self._log("attempt-to-create-internal-dir").debug2("internal file-system needs to be created at %s"%self._internalDirectoryPath)
                    os.makedirs(self._internalDirectoryPath)
                    self._log("created-internal-dir").debug2("internal file-system created in %s"%self._internalDirectoryPath)

                # internal dir should be created by now
                a.infra.format.json.writeToFile(self._log,internals,self._internalsJsonFilePath)

                self._log("fs-created-on-block-device").debug2("new file system (UUID='%s') was created for disk '%s'",currentUuid,self._logicalDiskName)
                self._activateData.currentUuid = currentUuid
                self._activateData.shouldUpdateCurrentUuid = False
            
            # full success - since this is the final stage
            self._log("activate-success").debug2("activation succeeded! activateData = %s",self._activateData)
            return ReturnCodes.kOk

        except Exception,e:
            self._log("activate-fs-phase4-exception").error("activatePhase4() failed! activateData = %s, exception = '%s'",self._activateData,e)
            return ReturnCodes.kGeneralError


    def activateGetCurrentUuid (self):
        if (self._activateData != None):
            return self._activateData.currentUuid
        return None


    def getDetailedStatus (self):
        if (self._activateData != None):
            statusDict = {}
            for k,v in self._activateData.__dict__.items():
                statusDict[k] = str(v)
            return statusDict,ReturnCodes.kOk

        return None,ReturnCodes.kOk



