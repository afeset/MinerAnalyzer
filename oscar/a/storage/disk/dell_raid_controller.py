# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: effiz

import a.infra.subprocess
import a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen #  impoting with 'as blinky_generated_enums' causes stupid pycheck warnings
blinky_generated_enums=a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen  
from a.infra.format.xml import xmlToDict
from a.infra.basic.return_codes import ReturnCodes
from a.infra.basic.exceptions import FunctionTimeOut,TimeOutException
from a.storage.disk.controller import Controller
from a.storage.disk.common import Timer, TIME_TO_KILL_AFTER_TERMINATE, MINIMAL_TERMINATE_TIME

import time


if  __package__ is None:
    G_NAME_GROUP_STORAGE_CONTROLLER_DELL_RAID_CONTROLLER_H710 = "unknown"
else:
    from . import G_NAME_GROUP_STORAGE_CONTROLLER_DELL_RAID_CONTROLLER_H710

class Status(object):
    
    def __str__ (self):
        return str(self.__dict__)

    def toDictionary (self):
        pass

class VdiskStatus(Status):
    
    KEY_VDISK_NAME                 = "vdisk-name"
    KEY_PDISK_IDS                  = "pdisk-ids"
    KEY_VDISK_ID                   = "vdisk-id"
    KEY_BLOCK_DEVICE               = "block-device"
    KEY_MEDIA_TYPE                 = "media-type"
    KEY_SIZE_RAW                   = "size-raw"
    KEY_SIZE                       = "size"
    KEY_STATE_RAW                  = "state-raw"
    KEY_STATE                      = "state"
    KEY_STATE_ENUM                 = "state-enum"
    KEY_STATUS_RAW                 = "status-raw"
    KEY_STATUS                     = "status"
    KEY_STATUS_ENUM                = "status-enum"
    KEY_BAD_BLOCKS_RAW             = "bad-blocks-raw"
    KEY_BAD_BLOCKS                 = "bad-blocks"
    KEY_CACHE_POLICY               = "cache-policy"
    KEY_DISK_CACHE_POLICY          = "disk-cache-policy"
    KEY_HOT_SPARE_POLICY_VIOLATION = "hot-spare-policy-violation"
    KEY_RAID_TYPE                  = "raid-type"
    KEY_READ_POLICY                = "read-policy"
    KEY_STRIPE_ELEMENT_SIZE        = "stripe-element-size"
    KEY_WRITE_POLICY               = "write-policy"


    def __init__ (self):
        self.vdiskName               = None
        self.pdiskIds                = None
        self.vdiskId                 = None
        self.blockDevice             = None
        self.mediaType               = None
        self.sizeRaw                 = None
        self.size                    = None
        self.stateRaw                = None
        self.state                   = None
        self.stateEnum               = None
        self.statusRaw               = None
        self.status                  = None
        self.statusEnum              = None
        self.badBlocksRaw            = None
        self.badBlocks               = None
        self.cachePolicy             = None
        self.diskCachePolicy         = None
        self.hotSparePolicyViolation = None
        self.raidType                = None
        self.readPolicy              = None
        self.stripeElementSize       = None
        self.writePolicy             = None


    def toDictionary (self):
        pdiskIdsString = ""
        if (self.pdiskIds != None):
            pdiskIdsString = " ".join(sorted(list(self.pdiskIds)))

        return {self.KEY_VDISK_NAME                  : self.vdiskName                       ,
                self.KEY_PDISK_IDS                   : pdiskIdsString                  ,
                self.KEY_VDISK_ID                    : self.vdiskId                         ,
                self.KEY_BLOCK_DEVICE                : self.blockDevice                     ,
                self.KEY_MEDIA_TYPE                  : self.mediaType                       ,
                self.KEY_SIZE_RAW                    : self.sizeRaw                         ,
                self.KEY_SIZE                        : self.size                            ,
                self.KEY_STATE_RAW                   : self.stateRaw                        ,
                self.KEY_STATE                       : self.state                           ,
                self.KEY_STATE_ENUM                  : self.stateEnum                       ,
                self.KEY_STATUS_RAW                  : self.statusRaw                       ,
                self.KEY_STATUS                      : self.status                          ,
                self.KEY_STATUS_ENUM                 : self.statusEnum                      ,
                self.KEY_BAD_BLOCKS_RAW              : self.badBlocksRaw                    ,
                self.KEY_BAD_BLOCKS                  : self.badBlocks                       ,
                self.KEY_CACHE_POLICY                : self.cachePolicy                     ,
                self.KEY_DISK_CACHE_POLICY           : self.diskCachePolicy                 ,
                self.KEY_HOT_SPARE_POLICY_VIOLATION  : self.hotSparePolicyViolation         ,
                self.KEY_RAID_TYPE                   : self.raidType                        ,
                self.KEY_READ_POLICY                 : self.readPolicy                      ,
                self.KEY_STRIPE_ELEMENT_SIZE         : self.stripeElementSize               ,
                self.KEY_WRITE_POLICY                : self.writePolicy                     }            


