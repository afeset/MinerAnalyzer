# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: naanas
#

from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.snmp_data_gen import SnmpData
from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.notifications.destination.destination_data_gen import DestinationData
from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.community.community_data_gen import CommunityData
from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.counters.counters_oper_data_gen import CountersOperData

from a.infra.basic.return_codes import ReturnCodes
import a.infra.process

import time

# Bypass for PyChecker
if  __package__ is None:
    G_MODULE_NAME_SNMP_MANAGER              = "unknown"
    G_GROUP_NAME_SNMP_MANAGER_CONFIGURATION    = "unknown"
else:
    from . import G_MODULE_NAME_SNMP_MANAGER                  
    from . import G_GROUP_NAME_SNMP_MANAGER_CONFIGURATION 


class ConfigurationError(Exception):
    def __init__ (self, errMessage):
        Exception.__init__(self)
        self.errMessage = errMessage

    def getErrorMessage (self):
        return self.errMessage


class SnmpManager(object):

    def __init__ (self, logger):
        self._logConfiguration = logger.createLogger(G_MODULE_NAME_SNMP_MANAGER, G_GROUP_NAME_SNMP_MANAGER_CONFIGURATION)

        ### Configuration ###
        self._configErrorMsgFunctor = lambda x: self._logConfiguration("config-error-msg-functor-not-set").debug1("error-msg-functor not set yet, called with message: %s", x)
        self._runningSettings   = SnmpData()
        self._candidateSettings = SnmpData()
        self._changedSettings   = SnmpData()

        self._zeroPointSnmpCounters = CountersOperData()
        self._zeroPointSnmpCounters.setAllNumericToZero()
        self._zeroPointSnmpCounters.setAllRequested()
        
        self._blinkySnmp = None

        self._wasStopped = False

        self._runningDestinations = {}
        self._runningCommunities = {}

        self.SLEEP_INTERVAL_SECONDS_BETWEEN_CHECK_STOP = 1

        self._enableSnmpAgentFunctor = lambda x, y: self._logConfiguration("enable-snmp-functor-not-set").error(
            "enable-snmp-agent functor not set yet. called with params: enabled=%s, verifyOnly=%s", x, y)

        self._readSnmpCountersFunctor = lambda x: self._logConfiguration("enable-read-snmp-counters-functor-not-set").error(
            "read-snmp-counters functor not set yet. called with params: operData=%s", x)
        
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

    def setEnableSnmpAgentFunctor (self, functor):
        """ Sets the enable snmp agent functor """
        def logAndCallFunctor (enabled, validateOnly):
            self._logConfiguration("enable-snmp-agent-functor-called").debug2("enable-snmp-agent-functor called with enabled=%s, validateOnly=%s", enabled, validateOnly)
            return functor(enabled, validateOnly)

        self._logConfiguration("set-enable-snmp-agent-functor").debug2("setting enable snmp agent functor to given functor %s", functor)
        self._enableSnmpAgentFunctor = logAndCallFunctor

    def setReadSnmpCountersFunctor (self, functor):
        """ Sets the read snmp counters functor """
        def logAndCallFunctor (operData):
            self._logConfiguration("read-snmp-counters-functor-called").debug2("read-snmp-counters-functor called. operData=%s", operData)
            if self._runningSettings.enabled:
                return functor(operData)
            else:
                return ReturnCodes.kOk

        self._logConfiguration("set-read-snmp-counters-functor").debug2("setting read snmp counters functor to given functor %s", functor)
        self._readSnmpCountersFunctor = logAndCallFunctor

    ######################
    # GETTERS
    ######################

    def getData (self):
        copyData = SnmpData()
        copyData.copyFrom(self._runningSettings)
        return copyData

    def getRunningDestination (self, key):
        self._logConfiguration("get-running-destination").debug2("called. key=%s", key)
        if key not in self._runningDestinations.keys():
            self._logConfiguration("get-runnning-destination-non-existing-key").debug2("cannot get destination: %s. It doesn't exists", key)
            return None
        return self._runningDestinations[key]

    def getRunningCommunity (self, key):
        self._logConfiguration("get-running-community").debug2("called. key=%s", key)
        if key not in self._runningCommunities.keys():
            self._logConfiguration("get-runnning-communities-non-existing-key").debug2("cannot get community: %s. It doesn't exists", key)
            return None
        return self._runningCommunities[key]

    ######################
    # TRANSACTION
    ######################

    def configStartTransaction (self):
        self._logConfiguration("config-start-transaction").debug2("configuration transaction started")

        self._candidateSettings.copyFrom(self._runningSettings)
        self._changedSettings = SnmpData()
            
        return ReturnCodes.kOk


    def preparePrivateSnmpData (self, blinkyData):        
        self._logConfiguration("prepare-private-snmp-data").debug2("got candidate data = %s", blinkyData)
        
        if blinkyData.hasEnabled():
            self._candidateSettings.enabled = blinkyData.enabled
            self._candidateSettings.setHasEnabled()

        self._changedSettings.copyFrom(blinkyData)

        return ReturnCodes.kOk

    def commitPrivateAddDestination (self, key):
        self._logConfiguration("commit-private-add-destination").debug2("called. key=%s", key)

        if key in self._runningDestinations.keys():
            self._logConfiguration("commit-private-add-destination-existing-key").error("cannot add destination: %s. It already exists", key)
            a.infra.process.processFatal("cannot add destination: %s. It already exists" % key)

        self._runningDestinations[key] = DestinationData()
        self._logConfiguration("commit-private-add-destination-done").debug2("done. key=%s. other keys: %s", key, self._runningDestinations.keys())
        return ReturnCodes.kOk

    def commitPrivateRemoveDestination (self, key):
        self._logConfiguration("commit-private-remove-destination").debug2("called. key=%s", key)
        
        if key not in self._runningDestinations.keys():
            self._logConfiguration("commit-private-remove-destination-non-existing-key").error("cannot remove destination: %s. It doesn't exists", key)
            a.infra.process.processFatal("cannot remove destination: %s. It doesn't exist" % key)

        del self._runningDestinations[key]
        self._logConfiguration("commit-private-remove-destination-done").debug2("done. key=%s. other keys: %s", key, self._runningDestinations.keys())
        return ReturnCodes.kOk

    def commitPrivateDestinationData (self, key, destinationData):
        self._logConfiguration("commit-private-destination-data").debug2("called. key=%s, destinationData=%s", key, destinationData)
        
        if key not in self._runningDestinations.keys():
            self._logConfiguration("commit-private-destination-data-non-existing-key").error("cannot update destination: %s. It doesn't exists", key)
            a.infra.process.processFatal("cannot update destination: %s. It doesn't exist" % key)

        self._runningDestinations[key] = destinationData
        self._logConfiguration("commit-private-destination-data-done").debug2("done. key=%s, destinationData=%s", key, self._runningDestinations[key])
        return ReturnCodes.kOk

    def commitPrivateAddCommunity (self, key):
        self._logConfiguration("commit-private-add-community").debug2("called. key=%s", key)

        if key in self._runningCommunities.keys():
            self._logConfiguration("commit-private-add-community-existing-key").error("cannot add community: %s. It already exists", key)
            a.infra.process.processFatal("cannot add community: %s. It already exists" % key)

        self._runningCommunities[key] = CommunityData()
        self._logConfiguration("commit-private-add-community-done").debug2("done. key=%s. other keys: %s", key, self._runningCommunities.keys())
        return ReturnCodes.kOk

    def commitPrivateRemoveCommunity (self, key):
        self._logConfiguration("commit-private-remove-community").debug2("called. key=%s", key)
        
        if key not in self._runningCommunities.keys():
            self._logConfiguration("commit-private-remove-community-non-existing-key").error("cannot remove community: %s. It doesn't exists", key)
            a.infra.process.processFatal("cannot remove community: %s. It doesn't exist" % key)

        del self._runningCommunities[key]
        self._logConfiguration("commit-private-remove-community-done").debug2("done. key=%s. other keys: %s", key, self._runningCommunities.keys())
        return ReturnCodes.kOk

    def commitPrivateCommunityData (self, key, communityData):
        self._logConfiguration("commit-private-community-data").debug2("called. key=%s, communityData=%s", key, communityData)
        
        if key not in self._runningCommunities.keys():
            self._logConfiguration("commit-private-community-data-non-existing-key").error("cannot update community: %s. It doesn't exists", key)
            a.infra.process.processFatal("cannot update community: %s. It doesn't exist" % key)

        self._runningCommunities[key] = communityData
        self._logConfiguration("commit-private-community-data-done").debug2("done. key=%s, communityData=%s", key, self._runningCommunities[key])
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
            raise ConfigurationError("manager must be configured to either enabled or disabled")

        # TODO (naamas): add here verification that we can edit confd.conf

    def configPreparePublicAfter (self):
        self._logConfiguration("config-prepare-public-after").debug2("doing nothing - already checked data in private")       
        return ReturnCodes.kOk


    def configCommitTransaction (self):        
        self._runningSettings.copyFrom(self._candidateSettings)
        self.applyRunningConfiguration(self._changedSettings)

        self._logConfiguration("config-commit-transaction").debug2("configuration transaction commited")
        self._wasConfigured = True
        return ReturnCodes.kOk

    def applyRunningConfiguration (self, changedSettings):
        self._logConfiguration("apply-running-configuration").debug2("called. changedSettings=%s", changedSettings)
        if changedSettings.hasEnabled():
            res = self._enableSnmpAgentFunctor(changedSettings.enabled, False)
            if res != ReturnCodes.kOk:
                self._logConfiguration("apply-running-configuration-functor-failed").error("_enableSnmpAgentFunctor() failed. changedSettings=%s", changedSettings)
                return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

    ################## OPER & GETTERS ###################    

    def clearSnmpCounters (self, userInfo):
        self._logConfiguration("clear-snmp-counters").debug3("called. userInfo=%s, self._zeroPointSnmpCounters=%s", userInfo, self._zeroPointSnmpCounters)

        res = self._readSnmpCountersFunctor(self._zeroPointSnmpCounters)
        if res != ReturnCodes.kOk:
            self._logConfiguration("clear-snmp-counters-read-snmp-counters-failed").error("_readSnmpCountersFunctor() failed. self._zeroPointSnmpCounters=%s", self._zeroPointSnmpCounters)
            return ReturnCodes.kGeneralError

        self._logConfiguration("clear-snmp-counters-done").debug3("done. userInfo=%s, self._zeroPointSnmpCounters=%s", userInfo, self._zeroPointSnmpCounters)
        return ReturnCodes.kOk
    
    def getObjCountersOperData (self, dpTrxContext, operData):        
        res = self.getSnmpCounters(operData)
        if res != ReturnCodes.kOk:
            self._logConfiguration("get-obj-snmp-counters-get-snmp-counters-failed").error("getSnmpCounters() failed. operData=%s", operData)
            return ReturnCodes.kGeneralError

        operData.subtractAllNumericHas(self._zeroPointSnmpCounters)

        self._logConfiguration("get-obj-counters-oper-data").debug3("returning: dpTrxContext=%s, operData=%s", dpTrxContext, operData)
        return ReturnCodes.kOk

    def getSnmpCounters (self, operData):
        self._logConfiguration("get-snmp-counters").debug3("called. operData=%s", operData)
        res = self._readSnmpCountersFunctor(operData)
        if res != ReturnCodes.kOk:
            self._logConfiguration("get-snmp-counters-read-snmp-counters-failed").error("_readSnmpCountersFunctor() failed. operData=%s", operData)
            return ReturnCodes.kGeneralError

        self._logConfiguration("get-snmp-counters-done").debug3("returning: operData=%s", operData)
        return ReturnCodes.kOk

    def launch (self):
        """ Called by the Application to launch the reporter manager """
        self._logConfiguration("launch-go").debug1("snmp manager was launched")

        while not self.wasStopped():            
            time.sleep(self.SLEEP_INTERVAL_SECONDS_BETWEEN_CHECK_STOP)

        self._logConfiguration("launch-stop").debug1("reporter-manager has stopped")

    def wasStopped (self):
        return self._wasStopped


    def stop (self):
        """ Called by the Application to stop the reporter manager """
        self._logConfiguration("stop").debug1("reporter-manager asked to be stopped")
        self._wasStopped = True

