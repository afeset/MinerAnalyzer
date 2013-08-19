# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 

import threading

# PowerSupplies Enums
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerRedundancyStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerNoRedundancyReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerForceOperationalStatusType

from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyDeviceOnlineStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyForceOperationalStatusType
                                                                             
# PowerSupplies Blinky Data
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_data_gen #PowerData
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.status.status_oper_data_gen #StatusOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.alarm.alarm_oper_data_gen #AlarmOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.simulation.simulation_data_gen

# PowerSupply Blinky Datas
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.power_supply_data_gen #PowerSupplyData
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.status.status_oper_data_gen #StatusOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.alarm.alarm_oper_data_gen #AlarmOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.device.device_data_gen #DeviceData
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.device.status.status_oper_data_gen #StatusOperData
import a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.simulation.simulation_data_gen

# User logs
import a.api.user_log.msg.platform
import a.infra.process

from a.infra.basic.return_codes import ReturnCodes
import a.infra.subprocess
import a.infra.time.monotonic_clock
import a.infra.time.elapsed_timer
 
import a.sys.platform.manager.component

class ConfigurationError(Exception):
    def __init__ (self, errMessage):
        Exception.__init__(self)
        self.errMessage = errMessage

    def getErrorMessage (self):
        return self.errMessage

 