class PdiskStatus(Status):
    
    KEY_VDISK_NAME               = "vdisk-name"           
    KEY_PDISK_ID                 = "pdisk-id"             
    KEY_STATUS_RAW               = "status-raw"           
    KEY_STATUS                   = "status"               
    KEY_STATUS_ENUM              = "status-enum"          
    KEY_STATE_RAW                = "state-raw"            
    KEY_STATE                    = "state"                
    KEY_STATE_ENUM               = "state-enum"           
    KEY_MEDIA_TYPE               = "media-type"           
    KEY_SIZE_RAW                 = "size-raw"             
    KEY_SIZE                     = "size"                 
    KEY_VENDOR                   = "vendor"               
    KEY_SERIAL_NUMBER            = "serial-number"        
    KEY_PART_NUMBER              = "part-number"          
    KEY_AVAILABLE_RAID_SPACE     = "available-raid-space" 
    KEY_CAPABLE_SPEED            = "capable-speed"        
    KEY_CERTIFIED                = "certified"            
    KEY_DEVICE_LIFE_REMAINING    = "device-life-remaining"
    KEY_DEVICE_LIFE_STATUS       = "device-life-status"   
    KEY_DEVICE_WRITE_CACHE       = "device-write-cache"   
    KEY_FAILURE_PREDICTED_RAW    = "failure-predicted-raw"
    KEY_FAILURE_PREDICTED        = "failure-predicted"    
    KEY_FIRMWARE_REVISION        = "firmware-revision"    
    KEY_HOT_SPARE                = "hot-spare"            
    KEY_MANUFACTURE_DAY          = "manufacture-day"      
    KEY_MANUFACTURE_WEEK         = "manufacture-week"     
    KEY_MANUFACTURE_YEAR         = "manufacture-year"     
    KEY_MODEL_NUMBER             = "model-number"         
    KEY_NEGOTIATED_SPEED         = "negotiated-speed"     
    KEY_POWER_STATUS             = "power-status"         
    KEY_PRODUCT_ID               = "product-id"           
    KEY_PROGRESS                 = "progress"             
    KEY_SAS_ADDRESS              = "sas-address"          
    KEY_USED_RAID_SPACE          = "used-raid-space"      


    def __init__ (self):
        self.vdiskName           = None
        self.pdiskId             = None
        self.statusRaw           = None
        self.status              = None
        self.statusEnum          = None
        self.stateRaw            = None
        self.state               = None
        self.stateEnum           = None
        self.mediaType           = None
        self.sizeRaw             = None
        self.size                = None
        self.vendor              = None
        self.serialNumber        = None
        self.partNumber          = None
        self.availableRaidSpace  = None
        self.capableSpeed        = None
        self.certified           = None
        self.deviceLifeRemaining = None
        self.deviceLifeStatus    = None
        self.deviceWriteCache    = None
        self.failurePredictedRaw = None
        self.failurePredicted    = None
        self.firmwareRevision    = None
        self.hotSpare            = None
        self.manufactureDay      = None
        self.manufactureWeek     = None
        self.manufactureYear     = None
        self.modelNumber         = None
        self.negotiatedSpeed     = None    
        self.powerStatus         = None    
        self.productId           = None    
        self.progress            = None    
        self.sasAddress          = None    
        self.usedRaidSpace       = None

        

    def toDictionary (self):
        # handle complex objects - make them json serializable

        return {self.KEY_VDISK_NAME            : self.vdiskName           ,
                self.KEY_PDISK_ID              : self.pdiskId             ,
                self.KEY_STATUS_RAW            : self.statusRaw           ,
                self.KEY_STATUS                : self.status              ,
                self.KEY_STATUS_ENUM           : self.statusEnum          ,
                self.KEY_STATE_RAW             : self.stateRaw            ,
                self.KEY_STATE                 : self.state               ,
                self.KEY_STATE_ENUM            : self.stateEnum           ,
                self.KEY_MEDIA_TYPE            : self.mediaType           ,
                self.KEY_SIZE_RAW              : self.sizeRaw             ,
                self.KEY_SIZE                  : self.size                ,
                self.KEY_VENDOR                : self.vendor              ,
                self.KEY_SERIAL_NUMBER         : self.serialNumber        ,
                self.KEY_PART_NUMBER           : self.partNumber          ,
                self.KEY_AVAILABLE_RAID_SPACE  : self.availableRaidSpace  ,
                self.KEY_CAPABLE_SPEED         : self.capableSpeed        ,
                self.KEY_CERTIFIED             : self.certified           ,
                self.KEY_DEVICE_LIFE_REMAINING : self.deviceLifeRemaining ,
                self.KEY_DEVICE_LIFE_STATUS    : self.deviceLifeStatus    ,
                self.KEY_DEVICE_WRITE_CACHE    : self.deviceWriteCache    ,
                self.KEY_FAILURE_PREDICTED_RAW : self.failurePredictedRaw ,
                self.KEY_FAILURE_PREDICTED     : self.failurePredicted    ,
                self.KEY_FIRMWARE_REVISION     : self.firmwareRevision    ,
                self.KEY_HOT_SPARE             : self.hotSpare            ,
                self.KEY_MANUFACTURE_DAY       : self.manufactureDay      ,
                self.KEY_MANUFACTURE_WEEK      : self.manufactureWeek     ,
                self.KEY_MANUFACTURE_YEAR      : self.manufactureYear     ,
                self.KEY_MODEL_NUMBER          : self.modelNumber         ,
                self.KEY_NEGOTIATED_SPEED      : self.negotiatedSpeed     ,
                self.KEY_POWER_STATUS          : self.powerStatus         ,
                self.KEY_PRODUCT_ID            : self.productId           ,
                self.KEY_PROGRESS              : self.progress            ,
                self.KEY_SAS_ADDRESS           : self.sasAddress          ,
                self.KEY_USED_RAID_SPACE       : self.usedRaidSpace      }


