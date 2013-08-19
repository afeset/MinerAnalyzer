# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

import os  
import sys   
import time
import re 
import optparse

import a.infra.process

from a.infra.basic.return_codes import ReturnCodes
from a.infra.net.ip_address import IpAddress
from a.sys.net.lnx.route import Ping
from a.sys.net.lnx.device import DeviceUtils

G_NAME_MODULE_SYS_NET_NETWORK_OPERATIONS_PING = "sys-net-oper-ping"

class PingOperation(object):
    """ping operation

    To check host reachability and network connectivity on IP networks, use the ping command in EXEC mode.
    """

    _OPTION_PARSER_FLAG_VERBOSE = "verbose"
    _OPTION_PARSER_FLAG_DEBUG   = "debug"
    _OPTION_PARSER_IP_ADDRESS   = "ip-address"
    _OPTION_PARSER_HOSTNAME     = "hostname"
    _OPTION_PARSER_IP_VERSION   = "ip-version"
    _OPTION_PARSER_COUNT        = "count"
    _OPTION_PARSER_SOURCE       = "source"
    _OPTION_PARSER_TIMEOUT      = "timeout"
    _OPTION_PARSER_SIZE         = "size"
    _OPTION_PARSER_DONOT_FRAG   = "donotfrag"
    _OPTION_PARSER_PATTERN      = "pattern"

    _COUNT_RANGE    = (0,2147483647) 
    _TIMEOUT_RANGE  = (0,3600) 
    _SIZE_RANGE     = (36,18024) 
    _PATTERN_RANGE  = (0,65535)

    def __init__ (self, log):
        self._log = log
        self.options = None
        self.args = None

        self.pingSent = 0
        self.rttList = []

        self._verbose   = False  
        self._debug     = False 
        self._target        = None
        self._ipVersion     = None
        self._repeatCount   = None
        self._source        = None
        self._timeoutInterval = None
        self._packetSize    = None
        self._pattern       = None
        self._donotFrag     = False

#-----------------------------------------------------------------------------------------------------------------------
    def __searchRegexInLine (self, string, regexPattern):

        regex = re.compile(regexPattern)
        match = regex.search(string)

        if not match:
            return None

        return match.groups()

#-----------------------------------------------------------------------------------------------------------------------
    def __printDebug (self, msg):
        if self._debug is True:
            print "%s" % (str(msg))

