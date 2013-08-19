# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz

if  __package__ is None:
    G_NAME_MODULE_STORAGE_DISK = "unknown"
    G_NAME_GROUP_STORAGE_DISK_PHISICAL_DISK_MANAGER = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_DISK
    from . import G_NAME_GROUP_STORAGE_DISK_PHISICAL_DISK_MANAGER


from a.infra.basic.return_codes import ReturnCodes
import physical_disk
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen
blinky_generated_enums=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen

class PhysicalDiskManager(object):

    def __init__ (self,logger,controllerManager):

        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_DISK, G_NAME_GROUP_STORAGE_DISK_PHISICAL_DISK_MANAGER)
        self._controllerManager = controllerManager
        self._candidatePhysicalDiskList = {}
        self._runningPhysicalDiskList   = {}



    ## Configuration related functions ##

    def preCreatePhysicalDisk (self,key):
        self._log("precreate-physical-disk").debug3("preCreatePhysicalDisk(key=%s)  was called, self._candidatePhysicalDiskList[%s] = None",key,key)

        if key in self._candidatePhysicalDiskList:
            self._log("physical-disk-already-exist").error("a physical disk named '%s' already exists",key)
            return ReturnCodes.kGeneralError

        self._candidatePhysicalDiskList[key] = None

        return ReturnCodes.kOk


    def createPhysicalDisk (self,key,implementatonType):

        physicalDisk = None
        if implementatonType == blinky_generated_enums.DiskPhysicalImplementationType.kDell:
            physicalDisk = physical_disk.DellPhysicalDisk(key,self._controllerManager,self._log)
        elif implementatonType == blinky_generated_enums.DiskPhysicalImplementationType.kSimulatedDevice:
            physicalDisk = physical_disk.DummyPhysicalDisk(key,self._controllerManager,self._log)
        elif implementatonType == blinky_generated_enums.DiskPhysicalImplementationType.kDirectory:
            physicalDisk = physical_disk.DummyPhysicalDisk(key,self._controllerManager,self._log)
        else:
            self._log("unsupported-type").error("physical disk type '%s' is not supported (physical disk '%s')",implementatonType,key)
            return None

        self._candidatePhysicalDiskList[key] = physicalDisk
        return physicalDisk

    def managerTrxStart (self):
        self._log("physical-disk-manager-trx-start").debug3("managerTrxStart()  was called, running --> candidate, running = %s ,candidate = %s",self._runningPhysicalDiskList,self._candidatePhysicalDiskList)
        self._candidatePhysicalDiskList = self._runningPhysicalDiskList.copy()
        return ReturnCodes.kOk


    def managerTrxVerifyPublicConfig (self):

        self._log("physical-disk-manager-trx-verify-public").debug3("managerTrxVerifyPublicConfig() was called")
        uniqueIds = set()

        for key,physicalDisk in self._candidatePhysicalDiskList.items():
            physicalDiskId = physicalDisk.getCandidateId()
            if physicalDiskId in uniqueIds:
                self._log("duplicate-physical-disk-id").error("physical disk %s shares the same physical id (%s) as another physical disk in the candidate list",key,physicalDiskId)
                return ReturnCodes.kGeneralError
            else:
                uniqueIds.add(physicalDiskId)

        return ReturnCodes.kOk

    def managerTrxCommit (self):
        self._log("physical-disk-manager-trx-start").debug3("managerTrxCommit()  was called, candidate --> running, running = %s ,candidate = %s",self._runningPhysicalDiskList,self._candidatePhysicalDiskList)
        self._runningPhysicalDiskList = self._candidatePhysicalDiskList.copy()
        return ReturnCodes.kOk


    def managerTrxAbort (self):
        self._log("physical-disk-manager-trx-abort").debug3("managerTrxAbort() was called, None --> candidate")
        self._candidatePhysicalDiskList = None
        return ReturnCodes.kOk


    #def diskPhysicalTrxStart (self,key):
    #    self._log("disk-physical-trx-start").debug3("diskPhysicalTrxStart(key=%s)  was called",key)
    #    if key not in self._candidatePhysicalDiskList:
    #        self._log("no-physical-disk-for-trx-start").error("diskPhysicalTrxStart(key=%s) failed, no physical disk with that name found")
    #        return ReturnCodes.kNotFound
    #
    #    physicalDisk = self._candidatePhysicalDiskList[key]
    #    rc = physicalDisk.diskPhysicalTrxStart()
    #    if rc != ReturnCodes.kOk:
    #        return ReturnCodes.kGeneralError
    #
    #    return ReturnCodes.kOk
    #
    #
    #def diskPhysicalValueSet (self,key,data):
    #    self._log("disk-physical-value-set").debug3("diskPhysicalValueSet(key=%s,data=%s)  was called",key,data)
    #    if key not in self._candidatePhysicalDiskList:
    #        self._log("no-physical-disk-for-value-set").error("diskPhysicalValueSet(key=%s,data=%s) failed, no physical disk with that name found")
    #        return ReturnCodes.kNotFound
    #
    #    physicalDisk = self._candidatePhysicalDiskList[key]
    #    rc = physicalDisk.diskPhysicalValueSet(data)
    #    if rc != ReturnCodes.kOk:
    #        return ReturnCodes.kGeneralError
    #
    #    return ReturnCodes.kOk
    #
    #
    #def diskPhysicalTrxCommit (self,key):
    #    self._log("disk-physical-trx-commit").debug3("diskPhysicalTrxCommit(key=%s)  was called",key)
    #    if key not in self._candidatePhysicalDiskList:
    #        self._log("no-physical-disk-for-trx-commit").error("diskPhysicalTrxCommit(key=%s) failed, no physical disk with that name found")
    #        return ReturnCodes.kNotFound
    #
    #    physicalDisk = self._candidatePhysicalDiskList[key]
    #    rc = physicalDisk.diskPhysicalTrxCommit()
    #    if rc != ReturnCodes.kOk:
    #        return ReturnCodes.kGeneralError
    #
    #    return ReturnCodes.kOk
    #
    #def diskPhysicalTrxAbort (self,key):
    #    self._log("disk-physical-trx-abort").debug3("diskPhysicalTrxAbort(key=%s)  was called",key)
    #    if key not in self._candidatePhysicalDiskList:
    #        self._log("no-physical-disk-for-trx-abort").error("diskPhysicalTrxAbort(key=%s) failed, no physical disk with that name found")
    #        return ReturnCodes.kNotFound
    #
    #    physicalDisk = self._candidatePhysicalDiskList[key]
    #    rc = physicalDisk.diskPhysicalTrxAbort()
    #    if rc != ReturnCodes.kOk:
    #        return ReturnCodes.kGeneralError
    #
    #    return ReturnCodes.kOk
    #

    ## Periodic-work related functions ##

    def getRunningPhysicalDisk (self,logicalDiskName):
        if logicalDiskName in self._runningPhysicalDiskList:
            return self._runningPhysicalDiskList[logicalDiskName]

        self._log("cannot-fetch-running-physical-disk").debug2("could not fetch running physical disk '%s'", logicalDiskName)
        return None

    def getCandidatePhysicalDisk (self,logicalDiskName):
        if logicalDiskName in self._candidatePhysicalDiskList:
            return self._candidatePhysicalDiskList[logicalDiskName]

        self._log("cannot-fetch-candidate-physical-disk").debug2("could not fetch candidate physical disk '%s'", logicalDiskName)
        return None
                