#class PowerSuppliesSubsystem(a.sys.platform.manager.component.PlatformManagedSubSystem):
class PowerSuppliesSubsystem(a.sys.platform.manager.component.Component):
    """
    Represents the managed power-supplies in the system.
    It has its own configuration and oper data.
    It is also responsible for getting its information from the appropriate sources (extension dependent)
    """

    def __init__ (self, logger):
        #a.sys.platform.manager.component.PlatformManagedSubSystem.__init__(self, logger, "power-supplies")
        a.sys.platform.manager.component.Component.__init__(self, logger, "power-supplies-subsystem")        
        
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
        # derive the new status & alarm of the power-supplies
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


    def _deriveOperationalStatus (self, powerStatus, newStatus):
        """ derives operational status according to redundancy status """
        # the requested is mostly for logging/debugging, so the fields will show up on prints
        newStatus.copyFrom(powerStatus)

        # check if there's a simulation configured
        with self._configLock:
            simulationData = self._runningSimulationData

        if simulationData.hasForceOperationalStatus() and simulationData.forceOperationalStatus != PowerForceOperationalStatusType.kNone:
            self._log("derive-operational-status").debug1("operational status was simulated to %s", simulationData.forceOperationalStatus.getDisplayName())
            if simulationData.forceOperationalStatus == PowerForceOperationalStatusType.kUp:
                newStatus.setOperationalStatus(PowerOperationalStatusType.kUp)
                newStatus.setOperationalStatusReason(PowerOperationalStatusReasonType.kSimulation)

            elif simulationData.forceOperationalStatus == PowerForceOperationalStatusType.kDegraded:
                newStatus.setOperationalStatus(PowerOperationalStatusType.kDegraded)
                newStatus.setOperationalStatusReason(PowerOperationalStatusReasonType.kSimulation)

            else:
                self._log("derive-operational-status-failed").error("could not derive operational status from the simulated status=%s", simulationData.forceOperationalStatus.getDisplayName())
            return

        if not newStatus.hasRedundancyStatus():
            self._log("derive-operational-status").debug1("no redundancy status was determined, can't derive operational status")
        else:
            if newStatus.redundancyStatus == PowerRedundancyStatusType.kFull:
                # all is good 
                newStatus.setOperationalStatus(PowerOperationalStatusType.kUp)
                newStatus.setOperationalStatusReason(PowerOperationalStatusReasonType.kRedundant)
    
            elif newStatus.redundancyStatus == PowerRedundancyStatusType.kLost:
                # redundancy is lost
                newStatus.setOperationalStatus(PowerOperationalStatusType.kDegraded)
                newStatus.setOperationalStatusReason(PowerOperationalStatusReasonType.kSingleSource)
    
            else:
                self._log("derive-operational-status-failed").error("could not derive operational status from the power status=%s", newStatus)

        # We've experimentally seen that omreport may lie to us... It might say everything is OK in the sub-system level, while a power supply is missing...
        # So we check it ourselves        
        for managedUnit in self.getManagedUnits():
            unitStatus = managedUnit.getStatus()
            if unitStatus.hasOperationalStatus() and unitStatus.operationalStatus == PowerSupplyOperationalStatusType.kDown:
                self._log("derive-operational-status").debug2("a power-supply unit is down, deriving from it that the power sub-system is degraded")
                newStatus.setOperationalStatus(PowerOperationalStatusType.kDegraded)
                newStatus.setOperationalStatusReason(PowerOperationalStatusReasonType.kSingleSource)


    def _deriveAlarmIfNotMute (self, powerStatus, powerAlarm):
        """ calls deriveAlarm if mute-reporting was not configured
        """
        # no need to use lock here, only needing a single boolean variable (reconsider if becomes more than that)
        if not self._runningData.muteReporting:
            self._deriveAlarm(powerStatus, powerAlarm)


    def _deriveAlarm (self, powerStatus, powerAlarm):
        # the requested is mostly for logging/debugging, so the fields will show up on prints
        if not powerStatus.hasOperationalStatus():
            self._log("derive-operational-status").debug1("no operational status was generated, can't derive alarms")
            return

        if powerStatus.operationalStatus == PowerOperationalStatusType.kUp:
            powerAlarm.setNoRedundancy(False)
            powerAlarm.setNoRedundancyReason(PowerNoRedundancyReasonType.kNone)

        elif powerStatus.operationalStatus == PowerOperationalStatusType.kDegraded:
            powerAlarm.setNoRedundancy(True)
            powerAlarm.setNoRedundancyReason(PowerNoRedundancyReasonType.kNoRedundancy)

        else:
            self._log("derive-alarm-failed").error("could not derive alarm from the power status=%s", powerStatus)


    def _logChangeStatus (self, oldStatus, newStatus):
        #TODO(shmulika): implement this with user log, and difference tracking
        self._log("log-change-status").debug2("old status was %s, new status is %s", oldStatus, newStatus)
        shouldLogChange = False

        if oldStatus.operationalStatus == PowerOperationalStatusType.kUnknown:
            if newStatus.operationalStatus == PowerOperationalStatusType.kDegraded:
                shouldLogChange = True
        else:
            if newStatus.operationalStatus != oldStatus.operationalStatus:
                shouldLogChange = True

        if shouldLogChange:
            a.infra.process.logUserMessage(a.api.user_log.msg.platform.PowerOperationalStatusChanged(self._operationalStatusToString(newStatus.operationalStatus)))

    # TODO(shmulika): this won't be needed when Blinky supports automatic conversion from enum to confd string
    def _operationalStatusToString (self, operationalStatus):
        if operationalStatus == PowerOperationalStatusType.kUp:
            return "up"
        elif operationalStatus == PowerOperationalStatusType.kDegraded:
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
        return a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_data_gen.PowerData()        

    @classmethod
    def newSimulationData (cls):
        __pychecker__ = "unusednames=cls"
        return a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.simulation.simulation_data_gen.SimulationData()        

    @classmethod
    def newStatus (cls):
        __pychecker__ = "unusednames=cls"
        status = a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.status.status_oper_data_gen.StatusOperData()
        status.setAllRequested()
        return status

    @classmethod
    def defaultStatus (cls):
        status = cls.newStatus()
        status.setRedundancyStatus(PowerRedundancyStatusType.kUnknown)
        status.setRedundancyStatusRaw("unknown")
        status.setOperationalStatus(PowerOperationalStatusType.kUnknown)
        status.setOperationalStatusReason(PowerOperationalStatusReasonType.kUnknown)
        return status

    @classmethod
    def newAlarm (cls):
        __pychecker__ = "unusednames=cls"
        alarm = a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.alarm.alarm_oper_data_gen.AlarmOperData()
        alarm.setAllRequested()
        return alarm

    @classmethod
    def defaultAlarm (cls):
        alarm = cls.newAlarm()
        alarm.setNoRedundancy(False)
        alarm.setNoRedundancyReason(PowerNoRedundancyReasonType.kNone)
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
class PowerSupplyUnit(a.sys.platform.manager.component.Component):
    """
    Represents a managed power-supply element in the system.
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
        # derive the new status & alarm of the power-supplies
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
        

        if simulationData.hasForceOperationalStatus() and simulationData.forceOperationalStatus != PowerSupplyForceOperationalStatusType.kNone:
            self._log("derive-operational-status").debug1("operational status was simulated to %s", simulationData.forceOperationalStatus.getDisplayName())
            if simulationData.forceOperationalStatus == PowerSupplyForceOperationalStatusType.kUp:
                newStatus.setOperationalStatus(PowerSupplyOperationalStatusType.kUp)
                newStatus.setOperationalStatusReason(PowerSupplyOperationalStatusReasonType.kSimulation)

            elif simulationData.forceOperationalStatus == PowerSupplyForceOperationalStatusType.kDown:
                newStatus.setOperationalStatus(PowerSupplyOperationalStatusType.kDown)
                newStatus.setOperationalStatusReason(PowerSupplyOperationalStatusReasonType.kSimulation)

            else:
                self._log("derive-operational-status-failed").error("could not derive operational status from the simulated status=%s", simulationData.forceOperationalStatus.getDisplayName())
            return

        if not deviceStatus.hasStatus():
            self._log("derive-operational-status").debug1("no device status was generated, can't derive operational status")
            return

        if deviceStatus.status == PowerSupplyDeviceStatusType.kOk:
            # device status is ok
            newStatus.setOperationalStatus(PowerSupplyOperationalStatusType.kUp)
            newStatus.setOperationalStatusReason(PowerSupplyOperationalStatusReasonType.kNone)

        elif deviceStatus.status == PowerSupplyDeviceStatusType.kCritical:
            # device status is critical
            newStatus.setOperationalStatus(PowerSupplyOperationalStatusType.kDown)

            # try to figure out the reason for it in the online status
            if deviceStatus.onlineStatus == PowerSupplyDeviceOnlineStatusType.kPresenceDetected:
                # the power supply is there, but has an unknown problem
                newStatus.setOperationalStatusReason(PowerSupplyOperationalStatusReasonType.kUnknown)

            elif deviceStatus.onlineStatus == PowerSupplyDeviceOnlineStatusType.kPowerSourceLost:
                # the power-source has been lost
                newStatus.setOperationalStatusReason(PowerSupplyOperationalStatusReasonType.kPowerSourceLost)
                
            elif deviceStatus.onlineStatus == PowerSupplyDeviceOnlineStatusType.kNotAvailable:
                # we do not know
                newStatus.setOperationalStatusReason(PowerSupplyOperationalStatusReasonType.kUnknown)            

        elif deviceStatus.status == PowerSupplyDeviceStatusType.kAbsent:
            # device status is absent
            newStatus.setOperationalStatus(PowerSupplyOperationalStatusType.kDown)
            newStatus.setOperationalStatusReason(PowerSupplyOperationalStatusReasonType.kAbsent)

        elif deviceStatus.status == PowerSupplyDeviceStatusType.kUnknown:
            # experimentally, we've seen that when omreport says "Unknown" there is something wrong with the power supply (e.g. when it isn't there...)
            # we decided that this situation will be considered as "absent"
            newStatus.setOperationalStatus(PowerSupplyOperationalStatusType.kDown)
            newStatus.setOperationalStatusReason(PowerSupplyOperationalStatusReasonType.kAbsent)

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
            self._log("derive-operational-status").debug1("no operational status was generated, can't derive alarms")
            return
        
        if status.operationalStatus == PowerSupplyOperationalStatusType.kUp:
            # the power-supply is ok
            alarm.setPowerSupplyFailure(False)
            alarm.setPowerSupplyFailureReason(PowerSupplyFailureReasonType.kNone)

        elif status.operationalStatus == PowerSupplyOperationalStatusType.kDown:
            # the power-supply failed
            alarm.setPowerSupplyFailure(True)

            # try to understand why it failed
            if status.operationalStatusReason == PowerSupplyOperationalStatusReasonType.kPowerSourceLost:
                alarm.setPowerSupplyFailureReason(PowerSupplyFailureReasonType.kPowerSourceLost)
            elif status.operationalStatusReason == PowerSupplyOperationalStatusReasonType.kAbsent:
                alarm.setPowerSupplyFailureReason(PowerSupplyFailureReasonType.kAbsent)
            else:
                alarm.setPowerSupplyFailureReason(PowerSupplyFailureReasonType.kUnknown)


        else:
            self._log("derive-alarm-failed").error("could not derive alarm from the power supply operational status=%s", status)


    def _logChangeStatus (self, oldStatus, newStatus):
        self._log("log-change-status").debug2("old status was %s, new status is %s", oldStatus, newStatus)
        shouldLogChange = False

        if oldStatus.operationalStatus == PowerSupplyOperationalStatusType.kUnknown:
            if newStatus.operationalStatus == PowerSupplyOperationalStatusType.kDown:
                shouldLogChange = True
        else:
            if newStatus.operationalStatus != oldStatus.operationalStatus:
                shouldLogChange = True

        if shouldLogChange:
            location = self._returnLocationOrNone(self._getLocation())
            statusString = newStatus.operationalStatus.getDisplayName()
            a.infra.process.logUserMessage(a.api.user_log.msg.platform.PowerSupplyOperationalStatusChanged(self._unitName, location, statusString))


    def _returnLocationOrNone (self, locationString):
        if locationString is None:
            return "unknown"
        else:
            return locationString


#    # TODO(shmulika): this won't be needed when Blinky supports automatic conversion from enum to confd string
#    def _operationalStatusToString (self, operationalStatus):
#        if operationalStatus == PowerSupplyOperationalStatusType.kUp:
#            return "up"
#        elif operationalStatus == PowerSupplyOperationalStatusType.kDown:
#            return "down"
#        else:
#            return "unknown"


    def _logChangeAlarm (self, oldAlarm, newAlarm):
        #TODO(shmulika): implement this with user log, and difference tracking
        self._log("log-change-alarm").debug2("old alarm was %s, new alarm is %s", oldAlarm, newAlarm)


    def _getFruId (self):
        with self._configLock:
            if self._runningDeviceData.hasFruId():
                return self._runningDeviceData.fruId
            else:                
                return None


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
        return a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.power_supply_data_gen.PowerSupplyData()        


    @classmethod
    def newDeviceConfigurationData (cls):
        __pychecker__ = "unusednames=cls"
        data = a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.device.device_data_gen.DeviceData()
        return data

    @classmethod
    def newSimulationConfigurationData (cls):
        __pychecker__ = "unusednames=cls"
        data = a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.simulation.simulation_data_gen.SimulationData()
        return data


    def copySetDeviceConfigurationData (self, dest, source):
        if source.hasFruId():
            dest.fruId = source.fruId
            dest.setHasFruId()

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
        deviceStatus = a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.device.status.status_oper_data_gen.StatusOperData()
        deviceStatus.setAllRequested()
        return deviceStatus

    @classmethod
    def newStatus (cls):
        __pychecker__ = "unusednames=cls"
        status = a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.status.status_oper_data_gen.StatusOperData()
        status.setAllRequested()
        return status

    @classmethod
    def newAlarm (cls):
        __pychecker__ = "unusednames=cls"
        alarm = a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.alarm.alarm_oper_data_gen.AlarmOperData()
        alarm.setAllRequested()
        return alarm

    @classmethod
    def defaultDeviceStatus (cls):
        deviceStatus = cls.newDeviceStatus()
        deviceStatus.setFruDevice("unknown")
        deviceStatus.setSerialNumber("unknown")
        deviceStatus.setPartNumber("unknown")
        deviceStatus.setManufacturer("unknown")
        deviceStatus.setManufactureDate("unknown")
        deviceStatus.setRevision("unknown")
        deviceStatus.setIndex("unknown")
        deviceStatus.setLocation("unknown")
        deviceStatus.setStatusRaw("unknown")        
        deviceStatus.setInputType("unknown")
        deviceStatus.setFirmwareVersion("unknown")
        deviceStatus.setRatedInputWattage("unknown")
        deviceStatus.setMaximumOutputWattage("unknown")
        deviceStatus.setOnlineStatusRaw("unknown")
        deviceStatus.setStatus(PowerSupplyDeviceStatusType.kUnknown)
        deviceStatus.setOnlineStatus(PowerSupplyDeviceOnlineStatusType.kUnknown)
        return deviceStatus

    @classmethod
    def defaultStatus (cls):
        status = cls.newStatus()
        status.setOperationalStatus(PowerSupplyOperationalStatusType.kUnknown)
        status.setOperationalStatusReason(PowerSupplyOperationalStatusReasonType.kUnknown)
        status.setLocation("unknown")
        return status

    @classmethod
    def defaultAlarm (cls):
        alarm = cls.newAlarm()
        alarm.setPowerSupplyFailure(False)
        alarm.setPowerSupplyFailureReason(PowerSupplyFailureReasonType.kNone)
        return alarm

    def copySetConfigurationData (self, dest, source):
        if source.hasMuteReporting():
            dest.muteReporting = source.muteReporting
            dest.setHasMuteReporting()

        if source.hasLocation():
            dest.location = source.location
            dest.setHasLocation()

