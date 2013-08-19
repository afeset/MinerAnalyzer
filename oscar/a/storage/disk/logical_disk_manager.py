# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz

if  __package__ is None:
    G_NAME_MODULE_STORAGE_DISK = "unknown"
    G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_MANAGER = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_DISK
    from . import G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_MANAGER

from a.storage.disk import dell_raid_controller,logical_disk
from a.infra.basic.return_codes import ReturnCodes
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen
blinky_generated_enums=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen




#class LogicalDiskManager(object):
#    """
#    A class to map between a logical-disk and content-disk
#    """
#

#
#
#    def init (self,diskControllersCfgJson,pdisksCfgJson,logicalDisksCfgJson):
#        """
#
#
#            if (ldiskType == "BlockDeviceLogicalDisk"):
#                blockDevice = logicalDiskCfg["blockDevice"]
#                newLogicalDisk = logical_disk.BlockDeviceLogicalDisk(ldiskName,blockDevice,self._log)
#                self._log("diectory-logical-disk-created").debug1("BlockDeviceLogicalDisk was created (name=%s)",ldiskName)
#
#
#            if (ldiskType == "DirectoryLogicalDisk"):
#                newLogicalDisk = logical_disk.DirectoryLogicalDisk(ldiskName,self._log)
#                self._log("diectory-logical-disk-created").debug1("DirectoryLogicalDisk was created (name=%s)",ldiskName)
#
#
#            if (newLogicalDisk == None):
#                self._log("unsupported-logical-disk-type").error("logical-disk type '$s' is not a familiar one!",ldiskType)
#                return ReturnCodes.kBadParameter
#            else:
#                # add to pool
#                self._logicalDisks[ldiskName] = newLogicalDisk
#                self._log("adding-logical-disk-to-manager-pool").debug2("logical-disk (name=%s) was added to LogicalDiskManager pool",ldiskName)
#
#        self._log("logical-disk-mngr-init").debug2("LogicalDiskManager init() ended successfully!")
#        return ReturnCodes.kOk
#
#