class DellRaidController(Controller):
    """
    A class represnting a DELL disk controller.
    performes action with the OpenMange cli utility.
    """
    # const timeouts
    INIT_TIME_OUT = 25

    # input strings
    INPUT_CONFIG_COMMAND = "/opt/dell/srvadmin/bin/omconfig"
    INPUT_REPORT_COMMAND = "/opt/dell/srvadmin/bin/omreport"
    INPUT_STORAGE_COMMAND_ELEMENT = "storage"
    INPUT_CONTROLLER_COMMAND_ELEMENT = "controller"
    INPUT_VDISK_COMMAND_ELEMENT = "vdisk"
    INPUT_PDISK_COMMAND_ELEMENT = "pdisk"
    CONTROLLER_OPT = "controller=%s"
    VDISK_OPT = "vdisk=%s"
    PDISK_OPT = "pdisk=%s"
    SIZE_OPT = "size=%s"
    SIZE_OPT_MAX_VALUE = "max"
    RAID_OPT = "raid=%s"
    DISK_CACHE_POLICY_OPT = "diskcachepolicy=%s"
    WRITE_POLICY_OPT = "writepolicy=%s"
    READ_POLICY_OPT = "readpolicy=%s"
    VDISK_NAME_OPT = "name=%s"
    ACTION_OPT = "action=%s"
    FORMAT_OPT = "-fmt"
    PDISK_ID_BETWEEN_ELEMENTS_DELIMITER = ":"
    PDISK_BETWEEN_IDS_DELIMITER = ","

    # output strings
    OUTPUT_TAG_VDISKS = "VirtualDisks"
    OUTPUT_TAG_STORAGE_OBJECT = "DCStorageObject"
    OUTPUT_TAG_VDISK_NAME = "Name"
    OUTPUT_TAG_DEVICE_ID = "DeviceID"
    OUTPUT_TAG_BLOCK_DEVICE = "DeviceName"
    OUTPUT_TAG_STATE = "ObjState"
    OUTPUT_TAG_STATUS = "ObjStatus"
    OUTPUT_TAG_MEDIA_TYPE = "MediaType"
    OUTPUT_TAG_SIZE = "Length"
    OUTPUT_TAG_VENDOR = "Vendor"
    OUTPUT_TAG_SERIAL_NUMBER = "DeviceSerialNumber"
    OUTPUT_TAG_PART_NUMBER = "PartNo"
    OUTPUT_TAG_AVAILABLE_RAID_SPACE = "FreeSpace"
    OUTPUT_TAG_CAPABLE_SPEED = "CapableSpeed"
    OUTPUT_TAG_REVISION = "Revision"
    OUTPUT_TAG_MANUFACTURE_DAY = "ManufactureDay"
    OUTPUT_TAG_MANUFACTURE_WEEK = "ManufactureWeek"
    OUTPUT_TAG_MANUFACTURE_YEAR = "ManufactureYear"
    OUTPUT_TAG_NEGOTIATED_SPEED = "NegotiatedSpeed"
    OUTPUT_TAG_POWER_STATUS = "PDPowerState"   
    OUTPUT_TAG_PRODUCT_ID = "ProductID"
    OUTPUT_TAG_SAS_ADDRESS = "SASAddress"
    OUTPUT_TAG_USED_RAID_SPACE = "UsedSpace"
    OUTPUT_TAG_BAD_BLOCKS = "VDBadBlocksDetected"
    OUTPUT_TAG_DISK_CACHE_POLICY = "DiskCachePolicy"
    OUTPUT_TAG_LAYOUT = "Layout"
    OUTPUT_TAG_READ_POLICY = "ReadPolicy"
    OUTPUT_TAG_STRIPE_SIZE = "StripeSize"
    OUTPUT_TAG_WRITE_POLICY = "WritePolicy"

    OUTPUT_TAG_PDISKS = "ArrayDisks"
    OUTPUT_TAG_PDISK_ID_ELEMENTS = ["Channel","EnclosureID","TargetID"]


    # errorMsg ids (Temporary)
    INVALID_VDISK = 1604
    INVALID_PDISK = 1602

    # pdisk state values
    PDISK_STATE_ONLINE  = 4
    PDISK_STATE_READY   = 1
    PDISK_STATE_FOREIGN = 274877906944
    PDISK_STATUS_OK     = 2

    # vdisk state values
    VDISK_STATE_READY = 1
    VDISK_STATUS_OK = 2

    # internals
    RAID_LEVEL_0 = "r0"
    DISK_CACHE_POLICY_ENABELED = "enabled"
    WRITE_POLICY_WRITE_THROUGH = "wt"
    READ_POLICY_ADAPTIVE_READ_AHEAD = "ara"


    def __init__ (self,name,internalId,groupName,logger):
        Controller.__init__(self,name,internalId,groupName,logger)
        self._onlineVdisks = {}
        self._faultyVdisks = {}
        self._onlinePdisks = {}
        self._readyPdisks = {}
        self._foreignPdisks = {}
        self._faultyButPresentPdisks = {}
        self._mappingInconsistent = True


    def init (self):
        self._log("dell-controller-init").debug2("DellRaidController.init() called")
        try:
            timer = Timer(self.INIT_TIME_OUT)
            while (self._getPdiskInfo(timer)[1] != ReturnCodes.kOk):
                self._log("dell-controller-init-wait").debug2("srvadmin-services.sh is not available yet. sleeping for 2 seconds...")
                time.sleep(2)

            self._log("dell-controller-init-success").debug2("DellRaidController.init() succeded")
            return ReturnCodes.kOk

        except:
            self._log("dell-controller-init-fail").error("DellRaidController.init() failed!")
            return ReturnCodes.kGeneralError


    def __setMappingInconsistent (self):
        self._log("mapping-inconsistent").debug1("entering danger zone - mapping inconsistent")
        self._mappingInconsistent = True

    def __setMappingConsistent (self):
        self._mappingInconsistent = False
        self._log("mapping-consistent").debug1("left danger zone - mapping consistent")

    def _getFromDict (self,key,dict,type,defaultVal=None,shouldWarn=True):

        try:
            return type(dict[key])
        except Exception,e:
            if shouldWarn:
                self._log('exception-getting attribute').warning("could not fetch key '%s' (%s) from dictionary! returning default %s. exception = '%s'",key,type,defaultVal,e)
            return defaultVal


    def buildVdiskStatusObject (self,vdiskInfo,pdiskIds):

        vdiskStatus = VdiskStatus()
        
        vdiskStatus.vdiskName               = self._getFromDict(self.OUTPUT_TAG_VDISK_NAME,vdiskInfo,str)
        vdiskStatus.pdiskIds                = pdiskIds
        vdiskStatus.vdiskId                 = self._getFromDict(self.OUTPUT_TAG_DEVICE_ID,vdiskInfo,str)
        vdiskStatus.blockDevice             = self._getFromDict(self.OUTPUT_TAG_BLOCK_DEVICE,vdiskInfo,str)
        vdiskStatus.mediaType               = self._getFromDict(self.OUTPUT_TAG_MEDIA_TYPE,vdiskInfo,str,"")
        vdiskStatus.sizeRaw                 = self._getFromDict(self.OUTPUT_TAG_SIZE,vdiskInfo,str,"")
        vdiskStatus.size                    = self._getFromDict(self.OUTPUT_TAG_SIZE,vdiskInfo,int,0)
        vdiskStatus.stateRaw                = self._getFromDict(self.OUTPUT_TAG_STATE,vdiskInfo,str,"")
        vdiskStatus.state                   = self._getFromDict(self.OUTPUT_TAG_STATE,vdiskInfo,int)
        if (vdiskStatus.state == self.VDISK_STATE_READY):
            vdiskStatus.stateEnum = blinky_generated_enums.RaidArrayStateType.kReady
        else:
            vdiskStatus.stateEnum = blinky_generated_enums.RaidArrayStateType.kFault

        vdiskStatus.statusRaw               = self._getFromDict(self.OUTPUT_TAG_STATUS,vdiskInfo,str,"")
        vdiskStatus.status                  = self._getFromDict(self.OUTPUT_TAG_STATUS,vdiskInfo,int)
        if (vdiskStatus.status == self.VDISK_STATUS_OK):
            vdiskStatus.statusEnum = blinky_generated_enums.RaidArrayStatusType.kOk
        else:
            vdiskStatus.statusEnum = blinky_generated_enums.RaidArrayStatusType.kFailure
            # TODO: handle critical case

        vdiskStatus.badBlocksRaw            = self._getFromDict(self.OUTPUT_TAG_BAD_BLOCKS,vdiskInfo,str,"No",False)
        vdiskStatus.badBlocks               = False if (vdiskStatus.badBlocksRaw == "No") else True
        vdiskStatus.cachePolicy             = "Not Applicable"
        vdiskStatus.diskCachePolicy         = self._getFromDict(self.OUTPUT_TAG_DISK_CACHE_POLICY,vdiskInfo,str,"")
        vdiskStatus.hotSparePolicyViolation = "Not Applicable"
        vdiskStatus.raidType                = self._getFromDict(self.OUTPUT_TAG_LAYOUT,vdiskInfo,str,"")
        vdiskStatus.readPolicy              = self._getFromDict(self.OUTPUT_TAG_READ_POLICY,vdiskInfo,str,"")
        vdiskStatus.stripeElementSize       = self._getFromDict(self.OUTPUT_TAG_STRIPE_SIZE,vdiskInfo,str,"")
        vdiskStatus.writePolicy             = self._getFromDict(self.OUTPUT_TAG_WRITE_POLICY,vdiskInfo,str,"")

        # obligatory fields - without them there is no way to work with this info
        if ((vdiskStatus.status==None) or \
            (vdiskStatus.state==None) or \
            (vdiskStatus.vdiskId==None) or \
            (vdiskStatus.blockDevice==None) or\
            (vdiskStatus.vdiskName==None)):
            self._log("unusable-vdisk-info").warning("the following object was found and is unusable '%s'",vdiskStatus)
            return None
        
        return vdiskStatus


    def buildPdiskStatusObject (self,pdiskInfo,vdiskName=None):

        pdiskStatus = PdiskStatus()

        pdiskStatus.vdiskName              = vdiskName
        pdiskStatus.pdiskId                = self._getPdiskIdFromPdiskInfo(pdiskInfo)
        pdiskStatus.statusRaw              = self._getFromDict(self.OUTPUT_TAG_STATUS,pdiskInfo,str,"")
        pdiskStatus.status                 = self._getFromDict(self.OUTPUT_TAG_STATUS,pdiskInfo,int)

        if (pdiskStatus.status == self.PDISK_STATUS_OK):
            pdiskStatus.statusEnum = blinky_generated_enums.PhysicalStatusType.kOk
        else:
            pdiskStatus.statusEnum = blinky_generated_enums.PhysicalStatusType.kFailure
            
        pdiskStatus.stateRaw               = self._getFromDict(self.OUTPUT_TAG_STATUS,pdiskInfo,str,"")
        pdiskStatus.state                  = self._getFromDict(self.OUTPUT_TAG_STATE,pdiskInfo,int)

        if (pdiskStatus.state == self.PDISK_STATE_ONLINE):
            pdiskStatus.stateEnum = blinky_generated_enums.PhysicalStateType.kOnline
        elif (pdiskStatus.state == self.PDISK_STATE_READY):
            pdiskStatus.stateEnum = blinky_generated_enums.PhysicalStateType.kReady
        elif (pdiskStatus.state == self.PDISK_STATE_FOREIGN):
            pdiskStatus.stateEnum = blinky_generated_enums.PhysicalStateType.kForeign
        else:
            pdiskStatus.stateEnum = blinky_generated_enums.PhysicalStateType.kFault

        pdiskStatus.mediaType              = self._getFromDict(self.OUTPUT_TAG_MEDIA_TYPE,pdiskInfo,str,"")
        pdiskStatus.sizeRaw                = self._getFromDict(self.OUTPUT_TAG_SIZE,pdiskInfo,str,"0")
        pdiskStatus.size                   = self._getFromDict(self.OUTPUT_TAG_SIZE,pdiskInfo,int,0)
        pdiskStatus.vendor                 = self._getFromDict(self.OUTPUT_TAG_VENDOR,pdiskInfo,str,"")
        pdiskStatus.serialNumber           = self._getFromDict(self.OUTPUT_TAG_SERIAL_NUMBER,pdiskInfo,str,"")
        pdiskStatus.partNumber             = self._getFromDict(self.OUTPUT_TAG_PART_NUMBER,pdiskInfo,str,"")
        pdiskStatus.availableRaidSpace     = self._getFromDict(self.OUTPUT_TAG_AVAILABLE_RAID_SPACE,pdiskInfo,str,"")
        pdiskStatus.capableSpeed           = self._getFromDict(self.OUTPUT_TAG_CAPABLE_SPEED,pdiskInfo,str,"")
        pdiskStatus.certified              = "YES"
        pdiskStatus.deviceLifeRemaining    = "Not Applicable"
        pdiskStatus.deviceLifeStatus       = "Not Applicable"
        pdiskStatus.deviceWriteCache       = "Not Applicable"
        pdiskStatus.failurePredictedRaw    = "No" # not to be found in xml format, so for now hardcoded
        pdiskStatus.failurePredicted       = blinky_generated_enums.PhysicalFailurePredictedType.kFalse
        pdiskStatus.firmwareRevision       = self._getFromDict(self.OUTPUT_TAG_REVISION,pdiskInfo,str,"")
        pdiskStatus.hotSpare               = "No"
        pdiskStatus.manufactureDay         = self._getFromDict(self.OUTPUT_TAG_MANUFACTURE_DAY,pdiskInfo,str,"")
        pdiskStatus.manufactureWeek        = self._getFromDict(self.OUTPUT_TAG_MANUFACTURE_WEEK,pdiskInfo,str,"")
        pdiskStatus.manufactureYear        = self._getFromDict(self.OUTPUT_TAG_MANUFACTURE_YEAR,pdiskInfo,str,"")
        pdiskStatus.modelNumber            = "Not Applicable"
        pdiskStatus.negotiatedSpeed        = self._getFromDict(self.OUTPUT_TAG_NEGOTIATED_SPEED,pdiskInfo,str,"")
        pdiskStatus.powerStatus            = self._getFromDict(self.OUTPUT_TAG_POWER_STATUS,pdiskInfo,str,"")
        pdiskStatus.productId              = self._getFromDict(self.OUTPUT_TAG_PRODUCT_ID,pdiskInfo,str,"")
        pdiskStatus.progress               = "Not Applicable"
        pdiskStatus.sasAddress             = self._getFromDict(self.OUTPUT_TAG_SAS_ADDRESS,pdiskInfo,str,"")
        pdiskStatus.usedRaidSpace          = self._getFromDict(self.OUTPUT_TAG_USED_RAID_SPACE,pdiskInfo,str,"") 

        # obligatory fields - without them there is no way to work with this info
        if ((pdiskStatus.pdiskId==None) or (pdiskStatus.status==None) or (pdiskStatus.state==None)):
            self._log("unusable-pdisk-info").warning("the following object was found and is unusable '%s'",pdiskStatus)
            return None

        return pdiskStatus


    def _runConfigCommand (self,args,timer):
        """
        Run a general 'omconfig storage' command.
        """
        return self._runCommand(self.INPUT_CONFIG_COMMAND,args,timer)

    def _runReportCommand (self,args,timer):
        """
        Run a general 'omreport storage' command.
        """
        return self._runCommand(self.INPUT_REPORT_COMMAND,args,timer)

    def _runCommand (self,cmdBase,args,timer):
        """
        Run a general 'omXXXXX storage' command.
        """
        # build command line list
        cmd = [cmdBase]
        cmd.append(self.INPUT_STORAGE_COMMAND_ELEMENT)
        controllerOptAndVal = [self.CONTROLLER_OPT%self._index] # TODO: cahnge this to come from config
        formatSuffix = [self.FORMAT_OPT,"xml"]
        cmd += args + controllerOptAndVal + formatSuffix

        # check timeout is valid or raise exception
        terminateTimeOut = timer.getTimeLeft()
        if (terminateTimeOut < MINIMAL_TERMINATE_TIME):
            self._log("timeout-before-running").error("running command '%s' failed before running on timeout=%.2f<%.2f=MINIMAL_TERMINATE_TIME",cmd,terminateTimeOut,MINIMAL_TERMINATE_TIME)
            raise FunctionTimeOut("_runCommand(cmdBase=%s,args=%s,terminateTimeOut=%.2f)"%(cmdBase,args,terminateTimeOut),terminateTimeOut)

        # instantiate a process to excute the command
        proc = a.infra.subprocess.Subprocess("om-cmd",self._log)

        # start the process
        proc.start(cmd,stdout=a.infra.subprocess.PIPE,stderr=a.infra.subprocess.PIPE)
        commandLine = proc.getCommandLine()
        self._log("run-command").debug2("running command '%s'",commandLine)

        # communicate (i.e. wait for command end or timeout)
        killTimeOut = terminateTimeOut + TIME_TO_KILL_AFTER_TERMINATE
        stdout,stderr = proc.communicate(terminateTimeOut=terminateTimeOut,killTimeOut=killTimeOut)

        rc = proc.getReturnCode()
        if (rc >= 0):
            # execution ended normally (with success or failure) - parse output
            if (rc==0):
                self._log("command-successful").debug3("the command '%s' ended successfully, stdout=%s",commandLine,stdout)
            else:
                self._log("command-unsuccessful").debug2("the command '%s' ended but was unsuccessful, stdout=%s, stderr=%s",commandLine,stdout,stderr)
            
            # parse xml output
            try:
                output = xmlToDict(stdout)
                return output,rc
            except Exception:
                # failed parsing
                self._log("xml-conversion-failed").error("the command '%s' output was no successfully converted from xml to dictionary",commandLine)
                # re-raise
                raise

        else:
            # command failed (signal sent) - log and rais exception
            self._log("command-failed-on-signal").error("the command '%s' failed (signal %d sent)",commandLine,rc)
            raise a.infra.subprocess.SubprocessDeathBySignal(proc)


    def _getOutputErrorIfAny(self,commandOutputDictionary):
        """
        Retrieve the error code from the XML if there is one, returns None if there isn't.
        """

        # TODO: make this more intelegent when you get a proper documentaion
        cliMsgIdTag = "CLIMsgID"
        if cliMsgIdTag in commandOutputDictionary:
            return int(commandOutputDictionary[cliMsgIdTag])
        return None


    def _updateOfflinePdiskMapping (self,timer):
        
        pdiskInfoList,rc = self._getPdiskInfo(timer)
        if (rc != ReturnCodes.kOk):
            self._log("pdisk-info-fail").error("_updateOfflinePdiskMapping() failed, could not get general pdisk info!")
            return ReturnCodes.kGeneralError

        for pdiskStatusObj in pdiskInfoList:
            pdiskId = pdiskStatusObj.pdiskId
            pdiskState = pdiskStatusObj.state

            if (pdiskState != self.PDISK_STATE_ONLINE):
                
                if pdiskId in self._onlinePdisks:
                    vdiskName = self._onlinePdisks.pop(pdiskId).vdiskName
                    if vdiskName in self._onlineVdisks:
                        self._onlineVdisks.pop(vdiskName)
                    self._log("invalid-online").warning("vdisk %s and pdisk %s are no longer online, updating mapping",vdiskName,pdiskId)

                if (pdiskState == self.PDISK_STATE_READY):
                    self._readyPdisks[pdiskId] = pdiskStatusObj
                    self._log("add-to-ready").debug3("pdisk '%s' was found in Ready state, adding to mapping",pdiskId)
    
                elif (pdiskState == self.PDISK_STATE_FOREIGN):
                    self._foreignPdisks[pdiskId] = pdiskStatusObj
                    self._log("add-to-foreign").debug3("pdisk '%s' was found in Foreign state, adding to mapping",pdiskId)
    
                else:
                    self._faultyButPresentPdisks[pdiskId] = pdiskStatusObj
                    self._log("unrecognized-pdisk-state").warning("pdisk '%s' was found in unknown state (=%s)",pdiskId,pdiskState)

        return ReturnCodes.kOk
        

    def  _updateVdiskPdiskMapping (self,timer):

        self._log("mapping-inconsistent").debug2("request to update mapping was issued - updating now")
        self._onlineVdisks = {}
        self._faultyVdisks = {}
        self._onlinePdisks = {}
        self._readyPdisks = {}
        self._foreignPdisks = {}
        self._faultyButPresentPdisks = {}

        vdiskInfoList,rc = self._getVdiskInfo(timer)
        if ((rc != ReturnCodes.kOk) and (rc != ReturnCodes.kNotFound)):
            self._log("vdisk-info-fail").error("_updateVdiskPdiskMapping() failed, could not get vdisk info!")
            return ReturnCodes.kGeneralError
        
        # for each online vdisk get his relevant pdisks and blockDevice
        for vdiskStatusObj in vdiskInfoList:

            vdiskState = vdiskStatusObj.state
            vdiskStatus = vdiskStatusObj.status
            vdiskName = vdiskStatusObj.vdiskName
            vdiskId = vdiskStatusObj.vdiskId

            if ((vdiskStatus != self.VDISK_STATUS_OK) or (vdiskState != self.VDISK_STATE_READY)):
                self._faultyVdisks[vdiskName] = vdiskStatusObj 
                self._log("vdisk-in-bad-state").warning("vdisk '%s' (vdiskId=%s) is in bad status ('%d' is not 'Ok') or bad state ('%d' is not ready), and will not be inserted to online disks group",vdiskName,vdiskId,vdiskStatus,vdiskState)
            else: 
                self._onlineVdisks[vdiskName] = vdiskStatusObj

            pdiskInfoList,rc = self._getPdiskInfo(timer,vdiskId,failIfOneIsBad=True)
            if (rc != ReturnCodes.kOk):
                self._log("pdisk-info-fail").warning("_updateVdiskPdiskMapping() partialy failed, could not get pdisk info for vdisk '%s' (vdiskId=%s)! it will not be inserted to online disks group",vdiskName,vdiskId)
                continue

            pdiskIds = set()
            for pdiskStatusObj in pdiskInfoList:
                pdiskId = pdiskStatusObj.pdiskId
                pdiskIds.add(pdiskId)
                pdiskStatusObj.vdiskName = vdiskName
                self._onlinePdisks[pdiskId] = pdiskStatusObj

            vdiskStatusObj.pdiskIds = pdiskIds
            self._log("add-to-mapping").debug3("vdisk '%s' is mapped to pdisks %s",vdiskName,pdiskIds)
        
        # map ready and foreign pdisks
        rc = self._updateOfflinePdiskMapping(timer)
        if (rc != ReturnCodes.kOk):
            self._log("offline-pdisk-update-fail").error("_updateVdiskPdiskMapping() failed while updating pdisk/vdisk mapping")
            return ReturnCodes.kGeneralError

        self._log("update-mapping-success").debug2("succssfully updated mapping")
        self.__setMappingConsistent()
        return ReturnCodes.kOk


    def _getVdiskInfo (self,timer,vdiskId=None,vdiskName=None,failIfOneIsBad=False):
        """
        Fetch vdisk(s) info.
        """
        args = None
        if (vdiskId == None):
            args = [self.INPUT_CONTROLLER_COMMAND_ELEMENT]
        else:
            args = [self.INPUT_VDISK_COMMAND_ELEMENT,self.VDISK_OPT%vdiskId]

        outputDictionary,rc = self._runReportCommand(args,timer)
        
        if (rc == 0):
            if (self.OUTPUT_TAG_VDISKS not in outputDictionary):
                return [],ReturnCodes.kNotFound

            # if no errors and vdisks info is present - return it
            toReturn = []
            foundVdisksInfoList = outputDictionary[self.OUTPUT_TAG_VDISKS][0][self.OUTPUT_TAG_STORAGE_OBJECT]

            if (vdiskName == None):
                self._log("vdisk-info-found").debug4("executed command %s -> vdisk info was found: %s",args,outputDictionary)
                
                for vdiskInfo in foundVdisksInfoList:
                    vdiskStatusObj = self.buildVdiskStatusObject(vdiskInfo,None)
                    if (vdiskStatusObj == None):
                        if (failIfOneIsBad or (vdiskId != None)): # fail if requested or vdiskId is used (just one vdisk requested - must fail)
                            self._log("fail-if-one-is-bad").error("_getVdiskInfo() failed because one vdisk status obj didn't have all data (%s)",vdiskStatusObj)
                            return [],ReturnCodes.kGeneralError

                    else:
                        # vdiskStatusObj is usable 
                        toReturn.append(vdiskStatusObj)
                
                return toReturn,ReturnCodes.kOk
                        
            else:
                for vdiskInfo in foundVdisksInfoList:
                    if (self._getFromDict(self.OUTPUT_TAG_VDISK_NAME,vdiskInfo,str) == vdiskName):
                        self._log("vdisk-info-with-name-found").debug3("executed command %s -> vdisk info was found: %s",args,vdiskInfo)
                        vdiskStatusObj = self.buildVdiskStatusObject(vdiskInfo,None)
                        if (vdiskStatusObj == None):
                            self._log("fail-if-one-is-bad").error("_getVdiskInfo() failed because the vdisk status obj didn't have all data (%s)",vdiskStatusObj)
                            return [],ReturnCodes.kGeneralError

                        return [vdiskStatusObj],ReturnCodes.kOk
                self._log("vdisk-info-with-name-not-found").debug3("executed command %s -> vdisk info for vdiskName=%s was not found",args,vdiskName)
                return [],ReturnCodes.kNotFound
                
        else:
            errorCode = self._getOutputErrorIfAny(outputDictionary)
            if (errorCode == self.INVALID_VDISK):
                # if error is INVALID_VDISK - return [] (there is no such vdisk)
                self._log("vdisk-info-not-found").debug2("executed command %s -> vdisk info was not found! %s",args)
                return [],ReturnCodes.kNotFound
            else:
                # otherwise this is an unexpected error
                self._log("get-vdisk-info-unexpected-error").error("_getVdiskInfo(vdiskId=%s) failed (errorCode=%s)",vdiskId,errorCode)
                return [],ReturnCodes.kGeneralError


    def _getPdiskInfo (self,timer,vdiskId=None,failIfOneIsBad=False):
        """
        Fetch pdisks info.
        """

        args = None
        if (vdiskId == None):
            args = [self.INPUT_CONTROLLER_COMMAND_ELEMENT]
        else:
            args = [self.INPUT_PDISK_COMMAND_ELEMENT,self.VDISK_OPT%vdiskId]

        outputDictionary,rc = self._runReportCommand(args,timer)

        if (rc == 0):
            toReturn = []

            if (self.OUTPUT_TAG_PDISKS in outputDictionary):
                # if no errors and pdisks info is present - return it
                self._log("pdisk-info-found").debug3("executed command %s -> pdisk info was found: %s",args,outputDictionary)
                pdiskInfoList = outputDictionary[self.OUTPUT_TAG_PDISKS][0][self.OUTPUT_TAG_STORAGE_OBJECT]
                
                for pdiskInfo in pdiskInfoList:
                    pdiskStatusObj = self.buildPdiskStatusObject(pdiskInfo)
                    if (pdiskStatusObj == None):
                        if (failIfOneIsBad or (vdiskId != None)): # fail if requested or vdiskId is used (just one vdisk requested - must fail)
                            self._log("fail-if-one-is-bad").error("_getPdiskInfo() failed because one pdisk status obj didn't have all data (%s)",pdiskStatusObj)
                            return [],ReturnCodes.kGeneralError
    
                    else:
                        # pdiskStatusObj is usable 
                        toReturn.append(pdiskStatusObj)
    
            return toReturn,ReturnCodes.kOk
            
        else:
            errorCode = self._getOutputErrorIfAny(outputDictionary)
            if ((errorCode == self.INVALID_VDISK) or (errorCode == self.INVALID_PDISK)):
                # if error is INVALID_VDISK or INVALID_PDISK- return [] (there is no such vdisk)
                self._log("pdisk-info-not-found").debug2("executed command %s -> pdisk info was not found! %s",args)
                return [],ReturnCodes.kNotFound
            else:
                # otherwise this is an unexpected error
                self._log("get-pdisk-info-unexpected-error").error("_getPdiskInfo(vdiskId=%s,failIfOneIsBad=%s) failed (errorCode=%s)",vdiskId,failIfOneIsBad,errorCode)
                return [],ReturnCodes.kGeneralError


    def _fastInitVdisk (self,vdiskId,timer):
        """
        Fast-init an existing vdisk by vdiskId.
        """

        args = [self.INPUT_VDISK_COMMAND_ELEMENT,self.VDISK_OPT%vdiskId,self.ACTION_OPT%"fastinit"]
        self.__setMappingInconsistent()
        outputDictionary,rc = self._runConfigCommand(args,timer)

        if (rc == 0):
            self._log("vdisk-fast-init-success").debug2("fast init for vdiskId=%s was successful",vdiskId)
            self.__setMappingConsistent()
            return ReturnCodes.kOk
        else:
            errorCode = self._getOutputErrorIfAny(outputDictionary)
            self._log("vdisk-fast-init-fail").debug1("fast init for vdiskId=%s failed (errorCode=%s)",vdiskId,errorCode)
            return ReturnCodes.kGeneralError


    def _getPdiskIdFromPdiskInfo(self,pdiskInfo):
        """
        Retrieve the pdiskId from the pdiskInfo dictionary.
        """
        idElems = []
        for idElem in self.OUTPUT_TAG_PDISK_ID_ELEMENTS:
            elem = self._getFromDict(idElem,pdiskInfo,str)
            if elem == None:
                self._log("bad-pdisk-id-elem").error("bad pdisk Id elem %s",idElem)
                return None
            idElems.append(pdiskInfo[idElem])

        pdiskId = self.PDISK_ID_BETWEEN_ELEMENTS_DELIMITER.join(idElems)
        self._log("pdosk-id-found").debug5("pdisk id %s was found",pdiskId)
        return pdiskId

    
    def _clearForeignConfig (self,timer):
        """ 
        Clear foreign config of controller
        """ 
        actionOptAndVal = self.ACTION_OPT%"clearforeignconfig"
        args = [self.INPUT_CONTROLLER_COMMAND_ELEMENT,actionOptAndVal]
        self.__setMappingInconsistent()
        outputDictionary,rc = self._runConfigCommand(args,timer)

        if (rc == 0):
            self._log("clear-foreign-config-success").debug1("successfully cleared foreign configuration")
            self._readyPdisks.update(self._foreignPdisks)
            self._foreignPdisks.clear()
            self.__setMappingConsistent()
            return ReturnCodes.kOk

        else:
            # this is an unexpected failure
            errorCode = self._getOutputErrorIfAny(outputDictionary)
            self._log("clear-foreign-config-fail").error("_clearForeignConfig() failed (errorCode=%s)",errorCode)
            return ReturnCodes.kGeneralError


    def _deleteVdisk (self,vdiskName,timer):
        """
        Delete a vdisk
        """
        vdiskId         = self._onlineVdisks[vdiskName].vdiskId
        vdiskOptAndVal  = self.VDISK_OPT%vdiskId
        actionOptAndVal = self.ACTION_OPT%"deletevdisk"

        args = [self.INPUT_VDISK_COMMAND_ELEMENT,actionOptAndVal,vdiskOptAndVal]
        self.__setMappingInconsistent()
        outputDictionary,rc = self._runConfigCommand(args,timer)

        if (rc == 0):
            self._log("delete-vdisk-success").debug1("successfully deleted vdisk '%s'",vdiskName)
            vdiskStatus = self._onlineVdisks.pop(vdiskName)
            pdiskIds = vdiskStatus.pdiskIds
            for pdiskId in pdiskIds:
                pdiskStatus = self._onlinePdisks.pop(pdiskId)
                pdiskStatus.vdiskName = None
                self._readyPdisks[pdiskId] = pdiskStatus
                # TODO - consider _updateOfflinePdiskMapping() instead of 4 lines above
            self.__setMappingConsistent()
            return ReturnCodes.kOk
        else:
            # this is an unexpected failure
            errorCode = self._getOutputErrorIfAny(outputDictionary)
            self._log("delete-vdisk-fail").error("failed to delete vdisk '%s' (errorCode=%s)",vdiskName,errorCode)
            return ReturnCodes.kGeneralError


    def _createNewVdisk(self,raidLevel,pdiskIdsList,vdiskName,diskCachePolicy,writePolicy,readPolicy,timer):
        """
        Create a new vdisk.
        """
        # before construction of the vdisk clear foreign config and destory vdisks, if needed
        for pdiskId in pdiskIdsList:
            if (pdiskId in self._foreignPdisks):
                self._log("clear-foreign-config-needed").debug2("pdisk '%s' is in Foreign state and is needed to be localized for the creation of vdisk '%s', attempting to clear foreign config",pdiskId,vdiskName)
                rc = self._clearForeignConfig(timer)
                if (rc != ReturnCodes.kOk):
                    self._log("create-new-vdisk-failed").error("failed to create new vdisk '%s' because of failure to clear foreign config (pdisk '%s' is foreign)!",vdiskName,pdiskId)
                    return rc
            
            if (pdiskId in self._onlinePdisks):
                badVdiskName = self._onlinePdisks[pdiskId].vdiskName
                self._log("destroy-vdisk-needed").debug2("pdisk '%s' is in use by vdisk '%s', attempting to delete this vdisk",pdiskId,badVdiskName)
                rc = self._deleteVdisk(badVdiskName,timer)
                if (rc != ReturnCodes.kOk):
                    self._log("create-new-vdisk-failed").error("failed to create new vdisk '%s' because of failure to delete vdisk '%s' that is using pdisk '%s'!",vdiskName,badVdiskName,pdiskId)
                    return rc

            if (pdiskId in self._faultyButPresentPdisks):
                self._log("create-new-vdisk-failed").error("failed to create new vdisk '%s', pdisk '%s' is in faulty state! '%s'",vdiskName,pdiskId,self._faultyButPresentPdisks[pdiskId])
                return ReturnCodes.kBadState

            if (pdiskId not in self._readyPdisks):
                self._log("create-new-vdisk-failed").error("failed to create new vdisk '%s', pdisk '%s' is not in Ready state!",vdiskName,pdiskId)
                return ReturnCodes.kNotFound
            

        actionOptAndVal          = self.ACTION_OPT%"createvdisk"
        vdiskNameOptAndVal       = self.VDISK_NAME_OPT%vdiskName
        sizeOptAndVal            = self.SIZE_OPT%self.SIZE_OPT_MAX_VALUE
        raidOptAndVal            = self.RAID_OPT%raidLevel
        pdiskOptAndVal           = self.PDISK_OPT%self.PDISK_BETWEEN_IDS_DELIMITER.join(pdiskIdsList)
        diskCachePolicyOptAndVal = self.DISK_CACHE_POLICY_OPT%diskCachePolicy
        writePolicyOptAndVal     = self.WRITE_POLICY_OPT%writePolicy
        readPolicyOptAndVal      = self.READ_POLICY_OPT%readPolicy

        args = [self.INPUT_CONTROLLER_COMMAND_ELEMENT,actionOptAndVal,vdiskNameOptAndVal,sizeOptAndVal,raidOptAndVal,pdiskOptAndVal,diskCachePolicyOptAndVal,writePolicyOptAndVal,readPolicyOptAndVal]
        self.__setMappingInconsistent()
        outputDictionary,rc =  self._runConfigCommand(args,timer)
        
        if (rc != 0):
            # unexpected failure
            errorCode = self._getOutputErrorIfAny(outputDictionary)
            self._log("create-vdisk-fail").error("_createNewVdisk(name=%s,pdiskIdsList=%s,raidLevel=%s) failed (errorCode=%s)",vdiskName,pdiskIdsList,raidLevel,errorCode)
            return ReturnCodes.kGeneralError

        # vdisk was created, we need to update our mapping
        self._log("create-vdisk-success").debug1("successfully created new vdisk (name=%s,pdiskIdsList=%s,raidLevel=%s) ",vdiskName,pdiskIdsList,raidLevel)
        vdiskInfoList,rc = self._getVdiskInfo(timer,vdiskName=vdiskName)
        if ((rc != ReturnCodes.kOk) or (len(vdiskInfoList) != 1)):
            self._log("vdisk-not-found-unexpected").error("vdisk '%s' could not be found even though it was just successfully created",vdiskName)
            return ReturnCodes.kGeneralError

        vdiskStatusObj = vdiskInfoList[0]

        # update online pdisks
        for pdiskId in pdiskIdsList:
            pdiskStatus = self._readyPdisks.pop(pdiskId)
            pdiskStatus.vdiskName = vdiskName
            self._onlinePdisks[pdiskId] = pdiskStatus

        # update online vdisks
        vdiskStatusObj.pdiskIds = set(pdiskIdsList)
        self._onlineVdisks[vdiskName] = vdiskStatusObj
        self.__setMappingConsistent()

        # init vdisk
        vdiskId = vdiskStatusObj.vdiskId
        rc = self._fastInitVdisk(vdiskId,timer)
        if (rc == ReturnCodes.kOk):
            self._log("fast-init-success").debug2("fast-init (vdisk='%s',vdiskId='%s') succeeded!",vdiskName,vdiskId)
        else:
            self._log("fail-on-init").error("_createNewVdisk(vdisk=%s) failed due to failed fast-init of vdisk",vdiskName)
            return ReturnCodes.kGeneralError

        self._log("create-new-vdisk-success").debug1("successfully created and initialized vdisk '%s'! (vdiskId='%s')",vdiskName,vdiskId)
        return ReturnCodes.kOk


    def createVdisk (self,raidLevel,pdiskIdsList,vdiskName,autoInit=True,forceInit=False,diskCachePolicy=None,writePolicy=None,readPolicy=None):
        """
        Create a new vdisk if one with the same name doesn't exist.
        """

        timer = Timer(100) # TODO: get this from configuration later
        blockDevice = None
        pdiskIdsRequested = set(pdiskIdsList)
        try:
            # First, if mapping is inconsistent update mapping
            if self._mappingInconsistent:
                rc = self._updateVdiskPdiskMapping(timer)
                if (rc != ReturnCodes.kOk):
                    self._log("update-mapping-fail").error("createVdisk() failed while updating pdisk/vdisk mapping")
                    return blockDevice,ReturnCodes.kGeneralError

            if vdiskName in self._onlineVdisks:
                vdiskStatus = self._onlineVdisks[vdiskName]
                pdiskIds = vdiskStatus.pdiskIds
                blockDevice = vdiskStatus.blockDevice
            
                if ((pdiskIds == pdiskIdsRequested) and (not forceInit)):
                    self._log("vdisk-already-exist").debug2("vdisk %s already exist, no further work needed. createVdisk() succeeded.",vdiskName)
                    return blockDevice,ReturnCodes.kAlreadyExists

                else: # (pdiskIds != pdiskIdsRequested) or forceInit=True --> need to delete existing vdisk
                    self._log("pdisks-mismatch").debug2("a mismatch of pdisks for vdisk '%s' was found (requstedPdisks=%s currentPdisks=%s) or force-init was used",vdiskName,pdiskIdsRequested,pdiskIds)
                    if not autoInit:
                        self._log("need-delete-but-not-allowed").error("failed to create vdisk '%s'! autoInit==%s but a mismatch of pdisks was found (requstedPdisks=%s currentPdisks=%s)",vdiskName,autoInit,pdiskIdsRequested,pdiskIds)
                        return blockDevice,ReturnCodes.kGeneralError

                    rc = self._deleteVdisk(vdiskName,timer)
                    if (rc != ReturnCodes.kOk):
                        self._log("create-vdisk-failed").error("failed to create vdisk '%s'! failure to delete it (requstedPdisks=%s currentPdisks=%s)",pdiskIdsRequested,pdiskIds)
                        return blockDevice,rc
            

            # vdisk is not online
            if not autoInit:
                self._log("create-vdisk-failed").error("failed to create vdisk '%s'! autoInit==%s but vdisk still needs to be built",vdiskName,autoInit)
                return blockDevice,ReturnCodes.kGeneralError
            
            # let us build
            if (diskCachePolicy == None):
                diskCachePolicy = self.DISK_CACHE_POLICY_ENABELED
            if (writePolicy == None):
                writePolicy = self.WRITE_POLICY_WRITE_THROUGH
            if (readPolicy == None):
                readPolicy = self.READ_POLICY_ADAPTIVE_READ_AHEAD

            rc = self._createNewVdisk(raidLevel,pdiskIdsList,vdiskName,diskCachePolicy,writePolicy,readPolicy,timer)
            if (rc != ReturnCodes.kOk):
                # creation of vdisk failed
                self._log("fail-to-create-new").error("failed create new vdisk %s ",vdiskName)
                return blockDevice,rc
            
            blockDevice = self._onlineVdisks[vdiskName].blockDevice
            self._log("create-vdisk-success").debug1("createVdisk(raidLevel=%s,pdiskIdsList=%s,vdiskName=%s,autoInit=%s,forceInit=%s) succeeded!",raidLevel,pdiskIdsList,vdiskName,autoInit,forceInit)
            return blockDevice,ReturnCodes.kOk

        except Exception,e:
            self._log("create-vdisk-exception").error("createVdisk(raidLevel=%s,pdiskIdsList=%s,vdiskName=%s,autoInit=%s,forceInit=%s) faild! exception = '%s'",raidLevel,pdiskIdsList,vdiskName,autoInit,forceInit,e)
            return blockDevice,ReturnCodes.kGeneralError
        

    def getVdiskStatus (self,vdiskName):
        """
        Fetch the vdisk status info.
        """
        #WARNING : DO NOT USE IN MID ACTIVATION
        try:
            timer = Timer(60) # TODO: get this from configuration later
            if self._mappingInconsistent:
                rc = self._updateVdiskPdiskMapping(timer) # TODO: HOLY SHIT THIS HAS TO BE HANDELED WHEN GOING MULTYTHREAD 
                if (rc != ReturnCodes.kOk):
                    self._log("update-mapping-fail").error("getVdiskStatus() failed while updating pdisk/vdisk mapping")
                    return None,ReturnCodes.kGeneralError

            vdiskStatusDictionary = None
            if vdiskName in self._onlineVdisks:
                vdiskStatus = self._onlineVdisks[vdiskName]
                vdiskStatusDictionary = vdiskStatus.toDictionary()
                self._log("vdisk-status-found").debug2("found vdisk '%s' status %s",vdiskName,vdiskStatusDictionary)
                return vdiskStatusDictionary,ReturnCodes.kOk

            elif vdiskName in self._faultyVdisks:
                vdiskStatus = self._faultyVdisks[vdiskName]
                vdiskStatusDictionary = vdiskStatus.toDictionary()
                self._log("vdisk-status-found").debug2("found vdisk '%s' status %s (in faulty group)",vdiskName,vdiskStatusDictionary)
                return vdiskStatusDictionary,ReturnCodes.kOk

            else:
                self._log("vdisk-status-not-found").debug2("could not find vdisk '%s' status, vdisk appears to be not present",vdiskName)
                return None,ReturnCodes.kOk
        
        except Exception,e:
            self._log("get-vdisk-status-exception").error("getVdiskStatus(vdiskName=%s) faild! exception = '%s'",vdiskName,e)
            return None,ReturnCodes.kGeneralError


    # WARNING : DO NOT USE IN MID ACTIVATION
    def getPdiskStatus (self,pdiskId):
        """
        Fetch the pdisk status info.
        """
        try:
            timer = Timer(60)  # TODO: get this from configuration later
            if self._mappingInconsistent:
                rc = self._updateVdiskPdiskMapping(timer)
                if (rc != ReturnCodes.kOk):
                    self._log("update-mapping-fail").error("getPdiskStatus() failed while updating pdisk/vdisk mapping")
                    return None,ReturnCodes.kGeneralError

            if pdiskId in self._onlinePdisks:
                self._log("pdisk-status-found").debug2("found pdisk '%s' status in online pdisks group",pdiskId)
                return self._onlinePdisks[pdiskId].toDictionary(),ReturnCodes.kOk

            elif pdiskId in self._readyPdisks:
                self._log("pdisk-status-found").debug2("found pdisk '%s' status in ready pdisks group",pdiskId)
                return self._readyPdisks[pdiskId].toDictionary(),ReturnCodes.kOk

            elif pdiskId in self._foreignPdisks:
                self._log("pdisk-status-found").debug2("found pdisk '%s' status in foreign pdisks group",pdiskId)
                return self._foreignPdisks[pdiskId].toDictionary(),ReturnCodes.kOk

            elif pdiskId in self._faultyButPresentPdisks:
                self._log("pdisk-status-found").debug2("found pdisk '%s' status in faulty pdisks group",pdiskId)
                return self._faultyButPresentPdisks[pdiskId].toDictionary(),ReturnCodes.kOk

            else:
                self._log("pdisk-status-not-found").debug2("pdisk '%s' status was not found, pdisk apears to be not available",pdiskId)
                return None,ReturnCodes.kOk

        except Exception,e:
            self._log("get-pdisk-status-exception").error("getPdiskStatus(pdiskId=%s) faild! exception = '%s'",pdiskId,e)
            return None,ReturnCodes.kGeneralError


class H710RaidController(DellRaidController):
    """
    A class representing the Dell H710 raid controller.
    """

    def __init__ (self,name,internalId,logger):
        DellRaidController.__init__(self,name,internalId,G_NAME_GROUP_STORAGE_CONTROLLER_DELL_RAID_CONTROLLER_H710,logger)
        self._log("dell-h710-created").debug1("Dell raid Controller H710 object was created")

