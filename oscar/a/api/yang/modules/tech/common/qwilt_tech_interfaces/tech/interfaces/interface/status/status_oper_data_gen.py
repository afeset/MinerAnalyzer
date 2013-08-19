


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperData
__pychecker__="no-classattr"

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import OperationalStatusType
from a.api.yang.modules.common.qwilt_types.qwilt_types_module_gen import Truthvalue
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import MibAdminStatusType
from a.api.yang.modules.common.iana.iana_if_type_mib.iana_if_type_mib_module_gen import Ianaiftype


class StatusOperData (object):

    def __init__ (self):

        self.interfaceIndex = 0
        self._myHasInterfaceIndex=False
        self._myInterfaceIndexRequested=False
        
        self.speedMegabit = 0
        self._myHasSpeedMegabit=False
        self._mySpeedMegabitRequested=False
        
        self.mibAdminStatus = MibAdminStatusType.kDown
        self._myHasMibAdminStatus=False
        self._myMibAdminStatusRequested=False
        
        self.promiscuous = Truthvalue.kFalse
        self._myHasPromiscuous=False
        self._myPromiscuousRequested=False
        
        self.mibName = ""
        self._myHasMibName=False
        self._myMibNameRequested=False
        
        self.mtu = 0
        self._myHasMtu=False
        self._myMtuRequested=False
        
        self.counterDiscontinuityTicks = 0
        self._myHasCounterDiscontinuityTicks=False
        self._myCounterDiscontinuityTicksRequested=False
        
        self.mibIanaType = Ianaiftype.kIfGsn
        self._myHasMibIanaType=False
        self._myMibIanaTypeRequested=False
        
        self.mibSpeed32Bit = 0
        self._myHasMibSpeed32Bit=False
        self._myMibSpeed32BitRequested=False
        
        self.speed = 0
        self._myHasSpeed=False
        self._mySpeedRequested=False
        
        self.connectorPresent = Truthvalue.kFalse
        self._myHasConnectorPresent=False
        self._myConnectorPresentRequested=False
        
        self.operationalStatus = OperationalStatusType.kDown
        self._myHasOperationalStatus=False
        self._myOperationalStatusRequested=False
        


    def copyFrom (self, other):

        self.interfaceIndex=other.interfaceIndex
        self._myHasInterfaceIndex=other._myHasInterfaceIndex
        self._myInterfaceIndexRequested=other._myInterfaceIndexRequested
        
        self.speedMegabit=other.speedMegabit
        self._myHasSpeedMegabit=other._myHasSpeedMegabit
        self._mySpeedMegabitRequested=other._mySpeedMegabitRequested
        
        self.mibAdminStatus=other.mibAdminStatus
        self._myHasMibAdminStatus=other._myHasMibAdminStatus
        self._myMibAdminStatusRequested=other._myMibAdminStatusRequested
        
        self.promiscuous=other.promiscuous
        self._myHasPromiscuous=other._myHasPromiscuous
        self._myPromiscuousRequested=other._myPromiscuousRequested
        
        self.mibName=other.mibName
        self._myHasMibName=other._myHasMibName
        self._myMibNameRequested=other._myMibNameRequested
        
        self.mtu=other.mtu
        self._myHasMtu=other._myHasMtu
        self._myMtuRequested=other._myMtuRequested
        
        self.counterDiscontinuityTicks=other.counterDiscontinuityTicks
        self._myHasCounterDiscontinuityTicks=other._myHasCounterDiscontinuityTicks
        self._myCounterDiscontinuityTicksRequested=other._myCounterDiscontinuityTicksRequested
        
        self.mibIanaType=other.mibIanaType
        self._myHasMibIanaType=other._myHasMibIanaType
        self._myMibIanaTypeRequested=other._myMibIanaTypeRequested
        
        self.mibSpeed32Bit=other.mibSpeed32Bit
        self._myHasMibSpeed32Bit=other._myHasMibSpeed32Bit
        self._myMibSpeed32BitRequested=other._myMibSpeed32BitRequested
        
        self.speed=other.speed
        self._myHasSpeed=other._myHasSpeed
        self._mySpeedRequested=other._mySpeedRequested
        
        self.connectorPresent=other.connectorPresent
        self._myHasConnectorPresent=other._myHasConnectorPresent
        self._myConnectorPresentRequested=other._myConnectorPresentRequested
        
        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        self._myOperationalStatusRequested=other._myOperationalStatusRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isInterfaceIndexRequested():
            self.interfaceIndex=other.interfaceIndex
            self._myHasInterfaceIndex=other._myHasInterfaceIndex
            self._myInterfaceIndexRequested=other._myInterfaceIndexRequested
        
        if self.isSpeedMegabitRequested():
            self.speedMegabit=other.speedMegabit
            self._myHasSpeedMegabit=other._myHasSpeedMegabit
            self._mySpeedMegabitRequested=other._mySpeedMegabitRequested
        
        if self.isMibAdminStatusRequested():
            self.mibAdminStatus=other.mibAdminStatus
            self._myHasMibAdminStatus=other._myHasMibAdminStatus
            self._myMibAdminStatusRequested=other._myMibAdminStatusRequested
        
        if self.isPromiscuousRequested():
            self.promiscuous=other.promiscuous
            self._myHasPromiscuous=other._myHasPromiscuous
            self._myPromiscuousRequested=other._myPromiscuousRequested
        
        if self.isMibNameRequested():
            self.mibName=other.mibName
            self._myHasMibName=other._myHasMibName
            self._myMibNameRequested=other._myMibNameRequested
        
        if self.isMtuRequested():
            self.mtu=other.mtu
            self._myHasMtu=other._myHasMtu
            self._myMtuRequested=other._myMtuRequested
        
        if self.isCounterDiscontinuityTicksRequested():
            self.counterDiscontinuityTicks=other.counterDiscontinuityTicks
            self._myHasCounterDiscontinuityTicks=other._myHasCounterDiscontinuityTicks
            self._myCounterDiscontinuityTicksRequested=other._myCounterDiscontinuityTicksRequested
        
        if self.isMibIanaTypeRequested():
            self.mibIanaType=other.mibIanaType
            self._myHasMibIanaType=other._myHasMibIanaType
            self._myMibIanaTypeRequested=other._myMibIanaTypeRequested
        
        if self.isMibSpeed32BitRequested():
            self.mibSpeed32Bit=other.mibSpeed32Bit
            self._myHasMibSpeed32Bit=other._myHasMibSpeed32Bit
            self._myMibSpeed32BitRequested=other._myMibSpeed32BitRequested
        
        if self.isSpeedRequested():
            self.speed=other.speed
            self._myHasSpeed=other._myHasSpeed
            self._mySpeedRequested=other._mySpeedRequested
        
        if self.isConnectorPresentRequested():
            self.connectorPresent=other.connectorPresent
            self._myHasConnectorPresent=other._myHasConnectorPresent
            self._myConnectorPresentRequested=other._myConnectorPresentRequested
        
        if self.isOperationalStatusRequested():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasInterfaceIndex():
            self.interfaceIndex=other.interfaceIndex
            self._myHasInterfaceIndex=other._myHasInterfaceIndex
            self._myInterfaceIndexRequested=other._myInterfaceIndexRequested
        
        if other.hasSpeedMegabit():
            self.speedMegabit=other.speedMegabit
            self._myHasSpeedMegabit=other._myHasSpeedMegabit
            self._mySpeedMegabitRequested=other._mySpeedMegabitRequested
        
        if other.hasMibAdminStatus():
            self.mibAdminStatus=other.mibAdminStatus
            self._myHasMibAdminStatus=other._myHasMibAdminStatus
            self._myMibAdminStatusRequested=other._myMibAdminStatusRequested
        
        if other.hasPromiscuous():
            self.promiscuous=other.promiscuous
            self._myHasPromiscuous=other._myHasPromiscuous
            self._myPromiscuousRequested=other._myPromiscuousRequested
        
        if other.hasMibName():
            self.mibName=other.mibName
            self._myHasMibName=other._myHasMibName
            self._myMibNameRequested=other._myMibNameRequested
        
        if other.hasMtu():
            self.mtu=other.mtu
            self._myHasMtu=other._myHasMtu
            self._myMtuRequested=other._myMtuRequested
        
        if other.hasCounterDiscontinuityTicks():
            self.counterDiscontinuityTicks=other.counterDiscontinuityTicks
            self._myHasCounterDiscontinuityTicks=other._myHasCounterDiscontinuityTicks
            self._myCounterDiscontinuityTicksRequested=other._myCounterDiscontinuityTicksRequested
        
        if other.hasMibIanaType():
            self.mibIanaType=other.mibIanaType
            self._myHasMibIanaType=other._myHasMibIanaType
            self._myMibIanaTypeRequested=other._myMibIanaTypeRequested
        
        if other.hasMibSpeed32Bit():
            self.mibSpeed32Bit=other.mibSpeed32Bit
            self._myHasMibSpeed32Bit=other._myHasMibSpeed32Bit
            self._myMibSpeed32BitRequested=other._myMibSpeed32BitRequested
        
        if other.hasSpeed():
            self.speed=other.speed
            self._myHasSpeed=other._myHasSpeed
            self._mySpeedRequested=other._mySpeedRequested
        
        if other.hasConnectorPresent():
            self.connectorPresent=other.connectorPresent
            self._myHasConnectorPresent=other._myHasConnectorPresent
            self._myConnectorPresentRequested=other._myConnectorPresentRequested
        
        if other.hasOperationalStatus():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.interfaceIndex=other.interfaceIndex
        self._myHasInterfaceIndex=other._myHasInterfaceIndex
        
        self.speedMegabit=other.speedMegabit
        self._myHasSpeedMegabit=other._myHasSpeedMegabit
        
        self.mibAdminStatus=other.mibAdminStatus
        self._myHasMibAdminStatus=other._myHasMibAdminStatus
        
        self.promiscuous=other.promiscuous
        self._myHasPromiscuous=other._myHasPromiscuous
        
        self.mibName=other.mibName
        self._myHasMibName=other._myHasMibName
        
        self.mtu=other.mtu
        self._myHasMtu=other._myHasMtu
        
        self.counterDiscontinuityTicks=other.counterDiscontinuityTicks
        self._myHasCounterDiscontinuityTicks=other._myHasCounterDiscontinuityTicks
        
        self.mibIanaType=other.mibIanaType
        self._myHasMibIanaType=other._myHasMibIanaType
        
        self.mibSpeed32Bit=other.mibSpeed32Bit
        self._myHasMibSpeed32Bit=other._myHasMibSpeed32Bit
        
        self.speed=other.speed
        self._myHasSpeed=other._myHasSpeed
        
        self.connectorPresent=other.connectorPresent
        self._myHasConnectorPresent=other._myHasConnectorPresent
        
        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        


    def setAllNumericToZero (self):
        
        self.interfaceIndex=0
        self.setHasInterfaceIndex()
        self.speedMegabit=0
        self.setHasSpeedMegabit()
        self.mtu=0
        self.setHasMtu()
        self.counterDiscontinuityTicks=0
        self.setHasCounterDiscontinuityTicks()
        self.mibSpeed32Bit=0
        self.setHasMibSpeed32Bit()
        self.speed=0
        self.setHasSpeed()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasInterfaceIndex():
            if other.hasInterfaceIndex():
                self.interfaceIndex -= other.interfaceIndex
        
        if self.hasSpeedMegabit():
            if other.hasSpeedMegabit():
                self.speedMegabit -= other.speedMegabit
        
        if self.hasMtu():
            if other.hasMtu():
                self.mtu -= other.mtu
        
        if self.hasCounterDiscontinuityTicks():
            if other.hasCounterDiscontinuityTicks():
                self.counterDiscontinuityTicks -= other.counterDiscontinuityTicks
        
        if self.hasMibSpeed32Bit():
            if other.hasMibSpeed32Bit():
                self.mibSpeed32Bit -= other.mibSpeed32Bit
        
        if self.hasSpeed():
            if other.hasSpeed():
                self.speed -= other.speed
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasInterfaceIndex():
            if other.hasInterfaceIndex():
                self.interfaceIndex += other.interfaceIndex
        
        if self.hasSpeedMegabit():
            if other.hasSpeedMegabit():
                self.speedMegabit += other.speedMegabit
        
        if self.hasMtu():
            if other.hasMtu():
                self.mtu += other.mtu
        
        if self.hasCounterDiscontinuityTicks():
            if other.hasCounterDiscontinuityTicks():
                self.counterDiscontinuityTicks += other.counterDiscontinuityTicks
        
        if self.hasMibSpeed32Bit():
            if other.hasMibSpeed32Bit():
                self.mibSpeed32Bit += other.mibSpeed32Bit
        
        if self.hasSpeed():
            if other.hasSpeed():
                self.speed += other.speed
        
        
        pass


    # has...() methods

    def hasInterfaceIndex (self):
        return self._myHasInterfaceIndex

    def hasSpeedMegabit (self):
        return self._myHasSpeedMegabit

    def hasMibAdminStatus (self):
        return self._myHasMibAdminStatus

    def hasPromiscuous (self):
        return self._myHasPromiscuous

    def hasMibName (self):
        return self._myHasMibName

    def hasMtu (self):
        return self._myHasMtu

    def hasCounterDiscontinuityTicks (self):
        return self._myHasCounterDiscontinuityTicks

    def hasMibIanaType (self):
        return self._myHasMibIanaType

    def hasMibSpeed32Bit (self):
        return self._myHasMibSpeed32Bit

    def hasSpeed (self):
        return self._myHasSpeed

    def hasConnectorPresent (self):
        return self._myHasConnectorPresent

    def hasOperationalStatus (self):
        return self._myHasOperationalStatus




    # setHas...() methods

    def setHasInterfaceIndex (self):
        self._myHasInterfaceIndex=True

    def setHasSpeedMegabit (self):
        self._myHasSpeedMegabit=True

    def setHasMibAdminStatus (self):
        self._myHasMibAdminStatus=True

    def setHasPromiscuous (self):
        self._myHasPromiscuous=True

    def setHasMibName (self):
        self._myHasMibName=True

    def setHasMtu (self):
        self._myHasMtu=True

    def setHasCounterDiscontinuityTicks (self):
        self._myHasCounterDiscontinuityTicks=True

    def setHasMibIanaType (self):
        self._myHasMibIanaType=True

    def setHasMibSpeed32Bit (self):
        self._myHasMibSpeed32Bit=True

    def setHasSpeed (self):
        self._myHasSpeed=True

    def setHasConnectorPresent (self):
        self._myHasConnectorPresent=True

    def setHasOperationalStatus (self):
        self._myHasOperationalStatus=True




    # isRequested...() methods

    def isInterfaceIndexRequested (self):
        return self._myInterfaceIndexRequested

    def isSpeedMegabitRequested (self):
        return self._mySpeedMegabitRequested

    def isMibAdminStatusRequested (self):
        return self._myMibAdminStatusRequested

    def isPromiscuousRequested (self):
        return self._myPromiscuousRequested

    def isMibNameRequested (self):
        return self._myMibNameRequested

    def isMtuRequested (self):
        return self._myMtuRequested

    def isCounterDiscontinuityTicksRequested (self):
        return self._myCounterDiscontinuityTicksRequested

    def isMibIanaTypeRequested (self):
        return self._myMibIanaTypeRequested

    def isMibSpeed32BitRequested (self):
        return self._myMibSpeed32BitRequested

    def isSpeedRequested (self):
        return self._mySpeedRequested

    def isConnectorPresentRequested (self):
        return self._myConnectorPresentRequested

    def isOperationalStatusRequested (self):
        return self._myOperationalStatusRequested




    # setRequested...() methods

    def setInterfaceIndexRequested (self):
        self._myInterfaceIndexRequested=True

    def setSpeedMegabitRequested (self):
        self._mySpeedMegabitRequested=True

    def setMibAdminStatusRequested (self):
        self._myMibAdminStatusRequested=True

    def setPromiscuousRequested (self):
        self._myPromiscuousRequested=True

    def setMibNameRequested (self):
        self._myMibNameRequested=True

    def setMtuRequested (self):
        self._myMtuRequested=True

    def setCounterDiscontinuityTicksRequested (self):
        self._myCounterDiscontinuityTicksRequested=True

    def setMibIanaTypeRequested (self):
        self._myMibIanaTypeRequested=True

    def setMibSpeed32BitRequested (self):
        self._myMibSpeed32BitRequested=True

    def setSpeedRequested (self):
        self._mySpeedRequested=True

    def setConnectorPresentRequested (self):
        self._myConnectorPresentRequested=True

    def setOperationalStatusRequested (self):
        self._myOperationalStatusRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myInterfaceIndexRequested:
            x = "+InterfaceIndex="
            if self._myHasInterfaceIndex:
                leafStr = str(self.interfaceIndex)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySpeedMegabitRequested:
            x = "+SpeedMegabit="
            if self._myHasSpeedMegabit:
                leafStr = str(self.speedMegabit)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMibAdminStatusRequested:
            x = "+MibAdminStatus="
            if self._myHasMibAdminStatus:
                leafStr = str(self.mibAdminStatus)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPromiscuousRequested:
            x = "+Promiscuous="
            if self._myHasPromiscuous:
                leafStr = str(self.promiscuous)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMibNameRequested:
            x = "+MibName="
            if self._myHasMibName:
                leafStr = str(self.mibName)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMtuRequested:
            x = "+Mtu="
            if self._myHasMtu:
                leafStr = str(self.mtu)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myCounterDiscontinuityTicksRequested:
            x = "+CounterDiscontinuityTicks="
            if self._myHasCounterDiscontinuityTicks:
                leafStr = str(self.counterDiscontinuityTicks)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMibIanaTypeRequested:
            x = "+MibIanaType="
            if self._myHasMibIanaType:
                leafStr = str(self.mibIanaType)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMibSpeed32BitRequested:
            x = "+MibSpeed32Bit="
            if self._myHasMibSpeed32Bit:
                leafStr = str(self.mibSpeed32Bit)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySpeedRequested:
            x = "+Speed="
            if self._myHasSpeed:
                leafStr = str(self.speed)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myConnectorPresentRequested:
            x = "+ConnectorPresent="
            if self._myHasConnectorPresent:
                leafStr = str(self.connectorPresent)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOperationalStatusRequested:
            x = "+OperationalStatus="
            if self._myHasOperationalStatus:
                leafStr = str(self.operationalStatus)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+InterfaceIndex="
        if self._myHasInterfaceIndex:
            leafStr = str(self.interfaceIndex)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInterfaceIndexRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+SpeedMegabit="
        if self._myHasSpeedMegabit:
            leafStr = str(self.speedMegabit)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySpeedMegabitRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MibAdminStatus="
        if self._myHasMibAdminStatus:
            leafStr = str(self.mibAdminStatus)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMibAdminStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Promiscuous="
        if self._myHasPromiscuous:
            leafStr = str(self.promiscuous)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPromiscuousRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MibName="
        if self._myHasMibName:
            leafStr = str(self.mibName)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMibNameRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Mtu="
        if self._myHasMtu:
            leafStr = str(self.mtu)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMtuRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+CounterDiscontinuityTicks="
        if self._myHasCounterDiscontinuityTicks:
            leafStr = str(self.counterDiscontinuityTicks)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCounterDiscontinuityTicksRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MibIanaType="
        if self._myHasMibIanaType:
            leafStr = str(self.mibIanaType)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMibIanaTypeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MibSpeed32Bit="
        if self._myHasMibSpeed32Bit:
            leafStr = str(self.mibSpeed32Bit)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMibSpeed32BitRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Speed="
        if self._myHasSpeed:
            leafStr = str(self.speed)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySpeedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ConnectorPresent="
        if self._myHasConnectorPresent:
            leafStr = str(self.connectorPresent)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myConnectorPresentRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OperationalStatus="
        if self._myHasOperationalStatus:
            leafStr = str(self.operationalStatus)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOperationalStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setInterfaceIndexRequested()
        self.setSpeedMegabitRequested()
        self.setMibAdminStatusRequested()
        self.setPromiscuousRequested()
        self.setMibNameRequested()
        self.setMtuRequested()
        self.setCounterDiscontinuityTicksRequested()
        self.setMibIanaTypeRequested()
        self.setMibSpeed32BitRequested()
        self.setSpeedRequested()
        self.setConnectorPresentRequested()
        self.setOperationalStatusRequested()
        
        


    def setInterfaceIndex (self, interfaceIndex):
        self.interfaceIndex = interfaceIndex
        self.setHasInterfaceIndex()

    def setSpeedMegabit (self, speedMegabit):
        self.speedMegabit = speedMegabit
        self.setHasSpeedMegabit()

    def setMibAdminStatus (self, mibAdminStatus):
        self.mibAdminStatus = mibAdminStatus
        self.setHasMibAdminStatus()

    def setPromiscuous (self, promiscuous):
        self.promiscuous = promiscuous
        self.setHasPromiscuous()

    def setMibName (self, mibName):
        self.mibName = mibName
        self.setHasMibName()

    def setMtu (self, mtu):
        self.mtu = mtu
        self.setHasMtu()

    def setCounterDiscontinuityTicks (self, counterDiscontinuityTicks):
        self.counterDiscontinuityTicks = counterDiscontinuityTicks
        self.setHasCounterDiscontinuityTicks()

    def setMibIanaType (self, mibIanaType):
        self.mibIanaType = mibIanaType
        self.setHasMibIanaType()

    def setMibSpeed32Bit (self, mibSpeed32Bit):
        self.mibSpeed32Bit = mibSpeed32Bit
        self.setHasMibSpeed32Bit()

    def setSpeed (self, speed):
        self.speed = speed
        self.setHasSpeed()

    def setConnectorPresent (self, connectorPresent):
        self.connectorPresent = connectorPresent
        self.setHasConnectorPresent()

    def setOperationalStatus (self, operationalStatus):
        self.operationalStatus = operationalStatus
        self.setHasOperationalStatus()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "interfaces", 
            "isCurrent": false
        }, 
        {
            "namespace": "interface", 
            "isCurrent": false
        }, 
        {
            "namespace": "status", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "interfaceIndex", 
            "yangName": "interface-index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "speedMegabit", 
            "yangName": "speed-megabit", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mibAdminStatus", 
            "yangName": "mib-admin-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "promiscuous", 
            "yangName": "promiscuous", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "mibName", 
            "yangName": "mib-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "mtu", 
            "yangName": "mtu", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "counterDiscontinuityTicks", 
            "yangName": "counter-discontinuity-ticks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "mibIanaType", 
            "yangName": "mib-iana-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "mibSpeed32Bit", 
            "yangName": "mib-speed-32bit", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "speed", 
            "yangName": "speed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "connectorPresent", 
            "yangName": "connector-present", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
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
    "createTime": "2013"
}
"""


