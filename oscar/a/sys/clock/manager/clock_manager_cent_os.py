# 
# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: lenak

import os
import time

from a.sys.clock.manager.clock_manager_base import ClockManagerBase

kConfigFilePath = "/etc/sysconfig/clock"
kConfigUtility = "tzdata-update"
kLinuxTzInfoPath = "/usr/share/zoneinfo"


class ClockManagerCentOs(ClockManagerBase):
    """Derived class of clock manager.

    """
    
    def _getConfigFile(self):
        """Returns the timezone configuration file.
        """
        return kConfigFilePath

    def _getConfigUtility(self):
        """Returns the timezone configuration utility.
        """
        return kConfigUtility

    def _isTimeZoneValid(self, name): 
        """Checks whether the requested timezone is valid.

        Checks if the timezone file exists.
    
        Args:
            name: requested timezone name
        Returns:
            Boolean value: True if valid, False otherwise
        """

        self._log("is-time-zone-valid-called").debug4("_isTimeZoneValid() called: name=%s", name) 
        rc = True
        tzFullPath = os.path.join(kLinuxTzInfoPath, name)
        if not os.path.isfile(tzFullPath):
            rc = False
            self._log("clock-manager-cent-os-is-valid-false").info("clock_manager_centos _isTimeZoneValid() False: %s",name)
        self._log("is-time-zone-valid-ended").debug4("_isTimeZoneValid() ended: rc=%s", rc)
        return rc

    def _getEpoch(self):
        """Returns the current epoch
        """
        return time.time()


