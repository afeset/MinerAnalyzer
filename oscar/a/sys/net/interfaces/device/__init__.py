 # Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.infra.basic.return_codes import ReturnCodes
from a.sys.hardware.pci import PciHal
from a.sys.net.lnx.device import DeviceUtils
from a.sys.net.lnx.device import EthTool
from a.sys.net.interfaces.oper.line_nic import LineNicStats
from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import DeviceCountersClearEventType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.counters.counters_oper_data_gen import CountersOperData
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.device.status.status_oper_data_gen import StatusOperData
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import DriverTypeType
from a.sys.net.tech_interfaces.tech.interfaces.interface.device.counters.blinky_counters_oper_gen import BlinkyOperCounters
from a.sys.net.tech_interfaces.tech.interfaces.interface.device.status.blinky_status_oper_gen import BlinkyOperStatus
from a.sys.net.interfaces.ip import IpVersion
from a.infra.misc.timeout_guard import TimeoutGuard
import a.sys.net.lnx.neighbour
import a.infra.process
import a.sys.net.lnx
import time
import subprocess

G_NAME_GROUP_NET_INTERFACES_DEVICE = "device"

#-----------------------------------------------------------------------------------------------------------------------
class Device(object):
    """A generic IP network device object.
    """
    TIMEOUT_MILI_SEC = 100 # 100 mili seconds

    def __init__(self, logger, interface=None):
        """
        Args:
            logger

        Raises:
            None
        """

        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_INTERFACES_DEVICE)
        self.candidateOsName = None
        self.runningOsName = None
        self.pciAddress = None
        self.candidatePciIndex = None
        self.runningPciIndex   = None
        self.countersClearEvent= DeviceCountersClearEventType.kNone
        self.parent=interface
        self.isFirstTrx = True
        self.operStatus=False
        self.countersOnClear = CountersOperData()
        self.pciHelper = PciHal(self._log)

        if self.pciHelper.init() is not True:
            a.infra.process.processFatal("PciHal init failed")
        
        # cmd configuration tweaks
        self.postInitCommand= None
        self.postUpCommand  = None
        self.postDownCommand= None

        # counters oper data cache
        self.countersOperData = CountersOperData()
        self.countersLastUpdateTime = time.time()
        self.sentGratuitousArpCount = 0
        self.sentGratuitousNdisc6Count = 0
        self.operStatusChangeCount  = 0

        # status oper data cache
        self.statusOperData = StatusOperData()
        self.statusLastUpdateTime = time.time()

        self.blinkyDevice = None

#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):     
        return str("%s/%s" % (self.runningOsName, self.pciAddress)) 

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyDevice):

        # clear-counters
        if self.parent.isActiveModule is True:
            blinkyDevice.setDoActionFunctor(self.doActionClearCounters)

        self.blinkyDevice = blinkyDevice

#-----------------------------------------------------------------------------------------------------------------------
    def doActionClearCounters (self, userInfo, actionPoint, actionName, params, nParams):
        self._log("do-action-clear-counters").debug2('called. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s', 
                                                     userInfo, actionPoint, actionName, params, nParams)

        rc = self._doClearCounters()
        
        if rc != ReturnCodes.kOk:
            self.blinkyDevice.setActionError(userInfo, '%s: failed on device clear counters', self.runningOsName)

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def _doClearCounters(self):

        counters = CountersOperData()
        rc = self.getCounters(None, counters)
        
        if rc != ReturnCodes.kOk:
            return rc

        for key, value in counters.__dict__.iteritems():
            if type(value) is int:
                self.countersOnClear.__dict__[key]  += value

        self._log("do-clear-counters").debug2("%s: clear counters snapshot - %s", self.runningOsName, self.countersOnClear)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyDevice:
            self.blinkyDevice.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):

        self._log("prepare-private-value-set").debug4("Device: prepare data - %s", data)

        if (len(data.pciVendorId) == 0) and (len(data.pciDeviceId) == 0) and (data.pciIndex == 0) and (len(data.osName) == 0):
            # empty container
            return ReturnCodes.kOk

        # 3 tuple per device
        vendorid = data.pciVendorId
        deviceid = data.pciDeviceId
        pciIndex = data.pciIndex

        # validate required parameters 
        if len(vendorid) == 0:
            self._log("pci-vendor-id-missing").error("no pci vendor id: %s", data)
            self.setConfigErrorStr("PCI Vendor id is missing")
            return ReturnCodes.kGeneralError

        if len(deviceid) == 0:
            self._log("pci-device-id-missing").error("no pci device id: %s", data)
            self.setConfigErrorStr("PCI Device id is missing")
            return ReturnCodes.kGeneralError

        if pciIndex < 0:
            self._log("bad-pci-index").error("bad pci index: %s", data)
            self.setConfigErrorStr("Bad PCI Index")
            return ReturnCodes.kGeneralError
        
        # get a pci device address by vendorId, deviceId and index
        deviceIdList = [int(deviceIdStr,16) for deviceIdStr in deviceid.split('|')]
        pciAddress = self.pciHelper.getDevicePciAddressByDeviceIdList(int(vendorid,16), deviceIdList, pciIndex)
        if pciAddress is None and self.parent.allowDynamicConfig:
            if len(data.osName) != 0:
                self._log("bad-device-params-error").error("no device with the given parameters: %s", data)
                self.setConfigErrorStr("Bad device parameters")
                return ReturnCodes.kGeneralError
            else:
                # in qvm-30 virutal pci device does not exist
                self._log("bad-device-params-warn").info("no device with the given parameters: %s", data)


        osName = None
        if self.parent is not None and self.parent.allowDynamicConfig is True:

            if pciAddress is not None:
                osName = DeviceUtils.getEthDeviceByPciAddress(pciAddress)

            # os device name is optional
            if len(data.osName) != 0:
                if ((data.osName != osName) and (DeviceUtils.isDeviceExists(data.osName) is True)):
                    self._log("os-name-duplicate").error("OS name '%s' already exists in a another device", data.osName)
                    self.setConfigErrorStr("OS name %s is in use" % data.osName)
                    return ReturnCodes.kGeneralError
        else:
            osName = data.osName
            if DeviceUtils.isDeviceExists(data.osName) is False:
                self._log("os-name-not-exist").error("OS name '%s' does not exist in machine", data.osName)
                self.setConfigErrorStr("OS name %s does not exist" % data.osName)
                return ReturnCodes.kGeneralError

        # we are successfull and can copy the data 
        # the os name holds the prior data until rename and commit
        self.candidateOsName = data.osName
        self.candidatePciIndex = data.pciIndex
        self.runningOsName = osName
        self.pciAddress = pciAddress
        
        self._log("actual-device-data").debug2("Device Name=%s , PCI Address=%s", self.runningOsName, self.pciAddress)


        if self._validateCommand(data.osName, "post-init-command", data.postInitCommand) != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        if self._validateCommand(data.osName, "post-up-command", data.postUpCommand) != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        if self._validateCommand(data.osName, "post-down-command", data.postDownCommand) != ReturnCodes.kOk:
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk
#-----------------------------------------------------------------------------------------------------------------------
    def _validateCommand(self, device, name, command):
        if command:
            if command.find("%(device)s") == -1:
                self._log("device-command-bad-syntax").error("device %s: %s command has invalid syntax - %s",device, name, command)
                self.setConfigErrorStr("OS device %s command %s syntax error" % (device, name))
                return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def shouldRename(self):
        if self.candidateOsName:
            return (self.runningOsName != self.candidateOsName)

        return False

#-----------------------------------------------------------------------------------------------------------------------
    def rename(self):
          
        self._log("rename-device").debug2("rename device from %s to %s", self.runningOsName, self.candidateOsName)

        # Note: device must be down
        rc = a.sys.net.lnx.device.IpLink.renameDevice(self._log, self.runningOsName, self.candidateOsName)
        self.runningOsName = self.candidateOsName

        if not a.sys.net.lnx.common.Command.isReturnOk(rc):
            a.infra.process.processFatal("%s: Device rename action failed", str(self))

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        __pychecker__="no-argsused"  # data not used

        # set commands
        self.postInitCommand= data.postInitCommand
        self.postUpCommand  = data.postUpCommand
        self.postDownCommand= data.postDownCommand

        if self.isFirstTrx is True:               
            if self.parent.isActiveModule is True:
                # first transaction commit
                rc = self._doClearCounters()
            
                if rc != ReturnCodes.kOk:
                    self._log("device-counters-on-start-fail").error("%s: failed retrieve rx and tx counters on start",
                                                                     self.runningOsName)

                self.actionOnInit()

            self.isFirstTrx = False

        # set data
        self.runningPciIndex = self.candidatePciIndex
        self.countersClearEvent = data.countersClearEvent

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        __pychecker__="no-argsused"  # data not used

        self.candidateOsName = self.runningOsName

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def actionOnInit(self):
        device = self.runningOsName

        if DeviceUtils.isDeviceExists(device) is True:
            self.runCommand(device, self.postInitCommand)

#-----------------------------------------------------------------------------------------------------------------------
    def actionOnStatusChange(self):
        device = self.runningOsName

        if DeviceUtils.isDeviceExists(device) is True:
            
            # operational status
            operStatusStr = DeviceUtils.getOperState(device, self._log, device)

            if "up" == operStatusStr:
                currentOperStatus = True
            else:
                currentOperStatus = False

            if self.operStatus != currentOperStatus:
                self.operStatus = currentOperStatus
                self._log("device-status-change").notice("%s: oper status was changed to %s", device, self.operStatus)
                self.operStatusChangeCount += 1 # update counter

                if self.operStatus is True:
                    self.runCommand(device, self.postUpCommand)

                    # send gratuitous arp on linux up change
                    self.sendGratuitousArp("oper up")
                else:
                    self.runCommand(device, self.postDownCommand)

#-----------------------------------------------------------------------------------------------------------------------
    def sendGratuitousArp(self, actionDesc):
        device = self.runningOsName

        if (self.parent.shouldSendGratuitousArp is True) and DeviceUtils.isDeviceExists(device):

            if self.parent.hasAddress(IpVersion.kIPv4):
                ipv4 = self.parent.getIpAddress(IpVersion.kIPv4)

                self._log("send-gratuitous-arp-ipv4").info("%s-%s: send a gratuitous arp reply for ipv4 address '%s'", 
                                                           device, actionDesc, ipv4)
                self.sentGratuitousArpCount += 1 # update counter
    
                a.sys.net.lnx.neighbour.Arping.sendArpReply(self._log, device, str(ipv4), count=3, blocking=False)

            if self.parent.hasAddress(IpVersion.kIPv6):
                ipv6 = self.parent.getIpAddress(IpVersion.kIPv6)

                self._log("send-gratuitous-ndisc-ipv6").info("%s-%s: send a gratuitous ndisc reply for ip address '%s'", 
                                                           device, actionDesc, ipv6)
                self.sentGratuitousNdisc6Count += 1 # update counter

                a.sys.net.lnx.neighbour.Ndisc.sendRdiscReply(self._log, device, str(ipv6), count=3, blocking=False)

#-----------------------------------------------------------------------------------------------------------------------
    def runCommand(self, device, command):
        self._log("device-cmd-info").debug2("%s: called run command line '%s'", device, command)

        if command:
            # command syntax contains %(device)s
            command = command % {'device': device}

            self._log("device-cmd-run").debug2("%s: execute command line '%s'", device, command)
            subprocess.Popen(command, shell=True)

#-----------------------------------------------------------------------------------------------------------------------
    def setOperErrorStr(self, tctx, msg):
        if self.blinkyDevice and tctx:
            self.blinkyDevice.setTransError(tctx, msg)

#-----------------------------------------------------------------------------------------------------------------------
    def getLineNicData(self):

        lineNicStats = LineNicStats(self._log, self.parent.name, self.parent.lineNicsFile)

        data = None
        if self.runningPciIndex is not None:
            data = lineNicStats.getNicData(self.runningPciIndex-2)

        return data

#-----------------------------------------------------------------------------------------------------------------------
    def getOsCounters(self, tctx, operData):
        if self.runningOsName is not None:
            self._log("eth-tool-show-statistics").debug3("%s: show ethernet card statistics", self.runningOsName)
           
            timeoutGuard = TimeoutGuard(self._log, '%s-show-eth-statistics' % (self.runningOsName), Device.TIMEOUT_MILI_SEC)
            rc = EthTool.showEthStatistics(self._log, self.runningOsName)
            timeoutGuard.checkAndLog(EthTool.showEthStatistics)
    
            if not a.sys.net.lnx.common.Command.isReturnOk(rc):
                self._log("device-fail").error("%s: failed getting ethernet card statistics", self.runningOsName)
                self.setOperErrorStr(tctx, "cannot get counters information: operation not permitted")
                return ReturnCodes.kGeneralError

            output = rc[1].splitlines()
            unsupportedFields = []

            counterToSetDict = { "rx_pkts_nic":         operData.setRxPktsNic,
                                 "tx_pkts_nic":         operData.setTxPktsNic,
                                 "rx_bytes_nic":        operData.setRxBytesNic,
                                 "tx_bytes_nic":        operData.setTxBytesNic,
                                 "lsc_int":             operData.setLscInt,
                                 "tx_busy":             operData.setTxBusy,
                                 "non_eop_descs":       operData.setNonEopDescs,
                                 "rx_no_buffer_count":  operData.setRxNoBufferCount,
                                 "collisions":          operData.setCollisions,
                                 "rx_over_errors":      operData.setRxOverErrors,
                                 "rx_crc_errors":       operData.setRxCrcErrors,
                                 "rx_frame_errors":     operData.setRxFrameErrors,
                                 "hw_rsc_aggregated":   operData.setHwRscAggregated,
                                 "hw_rsc_flushed":      operData.setHwRscFlushed,
                                 "fdir_match":          operData.setFdirMatch,
                                 "fdir_miss":           operData.setFdirMiss,
                                 "rx_fifo_errors":      operData.setRxFifoErrors,
                                 "rx_missed_errors":    operData.setRxMissedErrors,
                                 "tx_aborted_errors":   operData.setTxAbortedErrors,
                                 "tx_carrier_errors":   operData.setTxCarrierErrors,
                                 "tx_fifo_errors":      operData.setTxFifoErrors,
                                 "tx_heartbeat_errors": operData.setTxHeartbeatErrors,
                                 "tx_timeout_count":    operData.setTxTimeoutCount,
                                 "tx_restart_queue":    operData.setTxRestartQueue,
                                 "rx_long_length_errors":operData.setRxLongLengthErrors,
                                 "rx_short_length_errors":operData.setRxShortLengthErrors,
                                 "tx_flow_control_xon": operData.setTxFlowControlXon,
                                 "rx_flow_control_xon": operData.setRxFlowControlXon,
                                 "tx_flow_control_xoff":operData.setTxFlowControlXoff,
                                 "rx_flow_control_xoff":operData.setRxFlowControlXoff,
                                 "rx_csum_offload_errors":operData.setRxCsumOffloadErrors,
                                 "alloc_rx_page_failed":operData.setAllocRxPageFailed,
                                 "alloc_rx_buff_failed":operData.setAllocRxBuffFailed,
                                 "rx_no_dma_resources": operData.setRxNoDmaResources,
                                 "fcoe_bad_fccrc":      operData.setFcoeBadFccrc,
                                 "rx_fcoe_dropped":     operData.setRxFcoeDropped,
                                 "rx_fcoe_packets":     operData.setRxFcoePackets,
                                 "rx_fcoe_dwords":      operData.setRxFcoeDwords,
                                 "tx_fcoe_packets":     operData.setTxFcoePackets,
                                 "tx_fcoe_dwords":      operData.setTxFcoeDwords
                                 }    

            # set eth tool counters
            for line in output[1:]:

                (key, value) = line.split(":",1)
                key = key.strip()
                value = value.strip()
    
                self._log("device-new-field").debug4("%s: set new field - %s", self.runningOsName, key)               
                setFunctor = counterToSetDict.get(key,None) 
  
                if setFunctor is not None:
                    intValue = int(value)
                    setFunctor(intValue)
                    self._log("device-set-field").debug4("%s: set field - %s=%s", self.runningOsName, key, intValue)
                else:
                    unsupportedFields.append(key)

            if len(unsupportedFields) > 0:
                self._log("device-field-unsupported").debug2("%s: contains unsupported fields - %s", 
                                                               self.runningOsName, 
                                                               unsupportedFields)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getLineCounters(self, tctx, operData):
        __pychecker__="no-argsused"  # tctx not used

        data = self.getLineNicData()

        if data is not None:
            counters = data[LineNicStats.KEY_LINE_COUNTERS]

            operData.setRxLongLengthErrors(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_ERRORS_GIANTS, 0))
            operData.setRxMissedErrors(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_ERRORS_MISSED, 0))
            operData.setRxCrcErrors(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_ERRORS_CRC, 0))
            operData.setRxFrameErrors(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_ERRORS_LEN, 0))
            operData.setRxShortLengthErrors(counters.get(LineNicStats.KEY_LINE_COUNTERS_RX_ERRORS_RUNTS, 0))

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperCountersObj (self):
        return BlinkyOperCounters(self._log)

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperStatusObj (self):
        return BlinkyOperStatus(self._log)

