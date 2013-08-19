


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

from a.sys.blinky.example.lake_example.lake.fish_.fish__data_gen import FishData


from a.sys.blinky.example.lake_example.lake.fish_.antenna.blinky_antenna_gen import BlinkyAntenna

from a.sys.blinky.example.lake_example.lake.fish_.test_generation_underscore.blinky_test_generation_underscore_list_gen import BlinkyTestGenerationUnderscoreList

from a.sys.blinky.example.lake_example.lake.fish_.transparent_container.blinky_transparent_container_gen import BlinkyTransparentContainer


from a.sys.blinky.example.lake_example.lake_example_module_gen import ColorT
import struct


class BlinkyFish(BlinkyContainer):
    ourNamespace="http://qwilt.com/model/lake-example"
    #leaves
    
    ourXmlTagTransparentField="transparent-field"
    
    ourXmlTagColor="color"
    
    ourXmlTagEyeNumber="eye-number"
    
    ourXmlTagHasTail="has-tail"
    
    ourXmlTagFinNumber="fin-number"
    
    ourXmlTagLength="length"
    
    ourXmlTagIp6="ip6"
    
    ourXmlTagId="id"
    

    #descendants
    
    ourXmlTagAntenna="antenna"
    
    ourXmlTagTestGenerationUnderscoreList="test-generation_underscore"
    
    ourXmlTagTransparentContainer="transparent-container"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    ANTENNA_CREATE_FUNCTOR = 'ANTENNA_CREATE_FUNCTOR'
    ANTENNA_DELETE_FUNCTOR = 'ANTENNA_DELETE_FUNCTOR'
    
    TESTGENERATIONUNDERSCORELIST_CREATE_FUNCTOR = 'TESTGENERATIONUNDERSCORELIST_CREATE_FUNCTOR'
    TESTGENERATIONUNDERSCORELIST_DELETE_FUNCTOR = 'TESTGENERATIONUNDERSCORELIST_DELETE_FUNCTOR'
    
    TRANSPARENTCONTAINER_CREATE_FUNCTOR = 'TRANSPARENTCONTAINER_CREATE_FUNCTOR'
    TRANSPARENTCONTAINER_DELETE_FUNCTOR = 'TRANSPARENTCONTAINER_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateAntennaFunctor=None
        self.myDeleteAntennaFunctor=None
        self.myAntenna=None
        
        self.myCreateTestGenerationUnderscoreListFunctor=None
        self.myDeleteTestGenerationUnderscoreListFunctor=None
        self.myTestGenerationUnderscoreList=None
        
        self.myCreateTransparentContainerFunctor=None
        self.myDeleteTransparentContainerFunctor=None
        self.myTransparentContainer=None
        
        self.myValueSetFunctor=None
        self.myCandidateData=None
        self.myRunningData=None
        self.isInDestroy = False
        
        self.validateRegistrationDone = False
        self.actionRegistrationDone=False
        
        

    @classmethod
    def s_create (cls, logger, 
                  
                  lake, 
                  fish_, 
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkyfish').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyFish._validationPointId, BlinkyFish._actionPointId)

        confd_key=KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(fish_);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fish", "http://qwilt.com/model/lake-example", "lake-example"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(lake);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("lake", "http://qwilt.com/model/lake-example", "lake-example"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyFish(logger)
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

    
    def setCreateAntennaFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-antenna-functor-active").errorFunc():
                logFunc("setCreateAntennaFunctor() is illegal when blinky node is active")
        self.myCreateAntennaFunctor = functor

    def setDeleteAntennaFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-antenna-functor-active").errorFunc():
                logFunc("setDeleteAntennaFunctor() is illegal when blinky node is active")
        self.myDeleteAntennaFunctor = functor
    
    def setCreateTestGenerationUnderscoreListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-test-generation_underscore-functor-active").errorFunc():
                logFunc("setCreateTestGenerationUnderscoreListFunctor() is illegal when blinky node is active")
        self.myCreateTestGenerationUnderscoreListFunctor = functor

    def setDeleteTestGenerationUnderscoreListFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-test-generation_underscore-functor-active").errorFunc():
                logFunc("setDeleteTestGenerationUnderscoreListFunctor() is illegal when blinky node is active")
        self.myDeleteTestGenerationUnderscoreListFunctor = functor
    
    def setCreateTransparentContainerFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-transparent-container-functor-active").errorFunc():
                logFunc("setCreateTransparentContainerFunctor() is illegal when blinky node is active")
        self.myCreateTransparentContainerFunctor = functor

    def setDeleteTransparentContainerFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-transparent-container-functor-active").errorFunc():
                logFunc("setDeleteTransparentContainerFunctor() is illegal when blinky node is active")
        self.myDeleteTransparentContainerFunctor = functor
    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTransparentField)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.transparentField = newValue.asBool()
                self.myCandidateData.setHasTransparentField()
                
            else:
                self.setTransparentFieldDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagColor)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not ColorT.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-color-failed")\
                        .error("illegal enum value %s for color", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.color = ColorT.getByValue(newValue.asEnum())
                self.myCandidateData.setHasColor()
                
            else:
                self.setColorDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagEyeNumber)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.eyeNumber = newValue.asInt64()
                self.myCandidateData.setHasEyeNumber()
                
            else:
                self.setEyeNumberDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagHasTail)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.hasTail = newValue.asBool()
                self.myCandidateData.setHasHasTail()
                
            else:
                self.setHasTailDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagFinNumber)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.finNumber = newValue.asInt64()
                self.myCandidateData.setHasFinNumber()
                
            else:
                self.setFinNumberDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLength)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.length = newValue.asInt64()
                self.myCandidateData.setHasLength()
                
            else:
                self.setLengthDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagIp6)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.ip6 = (newValue.asIPv6())
                self.myCandidateData.setHasIp6()
                
            else:
                self.setIp6DefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagId)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.id = newValue.asString()
                self.myCandidateData.setHasId()
                
            else:
                self.setIdDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagAntenna)):
            return self.myAntenna
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagTestGenerationUnderscoreList)):
            return self.myTestGenerationUnderscoreList
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagTransparentContainer)):
            return self.myTransparentContainer
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyfish').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.blinky.example.lake_example.lake.fish_.blinky_fish__gen import BlinkyFish', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagAntenna)):
                    keyPathRegistered = BlinkyAntenna.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagTestGenerationUnderscoreList)):
                    keyPathRegistered = BlinkyTestGenerationUnderscoreList.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagTransparentContainer)):
                    keyPathRegistered = BlinkyTransparentContainer.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagTransparentField)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagColor)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagEyeNumber)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagHasTail)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagFinNumber)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagLength)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagIp6)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagId)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkyfish-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.blinky.example.lake_example.lake.fish_.blinky_fish__gen import BlinkyFish', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAntenna)):
            if (self.myAntenna):
                for logFunc in self._log("prepare-my-blinky-node-antenna-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myAntenna = BlinkyAntenna(self._log)
            self.myAntenna.setParent(self)
            self.myAntenna.setKeyPath(keyPath)
            self.myAntenna.setDomain(self.myDomain)

            return self.myAntenna
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTestGenerationUnderscoreList)):
            if (self.myTestGenerationUnderscoreList):
                for logFunc in self._log("prepare-my-blinky-node-testgenerationunderscorelist-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myTestGenerationUnderscoreList = BlinkyTestGenerationUnderscoreList(self._log)
            self.myTestGenerationUnderscoreList.setParent(self)
            self.myTestGenerationUnderscoreList.setKeyPath(keyPath)
            self.myTestGenerationUnderscoreList.setDomain(self.myDomain)

            return self.myTestGenerationUnderscoreList
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTransparentContainer)):
            if (self.myTransparentContainer):
                for logFunc in self._log("prepare-my-blinky-node-transparentcontainer-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.myTransparentContainer = BlinkyTransparentContainer(self._log)
            self.myTransparentContainer.setParent(self)
            self.myTransparentContainer.setKeyPath(keyPath)
            self.myTransparentContainer.setDomain(self.myDomain)

            return self.myTransparentContainer
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAntenna)):
            self.myAntenna = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTestGenerationUnderscoreList)):
            self.myTestGenerationUnderscoreList = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTransparentContainer)):
            self.myTransparentContainer = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAntenna)):
                if (self.myCreateAntennaFunctor):
                    if (not self.myAntenna):
                        for logFunc in self._log("handle-trx-element-create-antenna-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): antenna not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-antenna-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.ANTENNA_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.ANTENNA_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateAntennaFunctor(phase, self.myAntenna)
                    except:
                        for logFunc in self._log("handle-trx-element-create-antenna-functor-exception").exceptionFunc():
                            logFunc("Antenna's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateAntennaFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-antenna-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): antenna functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-antenna-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): antenna functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTestGenerationUnderscoreList)):
                if (self.myCreateTestGenerationUnderscoreListFunctor):
                    if (not self.myTestGenerationUnderscoreList):
                        for logFunc in self._log("handle-trx-element-create-testgenerationunderscorelist-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): testgenerationunderscorelist not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-testgenerationunderscorelist-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.TESTGENERATIONUNDERSCORELIST_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.TESTGENERATIONUNDERSCORELIST_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateTestGenerationUnderscoreListFunctor(phase, self.myTestGenerationUnderscoreList)
                    except:
                        for logFunc in self._log("handle-trx-element-create-testgenerationunderscorelist-functor-exception").exceptionFunc():
                            logFunc("TestGenerationUnderscoreList's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateTestGenerationUnderscoreListFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-testgenerationunderscorelist-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): testgenerationunderscorelist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-testgenerationunderscorelist-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): testgenerationunderscorelist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTransparentContainer)):
                if (self.myCreateTransparentContainerFunctor):
                    if (not self.myTransparentContainer):
                        for logFunc in self._log("handle-trx-element-create-transparentcontainer-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): transparentcontainer not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-transparentcontainer-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.TRANSPARENTCONTAINER_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.TRANSPARENTCONTAINER_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateTransparentContainerFunctor(phase, self.myTransparentContainer)
                    except:
                        for logFunc in self._log("handle-trx-element-create-transparentcontainer-functor-exception").exceptionFunc():
                            logFunc("TransparentContainer's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateTransparentContainerFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-transparentcontainer-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): transparentcontainer functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-transparentcontainer-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): transparentcontainer functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.myAntenna):
            self.myAntenna.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myTestGenerationUnderscoreList):
            self.myTestGenerationUnderscoreList.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myTransparentContainer):
            self.myTransparentContainer.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagAntenna)):
                res = self.activateDeleteAntennaFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-antenna-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): antenna functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-antenna-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): antenna functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTestGenerationUnderscoreList)):
                res = self.activateDeleteTestGenerationUnderscoreListFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-testgenerationunderscorelist-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): testgenerationunderscorelist functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-testgenerationunderscorelist-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): testgenerationunderscorelist functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagTransparentContainer)):
                res = self.activateDeleteTransparentContainerFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-transparentcontainer-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): transparentcontainer functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-transparentcontainer-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): transparentcontainer functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    
    def removeAntenna(self):
        self.myAntenna = None

    def activateDeleteAntennaFunctor(self, phase):
        for logFunc in self._log("activate-delete-antenna-functor").debug3Func(): logFunc("activateDeleteAntennaFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteAntennaFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-antenna-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.ANTENNA_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.ANTENNA_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteAntennaFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-antenna-functor-exception").exceptionFunc():
                        logFunc("Antenna's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteAntennaFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-antenna-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteAntennaFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-antenna-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteAntennaFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeTestGenerationUnderscoreList(self):
        self.myTestGenerationUnderscoreList = None

    def activateDeleteTestGenerationUnderscoreListFunctor(self, phase):
        for logFunc in self._log("activate-delete-testgenerationunderscorelist-functor").debug3Func(): logFunc("activateDeleteTestGenerationUnderscoreListFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteTestGenerationUnderscoreListFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-testgenerationunderscorelist-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.TESTGENERATIONUNDERSCORELIST_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.TESTGENERATIONUNDERSCORELIST_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteTestGenerationUnderscoreListFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-testgenerationunderscorelist-functor-exception").exceptionFunc():
                        logFunc("TestGenerationUnderscoreList's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteTestGenerationUnderscoreListFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-testgenerationunderscorelist-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteTestGenerationUnderscoreListFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-testgenerationunderscorelist-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteTestGenerationUnderscoreListFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeTransparentContainer(self):
        self.myTransparentContainer = None

    def activateDeleteTransparentContainerFunctor(self, phase):
        for logFunc in self._log("activate-delete-transparentcontainer-functor").debug3Func(): logFunc("activateDeleteTransparentContainerFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteTransparentContainerFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-transparentcontainer-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.TRANSPARENTCONTAINER_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.TRANSPARENTCONTAINER_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteTransparentContainerFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-transparentcontainer-functor-exception").exceptionFunc():
                        logFunc("TransparentContainer's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteTransparentContainerFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-transparentcontainer-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteTransparentContainerFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-transparentcontainer-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteTransparentContainerFunctor(): functor failed, phase=%s", phase)
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
        self.myCandidateData = FishData()
        
        res = self.setTransparentFieldDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-transparentfield-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setTransparentFieldDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setColorDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-color-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setColorDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setEyeNumberDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-eyenumber-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setEyeNumberDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setHasTailDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-hastail-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setHasTailDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setFinNumberDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-finnumber-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setFinNumberDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setLengthDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-length-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setLengthDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setIp6DefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-ip6-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setIp6DefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setIdDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-id-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setIdDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setTransparentFieldDefaultValue (self, setHas):
        for logFunc in self._log("set-transparentfield-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.transparentField = False
            
        if setHas:
            self.myCandidateData.setHasTransparentField()

        return ReturnCodes.kOk

    def setColorDefaultValue (self, setHas):
        for logFunc in self._log("set-color-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.color = ColorT.kRed
            
        if setHas:
            self.myCandidateData.setHasColor()

        return ReturnCodes.kOk

    def setEyeNumberDefaultValue (self, setHas):
        for logFunc in self._log("set-eyenumber-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.eyeNumber = 0
            
        if setHas:
            self.myCandidateData.setHasEyeNumber()

        return ReturnCodes.kOk

    def setHasTailDefaultValue (self, setHas):
        for logFunc in self._log("set-hastail-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.hasTail = False
            
        if setHas:
            self.myCandidateData.setHasHasTail()

        return ReturnCodes.kOk

    def setFinNumberDefaultValue (self, setHas):
        for logFunc in self._log("set-finnumber-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.finNumber = 0
            
        if setHas:
            self.myCandidateData.setHasFinNumber()

        return ReturnCodes.kOk

    def setLengthDefaultValue (self, setHas):
        for logFunc in self._log("set-length-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.length = 0
            
        if setHas:
            self.myCandidateData.setHasLength()

        return ReturnCodes.kOk

    def setIp6DefaultValue (self, setHas):
        for logFunc in self._log("set-ip6-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.ip6 = None
            
        if setHas:
            self.myCandidateData.setHasIp6()

        return ReturnCodes.kOk

    def setIdDefaultValue (self, setHas):
        for logFunc in self._log("set-id-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.id = ""
            
        if setHas:
            self.myCandidateData.setHasId()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = FishData()
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
        self.myRunningData = FishData()
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyfish-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyfish-failed").errorFunc():
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
                
                if (self.myAntenna):
                    res = self.myAntenna.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-antenna-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-antenna-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myTestGenerationUnderscoreList):
                    res = self.myTestGenerationUnderscoreList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-testgenerationunderscorelist-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-testgenerationunderscorelist-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myTransparentContainer):
                    res = self.myTransparentContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-transparentcontainer-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-transparentcontainer-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.myAntenna):
                    res = self.activateDeleteAntennaFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-antenna-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAntennaFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myAntenna):
                    res = self.myAntenna.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-antenna-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAntenna.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myTestGenerationUnderscoreList):
                    res = self.activateDeleteTestGenerationUnderscoreListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-testgenerationunderscorelist-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteTestGenerationUnderscoreListFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myTestGenerationUnderscoreList):
                    res = self.myTestGenerationUnderscoreList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-testgenerationunderscorelist-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myTestGenerationUnderscoreList.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.myTransparentContainer):
                    res = self.activateDeleteTransparentContainerFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-transparentcontainer-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteTransparentContainerFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.myTransparentContainer):
                    res = self.myTransparentContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-transparentcontainer-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myTransparentContainer.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                if (self.myAntenna):
                    res = self.myAntenna.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-antenna-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myAntenna.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeAntenna()
                
                if (self.myTestGenerationUnderscoreList):
                    res = self.myTestGenerationUnderscoreList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-testgenerationunderscorelist-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myTestGenerationUnderscoreList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeTestGenerationUnderscoreList()
                
                if (self.myTransparentContainer):
                    res = self.myTransparentContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-transparentcontainer-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myTransparentContainer.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeTransparentContainer()
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myAntenna):
                    res = self.myAntenna.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-antenna-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAntenna.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteAntennaFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-antenna-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAntennaFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteAntennaFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myTestGenerationUnderscoreList):
                    res = self.myTestGenerationUnderscoreList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-testgenerationunderscorelist-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myTestGenerationUnderscoreList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteTestGenerationUnderscoreListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-testgenerationunderscorelist-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteTestGenerationUnderscoreListFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteTestGenerationUnderscoreListFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.myTransparentContainer):
                    res = self.myTransparentContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-transparentcontainer-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myTransparentContainer.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteTransparentContainerFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-transparentcontainer-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteTransparentContainerFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteTransparentContainerFunctor failed in commit phase (private/public)")
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
                
                if (self.myAntenna):
                    res = self.myAntenna.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-antenna-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myAntenna.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myTestGenerationUnderscoreList):
                    res = self.myTestGenerationUnderscoreList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-testgenerationunderscorelist-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myTestGenerationUnderscoreList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myTransparentContainer):
                    res = self.myTransparentContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-transparentcontainer-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): myTransparentContainer.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
                if (self.myAntenna):
                    res = self.myAntenna.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-antenna-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myAntenna.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myAntenna):
                    res = self.activateDeleteAntennaFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-antenna-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteAntennaFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myTestGenerationUnderscoreList):
                    res = self.myTestGenerationUnderscoreList.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-testgenerationunderscorelist-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myTestGenerationUnderscoreList.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myTestGenerationUnderscoreList):
                    res = self.activateDeleteTestGenerationUnderscoreListFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-testgenerationunderscorelist-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteTestGenerationUnderscoreListFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.myTransparentContainer):
                    res = self.myTransparentContainer.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-transparentcontainer-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): myTransparentContainer.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.myTransparentContainer):
                    res = self.activateDeleteTransparentContainerFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-transparentcontainer-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteTransparentContainerFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.sys.blinky.example.lake_example.lake.fish_.fish__data_gen import FishData", 
        "moduleYangNamespacePrefix": "lake-example", 
        "validationPoint": null, 
        "yangName": "fish", 
        "namespace": "fish_", 
        "logGroupName": "blinky-fish", 
        "className": "BlinkyFish", 
        "logModuleName": "a-sys-blinky-example-lake-example-lake-fish--blinky-fish--gen", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.blinky_fish__gen import BlinkyFish", 
        "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
        "dataClassName": "FishData", 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "lake", 
            "namespace": "lake", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "lake", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lake"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": true, 
            "yangName": "fish", 
            "namespace": "fish_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "fish_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fish_"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkyAntenna", 
            "memberName": "Antenna", 
            "yangName": "antenna", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.blinky_antenna_gen import BlinkyAntenna"
        }, 
        {
            "className": "BlinkyTestGenerationUnderscoreList", 
            "memberName": "TestGenerationUnderscoreList", 
            "yangName": "test-generation_underscore", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.test_generation_underscore.blinky_test_generation_underscore_list_gen import BlinkyTestGenerationUnderscoreList"
        }, 
        {
            "className": "BlinkyTransparentContainer", 
            "memberName": "TransparentContainer", 
            "yangName": "transparent-container", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.transparent_container.blinky_transparent_container_gen import BlinkyTransparentContainer"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "finNumber", 
            "yangName": "fin-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "ip6", 
            "yangName": "ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "env": [
        "a", 
        "sys", 
        "blinky", 
        "example", 
        "lake_example"
    ], 
    "createTime": "2013"
}
"""

