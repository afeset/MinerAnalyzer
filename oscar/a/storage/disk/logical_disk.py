# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz

if  __package__ is None:
    G_NAME_MODULE_STORAGE_DISK = "unknown"
    G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_RAID_0 = "unknown"
    G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_ON_BLOCK_DEVICE = "unknown"
    G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_IN_DIRECTORY = "unknown"
    G_NAME_GROUP_STORAGE_DISK_PHISICAL_DISK = "unknown"
else:
    from . import G_NAME_MODULE_STORAGE_DISK
    from . import G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_RAID_0
    from . import G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_ON_BLOCK_DEVICE
    from . import G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_IN_DIRECTORY
    from . import G_NAME_GROUP_STORAGE_DISK_PHISICAL_DISK


from a.infra.basic.return_codes import ReturnCodes
import dell_raid_controller as drc
__pychecker__ = 'maxrefs=20'
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.raid_array_data_gen
blinky_generated_disk_raid_array_data=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.raid_array.raid_array_data_gen
import os



class LogicalDisk(object):
    """
    A base class representing a logical hardware disk
    """
    # detailed status keys
    DETAILED_STATUS_KEY_VDISK = "vdisk"
    DETAILED_STATUS_KEY_PDISK = "pdisk"

    # status keys
    STATUS_KEY_STATUS        = "status"
    STATUS_KEY_STATE         = "state"
    STATUS_KEY_SIZE          = "size"
    STATUS_KEY_SERIAL_NUMBER = "serial-number"

    # status values
    STATE_ACTIVE_STRING = "Active"
    STATE_FAULT_STRING  = "Fault"
    STATE_ABSENT_STRING = "Absent"
    STATUS_UP           = "Up"
    STATUS_DOWN         = "Down"
    NO_DATA             = ""


    def __init__ (self,logicalDiskName,physicalDiskManager,logger,groupName):
        self._log = logger.createLogger(G_NAME_MODULE_STORAGE_DISK, groupName)
        self._logicalDiskName = logicalDiskName
        self._physicalDiskManager = physicalDiskManager

        # configuration
        self._runningRaidArrayConfig   = blinky_generated_disk_raid_array_data.RaidArrayData()
        self._candidateRaidArrayConfig = blinky_generated_disk_raid_array_data.RaidArrayData()
        self._activeRaidArrayConfig    = blinky_generated_disk_raid_array_data.RaidArrayData()


    ## Configuration related functions ##

    def diskRaidArrayTrxStart (self):
        self._log("disk-raid-array-trx-start").debug3("diskRaidArrayTrxStart()  was called for raid-array disk %s, running --> candidate",self._logicalDiskName)
        self._candidateRaidArrayConfig.copyFrom(self._runningRaidArrayConfig)
        return ReturnCodes.kOk

    def diskRaidArrayValueSet (self,data):
        self._log("disk-raid-array-value-set").debug3("diskRaidArrayValueSet(data=%s)  was called for raid-array disk %s, data --> candidate",data,self._logicalDiskName)
        self._candidateRaidArrayConfig.copyFrom(data)
        return ReturnCodes.kOk

    def diskRaidArrayTrxCommit (self):
        self._log("disk-raid-array-trx-commit").debug3("diskRaidArrayTrxCommit()  was called for raid-array disk %s, candidate --> running",self._logicalDiskName)
        self._runningRaidArrayConfig.copyFrom(self._candidateRaidArrayConfig)
        return ReturnCodes.kOk

    def diskRaidArrayTrxAbort (self):
        self._log("disk-raid-array-trx-abort").debug3("diskRaidArrayTrxAbort()  was called for raid-array disk %s, None --> candidate",self._logicalDiskName)
        self._candidateRaidArrayConfig  = None
        return ReturnCodes.kOk

    ## Periodic-work related functions ##

    def pushRunningToActiveConfig (self):
        self._log("push-running-to-active").debug3("pushRunningToActiveConfig()  was called for logical disk %s, running -- selective --> active",self._logicalDiskName)
        self._activeRaidArrayConfig.copyFrom(self._runningRaidArrayConfig) # TODO: in future should be selective
        return ReturnCodes.kOk

    def getActiveRaidArrayName(self):
        return self._activeRaidArrayConfig.name

    def getCandidateRaidArrayName (self):
        return self._candidateRaidArrayConfig.name

    def _getActiveController (self):
        pass


    def activate (self,forceInit):
        """
        Make a LogocalDisk object usable
        """
        pass


    def getDetailedStatus (self):
        """
        Get Detailed status of the object (in unknown format)
        """
        pass


    def getStatus (self):
        """
        Get status of the object (a well formatted dict with the keys of this class)
        """
        pass

    

