 # Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.infra.basic.return_codes import ReturnCodes
from a.sys.net.lnx.device import DeviceUtils
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper
from a.infra.misc.enum_with_value import EnumWithValue
from a.sys.net.interfaces.connectivity import ConnectivityTestContainer
from a.sys.net.interfaces.connectivity import ConnectivityStatusMonitor
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.link.counters.counters_oper_data_gen import CountersOperData as LinkCountersOperData
from a.sys.net.tech_interfaces.tech.interfaces.interface.link.counters.blinky_counters_oper_gen import BlinkyOperCounters
import a.infra.process
import a.api.user_log.msg.net

G_NAME_GROUP_NET_INTERFACES_LINK = "link"

#-----------------------------------------------------------------------------------------------------------------------
class Link(ConnectivityTestContainer):
    """This object displays the network device link status.
    """
    def __init__(self, logger, interface):
        """
        Args:
            logger

        Raises:
            None
        """

        self.parent = interface

        # status
        self.linkOperStatus = False
        self.linkStatusMonitor = ConnectivityStatusMonitor(logger)

        # counters
        self.numLinkSuccessfulTests = 0
        self.numLinkErrors = 0
        self.numLinkFailures = 0
        self.linkStatusChangeCount = 0
        self.countersOnClear = LinkCountersOperData()

        ConnectivityTestContainer.__init__(self, logger, "%s-link" % self.parent.name)

        # update link monitor
        self.linkStatusMonitor.setCurrentConnectivityTest(self)
        self.linkStatusMonitor.oneTick()

#-----------------------------------------------------------------------------------------------------------------------
    def _registerOnAttachToBlinky(self, blinkyConnectivityTest):

        # clear-counters
        blinkyConnectivityTest.setDoActionFunctor(self.doActionClearCounters)

#-----------------------------------------------------------------------------------------------------------------------
    def doActionClearCounters(self, userInfo, actionPoint, actionName, params, nParams):
        self._log("do-action-clear-counters").debug2('called. userInfo=%s, actionPoint=%s, actionName=%s, params=%s, nParams=%s', 
                                                     userInfo, actionPoint, actionName, params, nParams)

        rc = self._doClearCounters()
        
        if rc != ReturnCodes.kOk:
            self.setActionError(userInfo, '%s: failed on link connectivity clear counters' % self.name)

        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def _doClearCounters(self):
        rc = self._getLinkCounters(None, self.countersOnClear, False)
        self._log("do-clear-counters").debug2("%s: clear counters snapshot - %s", self.name, self.countersOnClear)

        return rc
                        
#-----------------------------------------------------------------------------------------------------------------------
    def testLinkAvailability(self):

        self._log("link-availability-test").debug4("testLinkAvailability() was called - interface=%s", self.parent.name)

        if self.linkStatusMonitor.shouldTest() is False:
            return

        isLinkUp = None

        if self.testIntervalSec == 0:
            # assumes link is up
            isLinkUp = True
        else:

            isLinkUp = self.parent.isLinkUp()
            
            if self.testTimeoutSec == 0:
                # ran test, but assumes link is up
                isLinkUp = True

            self._log("connectivity-link-test").debug4("%s: test link rc=%s", self.parent.name, isLinkUp)

        # update counters
        if isLinkUp is True:
            self.numLinkSuccessfulTests += 1
        elif isLinkUp is False:
            self.numLinkFailures += 1
        else:
            self.numLinkErrors += 1

        # update test 
        self.linkStatusMonitor.addTestResult(isLinkUp)
        currentLinkOperStatus = self.linkStatusMonitor.isConnectivityAvailable() 
        
        # update oper status
        if self.linkOperStatus != currentLinkOperStatus:
            self._log("link-oper-change").notice("%s: link status changed to %s", self.parent.name, currentLinkOperStatus)
            self.linkStatusChangeCount += 1
            self.linkOperStatus = currentLinkOperStatus

            # state up/down/admin-down
            adminStatus = self.parent.runningEnabled
            state = StateTypes.kUp

            if self.linkOperStatus is not True:
                if adminStatus is False:
                    state = StateTypes.kAdminDOwn
                else:
                    state = StateTypes.kDown
            
            if self.parent.muteReporting is True:
                return # mute user-log and snmp traps

            # LinkUpDown @ user-log
            a.infra.process.logUserMessage(a.api.user_log.msg.net.LinkUpDown(self.parent.name, state)) 

            # send link snmp trap
            self.sendSnmpTrap()

#-----------------------------------------------------------------------------------------------------------------------
    def isLinkUp(self):
        if self.linkOperStatus is True:
            return True

        return False

#-----------------------------------------------------------------------------------------------------------------------
    def sendSnmpTrap(self):

        snmpTrapsManager = self.parent.snmpTrapsManager
        if snmpTrapsManager is None:
            return

        mibIfIndex = self.parent.mibIfIndex
        if self.isLinkUp() is True:
            snmpTrapsManager.sendLinkUpTrap(mibIfIndex)
        else:
            snmpTrapsManager.sendLinkDownTrap(mibIfIndex)

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperCountersObj (self):
        return BlinkyOperCounters(self._log)

#-----------------------------------------------------------------------------------------------------------------------
    def getCounters(self, tctx, operData):

        rc = self._getLinkCounters(tctx, operData, True)
        return rc

#-----------------------------------------------------------------------------------------------------------------------
    def _getLinkCounters(self, tctx, operData, shouldUseClear):

        self._log("link-availability-counters").debug3("link availability: get counters was called. tctx=%s", tctx)

        # set counters
        operData.setTests(self.numLinkSuccessfulTests + self.numLinkFailures + self.numLinkErrors)
        operData.setResultUp(self.numLinkSuccessfulTests)
        operData.setResultDown(self.numLinkFailures)
        operData.setResultUnknown(self.numLinkErrors)

        # substract counters on clear
        if shouldUseClear is True :
            self._log("link-counters-original-data").debug4("%s: get original counters oper data=%s", self.name, operData)

            for key, value in self.countersOnClear.__dict__.iteritems():
                if type(value) is int:
                    operData.__dict__[key]  -= value

        self._log("link-counters-results").debug3("link availability: counters results=%s", operData)
        return ReturnCodes.kOk


#----------------------------------------------
class State(EnumWithValue):
    """contains a single data member"""
    def __init__ (self, value, name):
        EnumWithValue.__init__(self, value, name)

class StateTypes(object):
    """ optional data members """
    kDown       = State(0, "down")
    kUp         = State(1, "up")
    kAdminDOwn  = State(2, "administratively down")
    kUnknown    = State(3, "unknown")
