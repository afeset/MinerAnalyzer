# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 

# Fans Enums
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansRedundancyStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansNoRedundancyReasonType

from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanDeviceStatusType

from a.infra.basic.return_codes import ReturnCodes
import a.sys.platform.manager.fans

#-----------------------------------------------------------------------------#
class FansSubsystem(a.sys.platform.manager.fans.FansSubsystem):        
    def __init__ (self, logger):
        a.sys.platform.manager.fans.FansSubsystem.__init__(self, logger)
        self._fansReporter  = None

    def initFansReporter (self, fansReporter):
        """ Inits the FansSource instance for this to get updated information from.
        """
        self._log("init-fans-reporter").debug1("fans-reporter initialized to %s", fansReporter)
        self._fansReporter = fansReporter


    def _createManagedUnit (self, name):
        """ To be implemented in platform-specific extension class """
        fan = FanUnit(self._log, name)
        fan.initFansReporter(self._fansReporter)
        return fan

    ################## LOGIC ###################

    def update (self):
        updatedFansStatus = a.sys.platform.manager.fans.FansSubsystem.newStatus()

        if self._fansReporter is None:
            self._log("update-data-no-fan-reporter").error("can't update data, no fan has been initialized yet")
        else:
            fansInformation = self._fansReporter.getData()    
            if fansInformation is not None:            
                self._updateFansStatus(updatedFansStatus, fansInformation.fansStatus)
            else:
                self._log("update-data").warning("did not get fan information from the fans-omreporer (got None instead)")

        self._updateData(updatedFansStatus)
        return (ReturnCodes.kOk, None)


    def _updateFansStatus (self, updatedFansStatus, fansStatus):
        if fansStatus is None:            
            return

        if fansStatus.hasRedundancyStatusRaw():
            updatedFansStatus.setRedundancyStatusRaw(fansStatus.redundancyStatusRaw)
            try:
                updatedFansStatus.setRedundancyStatus(self._redundancyStatusRawToEnum(fansStatus.redundancyStatusRaw))
            except:
                self._log("update-fans-status-status-unrecognized").debug1("cannot parse raw-status=%s", fansStatus.redundancyStatusRaw)


    def _redundancyStatusRawToEnum (self, redundancyStatusRaw):        
        return {"Full"      : FansRedundancyStatusType.kFull,
                "Lost"      : FansRedundancyStatusType.kLost,
                "Unknown"   : FansRedundancyStatusType.kUnknown}[redundancyStatusRaw]

#-----------------------------------------------------------------------------#
class FanUnit(a.sys.platform.manager.fans.FanUnit):
    """
    Gets the information Omreporters (FansSource).
    """

    def __init__ (self, logger, instanceName):
        a.sys.platform.manager.fans.FanUnit.__init__(self, logger, instanceName)
        self._fansReporter           = None

    def initFansReporter (self, fansReporter):
        """ Inits the FansSource instance for this to get updated information from.
        """
        self._log("init-fans-reporter").debug1("fans-reporter initialized to %s", fansReporter)
        self._fansReporter = fansReporter

    def update (self):
        updatedDeviceStatus = a.sys.platform.manager.fans.FanUnit.newDeviceStatus()

        if self._fansReporter is None:
            self._log("update-data-no-fan-reporter").error("can't update data, no fan has been initialized yet")
        else:
            fansInformation = self._fansReporter.getData()
            if fansInformation is not None:
                self._updateFanStatus(updatedDeviceStatus, self._getRelevantFanStatus(fansInformation.fanDeviceStatusList))
            else:
                self._log("update-data").warning("did not get fan information from the fans-omreporer (got None instead)")

        self._updateData(updatedDeviceStatus)
        return (ReturnCodes.kOk, None)


    def _getRelevantFanStatus (self, fanDeviceStatusList):
        myId = self._getId()
        if myId is None:
            self._log("get-relevant-device-information-no-id").error("the id (location) of this fan was not configured, cannot get relevant power-supply data")
            return None

        for deviceStatus in fanDeviceStatusList:
            if deviceStatus.hasProbeName() and deviceStatus.probeName == myId:
                return deviceStatus

        self._log("get-relevant-device-information-not-found").debug1("a device with this fan's id=%s was not found", myId)
        return None

    def _updateFanStatus (self, updatedDeviceStatus, deviceStatus):
        if deviceStatus is None:            
            updatedDeviceStatus.setStatus(FanDeviceStatusType.kNone)
            return
        
        updatedDeviceStatus.copySetFrom(deviceStatus)
        if deviceStatus.hasStatusRaw():
            try:
                updatedDeviceStatus.setStatus(self._deviceStatusRawToEnum(deviceStatus.statusRaw))
            except:
                self._log("update-fan-status").debug1("could not parse raw-status=%s", deviceStatus.statusRaw)


    def _deviceStatusRawToEnum (self, statusRaw):
        return {"Ok"        : FanDeviceStatusType.kOk,
                "Critical"  : FanDeviceStatusType.kCritical,
                "Unknown"   : FanDeviceStatusType.kUnknown}[statusRaw]
        

