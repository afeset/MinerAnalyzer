# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.sys.net.interfaces import IfContainerBase
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.enum_with_value import EnumWithValue
from ip import IpVersion
import copy

##############################################
# This class listens and notifies network configuration changes
##############################################
class IfClient(IfContainerBase):
    """This class works for the network configuration"""

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger, name, ifNotifier):
        
        if ifNotifier.mng is None and ifNotifier.delivery is None and ifNotifier.delivery2 is None:
            raise ValueError("notifier object is invalid!")
                    
        IfContainerBase.__init__(self, logger, name, False, True)      

        # interface notification on change
        self.ifNotifier = ifNotifier

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateAfter(self):
        self.notifyAfterChange()
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAfterChange(self):

        interfaces = self.interfaceList.runningValues()

        mngIf = None
        deliveryIf  = None
        delivery2If = None

        # detect the diffrent interfacs
        for currentI in interfaces:
            if currentI.isManagementEnabled() is True:
                if not currentI.candidateTechMode:
                    self._log("client-mng-interface").debug3("%s: management interface detected", currentI.name)
                    mngIf = currentI
            elif currentI.isDeliveryEnabled():
                if deliveryIf is None:
                    self._log("client-delivery-interface").debug3("%s: delivery interface detected", currentI.name)
                    deliveryIf = currentI
                else:
                    self._log("client-delivery2-interface").debug3("%s: 2nd delivery interface detected", currentI.name)
                    delivery2If = currentI

        mngIfPair       = None
        deliveryIfPair  = None
        delivery2IfPair = None

        # check for configuration change in the diffrent interfacs
        if self.ifNotifier.mng and mngIf:
            data = self.getInterfaceDataDiff(mngIf, self.ifNotifier.mng)
            if data is not None:
                mngIfPair = (mngIf.name, data)

        ######################
        # temp@2.7 - 1/15/2013
        deliveryStabilityDelay = 0
        if deliveryIf:
            deliveryStabilityDelay = max(deliveryStabilityDelay, deliveryIf.deliveryStabilityDelay)

        if delivery2If:
            deliveryStabilityDelay = max(deliveryStabilityDelay, delivery2If.deliveryStabilityDelay)
        ######################

        if self.ifNotifier.delivery and deliveryIf:
            data = self.getInterfaceDataDiff(deliveryIf, self.ifNotifier.delivery)
            if data is not None:
                data.setValueByKey("deliveryStabilityDelay", deliveryStabilityDelay)
                deliveryIfPair = (deliveryIf.name, data)

        if self.ifNotifier.delivery2 and delivery2If:
            data = self.getInterfaceDataDiff(delivery2If, self.ifNotifier.delivery2)
            if data is not None:
                data.setValueByKey("deliveryStabilityDelay", deliveryStabilityDelay)
                delivery2IfPair = (delivery2If.name, data)

        if mngIfPair or deliveryIfPair or delivery2IfPair:
            self.ifNotifier.notifyChangeOnInterfaces(mng=mngIfPair, 
                                                     delivery=deliveryIfPair, 
                                                     delivery2=delivery2IfPair)

#-----------------------------------------------------------------------------------------------------------------------
    def getDataFromInterface(self, interface, dataMember):

        data = ""

        # ipv4
        if IfDataMembers.kIpAddress == dataMember:
            address = interface.getIpAddress(IpVersion.kIPv4)
            if not address is None:
                data = str(address)
        elif IfDataMembers.kDefaultGateway == dataMember:
            gateway = interface.getDefaultGateway(IpVersion.kIPv4)
            if not gateway is None:
                data = str(gateway)
        #ipv6
        elif IfDataMembers.kIpv6Address == dataMember:
            address = interface.getIpAddress(IpVersion.kIPv6)
            if not address is None:
                data = str(address)
        elif IfDataMembers.kIpv6DefaultGateway == dataMember:
            gateway = interface.getDefaultGateway(IpVersion.kIPv6)
            if not gateway is None:
                data = str(gateway)

        elif IfDataMembers.kDeviceName == dataMember:
            data = interface.deviceName()
        elif IfDataMembers.kEnable == dataMember: 
            data = interface.candidateEnabled
        else:
            raise NotImplementedError

        return data

