 # Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class SnmpTrapsManager(object):

    def __init__ (self):
        self._log = None
        self._blinkyDomain = None

    def initLogger (self, logger):
        self._log = logger

    def init (self, blinkyDomain):
        self._log("init").debug2("called. blinkyDomain=%s", blinkyDomain)
        self._blinkyDomain = blinkyDomain

        res = self._blinkyDomain.registerSnmp()
        if res != ReturnCodes.kOk:
            self._log("register-snmp-failed").error("self._blinkyDomain.registerSnmp() failed. blinkyDomain=%s", blinkyDomain)
    
        return ReturnCodes.kOk

    def snmpInterfaceConfigured (self):
        self._log("snmp-interface-configured").notice("called snmpInterfaceConfigured.")

        trapName = "coldStart"
        res = self._blinkyDomain.sendSnmpTrap(None, trapName)
        if res != ReturnCodes.kOk:
            self._log('snmp-interface-configured-send-snmp-trap-failed').error('self._blinkyDomain.sendSnmpTrap(%s) failed. PARAMS', trapName)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def sendLinkUpTrap (self, mibIfIndex):
        self._log("send-link-up-trap").notice("called sendLinkUpTrap. mibIfIndex=%s", mibIfIndex)

        oids = [[1,3,6,1,2,1,2,2,1,1,mibIfIndex], [1,3,6,1,2,1,2,2,1,2,mibIfIndex], [1,3,6,1,2,1,2,2,1,3,mibIfIndex], [1,3,6,1,2,1,2,2,1,7,mibIfIndex], [1,3,6,1,2,1,2,2,1,8,mibIfIndex]]
        trapName = "linkUp"
        res = self._blinkyDomain.sendSnmpTrap(None, trapName, oids=oids)
        if res != ReturnCodes.kOk:
            self._log('send-link-up-trap-send-snmp-trap-failed').error('self._blinkyDomain.sendSnmpTrap(%s) failed. PARAMS', trapName)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

    def sendLinkDownTrap (self, mibIfIndex):
        self._log("send-link-down-trap").notice("called sendLinkDownTrap. mibIfIndex=%s", mibIfIndex)

        oids = [[1,3,6,1,2,1,2,2,1,1,mibIfIndex], [1,3,6,1,2,1,2,2,1,2,mibIfIndex], [1,3,6,1,2,1,2,2,1,3,mibIfIndex], [1,3,6,1,2,1,2,2,1,7,mibIfIndex], [1,3,6,1,2,1,2,2,1,8,mibIfIndex]]
        trapName = "linkDown"
        res = self._blinkyDomain.sendSnmpTrap(None, trapName, oids=oids)
        if res != ReturnCodes.kOk:
            self._log('send-link-down-trap-send-snmp-trap-failed').error('self._blinkyDomain.sendSnmpTrap(%s) failed. PARAMS', trapName)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk
