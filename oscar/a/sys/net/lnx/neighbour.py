# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave


from common import Command
from common import IpConstant
from common import IpOption
from common import IpAction
import subprocess

##############################################
# ip neigh - neighbour/arp tables management 
# neighbour entries are organized into tables - ARP or NDISC cache 
##############################################
class IpNeighbour(object):

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showNeighbours(logger, version=None):
        """This function list neighbour entries

        Args:
            logger
            version - IPv4 or IPv6 as an integer, 4 or 6
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        if version:
            if version == 4:
                return Command.executeIp(logger, IpConstant.IPV4, IpOption.NEIGHBOUR, IpAction.SHOW)   
            elif version == 6:
                return Command.executeIp(logger, IpConstant.IPV6, IpOption.NEIGHBOUR, IpAction.SHOW)   

        rc =  Command.executeIp(logger, IpOption.NEIGHBOUR, IpAction.SHOW)   
        return rc

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showNeighboursByDevice(logger, device, version=None):
        """This function list neighbour entries attached to the given device

        Args:
            logger
            device  - device name
            version - IPv4 or IPv6 as an integer, 4 or 6
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        args = []

        if version:
            if version == 4:
                args.append(IpConstant.IPV4)
            elif version == 6:
                args.append(IpConstant.IPV6)

        args += [IpOption.NEIGHBOUR, IpAction.SHOW, IpConstant.DEV, device]

        option = args[0]
        cmd = args[1:]

        rc =  Command.executeIp(logger, option, *cmd)   
        return rc 

##############################################
# arping - send ARP REQUEST to a neighbour host 
##############################################
class Arping(object):

    ARPING_COMMAND_NAME = "/sbin/arping"

    INTERFACE_OPTION = "-I"
    COUNT_OPTION = "-c"
    QUIET_OPTION = "-q"
    FIRST_REPLY_OPTION = "-f"
    TIMEOUT_OPTION = "-w"
    ARP_REPLY_OPTION = "-A"

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def sendArpRequest(logger, device, destination, count=3, timeout=1, quiet=False, firstReply=False, blocking=True):
        """This function sends ARP REQUEST to a neighbour host 

        Args:
            logger
            device - Name of network device where to send ARP REQUEST packets
            destination - destination IP to ping
            count - stop after sending X ARP REQUEST packets
            timeout - specify a timeout, in seconds, before arping exits
            quiet - quiet output
            firstReply - Finish after the first reply confirming that target is alive
            blocking - if True, waits for command to complete
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        args = [Arping.ARPING_COMMAND_NAME, 
                Arping.INTERFACE_OPTION, device, 
                Arping.COUNT_OPTION, str(count),
                Arping.TIMEOUT_OPTION, str(timeout)]

        if quiet is True:
            args.append(Arping.QUIET_OPTION)

        if firstReply is True:
            args.append(Arping.FIRST_REPLY_OPTION)

        # must set destination as last arg
        args.append(destination) 

        rc =  Command.execute(logger, Arping.ARPING_COMMAND_NAME, args, timeoutSec=(timeout+3), blocking=blocking)

        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def sendArpReply(logger, device, destination, count=3, quiet=False, blocking=True):
        """This function sends ARP REPLY to a neighbour host 

        Args:
            logger
            device - Name of network device where to send ARP REPLY packets
            destination - destination IP to ping
            count - stop after sending X ARP REQUEST packets
            quiet - quiet output
            blocking - if True, waits for command to complete
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        args = [Arping.ARPING_COMMAND_NAME, 
                Arping.INTERFACE_OPTION, device, 
                Arping.COUNT_OPTION, str(count),
                Arping.ARP_REPLY_OPTION]

        if quiet is True:
            args.append(Arping.QUIET_OPTION)

        # must set destination as last arg
        args.append(destination) 

        rc =  Command.execute(logger, Arping.ARPING_COMMAND_NAME, args, blocking=blocking)

        return rc 

