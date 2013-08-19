# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from interfaces.manager import IfManager
from interfaces.client import IfClient
from interfaces.interface import Interface
from interfaces.ip import IpVersion
from interfaces.oper.snmp_traps_manager import SnmpTrapsManager
from system import SystemContainer  
from network_ipv6 import NetworkIpv6Container
from a.sys.blinky.domain_priority import DomainPriority
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper
from a.infra.basic.return_codes import ReturnCodes
from a.infra.basic.memory_definitions import AtomicInt
from a.sys.net.tech_interfaces.tech.interfaces.blinky_interfaces_gen import BlinkyInterfaces
from a.sys.net.tech_content_interfaces.tech.content.interfaces.interface.blinky_interface_list_gen import BlinkyInterfaceList as BlinkyContentInterfaceList
from a.sys.net.tech_content_delivery.tech.content.delivery.blinky_delivery_gen import BlinkyDelivery
from a.sys.net.tech_system.tech.system.blinky_system_gen import BlinkySystem 
from a.sys.net.tech_network_ipv6.tech.network.ipv6.blinky_ipv6_gen import BlinkyIpv6 as BlinkyNetworkIpv6Neighbors
from a.sys.net import config_file
from content_interface import ContentIfTable
from content_interface import ContentDeliveryContainer
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.counters.counters_oper_data_gen import CountersOperData
from a.sys.net.local_ipv6_address_resolver import LocalIpv6AddressResolver
from a.sys.net.lnx.iptables import IpTablesService
from a.sys.net.lnx.iptables import IpTablesConfigFile
import a.sys.net.lnx.device
import a.sys.net.lnx.route
import a.sys.net.lnx.name
import a.sys.net.lnx.neighbour
import a.sys.net.lnx.common

from datetime import datetime
import os

if  __package__ is None:
    G_NAME_MODULE_NET = "unknown"
    G_NAME_GROUP_NET_CONFIG_MANAGER = "unknown"
else:
    from . import G_NAME_MODULE_NET
    from . import G_NAME_GROUP_NET_CONFIG_MANAGER

##############################################
# This class contains the network configuration
##############################################
class _NetBase(object):
    """This class contains the network configuration"""

    def __init__ (self, name, priority):
        self.name = name
        self.priority = priority

        self._log = None
        self._domain = None
        self.interfaceContainer = None
        
#-----------------------------------------------------------------------------------------------------------------------
    def _initLogger(self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_NET, G_NAME_GROUP_NET_CONFIG_MANAGER, instance = self.name)

        self._log("init-logger").debug2("Init logger.")

        # create interface container
        self.interfaceContainer = self._createInterfaceContainer()

#-----------------------------------------------------------------------------------------------------------------------
    def _initBlinky(self, agent):

        self._log("init-blinky").debug2("Init blinky by agent.")

        domain = agent.createConfigDomain("sys-net-%s" % self.name, self.priority)

        # hook for extra registration
        rc = self._registerToDomain(domain)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        blinkyInterfaces = BlinkyInterfaces.s_create(self._log, domain)

        # attach
        rc = self.interfaceContainer.attachToBlinky(blinkyInterfaces)
        if rc != ReturnCodes.kOk:
            self._log("attach-if-blinky-failed").error("net manager has failed attaching to interfacs blinky")
            return ReturnCodes.kGeneralError
      
        # register
        domain.registerNode(blinkyInterfaces)
      
        # attach oper after domain registeration is done
        self.interfaceContainer.attachToBlinkyOper()

        self._domain = domain

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def initExternalData(self, sysParamsCfg, specificParams):
        __pychecker__="no-argsused"  # sysParamsCfg not used
        pass

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self._domain:
            self._domain.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    # Note: Must be called after initExternalData()
    def activate(self, logger, agent):

        # init logger
        self._initLogger(logger)
        self._postInitLogger()

        # init blinky
        rc = self._initBlinky(agent)
        if rc != ReturnCodes.kOk:
            self._log("init-blinky-failed").error("net manager has failed in blinky initialzation")
            return ReturnCodes.kGeneralError

        # ready
        self._domain.registrationDone()

        self._log("activate").debug2("net manager has been activate")
        self._preActivation()

        # trigger
        rc = self._domain.triggerSubscriptions()
        if rc != ReturnCodes.kOk:
            self._log("trigger-failed").error("net manager has failed trigger the subscriptions")
            return ReturnCodes.kGeneralError

        self._postActivation()

        return ReturnCodes.kOk 
        
#-----------------------------------------------------------------------------------------------------------------------
    def shutdown(self):
        self._preShutdown()

        if self._domain:
            self._domain.shutdown()

        if self.interfaceContainer:
            self.interfaceContainer.shutdown()
        
#-----------------------------------------------------------------------------------------------------------------------
    def _postInitLogger(self):
        pass

#-----------------------------------------------------------------------------------------------------------------------
    def _preActivation(self):
        pass

#-----------------------------------------------------------------------------------------------------------------------
    def _postActivation(self):
        pass

