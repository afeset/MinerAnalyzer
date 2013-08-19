#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: Effiz
# 

G_NAME_MODULE_BLINKY_STORAGE_ADAPTOR = "blinky-storage-adaptor"
G_NAME_GROUP_BLINKY_STORAGE_GENERAL = "blinky-storage-general"
G_NAME_GROUP_BLINKY_DISK_MANAGER_ADAPTOR = "blinky-disk-manager-adaptor"
G_NAME_GROUP_BLINKY_STORAGE_MODULE_ADAPTOR = "blinky-storage-module-adaptor"

from a.infra.basic.return_codes import ReturnCodes
from a.storage.disk.tech_storage.tech.storage.disk.blinky_disk_list_gen import BlinkyDiskList
from a.storage.disk.tech_storage.tech.storage.disk.status.blinky_status_oper_gen import BlinkyOperStatus as DiskBlinkyOperStatus
from a.storage.disk.tech_storage.tech.storage.disk.alarms.blinky_alarms_oper_gen import BlinkyOperAlarms as DiskBlinkyOperAlarms
from a.storage.disk.tech_storage.tech.storage.disk.physical.status.blinky_status_oper_gen import BlinkyOperStatus as DiskPhysicalBlinkyOperStatus
from a.storage.disk.tech_storage.tech.storage.disk.raid_array.status.blinky_status_oper_gen import BlinkyOperStatus as DiskRaidArrayBlinkyOperStatus
from a.storage.disk.tech_storage.tech.storage.disk.file_system.status.blinky_status_oper_gen import BlinkyOperStatus as DiskFileSystemBlinkyOperStatus
from a.storage.disk.tech_storage.tech.storage.module.blinky_module_list_gen import BlinkyModuleList
from a.storage.disk.tech_storage.tech.storage.module.status.blinky_status_oper_gen import BlinkyOperStatus as ModuleBlinkyOperStatus
from a.storage.disk.tech_storage.tech.storage.module.actual.blinky_actual_oper_gen import BlinkyOperActual as ModuleBlinkyOperActual

import a.sys.blinky.domain_priority

#############################################################################################################################
#----------- Blinky Storage Adaptor class ----------------------------------------------------------------------------------#
#############################################################################################################################


class StorageBlinkyAdaptor(object):

#----------- Blinky initialization -----------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------#
    def __init__ (self, logger):

        self._log = logger.createLogger(G_NAME_MODULE_BLINKY_STORAGE_ADAPTOR, G_NAME_GROUP_BLINKY_STORAGE_GENERAL)

        # Blinky domain
        self._domain = None

        # DiskManagerAdaptor for attaching a new disk
        self._diskManagerBlinkyAdaptor = DiskManagerBlinkyAdaptor(self._log)

        # StorageModuleManagerAdaptor for attaching a new module
        self._storageModuleBlinkyAdaptor = StorageModuleAdapter(self._log)



    def initBlinky (self, domain, diskMapper, storageModuleManager):

        self._log("init-blinky").debug1("called.")

        # Create domain
        self._domain = domain

        # Create a blinky list objects
        blinkyDiskList = BlinkyDiskList.s_create(self._log,domain=self._domain)
        blinkyModuleList = BlinkyModuleList.s_create(self._log,domain=self._domain)

        # Attach to blinky
        rc = self._diskManagerBlinkyAdaptor.attachDiskListToBlinky(blinkyDiskList,diskMapper)
        if rc != ReturnCodes.kOk:
            self._log("attach-disk-list-to-blinky-failed").error("diskMapper failed to attach to blinky object")
            return ReturnCodes.kGeneralError

        rc = self._storageModuleBlinkyAdaptor.attachModuleListToBlinky(blinkyModuleList,storageModuleManager)
        if rc != ReturnCodes.kOk:
            self._log("attach-module-list-to-blinky-failed").error("storageModuleManager failed to attach to blinky object")
            return ReturnCodes.kGeneralError
      
        # Register this node
        self._domain.registerNode(blinkyDiskList)
        self._domain.registerNode(blinkyModuleList)

        return ReturnCodes.kOk


    def triggerBlinky (self):
        self._log("trigger-blinky").debug1("called.")
        self._domain.triggerSubscriptions()


