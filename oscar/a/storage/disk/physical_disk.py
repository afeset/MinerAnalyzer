# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz

if  __package__ is None:
    G_NAME_MODULE_STORAGE_DISK = "unknown"
    G_NAME_GROUP_STORAGE_DISK_PHISICAL_DISK = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_DISK
    from . import G_NAME_GROUP_STORAGE_DISK_PHISICAL_DISK


from a.infra.basic.return_codes import ReturnCodes
__pychecker__ = 'maxrefs=20'
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.physical_data_gen
blinky_generated_disk_physical_data=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.physical.physical_data_gen



class PhysicalDisk(object):
    """
    A phisical disk
    """
    def __init__ (self,logicalDiskName,controllerManager,logger):

        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_DISK, G_NAME_GROUP_STORAGE_DISK_PHISICAL_DISK)
        self._logicalDiskName = logicalDiskName
        self._controllerManager = controllerManager

        # configuration
        self._runningPhysicalConfig   = blinky_generated_disk_physical_data.PhysicalData()
        self._candidatePhysicalConfig = blinky_generated_disk_physical_data.PhysicalData()
        self._activePhysicalConfig    = blinky_generated_disk_physical_data.PhysicalData()


    ## Configuration related functions ##
    
    def diskPhysicalTrxStart (self):
        self._log("disk-physical-trx-start").debug3("diskPhysicalTrxStart()  was called for physical disk %s, running --> candidate",self._logicalDiskName)
        self._candidatePhysicalConfig.copyFrom(self._runningPhysicalConfig)
        return ReturnCodes.kOk

    def diskPhysicalValueSet (self,data):
        self._log("disk-physical-value-set").debug3("diskPhysicalValueSet(data=%s)  was called for physical disk %s, data --> candidate",data,self._logicalDiskName)
        self._candidatePhysicalConfig.copyFrom(data)
        return ReturnCodes.kOk

    def diskPhysicalTrxCommit (self):
        self._log("disk-physical-trx-commit").debug3("diskPhysicalTrxCommit()  was called for physical disk %s, candidate --> running",self._logicalDiskName)
        self._runningPhysicalConfig.copyFrom(self._candidatePhysicalConfig)
        return ReturnCodes.kOk

    def diskPhysicalTrxAbort (self):
        self._log("disk-physical-trx-abort").debug3("diskPhysicalTrxAbort()  was called for physical disk %s, None --> candidate",self._logicalDiskName)
        self._candidatePhysicalConfig  = None
        return ReturnCodes.kOk

    ## Periodic-work related functions ##

    def pushRunningToActiveConfig (self):
        self._log("push-running-to-active").debug3("pushRunningToActiveConfig()  was called for physical disk %s, running -- selective --> active",self._logicalDiskName)
        self._activePhysicalConfig.copyFrom(self._runningPhysicalConfig) # TODO: in future should be selective
        return ReturnCodes.kOk

    def getActiveId (self):
        return self._activePhysicalConfig.id

    def getCandidateId (self):
        return self._candidatePhysicalConfig.id

    def getActiveController (self):
        controllerName = self._activePhysicalConfig.controller
        controller = self._controllerManager.getController(controllerName)
        return controller

    def getDetailedStatus (self):
        pass



class DellPhysicalDisk(PhysicalDisk):
    """
    A Dell phisical disk
    """
    def __init__ (self,logicalDiskName,controllerManager,logger):
        PhysicalDisk.__init__(self,logicalDiskName,controllerManager,logger)


    def getDetailedStatus (self):
        """
        Get the full status of this pdisk
        """
        physicalDiskId   = self._activePhysicalConfig.id
        controller = self.getActiveController()
        if (controller == None):
            controllerName = self._activePhysicalConfig.controller
            self._log("get-pdisk-status-failed").error("getDetailedStatus() for pdiskId=%s failed! controller=%s was not found in controller manager",physicalDiskId,controllerName)
            return None,ReturnCodes.kGeneralError

        pdiskStatus,rc = controller.getPdiskStatus(pdiskId=physicalDiskId)

        if (rc == ReturnCodes.kOk):
            self._log("get-pdisk-status-success").debug3("getDetailedStatus() for pdiskId=%s succeded!",physicalDiskId)
        else:
            self._log("get-pdisk-status-failed").error("getDetailedStatus() for pdiskId=%s failed!",physicalDiskId)

        return pdiskStatus,rc


class DummyPhysicalDisk(PhysicalDisk):
    """
    A dummy physical disk
    """
    pass
