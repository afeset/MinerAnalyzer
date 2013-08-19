#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: yoave
# 

from a.sys.net.net_manager import NetManager 
from a.infra.basic.return_codes import ReturnCodes
from a.stats.stats_comm_over_file_client import StatsCommOverFileClient
import a.infra.process
import time

G_NAME_MODULE_APP_OSCAR_NET_MANAGER = "net-manager-app"
G_NAME_GROUP_APP_OSCAR_NET_MANAGER_GENERAL = "general"

class NetManagerApp: 
    """This application is the daemon in-charge of actively managing the overall QB system netwrok configuration"""

    # default values 
    DEFAULT_SLEEP_TIME = 0.2
    DEFAULT_STATS_INTERVAL_SEC = 60

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self):
        self.manager = NetManager(G_NAME_MODULE_APP_OSCAR_NET_MANAGER)
        self._log = None
        self._agent = None

        self.wasStopped = False
        self.sleepSecTime = self.DEFAULT_SLEEP_TIME

        #--------Stats--------------#
        self._statsReportingIntervalSec = self.DEFAULT_STATS_INTERVAL_SEC
        self._stats = None 
        self._statsDir = None
        self._lastTimeSentStats = None

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlInitLogger(self, logger):
        """Init the process logger to be used.

        Args:
            logger: a logger from which new loggers shall be created
        """

        self._log = logger.createLogger(G_NAME_MODULE_APP_OSCAR_NET_MANAGER, 
                                        G_NAME_GROUP_APP_OSCAR_NET_MANAGER_GENERAL)
        self._log("logger-net-manager").debug1("net manager logger init.")
             
#-----------------------------------------------------------------------------------------------------------------------
    def  daemonControlInitBlinky(self, agent):
        """Init the process blinky to be used.

        Args:
            agent: a blinky agent
        """
        self._log("blinky-net-manager").debug1("net manager blinky init.")
        self._agent = agent
      
#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlInitExternalData(self, sysParamsCfg, specificParams):
        """Init the data provided from outside

        Args:
            sysParamsCfg: a contatiner holding the sys params base configuration 
            specificParams: a dictionary holding the data under the "SPECIFIC_PARAM_KEY_..."                                        
        """

        self._log("ext-data-net-manager").debug1("net manager exteranl data init")
        self._log("params-cfg-net-manager").debug3("net manager: sysParamsCfg=%s, specificParams=%s", sysParamsCfg, specificParams)

        self.manager.initExternalData(sysParamsCfg, specificParams)

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlInitStats(self, statsDir):
        """init stats dir"""

        self._statsDir = statsDir 
                     
#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStart(self):
        """starting the process"""

        self._log("start-net-manager").notice("net manager has been started.")

        # init the stats object
        self._stats = StatsCommOverFileClient("net_manager", self._log)
        self._stats.init(self._statsDir)
        
        # activate
        rc = self.manager.activate(self._log, self._agent)
        if rc != ReturnCodes.kOk:
            a.infra.process.processFatal("%s: Failed at activate net manager", G_NAME_MODULE_APP_OSCAR_NET_MANAGER)

#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlRun(self):
        """running the process"""

        self._log("run-net-manager").notice("net manager is running.")

        # run in an endless loop and triggered by confd events
        self.wasStopped = False
        while not self.wasStopped:
            currentTime = time.time()

            # send stats if needed
            self.__sendStatsIfNeeded(currentTime)

            time.sleep(self.sleepSecTime)

        # shutdown
        self.manager.shutdown()

        self._log("done-net-manager").notice("net manager has been terminated")
        
#-----------------------------------------------------------------------------------------------------------------------
    def daemonControlStop(self):
        """stopping the process"""

        self._log("stop-net-manager").notice("net manager has been stopped.")
        self.wasStopped = True

#-----------------------------------------------------------------------------------------------------------------------
    def __sendStatsIfNeeded (self, currentTime = None):
        if currentTime == None:
            currentTime = time.time()

        sendStats = False
        if (self._lastTimeSentStats == None) or (currentTime - self._lastTimeSentStats >= self._statsReportingIntervalSec):
            sendStats = True
            self._lastTimeSentStats = currentTime
        
        if sendStats:
            self._log("main-loop-stats").debug3("sending stats counters")
            statsCounters = self.manager.getStatsCounters()
            self._stats.send(statsCounters)
