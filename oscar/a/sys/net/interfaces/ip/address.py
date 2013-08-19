# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

import google.ipaddr
import a.infra.net.ip_network

G_NAME_GROUP_NET_INTERFACES_IP_ADDRESS = "address"

#-----------------------------------------------------------------------------------------------------------------------
class IpNetwork(object):
    """A generic IPv4 or IPv6 Network Address object.
    """

    def __init__(self, logger, address, version):
        """
        Args:
            version: an integer, 4 or 6

        Raises:
            None
        """

        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_INTERFACES_IP_ADDRESS)
        self.version = version
        self.address =  a.infra.net.ip_network.IpNetwork(address, self.version)

        if self._isValid() is False:
            logger("address-not-valid").error("Ip '%s' is invalid", address)
            raise ValueError('%r does not appear to be a valid IP' % address)

#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):     
        return str(self.address) 

#-----------------------------------------------------------------------------------------------------------------------
    def __eq__(self, other):
        try:
            return (self.address == other.address)
        except AttributeError:
            return NotImplemented

#-----------------------------------------------------------------------------------------------------------------------
    def __hash__(self):
        return hash(self.address)

#-----------------------------------------------------------------------------------------------------------------------
    def __iter__(self):
        return self.address.__iter__()
            
#-----------------------------------------------------------------------------------------------------------------------
    def __getattr__(self, name):
        return self.address.__getattribute__(name)
                  
#-----------------------------------------------------------------------------------------------------------------------
    def _isValid(self):
        return IpNetwork.s_isIpValid(self._log, self.address.ip, self.address)
                          
#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def s_isIpValid(logger, ip, subnet):

        # supports inhertiance: 
        # (1) a.infra.net.ip_address.IpAddress (derived class) 
        # (2) google.ipaddr.IPAddress (base class)
        if not (isinstance(ip, google.ipaddr.IPv4Address) or isinstance(ip, google.ipaddr.IPv6Address)):
            logger("ip-bad-type").error("ip must be IP addresses")
            return False

        # checks the ip is not the device network ip
        # example: 192.168.10.9/255.255.0.0 --> 192.168.0.0
        if ip == subnet.network:
            logger("ip-network").notice("Ip '%s' cannot be the network IP", ip)
            return False
        
        # checks the ip is not the device broadcast ip
        # example: 192.168.10.9/255.255.0.0 --> 192.168.255.255
        if ip == subnet.broadcast:
            logger("ip-broadcast").notice("Ip '%s' cannot be the broadcast IP", ip)
            return False

        # checks if this address is multicast
        # ipv4 - 224.0.0.0/4    (RFC 3171)
        # ipv6 - ff00::/8       (RFC 2373 2.7)
        if ip.is_multicast is True:
            logger("ip-multicast").notice("Ip '%s' cannot be multicast", ip)
            return False

        # checks if this address is unspecified
        # ipv4 - 0.0.0.0    (RFC 5735 3)
        # ipv6 - ::         (RFC 2373 2.5.2)
        if ip.is_unspecified is True:
            logger("ip-unspecified").notice("Ip '%s' cannot be unspecified", ip)
            return False

        # checks if this address is loopback
        # ipv4 - 127.0.0.1/8    (RFC 3330)
        # ipv6 - ::1            (RFC 2373 2.5.3)
        if ip.is_loopback is True:
            logger("ip-loopback").notice("Ip '%s' cannot be loopback", ip)
            return False

        if ip.version == 4:
            # ipv4 specific checks
            
            # checks if this address is within the reserved IP Network range
            # ipv4 - 240.0.0.0/4
            if ip.is_reserved is True:
                logger("ip-reserved").notice("Ip '%s' cannot be within the reserved ip network range", ip)
                return False
        else:
            # ipv6 specific checks

            # checks if this address is link-local
            # ipv6 - fe80::/10  (RFC 4291)
            if ip.is_link_local is True:
                logger("ip-link-local").notice("Ip '%s' link-local is not supported", ip)
                return False

            # checks if this address is an IPv4 mapped address
            # ipv6 - ::ffff:192.168.0.1 or ::192.168.0.1
            if ip.ipv4_mapped is not None:
                logger("ip-ipv4-mapped").notice("Ip '%s' ipv4-mapped address is not supported", ip)
                return False

        return True

#-----------------------------------------------------------------------------------------------------------------------
    def overlaps(self, other):
        """Tell if self is partly contained in other."""

        # always false if one is v4 and the other is v6.
        if self.version != other.version:
            return False
        
        # always false if either one has no ip address configured.
        if not (self.address and other.address):
            return False

        return self.address.overlaps(other.address)

#-----------------------------------------------------------------------------------------------------------------------
class IPv4Network(IpNetwork):
    """A generic IPv4 Network Address object.
    """

    def __init__(self, address, logger):
        version = 4
        IpNetwork.__init__(self, logger, address, version)

#-----------------------------------------------------------------------------------------------------------------------
class IPv6Network(IpNetwork):
    """A generic IPv6 Network Address object.
    """

    def __init__(self, address, logger):
        version = 6
        IpNetwork.__init__(self, logger, address, version)

