# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities 
# without explicit written permission from Qwilt.
# 
# Author: naamas
#

import a.infra.process
import a.sys.blinky.domain_priority
import a.sys.snmp.manager.common.manager
import a.sys.snmp.manager.blinky.manager_blinky_adaptor
from a.infra.basic.return_codes import ReturnCodes

# Bypass for PyChecker
if  __package__ is None:
    G_MODULE_NAME_SNMP_MAIN            = "unknown"
    G_GROUP_NAME_BLINKY_SNMP_MAIN         = "unknown"
else:
    from . import G_MODULE_NAME_SNMP_MAIN
    from . import G_GROUP_NAME_BLINKY_SNMP_MAIN


class BlinkySnmpMain:

    def __init__ (self, logger):
        self._log = logger.createLogger(G_MODULE_NAME_SNMP_MAIN, G_GROUP_NAME_BLINKY_SNMP_MAIN)

        # logical elements
        self._snmpManager = None

        # blinky/configuration      
        self._configDomain = None

        self._snmpManagerBlinkyAdaptor = None


    def initSnmpManager (self):        
        self._log("init-snmp").debug1("initializing snmp")    
        self._snmpManager = a.sys.snmp.manager.common.manager.SnmpManager(self._log)        
        
    def initBlinkyAgent (self, blinkyAgent, confdConfFile):
        self._log("init-blinky-agent").debug1("called. blinkyAgent=%s, confdConfFile=%s", blinkyAgent, confdConfFile)
        self._createDomains(blinkyAgent)        
        self._snmpManagerBlinkyAdaptor = a.sys.snmp.manager.blinky.manager_blinky_adaptor.ManagerBlinkyAdaptor(self._log, self._configDomain, self._dpDomain, self._maapiDomain)

        res = self._snmpManagerBlinkyAdaptor.createAndAttachBlinkySnmp(self._snmpManager)
        if res != ReturnCodes.kOk:
            self._log("init-blinky-agent-create-and-attach-faield").error("self._snmpManagerBlinkyAdaptor.createAndAttachBlinkySnmp() failed. blinkyAgent=%s, confdConfFile=%s", blinkyAgent, confdConfFile)
            return ReturnCodes.kGeneralError

        self._snmpManagerBlinkyAdaptor.setConfdConfFile(confdConfFile)

        res = self._registerDone()
        if res != ReturnCodes.kOk:
            self._log("init-blinky-agent-registration-done-faield").error("self._registerDone() failed. blinkyAgent=%s, confdConfFile=%s", blinkyAgent, confdConfFile)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def _createDomains (self, blinkyAgent):
        self._log("create-domains").debug1("creating domains in blinkyAgent=%s", blinkyAgent)    
        priority=a.sys.blinky.domain_priority.DomainPriority.kDefault
        self._configDomain = blinkyAgent.createConfigDomain("config-snmp", priority)
        self._dpDomain = blinkyAgent.createConfigDomain("transformation-snmp", priority)
        self._maapiDomain = blinkyAgent.createMaapiDomain("maapi-snmp")

    def _registerDone (self):
        self._log("register-done").debug1("finishing registration and triggering subscriptions.")    
        self._configDomain.registrationDone()
        self._dpDomain.registrationDone()
        self._configDomain.triggerSubscriptions()

        return ReturnCodes.kOk


#################################################################
# GETTERS
#################################################################

    def getSnmpManager (self):
        return self._snmpManager


