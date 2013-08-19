# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: lenak
#


from a.infra.basic.return_codes import ReturnCodes
import a.sys.blinky.domain_priority
from a.sys.clock.app.timezone_list import kSupportedTimezonesString
from a.sys.clock.blinky.clock_blinky_adapter import ClockBlinkyAdapter
from a.sys.clock.manager.clock_manager_cent_os import ClockManagerCentOs
from a.sys.clock.tech_system_clock.tech.system.clock.blinky_clock_gen import BlinkyClock
from a.sys.clock.tech_system_clock.tech.system.clock.status.blinky_status_oper_gen import BlinkyOperStatus


# Bypass for PyChecker
if  __package__ is None:
    G_NAME_MODULE_CLOCK_MAIN = "unknown"
    G_NAME_GROUP_CLOCK_MAIN = "unknown"
else:
    from . import G_NAME_MODULE_CLOCK_MAIN                  
    from . import G_NAME_GROUP_CLOCK_MAIN        

class ClockMain(object):
    """Main clock handler class

    The correct way to use this class:
    1. Initiate an object
    2. call create(blinkyAgent, isMini).
    
    The class holds the list of the supported timezones

    Attributes:
        clockManager: clock manager
        clockAdapter: clock blinky adapter
        blinkyAgent: blinky agent
        blinkyClockConfig: blinky clock config node
        blinkyClockOper: blinky clock oper node
        configDomain: blinky config domain
        operDomain: blinky oper domain

    """

    kSupportedTimezoneList = kSupportedTimezonesString.split()

    def __init__ (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_CLOCK_MAIN, G_NAME_GROUP_CLOCK_MAIN)
        self._clockManager = None
        self._clockAdapter = None
        self._blinkyAgent = None
        self._blinkyClockConfig = None      
        self._blinkyClockOper = None
        self._configDomain = None
        self._operDomain = None


    def create(self, blinkyAgent, isMini):
        """Initialze the object 

        Args: 
            blinkyAgent: blinky agent
            isMini: boolean flag which indecates whether the platform is mini

        Returns:
                ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """

        self._log("create-called").debug1("create() called: blinkyAgent=%s, isMini=%s", blinkyAgent, isMini)
        self._createDomains(blinkyAgent)
        rc = self._createClockManager(isMini)

        if rc == ReturnCodes.kOk:
            self._createBlinkyNodes()
            self._createBlinkyAdapter()
            rc = self._attachToBlinky()
            if rc != ReturnCodes.kOk:
                self._log("create-error").error("create(): _createClockManager() returned an error")
                rc = ReturnCodes.kGeneralError
        else:
            self._log("create-erro").error("create(): _attachToBlinky() returned an error")
            rc = ReturnCodes.kGeneralError
        self._log("create-ended").debug1("create() ended: rc=%s", rc)
        return rc
        
    def _createDomains (self, blinkyAgent):
        """Creats blinky domains 

        Args: 
            blinkyAgent: blinky agent
        """
        self._log("create-domain").debug2("_createDomain() called: blinkyAgent=%s", blinkyAgent)
        priority=a.sys.blinky.domain_priority.DomainPriority.kDefault
        self._configDomain = blinkyAgent.createConfigDomain("config-clock", priority)
        self._operDomain = blinkyAgent.createConfigDomain("oper-clock", priority)
        self._log("create-domain-ended").debug2("_createDomain() ended: configDomain=%s, operDomain=%s", self._configDomain, self._operDomain)

    def _createClockManager (self, isMini):
        """Creates clock manager object 

        Args: 
            isMini: boolean flag which indecates whether the platform is mini

        Returns:
                ReturnCodes.kOk on success, ReturnCodes.kGeneralError otherwise
        """
        self._log("create-clock-manager").debug2("_createClockManager() called: isMini=%s", isMini)
        self._clockManager = ClockManagerCentOs(self._log)
        self._clockManager.initTimezoneSupportedList(self.kSupportedTimezoneList)
        if isMini:
            self._clockManager.limitConfigToRunning()
        rc = self._clockManager.createClockManager()
        if rc != ReturnCodes.kOk:
            rc = ReturnCodes.kGeneralError
        self._log("create-clock-manager-ended").debug2("_createClockManager() ended: clockManager=%s, rc=%s", self._clockManager, rc)
        return rc

    def _createBlinkyNodes(self):
        """Creates blinky nodes 
        """
        self._log("create-blinky-nodes").debug2("_createBlinkyNodes() called")
        # create blinky config node
        self._blinkyClockConfig = BlinkyClock.s_create(self._log, self._configDomain)
        # create blinky oper node
        self._blinkyClockOper = BlinkyOperStatus(self._log)
        self._blinkyClockOper.setParent(self._blinkyClockConfig)
        self._blinkyClockOper.setConfigObj(self._blinkyClockConfig)
        self._blinkyClockOper.setDomain(self._operDomain)
        # do registration
        self._operDomain.registrationDone()
        self._configDomain.registerNode(self._blinkyClockConfig)
        self._configDomain.registrationDone()
        self._log("create-blinky-nodes-ended").debug2("_createBlinkyNodes() ended: blinkyConfig=%s, blinkyOper=%s", self._blinkyClockConfig, self._blinkyClockOper)

    def _createBlinkyAdapter (self):
        """Creates blinky adapter 
        """
        self._clockAdapter = ClockBlinkyAdapter(self._log)
        self._log("create-blinky-adapter").debug2("_createBlinkyAdapter() called and ended: adapter=%s", self._clockAdapter)

    def _attachToBlinky(self):
        """Attaches to blinky 
        """
        self._log("attach-to-blinky").debug2("_attachToBlinky() called")
        self._clockAdapter.attachToBlinky(self._blinkyClockOper, self._blinkyClockConfig, self._clockManager)

        if self._configDomain.triggerSubscriptions() != ReturnCodes.kOk:
            self._log("attach-to-blinky").error("configDomain.triggerSubscriptions() failed: domain=%s", self._configDomain)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

       
        




     

