
#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

from a.sys.clock.app.clock_main import ClockMain
import a.sys.boot.utils
import a.sys.platform.manager.dell.blinky_platform_main

class PlatformManagerApp: 
    """This application is the daemon in-charge of platform managment"""
    PLATFORM_TYPE_DELL      = "Dell"

    SPECIFIC_PARAM_KEY_MINI_PLATFORM_FLAG = "mini-platform-flag"

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self):
        self._logger = None
        self._platformType = None
        

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
        #TODO(shmulika): get platform type here!
        __pychecker__ = 'unusednames=sysParamsCfg' 
        self._platformType = self.PLATFORM_TYPE_DELL
        self._miniPlatformFlag = specificParams[self.SPECIFIC_PARAM_KEY_MINI_PLATFORM_FLAG]


#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStart(self):
        """launching the process"""
        if self._platformType == self.PLATFORM_TYPE_DELL:
            self._main = a.sys.platform.manager.dell.blinky_platform_main.BlinkyPlatformMain(self._logger)
        else:
            # TODO(shmulika): log error here
            return

        self._main.initPlatformManagedComponenets()
        self._main.initBlinkyAgent(self._blinkyAgent)
        self._manager = self._main.getPlatformManager()
         
        self._clockMain = ClockMain(self._logger)
        self._clockMain.create(self._blinkyAgent, self._miniPlatformFlag)

        # This simply logs the current boot device at start-up; because we really want this logged.
        bootUtils = a.sys.boot.utils.BootUtils.s_getFromOsefOrCrash(a.infra.process.getOsef())
        bootUtils.isSecureDigialBootDevice()

    def daemonControlRun(self):
        """getting into the main loop"""
        self._manager.launch()

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStop(self):
        """stopping the process"""
        self._manager.stop()