#-----------------------------------------------------------------------------------------------------------------------
    def _prepare(self):

        options = self.options
        self._log("ping-cmd-line").info("options: %s", options)
        
        if hasattr(options, self._OPTION_PARSER_FLAG_VERBOSE):
            if getattr(options, self._OPTION_PARSER_FLAG_VERBOSE):
                self._verbose = True

        if hasattr(options, self._OPTION_PARSER_FLAG_DEBUG):
            if getattr(options, self._OPTION_PARSER_FLAG_DEBUG):
                self._debug = True

        if hasattr(options, self._OPTION_PARSER_DONOT_FRAG):
            if getattr(options, self._OPTION_PARSER_DONOT_FRAG):
                self._donotFrag = True
        
        # ip version
        self._ipVersion = getattr(options, self._OPTION_PARSER_IP_VERSION)

        # target ip address/hostname
        ipAddress   = getattr(options, self._OPTION_PARSER_IP_ADDRESS)
        hostname    = getattr(options, self._OPTION_PARSER_HOSTNAME)

        # target is an ip address
        if ipAddress:
            self._target = ipAddress

            try:
                targetIpAddress = IpAddress(self._target)
    
            except ValueError:
                print "Invalid Target IP address"
                return ReturnCodes.kGeneralError 

            # validate ping ip version
            if self._ipVersion is not None:
                if targetIpAddress.version != self._ipVersion:
                    print "Target IP address %s is not compatible with IPv%s" % (self._target, self._ipVersion)
                    return ReturnCodes.kGeneralError
            else:
                self._ipVersion = targetIpAddress.version

        # target is a hostname
        if hostname:
            
            if self._target is not None:
                print "Cannot specify both target IP address and hostname"
                return ReturnCodes.kGeneralError

            self._target = hostname

            if self._ipVersion is None:
                self._ipVersion = 4 # ipv4 by default   

        # no target to ping
        if self._target is None:
            print "Target IP address or hostname is required"
            return ReturnCodes.kGeneralError
        
        # repeat count
        self._repeatCount     = getattr(options, self._OPTION_PARSER_COUNT)

        repeatMin,repeatMax = self._COUNT_RANGE
        if self._repeatCount < repeatMin or self._repeatCount > repeatMax:
           print "Specified repeat count '%s' is out of range %s-%s" % (self._repeatCount, repeatMin, repeatMax)
           return ReturnCodes.kGeneralError

        # timeout interval
        self._timeoutInterval   = getattr(options, self._OPTION_PARSER_TIMEOUT)

        timeoutMin,timeoutMax = self._TIMEOUT_RANGE
        if self._timeoutInterval < timeoutMin or self._timeoutInterval > timeoutMax:
           print "Specified timeout interval '%s' is out of range %s-%s" % (self._timeoutInterval, timeoutMin, timeoutMax)
           return ReturnCodes.kGeneralError

        # packet size
        self._packetSize        = getattr(options, self._OPTION_PARSER_SIZE)

        sizeMin,sizeMax = self._SIZE_RANGE
        if self._packetSize < sizeMin or self._packetSize > sizeMax:
           print "Specified datagram size '%s' is out of range %s-%s" % (self._packetSize, sizeMin, sizeMax)
           return ReturnCodes.kGeneralError

        # data pattern
        self._pattern            = getattr(options, self._OPTION_PARSER_PATTERN)

        if self._pattern is not None:
            patternMin,patternMax = self._PATTERN_RANGE
            if self._pattern < patternMin or self._pattern > patternMax:
               print "Specified data pattern '%s' is out of range %s-%s" % (self._pattern, patternMin, patternMax)
               return ReturnCodes.kGeneralError

        # source interface
        source    = getattr(options, self._OPTION_PARSER_SOURCE)
        self._source = source

        if self._source is not None:
    
            try:
                # if source is an ip address, validate ping ip version
                sourceIpAddress = IpAddress(source)
                if sourceIpAddress.version != self._ipVersion:
                    print "Source IP address %s is not compatible with IPv%s" % (source, self._ipVersion)
                    return ReturnCodes.kGeneralError
    
            except ValueError:
    
                # source is an interface
                # static: GigabitEthernet0/0 -> eth-g0 and TenGigE0/0 -> eth-tg0
                # dynamic using MAAPI - TODO (yoave 1/2/2013)
                match1Gig   = self.__searchRegexInLine(source, r'GigabitEthernet0/(\d+)')
                matchTenGig = self.__searchRegexInLine(source, r'TenGigE0/(\d+)')
                osDevice = source
                
                if match1Gig is not None:
                    deviceIndex = match1Gig[0]
                    osDevice = "eth-g%s" % deviceIndex
    
                elif matchTenGig is not None:
                    deviceIndex = matchTenGig[0]
                    osDevice = "eth-tg%s" % deviceIndex

                if osDevice and DeviceUtils.isDeviceExists(osDevice) is True:
                    self._source = osDevice
                else:
                    print "Invalid source. Must use IP address or full interface name without spaces (e.g. GigabitEthernet0/0)"
                    return ReturnCodes.kGeneralError
            
        self.__printDebug("options: %s" % options)
        return ReturnCodes.kOk 

#-----------------------------------------------------------------------------------------------------------------------
    def _handlePingStart (self):
        
        print "Type escape sequence to abort."
        print "Sending %d, %s-byte ICMP Echos to %s, timeout is %d seconds:" % (self._repeatCount, self._packetSize, 
                                                                                self._target, self._timeoutInterval)

        self._log("ping-info").notice("ping info: target = %s , source = %s , count/size/timeout = %s/%s/%s", self._target,
                                      self._source, self._repeatCount, self._packetSize, self._timeoutInterval)

#-----------------------------------------------------------------------------------------------------------------------
    def _handleFirstPing (self, stdOut):
                
        hostnameOption    = getattr(self.options, self._OPTION_PARSER_HOSTNAME)
        if hostnameOption:

            # host:     the target hostname that was pinged
            # target:   the target ip address that was pinged
            #
            # examples:
            #   ipv4 - PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
            #   ipv6 - PING ::(::) 56 data bytes
            match = self.__searchRegexInLine(stdOut, r'PING (\S+)\s*\((\S+)\) ')
    
            if match is not None:

                host,target = match
                print "Translating \"%s\"...domain server (%s) [OK]" % (host,target)


        sourceOption    = getattr(self.options, self._OPTION_PARSER_SOURCE)
        if sourceOption:

            # source: the source that the ping was executed from
            # 
            # examples:
            #   ipv4 - PING 1.1.1.1 (1.1.1.1) from 10.9.8.15 em1: 56(84) bytes of data.
            #   ipv6 - PING ::(::) from ::1 em1: 56 data bytes
            match = self.__searchRegexInLine(stdOut, r' from (\S+) ')
            if match is not None:

                source = match[0]
                print "Translating \"%s\"...source (%s) [OK]" % (sourceOption,source)

