


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

from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.fan_data_gen import FanData


from a.sys.platform.tech_platform_fans.tech.platform.fans.fan.simulation.blinky_simulation_gen import BlinkySimulation

from a.sys.platform.tech_platform_fans.tech.platform.fans.fan.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults

from a.sys.platform.tech_platform_fans.tech.platform.fans.fan.device.blinky_device_gen import BlinkyDevice




class BlinkyFan(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"
    #leaves
    
    ourXmlTagName="name"
    
    ourXmlTagMuteReporting="mute-reporting"
    
    ourXmlTagLocation="location"
    

    #descendants
    
    ourXmlTagSimulation="simulation"
    
    ourXmlTagSystemDefaults="system-defaults"
    
    ourXmlTagDevice="device"
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    SIMULATION_CREATE_FUNCTOR = 'SIMULATION_CREATE_FUNCTOR'
    SIMULATION_DELETE_FUNCTOR = 'SIMULATION_DELETE_FUNCTOR'
    
    SYSTEMDEFAULTS_CREATE_FUNCTOR = 'SYSTEMDEFAULTS_CREATE_FUNCTOR'
    SYSTEMDEFAULTS_DELETE_FUNCTOR = 'SYSTEMDEFAULTS_DELETE_FUNCTOR'
    
    DEVICE_CREATE_FUNCTOR = 'DEVICE_CREATE_FUNCTOR'
    DEVICE_DELETE_FUNCTOR = 'DEVICE_DELETE_FUNCTOR'
    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myCreateSimulationFunctor=None
        self.myDeleteSimulationFunctor=None
        self.mySimulation=None
        
        self.myCreateSystemDefaultsFunctor=None
        self.myDeleteSystemDefaultsFunctor=None
        self.mySystemDefaults=None
        
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
                  
                  
                  
                  
                  fan, 
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkyfan').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyFan._validationPointId, BlinkyFan._actionPointId)

        confd_key=KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(fan);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fan", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fans", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("platform", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", "qt-pltf"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyFan(logger)
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

    
    def setCreateSimulationFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-simulation-functor-active").errorFunc():
                logFunc("setCreateSimulationFunctor() is illegal when blinky node is active")
        self.myCreateSimulationFunctor = functor

    def setDeleteSimulationFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-simulation-functor-active").errorFunc():
                logFunc("setDeleteSimulationFunctor() is illegal when blinky node is active")
        self.myDeleteSimulationFunctor = functor
    
    def setCreateSystemDefaultsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-create-system-defaults-functor-active").errorFunc():
                logFunc("setCreateSystemDefaultsFunctor() is illegal when blinky node is active")
        self.myCreateSystemDefaultsFunctor = functor

    def setDeleteSystemDefaultsFunctor(self, functor):
        if (self.myIsActive):
            for logFunc in self._log("set-delete-system-defaults-functor-active").errorFunc():
                logFunc("setDeleteSystemDefaultsFunctor() is illegal when blinky node is active")
        self.myDeleteSystemDefaultsFunctor = functor
    
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
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagName)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.name = newValue.asString()
                self.myCandidateData.setHasName()
                
            else:
                self.setNameDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMuteReporting)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.muteReporting = newValue.asBool()
                self.myCandidateData.setHasMuteReporting()
                
            else:
                self.setMuteReportingDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLocation)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.location = newValue.asString()
                self.myCandidateData.setHasLocation()
                
            else:
                self.setLocationDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagSimulation)):
            return self.mySimulation
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagSystemDefaults)):
            return self.mySystemDefaults
        
        if (keyPath.isTagEqual(keyDepth_PBR.value(), self.ourNamespace, self.ourXmlTagDevice)):
            return self.myDevice
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyfan').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.platform.tech_platform_fans.tech.platform.fans.fan.blinky_fan_gen import BlinkyFan', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagSimulation)):
                    keyPathRegistered = BlinkySimulation.isKeyPathRegistered(logger, keyPath, keyDepth+1)
                    found = True
            else:
                keyPathRegistered = True
                found = True
        
        if not found:
            if keyPath.getLen() > keyDepth+1:
                if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagSystemDefaults)):
                    keyPathRegistered = BlinkySystemDefaults.isKeyPathRegistered(logger, keyPath, keyDepth+1)
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
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagName)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMuteReporting)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagLocation)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkyfan-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.platform.tech_platform_fans.tech.platform.fans.fan.blinky_fan_gen import BlinkyFan', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSimulation)):
            if (self.mySimulation):
                for logFunc in self._log("prepare-my-blinky-node-simulation-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.mySimulation = BlinkySimulation(self._log)
            self.mySimulation.setParent(self)
            self.mySimulation.setKeyPath(keyPath)
            self.mySimulation.setDomain(self.myDomain)

            return self.mySimulation
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSystemDefaults)):
            if (self.mySystemDefaults):
                for logFunc in self._log("prepare-my-blinky-node-systemdefaults-already-exists").errorFunc():
                    logFunc("prepareMyBlinkyNode(): already exists, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
                return None
            self.mySystemDefaults = BlinkySystemDefaults(self._log)
            self.mySystemDefaults.setParent(self)
            self.mySystemDefaults.setKeyPath(keyPath)
            self.mySystemDefaults.setDomain(self.myDomain)

            return self.mySystemDefaults
        
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
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSimulation)):
            self.mySimulation = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSystemDefaults)):
            self.mySystemDefaults = None
            return
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDevice)):
            self.myDevice = None
            return
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSimulation)):
                if (self.myCreateSimulationFunctor):
                    if (not self.mySimulation):
                        for logFunc in self._log("handle-trx-element-create-simulation-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): simulation not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-simulation-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.SIMULATION_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.SIMULATION_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateSimulationFunctor(phase, self.mySimulation)
                    except:
                        for logFunc in self._log("handle-trx-element-create-simulation-functor-exception").exceptionFunc():
                            logFunc("Simulation's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateSimulationFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-simulation-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): simulation functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-simulation-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): simulation functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSystemDefaults)):
                if (self.myCreateSystemDefaultsFunctor):
                    if (not self.mySystemDefaults):
                        for logFunc in self._log("handle-trx-element-create-systemdefaults-not-exist").debug3Func():
                            logFunc("handleTrxElementCreate(): systemdefaults not exists, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        return ReturnCodes.kGeneralError
    
                    timeoutGuard = TimeoutGuard(self._log, '%s-create-systemdefaults-functor-%s' % (self.myKeyPath, phase), 
                                                self.getFunctorTimeoutForPhase(self.SYSTEMDEFAULTS_CREATE_FUNCTOR, phase),
                                                self.getFunctorMildTimeoutForPhase(self.SYSTEMDEFAULTS_CREATE_FUNCTOR, phase))
                    try:
                        res = self.myCreateSystemDefaultsFunctor(phase, self.mySystemDefaults)
                    except:
                        for logFunc in self._log("handle-trx-element-create-systemdefaults-functor-exception").exceptionFunc():
                            logFunc("SystemDefaults's create functor raised an exception. trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                        raise
                    timeoutGuard.checkAndLog("application problem: functor=%s" % self.myCreateSystemDefaultsFunctor.__name__)
                    if (res != ReturnCodes.kOk):
                        if (phase.getConfdPhase() == TrxPhase.kPrepare):
                            for logFunc in self._log("handle-trx-element-create-systemdefaults-functor-failed-prepare").noticeFunc():
                                logFunc("handleTrxElementCreate(): systemdefaults functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                       trxElement, keyDepth, phase)
                            self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        else:
                            for logFunc in self._log("handle-trx-element-create-systemdefaults-functor-failed").errorFunc():
                                logFunc("handleTrxElementCreate(): systemdefaults functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

        
        if (self.mySimulation):
            self.mySimulation.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.mySystemDefaults):
            self.mySystemDefaults.notifyDescendantsPrepareBlinkyDelete()
        
        if (self.myDevice):
            self.myDevice.notifyDescendantsPrepareBlinkyDelete()
        

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSimulation)):
                res = self.activateDeleteSimulationFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-simulation-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): simulation functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-simulation-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): simulation functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                    return ReturnCodes.kGeneralError
            
            if (trxElement.getKeyPath().isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSystemDefaults)):
                res = self.activateDeleteSystemDefaultsFunctor(phase)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("handle-trx-element-delete-systemdefaults-functor-failed-prepare").noticeFunc():
                            logFunc("handleTrxElementDelete(): systemdefaults functor-failed-prepare, trxElement=%s, keyDepth=%s, phase=%s",
                                   trxElement, keyDepth, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("handle-trx-element-delete-systemdefaults-functor-failed").errorFunc():
                            logFunc("handleTrxElementDelete(): systemdefaults functor-failed, trxElement=%s, keyDepth=%s, phase=%s",
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

    
    def removeSimulation(self):
        self.mySimulation = None

    def activateDeleteSimulationFunctor(self, phase):
        for logFunc in self._log("activate-delete-simulation-functor").debug3Func(): logFunc("activateDeleteSimulationFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteSimulationFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-simulation-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.SIMULATION_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.SIMULATION_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteSimulationFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-simulation-functor-exception").exceptionFunc():
                        logFunc("Simulation's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteSimulationFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-simulation-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteSimulationFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-simulation-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteSimulationFunctor(): functor failed, phase=%s", phase)
                    return ReturnCodes.kGeneralError
        return ReturnCodes.kOk
    
    def removeSystemDefaults(self):
        self.mySystemDefaults = None

    def activateDeleteSystemDefaultsFunctor(self, phase):
        for logFunc in self._log("activate-delete-systemdefaults-functor").debug3Func(): logFunc("activateDeleteSystemDefaultsFunctor(): called, phase=%s", phase)
        if (self.myIsActive):
            if (self.myDeleteSystemDefaultsFunctor):
                timeoutGuard = TimeoutGuard(self._log, '%s-delete-systemdefaults-functor-%s' % (self.myKeyPath, phase), 
                                            self.getFunctorTimeoutForPhase(self.SYSTEMDEFAULTS_DELETE_FUNCTOR, phase), 
                                            self.getFunctorMildTimeoutForPhase(self.SYSTEMDEFAULTS_DELETE_FUNCTOR, phase))
                try:
                    res = self.myDeleteSystemDefaultsFunctor(phase)
                except:
                    for logFunc in self._log("activate-delete-systemdefaults-functor-exception").exceptionFunc():
                        logFunc("SystemDefaults's delete functor raised an exception. phase=%s", phase)
                    raise
                timeoutGuard.checkAndLog("application problem: functor=%s" % self.myDeleteSystemDefaultsFunctor.__name__)
                if (res != ReturnCodes.kOk):
                    if (phase.getConfdPhase() == TrxPhase.kPrepare):
                        for logFunc in self._log("activate-delete-systemdefaults-functor-functor-failed-prepare").noticeFunc():
                            logFunc("activateDeleteSystemDefaultsFunctor(): functor failed, phase=%s", phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                    else:
                        for logFunc in self._log("activate-delete-systemdefaults-functor-functor-failed").errorFunc():
                            logFunc("activateDeleteSystemDefaultsFunctor(): functor failed, phase=%s", phase)
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
        self.myCandidateData = FanData()
        
        res = self.setNameDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-name-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setNameDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setMuteReportingDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-mutereporting-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMuteReportingDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setLocationDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-location-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setLocationDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setNameDefaultValue (self, setHas):
        for logFunc in self._log("set-name-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.name = ""
            
        if setHas:
            self.myCandidateData.setHasName()

        return ReturnCodes.kOk

    def setMuteReportingDefaultValue (self, setHas):
        for logFunc in self._log("set-mutereporting-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.muteReporting = False
            
        if setHas:
            self.myCandidateData.setHasMuteReporting()

        return ReturnCodes.kOk

    def setLocationDefaultValue (self, setHas):
        for logFunc in self._log("set-location-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.location = ""
            
        if setHas:
            self.myCandidateData.setHasLocation()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = FanData()
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
        self.myRunningData = FanData()
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyfan-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyfan-failed").errorFunc():
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
                
                if (self.mySimulation):
                    res = self.mySimulation.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulation-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-simulation-recursion-failed-prepare-blinky, phase=%s",
                                  phase)
                        return ReturnCodes.kGeneralError
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-prepare-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): delete-systemdefaults-recursion-failed-prepare-blinky, phase=%s",
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
                
                if (self.mySimulation):
                    res = self.activateDeleteSimulationFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulation-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSimulationFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.mySimulation):
                    res = self.mySimulation.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulation-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySimulation.handleInternalDestroy() failed, res=%s, phase=%s",
                                   res, phase)
                        return ReturnCodes.kGeneralError
                
                if (self.mySystemDefaults):
                    res = self.activateDeleteSystemDefaultsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-functor-failed-prepare").noticeFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSystemDefaultsFunctor() failed, res=%s, phase=%s",
                                   res, phase)
                        self.myDomain.setConfigErrorStr(self.myConfigErrorStr)
                        return ReturnCodes.kGeneralError
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-prepare-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
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
                
                if (self.mySimulation):
                    res = self.mySimulation.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulation-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySimulation.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeSimulation()
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-commit-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (blinky)")
                        return ReturnCodes.kGeneralError
                    self.removeSystemDefaults()
                
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
                
                if (self.mySimulation):
                    res = self.mySimulation.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulation-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySimulation.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteSimulationFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulation-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSimulationFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteSimulationFunctor failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-commit-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("handle internal destroy failed in commit phase (private/public)")
                        return ReturnCodes.kGeneralError
                    res = self.activateDeleteSystemDefaultsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-functor-failed-commit").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSystemDefaultsFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("activateDeleteSystemDefaultsFunctor failed in commit phase (private/public)")
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
                
                if (self.mySimulation):
                    res = self.mySimulation.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulation-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySimulation.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-abort-blinky").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
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
                
                if (self.mySimulation):
                    res = self.mySimulation.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulation-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySimulation.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.mySimulation):
                    res = self.activateDeleteSimulationFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-simulation-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSimulationFunctor() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("delete functor failed in abort (blinky)")
                        return ReturnCodes.kOk
                
                if (self.mySystemDefaults):
                    res = self.mySystemDefaults.handleInternalDestroy(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-recursion-failed-abort-private-or-public").errorFunc():
                            logFunc("handleInternalDestroy(): mySystemDefaults.handleInternalDestroy() failed, res=%s, phase=%s",
                                  res, phase)
                        a.infra.process.processFatal("internal destroy failed in abort (private/public)")
                        return ReturnCodes.kOk
                if (self.mySystemDefaults):
                    res = self.activateDeleteSystemDefaultsFunctor(phase)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-internal-destroy-delete-systemdefaults-functor-failed-abort").errorFunc():
                            logFunc("handleInternalDestroy(): activateDeleteSystemDefaultsFunctor() failed, res=%s, phase=%s",
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
        "dataImportStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.fan_data_gen import FanData", 
        "moduleYangNamespacePrefix": "qt-pltf-fans", 
        "validationPoint": null, 
        "yangName": "fan", 
        "namespace": "fan", 
        "logGroupName": "blinky-fan", 
        "className": "BlinkyFan", 
        "logModuleName": "a-sys-platform-tech-platform-fans-tech-platform-fans-fan-blinky-fan-gen", 
        "importStatement": "from a.sys.platform.tech_platform_fans.tech.platform.fans.fan.blinky_fan_gen import BlinkyFan", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
        "dataClassName": "FanData", 
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
            "moduleYangNamespacePrefix": "qt-pltf", 
            "yangName": "platform", 
            "namespace": "platform", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", 
            "name": "platform"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "yangName": "fans", 
            "namespace": "fans", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "fans"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "isCurrent": true, 
            "yangName": "fan", 
            "namespace": "fan", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "keyLeaf": {
                "varName": "fan", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fan"
        }
    ], 
    "descendants": [
        {
            "className": "BlinkySimulation", 
            "memberName": "Simulation", 
            "yangName": "simulation", 
            "importStatement": "from a.sys.platform.tech_platform_fans.tech.platform.fans.fan.simulation.blinky_simulation_gen import BlinkySimulation"
        }, 
        {
            "className": "BlinkySystemDefaults", 
            "memberName": "SystemDefaults", 
            "yangName": "system-defaults", 
            "importStatement": "from a.sys.platform.tech_platform_fans.tech.platform.fans.fan.system_defaults.blinky_system_defaults_gen import BlinkySystemDefaults"
        }, 
        {
            "className": "BlinkyDevice", 
            "memberName": "Device", 
            "yangName": "device", 
            "importStatement": "from a.sys.platform.tech_platform_fans.tech.platform.fans.fan.device.blinky_device_gen import BlinkyDevice"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
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
        "platform", 
        "tech_platform_fans"
    ], 
    "createTime": "2013"
}
"""