#-----------------------------------------------------------------------------------------------------------------------
    def _preShutdown(self):
        pass

#-----------------------------------------------------------------------------------------------------------------------
    def _registerToDomain(self, domain):
        __pychecker__="no-argsused"  # domain not used
        return ReturnCodes.kOk 

#-----------------------------------------------------------------------------------------------------------------------
    def _createInterfaceContainer(self):
        raise NotImplementedError

##############################################
# This class manages the network configuration
##############################################
class NetManager(_NetBase):
    """This class manages the network configuration"""

    # consts use for the specific params dictionary 
    SPECIFIC_PARAM_KEY_ALLOW_DYNAMIC_CONFIG    = "allow-dynamic-config" # allow only on std/vm
    SPECIFIC_PARAM_KEY_SSHD_PORT        = "sshd-port"
    SPECIFIC_PARAM_KEY_UPDATE_OSCAR_CMD   = "update-osc-cmd"
    SPECIFIC_PARAM_KEY_EARLY_CFG_FILE   = "early-cfg"
    SPECIFIC_PARAM_KEY_LINE_CFG_FILE    = "line-cfg"
    SPECIFIC_PARAM_KEY_LINE_STATE_FILE  = "line-state"
    SPECIFIC_PARAM_KEY_MNG_CFG_FILE     = "mng-cfg"
    SPECIFIC_PARAM_KEY_NET_STATE_FILE   = "net-sig"
    SPECIFIC_PARAM_KEY_LINE_NICS_FILE   = "line-nics"
    SPECIFIC_PARAM_KEY_DELIVERY_STATUS_FILE = "delivery-status"
    SPECIFIC_PARAM_KEY_IPV6_NEIGHBOR_TABLE_FILE = "ipv6-neighbor-table"
    SPECIFIC_PARAM_KEY_NDISC6_REQUESTS_DIRECTORY = "ndisc6-requests-directory"

    #consts for sections/fields names in sys-param
    CONFIG_SECTION_NET_MANAGER = "net-manager"
    CONFIG_VAR_NET_MANAGER_SSH_PORT= "ssh-port"

    #default values for data in sys-param
    DEFAULT_SSH_PORT = 2022

    DELIVERY_INTERFACES_STATE_INTERVAL_RATE_SEC = 3     # 3 seconds
    DELIVERY_INTERFACES_IPV6_NEIGHBOR_TABLE_INTERVAL_RATE_SEC = 10  #10 seconds
    DELIVERY_INTERFACES_IPV6_NDISC6_REQUESTS_INTERVAL_RATE_SEC = 10  #10 seconds



    def __init__ (self, name):
        _NetBase.__init__(self, name, DomainPriority.kSystemIP_NetworkMain)
        self.systemContainer = None
        self.contentInterfaceList = None
        self.contentDeliveryContainer = None

        self.networkIpv6Container = None
        self.applicationInitiatedDiscoveryContainer = None

        self.allowDynamicConfig = False
        self.lineNicsFile = ""
        self.startTrx = False
        self.sshPort = -1
        self.signalFile = None

        # network configuration files
        self.hostsFile = None
        self.resolvConfFile = None
        self.earlyCfgFile = None
        self.lineCfgFile = None  
        self.lineStateFile = None  
        self.mngCfgFile = None
        self.deliveryStatusFileName = None

        self.localIpv6AddressResolver = None
        self.processLineNdisc6RequestTask = None
        self.updateDeliveryIpv6NeighborTableTask = None

        # thread in charge of periodic tasks
        self.thread = None

        # cached interfaces - use to cache running interfaces for repeated periodic tasks
        self.cachedInterfaces = []

        # snmp traps manager
        self.snmpTrapsManager = SnmpTrapsManager()

#-----------------------------------------------------------------------------------------------------------------------
    def initExternalData(self, sysParamsCfg, specificParams):
        #__pychecker__="no-argsused"  # sysParamsCfg not used

        self.sshPort = sysParamsCfg.getInt(self.CONFIG_SECTION_NET_MANAGER, 
                                           self.CONFIG_VAR_NET_MANAGER_SSH_PORT, 
                                           self.DEFAULT_SSH_PORT)

        self.allowDynamicConfig = specificParams[self.SPECIFIC_PARAM_KEY_ALLOW_DYNAMIC_CONFIG]
        self.lineNicsFile = specificParams[self.SPECIFIC_PARAM_KEY_LINE_NICS_FILE]
        self.signalFile = specificParams[self.SPECIFIC_PARAM_KEY_NET_STATE_FILE]

        # set static update command
        config_file.SysWebConfigFile.setUpdateCommand(specificParams[self.SPECIFIC_PARAM_KEY_UPDATE_OSCAR_CMD])

        self.mngCfgFile = config_file.SysWebConfigFile(specificParams[self.SPECIFIC_PARAM_KEY_MNG_CFG_FILE])
        self.earlyCfgFile = config_file.EarlyConfigFile(specificParams[self.SPECIFIC_PARAM_KEY_EARLY_CFG_FILE])
        self.lineCfgFile = config_file.LineConfigFile(specificParams[self.SPECIFIC_PARAM_KEY_LINE_CFG_FILE])
        self.lineStateFile = config_file.LineStateFile(specificParams[self.SPECIFIC_PARAM_KEY_LINE_STATE_FILE])
        self.deliveryStatusFileName = specificParams.get(self.SPECIFIC_PARAM_KEY_DELIVERY_STATUS_FILE,None)

        lineIpv6NeighborTableFile = specificParams.get(self.SPECIFIC_PARAM_KEY_IPV6_NEIGHBOR_TABLE_FILE,None)
        lineNdisc6RequestsDirectory = specificParams.get(self.SPECIFIC_PARAM_KEY_NDISC6_REQUESTS_DIRECTORY,None)
        self.localIpv6AddressResolver = LocalIpv6AddressResolver(lineNdisc6RequestsDirectory, lineIpv6NeighborTableFile)

        # dump configuration
        #---------------------------------------------------------------------------
        logLines = []        
        for k,v  in specificParams.iteritems():
            logLines.append("%-*s : %s" % (25,k,v))
        logLines.sort()
        print "\n".join(logLines)   
         