#-----------------------------------------------------------------------------------------------------------------------
    def _handlePingSummary (self):
        # PIng statistics and Approximate round trip times in milli-seconds
        
        if self._verbose is False:
            print ""

        self._log("ping-rtt-list").debug2("ping rtt list snapshot: %s", self.rttList)

        # sent:         the number of ping request packets sent
        # received:     the number of ping reply packets received
        received = len(self.rttList) 
        sent = self.pingSent
        successRate = int(100*(int(received)/float(sent)))

        sys.stdout.write("Success rate is %s percent (%s/%s)" % (successRate, received, sent))
        self._log("ping-statistics").notice("ping statistics: received/sent/success-rate = %s/%s/%s%%", received, sent, successRate)

        if len(self.rttList) > 0:

            # minping: the minimum (fastest) round trip ping request/reply time (in millisec)
            # avgping: the average round trip ping time (in millisec)
            # maxping: the maximum (slowest) round trip ping time (in millisec)
            minping = min(self.rttList)
            maxping = max(self.rttList)
            avgping = (float(sum(self.rttList)) / len(self.rttList))
         
            sys.stdout.write(",round-trip min/avg/max = %s/%.2f/%s ms" % (minping, avgping, maxping))
            self._log("ping-round-trip-times").notice("ping rtt: min/avg/max = %s/%s/%s ms", minping, avgping, maxping)

        print "" # write new line and flush everything to the terminal

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _handlePingStdout (self, reqNum, retCode, stdOut):
        # ping replies
        #
        # seq:  the sequence number of ping reply packet which matches the ping request
        # ttl:  time-to-live - the number of routers between the source and destination
        # time: the round trip ping time (in millisec)

        char    = None
        string  = None
        matchReply      = None
        matchDestUnreach= None
        matchFrag       = None
        
        if retCode == 0:
            # 64 bytes from 1.1.1.1: icmp_seq=4 ttl=57 time=97.5 ms
            matchReply = self.__searchRegexInLine(stdOut, r'icmp_seq=\d+ ttl=\d+ time=(\d+\.?\d+) ms')

            time = 0
            if matchReply is not None:
                time = matchReply[0]

            # receipt of a reply
            char = "!" 
            string = "Reply to request %s (%s ms)" % (reqNum,time)

            self.rttList.append(float(time)) 

        elif retCode == 1:
            # From 172.241.0.3 icmp_seq=10 Destination Host Unreachable
            # From 2001:470:94:80::f icmp_seq=2 Destination unreachable: Address unreachable
            matchDestUnreach = self.__searchRegexInLine(stdOut, r'icmp_seq=\d+ Destination (Host )?[U|u]nreachable')

            # From 10.9.8.15 icmp_seq=1 Frag needed and DF set (mtu = 1500)
            # From 2001:470:94:80::f icmp_seq=1 Packet too big: mtu=1500
            matchFrag = self.__searchRegexInLine(stdOut, r'[Packet too big: |Frag needed and DF set (]mtu\s*=\s*(\d+)')

            if matchDestUnreach is not None:
                # a 'destination unreachable' error protocol data unit (PDU) was received 
                char = "U" 
                string = "Request %s destination unreachable" % (reqNum)

            elif matchFrag is not None:
                mtu = matchFrag[0]

                # fragmentation is needed, but the "don't fragment" bit in the IP header is set
                char = "M" 
                string = "Request %s fragmentation is needed (mtu=%s)" % (reqNum,mtu)

            else:
                # the network server timed out while waiting for a reply
                char = "." 
                string = "Request %s timed out" % (reqNum)

        else:
            char = "?" # Unknown packet type
            string = "Request %s unknown" % (reqNum)

        if not self._verbose:
            sys.stdout.write(char)
            sys.stdout.flush() # write everything to the terminal
        else:
            print string

        self._log("ping-handle-stdout").debug2("request #%s (rc=%s): char = %s , string = %s", reqNum, retCode, char, string)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _executePing (self, i, target, args):

        self.__printDebug("target=%s , args=%s" % (target, args))
        self._log("ping-command").info("target=%s , args=%s" % (target, args))

        retCode, stdOut, stdErr = Ping.ping(self._log, target, **args)
        
        if stdErr:
            # types of errors:
            #   bind: Cannot assign requested address
            #   cannot bind to specified iface, falling back: Operation not permitted
            #   connect: Network is unreachable
            #   ping: unknown host www.google.com
            #   ping: unknown iface eth-tg0
            stdErr = stdErr.strip()

            print stdErr
            self._log("ping-stderr").notice("#%s stderr (rc=%s): %s", i, retCode, stdErr)

            return ReturnCodes.kGeneralError 

        if self.pingSent == 0:
            self._handleFirstPing(stdOut)
        
        if stdOut:
            stdOut = stdOut.strip()

            self._log("ping-stdout").debug3("#%s stdout (rc=%s): %s", i, retCode, stdOut)
            self.__printDebug("out: %s\n rc = %s" % (stdOut, retCode))

        self.pingSent += 1
        self._handlePingStdout(i, retCode, stdOut)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _launch (self):

        # prepare ping arguements
        args = {'source'        : self._source,
                'version'       : self._ipVersion,
                'count'         : 1,
                'timeout'       : self._timeoutInterval,
                'size'          : self._packetSize}

        if self._pattern is not None:
            pdata = hex(self._pattern) # patterns must be specified as hex digits
            args['pattern'] = str(pdata)[2:]

        if self._donotFrag:
            args['mtu'] = "do" # prohibit fragmentation

        # run ping command
        i=0
        while i < self._repeatCount:

            i+=1
            rc = self._executePing(i, self._target, args)
            if rc != ReturnCodes.kOk:
                break
            
            if a.infra.process.getWasStopped():
                self._log("ping-process-stop-signal").info("process caught stop signal")
                break
    
            time.sleep(0.1)

    def genericAction_initFromDictionary (self, data):
        pass
            
