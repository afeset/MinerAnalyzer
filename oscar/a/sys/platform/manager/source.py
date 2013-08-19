# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: shmulika
#


import threading

__pychecker__ = 'maxrefs=20' 
import a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_data_gen

from a.infra.basic.return_codes import ReturnCodes
import a.infra.process
import a.infra.subprocess
import a.infra.time.monotonic_clock
import a.infra.time.elapsed_timer

# Bypass for PyChecker
if  __package__ is None:
    # TODO(shmulika): change this name to source something    
    G_GROUP_NAME_PLATFORM_SOURCE_CONFIGURATION = "unknown"
    G_GROUP_NAME_PLATFORM_SOURCE = "unknown"
    G_GROUP_NAME_PLATFORM_SOURCE_COUNTERS = "uknown"
else:
    from . import G_GROUP_NAME_PLATFORM_SOURCE_CONFIGURATION                  
    from . import G_GROUP_NAME_PLATFORM_SOURCE     
    from . import G_GROUP_NAME_PLATFORM_SOURCE_COUNTERS             

#-----------------------------------------------------------------------------#
class ConfigurationError(Exception):
    def __init__ (self, errMessage):
        Exception.__init__(self)
        self.errMessage = errMessage

    def getErrorMessage (self):
        return self.errMessage

#-----------------------------------------------------------------------------#
class Source:
    """ Source responsibility is to gather information from an external source (e.g. the output of an external process) and make available the information to other modules.
    A Source is polled by the platform manager using the poll() method.
    The information is made available to user modules with the getData() method.
    """

    POLL_TIMEOUT            = "poll-timeout"
    POLL_PARSE_ERROR        = "parse-error"
    POLL_FILE_ERROR         = "file-error"
    POLL_ERROR              = "poll-error"
    POLL_OK                 = "poll-ok"

    def __init__ (self, instanceName, logger):
        self._name = instanceName
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PLATFORM_SOURCE, instance = instanceName)
        self._logConfiguration = logger.createLoggerSameModule(G_GROUP_NAME_PLATFORM_SOURCE_CONFIGURATION, instance = instanceName)

        ### Configuration ###
        self._configErrorMsgFunctor = lambda x: self._logConfiguration("config-error-msg").debug1("error-msg-functor not set yet, called with message: %s", x)
        self._configLock = threading.RLock()
        self._runningSettings   = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_data_gen.SourceData()
        self._candidateSettings = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_data_gen.SourceData()
        self._changedSettings   = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_data_gen.SourceData()

        ### Counters ###
        self._counterReads                  = _Counter(self._log, "reads")
        self._counterParsingErrors          = _Counter(self._log, "parsing-errors")
        self._counterFileErrors             = _Counter(self._log, "file-errors")
        self._counterCommandErrors          = _Counter(self._log, "command-errors")
        self._counterCommandTimeoutWarnings = _Counter(self._log, "command-timeout-warnings")
        self._counterCommandTimeouts        = _Counter(self._log, "command-timeout")


        ### Logic ###
        self._storedData = None
        self._dataLock = threading.RLock()