#-----------------------------------------------------------------------------------------------------------------------
    def domainTrxProgress(self, progress):

        self._log("domain-trx-progress").debug2("Net manager progress=%s", progress)

        rc = ReturnCodes.kOk

        if progress.isPreparePrivateAfter():
            rc = self.preparePrivateAfter()
            if rc == ReturnCodes.kOk:
                self.startTrx = True
        elif progress.isCommitPrivateAfter():
            rc = self.commitPrivateAfter()
        elif progress.isAbortPrivateAfter():
            rc = self.abortPrivateAfter()

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateAfter(self):

        if self.startTrx is True:
            self._log("net-manager-commit-private-after").debug3("Net manager commitPrivateAfter was called")

            # commit
            self.lineCfgFile.commit()
            self.mngCfgFile.commit()
            self.earlyCfgFile.commit()

            if self.allowDynamicConfig: 
                self.hostsFile.commit()
                self.resolvConfFile.commit()

            self.startTrx = False

        # update interfaces cache
        # note: holds a copy of the interfaces list
        if self.interfaceContainer.interfaceList:
            self._log("cache-interfaces-update").debug3("Net manager updates cache interfaces")
            self.cachedInterfaces = self.interfaceContainer.interfaceList.runningValues()

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateAfter(self):

        if self.startTrx is True:
            self._log("net-manager-abort-private-after").debug3("Net manager abortPrivateAfter was called")

            self.mngCfgFile.abort()
            self.earlyCfgFile.abort()

            if self.allowDynamicConfig: 
                self.hostsFile.abort()
                self.resolvConfFile.abort()

            self.startTrx = False

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateAfter(self):

        self._log("net-manager-prepare-private-after").debug3("Net manager preparePrivateAfter was called")

        mngIf = None
        techIf = None
        deliveryIfList = []
        lineIfList = []

        if self.interfaceContainer.interfaceList:
            interfaces = self.interfaceContainer.interfaceList.candidateValues()

            for currentI in interfaces:

                if currentI.isDeliveryEnabled() is True:
                    deliveryIfList.append(currentI)

                elif currentI.isLineEnabled() is True:
                    lineIfList.append(currentI)

                elif currentI.isManagementEnabled() is True:

                    if currentI.candidateTechMode:
                        techIf = currentI
                    else:
                        mngIf = currentI
        
        rc = self.__validateContentInterfaces(deliveryIfList, lineIfList)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        # prepare configuration files
        rc = self.prepareConfigFiles(deliveryIfList, lineIfList, mngIf, techIf)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def prepareConfigFiles(self, deliveryIfList, lineIfList, mngIf, techIf):

        # clear data
        self.lineCfgFile.clear()
        self.mngCfgFile.clear()
        self.earlyCfgFile.clear()

        pairList = []
        hostname = self.systemContainer.getHostname(False)

        i=0
        # add delivery interfaces
        for deliveryIf in deliveryIfList:

            ipv4 = deliveryIf.getIpNetwork(IpVersion.kIPv4)
            ipv6 = deliveryIf.getIpNetwork(IpVersion.kIPv6)
            ipv4Gateway = deliveryIf.getDefaultGateway(IpVersion.kIPv4)
            ipv6Gateway = deliveryIf.getDefaultGateway(IpVersion.kIPv6)
            device = deliveryIf.deviceName(False)

            interface = self.lineCfgFile.deliveryInterfaces[i]
            i += 1

            interface.interfaceName = deliveryIf.name

            if ipv4: 
                interface.deliveryIPv4.deliveryIP = str(ipv4.ip)
                interface.deliveryIPv4.deliveryPrefixLen = int(ipv4.prefixlen)

            if ipv6: 
                interface.deliveryIPv6.deliveryIP = str(ipv6.ip)
                interface.deliveryIPv6.deliveryPrefixLen = int(ipv6.prefixlen)

            if ipv4Gateway: interface.deliveryIPv4.deliveryGateway = str(ipv4Gateway)
            if ipv6Gateway: interface.deliveryIPv6.deliveryGateway = str(ipv6Gateway)
            if device: interface.osDevice = device

            interface.adminEnable = deliveryIf.isUp(False)


        # set delivery-interface-failover
        self.lineCfgFile.deliveryInterfaceFailover = self.contentDeliveryContainer.candidateDeliveryInterfaceFailover

        # set lan IPv6 redirects configuration
        if self.applicationInitiatedDiscoveryContainer != None:
            self.lineCfgFile.lanIpv6Redirects.enabled = self.applicationInitiatedDiscoveryContainer.enabledCandidate
            self.lineCfgFile.lanIpv6Redirects.maxRequestsPerSec = self.applicationInitiatedDiscoveryContainer.maxRequestRateCandidate
            self.lineCfgFile.lanIpv6Redirects.requestsQueueSize = self.applicationInitiatedDiscoveryContainer.maxPendingRequestsCandidate

        # add line interfaces
        lineToDeliveryMap = self.__getLineToDeliveryMap()
        for lineIf in lineIfList:
            adminEnable = lineIf.isUp(False)
            self.lineCfgFile.addLineInterface(lineIf.name, 
                                              lineIf.device.candidatePciIndex,
                                              lineToDeliveryMap.get(lineIf.name,""),
                                              adminEnable)

        # add management interface
        if not mngIf is None:
            ipv4 = mngIf.getIpNetwork(IpVersion.kIPv4)
            gateway = mngIf.getDefaultGateway(IpVersion.kIPv4)
            
            if ipv4: 
                self.mngCfgFile.mngIp = str(ipv4.ip)
                self.earlyCfgFile.ip[mngIf.name] = str(ipv4)

            if hostname:
                self.earlyCfgFile.host = hostname

            if ipv4 and hostname:
                pair = (str(ipv4.ip), hostname)
                pairList.append(pair) 

            if gateway: self.earlyCfgFile.gw = str(gateway) 
            if hostname: 
                for interface in self.lineCfgFile.deliveryInterfaces:
                    interface.hostname = hostname 
                
        # add tech interface
        if not techIf is None: 
            ipv4 = techIf.getIpNetwork(IpVersion.kIPv4)

            if ipv4: self.earlyCfgFile.ip[techIf.name] = str(ipv4)

            if ipv4 and hostname:
                pair = (str(ipv4.ip), hostname+"-tech")
                pairList.append(pair) 

        # dump data
        self.mngCfgFile.dumpData()
        self.earlyCfgFile.dumpData()
        self.lineCfgFile.dumpData()

        if self.allowDynamicConfig: 
            # Set name-resolving information in resolv.conf
            nameResolution = self.systemContainer.getNameResolution()
            nameServers = []
            if nameResolution.getDnsEnabled():
                nameServers = nameResolution.getDnsNameServers()
            searchDomains = nameResolution.getDnsSearchDomains()
            self.resolvConfFile.dumpData(nameServers = nameServers, searchDomains = searchDomains)
    
            # Add static name-resolving information to /etc/hosts
            staticHosts = nameResolution.getStaticHosts() 
            for (addr, hosts) in staticHosts:
                if len(hosts) == 0:
                    self._log("empty-hosts-list").notice("No host names for ip %s" % addr)
                    self.setConfigErrorStr("No host names for ip %s" % addr)
                    return ReturnCodes.kGeneralError

            pairList.extend(nameResolution.getStaticHosts())
    
            self.hostsFile.dumpData(pairList)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