class DellRaid0Disk(LogicalDisk):
    """
    A Dell raid-0 implementation of LogicalDisk
    """

    def __init__ (self,logicalDiskName,physicalDiskManager,logger):
        LogicalDisk.__init__(self,logicalDiskName,physicalDiskManager,logger,G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_RAID_0)
        

    def _getActiveController (self):
        physicalDisk = self._physicalDiskManager.getRunningPhysicalDisk(self._logicalDiskName)
        if (physicalDisk == None):
            self._log("no-physical-disk").warning("no physical disk found for logical disk '%s'",self._logicalDiskName)
            return None

        controller = physicalDisk.getActiveController()
        if (controller == None):
            self._log("no-controller").warning("no controller found for physical disk '%s'",self._logicalDiskName)
            return None

        return controller


    def activate (self,forceInit):
        """
        Utilze this raid-0 object (=vdisk)
        """

        physicalDisk = self._physicalDiskManager.getRunningPhysicalDisk(self._logicalDiskName)
        if (physicalDisk == None):
            return None,ReturnCodes.kGeneralError
        physicalDiskId = physicalDisk.getActiveId()

        # get configuration params
        vdiskName = self._activeRaidArrayConfig.name
        autoInit = self._activeRaidArrayConfig.autoInit

        # get controller
        controller = self._getActiveController()
        if (controller == None):
            self._log("no-controller-found").error("no controller found for logical disk '%s'",self._logicalDiskName)
            return None,ReturnCodes.kGeneralError

        # activate
        blockDevice,rc = controller.createVdisk(raidLevel=drc.DellRaidController.RAID_LEVEL_0,pdiskIdsList=[physicalDiskId],vdiskName=vdiskName,autoInit=autoInit,forceInit=forceInit)

        if ((rc == ReturnCodes.kOk) or (rc == ReturnCodes.kAlreadyExists)):
            self._log("activate-success").debug2("activate(forceinit=%s) for logicalDisk '%s' succeded!",forceInit,self._logicalDiskName)
        else:
            self._log("activate-failed").error("activate(forceinit=%s) for logicalDisk '%s' failed!",forceInit,self._logicalDiskName)

        return blockDevice,rc


    def getDetailedStatus (self):
        """
        Get the full status of this raid-0 object (=vdisk)
        """
        
        vdiskName = self._activeRaidArrayConfig.name
        controller = self._getActiveController()
        physicalDisk = self._physicalDiskManager.getRunningPhysicalDisk(self._logicalDiskName)

        if ((controller == None) or (physicalDisk == None)):
            self._log("no-controller-or-pdisk").error("getDetailedStatus() for logicalDisk '%s' failed! no controller or no physical disk found for this logical disk")
            return None,ReturnCodes.kGeneralError
        
        vdiskStatusDict,rc1 = controller.getVdiskStatus(vdiskName=vdiskName)
        pdiskStatusDict,rc2 = physicalDisk.getDetailedStatus()
        
        if ((rc1 == ReturnCodes.kOk) and (rc2 == ReturnCodes.kOk)):
            statusDict = {self.DETAILED_STATUS_KEY_VDISK : vdiskStatusDict, self.DETAILED_STATUS_KEY_PDISK : pdiskStatusDict}
            self._log("get-r0-disk-detailed-status-success").debug3("getDetailedStatus() for logicalDisk '%s' succeded! statusDistionary=%s",self._logicalDiskName,statusDict)
            return statusDict,ReturnCodes.kOk
        else:
            self._log("get-r0-disk-detailed-status-failed").error("getDetailedStatus() for logicalDisk '%s' failed!",self._logicalDiskName)
            return None,ReturnCodes.kGeneralError


    def getStatus (self):
        """
        Get the status summery
        """
        statusDict = None
        detailedStatusDict,rc = self.getDetailedStatus()
        if (rc != ReturnCodes.kOk):
            self._log("get-r0-disk-status-failed").error("getStatus() for logicalDisk '%s' failed!",self._logicalDiskName)
            return statusDict,rc

        status       = self.STATUS_DOWN
        state        = self.STATE_FAULT_STRING
        size         = self.NO_DATA
        serialNumber = self.NO_DATA

        vdiskStatusDict = detailedStatusDict[self.DETAILED_STATUS_KEY_VDISK]
        pdiskStatusDict = detailedStatusDict[self.DETAILED_STATUS_KEY_PDISK]

        # get state, status and size
        if ((vdiskStatusDict == None) and (pdiskStatusDict == None)):
            state = self.STATE_ABSENT_STRING
            status = self.STATUS_DOWN

        else:
            if (vdiskStatusDict != None):
                stateNumber = vdiskStatusDict[drc.VdiskStatus.KEY_STATE]
                if (stateNumber == drc.DellRaidController.VDISK_STATE_READY):
                    state = self.STATE_ACTIVE_STRING
                    status = self.STATUS_UP
                else:
                    state = self.STATE_FAULT_STRING
                    status = self.STATUS_DOWN
    
                sizeCandidate = vdiskStatusDict[drc.VdiskStatus.KEY_SIZE]
                if sizeCandidate:
                    size = sizeCandidate

            # get serial number
            if (pdiskStatusDict != None):
                serialNumberCandidate = pdiskStatusDict[drc.PdiskStatus.KEY_SERIAL_NUMBER]
                if serialNumberCandidate:
                    serialNumber = serialNumberCandidate
                
        statusDict = {self.STATUS_KEY_STATUS        : status,      
                      self.STATUS_KEY_STATE         : state,       
                      self.STATUS_KEY_SIZE          : size,        
                      self.STATUS_KEY_SERIAL_NUMBER : serialNumber}

        self._log("get-status-success").debug2("status for logicalDisk '%s' is %s",self._logicalDiskName,statusDict)
        return statusDict,ReturnCodes.kOk
        


