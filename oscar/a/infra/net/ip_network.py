# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

import google.ipaddr
from a.infra.net.ip_address import Ipv4Address
from a.infra.net.ip_address import Ipv6Address

GROUP_NAME = "ip-network"

def IpNetwork(address, version=None):  
    """Take an IP string/int and return an object of the correct type.
    see ref: http://code.google.com/p/ipaddr-py/

    Args:
        logger

        address: A string or integer, the IP address.  Either IPv4 or
          IPv6 addresses may be supplied; integers less than 2**32 will
          be considered to be IPv4 by default.

        version: An Integer, if set, don't try to automatically
          determine what the IP address type is. important for things
          like IpNetwork(1), which could be IPv4, '0.0.0.1/32', or IPv6,
          '::1/128'.

    Returns:
        An Ipv4Network or Ipv6Network object.

    Raises:
        ValueError: if the string passed isn't either a v4 or a v6 address. 

    """

    if version:
        if version == 4:
            return Ipv4Network(address)
        elif version == 6:
            return Ipv6Network(address)

    try:
        return Ipv4Network(address)
    except (ValueError):
        pass

    try:
        return Ipv6Network(address)
    except (ValueError):
        pass

    raise ValueError('%r does not appear to be an IPv4 or IPv6 network' % address)

#-----------------------------------------------------------------------------------------------------------------------
class Ipv4Network(google.ipaddr.IPv4Network):
    """Represent and manipulate 32-bit IPv4 networks.

        Attributes: [examples for IPv4Network('1.2.3.4/27')]
        ._ip: 16909060
        .ip: IPv4Address('1.2.3.4')
        .network: IPv4Address('1.2.3.0')
        .hostmask: IPv4Address('0.0.0.31')
        .broadcast: IPv4Address('1.2.3.31')
        .netmask: IPv4Address('255.255.255.224')
        .prefixlen: 27
    """

    def __init__(self, address, netmask=None):
        """Instantiate a new IPv4 network object.

        Args:
            address: A string or integer representing the IP [& network].
              '192.168.1.1/24'
              '192.168.1.1/255.255.255.0'
              '192.168.1.1/0.0.0.255'
              are all functionally the same in IPv4. Similarly,
              '192.168.1.1'
              '192.168.1.1/255.255.255.255'
              '192.168.1.1/32'
              are also functionaly equivalent. That is to say, failing to
              provide a subnetmask will create an object with a mask of /32.

              If the mask (portion after the / in the argument) is given in
              dotted quad form, it is treated as a netmask if it starts with a
              non-zero field (e.g. /255.0.0.0 == /8) and as a hostmask if it
              starts with a zero field (e.g. 0.255.255.255 == /8), with the
              single exception of an all-zero mask which is treated as a
              netmask == /0. If no mask is given, a default of /32 is used.

              Additionally, an integer can be passed, so
              Ipv4Network('192.168.1.1') == Ipv4Network(3232235777).
              or, more generally
              Ipv4Network(int(IPv4Network('192.168.1.1'))) == Ipv4Network('192.168.1.1')

            netmask [optional]: netmask in either dotted quad form or prefix length form

        Raises:
            ValueError: (1) If ipaddr isn't a valid IPv4 address.
                        (2) If the netmask isn't valid for an IPv4 address.
        """

        if netmask:
            ip = Ipv4Address(address)
            address = "%s/%s" % (ip,netmask)

        google.ipaddr.IPv4Network.__init__(self, address, strict=False)

    def __repr__ (self):
        return '%s(%r)' % (self.__class__.__name__, str(self))

#-----------------------------------------------------------------------------------------------------------------------
class Ipv6Network(google.ipaddr.IPv6Network):
    """Represent and manipulates 128-bit IPv6 networks.

        Attributes: [examples for IPv6('2001:658:22A:CAFE:200::1/64')]
            .ip: IPv6Address('2001:658:22a:cafe:200::1')
            .network: IPv6Address('2001:658:22a:cafe::')
            .hostmask: IPv6Address('::ffff:ffff:ffff:ffff')
            .broadcast: IPv6Address('2001:658:22a:cafe:ffff:ffff:ffff:ffff')
            .netmask: IPv6Address('ffff:ffff:ffff:ffff::')
            .prefixlen: 64
    """


    def __init__(self, address, netmask=None):
        """Instantiate a new IPv6 Network object.

        Args:
            address: A string or integer representing the IPv6 network or the IP
              and prefix/netmask.
              '2001:4860::/128'
              '2001:4860:0000:0000:0000:0000:0000:0000/128'
              '2001:4860::'
              are all functionally the same in IPv6.  That is to say,
              failing to provide a subnetmask will create an object with
              a mask of /128.

              Additionally, an integer can be passed, so
              Ipv6Network('2001:4860::') == Ipv6Network(42541956101370907050197289607612071936L).
              or, more generally
              Ipv6Network(IPv6Network('2001:4860::')._ip) == Ipv6Network('2001:4860::')

            netmask [optional]: netmask in prefix length form only

        Raises:
            ValueError: (1) If address isn't a valid IPv6 address.
                        (2) If the netmask isn't valid for an IPv6 address.
        """

        if netmask:
            ip = Ipv6Address(address)
            address = "%s/%s" % (ip,netmask)

        google.ipaddr.IPv6Network.__init__(self, address, strict=False)

    def __repr__ (self):
        return '%s(%r)' % (self.__class__.__name__, str(self))
