#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: yoave
# 

import os.path

import utils
from a.sys.net.lnx.iptables import IpTablesService

class InterfaceCounters (object):

    def __init__ (self):
        self.bytesIn  = 0
        self.bytesOut = 0

#-------------------------------------------------------------------------------------------------
class VolumeCounters (object):

    def __init__ (self):
        # Delivery has 2 Interfaces
        self.volumeCounters = [InterfaceCounters(),InterfaceCounters()]

#-------------------------------------------------------------------------------------------------
class IpTablesClient(object):
   
    def __init__ (self, logger):  
        self.__log = logger
        self.__conf = None
        self.__ipTablesService = IpTablesService(logger)

    #-------------------------------------------------------------------------------------------------
    def init (self, conf):
        self.__conf = conf

    #-------------------------------------------------------------------------------------------------
    def start (self):
        self.__updateIpTables()

    #-------------------------------------------------------------------------------------------------
    def end (self):
        self.__clearIpTables()

    #-------------------------------------------------------------------------------------------------
    def __updateIpTables (self):

        if self.__conf.isMini is True:        
            return # do nothing
        
        # add rules
        self.__doIpTables(self.__addIpTablesRules, "Add")

        # log ip tables
        self.__logIpTablesRules(4)
        self.__logIpTablesRules(6)

    #-------------------------------------------------------------------------------------------------
    def __clearIpTables (self):

        if self.__conf.isMini is True:
            return # do nothing
        
        # delete rules
        self.__doIpTables(self.__deleteIpTablesRules, "Delete")

    #-------------------------------------------------------------------------------------------------
    def __doIpTables (self, func, command):
        # loops over all delivery interfaces
        for iConf in self.__conf.InterfaceMap.values():
            
            port = self.__conf.port
            device = iConf.egressInterface
            protocol = IpTablesService.TCP_PROTOCOL_VALUE

            self.__log("ip-tables-command").notice("%s: Ip Tables Interface %s Rule - Device = %s -- Port = %s Protocol = %s", 
                                                     iConf.name, command, device, port, protocol)

            if device:
                # ipv4 tables
                func(4, device, port, protocol)

                # ipv6 tables
                func(6, device, port, protocol)

    #-------------------------------------------------------------------------------------------------
    def __addIpTablesRules (self, ipVersion, device, port, protocol):
        self.__ipTablesService.addInRule(ipVersion, device, port, protocol)
        self.__ipTablesService.addOutRule(ipVersion, device, port, protocol)

    #-------------------------------------------------------------------------------------------------
    def __deleteIpTablesRules (self, ipVersion, device, port, protocol):
        self.__ipTablesService.deleteInRule(ipVersion, device, port, protocol)
        self.__ipTablesService.deleteOutRule(ipVersion, device, port, protocol)

    #-------------------------------------------------------------------------------------------------
    def __logIpTablesRules (self, ipVersion):
        output  = self.__ipTablesService.showRules(ipVersion)
        self.__log("ip-tables-list-rules").notice("IPv%s Tables Rules:\n%s", ipVersion, output)

#-------------------------------------------------------------------------------------------------
class VolumeManager(object):
   
    def __init__ (self, logger):  
        self.__log = logger
        self.__conf = None
        self.__wasEnabledIpTables = True
        self._volumeReporter = None

    #-------------------------------------------------------------------------------------------------
    def init (self, conf):

        self.__conf = conf
        self.__wasEnabledIpTables = conf.deliveryVolumeEnableIpTables
        self._volumeReporter = self.__createVolumeReporter()
        
    #-------------------------------------------------------------------------------------------------  
    def collectVolume (self, volume):
        if self._volumeReporter is None:
            return False

        rc =  self._volumeReporter.collectVolumeInfo(volume)

        # ip tables enabled was changed
        if self.__wasEnabledIpTables != self.__conf.deliveryVolumeEnableIpTables:
            self.__log("ip-tables-enable-change").notice("Volume Manager Detected Delivery Volume Ip Tables Enabled changed from %s to %s", 
                                                        self.__wasEnabledIpTables, self.__conf.deliveryVolumeEnableIpTables)

            # create a new delivery volume reporter type and sample first volume
            # the dummy volume counters are used for current snapshot, so the next call will collect the real diff
            volumeDummy = VolumeCounters()
            self._volumeReporter = self.__createVolumeReporter()
            self._volumeReporter.collectVolumeInfo(volumeDummy)
            self.__wasEnabledIpTables = self.__conf.deliveryVolumeEnableIpTables

        return rc

    #-------------------------------------------------------------------------------------------------
    def __createVolumeReporter (self):

        if self.__conf.deliveryVolumeEnableIpTables is True:
            volumeReporter = IpTableVolumeReporter(self.__log)
        else:
            volumeReporter = InterfaceVolumeReporter(self.__log)

        volumeReporter.init(self.__conf)
        return volumeReporter

