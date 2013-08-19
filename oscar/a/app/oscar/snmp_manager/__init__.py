
#
# Copyright Qwilt, 2013
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: naamas
# 

import a.sys.snmp.manager.common.blinky_snmp_main

class SnmpManagerApp: 
    """This application is the daemon in-charge of snmp managment"""

    SPECIFIC_PARAM_KEY_CONFD_CONF_FILE = "confd-conf-file"

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self):
        self._logger = None

        self._confdConfFile = None
        

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlInitLogger(self, logger):
        """Init the process logger to be used.

        Args:
            logger: a logger from which new loggers shall be created
        """
        self._logger = logger        

#-----------------------------------------------------------------------------------------------------------------------
    def  daemonControlInitBlinky(self, agent):
        """Init the process blinky to be used.

        Args:
            agent: a blinky agent
        """
        self._blinkyAgent = agent

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlInitExternalData(self, sysParamsCfg, specificParams):
        """Init the data provided from outside

        Args:
            sysParamsCfg: a contatiner holding the sys params base configuration 
            specificParams: a dictionary holding the data under the "SPECIFIC_PARAM_KEY_..."                                        
        """
        __pychecker__ = 'unusednames=sysParamsCfg' 
        self._confdConfFile = specificParams[self.SPECIFIC_PARAM_KEY_CONFD_CONF_FILE]
        self._logger('daemon-control-init-external-data').debug1('confdConfFile=%s', self._confdConfFile)



#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStart(self):
        """launching the process"""
        self._main = a.sys.snmp.manager.common.blinky_snmp_main.BlinkySnmpMain(self._logger)

        self._main.initSnmpManager()
        self._main.initBlinkyAgent(self._blinkyAgent, self._confdConfFile)

    def daemonControlRun(self):
        self._manager = self._main.getSnmpManager()
        self._manager.launch()

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStop(self):
        """stopping the process"""
        self._manager.stop()