###############################################################
# BLINKY, CONFIGURATION, OPER
###############################################################

    def setConfigMsgFunctor (self, functor):
        """ Sets the config error message functor - which will be used to report configuration error messages """
        def logAndCallFunctor (message):
            self._logConfiguration("config-error-msg").debug2("error-msg-functor called with message: %s", message)
            functor(message)

        self._logConfiguration("set-config-msg-functor").debug2("setting error msg functor to given functor %s", functor)
        self._configErrorMsgFunctor = logAndCallFunctor


    ######################
    # OPER
    ######################

    def getObjCountersOperData(self, trxContext, countersData):                
        self._logConfiguration("get-obj-counters-oper-data-called").debug3("called with trxContext = %s, countersData = %s", trxContext, countersData)
        countersData.setReads                  (self._counterReads.get())
        countersData.setParsingErrors          (self._counterParsingErrors.get())
        countersData.setFileErrors             (self._counterFileErrors.get())
        countersData.setCommandErrors          (self._counterCommandErrors.get())
        countersData.setCommandWarningTimeouts (self._counterCommandTimeoutWarnings.get())
        countersData.setCommandTimeouts        (self._counterCommandTimeouts.get())
        self._logConfiguration("get-obj-counters-oper-data-done").debug3("returned counters-oper-data=%s", countersData)
        return ReturnCodes.kOk  


    def actionClearCounters (self):
        self._counterReads.clear()
        self._counterParsingErrors.clear()
        self._counterFileErrors.clear()
        self._counterCommandErrors.clear()
        self._counterCommandTimeoutWarnings.clear()
        self._counterCommandTimeouts.clear()
        self._logConfiguration("action-clear-counters").debug1("counters cleared.")
        return (ReturnCodes.kOk, None)


    ######################
    # GETTERS
    ######################

    def getSettings (self):
        __pychecker__ = 'maxrefs=20' 
        with self._configLock:
            copyData = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_data_gen.SourceData()
            copyData.copyFrom(self._runningSettings)
        return copyData


    ######################
    # TRANSACTION
    ######################

    def configStartTransaction (self):
        __pychecker__ = 'maxrefs=20' 
        self._logConfiguration("config-start-transaction").debug1("configuration transaction started")

        with self._configLock:
            self._candidateSettings.copyFrom(self._runningSettings)
            self._changedSettings = a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_data_gen.SourceData()

        return ReturnCodes.kOk


    def preparePrivateData (self, sourceData):        
        self._logConfiguration("prepare-private-data").debug2("got candidate data = %s", sourceData)

        if sourceData.hasEnabled():
            self._candidateSettings.enabled = sourceData.enabled
            self._candidateSettings.setHasEnabled()

        if sourceData.hasCommandTimeout():
            self._candidateSettings.commandTimeout = sourceData.commandTimeout
            self._candidateSettings.setHasCommandTimeout()

        if sourceData.hasCommandWarningTimeout():
            self._candidateSettings.commandWarningTimeout = sourceData.commandWarningTimeout
            self._candidateSettings.setHasCommandWarningTimeout()

        if sourceData.hasSimulationFile():
            self._candidateSettings.simulationFile = sourceData.simulationFile
            self._candidateSettings.setHasSimulationFile()

        self._changedSettings.copyFrom(sourceData)

        return ReturnCodes.kOk


    def configAbortTransaction (self):
        self._logConfiguration("config-abort-transaction").debug2("configuration transaction aborted")
        return ReturnCodes.kOk


    def configPreparePrivateAfter (self):
        self._logConfiguration("config-prepare-private-after").debug2("checking configuration validity")                        
        try:
            self._checkCandidateConfigurationData(self._candidateSettings)
        except ConfigurationError as configurationError:
            self._logConfiguration("config-prepare-private-after-configuration-invalid").error("configuration invalid: %s", configurationError.getErrorMessage())
            self._configErrorMsgFunctor(configurationError.getErrorMessage())
            return ReturnCodes.kGeneralError
        else:
            self._logConfiguration("config-prepare-private-after-done").debug1("candidate configuration is valid")                
            return ReturnCodes.kOk


    def _checkCandidateConfigurationData (self, candidateSettings):
        if not candidateSettings.hasEnabled():
            raise ConfigurationError("source must be configured to either enabled or disabled")

        if not candidateSettings.hasCommandTimeout():
            raise ConfigurationError("source must be configured with command timeout")

        if not candidateSettings.hasCommandWarningTimeout():
            raise ConfigurationError("source must be configured with command warning threshold")
       
        if not candidateSettings.hasSimulationFile(): 
            raise ConfigurationError("source must be configured with simulation file")

        if candidateSettings.commandTimeout <= 0:
            raise ConfigurationError("command-timeout must be a positive value")

        if candidateSettings.commandWarningTimeout < 0:
            raise ConfigurationError("command-warning-threshold must be a non-negative value")

        if candidateSettings.commandWarningTimeout > candidateSettings.commandTimeout:
            raise ConfigurationError("command-warning-threshold must be smaller than or equal to command-timeout")

        # not checking simualtion-file, if it's non-existing or somehow bad - it will cause a file-error, which is counted
        # much simpler than trying to check the existence of the file now, especially since it's a tech feature only
    

    def configPreparePublicAfter (self):
        self._logConfiguration("config-prepare-public-after").debug2("doing nothing - already checked data in private")       
        return ReturnCodes.kOk


    def configCommitTransaction (self):        
        with self._configLock:
            self._runningSettings.copyFrom(self._candidateSettings)
            self.applyRunningConfiguration(self._changedSettings)

        self._logConfiguration("config-commit-transaction").debug2("configuration transaction commited")
        self._wasConfigured = True
        return ReturnCodes.kOk


    def applyRunningConfiguration (self, changedSettings):
        __pychecker__ = "unusednames=changedSettings"        
        pass

