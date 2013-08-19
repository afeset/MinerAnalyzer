# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz


if  __package__ is None:
    G_NAME_MODULE_STORAGE_DISK = "unknown"
    G_NAME_GROUP_STORAGE_DISK_FILE_SYSTEM_MANAGER = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_DISK
    from . import G_NAME_GROUP_STORAGE_DISK_FILE_SYSTEM_MANAGER

import file_system
from a.infra.basic.return_codes import ReturnCodes
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen
blinky_generated_enums=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen

class FileSystemManager(object):
    """
    A class to map between a file-system and content-disk
    """

    def __init__ (self,logger):
        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_DISK, G_NAME_GROUP_STORAGE_DISK_FILE_SYSTEM_MANAGER)
        self._candidateFileSystemList   = {}
        self._runningFileSystemList = {}


    ## Configuration related functions ##

    def preCreateFileSystem (self,key):
        self._log("precreate-file-system-disk").debug3("preCreateFileSystem(key=%s)  was called, self._candidateFileSystemList[%s] = None",key,key)

        if key in self._candidateFileSystemList:
            self._log("file-system-already-exist").error("a file system named '%s' already exists",key)
            return ReturnCodes.kGeneralError

        self._candidateFileSystemList[key] = None

        return ReturnCodes.kOk


    def createFileSystem (self,key,fileSystemType):

        fileSystem = None
        if ((fileSystemType == blinky_generated_enums.FileSystemTypeType.kExt3) or (fileSystemType == blinky_generated_enums.FileSystemTypeType.kExt4)):
            fileSystem = file_system.ExtFileSystem(key,self._log)
        elif (fileSystemType == blinky_generated_enums.FileSystemTypeType.kDirectory):
            fileSystem = file_system.DirectoryFileSystem(key,self._log)
        else:
            self._log("unsupported-type").error("file system type '%s' is not supported (file system '%s')",fileSystemType,key)
            return None

        self._candidateFileSystemList[key] = fileSystem
        return fileSystem


    def managerTrxStart (self):
        self._log("file-system-disk-manager-trx-start").debug3("managerTrxStart()  was called, running --> candidate, running = %s ,candidate = %s",self._runningFileSystemList,self._candidateFileSystemList)
        self._candidateFileSystemList = self._runningFileSystemList.copy()
        return ReturnCodes.kOk


    def managerTrxVerifyPublicConfig (self):

        self._log("file-system-manager-trx-verify-public").debug3("managerTrxVerifyPublicConfig() was called")
        # place holder

        return ReturnCodes.kOk

    def managerTrxCommit (self):
        self._log("file-system-manager-trx-start").debug3("managerTrxCommit()  was called, candidate --> running, running = %s ,candidate = %s",self._runningFileSystemList,self._candidateFileSystemList)
        self._runningFileSystemList= self._candidateFileSystemList.copy()
        return ReturnCodes.kOk


    def managerTrxAbort (self):
        self._log("file-system-manager-trx-abort").debug3("managerTrxAbort() was called, None --> candidate")
        self._candidateFileSystemList = None
        return ReturnCodes.kOk

   # def diskFileSystemTrxStart (self,key):
   #     self._log("disk-file-system-trx-start").debug3("diskFileSystemTrxStart(key=%s)  was called",key)
   #     if key not in self._candidateFileSystemList:
   #         self._log("no-file-system-disk-for-trx-start").error("diskFileSystemTrxStart(key=%s) failed, no file system with that name found")
   #         return ReturnCodes.kNotFound
   #
   #     fileSystem = self._candidateFileSystemList[key]
   #     rc = fileSystem.diskFileSystemTrxStart()
   #     if rc != ReturnCodes.kOk:
   #         return ReturnCodes.kGeneralError
   #
   #     return ReturnCodes.kOk
   #
   #
   # def diskFileSystemValueSet (self,key,data):
   #     self._log("disk-file-system-value-set").debug3("diskFileSystemValueSet(key=%s,data=%s)  was called",key,data)
   #     if key not in self._candidateFileSystemList:
   #         self._log("no-file-system-disk-for-value-set").error("diskFileSystemValueSet(key=%s,data=%s) failed, no file system with that name found")
   #         return ReturnCodes.kNotFound
   #
   #     fileSystem = self._candidateFileSystemList[key]
   #     rc = fileSystem.diskFileSystemValueSet(data)
   #     if rc != ReturnCodes.kOk:
   #         return ReturnCodes.kGeneralError
   #
   #     return ReturnCodes.kOk
   #
   #
   # def diskFileSystemTrxCommit (self,key):
   #     self._log("disk-file-system-trx-commit").debug3("diskFileSystemTrxCommit(key=%s)  was called",key)
   #     if key not in self._candidateFileSystemList:
   #         self._log("no-file-system-disk-for-trx-commit").error("diskFileSystemTrxCommit(key=%s) failed, no file system with that name found")
   #         return ReturnCodes.kNotFound
   #
   #     fileSystem = self._candidateFileSystemList[key]
   #     rc = fileSystem.diskFileSystemTrxCommit()
   #     if rc != ReturnCodes.kOk:
   #         return ReturnCodes.kGeneralError
   #
   #     return ReturnCodes.kOk
   #
   # def diskFileSystemTrxAbort (self,key):
   #     self._log("disk-file-system-trx-abort").debug3("diskFileSystemTrxAbort(key=%s)  was called",key)
   #     if key not in self._candidateFileSystemList:
   #         self._log("no-file-system-disk-for-trx-abort").error("diskFileSystemTrxAbort(key=%s) failed, no file system with that name found")
   #         return ReturnCodes.kNotFound
   #
   #     fileSystem = self._candidateFileSystemList[key]
   #     rc = fileSystem.diskFileSystemTrxAbort()
   #     if rc != ReturnCodes.kOk:
   #         return ReturnCodes.kGeneralError
   #
   #     return ReturnCodes.kOk
   #
   #
    ## Periodic-work related functions ##

    def getRunningFileSystem (self,logicalDiskName):
        if logicalDiskName in self._runningFileSystemList:
            return self._runningFileSystemList[logicalDiskName]

        self._log("cannot-fetch-running-file-system").debug2("could not fetch running file system '%s'", logicalDiskName)
        return None

    def getCandidateFileSystem (self,logicalDiskName):
        if logicalDiskName in self._candidateFileSystemList:
            return self._candidateFileSystemList[logicalDiskName]

        self._log("cannot-fetch-candidate-file-system").debug2("could not fetch candidate file system '%s'", logicalDiskName)
        return None

    def activateGetCurrentUuid (self,logicalDiskName):
        fileSystem = self._runningFileSystemList.get(logicalDiskName)
        if (fileSystem == None):
            self._log("no-such-file-system").error("can't fetch currentUuid of file-system (logical disk='%s')! no file system for that disk was defined.",logicalDiskName)
            return None

        return fileSystem.activateGetCurrentUuid()


    def getFileSystemDetailedStatus (self,logicalDiskName):
        fileSystem = self._runningFileSystemList.get(logicalDiskName)
        if (fileSystem == None):
            self._log("no-such-file-system").error("can't fetch detailed status for file-system (logical disk='%s')! no file system for that disk was defined.",logicalDiskName)
            return None,ReturnCodes.kNotFound

        return fileSystem.getDetailedStatus()


    def getFileSystemStatus (self,logicalDiskName,operData):
        fileSystem = self._runningFileSystemList.get(logicalDiskName)
        if (fileSystem == None):
            self._log("no-such-file-system").error("can't fetch oper status for file-system (logical disk='%s')! no file system for that disk was defined.",logicalDiskName)
            return ReturnCodes.kNotFound

        return fileSystem.getStatus(operData)


    def setInitialActivationParams (self,logicalDiskName,mountingPoint,expectedUuid,forceInit):
        fileSystem = self._runningFileSystemList.get(logicalDiskName)

        if (fileSystem == None):
            self._log("no-such-file-system").error("indusing setInitialActivationParams() of file-system for logical disk '%s' failed! no file system for that disk was defined.",logicalDiskName)
            return ReturnCodes.kNotFound

        rc = fileSystem.setInitialActivationParams(mountingPoint,expectedUuid,forceInit)
        if (rc != ReturnCodes.kOk):
            self._log("file-system-initial-param-failed").error("indusing setInitialActivationParams() of file-system for logical disk '%s' failed!",logicalDiskName)
        else:
            self._log("file-system-initial-param-success").debug2("indusing setInitialActivationParams() of file-system for logical disk '%s' succeeded!",logicalDiskName)
        return rc


    def setIntermediateActivationParams (self,logicalDiskName,blockDevice):
        fileSystem = self._runningFileSystemList.get(logicalDiskName)

        if (fileSystem == None):
            self._log("no-such-file-system").error("indusing setIntermediateActivationParams() of file-system for logical disk '%s' failed! no file-system for that disk was defined.",logicalDiskName)
            return ReturnCodes.kNotFound

        rc = fileSystem.setIntermediateActivationParams(blockDevice)
        if (rc != ReturnCodes.kOk):
            self._log("file-system-inter-param-failed").error("indusing setIntermediateActivationParams() of file-system for logical disk '%s' failed!",logicalDiskName)
        else:
            self._log("file-system-inter-param-success").debug2("indusing setIntermediateActivationParams() of file-system for logical disk '%s' succeeded!",logicalDiskName)
        return rc


    def unmount (self,logicalDiskName):
        fileSystem = self._runningFileSystemList.get(logicalDiskName)

        if (fileSystem == None):
            self._log("no-such-file-system").error("indusing unmount() of file-system for logical disk '%s' failed! no file-system for that disk was defined.",logicalDiskName)
            return ReturnCodes.kNotFound

        rc = fileSystem.unmount()
        if (rc != ReturnCodes.kOk):
            self._log("file-system-unmount-failed").error("indusing unmount() of file-system for logical disk '%s' failed!",logicalDiskName)
        else:
            self._log("file-system-unmount-success").debug2("indusing unmount() of file-system for logical disk '%s' succeeded!",logicalDiskName)
        return rc


    def activatePhase1 (self,logicalDiskName):
        fileSystem = self._runningFileSystemList.get(logicalDiskName)

        if (fileSystem == None):
            self._log("no-such-file-system").error("indusing activatePhase1() of file-system for logical disk '%s' failed! no file-system for that disk was defined.",logicalDiskName)
            return ReturnCodes.kNotFound

        rc = fileSystem.activatePhase1()
        if (rc != ReturnCodes.kOk):
            self._log("file-system-phase1-failed").error("indusing activatePhase1() of file-system for logical disk '%s' failed!",logicalDiskName)
        else:
            self._log("file-system-phase1-success").debug2("indusing activatePhase1() of file-system for logical disk '%s' succeeded!",logicalDiskName)
        return rc


    def activatePhase2 (self,logicalDiskName):
        fileSystem = self._runningFileSystemList.get(logicalDiskName)

        if (fileSystem == None):
            self._log("no-such-file-system").error("indusing activatePhase2() of file-system for logical disk '%s' failed! no file-system for that disk was defined.",logicalDiskName)
            return ReturnCodes.kNotFound

        rc = fileSystem.activatePhase2()
        if ((rc != ReturnCodes.kOk) and (rc != ReturnCodes.kAlreadyExists)):
            self._log("file-system-phase2-failed").error("indusing activatePhase2() of file-system for logical disk '%s' failed!",logicalDiskName)
        else:
            self._log("file-system-phase2-success").debug2("indusing activatePhase2() of file-system for logical disk '%s' succeeded!",logicalDiskName)
        return rc


    def activatePhase3 (self,logicalDiskName):
        fileSystem = self._runningFileSystemList.get(logicalDiskName)

        if (fileSystem == None):
            self._log("no-such-file-system").error("indusing activatePhase3() of file-system for logical disk '%s' failed! no file-system for that disk was defined.",logicalDiskName)
            return ReturnCodes.kNotFound

        rc = fileSystem.activatePhase3()
        if (rc != ReturnCodes.kOk):
            self._log("file-system-phase3-failed").error("indusing activatePhase3() of file-system for logical disk '%s' failed!",logicalDiskName)
        else:
            self._log("file-system-phase3-success").debug2("indusing activatePhase3() of file-system for logical disk '%s' succeeded!",logicalDiskName)
        return rc


    def activatePhase4 (self,logicalDiskName):
        fileSystem = self._runningFileSystemList.get(logicalDiskName)

        if (fileSystem == None):
            self._log("no-such-file-system").error("indusing activatePhase4() of file-system for logical disk '%s' failed! no file-system for that disk was defined.",logicalDiskName)
            return ReturnCodes.kNotFound

        rc = fileSystem.activatePhase4()
        if (rc != ReturnCodes.kOk):
            self._log("file-system-phase4-failed").error("indusing activatePhase4() of file-system for logical disk '%s' failed!",logicalDiskName)
        else:
            self._log("file-system-phase4-success").debug2("indusing activatePhase4() of file-system for logical disk '%s' succeeded!",logicalDiskName)
        return rc


    def unmountAll (self,logicalDiskNames):
        failedFileSystems = []
        for logicalDiskName in logicalDiskNames:
            rc = self.unmount(logicalDiskName)
            if (rc != ReturnCodes.kOk):
                self._log("failed-unmount").error("failed to unmount file system of logical disk %s",logicalDiskName)
                failedFileSystems.append(logicalDiskName)

        if (len(failedFileSystems) > 0):
            self._log("failed-unmount-list").error("the following logical disks failed to unmount %s",failedFileSystems)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk





