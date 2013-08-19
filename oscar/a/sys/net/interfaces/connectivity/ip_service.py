# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.enum_with_value import EnumWithValue
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper
from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import ConnectivityCheckIpv4MethodType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import ConnectivityCheckIpv6MethodType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.counters.counters_oper_data_gen import CountersOperData as Ipv4CountersOperData
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv6.counters.counters_oper_data_gen import CountersOperData as Ipv6CountersOperData
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import ConnectivityOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import ConnectivityOperationalStatusReasonType

from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.status.blinky_status_oper_gen import BlinkyOperStatus as Ipv4BlinkyOperStatus
from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.counters.blinky_counters_oper_gen import BlinkyOperCounters as Ipv4BlinkyOperCounters
from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv6.status.blinky_status_oper_gen import BlinkyOperStatus as Ipv6BlinkyOperStatus
from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv6.counters.blinky_counters_oper_gen import BlinkyOperCounters as Ipv6BlinkyOperCounters

import a.sys.net.lnx.device
import a.sys.net.lnx.neighbour
import a.sys.net.lnx.route
import a.infra.process
import a.api.user_log.msg.net

G_NAME_GROUP_NET_INTERFACES_CONNECTIVITY_IP = "ipv%s-connectivity"

#################
# IP CONNECTIVITY   
#################
#-----------------------------------------------------------------------------------------------------------------------
class _BaseIpConnectivity(object):
    """a generic base connectivity object.
    """

    def __init__(self, logger, interfaceName, version, ipMethodMap, counters):
        """
        Args:
            logger

        Raises:
            None
        """

        self.interfaceName = interfaceName
        self.version = version
        self.ipMethodMap = ipMethodMap # maps blinky ip version method type specific enum to a generic
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_INTERFACES_CONNECTIVITY_IP % version)

        # data
        self.candidateMethod = MethodTypes.kMethodLink
        self.runningMethod   = MethodTypes.kMethodLink
        self.ndisc = None
        self.ping = None
        self.muteReporting = False

        # dummy
        self.link = a.sys.net.interfaces.connectivity.ConnectivityTestContainer(self._log, 
                                                                               "%s-link%s" % (self.interfaceName, self.version),
                                                                                MethodTypes.kMethodLink) 
        self.countersOnClear = counters

        # status
        self.connectivityOperStatus = None
        self.operStatusReason = ConnectivityOperationalStatusReasonType.kInterfaceFunctionsDoesNotRequireConnectivityCheck
        self.actualMethod   = None

        # counters
        self.numNdiscSuccessfulTests= 0
        self.numNdiscTimeouts       = 0
        self.numNdiscErrors         = 0
        self.numPingSuccessfulTests = 0
        self.numPingTimeouts        = 0
        self.numPingErrors          = 0
        
        # connectivity availability
        self.connectivityStatusMonitor = a.sys.net.interfaces.connectivity.ConnectivityStatusMonitor(self._log)
        
        self.blinkyIpConnectivity = None

#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        return "%s-ipv%s: ndisc=%s , ping=%s" % (self.interfaceName, self.version, self.ndisc, self.ping)

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyIpConnectivity):
        self.blinkyIpConnectivity = blinkyIpConnectivity

        # clear-counters
        blinkyIpConnectivity.setDoActionFunctor(self.doActionClearCounters)

        self._registerOnAttachToBlinky(blinkyIpConnectivity)

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyIpConnectivity:
            self.blinkyIpConnectivity.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def setOperErrorStr(self, tctx, msg):
        if self.blinkyIpConnectivity is not None:
            self.blinkyIpConnectivity.setTransError(tctx, msg)

#-----------------------------------------------------------------------------------------------------------------------
    def doActionClearCounters(self, userInfo, actionPoint, actionName, params, nParams):
        self._log("do-action-clear-counters").debug2('called. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s', 
                                                     userInfo, actionPoint, actionName, params, nParams)

        rc = self._doClearCounters()
        
        if rc != ReturnCodes.kOk:
            self.blinkyIpConnectivity.setActionError(userInfo, '%s: failed on ipv%s connectivity clear counters', self.interfaceName, self.version)

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def _doClearCounters(self):
        rc = self._getConnectivityCounters(None, self.countersOnClear, False)
        self._log("do-clear-counters").debug2("%s: clear counters snapshot - %s", self.interfaceName, self.countersOnClear)

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        self._log("prepare-private-value-set").debug2("%s: ipv%s prepare data - %s", self.interfaceName, self.version, data)

        method = self.ipMethodMap.get(data.method, None)

        if method is None:
            self._log("candidate-method-invalid").error("Candidate IPv%s method type '%s' is invalid. see valid options: %s ", 
                                                        self.version, data.method, self.ipMethodMap)
            self.setConfigErrorStr("ipv%s method type '%s' is invalid" % (self.version, data.method))
            return ReturnCodes.kGeneralError

        # we are successfull 
        self.candidateMethod = method
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        __pychecker__="no-argsused"  # data not used
        self._log("commit-private-value-set").debug2("%s: ipv%s commit data - %s", self.interfaceName, self.version, data)

        self.runningMethod = self.candidateMethod

        # update connectivity monitor
        currentConnectivity = self.link

        # arp/ndisc6
        if self.runningMethod == MethodTypes.kMethodNeighDisc:
            currentConnectivity = self.ndisc
        # ping/ping6
        elif self.runningMethod == MethodTypes.kMethodPing:
            currentConnectivity = self.ping

        self.connectivityStatusMonitor.setCurrentConnectivityTest(currentConnectivity) 
        self._log("ip-connectivity-check-change").info("ipv%s connectivity check is going to be %s", self.version, self.runningMethod)      
        
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        __pychecker__="no-argsused"  # data not used

        self.candidateMethod = self.runningMethod
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getStatus(self, tctx, operData):

        self._log("ip-connectivity-availability-status").debug3("ipv%s connectivity availability: get status was called. tctx=%s", self.version, tctx)

        operStatusMap = {True  : ConnectivityOperationalStatusType.kUp,
                         False : ConnectivityOperationalStatusType.kDown,
                         None  : ConnectivityOperationalStatusType.kNotApplicable}
        # set data
        operData.setOperationalStatus(operStatusMap.get(self.connectivityOperStatus,ConnectivityOperationalStatusType.kUnknown))
        operData.setOperationalStatusReason(self.operStatusReason)

        if self.actualMethod is not None:
            for method in self.ipMethodMap:
                if self.ipMethodMap[method] == self.actualMethod:
                    operData.setActualMethod(method)
                    break


        self._log("ip-connectivity-status-results").debug3("ipv%s connectivity availability: status results=%s", self.version, operData)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getCounters(self, tctx, operData):

        rc = self._getConnectivityCounters(tctx, operData, True)
        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def _getConnectivityCounters(self, tctx, operData, shouldUseClear):
        self._log("ip-connectivity-availability-counters").debug3("ipv%s connectivity availability: get counters was called. tctx=%s", self.version, tctx)

        # set counters
        operData.setPingRequestsSent(self.numPingSuccessfulTests + self.numPingTimeouts + self.numPingErrors)
        operData.setPingSuccesses(self.numPingSuccessfulTests)
        operData.setPingTimeouts(self.numPingTimeouts)
        operData.setPingFailures(self.numPingErrors)

        self._setNdiscCounters(operData)

        # substract counters on clear
        if shouldUseClear is True :
            self._log("connectivity-counters-original-data").debug4("%s: get original counters oper data=%s", self.interfaceName, operData)

            for key, value in self.countersOnClear.__dict__.iteritems():
                if type(value) is int:
                    operData.__dict__[key]  -= value

        self._log("ip-connectivity-counters-results").debug3("ipv%s connectivity availability: counters results=%s", self.version, operData)

        return ReturnCodes.kOk


#-----------------------------------------------------------------------------------------------------------------------
    def createNeighDisc(self, phase, blinkyNdisc):
        self._log("create-neigh-disc").debug2("phase=%s, ipv%s blinkyNdisc=%s", phase, self.version, blinkyNdisc)

        if (phase.isPreparePrivate()):

            if self.version == 4:
                testName = "arp"
            else:
                testName = "ndisc6"

            ndisc = a.sys.net.interfaces.connectivity.ConnectivityTestContainer(self._log, 
                                                                                "%s-%s" % (self.interfaceName, testName),
                                                                                MethodTypes.kMethodNeighDisc)
            self.ndisc = SimpleContainerWrapper(self._log, ndisc)
            self.ndisc.attachToBlinky(blinkyNdisc)

        elif (phase.isAbortPrivate()):
            self.ndisc = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteNeighDisc(self, phase):
        self._log("delete-neigh-disc").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.ndisc = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createPing(self, phase, blinkyPing):
        self._log("create-ping").debug2("phase=%s, ipv%s blinkyPing=%s", phase, self.version, blinkyPing)

        if (phase.isPreparePrivate()):

            ping = a.sys.net.interfaces.connectivity.ConnectivityTestContainer(self._log, 
                                                                               "%s-ping%s" % (self.interfaceName, self.version),
                                                                               MethodTypes.kMethodPing)
            self.ping = SimpleContainerWrapper(self._log, ping)
            self.ping.attachToBlinky(blinkyPing)

        elif (phase.isAbortPrivate()):
            self.ping = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deletePing(self, phase):
        self._log("delete-ping").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.ping = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def testConnectivityDone(self, connectivityOperStatus, operStatusReason, actualMethod):

        currentConnectivityOperStatus = self.connectivityOperStatus

        # set data
        self.connectivityOperStatus = connectivityOperStatus
        self.operStatusReason       = operStatusReason
        self.actualMethod           = actualMethod
        
        # ConnectivityTestChange @ user-log
        if self.connectivityOperStatus != currentConnectivityOperStatus:
            self._logUserConnectivityTestChangeMessage()
        
        # we are done
        self.connectivityStatusMonitor.clear()

#-----------------------------------------------------------------------------------------------------------------------
    def testConnectivityCheck(self, osDevice, linkOperStatus, linkAdminStatus, defaultGateway, ipAddress):

        self._log("ip-connectivity-test").debug3("%s: testConnectivityCheck() ipv%s was called - device=%s, oper-status=%s",
                                                         self.interfaceName, self.version, osDevice, linkOperStatus)

        if not osDevice:
            a.infra.process.processFatal("%s: connectivity test ipv%s has no os device associated", self.interfaceName, self.version)


        self._log("ip-connectivity-data").debug4("%s: testConnectivityCheck() ipv%s was called with configuration- admin-status=%s, default-gateway=%s, ip-address=%s",
                                                 self.interfaceName, self.version, linkAdminStatus, defaultGateway, ipAddress)

        # -----------------------------------------
        # phase 1: prepare for connectivity check
        # -----------------------------------------

        # admin-down --> 
        #  - oper-status:   n/a
        #  - actual-method: disabled
        if linkAdminStatus is False:
            self._log("connectivity-admin-down").debug3("%s: connectivity test ipv%s admin is down", self.interfaceName, self.version)
            self.testConnectivityDone(None, ConnectivityOperationalStatusReasonType.kInterfaceAdministrativelyDown, None)
            return

        # no ip address --> 
        #  - oper-status:   n/a
        #  - actual-method: disabled
        if not ipAddress:
            self._log("connectivity-no-ip").debug3("%s: connectivity test ipv%s has no ip", self.interfaceName, self.version)
            self.testConnectivityDone(None, ConnectivityOperationalStatusReasonType.kInterfaceHasNoIpAddress, None)
            return 


        # -----------------------------------------
        # phase 2: choose actual connectivity check
        # -----------------------------------------

        self.connectivityStatusMonitor.oneTick()
        method = self.connectivityStatusMonitor.getTestMethod(default=MethodTypes.kMethodLink)
        self._log("connectivity-method-test-config").debug3("%s: configured connectivity test ipv%s - method=%s", self.interfaceName, self.version, method)

        # no default gateway (no ping/arp/ndisc)
        if not defaultGateway:
            self._log("connectivity-no-default-gateway").debug3("%s: connectivity test ipv%s has no defaultGateway", self.interfaceName, self.version)
            method = MethodTypes.kMethodLink

        # link is down (no ping/arp/ndisc)
        operStateStr = a.sys.net.lnx.device.DeviceUtils.getOperState(osDevice, self._log, osDevice)
        linkCurrentStatus = (operStateStr == "up")
        if linkCurrentStatus is False and linkOperStatus is False:
            self._log("connectivity-oper-down").debug3("%s: connectivity test ipv%s link oper is down", self.interfaceName, self.version)
            method = MethodTypes.kMethodLink

        # -----------------------------------------
        # phase 3: link check
        # -----------------------------------------
        
        isConnectivityAvailable = False
        downOperStatusReason = ConnectivityOperationalStatusReasonType.kUnknown
        self._log("connectivity-method-test-running").debug3("%s: running connectivity test ipv%s - method=%s", self.interfaceName, self.version, method)

        # link 
        if method == MethodTypes.kMethodLink:
           
            operStatusReason = ConnectivityOperationalStatusReasonType.kSuccess
            if linkOperStatus is False:
                operStatusReason = ConnectivityOperationalStatusReasonType.kLinkOperationalStatusDown               

            self.testConnectivityDone(linkOperStatus, operStatusReason, MethodTypes.kMethodLink)
            return

        # -----------------------------------------
        # phase 4: execute connectivity check
        # -----------------------------------------
        if self.connectivityStatusMonitor.shouldTest() is False:
            return

        self._log("connectivity-test-run").debug3("%s: going to run connectivity test ipv%s - method=%s", self.interfaceName, self.version, method)

        # arp/ndisc (link is up by now)
        if method == MethodTypes.kMethodNeighDisc:

            if self.ndisc.testIntervalSec == 0:
                # assumes arp/ndisc was successful
                isConnectivityAvailable = True
            elif linkCurrentStatus is False:
                # assumes arp/ndisc was failure
                isConnectivityAvailable = False
                rc = (1,)
            else:
                rc = self._sendNeighDiscRequest(osDevice, defaultGateway)
                isConnectivityAvailable = a.sys.net.lnx.common.Command.isReturnOk(rc)
                self._log("connectivity-ndisc-test").debug2("%s: test arp/ndisc ipv%s rc=%s", self.interfaceName, self.version, rc)

            # arping return code: 
            # 0 - Sent 2 probes (1 broadcast(s)) Received 2 response(s)
            # 1 - Sent 2 probes (1 broadcast(s)) Received 0 response(s)
            # 2 - unknown host / unknown iface / etc.
            if isConnectivityAvailable is True:
                self.numNdiscSuccessfulTests += 1
            else:
                if rc[0] != 1:
                    self.numNdiscErrors += 1
                    self._log("connectivity-ndisc-error").debug1("%s: test arp/ndisc ipv%s error=%s", self.interfaceName, self.version, rc[2])
                else:
                    self.numNdiscTimeouts += 1

            # set arp/ndisc down reason
            # note: even if arp/ndsic was successfull for a single test, we might still be in the up-period

            if linkOperStatus is False:
                downOperStatusReason = ConnectivityOperationalStatusReasonType.kLinkOperationalStatusDown
            else:
                if self.version == 4:
                    downOperStatusReason = ConnectivityOperationalStatusReasonType.kArpTestFailure
                else:
                    downOperStatusReason = ConnectivityOperationalStatusReasonType.kNeighborDiscoveryTestFailure

        # ping/ping6 (link is up by now)
        elif method == MethodTypes.kMethodPing:

            if self.ping.testIntervalSec == 0:
                # assumes ping/ping6 was successful
                isConnectivityAvailable = True
            elif linkCurrentStatus is False:
                # assumes ping/ping6 was failure
                isConnectivityAvailable = False
                rc = (1,)
            else:
                rc = self._sendPing(osDevice, defaultGateway)
                isConnectivityAvailable = a.sys.net.lnx.common.Command.isReturnOk(rc)
                self._log("connectivity-ping-test").debug4("%s: test ping ipv%s rc=%s", self.interfaceName, self.version, rc)

            # ping return code: 
            # 0 - 1 packets transmitted, 1 received, 0% packet loss
            # 1 - 1 packets transmitted, 0 received, 100% packet loss
            # 2 - unknown host / bad number of packets to transmit / etc.
            if isConnectivityAvailable is True:
                self.numPingSuccessfulTests += 1
            else:
                if rc[0] != 1:
                    self.numPingErrors += 1
                    self._log("connectivity-ping-error").debug1("%s: test ping ipv%s error=%s", self.interfaceName, self.version, rc[2])
                else:
                    self.numPingTimeouts += 1

            # set ping down reason
            # note: even if ping was successfull for a single test, we might still be in the up-period
            if linkOperStatus is False:
                downOperStatusReason = ConnectivityOperationalStatusReasonType.kLinkOperationalStatusDown
            else:
                downOperStatusReason = ConnectivityOperationalStatusReasonType.kPingTestFailure

        else:

            isConnectivityAvailable = False
            downOperStatusReason = ConnectivityOperationalStatusReasonType.kUnknown
            self._log("connectivity-unknown-test").error("%s: unknown ipv%s test method type - %s" , self.interfaceName, self.version, method)


        # update connectivity monitor (ran one of the tests ping/arp/ndisc by now)
        self.connectivityStatusMonitor.addTestResult(isConnectivityAvailable)
        currentConnectivityOperStatus = linkOperStatus and self.connectivityStatusMonitor.isConnectivityAvailable()

        self._log("connectivity-test-results").debug3("%s: ipv%s connectivity availability results is '%s' (method=%s)",
                                                 self.interfaceName, self.version, currentConnectivityOperStatus, self.actualMethod)

        if currentConnectivityOperStatus is True:
            currentOperStatusReason = ConnectivityOperationalStatusReasonType.kSuccess
        else:
            currentOperStatusReason = downOperStatusReason

        shouldUserLog = False

        # update oper status reason
        if self.operStatusReason != currentOperStatusReason:
            self._log("connectivity-reason-change").notice("%s: ipv%s connectivity reason changed to %s",
                                                           self.interfaceName, self.version, currentOperStatusReason)
            self.operStatusReason = currentOperStatusReason
            shouldUserLog = True

        # update oper status (if needed)
        if self.connectivityOperStatus != currentConnectivityOperStatus:
            self._log("connectivity-stats-change").notice("%s: ipv%s connectivity status changed to %s",
                                                          self.interfaceName, self.version, currentConnectivityOperStatus)
            self.connectivityOperStatus = currentConnectivityOperStatus 
            shouldUserLog = True

        # update actual method
        self.actualMethod = method

        if shouldUserLog is True:
            # ConnectivityTestChange @ user-log
            self._logUserConnectivityTestChangeMessage()

#-----------------------------------------------------------------------------------------------------------------------
    def _logUserConnectivityTestChangeMessage(self):
        # mute user-log
        if self.muteReporting is True:
            return

        operStatusMap = {True  : "up", 
                         False : "down",
                         None  : "not applicable"}

        operReasonMap = {ConnectivityOperationalStatusReasonType.kLinkOperationalStatusDown         : "link operational status down",
                         ConnectivityOperationalStatusReasonType.kInterfaceFunctionsDoesNotRequireConnectivityCheck : "interface functions does not require connectivity check",
                         ConnectivityOperationalStatusReasonType.kInterfaceHasNoIpAddress           : "interface has no ip address",
                         ConnectivityOperationalStatusReasonType.kArpTestFailure                    : "arp test failure",
                         ConnectivityOperationalStatusReasonType.kPingTestFailure                   : "ping test failure",
                         ConnectivityOperationalStatusReasonType.kNeighborDiscoveryTestFailure      : "neighbor discovery test failure",
                         ConnectivityOperationalStatusReasonType.kInterfaceAdministrativelyDown     : "interface administratively down",
                         ConnectivityOperationalStatusReasonType.kSuccess                           : "success"}

        state = operStatusMap.get(self.connectivityOperStatus,"unknown")
        reason = operReasonMap.get(self.operStatusReason,"unknown")


        # ConnectivityTestChange @ user-log
        a.infra.process.logUserMessage(a.api.user_log.msg.net.ConnectivityTestChange(self.interfaceName, 
                                                                                     "IPv%s" % self.version,
                                                                                     state, 
                                                                                     reason)) 

#-----------------------------------------------------------------------------------------------------------------------
    def isConnectivityAvailable(self):
        if self.connectivityOperStatus is True:
            return True

        return False

#-----------------------------------------------------------------------------------------------------------------------
    def getConnectivityReason(self):
        return self.operStatusReason

#-----------------------------------------------------------------------------------------------------------------------
    def setMuteReporting(self, muteReporting):
        self._log("connectivity-mute-reporting").info("%s: ipv%s connectivity mute reporting was changed to %s",
                                                      self.interfaceName, self.version, muteReporting)
        self.muteReporting = muteReporting

#-----------------------------------------------------------------------------------------------------------------------
    def _sendNeighDiscRequest(self, device, destination):
        raise NotImplementedError

#-----------------------------------------------------------------------------------------------------------------------
    def _sendPing(self, device, destination):
        return a.sys.net.lnx.route.Ping.ping(self._log, 
                                             destination,
                                             source=device,
                                             version=self.version,
                                             count=1,
                                             timeout=self.ping.testTimeoutSec,
                                             blocking=(self.ping.testTimeoutSec>0))

#-----------------------------------------------------------------------------------------------------------------------
    def _registerOnAttachToBlinky(self, blinkyIpConnectivity):
        raise NotImplementedError

#-----------------------------------------------------------------------------------------------------------------------
    def _setNdiscCounters(self, operData):
        raise NotImplementedError

#############
# IPv4
#############
#-----------------------------------------------------------------------------------------------------------------------
class Ipv4Connectivity(_BaseIpConnectivity):
    """IPv4 connectivity object.
    """

    def __init__(self, logger, interfaceName):
        """
        Args:
            logger

        Raises:
            None
        """

        ipv4MethodMap = {ConnectivityCheckIpv4MethodType.kLink : MethodTypes.kMethodLink,
                         ConnectivityCheckIpv4MethodType.kArp  : MethodTypes.kMethodNeighDisc,
                         ConnectivityCheckIpv4MethodType.kPing : MethodTypes.kMethodPing}

        ipv4Counters = Ipv4CountersOperData()

        _BaseIpConnectivity.__init__(self, logger, interfaceName, 4, 
                                     ipv4MethodMap, ipv4Counters)

#-----------------------------------------------------------------------------------------------------------------------
    def _sendNeighDiscRequest(self, device, destination):
        return a.sys.net.lnx.neighbour.Arping.sendArpRequest(self._log, 
                                                             device, 
                                                             destination,
                                                             count=1,
                                                             timeout=self.ndisc.testTimeoutSec,
                                                             firstReply=True,
                                                             blocking=(self.ndisc.testTimeoutSec>0))

