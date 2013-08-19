#!/usr/local/bin/python2.6
# 
# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: lenak

import os

from a.infra.basic.return_codes import ReturnCodes
from a.sys.clock.manager.clock_manager_base import ClockManagerBase

class ClockManagerUT(ClockManagerBase):
    """Derived class of clock manager.

    Attributes:
        requestedValidTZ: a list that holds all the valid time-zones
        configFile: configuration file
        configUtility: configuration utility
        requestedEpoch: requested epoch

    """
    
    def __init__(self, log, configFile, configUtility):
        ClockManagerBase.__init__(self, log)
        self._requestedValidTZ = []
        self._configFile = configFile
        self._configUtility = configUtility
        
    def setRequestedValidTZ (self, tzList):
        """sets the valid time-zone list

        Args:
            tzList: requested valid time-zone list 
    
        """
        self._requestedValidTZ = tzList

    def setEpochAndEnvVar (self, epoch):
        """sets the requested epoch and the TZ environment variable, to test the status data.
        """
        os.environ['TZ'] = self._clockDataRunningConfig.timezone
        self._requestedEpoch = epoch


    def _getConfigFile(self):
        """Returns the timezone configuration file.
        """
        return self._configFile

    def _getConfigUtility (self):
        """Returns the timezone configuration utility.
        """
        return self._configUtility

    def _isTimeZoneValid(self, timezone):
        """Returns true if the given timezone s valid and false otherwise
        """
        return timezone in self._requestedValidTZ

    def _getEpoch(self):
        """Returns the current epoch
        """

        return self._requestedEpoch