#-------------------------------------------------------------------------------------------------
class _BaseVolumeReporter(object):
   
    def __init__ (self, logger):  
        self._log = logger
        self._conf = None
        
        self.__initVolumeCounters = True
        self.__lastVolumeCounters = VolumeCounters()

    #-------------------------------------------------------------------------------------------------
    def init (self, conf):
        self._conf      = conf

    #-------------------------------------------------------------------------------------------------  
    def collectVolumeInfo (self, volume):

        if self._conf is None:
            return False

        curVolumeCounter = VolumeCounters()

        interfaces = self._conf.InterfaceMap.values()
        self._beforeCollectVolume(interfaces)

        i = 0   
        fail = 0 
        for iConf in interfaces:

            # Read Interfaces Counters
            if iConf.egressInterface and self._readInterfaceL2Bytes(iConf, curVolumeCounter.volumeCounters[i]):

                # RX Bytes
                if self.__lastVolumeCounters.volumeCounters[i].bytesIn == 0:
                    volume.volumeCounters[i].bytesIn = 0
                else:
                    volume.volumeCounters[i].bytesIn = curVolumeCounter.volumeCounters[i].bytesIn - self.__lastVolumeCounters.volumeCounters[i].bytesIn
                     
                self.__lastVolumeCounters.volumeCounters[i].bytesIn = curVolumeCounter.volumeCounters[i].bytesIn

                # TX Bytes
                if self.__lastVolumeCounters.volumeCounters[i].bytesOut == 0:
                    volume.volumeCounters[i].bytesOut = 0
                else:
                    volume.volumeCounters[i].bytesOut = curVolumeCounter.volumeCounters[i].bytesOut - self.__lastVolumeCounters.volumeCounters[i].bytesOut
                     
                self.__lastVolumeCounters.volumeCounters[i].bytesOut = curVolumeCounter.volumeCounters[i].bytesOut
            else:
                fail = fail + 1

            i = i + 1

        self._afterCollectVolume(interfaces)

        # Failed to read all interfaces counters
        if fail == len(self._conf.InterfaceMap):
            return False

        # Ignore first success read (Because diff is 0)
        if self.__initVolumeCounters:
            self.__initVolumeCounters = False
            return False
        else:
            return True
                
        return False

    # protected
    #-------------------------------------------------------------------------------------------------
    # Read Aggregated L2 Bytes from delivery Interfaces    
    def _readInterfaceL2Bytes (self, iConf, interCounters):

        #rx
        bytesIn  = self._readDeviceL2Bytes(iConf.egressInterface, True)
        #tx
        bytesOut = self._readDeviceL2Bytes(iConf.egressInterface, False)

        self._log("interface-l2-bytes").debug4("Read Interface '%s': RX L2 Bytes - %s , TX L2 Bytes - %s", 
                                                iConf.egressInterface, bytesIn, bytesOut)
    
        #fail in reading
        if bytesIn < 0 or bytesOut < 0:
            return False
            
        interCounters.bytesIn  = bytesIn    
        interCounters.bytesOut = bytesOut                   
       
        return True

    #-------------------------------------------------------------------------------------------------
    # Read L2 Bytes from delivery Ethernet Interface    
    def _readDeviceL2Bytes (self, egressInterface, isRx):
        raise NotImplementedError

    #-------------------------------------------------------------------------------------------------
    def _clear (self):
        self.__initVolumeCounters = True
        self.__lastVolumeCounters = VolumeCounters()

    #-------------------------------------------------------------------------------------------------
    def _beforeCollectVolume(self, interfaces):
        __pychecker__="no-argsused"  # interfaces not used
        pass

    #-------------------------------------------------------------------------------------------------
    def _afterCollectVolume(self, interfaces):
        __pychecker__="no-argsused"  # interfaces not used
        pass

#-------------------------------------------------------------------------------------------------
class InterfaceVolumeReporter(_BaseVolumeReporter):
    """  Reports volume based on the statistics files at /sys/class/net/
    """
   
    def __init__ (self, logger):  
        _BaseVolumeReporter.__init__(self, logger)

    #-------------------------------------------------------------------------------------------------
    def _readDeviceL2Bytes (self, egressInterface, isRx):
        
        if isRx:
            filePath =  os.path.join("/sys/class/net/", egressInterface, "statistics/rx_bytes")
        else:
            filePath =  os.path.join("/sys/class/net/", egressInterface, "statistics/tx_bytes")

        try:
            tempFile = open(filePath,'r')
        except IOError, e:
            self._log("read-l2-bytes-fail").error("Failed to Open Interface File for reading L2 bytes %s - %s", filePath, utils.parseErrnoToString(e))
            return -1

        bytesRead =  int(tempFile.read())
        tempFile.close()
       
        return bytesRead

