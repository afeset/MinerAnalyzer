


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyContainer
__pychecker__="no-classattr"

from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.timeout_guard import TimeoutGuard
import a.infra.process.captain
from a.sys.blinky.blinky_container import BlinkyContainer
from a.sys.blinky.trx_phase import TrxPhase
from a.sys.confd.pyconfdlib import pyconfdlib
from a.sys.confd.pyconfdlib.key_path import KeyPath
from a.sys.confd.pyconfdlib.value import Value
import copy

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.system_defaults_data_gen import SystemDefaultsData


from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.content.blinky_content_gen import BlinkyContent

from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.blinky_connectivity_check_gen import BlinkyConnectivityCheck

from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.management.blinky_management_gen import BlinkyManagement

from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.link.blinky_link_gen import BlinkyLink

from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.device.blinky_device_gen import BlinkyDevice




class BlinkySystemDefaults(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
    #leaves
    
    ourXmlTagConfigurationDelay="configuration-delay"
    
    ourXmlTagMuteReporting="mute-reporting"
    
    ourXmlTagSendGratuitousArp="send-gratuitous-arp"
    
    ourXmlTagShutdown="shutdown"
    
    ourXmlTagTechMode="tech-mode"
    

    #descendants
    
    ourXmlTagContent="content"
    
    ourXmlTagConnectivityCheck="connectivity-check"
    
    ourXmlTagManagement="management"
    
    ourXmlTagLink="link"
    
    ourXmlTagDevice="device"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    CONTENT_CREATE_FUNCTOR = 'CONTENT_CREATE_FUNCTOR'
    CONTENT_DELETE_FUNCTOR = 'CONTENT_DELETE_FUNCTOR'
    
    CONNECTIVITYCHECK_CREATE_FUNCTOR = 'CONNECTIVITYCHECK_CREATE_FUNCTOR'
    CONNECTIVITYCHECK_DELETE_FUNCTOR = 'CONNECTIVITYCHECK_DELETE_FUNCTOR'
    
    MANAGEMENT_CREATE_FUNCTOR = 'MANAGEMENT_CREATE_FUNCTOR'
    MANAGEMENT_DELETE_FUNCTOR = 'MANAGEMENT_DELETE_FUNCTOR'
    
    LINK_CREATE_FUNCTOR = 'LINK_CREATE_FUNCTOR'
    LINK_DELETE_FUNCTOR = 'LINK_DELETE_FUNCTOR'
    
    DEVICE_CREATE_FUNCTOR = 'DEVICE_CREATE_FUNCTOR'
    DEVICE_DELETE_FUNCTOR = 'DEVICE_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateContentFunctor=None
        self.myDeleteContentFunctor=None
        self.myContent=None
        
        self.myCreateConnectivityCheckFunctor=None
        self.myDeleteConnectivityCheckFunctor=None
        self.myConnectivityCheck=None
        
        self.myCreateManagementFunctor=None
        self.myDeleteManagementFunctor=None
        self.myManagement=None
        
        self.myCreateLinkFunctor=None
        self.myDeleteLinkFunctor=None
        self.myLink=None
        
        self.myCreateDeviceFunctor=None
        self.myDeleteDeviceFunctor=None
        self.myDevice=None
        
        self.myValueSetFunctor=None
        self.myCandidateData=None
        self.myRunningData=None
        self.isInDestroy = False
        
        self.validateRegistrationDone = False
        self.actionRegistrationDone=False
        
        

    @classmethod
    def s_create (cls, logger, 
                  
                  
                  
                  interface, 
                  
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkysystemdefaults').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkySystemDefaults._validationPointId, BlinkySystemDefaults._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(interface);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interfaces", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkySystemDefaults(logger)
        logger("s-create-keypath").info("confd_key=%s", confd_key)
        newNode.setParent(None)
        newNode.setKeyPath(confd_key)
        newNode.setDomain(domain)
        res = newNode.internalInit()
        if (res != ReturnCodes.kOk):
            logger("s-create-internal-init-failed")\
                .error("internalInit() failed. confd_key=%s", confd_key)

        if newNode._validationPointId:
            res = domain.registerValidationPoint(newNode._validationPointId, newNode)
            if (res != ReturnCodes.kOk):
                logger("s-create-register-validation-node--failed")\
                    .error("registerValidationNode(%s) failed",  newNode._validationPointId)
                return None
        newNode.validateRegistrationDone = True
        if newNode._actionPointId:
            res = domain.registerActionPoint(newNode._actionPointId, newNode)
            if (res != ReturnCodes.kOk):
                logger("s-create-register-action-node--failed")\
                    .error("registerActionNode(%s) failed",  newNode._actionPointId)
                return None
        newNode.actionRegistrationDone = True

        return newNode

    
    def setCreateContentFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-content-functor-active").errorFunc():
                logFunc("setCreateContentFunctor() is illegal when blinky node is active")
        self.myCreateContentFunctor = functor

    def setDeleteContentFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-content-functor-active").errorFunc():
                logFunc("setDeleteContentFunctor() is illegal when blinky node is active")
        self.myDeleteContentFunctor = functor
    
    def setCreateConnectivityCheckFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-connectivity-check-functor-active").errorFunc():
                logFunc("setCreateConnectivityCheckFunctor() is illegal when blinky node is active")
        self.myCreateConnectivityCheckFunctor = functor

    def setDeleteConnectivityCheckFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-connectivity-check-functor-active").errorFunc():
                logFunc("setDeleteConnectivityCheckFunctor() is illegal when blinky node is active")
        self.myDeleteConnectivityCheckFunctor = functor
    
    def setCreateManagementFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-management-functor-active").errorFunc():
                logFunc("setCreateManagementFunctor() is illegal when blinky node is active")
        self.myCreateManagementFunctor = functor

    def setDeleteManagementFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-management-functor-active").errorFunc():
                logFunc("setDeleteManagementFunctor() is illegal when blinky node is active")
        self.myDeleteManagementFunctor = functor
    
    def setCreateLinkFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-link-functor-active").errorFunc():
                logFunc("setCreateLinkFunctor() is illegal when blinky node is active")
        self.myCreateLinkFunctor = functor

    def setDeleteLinkFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-link-functor-active").errorFunc():
                logFunc("setDeleteLinkFunctor() is illegal when blinky node is active")
        self.myDeleteLinkFunctor = functor
    
    def setCreateDeviceFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-device-functor-active").errorFunc():
                logFunc("setCreateDeviceFunctor() is illegal when blinky node is active")
        self.myCreateDeviceFunctor = functor

    def setDeleteDeviceFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-device-functor-active").errorFunc():
                logFunc("setDeleteDeviceFunctor() is illegal when blinky node is active")
        self.myDeleteDeviceFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConfigurationDelay)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.configurationDelay = newValue.asUint64()
                self.myCandidateData.setHasConfigurationDelay()
                
            else:
                self.setConfigurationDelayDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMuteReporting)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.muteReporting = newValue.asBool()
                self.myCandidateData.setHasMuteReporting()
                
            else:
                self.setMuteReportingDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSendGratuitousArp)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.sendGratuitousArp = newValue.asBool()
                self.myCandidateData.setHasSendGratuitousArp()
                
            else:
                self.setSendGratuitousArpDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagShutdown)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.shutdown = newValue.asBool()
                self.myCandidateData.setHasShutdown()
                
            else:
                self.setShutdownDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTechMode)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.techMode = newValue.asBool()
                self.myCandidateData.setHasTechMode()
                
            else:
                self.setTechModeDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagContent)):
            return self.myContent
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagConnectivityCheck)):
            return self.myConnectivityCheck
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagManagement)):
            return self.myManagement
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagLink)):
            return self.myLink
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagDevice)):
            return self.myDevice
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkysystemdefaults').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagContent)):
                    keyPathRegistered = BlinkyContent.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagConnectivityCheck)):
                    keyPathRegistered = BlinkyConnectivityCheck.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagManagement)):
                    keyPathRegistered = BlinkyManagement.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagLink)):
                    keyPathRegistered = BlinkyLink.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagDevice)):
                    keyPathRegistered = BlinkyDevice.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagConfigurationDelay)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMuteReporting)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagSendGratuitousArp)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagShutdown)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagTechMode)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkysystemdefaults-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagContent)):
            if (self.myContent):
                for logFunc in self._log("prepare-my-blinky-node-content-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myContent = BlinkyContent(self._log)
            self.myContent.setParent(self)
            self.myContent.setKeyPath(keyPath)
            self.myContent.setDomain(self.myDomain)

            return self.myContent
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConnectivityCheck)):
            if (self.myConnectivityCheck):
                for logFunc in self._log("prepare-my-blinky-node-connectivitycheck-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myConnectivityCheck = BlinkyConnectivityCheck(self._log)
            self.myConnectivityCheck.setParent(self)
            self.myConnectivityCheck.setKeyPath(keyPath)
            self.myConnectivityCheck.setDomain(self.myDomain)

            return self.myConnectivityCheck
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagManagement)):
            if (self.myManagement):
                for logFunc in self._log("prepare-my-blinky-node-management-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myManagement = BlinkyManagement(self._log)
            self.myManagement.setParent(self)
            self.myManagement.setKeyPath(keyPath)
            self.myManagement.setDomain(self.myDomain)

            return self.myManagement
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLink)):
            if (self.myLink):
                for logFunc in self._log("prepare-my-blinky-node-link-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myLink = BlinkyLink(self._log)
            self.myLink.setParent(self)
            self.myLink.setKeyPath(keyPath)
            self.myLink.setDomain(self.myDomain)

            return self.myLink
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDevice)):
            if (self.myDevice):
                for logFunc in self._log("prepare-my-blinky-node-device-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myDevice = BlinkyDevice(self._log)
            self.myDevice.setParent(self)
            self.myDevice.setKeyPath(keyPath)
            self.myDevice.setDomain(self.myDomain)

            return self.myDevice
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagContent)):
            self.myContent = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConnectivityCheck)):
            self.myConnectivityCheck = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagManagement)):
            self.myManagement = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLink)):
            self.myLink = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDevice)):
            self.myDevice = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagContent)):
                if (self.myCreateContentFunctor):
                    if (not self.myContent):
                        for logFunc in self._log("handle-trx-element-create-content-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): content not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-content-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.CONTENT_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.CONTENT_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateContentFunctor(phase, self.myContent)
                    except:
                        for logFunc in self._log("handle-trx-element-create-content-functor-exception").exceptionFunc():
                            logFunc("Content's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateContentFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-content-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): content functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-content-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): content functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConnectivityCheck)):
                if (self.myCreateConnectivityCheckFunctor):
                    if (not self.myConnectivityCheck):
                        for logFunc in self._log("handle-trx-element-create-connectivitycheck-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): connectivitycheck not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-connectivitycheck-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.CONNECTIVITYCHECK_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.CONNECTIVITYCHECK_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateConnectivityCheckFunctor(phase, self.myConnectivityCheck)
                    except:
                        for logFunc in self._log("handle-trx-element-create-connectivitycheck-functor-exception").exceptionFunc():
                            logFunc("ConnectivityCheck's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateConnectivityCheckFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-connectivitycheck-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): connectivitycheck functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-connectivitycheck-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): connectivitycheck functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagManagement)):
                if (self.myCreateManagementFunctor):
                    if (not self.myManagement):
                        for logFunc in self._log("handle-trx-element-create-management-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): management not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-management-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.MANAGEMENT_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.MANAGEMENT_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateManagementFunctor(phase, self.myManagement)
                    except:
                        for logFunc in self._log("handle-trx-element-create-management-functor-exception").exceptionFunc():
                            logFunc("Management's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateManagementFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-management-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): management functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-management-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): management functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLink)):
                if (self.myCreateLinkFunctor):
                    if (not self.myLink):
                        for logFunc in self._log("handle-trx-element-create-link-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): link not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-link-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.LINK_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.LINK_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateLinkFunctor(phase, self.myLink)
                    except:
                        for logFunc in self._log("handle-trx-element-create-link-functor-exception").exceptionFunc():
                            logFunc("Link's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateLinkFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-link-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): link functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-link-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): link functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDevice)):
                if (self.myCreateDeviceFunctor):
                    if (not self.myDevice):
                        for logFunc in self._log("handle-trx-element-create-device-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): device not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-device-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.DEVICE_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.DEVICE_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateDeviceFunctor(phase, self.myDevice)
                    except:
                        for logFunc in self._log("handle-trx-element-create-device-functor-exception").exceptionFunc():
                            logFunc("Device's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateDeviceFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-device-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): device functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-device-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): device functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            pass
        return ReturnCodes.kOk
    
    def handleTrxElementPrepareBlinkyDelete(self, trxElement, keyDepth):
        for logFunc in self._log("handle-trx-element-prepare-blinky-delete-called").debug2Func():
            logFunc("called: element-key-path=%s, element-op-code=%s, keyDepth=%s",
                    trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth)

        self.notifyDescendantsPrepareBlinkyDelete()

        # if deleted item is a leaf - clear it in the data
        return self.handleTrxElementPrepareBlinkyValueSet(trxElement, keyDepth)

    def notifyDescendantsPrepareBlinkyDelete(self):
        for logFunc in self._log("notify-descendants-prepare-blinky-delete-called").debug2Func(): logFunc("called")

        self.myDomain.registerNodeToProgressNotification(self)

        
        if (self.myContent):
            self.myContent.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myConnectivityCheck):
            self.myConnectivityCheck.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myManagement):
            self.myManagement.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myLink):
            self.myLink.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myDevice):
            self.myDevice.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagContent)):
                res = self.activateDeleteContentFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-content-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): content functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-content-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): content functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagConnectivityCheck)):
                res = self.activateDeleteConnectivityCheckFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-connectivitycheck-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): connectivitycheck functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-connectivitycheck-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): connectivitycheck functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagManagement)):
                res = self.activateDeleteManagementFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-management-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): management functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-management-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): management functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLink)):
                res = self.activateDeleteLinkFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-link-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): link functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-link-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): link functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDevice)):
                res = self.activateDeleteDeviceFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-device-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): device functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-device-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): device functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeContent(self):
        self.myContent = None

    def activateDeleteContentFunctor(self, phase):
        for logFunc in self._log("activate-delete-content-functor").debug3Func(): logFunc("activateDeleteContentFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteContentFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-content-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.CONTENT_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.CONTENT_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteContentFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-content-functor-exception").exceptionFunc():
                        logFunc("Content's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteContentFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-content-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteContentFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-content-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteContentFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeConnectivityCheck(self):
        self.myConnectivityCheck = None

    def activateDeleteConnectivityCheckFunctor(self, phase):
        for logFunc in self._log("activate-delete-connectivitycheck-functor").debug3Func(): logFunc("activateDeleteConnectivityCheckFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteConnectivityCheckFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-connectivitycheck-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.CONNECTIVITYCHECK_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.CONNECTIVITYCHECK_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteConnectivityCheckFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-connectivitycheck-functor-exception").exceptionFunc():
                        logFunc("ConnectivityCheck's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteConnectivityCheckFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-connectivitycheck-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteConnectivityCheckFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-connectivitycheck-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteConnectivityCheckFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeManagement(self):
        self.myManagement = None

    def activateDeleteManagementFunctor(self, phase):
        for logFunc in self._log("activate-delete-management-functor").debug3Func(): logFunc("activateDeleteManagementFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteManagementFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-management-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.MANAGEMENT_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.MANAGEMENT_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteManagementFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-management-functor-exception").exceptionFunc():
                        logFunc("Management's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteManagementFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-management-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteManagementFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-management-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteManagementFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeLink(self):
        self.myLink = None

    def activateDeleteLinkFunctor(self, phase):
        for logFunc in self._log("activate-delete-link-functor").debug3Func(): logFunc("activateDeleteLinkFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteLinkFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-link-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.LINK_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.LINK_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteLinkFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-link-functor-exception").exceptionFunc():
                        logFunc("Link's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteLinkFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-link-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteLinkFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-link-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteLinkFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeDevice(self):
        self.myDevice = None

    def activateDeleteDeviceFunctor(self, phase):
        for logFunc in self._log("activate-delete-device-functor").debug3Func(): logFunc("activateDeleteDeviceFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteDeviceFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-device-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.DEVICE_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.DEVICE_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteDeviceFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-device-functor-exception").exceptionFunc():
                        logFunc("Device's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteDeviceFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-device-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteDeviceFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-device-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteDeviceFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    

    

    def setValueSetFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-value-set-functor-not-active").errorFunc():
                logFunc("setValueSetFunctor(): is illegal when blinky container is active")
        self.myValueSetFunctor = functor
    
    def activateValueSetFunctor(self, phase, data):
        for logFunc in self._log("activate-value-set-functor").debug3Func():
            logFunc("activateValueSetFunctor(): called, myIsActive=%s, phase=%s, data=%s, candidate=%s, running=%s, functor=%s",
                   self.myIsActive, phase, data, self.myCandidateData, self.myRunningData, self.myValueSetFunctor)
        res = ReturnCodes.kOk
        if (self.myIsActive):
            if (self.myValueSetFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-value-set-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.VALUE_SET_FUNCTOR, phase),
                                            self.getFunctorMildTimeoutForPhase(self.VALUE_SET_FUNCTOR, phase))
                try:
                    res = self.myValueSetFunctor(phase, data)
                except:
                    for logFunc in self._log("activate-value-set-functor-functor-exception").exceptionFunc():
                        logFunc("functor raised an exception. phase=%s, data=%s", phase, data)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myValueSetFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-value-set-functor-failed-prepare").noticeFunc():
                            logFunc("activateValueSetFunctor(): functor failed, phase=%s, data=%s, res=%s",
                                   phase, data, res)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-value-set-functor-failed").errorFunc():
                            logFunc("activateValueSetFunctor(): functor failed, phase=%s, data=%s, res=%s",
                                  phase, data, res)
                    return ReturnCodes.kGeneralError
        return res
    
    def notifyWithCandidate(self, phase):
        for logFunc in self._log("notify-with-candidate").debug3Func(): logFunc("notifyWithCandidate(): called, candidate=%s, phase=%s",
                                                              self.myCandidateData, phase)
        return self.activateValueSetFunctor(phase, self.myCandidateData)
    
    def allocMyCandidate(self):
        for logFunc in self._log("alloc-my-candidate").debug3Func():
            logFunc("called")
        self.myCandidateData = SystemDefaultsData()
        
        res = self.setConfigurationDelayDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-configurationdelay-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setConfigurationDelayDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setMuteReportingDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-mutereporting-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMuteReportingDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setSendGratuitousArpDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-sendgratuitousarp-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setSendGratuitousArpDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setShutdownDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-shutdown-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setShutdownDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setTechModeDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-techmode-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setTechModeDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setConfigurationDelayDefaultValue (self, setHas):
        for logFunc in self._log("set-configurationdelay-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.configurationDelay = 0
            
        if setHas:
            self.myCandidateData.setHasConfigurationDelay()

        return ReturnCodes.kOk

    def setMuteReportingDefaultValue (self, setHas):
        for logFunc in self._log("set-mutereporting-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.muteReporting = False
            
        if setHas:
            self.myCandidateData.setHasMuteReporting()

        return ReturnCodes.kOk

    def setSendGratuitousArpDefaultValue (self, setHas):
        for logFunc in self._log("set-sendgratuitousarp-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.sendGratuitousArp = True
            
        if setHas:
            self.myCandidateData.setHasSendGratuitousArp()

        return ReturnCodes.kOk

    def setShutdownDefaultValue (self, setHas):
        for logFunc in self._log("set-shutdown-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.shutdown = True
            
        if setHas:
            self.myCandidateData.setHasShutdown()

        return ReturnCodes.kOk

    def setTechModeDefaultValue (self, setHas):
        for logFunc in self._log("set-techmode-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.techMode = False
            
        if setHas:
            self.myCandidateData.setHasTechMode()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = SystemDefaultsData()
            self.myCandidateData.copyFrom(self.myRunningData)
            
        else:
            for logFunc in self._log("copy-running-to-candidate-no-running").debug3Func(): logFunc("copyRunningToCandidate(): myRunningData is None")
            res = self.allocMyCandidate()
            if res != ReturnCodes.kOk:
                for logFunc in self._log("copy-running-to-candidate-alloc-my-candidate-failed").errorFunc(): logFunc("copyRunningToCandidate(): myRunningData is None and allocMyCandidate() failed. aborting")
                a.infra.process.processFatal("copyRunningToCandidate(): myRunningData is None and allocMyCandidate() failed")
    
    def deleteMyCandidate(self):
        for logFunc in self._log("delete-my-candidate").debug3Func(): logFunc("deleteMyCandidate(): called, candidate=%s, running=%s",
                                                     self.myCandidateData, self.myRunningData)
        self.myCandidateData = None
    
    def activateCandidate(self):
        phase=TrxPhase(TrxPhase.kCommit, TrxPhase.kBlinky)
        for logFunc in self._log("activate-candidate").debug3Func(): logFunc("activateCandidate(): called, candidate=%s, running=%s, isPhaseDone()=%s",
                                               self.myCandidateData, self.myRunningData, self.myState.isPhaseDone(phase))
        if (self.myState.isPhaseDone(phase)):
            # running config already updated - skip
            return
        self.myRunningData = SystemDefaultsData()
        self.myRunningData.copyFrom(self.myCandidateData)
        self.myCandidateData = None
        self.myState.setPhaseDone(phase)
        for logFunc in self._log("activate-candidate-done").debug3Func(): logFunc("activateCandidate(): done, candidate=%s, running=%s, isPhaseDone()=%s",
                                                    self.myCandidateData, self.myRunningData, self.myState.isPhaseDone(phase))

    

    

    def getRunningCfgData (self):
        if self.myRunningData:
            return copy.copy(self.myRunningData)
        elif self.myCandidateData:
            # running is not yet initialized. getting the candidate that will soon be running
            return copy.copy(self.myCandidateData)
        for logFunc in self._log("get-running-cfg-data").errorFunc(): logFunc("both running and candidate data are none")
        return None

    def getCandidateCfgData (self):
        if self.myCandidateData:
            # when there is no active transaction, there will be no candidate configuration - give the running instead
            if not self.myRunningData:
                for logFunc in self._log("get-candidate-cfg-data").errorFunc(): logFunc("no running and no candidate")
                return None
            return copy.copy(self.myRunningData)
        else:
            # running is not yet initialized. getting the candidate that will soon be running
            return copy.copy(self.myCandidateData)

    def activateSpecific(self):
        for logFunc in self._log("activate-specific").debug3Func(): logFunc("called")
        if self._actionPointId:
            if not self.actionRegistrationDone:
                
                pass
                
        return ReturnCodes.kOk

    def handleTrxProgressNotificationSpecific (self, progress):
        for logFunc in self._log("handle-trx-progress-notification-specific").debug3Func(): logFunc("called. progress=%s, isInDestroy=%s", progress, self.isInDestroy)
        if progress.isCommitBlinkyBefore() or progress.isAbortBlinkyBefore():
            if self.isInDestroy:
                if self._validationPointId and self.validateRegistrationDone:
                    res = self.myDomain.unregisterValidationPoint(self._validationPointId, self)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkysystemdefaults-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkysystemdefaults-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterActionPoint(%s) failed, progress=%s",  self._actionPointId, progress)
                        return ReturnCodes.kGeneralError
        return ReturnCodes.kOk


    def handleInternalDestroy(self, phase):
        __pychecker__ = 'maxreturns=100 maxlines=1000 maxbranches=100'
        for logFunc in self._log("internal-prepare-destroy-helper").debug3Func(): logFunc("handleInternalDestroy(): called, phase=%s", phase)
        res = ReturnCodes.kOk
        self.isInDestroy = True
        if (phase.getConfdPhase() == TrxPhase.kPrepare):
            self.myDomain.registerNodeToProgressNotification(self)
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myContent):
                    res = self.myContent.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-content-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-content-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myConnectivityCheck):
                    res = self.myConnectivityCheck.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-connectivitycheck-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-connectivitycheck-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myManagement):
                    res = self.myManagement.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-management-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-management-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myLink):
                    res = self.myLink.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-link-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-link-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myDevice):
                    res = self.myDevice.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-device-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-device-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-delete-destroy-self-functor-failed-prepare").noticeFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                               res, phase)
                    self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    return ReturnCodes.kGeneralError
                
                if (self.myContent):
                    res = self.activateDeleteContentFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-content-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteContentFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myContent):
                    res = self.myContent.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-content-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myContent.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myConnectivityCheck):
                    res = self.activateDeleteConnectivityCheckFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-connectivitycheck-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConnectivityCheckFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myConnectivityCheck):
                    res = self.myConnectivityCheck.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-connectivitycheck-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConnectivityCheck.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myManagement):
                    res = self.activateDeleteManagementFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-management-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteManagementFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myManagement):
                    res = self.myManagement.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-management-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myManagement.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myLink):
                    res = self.activateDeleteLinkFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-link-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteLinkFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myLink):
                    res = self.myLink.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-link-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myLink.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myDevice):
                    res = self.activateDeleteDeviceFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-device-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteDeviceFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myDevice):
                    res = self.myDevice.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-device-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myDevice.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myContent):
                    res = self.myContent.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-content-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myContent.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeContent()
                
                if (self.myConnectivityCheck):
                    res = self.myConnectivityCheck.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-connectivitycheck-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myConnectivityCheck.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeConnectivityCheck()
                
                if (self.myManagement):
                    res = self.myManagement.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-management-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myManagement.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeManagement()
                
                if (self.myLink):
                    res = self.myLink.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-link-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myLink.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeLink()
                
                if (self.myDevice):
                    res = self.myDevice.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-device-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myDevice.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeDevice()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myContent):
                    res = self.myContent.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-content-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myContent.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteContentFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-content-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteContentFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteContentFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myConnectivityCheck):
                    res = self.myConnectivityCheck.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-connectivitycheck-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConnectivityCheck.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteConnectivityCheckFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-connectivitycheck-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConnectivityCheckFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteConnectivityCheckFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myManagement):
                    res = self.myManagement.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-management-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myManagement.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteManagementFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-management-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteManagementFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteManagementFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myLink):
                    res = self.myLink.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-link-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myLink.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteLinkFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-link-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteLinkFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteLinkFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myDevice):
                    res = self.myDevice.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-device-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myDevice.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteDeviceFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-device-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteDeviceFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteDeviceFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-delete-destroy-self-functor-failed-commit").errorFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                              res, phase)
                    a.infra.process.processFatal("destroy self functor failed in commit")
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("handle-internal-destroy-delete-commit-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): commit-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kAbort):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myContent):
                    res = self.myContent.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-content-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myContent.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myConnectivityCheck):
                    res = self.myConnectivityCheck.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-connectivitycheck-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myConnectivityCheck.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myManagement):
                    res = self.myManagement.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-management-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myManagement.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myLink):
                    res = self.myLink.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-link-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myLink.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myDevice):
                    res = self.myDevice.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-device-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myDevice.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myContent):
                    res = self.myContent.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-content-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myContent.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myContent):
                    res = self.activateDeleteContentFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-content-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteContentFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myConnectivityCheck):
                    res = self.myConnectivityCheck.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-connectivitycheck-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myConnectivityCheck.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myConnectivityCheck):
                    res = self.activateDeleteConnectivityCheckFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-connectivitycheck-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteConnectivityCheckFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myManagement):
                    res = self.myManagement.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-management-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myManagement.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myManagement):
                    res = self.activateDeleteManagementFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-management-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteManagementFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myLink):
                    res = self.myLink.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-link-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myLink.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myLink):
                    res = self.activateDeleteLinkFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-link-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteLinkFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myDevice):
                    res = self.myDevice.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-device-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myDevice.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myDevice):
                    res = self.activateDeleteDeviceFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-device-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteDeviceFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                res = self.activateDestroySelfFunctor(phase)
                if (res != ReturnCodes.kOk):
                    for logFunc in self._log("handle-internal-destroy-activate-destroy-self-functor-failed-abort").errorFunc():
                        logFunc("handleInternalDestroy(): activateDestroySelfFunctor() failed, res=%s, phase=%s",
                              res, phase)
                    a.infra.process.processFatal("destroy self functor failed in abort")
                    return ReturnCodes.kOk
            else:
                for logFunc in self._log("handle-internal-destroy-delete-abort-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): abort-illegal-blinky, res=%s, phase=%s", res, phase)
                return ReturnCodes.kGeneralError
        else:
            for logFunc in self._log("handle-internal-destroy-delete-illegal-confd").noticeFunc():
                logFunc("handleInternalDestroy(): illegal-confd, res=%s, phase=%s", res, phase)
            return ReturnCodes.kGeneralError
    
        return ReturnCodes.kOk
    
