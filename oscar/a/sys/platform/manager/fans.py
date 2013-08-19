# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 

import threading

# Fans Enums
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansRedundancyStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansNoRedundancyReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansForceOperationalStatusType

from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanDeviceStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanForceOperationalStatusType

# Fans Blinky Data
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fans_data_gen # FansData
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.status.status_oper_data_gen # StatusOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.alarm.alarm_oper_data_gen # AlarmOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.simulation.simulation_data_gen

# Fan Blinky Data
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.fan_data_gen #FanData
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.status.status_oper_data_gen #StatusOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.alarm.alarm_oper_data_gen #AlarmOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.device_data_gen #DeviceData
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.status.status_oper_data_gen #StatusOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.simulation.simulation_data_gen


# User logs
import a.api.user_log.msg.platform
import a.infra.process

from a.infra.basic.return_codes import ReturnCodes
import a.infra.subprocess
import a.infra.time.monotonic_clock
import a.infra.time.elapsed_timer

# TODO(shmulika): need to change name of file, from component_base to component_base or unit_base...
import a.sys.platform.manager.component


class ConfigurationError(Exception):
    def __init__ (self, errMessage):
        Exception.__init__(self)
        self.errMessage = errMessage

    def getErrorMessage (self):
        return self.errMessage