#-----------------------------------------------------------------------------------------------------------------------
    def _registerOnAttachToBlinky(self, blinkyIpConnectivity):

        # arp
        blinkyIpConnectivity.setCreateArpFunctor(self.createNeighDisc)
        blinkyIpConnectivity.setDeleteArpFunctor(self.deleteNeighDisc)
    
        # ping
        blinkyIpConnectivity.setCreatePingFunctor(self.createPing)
        blinkyIpConnectivity.setDeletePingFunctor(self.deletePing)

#-----------------------------------------------------------------------------------------------------------------------
    def _setNdiscCounters(self, operData):

        operData.setArpRequestsSent(self.numNdiscSuccessfulTests + self.numNdiscTimeouts + self.numNdiscErrors)
        operData.setArpSuccesses(self.numNdiscSuccessfulTests)
        operData.setArpTimeouts(self.numNdiscTimeouts)
        operData.setArpFailures(self.numNdiscErrors)

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperStatusObj (self):
        return Ipv4BlinkyOperStatus(self._log)

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperCountersObj (self):
        return Ipv4BlinkyOperCounters(self._log)


#############
# IPv6
#############
#-----------------------------------------------------------------------------------------------------------------------
class Ipv6Connectivity(_BaseIpConnectivity):
    """IPv6 connectivity object.
    """

    def __init__(self, logger, interfaceName):
        """
        Args:
            logger

        Raises:
            None
        """

        ipv6MethodMap = {ConnectivityCheckIpv6MethodType.kLink                : MethodTypes.kMethodLink,
                         ConnectivityCheckIpv6MethodType.kNeighborDiscovery   : MethodTypes.kMethodNeighDisc,
                         ConnectivityCheckIpv6MethodType.kPing                : MethodTypes.kMethodPing}
        ipv6Counters = Ipv6CountersOperData()

        _BaseIpConnectivity.__init__(self, logger, interfaceName, 6, 
                                     ipv6MethodMap, ipv6Counters)


#-----------------------------------------------------------------------------------------------------------------------
    def _sendNeighDiscRequest(self, device, destination):
        return a.sys.net.lnx.neighbour.Ndisc.sendNdiscRequest(self._log,
                                                              device,
                                                              destination,
                                                              count=1,
                                                              timeout=self.ndisc.testTimeoutSec,
                                                              firstReply=True,
                                                              blocking=(self.ndisc.testTimeoutSec>0))

#-----------------------------------------------------------------------------------------------------------------------
    def _registerOnAttachToBlinky(self, blinkyIpConnectivity):

        # ndisc6
        blinkyIpConnectivity.setCreateNeighborDiscoveryFunctor(self.createNeighDisc)
        blinkyIpConnectivity.setDeleteNeighborDiscoveryFunctor(self.deleteNeighDisc)
    
        # ping6
        blinkyIpConnectivity.setCreatePingFunctor(self.createPing)
        blinkyIpConnectivity.setDeletePingFunctor(self.deletePing)

#-----------------------------------------------------------------------------------------------------------------------
    def _setNdiscCounters(self, operData):

        operData.setNeighborDiscoveryRequestsSent(self.numNdiscSuccessfulTests + self.numNdiscTimeouts + self.numNdiscErrors)
        operData.setNeighborDiscoverySuccesses(self.numNdiscSuccessfulTests)
        operData.setNeighborDiscoveryTimeouts(self.numNdiscTimeouts)
        operData.setNeighborDiscoveryFailures(self.numNdiscErrors)

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperStatusObj (self):
        return Ipv6BlinkyOperStatus(self._log)

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperCountersObj (self):
        return Ipv6BlinkyOperCounters(self._log)

#----------------------------------------------
class Method(EnumWithValue):
    """contains a single data member"""
    def __init__ (self, value, name):
        EnumWithValue.__init__(self, value, name)

class MethodTypes(object):
    """ optional data members """
    kMethodLink          = Method(0, "kMethodLink")
    kMethodNeighDisc     = Method(1, "kMethodNeighDisc")
    kMethodPing          = Method(2, "kMethodPing")