class DiskManagerBlinkyAdaptor(object):

    def __init__ (self, logger):

        self._log = logger.createLogger(G_NAME_MODULE_BLINKY_STORAGE_ADAPTOR, G_NAME_GROUP_BLINKY_DISK_MANAGER_ADAPTOR)
        self._blinkyDiskList = None
        self._diskMapper = None


    def attachDiskListToBlinky (self,blinkyDiskList, diskMapper):

        self._log("attach-to-blinky-disk-list").debug1("called. blinkyDiskList=%s", blinkyDiskList)

        self._blinkyDiskList = blinkyDiskList
        self._diskMapper = diskMapper

        blinkyDiskList.setCreateFunctor(self.createDiskFunctor)
        blinkyDiskList.setDeleteFunctor(self.deleteDiskFunctor)
        blinkyDiskList.setDestroySelfFunctor(self.diskListDestroySelfFunctor)
        blinkyDiskList.setNotifyTrxProgressFunctor(self.diskListTrxProgressFunctor, True)

        rc = blinkyDiskList.activate()
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk
        

    def createDiskFunctor (self, phase, key, blinkyDisk):
        self._log("create-disk").debug1("called. phase=%s, key=%s", phase, key)

        if (phase.isPreparePrivate()):
            if not self._blinkyDiskList.isInTrigger():
                self._blinkyDiskList.setConfigErrorStr("Internal error: add disk '%s' is not allowed"%key)
                self._log("add-disk-not-allowed").error("add disk '%s' is not allowed",key)
                return ReturnCodes.kGeneralError
        
            rc = self._diskMapper.preCreateDisk(key)
            if rc != ReturnCodes.kOk:
                self._log("pre-create-disk-failed").error("add disk '%s' failed in preCreate phase of disk mapper",key)
                return ReturnCodes.kGeneralError
    
            rc = self.attachDiskToBlinky(blinkyDisk, key)
            if rc != ReturnCodes.kOk:
                self._log("attach-disk-failed").error("add disk '%s' failed attaching to blinky",key)
                return ReturnCodes.kGeneralError

        if (phase.isCommitPublic()):
            rc = self.attachDiskToBlinkyOper(blinkyDisk,key)
            if rc != ReturnCodes.kOk:
                self._log("attach-disk-oper-failed").error("add disk '%s' failed attaching to blinky oper",key)
                # TODO: should I fail transaction in commit phase?
                return ReturnCodes.kOk
    
        return ReturnCodes.kOk


    def deleteDiskFunctor (self, phase, key):
        self._log("remove-disk").debug1("called. phase=%s, key=%s", phase, key)

        if (phase.isPreparePrivate()):
            self._blinkyDiskList.setConfigErrorStr("removal of disks (key = %s) is not allowed")
            return ReturnCodes.kGeneralError

        # this return also covers phases that we don't need to support
        return ReturnCodes.kOk


    def diskListDestroySelfFunctor (self, phase):
        self._log("disk-list-destroy-self").debug1("called.  phase=%s", phase)

        if (phase.isCommitPrivate()):
            self._blinkyDiskList.deactivate()

        return ReturnCodes.kOk


    def diskListTrxProgressFunctor (self, progress):
        self._log("disk-list-trx-progress").debug1("called.  progress=%s", progress)

        if progress.isPreparePrivateBefore():
            rc = self._diskMapper.managerTrxStart()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if progress.isPreparePublicBefore():
            rc = self._diskMapper.managerTrxVerifyPublicConfig()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if progress.isCommitPublicAfter():
            rc = self._diskMapper.managerTrxCommit()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if progress.isAbortPrivateAfter():
            rc = self._diskMapper.managerTrxAbort()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def attachDiskToBlinky (self,blinkyDisk,key):
        self._log("attach-disk-to-blinky").debug1("called. key=%s", key)

        blinkyDisk.setValueSetFunctor(self._createDiskValueSetFunctor(key))
        blinkyDisk.setCreatePhysicalFunctor(self._createCreateDiskPhysicalFunctor(blinkyDisk,key))
        blinkyDisk.setCreateRaidArrayFunctor(self._createCreateDiskRaidArrayFunctor(blinkyDisk,key))
        blinkyDisk.setCreateFileSystemFunctor(self._createCreateDiskFileSystemFunctor(blinkyDisk,key))
        blinkyDisk.setDestroySelfFunctor(self._createDiskDestroySelfFunctor(blinkyDisk,key))
        blinkyDisk.setNotifyTrxProgressFunctor(self._createDiskTrxProgressFunctor(key),True)

        rc = blinkyDisk.activate()
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def attachDiskToBlinkyOper (self,blinkyDisk,key):
        self._log("attach-disk-to-blinky-oper").debug1("called. key=%s", key)

        # status oper
        blinkyStatuaOperObj = DiskBlinkyOperStatus(self._log)
        blinkyStatuaOperObj.setConfigObj(blinkyDisk)
        blinkyStatuaOperObj.setDomain(blinkyDisk.getDomain())
        blinkyStatuaOperObj.setBasicFunctors(self.createGetDiskStatusFunctor(key))
        rc = blinkyStatuaOperObj.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-status-oper-activate-failed").error("blinkyStatuaOperObj.activate() failed. blinkyStatuaOperObj=%s", blinkyStatuaOperObj)
            return ReturnCodes.kGeneralError

        # alarm oper
        blinkyAlarmsOperObj = DiskBlinkyOperAlarms(self._log)
        blinkyAlarmsOperObj.setConfigObj(blinkyDisk)
        blinkyAlarmsOperObj.setDomain(blinkyDisk.getDomain())
        blinkyAlarmsOperObj.setBasicFunctors(self.createGetDiskAlarmsFunctor(key))
        rc = blinkyAlarmsOperObj.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-alarms-oper-activate-failed").error("blinkyAlarmsOperObj.activate() failed. blinkyAlarmsOperObj=%s", blinkyAlarmsOperObj)
            return ReturnCodes.kGeneralError

    
        return ReturnCodes.kOk


    def createGetDiskStatusFunctor (self, key):

        def getDiskStatus (tctx, operData):
            __pychecker__ = 'unusednames=tctx'
            rc = self._diskMapper.getDiskStatus(key,tctx,operData)
            if (rc != ReturnCodes.kOk):
                pass # TODO: effiz, how should I handle this?
            
            return ReturnCodes.kOk

        return getDiskStatus


    def createGetDiskAlarmsFunctor (self, key):
        
        def getDiskAlarm (tctx, operData):
            __pychecker__ = 'unusednames=tctx'
            rc = self._diskMapper.getDiskAlarm(key,tctx,operData)
            if (rc != ReturnCodes.kOk):
                pass # TODO: effiz, how should I handle this?
            
            return ReturnCodes.kOk

        return getDiskAlarm


    def attachDiskPhysicalToBlinky (self,blinkyDiskPhysical,key):
        self._log("attach-disk-physical-to-blinky").debug1("called. key=%s", key)

        blinkyDiskPhysical.setValueSetFunctor(self._createDiskPhysicalValueSetFunctor(key))
        blinkyDiskPhysical.setDestroySelfFunctor(self._createDiskPhysicalDestroySelfFunctor(blinkyDiskPhysical,key))

        rc = blinkyDiskPhysical.activate()
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def attachDiskPhysicalToBlinkyOper (self,blinkyDiskPhysical,key):
        self._log("attach-disk-physical-to-blinky-oper").debug1("called. key=%s", key)
        blinkyOperObj = DiskPhysicalBlinkyOperStatus(self._log)
        blinkyOperObj.setConfigObj(blinkyDiskPhysical)
        blinkyOperObj.setDomain(blinkyDiskPhysical.getDomain())
        blinkyOperObj.setBasicFunctors(self.createGetDiskPhysicalStatusFunctor(key))
        rc = blinkyOperObj.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-oper-activate-failed").error("blinkyOperObj.activate() failed. blinkyOperObj=%s", blinkyOperObj)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk


    def createGetDiskPhysicalStatusFunctor (self,key):

        def getDiskPhysicalStatus (tctx, operData):

            rc = self._diskMapper.getDiskPhysicalStatus(key,tctx,operData)
            if (rc != ReturnCodes.kOk):
                pass # TODO: effiz, how should I handle this?
            
            return ReturnCodes.kOk

        return getDiskPhysicalStatus


    def attachDiskRaidArrayToBlinky (self,blinkyDiskRaidArray,key):
        self._log("attach-disk-raid-array-to-blinky").debug1("called. key=%s", key)

        blinkyDiskRaidArray.setValueSetFunctor(self._createDiskRaidArrayValueSetFunctor(key)) 
        blinkyDiskRaidArray.setDestroySelfFunctor(self._createDiskRaidArrayDestroySelfFunctor(blinkyDiskRaidArray,key))

        rc = blinkyDiskRaidArray.activate()
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def attachDiskRaidArrayToBlinkyOper (self,blinkyDiskRaidArray,key):
        self._log("attach-disk-raid-array-to-blinky-oper").debug1("called. key=%s", key)
        blinkyOperObj = DiskRaidArrayBlinkyOperStatus(self._log)
        blinkyOperObj.setConfigObj(blinkyDiskRaidArray)
        blinkyOperObj.setDomain(blinkyDiskRaidArray.getDomain())
        blinkyOperObj.setBasicFunctors(self.createGetDiskRaidArrayStatusFunctor(key))
        rc = blinkyOperObj.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-oper-activate-failed").error("blinkyOperObj.activate() failed. blinkyOperObj=%s", blinkyOperObj)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def createGetDiskRaidArrayStatusFunctor (self,key):

        def getDiskRaidArrayStatus (tctx, operData):

            rc = self._diskMapper.getDiskRaidArrayStatus(key,tctx,operData)####
            if (rc != ReturnCodes.kOk):
                pass # TODO: effiz, how should I handle this?

            return ReturnCodes.kOk

        return getDiskRaidArrayStatus


    def attachDiskFileSystemToBlinky (self,blinkyDiskFileSystem,key):
        self._log("attach-disk-file-system-to-blinky").debug1("called. key=%s", key)

        blinkyDiskFileSystem.setValueSetFunctor(self._createDiskFileSystemValueSetFunctor(key))
        blinkyDiskFileSystem.setCreateCommandsFunctor(self._createCreateDiskFileSystemCommandsFunctor(key,blinkyDiskFileSystem))
        blinkyDiskFileSystem.setCreateTimeoutsFunctor(self._createCreateDiskFileSystemTimeoutsFunctor(key,blinkyDiskFileSystem))
        blinkyDiskFileSystem.setDestroySelfFunctor(self._createDiskFileSystemDestroySelfFunctor(blinkyDiskFileSystem,key))

        rc = blinkyDiskFileSystem.activate()
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def attachDiskFileSystemToBlinkyOper (self,blinkyDiskFileSystem,key):
        self._log("attach-disk-file-system-to-blinky-oper").debug1("called. key=%s", key)
        blinkyOperObj = DiskFileSystemBlinkyOperStatus(self._log)
        blinkyOperObj.setConfigObj(blinkyDiskFileSystem)
        blinkyOperObj.setDomain(blinkyDiskFileSystem.getDomain())
        blinkyOperObj.setBasicFunctors(self.createGetDiskFileSystemStatusFunctor(key))
        rc = blinkyOperObj.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-oper-activate-failed").error("blinkyOperObj.activate() failed. blinkyOperObj=%s", blinkyOperObj)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk


    def createGetDiskFileSystemStatusFunctor (self,key):

        def getDiskFileSystemStatus (tctx, operData):

            rc = self._diskMapper.getDiskFileSystemStatus(key,tctx,operData) #####
            if (rc != ReturnCodes.kOk):
                pass # TODO: effiz, how should I handle this?
            
            return ReturnCodes.kOk

        return getDiskFileSystemStatus


    def attachDiskFileSystemCommandsToBlinky (self,blinkyDiskFileSystemCommands,key):
        self._log("attach-disk-file-system-commands-to-blinky").debug1("called. key=%s", key)

        blinkyDiskFileSystemCommands.setValueSetFunctor(self._createDiskFileSystemCommandsValueSetFunctor(key))
        blinkyDiskFileSystemCommands.setDestroySelfFunctor(self._createDiskFileSystemCommandsDestroySelfFunctor(blinkyDiskFileSystemCommands,key))

        rc = blinkyDiskFileSystemCommands.activate()
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def attachDiskFileSystemTimeoutsToBlinky (self,blinkyDiskFileSystemTimeouts,key):
        self._log("attach-disk-file-system-timeouts-to-blinky").debug1("called. key=%s", key)

        blinkyDiskFileSystemTimeouts.setValueSetFunctor(self._createDiskFileSystemTimeoutsValueSetFunctor(key))
        blinkyDiskFileSystemTimeouts.setDestroySelfFunctor(self._createDiskFileSystemTimeoutsDestroySelfFunctor(blinkyDiskFileSystemTimeouts,key))

        rc = blinkyDiskFileSystemTimeouts.activate()
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#----------- Private helpers ------------------------------------------------------------------------------------------------#


    def _createDiskValueSetFunctor(self, key):

        def diskValueSetFunctor(phase, data):

            self._log("disk-value-set").debug1("called. key=%s, phase=%s, data=%s", key, phase, data)

            if (phase.isPreparePrivate()):
                rc = self._diskMapper.diskValueSet(key,data)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskValueSetFunctor


    def _createCreateDiskPhysicalFunctor(self, blinkyDisk, key):

        def createDiskPhysicalFunctor(phase, blinkyDiskPhysical):

            self._log("create-disk-physical").debug1("called. key=%s, phase=%s", key, phase)

            if (phase.isPreparePrivate()):
                if not blinkyDisk.isInTrigger():
                    blinkyDisk.setConfigErrorStr("Internal error: creating disk '%s' physical is not allowed"%key)
                    self._log("create-physical-not-allowed").error("creating disk '%s' physical is not allowed",key)
                    return ReturnCodes.kGeneralError

                if not self._diskMapper.isDiskInMap(key):
                    self._log("create-disk-physical-failed").error("creating disk physical failed, '%s' is not in disk mapper's map",key)
                    return ReturnCodes.kGeneralError

                if (self._diskMapper.preCreatePhysicalDisk(key) != ReturnCodes.kOk):
                    self._log("precreate-physical-disk-failed").error("creating disk physical failed, diskMapper.preCreatePhysicalDisk('%s') failed",key)
                    return ReturnCodes.kGeneralError

                if (self.attachDiskPhysicalToBlinky(blinkyDiskPhysical,key) != ReturnCodes.kOk):
                    self._log("attach-disk-physical-failed").error("add disk '%s' physical failed attaching to blinky",key)
                    return ReturnCodes.kGeneralError

            if (phase.isCommitPublic()):
                rc = self.attachDiskPhysicalToBlinkyOper(blinkyDiskPhysical,key)
                if rc != ReturnCodes.kOk:
                    self._log("attach-disk-physical-oper-failed").error("add disk '%s' physical failed attaching to blinky oper",key)
                    # TODO: should I fail transaction in commit phase?
                    return ReturnCodes.kOk
        
            return ReturnCodes.kOk

        return createDiskPhysicalFunctor


    def _createCreateDiskRaidArrayFunctor(self, blinkyDisk, key):

        def createDiskRaidArrayFunctor(phase, blinkyDiskRaidArray):

            self._log("create-disk-raid-array").debug1("called. key=%s, phase=%s", key, phase)

            if (phase.isPreparePrivate()):
                if not blinkyDisk.isInTrigger():
                    blinkyDisk.setConfigErrorStr("Internal error: creating disk '%s' raid-array is not allowed"%key)
                    self._log("create-raid-array-not-allowed").error("creating disk '%s' raid-array is not allowed",key)
                    return ReturnCodes.kGeneralError

                if not self._diskMapper.isDiskInMap(key):
                    self._log("create-disk-raid-array-failed").error("creating disk raid-array failed, '%s' is not in disk mapper's map",key)
                    return ReturnCodes.kGeneralError

                if (self._diskMapper.preCreateLogicalDisk(key) != ReturnCodes.kOk):
                    self._log("precreate-logical-disk-failed").error("creating disk raid array failed, diskMapper.preCreateLogicalDisk('%s') failed",key)
                    return ReturnCodes.kGeneralError

                if (self.attachDiskRaidArrayToBlinky(blinkyDiskRaidArray,key) != ReturnCodes.kOk):
                    self._log("attach-disk-raid-array-failed").error("add disk '%s' raid-array failed attaching to blinky",key)
                    return ReturnCodes.kGeneralError

            if (phase.isCommitPublic()):
                rc = self.attachDiskRaidArrayToBlinkyOper(blinkyDiskRaidArray,key)
                if rc != ReturnCodes.kOk:
                    self._log("attach-disk-raid-array-oper-failed").error("add disk '%s' raid-array failed attaching to blinky oper",key)
                    # TODO: should I fail transaction in commit phase?
                    return ReturnCodes.kOk
        
            return ReturnCodes.kOk

        return createDiskRaidArrayFunctor


    def _createCreateDiskFileSystemFunctor(self, blinkyDisk, key):
        
        def createDiskFileSystemFunctor(phase, blinkyDiskFileSystem):

            self._log("create-disk-file-system").debug1("called. key=%s, phase=%s", key, phase)

            if (phase.isPreparePrivate()):
                if not blinkyDisk.isInTrigger():
                    blinkyDisk.setConfigErrorStr("Internal error: creating disk '%s' file-system is not allowed"%key)
                    self._log("create-file-system-not-allowed").error("creating disk '%s' file-system is not allowed",key)
                    return ReturnCodes.kGeneralError

                if not self._diskMapper.isDiskInMap(key):
                    self._log("create-disk-file-system-failed").error("creating disk file-system failed, '%s' is not in disk mapper's map",key)
                    return ReturnCodes.kGeneralError

                if (self._diskMapper.preCreateFileSystem(key) != ReturnCodes.kOk):
                    self._log("precreate-file-system-failed").error("creating disk raid array failed, diskMapper.preCreateFileSystem('%s') failed",key)
                    return ReturnCodes.kGeneralError

                if (self.attachDiskFileSystemToBlinky(blinkyDiskFileSystem,key) != ReturnCodes.kOk):
                    self._log("attach-disk-file-system-failed").error("add disk '%s' file-system failed attaching to blinky",key)
                    return ReturnCodes.kGeneralError

            if (phase.isCommitPublic()):
                rc = self.attachDiskFileSystemToBlinkyOper(blinkyDiskFileSystem,key)
                if rc != ReturnCodes.kOk:
                    self._log("attach-disk-file-system-oper-failed").error("add disk '%s' file-system failed attaching to blinky oper",key)
                    # TODO: should I fail transaction in commit phase?
                    return ReturnCodes.kOk
        
            return ReturnCodes.kOk

        return createDiskFileSystemFunctor


    def _createDiskDestroySelfFunctor(self, blinkyDisk, key):

        def diskDestroySelfFunctor(phase):

            self._log("disk-destroy-self").debug1("called. key=%s, phase=%s", key, phase)
            
            # Since all lists are static in nature, this functor should not be called, at all!
            if (phase.isPreparePrivate()):
                blinkyDisk.setConfigErrorStr("removal of disks (key = %s) is not allowed"%key)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskDestroySelfFunctor


    def _createDiskTrxProgressFunctor (self, key):

        def diskTrxProgressFunctor (progress):
            self._log("disk-trx-progress").debug1("called. key=%s, progress=%s", key, progress)
    
            if progress.isPreparePrivateBefore():
                rc = self._diskMapper.diskTrxStart(key)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isCommitPublicBefore():
                rc = self._diskMapper.diskTrxCommit(key)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isAbortPublicBefore():
                rc = self._diskMapper.diskTrxAbort(key)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            return ReturnCodes.kOk

        return diskTrxProgressFunctor


    def _createDiskPhysicalValueSetFunctor(self, key):

        def diskPhysicalValueSetFunctor(phase, data):

            self._log("disk-physical-value-set").debug1("called. key=%s, phase=%s, data=%s", key, phase, data)

            if (phase.isPreparePrivate()):
                rc = self._diskMapper.diskPhysicalValueSet(key,data)
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskPhysicalValueSetFunctor


    def _createDiskPhysicalDestroySelfFunctor(self, blinkyDiskPhysical, key):

        def diskPhysicalDestroySelfFunctor(phase):

            self._log("disk-physical-destroy-self").debug1("called. key=%s, phase=%s", key, phase)
            
            # Since all lists are static in nature, this functor should not be called, at all!
            if (phase.isPreparePrivate()):
                blinkyDiskPhysical.setConfigErrorStr("removal of disk physical (key = %s) is not allowed"%key)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskPhysicalDestroySelfFunctor


    def _createDiskRaidArrayValueSetFunctor(self, key):

        def diskRaidArrayValueSetFunctor(phase, data):

            self._log("disk-raid-array-value-set").debug1("called. key=%s, phase=%s, data=%s", key, phase, data)

            if (phase.isPreparePrivate()):
                rc = self._diskMapper.diskRaidArrayValueSet(key,data)####
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskRaidArrayValueSetFunctor


    def _createDiskRaidArrayDestroySelfFunctor(self, blinkyDiskRaidArray, key):

        def diskRaidArrayDestroySelfFunctor(phase):

            self._log("disk-raid-array-destroy-self").debug1("called. key=%s, phase=%s", key, phase)
            
            # Since all lists are static in nature, this functor should not be called, at all!
            if (phase.isPreparePrivate()):
                blinkyDiskRaidArray.setConfigErrorStr("removal of disk raid-array (key = %s) is not allowed"%key)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskRaidArrayDestroySelfFunctor


    def _createDiskFileSystemValueSetFunctor(self, key):

        def diskFileSystemValueSetFunctor(phase, data):

            self._log("disk-file-system-value-set").debug1("called. key=%s, phase=%s, data=%s", key, phase, data)

            if (phase.isPreparePrivate()):
                rc = self._diskMapper.diskFileSystemValueSet(key,data)####
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskFileSystemValueSetFunctor


    def _createCreateDiskFileSystemCommandsFunctor(self, key, blinkyDiskFileSystem):

        def createDiskFileSystemCommandsFunctor(phase, blinkyDiskFileSystemCommands):
        
            self._log("create-disk-file-system-commands").debug2("called. key=%s, phase=%s", key, phase)
        
            if (phase.isPreparePrivate()):
                if not blinkyDiskFileSystem.isInTrigger():
                    blinkyDiskFileSystem.setConfigErrorStr("Internal error: creating disk '%s' file-system-commands is not allowed"%key)
                    self._log("create-file-system-commands-not-allowed").error("creating disk '%s' file-system-commands is not allowed",key)
                    return ReturnCodes.kGeneralError
        
                if not self._diskMapper.isDiskInMap(key):
                    self._log("create-disk-file-system-commands-failed").error("creating disk file-system-commands failed, '%s' is not in disk mapper's map",key)
                    return ReturnCodes.kGeneralError
        
                if (self.attachDiskFileSystemCommandsToBlinky(blinkyDiskFileSystemCommands,key) != ReturnCodes.kOk):
                    self._log("attach-disk-file-system-commands-failed").error("add disk '%s' file-system-commands failed attaching to blinky",key)
                    return ReturnCodes.kGeneralError
        
            return ReturnCodes.kOk
        
        return createDiskFileSystemCommandsFunctor


    def _createCreateDiskFileSystemTimeoutsFunctor(self, key, blinkyDiskFileSystem):

        def createDiskFileSystemTimeoutsFunctor(phase, blinkyDiskFileSystemTimeouts):
        
            self._log("create-disk-file-system-timeouts").debug2("called. key=%s, phase=%s", key, phase)
        
            if (phase.isPreparePrivate()):
                if not blinkyDiskFileSystem.isInTrigger():
                    blinkyDiskFileSystem.setConfigErrorStr("Internal error: creating disk '%s' file-system-timeouts is not allowed"%key)
                    self._log("create-file-system-timeouts-not-allowed").error("creating disk '%s' file-system-timeouts is not allowed",key)
                    return ReturnCodes.kGeneralError
        
                if not self._diskMapper.isDiskInMap(key):
                    self._log("create-disk-file-system-timeouts-failed").error("creating disk file-system-timeouts failed, '%s' is not in disk mapper's map",key)
                    return ReturnCodes.kGeneralError
        
                if (self.attachDiskFileSystemTimeoutsToBlinky(blinkyDiskFileSystemTimeouts,key) != ReturnCodes.kOk):
                    self._log("attach-disk-file-system-timeouts-failed").error("add disk '%s' file-system-timeouts failed attaching to blinky",key)
                    return ReturnCodes.kGeneralError
        
            return ReturnCodes.kOk
        
        return createDiskFileSystemTimeoutsFunctor


    def _createDiskFileSystemDestroySelfFunctor(self, blinkyDiskFileSystem, key):

        def diskFileSystemDestroySelfFunctor(phase):

            self._log("disk-file-system-destroy-self").debug1("called. key=%s, phase=%s", key, phase)

            # Since all lists are static in nature, this functor should not be called, at all!
            if (phase.isPreparePrivate()):
                blinkyDiskFileSystem.setConfigErrorStr("removal of disk file-system (key = %s) is not allowed"%key)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskFileSystemDestroySelfFunctor


    def _createDiskFileSystemCommandsValueSetFunctor(self, key) :

        def diskFileSystemCommandsValueSetFunctor(phase, data):

            self._log("disk-file-system-commands-value-set").debug1("called. key=%s, phase=%s, data=%s", key, phase, data)

            if (phase.isPreparePrivate()):
                rc = self._diskMapper.diskFileSystemCommandsValueSet(key,data)####
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskFileSystemCommandsValueSetFunctor


    def _createDiskFileSystemCommandsDestroySelfFunctor (self,key,blinkyDiskFileSystemCommands):

        def diskFileSystemCommandsDestroySelfFunctor(phase):

            self._log("disk-file-system-commands-destroy-self").debug1("called. key=%s, phase=%s", key, phase)

            # Since all lists are static in nature, this functor should not be called, at all!
            if (phase.isPreparePrivate()):
                blinkyDiskFileSystemCommands.setConfigErrorStr("removal of disk file-system-commands (key = %s) is not allowed"%key)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskFileSystemCommandsDestroySelfFunctor


    def _createDiskFileSystemTimeoutsValueSetFunctor(self, key) :

        def diskFileSystemTimeoutsValueSetFunctor(phase, data):

            self._log("disk-file-system-timeouts-value-set").debug1("called. key=%s, phase=%s, data=%s", key, phase, data)

            if (phase.isPreparePrivate()):
                rc = self._diskMapper.diskFileSystemTimeoutsValueSet(key,data)####
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskFileSystemTimeoutsValueSetFunctor


    def _createDiskFileSystemTimeoutsDestroySelfFunctor (self,key,blinkyDiskFileSystemTimeouts):

        def diskFileSystemTimeoutsDestroySelfFunctor(phase):

            self._log("disk-file-system-timeouts-destroy-self").debug1("called. key=%s, phase=%s", key, phase)

            # Since all lists are static in nature, this functor should not be called, at all!
            if (phase.isPreparePrivate()):
                blinkyDiskFileSystemTimeouts.setConfigErrorStr("removal of disk file-system-timeouts (key = %s) is not allowed"%key)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return diskFileSystemTimeoutsDestroySelfFunctor


class StorageModuleAdapter(object):

    def __init__ (self, logger):

        self._log = logger.createLogger(G_NAME_MODULE_BLINKY_STORAGE_ADAPTOR, G_NAME_GROUP_BLINKY_STORAGE_MODULE_ADAPTOR)
        self._blinkyModuleList = None
        self._storageModuleManager = None


    def attachModuleListToBlinky (self,blinkyModuleList, storageModuleManager):

        self._log("attach-to-blinky-module-list").debug1("called. blinkyModuleList=%s", blinkyModuleList)

        self._blinkyModuleList = blinkyModuleList
        self._storageModuleManager = storageModuleManager

        blinkyModuleList.setCreateFunctor(self.createModuleFunctor)
        blinkyModuleList.setDeleteFunctor(self.deleteModuleFunctor)
        blinkyModuleList.setDestroySelfFunctor(self.moduleListDestroySelfFunctor)
        blinkyModuleList.setNotifyTrxProgressFunctor(self.moduleListTrxProgressFunctor, True)

        rc = blinkyModuleList.activate()
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def createModuleFunctor (self, phase, key, blinkyModule):
        self._log("create-module").debug1("called. phase=%s, key=%s", phase, key)

        if (phase.isPreparePrivate()):
            if not self._blinkyModuleList.isInTrigger():
                self._blinkyModuleList.setConfigErrorStr("Internal error: add module '%s' is not allowed"%key)
                self._log("add-module-not-allowed").error("add module '%s' is not allowed",key)
                return ReturnCodes.kGeneralError

            module = self._storageModuleManager.createModule(key)
            if module == None:
                self._log("create-module-failed").error("add module '%s' failed!",key)
                return ReturnCodes.kGeneralError

            rc = self.attachModuleToBlinky(blinkyModule, module ,key)
            if rc != ReturnCodes.kOk:
                self._log("attach-module-failed").error("add module '%s' failed attaching to blinky",key)
                return ReturnCodes.kGeneralError

        if (phase.isCommitPublic()):
            module = self._storageModuleManager.getCandidateStorageModule(key)
            if module == None:
                self._log("create-module-failed").error("get module '%s' failed!",key)
                return ReturnCodes.kGeneralError

            rc = self.attachModuleToBlinkyOper(blinkyModule,module ,key)
            if rc != ReturnCodes.kOk:
                self._log("attach-module-oper-failed").error("add module '%s' failed attaching to blinky oper",key)
                # TODO: should I fail transaction in commit phase?
                return ReturnCodes.kOk

        return ReturnCodes.kOk


    def deleteModuleFunctor (self, phase, key):
        self._log("remove-module").debug1("called. phase=%s, key=%s", phase, key)

        if (phase.isPreparePrivate()):
            self._blinkyModuleList.setConfigErrorStr("removal of modules (key = %s) is not allowed")
            return ReturnCodes.kGeneralError

        # this return also covers phases that we don't need to support
        return ReturnCodes.kOk


    def moduleListDestroySelfFunctor (self, phase):
        self._log("module-list-destroy-self").debug1("called.  phase=%s", phase)

        if (phase.isCommitPrivate()):
            self._blinkyModuleList.deactivate()

        return ReturnCodes.kOk


    def moduleListTrxProgressFunctor (self, progress):
        self._log("module-list-trx-progress").debug1("called.  progress=%s", progress)

        if progress.isPreparePrivateBefore():
            rc = self._storageModuleManager.managerTrxStart()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if progress.isPreparePublicBefore():
            rc = self._storageModuleManager.managerTrxVerifyPublicConfig()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if progress.isCommitPublicAfter():
            rc = self._storageModuleManager.managerTrxCommit()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if progress.isAbortPrivateAfter():
            rc = self._storageModuleManager.managerTrxAbort()
            if rc!=ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk


    def attachModuleToBlinky(self, blinkyModule, module, key):
        self._log("attach-module-to-blinky").debug1("called. key=%s", key)

        blinkyModule.setValueSetFunctor(self._createModuleValueSetFunctor(blinkyModule,module,key))
        blinkyModule.setDestroySelfFunctor(self._createModuleDestroySelfFunctor(blinkyModule,key))
        blinkyModule.setNotifyTrxProgressFunctor(self._createModuleTrxProgressFunctor(module,key),True)#TODO

        rc = blinkyModule.activate()
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def attachModuleToBlinkyOper (self,blinkyModule,module,key):
        self._log("attach-module-to-blinky-oper").debug1("called. key=%s", key)
  
        # status oper
        blinkyStatuaOperObj = ModuleBlinkyOperStatus(self._log)
        blinkyStatuaOperObj.setConfigObj(blinkyModule)
        blinkyStatuaOperObj.setDomain(blinkyModule.getDomain())
        blinkyStatuaOperObj.setBasicFunctors(self.createGetModuleStatusFunctor(module))
        rc = blinkyStatuaOperObj.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-status-oper-activate-failed").error("blinkyStatuaOperObj.activate() failed. blinkyStatuaOperObj=%s", blinkyStatuaOperObj)
            return ReturnCodes.kGeneralError
  
  #      # alarm oper
  #      blinkyAlarmsOperObj = DiskBlinkyOperAlarms(self._log)
  #      blinkyAlarmsOperObj.setConfigObj(blinkyDisk)
  #      blinkyAlarmsOperObj.setDomain(blinkyDisk.getDomain())
  #      blinkyAlarmsOperObj.setBasicFunctors(self.createGetDiskAlarmsFunctor(key))
  #      rc = blinkyAlarmsOperObj.activate()
  #      if rc != ReturnCodes.kOk:
  #          self._log("attach-to-blinky-alarms-oper-activate-failed").error("blinkyAlarmsOperObj.activate() failed. blinkyAlarmsOperObj=%s", blinkyAlarmsOperObj)
  #          return ReturnCodes.kGeneralError
  #          
        # actual oper
        blinkyActualOperObj = ModuleBlinkyOperActual(self._log)
        blinkyActualOperObj.setConfigObj(blinkyModule)
        blinkyActualOperObj.setDomain(blinkyModule.getDomain())
        blinkyActualOperObj.setBasicFunctors(self.createGetModuleActualFunctor(module))
        rc = blinkyActualOperObj.activate()
        if rc != ReturnCodes.kOk:
            self._log("attach-to-blinky-status-oper-activate-failed").error("blinkyActualOperObj.activate() failed. blinkyActualOperObj=%s", blinkyActualOperObj)
            return ReturnCodes.kGeneralError
  
  
        return ReturnCodes.kOk
  

    def createGetModuleStatusFunctor (self, module):
        
        def getModuleStatus (tctx, operData):
            __pychecker__ = 'unusednames=tctx'
            rc = module.getModuleStatus(tctx,operData)
            if (rc != ReturnCodes.kOk):
                pass # TODO: effiz, how should I handle this?
  
            return ReturnCodes.kOk
  
        return getModuleStatus

  
    def createGetModuleActualFunctor (self, module):
  
        def getModuleActual (tctx, operData):
            __pychecker__ = 'unusednames=tctx'
            rc = module.getActualConfig(tctx,operData)
            if (rc != ReturnCodes.kOk):
                pass # TODO: effiz, how should I handle this?
  
            return ReturnCodes.kOk
  
        return getModuleActual
  
  
  #  def createGetDiskAlarmsFunctor (self, key):
  #
  #      def getDiskAlarm (tctx, operData):
  #          __pychecker__ = 'unusednames=tctx'
  #          rc = self._diskMapper.getDiskAlarm(key,tctx,operData)
  #          if (rc != ReturnCodes.kOk):
  #              pass # TODO: effiz, how should I handle this?
  #
  #          return ReturnCodes.kOk
  #
  #      return getDiskAlarm

    def _createModuleValueSetFunctor (self,blinkyModule,module,key):

        def moduleValueSetFunctor(phase, data):

            self._log("module-value-set").debug1("called. key=%s, phase=%s, data=%s", key, phase, data)

            if (phase.isPreparePrivate()):
                rc,errorString = module.moduleValueSet(data)
                if rc != ReturnCodes.kOk:
                    blinkyModule.setConfigErrorStr("Internal error: %s"%errorString)
                    return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return moduleValueSetFunctor


    def _createModuleDestroySelfFunctor (self,blinkyModule,key):

        def moduleDestroySelfFunctor(phase):

            self._log("module-destroy-self").debug1("called. key=%s, phase=%s", key, phase)
            
            # Since all lists are static in nature, this functor should not be called, at all!
            if (phase.isPreparePrivate()):
                blinkyModule.setConfigErrorStr("removal of modules (key = %s) is not allowed"%key)
                return ReturnCodes.kGeneralError

            return ReturnCodes.kOk

        return moduleDestroySelfFunctor


    def _createModuleTrxProgressFunctor (self,module,key):

        def moduleTrxProgressFunctor (progress):
            self._log("module-trx-progress").debug1("called. key=%s, progress=%s", key, progress)
    
            if progress.isPreparePrivateBefore():
                rc = module.moduleTrxStart()
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isCommitPublicBefore():
                rc = module.moduleTrxCommit()
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError

            if progress.isAbortPublicBefore():
                rc = module.moduleTrxAbort()
                if rc != ReturnCodes.kOk:
                    return ReturnCodes.kGeneralError
    
            return ReturnCodes.kOk

        return moduleTrxProgressFunctor
