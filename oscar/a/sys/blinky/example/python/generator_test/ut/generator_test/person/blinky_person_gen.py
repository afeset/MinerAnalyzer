


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

from a.sys.blinky.example.python.generator_test.ut.generator_test.person.person_data_gen import PersonData



from a.infra.net.mac_address import MacAddress
from a.sys.blinky.example.python.generator_test.ut.generator_test_types.generator_test_types_module_gen import GenderT
import struct


class BlinkyPerson(BlinkyContainer):
    ourNamespace="http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"
    #leaves
    
    ourXmlTagHomeIp="home-ip"
    
    ourXmlTagName="name"
    
    ourXmlTagGender="gender"
    
    ourXmlTagNumber="number"
    
    ourXmlTagMobileIp="mobile-ip"
    
    ourXmlTagHomeIp6="home-ip6"
    
    ourXmlTagOfficeIp6="office-ip6"
    
    ourXmlTagOfficeIp="office-ip"
    
    ourXmlTagDesiredGender="desired-gender"
    
    ourXmlTagLinux_="linux"
    
    ourXmlTagSecondaryNumber="secondary-number"
    
    ourXmlTagEmployed="employed"
    
    ourXmlTagHeight="height"
    
    ourXmlTagMacAddress="mac-address"
    

    #descendants
    

    _validationPointId=None
    
    _actionPointId=None
    

    
    VALUE_SET_FUNCTOR = 'VALUE_SET_FUNCTOR'
    VALIDATE_TRX_FUNCTOR = 'VALIDATE_TRX_FUNCTOR'
    DO_ACTION_FUNCTOR = 'DO_ACTION_FUNCTOR'

    # Improve performance: Store hashed values of these strings here as well.

    def __init__ (self, logger):
        BlinkyContainer.__init__(self, logger)
        
        self.myValueSetFunctor=None
        self.myCandidateData=None
        self.myRunningData=None
        self.isInDestroy = False
        
        self.validateRegistrationDone = False
        self.actionRegistrationDone=False
        
        

    @classmethod
    def s_create (cls, logger, 
                  
                  person, 
                  domain):
        __pychecker__="no-argsused"

        logger('s-create-blinkyperson').info('called. domain=%s, _validationPointId=%s, _actionPointId=%s', domain, BlinkyPerson._validationPointId, BlinkyPerson._actionPointId)

        confd_key=KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(person);
        confd_key.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("people", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", "le"))
        confd_key.addKeyPathPrefix(xmlVal)
        
        newNode=BlinkyPerson(logger)
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

    

    

    

    def trxElementUpdateCandidate(self, trxElement, keyDepth):
        keyPath = trxElement.getKeyPath()
        for logFunc in self._log("trx-element-update-candidate").debug3Func():
            logFunc("trxElementUpdateCandidate(): called, keyPath=%s, keyDepth=%s, trxElement=%s", keyPath, keyDepth, trxElement)
        
        
        if (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagHomeIp)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.homeIp = (newValue.asIPv4())
                self.myCandidateData.setHasHomeIp()
                
            else:
                self.setHomeIpDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagName)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.name = newValue.asString()
                self.myCandidateData.setHasName()
                
            else:
                self.setNameDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagGender)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not GenderT.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-gender-failed")\
                        .error("illegal enum value %s for gender", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.gender = GenderT.getByValue(newValue.asEnum())
                self.myCandidateData.setHasGender()
                
            else:
                self.setGenderDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagNumber)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.number = newValue.asString()
                self.myCandidateData.setHasNumber()
                
            else:
                self.setNumberDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMobileIp)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.mobileIp = newValue.asString()
                self.myCandidateData.setHasMobileIp()
                
            else:
                self.setMobileIpDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagHomeIp6)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.homeIp6 = (newValue.asIPv6())
                self.myCandidateData.setHasHomeIp6()
                
            else:
                self.setHomeIp6DefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOfficeIp6)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.officeIp6 = (newValue.asIPv6Prefix())
                self.myCandidateData.setHasOfficeIp6()
                
            else:
                self.setOfficeIp6DefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagOfficeIp)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.officeIp = (newValue.asIPv4Prefix())
                self.myCandidateData.setHasOfficeIp()
                
            else:
                self.setOfficeIpDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagDesiredGender)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                if not GenderT.isValidValue(newValue.asEnum()):
                    self._log("trx-element-update-candidate-illegal-enum-desiredgender-failed")\
                        .error("illegal enum value %s for desiredGender", newValue.asEnum())
                    return ReturnCodes.kGeneralError
                self.myCandidateData.desiredGender = GenderT.getByValue(newValue.asEnum())
                self.myCandidateData.setHasDesiredGender()
                
            else:
                self.setDesiredGenderDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagLinux_)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.linux_ = newValue.asString()
                self.myCandidateData.setHasLinux_()
                
            else:
                self.setLinux_DefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagSecondaryNumber)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.secondaryNumber = newValue.asString()
                self.myCandidateData.setHasSecondaryNumber()
                
            else:
                self.setSecondaryNumberDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagEmployed)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.employed = newValue.asBool()
                self.myCandidateData.setHasEmployed()
                
            else:
                self.setEmployedDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagHeight)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.height = newValue.asInt64()
                self.myCandidateData.setHasHeight()
                
            else:
                self.setHeightDefaultValue(True)
            
        elif (keyPath.isTagEqual(keyDepth, self.ourNamespace, self.ourXmlTagMacAddress)):
            if trxElement.getNewVal():
                newValue = trxElement.getNewVal()
                self.myCandidateData.macAddress = MacAddress(newValue.asBinary())
                self.myCandidateData.setHasMacAddress()
                
            else:
                self.setMacAddressDefaultValue(True)
            
        for logFunc in self._log("trx-element-update-candidate-done").debug3Func():
            logFunc("trxElementUpdateCandidate(): After update, candidate is %s", self.myCandidateData)
    
    def getDescendant(self, keyPath, keyDepth_PBR):
        for logFunc in self._log("get-descendant").debug3Func(): logFunc("getDescendant(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        
        for logFunc in self._log("get-descendant-unknown").debug3Func(): logFunc("getDescendant(): unknown, keyPath=%s, keyDepth=%s", keyPath, keyDepth_PBR)
        return None
    
    @classmethod
    def isKeyPathRegistered (cls, logger, keyPath, keyDepth):
        __pychecker__="no-argsused no-local"
        logger('is-key-path-registered-blinkyperson').debug3('isKeyPathRegistered() called. keyPath=%s, keyDepth=%d, I am: from a.sys.blinky.example.python.generator_test.ut.generator_test.person.blinky_person_gen import BlinkyPerson', keyPath, keyDepth)
        keyPathRegistered = False
        found = False
        
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagHomeIp)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagName)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagGender)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagNumber)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMobileIp)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagHomeIp6)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagOfficeIp6)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagOfficeIp)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagDesiredGender)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagLinux_)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagSecondaryNumber)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagEmployed)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagHeight)):
                keyPathRegistered = True
                found = True
        
        if not found:
            if (keyPath.isTagEqual(keyDepth, cls.ourNamespace, cls.ourXmlTagMacAddress)):
                keyPathRegistered = True
                found = True
        
        logger('is-key-path-registered-blinkyperson-done').debug3('isKeyPathRegistered() done. registered=%s. keyPath=%s, keyDepth=%d, I am: from a.sys.blinky.example.python.generator_test.ut.generator_test.person.blinky_person_gen import BlinkyPerson', keyPathRegistered, keyPath, keyDepth)
        return keyPathRegistered

    def prepareMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("prepare-my-blinky-node").debug3Func(): logFunc("prepareMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        
        for logFunc in self._log("prepare-my-blinky-not-found").errorFunc():
            logFunc("prepareMyBlinkyNode(): not found, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        return None
    
    def abortMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("abort-my-blinky-node").debug3Func(): logFunc("abortMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        self.deleteMyBlinkyNode(keyPath, keyDepth)
    
    def deleteMyBlinkyNode(self, keyPath, keyDepth):
        for logFunc in self._log("delete-my-blinky-node").debug3Func(): logFunc("deleteMyBlinkyNode(): called, keyPath=%s, keyDepth=%s", keyPath, keyDepth)
        

    def handleTrxElementCreate(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-create-details").debug3Func():
            logFunc("handleTrxElementCreate(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            
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

        pass

        for logFunc in self._log("notify-descendants-prepare-blinky-delete-done").debug2Func(): logFunc("done")

    def handleTrxElementDelete(self, trxElement, keyDepth, phase):
        for logFunc in self._log("handle-trx-element-delete-details").debug3Func():
            logFunc("handleTrxElementDelete(): called, element-key-path=%s, element-op-code=%s, keyDepth=%s, phase=%s",
                   trxElement.getKeyPath(), trxElement.getOpCode(), keyDepth, phase)
        if (self.myIsActive):
            pass
        # if a leaf is deleted - notify candidate date changed
        return self.notifyWithCandidate(phase)

    

    

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
        self.myCandidateData = PersonData()
        
        res = self.setHomeIpDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-homeip-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setHomeIpDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setNameDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-name-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setNameDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setGenderDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-gender-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setGenderDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setNumberDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-number-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setNumberDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setMobileIpDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-mobileip-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMobileIpDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setHomeIp6DefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-homeip6-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setHomeIp6DefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setOfficeIp6DefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-officeip6-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setOfficeIp6DefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setOfficeIpDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-officeip-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setOfficeIpDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setDesiredGenderDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-desiredgender-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setDesiredGenderDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setLinux_DefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-linux_-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setLinux_DefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setSecondaryNumberDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-secondarynumber-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setSecondaryNumberDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setEmployedDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-employed-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setEmployedDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setHeightDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-height-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setHeightDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        res = self.setMacAddressDefaultValue(True)
        if res != ReturnCodes.kOk:
            for logFunc in self._log("alloc-my-candidate-set-macaddress-default-value-failed").errorFunc():
                logFunc("allocMyCandidate(): setMacAddressDefaultValue failed. res=%s",
                      res)
            return ReturnCodes.kGeneralError
        
        return ReturnCodes.kOk

    def setHomeIpDefaultValue (self, setHas):
        for logFunc in self._log("set-homeip-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.homeIp = None
            
        if setHas:
            self.myCandidateData.setHasHomeIp()

        return ReturnCodes.kOk

    def setNameDefaultValue (self, setHas):
        for logFunc in self._log("set-name-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.name = ""
            
        if setHas:
            self.myCandidateData.setHasName()

        return ReturnCodes.kOk

    def setGenderDefaultValue (self, setHas):
        for logFunc in self._log("set-gender-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.gender = GenderT.kMale
            
        if setHas:
            self.myCandidateData.setHasGender()

        return ReturnCodes.kOk

    def setNumberDefaultValue (self, setHas):
        for logFunc in self._log("set-number-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.number = "123"
            
        if setHas:
            self.myCandidateData.setHasNumber()

        return ReturnCodes.kOk

    def setMobileIpDefaultValue (self, setHas):
        for logFunc in self._log("set-mobileip-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.mobileIp = ""
            
        if setHas:
            self.myCandidateData.setHasMobileIp()

        return ReturnCodes.kOk

    def setHomeIp6DefaultValue (self, setHas):
        for logFunc in self._log("set-homeip6-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.homeIp6 = None
            
        if setHas:
            self.myCandidateData.setHasHomeIp6()

        return ReturnCodes.kOk

    def setOfficeIp6DefaultValue (self, setHas):
        for logFunc in self._log("set-officeip6-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.officeIp6 = None
            
        if setHas:
            self.myCandidateData.setHasOfficeIp6()

        return ReturnCodes.kOk

    def setOfficeIpDefaultValue (self, setHas):
        for logFunc in self._log("set-officeip-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.officeIp = None
            
        if setHas:
            self.myCandidateData.setHasOfficeIp()

        return ReturnCodes.kOk

    def setDesiredGenderDefaultValue (self, setHas):
        for logFunc in self._log("set-desiredgender-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.desiredGender = GenderT.kMale
            
        if setHas:
            self.myCandidateData.setHasDesiredGender()

        return ReturnCodes.kOk

    def setLinux_DefaultValue (self, setHas):
        for logFunc in self._log("set-linux_-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.linux_ = ""
            
        if setHas:
            self.myCandidateData.setHasLinux_()

        return ReturnCodes.kOk

    def setSecondaryNumberDefaultValue (self, setHas):
        for logFunc in self._log("set-secondarynumber-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.secondaryNumber = "789"
            
        if setHas:
            self.myCandidateData.setHasSecondaryNumber()

        return ReturnCodes.kOk

    def setEmployedDefaultValue (self, setHas):
        for logFunc in self._log("set-employed-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.employed = False
            
        if setHas:
            self.myCandidateData.setHasEmployed()

        return ReturnCodes.kOk

    def setHeightDefaultValue (self, setHas):
        for logFunc in self._log("set-height-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.height = 175
            
        if setHas:
            self.myCandidateData.setHasHeight()

        return ReturnCodes.kOk

    def setMacAddressDefaultValue (self, setHas):
        for logFunc in self._log("set-macaddress-default-value").debug3Func():
            logFunc("called. setHas=%s", setHas)
        
        
        self.myCandidateData.macAddress = MacAddress('\0'*6)
            
        if setHas:
            self.myCandidateData.setHasMacAddress()

        return ReturnCodes.kOk

    
    def copyRunningToCandidate(self):
        for logFunc in self._log("copy-running-to-candidate").debug3Func(): logFunc("copyRunningToCandidate(): called, candidate=%s, running=%s",
                                                              self.myCandidateData, self.myRunningData)
        if (self.myCandidateData != None):
            # already coppied - skip
            return

        if (self.myRunningData != None):
            self.myCandidateData = PersonData()
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
        self.myRunningData = PersonData()
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
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-validation-point-blinkyperson-failed").errorFunc():
                            logFunc("handleTrxProgressNotificationSpecific(): unregisterValidationPoint(%s) failed, progress=%s",  self._validationPointId, progress)
                        return ReturnCodes.kGeneralError
                if self._actionPointId and self.actionRegistrationDone:
                    res = self.myDomain.unregisterActionPoint(self, self._actionPointId)
                    if (res != ReturnCodes.kOk):
                        for logFunc in self._log("handle-trx-progress-notification-specitic-unregister-action-point-blinkyperson-failed").errorFunc():
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
                
            else:
                for logFunc in self._log("handle-internal-destroy-delete-prepare-illegal-blinky").noticeFunc():
                    logFunc("handleInternalDestroy(): prepare-illegal-blinky, res=%s, phase=%s",
                           res, phase)
                return ReturnCodes.kGeneralError
        elif (phase.getConfdPhase() == TrxPhase.kCommit):
            if (phase.getBlinkyPhase() == TrxPhase.kBlinky):
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
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
                
                pass
            elif (phase.getBlinkyPhase() == TrxPhase.kPrivate) or \
                 (phase.getBlinkyPhase() == TrxPhase.kPublic):
                
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
        "dataImportStatement": "from a.sys.blinky.example.python.generator_test.ut.generator_test.person.person_data_gen import PersonData", 
        "moduleYangNamespacePrefix": "le", 
        "validationPoint": null, 
        "yangName": "people", 
        "namespace": "person", 
        "logGroupName": "blinky-person", 
        "className": "BlinkyPerson", 
        "logModuleName": "a-sys-blinky-example-python-generator-test-ut-generator-test-person-blinky-person-gen", 
        "importStatement": "from a.sys.blinky.example.python.generator_test.ut.generator_test.person.blinky_person_gen import BlinkyPerson", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
        "dataClassName": "PersonData", 
        "actionPoint": null
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "le", 
            "isCurrent": true, 
            "yangName": "people", 
            "namespace": "person", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "keyLeaf": {
                "varName": "person", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "person"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "homeIp", 
            "yangName": "home-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "gender", 
            "yangName": "gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "male", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "mobileIp", 
            "yangName": "mobile-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "homeIp6", 
            "yangName": "home-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: Ipv6PrefixHandlerPy", 
            "memberName": "officeIp6", 
            "yangName": "office-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "officeIp", 
            "yangName": "office-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "desiredGender", 
            "yangName": "desired-gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "linux_", 
            "yangName": "linux", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "secondaryNumber", 
            "yangName": "secondary-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "789", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "employed", 
            "yangName": "employed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "175", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
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
        "python", 
        "generator_test", 
        "ut", 
        "generator_test"
    ], 
    "createTime": "2013"
}
"""

