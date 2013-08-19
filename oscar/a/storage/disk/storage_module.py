# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz

if  __package__ is None:
    G_NAME_MODULE_STORAGE_MODULE = "unknown"
    G_NAME_GROUP_STORAGE_MODULE_STORAGE_MODULE = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_MODULE
    from . import G_NAME_GROUP_STORAGE_MODULE_STORAGE_MODULE


from a.infra.basic.return_codes import ReturnCodes
__pychecker__ = 'maxrefs=20'
import a.api.yang.modules.tech.common.qwilt_tech_storage_module.tech.storage.module.module_data_gen
blinky_generated_storage_module_data=a.api.yang.modules.tech.common.qwilt_tech_storage_module.tech.storage.module.module_data_gen
import a.api.yang.modules.tech.common.qwilt_tech_storage_module.qwilt_tech_storage_module_module_gen
blinky_generated_enums=a.api.yang.modules.tech.common.qwilt_tech_storage_module.qwilt_tech_storage_module_module_gen



class StorageModule(object):
    """
    A storage module
    """
    def __init__ (self,storageModuleName,controllerManager,logger):

        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_MODULE, G_NAME_GROUP_STORAGE_MODULE_STORAGE_MODULE)
        self._storageModuleName = storageModuleName
        self._controllerManager = controllerManager

        # configuration
        self._runningModuleConfig   = blinky_generated_storage_module_data.ModuleData()
        self._candidateModuleConfig = blinky_generated_storage_module_data.ModuleData()
        self._activeModuleConfig    = blinky_generated_storage_module_data.ModuleData()


    ## Configuration related functions ##
    
    def moduleTrxStart (self):
        self._log("storage-module-trx-start").debug3("moduleTrxStart()  was called for storage module %s, running --> candidate",self._storageModuleName)
        self._candidateModuleConfig.copyFrom(self._runningModuleConfig)
        return ReturnCodes.kOk

    def moduleValueSet (self,data):
        self._log("storage-module-value-set").debug3("moduleValueSet(data=%s)  was called for storage module %s, data --> candidate",data,self._storageModuleName)
        if not data.enabled:
            if (data.locationType == blinky_generated_enums.StorageModuleLocationTypeType.kInternal):
                errorString = "disabling internal storage module '%s' is not allowed"%self._storageModuleName
                return ReturnCodes.kGeneralError,errorString

        self._candidateModuleConfig.copyFrom(data)
        return ReturnCodes.kOk,None

    def moduleTrxCommit (self):
        self._log("storage-module-trx-commit").debug3("moduleTrxCommit()  was called for storage module %s, candidate --> running",self._storageModuleName)
        self._runningModuleConfig.copyFrom(self._candidateModuleConfig)
        return ReturnCodes.kOk

    def moduleTrxAbort (self):
        self._log("storage-module-trx-abort").debug3("moduleTrxAbort()  was called for storage module %s, None --> candidate",self._storageModuleName)
        self._candidateModuleConfig  = None
        return ReturnCodes.kOk


    ## Periodic-work related functions ##

    def pushRunningToActiveConfig (self):
        self._log("push-running-to-active").debug3("pushRunningToActiveConfig()  was called for storage module %s, running -- selective --> active",self._storageModuleName)
        self._activeModuleConfig.copyFrom(self._runningModuleConfig) # TODO: in future should be selective
        return ReturnCodes.kOk


    def isEnabled (self):
        return self._activeModuleConfig.enabled


    def getModuleStatus (self, tctx, operData):
        __pychecker__ = 'unusednames=tctx'
        if (self._activeModuleConfig.locationType == blinky_generated_enums.StorageModuleLocationTypeType.kInternal):
            operData.setLocation("internal")
        elif (self._activeModuleConfig.locationType == blinky_generated_enums.StorageModuleLocationTypeType.kExternal):
            operData.setLocation("external (controller at slot 6)") # TODO: in future get from hardware
        
        return ReturnCodes.kOk


    def getActualConfig(self, tctx, operData):
        __pychecker__ = 'unusednames=tctx'
        operData.setEnabled(self._activeModuleConfig.enabled)
        return ReturnCodes.kOk
