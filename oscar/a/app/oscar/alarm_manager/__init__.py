
#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

import a.sys.mng.alarm.alarm_manager

class AlarmManagerApp: 
    """This application is the daemon in-charge of alarm managment"""

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self):
        pass
        

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlInitLogger(self, logger):
        """Init the process logger to be used.

        Args:
            logger: a logger from which new loggers shall be created
        """
        self._manager = a.sys.mng.alarm.alarm_manager.AlarmManager(logger)

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
        __pychecker__ = 'unusednames=sysParamsCfg,specificParams' 

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStart(self):
        """launching the process"""
        self._manager.initializeAlarmsAndSources()
        self._manager.attachToBlinky(self._blinkyAgent)

    def daemonControlRun(self):
        """getting into the main loop"""
        self._manager.launch()

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStop(self):
        """stopping the process"""
        self._manager.stop()


