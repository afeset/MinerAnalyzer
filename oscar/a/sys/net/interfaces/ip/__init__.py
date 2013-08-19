 # Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from address import IpNetwork  
from a.infra.basic.return_codes import ReturnCodes
import a.sys.blinky.util
from a.sys.blinky.util.simple_list_wrapper import SimpleStringList
import a.infra.process
import a.infra.net.ip_address

G_NAME_GROUP_NET_INTERFACES_IP = "ip"

class IpVersion(object):
    """ Standard ip versions. We keep the numerical values identical to the version values"""
    kIPv4 = 4
    kIPv6 = 6

#-----------------------------------------------------------------------------------------------------------------------
class _IpBase(object):
    """A generic IP network object.
    """

    class CreateIpFunc(object):
        def __init__ (self, version):
            self.version = version

        def __call__(self, logger, name):

            try:
                address = IpNetwork(logger, name, self.version)
            except ValueError as ex:
                logger("ip-addr-invalid").error("IPv%s Network '%s' is invalid: %s", self.version, name, ex)
                raise a.sys.blinky.util.common.ConfigError(("IPv%s Address '%s' is Invalid!" % (self.version, name)))

            addressWrapper = a.sys.blinky.util.simple_container_wrapper.SimpleContainerWrapper(logger, address)
            return addressWrapper

    def __init__(self, logger, version):
        """
        Args:
            version: an integer, 4 or 6

        Raises:
            None
        """

        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_INTERFACES_IP, instance=("ipv%s" % version))

        self.version = version
        self.candidateDefaultGateway = None
        self.runningDefaultGateway = None

        # holds a list of ip network addresses
        self.ipList = None
        self.blinkyIp = None

#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        strList = []

        ipList = self.ipList.runningValues()
        for address in ipList:
            strList.append("inet%s addr: %s" % (self.version, address))

        if self.candidateDefaultGateway:
            strList.append("ipv%s default gateway via %s" % (self.version, self.candidateDefaultGateway))

        return '\n'.join(strList) 

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyIp:
            self.blinkyIp.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def getCandidateAddress(self):
        if self.ipList is None:
            return None

        candidateIpList = self.ipList.candidateValues()

        if len(candidateIpList) == 0:
            return None

        return candidateIpList[0]

#-----------------------------------------------------------------------------------------------------------------------
    def overlaps(self, other):
        """Tell if self is partly contained in other."""

        if other is None:
            return False

        if (self.ipList is None) or (other.ipList is None):
            return False

        addressList = self.ipList.candidateValues()
        otherAddressList = other.ipList.candidateValues()

        for address in addressList:
            for otherAddress in otherAddressList:

                if address is None:
                    break

                if otherAddress is None:
                    break

                if address.overlaps(otherAddress) is True:
                    return True

        return False