#-------------------------------------------------------------------------------------------------
class IpTableVolumeReporter(_BaseVolumeReporter):
    """  Reports volume based on the ip tables rules
    """
   
    def __init__ (self, logger):  
        _BaseVolumeReporter.__init__(self, logger)

        self.ipTablesService = IpTablesService(logger)
        self._ipv4Rules = {}
        self._ipv6Rules = {}

    #-------------------------------------------------------------------------------------------------
    def init (self, conf):
        _BaseVolumeReporter.init(self, conf)
        self.prevPort = self._conf.port

    #-------------------------------------------------------------------------------------------------  
    def collectVolumeInfo (self, volume):

        if self._conf.port != self.prevPort:
            self._log("port-change").notice("Port changed from %s to %s", self.prevPort, self._conf.port)
            self.prevPort = self._conf.port
            self._clear()

        return _BaseVolumeReporter.collectVolumeInfo(self, volume)

    #-------------------------------------------------------------------------------------------------
    def _readDeviceL2Bytes (self, egressInterface, isRx):
        
        bytesIpv4Read = self.__readDeviceL2BytesPerIpVersion(4, self._ipv4Rules, egressInterface, isRx)
        bytesIpv6Read = self.__readDeviceL2BytesPerIpVersion(6, self._ipv6Rules, egressInterface, isRx)

        # in case an error occured
        if bytesIpv4Read < 0 or bytesIpv6Read < 0:
            return -1

        numL2Bytes =  bytesIpv4Read + bytesIpv6Read
       
        return numL2Bytes

    #-------------------------------------------------------------------------------------------------
    def __readDeviceL2BytesPerIpVersion (self, ipVersion, rulesMap, egressInterface,isRx):
        
        if not rulesMap.has_key(egressInterface):
            self._log("interface-ip-rule-match-fail").error("Failed to Match Interface %s IPv%s Rule for reading L2 bytes (RX=%s)", 
                                                            egressInterface, ipVersion, isRx)
            return -1

        rules = rulesMap[egressInterface]
        if len(rules) != 2:
            self._log("interface-ip-rule-match-fail").error("Failed to Match Interface %s IPv%s Rule for reading L2 bytes (RX=%s)",
                                                            egressInterface, ipVersion, isRx)
            return -1

        if isRx:
            rule = rules[0] # input chain
        else:
            rule = rules[1] # output chain

        numL3Bytes = 0
        numPackets = 0
        matchedIpRule = rule.split(None,2)

        try:
            numPackets = int(matchedIpRule[0])
            numL3Bytes = int(matchedIpRule[1])
            
        except (IndexError, ValueError, TypeError), e:
            self._log("read-l2-bytes-fail").error("Failed to Parse Interface %s IPv%s Rule for reading L2 bytes %s - %s", 
                                                  egressInterface, ipVersion, matchedIpRule, utils.parseErrnoToString(e))
            return -1

        # compute layer 2 bytes
        numL2Bytes =  numL3Bytes + numPackets*self._conf.kConf.kEthHeaderLength

        if isRx is True:
            self._log("interface-l2-rx-bytes-ip-version").debug4("Read Interface '%s': IPv%s RX Packets - %s , L3 Bytes - %s, L2 Bytes - %s",
                                                                 egressInterface, ipVersion, numPackets, numL3Bytes, numL2Bytes)
        else:
            self._log("interface-l2-tx-bytes-ip-version").debug4("Read Interface '%s': IPv%s TX Packets - %s , L3 Bytes - %s, L2 Bytes - %s",
                                                                 egressInterface, ipVersion, numPackets, numL3Bytes, numL2Bytes)

        return numL2Bytes

    #-------------------------------------------------------------------------------------------------
    def _beforeCollectVolume(self, interfaces):

        self.__handleRulesOutput(interfaces, 4, self._ipv4Rules)
        self.__handleRulesOutput(interfaces, 6, self._ipv6Rules)

    #-------------------------------------------------------------------------------------------------
    def _afterCollectVolume(self, interfaces):
        __pychecker__="no-argsused"  # interfaces not used

        self._ipv4Rules.clear()
        self._ipv6Rules.clear()

    #-------------------------------------------------------------------------------------------------
    def __handleRulesOutput(self, interfaces, ipVersion, rulesMap):

        port = self._conf.port
        protocol = IpTablesService.TCP_PROTOCOL_VALUE
    
        output = self.ipTablesService.showRules(ipVersion, [protocol, port])
        self._log("ip-table-output").debug5("Ip Table Output - %s",output)

        # filters ACCEPT/DROP rules
        ruleList = output.splitlines()
        ruleList = filter(lambda x: x.split()[2] == protocol, ruleList) 

        # populate interface->rules map
        for iface in interfaces:
            rulesMap[iface.egressInterface] = []

        # loops over all rules
        for rule in ruleList:

            # loops over all interfaces
            for iface in interfaces:
                if iface.egressInterface in rule:

                    # found a match - add rule to map
                    rulesMap[iface.egressInterface].append(rule) 
                    break

        if len(rulesMap) > 0:
            self._log("ip-table-rules").debug5("Ip Table Rules per Interface - %s",rulesMap)

