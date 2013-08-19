#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: amiry

import time, os
import a.sys.net.net_manager
import a.sys.net.interfaces

from a.sys.blinky.domain_priority import DomainPriority
from a.content.reporting.reporting_manager import ReportingManager
from a.content.reporting.reporting_blinky_adapter import ReportingBlinkyAdapter
from a.content.reporting.tech_content_reporting.tech.content.reporting.blinky_reporting_gen import BlinkyReporting

if  __package__ is None:
    G_NAME_MODULE_CDN_INTEGRARION        = "unknown"
    G_NAME_GROUP_CDN_INTEGRARION_GENERAL = "unknown"
else:
    from . import G_NAME_MODULE_CDN_INTEGRARION                   
    from . import G_NAME_GROUP_CDN_INTEGRARION_GENERAL            

########################################################################################################################

class CdnIntegrationConfig:
    """ This class contains configuration that comes from Oscar (Non CLI) """
    def __init__ (self):
        self.logDir = None
        self.confDir = None
        self.historyDir = None
        self.configFile = None
        self.llnwdLogpusherExecutable = None
        # TODO(amiry) - We currently support only one integration. When we support multiple, 
        # mointor-listen-port should become a "base" number for port range
        self.llnwdMonitorListenPort = None
        self.qbNetStateFile = None

        ##############################################################################
        # TODO(amiry) - The below is currently condifured in user papam. should 
        # be configured via profile
        self.llnwdRotationTimeSec = None
        self.llnwdRotationSizeKB = None
        self.llnwdUnsentQueueMaxSizeMB = None        
        self.llnwdSentArchiveMaxSizeGB = None        
        self.llnwdUnsentArchiveMaxSizeGB = None        
        self.llnwdMetaArchiveMaxSizeGB = None        
        self.llnwdForceIfaceToBind = None
        self.llnwdMetaFlushIntervalSec = None
        # Alarms
        self.llnwdLogQueueGettingFullThreshold = None
        self.llnwdClearLogQueueGettingFullThreshold = None
        self.llnwdLogQueueFullThreshold = None
        self.llnwdClearLogQueueFullThreshold = None

########################################################################################################################