"""
Extracted from the below data: 
{
    "node": {
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.system_defaults.system_defaults_data_gen import SystemDefaultsData", 
        "moduleYangNamespacePrefix": "qt-if", 
        "validationPoint": null, 
        "yangName": "system-defaults", 
        "namespace": "system_defaults", 
        "logGroupName": "blinky-system-defaults", 
        "className": "BlinkySystemDefaults", 
        "logModuleName": "a-sys-net-tech-interfaces-tech-interfaces-interface-system-defaults-blinky-system-defaults-gen", 
        "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
        "dataClassName": "SystemDefaultsData", 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyContent", 
            "memberName": "Content", 
            "yangName": "content", 
            "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.content.blinky_content_gen import BlinkyContent"
        }, 
        {
            "className": "BlinkyConnectivityCheck", 
            "memberName": "ConnectivityCheck", 
            "yangName": "connectivity-check", 
            "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.connectivity_check.blinky_connectivity_check_gen import BlinkyConnectivityCheck"
        }, 
        {
            "className": "BlinkyManagement", 
            "memberName": "Management", 
            "yangName": "management", 
            "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.management.blinky_management_gen import BlinkyManagement"
        }, 
        {
            "className": "BlinkyLink", 
            "memberName": "Link", 
            "yangName": "link", 
            "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.link.blinky_link_gen import BlinkyLink"
        }, 
        {
            "className": "BlinkyDevice", 
            "memberName": "Device", 
            "yangName": "device", 
            "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.system_defaults.device.blinky_device_gen import BlinkyDevice"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "configurationDelay", 
            "yangName": "configuration-delay", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "sendGratuitousArp", 
            "yangName": "send-gratuitous-arp", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shutdown", 
            "yangName": "shutdown", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "techMode", 
            "yangName": "tech-mode", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "env": [
        "a", 
        "sys", 
        "net", 
        "tech_interfaces"
    ], 
    "createTime": "2013"
}
"""

