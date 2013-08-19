 # Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.infra.basic.return_codes import ReturnCodes
from a.sys.net.lnx.device import DeviceUtils

from a.sys.net.tech_interfaces.tech.interfaces.interface.ethernet.status.blinky_status_oper_gen import BlinkyOperStatus

import a.infra.net.mac_address

G_NAME_GROUP_NET_INTERFACES_ETHERNET = "ethernet"

#-----------------------------------------------------------------------------------------------------------------------
class Ethernet(object):
    """This object displays ethernet card status.
    """
    def __init__(self, logger, interface=None):
        """
        Args:
            logger

        Raises:
            None
        """

        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_INTERFACES_ETHERNET)
        self.parent = interface

        self.blinkyEthernet = None

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyEthernet):
        self.blinkyEthernet = blinkyEthernet

#-----------------------------------------------------------------------------------------------------------------------
    def setOperErrorStr(self, tctx, msg):
        if self.blinkyEthernet is not None:
            self.blinkyEthernet.setTransError(tctx, msg)

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperStatusObj (self):
        blinkyOper = BlinkyOperStatus(self._log)
        blinkyOper.setFunctorTimeout(blinkyOper.GET_OBJ_FUNCTOR, 300)
        return blinkyOper

#-----------------------------------------------------------------------------------------------------------------------
    def getStatus(self, tctx, operData):

        self._log("ethernet-status").debug3("ethernet %s: get status was called. tctx=%s", self.parent.name, tctx)

        # mac address
        macAddress = self.parent.getMacAddress()
        if macAddress is not None:
            infraMacAddress = a.infra.net.mac_address.MacAddress(macAddress)
            operData.setMacAddress(infraMacAddress)

        self._log("ethernet-status-results").debug3("ethernet %s: status results=%s", self.parent.name, operData)
        return ReturnCodes.kOk





