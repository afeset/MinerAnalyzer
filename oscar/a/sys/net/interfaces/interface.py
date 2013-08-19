# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from ip import IPv4If
from ip import IPv6If
from ip import IpVersion
from device import Device
from management import Management 
from content import Content
from ethernet import Ethernet
from link import Link
from connectivity import ConnectivityCheck
from a.infra.basic.return_codes import ReturnCodes
from threading import Thread
from oper.line_nic import LineNicStats
from a.infra.misc.timeout_guard import TimeoutGuard
from a.sys.blinky.trx_phase import TrxPhase
from a.sys.blinky.trx_progress import TrxProgress
import a.sys.net.lnx.device
import a.sys.net.lnx.common
import a.sys.net.lnx.route
import a.sys.blinky.util
import a.infra.process
import a.api.user_log.msg.net
import a.infra.net.ip_address
import a.infra.net.ip_network
import time
import Queue

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.counters.counters_oper_data_gen import CountersOperData
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.status.status_oper_data_gen import StatusOperData
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.alarms.alarms_oper_data_gen import AlarmsOperData

from a.api.yang.modules.common.qwilt_types.qwilt_types_module_gen import Truthvalue
from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import OperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import DeviceCountersClearEventType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import DriverTypeType
from a.api.yang.modules.common.iana.iana_if_type_mib.iana_if_type_mib_module_gen import Ianaiftype
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import MibAdminStatusType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceIpv6ConnectivityFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceIpv4ConnectivityFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import ConnectivityOperationalStatusReasonType

from a.sys.net.tech_interfaces.tech.interfaces.interface.status.blinky_status_oper_gen import BlinkyOperStatus as BlinkyOperIfStatus
from a.sys.net.tech_interfaces.tech.interfaces.interface.counters.blinky_counters_oper_gen import BlinkyOperCounters as BlinkyOperIfCounters
from a.sys.net.tech_interfaces.tech.interfaces.interface.continuous_counters.blinky_continuous_counters_oper_gen import BlinkyOperContinuousCounters as BlinkyOperIfContCounters64Bit
from a.sys.net.tech_interfaces.tech.interfaces.interface.continuous_counters_32bit.blinky_continuous_counters_32bit_oper_gen import BlinkyOperContinuousCounters32Bit as BlinkyOperIfContCounters32Bit
from a.sys.net.tech_interfaces.tech.interfaces.interface.alarms.blinky_alarms_oper_gen import BlinkyOperAlarms as BlinkyOperIfAlarms

if  __package__ is None:
    G_NAME_GROUP_NET_INTERFACES_INTERFACE = "unknown"
else:
    from . import G_NAME_GROUP_NET_INTERFACES_INTERFACE
      
class IpData(object):
    def __init__(self):
        self.ipAddress = ""
        self.defaultGateway = ""

##############################################
# This class manages the network interface configuration and protocol addresses:
# 1) Network device and the corresponding commands display and change the state of devices 
# 2) The address is a protocol (IPv4 or IPv6) address attached to a network device
##############################################
class Interface(object):
    """This class represents a network device"""

    TECH_IPV4_ADDRESS = a.infra.net.ip_network.Ipv4Network("10.100.101.100/24")
    MANAGEMENT_TABLE_ID = "main"
    DELIVERY_TABLE_ID_PATTERN = "10%s" # e.g. 10X pattern, where x is the interface index

    # rate calculated on last 5 minutes
    PERIODIC_COUNTERS_NUM_INTERVALS = 3     # 3 times in 30 seconds
    PERIODIC_COUNTERS_INTERVAL_RATE_SEC = 10# 10 seconds
    DEVICE_EVENTS_INTERVAL_RATE_SEC = 3     # 3 seconds
    CONNECTIVITY_CHECK_INTERVAL_RATE_SEC = 0.5 # 0.5 sec

    KEY_OS_RX_PACKETS   = "rx_packets"
    KEY_OS_RX_BYTES     = "rx_bytes"
    KEY_OS_RX_ERRORS    = "rx_errors"
    KEY_OS_RX_DROPPED   = "rx_dropped"
    KEY_OS_TX_PACKETS   = "tx_packets"
    KEY_OS_TX_BYTES     = "tx_bytes"
    KEY_OS_TX_ERRORS    = "tx_errors"
    KEY_OS_TX_DROPPED   = "tx_dropped"

    DEFAULT_TIMEOUT_MILI_SEC = 300  # 300 mili seconds
    OPER_TIMEOUT_MILI_SEC    = 1000 # 1 seconds
    MAX_TIMEOUT_MILI_SEC     = 1500 # 1.5 seconds

    MAX_UINT_32BIT = pow(2,32)

    # alarms reasons mapping
    ourLinkAlarmReasons = {True   : InterfaceFailureReasonType.kLinkOperDown}

    ourIpv4AlarmReasons = {ConnectivityOperationalStatusReasonType.kLinkOperationalStatusDown   : InterfaceIpv4ConnectivityFailureReasonType.kLinkOperDown,
                           ConnectivityOperationalStatusReasonType.kArpTestFailure              : InterfaceIpv4ConnectivityFailureReasonType.kArpTestFailure,
                           ConnectivityOperationalStatusReasonType.kPingTestFailure             : InterfaceIpv4ConnectivityFailureReasonType.kPingTestFailure}

    ourIpv6AlarmReasons = {ConnectivityOperationalStatusReasonType.kLinkOperationalStatusDown   : InterfaceIpv6ConnectivityFailureReasonType.kLinkOperDown,
                           ConnectivityOperationalStatusReasonType.kNeighborDiscoveryTestFailure: InterfaceIpv6ConnectivityFailureReasonType.kNeighborDiscoveryTestFailure,
                           ConnectivityOperationalStatusReasonType.kPingTestFailure             : InterfaceIpv6ConnectivityFailureReasonType.kPingTestFailure}

    # mib naming prefix mapping
    ourMibNamePrfixMap = {"GigabitEthernet" : "Gi",
                          "TenGigE"         : "Tg"}


    # GigabitEthernet
    ourGigEthCounterToSetDict = { # platforms 6a2, 6b2, 10b5
                                 "rx_bcast_packets":"setInBroadcastPackets",
                                 "rx_mcast_packets":"setInMulticastPackets",
                                 "rx_ucast_packets":"setInUnicastPackets",
                                 "tx_bcast_packets":"setOutBroadcastPackets",
                                 "tx_mcast_packets":"setOutMulticastPackets",
                                 "tx_ucast_packets":"setOutUnicastPackets",
                
                                 # platforms 6v2
                                 "rx_broadcast":"setInBroadcastPackets",
                                 "rx_multicast":"setInMulticastPackets",
                                 "tx_broadcast":"setOutBroadcastPackets",
                                 "tx_multicast":"setOutMulticastPackets"}
    # TenGigE
    ourTenGigEthCounterToSetDict = { # platforms 6a2, 6b2, 10b5
                                     "broadcast":"setInBroadcastPackets",
                                     "multicast":"setInMulticastPackets"}

    ourSysNetProcs = {"/proc/sys/net/ipv6/conf/%s/accept_dad"   : 0,
                      "/proc/sys/net/ipv6/conf/%s/dad_transmits": 0,
                      "/proc/sys/net/ipv6/conf/%s/autoconf": 0}

    #-----------------------------------------------------------------------------------------------------------------------
    class CachedIpData(IpData):
        def __init__(self):
            IpData.__init__(self)
            self.queue = Queue.Queue()

    def __init__ (self, logger, name):
        """Instantiate a new a network device object.

        Args:
            name: the interface name
            deviceName: the netwrok device
            tableid: tableid may be a number or a string

        Raises:
            None
        """

        self.name = name
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_INTERFACES_INTERFACE, instance = self.name)
        self.isActiveModule = False
        self.allowDynamicConfig = False
        self.lineNicsFile = None # read only
        self.snmpTrapsManager = None

        ifPrefix, ifIndex = self.name.split("0/")
        self.ifIndex    = int(ifIndex)
        self.mibName    = "%s0/%s" % (Interface.ourMibNamePrfixMap.get(ifPrefix,None),ifIndex)
        self.driverType = None

        # data
        self.candidateEnabled = False
        self.runningEnabled = False
        self.candidateTechMode = False
        self.runningTechMode = False
        self.shouldSendGratuitousArp = True
        self.tableid = None
        self.mibIfIndex= None 
        self.isTrxStart = False
        self.isFirstTrx = True
        self.countersOnStart = CountersOperData()
        self.countersOnClear = CountersOperData()
        self.countersFromLastOsClear = CountersOperData()
        self.deliveryStabilityDelay = 0 # temp@2.7 - 1/15/2013
        self.muteReporting = False

        # cached data - use to cache running ip data for repeated connectivity check
        self.ipv4CacheData = Interface.CachedIpData()
        self.ipv6CacheData = Interface.CachedIpData()
        
        # containers
        self.content = None
        self.mng = None
        self.device = None
        self.ipv4 = None
        self.ipv6 = None
        self.ethernet = None
        self.link = None
        self.connectivityCheck = None

        currentTime = time.time()

        # counters oper data cache
        self.countersOperData = CountersOperData()
        self.countersLastUpdateTime = currentTime

        # status oper data cache
        self.statusOperData = StatusOperData()
        self.statusLastUpdateTime = currentTime

        # alarms oper data cache
        self.alarmsOperData = AlarmsOperData()
        self.alarmsLastUpdateTime = currentTime

        self.blinkyInterface = None
        self.thread = None
        self.periodicCounters = PeriodicCountersContainer(self._log, self, self.PERIODIC_COUNTERS_NUM_INTERVALS)

#-----------------------------------------------------------------------------------------------------------------------  
    def setAsActiveModule(self):
        self._log("interface-active-module").debug1("Interface %s: set as active module", self.name)
        self.isActiveModule = True
        
#-----------------------------------------------------------------------------------------------------------------------  
    def setAllowDynamicConfig(self):
        self._log("interface-allow-dynamic-config").debug1("Interface %s: allow dynamic configuration", self.name)
        self.allowDynamicConfig = True

#-----------------------------------------------------------------------------------------------------------------------  
    def setLineNicsFile(self, lineNicsFile):
        self._log("interface-line-nics-file").debug1("Interface %s: line nics file is %s", self.name, lineNicsFile)
        self.lineNicsFile = lineNicsFile

#-----------------------------------------------------------------------------------------------------------------------  
    def setSnmpTrapsManager(self, snmpTrapsManager):
        self._log("interface-snmp-traps-manager").debug1("Interface %s: set snmp traps manager", self.name)
        self.snmpTrapsManager = snmpTrapsManager

#-----------------------------------------------------------------------------------------------------------------------  
    def shutdown(self):
        if self.thread is not None:
            if self.isFirstTrx is False:
                # stop and wait until the thread terminates
                self.thread.stop()
                self.thread.join(0.1)
        
                if self.thread.isAlive():
                    self._log("interface-thread-alive").notice("Interface %s: after deletion thread is still alive", self.name)

        self.thread=None
       
#-----------------------------------------------------------------------------------------------------------------------  
    def __del__(self):
        self.shutdown()
               
#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        strList = []
        strList.append("%s:" % self.name)
        strList.append("device: %s" % self.device)
        strList.append("ipv4: %s" % self.ipv4)
        strList.append("ipv6: %s" % self.ipv6)
        strList.append("mng: %s" % self.mng)
        strList.append("content: %s" % self.content)
        
        return '\t'.join(strList) 

#-----------------------------------------------------------------------------------------------------------------------
    def __eq__(self, other):
        try:
            return (self.name == other.name)
        except AttributeError:
            return NotImplemented

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyInterface:
            self.blinkyInterface.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def isUp(self, actual=True):
        if actual is True:
            return self.runningEnabled
        else:
            return self.candidateEnabled

#-----------------------------------------------------------------------------------------------------------------------
    def deviceName(self, actual=True):
        if not self.device is None:
            if actual is True:
                return self.device.runningOsName
            else:
                return self.device.candidateOsName

        return None

#-----------------------------------------------------------------------------------------------------------------------
    def actionOnDeviceChange(self):
        self._log("device-change-call").debug5("%s: called actionOnDeviceChange().", self.name)

        if not self.device is None:
            self.device.actionOnStatusChange()

#-----------------------------------------------------------------------------------------------------------------------
    def actionOnConnectivityCheck(self):
        self._log("connectivity-check-call").debug5("%s: called actionOnConnectivityCheck().", self.name)

        if self.link and self.device:
            # test link availability (for all interfaces)
            self.link.testLinkAvailability()

            # test connectivity check (only for delivery interfaces)
            if self.isDeliveryEnabled():
                if self.connectivityCheck:

                    linkOperStatus = self.link.isLinkUp()
                    linkAdminStatus = self.runningEnabled

                    # ipv4 check
                    self.actionOnIpConnectivityCheck(self.device.runningOsName, 
                                                     linkOperStatus, linkAdminStatus,
                                                     self.ipv4CacheData,
                                                     version=4)

                    # ipv6 check
                    self.actionOnIpConnectivityCheck(self.device.runningOsName, 
                                                     linkOperStatus, linkAdminStatus,
                                                     self.ipv6CacheData,
                                                     version=6)

#-----------------------------------------------------------------------------------------------------------------------
    def actionOnIpConnectivityCheck(self, osName, linkOperStatus, linkAdminStatus, cacheData, version):
        self._log("connectivity-check-call-ip").debug5("%s: called IPv%s actionOnIpConnectivityCheck().", self.name, version)

        # ip check
        # Note: the read/write operation is thread-safe
        try:
            newData = cacheData.queue.get(block=True, timeout=0.1)
            newConf = True                
        except Queue.Empty:
            newConf = False

        # handle new configuration
        if newConf:
            cacheData.ipAddress      = newData.ipAddress
            cacheData.defaultGateway = newData.defaultGateway

            self._log("queue-get-data").info("%s: get new config from queue ipv%s address '%s' and default-gateway '%s'",
                                             self.name, version, newData.ipAddress, newData.defaultGateway)


        self.connectivityCheck.actionOnConnectivityCheck(osName, linkOperStatus, linkAdminStatus,
                                                         cacheData.defaultGateway, 
                                                         cacheData.ipAddress,
                                                         version=version)

        self._log("ip-connectivity-check").debug5("%s: ipv%s connectivity-check address '%s' and default-gateway '%s'",
                                                  self.name, version, cacheData.ipAddress, cacheData.defaultGateway)

#-----------------------------------------------------------------------------------------------------------------------
    def hasDefaultGateway(self, version=IpVersion.kIPv4):
        return (not self.getDefaultGateway(version) is None) 

#-----------------------------------------------------------------------------------------------------------------------
    def getDefaultGateway(self, version=IpVersion.kIPv4):
        ip = self.ipv4

        if version == IpVersion.kIPv6:
            ip = self.ipv6

        if not ip is None:
            return ip.candidateDefaultGateway

        return None 

#-----------------------------------------------------------------------------------------------------------------------
    def hasAddress(self, version=IpVersion.kIPv4):
        return (not self.getIpNetwork(version) is None) 

#-----------------------------------------------------------------------------------------------------------------------
    def getIpAddress(self, version=IpVersion.kIPv4):
        ipNetwork = self.getIpNetwork(version)

        if not ipNetwork is None:
            return ipNetwork.ip

        return None 

#-----------------------------------------------------------------------------------------------------------------------
    def getIpNetwork(self, version=IpVersion.kIPv4):
        ip = self.ipv4
        if version == IpVersion.kIPv6:
            ip = self.ipv6

        if not ip is None:
            return ip.getCandidateAddress()

        return None 

#-----------------------------------------------------------------------------------------------------------------------
    def isManagementEnabled(self):
        return self.mng and self.mng.isServiceEnabled()
         
#-----------------------------------------------------------------------------------------------------------------------
    def isLineEnabled(self):
        return self.content and self.content.isLineEnabled()

#-----------------------------------------------------------------------------------------------------------------------
    def isDeliveryEnabled(self):
        return self.content and self.content.isDeliveryEnabled()

#-----------------------------------------------------------------------------------------------------------------------
    def _isCountersClearPostUp(self):
        if self.device:
            return (self.device.countersClearEvent == DeviceCountersClearEventType.kOnPortUp)

        return False
                       
#-----------------------------------------------------------------------------------------------------------------------
    def _isCountersClearPostDown(self):
        if self.device:
            return (self.device.countersClearEvent == DeviceCountersClearEventType.kOnPortDown)

        return False

#-----------------------------------------------------------------------------------------------------------------------
    def overlaps(self, other):
        """Tell if self is partly contained in other."""

        isOverlaps = False

        if self.ipv4 is not None:
            isOverlaps = self.ipv4.overlaps(other.ipv4) 

        if isOverlaps is False:
            if self.ipv6 is not None:
                isOverlaps = self.ipv6.overlaps(other.ipv6) 

        return isOverlaps

#-----------------------------------------------------------------------------------------------------------------------
    def equals(self, other):
        """Tell if self source equals to other."""

        isEquals = False

        if self.ipv4 is not None:
            isEquals = self.ipv4.equals(other.ipv4) 

        if isEquals is False:
            if self.ipv6 is not None:
                isEquals = self.ipv6.equals(other.ipv6) 

        return isEquals

#-----------------------------------------------------------------------------------------------------------------------
    def showStatistics(self):
        """This function displays the interface statitics.
        """

        deviceName = self.deviceName()

        if deviceName:
            stats = a.sys.net.lnx.device.DeviceUtils.getStatistics(self.name, self._log, deviceName) 
            if stats:
                for key in stats:
                    print "%s: %s" % (key, stats[key])

#-----------------------------------------------------------------------------------------------------------------------
    def showOperState(self):
        """This function displays the interface activation mode on/off.
        """
        
        deviceName = self.deviceName()

        if deviceName:
            state = a.sys.net.lnx.device.DeviceUtils.getOperState(self.name, self._log, deviceName) 
            print "operstate: %s" % state

#-----------------------------------------------------------------------------------------------------------------------
    def showStateOnOs(self):
        """This function displays the interface as seen by the OS.
        """

        deviceName = self.deviceName()

        if deviceName:
            rc = a.sys.net.lnx.device.IpLink.showDevice(self._log, deviceName) 
            if a.sys.net.lnx.common.Command.isReturnOk(rc):
                print rc[1] # stdout
            else:
                print rc[2] # stderr


#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyInterface):

        self._log("notify-attach-blinky").debug2("%s: attach by blinky interface", self.name)

        # ipv4
        blinkyInterface.setCreateIpv4Functor(self.createIpv4)
        blinkyInterface.setDeleteIpv4Functor(self.deleteIpv4)

        # ipv6
        blinkyInterface.setCreateIpv6Functor(self.createIpv6)
        blinkyInterface.setDeleteIpv6Functor(self.deleteIpv6)

        # content
        blinkyInterface.setCreateContentFunctor(self.createContent)
        blinkyInterface.setDeleteContentFunctor(self.deleteContent)

        # management
        blinkyInterface.setCreateManagementFunctor(self.createMng)
        blinkyInterface.setDeleteManagementFunctor(self.deleteMng)

        # device
        blinkyInterface.setCreateDeviceFunctor(self.createDevice)
        blinkyInterface.setDeleteDeviceFunctor(self.deleteDevice)
    

        if self.isActiveModule is True:
            # ethernet
            blinkyInterface.setCreateEthernetFunctor(self.createEthernet)
            blinkyInterface.setDeleteEthernetFunctor(self.deleteEthernet)

            # link
            blinkyInterface.setCreateLinkFunctor(self.createLink)
            blinkyInterface.setDeleteLinkFunctor(self.deleteLink)

            # connectivity check
            blinkyInterface.setCreateConnectivityCheckFunctor(self.createConnectivityCheck)
            blinkyInterface.setDeleteConnectivityCheckFunctor(self.deleteConnectivityCheck)

            # clear-counters
            blinkyInterface.setDoActionFunctor(self.doActionClearCounters)

            # change default timeout for commit-private-before 
            # Note (1) activate takes up to 1100 mili
            #      (2) rename   takes up to 300  mili
            commitPrivatePhase = TrxPhase(TrxPhase.kCommit, TrxPhase.kPrivate)
            commitPrivateBeforeProgress = TrxProgress(commitPrivatePhase, TrxProgress.kBefore)
            blinkyInterface.setFunctorTimeoutForProgress(blinkyInterface.TRX_PROGRESS_FUNCTOR, 
                                                         commitPrivateBeforeProgress, 
                                                         Interface.MAX_TIMEOUT_MILI_SEC)
            
        self.blinkyInterface = blinkyInterface

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinkyOper(self, blinkyInterface):

        # get continuous-counters-64bit functor
        self._log("get-blinky-oper-continuous-counters-64bit-obj").debug1("creating BlinkyOperIfContCounters64Bit on %s", self)
        blinkyOper64BitObj = BlinkyOperIfContCounters64Bit(self._log)
        blinkyOper64BitObj.setFunctorTimeout(blinkyOper64BitObj.GET_OBJ_FUNCTOR, Interface.OPER_TIMEOUT_MILI_SEC)

        if hasattr(blinkyOper64BitObj, 'setBasicFunctors'):
            blinkyOper64BitObj.setConfigObj(blinkyInterface)
            blinkyOper64BitObj.setDomain(blinkyInterface.getDomain())
            blinkyOper64BitObj.setBasicFunctors(self.getContCounters64Bit)
            rc = blinkyOper64BitObj.activate()
            if (rc != ReturnCodes.kOk):
                self._log("attach-to-blinky-oper-activate-continuous-counters-64bit-failed").error("blinkyOper64BitObj.activate() failed. blinkyOper64BitObj=%s", blinkyOper64BitObj)
                # not failing the transaction in commit phase
                return

        # get continuous-counters-32bit functor
        self._log("get-blinky-oper-continuous-counters-32bit-obj").debug1("creating BlinkyOperIfContCounters32Bit on %s", self)
        blinkyOper32BitObj = BlinkyOperIfContCounters32Bit(self._log)
        blinkyOper32BitObj.setFunctorTimeout(blinkyOper32BitObj.GET_OBJ_FUNCTOR, Interface.OPER_TIMEOUT_MILI_SEC)

        if hasattr(blinkyOper32BitObj, 'setBasicFunctors'):
            blinkyOper32BitObj.setConfigObj(blinkyInterface)
            blinkyOper32BitObj.setDomain(blinkyInterface.getDomain())
            blinkyOper32BitObj.setBasicFunctors(self.getContCounters32Bit)
            rc = blinkyOper32BitObj.activate()
            if (rc != ReturnCodes.kOk):
                self._log("attach-to-blinky-oper-activate-continuous-counters-32bit-failed").error("blinkyOper32BitObj.activate() failed. blinkyOper32BitObj=%s", blinkyOper32BitObj)
                # not failing the transaction in commit phase
                return