class BlockDeviceLogicalDisk(LogicalDisk):
    """
    A logical disk based on a given block device (VM use)
    """
    def __init__ (self,logicalDiskName,physicalDiskManager,logger):
        LogicalDisk.__init__(self,logicalDiskName,physicalDiskManager,logger,G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_ON_BLOCK_DEVICE)
        #self._blockDevice = blockDevice

    def activate (self,forceInit):

        blockDevice = self._activeRaidArrayConfig.osDevice
        autoInit = self._activeRaidArrayConfig.autoInit

        if (blockDevice and os.path.exists(blockDevice)):
            self._log("successful-activation").debug1("successfully activated disk '%s' (autoInit=%s,forceinit=%s)",self._logicalDiskName,autoInit,forceInit)
            return blockDevice,ReturnCodes.kAlreadyExists

        self._log("failed-activation").error("failed to activated disk '%s' (autoInit=%s,forceinit=%s)",self._logicalDiskName,autoInit,forceInit)
        return blockDevice,ReturnCodes.kGeneralError


    def getDetailedStatus (self):
        """
        Get Detailed status of the object (same as status summary in this class)
        """
        return self.getStatus()


    def getStatus (self):
        """
        Get the status summery
        """        
        status       = self.STATUS_DOWN       
        state        = self.STATE_ABSENT_STRING
        size         = self.NO_DATA
        serialNumber = self.NO_DATA

        blockDevice = self._activeRaidArrayConfig.osDevice

        try:
            if os.path.exists(blockDevice):
            
                status = self.STATUS_UP
                state = self.STATE_ACTIVE_STRING
    
                deviceSuffix = os.path.split(blockDevice)[1]
                sizePath = os.path.join("/sys/class/block",deviceSuffix,"size")
                sizeFileFd = open(sizePath)
                # file size is given in this location in sectors (512 bytes) --> need to multiply by 512 to get size in bytes
                size = int(sizeFileFd.read())*512
            
        except Exception,e:
            self._log("failed-to-get-status").error("failed to fetch full status for disk '%s', returning best effort. exception = '%s'",self._logicalDiskName,e)
            
        statusDict = {self.STATUS_KEY_STATUS        : status,      
                      self.STATUS_KEY_STATE         : state,       
                      self.STATUS_KEY_SIZE          : size,        
                      self.STATUS_KEY_SERIAL_NUMBER : serialNumber}

        return statusDict,ReturnCodes.kOk
        




class DirectoryLogicalDisk(LogicalDisk):
    """
    A dummy logical disk for qm-10
    """

    def __init__ (self,logicalDiskName,physicalDiskManager,logger):
        LogicalDisk.__init__(self,logicalDiskName,physicalDiskManager,logger,G_NAME_GROUP_STORAGE_DISK_LOGICAL_DISK_IN_DIRECTORY)

    def activate (self,forceInit):
        autoInit = self._activeRaidArrayConfig.autoInit
        self._log("successful-activation").debug1("successfully activated disk '%s' (autoInit=%s,forceinit=%s)",self._logicalDiskName,autoInit,forceInit)
        blockDevice = None # we won't need the block device, just to be consistent with API, we must return something
        return blockDevice,ReturnCodes.kAlreadyExists



    def getDetailedStatus (self):
        """
        Get Detailed status of the object (same as status summary in this class)
        """
        return self.getStatus()


    def getStatus (self):
        """
        Get the status summery (Hint: it's always all good)
        """
        statusDict = {self.STATUS_KEY_STATUS        : self.STATUS_UP,
                      self.STATUS_KEY_STATE         : self.STATE_ACTIVE_STRING,
                      self.STATUS_KEY_SIZE          : self.NO_DATA,
                      self.STATUS_KEY_SERIAL_NUMBER : self.NO_DATA}

        return statusDict,ReturnCodes.kOk
