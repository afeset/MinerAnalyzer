# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz

if  __package__ is None:
    G_NAME_MODULE_STORAGE_MODULE = "unknown"
    G_NAME_GROUP_STORAGE_MODULE_STORAGE_MODULE_MANAGER = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_MODULE
    from . import G_NAME_GROUP_STORAGE_MODULE_STORAGE_MODULE_MANAGER


from a.infra.basic.return_codes import ReturnCodes
import storage_module

class StorageModuleManager(object):

    def __init__ (self,logger,controllerManager):

        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_MODULE, G_NAME_GROUP_STORAGE_MODULE_STORAGE_MODULE_MANAGER)
        self._controllerManager = controllerManager
        self._candidateStorageModuleList = {}
        self._runningStorageModuleList   = {}



    ## Configuration related functions ##

    def createModule (self,key):

        module = storage_module.StorageModule(key,self._controllerManager,self._log)
        self._candidateStorageModuleList[key] = module
        return module

    def managerTrxStart (self):
        self._log("storage-module-manager-trx-start").debug3("managerTrxStart()  was called, running --> candidate, running = %s ,candidate = %s",self._runningStorageModuleList,self._candidateStorageModuleList)
        self._candidateStorageModuleList = self._runningStorageModuleList.copy()
        return ReturnCodes.kOk


    def managerTrxVerifyPublicConfig (self):

        self._log("storage-module-manager-trx-verify-public").debug3("managerTrxVerifyPublicConfig() was called")
        return ReturnCodes.kOk

    def managerTrxCommit (self):
        self._log("storage-module-manager-trx-start").debug3("managerTrxCommit()  was called, candidate --> running, running = %s ,candidate = %s",self._runningStorageModuleList,self._candidateStorageModuleList)
        self._runningStorageModuleList = self._candidateStorageModuleList.copy()
        return ReturnCodes.kOk


    def managerTrxAbort (self):
        self._log("storage-module-manager-trx-abort").debug3("managerTrxAbort() was called, None --> candidate")
        self._candidateStorageModuleList = None
        return ReturnCodes.kOk


    ## Periodic-work related functions ##

    def pushAllStorageModuleRunningToActive (self):

        for key,module in self._runningStorageModuleList.items():
            if (module.pushRunningToActiveConfig() != ReturnCodes.kOk):
                self._log("push-running-to-active-fail").error("pushing running to active of storage module '%s' failed!",key)
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def getStorageModule (self,storageModuleName):
        if storageModuleName in self._runningStorageModuleList:
            return self._runningStorageModuleList[storageModuleName]

        self._log("cannot-fetch-running-storage-module").debug2("could not fetch running storage module '%s'", storageModuleName)
        return None


    def getCandidateStorageModule (self,storageModuleName):
        if storageModuleName in self._candidateStorageModuleList:
            return self._candidateStorageModuleList[storageModuleName]

        self._log("cannot-fetch-candidate-storage-module").debug2("could not fetch candidate storage module '%s'", storageModuleName)
        return None


    def isQsmEnabled (self):
        if (len(self._runningStorageModuleList) > 1):
            for module in self._runningStorageModuleList.values():
                if not module.isEnabled():
                    break

            else:
                return True

        return False