### temp until 2.7.0 (1/11/2012)###
    def __validateContentInterfaces(self, deliveryIfList, lineIfList):

        deliveryNames = []
        for  deliveryIf in deliveryIfList:
            deliveryNames.append(deliveryIf.name)

        lineNames = []
        for  lineIf in lineIfList:
            lineNames.append(lineIf.name)

        if self.contentInterfaceList:
            contentInterfaces = self.contentInterfaceList.candidateValues()

            for currentI in contentInterfaces:
                if currentI.delivery is not None:
                    preferredDeliveryInterface = currentI.delivery.candidatePreferredDeliveryInterface

                    # line interface must be mapped to delivery interface
                    if (currentI.name in lineNames) and (not preferredDeliveryInterface in deliveryNames):
   
                        self._log("invalid-preferred-delivery-interface").notice("%s: preferredDeliveryInterface '%s' is not a valid delivery interface", 
                                                                                currentI.name, preferredDeliveryInterface)
                        self.setConfigErrorStr("%s: preferred-delivery-interface '%s' is not a valid delivery interface" % 
                                               (currentI.name, preferredDeliveryInterface))

                        return ReturnCodes.kGeneralError

        return ReturnCodes.kOk 

#-----------------------------------------------------------------------------------------------------------------------
### temp until 2.7.0 (1/11/2012)###
    def __getLineToDeliveryMap(self):

        lineToDeliveryMap = {}

        if self.contentInterfaceList:
            contentInterfaces = self.contentInterfaceList.candidateValues()

            for currentI in contentInterfaces:
                if currentI.delivery is not None:
                    preferredDeliveryInterface = currentI.delivery.candidatePreferredDeliveryInterface
                    lineToDeliveryMap[currentI.name] = preferredDeliveryInterface

        return lineToDeliveryMap 