#-----------------------------------------------------------------------------------------------------------------------
    def getCounters(self, tctx, operData):

        self._log("device-counters").debug3("device %s: get counters was called. tctx=%s", self.runningOsName, tctx)

        if (time.time()-self.countersLastUpdateTime) < 1: # less than 1 sec
            # read from cache
            operData.copyDataFrom(self.countersOperData)
            self._log("device-counters-results-cache").debug3("device %s: counters results=%s", self.runningOsName, operData)
            return ReturnCodes.kOk
        
        if self.parent.isLineEnabled():
            rc = self.getLineCounters(tctx, operData)
        else:
            timeoutGuard = TimeoutGuard(self._log, '%s-get-os-counters' % (self.runningOsName), Device.TIMEOUT_MILI_SEC)
            rc = self.getOsCounters(tctx, operData) 
            timeoutGuard.checkAndLog(self.getOsCounters)

        if rc != ReturnCodes.kOk:
            self._log("device-get-counters-fail").debug3("%s: failed retrieve device counters", self.runningOsName)
            return ReturnCodes.kGeneralError

            # substract counters on clear
        if self.isFirstTrx is False:
            self._log("device-counters-original-data").debug4("%s: get original counters oper data=%s", self.runningOsName, operData)

            for key, value in self.countersOnClear.__dict__.iteritems():
                if type(value) is int:
                    operData.__dict__[key]  -= value

        # cache the counters
        self.countersLastUpdateTime = time.time()
        self.countersOperData.copyDataFrom(operData)

        self._log("device-counters-results").debug3("device %s: counters results=%s", self.runningOsName, operData)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getStatus(self, tctx, operData):

        self._log("device-status").debug3("device %s: get status was called. tctx=%s", self.runningOsName, tctx)

        timeDelta = time.time()-self.statusLastUpdateTime
        if timeDelta < 1: # less than 1 sec
            # read from cache
            operData.copyDataFrom(self.statusOperData)
            self._log("device-status-data-cache").debug3("%s: get status oper data=%s", self.runningOsName, operData)
            return ReturnCodes.kOk

        # driver type
        driverType = self.parent.getDriverType(True)
        
        if driverType is not None:
            statusToEnum = { "os": DriverTypeType.kOs, 
                             "dpdk": DriverTypeType.kDedicated, 
                             "jake": DriverTypeType.kVirtual
                             }

            operData.setDriverType(statusToEnum.get(driverType,
                                                    DriverTypeType.kNone))

        # PCI address
        if self.pciAddress is not None:
            operData.setPciAddress(self.pciAddress)

        # route table id
        tableid = self.parent.tableid
        if tableid is not None:
            operData.setRouteTableId(tableid)

        # cache the status
        self.statusLastUpdateTime = time.time()
        self.statusOperData.copyDataFrom(operData)

        self._log("device-status-results").debug3("device %s: status results=%s", self.runningOsName, operData)
        return ReturnCodes.kOk
