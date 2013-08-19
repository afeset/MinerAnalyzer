


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from status_maapi_base_gen import StatusMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import OperationalStatusType
from a.api.yang.modules.common.qwilt_types.qwilt_types_module_gen import Truthvalue
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import MibAdminStatusType
from a.api.yang.modules.common.iana.iana_if_type_mib.iana_if_type_mib_module_gen import Ianaiftype


class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.interfaceIndexRequested = False
        self.interfaceIndex = None
        self.interfaceIndexSet = False
        
        self.speedMegabitRequested = False
        self.speedMegabit = None
        self.speedMegabitSet = False
        
        self.mibAdminStatusRequested = False
        self.mibAdminStatus = None
        self.mibAdminStatusSet = False
        
        self.promiscuousRequested = False
        self.promiscuous = None
        self.promiscuousSet = False
        
        self.mibNameRequested = False
        self.mibName = None
        self.mibNameSet = False
        
        self.mtuRequested = False
        self.mtu = None
        self.mtuSet = False
        
        self.counterDiscontinuityTicksRequested = False
        self.counterDiscontinuityTicks = None
        self.counterDiscontinuityTicksSet = False
        
        self.mibIanaTypeRequested = False
        self.mibIanaType = None
        self.mibIanaTypeSet = False
        
        self.mibSpeed32BitRequested = False
        self.mibSpeed32Bit = None
        self.mibSpeed32BitSet = False
        
        self.speedRequested = False
        self.speed = None
        self.speedSet = False
        
        self.connectorPresentRequested = False
        self.connectorPresent = None
        self.connectorPresentSet = False
        
        self.operationalStatusRequested = False
        self.operationalStatus = None
        self.operationalStatusSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInterfaceIndex(True)
        
        self.requestSpeedMegabit(True)
        
        self.requestMibAdminStatus(True)
        
        self.requestPromiscuous(True)
        
        self.requestMibName(True)
        
        self.requestMtu(True)
        
        self.requestCounterDiscontinuityTicks(True)
        
        self.requestMibIanaType(True)
        
        self.requestMibSpeed32Bit(True)
        
        self.requestSpeed(True)
        
        self.requestConnectorPresent(True)
        
        self.requestOperationalStatus(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInterfaceIndex(False)
        
        self.requestSpeedMegabit(False)
        
        self.requestMibAdminStatus(False)
        
        self.requestPromiscuous(False)
        
        self.requestMibName(False)
        
        self.requestMtu(False)
        
        self.requestCounterDiscontinuityTicks(False)
        
        self.requestMibIanaType(False)
        
        self.requestMibSpeed32Bit(False)
        
        self.requestSpeed(False)
        
        self.requestConnectorPresent(False)
        
        self.requestOperationalStatus(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInterfaceIndex(True)
        
        self.requestSpeedMegabit(True)
        
        self.requestMibAdminStatus(True)
        
        self.requestPromiscuous(True)
        
        self.requestMibName(True)
        
        self.requestMtu(True)
        
        self.requestCounterDiscontinuityTicks(True)
        
        self.requestMibIanaType(True)
        
        self.requestMibSpeed32Bit(True)
        
        self.requestSpeed(True)
        
        self.requestConnectorPresent(True)
        
        self.requestOperationalStatus(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInterfaceIndex(False)
        
        self.requestSpeedMegabit(False)
        
        self.requestMibAdminStatus(False)
        
        self.requestPromiscuous(False)
        
        self.requestMibName(False)
        
        self.requestMtu(False)
        
        self.requestCounterDiscontinuityTicks(False)
        
        self.requestMibIanaType(False)
        
        self.requestMibSpeed32Bit(False)
        
        self.requestSpeed(False)
        
        self.requestConnectorPresent(False)
        
        self.requestOperationalStatus(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , interface
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(interface, trxContext)

    def read (self
              , interface
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  True,
                                  trxContext)



    def requestInterfaceIndex (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-interfaceindex').debug3Func(): logFunc('called. requested=%s', requested)
        self.interfaceIndexRequested = requested
        self.interfaceIndexSet = False

    def isInterfaceIndexRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-interfaceindex-requested').debug3Func(): logFunc('called. requested=%s', self.interfaceIndexRequested)
        return self.interfaceIndexRequested

    def getInterfaceIndex (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-interfaceindex').debug3Func(): logFunc('called. self.interfaceIndexSet=%s, self.interfaceIndex=%s', self.interfaceIndexSet, self.interfaceIndex)
        if self.interfaceIndexSet:
            return self.interfaceIndex
        return None

    def hasInterfaceIndex (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-interfaceindex').debug3Func(): logFunc('called. self.interfaceIndexSet=%s, self.interfaceIndex=%s', self.interfaceIndexSet, self.interfaceIndex)
        if self.interfaceIndexSet:
            return True
        return False

    def setInterfaceIndex (self, interfaceIndex):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-interfaceindex').debug3Func(): logFunc('called. interfaceIndex=%s, old=%s', interfaceIndex, self.interfaceIndex)
        self.interfaceIndexSet = True
        self.interfaceIndex = interfaceIndex

    def requestSpeedMegabit (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-speedmegabit').debug3Func(): logFunc('called. requested=%s', requested)
        self.speedMegabitRequested = requested
        self.speedMegabitSet = False

    def isSpeedMegabitRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-speedmegabit-requested').debug3Func(): logFunc('called. requested=%s', self.speedMegabitRequested)
        return self.speedMegabitRequested

    def getSpeedMegabit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-speedmegabit').debug3Func(): logFunc('called. self.speedMegabitSet=%s, self.speedMegabit=%s', self.speedMegabitSet, self.speedMegabit)
        if self.speedMegabitSet:
            return self.speedMegabit
        return None

    def hasSpeedMegabit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-speedmegabit').debug3Func(): logFunc('called. self.speedMegabitSet=%s, self.speedMegabit=%s', self.speedMegabitSet, self.speedMegabit)
        if self.speedMegabitSet:
            return True
        return False

    def setSpeedMegabit (self, speedMegabit):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-speedmegabit').debug3Func(): logFunc('called. speedMegabit=%s, old=%s', speedMegabit, self.speedMegabit)
        self.speedMegabitSet = True
        self.speedMegabit = speedMegabit

    def requestMibAdminStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mibadminstatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.mibAdminStatusRequested = requested
        self.mibAdminStatusSet = False

    def isMibAdminStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mibadminstatus-requested').debug3Func(): logFunc('called. requested=%s', self.mibAdminStatusRequested)
        return self.mibAdminStatusRequested

    def getMibAdminStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mibadminstatus').debug3Func(): logFunc('called. self.mibAdminStatusSet=%s, self.mibAdminStatus=%s', self.mibAdminStatusSet, self.mibAdminStatus)
        if self.mibAdminStatusSet:
            return self.mibAdminStatus
        return None

    def hasMibAdminStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mibadminstatus').debug3Func(): logFunc('called. self.mibAdminStatusSet=%s, self.mibAdminStatus=%s', self.mibAdminStatusSet, self.mibAdminStatus)
        if self.mibAdminStatusSet:
            return True
        return False

    def setMibAdminStatus (self, mibAdminStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mibadminstatus').debug3Func(): logFunc('called. mibAdminStatus=%s, old=%s', mibAdminStatus, self.mibAdminStatus)
        self.mibAdminStatusSet = True
        self.mibAdminStatus = mibAdminStatus

    def requestPromiscuous (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-promiscuous').debug3Func(): logFunc('called. requested=%s', requested)
        self.promiscuousRequested = requested
        self.promiscuousSet = False

    def isPromiscuousRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-promiscuous-requested').debug3Func(): logFunc('called. requested=%s', self.promiscuousRequested)
        return self.promiscuousRequested

    def getPromiscuous (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-promiscuous').debug3Func(): logFunc('called. self.promiscuousSet=%s, self.promiscuous=%s', self.promiscuousSet, self.promiscuous)
        if self.promiscuousSet:
            return self.promiscuous
        return None

    def hasPromiscuous (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-promiscuous').debug3Func(): logFunc('called. self.promiscuousSet=%s, self.promiscuous=%s', self.promiscuousSet, self.promiscuous)
        if self.promiscuousSet:
            return True
        return False

    def setPromiscuous (self, promiscuous):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-promiscuous').debug3Func(): logFunc('called. promiscuous=%s, old=%s', promiscuous, self.promiscuous)
        self.promiscuousSet = True
        self.promiscuous = promiscuous

    def requestMibName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mibname').debug3Func(): logFunc('called. requested=%s', requested)
        self.mibNameRequested = requested
        self.mibNameSet = False

    def isMibNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mibname-requested').debug3Func(): logFunc('called. requested=%s', self.mibNameRequested)
        return self.mibNameRequested

    def getMibName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mibname').debug3Func(): logFunc('called. self.mibNameSet=%s, self.mibName=%s', self.mibNameSet, self.mibName)
        if self.mibNameSet:
            return self.mibName
        return None

    def hasMibName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mibname').debug3Func(): logFunc('called. self.mibNameSet=%s, self.mibName=%s', self.mibNameSet, self.mibName)
        if self.mibNameSet:
            return True
        return False

    def setMibName (self, mibName):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mibname').debug3Func(): logFunc('called. mibName=%s, old=%s', mibName, self.mibName)
        self.mibNameSet = True
        self.mibName = mibName

    def requestMtu (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mtu').debug3Func(): logFunc('called. requested=%s', requested)
        self.mtuRequested = requested
        self.mtuSet = False

    def isMtuRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mtu-requested').debug3Func(): logFunc('called. requested=%s', self.mtuRequested)
        return self.mtuRequested

    def getMtu (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mtu').debug3Func(): logFunc('called. self.mtuSet=%s, self.mtu=%s', self.mtuSet, self.mtu)
        if self.mtuSet:
            return self.mtu
        return None

    def hasMtu (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mtu').debug3Func(): logFunc('called. self.mtuSet=%s, self.mtu=%s', self.mtuSet, self.mtu)
        if self.mtuSet:
            return True
        return False

    def setMtu (self, mtu):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mtu').debug3Func(): logFunc('called. mtu=%s, old=%s', mtu, self.mtu)
        self.mtuSet = True
        self.mtu = mtu

    def requestCounterDiscontinuityTicks (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-counterdiscontinuityticks').debug3Func(): logFunc('called. requested=%s', requested)
        self.counterDiscontinuityTicksRequested = requested
        self.counterDiscontinuityTicksSet = False

    def isCounterDiscontinuityTicksRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-counterdiscontinuityticks-requested').debug3Func(): logFunc('called. requested=%s', self.counterDiscontinuityTicksRequested)
        return self.counterDiscontinuityTicksRequested

    def getCounterDiscontinuityTicks (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-counterdiscontinuityticks').debug3Func(): logFunc('called. self.counterDiscontinuityTicksSet=%s, self.counterDiscontinuityTicks=%s', self.counterDiscontinuityTicksSet, self.counterDiscontinuityTicks)
        if self.counterDiscontinuityTicksSet:
            return self.counterDiscontinuityTicks
        return None

    def hasCounterDiscontinuityTicks (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-counterdiscontinuityticks').debug3Func(): logFunc('called. self.counterDiscontinuityTicksSet=%s, self.counterDiscontinuityTicks=%s', self.counterDiscontinuityTicksSet, self.counterDiscontinuityTicks)
        if self.counterDiscontinuityTicksSet:
            return True
        return False

    def setCounterDiscontinuityTicks (self, counterDiscontinuityTicks):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-counterdiscontinuityticks').debug3Func(): logFunc('called. counterDiscontinuityTicks=%s, old=%s', counterDiscontinuityTicks, self.counterDiscontinuityTicks)
        self.counterDiscontinuityTicksSet = True
        self.counterDiscontinuityTicks = counterDiscontinuityTicks

    def requestMibIanaType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mibianatype').debug3Func(): logFunc('called. requested=%s', requested)
        self.mibIanaTypeRequested = requested
        self.mibIanaTypeSet = False

    def isMibIanaTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mibianatype-requested').debug3Func(): logFunc('called. requested=%s', self.mibIanaTypeRequested)
        return self.mibIanaTypeRequested

    def getMibIanaType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mibianatype').debug3Func(): logFunc('called. self.mibIanaTypeSet=%s, self.mibIanaType=%s', self.mibIanaTypeSet, self.mibIanaType)
        if self.mibIanaTypeSet:
            return self.mibIanaType
        return None

    def hasMibIanaType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mibianatype').debug3Func(): logFunc('called. self.mibIanaTypeSet=%s, self.mibIanaType=%s', self.mibIanaTypeSet, self.mibIanaType)
        if self.mibIanaTypeSet:
            return True
        return False

    def setMibIanaType (self, mibIanaType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mibianatype').debug3Func(): logFunc('called. mibIanaType=%s, old=%s', mibIanaType, self.mibIanaType)
        self.mibIanaTypeSet = True
        self.mibIanaType = mibIanaType

    def requestMibSpeed32Bit (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mibspeed32bit').debug3Func(): logFunc('called. requested=%s', requested)
        self.mibSpeed32BitRequested = requested
        self.mibSpeed32BitSet = False

    def isMibSpeed32BitRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mibspeed32bit-requested').debug3Func(): logFunc('called. requested=%s', self.mibSpeed32BitRequested)
        return self.mibSpeed32BitRequested

    def getMibSpeed32Bit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mibspeed32bit').debug3Func(): logFunc('called. self.mibSpeed32BitSet=%s, self.mibSpeed32Bit=%s', self.mibSpeed32BitSet, self.mibSpeed32Bit)
        if self.mibSpeed32BitSet:
            return self.mibSpeed32Bit
        return None

    def hasMibSpeed32Bit (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mibspeed32bit').debug3Func(): logFunc('called. self.mibSpeed32BitSet=%s, self.mibSpeed32Bit=%s', self.mibSpeed32BitSet, self.mibSpeed32Bit)
        if self.mibSpeed32BitSet:
            return True
        return False

    def setMibSpeed32Bit (self, mibSpeed32Bit):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mibspeed32bit').debug3Func(): logFunc('called. mibSpeed32Bit=%s, old=%s', mibSpeed32Bit, self.mibSpeed32Bit)
        self.mibSpeed32BitSet = True
        self.mibSpeed32Bit = mibSpeed32Bit

    def requestSpeed (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-speed').debug3Func(): logFunc('called. requested=%s', requested)
        self.speedRequested = requested
        self.speedSet = False

    def isSpeedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-speed-requested').debug3Func(): logFunc('called. requested=%s', self.speedRequested)
        return self.speedRequested

    def getSpeed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-speed').debug3Func(): logFunc('called. self.speedSet=%s, self.speed=%s', self.speedSet, self.speed)
        if self.speedSet:
            return self.speed
        return None

    def hasSpeed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-speed').debug3Func(): logFunc('called. self.speedSet=%s, self.speed=%s', self.speedSet, self.speed)
        if self.speedSet:
            return True
        return False

    def setSpeed (self, speed):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-speed').debug3Func(): logFunc('called. speed=%s, old=%s', speed, self.speed)
        self.speedSet = True
        self.speed = speed

    def requestConnectorPresent (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-connectorpresent').debug3Func(): logFunc('called. requested=%s', requested)
        self.connectorPresentRequested = requested
        self.connectorPresentSet = False

    def isConnectorPresentRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-connectorpresent-requested').debug3Func(): logFunc('called. requested=%s', self.connectorPresentRequested)
        return self.connectorPresentRequested

    def getConnectorPresent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-connectorpresent').debug3Func(): logFunc('called. self.connectorPresentSet=%s, self.connectorPresent=%s', self.connectorPresentSet, self.connectorPresent)
        if self.connectorPresentSet:
            return self.connectorPresent
        return None

    def hasConnectorPresent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-connectorpresent').debug3Func(): logFunc('called. self.connectorPresentSet=%s, self.connectorPresent=%s', self.connectorPresentSet, self.connectorPresent)
        if self.connectorPresentSet:
            return True
        return False

    def setConnectorPresent (self, connectorPresent):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-connectorpresent').debug3Func(): logFunc('called. connectorPresent=%s, old=%s', connectorPresent, self.connectorPresent)
        self.connectorPresentSet = True
        self.connectorPresent = connectorPresent

    def requestOperationalStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-operationalstatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.operationalStatusRequested = requested
        self.operationalStatusSet = False

    def isOperationalStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-operationalstatus-requested').debug3Func(): logFunc('called. requested=%s', self.operationalStatusRequested)
        return self.operationalStatusRequested

    def getOperationalStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-operationalstatus').debug3Func(): logFunc('called. self.operationalStatusSet=%s, self.operationalStatus=%s', self.operationalStatusSet, self.operationalStatus)
        if self.operationalStatusSet:
            return self.operationalStatus
        return None

    def hasOperationalStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-operationalstatus').debug3Func(): logFunc('called. self.operationalStatusSet=%s, self.operationalStatus=%s', self.operationalStatusSet, self.operationalStatus)
        if self.operationalStatusSet:
            return True
        return False

    def setOperationalStatus (self, operationalStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-operationalstatus').debug3Func(): logFunc('called. operationalStatus=%s, old=%s', operationalStatus, self.operationalStatus)
        self.operationalStatusSet = True
        self.operationalStatus = operationalStatus


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.interfaceIndex = 0
        self.interfaceIndexSet = False
        
        self.speedMegabit = 0
        self.speedMegabitSet = False
        
        self.mibAdminStatus = 0
        self.mibAdminStatusSet = False
        
        self.promiscuous = 0
        self.promiscuousSet = False
        
        self.mibName = 0
        self.mibNameSet = False
        
        self.mtu = 0
        self.mtuSet = False
        
        self.counterDiscontinuityTicks = 0
        self.counterDiscontinuityTicksSet = False
        
        self.mibIanaType = 0
        self.mibIanaTypeSet = False
        
        self.mibSpeed32Bit = 0
        self.mibSpeed32BitSet = False
        
        self.speed = 0
        self.speedSet = False
        
        self.connectorPresent = 0
        self.connectorPresentSet = False
        
        self.operationalStatus = 0
        self.operationalStatusSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(interface);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interfaces", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        interface, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(interface, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       interface, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               interface, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isInterfaceIndexRequested():
            valInterfaceIndex = Value()
            valInterfaceIndex.setEmpty()
            tagValueList.push(("interface-index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInterfaceIndex)
        
        if self.isSpeedMegabitRequested():
            valSpeedMegabit = Value()
            valSpeedMegabit.setEmpty()
            tagValueList.push(("speed-megabit", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valSpeedMegabit)
        
        if self.isMibAdminStatusRequested():
            valMibAdminStatus = Value()
            valMibAdminStatus.setEmpty()
            tagValueList.push(("mib-admin-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMibAdminStatus)
        
        if self.isPromiscuousRequested():
            valPromiscuous = Value()
            valPromiscuous.setEmpty()
            tagValueList.push(("promiscuous", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPromiscuous)
        
        if self.isMibNameRequested():
            valMibName = Value()
            valMibName.setEmpty()
            tagValueList.push(("mib-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMibName)
        
        if self.isMtuRequested():
            valMtu = Value()
            valMtu.setEmpty()
            tagValueList.push(("mtu", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMtu)
        
        if self.isCounterDiscontinuityTicksRequested():
            valCounterDiscontinuityTicks = Value()
            valCounterDiscontinuityTicks.setEmpty()
            tagValueList.push(("counter-discontinuity-ticks", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valCounterDiscontinuityTicks)
        
        if self.isMibIanaTypeRequested():
            valMibIanaType = Value()
            valMibIanaType.setEmpty()
            tagValueList.push(("mib-iana-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMibIanaType)
        
        if self.isMibSpeed32BitRequested():
            valMibSpeed32Bit = Value()
            valMibSpeed32Bit.setEmpty()
            tagValueList.push(("mib-speed-32bit", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valMibSpeed32Bit)
        
        if self.isSpeedRequested():
            valSpeed = Value()
            valSpeed.setEmpty()
            tagValueList.push(("speed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valSpeed)
        
        if self.isConnectorPresentRequested():
            valConnectorPresent = Value()
            valConnectorPresent.setEmpty()
            tagValueList.push(("connector-present", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valConnectorPresent)
        
        if self.isOperationalStatusRequested():
            valOperationalStatus = Value()
            valOperationalStatus.setEmpty()
            tagValueList.push(("operational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOperationalStatus)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isInterfaceIndexRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "interface-index") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-interfaceindex').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "interfaceIndex", "interface-index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint32()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-interface-index-bad-value').infoFunc(): logFunc('interfaceIndex not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInterfaceIndex(tempVar)
            for logFunc in self._log('read-tag-values-interface-index').debug3Func(): logFunc('read interfaceIndex. interfaceIndex=%s, tempValue=%s', self.interfaceIndex, tempValue.getType())
        
        if self.isSpeedMegabitRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "speed-megabit") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-speedmegabit').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "speedMegabit", "speed-megabit", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint32()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-speed-megabit-bad-value').infoFunc(): logFunc('speedMegabit not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSpeedMegabit(tempVar)
            for logFunc in self._log('read-tag-values-speed-megabit').debug3Func(): logFunc('read speedMegabit. speedMegabit=%s, tempValue=%s', self.speedMegabit, tempValue.getType())
        
        if self.isMibAdminStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mib-admin-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mibadminstatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mibAdminStatus", "mib-admin-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mib-admin-status-bad-value').infoFunc(): logFunc('mibAdminStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMibAdminStatus(tempVar)
            for logFunc in self._log('read-tag-values-mib-admin-status').debug3Func(): logFunc('read mibAdminStatus. mibAdminStatus=%s, tempValue=%s', self.mibAdminStatus, tempValue.getType())
        
        if self.isPromiscuousRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "promiscuous") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-promiscuous').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "promiscuous", "promiscuous", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-promiscuous-bad-value').infoFunc(): logFunc('promiscuous not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPromiscuous(tempVar)
            for logFunc in self._log('read-tag-values-promiscuous').debug3Func(): logFunc('read promiscuous. promiscuous=%s, tempValue=%s', self.promiscuous, tempValue.getType())
        
        if self.isMibNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mib-name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mibname').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mibName", "mib-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mib-name-bad-value').infoFunc(): logFunc('mibName not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMibName(tempVar)
            for logFunc in self._log('read-tag-values-mib-name').debug3Func(): logFunc('read mibName. mibName=%s, tempValue=%s', self.mibName, tempValue.getType())
        
        if self.isMtuRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mtu") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mtu').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mtu", "mtu", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt32()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mtu-bad-value').infoFunc(): logFunc('mtu not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMtu(tempVar)
            for logFunc in self._log('read-tag-values-mtu').debug3Func(): logFunc('read mtu. mtu=%s, tempValue=%s', self.mtu, tempValue.getType())
        
        if self.isCounterDiscontinuityTicksRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "counter-discontinuity-ticks") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-counterdiscontinuityticks').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "counterDiscontinuityTicks", "counter-discontinuity-ticks", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint32()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-counter-discontinuity-ticks-bad-value').infoFunc(): logFunc('counterDiscontinuityTicks not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCounterDiscontinuityTicks(tempVar)
            for logFunc in self._log('read-tag-values-counter-discontinuity-ticks').debug3Func(): logFunc('read counterDiscontinuityTicks. counterDiscontinuityTicks=%s, tempValue=%s', self.counterDiscontinuityTicks, tempValue.getType())
        
        if self.isMibIanaTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mib-iana-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mibianatype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mibIanaType", "mib-iana-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mib-iana-type-bad-value').infoFunc(): logFunc('mibIanaType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMibIanaType(tempVar)
            for logFunc in self._log('read-tag-values-mib-iana-type').debug3Func(): logFunc('read mibIanaType. mibIanaType=%s, tempValue=%s', self.mibIanaType, tempValue.getType())
        
        if self.isMibSpeed32BitRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mib-speed-32bit") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mibspeed32bit').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mibSpeed32Bit", "mib-speed-32bit", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint32()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mib-speed-32bit-bad-value').infoFunc(): logFunc('mibSpeed32Bit not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMibSpeed32Bit(tempVar)
            for logFunc in self._log('read-tag-values-mib-speed-32bit').debug3Func(): logFunc('read mibSpeed32Bit. mibSpeed32Bit=%s, tempValue=%s', self.mibSpeed32Bit, tempValue.getType())
        
        if self.isSpeedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "speed") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-speed').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "speed", "speed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-speed-bad-value').infoFunc(): logFunc('speed not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSpeed(tempVar)
            for logFunc in self._log('read-tag-values-speed').debug3Func(): logFunc('read speed. speed=%s, tempValue=%s', self.speed, tempValue.getType())
        
        if self.isConnectorPresentRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "connector-present") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-connectorpresent').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "connectorPresent", "connector-present", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-connector-present-bad-value').infoFunc(): logFunc('connectorPresent not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setConnectorPresent(tempVar)
            for logFunc in self._log('read-tag-values-connector-present').debug3Func(): logFunc('read connectorPresent. connectorPresent=%s, tempValue=%s', self.connectorPresent, tempValue.getType())
        
        if self.isOperationalStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "operational-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-operationalstatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "operationalStatus", "operational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-operational-status-bad-value').infoFunc(): logFunc('operationalStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOperationalStatus(tempVar)
            for logFunc in self._log('read-tag-values-operational-status').debug3Func(): logFunc('read operationalStatus. operationalStatus=%s, tempValue=%s', self.operationalStatus, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "interfaceIndex", 
            "yangName": "interface-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "speedMegabit", 
            "yangName": "speed-megabit", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mibAdminStatus", 
            "yangName": "mib-admin-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "promiscuous", 
            "yangName": "promiscuous", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mibName", 
            "yangName": "mib-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "mtu", 
            "yangName": "mtu", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "counterDiscontinuityTicks", 
            "yangName": "counter-discontinuity-ticks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mibIanaType", 
            "yangName": "mib-iana-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "mibSpeed32Bit", 
            "yangName": "mib-speed-32bit", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "speed", 
            "yangName": "speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "connectorPresent", 
            "yangName": "connector-present", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "interfaceIndex", 
            "yangName": "interface-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "speedMegabit", 
            "yangName": "speed-megabit", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mibAdminStatus", 
            "yangName": "mib-admin-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "promiscuous", 
            "yangName": "promiscuous", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "mibName", 
            "yangName": "mib-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "mtu", 
            "yangName": "mtu", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "counterDiscontinuityTicks", 
            "yangName": "counter-discontinuity-ticks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mibIanaType", 
            "yangName": "mib-iana-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "mibSpeed32Bit", 
            "yangName": "mib-speed-32bit", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "speed", 
            "yangName": "speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "connectorPresent", 
            "yangName": "connector-present", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