#-----------------------------------------------------------------------------------------------------------------------
    def getInterfaceDataDiff(self, interface, interfaceDataInfo):
        
        if not interface is None:
            self._log("client-notify-interface").debug3("%s: notify interface with data: %s", interface.name, interfaceDataInfo)

            dataDelta = InterfaceDataInfo()
    
            for dataMember in IfDataMember.iteritems():
                if interfaceDataInfo.isOn(dataMember):
    
                    currentValue = self.getDataFromInterface(interface, dataMember)
                    prevValue = interfaceDataInfo.getByKey(dataMember)
    
                    # set value (if changed)
                    if currentValue != prevValue:
                        dataDelta.setValueByKey(dataMember, currentValue)
                        interfaceDataInfo.setValueByKey(dataMember, currentValue)
    
            if dataDelta.hasData():
                self._log("client-interface-data-delta").debug3("%s: data changes are <%s>", 
                                                                interface.name, dataDelta)
                return dataDelta

        return None

#-----------------------------------------------------------------------------------------------------------------------
class InterfaceCfgNotifier(object):
    def __init__(self, mng=None, delivery=None, delivery2=None):

        if mng and not isinstance(mng, InterfaceDataInfo):
            raise TypeError("%s is not a InterfaceDataInfo object" % str(mng))

        if delivery and not isinstance(delivery, InterfaceDataInfo):
            raise TypeError("%s is not a InterfaceDataInfo object" % str(delivery))

        if delivery2 and not isinstance(delivery2, InterfaceDataInfo):
            raise TypeError("%s is not a InterfaceDataInfo object" % str(delivery2))

        self.mng =  copy.copy(mng)
        self.delivery  = copy.copy(delivery)
        self.delivery2 = copy.copy(delivery2)

    # each interface (if exists) is a pair <key,data>
    def notifyChangeOnInterfaces(self, mng=None, delivery=None, delivery2=None):
        __pychecker__="no-argsused"  # args not used
        pass

    def __str__(self):
        strList = []
        
        if self.mng:
            strList.append("managment interface: %s" % self.mng)
        
        if self.delivery:
            strList.append("1st delivery interface: %s" % self.delivery)
        
        if self.delivery2:
            strList.append("2nd delivery interface: %s" % self.delivery2)
        
        return '\t'.join(strList) 

#-----------------------------------------------------------------------------------------------------------------------
class InterfaceDataInfo(object):

    def __init__(self, *args):

        for key in args:
            if not isinstance(key, IfDataMember):
                raise TypeError("%s is not a IfDataMember object" % str(key))

            name = key.getName()
            setattr(self, name, "")

    def getByKey(self, key):
        return self.__dict__.get(str(key), "")

    def setValueByKey(self, key, value):
        self.__dict__[str(key)] = value

    def isOn(self, key):
        return str(key) in self.__dict__

    def hasData(self):
        return (len(self.__dict__) > 0)

    def __str__(self):
        return str(self.__dict__)

#-----------------------------------------------------------------------------------------------------------------------
class IfDataMember(EnumWithValue):
    """contains a single data member"""
    def __init__ (self, value, name):
        EnumWithValue.__init__(self, value, name)

class IfDataMembers(object):
    """ optional data members """
    kIpAddress          = IfDataMember(0, "kIpv4Address")
    kDefaultGateway     = IfDataMember(1, "kIpv4DefaultGateway")
    kIpv6Address        = IfDataMember(2, "kIpv6Address")
    kIpv6DefaultGateway = IfDataMember(3, "kIpv6DefaultGateway")
    kDeviceName         = IfDataMember(4, "kDeviceName")
    kEnable             = IfDataMember(5, "kEnable")