###############################################################
# SOURCE - MAIN LOGIC & INTERFACE
###############################################################

    def getData (self):
        """ Returns the most recently udpated data, in a extension-specific data structure 
        The object type is according to the extension class.
        Returns: object of appropriate data structure, or None if no result has been read yet.
        Raises: None
        """
        with self._dataLock:            
            data = self._storedData
        self._log("get-data").debug1("data was returned = %s", data)
        return data


    def poll (self):
        """ Polls the source and updates the stored data for next getData() calls. 
        When poll is disabled, or fails - the stored data is Noneified       
        Returns: ReturnCodes.kOk - if poll succesfull
        Raises: None
        """   
        settings = self.getSettings()

        if settings.hasEnabled() and not settings.enabled:
            self._updateData(None)
            return ReturnCodes.kOk

        self._counterReads.increment()

        if settings.hasSimulationFile() and settings.simulationFile != "":            
            simulationFile = a.infra.process.substitueSystemKnownPaths(settings.simulationFile)
            if simulationFile is None:
                self._log("poll-simulation-file-error").debug2("invalid simulation file format = %s", settings.simulationFile)
                self._counterFileErrors.increment()            
                return ReturnCodes.kGeneralError
            else:
                self._log("poll-simulation-file").debug2("polling text from simulation file = %s", simulationFile)

        else:
            simulationFile = None
        
        pollReturnCode = self._poll(settings.commandWarningTimeout, settings.commandTimeout, simulationFile)

        # non-failure return codes
        if pollReturnCode == Source.POLL_OK:             
            return ReturnCodes.kOk

        # failure return codes
        elif pollReturnCode == Source.POLL_TIMEOUT:        
            self._counterCommandTimeouts.increment()                   
        elif pollReturnCode == Source.POLL_PARSE_ERROR:
            self._counterParsingErrors.increment()         
        elif pollReturnCode == Source.POLL_FILE_ERROR:
            self._counterFileErrors.increment()            
        elif pollReturnCode == Source.POLL_ERROR:          
            self._counterCommandErrors.increment()         
        
        self._updateData(None)
        return ReturnCodes.kGeneralError


    def _reportWarningTimeout (self):
        """ Called by the extension class, when a warning timeout has occured """
        self._counterCommandTimeoutWarnings.increment()

    def _poll (self, warningTimeout, timeout, simulationFile = None):
        """ Polls the source and updates the stored data for next getData() calls.
        Arguments:
            timeout         - maximum time to try the poll, if exceeded - stop and return POLL_TIMEOUT
            warningTimeout  - warning timeout < timeout; if exceeded (but poll done) must call _reportWarningTimeout
            simulationFile  - when not None, should read the file and take information from it instead of usual source of information

        Should be extended by specific source class.
        Returns:
            Source.POLL_TIMEOUT         - when the command timed out
            Source.POLL_PARSE_ERROR     - when parsing the information failed
            Source.POLL_FILE_ERROR      - when reading the file failed
            Source.POLL_ERROR           - when there was an error
            Source.POLL_OK              - when poll was ok
         
        Raises: None
        """
        __pychecker__ = "unusednames=warningTimeout,timeout,simulationFile"        
        return Source.POLL_ERROR


    def getName (self):
        return self._name

    
    def _updateData (self, udpatedData):
        """ Called by the extension class to udpated the stored data
        """
        with self._dataLock:
            self._log("update-data").debug1("data is updated to %s", udpatedData)
            self._storedData = udpatedData





###############################################################
# INTERNAL UTILITY CLASSES
###############################################################

class _Counter:
    """ Utility for maintaining a counter
    Note: could have simply be an int, but feels like there would have been code replication
    """

    def __init__ (self, logger, instanceName):
        self._log = logger.createLoggerSameModule(G_GROUP_NAME_PLATFORM_SOURCE_COUNTERS, instance = instanceName)
        self._value = 0
        self._clearBase = 0
        self._instanceName = instanceName

    def increment (self):
        self._value = self._value + 1
        self._log("counter-increment").debug4("counter %s was incremented to value %s", self._instanceName, self._value)        

    def incrementBy (self, addition):
        self._value = self._value + addition
        self._log("counter-increment").debug4("counter %s was incremented by %s to value %s", self._instanceName, addition, self._value)        

    def get (self):
        value = int(self._value - self._clearBase)
        self._log("counter-get").debug3("returning counter %s value %s", self._instanceName, value)
        return value

    def getUncleared (self):
        value = int(self._value)
        self._log("counter-get").debug3("returning counter %s uncleared value %s", self._instanceName, value)
        return value

    def clear (self):
        self._clearBase = self._value
        self._log("counter-clear").debug2("clearing counter %s, clear-base-value=%s", self._instanceName, self._clearBase)

    def __str__ (self):
        return "{counter %s: (value = %s, uncleared-value=%s}"%(self._instanceName, self.get(), self.getUncleared())