#-----------------------------------------------------------------------------------------------------------------------
    def getStatsCounters(self):

        self._log("net-manager-get-stats-counters").debug3("Net manager getStatsCounters was called")

        interfacesCountersMap = {}
        iCountersData = CountersOperData() 

        for currentI in self.cachedInterfaces:

            iCountersData.__init__() # clear
            rc = currentI.getIfCounters(None, iCountersData, isRateCounters=True, shouldSetExtCounters=True)

            if rc == ReturnCodes.kOk:
                for key, value in iCountersData.__dict__.iteritems():
                    if type(value) is int:
                        # '/' char is considred a path notation in stats
                        # so TenGigE0/0 will be modified to TenGigE0-0
                        iName = currentI.name.replace("/","-",1)
                        iKey = "%s-%s" % (iName,key) 

                        interfacesCountersMap[iKey] = value

        self._log("net-manager-stats-counters-results").debug4("Net manager stats counters= %s" % interfacesCountersMap)

        return interfacesCountersMap

#-----------------------------------------------------------------------------------------------------------------------
    def __registerBlinkySystem(self, domain):

        blinkySystem = BlinkySystem.s_create(self._log, domain)

        systemContainer = SystemContainer(self._log)
        if self.allowDynamicConfig:
            systemContainer.setAllowDynamicConfig()

        self.systemContainer = SimpleContainerWrapper(self._log, systemContainer)
        self.hostsFile = a.sys.net.lnx.name.HostsFile(self._log)
        self.resolvConfFile = a.sys.net.lnx.name.ResolvConfFile(self._log)

        # attach
        rc = self.systemContainer.attachToBlinky(blinkySystem)
        if rc != ReturnCodes.kOk:
            self._log("attach-sys-blinky-failed").error("net manager has failed attaching to system blinky")
            return ReturnCodes.kGeneralError
      
        # register
        domain.registerNode(blinkySystem)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def __registerBlinkyNetworkIpv6(self, domain):

        blinkyNetworkIpv6Neighbors = BlinkyNetworkIpv6Neighbors.s_create(self._log, domain)

        networkIpv6Container = NetworkIpv6Container(self._log)

        ### get applicationInitiatedDiscovery class ###
        self.applicationInitiatedDiscoveryContainer = networkIpv6Container.neighbors.applicationInitiatedDiscovery

        # configurable periodic tasks
        self.processLineNdisc6RequestTask = a.sys.net.interfaces.interface.Task(self._processLineNdisc6Requests, self.DELIVERY_INTERFACES_IPV6_NDISC6_REQUESTS_INTERVAL_RATE_SEC)
        self.updateDeliveryIpv6NeighborTableTask = a.sys.net.interfaces.interface.Task(self._updateDeliveryIpv6NeighborTable,self.DELIVERY_INTERFACES_IPV6_NEIGHBOR_TABLE_INTERVAL_RATE_SEC)

        ### attach localAddressResolver and ndisc6 file read/write tasks to applicationInitiatedDiscovery ###
        self.applicationInitiatedDiscoveryContainer.setLocalAddressResolver(self.localIpv6AddressResolver)
        self.applicationInitiatedDiscoveryContainer.setRequestReadPeriodicTask(self.processLineNdisc6RequestTask)
        self.applicationInitiatedDiscoveryContainer.setTableReadPeriodicTask(self.updateDeliveryIpv6NeighborTableTask)

        self.networkIpv6Container = SimpleContainerWrapper(self._log, networkIpv6Container)

        # attach
        rc = self.networkIpv6Container.attachToBlinky(blinkyNetworkIpv6Neighbors)
        if rc != ReturnCodes.kOk:
            self._log("attach-network-ipv6-blinky-failed").error("net manager has failed attaching to network ipv6 blinky")
            return ReturnCodes.kGeneralError
      
        # register
        domain.registerNode(blinkyNetworkIpv6Neighbors)

        return ReturnCodes.kOk 

