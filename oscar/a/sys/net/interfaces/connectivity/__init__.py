# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

import ip_service
from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper

import time
import Queue

G_NAME_GROUP_NET_INTERFACES_CONNECTIVITY = "connectivity"

class ConnectivityCheck(object):
    """This class represents a connectivity check object"""

    def __init__ (self, logger, interfaceName):
        """Instantiate a new content connectivity check object.

        Args:
            logger

        Raises:
            None
        """

        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_INTERFACES_CONNECTIVITY)

        self.interfaceName = interfaceName
        self.ipv4 = None
        self.ipv6 = None

        self.blinkyConnectivityCheck = None

#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        strList = []
        strList.append("ipv4 connectivity: %s" % self.ipv4)
        strList.append("ipv6 connectivity: %s" % self.ipv6)

        return '\t'.join(strList) 

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyConnectivityCheck):

        self._log("notify-attach-blinky").debug2("attach by blinky connectivity check")

        # ipv4
        blinkyConnectivityCheck.setCreateIpv4Functor(self.createIpv4)
        blinkyConnectivityCheck.setDeleteIpv4Functor(self.deleteIpv4)

        # ipv6
        blinkyConnectivityCheck.setCreateIpv6Functor(self.createIpv6)
        blinkyConnectivityCheck.setDeleteIpv6Functor(self.deleteIpv6)

        self.blinkyConnectivityCheck = blinkyConnectivityCheck

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyConnectivityCheck:
            self.blinkyConnectivityCheck.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def createIpv4(self, phase, blinkyIpv4):
        self._log("create-service-ipv4").debug2("phase=%s, blinkyIpv4=%s", phase, blinkyIpv4)

        if (phase.isPreparePrivate()):

            ipv4 = ip_service.Ipv4Connectivity(self._log, self.interfaceName)
            self.ipv4 = SimpleContainerWrapper(self._log, ipv4,
                                               setOperDataFunctor=True)
            self.ipv4.attachToBlinky(blinkyIpv4)

        elif (phase.isCommitPublic()):
            self.ipv4.attachToBlinkyOper()
        elif (phase.isAbortPrivate()):
            self.ipv4 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteIpv4(self, phase):
        self._log("delete-service-ipv4").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.ipv4 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def createIpv6(self, phase, blinkyIpv6):
        self._log("create-service-ipv6").debug2("phase=%s, blinkyIpv6=%s", phase, blinkyIpv6)

        if (phase.isPreparePrivate()):

            ipv6 = ip_service.Ipv6Connectivity(self._log, self.interfaceName)
            self.ipv6 = SimpleContainerWrapper(self._log, ipv6,
                                               setOperDataFunctor=True)
            self.ipv6.attachToBlinky(blinkyIpv6)

        elif (phase.isCommitPublic()):
            self.ipv6.attachToBlinkyOper()
        elif (phase.isAbortPrivate()):
            self.ipv6 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def deleteIpv6(self, phase):
        self._log("delete-service-ipv6").debug2("phase=%s", phase)

        if (phase.isCommitPrivate()):
            self.ipv6 = None

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def actionOnConnectivityCheck(self, osDevice, linkOperStatus, linkAdminStatus, defaultGateway, ipAddress, version=4):
        self._log("action-connectivity-check").debug4("%s: actionOnConnectivityCheck() was called ", self.interfaceName)

        if version == 4 and self.ipv4:
            self.ipv4.testConnectivityCheck(osDevice, linkOperStatus, linkAdminStatus, defaultGateway, ipAddress)
            
        if version == 6 and self.ipv6:
            self.ipv6.testConnectivityCheck(osDevice, linkOperStatus, linkAdminStatus, defaultGateway, ipAddress)  
            
#-----------------------------------------------------------------------------------------------------------------------
    def isConnectivityAvailable(self, version=4):

        isConnectivityAvailable = False

        if version == 4 and self.ipv4:
            isConnectivityAvailable = self.ipv4.isConnectivityAvailable()

        elif version == 6 and self.ipv6:
            isConnectivityAvailable = self.ipv6.isConnectivityAvailable()   

        return isConnectivityAvailable

#-----------------------------------------------------------------------------------------------------------------------
    def getConnectivityReason(self, version=4):

        connectivityReason = None

        if version == 4 and self.ipv4:
            connectivityReason = self.ipv4.getConnectivityReason()

        elif version == 6 and self.ipv6:
            connectivityReason = self.ipv6.getConnectivityReason()   

        return connectivityReason

#-----------------------------------------------------------------------------------------------------------------------
    def setMuteReporting(self, muteReporting):

        if self.ipv4:
            self.ipv4.setMuteReporting(muteReporting)

        if self.ipv6:
            self.ipv6.setMuteReporting(muteReporting)

#----------------------------------------------
class ConnectivityTestContainer(object):
    """a generic connectivity test container object.
    """

    TEST_INTERVAL_MS_RANGE = (1000,60000) 
    TEST_TIMEOUT_MS_RANGE  = (1000,60000) 
    TEST_PERIOD_SEC_RANGE  = (0,60) 

    def __init__(self, logger, name, method=None):
        """
        Args:
            logger

        Raises:
            None
        """

        self._log = logger
        self.name = name
        self.method = method

        # data
        self.testIntervalSec = 1 
        self.testTimeoutSec  = 1  
        self.upPeriodSec     = 10   
        self.downPeriodSec   = 5   

        self.blinkyConnectivityTest = None

#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        strList = []
        strList.append("testIntervalSec=%s" % self.testIntervalSec)
        strList.append("testTimeoutSec=%s"  % self.testTimeoutSec)
        strList.append("upPeriodSec=%s"     % self.upPeriodSec)
        strList.append("downPeriodSec=%s"   % self.downPeriodSec)

        return '\t'.join(strList)

#-----------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyConnectivityTest):
        self.blinkyConnectivityTest = blinkyConnectivityTest

        self._registerOnAttachToBlinky(blinkyConnectivityTest)

#-----------------------------------------------------------------------------------------------------------------------
    def _registerOnAttachToBlinky(self, blinkyConnectivityTest):
        pass

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyConnectivityTest:
            self.blinkyConnectivityTest.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def setActionError(self, userInfo, msg):
        if self.blinkyConnectivityTest:
            self.blinkyConnectivityTest.setActionError(userInfo,msg)

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):

        testInterval = data.testIntervalMsec
        testTimeout  = data.testTimeoutMsec
        upPeriod     = data.upPeriod
        downPeriod   = data.downPeriod

        # test-interval-ms
        if testInterval != 0:
            intervaMin,intervaMax = ConnectivityTestContainer.TEST_INTERVAL_MS_RANGE

            if testInterval < intervaMin or testInterval > intervaMax:
                self._log("test-interval-invalid").error("testInterval '%s' is invalid. must be in range (%s-%s) ",
                                                         testInterval, intervaMin, intervaMax)
                self.setConfigErrorStr("test-interval-msec '%s' is out of range %s-%s" % (testInterval, intervaMin, intervaMax))
                return ReturnCodes.kGeneralError

        # test-timeout-ms
        if testTimeout != 0:
            timeoutMin,timeoutMax = ConnectivityTestContainer.TEST_TIMEOUT_MS_RANGE

            if testTimeout < timeoutMin or testTimeout > timeoutMax:
                self._log("test-timeout-invalid").error("testTimeout '%s' is invalid. must be in range (%s-%s) ",
                                                         testTimeout, timeoutMin, timeoutMax)
                self.setConfigErrorStr("test-timeout-msec '%s' is out of range %s-%s" % (testTimeout, timeoutMin, timeoutMax))
                return ReturnCodes.kGeneralError

        # test-timeout-ms <= test-interval-ms
        if (testInterval > 0) and (testInterval < testTimeout):
            self._log("timeout-greater-than-interval").error("testInterval must be greater/equal to testTimeout, see data: %s", data)
            self.setConfigErrorStr("test-timeout-msec '%s' is greater than test-interval-msec '%s'" % (testTimeout, testInterval))
            return ReturnCodes.kGeneralError

        # up/down periods
        periodMin,periodMax = ConnectivityTestContainer.TEST_PERIOD_SEC_RANGE
        if upPeriod < periodMin or upPeriod > periodMax:
            self._log("test-up-period-invalid").error("upPeriod '%s' is invalid. must be in range (%s-%s) ",upPeriod, periodMin, periodMax)
            self.setConfigErrorStr("up-period '%s' is out of range %s-%s" % (upPeriod, periodMin, periodMax))
            return ReturnCodes.kGeneralError             

        if downPeriod < periodMin or downPeriod > periodMax:
            self._log("test-down-period-invalid").error("downPeriod '%s' is invalid. must be in range (%s-%s) ",downPeriod, periodMin, periodMax)
            self.setConfigErrorStr("down-period '%s' is out of range %s-%s" % (downPeriod, periodMin, periodMax))
            return ReturnCodes.kGeneralError  
            
        # test-interval-ms >= up-period
        if (upPeriod > 0) and ((upPeriod*1000) < testInterval):
            self._log("interval-greater-than-up-period").error("upPeriod must be greater/equal to testInterval, see data: %s", data)
            self.setConfigErrorStr("test-interval '%s' is greater than up-period '%s'" % (testInterval/1000.0, upPeriod))
            return ReturnCodes.kGeneralError  

        # test-interval-ms >= down-period
        if (downPeriod > 0) and ((downPeriod*1000) < testInterval):
            self._log("interval-greater-than-down-period").error("downPeriod must be greater/equal to testInterval, see data: %s", data)
            self.setConfigErrorStr("test-interval '%s' is greater than down-period '%s'" % (testInterval/1000.0, downPeriod))
            return ReturnCodes.kGeneralError  

        # we are successfull 
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):

        # set data
        self.testIntervalSec = (data.testIntervalMsec/1000.0)
        self.testTimeoutSec  = round(data.testTimeoutMsec/1000.0)
        self.upPeriodSec     = data.upPeriod
        self.downPeriodSec   = data.downPeriod

        return ReturnCodes.kOk

#----------------------------------------------
class ConnectivityStatusMonitor(object):
    def __init__(self, logger):
        self._log = logger
        
        self.connectivityTestCfg     = None
        self.currentStatusResult= False
        self.lastStatusResult   = False
        self.statusPeriodSec    = 0
        self.isActive = False

        now = time.time()
        self.lastStatusTime     = now
        self.nextTest           = now

        self.testQueue = Queue.Queue()

#-----------------------------------------------------------------------------------------------------------------------  
    def __str__(self):
        return str(self.connectivityTestCfg)

#-----------------------------------------------------------------------------------------------------------------------
    def setCurrentConnectivityTest(self, connectivityTestCfg):
        if connectivityTestCfg is None:
            # monitoring is inactive
            self._log("no-connectivity-test").error("connectivity test is none")
            return

        self._log("add-connectivity-test").info("%s: add to queue new connectivity test - %s",
                                                connectivityTestCfg.name, connectivityTestCfg)
        self.testQueue.put_nowait(connectivityTestCfg)

#-----------------------------------------------------------------------------------------------------------------------
    def clear(self):
        # status is down
        self.currentStatusResult = False
        self.statusPeriodSec= 0
        self.lastStatusTime = time.time()

        if self.connectivityTestCfg:
            self._log("connectivity-clear").debug1("%s: connectivity cleared back to down", self.connectivityTestCfg.name)

#-----------------------------------------------------------------------------------------------------------------------
    def oneTick(self):

        try:
            connectivityTestCfg = self.testQueue.get(block=True, timeout=0.1)
            newConf = True                
        except Queue.Empty:
            newConf = False

        # handle new configuration
        if newConf:
            self.connectivityTestCfg = connectivityTestCfg

            self._log("get-connectivity-test").info("%s: get from queue new connectivity test - %s",
                                                      connectivityTestCfg.name, connectivityTestCfg)
            self.isActive = True

#-----------------------------------------------------------------------------------------------------------------------
    def shouldTest(self):
        if self.isActive is False:
            return False

        now = time.time()
        shouldTest = (now >= self.nextTest)

        # prepare interval for next test
        if shouldTest is True:
            self.nextTest += self.connectivityTestCfg.testIntervalSec

            # in case was not called more than test interval secs
            if self.nextTest < now:
                self.nextTest = now + self.connectivityTestCfg.testIntervalSec

        self._log("should-test").debug4("%s: should test - %s (current=%s, next=%s)",
                                        self.connectivityTestCfg.name, shouldTest, now, self.nextTest)

        return shouldTest

#-----------------------------------------------------------------------------------------------------------------------
    def getTestMethod(self, default=None):
        if self.connectivityTestCfg is None:
            return default

        return self.connectivityTestCfg.method

#-----------------------------------------------------------------------------------------------------------------------
    def addTestResult(self, newTestResult):
        # in case test was changed between the calls of shouldTest() and addTestResult()
        if self.isActive is False:
            return

        currentStatusTime = time.time()

        if self.currentStatusResult == newTestResult:
            # no change in connectivity check
            self.statusPeriodSec   = 0
        else:
            self._log("connectivity-check-change").debug2("%s: detected connectivity single check changed to %s", 
                                                          self.connectivityTestCfg.name, newTestResult)
            self.statusPeriodSec += (currentStatusTime-self.lastStatusTime)

            if newTestResult is True:
                # status should change to up
                if self.statusPeriodSec >= self.connectivityTestCfg.upPeriodSec:
                    self.currentStatusResult = True
                    self.statusPeriodSec   = 0
                    self._log("connectivity-check-down").debug1("%s: connectivity changed to up", self.connectivityTestCfg.name)
            else:
                # status should change to down
                if self.statusPeriodSec >= self.connectivityTestCfg.downPeriodSec:
                    self.currentStatusResult = False
                    self.statusPeriodSec   = 0
                    self._log("connectivity-check-up").debug1("%s: connectivity changed to down", self.connectivityTestCfg.name)

        # prepare status timestamp
        self.lastStatusTime = currentStatusTime
        
#-----------------------------------------------------------------------------------------------------------------------
    def isConnectivityAvailable(self):
        return self.currentStatusResult
