# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from common import Command

#-----------------------------------------------------------------------------------------------
class IpTablesService(object):
    """ Iptables is used to set up, maintain, and inspect the tables of IP packet filter rules in the Linux kernel
    """

    # service
    IPV4_TABLE_COMMAND_NAME = "iptables"
    IPV6_TABLE_COMMAND_NAME = "ip6tables"

    # options
    INSERT_OPTION       = "--insert"
    DELETE_OPTION       = "--delete"
    LIST_OPTION         = "--list"
    NUMERIC_OPTION      = "-n"
    VERBOSE_OPTION      = "-v"
    EXACT_OPTION        = "-x"
    LINE_NUM_OPTION     = "--line-numbers"

    # parameters
    IN_INTERFACE_PARAM  = "--in-interface"
    OUT_INTERFACE_PARAM = "--out-interface"
    PROTOCOL_PARAM      = "--protocol"
    SOURCE_PORT_PARAM   = "--sport"
    DEST_PORT_PARAM     = "--dport"

    # values
    INPUT_CHAIN_VALUE   = "INPUT"
    OUTPUT_CHAIN_VALUE  = "OUTPUT"
    TCP_PROTOCOL_VALUE  = "tcp"

    def __init__ (self, logger):
        self.__log = logger

    # public
    #-------------------------------------------------------------------------------------------------
    def addInRule (self, ipVersion, device, port, protocol):
        """This function inserts a rule at the head of the INPUT chain (for packets destined to local sockets)

        Args:
            ipVersion -   IPv4 or IPv6 as an integer, 4 or 6
            device  -   Name of an interface via which a packet was received
            port    -   Destination port
            protocol-   The protocol of the rule or of the packet to check

        Returns: 
            True/False
        """
        return self.__executeInRule(ipVersion, self.INSERT_OPTION, device, port, protocol)

    #-------------------------------------------------------------------------------------------------
    def addOutRule (self, ipVersion, device, port, protocol):
        """This function inserts a rule at the head of the OUTPUT chain (for locally-generated packets)

        Args:
            ipVersion -   IPv4 or IPv6 as an integer, 4 or 6
            device  -   Name of an interface via which a packet is going to be sent
            port    -   Source port
            protocol-   The protocol of the rule or of the packet to check

        Returns: 
            True/False
        """
        return self.__executeOutRule(ipVersion, self.INSERT_OPTION, device, port, protocol)

    #-------------------------------------------------------------------------------------------------
    def deleteInRule (self, ipVersion, device, port, protocol):
        """This function deletes a rule match fom the INPUT chain

        Args:
            ipVersion -   IPv4 or IPv6 as an integer, 4 or 6
            device  -   Name of an interface via which a packet was received
            port    -   Destination port
            protocol-   The protocol of the rule or of the packet to check

        Returns: 
            True/False
        """
        return self.__executeInRule(ipVersion, self.DELETE_OPTION, device, port, protocol)

    #-------------------------------------------------------------------------------------------------
    def deleteOutRule (self, ipVersion, device, port, protocol):
        """This function deletes a rule match fom the OUTPUT chain

        Args:
            ipVersion -   IPv4 or IPv6 as an integer, 4 or 6
            device  -   Name of an interface via which a packet is going to be sent
            port    -   Source port
            protocol-   The protocol of the rule or of the packet to check

        Returns: 
            True/False
        """
        return self.__executeOutRule(ipVersion, self.DELETE_OPTION, device, port, protocol)

    #-------------------------------------------------------------------------------------------------
    def listInRules (self, ipVersion, filters=None):
        """This function lists all rules in the INPUT chain

        Args:
            ipVersion -   IPv4 or IPv6 as an integer, 4 or 6
            filters   -   Filter rules using a common regular expression syntax

        Returns: 
            list of rules
        """
        stdOut = self.__listRules(ipVersion, self.INPUT_CHAIN_VALUE, filters)
        return stdOut.splitlines()

    #-------------------------------------------------------------------------------------------------
    def listOutRules (self, ipVersion, filters=None):
        """This function lists all rules in the OUTPUT chain

        Args:
            ipVersion -   IPv4 or IPv6 as an integer, 4 or 6
            filters   -   Filter rules

        Returns: 
            list of rules
        """
        stdOut = self.__listRules(ipVersion, self.OUTPUT_CHAIN_VALUE, filters)
        return stdOut.splitlines()

    #-------------------------------------------------------------------------------------------------
    def showRules (self, ipVersion, filters=None):
        """This function shows all rules in all chains

        Args:
            ipVersion -   IPv4 or IPv6 as an integer, 4 or 6

        Returns: 
            table output as string
        """
        stdOut = self.__listRules(ipVersion, chain=None, filters=filters)
        return stdOut

    # private
    #-------------------------------------------------------------------------------------------------
    def __executeInRule (self, ipVersion, command, device, port, protocol):

        # e.g. iptables -I <command>  1 -i eth-tg8 -p tcp --dport 80      
        args = [command, self.INPUT_CHAIN_VALUE,
                self.IN_INTERFACE_PARAM, str(device),
                self.PROTOCOL_PARAM, str(protocol),
                self.DEST_PORT_PARAM, str(port)]

        (rc,stdOut) = self.__executeIpTablesCmd(ipVersion, args)
        return rc

    #-------------------------------------------------------------------------------------------------
    def __executeOutRule (self, ipVersion, command, device, port, protocol):

        # e.g. iptables -I <command> 1 -o eth-tg8 -p tcp --sport 80      
        args = [command, self.OUTPUT_CHAIN_VALUE,
                self.OUT_INTERFACE_PARAM, str(device),
                self.PROTOCOL_PARAM, str(protocol),
                self.SOURCE_PORT_PARAM, str(port)]

        (rc,stdOut) = self.__executeIpTablesCmd(ipVersion, args)
        return rc

    #-------------------------------------------------------------------------------------------------
    def __listRules (self, ipVersion, chain, filters):

        # e.g. iptables -nvx -L INPUT      
        args = [self.NUMERIC_OPTION,
                self.VERBOSE_OPTION, 
                self.EXACT_OPTION, 
                self.LIST_OPTION]

        if chain:
            args.append(str(chain))

        (rc,stdOut) = self.__executeIpTablesCmd(ipVersion, args, filters=filters)
        
        return stdOut

    #-------------------------------------------------------------------------------------------------
    def __executeIpTablesCmd (self, ipVersion, args, filters=None):

        commandName = self.IPV4_TABLE_COMMAND_NAME
        if ipVersion == 6:
            commandName = self.IPV6_TABLE_COMMAND_NAME         

        args.insert(0,commandName)
        command = " ".join(args)

        if filters:
            for text in filters:
                command += (" | grep %s" % text)

        self.__log("iptables-cmd-run").debug4("Run IPv%s Tables Cmd - '%s'", ipVersion, command)

        # execute command
        (rc, stdOut, stdErr) =  Command.execute(self.__log, "iptables", command) 

        
        if rc == 0:
            self.__log("iptables-cmd-stdout").debug3("show output of IPv%s tables command '%s' (rc=%s) - %s",
                                                     ipVersion, command, rc, stdOut)
        else:
            self.__log("iptables-cmd-failed").error("fail to run IPv%s tables command  '%s' (rc=%s) - %s", 
                                                    ipVersion, command, rc, stdErr)

        return (rc,stdOut)

