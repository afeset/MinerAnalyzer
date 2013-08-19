# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave


from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper
from a.sys.blinky.util.simple_list_wrapper import SimpleStringList
from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.delivery.delivery_data_gen import DeliveryData
from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.delivery.delivery_data_gen import DeliveryData as ContentDeliveryData

from a.sys.net.tech_content_interfaces.tech.content.interfaces.interface.delivery.ipv4.status.blinky_status_oper_gen import BlinkyOperStatus as Ipv4BlinkyOperStatus
from a.sys.net.tech_content_interfaces.tech.content.interfaces.interface.delivery.ipv6.status.blinky_status_oper_gen import BlinkyOperStatus as Ipv6BlinkyOperStatus


import os
import a.infra.format.json

G_NAME_GROUP_NET_CONTENT_INTERFACE = "content-interface"
      
class ContentIfTable(SimpleStringList):
    """A content interface table object.
    """

    class CreateContentInterfaceFunc(object):
        def __init__(self, setStatusFunc):
            self.setStatusFunc = setStatusFunc

        def __call__(self, logger, name):

            logger("create-content-interface").debug3("%s: creates content interface", name)
            interface = ContentInterface(logger, name, self.setStatusFunc)
            interfaceWrapper = SimpleContainerWrapper(logger, interface)

            return interfaceWrapper

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger):
        
        createContentInterfaceFunc = self.CreateContentInterfaceFunc(self.setInterfaceStatus)
        self.statusFileName = None
        SimpleStringList.__init__(self, logger, createContentInterfaceFunc)

#-----------------------------------------------------------------------------------------------------------------------
    def setStatusFile(self, filename):
        self.statusFileName = filename

#-----------------------------------------------------------------------------------------------------------------------
    def setInterfaceStatus(self, interfaceName, operData, version=4):
        self._log("interface-set-status").debug1("%s: ipv%s setInterfaceStatus() was called", interfaceName, version)

        if self.statusFileName and os.path.exists(self.statusFileName):
            data = a.infra.format.json.readFromFile(self._log, self.statusFileName)
            self._log("interface-set-status").debug2("%s: ipv%s status read from file - %s", interfaceName, version, data)
            lineInterfaces = data.get("lineInterfaces",None)
            if lineInterfaces:
                for line in lineInterfaces:
                    if line["interfaceName"] == interfaceName:
                        if version == 4:
                            operData.setActualDeliveryInterface(line.get("ipv4ActualDeliveryInterface", "none"))
                        else:
                            operData.setActualDeliveryInterface(line.get("ipv6ActualDeliveryInterface", "none"))
                        break

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateOnCreate(self, name, blinkyIfTable):

        # interface creation after trigger is not premitted
        if blinkyIfTable.isInTrigger() is False:
            self._log("interface-create-after-trigger").error("%s: create interface after trigger", name)
            blinkyIfTable.setConfigErrorStr("Interface '%s' cannot be created" % name)
            
            return ReturnCodes.kGeneralError

        return SimpleStringList.preparePrivateOnCreate(self, name, blinkyIfTable)

##############################################
# This class manages the global system network
##############################################
class ContentInterface(object):
    """This class represents a content interface"""

    def __init__ (self, logger, name, setStatusFunc):
        """Instantiate a new content interface object.

        Args:
            name: the interface name

        Raises:
            None
        """

        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_CONTENT_INTERFACE)
        self.name = name
        self.setStatusFunc = setStatusFunc

        # data
        self.delivery = None

        self.blinkyInterface = None
                        
#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        return "%s: delivery=%s" % (self.name, self.delivery)

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyInterface):
        self.blinkyInterface = blinkyInterface

        self._log("notify-attach-blinky").debug2("%s: attach by blinky interface", self.name)

        # Delivery
        blinkyInterface.setCreateDeliveryFunctor(self.createDelivery)
        blinkyInterface.setDeleteDeliveryFunctor(self.deleteDelivery)

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyInterface:
            self.blinkyInterface.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def createDelivery(self, phase, blinkyDelivery):
        self._log("create-delivery").debug2("%s: blinkyDelivery=%s", phase, blinkyDelivery)

        if (phase.isPreparePrivate()):

            delivery = DeliveryContainer(self._log, self)
            self.delivery = SimpleContainerWrapper(self._log, delivery)
            self.delivery.attachToBlinky(blinkyDelivery)

        elif (phase.isAbortPrivate()):
            self.delivery = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteDelivery(self, phase):
        self._log("delete-delivery").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.delivery = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateDestroySelf(self):
        self._log("content-interface-destroy-self").debug2("%s: destroy interface", self.name)
        self.setConfigErrorStr("content interface '%s' cannot be deleted" % self.name)

        return ReturnCodes.kGeneralError

#-----------------------------------------------------
class DeliveryContainer(object):
    """This class represents a delivery container"""

    def __init__ (self, logger, parent):
        """Instantiate a new content interface object.
        """

        self._log = logger
        self.parent = parent

        # data
        self.candidatePreferredDeliveryInterface = ""
        self.runningData = DeliveryData()

        self.ipv4 = None
        self.ipv6 = None

        self.blinkyDelivery = None
                        