#-----------------------------------------------------------------------------------------------------------------------
    def __registerBlinkyContentInterfaces(self, domain):

        blinkyContentInterfaceList = BlinkyContentInterfaceList.s_create(self._log, domain)
        self.contentInterfaceList = ContentIfTable(self._log)
        self.contentInterfaceList.setStatusFile(self.deliveryStatusFileName)

        # attach
        rc = self.contentInterfaceList.attachToBlinky(blinkyContentInterfaceList)
        if rc != ReturnCodes.kOk:
            self._log("attach-content-interfaces-blinky-failed").error("net manager has failed attaching to content interface list blinky")
            return ReturnCodes.kGeneralError
      
        # register 
        domain.registerNode(blinkyContentInterfaceList)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def __registerBlinkyDelivery(self, domain):

        blinkyDelivery = BlinkyDelivery.s_create(self._log, domain)
        contentDeliveryContainer = ContentDeliveryContainer(self._log, self)
        self.contentDeliveryContainer = SimpleContainerWrapper(self._log, contentDeliveryContainer)
        
        # attach
        rc = self.contentDeliveryContainer.attachToBlinky(blinkyDelivery)
        if rc != ReturnCodes.kOk:
            self._log("attach-content-delivery-blinky-failed").error("net manager has failed attaching to content delivery blinky")
            return ReturnCodes.kGeneralError
      
        # register 
        domain.registerNode(blinkyDelivery)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def _registerToDomain(self, domain):

        # register trx progress functor
        domain.registerNotifyTrxProgressFunctor(self.domainTrxProgress)

        # register BlinkySystem
        rc = self.__registerBlinkySystem(domain)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        # register BlinkyContentInterfaceList
        rc = self.__registerBlinkyContentInterfaces(domain)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        # register BlinkyDelivery
        rc = self.__registerBlinkyDelivery(domain)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        # register BlinkyNetworkIpv6
        rc = self.__registerBlinkyNetworkIpv6(domain)
        if rc != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        # init snmp
        self.snmpTrapsManager.init(domain)
        
        return ReturnCodes.kOk 

#-----------------------------------------------------------------------------------------------------------------------
    def _preActivation(self):

        # check for IPv6 support in the current running kernel
        if os.path.exists("/proc/net/if_inet6") is True:
            self._log("kernel-ipv6-ready").notice("running kernel is ipv6 ready")
        else:
            self._log("kernel-ipv6-not-ready").error("running kernel is NOT ipv6 ready")
            raise RuntimeError("Running kernel is NOT IPv6 ready")

        if self.allowDynamicConfig:  
            # start ip table service
            self.__startIpTable()
             
            # activate Loopback
            self.__activateLoopback()
    
            # deactivate all eth devices and set a temporary name
            self.__renameAndDownEths()

            # dumps all the rules
            self.__clearRoutingPolicy()

#-----------------------------------------------------------------------------------------------------------------------
    def _postActivation(self):

        # cold start notification
        self.snmpTrapsManager.snmpInterfaceConfigured()

        # launch interface periodic tasks thread
        for currentI in self.cachedInterfaces:
            currentI.launchTasksThread()

        # create and start thread
        self.thread = a.sys.net.interfaces.interface.TasksThread(self._log, self.CONFIG_SECTION_NET_MANAGER)
        self.thread.addTask(self._updateInterfacesPeriodicCounters, Interface.PERIODIC_COUNTERS_INTERVAL_RATE_SEC)
        self.thread.addTask(self._updateDevicesChange, Interface.DEVICE_EVENTS_INTERVAL_RATE_SEC)
        self.thread.addTask(self._updateDeliveryInterfacesState, self.DELIVERY_INTERFACES_STATE_INTERVAL_RATE_SEC)

        # add configurable tasks
        self.thread.addTaskObject(self.processLineNdisc6RequestTask)
        self.thread.addTaskObject(self.updateDeliveryIpv6NeighborTableTask) #not on mini?

        self.thread.start()

        # signal activation done
        if os.path.exists(self.signalFile):
            a.infra.process.processFatal("signal file was already exists - %s", self.signalFile)

        fd = open(self.signalFile, 'w')
        fd.close()

        self._log("signal-file").debug3("net manager has signaled activation by creating %s" % self.signalFile)

#-----------------------------------------------------------------------------------------------------------------------
    def _preShutdown(self):
        if self.thread is not None:
            # stop and wait until the thread terminates
            self.thread.stop()
            self.thread.join(0.1)
    
            if self.thread.isAlive():
                self._log("net-manager-thread-alive").notice("net manager thread after shutdown is still alive")

        self.thread=None

        self.localIpv6AddressResolver.shutDown()

#-----------------------------------------------------------------------------------------------------------------------
    def _updateInterfacesPeriodicCounters(self):

        for currentI in self.cachedInterfaces:
            currentI.periodicCounters.tick()

#-----------------------------------------------------------------------------------------------------------------------
    def _updateDevicesChange(self):

        for currentI in self.cachedInterfaces:
            currentI.actionOnDeviceChange()