# tempalte for iptables system config file
class IpTablesConfigFile(object):

    IPV4_TABLE_CONFIG_FILE = "/etc/sysconfig/iptables"
    IPV6_TABLE_CONFIG_FILE = "/etc/sysconfig/ip6tables"

    IPV4TABLES_CONFIG_TEMPLATE = """
# Generated by iptables-save v1.4.7 via service oscar
*filter
:INPUT ACCEPT   [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT  [0:0]
-A INPUT -p tcp --sport 0  -j DROP
-A INPUT -i eth-tg8 -p tcp --dport 80  -j ACCEPT
-A INPUT -i eth-tg9 -p tcp --dport 80  -j ACCEPT
-A INPUT -i eth-tg8 -p tcp --sport 10957  -j ACCEPT
-A INPUT -i eth-tg9 -p tcp --sport 10957  -j ACCEPT
-A INPUT -i eth-tg8 -p icmp --icmp-type echo-request -j ACCEPT
-A INPUT -i eth-tg9 -p icmp --icmp-type echo-request -j ACCEPT
-A INPUT -i eth-tg8 -p icmp --icmp-type echo-reply -j ACCEPT
-A INPUT -i eth-tg9 -p icmp --icmp-type echo-reply -j ACCEPT
-A INPUT -i eth-tg8 -s 0.0.0.0/0  -j DROP
-A INPUT -i eth-tg9 -s 0.0.0.0/0  -j DROP
COMMIT
# Completed on %(timestamp)s
"""

    IPV6TABLES_CONFIG_TEMPLATE = """
# Generated by ip6tables-save v1.4.7 via service oscar
*filter
:INPUT ACCEPT   [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT  [0:0]
-A INPUT -p tcp --sport 0  -j DROP
-A INPUT -i eth-tg8 -p tcp --dport 80  -j ACCEPT
-A INPUT -i eth-tg9 -p tcp --dport 80  -j ACCEPT
-A INPUT -i eth-tg8 -p icmpv6 --icmpv6-type echo-request -j ACCEPT
-A INPUT -i eth-tg9 -p icmpv6 --icmpv6-type echo-request -j ACCEPT
-A INPUT -i eth-tg8 -p icmpv6 --icmpv6-type echo-reply -j ACCEPT
-A INPUT -i eth-tg9 -p icmpv6 --icmpv6-type echo-reply -j ACCEPT
-A INPUT -i eth-tg8 -p icmpv6 --icmpv6-type neighbour-solicitation -j ACCEPT
-A INPUT -i eth-tg9 -p icmpv6 --icmpv6-type neighbour-solicitation -j ACCEPT
-A INPUT -i eth-tg8 -p icmpv6 --icmpv6-type neighbour-advertisement -j ACCEPT
-A INPUT -i eth-tg9 -p icmpv6 --icmpv6-type neighbour-advertisement -j ACCEPT
-A INPUT -i eth-tg8 -s ::/0  -j DROP
-A INPUT -i eth-tg9 -s ::/0  -j DROP
COMMIT
# Completed on %(timestamp)s
"""