#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        return str(self.runningData)

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyDelivery):
        self.blinkyDelivery = blinkyDelivery

        # ipv4
        blinkyDelivery.setCreateIpv4Functor(self.createIpv4)
        blinkyDelivery.setDeleteIpv4Functor(self.deleteIpv4)

        # ipv6
        blinkyDelivery.setCreateIpv6Functor(self.createIpv6)
        blinkyDelivery.setDeleteIpv6Functor(self.deleteIpv6)

        self._log("notify-attach-blinky").debug2("%s: attach by blinky delivery", self.parent.name)

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyDelivery:
            self.blinkyDelivery.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def createIpv4(self, phase, blinkyIpv4):
        self._log("create-ipv4").debug2("%s: blinkyIpv4=%s", phase, blinkyIpv4)

        if (phase.isPreparePrivate()):

            ipv4 = DeliveryIpv4Status(self._log, self.parent)
            self.ipv4 = SimpleContainerWrapper(self._log, ipv4,setOperDataFunctor=True)
            self.ipv4.attachToBlinky(blinkyIpv4)

        elif (phase.isCommitPublic()):
            self.ipv4.attachToBlinkyOper()
        elif (phase.isAbortPrivate()):
            self.ipv4 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteIpv4(self, phase):
        self._log("delete-ipv4").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.ipv4 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createIpv6(self, phase, blinkyIpv6):
        self._log("create-ipv6").debug2("%s: blinkyIpv6=%s", phase, blinkyIpv6)

        if (phase.isPreparePrivate()):

            ipv6 = DeliveryIpv6Status(self._log, self.parent)
            self.ipv6 = SimpleContainerWrapper(self._log, ipv6,setOperDataFunctor=True)
            self.ipv6.attachToBlinky(blinkyIpv6)

        elif (phase.isCommitPublic()):
            self.ipv6.attachToBlinkyOper()
        elif (phase.isAbortPrivate()):
            self.ipv6 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteIpv6(self, phase):
        self._log("delete-ipv6").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.ipv6 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        self._log("content-interface-delivery-prepare-private-value-set").debug4("%s: prepare data - %s", self.parent.name, data)

        self.candidatePreferredDeliveryInterface = data.preferredDeliveryInterface

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        self._log("content-interface-delivery-abort-private-value-set").debug4("%s: abort data - %s", self.parent.name, data)

        self.candidatePreferredDeliveryInterface = self.runningData.preferredDeliveryInterface

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        self._log("content-interface-delivery-commit-private-value-set").debug4("%s: commit data - %s", self.parent.name, data)

        # copy data
        self.runningData.copyFrom(data)
                                    
        return ReturnCodes.kOk

#-----------------------------------------------------
class _DeliveryIpStatus(object):
    """This class represents a delivery ip status container"""

    def __init__ (self, logger, interface, version):
        """Instantiate a new ip status object.
        """
        self._log = logger
        self.interface = interface
        self.version = version

        self.blinkyIp = None
                        
#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyIp):
        self.blinkyIp = blinkyIp

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperStatusObj (self):
        raise NotImplementedError

#-----------------------------------------------------------------------------------------------------------------------
    def getStatus(self, tctx, operData):
        interfaceName = self.interface.name

        self._log("content-interface-delivery-status").debug3("%s: get status was called. tctx=%s", interfaceName, tctx)

        self.interface.setStatusFunc(interfaceName, operData, self.version)

        self._log("interface-status-data").debug3("%s: get status oper data=%s", interfaceName, operData)
        return ReturnCodes.kOk

class DeliveryIpv4Status(_DeliveryIpStatus):
    """IPv4 delivery status object.
    """

    def __init__(self, logger, interface):
        _DeliveryIpStatus.__init__(self, logger, interface, 4)

    def getBlinkyOperStatusObj (self):
        return Ipv4BlinkyOperStatus(self._log)

class DeliveryIpv6Status(_DeliveryIpStatus):
    """IPv6 delivery status object.
    """

    def __init__(self, logger, interface):
        _DeliveryIpStatus.__init__(self, logger, interface, 6)

    def getBlinkyOperStatusObj (self):
        return Ipv6BlinkyOperStatus(self._log)

#-----------------------------------------------------
class ContentDeliveryContainer(object):
    """This class represents a content delivery container @ /tech/content/delivery"""

    def __init__ (self, logger, parent):
        """Instantiate a new content delivery object.
        """

        self._log = logger
        self.parent = parent

        # data
        self.candidateDeliveryInterfaceFailover = True
        self.runningData = ContentDeliveryData()

        self.blinkyDelivery = None
                        
#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        return str(self.runningData)

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyDelivery):
        self.blinkyDelivery = blinkyDelivery

        self._log("notify-attach-blinky").debug2("%s: attach by blinky content delivery", self.parent.name)

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        self._log("content-delivery-prepare-private-value-set").debug4("%s: prepare data - %s", self.parent.name, data)

        self.candidateDeliveryInterfaceFailover = data.deliveryInterfaceFailover

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        self._log("content-delivery-abort-private-value-set").debug4("%s: abort data - %s", self.parent.name, data)

        self.candidateDeliveryInterfaceFailover = self.runningData.deliveryInterfaceFailover

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        self._log("content-interface-delivery-commit-private-value-set").debug4("%s: commit data - %s", self.parent.name, data)

        # copy data
        self.runningData.copyFrom(data)
                                    
        return ReturnCodes.kOk