##### new part for 3.0 starts here
class LogicalDiskManager(object):
    """                                                    
    A class to map between a logical-disk and content-disk 
    """                                                    
    def __init__ (self,logger,physicalDiskManager):

        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_DISK, G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_MANAGER)
        self._physicalDiskManager = physicalDiskManager
        self._candidateLogicalDiskList = {}
        self._runningLogicalDiskList   = {}



    ## Configuration related functions ##

    def preCreateLogicalDisk (self,key):
        self._log("precreate-logical-disk").debug3("preCreateLogicalDisk(key=%s)  was called, self._candidateLogicalDiskList[%s] = None",key,key)

        if key in self._candidateLogicalDiskList:
            self._log("logical-disk-already-exist").error("a logical disk named '%s' already exists",key)
            return ReturnCodes.kGeneralError

        self._candidateLogicalDiskList[key] = None

        return ReturnCodes.kOk


    def createLogicalDisk (self,key,implementatonType):

        logicalDisk = None
        if implementatonType == blinky_generated_enums.RaidArrayImplementationType.kDell:
            logicalDisk = logical_disk.DellRaid0Disk(key,self._physicalDiskManager,self._log)
        elif implementatonType == blinky_generated_enums.RaidArrayImplementationType.kSimulatedDevice:
            logicalDisk = logical_disk.BlockDeviceLogicalDisk(key,self._physicalDiskManager,self._log)
        elif implementatonType == blinky_generated_enums.RaidArrayImplementationType.kDirectory:
            logicalDisk = logical_disk.DirectoryLogicalDisk(key,self._physicalDiskManager,self._log)
        else:
            self._log("unsupported-type").error("logical disk type '%s' is not supported (logical disk '%s')",implementatonType,key)
            return None

        self._candidateLogicalDiskList[key] = logicalDisk
        return logicalDisk

    def managerTrxStart (self):
        self._log("logical-disk-manager-trx-start").debug3("managerTrxStart()  was called, running --> candidate, running = %s ,candidate = %s",self._runningLogicalDiskList,self._candidateLogicalDiskList)
        self._candidateLogicalDiskList = self._runningLogicalDiskList.copy()
        return ReturnCodes.kOk


    def managerTrxVerifyPublicConfig (self):

        self._log("logical-disk-manager-trx-verify-public").debug3("managerTrxVerifyPublicConfig() was called")
        ## place holder

        return ReturnCodes.kOk

    def managerTrxCommit (self):
        self._log("logical-disk-manager-trx-start").debug3("managerTrxCommit()  was called, candidate --> running, running = %s ,candidate = %s",self._runningLogicalDiskList,self._candidateLogicalDiskList)
        self._runningLogicalDiskList = self._candidateLogicalDiskList.copy()
        return ReturnCodes.kOk


    def managerTrxAbort (self):
        self._log("logical-disk-manager-trx-abort").debug3("managerTrxAbort() was called, None --> candidate")
        self._candidateLogicalDiskList = None
        return ReturnCodes.kOk


    #def diskRaidArrayTrxStart (self,key):
    #    self._log("disk-raid-array-trx-start").debug3("diskRaidArrayTrxStart(key=%s)  was called",key)
    #    if key not in self._candidateLogicalDiskList:
    #        self._log("no-logical-disk-for-trx-start").error("diskRaidArrayTrxStart(key=%s) failed, no logical disk with that name found")
    #        return ReturnCodes.kNotFound
    #
    #    logicalDisk = self._candidateLogicalDiskList[key]
    #    rc = logicalDisk.diskRaidArrayTrxStart()
    #    if rc != ReturnCodes.kOk:
    #        return ReturnCodes.kGeneralError
    #
    #    return ReturnCodes.kOk
    #
    #
    #def diskRaidArrayValueSet (self,key,data):
    #    self._log("disk-raid-array-value-set").debug3("diskRaidArrayValueSet(key=%s,data=%s)  was called",key,data)
    #    if key not in self._candidateLogicalDiskList:
    #        self._log("no-logical-disk-for-value-set").error("diskRaidArrayValueSet(key=%s,data=%s) failed, no logical disk with that name found")
    #        return ReturnCodes.kNotFound
    #
    #    logicalDisk = self._candidateLogicalDiskList[key]
    #    rc = logicalDisk.diskRaidArrayValueSet(data)
    #    if rc != ReturnCodes.kOk:
    #        return ReturnCodes.kGeneralError
    #
    #    return ReturnCodes.kOk
    #
    #
    #def diskRaidArrayTrxCommit (self,key):
    #    self._log("disk-raid-array-trx-commit").debug3("diskRaidArrayTrxCommit(key=%s)  was called",key)
    #    if key not in self._candidateLogicalDiskList:
    #        self._log("no-logical-disk-for-trx-commit").error("diskRaidArrayTrxCommit(key=%s) failed, no logical disk with that name found")
    #        return ReturnCodes.kNotFound
    #
    #    logicalDisk = self._candidateLogicalDiskList[key]
    #    rc = logicalDisk.diskRaidArrayTrxCommit()
    #    if rc != ReturnCodes.kOk:
    #        return ReturnCodes.kGeneralError
    #
    #    return ReturnCodes.kOk
    #
    #def diskRaidArrayTrxAbort (self,key):
    #    self._log("disk-raid-array-trx-abort").debug3("diskRaidArrayTrxAbort(key=%s)  was called",key)
    #    if key not in self._candidateLogicalDiskList:
    #        self._log("no-logical-disk-for-trx-abort").error("diskRaidArrayTrxAbort(key=%s) failed, no logical disk with that name found")
    #        return ReturnCodes.kNotFound
    #
    #    logicalDisk = self._candidateLogicalDiskList[key]
    #    rc = logicalDisk.diskRaidArrayTrxAbort()
    #    if rc != ReturnCodes.kOk:
    #        return ReturnCodes.kGeneralError
    #
    #    return ReturnCodes.kOk
    #
    #
    ## Periodic-work related functions ##

    def getRunningLogicalDisk (self,logicalDiskName):
        if logicalDiskName in self._runningLogicalDiskList:
            return self._runningLogicalDiskList[logicalDiskName]

        self._log("cannot-fetch-running-logical-disk").debug2("could not fetch running logical disk '%s'", logicalDiskName)
        return None

    def getCandidateLogicalDisk (self,logicalDiskName):
        if logicalDiskName in self._candidateLogicalDiskList:
            return self._candidateLogicalDiskList[logicalDiskName]

        self._log("cannot-fetch-candidate-logical-disk").debug2("could not fetch candidate logical disk '%s'", logicalDiskName)
        return None


    def activateLogicalDisk (self,logicalDiskName,forceInit):
        logicalDisk = self.getRunningLogicalDisk(logicalDiskName)
        if (logicalDisk == None):
            self._log("no-such-logical-disk").error("Activation of logical disk '%s' failed! no logical disk with that name exist.",logicalDiskName)
            return None,ReturnCodes.kNotFound
    
        self._log("activate-logical-disk").debug2("entering the activation of logical disk '%s'",logicalDiskName)
        blockDevice,rc = logicalDisk.activate(forceInit)
        return blockDevice,rc
    
    
    def getLogicalDiskDetailedStatus (self,logicalDiskName):
        logicalDisk = self.getRunningLogicalDisk(logicalDiskName)
        if (logicalDisk == None):
            self._log("no-such-logical-disk").error("status retrieval for logical disk '%s' failed! no logical disk with that name exist.",logicalDiskName)
            return None,ReturnCodes.kNotFound
    
        self._log("get-status-logical-disk").debug2("fetching status of logical disk '%s'",logicalDiskName)
        logicalDiskStatus,rc = logicalDisk.getDetailedStatus()
        return logicalDiskStatus,rc
    
    
    def getLogicalDiskStatus (self,logicalDiskName):
        logicalDisk = self.getRunningLogicalDisk(logicalDiskName)
        if (logicalDisk == None):
            self._log("no-such-logical-disk").error("status retrieval for logical disk '%s' failed! no logical disk with that name exist.",logicalDiskName)
            return None,ReturnCodes.kNotFound
    
        self._log("get-status-logical-disk").debug2("fetching status of logical disk '%s'",logicalDiskName)
        logicalDiskStatus,rc = logicalDisk.getStatus()
        return logicalDiskStatus,rc
    
   