#-----------------------------------------------------------------------------------------------------------------------
    def _updateDeliveryInterfacesState(self):

        if len(self.cachedInterfaces) > 0:

            i=0
            for currentI in self.cachedInterfaces:
    
                if currentI.isDeliveryEnabled() is True:
                    
                    deliveryIf = self.lineStateFile.deliveryInterfaces[i]
                    i += 1
    
                    # 1 - set interface name
                    deliveryIf.interfaceName = currentI.name
    
                    # 2 - connectivity check
                    if currentI.connectivityCheck:
                        deliveryIf.deliveryIPv4State.serviceStatus = currentI.connectivityCheck.isConnectivityAvailable(IpVersion.kIPv4)
                        deliveryIf.deliveryIPv6State.serviceStatus = currentI.connectivityCheck.isConnectivityAvailable(IpVersion.kIPv6)

                    # 3 - resolve default gateway MAC address
                    osDevice = currentI.deviceName(True)
                    if osDevice:
                        
                        # ipv4
                        ipv4Gateway = currentI.getDefaultGateway(IpVersion.kIPv4)
                        if ipv4Gateway:
                            
                            macV4 = a.sys.net.lnx.neighbour.NeighbourUtils.getNeighbourMacAddress(self._log, osDevice, 
                                                                                                  str(ipv4Gateway),
                                                                                                  IpVersion.kIPv4)
                            if macV4: 
                                deliveryIf.deliveryIPv4State.deliveryGatewayMac = macV4
                            else:
                                a.sys.net.lnx.neighbour.Arping.sendArpRequest(self._log, osDevice, str(ipv4Gateway),
                                                                              count=3,timeout=1,blocking=False)
                        else:
                            deliveryIf.deliveryIPv4State.deliveryGatewayMac = ""


                        # ipv6
                        ipv6Gateway = currentI.getDefaultGateway(IpVersion.kIPv6)
                        if ipv6Gateway:
        
                            macV6 = a.sys.net.lnx.neighbour.NeighbourUtils.getNeighbourMacAddress(self._log, osDevice,
                                                                                                  str(ipv6Gateway),
                                                                                                  IpVersion.kIPv6)
                            if macV6: 
                                deliveryIf.deliveryIPv6State.deliveryGatewayMac = macV6
                            else:
                                a.sys.net.lnx.neighbour.Ndisc.sendNdiscRequest(self._log, osDevice, str(ipv6Gateway),
                                                                               count=3,timeout=1,blocking=False)
                        else:
                            deliveryIf.deliveryIPv6State.deliveryGatewayMac = ""

    
            # dump and commit
            self.lineStateFile.dumpData()
            self.lineStateFile.commit()

#-----------------------------------------------------------------------------------------------------------------------
    def _updateDeliveryIpv6NeighborTable(self):
        if len(self.cachedInterfaces) > 0:
            cachedDeliveryInterfaces = []
            for currentI in self.cachedInterfaces:
    
                if currentI.isDeliveryEnabled() is True:
                    cachedDeliveryInterfaces.append(currentI.deviceName(True))

            self.localIpv6AddressResolver.updateDeliveryIpv6NeighborTable(cachedDeliveryInterfaces)


#-----------------------------------------------------------------------------------------------------------------------
    def _processLineNdisc6Requests(self):
        if len(self.cachedInterfaces) > 0:
            cachedDeliveryInterfaces = []
            for currentI in self.cachedInterfaces:
                
                if currentI.isDeliveryEnabled() is True:
                    if currentI.deviceName(True):
                        cachedDeliveryInterfaces.append(currentI.deviceName(True))

            self.localIpv6AddressResolver.processNdisc6Requests(cachedDeliveryInterfaces)
            

#-----------------------------------------------------------------------------------------------------------------------
    def _createInterfaceContainer(self):
        ifManager = IfManager(self._log, self.name, self.allowDynamicConfig, self.lineNicsFile, self.snmpTrapsManager)
        ifManager.initData(self.sshPort)

        return ifManager

#-----------------------------------------------------------------------------------------------------------------------
    def _postInitLogger(self):

        # init logger
        self.mngCfgFile.initLogger(self._log)
        self.earlyCfgFile.initLogger(self._log)
        self.lineCfgFile.initLogger(self._log)
        self.lineStateFile.initLogger(self._log)
        self.localIpv6AddressResolver.initLogger(self._log)
        self.snmpTrapsManager.initLogger(self._log)
                 
        # dump first config files
        self.__dumpData(self.earlyCfgFile)
        self.__dumpData(self.lineCfgFile)
        self.__dumpData(self.mngCfgFile)

#-----------------------------------------------------------------------------------------------------------------------
    def __startIpTable(self):

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.__createIpTablesFileIfNeeded(IpTablesConfigFile.IPV4_TABLE_CONFIG_FILE, IpTablesConfigFile.IPV4TABLES_CONFIG_TEMPLATE, timestamp)
        self.__createIpTablesFileIfNeeded(IpTablesConfigFile.IPV6_TABLE_CONFIG_FILE, IpTablesConfigFile.IPV6TABLES_CONFIG_TEMPLATE, timestamp)
        
        # restarting the iptables service flushes exisitng firewall rules 
        # and reloads new rules from the iptables config file
        self.__restartServiceOrCrash(IpTablesService.IPV4_TABLE_COMMAND_NAME)
        self.__restartServiceOrCrash(IpTablesService.IPV6_TABLE_COMMAND_NAME)

        self._log("iptables-config-file").notice("iptables config files: ipv4 = '%s' , ipv6 = '%s'", 
                                                 IpTablesConfigFile.IPV4_TABLE_CONFIG_FILE, 
                                                 IpTablesConfigFile.IPV6_TABLE_CONFIG_FILE)