#-----------------------------------------------------------------------------------------------------------------------
    def equals(self, other):
        """Tell if self source equals to other."""

        if other is None:
            return False

        if (self.ipList is None) or (other.ipList is None):
            return False

        addressList = self.ipList.candidateValues()
        otherAddressList = other.ipList.candidateValues()

        for address in addressList:
            for otherAddress in otherAddressList:

                if address is None:
                    break

                if otherAddress is None:
                    break

                if address.ip == otherAddress.ip:
                    return True

        return False

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):

        self._log("prepare-ip-data").debug3("prepare IPv%s data - %s", self.version, data)

        candidateDefaultGateway = None
        if data.hasDefaultGateway() and data.defaultGateway is not None:
            if (isinstance(data.defaultGateway, (int, long)) and data.defaultGateway>0) or len(data.defaultGateway) > 0:            

                # checks that the gateway is a valid ip address
                try:
                    gwIpAddress = a.infra.net.ip_address.IpAddress(data.defaultGateway, self.version)
                except ValueError as ex:
                    self._log("default-gw-invalid").notice("Gateway IPv%s '%s' is invalid: %s", self.version, data.defaultGateway, ex)
                    self.setConfigErrorStr("ipv%s default gateway %s is invalid" % (self.version, data.defaultGateway))
                    return ReturnCodes.kGeneralError
    
                candidateDefaultGateway = gwIpAddress

        # set candidate
        self.candidateDefaultGateway = candidateDefaultGateway

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateAfter(self):

        self._log("ip-prepare-private-after").debug3("IPv%s: preparePrivateAfter was called", self.version)

        ipsLen = 0
        if self.ipList is not None:
            candidateIpList = self.ipList.candidateValues()
            ipsLen = len(candidateIpList) 

        # must have up to one ip network subnet
        if ipsLen > 1:
            self._log("multiple-addresses-invalid").notice("Must have up to one ipv%s network address: %s", self.version, candidateIpList)
            self.setConfigErrorStr("multiple ipv%s addresses are not allowed" % self.version)
            return ReturnCodes.kGeneralError

        elif ipsLen == 1:

            deviceIpAddress = candidateIpList[0]

            if self.candidateDefaultGateway:
                
                # checks the the default gateway is in the device subnet
                # example: 192.168.10.9/255.255.255.0 --> 192.168.10.0 < X.X.X.X < 192.168.10.255
                # note: a.infra.net.ip_network.IpNetwork uses a fast hash based __contains__ (very efficient for IPv6)
                #       therefore, we use deviceIpAddress.address (and not deviceIpAddress)
                if not self.candidateDefaultGateway in deviceIpAddress.address:
                    self._log("gw-not-subnet").notice("IPv%s Gateway '%s' is not in interface subnet '%s'", 
                                                     self.version, self.candidateDefaultGateway, deviceIpAddress)
                    self.setConfigErrorStr("ipv%s default gateway %s is not in interface subnet %s" % 
                                           (self.version, self.candidateDefaultGateway, deviceIpAddress))
                    return ReturnCodes.kGeneralError

                # checks the default gateway is not the same as the device ip
                if self.candidateDefaultGateway == deviceIpAddress.ip:
                    self._log("gw-same-address").notice("IPv%s Gateway '%s' is the same address as its interface ip", 
                                                       self.version, self.candidateDefaultGateway)
                    self.setConfigErrorStr("ipv%s default gateway %s is the same address as its interface address" % 
                                           (self.version, self.candidateDefaultGateway))
                    return ReturnCodes.kGeneralError
                
                # checks the default gateway is valid
                if IpNetwork.s_isIpValid(self._log, self.candidateDefaultGateway, deviceIpAddress) is False:
                    self._log("gw-network").notice("IPv%s Gateway '%s' is invalid", self.version, self.candidateDefaultGateway)
                    self.setConfigErrorStr("ipv%s default gateway %s is invalid" % 
                                           (self.version, self.candidateDefaultGateway))
                    return ReturnCodes.kGeneralError

        else:
            # ipsLen == 0
            if self.candidateDefaultGateway:
                self._log("gw-with-no-subnet").notice("IPv%s Gateway '%s' cannot be configured without a network subnet", 
                                                     self.version, self.candidateDefaultGateway)
                self.setConfigErrorStr("ipv%s default gateway %s cannot be set when interface ip address is not set" % 
                                       (self.version, self.candidateDefaultGateway))
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        __pychecker__="no-argsused"  # data not used
        """the device changes are being aborted

            Raises:
                FATAL if fails
        """

        self.runningDefaultGateway = self.candidateDefaultGateway
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        __pychecker__="no-argsused"  # data not used
        """the device changes are being aborted

            Raises:
                FATAL if fails
        """

        self.candidateDefaultGateway = self.runningDefaultGateway
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyIp):

        self._log("notify-attach-blinky").debug2("attach by blinky ipv%s", self.version)
        self.blinkyIp = blinkyIp

        blinkyIp.setCreateAddressListFunctor(self.createAddressList)
        blinkyIp.setDeleteAddressListFunctor(self.deleteAddressList)

#-----------------------------------------------------------------------------------------------------------------------
    def createAddressList(self, phase, blinkyAddressList):
        self._log("create-address-list").debug2("phase=%s, blinkyAddressList=%s", phase, blinkyAddressList)

        if (phase.isPreparePrivate()):

            # holds a list of ip network addresses
            createIpFunctor = self.CreateIpFunc(self.version)
            self.ipList = a.sys.blinky.util.simple_list_wrapper.SimpleStringList(self._log, createIpFunctor)
            self.ipList.attachToBlinky(blinkyAddressList)

        elif (phase.isAbortPrivate()):
            self.ipList = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteAddressList(self, phase):
        self._log("delete-address-list").debug2("called, phase=%s, self=%s", phase)

        if (phase.isCommitPrivate()):
            self.ipList = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
class IPv4If(_IpBase):
    """An IPv4 network object.
    """

    def __init__(self, logger):
        version = IpVersion.kIPv4
        _IpBase.__init__(self, logger, version)

#-----------------------------------------------------------------------------------------------------------------------
class IPv6If(_IpBase):
    """An IPv6 network object.
    """

    def __init__(self, logger):
        version = IpVersion.kIPv6
        _IpBase.__init__(self, logger, version)


