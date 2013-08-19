# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz


if  __package__ is None:
    G_NAME_MODULE_STORAGE_DISK = "unknown"
    G_NAME_GROUP_STORAGE_DISK_CONTENT_DISK_MANAGER = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_DISK
    from . import G_NAME_GROUP_STORAGE_DISK_CONTENT_DISK_MANAGER

from a.infra.basic.return_codes import ReturnCodes
import a.infra.subprocess
import content_disk
import common
import logical_disk as ld, dell_raid_controller as drc
import re
import time
import json
import a.infra.format.json
import email.utils
import os


# utlity for sorting in human order
def atoi(text):
    return int(text) if text.isdigit() else text
def humanOrder(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]


class ContentDiskManagerExternalCfg(object):
    def __init__ (self):

        # TODO: take out un needed fields here (json)
        self.diskControllersCfg    = None
        self.pdisksCfg             = None
        self.logicalDisksCfg       = None
        self.fssCfg                = None
        self.contentDisksCfg       = None
        self.contentDiskManagerCfg = None
        self.stateDir              = None
        self.doCleanContent        = None
        self.doCleanContentRm      = None
        self.maxDiskCount          = None
        self.minDiskCount          = None
        self.acceptAnyUuid         = None
        self.disableRemoveLvm      = None
        self.disableAutoInit       = None
        self.blockDeviceReadahead  = None
        self.forceInitList         = None




    def __str__ (self):
        return str(self.__dict__)