#-----------------------------------------------------------------------------#
class FansSubsystem(a.sys.platform.manager.component.Component):
    """
    Represents the managed fans in the system.
    It has its own configuration and oper data.
    It is also responsible for getting its information from the appropriate sources (extension dependent)
    """
    def __init__ (self, logger):
        a.sys.platform.manager.component.Component.__init__(self, logger, "fans-subsystem")        
        
        ## CONFIG ##
        self._configErrorMsgFunctor = lambda x: self._log("config-error-msg").debug1("error-msg-functor not set yet, called with message: %s", x)

        self._configLock = threading.RLock()
        self._runningData = self.newConfigurationData()
        self._candidateData = self.newConfigurationData()
        self._changedData = self.newConfigurationData()

        self._runningSimulationData = self.newSimulationData()
        self._candidateSimulationData = self.newSimulationData()
        self._changedSimulationData = self.newSimulationData()

        ## LIST OF MANAGED UNITS ##
        self._candidateManagedUnits = None
        self._runningManagedUnits = {}

        ## OPER ##
        self._operLock = threading.RLock()
        self._status = self.defaultStatus()
        self._alarm  = self.defaultAlarm()        

        # the last actual status/alarm are saved even when the component is disabled, for comparison with new values after enabling...
        self._lastActualStatus = self.defaultStatus()
        self._lastActualAlarm  = self.defaultAlarm()
        self._wasDisabled = False
        
    ################## MANAGED UNITS ###################

    def _createManagedUnit (self, name):
        """ To be implemented in platform-specific extension class """
        __pychecker__ = "unusednames=name"
        return None


    def createManagedUnit (self, name):
        if self._candidateManagedUnits is None:
            self._log("create-managed-unit-not-in-transaction").error("attempt to create a managed unit not during configuration transaction - retruning None")
            return None

        if name in self._candidateManagedUnits:
            self._log("create-managed-unit-already-exists").error("attempt to create an already existing managed unit - returning None")
            return None

        managedUnit = self._createManagedUnit(name)
        if managedUnit is None:
            self._log("create-managed-unit-created-none").error("platform-specific creation method was not implemented, or returned None - returning None")
            return None

        self._candidateManagedUnits[name] = managedUnit
        self._log("create-managed-unit").debug1("managed unit %s was created and added to candidates", managedUnit)
        return managedUnit


    def getManagedUnit (self, name):
        with self._configLock:
            if name in self._runningManagedUnits:
                managedUnit = self._runningManagedUnits[name]
                self._log("get-managed-unit").debug2("returning running managed unit %s of name %s", managedUnit, name)
                return managedUnit
            else:
                self._log("get-managed-unit-not-exist").error("running managed unit of name %s does not exist - returning None", managedUnit)
                return None
            
    def getManagedUnits (self):
        with self._configLock:
            managedUnits = self._runningManagedUnits.values()
        return managedUnits

    ################## MODULE CONFIGURATION ###################

    def configStartTransaction (self):        
        with self._configLock:            
            self._configStartTransaction()
            for managedUnit in self._runningManagedUnits.values():
                managedUnit._configStartTransaction()

        return ReturnCodes.kOk


    def configPreparePrivateAfter (self):
        self._log("config-prepare-private-after").debug2("checking configuration validity")                        
        try:
            self._configPreparePrivateAfter()
            for managedUnit in self._runningManagedUnits.values():
                managedUnit._configPreparePrivateAfter()

        except ConfigurationError as configurationError:
            self._log("config-prepare-private-after-configuration-invalid").error("configuration invalid: %s", configurationError.getErrorMessage())
            self._configErrorMsgFunctor(configurationError.getErrorMessage())
            return ReturnCodes.kGeneralError
        else:
            self._log("config-prepare-private-after-done").debug1("candidate configuration is valid")                
            return ReturnCodes.kOk


    def configPreparePublicAfter (self):
        self._log("config-prepare-public-after").debug2("doing nothing - already checked data in private")       
        try:
            self._configPreparePublicAfter()
            for managedUnit in self._runningManagedUnits.values():
                managedUnit._configPreparePublicAfter()

        except ConfigurationError as configurationError:
            self._log("config-prepare-private-after-configuration-invalid").error("configuration invalid: %s", configurationError.getErrorMessage())
            self._configErrorMsgFunctor(configurationError.getErrorMessage())
            return ReturnCodes.kGeneralError
        else:
            self._log("config-prepare-private-after-done").debug1("candidate configuration is valid")                
            return ReturnCodes.kOk


    def configAbortTransaction (self):
        self._log("config-abort-transaction").debug2("configuration transaction aborted")
        with self._configLock:
            self._configAbortTransaction()            
            for managedUnit in self._runningManagedUnits.values():
                managedUnit._configAbortTransaction()

        return ReturnCodes.kOk


    def configCommitTransaction (self):        
        with self._configLock:
            self._configCommitTransaction() 
            for managedUnit in self._runningManagedUnits.values():
                managedUnit._configCommitTransaction()           

        self._log("config-commit-transaction").debug2("configuration transaction commited")
        self._wasConfigured = True
        return ReturnCodes.kOk


    ################## CONFIGURATION ###################

    def setConfigMsgFunctor (self, functor):
        """ Sets the config error message functor - which will be used to report configuration error messages """
        def logAndCallFunctor (message):
            self._log("config-error-msg").debug2("error-msg-functor called with message: %s", message)
            functor(message)

        self._log("set-config-msg-functor").debug2("setting error msg functor to given functor %s", functor)
        self._configErrorMsgFunctor = logAndCallFunctor


    def setConfigErrorStr(self, errorMsg):
        self._configErrorMsgFunctor(errorMsg)


    def _configStartTransaction (self):
        self._log("config-start-transaction").debug2("configuration transaction started")
        self._candidateData.copyFrom(self._runningData)
        self._changedData = self.newConfigurationData()
        self._candidateSimulationData.copyFrom(self._runningSimulationData)
        self._changedSimulationData = self.newSimulationData()
        self._candidateManagedUnits = self._runningManagedUnits.copy()                    


    def preparePrivateData (self, blinkyData):        
        self._log("prepare-private-data").debug2("got candidate data = %s", blinkyData)
        self.copySetConfigurationData(self._candidateData, blinkyData)
        self._changedData.copyFrom(blinkyData)
        return ReturnCodes.kOk

    def preparePrivateSimulationData (self, blinkyData):        
        self._log("prepare-private-simulation-data").debug2("got candidate simulation data = %s", blinkyData)
        self.copySetSimulationData(self._candidateSimulationData, blinkyData)
        self._changedSimulationData.copyFrom(blinkyData)
        return ReturnCodes.kOk


    def _configPreparePrivateAfter (self):
        self._log("config-prepare-private-after").debug2("checking configuration validity")
        self._checkCandidateConfigurationData(self._candidateData)
        self._checkCandidateSimulationData(self._candidateData)


    def _configPreparePublicAfter (self):
        pass        


    def _configAbortTransaction (self):
        self._candidateData = self.newConfigurationData()
        self._changedData = self.newConfigurationData()
        self._candidateSimulationData = self.newSimulationData()
        self._changedSimulationData = self.newSimulationData()
        self._candidateManagedUnits = None


    def _configCommitTransaction (self):
        self._runningData.copyFrom(self._candidateData)
        self._applyRunningConfigurationData(self._runningData, self._changedData)
        self._runningSimulationData.copyFrom(self._candidateSimulationData)
        self._applyRunningSimulationData(self._runningSimulationData, self._changedSimulationData)
        self._runningManagedUnits = self._candidateManagedUnits
        self._candidateManagedUnits = None

    
    ################## OPER & GETTERS ###################    

    def getObjStatusOperData (self, dpTrxContext, operData):        
        operData.copyRequestedFrom(self.getStatus())
        self._log("get-obj-status-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
        return ReturnCodes.kOk


    def getObjAlarmOperData (self, dpTrxContext, operData):        
        operData.copyRequestedFrom(self.getAlarm())
        self._log("get-obj-alarm-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
        return ReturnCodes.kOk


    def getStatus (self):
        #TODO(shmulika): when Blinky comes, this will become an oper request
        with self._operLock:
            statusCopy = self.defaultStatus()
            statusCopy.copySetFrom(self._status)
        return statusCopy


    def getAlarm (self):
        #TODO(shmulika): when Blinky comes, this will become an oper request
        with self._operLock:
            alarmCopy  = self.defaultAlarm()
            alarmCopy.copySetFrom(self._alarm)
        return alarmCopy

    ###### SPECIFIC CONFIGURATION CHECKERS & APPLIERS #####

    def _checkCandidateConfigurationData (self, candiadteData):
        """ To be implemented by extension-class
        """
        __pychecker__ = "unusednames=candiadteData"
        # nothing to check about mute-reporting
        pass

    def _checkCandidateSimulationData (self, candiadteData):
        """ To be implemented by extension-class
        """
        __pychecker__ = "unusednames=candiadteData"
        # nothing to check about mute-reporting
        pass

    def _applyRunningConfigurationData (self, runningData, changedData):
        """ To be implemented by extension-class
        """
        __pychecker__ = "unusednames=runningData,changedData"
        #TODO(shmulika): apply mute-reporting if necessary
        pass

    def _applyRunningSimulationData (self, runningData, changedData):
        """ To be implemented by extension-class
        """
        __pychecker__ = "unusednames=runningData,changedData"
        #TODO(shmulika): apply mute-reporting if necessary
        pass

    ################## LOGIC ###################

    def updateOrClear (self, enabled = True):
        """
        If enabled, gets updated information from relevant sources and updates the data.
        If disabled, clears the information (set unknown status instead)
        """
        if not enabled or not self._runningData.enabled:            
            for managedUnit in self.getManagedUnits():
                managedUnit.updateOrClear(enabled = False)

            with self._operLock:
                if not self._wasDisabled:
                    self._lastActualStatus = self._status
                    self._lastActualAlarm  = self._alarm 
                    self._wasDisabled = True

                self._status = self.defaultStatus()
                self._alarm = self.defaultAlarm()
                
            return
        
        for managedUnit in self.getManagedUnits():
            managedUnit.updateOrClear(enabled = True)

        self.update()


    def _updateData (self, newData):
        """
        Called to by the update() method with updated data
        """       
        # update all the managed units
        for managedUnit in self.getManagedUnits():
            managedUnit.update()
         
        # derive the new status & alarm of the fans
        newStatus = self.newStatus()
        newAlarm = self.newAlarm()

        self._deriveOperationalStatus(newData, newStatus)
        self._deriveAlarmIfNotMute(newStatus, newAlarm)
        
        fullStatus = self.defaultStatus()
        fullStatus.copySetFrom(newStatus)

        fullAlarm  = self.defaultAlarm()
        fullAlarm.copySetFrom(newAlarm)

        self._logChangeStatus(self._lastActualStatus, fullStatus)
        self._logChangeAlarm(self._lastActualAlarm, fullAlarm)

        with self._operLock:
            self._status = fullStatus
            self._alarm = fullAlarm
            self._lastActualStatus = self._status
            self._lastActualAlarm  = self._alarm 
            self._wasDisabled = False


    def _deriveOperationalStatus (self, fansStatus, newStatus):
        """ derives operational status according to redundancy status """
        newStatus.copyFrom(fansStatus)        

        # check if there's a simulation configured
        with self._configLock:
            simulationData = self._runningSimulationData

        if simulationData.hasForceOperationalStatus() and simulationData.forceOperationalStatus != FansForceOperationalStatusType.kNone:
            self._log("derive-operational-status").debug1("operational status was simulated to %s", simulationData.forceOperationalStatus.getDisplayName())
            if simulationData.forceOperationalStatus == FansForceOperationalStatusType.kUp:
                newStatus.setOperationalStatus(FansOperationalStatusType.kUp)
                newStatus.setOperationalStatusReason(FansOperationalStatusReasonType.kSimulation)

            elif simulationData.forceOperationalStatus == FansForceOperationalStatusType.kDegraded:
                newStatus.setOperationalStatus(FansOperationalStatusType.kDegraded)
                newStatus.setOperationalStatusReason(FansOperationalStatusReasonType.kSimulation)

            elif simulationData.forceOperationalStatus == FansForceOperationalStatusType.kDown:
                newStatus.setOperationalStatus(FansOperationalStatusType.kDown)
                newStatus.setOperationalStatusReason(FansOperationalStatusReasonType.kSimulation)

            else:
                self._log("derive-operational-status-failed").error("could not derive operational status from the simulated status=%s", simulationData.forceOperationalStatus.getDisplayName())
            return

        if not newStatus.hasRedundancyStatus():
            self._log("derive-operational-status").debug1("no fans status was generated, can't derive operational status")
            return

        if newStatus.redundancyStatus == FansRedundancyStatusType.kFull:
            # all is good 
            newStatus.setOperationalStatus(FansOperationalStatusType.kUp)
            newStatus.setOperationalStatusReason(FansOperationalStatusReasonType.kRedundant)

        elif newStatus.redundancyStatus == FansRedundancyStatusType.kLost:
            # redundancy is lost
            newStatus.setOperationalStatus(FansOperationalStatusType.kDegraded)
            newStatus.setOperationalStatusReason(FansOperationalStatusReasonType.kNoRedundancy)

        #TODO(shmulika): check if I can derive the DOWN situation (where seemingly all fans failed)
        else:
            self._log("derive-operational-status-failed").error("could not derive operational status from the fans status=%s", newStatus)


    def _deriveAlarmIfNotMute (self, fansStatus, fansAlarm):
        """ calls deriveAlarm if mute-reporting was not configured
        """
        # no need to use lock here, only needing a single boolean variable (reconsider if becomes more than that)
        if not self._runningData.muteReporting:
            self._deriveAlarm(fansStatus, fansAlarm)


    def _deriveAlarm (self, fansStatus, fansAlarm):
        if not fansStatus.hasOperationalStatus():
            self._log("derive-operational-status").debug1("no operational status was generated, can't derive alarms")
            return

        if fansStatus.operationalStatus == FansOperationalStatusType.kUp:
            fansAlarm.setNoRedundancy(False)
            fansAlarm.setNoRedundancyReason(FansNoRedundancyReasonType.kNone)

        elif fansStatus.operationalStatus == FansOperationalStatusType.kDegraded:
            fansAlarm.setNoRedundancy(True)
            fansAlarm.setNoRedundancyReason(FansNoRedundancyReasonType.kNoRedundancy)

        elif fansStatus.operationalStatus == FansOperationalStatusType.kDown:
            fansAlarm.setNoRedundancy(True)
            fansAlarm.setNoRedundancyReason(FansNoRedundancyReasonType.kNoRedundancy)
        else:
            self._log("derive-alarm-failed").error("could not derive alarm from the fans status=%s", fansStatus)


    def _logChangeStatus (self, oldStatus, newStatus):
        #TODO(shmulika): implement this with user log, and difference tracking
        self._log("log-change-status").debug2("old status was %s, new status is %s", oldStatus, newStatus)
        shouldLogChange = False

        if oldStatus.operationalStatus == FansOperationalStatusType.kUnknown:
            if newStatus.operationalStatus == FansOperationalStatusType.kDegraded:
                shouldLogChange = True
        else:
            if newStatus.operationalStatus != oldStatus.operationalStatus:
                shouldLogChange = True

        if shouldLogChange:
            a.infra.process.logUserMessage(a.api.user_log.msg.platform.FansOperationalStatusChanged(self._operationalStatusToString(newStatus.operationalStatus)))

    # TODO(shmulika): this won't be needed when Blinky supports automatic conversion from enum to confd string
    def _operationalStatusToString (self, operationalStatus):
        if operationalStatus == FansOperationalStatusType.kUp:
            return "up"
        elif operationalStatus == FansOperationalStatusType.kDegraded:
            return "degraded"
        else:
            return "unknown"


    def _logChangeAlarm (self, oldAlarm, newAlarm):
        #TODO(shmulika): implement this with user log, and difference tracking
        self._log("log-change-alarm").debug2("old alarm was %s, new alarm is %s", oldAlarm, newAlarm)


    ################## SPECIFIC DATA TYPES ###################

    @classmethod
    def newConfigurationData (cls):
        __pychecker__ = "unusednames=cls"
        return a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fans_data_gen.FansData()

    @classmethod
    def newSimulationData (cls):
        __pychecker__ = "unusednames=cls"
        return a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.simulation.simulation_data_gen.SimulationData()        

    @classmethod
    def newStatus (cls):
        __pychecker__ = "unusednames=cls"
        status = a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.status.status_oper_data_gen.StatusOperData()
        status.setAllRequested()
        return status

    @classmethod
    def defaultStatus (cls):
        status = cls.newStatus()
        status.setRedundancyStatus(FansRedundancyStatusType.kUnknown)
        status.setRedundancyStatusRaw("unknown")
        status.setOperationalStatus(FansOperationalStatusType.kUnknown)
        status.setOperationalStatusReason(FansOperationalStatusReasonType.kUnknown)
        return status

    @classmethod
    def newAlarm (cls):
        __pychecker__ = "unusednames=cls"
        alarm = a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.alarm.alarm_oper_data_gen.AlarmOperData()
        alarm.setAllRequested()
        return alarm

    @classmethod
    def defaultAlarm (cls):
        alarm = cls.newAlarm()
        alarm.setNoRedundancy(False)
        alarm.setNoRedundancyReason(FansNoRedundancyReasonType.kNone)
        return alarm


    def copySetConfigurationData (self, dest, source):
        if source.hasMuteReporting():
            dest.muteReporting = source.muteReporting
            dest.setHasMuteReporting()

        if source.hasEnabled():
            dest.enabled = source.enabled
            dest.setHasEnabled()

    def copySetSimulationData (self, dest, source):
        if source.hasForceOperationalStatus():
            dest.forceOperationalStatus = source.forceOperationalStatus
            dest.setHasForceOperationalStatus()

#-----------------------------------------------------------------------------#
class FanUnit(a.sys.platform.manager.component.Component):
    """
    Represents a managed fan element in the system.
    It has its own configuration and oper data.
    It is also responsible for getting its information from the appropriate sources (extension dependent)
    """
    
    def __init__ (self, logger, instanceName):
        a.sys.platform.manager.component.Component.__init__ (self, logger, instanceName)
        self._unitName = instanceName

        ## CONFIG ##
        self._configErrorMsgFunctor = lambda x: self._log("config-error-msg").debug1("error-msg-functor not set yet, called with message: %s", x)

        self._configLock = threading.RLock() #TODO(shmulika): remove this later
        self._runningData = self.newConfigurationData()
        self._runningDeviceData = self.newDeviceConfigurationData()        
        self._runningSimulationData = self.newSimulationConfigurationData()        
        self._candidateData = self.newConfigurationData()
        self._changedData = self.newConfigurationData()
        self._candidateDeviceData = self.newDeviceConfigurationData()
        self._changedDeviceData = self.newDeviceConfigurationData()
        self._candidateSimulationData = self.newSimulationConfigurationData()
        self._changedSimulationData = self.newSimulationConfigurationData()

        ## OPER ##
        self._operLock = threading.RLock() #TODO(shmulika): remove this later
        self._status = self.defaultStatus()
        self._alarm  = self.defaultAlarm()
        self._deviceStatus = self.newDeviceStatus()

        # the last actual status/alarm are saved even when the component is disabled, for comparison with new values after enabling...
        self._lastActualStatus = self.defaultStatus()
        self._lastActualAlarm  = self.defaultAlarm()
        self._wasDisabled = False


    ################## CONFIGURATION ###################    

    def setConfigMsgFunctor (self, functor):
        """ Sets the config error message functor - which will be used to report configuration error messages """
        def logAndCallFunctor (message):
            self._log("config-error-msg").debug2("error-msg-functor called with message: %s", message)
            functor(message)

        self._log("set-config-msg-functor").debug2("setting error msg functor to given functor %s", functor)
        self._configErrorMsgFunctor = logAndCallFunctor


    def setConfigErrorStr(self, errorMsg):
        self._configErrorMsgFunctor(errorMsg)


    def _configStartTransaction (self):
        self._log("config-start-transaction").debug2("configuration transaction started")
        self._candidateData.copyFrom(self._runningData)
        self._changedData = self.newConfigurationData()
        self._candidateDeviceData.copyFrom(self._runningDeviceData)
        self._changedDeviceData = self.newDeviceConfigurationData()
        self._candidateSimulationData.copyFrom(self._runningSimulationData)
        self._changedSimulationData = self.newSimulationConfigurationData()


    def preparePrivateData (self, blinkyData):        
        self._log("prepare-private-data").debug2("got candidate data = %s", blinkyData)
        self.copySetConfigurationData(self._candidateData, blinkyData)
        self._changedData.copyFrom(blinkyData)
        return ReturnCodes.kOk

    def preparePrivateDeviceData (self, blinkyDeviceData):        
        self._log("prepare-private-device-data").debug2("got candidate device-data = %s", blinkyDeviceData)
        self.copySetDeviceConfigurationData(self._candidateDeviceData, blinkyDeviceData)
        self._changedDeviceData.copyFrom(blinkyDeviceData)
        return ReturnCodes.kOk

    def preparePrivateSimulationData(self, blinkySimulationData):
        self._log("prepare-private-simluation-data").debug2("got candidate simulation-data = %s", blinkySimulationData)
        self.copySetSimulationConfigurationData(self._candidateSimulationData, blinkySimulationData)
        self._changedSimulationData.copyFrom(blinkySimulationData)
        return ReturnCodes.kOk


    def _configPreparePrivateAfter (self):
        self._log("config-prepare-private-after").debug2("checking configuration validity")
        self._checkCandidateConfigurationData(self._candidateData)
        self._checkCandidateDeviceConfigurationData(self._changedDeviceData)
        self._checkCandidateSimulationConfigurationData(self._changedSimulationData)


    def _configPreparePublicAfter (self):
        pass        


    def _configAbortTransaction (self):
        self._candidateData = self.newConfigurationData()
        self._changedData = self.newConfigurationData()
        self._candidateDeviceData = self.newDeviceConfigurationData()
        self._candidateSimulationData = self.newSimulationConfigurationData()


    def _configCommitTransaction (self):
        with self._configLock:
            self._runningData.copyFrom(self._candidateData)
            self._applyRunningConfigurationData(self._runningData, self._changedData)
            self._runningDeviceData.copyFrom(self._candidateDeviceData)
            self._applyRunningDeviceConfigurationData(self._runningDeviceData, self._changedDeviceData)
            self._runningSimulationData.copyFrom(self._candidateSimulationData)
            self._applyRunningSimulationConfigurationData(self._runningSimulationData, self._changedSimulationData)

    ################## OPER & GETTERS ###################    

    def getObjStatusOperData (self, dpTrxContext, operData):        
        operData.copyRequestedFrom(self.getStatus())
        self._log("get-obj-status-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
        return ReturnCodes.kOk


    def getObjAlarmOperData (self, dpTrxContext, operData):        
        operData.copyRequestedFrom(self.getAlarm())
        self._log("get-obj-alarm-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
        return ReturnCodes.kOk


    def getObjDeviceStatusOperData (self, dpTrxContext, operData):        
        operData.copyRequestedFrom(self.getDeviceStatus())
        self._log("get-obj-device-status-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
        return ReturnCodes.kOk


    def getStatus (self):
        #TODO(shmulika): when Blinky comes, this will become an oper request
        with self._operLock:
            statusCopy = self.defaultStatus()
            statusCopy.copySetFrom(self._status)
        return statusCopy


    def getAlarm (self):
        #TODO(shmulika): when Blinky comes, this will become an oper request
        with self._operLock:
            alarmCopy  = self.defaultAlarm()
            alarmCopy.copySetFrom(self._alarm)
        return alarmCopy


    def getDeviceStatus (self):
        #TODO(shmulika): when Blinky comes, this will become an oper request
        with self._operLock:
            deviceStatusCopy  = self.defaultDeviceStatus()
            deviceStatusCopy.copySetFrom(self._deviceStatus)
        return deviceStatusCopy


    ###### SPECIFIC CONFIGURATION CHECKERS & APPLIERS #####

    def _checkCandidateConfigurationData (self, candidateData):
        """ To be implemented by extension-class
        """
        if self._runningData.hasName() and candidateData.name != self._runningData.name:
            raise ConfigurationError("cannot change name of element, list is static")


    def _applyRunningConfigurationData (self, runningData, changedData):
        """ To be implemented by extension-class
        """
        __pychecker__ = "unusednames=runningData,changedData"
        #TODO(shmulika): apply mute-reporting if necessary
        pass


    def _checkCandidateDeviceConfigurationData (self, candidateDeviceData):
        """ To be implemented by extension-class
        """
        __pychecker__ = "unusednames=candidateDeviceData"
        pass


    def _checkCandidateSimulationConfigurationData (self, candidateSimulationData):
        """ To be implemented by extension-class
        """
        __pychecker__ = "unusednames=candidateSimulationData"
        pass

    def _applyRunningDeviceConfigurationData (self, runningDeviceData, changedDeviceData):
        """ To be implemented by extension-class
        """
        __pychecker__ = "unusednames=runningDeviceData,changedDeviceData"
        pass

    def _applyRunningSimulationConfigurationData (self, runningSimulationData, changedSimulationData):
        """ To be implemented by extension-class
        """
        __pychecker__ = "unusednames=runningSimulationData,changedSimulationData"
        pass

    ################## LOGIC ###################

    def updateOrClear (self, enabled = True):
        """
        If enabled, gets updated information from relevant sources and updates the data.
        If disabled, clears the information (set unknown status instead)
        """
        if not enabled:
            with self._operLock:
                if not self._wasDisabled:
                    self._lastActualStatus = self._status
                    self._lastActualAlarm  = self._alarm 
                    self._wasDisabled = True

                self._status = self.defaultStatus()
                self._alarm = self.defaultAlarm()
                self._deviceStatus = self.defaultDeviceStatus()
            return

        self.update()


    def _updateData (self, newData):
        """
        Called to by the update() method with updated data
        """        
        # derive the new status & alarm of the fans
        newStatus = self.newStatus()
        newAlarm = self.newAlarm()

        self._deriveOperationalStatus(newData, newStatus)
        self._deriveLocationStatus(newStatus)
        self._deriveAlarmIfNotMute(newStatus, newAlarm)
        fullStatus = self.defaultStatus()
        fullStatus.copySetFrom(newStatus)

        fullAlarm  = self.defaultAlarm()
        fullAlarm.copySetFrom(newAlarm)
        
        self._logChangeStatus(self._lastActualStatus, fullStatus)
        self._logChangeAlarm(self._lastActualAlarm, fullAlarm)

        with self._operLock:
            self._status = fullStatus
            self._alarm = fullAlarm
            self._deviceStatus = newData
            self._lastActualStatus = self._status
            self._lastActualAlarm  = self._alarm 
            self._wasDisabled = False


    def _deriveLocationStatus (self, newStatus):
        # just take the location from the configuration
        with self._configLock:
            configurationData = self._runningData

        if configurationData.hasLocation():
            newStatus.setLocation(configurationData.location)


    def _deriveOperationalStatus (self, deviceStatus, newStatus):
        # check if there's a simulation configured
        with self._configLock:
            simulationData = self._runningSimulationData

        if simulationData.hasForceOperationalStatus() and simulationData.forceOperationalStatus != FanForceOperationalStatusType.kNone:
            self._log("derive-operational-status").debug1("operational status was simulated to %s", simulationData.forceOperationalStatus.getDisplayName())
            if simulationData.forceOperationalStatus == FanForceOperationalStatusType.kUp:
                newStatus.setOperationalStatus(FanOperationalStatusType.kUp)
                newStatus.setOperationalStatusReason(FanOperationalStatusReasonType.kSimulation)

            elif simulationData.forceOperationalStatus == FanForceOperationalStatusType.kDown:
                newStatus.setOperationalStatus(FanOperationalStatusType.kDown)
                newStatus.setOperationalStatusReason(FanOperationalStatusReasonType.kSimulation)

            else:
                self._log("derive-operational-status-failed").error("could not derive operational status from the simulated status=%s", simulationData.forceOperationalStatus.getDisplayName())
            return

        if not deviceStatus.hasStatus():
            self._log("derive-operational-status").debug1("no device status was determined, can't derive operational status")
            return

        if deviceStatus.status == FanDeviceStatusType.kOk:
            # device status is ok
            newStatus.setOperationalStatus(FanOperationalStatusType.kUp)
            newStatus.setOperationalStatusReason(FanOperationalStatusReasonType.kNone)

        elif deviceStatus.status == FanDeviceStatusType.kCritical:
            # device status is critical
            newStatus.setOperationalStatus(FanOperationalStatusType.kDown)
            newStatus.setOperationalStatusReason(FanOperationalStatusReasonType.kUnknown)

#            if self._checkIfLowRpm(deviceStatus):
#                newStatus.setOperationalStatusReason(FanOperationalStatusReasonType.kLowRpm)
#            else:
#                newStatus.setOperationalStatusReason(FanOperationalStatusReasonType.kUnknown)

        elif deviceStatus.status == FanDeviceStatusType.kNone:
            # device status is absent
            newStatus.setOperationalStatus(FanOperationalStatusType.kDown)
            newStatus.setOperationalStatusReason(FanOperationalStatusReasonType.kAbsent)

        elif deviceStatus.status == FanDeviceStatusType.kUnknown:
            # we decided that this situation will be considered as "absent"
            newStatus.setOperationalStatus(FanOperationalStatusType.kDown)
            newStatus.setOperationalStatusReason(FanOperationalStatusReasonType.kAbsent)

        else:
            self._log("derive-operational-status-failed").error("could not derive operational status from the device status=%s", deviceStatus)


    def _deriveAlarmIfNotMute (self, status, alarm):
        """ calls deriveAlarm if mute-reporting was not configured
        """
        # no need to use lock here, only needing a single boolean variable (reconsider if becomes more than that)
        if not self._runningData.muteReporting:
            self._deriveAlarm(status, alarm)


    def _deriveAlarm (self, status, alarm):
        if not status.hasOperationalStatus():
            self._log("derive-operational-status").debug1("no operational status was determined, can't derive alarms")
            return

        if status.operationalStatus == FanOperationalStatusType.kUp:
            # the fan is ok
            alarm.setFanFailure(False)
            alarm.setFanFailureReason(FanFailureReasonType.kNone)

        elif status.operationalStatus == FanOperationalStatusType.kDown:
            # the fan failed
            alarm.setFanFailure(True)

            # try to understand why it failed
            if status.operationalStatusReason == FanOperationalStatusReasonType.kLowRpm:
                alarm.setFanFailureReason(FanFailureReasonType.kLowRpm)
            elif status.operationalStatusReason == FanOperationalStatusReasonType.kAbsent:
                alarm.setFanFailureReason(FanFailureReasonType.kAbsent)
            else:
                alarm.setFanFailureReason(FanFailureReasonType.kUnknown)

        else:
            self._log("derive-alarm-failed").error("could not derive alarm from the fan operational status=%s", status)

#    def _checkIfLowRpm (self, deviceStatus):
#        """ Returns True if currentRpm is lower than the minimum error rpm
#            Falue if not, or cannot determine.
#         """
#        if deviceStatus.hasCurrentRpm() and deviceStatus.hasMinimumErrorRpm():
#            try:
#                # TODO(shmulika): this is wrong!! 
#                # the extraction of the values should be in the specific extension class (not in the base class)
#                # extracted values should be placed in a "parsed" field, and original kept in a "raw" field.
#                # if the values were parsed by the extension, the comparison should be kept here, unless
#                # we want the extension to decide on the final "low-rpm" status.... talk to gaash
#                matches = re.search("^(?P<rpm>\d+)\s*RPM$", deviceStatus.currentRpm)
#                currentRpm = int(matches.group('rpm'))
#                matches = re.search("^(?P<rpm>\d+)\s*RPM$", deviceStatus.minimumErrorRpm)
#                minimumErrorRpm = int(matches.group('rpm'))
#                return currentRpm <= minimumErrorRpm
#            except:
#                return False
#        return False


    def _logChangeStatus (self, oldStatus, newStatus):
        #TODO(shmulika): implement this with user log, and difference tracking
        self._log("log-change-status").debug2("old status was %s, new status is %s", oldStatus, newStatus)
        shouldLogChange = False

        if oldStatus.operationalStatus == FanOperationalStatusType.kUnknown:
            if newStatus.operationalStatus == FanOperationalStatusType.kDown:
                shouldLogChange = True
        else:
            if newStatus.operationalStatus != oldStatus.operationalStatus:
                shouldLogChange = True

        if shouldLogChange:
            location = self._returnLocationOrNone(self._getLocation())
            statusString = newStatus.operationalStatus.getDisplayName()
            a.infra.process.logUserMessage(a.api.user_log.msg.platform.FanOperationalStatusChanged(self._unitName, location, statusString))


    def _returnLocationOrNone (self, locationString):
        if locationString is None:
            return "unknown"
        else:
            return locationString

#    # TODO(shmulika): this won't be needed when Blinky supports automatic conversion from enum to confd string
#    def _operationalStatusToString (self, operationalStatus):
#        if operationalStatus == FanOperationalStatusType.kUp:
#            return "up"
#        elif operationalStatus == FanOperationalStatusType.kDown:
#            return "down"
#        else:
#            return "unknown"


    def _logChangeAlarm (self, oldAlarm, newAlarm):
        #TODO(shmulika): implement this with user log, and difference tracking
        self._log("log-change-alarm").debug2("old alarm was %s, new alarm is %s", oldAlarm, newAlarm)


    def _getId (self):
        with self._configLock:
            if self._runningDeviceData.hasId():
                return self._runningDeviceData.id
            else:                
                return None


    def _getLocation (self):
        with self._configLock:
            configurationData = self._runningData

        if configurationData.hasLocation():
            return configurationData.location
        else:
            return None

    ################## SPECIFIC DATA TYPES ###################

    @classmethod
    def newConfigurationData (cls):
        __pychecker__ = "unusednames=cls"
        return a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.fan_data_gen.FanData()

    @classmethod
    def newDeviceConfigurationData (cls):
        __pychecker__ = "unusednames=cls"
        data = a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.device_data_gen.DeviceData()        
        return data

    @classmethod
    def newSimulationConfigurationData (cls):
        __pychecker__ = "unusednames=cls"
        data = a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.simulation.simulation_data_gen.SimulationData()
        return data

    def copySetDeviceConfigurationData (self, dest, source):
        if source.hasId():
            dest.id = source.id
            dest.setHasId()

    def copySetSimulationConfigurationData (self, dest, source):
        if source.hasForceOperationalStatus():
            dest.forceOperationalStatus = source.forceOperationalStatus
            dest.setHasForceOperationalStatus()

    @classmethod
    def newDeviceStatus (cls):
        __pychecker__ = "unusednames=cls"
        deviceStatus = a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.status.status_oper_data_gen.StatusOperData()
        deviceStatus.setAllRequested()
        return deviceStatus

    @classmethod
    def newStatus (cls):
        __pychecker__ = "unusednames=cls"
        status = a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.status.status_oper_data_gen.StatusOperData()       
        status.setAllRequested()
        return status

    @classmethod
    def newAlarm (cls):
        __pychecker__ = "unusednames=cls"
        alarm = a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.alarm.alarm_oper_data_gen.AlarmOperData()          
        alarm.setAllRequested()
        return alarm

    @classmethod
    def defaultDeviceStatus (cls):
        deviceStatus = cls.newDeviceStatus()
        deviceStatus.setIndex("unknown")
        deviceStatus.setProbeName("unknown")
        deviceStatus.setCurrentRpm("unknown")
        deviceStatus.setStatusRaw("unknown")        
        deviceStatus.setMinimumWarningRpm("unknown")
        deviceStatus.setMaximumWarningRpm("unknown")
        deviceStatus.setMinimumErrorRpm("unknown")
        deviceStatus.setMaximumErrorRpm("unknown")
        deviceStatus.setStatus(FanDeviceStatusType.kUnknown)
        return deviceStatus


    @classmethod
    def defaultStatus (cls):
        status = cls.newStatus()
        status.setOperationalStatus(FanOperationalStatusType.kUnknown)
        status.setOperationalStatusReason(FanOperationalStatusReasonType.kUnknown)
        status.setLocation("unknown")
        return status

    @classmethod
    def defaultAlarm (cls):
        alarm = cls.newAlarm()
        alarm.setFanFailure(False)
        alarm.setFanFailureReason(FanFailureReasonType.kNone)
        return alarm


    def copySetConfigurationData (self, dest, source):
        if source.hasMuteReporting():
            dest.muteReporting = source.muteReporting
            dest.setHasMuteReporting()

        if source.hasLocation():
            dest.location = source.location
            dest.setHasLocation()
