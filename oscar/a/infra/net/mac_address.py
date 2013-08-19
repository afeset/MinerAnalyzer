# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

import netaddr
import binascii

GROUP_NAME = "mac-address"

class MacAddrFormatError(netaddr.AddrFormatError):
    """Exception raised for address format errors.
    """

#-----------------------------------------------------------------------------------------------------------------------
class MacAddress(netaddr.EUI):
    """ MAC Address object.
        see ref: http://packages.python.org/netaddr/tutorial_02.html

        An IEEE EUI (Extended Unique Identifier).
     
        Both EUI-48 (used for layer 2 MAC addresses) and EUI-64 are supported.
        Input parsing for EUI-48 addresses is flexible, supporting many MAC variants.

        Formatting:

        IEEE EUI-48 format                  MacAddress('00-1B-77-49-54-FD')
        IEEE EUI-48 lowercase format        MacAddress('00-1b-77-49-54-fd')
        Common UNIX format                  MacAddress('0:1b:77:49:54:fd')
        Cisco triple hextet format          MacAddress('001b:7749:54fd') or MacAddress('1b:7749:54fd') or MacAddress('1B:7749:54FD')
        Bare MAC addresses (no delimiters)  MacAddress('001b774954fd') or MacAddress('01B774954FD')
        PostreSQL format                    MacAddress('001B77:4954FD')
        Raw bytes format                    MacAddress('\x00\x1b\x77\x49\x54\xfd')
    """

    class _UnixFormat(netaddr.mac_unix): 
        """ a UNIX MAC dialect that generates uppercase, zero-filled octets
        """

        # MAC string output is Common UNIX format
        word_fmt = '%.2X'

    def __init__(self, mac):
        """
        Args:
            mac     - MAC address in many different formats

        Raises:
            AddrFormatError
        """

        if isinstance(mac, str) and len(mac) == 6:
            try:
                # support raw bytes format
                mac = binascii.hexlify(mac)

            except (ValueError,TypeError):
                pass 

        try:
            netaddr.EUI.__init__(self, mac, dialect = MacAddress._UnixFormat)
        except netaddr.AddrFormatError as ex:
            raise MacAddrFormatError(ex)

    def __repr__ (self):
        return '%s(%r)' % (self.__class__.__name__, str(self))

    def getAddress (self):
        return binascii.unhexlify(netaddr.EUI.__str__(self).replace(':', ''))
