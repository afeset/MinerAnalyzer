#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

import time
import a.sys.log.housekeeper.infra_logger_housekeeper
import a.sys.log.housekeeper.blinky.infra_logger_housekeeper_blinky_adapter

class LogHousekeeperApp: 
    """This application is the daemon in-charge of log files managment"""    

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self):
        self._shallStop = False

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
        #__pychecker__ = 'unusednames=sysParamsCfg' 
        #__pychecker__ = 'unusednames=specificParams' 
        pass

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStart(self):
        """launching the process"""

        #creating the operational classes
        self._infraLoggerHousekeeper = a.sys.log.housekeeper.infra_logger_housekeeper.InfraLoggerHousekeeper(self._logger)        
        def shallStopFunctor():
            return self._shallStop
        self._infraLoggerHousekeeper.initStopFlagFunctor(shallStopFunctor)

        #connecting to blinky
        self._blinkyAdapter = a.sys.log.housekeeper.blinky.infra_logger_housekeeper_blinky_adapter.LoggerLoggerHousekeeperBlinkyAdapter(self._logger)
        self._blinkyAdapter.createDomainAndBlinkyLoggerHousekeeperAndAttach(self._blinkyAgent, self._infraLoggerHousekeeper)

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlRun(self):
        """getting into the main loop"""

        while not self._shallStop:
            self._infraLoggerHousekeeper.poll()
            time.sleep(0.2)#short sleep so we will not stuck oscar when going dwn

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStop(self):
        """stopping the process"""
        self._shallStop = True


