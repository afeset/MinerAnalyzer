


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

from fish__maapi_base_gen import FishMaapiBase

from a.sys.blinky.example.lake_example.lake.fish_.mood.mood_maapi_gen import BlinkyMoodMaapi
from a.sys.blinky.example.lake_example.lake.fish_.antenna.antenna_maapi_gen import BlinkyAntennaMaapi
from a.sys.blinky.example.lake_example.lake.fish_.test_generation_underscore.test_generation_underscore_maapi_list_gen import BlinkyTestGenerationUnderscoreMaapiList
from a.sys.blinky.example.lake_example.lake.fish_.design.design_maapi_gen import BlinkyDesignMaapi
from a.sys.blinky.example.lake_example.lake.fish_.transparent_container.transparent_container_maapi_gen import BlinkyTransparentContainerMaapi

from a.sys.blinky.example.lake_example.lake_example_module_gen import ColorT
import struct


class BlinkyFishMaapi(FishMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-fish_")
        self.domain = None

        
        self.moodObj = None
        
        self.antennaObj = None
        
        self.testGenerationUnderscoreListObj = None
        
        self.designObj = None
        
        self.transparentContainerObj = None
        

        
        self.transparentFieldRequested = False
        self.transparentField = None
        self.transparentFieldSet = False
        
        self.colorRequested = False
        self.color = None
        self.colorSet = False
        
        self.eyeNumberRequested = False
        self.eyeNumber = None
        self.eyeNumberSet = False
        
        self.hasTailRequested = False
        self.hasTail = None
        self.hasTailSet = False
        
        self.finNumberRequested = False
        self.finNumber = None
        self.finNumberSet = False
        
        self.lengthRequested = False
        self.length = None
        self.lengthSet = False
        
        self.ip6Requested = False
        self.ip6 = None
        self.ip6Set = False
        
        self.idRequested = False
        self.id = None
        self.idSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTransparentField(True)
        
        self.requestColor(True)
        
        self.requestEyeNumber(True)
        
        self.requestHasTail(True)
        
        self.requestFinNumber(True)
        
        self.requestLength(True)
        
        self.requestIp6(True)
        
        self.requestId(True)
        
        
        
        if not self.moodObj:
            self.moodObj = self.newMood()
            self.moodObj.requestConfigAndOper()
        
        if not self.antennaObj:
            self.antennaObj = self.newAntenna()
            self.antennaObj.requestConfigAndOper()
        
        if not self.testGenerationUnderscoreListObj:
            self.testGenerationUnderscoreListObj = self.newTestGenerationUnderscoreList()
            self.testGenerationUnderscoreListObj.requestConfigAndOper()
        
        if not self.designObj:
            self.designObj = self.newDesign()
            self.designObj.requestConfigAndOper()
        
        if not self.transparentContainerObj:
            self.transparentContainerObj = self.newTransparentContainer()
            self.transparentContainerObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTransparentField(True)
        
        self.requestColor(True)
        
        self.requestEyeNumber(True)
        
        self.requestHasTail(True)
        
        self.requestFinNumber(True)
        
        self.requestLength(True)
        
        self.requestIp6(True)
        
        self.requestId(True)
        
        
        
        if not self.moodObj:
            self.moodObj = self.newMood()
            self.moodObj.requestConfig()
        
        if not self.antennaObj:
            self.antennaObj = self.newAntenna()
            self.antennaObj.requestConfig()
        
        if not self.testGenerationUnderscoreListObj:
            self.testGenerationUnderscoreListObj = self.newTestGenerationUnderscoreList()
            self.testGenerationUnderscoreListObj.requestConfig()
        
        if not self.designObj:
            self.designObj = self.newDesign()
            self.designObj.requestConfig()
        
        if not self.transparentContainerObj:
            self.transparentContainerObj = self.newTransparentContainer()
            self.transparentContainerObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTransparentField(False)
        
        self.requestColor(False)
        
        self.requestEyeNumber(False)
        
        self.requestHasTail(False)
        
        self.requestFinNumber(False)
        
        self.requestLength(False)
        
        self.requestIp6(False)
        
        self.requestId(False)
        
        
        
        if not self.moodObj:
            self.moodObj = self.newMood()
            self.moodObj.requestOper()
        
        if not self.antennaObj:
            self.antennaObj = self.newAntenna()
            self.antennaObj.requestOper()
        
        if not self.testGenerationUnderscoreListObj:
            self.testGenerationUnderscoreListObj = self.newTestGenerationUnderscoreList()
            self.testGenerationUnderscoreListObj.requestOper()
        
        if not self.designObj:
            self.designObj = self.newDesign()
            self.designObj.requestOper()
        
        if not self.transparentContainerObj:
            self.transparentContainerObj = self.newTransparentContainer()
            self.transparentContainerObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestTransparentField(False)
        
        self.requestColor(False)
        
        self.requestEyeNumber(False)
        
        self.requestHasTail(False)
        
        self.requestFinNumber(False)
        
        self.requestLength(False)
        
        self.requestIp6(False)
        
        self.requestId(False)
        
        
        
        if not self.moodObj:
            self.moodObj = self.newMood()
            self.moodObj.clearAllRequested()
        
        if not self.antennaObj:
            self.antennaObj = self.newAntenna()
            self.antennaObj.clearAllRequested()
        
        if not self.testGenerationUnderscoreListObj:
            self.testGenerationUnderscoreListObj = self.newTestGenerationUnderscoreList()
            self.testGenerationUnderscoreListObj.clearAllRequested()
        
        if not self.designObj:
            self.designObj = self.newDesign()
            self.designObj.clearAllRequested()
        
        if not self.transparentContainerObj:
            self.transparentContainerObj = self.newTransparentContainer()
            self.transparentContainerObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setTransparentField(None)
        self.transparentFieldSet = False
        
        self.setColor(None)
        self.colorSet = False
        
        self.setEyeNumber(None)
        self.eyeNumberSet = False
        
        self.setHasTail(None)
        self.hasTailSet = False
        
        self.setFinNumber(None)
        self.finNumberSet = False
        
        self.setLength(None)
        self.lengthSet = False
        
        self.setIp6(None)
        self.ip6Set = False
        
        self.setId(None)
        self.idSet = False
        
        
        if self.moodObj:
            self.moodObj.clearAllSet()
        
        if self.antennaObj:
            self.antennaObj.clearAllSet()
        
        if self.testGenerationUnderscoreListObj:
            self.testGenerationUnderscoreListObj.clearAllSet()
        
        if self.designObj:
            self.designObj.clearAllSet()
        
        if self.transparentContainerObj:
            self.transparentContainerObj.clearAllSet()
        

    def write (self
              , lake
              , fish_
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(lake, fish_, trxContext)

    def read (self
              , lake
              , fish_
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lake, fish_, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , lake
                       , fish_
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lake, fish_, 
                                  True,
                                  trxContext)

    def newMood (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-mood').debug3Func(): logFunc('called.')
        mood = BlinkyMoodMaapi(self._log)
        mood.init(self.domain)
        return mood

    def setMoodObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mood').debug3Func(): logFunc('called. obj=%s', obj)
        self.moodObj = obj

    def getMoodObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mood').debug3Func(): logFunc('called. self.moodObj=%s', self.moodObj)
        return self.moodObj

    def hasMood (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mood').debug3Func(): logFunc('called. self.moodObj=%s', self.moodObj)
        if self.moodObj:
            return True
        return False

    def newAntenna (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-antenna').debug3Func(): logFunc('called.')
        antenna = BlinkyAntennaMaapi(self._log)
        antenna.init(self.domain)
        return antenna

    def setAntennaObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-antenna').debug3Func(): logFunc('called. obj=%s', obj)
        self.antennaObj = obj

    def getAntennaObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-antenna').debug3Func(): logFunc('called. self.antennaObj=%s', self.antennaObj)
        return self.antennaObj

    def hasAntenna (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-antenna').debug3Func(): logFunc('called. self.antennaObj=%s', self.antennaObj)
        if self.antennaObj:
            return True
        return False

    def newTestGenerationUnderscoreList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-testgenerationunderscorelist').debug3Func(): logFunc('called.')
        testGenerationUnderscoreList = BlinkyTestGenerationUnderscoreMaapiList(self._log)
        testGenerationUnderscoreList.init(self.domain)
        return testGenerationUnderscoreList

    def setTestGenerationUnderscoreListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-testgenerationunderscorelist').debug3Func(): logFunc('called. obj=%s', obj)
        self.testGenerationUnderscoreListObj = obj

    def getTestGenerationUnderscoreListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-testgenerationunderscorelist').debug3Func(): logFunc('called. self.testGenerationUnderscoreListObj=%s', self.testGenerationUnderscoreListObj)
        return self.testGenerationUnderscoreListObj

    def hasTestGenerationUnderscoreList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-testgenerationunderscorelist').debug3Func(): logFunc('called. self.testGenerationUnderscoreListObj=%s', self.testGenerationUnderscoreListObj)
        if self.testGenerationUnderscoreListObj:
            return True
        return False

    def newDesign (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-design').debug3Func(): logFunc('called.')
        design = BlinkyDesignMaapi(self._log)
        design.init(self.domain)
        return design

    def setDesignObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-design').debug3Func(): logFunc('called. obj=%s', obj)
        self.designObj = obj

    def getDesignObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-design').debug3Func(): logFunc('called. self.designObj=%s', self.designObj)
        return self.designObj

    def hasDesign (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-design').debug3Func(): logFunc('called. self.designObj=%s', self.designObj)
        if self.designObj:
            return True
        return False

    def newTransparentContainer (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-transparentcontainer').debug3Func(): logFunc('called.')
        transparentContainer = BlinkyTransparentContainerMaapi(self._log)
        transparentContainer.init(self.domain)
        return transparentContainer

    def setTransparentContainerObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-transparentcontainer').debug3Func(): logFunc('called. obj=%s', obj)
        self.transparentContainerObj = obj

    def getTransparentContainerObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-transparentcontainer').debug3Func(): logFunc('called. self.transparentContainerObj=%s', self.transparentContainerObj)
        return self.transparentContainerObj

    def hasTransparentContainer (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-transparentcontainer').debug3Func(): logFunc('called. self.transparentContainerObj=%s', self.transparentContainerObj)
        if self.transparentContainerObj:
            return True
        return False



    def requestTransparentField (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-transparentfield').debug3Func(): logFunc('called. requested=%s', requested)
        self.transparentFieldRequested = requested
        self.transparentFieldSet = False

    def isTransparentFieldRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-transparentfield-requested').debug3Func(): logFunc('called. requested=%s', self.transparentFieldRequested)
        return self.transparentFieldRequested

    def getTransparentField (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-transparentfield').debug3Func(): logFunc('called. self.transparentFieldSet=%s, self.transparentField=%s', self.transparentFieldSet, self.transparentField)
        if self.transparentFieldSet:
            return self.transparentField
        return None

    def hasTransparentField (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-transparentfield').debug3Func(): logFunc('called. self.transparentFieldSet=%s, self.transparentField=%s', self.transparentFieldSet, self.transparentField)
        if self.transparentFieldSet:
            return True
        return False

    def setTransparentField (self, transparentField):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-transparentfield').debug3Func(): logFunc('called. transparentField=%s, old=%s', transparentField, self.transparentField)
        self.transparentFieldSet = True
        self.transparentField = transparentField

    def requestColor (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-color').debug3Func(): logFunc('called. requested=%s', requested)
        self.colorRequested = requested
        self.colorSet = False

    def isColorRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-color-requested').debug3Func(): logFunc('called. requested=%s', self.colorRequested)
        return self.colorRequested

    def getColor (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-color').debug3Func(): logFunc('called. self.colorSet=%s, self.color=%s', self.colorSet, self.color)
        if self.colorSet:
            return self.color
        return None

    def hasColor (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-color').debug3Func(): logFunc('called. self.colorSet=%s, self.color=%s', self.colorSet, self.color)
        if self.colorSet:
            return True
        return False

    def setColor (self, color):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-color').debug3Func(): logFunc('called. color=%s, old=%s', color, self.color)
        self.colorSet = True
        self.color = color

    def requestEyeNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-eyenumber').debug3Func(): logFunc('called. requested=%s', requested)
        self.eyeNumberRequested = requested
        self.eyeNumberSet = False

    def isEyeNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-eyenumber-requested').debug3Func(): logFunc('called. requested=%s', self.eyeNumberRequested)
        return self.eyeNumberRequested

    def getEyeNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-eyenumber').debug3Func(): logFunc('called. self.eyeNumberSet=%s, self.eyeNumber=%s', self.eyeNumberSet, self.eyeNumber)
        if self.eyeNumberSet:
            return self.eyeNumber
        return None

    def hasEyeNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-eyenumber').debug3Func(): logFunc('called. self.eyeNumberSet=%s, self.eyeNumber=%s', self.eyeNumberSet, self.eyeNumber)
        if self.eyeNumberSet:
            return True
        return False

    def setEyeNumber (self, eyeNumber):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-eyenumber').debug3Func(): logFunc('called. eyeNumber=%s, old=%s', eyeNumber, self.eyeNumber)
        self.eyeNumberSet = True
        self.eyeNumber = eyeNumber

    def requestHasTail (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-hastail').debug3Func(): logFunc('called. requested=%s', requested)
        self.hasTailRequested = requested
        self.hasTailSet = False

    def isHasTailRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-hastail-requested').debug3Func(): logFunc('called. requested=%s', self.hasTailRequested)
        return self.hasTailRequested

    def getHasTail (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-hastail').debug3Func(): logFunc('called. self.hasTailSet=%s, self.hasTail=%s', self.hasTailSet, self.hasTail)
        if self.hasTailSet:
            return self.hasTail
        return None

    def hasHasTail (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-hastail').debug3Func(): logFunc('called. self.hasTailSet=%s, self.hasTail=%s', self.hasTailSet, self.hasTail)
        if self.hasTailSet:
            return True
        return False

    def setHasTail (self, hasTail):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-hastail').debug3Func(): logFunc('called. hasTail=%s, old=%s', hasTail, self.hasTail)
        self.hasTailSet = True
        self.hasTail = hasTail

    def requestFinNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-finnumber').debug3Func(): logFunc('called. requested=%s', requested)
        self.finNumberRequested = requested
        self.finNumberSet = False

    def isFinNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-finnumber-requested').debug3Func(): logFunc('called. requested=%s', self.finNumberRequested)
        return self.finNumberRequested

    def getFinNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-finnumber').debug3Func(): logFunc('called. self.finNumberSet=%s, self.finNumber=%s', self.finNumberSet, self.finNumber)
        if self.finNumberSet:
            return self.finNumber
        return None

    def hasFinNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-finnumber').debug3Func(): logFunc('called. self.finNumberSet=%s, self.finNumber=%s', self.finNumberSet, self.finNumber)
        if self.finNumberSet:
            return True
        return False

    def setFinNumber (self, finNumber):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-finnumber').debug3Func(): logFunc('called. finNumber=%s, old=%s', finNumber, self.finNumber)
        self.finNumberSet = True
        self.finNumber = finNumber

    def requestLength (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-length').debug3Func(): logFunc('called. requested=%s', requested)
        self.lengthRequested = requested
        self.lengthSet = False

    def isLengthRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-length-requested').debug3Func(): logFunc('called. requested=%s', self.lengthRequested)
        return self.lengthRequested

    def getLength (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-length').debug3Func(): logFunc('called. self.lengthSet=%s, self.length=%s', self.lengthSet, self.length)
        if self.lengthSet:
            return self.length
        return None

    def hasLength (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-length').debug3Func(): logFunc('called. self.lengthSet=%s, self.length=%s', self.lengthSet, self.length)
        if self.lengthSet:
            return True
        return False

    def setLength (self, length):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-length').debug3Func(): logFunc('called. length=%s, old=%s', length, self.length)
        self.lengthSet = True
        self.length = length

    def requestIp6 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-ip6').debug3Func(): logFunc('called. requested=%s', requested)
        self.ip6Requested = requested
        self.ip6Set = False

    def isIp6Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-ip6-requested').debug3Func(): logFunc('called. requested=%s', self.ip6Requested)
        return self.ip6Requested

    def getIp6 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ip6').debug3Func(): logFunc('called. self.ip6Set=%s, self.ip6=%s', self.ip6Set, self.ip6)
        if self.ip6Set:
            return self.ip6
        return None

    def hasIp6 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ip6').debug3Func(): logFunc('called. self.ip6Set=%s, self.ip6=%s', self.ip6Set, self.ip6)
        if self.ip6Set:
            return True
        return False

    def setIp6 (self, ip6):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ip6').debug3Func(): logFunc('called. ip6=%s, old=%s', ip6, self.ip6)
        self.ip6Set = True
        self.ip6 = ip6

    def requestId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-id').debug3Func(): logFunc('called. requested=%s', requested)
        self.idRequested = requested
        self.idSet = False

    def isIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-id-requested').debug3Func(): logFunc('called. requested=%s', self.idRequested)
        return self.idRequested

    def getId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-id').debug3Func(): logFunc('called. self.idSet=%s, self.id=%s', self.idSet, self.id)
        if self.idSet:
            return self.id
        return None

    def hasId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-id').debug3Func(): logFunc('called. self.idSet=%s, self.id=%s', self.idSet, self.id)
        if self.idSet:
            return True
        return False

    def setId (self, id):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-id').debug3Func(): logFunc('called. id=%s, old=%s', id, self.id)
        self.idSet = True
        self.id = id


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.moodObj:
            self.moodObj._clearAllReadData()
        
        if self.antennaObj:
            self.antennaObj._clearAllReadData()
        
        if self.testGenerationUnderscoreListObj:
            self.testGenerationUnderscoreListObj._clearAllReadData()
        
        if self.designObj:
            self.designObj._clearAllReadData()
        
        if self.transparentContainerObj:
            self.transparentContainerObj._clearAllReadData()
        

        
        self.transparentField = 0
        self.transparentFieldSet = False
        
        self.color = 0
        self.colorSet = False
        
        self.eyeNumber = 0
        self.eyeNumberSet = False
        
        self.hasTail = 0
        self.hasTailSet = False
        
        self.finNumber = 0
        self.finNumberSet = False
        
        self.length = 0
        self.lengthSet = False
        
        self.ip6 = 0
        self.ip6Set = False
        
        self.id = 0
        self.idSet = False
        

    def _getSelfKeyPath (self, lake
                         , fish_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(fish_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fish", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(lake);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("lake", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        lake, 
                        fish_, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(lake, 
                                         fish_, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(lake, 
                                       fish_, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       lake, 
                       fish_, 
                       
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

        keyPath = self._getSelfKeyPath(lake, 
                                       fish_, 
                                       
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
                               lake, 
                               fish_, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.moodObj:
            res = self.moodObj._collectItemsToDelete(lake, 
                                                                          fish_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-mood-failed').errorFunc(): logFunc('moodObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.antennaObj:
            res = self.antennaObj._collectItemsToDelete(lake, 
                                                                          fish_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-antenna-failed').errorFunc(): logFunc('antennaObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.testGenerationUnderscoreListObj:
            res = self.testGenerationUnderscoreListObj._collectItemsToDelete(lake, 
                                                                          fish_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-test-generation_underscore-failed').errorFunc(): logFunc('testGenerationUnderscoreListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.designObj:
            res = self.designObj._collectItemsToDelete(lake, 
                                                                          fish_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-design-failed').errorFunc(): logFunc('designObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.transparentContainerObj:
            res = self.transparentContainerObj._collectItemsToDelete(lake, 
                                                                          fish_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-transparent-container-failed').errorFunc(): logFunc('transparentContainerObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasTransparentField():
            valTransparentField = Value()
            if self.transparentField is not None:
                valTransparentField.setBool(self.transparentField)
            else:
                valTransparentField.setEmpty()
            tagValueList.push(("transparent-field", "http://qwilt.com/model/lake-example"), valTransparentField)
        
        if self.hasColor():
            valColor = Value()
            if self.color is not None:
                valColor.setEnum(self.color.getValue())
            else:
                valColor.setEmpty()
            tagValueList.push(("color", "http://qwilt.com/model/lake-example"), valColor)
        
        if self.hasEyeNumber():
            valEyeNumber = Value()
            if self.eyeNumber is not None:
                valEyeNumber.setInt64(self.eyeNumber)
            else:
                valEyeNumber.setEmpty()
            tagValueList.push(("eye-number", "http://qwilt.com/model/lake-example"), valEyeNumber)
        
        if self.hasHasTail():
            valHasTail = Value()
            if self.hasTail is not None:
                valHasTail.setBool(self.hasTail)
            else:
                valHasTail.setEmpty()
            tagValueList.push(("has-tail", "http://qwilt.com/model/lake-example"), valHasTail)
        
        if self.hasFinNumber():
            valFinNumber = Value()
            if self.finNumber is not None:
                valFinNumber.setInt64(self.finNumber)
            else:
                valFinNumber.setEmpty()
            tagValueList.push(("fin-number", "http://qwilt.com/model/lake-example"), valFinNumber)
        
        if self.hasLength():
            valLength = Value()
            if self.length is not None:
                valLength.setInt64(self.length)
            else:
                valLength.setEmpty()
            tagValueList.push(("length", "http://qwilt.com/model/lake-example"), valLength)
        
        if self.hasIp6():
            valIp6 = Value()
            if self.ip6 is not None:
                valIp6.setIPv6(self.ip6)
            else:
                valIp6.setEmpty()
            tagValueList.push(("ip6", "http://qwilt.com/model/lake-example"), valIp6)
        
        if self.hasId():
            valId = Value()
            if self.id is not None:
                valId.setString(self.id)
            else:
                valId.setEmpty()
            tagValueList.push(("id", "http://qwilt.com/model/lake-example"), valId)
        

        
        if self.moodObj:
            valBegin = Value()
            (tag, ns, prefix) = ("mood" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.moodObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-mood-failed').errorFunc(): logFunc('moodObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.antennaObj:
            valBegin = Value()
            (tag, ns, prefix) = ("antenna" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.antennaObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-antenna-failed').errorFunc(): logFunc('antennaObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.testGenerationUnderscoreListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("test-generation_underscore" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.testGenerationUnderscoreListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-test-generation_underscore-failed').errorFunc(): logFunc('testGenerationUnderscoreListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.designObj:
            valBegin = Value()
            (tag, ns, prefix) = ("design" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.designObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-design-failed').errorFunc(): logFunc('designObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.transparentContainerObj:
            valBegin = Value()
            (tag, ns, prefix) = ("transparent-container" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.transparentContainerObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-transparent-container-failed').errorFunc(): logFunc('transparentContainerObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isTransparentFieldRequested():
            valTransparentField = Value()
            valTransparentField.setEmpty()
            tagValueList.push(("transparent-field", "http://qwilt.com/model/lake-example"), valTransparentField)
        
        if self.isColorRequested():
            valColor = Value()
            valColor.setEmpty()
            tagValueList.push(("color", "http://qwilt.com/model/lake-example"), valColor)
        
        if self.isEyeNumberRequested():
            valEyeNumber = Value()
            valEyeNumber.setEmpty()
            tagValueList.push(("eye-number", "http://qwilt.com/model/lake-example"), valEyeNumber)
        
        if self.isHasTailRequested():
            valHasTail = Value()
            valHasTail.setEmpty()
            tagValueList.push(("has-tail", "http://qwilt.com/model/lake-example"), valHasTail)
        
        if self.isFinNumberRequested():
            valFinNumber = Value()
            valFinNumber.setEmpty()
            tagValueList.push(("fin-number", "http://qwilt.com/model/lake-example"), valFinNumber)
        
        if self.isLengthRequested():
            valLength = Value()
            valLength.setEmpty()
            tagValueList.push(("length", "http://qwilt.com/model/lake-example"), valLength)
        
        if self.isIp6Requested():
            valIp6 = Value()
            valIp6.setEmpty()
            tagValueList.push(("ip6", "http://qwilt.com/model/lake-example"), valIp6)
        
        if self.isIdRequested():
            valId = Value()
            valId.setEmpty()
            tagValueList.push(("id", "http://qwilt.com/model/lake-example"), valId)
        

        
        if self.moodObj:
            valBegin = Value()
            (tag, ns, prefix) = ("mood" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.moodObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-mood-failed').errorFunc(): logFunc('moodObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.antennaObj:
            valBegin = Value()
            (tag, ns, prefix) = ("antenna" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.antennaObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-antenna-failed').errorFunc(): logFunc('antennaObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.testGenerationUnderscoreListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("test-generation_underscore" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.testGenerationUnderscoreListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-test-generation_underscore-failed').errorFunc(): logFunc('testGenerationUnderscoreListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.designObj:
            valBegin = Value()
            (tag, ns, prefix) = ("design" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.designObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-design-failed').errorFunc(): logFunc('designObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.transparentContainerObj:
            valBegin = Value()
            (tag, ns, prefix) = ("transparent-container" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.transparentContainerObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-transparent-container-failed').errorFunc(): logFunc('transparentContainerObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isTransparentFieldRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "transparent-field") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-transparentfield').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "transparentField", "transparent-field", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-transparent-field-bad-value').infoFunc(): logFunc('transparentField not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTransparentField(tempVar)
            for logFunc in self._log('read-tag-values-transparent-field').debug3Func(): logFunc('read transparentField. transparentField=%s, tempValue=%s', self.transparentField, tempValue.getType())
        
        if self.isColorRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "color") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-color').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "color", "color", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-color-bad-value').infoFunc(): logFunc('color not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setColor(tempVar)
            for logFunc in self._log('read-tag-values-color').debug3Func(): logFunc('read color. color=%s, tempValue=%s', self.color, tempValue.getType())
        
        if self.isEyeNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "eye-number") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-eyenumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "eyeNumber", "eye-number", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-eye-number-bad-value').infoFunc(): logFunc('eyeNumber not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEyeNumber(tempVar)
            for logFunc in self._log('read-tag-values-eye-number').debug3Func(): logFunc('read eyeNumber. eyeNumber=%s, tempValue=%s', self.eyeNumber, tempValue.getType())
        
        if self.isHasTailRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "has-tail") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-hastail').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "hasTail", "has-tail", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-has-tail-bad-value').infoFunc(): logFunc('hasTail not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHasTail(tempVar)
            for logFunc in self._log('read-tag-values-has-tail').debug3Func(): logFunc('read hasTail. hasTail=%s, tempValue=%s', self.hasTail, tempValue.getType())
        
        if self.isFinNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "fin-number") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-finnumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "finNumber", "fin-number", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-fin-number-bad-value').infoFunc(): logFunc('finNumber not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFinNumber(tempVar)
            for logFunc in self._log('read-tag-values-fin-number').debug3Func(): logFunc('read finNumber. finNumber=%s, tempValue=%s', self.finNumber, tempValue.getType())
        
        if self.isLengthRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "length") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-length').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "length", "length", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-length-bad-value').infoFunc(): logFunc('length not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLength(tempVar)
            for logFunc in self._log('read-tag-values-length').debug3Func(): logFunc('read length. length=%s, tempValue=%s', self.length, tempValue.getType())
        
        if self.isIp6Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ip6") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-ip6').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "ip6", "ip6", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = (tempValue.asIPv6())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ip6-bad-value').infoFunc(): logFunc('ip6 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setIp6(tempVar)
            for logFunc in self._log('read-tag-values-ip6').debug3Func(): logFunc('read ip6. ip6=%s, tempValue=%s', self.ip6, tempValue.getType())
        
        if self.isIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "id") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-id').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "id", "id", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-id-bad-value').infoFunc(): logFunc('id not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setId(tempVar)
            for logFunc in self._log('read-tag-values-id').debug3Func(): logFunc('read id. id=%s, tempValue=%s', self.id, tempValue.getType())
        

        
        if self.moodObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "mood") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "mood", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.moodObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-mood-failed').errorFunc(): logFunc('moodObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "mood") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "mood", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.antennaObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "antenna") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "antenna", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.antennaObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-antenna-failed').errorFunc(): logFunc('antennaObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "antenna") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "antenna", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.testGenerationUnderscoreListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "test-generation_underscore") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "test-generation_underscore", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.testGenerationUnderscoreListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-test-generation_underscore-failed').errorFunc(): logFunc('testGenerationUnderscoreListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "test-generation_underscore") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "test-generation_underscore", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.designObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "design") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "design", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.designObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-design-failed').errorFunc(): logFunc('designObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "design") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "design", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.transparentContainerObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "transparent-container") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "transparent-container", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.transparentContainerObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-transparent-container-failed').errorFunc(): logFunc('transparentContainerObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "transparent-container") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "transparent-container", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "fish_", 
        "namespace": "fish_", 
        "className": "FishMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.fish__maapi_gen import FishMaapi", 
        "baseClassName": "FishMaapiBase", 
        "baseModule": "fish__maapi_base_gen"
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
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "mood", 
            "yangName": "mood", 
            "className": "BlinkyMoodMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.mood.mood_maapi_gen import BlinkyMoodMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "antenna", 
            "yangName": "antenna", 
            "className": "BlinkyAntennaMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.antenna_maapi_gen import BlinkyAntennaMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "testGenerationUnderscoreList", 
            "yangName": "test-generation_underscore", 
            "className": "BlinkyTestGenerationUnderscoreMaapiList", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.test_generation_underscore.test_generation_underscore_maapi_list_gen import BlinkyTestGenerationUnderscoreMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "design", 
            "yangName": "design", 
            "className": "BlinkyDesignMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.design.design_maapi_gen import BlinkyDesignMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "transparentContainer", 
            "yangName": "transparent-container", 
            "className": "BlinkyTransparentContainerMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.transparent_container.transparent_container_maapi_gen import BlinkyTransparentContainerMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "finNumber", 
            "yangName": "fin-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "ip6", 
            "yangName": "ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
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
            "lake_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "finNumber", 
            "yangName": "fin-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: Ipv6AddressHandlerPy", 
            "memberName": "ip6", 
            "yangName": "ip6", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