#-----------------------------------------------------------------------------------------------------------------------
    def doActionClearCounters(self, userInfo, actionPoint, actionName, params, nParams):
        self._log("do-action-clear-counters").debug2('called. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s', 
                                                     userInfo, actionPoint, actionName, params, nParams)

        rc = self._doClearCounters()
        
        if rc != ReturnCodes.kOk:
            self.blinkyInterface.setActionError(userInfo, '%s: failed on interface clear counters', self.name)

        # ClearCounter @ user-log
        a.infra.process.logUserMessage(a.api.user_log.msg.net.ClearCounter(self.name))   

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def _doClearCounters(self):
        self.countersOnClear.__init__() # clear
        rc = self.getIfCounters(None, self.countersOnClear, isRateCounters=False, shouldSetExtCounters=True)
        self._log("do-clear-counters").info("%s: clear counters snapshot - %s", self.name, self.countersOnClear.debugStr())

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def createIpv4(self, phase, blinkyIpv4):
        self._log("create-ipv4").debug2("%s: blinkyIpv4=%s", phase, blinkyIpv4)

        if (phase.isPreparePrivate()):

            ipv4 = IPv4If(self._log)
            self.ipv4 = a.sys.blinky.util.simple_container_wrapper.SimpleContainerWrapper(self._log, ipv4, 
                                                                                          notifyTrxProgressFunctor=self.isActiveModule, 
                                                                                          notifyDescendantsModifications=True)
            self.ipv4.attachToBlinky(blinkyIpv4)

        elif (phase.isAbortPrivate()):
            self.ipv4 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteIpv4(self, phase):
        self._log("delete-ipv4").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.ipv4 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createIpv6(self, phase, blinkyIpv6):
        self._log("create-ipv6").debug2("%s: blinkyIpv6=%s", phase, blinkyIpv6)

        if (phase.isPreparePrivate()):

            ipv6 = IPv6If(self._log)
            self.ipv6 = a.sys.blinky.util.simple_container_wrapper.SimpleContainerWrapper(self._log, ipv6, 
                                                                                          notifyTrxProgressFunctor=self.isActiveModule, 
                                                                                          notifyDescendantsModifications=True)
            self.ipv6.attachToBlinky(blinkyIpv6)

        elif (phase.isAbortPrivate()):
            self.ipv6 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteIpv6(self, phase):
        self._log("delete-ipv6").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.ipv6 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createContent(self, phase, blinkyContent):
        self._log("create-content").debug2("%s: blinkyContent=%s", phase, blinkyContent)

        if (phase.isPreparePrivate()):

            content = Content(self._log)
            self.content = a.sys.blinky.util.simple_container_wrapper.SimpleContainerWrapper(self._log, content, 
                                                                                             notifyTrxProgressFunctor=self.isActiveModule, 
                                                                                             notifyDescendantsModifications=True)
            self.content.attachToBlinky(blinkyContent)

        elif (phase.isAbortPrivate()):
            self.content = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteContent(self, phase):
        self._log("delete-content").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.content = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createMng(self, phase, blinkyMng):
        self._log("create-mng").debug2("%s: blinkyMng=%s", phase, blinkyMng)

        if (phase.isPreparePrivate()):

            mng = Management(self._log)
            self.mng = a.sys.blinky.util.simple_container_wrapper.SimpleContainerWrapper(self._log, mng)
            self.mng.attachToBlinky(blinkyMng)

        elif (phase.isAbortPrivate()):
            self.mng = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteMng(self, phase):
        self._log("delete-mng").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.mng = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createDevice(self, phase, blinkyDevice):
        self._log("create-device").debug2("%s: blinkyDevice=%s", phase, blinkyDevice)

        if (phase.isPreparePrivate()):

            device = Device(self._log, self)
            shouldSetOperDataFunctor = self.isActiveModule

            self.device = a.sys.blinky.util.simple_container_wrapper.SimpleContainerWrapper(self._log, 
                                                                                            device,
                                                                                            setOperDataFunctor=shouldSetOperDataFunctor)
            self.device.attachToBlinky(blinkyDevice)

        elif (phase.isCommitPublic()):
            self.device.attachToBlinkyOper()
        elif (phase.isAbortPrivate()):
            self.device = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteDevice(self, phase):
        self._log("delete-device").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.device = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createEthernet(self, phase, blinkyEthernet):
        self._log("create-ethernet").debug2("%s: blinkyEthernet=%s", phase, blinkyEthernet)

        if (phase.isPreparePrivate()):

            ethernet = Ethernet(self._log, self)

            isLine = self.isLineEnabled()
            shouldSetOperDataFunctor = (self.isActiveModule and not isLine)

            self.ethernet = a.sys.blinky.util.simple_container_wrapper.SimpleContainerWrapper(self._log,
                                                                                              ethernet,
                                                                                              setOperDataFunctor=shouldSetOperDataFunctor)
            self.ethernet.attachToBlinky(blinkyEthernet)

        elif (phase.isCommitPublic()):
            self.ethernet.attachToBlinkyOper()
        elif (phase.isAbortPrivate()):
            self.ethernet = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteEthernet(self, phase):
        self._log("delete-ethernet").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.ethernet = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createLink(self, phase, blinkyLink):
        self._log("create-link").debug2("%s: blinkyLink=%s", phase, blinkyLink)

        if (phase.isPreparePrivate()):

            link = Link(self._log, self)

            shouldSetOperDataFunctor = self.isActiveModule

            self.link = a.sys.blinky.util.simple_container_wrapper.SimpleContainerWrapper(self._log,
                                                                                          link,
                                                                                          setOperDataFunctor=shouldSetOperDataFunctor)
            self.link.attachToBlinky(blinkyLink)

        elif (phase.isCommitPublic()):
            self.link.attachToBlinkyOper()
        elif (phase.isAbortPrivate()):
            self.link = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteLink(self, phase):
        self._log("delete-link").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.link = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createConnectivityCheck(self, phase, blinkyConnectivityCheck):
        self._log("create-connectivity-check").debug2("%s: blinkyConnectivityCheck=%s", phase, blinkyConnectivityCheck)

        if (phase.isPreparePrivate()):

            connectivityCheck = ConnectivityCheck(self._log, self.name)
            self.connectivityCheck = a.sys.blinky.util.simple_container_wrapper.SimpleContainerWrapper(self._log, connectivityCheck,
                                                                                                       notifyDescendantsModifications=False)
            self.connectivityCheck.attachToBlinky(blinkyConnectivityCheck)

        elif (phase.isAbortPrivate()):
            self.connectivityCheck = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteConnectivityCheck(self, phase):
        self._log("delete-connectivity-check").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.connectivityCheck = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateDestroySelf(self):
        self._log("interface-destroy-self").debug2("%s: destroy interface", self.name)
        self.setConfigErrorStr("Interface '%s' cannot be deleted" % self.name)

        return ReturnCodes.kGeneralError

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        """the interface is being evaluated and verified for correctness"""

        self._log("prepare-private-value-set").debug4("%s: prepare data - %s", self.name, data)

        if self.blinkyInterface and self.blinkyInterface.isInTrigger() is False:

            # changing mib index after trigger is not premitted
            if self.mibIfIndex != data.mibIfIndex:
                self._log("mib-index-change").notice("mibIfIndex '%s' cannot be changed after trigger", data.mibIfIndex)
                self.setConfigErrorStr("mib-index '%s' modification is not premitted" % (data.mibIfIndex))
                return ReturnCodes.kGeneralError

        delayMin,delayMax = 0,10
        deliveryStabilityDelay = data.configurationDelay
        if deliveryStabilityDelay < delayMin or deliveryStabilityDelay > delayMax:
            self._log("invalid-configuration-delay").notice("configurationDelay '%s' is invalid. must be in range (%s-%s) ",
                                                           deliveryStabilityDelay, delayMin, delayMax)
            self.setConfigErrorStr("configuration-delay '%s' is out of range %s-%s" % (deliveryStabilityDelay, delayMin, delayMax))
            return ReturnCodes.kGeneralError

        # set data
        self.candidateEnabled = not data.shutdown  
        self.candidateTechMode = data.techMode 

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        """the interface changes are being aborted

            Raises:
                FATAL if fails
        """

        self._log("abort-private-value-set").debug4("%s: abort data - %s", self.name, data)

        self.candidateEnabled = self.runningEnabled 
        self.candidateTechMode = self.runningTechMode 

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        """the interface changes are being commited

            Raises:
                FATAL if fails
        """

        self._log("commit-private-value-set").debug4("%s: commit data - %s", self.name, data)

        self.runningEnabled = self.candidateEnabled 
        self.runningTechMode = self.candidateTechMode 
        self.mibIfIndex = data.mibIfIndex
        self.shouldSendGratuitousArp = data.sendGratuitousArp
        self.deliveryStabilityDelay = data.configurationDelay       

        # mute reporting was changed
        if self.muteReporting != data.muteReporting:
            self.muteReporting = data.muteReporting

            if self.connectivityCheck:
                self.connectivityCheck.setMuteReporting(self.muteReporting)

            self._log("interface-mute-reporting").notice("interface %s mute reporting was changed to %s", self.name, data.muteReporting)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _wasOkOrCrash(self, rc, msg):
        if not a.sys.net.lnx.common.Command.isReturnOk(rc):
            a.infra.process.processFatal("%s: %s", self.name, msg)

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateAfter(self):
        """the interface is being evaluated and verified for correctness"""

        self._log("prepare-private-after").debug4("%s: interface preparePrivateAfter was called", self.name)

        numServices = 0

        # managemnet
        if self.isManagementEnabled():
            numServices+=1

            if self.prepareManagement() != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        # line
        if self.isLineEnabled():
            numServices+=1

            if self.prepareLine() != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        # delivery
        if self.isDeliveryEnabled():
            numServices+=1

            if self.prepareDelivery() != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        if numServices > 1:
            self._log("too-many-functions").notice("Unsupported combination of functions for interface '%s'", self.name)
            self.setConfigErrorStr("content and management combination is not supported")
            return ReturnCodes.kGeneralError

        # in line after DPDK is up the eth device not exposed by Linux kernel
        if numServices==1 and not self.isLineEnabled():
            deviceName = self.deviceName()
            if ((deviceName is None) or (a.sys.net.lnx.device.DeviceUtils.isDeviceExists(deviceName) is False)):
                    self._log("os-device-no-exist").notice("Interface '%s' associated os device '%s' is invalid", self.name, deviceName)
                    self.setConfigErrorStr("Interface '%s': associated OS device '%s' is invalid" % (self.name, deviceName))
                    return ReturnCodes.kGeneralError

        # static configuration on mini platform
        if not self.allowDynamicConfig:
            if self.prepareForStaticCfg() != ReturnCodes.kOk:
                return ReturnCodes.kGeneralError

        # on success only
        if self.isDeliveryEnabled():
            self.tableid = (Interface.DELIVERY_TABLE_ID_PATTERN % self.ifIndex)
        elif ((self.isManagementEnabled()) and (self.candidateTechMode is False)):
            self.tableid = Interface.MANAGEMENT_TABLE_ID
        else:
            self.tableid = None

        self.isTrxStart = True
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def prepareForStaticCfg(self):
        return (self.__prepareForStaticCfg(IpVersion.kIPv4) and self.__prepareForStaticCfg(IpVersion.kIPv6))

#-----------------------------------------------------------------------------------------------------------------------
    def __prepareForStaticCfg(self, version):

        self._log("prepare-static-cfg").debug2("%s: interface prepare on static ipv%s configuration", self.name, version)

        deviceName = self.deviceName()
        if deviceName and (a.sys.net.lnx.device.DeviceUtils.isDeviceExists(deviceName)):

            if self.hasAddress(version) is True:
                candidateAddress = self.getIpNetwork(version)
                self._log("cnadidate-addr").debug2("Candidate IPv%s Address is: %s", version, candidateAddress)

                address = a.sys.net.lnx.device.DeviceUtils.getIpAddress(self._log, deviceName, version)
                self._log("running-addr").debug2("Running IP%s Address is: %s", version, address)

                runningAddress = None
                if address is not None:
                    try:
                        runningAddress = a.infra.net.ip_network.IpNetwork(address, version)
                    except ValueError as ex:
                        self._log("running-addr-invalid").notice("Runnigng IPv%s Address '%s' is invalid: %s", version,  address, ex)
                        self.setConfigErrorStr("ipv%s address %s is invalid" % (version, address))
                        return ReturnCodes.kGeneralError
    
                if candidateAddress != runningAddress:
                    self._log("candidate-addr-invalid").notice("Candidate IPv%s Address must be: %s or localhost", version, runningAddress)
                    self.setConfigErrorStr("in this platform, ipv%s address must be: %s" % (version, runningAddress))
                    return ReturnCodes.kGeneralError

        if self.hasDefaultGateway(version) is True:
            candidateDG = self.getDefaultGateway(version)
            self._log("candidate-dg").debug2("Candidate IPv%s Default Gateway is: %s", version, candidateDG)

            dg = a.sys.net.lnx.route.RoutingUtils.getDefaultGateway(self._log, 
                                                                    a.sys.net.lnx.route.RoutingUtils.MAIN_TABLE_NAME, 
                                                                    version)
            self._log("running-dg").debug2("Running IPv%s Default Gateway is: %s", version, dg)

            runningDG = None
            if dg is not None:
                try:
                    runningDG = a.infra.net.ip_address.IpAddress(dg, version)
                except ValueError as ex:
                    self._log("running-gw-invalid").notice("Running IPv%s Gateway '%s' is invalid: %s", version, dg, ex)
                    self.setConfigErrorStr("ipv%s default gateway %s is invalid" % (version, dg))
                    return ReturnCodes.kGeneralError
    
            if candidateDG != runningDG:
                self._log("candidate-gw-invalid").notice("Candidate IPv%s Gateway must be: %s", version, runningDG)
                self.setConfigErrorStr("in this platform, ipv%s default gateway must be: %s" % (version, runningDG))
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def prepareManagement(self):

        self._log("prepare-management").debug2("%s: interface prepare on Management", self.name)

        # management supported interface does not support ipv6
        if self.hasAddress(IpVersion.kIPv6) is True:
            self._log("mng-no-ipv6-addr").notice("Cannot set an ipv6 address to the management interface '%s'", self.name)
            self.setConfigErrorStr("Interface '%s': management interface cannot have an ipv6 address" % self.name)
            return ReturnCodes.kGeneralError

        if self.hasDefaultGateway(IpVersion.kIPv6) is True:
            self._log("mng-no-ipv6-dg").notice("Cannot set an ipv6 default gateway to the management interface '%s'", self.name)
            self.setConfigErrorStr("Interface '%s': management interface cannot have an ipv6 default gateway" % self.name)
            return ReturnCodes.kGeneralError

        if self.candidateTechMode is True:

            self._log("prepare-tech").debug3("%s: interface prepare in Tech mode", self.name)

            # tech supported interface cannot be deactivated
            if self.candidateEnabled is False:
                self._log("tech-deactivate").notice("Cannot deactivate the managment interface '%s' in tech mode", self.name)
                self.setConfigErrorStr("Interface '%s': cannot be shutdown in tech mode" % self.name)
                return ReturnCodes.kGeneralError

            # tech supported interface has no ipv4 default gateway
            if self.hasDefaultGateway(IpVersion.kIPv4) is True:
                self._log("tech-no-default-gw").notice("Cannot set a default gateway to the managment interface '%s' in tech mode", self.name)
                self.setConfigErrorStr("Interface '%s': cannot set default gateway in tech mode" % self.name)
                return ReturnCodes.kGeneralError

            address = self.getIpNetwork(IpVersion.kIPv4)
            if Interface.TECH_IPV4_ADDRESS != address:
                self._log("tech-fixed-ip").notice("Managment interface '%s' in tech mode is locked to %s", self.name, Interface.TECH_IPV4_ADDRESS)
                self.setConfigErrorStr("Interface '%s': cannot change ip address in tech mode" % self.name)
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def prepareDelivery(self):

        self._log("prepare-delivery").debug2("%s: interface prepare on Delivery", self.name)

        if self.candidateTechMode is True:
            self._log("delivery-no-tech").notice("Delivery interface '%s' does not support tech mode", self.name)
            self.setConfigErrorStr("Interface '%s': does not support tech mode" % self.name)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def prepareLine(self):

        self._log("prepare-line").debug2("%s: interface prepare on Line", self.name)

        if self.candidateTechMode is True:
            self._log("line-no-tech").error("Line interface '%s' does not support tech mode", self.name)
            self.setConfigErrorStr("Interface '%s': does not support tech mode" % self.name)
            return ReturnCodes.kGeneralError

        # analytics/acquisition supported interface has no ip address (rx only)
        if self.hasAddress(IpVersion.kIPv4) is True or self.hasAddress(IpVersion.kIPv6) is True:
            self._log("line-no-ip-addr").error("Cannot set an ip address to the interface '%s' supporting analytics/acquisition", self.name)
            self.setConfigErrorStr("Interface '%s': analytics/acquisition supported interface cannot have an ip address" % self.name)
            return ReturnCodes.kGeneralError

        # analytics/acquisition supported interface has no default gateway
        if self.hasDefaultGateway(IpVersion.kIPv4) is True or self.hasDefaultGateway(IpVersion.kIPv6) is True:
            self._log("line-no-default-gw").error("Cannot set a default gateway to the interface '%s' supporting analytics/acquisition", self.name)
            self.setConfigErrorStr("Interface '%s': analytics/acquisition supported interface cannot have a default gateway" % self.name)
            return ReturnCodes.kGeneralError
                                            
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitNameAndState(self):

        deviceName = self.deviceName()

        # set driver type
        self._setDriverType(deviceName)

        if self.isLineEnabled():
            return
    
        if a.sys.net.lnx.device.DeviceUtils.isDeviceExists(deviceName) is True:
    
            if self.device.shouldRename() is True:
            
                # device must be down before renaming
                self._log("deactivate-device-pre-rename").debug2("%s: device %s is down for renaming", self.name, deviceName)
                rc = a.sys.net.lnx.device.IpLink.deactivateDevice(self._log, deviceName)
                self._wasOkOrCrash(rc, "Interface commit action failed on deacivate device")
                self.runningEnabled = False
    
                # rename device
                timeoutGuard = TimeoutGuard(self._log, '%s-device-rename' % (self.name), Interface.DEFAULT_TIMEOUT_MILI_SEC) 
                self.device.rename()
                timeoutGuard.checkAndLog(self.device.rename)

                deviceName = self.deviceName()
   
                if not a.sys.net.lnx.common.Command.isReturnOk(rc):
                    a.infra.process.processFatal("%s: Device commit action failed", self.name)
    
            self._log("device-state").debug3("%s: device %s - enabled=%s, actualEnabled=%s", 
                                             self.name, deviceName, self.candidateEnabled, self.runningEnabled)

            # if device state should change
            # Note: device might be down because of the rename
            if self.candidateEnabled != self.runningEnabled: 

                if self.candidateEnabled:

                    # must reset procs prior to activating the device
                    # Note: only for ipv6 @ temp for 2.7.0 - 21/1/2013
                    if not self.ipv6 is None:
                        self._writeSysNetProcs() 

                    self._log("activate-device").debug2("%s: device %s is up", self.name, deviceName)

                    # capture counters before clear by os (if needed)
                    shouldReadCounters = (self.isFirstTrx is False and self._isCountersClearPostUp())
                    if shouldReadCounters is True:
                        self._updateCountersPreClear("pre-activate")

                    timeoutGuard = TimeoutGuard(self._log, '%s-activate-device' % (self.name), Interface.MAX_TIMEOUT_MILI_SEC) 
                    rc = a.sys.net.lnx.device.IpLink.activateDevice(self._log, deviceName) 
                    timeoutGuard.checkAndLog(a.sys.net.lnx.device.IpLink.activateDevice)

                    self._wasOkOrCrash(rc, "Interface commit action failed on acivate device")

                    # send gratuitous arp on admin enable
                    if self.device and self.shouldSendGratuitousArp:
                        self.device.sendGratuitousArp("admin enable")
                else:
                    self._log("deactivate-device").debug2("%s: device %s is down", self.name, deviceName)

                    # capture counters before clear by os (if needed)
                    shouldReadCounters = (self.isFirstTrx is False and self._isCountersClearPostDown())
                    if shouldReadCounters is True:
                        self._updateCountersPreClear("pre-deactivate")

                    rc = a.sys.net.lnx.device.IpLink.deactivateDevice(self._log, deviceName)
                    self._wasOkOrCrash(rc, "Interface commit action failed on deacivate device")
    
                self.runningEnabled = self.candidateEnabled  
        else:
            self._log("device-not-exist-state").notice("%s: device %s does not exist", self.name, deviceName)

#-----------------------------------------------------------------------------------------------------------------------
    def commitDynamicCfg(self, adminStateChange):

        if self.isLineEnabled():
            return

        deviceName = self.deviceName()

        if a.sys.net.lnx.device.DeviceUtils.isDeviceExists(deviceName) is True:

            if not self.ipv4 is None:
                self.__commitIpCfg(deviceName, self.ipv4, self.ipv4CacheData, adminStateChange)

            if not self.ipv6 is None:
                self.__commitIpCfg(deviceName, self.ipv6, self.ipv6CacheData, adminStateChange)

        else:
            self._log("device-not-exist-addr").notice("%s: device %s does not exist", self.name, deviceName)

#-----------------------------------------------------------------------------------------------------------------------
    def __commitIpCfg(self, deviceName, ipContainer, cacheData, adminStateChange):

        timeoutGuard = TimeoutGuard(self._log, '%s-ipv%s-commit-ip-addr' % (self.name, ipContainer.version), Interface.DEFAULT_TIMEOUT_MILI_SEC) 
        self.__commitIpAddress(deviceName, ipContainer, cacheData, adminStateChange)
        timeoutGuard.checkAndLog(self.__commitIpAddress)

        timeoutGuard = TimeoutGuard(self._log, '%s-ipv%s-commit-ip-route' % (self.name, ipContainer.version), Interface.DEFAULT_TIMEOUT_MILI_SEC)
        self.__commitIpDefaultGateway(deviceName, ipContainer, cacheData, adminStateChange)
        timeoutGuard.checkAndLog(self.__commitIpDefaultGateway)

        timeoutGuard = TimeoutGuard(self._log, '%s-ipv%s-commit-ip-rule' % (self.name, ipContainer.version), Interface.DEFAULT_TIMEOUT_MILI_SEC)
        self.__commitIpRule(deviceName, ipContainer, cacheData, adminStateChange)
        timeoutGuard.checkAndLog(self.__commitIpRule)

#-----------------------------------------------------------------------------------------------------------------------
    def __commitIpAddress(self, deviceName, ipContainer, cacheData, adminStateChange):
        __pychecker__="no-argsused"  # cacheData not used

        address = ""
        if self.hasAddress(ipContainer.version) is True:
            address = self.getIpNetwork(ipContainer.version)
            self._log("add-addr").debug2("%s: device %s add IPv%s address %s", 
                                         self.name, deviceName, ipContainer.version, address)

            if cacheData.ipAddress == str(address) and adminStateChange is False:
                self._log("add-addr-no-change").debug3("%s: no change for device %s adding IPv%s address %s", 
                                                       self.name, deviceName, ipContainer.version, address)
                return # no change

        # removing all IP address information from a device
        self._log("flush-addr").debug2("%s: device %s flush all IPv%s addresses", 
                                       self.name, deviceName, ipContainer.version)

        rc = a.sys.net.lnx.device.IpAddress.flushAddresses(self._log, deviceName, scope="global", version=ipContainer.version)
        self._wasOkOrCrash(rc, "Interface commit action failed on flush addresses") 
               
        if address:

            # adding IP address to a device
            rc = a.sys.net.lnx.device.IpAddress.addAddress(self._log, str(address), deviceName, ipContainer.version)
            self._wasOkOrCrash(rc, "Interface commit action failed on add address")

            # send gratuitous arp on ip change
            if self.device and self.shouldSendGratuitousArp:
                self.device.sendGratuitousArp("ip change")

            if (self.tableid is not None) and (not a.sys.net.lnx.route.RoutingUtils.isTableMain(self.tableid)):

                if self.runningEnabled is True:
                            destination = "%s/%s" % (address.network, address.prefixlen)
                            source = str(address.ip)
                            scope = "link"
        
                            # 2 IPv6 addresses are allocated per each interface:
                            # (1) local  (fe80::/10) 
                            # (2) global (2000::/3) 
                            if ipContainer.version == 6:
                                source = None
                                scope  = None

                            # Note: (1) device must be up
                            #       (2) the main table is populated automatically by the kernel when 
                            #           new interfaces are brought up with IP addresses

                            # in order to support management and delivery under the same subnet
                            # remove auto created route scope link and readd it with a lower priority metric in the main routing table
                            rc = a.sys.net.lnx.route.IpRoute.flushRoutes(self._log, table=Interface.MANAGEMENT_TABLE_ID, 
                                                                         device=deviceName, version=ipContainer.version, 
                                                                         scope=scope, proto="kernel")
                            self._wasOkOrCrash(rc, "Interface commit action failed on flush routes at table %s" % Interface.MANAGEMENT_TABLE_ID) 

                            rc = a.sys.net.lnx.route.IpRoute.replaceRoute(self._log, destination, table=Interface.MANAGEMENT_TABLE_ID, 
                                                                          device=deviceName, version=ipContainer.version, 
                                                                          scope=scope, metric=1000, src=source)
                            self._wasOkOrCrash(rc, "Interface commit action failed on replace route at table %s" % Interface.MANAGEMENT_TABLE_ID)

                            rc = a.sys.net.lnx.route.IpRoute.flushRoutes(self._log, table=self.tableid,
                                                                         device=deviceName, version=ipContainer.version, 
                                                                         scope=scope)
                            self._wasOkOrCrash(rc, "Interface commit action failed on flush routes at table %s" % self.tableid) 

                            # add a default route scope link, for network that is valid and reachable through this device
                            # e.g. ip route add 172.240.0.0/16 dev eth-tg0 table 100 scope link src 172.240.0.1
                            rc = a.sys.net.lnx.route.IpRoute.replaceRoute(self._log, destination, table=self.tableid, 
                                                                          device=deviceName, version=ipContainer.version, 
                                                                          scope=scope, src=source)
                            self._wasOkOrCrash(rc, "Interface commit action failed on replace route at table %s" % self.tableid)  

#-----------------------------------------------------------------------------------------------------------------------
    def __commitIpDefaultGateway(self, deviceName, ipContainer, cacheData, adminStateChange):
        __pychecker__="no-argsused"  # cacheData not used

        defaultGateway = ""
        if self.hasDefaultGateway(ipContainer.version) is True:

            defaultGateway = self.getDefaultGateway(ipContainer.version)
            self._log("add-dg").debug2("%s: add default gateway %s at table %s device %s", 
                                       self.name, defaultGateway, self.tableid, deviceName)

            if cacheData.defaultGateway == str(defaultGateway) and adminStateChange is False:
                self._log("add-dg-no-change").debug3("%s: no change for adding default gateway %s at table %s device %s", 
                                                     self.name, defaultGateway, self.tableid, deviceName)
                return # no change

        if self.tableid:

            # flush default gateway (if exsits)
            a.sys.net.lnx.route.IpRoute.flushDefaultRoute(self._log, self.tableid, ipContainer.version)           

        if defaultGateway:

            if self.runningEnabled is True:
                # adding default gateway route
                # Note: device must be up
                rc = a.sys.net.lnx.route.IpRoute.addDefaultRoute(self._log, str(defaultGateway), self.tableid, 
                                                                 deviceName, ipContainer.version) 
                self._wasOkOrCrash(rc, "Interface commit action failed on add default gateway")
        
#-----------------------------------------------------------------------------------------------------------------------
    def __commitIpRule(self, deviceName, ipContainer, cacheData, adminStateChange):
        __pychecker__="no-argsused"  # cacheData not used

        if self.hasDefaultGateway(ipContainer.version) is True:
            if not a.sys.net.lnx.route.RoutingUtils.isTableMain(self.tableid):
    
                # inserts a new rule for updating routing policy (if not main table)
                # for source base routing
    
                if a.sys.net.lnx.route.RoutingUtils.hasMatchingRule(self._log, self.tableid, ipContainer.version):
    
                    self._log("flush-rules").debug2("%s: flush all rules at table %s", 
                                           self.name, self.tableid)
    
                    rc = a.sys.net.lnx.route.IpRule.flushRules(self._log, self.tableid, ipContainer.version)
                    self._wasOkOrCrash(rc, "Interface commit action failed on flush rules")
    
                if self.runningEnabled is True:
                    address = self.getIpAddress(ipContainer.version)
    
                    self._log("add-rule").debug2("%s: add source base rule %s at table %s",
                                                 self.name, address, self.tableid)
    
                    if not address is None:
                        # Note: device must be up
                        rc = a.sys.net.lnx.route.IpRule.addRule(self._log, str(address), self.tableid, ipContainer.version)
                        self._wasOkOrCrash(rc, "Interface commit action failed on add rule")

#-----------------------------------------------------------------------------------------------------------------------
    def _writeSysNetProcs(self):

        deviceName = self.deviceName()
        
        if a.sys.net.lnx.device.DeviceUtils.isDeviceExists(deviceName) is True:
            self._log("write-proc-sys-net").debug1("%s: writing to /proc/sys/net/ - '%s'", self.name, self.ourSysNetProcs)

            for proc in self.ourSysNetProcs:
                value = self.ourSysNetProcs[proc]
                target = proc % deviceName

                # write value to /proc/sys/net/...
                self._writeValueToTarget(target,value)

#-----------------------------------------------------------------------------------------------------------------------
    def _readTargetCurrentValue(self, target):

        try:
            fd = open(target, "r")
            value = fd.read().strip()
            self._log("read-from-file").debug1("%s: read from file '%s', the value '%s'", self.name, target, value)
            fd.close()
        except IOError as (errno, strerror):            
            self._log("failed-read-from-file").exception("%s: Failed to read from file %s: I/O error(%d): {%s}", self.name, 
                                                         target, errno, strerror)
            return (ReturnCodes.kGeneralError, None)

        self._log("read-from-file").notice("%s: reading from file '%s', the value '%s'", self.name, target, value)
        
        return (ReturnCodes.kOk, value)

#-----------------------------------------------------------------------------------------------------------------------
    def _writeValueToTarget(self, target, value):
        self._log("write-to-file").notice("%s: writing to file '%s', the value '%s'", self.name, target, value)

        try:
            fd = open(target, "w")
            strToWrite = str(value)+"\n"
            fd.write(strToWrite)            
            fd.close()
        except IOError as (errno, strerror):            
            self._log("failed-write-to-file").exception("%s: Failed to write to file %s: I/O error(%d): {%s}", self.name, 
                                                        target, errno, strerror)
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk
                                                      
#-----------------------------------------------------------------------------------------------------------------------
    def updateCfgCache(self):

        if not self.ipv4 is None:
            self.__updateIpCache(self.ipv4, self.ipv4CacheData)

        if not self.ipv6 is None:
            self.__updateIpCache(self.ipv6, self.ipv6CacheData)

#-----------------------------------------------------------------------------------------------------------------------
    def __updateIpCache(self, ipContainer, cacheData):

        defaultGateway = ""
        if self.hasDefaultGateway(ipContainer.version) is True:
            defaultGateway = self.getDefaultGateway(ipContainer.version)

        address = ""
        if self.hasAddress(ipContainer.version) is True:
            address = self.getIpNetwork(ipContainer.version)
           
        newData = IpData()
        newData.defaultGateway = str(defaultGateway)
        newData.ipAddress = str(address)

        cacheData.queue.put_nowait(newData)
        self._log("queue-put-data").info("%s: add new config to queue ipv%s address '%s' and default-gateway '%s'", 
                                         self.name, ipContainer.version, newData.ipAddress, newData.defaultGateway)

#-----------------------------------------------------------------------------------------------------------------------
    def _updateCountersPreClear(self, desc):
        counters = CountersOperData()
        rc = self.getIfCounters(None, counters, isRateCounters=False, shouldSetExtCounters=True)
    
        if rc == ReturnCodes.kOk:
            self._log("interface-counters-os-clear-update").info("%s: update rx and tx counters before os clear (%s) - %s", 
                                                                     self.name, desc, counters.debugStr())
    
            # updates counters before OS clear
            self.countersFromLastOsClear.inPackets          = counters.inPackets
            self.countersFromLastOsClear.outPackets         = counters.outPackets
            self.countersFromLastOsClear.inOctets           = counters.inOctets
            self.countersFromLastOsClear.outOctets          = counters.outOctets
            self.countersFromLastOsClear.inErrorPackets     = counters.inErrorPackets
            self.countersFromLastOsClear.outErrorPackets    = counters.outErrorPackets
            self.countersFromLastOsClear.inDiscardPackets   = counters.inDiscardPackets
            self.countersFromLastOsClear.outDiscardPackets  = counters.outDiscardPackets
            self.countersFromLastOsClear.inBroadcastPackets = counters.inBroadcastPackets
            self.countersFromLastOsClear.outBroadcastPackets= counters.outBroadcastPackets
            self.countersFromLastOsClear.inMulticastPackets = counters.inMulticastPackets
            self.countersFromLastOsClear.outMulticastPackets= counters.outMulticastPackets
            self.countersFromLastOsClear.inUnicastPackets   = counters.inUnicastPackets
            self.countersFromLastOsClear.outUnicastPackets  = counters.outUnicastPackets

        else:
            self._log("interface-counters-pre-activate-fail").error("%s: failed retrieve rx and tx counters (%s)", self.name, desc)

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateBefore(self):
        """the interface changes are being committed

            Raises:
                FATAL if fails
        """

        self._log("commit-private-before").debug4("%s: interface commitPrivateBefore was called", self.name)

        if self.allowDynamicConfig:
            if self.isTrxStart is True:

                adminStateChange = (self.candidateEnabled != self.runningEnabled)

                # rename device and change state up/down
                # Note: must be before addRule() is called
                #timeoutGuard = TimeoutGuard(self._log, '%s-commit-name-and-state' % (self.name), Interface.MAX_TIMEOUT_MILI_SEC) 
                self.commitNameAndState()
                #timeoutGuard.checkAndLog(self.commitNameAndState)
        
                # ip address, route and rule
                self.commitDynamicCfg(adminStateChange)

        self.updateCfgCache()

        if self.isFirstTrx is True:

            shouldClearCounters= self._isCountersClearPostUp() is False and self._isCountersClearPostDown() is False
            if shouldClearCounters is True:
                # interface counters start as non-zeros
                # first transaction commit
                rc = self._doClearCounters()
                self.countersOnStart.copyDataFrom(self.countersOnClear) # copy counters snapshot
            
                if rc != ReturnCodes.kOk:
                    self._log("interface-counters-on-start-fail").error("%s: failed retrieve rx and tx counters on start", 
                                                                         self.name)
            self.isFirstTrx = False

        self.isTrxStart = False
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def launchTasksThread(self):
        self._log("interface-launch-tasks-thread").debug1("%s: launchTasksThread() was called.", self.name)

        if self.isFirstTrx is True:
            a.infra.process.processFatal("%s: launchTasksThread() was called before the first transaction", self.name)

        if self.thread is None and self.isActiveModule is True:
            
            # dedicated thread in charge of periodic connectivity checks
            # note: ping/arp can have a timeout up to 60 secs
            self.thread = TasksThread(self._log, self.name)
            self.thread.addTask(self.actionOnConnectivityCheck, self.CONNECTIVITY_CHECK_INTERVAL_RATE_SEC)
            self.thread.start()

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateBefore(self):
        """the interface changes are being aborted

            Raises:
                FATAL if fails
        """
        
        self._log("abort-private-before").debug4("%s: interface abortPrivateBefore was called", self.name)

        self.isTrxStart = False
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getMacAddress(self):

        mac = None

        if self.isLineEnabled():
            # line interface
            data = self.getLineNicData()

            if data is not None:
                mac = data.get(LineNicStats.KEY_LINE_MAC,None)
        else:
            # management/delivery interface
            deviceName = self.deviceName()
            if a.sys.net.lnx.device.DeviceUtils.isDeviceExists(deviceName) is True:
                mac = a.sys.net.lnx.device.DeviceUtils.getMacAddress(self.name, self._log, deviceName)

        return mac       

#-----------------------------------------------------------------------------------------------------------------------
    def getDriverType(self, isVolatileRead=False):

        if isVolatileRead is True:
            deviceName = self.deviceName()
    
            # set driver type
            self._setDriverType(deviceName)

        return self.driverType

#-----------------------------------------------------------------------------------------------------------------------
    def _setDriverType(self, deviceName):

        if self.isLineEnabled():
            # line interface
            data = self.getLineNicData()

            if data is not None:
                self.driverType = data.get(LineNicStats.KEY_LINE_TYPE,None)
            else:
                self.driverType = None
        else:
            # management/delivery interface
            if a.sys.net.lnx.device.DeviceUtils.isDeviceExists(deviceName) is True:
                self.driverType = "os"
            else:
                self.driverType = None

#-----------------------------------------------------------------------------------------------------------------------
    def isLinkUp(self):

        self._log("interface-link-up").debug3("%s: is link up was called.", self.name)

        isLinkUp = None

        if self.isLineEnabled():
            data = self.getLineNicData()

            if data is not None:
                # line link  status
                isLinkUp = data.get(LineNicStats.KEY_LINE_UP, None)
        else:
            deviceName = self.deviceName()

            if a.sys.net.lnx.device.DeviceUtils.isDeviceExists(deviceName) is True:
    
                # os link status
                operStatusStr = a.sys.net.lnx.device.DeviceUtils.getOperState(deviceName, self._log, deviceName) 
                          
                if "up" == operStatusStr:
                    isLinkUp = True
                elif "down" == operStatusStr:
                    isLinkUp = False

        return isLinkUp

#-----------------------------------------------------------------------------------------------------------------------
    def getLineNicData(self):

        data = None
        if self.device is not None:
            data = self.device.getLineNicData()

        return data

#-----------------------------------------------------------------------------------------------------------------------
    def getLineCounters(self, operData, shouldSetExtCounters):

        self._log("interface-line-counters").debug4("%s: get line counters was called", self.name)

        data = self.getLineNicData()

        if data is not None:
            counters = data[LineNicStats.KEY_LINE_COUNTERS]

            # rx/tx packets, bytes, errors, discards
            operData.setInPackets(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_PACKETS,0))
            operData.setOutPackets(counters.get(LineNicStats.KEY_LINE_COUNTERS_TX_PACKETS,0))
            operData.setInOctets(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_BYTES,0))
            operData.setOutOctets(counters.get(LineNicStats.KEY_LINE_COUNTERS_TX_BYTES,0))
            operData.setInErrorPackets(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_ERRORS,0))
            operData.setOutErrorPackets(counters.get(LineNicStats.KEY_LINE_COUNTERS_TX_ERRORS,0))
            operData.setInDiscardPackets(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_DROPS,0))
            operData.setOutDiscardPackets(0)

            if shouldSetExtCounters is True:
                # rx bcast, mcast, ucast packets
                operData.setInBroadcastPackets(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_BCASTS,0))
                operData.setInMulticastPackets(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_MCASTS,0))

                rxUcastPackets = operData.inPackets - operData.inBroadcastPackets - operData.inMulticastPackets
                operData.setInUnicastPackets(max(0,rxUcastPackets))

                # tx bcast, mcast, ucast packets - always 0
                operData.setOutBroadcastPackets(0)
                operData.setOutMulticastPackets(0)
                operData.setOutUnicastPackets(0)
    
                # other
                operData.setInUnknownProtocolPackets(0) # always 0

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _handleEthToolCounters(self, operData, deviceName):

        counterToSetDict = {}

        if self.isDeliveryEnabled():
            # TenGigE
            counterToSetDict = Interface.ourTenGigEthCounterToSetDict
        else:
            # GigabitEthernet
            counterToSetDict = Interface.ourGigEthCounterToSetDict

        rc = a.sys.net.lnx.device.EthTool.showEthStatistics(self._log, deviceName)   
        if not a.sys.net.lnx.common.Command.isReturnOk(rc):
            return

        output = rc[1].splitlines()

        # set ethtool counters
        for line in output[1:]:

            (key, value) = line.split(":",1)
            key = key.strip()
            value = value.strip()
      
            setFunctorAttr = counterToSetDict.get(key,None) 

            if setFunctorAttr is not None and value.isdigit():
                intValue = int(value)

                if hasattr(operData, setFunctorAttr):
                    setFunctor = getattr(operData, setFunctorAttr)
                    setFunctor(intValue)
                    self._log("interface-set-ethtool-counter").debug4("%s: set field - %s=%s (functor=%s)", 
                                                                      self.name, key, intValue, setFunctorAttr)
                else:
                    self._log("interface-set-ethtool-counter-error").error("%s: set field failure - %s=%s (functor=%s)", 
                                                                      self.name, key, intValue, setFunctorAttr)


#-----------------------------------------------------------------------------------------------------------------------
    def getOsCounters(self, operData, shouldSetExtCounters):

        self._log("interface-os-counters").debug4("%s: get os counters was called", self.name)

        deviceName = self.deviceName()

        if a.sys.net.lnx.device.DeviceUtils.isDeviceExists(deviceName) is True:
                    
            statsContainer = a.sys.net.lnx.device.DeviceUtils.getStatistics(self.name, self._log, deviceName)

            if statsContainer is not None:
                self._log("interface-os-counters-get").debug4("%s: %s", self.name, statsContainer)

                # rx/tx packets, bytes, errors, discards
                operData.setInPackets(int(statsContainer.get(self.KEY_OS_RX_PACKETS,0)))
                operData.setOutPackets(int(statsContainer.get(self.KEY_OS_TX_PACKETS,0)))
                operData.setInOctets(int(statsContainer.get(self.KEY_OS_RX_BYTES,0)))
                operData.setOutOctets(int(statsContainer.get(self.KEY_OS_TX_BYTES,0)))
                operData.setInErrorPackets(int(statsContainer.get(self.KEY_OS_RX_ERRORS,0)))
                operData.setOutErrorPackets(int(statsContainer.get(self.KEY_OS_TX_ERRORS,0)))
                operData.setInDiscardPackets(int(statsContainer.get(self.KEY_OS_RX_DROPPED,0)))
                operData.setOutDiscardPackets(int(statsContainer.get(self.KEY_OS_TX_DROPPED,0)))

                if shouldSetExtCounters is True:
    
                    self._handleEthToolCounters(operData, deviceName)

                    # rx ucast packets (if needed)
                    if not operData.hasInUnicastPackets():
                        rxUcastPackets = operData.inPackets - operData.inBroadcastPackets - operData.inMulticastPackets
                        operData.setInUnicastPackets(max(0,rxUcastPackets))

                    # tx ucast packets (if needed)
                    if not operData.hasOutUnicastPackets():
                        txUcastPackets = operData.outPackets - operData.outBroadcastPackets - operData.outMulticastPackets
                        operData.setOutUnicastPackets(max(0,txUcastPackets))

                    if self.isDeliveryEnabled():

                        # tx bcast and mcast packets - not supported for delivery interfaces (1/3/2013)
                        operData.setOutBroadcastPackets(0)
                        operData.setOutMulticastPackets(0)
    
                    # other
                    operData.setInUnknownProtocolPackets(0) # always 0

                if self.device:
                    operData.setOutGratuitousArpPackets(self.device.sentGratuitousArpCount)

                if self.link:
                    operData.setOperationalStatusChanges(self.link.linkStatusChangeCount)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getLineStatus(self, operData):
        
        self._log("interface-line-status").debug4("%s: get line status was called", self.name)   
        
        data = self.getLineNicData()

        if data is not None:

            # speed
            speed = data.get(LineNicStats.KEY_LINE_SPEED, None)
            if speed is not None:
                operData.setSpeedMegabit(speed) # Mb/s

            # mtu
            operData.setMtu(1500)

        # promiscuous on
        operData.setPromiscuous(Truthvalue.kTrue)

        return ReturnCodes.kOk 