##############################################
# ndisc6 - send IPv6 neighbor discovery to a neighbour host 
# rdisc6 - send IPv6 router discovery to a neighbour host 
##############################################
class Ndisc(object):

    NDISC6_COMMAND_NAME = "qb-ndisc6"
    RDISC6_COMMAND_NAME = "qb-rdisc6"

    INTERFACE_OPTION = "-I"
    COUNT_OPTION = "-r"
    QUIET_OPTION = "-q"
    FIRST_REPLY_OPTION = "-1"
    TIMEOUT_OPTION = "-w"

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def sendNdiscRequest(logger, device, destination, count=3,  timeout=1, quiet=False, firstReply=False, blocking=True):
        """This function sends IPv6 neighbor discovery to a neighbour host 

        Args:
            logger
            device - Name of network device where to send ARP REQUEST packets
            destination - destination IP to ping
            count - send ICMPv6 Neighbor Discovery X times
            timeout - specify a timeout, in seconds, before ndisc exits
            quiet - quiet output
            firstReply - Exit as soon as the first advertisement is received
            blocking - if True, waits for command to complete
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        args = [Ndisc.NDISC6_COMMAND_NAME, 
                Ndisc.COUNT_OPTION, str(count),
                Ndisc.TIMEOUT_OPTION, str(int(timeout)*1000)] # convert to milisec

        if quiet is True:
            args.append(Ndisc.QUIET_OPTION)

        if firstReply is True:
            args.append(Ndisc.FIRST_REPLY_OPTION)

        # must set <destination> <iface> as last args
        args.append(destination) 
        args.append(device) 

        rc =  Command.execute(logger, Ndisc.NDISC6_COMMAND_NAME, args, timeoutSec=(timeout+3), blocking=blocking)

        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def sendRdiscReply(logger, device, destination, count=3, quiet=False, blocking=True):
        """This function sends IPv6 router discovery to a neighbour host 

        Args:
            logger
            device - Name of network device where to send ICMPv6 Router Discovery packets
            destination - destination IP to ping
            count - send ICMPv6 Router Discovery X times
            quiet - quiet output
            blocking - if True, waits for command to complete
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        args = [Ndisc.RDISC6_COMMAND_NAME, 
                Ndisc.COUNT_OPTION, str(count)]

        if quiet is True:
            args.append(Ndisc.QUIET_OPTION)

        # must set <destination> <iface> as last args
        args.append(destination) 
        args.append(device) 

        rc =  Command.execute(logger, Ndisc.RDISC6_COMMAND_NAME, args, blocking=blocking)

        return rc

##############################################
# This class holds neighbour utilities
##############################################
class NeighbourUtils(object):
    """This class holds neighbour utilities"""

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getNeighbourTable(logger, device, version=4):
        """This function returns the neighbour table"""

        (rc, stdout, stderr) = IpNeighbour.showNeighboursByDevice(logger, device, version)

        if rc != 0:
            return None

        if logger:
            logger("neigh-table-get").debug2("retrieving device %s neighbor table", device, stdout)

        # example:
        # ipv4 --> 199.120.69.13 dev eth-tg8 lladdr 00:0d:66:33:dc:19 REACHABLE
        # ipv6 --> 2000::223:5eff:fe2d:cf81 dev eth-tg8 lladdr 00:23:5e:2d:cf:81 router STALE
        output = stdout.splitlines()

        return output

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getNeighbourMacAddress(logger, device, dstIp, version=4):
        """This function returns the neighbour mac address"""

        output = NeighbourUtils.getNeighbourTable(logger,device,version)

        if output is None:
            return None
 
        for line in output:
            if dstIp == line.split()[0]:
                try:
                    mac = line.split("lladdr",1)[1].split()[0]
                    if logger:
                        logger("neigh-mac-show").debug3("Destination IP's ('%s') MAC address is '%s'", dstIp, mac)
                
                except IndexError:
                    mac = None
                    if logger:
                        logger("neigh-mac-failed").debug1("failed extracting destination IP's ('%s') MAC address from table {%s}", dstIp, output)

                return mac

        return None