class ContentDiskManager(object):

    EXPECTED_UUIDS_FILE_NAME = "expected_uuids.json"
    
    # status keys
    DETAILED_STATUS_KEY_CONTENT_DISKS = "content-disks"
    DETAILED_STATUS_KEY_GLOBAL = "global"
    DETAILED_STATUS_GLOBAL_SECION_KEY_ACTIVE_DISK_COUNT = "active-disk-count"
    DETAILED_STATUS_GLOBAL_SECION_KEY_TOTAL_DISK_COUNT = "total-disk-count"
    DETAILED_STATUS_GLOBAL_SECION_KEY_DATE_UPDATED = "last-updated" 
    DETAILED_STATUS_GLOBAL_SECION_KEY_EXPECTED_UUIDS = "expected-uuids"

    # status summary headlines
    STATUS_HEADLINE_DISK = "Disk"
    STATUS_HEADLINE_STATUS = "Status" 
    STATUS_HEADLINE_STATE = "State"
    STATUS_HEADLINE_SIZE = "Size[G]"
    STATUS_HEADLINE_SERIAL_NUMBER = "Serial-Number"

    def __init__ (self,logicalDiskManager,physicalDiskManager,fileSystemManager,storageModuleManager,logger):
        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_DISK, G_NAME_GROUP_STORAGE_DISK_CONTENT_DISK_MANAGER)
        self._logicalDiskManager   = logicalDiskManager
        self._physicalDiskManager  = physicalDiskManager
        self._fileSystemManager    = fileSystemManager
        self._storageModuleManager = storageModuleManager
        self._stateDir             = None
        self._doCleanContent       = None
        self._doCleanContentRm     = None
        self._maxDiskCount         = None
        self._minDiskCount         = None
        self._acceptAnyUuid        = None
        self._disableRemoveLvm     = None
        self._disableAutoInit      = None
        self._blockDeviceReadahead = None
        self._expectedUuidsJson    = None
        self._doRemoveLvm          = True

        # configuration
        self._candidateContentDisksList = {}
        self._runningContentDisksList   = {}

        # members to be updated in activation process
        self._requestedForActivationContentDisksNames = set()
        self._activeContentDisks = {}
        self._currentUuids = {}
        self._isStateSupported = False


    def init (self,contentDiskManagerExternalCfg):

        contentDiskManagerCfgJson  = contentDiskManagerExternalCfg.contentDiskManagerCfg   
        self._stateDir             = contentDiskManagerExternalCfg.stateDir          
        self._doCleanContent       = contentDiskManagerExternalCfg.doCleanContent
        self._doCleanContentRm     = contentDiskManagerExternalCfg.doCleanContentRm
        self._maxDiskCount         = contentDiskManagerExternalCfg.maxDiskCount      
        self._minDiskCount         = contentDiskManagerExternalCfg.minDiskCount
        self._acceptAnyUuid        = contentDiskManagerExternalCfg.acceptAnyUuid       
        self._disableRemoveLvm     = contentDiskManagerExternalCfg.disableRemoveLvm    
        self._disableAutoInit      = contentDiskManagerExternalCfg.disableAutoInit     
        self._blockDeviceReadahead = contentDiskManagerExternalCfg.blockDeviceReadahead

        self._log("conetent-disk-mngr-init").debug2("ContentDiskManager init() is called (contentDiskManagerExternalCfg=%s)",contentDiskManagerExternalCfg)

        # parse content disk objects configuration
        try:
            contentDiskManagerCfg = a.infra.format.json.readFromFile(self._log,contentDiskManagerCfgJson)
            self._log("content-disk-manager-cfg-obtained").debug3("contentDiskManagerCfg for ContentDiskManager init() is %s",contentDiskManagerCfg)
            self._doRemoveLvm = contentDiskManagerCfg["removeLvm"]

        except Exception,e: 
            self._log("bad-cfg-json").exception("error loading json cfg file '%s'! exception = %s",contentDiskManagerCfgJson,e)
            return ReturnCodes.kGeneralError


        # content disk manager's stuff
        self._expectedUuidsJson = os.path.join(self._stateDir,self.EXPECTED_UUIDS_FILE_NAME)
        
        self._log("conetent-disk-mngr-cfg").debug3("for ContentDiskManager expectedUuidsJson=%s",self._expectedUuidsJson)

        self._log("conetent-disk-mngr-init-success").debug2("ContentDiskManager init() succeeded!")
        return ReturnCodes.kOk


    def managerTrxStart (self):
        self._log("content-disk-manager-trx-start").debug3("managerTrxStart()  was called, running --> candidate, running = %s ,candidate = %s",self._runningContentDisksList,self._candidateContentDisksList)
        self._candidateContentDisksList = self._runningContentDisksList.copy()
        if ((self._logicalDiskManager.managerTrxStart() == ReturnCodes.kOk) and
            (self._physicalDiskManager.managerTrxStart() == ReturnCodes.kOk) and
            (self._fileSystemManager.managerTrxStart() == ReturnCodes.kOk)):
            return ReturnCodes.kOk

        self._log("content-disk-manager-trx-start-fail").error("managerTrxStart() failed!")
        return ReturnCodes.kGeneralError


    def managerTrxVerifyPublicConfig (self):

        self._log("content-disk-manager-trx-verify-public").debug3("managerTrxVerifyPublicConfig() was called")
        # put between content disk verfication here
        if ((self._logicalDiskManager.managerTrxVerifyPublicConfig() == ReturnCodes.kOk) and
            (self._physicalDiskManager.managerTrxVerifyPublicConfig() == ReturnCodes.kOk) and
            (self._fileSystemManager.managerTrxVerifyPublicConfig() == ReturnCodes.kOk)):
            return ReturnCodes.kOk

        self._log("content-disk-manager-trx-verify-public-fail").error("managerTrxVerifyPublicConfig() failed!")
        return ReturnCodes.kGeneralError


    def managerTrxCommit (self):
        self._log("content-disk-manager-trx-start").debug3("managerTrxCommit()  was called, candidate --> running, running = %s ,candidate = %s",self._runningContentDisksList,self._candidateContentDisksList)
        self._runningContentDisksList = self._candidateContentDisksList.copy()
        if ((self._logicalDiskManager.managerTrxCommit() == ReturnCodes.kOk) and
            (self._physicalDiskManager.managerTrxCommit() == ReturnCodes.kOk) and
            (self._fileSystemManager.managerTrxCommit() == ReturnCodes.kOk)):
            return ReturnCodes.kOk

        self._log("content-disk-manager-trx-commit-fail").error("managerTrxCommit() failed!")
        return ReturnCodes.kGeneralError
            

    def managerTrxAbort (self):
        self._log("content-disk-manager-trx-abort").debug3("managerTrxAbort() was called, None --> candidate")
        self._candidateContentDisksList = None
        if ((self._logicalDiskManager.managerTrxAbort() == ReturnCodes.kOk) and
            (self._physicalDiskManager.managerTrxAbort() == ReturnCodes.kOk) and
            (self._fileSystemManager.managerTrxAbort() == ReturnCodes.kOk)):
            return ReturnCodes.kOk

        self._log("content-disk-manager-trx-abort-fail").error("managerTrxAbort() failed!")
        return ReturnCodes.kGeneralError


    def createDisk (self,key):

        if key in self._candidateContentDisksList:
            self._log("content-disk-already-exist").error("a disk named '%s' already exists",key)
            return ReturnCodes.kAlreadyExists

        contentDisk = content_disk.ContentDisk(key,self._logicalDiskManager,self._physicalDiskManager,self._fileSystemManager,self._storageModuleManager,self._log)
        self._candidateContentDisksList[key] = contentDisk
        return ReturnCodes.kOk


    def diskTrxStart (self,key):
        self._log("disk-trx-start").debug3("diskTrxStart(key=%s)  was called",key)
        if key not in self._candidateContentDisksList:
            self._log("no-content-disk-for-trx-start").error("diskTrxStart(key=%s) failed, no content disk with that name found")
            return ReturnCodes.kNotFound
    
        contentDisk = self._candidateContentDisksList[key]
        if (contentDisk.diskTrxStart() != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
    
    def diskTrxCommit (self,key):
        self._log("disk--trx-commit").debug3("diskTrxCommit(key=%s)  was called",key)
        if key not in self._candidateContentDisksList:
            self._log("no-content-disk-for-trx-commit").error("diskTrxCommit(key=%s) failed, no content disk with that name found")
            return ReturnCodes.kNotFound
    
        contentDisk = self._candidateContentDisksList[key]
        if (contentDisk.diskTrxCommit() != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    

    def diskTrxAbort (self,key):
        self._log("disk-trx-abort").debug3("diskTrxAbort(key=%s)  was called",key)
        if key not in self._candidateContentDisksList:
            self._log("no-content-disk-for-trx-abort").error("diskTrxAbort(key=%s) failed, no content disk with that name found")
            return ReturnCodes.kNotFound
    
        contentDisk = self._candidateContentDisksList[key]
        if (contentDisk.diskTrxAbort() != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk


    def diskValueSet (self,key,data):
        self._log("disk-value-set").debug3("diskValueSet(key=%s,data=%s)  was called",key,data)
        if key not in self._candidateContentDisksList:
            self._log("no-content-disk-for-value-set").error("diskValueSet(key=%s,data=%s) failed, no content disk with that name found")
            return ReturnCodes.kNotFound
    
        contentDisk = self._candidateContentDisksList[key]
        if (contentDisk.diskValueSet(data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk


    def diskPhysicalValueSet (self, key, data):
        self._log("disk-physical-value-set").debug3("diskPhysicalValueSet(key=%s,data=%s)  was called",key,data)
        if key not in self._candidateContentDisksList:
            self._log("no-content-disk-for-value-set").error("diskPhysicalValueSet(key=%s,data=%s) failed, no content disk with that name found")
            return ReturnCodes.kNotFound
    
        contentDisk = self._candidateContentDisksList[key]
        if (contentDisk.diskPhysicalValueSet(data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk


    def diskRaidArrayValueSet (self, key, data):
        self._log("disk-raid-array-value-set").debug3("diskRaidArrayValueSet(key=%s,data=%s)  was called",key,data)
        if key not in self._candidateContentDisksList:
            self._log("no-content-disk-for-value-set").error("diskRaidArrayValueSet(key=%s,data=%s) failed, no content disk with that name found")
            return ReturnCodes.kNotFound
    
        contentDisk = self._candidateContentDisksList[key]
        if (contentDisk.diskRaidArrayValueSet(data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk


    def diskFileSystemValueSet (self, key, data):
        self._log("disk-file-system-value-set").debug3("diskFileSystemValueSet(key=%s,data=%s)  was called",key,data)
        if key not in self._candidateContentDisksList:
            self._log("no-content-disk-for-value-set").error("diskFileSystemValueSet(key=%s,data=%s) failed, no content disk with that name found")
            return ReturnCodes.kNotFound
    
        contentDisk = self._candidateContentDisksList[key]
        if (contentDisk.diskFileSystemValueSet(data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk


    def diskFileSystemCommandsValueSet (self, key, data):
        self._log("disk-file-system-commands-value-set").debug3("diskFileSystemCommandsValueSet(key=%s,data=%s)  was called",key,data)
        if key not in self._candidateContentDisksList:
            self._log("no-content-disk-for-value-set").error("diskFileSystemCommandsValueSet(key=%s,data=%s) failed, no content disk with that name found")
            return ReturnCodes.kNotFound
    
        contentDisk = self._candidateContentDisksList[key]
        if (contentDisk.diskFileSystemCommandsValueSet(data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk


    def diskFileSystemTimeoutsValueSet (self, key, data):
        self._log("disk-file-system-timeouts-value-set").debug3("diskFileSystemTimeoutsValueSet(key=%s,data=%s)  was called",key,data)
        if key not in self._candidateContentDisksList:
            self._log("no-content-disk-for-value-set").error("diskFileSystemTimeoutsValueSet(key=%s,data=%s) failed, no content disk with that name found")
            return ReturnCodes.kNotFound
    
        contentDisk = self._candidateContentDisksList[key]
        if (contentDisk.diskFileSystemTimeoutsValueSet(data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk



    ## Periodic-work related functions and getters ##

    def getRunningDisk (self,logicalDiskName):
        if logicalDiskName in self._runningContentDisksList:
            return self._runningContentDisksList[logicalDiskName]

        self._log("cannot-fetch-running-content-disk").debug2("could not fetch running content disk '%s'", logicalDiskName)
        return None

    def getCandidateDisk (self,logicalDiskName):
        if logicalDiskName in self._candidateContentDisksList:
            return self._candidateContentDisksList[logicalDiskName]

        self._log("cannot-fetch-candidate-content-disk").debug2("could not fetch candidate content disk '%s'", logicalDiskName)
        return None


    def _runCommand (self,cmdString,timer):
        """
        Run a general filesystem related command. 
        """
        return common.runCommand (self._log,cmdString,timer)


    def removeLVM (self):
        """
        Remove the old LVM structure: VGs and LVs
        """

        # consts
        TOTAL_REMOVE_LVM_EXPECTED_TIME = 20
        GET_VG_NAMES_COMMAND_STRING = "vgs -o name --noheading"
        REMOVE_VG_PATTERNS = ["vg_c[0-9][0-9]"]
        KEEP_VG_PATTERNS = ["vg_sys"]
        REMOVE_VG_COMMAND_STRING = "vgremove -f %s"
        
        try:
            # start timer
            timer = common.Timer(TOTAL_REMOVE_LVM_EXPECTED_TIME)


            # get list of VG names
            stdout,stderr,rc = common.runCommand (self._log,GET_VG_NAMES_COMMAND_STRING,timer)
            if (rc != 0):
                self._log("get-vgs-failed").error("removeLVM() faild to get VG names! (command='%s', rc=%d, stderr=%s)",GET_VG_NAMES_COMMAND_STRING,rc,stderr)
                return ReturnCodes.kGeneralError

            vgNames = stdout.strip().split("\n")
            vgNamesLeft = set(vgNames)
            

            # per VG, if fits the known patterns for removal - remove it
            failedToBeRemovedVgs = []
            for vgName in vgNames:
                for pattern in REMOVE_VG_PATTERNS:
                    if (re.search(pattern,vgName) != None):
                        # found a VG for removal -> if allowed destroy and remove from vgNamesLeft
                        if (self._disableRemoveLvm):
                            self._log("cannot-remove-vg").error("some VGs (VG '%s') needs to be removed but disable-remove-lvm is '%s'. destruction of LVM failed!",vgName,self._disableRemoveLvm)
                            return ReturnCodes.kGeneralError
                        
                        # we are good to go on the removal of this VG
                        stdout,stderr,rc = common.runCommand (self._log,REMOVE_VG_COMMAND_STRING%vgName,timer)
                        if (rc == 0):
                            self._log("successful-vg-removal").info("VG '%s' was removed successfully",vgName)
                            vgNamesLeft.remove(vgName)

                        else:
                            self._log("vg-removal-fail").error("VG '%s' failed to be removed!",vgName)
                            failedToBeRemovedVgs.append(vgName)
                        break

            if (len(failedToBeRemovedVgs) > 0):
                self._log("failed-to-be removed-vgs").error("the following VGs could not be removed %s. destruction of LVM failed!",failedToBeRemovedVgs)
                return ReturnCodes.kGeneralError

            # check for renegade VGs (ones that are not supposed to be)
            renegadeVgs = []
            for vgName in vgNamesLeft:
                for pattern in KEEP_VG_PATTERNS:
                    if (re.search(pattern,vgName) != None):
                        break

                else:
                    # here is a place where only renegade VGs get to
                    self._log("renegade-vg-found").error("VG '%s' doesn't fit the allowed patterns nor the ones for removal",vgName)
                    renegadeVgs.append(vgName)

            if (len(renegadeVgs) > 0):
                self._log("renegade-vgs").error("the following VGs are renegade %s. destruction of LVM failed! (patternsToRemove=%s, pattersToKeep=%s)",renegadeVgs,REMOVE_VG_PATTERNS,KEEP_VG_PATTERNS)
                return ReturnCodes.kGeneralError

            # full success
            self._log("lvm-removed-successfuly").info("removeLVM() done successfully")
            return ReturnCodes.kOk

        except Exception,e:
            self._log("remove-lvm-exception").error("removeLVM() faild! exception = '%s'",e)
            return ReturnCodes.kGeneralError


    def getDiskStatus(self,logicalDiskName,operData):

        if ((logicalDiskName not in self._runningContentDisksList) or (self._runningContentDisksList[logicalDiskName] == None)):
            self._log("no-disk-for-status-retrieval").error("getDiskStatus(logicalDiskName=%s) failed, no disk with that name found",logicalDiskName)
            return ReturnCodes.kGeneralError

        if (logicalDiskName not in self._requestedForActivationContentDisksNames):
            self._log("disk-wasnt-activated").debug2("getDiskStatus(logicalDiskName=%s) was requested for a disk that wasn't requested for activation",logicalDiskName)
            return ReturnCodes.kOk
        
        contentDisk = self._runningContentDisksList[logicalDiskName]
        contentDiskStatusDict,rc  = contentDisk.getDetailedStatus()
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
            
        logicalDiskStatus = contentDiskStatusDict[content_disk.ContentDisk.DETAILED_STATUS_KEY_LOGICAL_DISK]
        if ld.LogicalDisk.DETAILED_STATUS_KEY_VDISK in logicalDiskStatus:
            vdiskStatus = logicalDiskStatus[ld.LogicalDisk.DETAILED_STATUS_KEY_VDISK]
            if ((vdiskStatus != None) and (ld.LogicalDisk.STATUS_KEY_SIZE in vdiskStatus)) :
                operData.setSize(int(vdiskStatus[ld.LogicalDisk.STATUS_KEY_SIZE]))

        if (contentDisk._blockDevice != None):
            operData.setOsDevice(str(contentDisk._blockDevice))
        operData.setOprtationalStatus(contentDisk.statusEnum)
        operData.setOperationalStatusReason(contentDisk.statusReasonEnum)

        return ReturnCodes.kOk

    
    def getDiskAlarm (self,logicalDiskName,operData):

        if ((logicalDiskName not in self._runningContentDisksList) or (self._runningContentDisksList[logicalDiskName] == None)):
            self._log("no-disk-for-alarm-retrieval").error("getDiskAlarm(logicalDiskName=%s) failed, no disk with that name found",logicalDiskName)
            return ReturnCodes.kGeneralError

        if (logicalDiskName not in self._requestedForActivationContentDisksNames):
            self._log("disk-wasnt-activated").debug2("getDiskAlarm(logicalDiskName=%s) was requested for a disk that wasn't requested for activation",logicalDiskName)
            return ReturnCodes.kOk
        
        contentDisk = self._runningContentDisksList[logicalDiskName]
        operData.setContentDiskFailureAlarm(contentDisk.failureAlarm)
        operData.setContentDiskFailureReason(contentDisk.failureAlarmReason)

        return ReturnCodes.kOk


    def getDiskPhysicalStatus (self,logicalDiskName,operData):

        if ((logicalDiskName not in self._runningContentDisksList) or (self._runningContentDisksList[logicalDiskName] == None)):
            self._log("no-disk-for-status-retrieval").error("getDiskPhysicalStatus(logicalDiskName=%s) failed, no disk with that name found",logicalDiskName)
            return ReturnCodes.kGeneralError

        if (logicalDiskName not in self._requestedForActivationContentDisksNames):
            self._log("disk-wasnt-activated").debug2("getDiskPhysicalStatus(logicalDiskName=%s) was requested for a disk that wasn't requested for activation",logicalDiskName)
            return ReturnCodes.kOk
        
        contentDisk = self._runningContentDisksList[logicalDiskName]
        contentDiskStatusDict,rc  = contentDisk.getDetailedStatus()
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError
        
        logicalDiskStatus = contentDiskStatusDict[content_disk.ContentDisk.DETAILED_STATUS_KEY_LOGICAL_DISK]
        if ld.LogicalDisk.DETAILED_STATUS_KEY_PDISK in logicalDiskStatus:
            pdiskStatus = logicalDiskStatus[ld.LogicalDisk.DETAILED_STATUS_KEY_PDISK]
            if (pdiskStatus != None):
                operData.setProductId(pdiskStatus.get(drc.PdiskStatus.KEY_PRODUCT_ID))
                operData.setSasAddress(pdiskStatus.get(drc.PdiskStatus.KEY_SAS_ADDRESS))
                operData.setModelNumber(pdiskStatus.get(drc.PdiskStatus.KEY_MODEL_NUMBER))
                operData.setSerialNumber(pdiskStatus.get(drc.PdiskStatus.KEY_SERIAL_NUMBER))
                operData.setUsedRaidSpace(pdiskStatus.get(drc.PdiskStatus.KEY_USED_RAID_SPACE))
                operData.setStatusRaw(pdiskStatus.get(drc.PdiskStatus.KEY_STATUS_RAW))
                operData.setFirmwareRevision(pdiskStatus.get(drc.PdiskStatus.KEY_FIRMWARE_REVISION))
                operData.setSize(pdiskStatus.get(drc.PdiskStatus.KEY_SIZE))
                operData.setFailurePredicted(pdiskStatus.get(drc.PdiskStatus.KEY_FAILURE_PREDICTED))
                operData.setSizeRaw(pdiskStatus.get(drc.PdiskStatus.KEY_SIZE_RAW))
                operData.setDeviceLifeStatus(pdiskStatus.get(drc.PdiskStatus.KEY_DEVICE_LIFE_STATUS))
                operData.setDeviceLifeRemaining(pdiskStatus.get(drc.PdiskStatus.KEY_DEVICE_LIFE_REMAINING))
                operData.setPowerStatus(pdiskStatus.get(drc.PdiskStatus.KEY_POWER_STATUS))
                operData.setState(pdiskStatus.get(drc.PdiskStatus.KEY_STATE_ENUM))
                operData.setProgress(pdiskStatus.get(drc.PdiskStatus.KEY_PROGRESS))
                operData.setStatus(pdiskStatus.get(drc.PdiskStatus.KEY_STATUS_ENUM)) 
                operData.setManufactureYear(pdiskStatus.get(drc.PdiskStatus.KEY_MANUFACTURE_YEAR))
                operData.setFailurePredictedRaw(pdiskStatus.get(drc.PdiskStatus.KEY_FAILURE_PREDICTED_RAW))
                operData.setMediaType(pdiskStatus.get(drc.PdiskStatus.KEY_MEDIA_TYPE))
                operData.setManufactureDay(pdiskStatus.get(drc.PdiskStatus.KEY_MANUFACTURE_DAY))
                operData.setAvailableRaidSpace(pdiskStatus.get(drc.PdiskStatus.KEY_AVAILABLE_RAID_SPACE))
                operData.setPartNumber(pdiskStatus.get(drc.PdiskStatus.KEY_PART_NUMBER))
                operData.setHotSpare(pdiskStatus.get(drc.PdiskStatus.KEY_HOT_SPARE))
                operData.setCapableSpeed(pdiskStatus.get(drc.PdiskStatus.KEY_CAPABLE_SPEED))
                operData.setCertified(pdiskStatus.get(drc.PdiskStatus.KEY_CERTIFIED))
                operData.setDeviceWriteCache(pdiskStatus.get(drc.PdiskStatus.KEY_DEVICE_WRITE_CACHE))
                operData.setStateRaw(pdiskStatus.get(drc.PdiskStatus.KEY_STATE_RAW))
                operData.setManufactureWeek(pdiskStatus.get(drc.PdiskStatus.KEY_MANUFACTURE_WEEK))
                operData.setNegotiatedSpeed(pdiskStatus.get(drc.PdiskStatus.KEY_NEGOTIATED_SPEED))
                operData.setVendorId(pdiskStatus.get(drc.PdiskStatus.KEY_VENDOR))

        return ReturnCodes.kOk

    def getDiskRaidArrayStatus (self,logicalDiskName, operData):
        
        if ((logicalDiskName not in self._runningContentDisksList) or (self._runningContentDisksList[logicalDiskName] == None)):
            self._log("no-disk-for-status-retrieval").error("getDiskRaidArrayStatus(logicalDiskName=%s) failed, no disk with that name found")
            return ReturnCodes.kGeneralError

        if (logicalDiskName not in self._requestedForActivationContentDisksNames):
            self._log("disk-wasnt-activated").debug2("getDiskRaidArrayStatus(logicalDiskName=%s) was requested for a disk that wasn't requested for activation",logicalDiskName)
            return ReturnCodes.kOk
        
        contentDisk = self._runningContentDisksList[logicalDiskName]
        contentDiskStatusDict,rc  = contentDisk.getDetailedStatus()
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        logicalDiskStatus = contentDiskStatusDict[content_disk.ContentDisk.DETAILED_STATUS_KEY_LOGICAL_DISK]
        if ld.LogicalDisk.DETAILED_STATUS_KEY_VDISK in logicalDiskStatus:
            vdiskStatus = logicalDiskStatus[ld.LogicalDisk.DETAILED_STATUS_KEY_VDISK]
            if (vdiskStatus != None):
                operData.setPhysicalIdList(vdiskStatus.get(drc.VdiskStatus.KEY_PDISK_IDS))         
                operData.setStatus(vdiskStatus.get(drc.VdiskStatus.KEY_STATUS_ENUM))                 
                operData.setStateRaw(vdiskStatus.get(drc.VdiskStatus.KEY_STATE_RAW))               
                operData.setReadPolicy(vdiskStatus.get(drc.VdiskStatus.KEY_READ_POLICY))             
                operData.setBadBlocks(vdiskStatus.get(drc.VdiskStatus.KEY_BAD_BLOCKS))              
                operData.setMediaType(vdiskStatus.get(drc.VdiskStatus.KEY_MEDIA_TYPE))              
                operData.setHotSparePolicyViolation(vdiskStatus.get(drc.VdiskStatus.KEY_HOT_SPARE_POLICY_VIOLATION))
                operData.setId(vdiskStatus.get(drc.VdiskStatus.KEY_VDISK_ID))                     
                operData.setState(vdiskStatus.get(drc.VdiskStatus.KEY_STATE_ENUM))                  
                operData.setStatusRaw(vdiskStatus.get(drc.VdiskStatus.KEY_STATUS_RAW))              
                operData.setDiskCachePolicy(vdiskStatus.get(drc.VdiskStatus.KEY_DISK_CACHE_POLICY))        
                operData.setBadBlocksRaw(vdiskStatus.get(drc.VdiskStatus.KEY_BAD_BLOCKS_RAW))           
                operData.setCachePolicy(vdiskStatus.get(drc.VdiskStatus.KEY_CACHE_POLICY))            
                operData.setWritePolicy(vdiskStatus.get(drc.VdiskStatus.KEY_WRITE_POLICY))            
                operData.setRaidType(vdiskStatus.get(drc.VdiskStatus.KEY_RAID_TYPE))               
                operData.setStripeElementSize(vdiskStatus.get(drc.VdiskStatus.KEY_STRIPE_ELEMENT_SIZE))      
                operData.setSizeRaw(vdiskStatus.get(drc.VdiskStatus.KEY_SIZE_RAW))                
                operData.setSize(vdiskStatus.get(drc.VdiskStatus.KEY_SIZE))                   

        return ReturnCodes.kOk


    def getDiskFileSystemStatus (self,logicalDiskName, operData):
        if ((logicalDiskName not in self._runningContentDisksList) or (self._runningContentDisksList[logicalDiskName] == None)):
            self._log("no-disk-for-status-retrieval").error("getDiskFileSystemStatus(logicalDiskName=%s) failed, no disk with that name found")
            return ReturnCodes.kGeneralError

        if (logicalDiskName not in self._requestedForActivationContentDisksNames):
            self._log("disk-wasnt-activated").debug2("getDiskFileSystemStatus(logicalDiskName=%s) was requested for a disk that wasn't requested for activation",logicalDiskName)
            return ReturnCodes.kOk
        
        contentDisk = self._runningContentDisksList[logicalDiskName]
        rc = contentDisk.getFileSystemStatus(operData)
        if (rc != ReturnCodes.kOk):
            self._log("failed-to-fetch-fs-oper-status").error("failed to fetch file system oper status for %s",logicalDiskName)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

            
    def getDetailedStatusString (self):
        """
        detailed status in json format
        """

        statusDict = {}

        # content disks status
        allContentDisksStatus = {}
        for logicalDiskName in sorted(self._requestedForActivationContentDisksNames,key=humanOrder):
            contentDisk = self._runningContentDisksList[logicalDiskName]
            contentDiskStatusDict,rc = contentDisk.getDetailedStatus()
            if (rc == ReturnCodes.kOk):
                allContentDisksStatus[logicalDiskName] = str(contentDiskStatusDict)

        statusDict[self.DETAILED_STATUS_KEY_CONTENT_DISKS] = allContentDisksStatus


        # global status
        globalStatus = {}
        activeContentDiskCnt = len(self._activeContentDisks)
        totalContentDiskCount = len(self._runningContentDisksList)
        dateUpdated = time.time()

        globalStatus[self.DETAILED_STATUS_GLOBAL_SECION_KEY_ACTIVE_DISK_COUNT] = activeContentDiskCnt
        globalStatus[self.DETAILED_STATUS_GLOBAL_SECION_KEY_TOTAL_DISK_COUNT] = totalContentDiskCount
        globalStatus[self.DETAILED_STATUS_GLOBAL_SECION_KEY_DATE_UPDATED] = dateUpdated
        globalStatus[self.DETAILED_STATUS_GLOBAL_SECION_KEY_EXPECTED_UUIDS] = self._currentUuids

        statusDict[self.DETAILED_STATUS_KEY_GLOBAL] = globalStatus

        return json.dumps(statusDict,sort_keys=True, indent=4)


    def getStatusSummaryString (self): # TODO: show status only for module enabled disks (use cd.isModuleEnabled ())

        # heading
        statusSummaryString =  "%-10s %-7s %-7s %-8s %-13s\n"%(self.STATUS_HEADLINE_DISK,
                                              self.STATUS_HEADLINE_STATUS,
                                              self.STATUS_HEADLINE_STATE,
                                              self.STATUS_HEADLINE_SIZE,
                                              self.STATUS_HEADLINE_SERIAL_NUMBER)

        underline = "-"*50+"\n"
        statusSummaryString += underline

        # per disk lines
        gigaDevisor = 1024**3
        for name in sorted(self._requestedForActivationContentDisksNames,key=humanOrder):
            contentDisk = self._runningContentDisksList[name]

            if contentDisk.isModuleEnabled(): # status summary includes only the status of content disks that have an enabled module
                contentDiskStatus,rc = contentDisk.getStatus()
                if (rc == ReturnCodes.kOk):
                    diskSize = contentDiskStatus[ld.LogicalDisk.STATUS_KEY_SIZE]
                    if isinstance(diskSize,int):
                        diskSizeString = "%d"%(diskSize/gigaDevisor)
                    else:
                        # keep original string
                        diskSizeString = contentDiskStatus[ld.LogicalDisk.STATUS_KEY_SIZE]
    
                    lineString =  "%-10s %-7s %-7s %8s %13s\n"%(name,
                                                 contentDiskStatus[ld.LogicalDisk.STATUS_KEY_STATUS],
                                                 contentDiskStatus[ld.LogicalDisk.STATUS_KEY_STATE],
                                                 diskSizeString,
                                                 contentDiskStatus[ld.LogicalDisk.STATUS_KEY_SERIAL_NUMBER])
                    statusSummaryString += lineString
        
        # global announcements
        if (not self._isStateSupported):
            statusSummaryString += "\nWarning: active content disk count is below the required minimum, %d content disks."%self._minDiskCount
            statusSummaryString += "\nWarning: Acquisition and delivery are disabled.\n"

        # last updated on
        statusSummaryString += "\nLast Updated On %s"%email.utils.formatdate(localtime=True)

        return statusSummaryString

    def __getModuleEnabledDiskCount (self):
        moduleEnabledContentDiskCnt = 0
        for name in self._requestedForActivationContentDisksNames:
            contentDisk = self._runningContentDisksList[name]
            if contentDisk.isModuleEnabled():
                moduleEnabledContentDiskCnt += 1

        return moduleEnabledContentDiskCnt

    def getSystemStatusString (self):

        totalDiskCount = self.__getModuleEnabledDiskCount()
        statusString = "%d of %d active content disks. "%(len(self._activeContentDisks),totalDiskCount)
        if not self._isStateSupported:
            statusString += "NOT ENOUGH DISKS. DISABLING ACQUISITION AND DELIVERY. "

        statusString += "Last Updated On %s."%email.utils.formatdate(localtime=True)

        return statusString


    def _pushAllContentDisksRunningToActive (self):

        for key,contentDisk in self._runningContentDisksList.items():
            if (contentDisk.pushRunningToActiveConfig() != ReturnCodes.kOk):
                self._log("push-running-to-active-fail").error("pushing running to active of content disk '%s' failed!",key)
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def activateAllDisks (self,externalActivationDataPerDisk):

        ############################## PATCH ALERT ################################################
        # setting the system disk write cache policy
        # TODO: when moving to system disk support remove this part, it has no place here. 
        # consider if it is even relevant any more as maybe all systems will be set to write-through by then


        # build command line list
        cmd = ["/opt/dell/srvadmin/bin/omconfig","storage","vdisk","controller=0","vdisk=0","action=changepolicy","writepolicy=wt"]
        
        # timeouts
        terminateTimeOut = 60
        killTimeOut = terminateTimeOut + 20
        
        # instantiate a process to excute the command
        proc = a.infra.subprocess.Subprocess("om-cmd",self._log)

        # start the process
        proc.start(cmd,stdout=a.infra.subprocess.PIPE,stderr=a.infra.subprocess.PIPE)
        commandLine = proc.getCommandLine()
        self._log("run-command").debug2("running command '%s'",commandLine)

        # communicate (i.e. wait for command end or timeout)
        
        stdout,stderr = proc.communicate(terminateTimeOut=terminateTimeOut,killTimeOut=killTimeOut)

        rc = proc.getReturnCode()
        if (rc == 0):
            self._log("command-successful").debug3("the command '%s' ended successfully, stdout=%s",commandLine,stdout)
        else:
            self._log("command-unsuccessful").debug1("the command '%s' ended but was unsuccessful, rc=%s, stdout=%s, stderr=%s",commandLine,rc,stdout,stderr)
        
        ################################ PATCH ALERT END ##########################################



        # before we start activating update the active configuration
        if ((self._storageModuleManager.pushAllStorageModuleRunningToActive() != ReturnCodes.kOk) or (self._pushAllContentDisksRunningToActive() != ReturnCodes.kOk)):
            self._log("push-running-to-active-fail").error("pushing running to active of content disks or storage modules failed!")
            return ReturnCodes.kGeneralError


        # content disks to activate are those requested in the external data
        self._requestedForActivationContentDisksNames = set(externalActivationDataPerDisk)
        definedNames = set(self._runningContentDisksList)
        undefinedDisks = self._requestedForActivationContentDisksNames - definedNames
        if (len(undefinedDisks) > 0):
            self._log("undefined-disks").warning("the following disks are not defined in system configuration and will not be activated %s",list(undefinedDisks))
        validRequestedForActivationNames = self._requestedForActivationContentDisksNames-undefinedDisks
        self._activeContentDisks = dict((name,self._runningContentDisksList[name]) for name in validRequestedForActivationNames)

        # prior to activation - chack if we have enough candiates for the process
        currentDiskCount = len(self._activeContentDisks)
        if (currentDiskCount < self._minDiskCount):
            self._log("not-enough-disks").warning("prior to activation, found %d candidate content-disks for activation where the minimum allowed is %d",currentDiskCount,self._minDiskCount)


        # get expected UUIDs
        expectedUuids = {}      #------> read in this function
        self._currentUuids = {} #------> to be updated in activation process and writen in the end

        # alert on clean content
        if self._doCleanContent or self._doCleanContentRm:
            self._log("clean-content-requested").notice("Clean Content request was made - ALL CONTENT WILL BE LOST!")


        # get expected uuid
        if self._doCleanContent:
            self._log("heavy-content-clean").debug2("content clean requested simulating no expected uuids file")

        elif (os.path.exists(self._expectedUuidsJson)):
            try:
                expectedUuids = a.infra.format.json.readFromFile(self._log,self._expectedUuidsJson)
            except Exception:
                self._log("bad-expected-uuids-json-read").exception("error loading json file '%s'",self._expectedUuidsJson)
                return ReturnCodes.kGeneralError

        else:
            self._log("expected-uuids-not-found").info("Could not find '%s' (expected UUIDs file) - all content on content disks will be lost!",self._expectedUuidsJson)


        # preparations for activation 
        # -------------------------------

        # input params for activation cycle
        for logicalDiskName in self._activeContentDisks.keys():
            contentDiskExternalData = externalActivationDataPerDisk[logicalDiskName]
            mountingPoint = contentDiskExternalData.mountingPoint
            metaDir = contentDiskExternalData.metaDir
            mediaDir = contentDiskExternalData.mediaDir
            vitalDir = contentDiskExternalData.vitalDir
            expectedUuid = expectedUuids.get(logicalDiskName) # may be None
            self._runPhaseOnContentDisk(logicalDiskName,content_disk.ContentDisk.setInitialActivationParams,mountingPoint,metaDir,mediaDir,vitalDir,expectedUuid,self._doCleanContentRm)

        # unomunt all
        rc = self._fileSystemManager.unmountAll(self._activeContentDisks.keys())
        if (rc != ReturnCodes.kOk):
            self._log("prepare-for-activate-unmount-fail").error("failed to unmount all file-systems in preparation for activation")
            return ReturnCodes.kGeneralError

        # remove lvm #TODO: remove this part - no more lvm support needed
        if (self._doRemoveLvm):
            rc = self.removeLVM()
            if (rc != ReturnCodes.kOk):
                self._log("prepare-for-activate-remove-lvm-fail").error("failed to rmove LVM in preparation for activation")
                return ReturnCodes.kGeneralError


        # end of preparation - lets get this show on the road
        #------------------------------------------------------

        # activation phases
        # phase0 is just enabled/disabled selection - failing this phase should not be logged as error
        self._runPhaseOnAllContentDiskAndRemoveFailedFromActivationCycle(content_disk.ContentDisk.activatePhase0,False)


        for phaseFunc in (content_disk.ContentDisk.activatePhase1,content_disk.ContentDisk.activatePhase2,content_disk.ContentDisk.activatePhase3,content_disk.ContentDisk.activatePhase4):
            self._runPhaseOnAllContentDiskAndRemoveFailedFromActivationCycle(phaseFunc)


        # update current UUIDs
        for logicalDiskName in self._activeContentDisks.keys():
            contentDisk = self._activeContentDisks[logicalDiskName]
            contentDiskCurrentUuid = contentDisk.activateGetCurrentUuid()
            self._currentUuids[logicalDiskName] = contentDiskCurrentUuid

        try:
            a.infra.format.json.writeToFile(self._log,self._currentUuids,self._expectedUuidsJson,indent=4)
        except Exception:
            self._log("bad-expected-uuids-json-write").exception("error writing json file '%s'",self._expectedUuidsJson)
            return ReturnCodes.kGeneralError


        # check the active content disk count - and update isStateSupported flag
        currentDiskCount = len(self._activeContentDisks)
        totalDiskCount = self.__getModuleEnabledDiskCount()
       
        # user log
        a.infra.process.logUserMessage(a.api.user_log.msg.storage.ContentDiskCount(currentDiskCount,totalDiskCount,self._minDiskCount))

        self._isStateSupported = (currentDiskCount >= self._minDiskCount)
        if (not self._isStateSupported):
            # user log
            a.infra.process.logUserMessage(a.api.user_log.msg.storage.ContentDiskLowCount(currentDiskCount,totalDiskCount,self._minDiskCount))
            self._log("bad-disk-count").error("after activation, found %d  content-disks active (minDiskCount=%d, maxDiskCount=%d)",currentDiskCount,self._minDiskCount,self._maxDiskCount)
            return ReturnCodes.kUnSupported

        return ReturnCodes.kOk


    def _activateGetCurrentUuid (self,logicalDiskName):
        contentDisk = self._runningContentDisksList.get(logicalDiskName)# this function can be called on failed-to-activate disks as well
        if (contentDisk == None):
            self._log("bad-logical-disk-name").error("can't fetch currentUuid of content disk '%s'! no such disk was defined.",logicalDiskName)
            return None

        return contentDisk.activateGetCurrentUuid()

    def _removeContentDiskFromActivationCycle (self,logicalDiskName):
        self._activeContentDisks.pop(logicalDiskName)
        self._currentUuids[logicalDiskName] = None

    def _runPhaseOnContentDisk (self,logicalDiskName,phaseFunc,*args):
        if logicalDiskName not in self._activeContentDisks:
            self._log("bad-logical-disk-name").error("content disk '%s' is not a candidate for '%s'",logicalDiskName,phaseFunc.__name__)
            return ReturnCodes.kGeneralError

        contentDisk = self._activeContentDisks[logicalDiskName]
        rc = phaseFunc(contentDisk,*args)
        return rc

    def _runPhaseOnAllContentDiskAndRemoveFailedFromActivationCycle (self,phaseFunc,logFailAsError=True):
        funcName = phaseFunc.__name__
        for logicalDiskName in sorted(self._activeContentDisks.keys(),key=humanOrder):
            rc = self._runPhaseOnContentDisk(logicalDiskName,phaseFunc) # no special args - running on all
            if (rc != ReturnCodes.kOk):
                # specific content disk failed on this phase -> remove it from activation cycle
                self._removeContentDiskFromActivationCycle(logicalDiskName)
                if logFailAsError:
                    self._log("disk-fail-on-activate-phase").error("content disk '%s' failed on '%s' and was removed from activation cycle",logicalDiskName,funcName)
                else:
                    self._log("disk-extracted-from activation-cycle").info("content disk '%s' was removed from activation cycle on '%s'",logicalDiskName,funcName)



    def getActiveDisksList (self):
        return self._activeContentDisks.keys()


    def isQsmEnabled (self):
        return self._storageModuleManager.isQsmEnabled()

    def shutDown (self):

        # UNMOUNT ALL HERE
        # maybe do other stuff
        # log errors and stages in shut down

        return ReturnCodes.kOk