#-----------------------------------------------------------------------------------------------------------------------
    def getOsStatus(self, operData):
        
        self._log("interface-os-status").debug4("%s: get os status was called", self.name)    

        deviceName = self.deviceName()

        if a.sys.net.lnx.device.DeviceUtils.isDeviceExists(deviceName) is True:

            # speed
            speed = a.sys.net.lnx.device.DeviceUtils.getSpeed(self._log, deviceName)
            if speed is not None:
                operData.setSpeedMegabit(speed) # Mb/s

            # mtu
            mtu = a.sys.net.lnx.device.DeviceUtils.getMtu(self.name, self._log, deviceName)
            if mtu is not None:
                operData.setMtu(mtu)

        # promiscuous off
        operData.setPromiscuous(Truthvalue.kFalse)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperStatusObj (self):
        blinkyOper = BlinkyOperIfStatus(self._log)
        blinkyOper.setFunctorTimeout(blinkyOper.GET_OBJ_FUNCTOR, Interface.OPER_TIMEOUT_MILI_SEC)
        return blinkyOper

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperCountersObj (self):
        blinkyOper = BlinkyOperIfCounters(self._log)
        blinkyOper.setFunctorTimeout(blinkyOper.GET_OBJ_FUNCTOR, Interface.OPER_TIMEOUT_MILI_SEC)
        return blinkyOper

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperAlarmsObj (self):
        blinkyOper = BlinkyOperIfAlarms(self._log)
        blinkyOper.setFunctorTimeout(blinkyOper.GET_OBJ_FUNCTOR, Interface.OPER_TIMEOUT_MILI_SEC)
        return blinkyOper

