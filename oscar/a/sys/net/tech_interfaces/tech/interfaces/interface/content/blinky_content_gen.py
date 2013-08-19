


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




from a.sys.net.tech_interfaces.tech.interfaces.interface.content.delivery.blinky_delivery_gen import BlinkyDelivery

from a.sys.net.tech_interfaces.tech.interfaces.interface.content.analytics.blinky_analytics_gen import BlinkyAnalytics

from a.sys.net.tech_interfaces.tech.interfaces.interface.content.acquisition.blinky_acquisition_gen import BlinkyAcquisition




class BlinkyContent(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
    #leaves
    

    #descendants
    
    ourXmlTagDelivery="delivery"
    
    ourXmlTagAnalytics="analytics"
    
    ourXmlTagAcquisition="acquisition"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    DELIVERY_CREATE_FUNCTOR = 'DELIVERY_CREATE_FUNCTOR'
    DELIVERY_DELETE_FUNCTOR = 'DELIVERY_DELETE_FUNCTOR'
    
    ANALYTICS_CREATE_FUNCTOR = 'ANALYTICS_CREATE_FUNCTOR'
    ANALYTICS_DELETE_FUNCTOR = 'ANALYTICS_DELETE_FUNCTOR'
    
    ACQUISITION_CREATE_FUNCTOR = 'ACQUISITION_CREATE_FUNCTOR'
    ACQUISITION_DELETE_FUNCTOR = 'ACQUISITION_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateDeliveryFunctor=None
        self.myDeleteDeliveryFunctor=None
        self.myDelivery=None
        
        self.myCreateAnalyticsFunctor=None
        self.myDeleteAnalyticsFunctor=None
        self.myAnalytics=None
        
        self.myCreateAcquisitionFunctor=None
        self.myDeleteAcquisitionFunctor=None
        self.myAcquisition=None
        
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

        logger('s-create-blinkycontent').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyContent._validationPointId, BlinkyContent._actionPointId)

        confd_key=KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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
        
        newNode=BlinkyContent(logger)
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

    
    def setCreateDeliveryFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-delivery-functor-active").errorFunc():
                logFunc("setCreateDeliveryFunctor() is illegal when blinky node is active")
        self.myCreateDeliveryFunctor = functor

    def setDeleteDeliveryFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-delivery-functor-active").errorFunc():
                logFunc("setDeleteDeliveryFunctor() is illegal when blinky node is active")
        self.myDeleteDeliveryFunctor = functor
    
    def setCreateAnalyticsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-analytics-functor-active").errorFunc():
                logFunc("setCreateAnalyticsFunctor() is illegal when blinky node is active")
        self.myCreateAnalyticsFunctor = functor

    def setDeleteAnalyticsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-analytics-functor-active").errorFunc():
                logFunc("setDeleteAnalyticsFunctor() is illegal when blinky node is active")
        self.myDeleteAnalyticsFunctor = functor
    
    def setCreateAcquisitionFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-acquisition-functor-active").errorFunc():
                logFunc("setCreateAcquisitionFunctor() is illegal when blinky node is active")
        self.myCreateAcquisitionFunctor = functor

    def setDeleteAcquisitionFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-acquisition-functor-active").errorFunc():
                logFunc("setDeleteAcquisitionFunctor() is illegal when blinky node is active")
        self.myDeleteAcquisitionFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagDelivery)):
            return self.myDelivery
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagAnalytics)):
            return self.myAnalytics
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagAcquisition)):
            return self.myAcquisition
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkycontent').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.net.tech_interfaces.tech.interfaces.interface.content.blinky_content_gen import BlinkyContent', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagDelivery)):
                    keyPathRegistered = BlinkyDelivery.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagAnalytics)):
                    keyPathRegistered = BlinkyAnalytics.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagAcquisition)):
                    keyPathRegistered = BlinkyAcquisition.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        logger('is-key-path-registered-blinkycontent-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.net.tech_interfaces.tech.interfaces.interface.content.blinky_content_gen import BlinkyContent', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDelivery)):
            if (self.myDelivery):
                for logFunc in self._log("prepare-my-blinky-node-delivery-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myDelivery = BlinkyDelivery(self._log)
            self.myDelivery.setParent(self)
            self.myDelivery.setKeyPath(keyPath)
            self.myDelivery.setDomain(self.myDomain)

            return self.myDelivery
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAnalytics)):
            if (self.myAnalytics):
                for logFunc in self._log("prepare-my-blinky-node-analytics-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myAnalytics = BlinkyAnalytics(self._log)
            self.myAnalytics.setParent(self)
            self.myAnalytics.setKeyPath(keyPath)
            self.myAnalytics.setDomain(self.myDomain)

            return self.myAnalytics
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAcquisition)):
            if (self.myAcquisition):
                for logFunc in self._log("prepare-my-blinky-node-acquisition-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myAcquisition = BlinkyAcquisition(self._log)
            self.myAcquisition.setParent(self)
            self.myAcquisition.setKeyPath(keyPath)
            self.myAcquisition.setDomain(self.myDomain)

            return self.myAcquisition
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDelivery)):
            self.myDelivery = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAnalytics)):
            self.myAnalytics = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAcquisition)):
            self.myAcquisition = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDelivery)):
                if (self.myCreateDeliveryFunctor):
                    if (not self.myDelivery):
                        for logFunc in self._log("handle-trx-element-create-delivery-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): delivery not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-delivery-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.DELIVERY_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.DELIVERY_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateDeliveryFunctor(phase, self.myDelivery)
                    except:
                        for logFunc in self._log("handle-trx-element-create-delivery-functor-exception").exceptionFunc():
                            logFunc("Delivery's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateDeliveryFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-delivery-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): delivery functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-delivery-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): delivery functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAnalytics)):
                if (self.myCreateAnalyticsFunctor):
                    if (not self.myAnalytics):
                        for logFunc in self._log("handle-trx-element-create-analytics-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): analytics not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-analytics-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.ANALYTICS_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.ANALYTICS_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateAnalyticsFunctor(phase, self.myAnalytics)
                    except:
                        for logFunc in self._log("handle-trx-element-create-analytics-functor-exception").exceptionFunc():
                            logFunc("Analytics's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateAnalyticsFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-analytics-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): analytics functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-analytics-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): analytics functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAcquisition)):
                if (self.myCreateAcquisitionFunctor):
                    if (not self.myAcquisition):
                        for logFunc in self._log("handle-trx-element-create-acquisition-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): acquisition not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-acquisition-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.ACQUISITION_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.ACQUISITION_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateAcquisitionFunctor(phase, self.myAcquisition)
                    except:
                        for logFunc in self._log("handle-trx-element-create-acquisition-functor-exception").exceptionFunc():
                            logFunc("Acquisition's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateAcquisitionFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-acquisition-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): acquisition functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-acquisition-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): acquisition functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.myDelivery):
            self.myDelivery.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myAnalytics):
            self.myAnalytics.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myAcquisition):
            self.myAcquisition.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDelivery)):
                res = self.activateDeleteDeliveryFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-delivery-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): delivery functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-delivery-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): delivery functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAnalytics)):
                res = self.activateDeleteAnalyticsFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-analytics-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): analytics functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-analytics-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): analytics functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAcquisition)):
                res = self.activateDeleteAcquisitionFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-acquisition-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): acquisition functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-acquisition-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): acquisition functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeDelivery(self):
        self.myDelivery = None

    def activateDeleteDeliveryFunctor(self, phase):
        for logFunc in self._log("activate-delete-delivery-functor").debug3Func(): logFunc("activateDeleteDeliveryFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteDeliveryFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-delivery-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.DELIVERY_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.DELIVERY_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteDeliveryFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-delivery-functor-exception").exceptionFunc():
                        logFunc("Delivery's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteDeliveryFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-delivery-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteDeliveryFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-delivery-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteDeliveryFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeAnalytics(self):
        self.myAnalytics = None

    def activateDeleteAnalyticsFunctor(self, phase):
        for logFunc in self._log("activate-delete-analytics-functor").debug3Func(): logFunc("activateDeleteAnalyticsFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteAnalyticsFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-analytics-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.ANALYTICS_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.ANALYTICS_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteAnalyticsFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-analytics-functor-exception").exceptionFunc():
                        logFunc("Analytics's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteAnalyticsFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-analytics-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteAnalyticsFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-analytics-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteAnalyticsFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeAcquisition(self):
        self.myAcquisition = None

    def activateDeleteAcquisitionFunctor(self, phase):
        for logFunc in self._log("activate-delete-acquisition-functor").debug3Func(): logFunc("activateDeleteAcquisitionFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteAcquisitionFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-acquisition-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.ACQUISITION_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.ACQUISITION_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteAcquisitionFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-acquisition-functor-exception").exceptionFunc():
                        logFunc("Acquisition's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteAcquisitionFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-acquisition-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteAcquisitionFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-acquisition-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteAcquisitionFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    

    

    
    
    def notifyWithCandidate(self, phase):
        for logFunc in self._log("notify-with-candidate").debug3Func(): logFunc("notifyWithCandidate(): called, candidate=%s, phase=%s",
                                                              self.myCandidateData, phase)
        return ReturnCodes.kOk
    
    def allocMyCandidate(self):
        for logFunc in self._log("alloc-my-candidate").debug3Func():
            logFunc("called")
        
        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            pass
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkycontent-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkycontent-failed").errorFunc():
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
                
                if (self.myDelivery):
                    res = self.myDelivery.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-delivery-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-delivery-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myAnalytics):
                    res = self.myAnalytics.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-analytics-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-analytics-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myAcquisition):
                    res = self.myAcquisition.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-acquisition-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-acquisition-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.myDelivery):
                    res = self.activateDeleteDeliveryFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-delivery-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteDeliveryFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myDelivery):
                    res = self.myDelivery.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-delivery-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myDelivery.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myAnalytics):
                    res = self.activateDeleteAnalyticsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-analytics-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAnalyticsFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myAnalytics):
                    res = self.myAnalytics.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-analytics-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAnalytics.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myAcquisition):
                    res = self.activateDeleteAcquisitionFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-acquisition-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAcquisitionFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myAcquisition):
                    res = self.myAcquisition.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-acquisition-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAcquisition.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myDelivery):
                    res = self.myDelivery.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-delivery-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myDelivery.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeDelivery()
                
                if (self.myAnalytics):
                    res = self.myAnalytics.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-analytics-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myAnalytics.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeAnalytics()
                
                if (self.myAcquisition):
                    res = self.myAcquisition.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-acquisition-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myAcquisition.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeAcquisition()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myDelivery):
                    res = self.myDelivery.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-delivery-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myDelivery.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteDeliveryFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-delivery-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteDeliveryFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteDeliveryFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myAnalytics):
                    res = self.myAnalytics.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-analytics-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAnalytics.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteAnalyticsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-analytics-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAnalyticsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteAnalyticsFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myAcquisition):
                    res = self.myAcquisition.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-acquisition-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAcquisition.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteAcquisitionFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-acquisition-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAcquisitionFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteAcquisitionFunctor failed in commit phase (private/public)")
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
                
                if (self.myDelivery):
                    res = self.myDelivery.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-delivery-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myDelivery.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myAnalytics):
                    res = self.myAnalytics.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-analytics-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myAnalytics.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myAcquisition):
                    res = self.myAcquisition.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-acquisition-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myAcquisition.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myDelivery):
                    res = self.myDelivery.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-delivery-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myDelivery.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myDelivery):
                    res = self.activateDeleteDeliveryFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-delivery-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteDeliveryFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myAnalytics):
                    res = self.myAnalytics.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-analytics-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAnalytics.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myAnalytics):
                    res = self.activateDeleteAnalyticsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-analytics-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAnalyticsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myAcquisition):
                    res = self.myAcquisition.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-acquisition-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAcquisition.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myAcquisition):
                    res = self.activateDeleteAcquisitionFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-acquisition-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAcquisitionFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.content.content_data_gen import ContentData", 
        "moduleYangNamespacePrefix": "qt-if", 
        "validationPoint": null, 
        "yangName": "content", 
        "namespace": "content", 
        "logGroupName": "blinky-content", 
        "className": "BlinkyContent", 
        "logModuleName": "a-sys-net-tech-interfaces-tech-interfaces-interface-content-blinky-content-gen", 
        "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.content.blinky_content_gen import BlinkyContent", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
        "dataClassName": "ContentData", 
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
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "content"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyDelivery", 
            "memberName": "Delivery", 
            "yangName": "delivery", 
            "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.content.delivery.blinky_delivery_gen import BlinkyDelivery"
        }, 
        {
            "className": "BlinkyAnalytics", 
            "memberName": "Analytics", 
            "yangName": "analytics", 
            "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.content.analytics.blinky_analytics_gen import BlinkyAnalytics"
        }, 
        {
            "className": "BlinkyAcquisition", 
            "memberName": "Acquisition", 
            "yangName": "acquisition", 
            "importStatement": "from a.sys.net.tech_interfaces.tech.interfaces.interface.content.acquisition.blinky_acquisition_gen import BlinkyAcquisition"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [], 
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

