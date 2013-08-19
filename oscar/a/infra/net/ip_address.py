# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

import google.ipaddr
import socket

GROUP_NAME = "ip-address"

def IpAddress(address, version=None):
    """Take an IP string/int and return an object of the correct type.
    see ref: http://code.google.com/p/ipaddr-py/

    Args:
        address: A string or integer, the IP address.  Either IPv4 or
          IPv6 addresses may be supplied; integers less than 2**32 will
          be considered to be IPv4 by default.

        version: An Integer, 4 or 6. If set, don't try to automatically
          determine what the IP address type is. important for things
          like IPAddress(1), which could be IPv4, '0.0.0.1',  or IPv6,
          '::1'.

    Returns:
        An Ipv4Address or Ipv6Address object.

    Raises:
        ValueError: if the string passed isn't either a v4 or a v6 address.

    """

    if version:
        if version == 4:
            return Ipv4Address(address)
        elif version == 6:
            return Ipv6Address(address)

    try:
        return Ipv4Address(address)
    except (ValueError):
        pass

    try:
        return Ipv6Address(address)
    except (ValueError):
        pass

    raise ValueError('%r does not appear to be an IPv4 or IPv6 address' % address)

#-----------------------------------------------------------------------------------------------------------------------
class Ipv4Address(google.ipaddr.IPv4Address):
    """Represent and manipulate single IPv4 Addresses.
    """

    def __init__(self, address):
        """Instantiate a new IPv4 address object.

        Args:
            address: A string or integer representing the IP
              '192.168.1.1'

              Additionally, an integer can be passed, so
              Ipv4Address('192.168.1.1') == Ipv4Address(3232235777).
              or, more generally
              Ipv4Address(int(Ipv4Address('192.168.1.1'))) == Ipv4Address('192.168.1.1')

        Raises:
            ValueError: If address isn't a valid IPv4 address.

        """

        google.ipaddr.IPv4Address.__init__(self, address)

    def __repr__ (self):
        return '%s(%r)' % (self.__class__.__name__, str(self))

#-----------------------------------------------------------------------------------------------------------------------
class Ipv6Address(google.ipaddr.IPv6Address):
    """Represent and manipulate single IPv6 Addresses.
    """

    def __init__(self, address):
        """Instantiate a new IPv6 address object.

        Args:
            address: A string or integer or binary format representing the IP

              Additionally, an integer can be passed, so
              Ipv6Address('2001:4860::') == Ipv6Address(42541956101370907050197289607612071936L).
              or, more generally
              Ipv6Address(Ipv6Address('2001:4860::')._ip) == Ipv6Address('2001:4860::')

              Additionally, a packed binary format can be passed, so
              Ipv6Address('2001:4860::') == Ipv6Address(' \x01H`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00').
              or, more generally
              Ipv6Address(Ipv6Address('2001:4860::').packed) == Ipv6Address('2001:4860::')
              
        Raises:
            ValueError: If address isn't a valid IPv6 address.

        """

        if isinstance(address, str):
            try:
                # convert a packed binary format IPv6 address to its IPv6 string representation (for example, '5aef:2b::8') 
                address = socket.inet_ntop(socket.AF_INET6, address)
            except (ValueError,TypeError):
                pass 

        google.ipaddr.IPv6Address.__init__(self, address)

    def __repr__ (self):
        return '%s(%r)' % (self.__class__.__name__, str(self))