#-----------------------------------------------------------------------------------------------------------------------
    def __restartServiceOrCrash(self, serviceName):
        (rc, stdOut, stdErr) = a.sys.net.lnx.common.Command.execute(self._log, self.CONFIG_SECTION_NET_MANAGER, 
                                                                    ("service %s restart" % serviceName), blocking=True)

        if rc != 0:
            self._log("restart-service-failed").error("failed to restart service %s (rc=%s) - %s", serviceName,  rc, stdErr)
            a.infra.process.processFatal("service %s failed loading", serviceName)

#-----------------------------------------------------------------------------------------------------------------------
    def __createIpTablesFileIfNeeded(self, filename, template, timestamp):
        if not os.path.exists(filename):

            data = {'timestamp' : timestamp}
            self._log("create-iptables-config-file").notice("creates iptables config file '%s' - template: %s", 
                                                            filename, template)
    
            fd =  open(filename, 'w')
            fd.write(template % data)
            fd.close()          

#-----------------------------------------------------------------------------------------------------------------------
    def __activateLoopback(self):
        rc = a.sys.net.lnx.device.IpLink.activateDevice(self._log, "lo")
        self._log("loopback-activate").debug2("Activating Loopback device.")

        if not a.sys.net.lnx.common.Command.isReturnOk(rc):
            a.infra.process.processFatal("%s: Failed at activate Loopback device", self.name)

#-----------------------------------------------------------------------------------------------------------------------
    def __clearRoutingPolicy(self):
        routeTables = [100,101, # qb100-6a2 and qvm-30
                       108,109] # qb100-6b2

        for table in routeTables:
            a.sys.net.lnx.route.IpRule.flushRules(self._log, str(table), version=4)
            a.sys.net.lnx.route.IpRule.flushRules(self._log, str(table), version=6)
            self._log("flush-rules").debug2("Flushing all ip rules of table %s.", table)

#-----------------------------------------------------------------------------------------------------------------------
    def __renameAndDownEths(self):

        ethList = a.sys.net.lnx.device.DeviceUtils.getEthDevices()
        self._log("eth-list").debug2("eth List: ", ethList)

        for eth in ethList:

            # device is down
            rc = a.sys.net.lnx.device.IpLink.deactivateDevice(self._log, eth)
            self._log("eth-deactivate").debug2("Deactivating %s device", eth)

            if a.sys.net.lnx.common.Command.isReturnOk(rc):
                # removing all IPs from a device
                rc = a.sys.net.lnx.device.IpAddress.flushAddresses(self._log, eth, scope="global")
                self._log("flush-addr").debug2("Flush all IP addresses of %s device", eth)
    
                if not a.sys.net.lnx.common.Command.isReturnOk(rc):
                    a.infra.process.processFatal("%s: Failed flushing all IPs of %s device", self.name, eth)
    
                # eth device name length is limited
                if len(eth) < 10:
                    # set temp name to device
                    tempEth = "%s-tmp" % eth
                    rc = a.sys.net.lnx.device.IpLink.renameDevice(self._log, eth, tempEth)
                    self._log("eth-tmp-rename").debug2("Renaming %s device to %s", eth, tempEth)
        
                    if not a.sys.net.lnx.common.Command.isReturnOk(rc):
                        a.infra.process.processFatal("%s: Failed renaming %s device", self.name, eth)
            else:
                # Note: DPDK interfaces are handled in user space 
                # and are not visible to the Linux kernel
                self._log("eth-deactivate-failed").debug2("Failed at deactivate %s device", eth)

#-----------------------------------------------------------------------------------------------------------------------
    def __dumpData(self, fileObject):
        fileObject.dumpData()
        fileObject.commit()

##############################################
# This class listens and notifies network configuration changes
##############################################
class _NetListenerBase(_NetBase):
    """This class listens and notifies network configuration changes"""

    def __init__ (self, name, priority, notifier):
        _NetBase.__init__(self, name, priority)
        self.notifier = notifier
       
#-----------------------------------------------------------------------------------------------------------------------
    def _createInterfaceContainer(self):
        return IfClient(self._log, self.name, self.notifier)

#-----------------------------------------------------------------------------------------------------------------------
class NetPreListener(_NetListenerBase):
    """This class listens and notifies network configuration before changes"""

    def __init__ (self, name, notifier):
        _NetListenerBase.__init__(self, name, DomainPriority.kSystemIP_NetworkBefore, notifier)

#-----------------------------------------------------------------------------------------------------------------------
class NetPostListener(_NetListenerBase):
    """This class listens and notifies network configuration after changes"""

    def __init__ (self, name, notifier):
        _NetListenerBase.__init__(self, name, DomainPriority.kSystemIP_NetworkAfter, notifier)

