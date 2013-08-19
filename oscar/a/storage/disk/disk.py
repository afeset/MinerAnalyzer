# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz


if  __package__ is None:
    G_NAME_MODULE_STORAGE_DISK = "unknown"
    G_NAME_GROUP_STORAGE_DISK_DISK_MAPPER = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_DISK
    from . import G_NAME_GROUP_STORAGE_DISK_DISK_MAPPER


from a.infra.basic.return_codes import ReturnCodes
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen #  impoting with 'as blinky_generated_enums' causes stupid pycheck warnings
blinky_generated_enums=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen  



class DiskMapper(object):

    def __init__ (self,contentDiskManager,logicalDiskManager,physicalDiskManager,fileSystemManager,logger):

        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_DISK, G_NAME_GROUP_STORAGE_DISK_DISK_MAPPER)

        self._runningMap = {}
        self._candidateMap = {}
        self._contentDiskManager  = contentDiskManager
        self._logicalDiskManager  = logicalDiskManager 
        self._physicalDiskManager = physicalDiskManager
        self._fileSystemManager   = fileSystemManager  

    def __repr__ (self):
        return "disk-mapper"


    def setConfigMsgFunctor (self, configMsgFunctor):
        self._setConfigMsg = configMsgFunctor
    

    def _dummyMsgFunctor (self):
        pass


    #---- disk manager related functions -----------#

    def managerTrxStart (self):
        self._log("disk-mapper-trx-start").debug2("managerTrxStart()  was called, running --> candidate, running = %s ,candidate = %s",self._runningMap,self._candidateMap)
        self._candidateMap = self._runningMap.copy()
        if (self._contentDiskManager.managerTrxStart() == ReturnCodes.kOk): #TODO: add system disk manager
            return ReturnCodes.kOk

        self._log("disk-mapper-trx-start-fail").error("managerTrxStart() failed!")
        return ReturnCodes.kGeneralError


    def managerTrxVerifyPublicConfig (self):
        if (None in self._candidateMap.values()):
            self._log("disk-mapper-trx-validate-public-fail").error("managerTrxVerifyPublicConfig() failed! some disks were not created (map = %s)",self._candidateMap)
            return ReturnCodes.kGeneralError

        if (self._contentDiskManager.managerTrxVerifyPublicConfig() != ReturnCodes.kOk): # TODO: add system disk manager
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def managerTrxCommit (self):
        self._log("disk-mapper-trx-start").debug2("managerTrxCommit()  was called, candidate --> running, running = %s ,candidate = %s",self._runningMap,self._candidateMap)
        self._runningMap = self._candidateMap.copy()
        if (self._contentDiskManager.managerTrxCommit() == ReturnCodes.kOk):
            return ReturnCodes.kOk

        self._log("disk-mapper-trx-commit-fail").error("managerTrxCommit() failed!")
        return ReturnCodes.kGeneralError


    def managerTrxAbort (self):
        self._log("disk-mapper-trx-abort").debug2("managerTrxAbort() was called, None --> candidate")
        self._candidateMap = None
        if (self._contentDiskManager.managerTrxAbort() == ReturnCodes.kOk):
            return ReturnCodes.kOk

        self._log("disk-mapper-trx-abort-fail").error("managerTrxAbort() failed!")
        return ReturnCodes.kGeneralError


    def isDiskInMap (self,key):
        return (key in self._candidateMap)

    def preCreateDisk (self,key):
        self._log("pre-create-disk").debug1("preCreateDisk(key=%s) called, self._candidateMap[%s] = None",key,key)
        if self.isDiskInMap(key):
            self._log("disk-already-exists").error("cannot re-add disk '%s'", key)
            self._setConfigMsg("cannot re-add disk '%s'"%key)
            return ReturnCodes.kAlreadyExists

        self._candidateMap[key] = None

        return ReturnCodes.kOk

    
    #---- disk related functions -----------#

    def diskTrxStart (self,key):

        self._log("disk-trx-start").debug1("diskTrxStart(key=%s) called -> inducing disk manager's function for this disk",key)
        if key not in self._candidateMap or (self._candidateMap[key] == None):
            self._log("disk-not-found").error("diskTrxStart(key=%s) failed: disk is not defined",key)

        if (self._candidateMap[key].diskTrxStart(key) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def diskTrxCommit (self,key):

        self._log("disk-trx-commit").debug1("diskTrxCommit(key=%s) called -> inducing disk manager's function for this disk",key)
        if key not in self._candidateMap or (self._candidateMap[key] == None):
            self._log("disk-not-found").error("diskTrxCommit(key=%s) failed: disk is not defined",key)

        if (self._candidateMap[key].diskTrxCommit(key) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def diskTrxAbort (self,key):

        self._log("disk-trx-abort").debug1("diskTrxAbort(key=%s) called -> inducing disk manager's function for this disk",key)
        if key not in self._candidateMap or (self._candidateMap[key] == None):
            self._log("disk-not-found").error("diskTrxAbort(key=%s) failed: disk is not defined",key)

        if (self._candidateMap[key].diskTrxAbort(key) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def diskValueSet (self,key,data):

        self._log("disk-value-set").debug1("diskValueSet(key=%s,data=%s) called -> inducing disk manager's function for this disk",key,data)
        if key not in self._candidateMap:
            self._log("key-not-in-map").error("cannot value set disk '%s'. key is not in disk mapper")
            return ReturnCodes.kGeneralError

        if (self._candidateMap[key] == None): # late create
            if (data.functionalType == blinky_generated_enums.DiskFunctionalTypesType.kContent):
                self._candidateMap[key] = self._contentDiskManager
                if (self._contentDiskManager.createDisk(key) != ReturnCodes.kOk):
                    self._log("failed-create-content-disk").error("failed to create content disk '%s'",key)
                    return ReturnCodes.kGeneralError

            else:
                return ReturnCodes.kUnSupported # TODO: continue this switch statement

        if (self._candidateMap[key].diskValueSet(key,data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def getDiskStatus (self, key, tctx, operData):
        __pychecker__ = 'unusednames=tctx'

        self._log("get-disk-status").debug1("getDiskStatus(key=%s) called -> inducing disk manager's function for this disk",key)
        if ((key not in self._runningMap) or (self._runningMap[key] == None)):
            self._log("disk-not-found").error("getDiskStatus(key=%s) failed: disk is not defined well (None in mapper)",key)
            return ReturnCodes.kGeneralError


        rc = self._runningMap[key].getDiskStatus(key,operData)
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk
        

    def getDiskAlarm (self, key, tctx, operData):  
        __pychecker__ = 'unusednames=tctx'

        self._log("get-disk-alarm").debug1("getDiskAlarm(key=%s) called -> inducing disk manager's function for this disk",key)
        if key not in self._runningMap or (self._runningMap[key] == None):
            self._log("disk-not-found").error("getDiskAlarm(key=%s) failed: disk is not defined well (None in mapper)",key)
            return ReturnCodes.kGeneralError

        rc = self._runningMap[key].getDiskAlarm(key,operData)
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    #---- disk physical related functions -----------#

    def preCreatePhysicalDisk (self, key):
        self._log("pre-create-physical-disk").debug1("preCreatePhysicalDisk(key=%s) called in mapper",key)
        if (self._physicalDiskManager.preCreatePhysicalDisk(key) != ReturnCodes.kOk):
            self._log("pre-create-failed").error("preCreatePhysicalDisk(key=%s) failed!",key)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


   # def diskPhysicalTrxStart (self, key):
   #     self._log("disk-physical-trx-start").debug1("diskPhysicalTrxStart(key=%s) called -> inducing disk manager's function for this disk physical",key)
   #     if key not in self._candidateMap or (self._candidateMap[key] == None):
   #         self._log("disk-not-found").error("diskPhysicalTrxStart(key=%s) failed: disk is not defined",key)
   #
   #     #self._candidateMap[key].diskTrxStart(key) # TODO: uncomment
   #     return ReturnCodes.kOk
   #
   #
   # def diskPhysicalTrxCommit (self, key):
   #     self._log("disk-physical-trx-commit").debug1("diskPhysicalTrxCommit(key=%s) called -> inducing disk manager's function for this disk physical",key)
   #     #self._candidateMap[key].diskTrxCommit(key) # TODO: uncomment
   #
   #     return ReturnCodes.kOk
   #
   #
   # def diskPhysicalTrxAbort (self, key):
   #     self._log("disk-physical-trx-abort").debug1("diskPhysicalTrxAbort(key=%s) called -> inducing disk manager's function for this disk physical",key)
   #     #self._candidateMap[key].diskTrxAbort(key) # TODO: uncomment
   #
   #     return ReturnCodes.kOk
   #

    def diskPhysicalValueSet (self, key, data):
        self._log("disk-physical-value-set").debug1("diskPhysicalValueSet(key=%s,data=%s) called -> inducing disk manager's function for this disk physical",key,data)
        if key not in self._candidateMap or (self._candidateMap[key] == None):
            self._log("disk-not-found").error("diskPhysicalValueSet(key=%s) failed: disk is not in mapper",key)

        if (self._candidateMap[key].diskPhysicalValueSet(key,data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    
    def getDiskPhysicalStatus (self, key, tctx, operData):
        __pychecker__ = 'unusednames=tctx'

        self._log("get-disk-physical-status").debug1("getDiskPhysicalStatus(key=%s) called -> inducing disk manager's function for this disk",key)
        if ((key not in self._runningMap) or (self._runningMap[key] == None)):
            self._log("disk-not-found").error("getDiskPhysicalStatus(key=%s) failed: disk is not defined well (None in mapper)",key)
            return ReturnCodes.kGeneralError

        rc = self._runningMap[key].getDiskPhysicalStatus(key,operData)
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk        


    #---- disk raid-array related functions -----------#

    def preCreateLogicalDisk (self, key):
        self._log("pre-create-logical-disk").debug1("preCreateLogicalDisk(key=%s) called in mapper",key)
        if (self._logicalDiskManager.preCreateLogicalDisk(key) != ReturnCodes.kOk):
            self._log("pre-create-failed").error("preCreateLogicalDisk(key=%s) failed!",key)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


   # def diskRaidArrayTrxStart (self, key):
   #     self._log("disk-raid-array-trx-start").debug1("diskRaidArrayTrxStart(key=%s) called -> inducing disk manager's function for this disk raid-array",key)
   #     if key not in self._candidateMap or (self._candidateMap[key] == None):
   #         self._log("disk-not-found").error("diskRaidArrayTrxStart(key=%s) failed: disk is not defined",key)
   #
   #     #self._candidateMap[key].diskTrxStart(key) # TODO: uncomment
   #     return ReturnCodes.kOk
   #
   #
   # def diskRaidArrayTrxCommit (self, key):
   #     self._log("disk-raid-array-trx-commit").debug1("diskRaidArrayTrxCommit(key=%s) called -> inducing disk manager's function for this disk raid-array",key)
   #     #self._candidateMap[key].diskTrxCommit(key) # TODO: uncomment
   #
   #     return ReturnCodes.kOk
   #
   #
   # def diskRaidArrayTrxAbort (self, key):
   #     self._log("disk-raid-array-trx-abort").debug1("diskRaidArrayTrxAbort(key=%s) called -> inducing disk manager's function for this disk raid-array",key)
   #     #self._candidateMap[key].diskTrxAbort(key) # TODO: uncomment
   #
   #     return ReturnCodes.kOk


    def diskRaidArrayValueSet (self, key, data):
        self._log("disk-raid-array-value-set").debug1("diskRaidArrayValueSet(key=%s,data=%s) called -> inducing disk manager's function for this disk raid-array",key,data)
        if key not in self._candidateMap or (self._candidateMap[key] == None):
            self._log("disk-not-found").error("diskRaidArrayValueSet(key=%s) failed: disk is not in mapper",key)

        if (self._candidateMap[key].diskRaidArrayValueSet(key,data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    
    def getDiskRaidArrayStatus (self, key, tctx, operData):
        __pychecker__ = 'unusednames=tctx'

        self._log("get-disk-raid-array-status").debug1("getDiskRaidArrayStatus(key=%s) called -> inducing disk manager's function for this disk",key)
        if ((key not in self._runningMap) or (self._runningMap[key] == None)):
            self._log("disk-not-found").error("getDiskRaidArrayStatus(key=%s) failed: disk is not defined well (None in mapper)",key)
            return ReturnCodes.kGeneralError

        rc = self._runningMap[key].getDiskRaidArrayStatus(key,operData)
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    #---- disk file-system related functions -----------#
    
    def preCreateFileSystem (self, key):
        self._log("pre-create-file-system").debug1("preCreateFileSystem(key=%s) called in mapper",key)
        if (self._fileSystemManager.preCreateFileSystem(key) != ReturnCodes.kOk):
            self._log("pre-create-failed").error("preCreateFileSystem(key=%s) failed!",key)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk
    

    #def diskFileSystemTrxStart (self, key):
    #    self._log("disk-file-system-trx-start").debug1("diskFileSystemTrxStart(key=%s) called -> inducing disk manager's function for this disk file-system",key)
    #    if key not in self._candidateMap or (self._candidateMap[key] == None):
    #        self._log("disk-not-found").error("diskFileSystemTrxStart(key=%s) failed: disk is not defined",key)
    #
    #    #self._candidateMap[key].diskTrxStart(key) # TODO: uncomment
    #    return ReturnCodes.kOk
    #
    #
    #def diskFileSystemTrxCommit (self, key):
    #    self._log("disk-file-system-trx-commit").debug1("diskFileSystemTrxCommit(key=%s) called -> inducing disk manager's function for this disk file-system",key)
    #    #self._candidateMap[key].diskTrxCommit(key) # TODO: uncomment
    #
    #    return ReturnCodes.kOk
    #
    #
    #def diskFileSystemTrxAbort (self, key):
    #    self._log("disk-file-system-trx-abort").debug1("diskFileSystemTrxAbort(key=%s) called -> inducing disk manager's function for this disk file-system",key)
    #    #self._candidateMap[key].diskTrxAbort(key) # TODO: uncomment
    #
    #    return ReturnCodes.kOk


    def diskFileSystemValueSet (self, key, data):
        self._log("disk-file-system-value-set").debug1("diskFileSystemValueSet(key=%s,data=%s) called -> inducing disk manager's function for this disk file-system",key,data)
        if key not in self._candidateMap or (self._candidateMap[key] == None):
            self._log("disk-not-found").error("diskFileSystemValueSet(key=%s) failed: disk is not in mapper",key)

        if (self._candidateMap[key].diskFileSystemValueSet(key,data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def getDiskFileSystemStatus (self, key, tctx, operData):
        __pychecker__ = 'unusednames=tctx'

        self._log("get-disk-file-system-status").debug1("getDiskFileSystemStatus(key=%s) called -> inducing disk manager's function for this disk",key)
        if ((key not in self._runningMap) or (self._runningMap[key] == None)):
            self._log("disk-not-found").error("getDiskFileSystemStatus(key=%s) failed: disk is not defined well (None in mapper)",key)
            return ReturnCodes.kGeneralError

        rc = self._runningMap[key].getDiskFileSystemStatus(key,operData)
        if (rc != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk
        

    #---- disk file-system commands and timeouts related functions -----------#

    def diskFileSystemCommandsValueSet (self, key, data):
        self._log("disk-file-system-commands-value-set").debug1("diskFileSystemCommandsValueSet(key=%s,data=%s) called -> inducing disk manager's function for this disk file-system",key,data)
        if key not in self._candidateMap or (self._candidateMap[key] == None):
            self._log("disk-not-found").error("diskFileSystemCommandsValueSet(key=%s) failed: disk is not in mapper",key)

        if (self._candidateMap[key].diskFileSystemCommandsValueSet(key,data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def diskFileSystemTimeoutsValueSet (self, key, data):
        self._log("disk-file-system-timeouts-value-set").debug1("diskFileSystemTimeoutsValueSet(key=%s,data=%s) called -> inducing disk manager's function for this disk file-system",key,data)
        if key not in self._candidateMap or (self._candidateMap[key] == None):
            self._log("disk-not-found").error("diskFileSystemTimeoutsValueSet(key=%s) failed: disk is not in mapper",key)

        if (self._candidateMap[key].diskFileSystemTimeoutsValueSet(key,data) != ReturnCodes.kOk):
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk



