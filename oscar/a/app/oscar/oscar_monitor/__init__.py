#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import a.sys.utils.oscar_monitor

class OscarMonitorApp: 
    def __init__ (self):
        self._instance = a.sys.utils.oscar_monitor.OscarMonitor()
    ###implementing functions called directly by oscar
    def daemonControlInitLogger(self, logger):
        """Init the class logger to be used.

        Init the logger. This function has a predefined syntax matching the OscarPythonDaemon convention.
        This function shall be called before any other functions of the class

        Args:
            logger: a logger from which new loggers shall be created

        Returns:
            None

        Raises:
            None
        """
        self._instance.initLogger(logger)        

    def daemonControlInitExternalData(self, sysParamsCfg, specificParams):
        """Init the data provided from outside

        Init the data provided from outside - both from configuration and operational consts
        This function has a predefined syntax matching the OscarPythonDaemon convention

        Args:
            sysParamsCfg: a contatiner holding the sys params base configuration (that are destined to move to blinky)
            specificParams: a dictionary holding the data under the "SPECIFIC_PARAM_KEY_..." keys defined at the begining of this class                                            

        Returns:
            None

        Raises:
            None
        """

        self._instance.initExternalData(sysParamsCfg, specificParams)


    def daemonControlRun(self):
        """launching the module

        do our thing:) and keep on doing so until the stop command is alled
        This function has a predefined syntax matching the OscarPythonDaemon convention
        This function may sys.exit upon failure

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        self._instance.launch()


