


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from person_maapi_base_gen import PersonMaapiBase

from a.sys.blinky.example.python.generator_test.ut.generator_test.person.status.status_maapi_gen import BlinkyStatusMaapi

from a.infra.net.mac_address import MacAddress
from a.sys.blinky.example.python.generator_test.ut.generator_test_types.generator_test_types_module_gen import GenderT
import struct


class BlinkyPersonMaapi(PersonMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-person")
        self.domain = None

        
        self.statusObj = None
        

        
        self.homeIpRequested = False
        self.homeIp = None
        self.homeIpSet = False
        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        
        self.genderRequested = False
        self.gender = None
        self.genderSet = False
        
        self.numberRequested = False
        self.number = None
        self.numberSet = False
        
        self.mobileIpRequested = False
        self.mobileIp = None
        self.mobileIpSet = False
        
        self.homeIp6Requested = False
        self.homeIp6 = None
        self.homeIp6Set = False
        
        self.officeIp6Requested = False
        self.officeIp6 = None
        self.officeIp6Set = False
        
        self.officeIpRequested = False
        self.officeIp = None
        self.officeIpSet = False
        
        self.desiredGenderRequested = False
        self.desiredGender = None
        self.desiredGenderSet = False
        
        self.linux_Requested = False
        self.linux_ = None
        self.linux_Set = False
        
        self.secondaryNumberRequested = False
        self.secondaryNumber = None
        self.secondaryNumberSet = False
        
        self.employedRequested = False
        self.employed = None
        self.employedSet = False
        
        self.heightRequested = False
        self.height = None
        self.heightSet = False
        
        self.macAddressRequested = False
        self.macAddress = None
        self.macAddressSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestHomeIp(True)
        
        self.requestName(True)
        
        self.requestGender(True)
        
        self.requestNumber(True)
        
        self.requestMobileIp(True)
        
        self.requestHomeIp6(True)
        
        self.requestOfficeIp6(True)
        
        self.requestOfficeIp(True)
        
        self.requestDesiredGender(True)
        
        self.requestLinux_(True)
        
        self.requestSecondaryNumber(True)
        
        self.requestEmployed(True)
        
        self.requestHeight(True)
        
        self.requestMacAddress(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestHomeIp(True)
        
        self.requestName(True)
        
        self.requestGender(True)
        
        self.requestNumber(True)
        
        self.requestMobileIp(True)
        
        self.requestHomeIp6(True)
        
        self.requestOfficeIp6(True)
        
        self.requestOfficeIp(True)
        
        self.requestDesiredGender(True)
        
        self.requestLinux_(True)
        
        self.requestSecondaryNumber(True)
        
        self.requestEmployed(True)
        
        self.requestHeight(True)
        
        self.requestMacAddress(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestHomeIp(False)
        
        self.requestName(False)
        
        self.requestGender(False)
        
        self.requestNumber(False)
        
        self.requestMobileIp(False)
        
        self.requestHomeIp6(False)
        
        self.requestOfficeIp6(False)
        
        self.requestOfficeIp(False)
        
        self.requestDesiredGender(False)
        
        self.requestLinux_(False)
        
        self.requestSecondaryNumber(False)
        
        self.requestEmployed(False)
        
        self.requestHeight(False)
        
        self.requestMacAddress(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestHomeIp(False)
        
        self.requestName(False)
        
        self.requestGender(False)
        
        self.requestNumber(False)
        
        self.requestMobileIp(False)
        
        self.requestHomeIp6(False)
        
        self.requestOfficeIp6(False)
        
        self.requestOfficeIp(False)
        
        self.requestDesiredGender(False)
        
        self.requestLinux_(False)
        
        self.requestSecondaryNumber(False)
        
        self.requestEmployed(False)
        
        self.requestHeight(False)
        
        self.requestMacAddress(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setHomeIp(None)
        self.homeIpSet = False
        
        self.setName(None)
        self.nameSet = False
        
        self.setGender(None)
        self.genderSet = False
        
        self.setNumber(None)
        self.numberSet = False
        
        self.setMobileIp(None)
        self.mobileIpSet = False
        
        self.setHomeIp6(None)
        self.homeIp6Set = False
        
        self.setOfficeIp6(None)
        self.officeIp6Set = False
        
        self.setOfficeIp(None)
        self.officeIpSet = False
        
        self.setDesiredGender(None)
        self.desiredGenderSet = False
        
        self.setLinux_(None)
        self.linux_Set = False
        
        self.setSecondaryNumber(None)
        self.secondaryNumberSet = False
        
        self.setEmployed(None)
        self.employedSet = False
        
        self.setHeight(None)
        self.heightSet = False
        
        self.setMacAddress(None)
        self.macAddressSet = False
        
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        

    def write (self
              , person
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(person, trxContext)

    def read (self
              , person
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(person, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , person
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(person, 
                                  True,
                                  trxContext)

    def newStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-status').debug3Func(): logFunc('called.')
        status = BlinkyStatusMaapi(self._log)
        status.init(self.domain)
        return status

    def setStatusObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. obj=%s', obj)
        self.statusObj = obj

    def getStatusObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        return self.statusObj

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        if self.statusObj:
            return True
        return False



    def requestHomeIp (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-homeip').debug3Func(): logFunc('called. requested=%s', requested)
        self.homeIpRequested = requested
        self.homeIpSet = False

    def isHomeIpRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-homeip-requested').debug3Func(): logFunc('called. requested=%s', self.homeIpRequested)
        return self.homeIpRequested

    def getHomeIp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-homeip').debug3Func(): logFunc('called. self.homeIpSet=%s, self.homeIp=%s', self.homeIpSet, self.homeIp)
        if self.homeIpSet:
            return self.homeIp
        return None

    def hasHomeIp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-homeip').debug3Func(): logFunc('called. self.homeIpSet=%s, self.homeIp=%s', self.homeIpSet, self.homeIp)
        if self.homeIpSet:
            return True
        return False

    def setHomeIp (self, homeIp):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-homeip').debug3Func(): logFunc('called. homeIp=%s, old=%s', homeIp, self.homeIp)
        self.homeIpSet = True
        self.homeIp = homeIp

    def requestName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-name').debug3Func(): logFunc('called. requested=%s', requested)
        self.nameRequested = requested
        self.nameSet = False

    def isNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-name-requested').debug3Func(): logFunc('called. requested=%s', self.nameRequested)
        return self.nameRequested

    def getName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return self.name
        return None

    def hasName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return True
        return False

    def setName (self, name):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-name').debug3Func(): logFunc('called. name=%s, old=%s', name, self.name)
        self.nameSet = True
        self.name = name

    def requestGender (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-gender').debug3Func(): logFunc('called. requested=%s', requested)
        self.genderRequested = requested
        self.genderSet = False

    def isGenderRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-gender-requested').debug3Func(): logFunc('called. requested=%s', self.genderRequested)
        return self.genderRequested

    def getGender (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-gender').debug3Func(): logFunc('called. self.genderSet=%s, self.gender=%s', self.genderSet, self.gender)
        if self.genderSet:
            return self.gender
        return None

    def hasGender (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-gender').debug3Func(): logFunc('called. self.genderSet=%s, self.gender=%s', self.genderSet, self.gender)
        if self.genderSet:
            return True
        return False

    def setGender (self, gender):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-gender').debug3Func(): logFunc('called. gender=%s, old=%s', gender, self.gender)
        self.genderSet = True
        self.gender = gender

    def requestNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-number').debug3Func(): logFunc('called. requested=%s', requested)
        self.numberRequested = requested
        self.numberSet = False

    def isNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-number-requested').debug3Func(): logFunc('called. requested=%s', self.numberRequested)
        return self.numberRequested

    def getNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-number').debug3Func(): logFunc('called. self.numberSet=%s, self.number=%s', self.numberSet, self.number)
        if self.numberSet:
            return self.number
        return None

    def hasNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-number').debug3Func(): logFunc('called. self.numberSet=%s, self.number=%s', self.numberSet, self.number)
        if self.numberSet:
            return True
        return False

    def setNumber (self, number):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-number').debug3Func(): logFunc('called. number=%s, old=%s', number, self.number)
        self.numberSet = True
        self.number = number

    def requestMobileIp (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mobileip').debug3Func(): logFunc('called. requested=%s', requested)
        self.mobileIpRequested = requested
        self.mobileIpSet = False

    def isMobileIpRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mobileip-requested').debug3Func(): logFunc('called. requested=%s', self.mobileIpRequested)
        return self.mobileIpRequested

    def getMobileIp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mobileip').debug3Func(): logFunc('called. self.mobileIpSet=%s, self.mobileIp=%s', self.mobileIpSet, self.mobileIp)
        if self.mobileIpSet:
            return self.mobileIp
        return None

    def hasMobileIp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mobileip').debug3Func(): logFunc('called. self.mobileIpSet=%s, self.mobileIp=%s', self.mobileIpSet, self.mobileIp)
        if self.mobileIpSet:
            return True
        return False

    def setMobileIp (self, mobileIp):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mobileip').debug3Func(): logFunc('called. mobileIp=%s, old=%s', mobileIp, self.mobileIp)
        self.mobileIpSet = True
        self.mobileIp = mobileIp

    def requestHomeIp6 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-homeip6').debug3Func(): logFunc('called. requested=%s', requested)
        self.homeIp6Requested = requested
        self.homeIp6Set = False

    def isHomeIp6Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-homeip6-requested').debug3Func(): logFunc('called. requested=%s', self.homeIp6Requested)
        return self.homeIp6Requested

    def getHomeIp6 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-homeip6').debug3Func(): logFunc('called. self.homeIp6Set=%s, self.homeIp6=%s', self.homeIp6Set, self.homeIp6)
        if self.homeIp6Set:
            return self.homeIp6
        return None

    def hasHomeIp6 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-homeip6').debug3Func(): logFunc('called. self.homeIp6Set=%s, self.homeIp6=%s', self.homeIp6Set, self.homeIp6)
        if self.homeIp6Set:
            return True
        return False

    def setHomeIp6 (self, homeIp6):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-homeip6').debug3Func(): logFunc('called. homeIp6=%s, old=%s', homeIp6, self.homeIp6)
        self.homeIp6Set = True
        self.homeIp6 = homeIp6

    def requestOfficeIp6 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-officeip6').debug3Func(): logFunc('called. requested=%s', requested)
        self.officeIp6Requested = requested
        self.officeIp6Set = False

    def isOfficeIp6Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-officeip6-requested').debug3Func(): logFunc('called. requested=%s', self.officeIp6Requested)
        return self.officeIp6Requested

    def getOfficeIp6 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-officeip6').debug3Func(): logFunc('called. self.officeIp6Set=%s, self.officeIp6=%s', self.officeIp6Set, self.officeIp6)
        if self.officeIp6Set:
            return self.officeIp6
        return None

    def hasOfficeIp6 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-officeip6').debug3Func(): logFunc('called. self.officeIp6Set=%s, self.officeIp6=%s', self.officeIp6Set, self.officeIp6)
        if self.officeIp6Set:
            return True
        return False

    def setOfficeIp6 (self, officeIp6):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-officeip6').debug3Func(): logFunc('called. officeIp6=%s, old=%s', officeIp6, self.officeIp6)
        self.officeIp6Set = True
        self.officeIp6 = officeIp6

    def requestOfficeIp (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-officeip').debug3Func(): logFunc('called. requested=%s', requested)
        self.officeIpRequested = requested
        self.officeIpSet = False

    def isOfficeIpRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-officeip-requested').debug3Func(): logFunc('called. requested=%s', self.officeIpRequested)
        return self.officeIpRequested

    def getOfficeIp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-officeip').debug3Func(): logFunc('called. self.officeIpSet=%s, self.officeIp=%s', self.officeIpSet, self.officeIp)
        if self.officeIpSet:
            return self.officeIp
        return None

    def hasOfficeIp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-officeip').debug3Func(): logFunc('called. self.officeIpSet=%s, self.officeIp=%s', self.officeIpSet, self.officeIp)
        if self.officeIpSet:
            return True
        return False

    def setOfficeIp (self, officeIp):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-officeip').debug3Func(): logFunc('called. officeIp=%s, old=%s', officeIp, self.officeIp)
        self.officeIpSet = True
        self.officeIp = officeIp

    def requestDesiredGender (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-desiredgender').debug3Func(): logFunc('called. requested=%s', requested)
        self.desiredGenderRequested = requested
        self.desiredGenderSet = False

    def isDesiredGenderRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-desiredgender-requested').debug3Func(): logFunc('called. requested=%s', self.desiredGenderRequested)
        return self.desiredGenderRequested

    def getDesiredGender (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-desiredgender').debug3Func(): logFunc('called. self.desiredGenderSet=%s, self.desiredGender=%s', self.desiredGenderSet, self.desiredGender)
        if self.desiredGenderSet:
            return self.desiredGender
        return None

    def hasDesiredGender (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-desiredgender').debug3Func(): logFunc('called. self.desiredGenderSet=%s, self.desiredGender=%s', self.desiredGenderSet, self.desiredGender)
        if self.desiredGenderSet:
            return True
        return False

    def setDesiredGender (self, desiredGender):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-desiredgender').debug3Func(): logFunc('called. desiredGender=%s, old=%s', desiredGender, self.desiredGender)
        self.desiredGenderSet = True
        self.desiredGender = desiredGender

    def requestLinux_ (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-linux_').debug3Func(): logFunc('called. requested=%s', requested)
        self.linux_Requested = requested
        self.linux_Set = False

    def isLinux_Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-linux_-requested').debug3Func(): logFunc('called. requested=%s', self.linux_Requested)
        return self.linux_Requested

    def getLinux_ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-linux_').debug3Func(): logFunc('called. self.linux_Set=%s, self.linux_=%s', self.linux_Set, self.linux_)
        if self.linux_Set:
            return self.linux_
        return None

    def hasLinux_ (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-linux_').debug3Func(): logFunc('called. self.linux_Set=%s, self.linux_=%s', self.linux_Set, self.linux_)
        if self.linux_Set:
            return True
        return False

    def setLinux_ (self, linux_):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-linux_').debug3Func(): logFunc('called. linux_=%s, old=%s', linux_, self.linux_)
        self.linux_Set = True
        self.linux_ = linux_

    def requestSecondaryNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-secondarynumber').debug3Func(): logFunc('called. requested=%s', requested)
        self.secondaryNumberRequested = requested
        self.secondaryNumberSet = False

    def isSecondaryNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-secondarynumber-requested').debug3Func(): logFunc('called. requested=%s', self.secondaryNumberRequested)
        return self.secondaryNumberRequested

    def getSecondaryNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-secondarynumber').debug3Func(): logFunc('called. self.secondaryNumberSet=%s, self.secondaryNumber=%s', self.secondaryNumberSet, self.secondaryNumber)
        if self.secondaryNumberSet:
            return self.secondaryNumber
        return None

    def hasSecondaryNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-secondarynumber').debug3Func(): logFunc('called. self.secondaryNumberSet=%s, self.secondaryNumber=%s', self.secondaryNumberSet, self.secondaryNumber)
        if self.secondaryNumberSet:
            return True
        return False

    def setSecondaryNumber (self, secondaryNumber):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-secondarynumber').debug3Func(): logFunc('called. secondaryNumber=%s, old=%s', secondaryNumber, self.secondaryNumber)
        self.secondaryNumberSet = True
        self.secondaryNumber = secondaryNumber

    def requestEmployed (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-employed').debug3Func(): logFunc('called. requested=%s', requested)
        self.employedRequested = requested
        self.employedSet = False

    def isEmployedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-employed-requested').debug3Func(): logFunc('called. requested=%s', self.employedRequested)
        return self.employedRequested

    def getEmployed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-employed').debug3Func(): logFunc('called. self.employedSet=%s, self.employed=%s', self.employedSet, self.employed)
        if self.employedSet:
            return self.employed
        return None

    def hasEmployed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-employed').debug3Func(): logFunc('called. self.employedSet=%s, self.employed=%s', self.employedSet, self.employed)
        if self.employedSet:
            return True
        return False

    def setEmployed (self, employed):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-employed').debug3Func(): logFunc('called. employed=%s, old=%s', employed, self.employed)
        self.employedSet = True
        self.employed = employed

    def requestHeight (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-height').debug3Func(): logFunc('called. requested=%s', requested)
        self.heightRequested = requested
        self.heightSet = False

    def isHeightRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-height-requested').debug3Func(): logFunc('called. requested=%s', self.heightRequested)
        return self.heightRequested

    def getHeight (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-height').debug3Func(): logFunc('called. self.heightSet=%s, self.height=%s', self.heightSet, self.height)
        if self.heightSet:
            return self.height
        return None

    def hasHeight (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-height').debug3Func(): logFunc('called. self.heightSet=%s, self.height=%s', self.heightSet, self.height)
        if self.heightSet:
            return True
        return False

    def setHeight (self, height):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-height').debug3Func(): logFunc('called. height=%s, old=%s', height, self.height)
        self.heightSet = True
        self.height = height

    def requestMacAddress (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-macaddress').debug3Func(): logFunc('called. requested=%s', requested)
        self.macAddressRequested = requested
        self.macAddressSet = False

    def isMacAddressRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-macaddress-requested').debug3Func(): logFunc('called. requested=%s', self.macAddressRequested)
        return self.macAddressRequested

    def getMacAddress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-macaddress').debug3Func(): logFunc('called. self.macAddressSet=%s, self.macAddress=%s', self.macAddressSet, self.macAddress)
        if self.macAddressSet:
            return self.macAddress
        return None

    def hasMacAddress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-macaddress').debug3Func(): logFunc('called. self.macAddressSet=%s, self.macAddress=%s', self.macAddressSet, self.macAddress)
        if self.macAddressSet:
            return True
        return False

    def setMacAddress (self, macAddress):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-macaddress').debug3Func(): logFunc('called. macAddress=%s, old=%s', macAddress, self.macAddress)
        self.macAddressSet = True
        self.macAddress = macAddress


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        

        
        self.homeIp = 0
        self.homeIpSet = False
        
        self.name = 0
        self.nameSet = False
        
        self.gender = 0
        self.genderSet = False
        
        self.number = 0
        self.numberSet = False
        
        self.mobileIp = 0
        self.mobileIpSet = False
        
        self.homeIp6 = 0
        self.homeIp6Set = False
        
        self.officeIp6 = 0
        self.officeIp6Set = False
        
        self.officeIp = 0
        self.officeIpSet = False
        
        self.desiredGender = 0
        self.desiredGenderSet = False
        
        self.linux_ = 0
        self.linux_Set = False
        
        self.secondaryNumber = 0
        self.secondaryNumberSet = False
        
        self.employed = 0
        self.employedSet = False
        
        self.height = 0
        self.heightSet = False
        
        self.macAddress = 0
        self.macAddressSet = False
        

    def _getSelfKeyPath (self, person
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(person);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("people", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", "le"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        person, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(person, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(person, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       person, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(person, 
                                       
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               person, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.statusObj:
            res = self.statusObj._collectItemsToDelete(person, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-failed').errorFunc(): logFunc('statusObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasHomeIp():
            valHomeIp = Value()
            if self.homeIp is not None:
                valHomeIp.setIPv4(self.homeIp)
            else:
                valHomeIp.setEmpty()
            tagValueList.push(("home-ip", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valHomeIp)
        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valName)
        
        if self.hasGender():
            valGender = Value()
            if self.gender is not None:
                valGender.setEnum(self.gender.getValue())
            else:
                valGender.setEmpty()
            tagValueList.push(("gender", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valGender)
        
        if self.hasNumber():
            valNumber = Value()
            if self.number is not None:
                valNumber.setString(self.number)
            else:
                valNumber.setEmpty()
            tagValueList.push(("number", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valNumber)
        
        if self.hasMobileIp():
            valMobileIp = Value()
            if self.mobileIp is not None:
                valMobileIp.setString(self.mobileIp)
            else:
                valMobileIp.setEmpty()
            tagValueList.push(("mobile-ip", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valMobileIp)
        
        if self.hasHomeIp6():
            valHomeIp6 = Value()
            if self.homeIp6 is not None:
                valHomeIp6.setIPv6(self.homeIp6)
            else:
                valHomeIp6.setEmpty()
            tagValueList.push(("home-ip6", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valHomeIp6)
        
        if self.hasOfficeIp6():
            valOfficeIp6 = Value()
            if self.officeIp6 is not None:
                valOfficeIp6.setIPv6Prefix(self.officeIp6)
            else:
                valOfficeIp6.setEmpty()
            tagValueList.push(("office-ip6", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valOfficeIp6)
        
        if self.hasOfficeIp():
            valOfficeIp = Value()
            if self.officeIp is not None:
                valOfficeIp.setIPv4Prefix(self.officeIp)
            else:
                valOfficeIp.setEmpty()
            tagValueList.push(("office-ip", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valOfficeIp)
        
        if self.hasDesiredGender():
            valDesiredGender = Value()
            if self.desiredGender is not None:
                valDesiredGender.setEnum(self.desiredGender.getValue())
            else:
                valDesiredGender.setEmpty()
            tagValueList.push(("desired-gender", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valDesiredGender)
        
        if self.hasLinux_():
            valLinux_ = Value()
            if self.linux_ is not None:
                valLinux_.setString(self.linux_)
            else:
                valLinux_.setEmpty()
            tagValueList.push(("linux", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valLinux_)
        
        if self.hasSecondaryNumber():
            valSecondaryNumber = Value()
            if self.secondaryNumber is not None:
                valSecondaryNumber.setString(self.secondaryNumber)
            else:
                valSecondaryNumber.setEmpty()
            tagValueList.push(("secondary-number", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valSecondaryNumber)
        
        if self.hasEmployed():
            valEmployed = Value()
            if self.employed is not None:
                valEmployed.setBool(self.employed)
            else:
                valEmployed.setEmpty()
            tagValueList.push(("employed", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valEmployed)
        
        if self.hasHeight():
            valHeight = Value()
            if self.height is not None:
                valHeight.setInt64(self.height)
            else:
                valHeight.setEmpty()
            tagValueList.push(("height", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valHeight)
        
        if self.hasMacAddress():
            valMacAddress = Value()
            if self.macAddress is not None:
                valMacAddress.setBinary(self.macAddress.getAddress())
            else:
                valMacAddress.setEmpty()
            tagValueList.push(("mac-address", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valMacAddress)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", "le")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isHomeIpRequested():
            valHomeIp = Value()
            valHomeIp.setEmpty()
            tagValueList.push(("home-ip", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valHomeIp)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valName)
        
        if self.isGenderRequested():
            valGender = Value()
            valGender.setEmpty()
            tagValueList.push(("gender", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valGender)
        
        if self.isNumberRequested():
            valNumber = Value()
            valNumber.setEmpty()
            tagValueList.push(("number", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valNumber)
        
        if self.isMobileIpRequested():
            valMobileIp = Value()
            valMobileIp.setEmpty()
            tagValueList.push(("mobile-ip", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valMobileIp)
        
        if self.isHomeIp6Requested():
            valHomeIp6 = Value()
            valHomeIp6.setEmpty()
            tagValueList.push(("home-ip6", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valHomeIp6)
        
        if self.isOfficeIp6Requested():
            valOfficeIp6 = Value()
            valOfficeIp6.setEmpty()
            tagValueList.push(("office-ip6", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valOfficeIp6)
        
        if self.isOfficeIpRequested():
            valOfficeIp = Value()
            valOfficeIp.setEmpty()
            tagValueList.push(("office-ip", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valOfficeIp)
        
        if self.isDesiredGenderRequested():
            valDesiredGender = Value()
            valDesiredGender.setEmpty()
            tagValueList.push(("desired-gender", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valDesiredGender)
        
        if self.isLinux_Requested():
            valLinux_ = Value()
            valLinux_.setEmpty()
            tagValueList.push(("linux", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valLinux_)
        
        if self.isSecondaryNumberRequested():
            valSecondaryNumber = Value()
            valSecondaryNumber.setEmpty()
            tagValueList.push(("secondary-number", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valSecondaryNumber)
        
        if self.isEmployedRequested():
            valEmployed = Value()
            valEmployed.setEmpty()
            tagValueList.push(("employed", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valEmployed)
        
        if self.isHeightRequested():
            valHeight = Value()
            valHeight.setEmpty()
            tagValueList.push(("height", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valHeight)
        
        if self.isMacAddressRequested():
            valMacAddress = Value()
            valMacAddress.setEmpty()
            tagValueList.push(("mac-address", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"), valMacAddress)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", "le")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isHomeIpRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "home-ip") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-homeip').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "homeIp", "home-ip", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = (tempValue.asIPv4())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-home-ip-bad-value').infoFunc(): logFunc('homeIp not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHomeIp(tempVar)
            for logFunc in self._log('read-tag-values-home-ip').debug3Func(): logFunc('read homeIp. homeIp=%s, tempValue=%s', self.homeIp, tempValue.getType())
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-name-bad-value').infoFunc(): logFunc('name not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setName(tempVar)
            for logFunc in self._log('read-tag-values-name').debug3Func(): logFunc('read name. name=%s, tempValue=%s', self.name, tempValue.getType())
        
        if self.isGenderRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "gender") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-gender').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "gender", "gender", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-gender-bad-value').infoFunc(): logFunc('gender not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setGender(tempVar)
            for logFunc in self._log('read-tag-values-gender').debug3Func(): logFunc('read gender. gender=%s, tempValue=%s', self.gender, tempValue.getType())
        
        if self.isNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "number") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-number').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "number", "number", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-number-bad-value').infoFunc(): logFunc('number not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNumber(tempVar)
            for logFunc in self._log('read-tag-values-number').debug3Func(): logFunc('read number. number=%s, tempValue=%s', self.number, tempValue.getType())
        
        if self.isMobileIpRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mobile-ip") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mobileip').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "mobileIp", "mobile-ip", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mobile-ip-bad-value').infoFunc(): logFunc('mobileIp not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMobileIp(tempVar)
            for logFunc in self._log('read-tag-values-mobile-ip').debug3Func(): logFunc('read mobileIp. mobileIp=%s, tempValue=%s', self.mobileIp, tempValue.getType())
        
        if self.isHomeIp6Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "home-ip6") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-homeip6').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "homeIp6", "home-ip6", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = (tempValue.asIPv6())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-home-ip6-bad-value').infoFunc(): logFunc('homeIp6 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHomeIp6(tempVar)
            for logFunc in self._log('read-tag-values-home-ip6').debug3Func(): logFunc('read homeIp6. homeIp6=%s, tempValue=%s', self.homeIp6, tempValue.getType())
        
        if self.isOfficeIp6Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "office-ip6") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-officeip6').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "officeIp6", "office-ip6", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = (tempValue.asIPv6Prefix())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-office-ip6-bad-value').infoFunc(): logFunc('officeIp6 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOfficeIp6(tempVar)
            for logFunc in self._log('read-tag-values-office-ip6').debug3Func(): logFunc('read officeIp6. officeIp6=%s, tempValue=%s', self.officeIp6, tempValue.getType())
        
        if self.isOfficeIpRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "office-ip") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-officeip').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "officeIp", "office-ip", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = (tempValue.asIPv4Prefix())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-office-ip-bad-value').infoFunc(): logFunc('officeIp not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOfficeIp(tempVar)
            for logFunc in self._log('read-tag-values-office-ip').debug3Func(): logFunc('read officeIp. officeIp=%s, tempValue=%s', self.officeIp, tempValue.getType())
        
        if self.isDesiredGenderRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "desired-gender") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-desiredgender').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "desiredGender", "desired-gender", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-desired-gender-bad-value').infoFunc(): logFunc('desiredGender not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDesiredGender(tempVar)
            for logFunc in self._log('read-tag-values-desired-gender').debug3Func(): logFunc('read desiredGender. desiredGender=%s, tempValue=%s', self.desiredGender, tempValue.getType())
        
        if self.isLinux_Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "linux") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-linux_').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "linux_", "linux", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-linux-bad-value').infoFunc(): logFunc('linux_ not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLinux_(tempVar)
            for logFunc in self._log('read-tag-values-linux').debug3Func(): logFunc('read linux_. linux_=%s, tempValue=%s', self.linux_, tempValue.getType())
        
        if self.isSecondaryNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "secondary-number") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-secondarynumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "secondaryNumber", "secondary-number", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-secondary-number-bad-value').infoFunc(): logFunc('secondaryNumber not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSecondaryNumber(tempVar)
            for logFunc in self._log('read-tag-values-secondary-number').debug3Func(): logFunc('read secondaryNumber. secondaryNumber=%s, tempValue=%s', self.secondaryNumber, tempValue.getType())
        
        if self.isEmployedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "employed") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-employed').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "employed", "employed", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-employed-bad-value').infoFunc(): logFunc('employed not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEmployed(tempVar)
            for logFunc in self._log('read-tag-values-employed').debug3Func(): logFunc('read employed. employed=%s, tempValue=%s', self.employed, tempValue.getType())
        
        if self.isHeightRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "height") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-height').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "height", "height", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-height-bad-value').infoFunc(): logFunc('height not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHeight(tempVar)
            for logFunc in self._log('read-tag-values-height').debug3Func(): logFunc('read height. height=%s, tempValue=%s', self.height, tempValue.getType())
        
        if self.isMacAddressRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mac-address") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-macaddress').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "macAddress", "mac-address", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = MacAddress('\0'*6)
            tempVar = MacAddress(tempValue.asBinary())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mac-address-bad-value').infoFunc(): logFunc('macAddress not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMacAddress(tempVar)
            for logFunc in self._log('read-tag-values-mac-address').debug3Func(): logFunc('read macAddress. macAddress=%s, tempValue=%s', self.macAddress, tempValue.getType())
        

        
        if self.statusObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.statusObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-status-failed').errorFunc(): logFunc('statusObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "person", 
        "namespace": "person", 
        "className": "PersonMaapi", 
        "importStatement": "from a.sys.blinky.example.python.generator_test.ut.generator_test.person.person_maapi_gen import PersonMaapi", 
        "baseClassName": "PersonMaapiBase", 
        "baseModule": "person_maapi_base_gen"
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
    "descendants": [
        {
            "moduleYangNamespacePrefix": "le", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.sys.blinky.example.python.generator_test.ut.generator_test.person.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "homeIp", 
            "yangName": "home-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "gender", 
            "yangName": "gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "male", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "mobileIp", 
            "yangName": "mobile-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "homeIp6", 
            "yangName": "home-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv6PrefixHandlerPy", 
            "memberName": "officeIp6", 
            "yangName": "office-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "officeIp", 
            "yangName": "office-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "desiredGender", 
            "yangName": "desired-gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "linux_", 
            "yangName": "linux", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "secondaryNumber", 
            "yangName": "secondary-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "789", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "employed", 
            "yangName": "employed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "175", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "python", 
            "generator_test", 
            "ut", 
            "generator_test"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "homeIp", 
            "yangName": "home-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "gender", 
            "yangName": "gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "male", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "number", 
            "yangName": "number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: BuiltinStringHandler", 
            "memberName": "mobileIp", 
            "yangName": "mobile-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "homeIp6", 
            "yangName": "home-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv6PrefixHandlerPy", 
            "memberName": "officeIp6", 
            "yangName": "office-ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: Ipv4PrefixHandlerPy", 
            "memberName": "officeIp", 
            "yangName": "office-ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "desiredGender", 
            "yangName": "desired-gender", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "linux_", 
            "yangName": "linux", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "secondaryNumber", 
            "yangName": "secondary-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "789", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "employed", 
            "yangName": "employed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "175", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/generator-test", 
            "moduleYangNamespacePrefix": "le", 
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