#-----------------------------------------------------------------------------------------------------------------------
    def genericAction_run (self, args):

        parser = optparse.OptionParser(usage="",prog="ping")
        self._addToOptParser(parser)
        (self.options, self.args) = parser.parse_args(args)

        rc = self._prepare()
        if rc != ReturnCodes.kOk:
            return rc
  
        self._handlePingStart()

        try:
            self._launch()
    
        except IOError, ex:

            # Interrupted system call
            self._log("ping-run-error").error("Error during ping -  %s", ex)
       
        if self.pingSent > 0:
            self._handlePingSummary()

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _addToOptParser(self, optParser):
        optParser.add_option("--verbose", action="store_true", 
                             dest=self._OPTION_PARSER_FLAG_VERBOSE, default=False, help="Sets verbose output")
        optParser.add_option("--debug", action="store_true", 
                             dest=self._OPTION_PARSER_FLAG_DEBUG, default=False, help="Sets debug mode")
        optParser.add_option("--ip-address", type="string", default=None,
                              action="store", dest=self._OPTION_PARSER_IP_ADDRESS, help="Target IP address of the system to ping")
        optParser.add_option("--hostname", type="string", default=None,
                              action="store", dest=self._OPTION_PARSER_HOSTNAME, help="Target hostname of the system to ping")
        optParser.add_option("--ipv4", action="store_const", const=4, 
                             dest=self._OPTION_PARSER_IP_VERSION, help="Specifies IPv4 address prefixes")
        optParser.add_option("--ipv6", action="store_const", const=6, 
                             dest=self._OPTION_PARSER_IP_VERSION, help="Specifies IPv6 address prefixes")

        optParser.add_option("--count", type="int", default=5,
                      action="store", dest=self._OPTION_PARSER_COUNT, help="Specify repeat count. Range is 0 to 2147483647 [default: %default]")
        optParser.add_option("--source", type="string", default=None,
                      action="store", dest=self._OPTION_PARSER_SOURCE, help="Specify source IP address or source interface [default: %default]")
        optParser.add_option("--timeout", type="int", default=2,
                             action="store", dest=self._OPTION_PARSER_TIMEOUT, help="Specify the timeout interval (in seconds). Range is 0 to 3600 [default: %default]")
        optParser.add_option("--size", type="int", default=100,
                             action="store", dest=self._OPTION_PARSER_SIZE, help="Specify the datagram size (in bytes). Range is 36 to 18024 [default: %default]")
        optParser.add_option("--pattern", type="int", default=None,
                             action="store", dest=self._OPTION_PARSER_PATTERN, help="Specify the data pattern. Range is 0 to 65535 [default: %default]")
        optParser.add_option("--donotfrag", action="store_true", 
                             dest=self._OPTION_PARSER_DONOT_FRAG, default=False, help="Enables the Don't Fragment (DF) bit in the IP header")

