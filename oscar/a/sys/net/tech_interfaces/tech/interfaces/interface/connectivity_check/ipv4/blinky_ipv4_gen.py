


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

from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.ipv4_data_gen import Ipv4Data


from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.arp.blinky_arp_gen import BlinkyArp

from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.ping.blinky_ping_gen import BlinkyPing


from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import ConnectivityCheckIpv4MethodType


class BlinkyIpv4(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
    #leaves
    
    ourXmlTagMethod="method"
    

    #descendants
    
    ourXmlTagArp="arp"
    
    ourXmlTagPing="ping"
    

    _validationPointId=None
    
    _actionPointId=None
    _actionPointId="tech-interfaces-interface-connectivity-check-ipv4-clear-counters-actionpoint"

    
    ARP_CREATE_FUNCTOR = 'ARP_CREATE_FUNCTOR'
    ARP_DELETE_FUNCTOR = 'ARP_DELETE_FUNCTOR'
    
    PING_CREATE_FUNCTOR = 'PING_CREATE_FUNCTOR'
    PING_DELETE_FUNCTOR = 'PING_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateArpFunctor=None
        self.myDeleteArpFunctor=None
        self.myArp=None
        
        self.myCreatePingFunctor=None
        self.myDeletePingFunctor=None
        self.myPing=None
        
        self.myValueSetFunctor=None
        self.myCandidateData=None
        self.myRunningData=None
        self.isInDestroy = False
        
        self.validateRegistrationDone = False
        self.actionRegistrationDone=False
        
        
        self.doActionFunctor = None
        

    @classmethod
    def s_create (cls, logger, 
                  
                  
                  
                  interface, 
                  
                  
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkyipv4').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyIpv4._validationPointId, BlinkyIpv4._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ipv4", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("connectivity-check", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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
        
        newNode=BlinkyIpv4(logger)
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

    
    def setCreateArpFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-arp-functor-active").errorFunc():
                logFunc("setCreateArpFunctor() is illegal when blinky node is active")
        self.myCreateArpFunctor = functor

    def setDeleteArpFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-arp-functor-active").errorFunc():
                logFunc("setDeleteArpFunctor() is illegal when blinky node is active")
        self.myDeleteArpFunctor = functor
    
    def setCreatePingFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-ping-functor-active").errorFunc():
                logFunc("setCreatePingFunctor() is illegal when blinky node is active")
        self.myCreatePingFunctor = functor

    def setDeletePingFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-ping-functor-active").errorFunc():
                logFunc("setDeletePingFunctor() is illegal when blinky node is active")
        self.myDeletePingFunctor = functor
    

    

    
    def setDoActionFunctor(self, functor):
        if self.myIsActive:
            for logFunc in self._log("set-do-action-functor-active").errorFunc():
                logFunc("illegal when blinky node is active")
        self.doActionFunctor = functor
    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMethod)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not ConnectivityCheckIpv4MethodType.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-method-failed")\
                        .error("illegal enum value %s for method", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.method = ConnectivityCheckIpv4MethodType.getByValue(newValue.asEnum())
                self.myCandidateData.setHasMethod()
                
            else:
                self.setMethodDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagArp)):
            return self.myArp
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagPing)):
            return self.myPing
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyipv4').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.blinky_ipv4_gen import BlinkyIpv4', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagArp)):
                    keyPathRegistered = BlinkyArp.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagPing)):
                    keyPathRegistered = BlinkyPing.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMethod)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkyipv4-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.blinky_ipv4_gen import BlinkyIpv4', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagArp)):
            if (self.myArp):
                for logFunc in self._log("prepare-my-blinky-node-arp-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myArp = BlinkyArp(self._log)
            self.myArp.setParent(self)
            self.myArp.setKeyPath(keyPath)
            self.myArp.setDomain(self.myDomain)

            return self.myArp
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPing)):
            if (self.myPing):
                for logFunc in self._log("prepare-my-blinky-node-ping-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myPing = BlinkyPing(self._log)
            self.myPing.setParent(self)
            self.myPing.setKeyPath(keyPath)
            self.myPing.setDomain(self.myDomain)

            return self.myPing
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagArp)):
            self.myArp = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPing)):
            self.myPing = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagArp)):
                if (self.myCreateArpFunctor):
                    if (not self.myArp):
                        for logFunc in self._log("handle-trx-element-create-arp-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): arp not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-arp-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.ARP_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.ARP_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateArpFunctor(phase, self.myArp)
                    except:
                        for logFunc in self._log("handle-trx-element-create-arp-functor-exception").exceptionFunc():
                            logFunc("Arp's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateArpFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-arp-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): arp functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-arp-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): arp functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPing)):
                if (self.myCreatePingFunctor):
                    if (not self.myPing):
                        for logFunc in self._log("handle-trx-element-create-ping-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): ping not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-ping-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.PING_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.PING_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreatePingFunctor(phase, self.myPing)
                    except:
                        for logFunc in self._log("handle-trx-element-create-ping-functor-exception").exceptionFunc():
                            logFunc("Ping's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreatePingFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-ping-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): ping functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-ping-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): ping functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.myArp):
            self.myArp.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myPing):
            self.myPing.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagArp)):
                res = self.activateDeleteArpFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-arp-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): arp functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-arp-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): arp functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagPing)):
                res = self.activateDeletePingFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-ping-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): ping functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-ping-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): ping functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeArp(self):
        self.myArp = None

    def activateDeleteArpFunctor(self, phase):
        for logFunc in self._log("activate-delete-arp-functor").debug3Func(): logFunc("activateDeleteArpFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteArpFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-arp-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.ARP_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.ARP_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteArpFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-arp-functor-exception").exceptionFunc():
                        logFunc("Arp's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteArpFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-arp-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteArpFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-arp-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteArpFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removePing(self):
        self.myPing = None

    def activateDeletePingFunctor(self, phase):
        for logFunc in self._log("activate-delete-ping-functor").debug3Func(): logFunc("activateDeletePingFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeletePingFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-ping-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.PING_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.PING_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeletePingFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-ping-functor-exception").exceptionFunc():
                        logFunc("Ping's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeletePingFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-ping-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeletePingFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-ping-functor-functor-failed").errorFunc():
                            logFunc("activateDeletePingFunctor(): functor failed, phase=%s", phase)
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
        self.myCandidateData = Ipv4Data()
        
        res = self.setMethodDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-method-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMethodDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setMethodDefaultValue (self, setHas):
        for logFunc in self._log("set-method-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.method = ConnectivityCheckIpv4MethodType.kArp
            
        if setHas:
            self.myCandidateData.setHasMethod()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = Ipv4Data()
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
        self.myRunningData = Ipv4Data()
        self.myRunningData.copyFrom(self.myCandidateData)
        self.myCandidateData = None
        self.myState.setPhaseDone(phase)
        for logFunc in self._log("activate-candidate-done").debug3Func(): logFunc("activateCandidate(): done, candidate=%s, running=%s, isPhaseDone()=%s",
                                                    self.myCandidateData, self.myRunningData, self.myState.isPhaseDone(phase))

    

    
    def doAction (self, userInfo, actionPoint, actionName, keypath, params, nParams):
        for logFunc in self._log("do-action").debug3Func(): logFunc("called. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
        if self.myIsActive:
            if self.doActionFunctor:
                timeoutGuard = TimeoutGuard(self._log, '%s-do-action-functor-%s' % (keypath, actionPoint), 
                                            self.getFunctorTimeout(self.DO_ACTION_FUNCTOR), 
                                            self.getFunctorMildTimeout(self.DO_ACTION_FUNCTOR))
                try:
                    res = self.doActionFunctor(userInfo, actionPoint, actionName, params, nParams)
                except:
                    for logFunc in self._log("do-action-functor-exception").exceptionFunc():
                        logFunc("functor raised an exception. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.doActionFunctor.__name__)
                if res != ReturnCodes.kOk:
                    for logFunc in self._log("do-action-functor-failed").errorFunc(): logFunc("functor failed. res=%s, userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", res, userInfo, actionPoint, actionName, keypath, params, nParams)
                    return ReturnCodes.kGeneralError
            else:
                for logFunc in self._log("do-action-functor-unset").debug3Func(): logFunc("no do-action functor set. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
            return ReturnCodes.kOk
        else:
            #TODO (naamas) - add error string
            for logFunc in self._log("d-action-inactive").errorFunc(): logFunc("Blinky node is inactive. userInfo=%s, actionPoint=%s, actionName=%s, keypath=%s, paramas=%s, nParams=%s", userInfo, actionPoint, actionName, keypath, params, nParams)
            return ReturnCodes.kGeneralError
    

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
                
                if self.doActionFunctor:
                    res = self.myDomain.registerActionPoint(self._actionPointId, self)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("activate-specitic-register-action-point-failed").errorFunc():
                            logFunc("activateSpecific(): registerActionPoint(%s) failed",  self._actionPointId)
                        return None
                
        return ReturnCodes.kOk

    def handleTrxProgressNotificationSpecific (self, progress):
        for logFunc in self._log("handle-trx-progress-notification-specific").debug3Func(): logFunc("called. progress=%s, isInDestroy=%s", progress, self.isInDestroy)
        if progress.isCommitBlinkyBefore() or progress.isAbortBlinkyBefore():
            if self.isInDestroy:
                if self._validationPointId and self.validateRegistrationDone:
                    res = self.myDomain.unregisterValidationPoint(self._validationPointId, self)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyipv4-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyipv4-failed").errorFunc():
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
                
                if (self.myArp):
                    res = self.myArp.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-arp-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-arp-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myPing):
                    res = self.myPing.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ping-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-ping-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.myArp):
                    res = self.activateDeleteArpFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-arp-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteArpFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myArp):
                    res = self.myArp.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-arp-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myArp.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myPing):
                    res = self.activateDeletePingFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ping-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeletePingFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myPing):
                    res = self.myPing.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ping-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myPing.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myArp):
                    res = self.myArp.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-arp-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myArp.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeArp()
                
                if (self.myPing):
                    res = self.myPing.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ping-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myPing.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removePing()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myArp):
                    res = self.myArp.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-arp-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myArp.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteArpFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-arp-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteArpFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteArpFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myPing):
                    res = self.myPing.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ping-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myPing.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeletePingFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ping-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeletePingFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeletePingFunctor failed in commit phase (private/public)")
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
                
                if (self.myArp):
                    res = self.myArp.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-arp-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myArp.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myPing):
                    res = self.myPing.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ping-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myPing.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myArp):
                    res = self.myArp.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-arp-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myArp.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myArp):
                    res = self.activateDeleteArpFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-arp-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteArpFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myPing):
                    res = self.myPing.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ping-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myPing.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myPing):
                    res = self.activateDeletePingFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-ping-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeletePingFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.ipv4_data_gen import Ipv4Data", 
        "moduleYangNamespacePrefix": "qt-if", 
        "validationPoint": null, 
        "yangName": "ipv4", 
        "namespace": "ipv4", 
        "logGroupName": "blinky-ipv4", 
        "className": "BlinkyIpv4", 
        "logModuleName": "a-sys-net-tech-interfaces-tech-interfaces-interface-connectivity-check-ipv4-blinky-ipv4-gen", 
        "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.blinky_ipv4_gen import BlinkyIpv4", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
        "dataClassName": "Ipv4Data", 
        "actionPoint": "tech-interfaces-interface-connectivity-check-ipv4-clear-counters-actionpoint"
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
            "yangName": "connectivity-check", 
            "namespace": "connectivity_check", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "connectivity-check"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "ipv4", 
            "namespace": "ipv4", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "ipv4"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyArp", 
            "memberName": "Arp", 
            "yangName": "arp", 
            "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.arp.blinky_arp_gen import BlinkyArp"
        }, 
        {
            "className": "BlinkyPing", 
            "memberName": "Ping", 
            "yangName": "ping", 
            "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.ping.blinky_ping_gen import BlinkyPing"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "method", 
            "yangName": "method", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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

