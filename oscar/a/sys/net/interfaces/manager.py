# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

from a.sys.net.interfaces import IfContainerBase
from a.infra.basic.return_codes import ReturnCodes
from a.sys.net.lnx.ssh import SshdConfigFile
from a.sys.blinky.trx_phase import TrxPhase
from a.sys.blinky.trx_progress import TrxProgress
from a.sys.net.tech_interfaces.tech.interfaces.status.blinky_status_oper_gen import BlinkyOperStatus as BlinkyOperIfMngrStatus

##############################################
# This class manages the network configuration
##############################################
class IfManager(IfContainerBase):
    """This class manages the network configuration"""

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger, name, allowDynamicConfig, lineNicsFile, snmpTrapsManager):

        IfContainerBase.__init__(self, logger, name, True, allowDynamicConfig, lineNicsFile, snmpTrapsManager)
        self.allowDynamicConfig = allowDynamicConfig
       
        # network configuration files
        self.sshdCfgFile = None
       
#-----------------------------------------------------------------------------------------------------------------------
    def initData(self, sshPort):
        self._log("init-data").debug3("Init data: sshPort=%s", sshPort)
        self.sshdCfgFile = SshdConfigFile(self._log, sshPort)  
            
#-----------------------------------------------------------------------------------------------------------------------
    def _attachToBlinkyIfList(self, blinkyInterfaceList):
        self._log("attach-blinky-interface-manager").debug2("attach to blinky: %s", blinkyInterfaceList)

        # change default timeout for commit-private-after 
        # Note: sshd restart takes ~170 mili
        commitPrivatePhase = TrxPhase(TrxPhase.kCommit, TrxPhase.kPrivate)
        commitPrivateAfterProgress = TrxProgress(commitPrivatePhase, TrxProgress.kAfter)
        blinkyInterfaceList.setFunctorTimeoutForProgress(blinkyInterfaceList.TRX_PROGRESS_FUNCTOR, commitPrivateAfterProgress, 1000)

        rc = IfContainerBase._attachToBlinkyIfList(self, blinkyInterfaceList) 

        return rc  

#-----------------------------------------------------------------------------------------------------------------------
    def attachToBlinkyOper(self):

        # get status functor
        self._log("get-blinky-oper-status-obj").debug1("creating BlinkyOperIfMngrStatus on %s", self.blinkyInterfaceList)
        blinkyOperObj = BlinkyOperIfMngrStatus(self._log)

        blinkyOperObj.setConfigObj(self.blinkyInterfaces)
        blinkyOperObj.setDomain(self.blinkyInterfaces.getDomain())
        blinkyOperObj.setBasicFunctors(self.getStatus)
        rc = blinkyOperObj.activate()
        if (rc != ReturnCodes.kOk):
            self._log("attach-to-blinky-oper-activate-status-failed").error("blinkyOperObj.activate() failed. blinkyOperObj=%s", blinkyOperObj)
            # not failing the transaction in commit phase
            return

#-----------------------------------------------------------------------------------------------------------------------
    def getStatus(self, tctx, operData):

        self._log("if-manager-status").debug3("if-manager: get status was called. tctx=%s", tctx)

        interfaces = self.interfaceList.runningValues()

        operData.setInterfaceNumber(len(interfaces))
        operData.setTableLastChangeTicks(0)

        self._log("if-manager-status-data").debug3("if-manager: get status oper data=%s. interfaces=%s", operData, interfaces)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateAfter(self):
        """all interfaces are being evaluated and verified for correctness system-wise"""

        self._log("manager-prepare-private-after").debug3("preparePrivateAfter was called")

        interfaces = self.interfaceList.candidateValues()

        i=0

        mngIf = None
        techIf = None
        deliveryIfMap = {}

        for currentI in interfaces:
            i+=1
            currentName = currentI.deviceName()
           
            if self.allowDynamicConfig:
                for otherI in interfaces[i:]:
                    otherName = otherI.deviceName()
    
                    if not (currentName is None or otherName is None):
                        # check if interfaces device not the same
                        if currentName == otherName:
                            self._log("device-duplicate").notice("Device is duplicated: %s vs. %s", currentI, otherI)
                            self.setConfigErrorStr("Interfaces %s and %s have the same OS name %s" % 
                                                   (currentI.name, otherI.name, currentName))
                            return ReturnCodes.kGeneralError

            if currentI.isManagementEnabled() is True:
                if currentI.candidateTechMode:
                    self._log("manager-tech-interface").debug3("%s: tech interface detected", currentI.name)

                    if techIf is None:
                        techIf = currentI
                    else:
                        self._log("tech-interface-duplicate").notice("%s: tech interface %s was already configured", 
                                                                    currentI.name, techIf.name)
                        self.setConfigErrorStr("Interfaces %s and %s both were configured as tech" % 
                                               (currentI.name, techIf.name))
                        return ReturnCodes.kGeneralError

                else:
                    self._log("manager-mng-interface").debug3("%s: management interface detected", currentI.name)

                    if mngIf is None:
                        mngIf = currentI
                    else:
                        self._log("mng-interface-duplicate").notice("%s: management interface %s was already configured", 
                                                                    currentI.name, mngIf.name)
                        self.setConfigErrorStr("Interfaces %s and %s both were configured as management" % 
                                               (currentI.name, mngIf.name))
                        return ReturnCodes.kGeneralError

            elif currentI.isDeliveryEnabled():
                self._log("manager-delivery-interface").debug3("%s: delivery interface detected", currentI.name)
                deliveryIfMap[currentI.name] = currentI

        # must have exactly 2 delivery interfaces
        if len(deliveryIfMap) > 2:
            self._log("delivery-interface-invalid").notice("Invalid number of delivery interfaces were configured - %s", deliveryIfMap.keys())
            self.setConfigErrorStr("Must configure exactly 2 delivery Interfaces. '%s' - all were configured as delivery" % 
                                   deliveryIfMap.keys())
            return ReturnCodes.kGeneralError

        # delivery interfaces cannot have the same source IP address
        if len(deliveryIfMap) == 2:
            delivery2 = deliveryIfMap.popitem()[1]
            delivery1 = deliveryIfMap.popitem()[1]

            if delivery1.equals(delivery2) is True:
                self._log("delivery-src-ips").notice("Delivery interfaces addresses are equal: %s vs. %s", delivery1.name, delivery2.name)
                self.setConfigErrorStr("Delivery interfaces %s and %s addresses are identical" % (delivery1.name, delivery2.name))
                return ReturnCodes.kGeneralError  
                
        # management interface subnet does not overlap with tech
        if not ((mngIf is None) or (techIf is None)):
            if mngIf.overlaps(techIf) is True:
                self._log("mng-tech-overlap").notice("Management interfaces subnets overlap: %s vs. %s", mngIf.name, techIf.name)
                self.setConfigErrorStr("Management interfaces %s and %s subnets overlap" % (mngIf.name, techIf.name))
                return ReturnCodes.kGeneralError       

        # prepare configuration files
        self.prepareConfigFiles(mngIf, techIf)

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def prepareConfigFiles(self, mngIf, techIf):

        # clear data
        self.sshdCfgFile.clear()
           
        if not mngIf is None:
            ip = mngIf.getIpAddress()
            if ip: self.sshdCfgFile.addIpAddress(str(ip))
  
        if not techIf is None: 
            ip = techIf.getIpAddress()
            if ip: self.sshdCfgFile.addIpAddress(str(ip))

        # dump data
        if self.allowDynamicConfig:
            self.sshdCfgFile.dumpData()

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateAfter(self):

        self._log("manager-commit-private-after").debug3("commitPrivateAfter was called")

        if self.allowDynamicConfig:
            self.sshdCfgFile.commit()

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateAfter(self):

        self._log("manager-abort-private-after").debug3("abortPrivateAfter was called")

        if self.allowDynamicConfig:
            self.sshdCfgFile.abort()

        return ReturnCodes.kOk


