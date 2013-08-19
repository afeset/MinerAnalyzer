# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from common import Command
from common import IpConstant
from common import IpOption
from common import IpAction
from common import ConfigFile
import subprocess

##############################################
#  ip route - routing table management
#  Manipulate route entries in the kernel 
#  routing tables keep information about paths to other networked nodes. 
##############################################
class IpRoute(object):

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showRoutes(logger, table, version=None):
        """This function list all routes

        Args:
            logger
            table -     show the routes from this table
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None

        """

        if version:
            if version == 4:
                return Command.executeIp(logger, IpConstant.IPV4, IpOption.ROUTE, IpAction.SHOW, IpConstant.TABLE, table)  
            elif version == 6:
                return Command.executeIp(logger, IpConstant.IPV6, IpOption.ROUTE, IpAction.SHOW, IpConstant.TABLE, table)  

        rc =  Command.executeIp(logger, IpOption.ROUTE, IpAction.SHOW, IpConstant.TABLE, table) 
 
        return rc 
         
#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def replaceRoute(logger, destination, gateway=None, table=None, device=None, version=None, scope=None, metric=None, src=None):
        """This function adds a new IP route or changes an existing IP route

        Args:
            logger
            destination-the destination prefix of the route 
            gateway -   the address of the nexthop router.
            table -     the table to add this route to. TABLEID may be a number or a string
            device -    the name specifies network device
            version -   IPv4 or IPv6 as an integer, 4 or 6
            scope -     the scope of the area where this address is valid: global, site, link, host
            metric -    the preference value of the route. NUMBER is an arbitrary 32bit number.
            src -       the source address to prefer when sending to the destinations covered by the route prefix
            
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

        args += [IpOption.ROUTE, IpAction.REPLACE, destination]

        if gateway: args += [IpConstant.VIA, gateway]
        if device: args += [IpConstant.DEV, device]
        if table: args += [IpConstant.TABLE, table]
        if scope: args += [IpConstant.SCOPE, scope]
        if metric: args += [IpConstant.METRIC, str(metric)]
        if src: args += [IpConstant.SRC, src]

        option = args[0]
        cmd = args[1:]

        rc =  Command.executeIp(logger, option, *cmd)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def addDefaultRoute(logger, gateway, table, device, version=None):
        """This function adds a new IP default route or changes an existing default IP route

        Args:
            logger
            gateway -   the address of the nexthop router.
            table -     the table to add this route to. TABLEID may be a number or a string
            device - the name specifies network device
            version -   IPv4 or IPv6 as an integer, 4 or 6
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        rc = IpRoute.replaceRoute(logger, IpConstant.DEFAULT, gateway, table, device, version)
        return rc

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def deleteRoute(logger, destination, gateway, table, version=None):
        """This function deletes an IP route

        Args:
            logger
            destination-the destination prefix of the route 
            gateway -   the address of the nexthop router.
            table -     the table to delete this route from. TABLEID may be a number or a string
            version -   IPv4 or IPv6 as an integer, 4 or 6
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        if version:
            if version == 4:
                return Command.executeIp(logger, IpConstant.IPV4, IpOption.ROUTE, IpAction.DELETE, 
                                    destination, IpConstant.VIA, gateway, IpConstant.TABLE, table)  
            elif version == 6:
                return Command.executeIp(logger, IpConstant.IPV6, IpOption.ROUTE, IpAction.DELETE, 
                                    destination, IpConstant.VIA, gateway, IpConstant.TABLE, table)  

        rc =  Command.executeIp(logger, IpOption.ROUTE, IpAction.DELETE, 
                                    destination, IpConstant.VIA, gateway, IpConstant.TABLE, table)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def flushRoutes(logger, table=None, device=None, version=None, scope=None, proto=None):
        """This function flushes all IP routes assigned to a device

        Args:
            logger
            table -     the table to add this route to. TABLEID may be a number or a string
            device -    the name specifies network device
            version -   IPv4 or IPv6 as an integer, 4 or 6
            scope -     the scope of the area where this address is valid: global, site, link, host
            proto -     the routing protocol identifier of this route: kernel, boot, static, etc.
            
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

        args += [IpOption.ROUTE, IpAction.FLUSH]

        if device: args += [IpConstant.DEV, device]
        if table: args += [IpConstant.TABLE, table]
        if scope: args += [IpConstant.SCOPE, scope]
        if proto: args += [IpConstant.PROTO, proto]

        option = args[0]
        cmd = args[1:]

        rc =  Command.executeIp(logger, option, *cmd)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def flushDefaultRoute(logger, table, version=None):
        """This function flushes an existing IP default route 

        Args:
            logger
            table -     the table to add this route to. TABLEID may be a number or a string
            version -   IPv4 or IPv6 as an integer, 4 or 6
            
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

        args += [IpOption.ROUTE, IpAction.FLUSH, IpConstant.DEFAULT]

        if table: args += [IpConstant.TABLE, table]

        option = args[0]
        cmd = args[1:]

        rc =  Command.executeIp(logger, option, *cmd)   
        return rc 

##############################################
#  ip rule - routing policy database management
#  Rules in the routing policy database control the route selection algorithm
##############################################
class IpRule(object):

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def showRules(logger, version=None):
        """This function list all rules

        Args:
            logger
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        if version:
            if version == 4:
                return Command.executeIp(logger, IpConstant.IPV4, IpOption.RULE, IpAction.SHOW)  
            elif version == 6:
                return Command.executeIp(logger, IpConstant.IPV6, IpOption.RULE, IpAction.SHOW) 

        rc =  Command.executeIp(logger, IpOption.RULE, IpAction.SHOW)  
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def addRule(logger, source, table, version=None):
        """This function inserts a new rule

        Args:
            logger
            source  -   select the source prefix to match. 
            table   -   the routing table identifier to lookup if the rule selector matches. TABLEID may be a number or a string
            version -   IPv4 or IPv6 as an integer, 4 or 6
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        if version:
            if version == 4:
                return Command.executeIp(logger, IpConstant.IPV4, IpOption.RULE, IpAction.ADD, 
                                    IpConstant.FROM, source, IpConstant.TABLE, table)  
            elif version == 6:
                return Command.executeIp(logger, IpConstant.IPV6, IpOption.RULE, IpAction.ADD, 
                                    IpConstant.FROM, source, IpConstant.TABLE, table) 

        rc =  Command.executeIp(logger, IpOption.RULE, IpAction.ADD, 
                                    IpConstant.FROM, source, IpConstant.TABLE, table)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def deleteRule(logger, source, table, version=None):
        """This function deletes a rule

        Args:
            logger
            source  -   select the source prefix to match. 
            table   -   the routing table identifier to lookup if the rule selector matches. TABLEID may be a number or a string
            version -   IPv4 or IPv6 as an integer, 4 or 6
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        if version:
            if version == 4:
                return Command.executeIp(logger, IpConstant.IPV4, IpOption.RULE, IpAction.DELETE, 
                                    IpConstant.FROM, source, IpConstant.TABLE, table)  
            elif version == 6:
                return Command.executeIp(logger, IpConstant.IPV6, IpOption.RULE, IpAction.DELETE, 
                                    IpConstant.FROM, source, IpConstant.TABLE, table)  

        rc =  Command.executeIp(logger, IpOption.RULE, IpAction.DELETE, 
                                    IpConstant.FROM, source, IpConstant.TABLE, table)   
        return rc 

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def flushRules(logger, table, version=None):
        """This function flushes all rules associated with the table

        Args:
            logger
            table   -   the routing table identifier to lookup if the rule selector matches. TABLEID may be a number or a string
            version -   IPv4 or IPv6 as an integer, 4 or 6
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        if version:
            if version == 4:
                return Command.executeIp(logger, IpConstant.IPV4, IpOption.RULE, IpAction.DELETE, 
                                    IpConstant.TABLE, table)  
            elif version == 6:
                return Command.executeIp(logger, IpConstant.IPV6, IpOption.RULE, IpAction.DELETE, 
                                    IpConstant.TABLE, table)  

        rc =  Command.executeIp(logger, IpOption.RULE, IpAction.DELETE, 
                                    IpConstant.TABLE, table)   
        return rc 

##############################################
# ping, ping6 - send ICMP ECHO_REQUEST to network hosts 
##############################################
class Ping(object):

    PING_COMMAND_NAME  = "/bin/ping"
    PING6_COMMAND_NAME = "/bin/ping6"

    INTERFACE_OPTION= "-I"
    COUNT_OPTION    = "-c"
    INTERVAL_OPTION = "-i"
    QUIET_OPTION    = "-q"
    TIMEOUT_OPTION  = "-W"
    PACKET_SIZE_OPTION  = "-s"
    PATTERN_OPTION  = "-p"
    MTU_OPTION      = "-M"

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def ping(logger, destination, source=None, version=4, count=3, interval=1, timeout=1, quiet=False, blocking=True, 
             size=56, pattern=None, mtu=None):
        """This function shows current settings of the specified device

        Args:
            logger
            destination-destination IP to ping
            source -    name of network device where to send ARP REQUEST packets
            version -   IPv4 or IPv6 as an integer, 4 or 6
            count -     stop after sending X ECHO_REQUEST packets
            interval -  wait X seconds between sending each packet
            timeout -   time to wait for a response, in seconds
            quiet -     quiet output
            blocking -  if True, waits for command to complete
            size -      specifies the number of data bytes to be sent
            pattern -   specify up to 16 ''pad'' bytes (in hex) to fill out the packet you send
            mtu -       select Path MTU Discovery strategy
            
        Return:
            tuple (rc, stdout, stderr) 

        Raise:
            None
        """

        pingCommand = Ping.PING_COMMAND_NAME
        if version == 6:
            pingCommand = Ping.PING6_COMMAND_NAME           

        args = [pingCommand, 
                Ping.COUNT_OPTION, str(count),
                Ping.INTERVAL_OPTION, str(interval),
                Ping.TIMEOUT_OPTION, str(timeout),
                Ping.PACKET_SIZE_OPTION, str(size)]

        if source:
            args += [Ping.INTERFACE_OPTION, str(source)]

        if pattern is not None:
            args += [Ping.PATTERN_OPTION, str(pattern)]

        if mtu is not None:
            args += [Ping.MTU_OPTION, str(mtu)]

        if quiet is True:
            args.append(Ping.QUIET_OPTION)

        # must set destination as last arg
        args.append(destination) 

        logger("execute-ping").debug1("execute ping command: %s", " ".join(args))
        rc =  Command.execute(logger, pingCommand, args, timeoutSec=(timeout+3), blocking=blocking)

        return rc 


##############################################
#  This class view/edit the /etc/sysconfig/network configuration file
#  The file is used to specify information about the desired network configuration
#  
# Example:
#           NETWORKING=yes
#           FORWARD_IPV4=yes
#           HOSTNAME=deep.openna.com
#           GATEWAY=0.0.0.0
##############################################
class NetworkFile(object):
    """Network file is used to specify information about the desired network configuration on your server."""

    NETWORK_FILE_NAME = "/etc/sysconfig/network"

    HOSTNAME_KEY = "HOSTNAME="
    GATEWAY_KEY = "GATEWAY="

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def isFileValid():
        return ConfigFile.isFileValid(NetworkFile.NETWORK_FILE_NAME)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getHost(logger):

        host = ConfigFile.getValueByKey(logger, 
                                  NetworkFile.NETWORK_FILE_NAME, 
                                  NetworkFile.HOSTNAME_KEY)
        return host

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def setHost(logger, hostname):
        ConfigFile.changeKey(logger, 
                           NetworkFile.NETWORK_FILE_NAME, 
                           NetworkFile.HOSTNAME_KEY, 
                           hostname)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getGateway(logger):

        gw = ConfigFile.getValueByKey(logger, 
                                NetworkFile.NETWORK_FILE_NAME, 
                                NetworkFile.GATEWAY_KEY)
        return gw

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def setGateway(logger, gateway):
        ConfigFile.changeKey(logger, 
                           NetworkFile.NETWORK_FILE_NAME, 
                           NetworkFile.GATEWAY_KEY, 
                           gateway)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def commit():
        ConfigFile.commit(NetworkFile.NETWORK_FILE_NAME)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def abort():
        ConfigFile.abort(NetworkFile.NETWORK_FILE_NAME)

##############################################
# This class view/edit the /etc/iproute2/rt_tables configuration file
#  
# Example:
#           255     local
#           254     main
#           253     default
#           0       unspec     
##############################################
class RtTablesFile(object):
    """Routing tables file holds several routing tables identified by a number in the range from 1 to 255 or by name"""

    TR_TABLES_FILE_NAME = "/etc/iproute2/rt_tables"

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def isFileValid():
        return ConfigFile.isFileValid(RtTablesFile.TR_TABLES_FILE_NAME)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getTableName(logger, number):

        name = ConfigFile.getValueByKey(logger, RtTablesFile.TR_TABLES_FILE_NAME, str(number))

        if not name:
            return None

        return name.strip()

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def addRouteTable(logger, number, name):

        ConfigFile.addKey(logger, RtTablesFile.TR_TABLES_FILE_NAME,
                           "%s " % number,
                           name)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def commit():
        ConfigFile.commit(RtTablesFile.TR_TABLES_FILE_NAME)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def abort():
        ConfigFile.abort(RtTablesFile.TR_TABLES_FILE_NAME)

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getRouteTables(logger):

        logger("rt-tables-get").debug1("%s: looking for routing tables in file", RtTablesFile.TR_TABLES_FILE_NAME)

        # opens the file for reading
        ifile = open(RtTablesFile.TR_TABLES_FILE_NAME, 'r')

        rtTables = {}

        # iterates source file
        # skips comments (starts by #)
        for line in ifile:
            if not line.startswith('#'):
                number,name = line.split()
                rtTables[int(number)] = name

        # close file
        ifile.close()

        return rtTables

##############################################
# This class holds routing utilities
##############################################
class RoutingUtils(object):
    """This class holds routing utilities"""

    MAIN_TABLE_NAME = "main"

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def isTableIdValid(logger, tableid):
        """This function returns whether the given table id is valid"""

        # number in the range from 1 to 255
        if tableid.isdigit():
            tid = int(tableid)
            return (tid > 0 and tid < 256)

        # by name from the file /etc/iproute2/rt_tables
        rtTables = RtTablesFile.getRouteTables(logger)
        
        for value in rtTables.values():
            if value == tableid:
                return True

        return False
#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getDefaultGateway(logger, table, version=4):
        (rc, stdout, stderr) = IpRoute.showRoutes(logger, table, version)

        dg = None
        if rc == 0:
            # example:
            # 10.9.8.0/24 dev eth0  proto kernel  scope link  src 10.9.8.11
            # 169.254.0.0/16 dev eth0  scope link  metric 1002
            # default via 10.9.8.1 dev eth0
            lastLine = stdout.splitlines()[-1]
    
            if lastLine.startswith("default"):
                # e.g. 'default via 10.9.8.1 dev eth0'
                dg = lastLine.split()[2]

        return dg

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def getTableIdByName(logger, tablename):
        """This function returns the given table id mapping"""

        tablesMap = RtTablesFile.getRouteTables(logger)

        for tableid, name in tablesMap.iteritems():
            if name == tablename:
                return tableid

        return None

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def isTableMain(tableid):
        """This function returns whether the given table id is the main table"""

        # main table (ID 254)
        if type(tableid) is int or tableid.isdigit():
            tid = int(tableid)
            return tid == 254
        
        return (tableid == RoutingUtils.MAIN_TABLE_NAME)


#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def hasMatchingRule(logger, tableid, version=None):
        """This function returns whether the given table id has any rule matching"""

        (rc, stdout, stderr) = IpRule.showRules(logger, version)

        if rc != 0:
            return False

        tableid2 = None
        if tableid.isdigit():
            tableid2 = RtTablesFile.getTableName(logger, tableid)
        else:
            tableid2 = RoutingUtils.getTableIdByName(logger, tableid)          


        rules = stdout.splitlines()
        for r in rules:
            lookupTable = r.rsplit('lookup', 1)[1].strip()

            if lookupTable ==  tableid:
                return True

            if not tableid2 is None and lookupTable == tableid2:
                return True

        return False