#-----------------------------------------------------------------------------------------------------------------------
    def getCounters(self, tctx, operData):
        self._log("get-counters").debug3("%s: get counters was called. tctx=%s", self.name, tctx)
        rc = self.getIfCounters(tctx, operData, isRateCounters=True, shouldSetExtCounters=True)

        self._log("interface-counters-original-data").debug4("%s: get original counters oper data=%s", self.name, operData.debugStr())
        
        # substract counters of last clear
        Interface._subtractFromCounters(operData, self.countersOnClear)

        self._log("interface-counters-data").info("%s: get counters results = %s (rc=%s)", self.name, operData, rc)

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def getContCounters64Bit(self, tctx, operData):

        self._log("get-cont-counters-64bit").debug3("%s: get continuous counters 64-bit was called. tctx=%s", self.name, tctx)
        rc = self.getIfCounters(tctx, operData, isRateCounters=True, shouldSetExtCounters=True)

        # substract counters of start
        Interface._subtractFromCounters(operData, self.countersOnStart)

        self._log("interface-cont-counters-64-bit-data").info("%s: get continuous counters 64-bit results = %s (rc=%s)", self.name, operData, rc)

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def getContCounters32Bit(self, tctx, operData):
        operData64Bit = CountersOperData()

        self._log("get-cont-counters-32bit").debug3("%s: get continuous counters 32-bit was called. tctx=%s", self.name, tctx)
        rc = self.getContCounters64Bit(tctx, operData64Bit)

        # should be modulo 32 of 64bit int value
        if operData64Bit.hasInOctets():
            operData.setInOctets(operData64Bit.inOctets % Interface.MAX_UINT_32BIT)
            
        if operData64Bit.hasOutOctets():
            operData.setOutOctets(operData64Bit.outOctets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasInErrorPackets():
            operData.setInErrorPackets(operData64Bit.inErrorPackets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasOutErrorPackets():
            operData.setOutErrorPackets(operData64Bit.outErrorPackets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasInDiscardPackets():
            operData.setInDiscardPackets(operData64Bit.inDiscardPackets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasOutDiscardPackets():
            operData.setOutDiscardPackets(operData64Bit.outDiscardPackets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasInBroadcastPackets():
            operData.setInBroadcastPackets(operData64Bit.inBroadcastPackets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasOutBroadcastPackets():
            operData.setOutBroadcastPackets(operData64Bit.outBroadcastPackets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasInMulticastPackets():
            operData.setInMulticastPackets(operData64Bit.inMulticastPackets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasOutMulticastPackets():
            operData.setOutMulticastPackets(operData64Bit.outMulticastPackets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasInErrorPackets():
            operData.setInUnicastPackets(operData64Bit.inUnicastPackets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasOutUnicastPackets():
            operData.setOutUnicastPackets(operData64Bit.outUnicastPackets % Interface.MAX_UINT_32BIT)

        if operData64Bit.hasInUnknownProtocolPackets():
            operData.setInUnknownProtocolPackets(operData64Bit.inUnknownProtocolPackets % Interface.MAX_UINT_32BIT)

        self._log("interface-cont-counters-32-bit-data").info("%s: get continuous counters 32-bit results = %s (rc=%s)", self.name, operData, rc)

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def setOperErrorStr(self, tctx, msg):
        if self.blinkyInterface and tctx:
            self.blinkyInterface.setTransError(tctx, msg)

#-----------------------------------------------------------------------------------------------------------------------
    def getIfCounters(self, tctx, operData, isRateCounters, shouldSetExtCounters):

        self._log("interface-counters").debug3("%s: get counters was called", self.name)

        # cache only if all flags are ON
        shouldCache = isRateCounters and shouldSetExtCounters

        # should read from cache only in this context
        if shouldCache is True: 
            timeDelta = time.time()-self.countersLastUpdateTime
            if timeDelta < 1: # less than 1 sec
                # read from cache
                operData.copyDataFrom(self.countersOperData)
                self._log("interface-counters-data-cache").debug3("%s: get counters oper data=%s", self.name, operData.debugStr())
                return ReturnCodes.kOk

        if self.isLineEnabled():
            rc = self.getLineCounters(operData, shouldSetExtCounters)
        else:
            rc = self.getOsCounters(operData, shouldSetExtCounters) 

        if rc != ReturnCodes.kOk:
            self._log("interface-get-counters-fail").debug3("%s: failed retrieve rx and tx counters", self.name)
            if tctx is not None: 
                self.setOperErrorStr(tctx, "cannot get interface %s counters information" % self.name)

            return ReturnCodes.kGeneralError

        # update counters in case of OS clear
        Interface._addToCounters(operData, self.countersFromLastOsClear)

        if isRateCounters is True:
            # reading an int counter is atomic @ thread-safe
            # Note: operations on shared variables of builtin data types (int, list, dict, etc) are atomic
            #       see: http://effbot.org/pyfaq/what-kinds-of-global-value-mutation-are-thread-safe.htm
            operData.setInPacketsRate(self.periodicCounters.rxPacketsPerSec)
            operData.setOutPacketsRate(self.periodicCounters.txPacketsPerSec)
            operData.setInBitsRate(self.periodicCounters.rxBitsPerSec)
            operData.setOutBitsRate(self.periodicCounters.txBitsPerSec)

        if shouldCache is True:
            # cache the counters
            self.countersLastUpdateTime = time.time()
            self.countersOperData.copyDataFrom(operData)

        self._log("interface-counters-data").debug3("%s: get counters oper data=%s", self.name, operData.debugStr())            
        return ReturnCodes.kOk
                
#-----------------------------------------------------------------------------------------------------------------------
    def getStatus(self, tctx, operData):

        self._log("interface-status").debug3("%s: get status was called. tctx=%s", self.name, tctx)

        timeDelta = time.time()-self.statusLastUpdateTime
        if timeDelta < 1: # less than 1 sec
            # read from cache
            operData.copyDataFrom(self.statusOperData)
            self._log("interface-status-data-cache").debug3("%s: get status oper data=%s", self.name, operData)
            return ReturnCodes.kOk

        if self.isLineEnabled():
            rc =  self.getLineStatus(operData)
        else:
            rc =  self.getOsStatus(operData)

        if rc != ReturnCodes.kOk:
            self._log("interface-get-status-fail").debug3("%s: failed retrieve status", self.name)
            self.setOperErrorStr(tctx, "cannot get interface %s status information" % self.name)
            return ReturnCodes.kGeneralError

        # common
        operData.setCounterDiscontinuityTicks(0) # always 0
        operData.setMibIanaType(Ianaiftype.kEthernetcsmacd) #  always ethernet
        operData.setConnectorPresent(Truthvalue.kTrue) # always true for physical interfaces
        operData.setInterfaceIndex(self.ifIndex)
        operData.setMibName(self.mibName)

        mibStatusToEnum = {True    : MibAdminStatusType.kUp,
                           False   : MibAdminStatusType.kDown}
        operData.setMibAdminStatus(mibStatusToEnum.get(self.runningEnabled,MibAdminStatusType.kDown))
        # operational status
        if self.link:
            isLinkUp = self.link.isLinkUp()
    
            statusToEnum = { True : OperationalStatusType.kUp, 
                             False: OperationalStatusType.kDown }
            operData.setOperationalStatus(statusToEnum.get(isLinkUp, 
                                                           OperationalStatusType.kUnknown))

        # speed 0 if oper-down
        if operData.operationalStatus == OperationalStatusType.kDown:
            operData.setSpeedMegabit(0)

        if operData.hasSpeedMegabit():
            speedbps = operData.speedMegabit*1000*1000 # convert Mb/s to b/s
            operData.setSpeed(speedbps)
            operData.setMibSpeed32Bit(min(speedbps,Interface.MAX_UINT_32BIT-1)) # maximum 2^32-1

        # cache the status
        self.statusLastUpdateTime = time.time()
        self.statusOperData.copyDataFrom(operData)

        self._log("interface-status-data").debug3("%s: get status oper data=%s", self.name, operData)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getAlarms(self, tctx, operData):

        self._log("interface-alarms").debug3("%s: get alarms was called. tctx=%s", self.name, tctx)

        timeDelta = time.time()-self.alarmsLastUpdateTime
        if timeDelta < 1: # less than 1 sec
            # read from cache
            operData.copyDataFrom(self.alarmsOperData)
            self._log("interface-alarms-data-cache").debug3("%s: get alarms oper data=%s", self.name, operData)
            return ReturnCodes.kOk


        if self.link:
            operStatus = self.link.isLinkUp()
            adminStatus = self.runningEnabled

            # link
            # oper-down and admin-up
            linkAlarm = ((operStatus is False) and (adminStatus is True))
            self._log("interface-alarm-link").debug1("%s: interface link alarm is %s (oper=%s, admin=%s)", 
                                                   self.name, linkAlarm, operStatus, adminStatus)

            operData.setInterfaceFailureAlarm(linkAlarm)
            operData.setInterfaceFailureReason(self.ourLinkAlarmReasons.get(linkAlarm,InterfaceFailureReasonType.kNone))

        if self.isDeliveryEnabled() is True:

            if self.connectivityCheck:

                isIpv4Available = self.connectivityCheck.isConnectivityAvailable(IpVersion.kIPv4)
                isIpv6Available = self.connectivityCheck.isConnectivityAvailable(IpVersion.kIPv6)

                ipv4ConnectivityReason = self.connectivityCheck.getConnectivityReason(IpVersion.kIPv4)
                ipv6ConnectivityReason = self.connectivityCheck.getConnectivityReason(IpVersion.kIPv6)
    
                # ipv4
                # no ipv4 connectivity due to oper-down or failed arp/ping
                ipv4ConnectivityAlarm = ((isIpv4Available is False) and (ipv4ConnectivityReason in self.ourIpv4AlarmReasons))
                self._log("interface-alarm-ipv4-conn").debug1("%s: ipv4 connectivity alarm is %s (status=%s, reason=%s)", 
                                                            self.name, ipv4ConnectivityAlarm, isIpv4Available, ipv4ConnectivityReason)

                operData.setInterfaceIpv4ConnectivityFailureAlarm(ipv4ConnectivityAlarm)
                operData.setInterfaceIpv4ConnectivityFailureReason(self.ourIpv4AlarmReasons.get(ipv4ConnectivityReason,
                                                                                                InterfaceIpv4ConnectivityFailureReasonType.kNone))

                # ipv6
                # no ipv6 connectivity due to oper-down or failed ndisc/ping
                ipv6ConnectivityAlarm = ((isIpv6Available is False) and (ipv6ConnectivityReason in self.ourIpv6AlarmReasons))
                self._log("interface-alarm-ipv6-conn").debug1("%s: ipv6 connectivity alarm is %s (status=%s, reason=%s)",
                                                            self.name, ipv6ConnectivityAlarm, isIpv6Available, ipv6ConnectivityReason)

                operData.setInterfaceIpv6ConnectivityFailureAlarm(ipv6ConnectivityAlarm)
                operData.setInterfaceIpv6ConnectivityFailureReason(self.ourIpv6AlarmReasons.get(ipv6ConnectivityReason,
                                                                                                InterfaceIpv6ConnectivityFailureReasonType.kNone))
        # mute alarms (if needed)
        if self.muteReporting is True:
            operData.setInterfaceFailureAlarm(False)
            operData.setInterfaceIpv4ConnectivityFailureAlarm(False)
            operData.setInterfaceIpv6ConnectivityFailureAlarm(False)

        # cache the alarm
        self.alarmsLastUpdateTime = time.time()
        self.alarmsOperData.copyDataFrom(operData)

        self._log("interface-alarm-data").debug3("%s: get alarm oper data=%s", self.name, operData)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __multilpyAndAddCounters(counters, other, multiplier):
        counters.inPackets          += (multiplier*other.inPackets)
        counters.outPackets         += (multiplier*other.outPackets)
        counters.inOctets           += (multiplier*other.inOctets)
        counters.outOctets          += (multiplier*other.outOctets)
        counters.inErrorPackets     += (multiplier*other.inErrorPackets)
        counters.outErrorPackets    += (multiplier*other.outErrorPackets)
        counters.inDiscardPackets   += (multiplier*other.inDiscardPackets)
        counters.outDiscardPackets  += (multiplier*other.outDiscardPackets)
        counters.inBroadcastPackets += (multiplier*other.inBroadcastPackets)
        counters.outBroadcastPackets+= (multiplier*other.outBroadcastPackets)
        counters.inMulticastPackets += (multiplier*other.inMulticastPackets)
        counters.outMulticastPackets+= (multiplier*other.outMulticastPackets)
        counters.inUnicastPackets   += (multiplier*other.inUnicastPackets)
        counters.outUnicastPackets  += (multiplier*other.outUnicastPackets)
        counters.inUnknownProtocolPackets   += (multiplier*other.inUnknownProtocolPackets)
        counters.outGratuitousArpPackets    += (multiplier*other.outGratuitousArpPackets)
        counters.operationalStatusChanges   += (multiplier*other.operationalStatusChanges)

    @staticmethod
    def _addToCounters(counters, other):
        Interface.__multilpyAndAddCounters(counters, other, 1)

    @staticmethod
    def _subtractFromCounters(counters, other):
        Interface.__multilpyAndAddCounters(counters, other, -1)

#-----------------------------------------------------------------------------------------------------------------------
class PeriodicCountersContainer(object):

    class PeriodicCounter(object):
        def __init__(self, numIntervals):
            self.values  = []
            self.average   = 0
            self.numIntervals = numIntervals

        def __str__(self):
            return str(self.average)

        def addValue(self, val):

            if len(self.values) == self.numIntervals+1:
                # removes the first item
                self.values.pop(0)

            # adds an item to the end
            # Note: must be an integer
            self.values.append(val)

            self._calcAverage()

        def _calcAverage(self):
            if len(self.values)>1:
                numIntervals = len(self.values)-1
                self.average = float((self.values[numIntervals] - self.values[0])) / numIntervals

    def __init__(self, logger, interface, numIntervals):
        """Instantiate a new periodic counters contianer object.

        Args:
            logger: 
            interface:
            numIntervals: specified num of times to save history

        Raises:
            None
        """

        self._log = logger
        self.interface = interface      

        # counters
        self.countersData = CountersOperData() 
        self._rxPacketsCounter  = self.PeriodicCounter(numIntervals)
        self._txPacketsCounter  = self.PeriodicCounter(numIntervals)
        self._rxBytesCounter    = self.PeriodicCounter(numIntervals)
        self._txBytesCounter    = self.PeriodicCounter(numIntervals)

        # rates
        self.rxPacketsPerSec = 0
        self.txPacketsPerSec = 0
        self.rxBitsPerSec    = 0
        self.txBitsPerSec    = 0

    def tick(self):

        self._log("call-periodic-counters").debug5("%s: called periodic counters tick().", self.interface.name)

        countersData = self._getCounters()

        if countersData is not None:
            self._rxPacketsCounter.addValue(countersData.inPackets)
            self._txPacketsCounter.addValue(countersData.outPackets)
            self._rxBytesCounter.addValue(countersData.inOctets)
            self._txBytesCounter.addValue(countersData.outOctets)

            self.rxPacketsPerSec = self._getAsPacketsPerSec(self._rxPacketsCounter)
            self.txPacketsPerSec = self._getAsPacketsPerSec(self._txPacketsCounter)
            self.rxBitsPerSec = self._getAsBitsPerSec(self._rxBytesCounter)
            self.txBitsPerSec = self._getAsBitsPerSec(self._txBytesCounter)


            rateInMinutes = Interface.PERIODIC_COUNTERS_INTERVAL_RATE_SEC * Interface.PERIODIC_COUNTERS_NUM_INTERVALS / 60

            self._log("interface-periodic-counters-rx-rate").debug4("%s: %s minutes rx rate %s bits/sec, %s packets/sec", 
                                                                    self.interface.name, 
                                                                    rateInMinutes,
                                                                    self.rxBitsPerSec, self.rxPacketsPerSec)

            self._log("interface-periodic-counters-tx-rate").debug4("%s: %s minutes tx rate %s bits/sec, %s packets/sec", 
                                                                    self.interface.name, 
                                                                    rateInMinutes,
                                                                    self.txBitsPerSec, self.txPacketsPerSec)

    def _getAsBitsPerSec(self, bytesCounter):
        return int(bytesCounter.average * 8 / Interface.PERIODIC_COUNTERS_INTERVAL_RATE_SEC)

    def _getAsPacketsPerSec(self, packetsCounter):
        return int(packetsCounter.average / Interface.PERIODIC_COUNTERS_INTERVAL_RATE_SEC) 

    def _getCounters(self):
        self.countersData.__init__() # clear
        rc = self.interface.getIfCounters(None, self.countersData, isRateCounters=False, shouldSetExtCounters=False)
        
        if rc != ReturnCodes.kOk:
            self._log("interface-periodic-counters-fail").debug4("%s: failed retrieve rx and tx counters", self.interface.name)
            return None

        self._log("interface-periodic-counters").debug3("%s: rx and tx counters are %s", self.interface.name, self.countersData)
        return self.countersData


#-----------------------------------------------------------------------------------------------------------------------
class Task(object):

    class Config:
        def __init__ (self, interval, enabled):
            self.isEnabled = enabled
            self.interval = interval

    def __init__ (self, functor, interval):
        """Instantiate a new task object.

        Args:
            functor: callable object to be invoked
            task: specified periodic interval (in seconds)

        Raises:
            None
        """

        self.name = functor.__name__
        self.functor = functor
        self.config = Task.Config(interval, True)
        ### this may create a burst of calls if creation and run have a big time difference ###
        self.nextRun = time.time() + self.config.interval
        

    def shouldRun(self):
        shouldRun = time.time() >= self.nextRun
        ### writing reference (pointer) is atomic, so we shouldn't have a problem if we access the current config class ###
        if not self.config.isEnabled:
            if shouldRun:
                self.nextRun += self.config.interval
            return False

        return shouldRun

    def run(self):
        self.functor()
        self.nextRun += self.config.interval
        
    def setConfig(self, config):
        self.config = config

    def getConfig(self):
        return self.config

    def createConfig(self):
        return Task.Config(0,True)

class TasksThread(Thread):

    DEFAULT_SLEEP_TIME = 0.1
    DEFAULT_MAX_RETRY  = 10

    def __init__ (self, logger, name):
        Thread.__init__(self, name=("%s-tasks-thread" % name))

        self._log = logger
        self.tasks = []
        self.wasStopped = False
        self.numRetries = 0
        self.sleepSecTime = self.DEFAULT_SLEEP_TIME
        self.daemon = True # a daemon thread - does not affect app exit

    def addTask(self, functor, interval):
        task = Task(functor, interval)
        self.tasks.append(task)
        return task

    def addTaskObject (self, task):
        self.tasks.append(task)

    def run(self):
        self._log("stop-tasks-thread").notice("%s: tasks thread has been launched.", self.name)
        
        while not self.wasStopped:
            for t in self.tasks:
                if t.shouldRun():
                    try:
                        self._log("stop-run").debug4("%s: task '%s' has been executed.", self.name, t.name)
                        t.run()

                    except Exception as ex:  
                        self.numRetries += 1
                        
                        if self.numRetries > self.DEFAULT_MAX_RETRY:
                            a.infra.process.processFatal(str(self.name) + ": task '"+ str(t.name) + "' exceptions exceeded max retries")
                        else:
                            self._log("task-exception").error("%s: unexpected error #%s for task '%s' - %s", self.name, self.numRetries, t.name, ex)  

            
            time.sleep(self.sleepSecTime)
        
        self._log("stop-tasks-thread").notice("%s: tasks thread has been terminated.", self.name)

    def stop(self):
        self._log("stop-tasks-thread").notice("%s: tasks thread has been stopped.", self.name)
        self.wasStopped = True