class CdnIntegrationManager:

    MAIN_LOOP_INTERVAL = 5

    def __init__ (self):
        self._log = None
        self._wasStopped = False

        # Config
        self._blinkyAgent = None
        self._configDomain = None
        self._operDomain = None
        self._blinkyReporting = None
        self._reportingManager = None
        self._reportingBlinkyAdapter = None

        # Network configuration
        self._netPostListener = None
        self._currIfaceList = {}


    def initLogger (self, logger):
        self._log = logger.createLogger(G_NAME_MODULE_CDN_INTEGRARION, G_NAME_GROUP_CDN_INTEGRARION_GENERAL)


    def initConfig (self, cfg):
        self._cfg = cfg


    def initReportingManager (self):
        self._reportingManager = ReportingManager(self._log, self, self._cfg)


    def attachToBlinky (self, blinkyAgent):
        self._log("attach").debug1("Attach to blinky")

        self._blinkyAgent = blinkyAgent
        self._configDomain = blinkyAgent.createConfigDomain("cdn-integration-manager-config", DomainPriority.kDefault)
        self._operDomain = blinkyAgent.createConfigDomain("cdn-integration-manager-oper", DomainPriority.kDefault)

        # Attach to blinky reporting 
        self._reportingBlinkyAdapter = ReportingBlinkyAdapter(self._log, self._operDomain)
        self._blinkyReporting = BlinkyReporting.s_create(self._log, self._configDomain)
        self._reportingBlinkyAdapter.attachToBlinky(self._blinkyReporting, self._reportingManager)

        # Do registertion
        self._operDomain.registrationDone()
        self._configDomain.registerNode(self._blinkyReporting)
        self._configDomain.registrationDone()
        self._configDomain.triggerSubscriptions()

        # Register on network configuration change notifications using net-client
        self._log("start-config-agent").debug1("Start network configuration agent")
        self._netPostListener = a.sys.net.net_manager.NetPostListener("postconfig", NetConfigNotifier(self._netConfigChanged, self._log))
        self._netPostListener.activate(self._log, self._blinkyAgent)
        self._log("after-listener-activate").debug1("Network configuration agent activated")

    def launch (self):
        self._log("launch").debug1("Launched")

        # Main loop
        while not self._wasStopped:

            self._updateServiceStatus()

            if not self._wasStopped:
                self._reportingManager.watchdog()

            if not self._wasStopped:
                time.sleep(self.MAIN_LOOP_INTERVAL)

        # Cleanup
        self._deattachFromBlinky()
        self._reportingManager.stop()


    def stop (self):
        self._log("stop").debug1("Raising 'wasStopped' flag")
        self._wasStopped = True


    def getIfaceList (self):
        return self._currIfaceList


    def _deattachFromBlinky (self):
        self._log("deattach").debug1("Deattaching from blinky")

        self._netPostListener.shutdown()
        self._log("end-config-agent").info("Shutdown network configuration agent")  
        self._netPostListener = None
        
        self._configDomain.shutdown()
        self._blinkyAgent = None
        return True


    def _netConfigChanged (self, changedIfaceList):

        # First we merge the changed list into the current list
        newIfaceList = self._currIfaceList.copy()

        for changedIfaceName, changedIface in changedIfaceList.items():
            # For each of the changed interfaces, get teh current configuration
            iface = newIfaceList.get(changedIfaceName)

            # If it is not in the current list we add it to the new list.
            if iface is None:
                newIfaceList[changedIfaceName] = changedIface
                # Make sure our iface always have the status feild.
                changedIface["ipv4ServiceStatus"] = False
                continue

            # Now we set the changed values
            currEnable = iface.get("enable")
            currIpv4Address = iface.get("ipv4Address")
            iface["enable"] = changedIface.get("enable", currEnable)
            iface["ipv4Address"] = changedIface.get("ipv4Address", currIpv4Address)

        self._log("config-chenged").debug1("Config changed: %s" % newIfaceList)

        # Now we notify the reporting manager
        self._reportingManager.netConfigChanged(newIfaceList)

        # Finally we copy the new configuration to the current configuration
        self._currIfaceList = newIfaceList.copy()


    def _updateServiceStatus (self):
        try:
            if not os.path.exists(self._cfg.qbNetStateFile):
                self._log("no-state-file").info("No network state file. Skip iface status check. File %s" % self._cfg.qbNetStateFile)
                return

            self._log("service status").debug1("Check service status. Curr iface list %s. File %s" % (self._currIfaceList, self._cfg.qbNetStateFile))

            netState = a.infra.format.json.readFromFile(self._log, self._cfg.qbNetStateFile)
            deliveryInterfaces = netState.get("deliveryInterfaces")
            if deliveryInterfaces is None:
                self._log("qbnet-state-bad-file").error("Wrong data in network state file %s. %s" % (self._cfg.qbNetStateFile, netState))

            changed = False
            for deliveryIface in deliveryInterfaces:
                ifaceName = deliveryIface["interfaceName"]
                ipv4ServiceStatus = deliveryIface["deliveryIPv4State"]["serviceStatus"]
                iface = self._currIfaceList.get(ifaceName)
                if iface:
                    if iface["ipv4ServiceStatus"] != ipv4ServiceStatus:
                        self._log("qbnet-state-chenged").notice("Iface %s changed oper status from %s to %s" %  (ifaceName, iface["ipv4ServiceStatus"], ipv4ServiceStatus))
                        iface["ipv4ServiceStatus"] = ipv4ServiceStatus
                        changed = True

            if changed:
                self._reportingManager.netStatusChanged(self._currIfaceList)

        except Exception as ex:
            self._log("read-qbnet-state-error").error("Error in read network state file %s. %s" % (self._cfg.qbNetStateFile, ex))
        

#-----------------------------------------------------------------------------------------------------------------------

class NetConfigNotifier (a.sys.net.interfaces.client.InterfaceCfgNotifier):

    def __init__(self, notifyFunc, logger):
        data = a.sys.net.interfaces.client.InterfaceDataInfo(
            a.sys.net.interfaces.client.IfDataMembers.kIpAddress,
            a.sys.net.interfaces.client.IfDataMembers.kEnable)
        a.sys.net.interfaces.client.InterfaceCfgNotifier.__init__(self, delivery=data, delivery2=data)
        self._notifyFunc = notifyFunc
        self._log = logger


    def notifyChangeOnInterfaces(self, mng = None, delivery = None, delivery2 = None):
        __pychecker__="no-argsused"  # mng not used

        ifaceList = {}
        if delivery is not None:
            name = delivery[0]
            iface = self.getDeliveryConfigChange(delivery[1])
            ifaceList[name] = iface
            self._log("got-delivery-change").notice("Got delivery iface 1 change notification. %s %s" % (name, iface))

        if delivery2 is not None:
            name = delivery2[0]
            iface = self.getDeliveryConfigChange(delivery2[1])
            ifaceList[name] = iface
            self._log("got-delivery2-change").notice("Got delivery iface 2 change notification. %s %s" % (name, iface))

        if len(ifaceList) > 0:
            self._notifyFunc(ifaceList)


    def getDeliveryConfigChange(self, data):
        iface = {}
        if data.isOn(a.sys.net.interfaces.client.IfDataMembers.kIpAddress):
            iface["ipv4Address"] = data.getByKey(a.sys.net.interfaces.client.IfDataMembers.kIpAddress)
        if data.isOn(a.sys.net.interfaces.client.IfDataMembers.kEnable):
            iface["enable"] = data.getByKey(a.sys.net.interfaces.client.IfDataMembers.kEnable)
        return iface

