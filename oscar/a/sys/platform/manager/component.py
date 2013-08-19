# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#
__pychecker__ = 'maxrefs=20' 

#from a.infra.basic.return_codes import ReturnCodes
#import a.infra.subprocess
#import a.infra.time.monotonic_clock
#import a.infra.time.elapsed_timer

# Bypass for PyChecker
if  __package__ is None:
    G_GROUP_NAME_PLATFORM_MANAGED_COMPONENT = "unknown"    
else:    
    from . import G_GROUP_NAME_PLATFORM_MANAGED_COMPONENT


#class ConfigurationError(Exception):
#    def __init__ (self, errMessage):
#        Exception.__init__(self)
#        self.errMessage = errMessage
#
#    def getErrorMessage (self):
#        return self.errMessage


###############################################################
# MANAGED PLATFORM ELEMENTS
###############################################################
       
class Component:
    def __init__ (self, logger, instanceName):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PLATFORM_MANAGED_COMPONENT, instance = instanceName)
        self._name = instanceName
        

    def updateOrClear (self, enabled = True):
        """
        If enabled, gets updated information from relevant sources and updates the data.
        If disabled, clears the information (set unknown status instead)
        """
        pass

    def update (self):
        """ Extension-specific.
        Gets updated information from the relevant sources, and updates it in the oper structures of this class.
        All updates occur at once as under the oper-lock with the _updateData() method
        """
        pass

    def getName (self):
        return self._name


#        ## CONFIG ##
#        self._configErrorMsgFunctor = lambda x: self._log("config-error-msg").debug1("error-msg-functor not set yet, called with message: %s", x)
#
#        self._configLock = threading.RLock()
#        self._runningData = self.newConfigurationData()
#        self._candidateData = self.newConfigurationData()
#        self._changedData = self.newConfigurationData()
#
#        ## OPER ##
#        self._operLock = threading.RLock()
#        self._status = self.newStatus()
#        self._alarm  = self.newAlarm()
#
#    ################## DATAS ###################
#
#    @classmethod
#    def newConfigurationData (cls):
#        __pychecker__ = "unusednames=cls"
#        return None
#
#    @classmethod
#    def newStatus (cls):
#        __pychecker__ = "unusednames=cls"
#        return None
#
#    @classmethod
#    def defaultStatus (cls):
#        status = cls.newStatus()
#        #change to defaults here        
#        return status
#
#    @classmethod
#    def newAlarm (cls):
#        __pychecker__ = "unusednames=cls"        
#        return None
#
#    @classmethod
#    def defaultAlarm (cls):
#        alarm = cls.newAlarm()
#        #change to defaults here        
#        return alarm
#
#
#    def copySetConfigurationData (self, dest, source):
#        pass
#
#    ################## CONFIGURATION ###################
#
#    def attachToBlinky (self, blinkyAdaptor):
#        """ To be implemented by extension class """
#        __pychecker__ = "unusednames=blinkyAdaptor"
#        pass
#
#    def setConfigMsgFunctor (self, functor):
#        """ Sets the config error message functor - which will be used to report configuration error messages """
#        def logAndCallFunctor (message):
#            self._log("config-error-msg").debug2("error-msg-functor called with message: %s", message)
#            functor(message)
#
#        self._log("set-config-msg-functor").debug2("setting error msg functor to given functor %s", functor)
#        self._configErrorMsgFunctor = logAndCallFunctor
#
#    def configStartTransaction (self):
#        self._log("config-start-transaction").debug2("configuration transaction started")
#        with self._configLock:
#            self._configStartTransaction()
#            
#        return ReturnCodes.kOk
#
#    def _configStartTransaction (self):
#        """ Can be extended by extensions classes
#        """
#        self._candidateData.copyFrom(self._runningData)
#        self._changedData = self.newConfigurationData()
#
#
#    def preparePrivateData (self, blinkyData):        
#        self._log("prepare-private-data").debug2("got candidate data = %s", blinkyData)
#        self.copySetConfigurationData(self._candidateData, blinkyData)
#        self._changedData.copyFrom(blinkyData)
#        return ReturnCodes.kOk
#
#
#    def configAbortTransaction (self):
#        self._log("config-abort-transaction").debug2("configuration transaction aborted")
#        return ReturnCodes.kOk
#
#
#    def configPreparePrivateAfter (self):
#        self._log("config-prepare-private-after").debug2("checking configuration validity")                        
#        try:
#            self._configPreparePrivateAfter()
#        except ConfigurationError as configurationError:
#            self._log("config-prepare-private-after-configuration-invalid").error("configuration invalid: %s", configurationError.getErrorMessage())
#            self._configErrorMsgFunctor(configurationError.getErrorMessage())
#            return ReturnCodes.kGeneralError
#        else:
#            self._log("config-prepare-private-after-done").debug1("candidate configuration is valid")                
#            return ReturnCodes.kOk
#
#
#    def _configPreparePrivateAfter (self):
#        """ Raises ConfigurationError if configuration is invalid
#        """
#        self._checkCandidateConfigurationData(self._candidateData)
#
#
#    def configPreparePublicAfter (self):
#        self._log("config-prepare-public-after").debug2("doing nothing - already checked data in private")       
#        return ReturnCodes.kOk
#
#
#    def configCommitTransaction (self):        
#        with self._configLock:
#            self._configCommitTransaction()
#            
#        self._log("config-commit-transaction").debug2("configuration transaction commited")
#        self._wasConfigured = True
#        return ReturnCodes.kOk
#
#
#    def _configCommitTransaction (self):
#        """ Can be extended by extensions classes
#        """
#        self._runningData.copyFrom(self._candidateData)
#        self._applyRunningConfigurationData(self._runningData, self._changedData)
#
#
#    def _checkCandidateConfigurationData (self, candiadteData):
#        """ To be implemented by extension-class
#        """
#        __pychecker__ = "unusednames=candiadteData,changedData"
#        pass
#
#    def _applyRunningConfigurationData (self, runningData, changedData):
#        """ To be implemented by extension-class
#        """
#        __pychecker__ = "unusednames=runningData,changedData"
#        pass
#
#
#    def getObjStatusOperData (self, dpTrxContext, operData):        
#        operData.copyRequestedFrom(self.getStatus())
#        self._log("get-obj-status-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
#        return ReturnCodes.kOk
#
#
#    def getObjAlarmOperData (self, dpTrxContext, operData):        
#        operData.copyRequestedFrom(self.getAlarm())
#        self._log("get-obj-alarm-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
#        return ReturnCodes.kOk
#
#
#    def getStatus (self):
#        #TODO(shmulika): when Blinky comes, this will become an oper request
#        with self._operLock:
#            statusCopy = self.defaultStatus()
#            statusCopy.copySetFrom(self._status)
#        return statusCopy
#
#
#    def getAlarm (self):
#        #TODO(shmulika): when Blinky comes, this will become an oper request
#        with self._operLock:
#            alarmCopy  = self.defaultAlarm()
#            alarmCopy.copySetFrom(self._alarm)
#        return alarmCopy
#
#
#    ################## LOGIC ###################
#
#    def update (self):
#        """ Extension-specific.
#        Gets updated information from the relevant sources, and updates it in the oper structures of this class.
#        All updates occur at once as under the oper-lock with the _updateData() method
#        """
#        pass
#
#
#    def _updateData (self, newData):
#        """
#        Called to by the update() method with updated data
#        """        
#        # derive the new status & alarm of the power-supplies
#        newStatus = self.newStatus()
#        newAlarm = self.newAlarm()
#
#        self._deriveOperationalStatus(newData, newStatus)
#        self._deriveAlarmIfNotMute(newStatus, newAlarm)
#        self._logChangeStatus(self._status, newStatus)
#        self._logChangeAlarm(self._alarm, newAlarm)
#
#        with self._operLock:
#            self._writeDataStatusAlarm(newData, newStatus, newAlarm)
#        
#
#    def _writeDataStatusAlarm (self, newData, newStatus, newAlarm):    
#        __pychecker__ = "unusednames=newData"
#        self._status = newStatus
#        self._alarm = newAlarm
#
#
#    def _deriveOperationalStatus (self, powerStatus, newStatus):
#        """ should be implemented by extension classes
#        """
#        pass
#
#
#    def _deriveAlarmIfNotMute (self, powerStatus, powerAlarm):
#        """ calls deriveAlarm if mute-reporting was not configured
#        """
#        # no need to use lock here, only needing a single boolean variable (reconsider if becomes more than that)
#        if not self._runningData.muteReporting:
#            self._deriveAlarm(powerStatus, powerAlarm)
#
#
#    def _deriveAlarm (self, powerStatus, powerAlarm):
#        """ should be implemented by extension classes
#        """
#        pass
#
#    def _logChangeStatus (self, oldStatus, newStatus):
#        """ should be implemented by extension classes
#        """
#        pass
#
#    def _logChangeAlarm (self, oldAlarm, newAlarm):
#        """ should be implemented by extension classes
#        """
#        pass
#
#
#class PlatformManagedSubSystem(Component):
#    # TODO(shmulika):
#    # we decided to flatten the object creation, so only the platform initializer creates elements/units
#    # so this class is actually not neccessary now, but I'll keep it anyway just in case some functionality in this level re-emerges
#    def __init__ (self, logger, instanceName):
#        Component.__init__ (self, logger, instanceName)
#
#        self._elements = {}
#    
#    def getElement (self, name):
#        if name in self._elements:
#            return self._elements[name]
#        else:
#            element = self.createElement(name)
#            element.initPlatformManager(self._platformManager)
#            self._elements[name] = element
#            return element
#
#    def createElement (self, name):
#        """ To be implemented by extension class """
#        __pychecker__ = "unusednames=name"
#        return None
#
#
#class PlatformManagedUnitBase(Component):
#    def __init__ (self, logger, instanceName):
#        Component.__init__ (self, logger, instanceName)
#        self._runningDeviceData = self.newDeviceConfigurationData()
#        self._candidateDeviceData = self.newDeviceConfigurationData()
#        self._changedDeviceData = self.newDeviceConfigurationData()
#
#        self._deviceStatus = self.newDeviceStatus()
#
#    ################## DATAS ###################
#
#    @classmethod
#    def newDeviceConfigurationData (cls):
#        __pychecker__ = "unusednames=cls"
#        return None
#
#    @classmethod
#    def newDeviceStatus (cls):
#        __pychecker__ = "unusednames=cls"        
#        return None
#
#    @classmethod
#    def defaultDeviceStatus (cls):
#        return cls.newDeviceStatus()
#
#
#    def copySetDeviceConfigurationData (self, dest, source):
#        pass
#
#    ################## CONFIGURATION ###################
#
#    def _configStartTransaction (self):
#        """ Can be extended by extensions classes
#        """
#        Component._configStartTransaction(self)
#        self._candidateDeviceData.copyFrom(self._runningDeviceData)
#        self._changedDeviceData = self.newDeviceConfigurationData()
#
#
#    def preparePrivateDeviceData (self, blinkyDeviceData):        
#        self._log("prepare-private-device-data").debug2("got candidate device-data = %s", blinkyDeviceData)
#        self.copySetDeviceConfigurationData(self._candidateDeviceData, blinkyDeviceData)
#        self._changedDeviceData.copyFrom(blinkyDeviceData)
#        return ReturnCodes.kOk
#
#
#    def _configPreparePrivateAfter (self):
#        """ Raises ConfigurationError if configuration is invalid
#        """
#        Component._configPreparePrivateAfter(self)
#        self._checkCandidateDeviceConfigurationData(self._changedDeviceData)
#
#
#    def _configCommitTransaction (self):
#        """ Can be extended by extensions classes
#        """
#        Component._configCommitTransaction(self)
#        self._runningDeviceData.copyFrom(self._candidateDeviceData)
#        self._applyRunningDeviceConfigurationData(self._runningDeviceData, self._changedDeviceData)
#
#
#    def _checkCandidateConfigurationData (self, candidateData):
#        """ To be implemented by extension-class
#        """
#        if self._runningData.hasName() and candidateData.name != self._runningData.name:
#            raise ConfigurationError("cannot change name of element, list is static")
#
#    def _checkCandidateDeviceConfigurationData (self, candidateDeviceData):
#        """ To be implemented by extension-class
#        """
#        __pychecker__ = "unusednames=candidateDeviceData"
#        pass
#
#    def _applyRunningDeviceConfigurationData (self, runningDeviceData, changedDeviceData):
#        """ To be implemented by extension-class
#        """
#        __pychecker__ = "unusednames=runningDeviceData,changedDeviceData"
#        pass
#
#
#    def getObjDeviceStatusOperData (self, dpTrxContext, operData):        
#        operData.copyRequestedFrom(self.getDeviceStatus())
#        self._log("get-obj-device-status-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
#        return ReturnCodes.kOk
#
#    def getDeviceStatus (self):
#        #TODO(shmulika): when Blinky comes, this will become an oper request
#        with self._operLock:
#            deviceStatusCopy  = self.defaultDeviceStatus()
#            deviceStatusCopy.copySetFrom(self._deviceStatus)
#        return deviceStatusCopy
#
#
#    def setDeviceData (self, deviceData):
#        #TODO(shmulika): when Blinky comes, this will become a config operation, and of course will be part of a transaction
#        with self._configLock:
#            self._runningDeviceData.copyFrom(deviceData)
#
#    ################## LOGIC ###################
#
#    def _writeDataStatusAlarm (self, newData, newStatus, newAlarm):    
#        Component._writeDataStatusAlarm(self, newData, newStatus, newAlarm)
#        self._deviceStatus = newData


