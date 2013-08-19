


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

from antenna_maapi_base_gen import AntennaMaapiBase

from a.sys.blinky.example.lake_example.lake.fish_.antenna.part.part_maapi_list_gen import BlinkyPartMaapiList



class BlinkyAntennaMaapi(AntennaMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-antenna")
        self.domain = None

        
        self.partListObj = None
        

        
        self.aRequested = False
        self.a = None
        self.aSet = False
        
        self.cRequested = False
        self.c = None
        self.cSet = False
        
        self.bRequested = False
        self.b = None
        self.bSet = False
        
        self.eRequested = False
        self.e = None
        self.eSet = False
        
        self.dRequested = False
        self.d = None
        self.dSet = False
        
        self.heightRequested = False
        self.height = None
        self.heightSet = False
        
        self.a1Requested = False
        self.a1 = None
        self.a1Set = False
        
        self.b1Requested = False
        self.b1 = None
        self.b1Set = False
        
        self.c1Requested = False
        self.c1 = None
        self.c1Set = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestA(True)
        
        self.requestC(True)
        
        self.requestB(True)
        
        self.requestE(True)
        
        self.requestD(True)
        
        self.requestHeight(True)
        
        self.requestA1(True)
        
        self.requestB1(True)
        
        self.requestC1(True)
        
        
        
        if not self.partListObj:
            self.partListObj = self.newPartList()
            self.partListObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestA(True)
        
        self.requestC(True)
        
        self.requestB(True)
        
        self.requestE(True)
        
        self.requestD(True)
        
        self.requestHeight(True)
        
        self.requestA1(True)
        
        self.requestB1(True)
        
        self.requestC1(True)
        
        
        
        if not self.partListObj:
            self.partListObj = self.newPartList()
            self.partListObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestA(False)
        
        self.requestC(False)
        
        self.requestB(False)
        
        self.requestE(False)
        
        self.requestD(False)
        
        self.requestHeight(False)
        
        self.requestA1(False)
        
        self.requestB1(False)
        
        self.requestC1(False)
        
        
        
        if not self.partListObj:
            self.partListObj = self.newPartList()
            self.partListObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestA(False)
        
        self.requestC(False)
        
        self.requestB(False)
        
        self.requestE(False)
        
        self.requestD(False)
        
        self.requestHeight(False)
        
        self.requestA1(False)
        
        self.requestB1(False)
        
        self.requestC1(False)
        
        
        
        if not self.partListObj:
            self.partListObj = self.newPartList()
            self.partListObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setA(None)
        self.aSet = False
        
        self.setC(None)
        self.cSet = False
        
        self.setB(None)
        self.bSet = False
        
        self.setE(None)
        self.eSet = False
        
        self.setD(None)
        self.dSet = False
        
        self.setHeight(None)
        self.heightSet = False
        
        self.setA1(None)
        self.a1Set = False
        
        self.setB1(None)
        self.b1Set = False
        
        self.setC1(None)
        self.c1Set = False
        
        
        if self.partListObj:
            self.partListObj.clearAllSet()
        

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

    def newPartList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-partlist').debug3Func(): logFunc('called.')
        partList = BlinkyPartMaapiList(self._log)
        partList.init(self.domain)
        return partList

    def setPartListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-partlist').debug3Func(): logFunc('called. obj=%s', obj)
        self.partListObj = obj

    def getPartListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-partlist').debug3Func(): logFunc('called. self.partListObj=%s', self.partListObj)
        return self.partListObj

    def hasPartList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-partlist').debug3Func(): logFunc('called. self.partListObj=%s', self.partListObj)
        if self.partListObj:
            return True
        return False



    def requestA (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a').debug3Func(): logFunc('called. requested=%s', requested)
        self.aRequested = requested
        self.aSet = False

    def isARequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a-requested').debug3Func(): logFunc('called. requested=%s', self.aRequested)
        return self.aRequested

    def getA (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a').debug3Func(): logFunc('called. self.aSet=%s, self.a=%s', self.aSet, self.a)
        if self.aSet:
            return self.a
        return None

    def hasA (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a').debug3Func(): logFunc('called. self.aSet=%s, self.a=%s', self.aSet, self.a)
        if self.aSet:
            return True
        return False

    def setA (self, a):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a').debug3Func(): logFunc('called. a=%s, old=%s', a, self.a)
        self.aSet = True
        self.a = a

    def requestC (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c').debug3Func(): logFunc('called. requested=%s', requested)
        self.cRequested = requested
        self.cSet = False

    def isCRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c-requested').debug3Func(): logFunc('called. requested=%s', self.cRequested)
        return self.cRequested

    def getC (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c').debug3Func(): logFunc('called. self.cSet=%s, self.c=%s', self.cSet, self.c)
        if self.cSet:
            return self.c
        return None

    def hasC (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c').debug3Func(): logFunc('called. self.cSet=%s, self.c=%s', self.cSet, self.c)
        if self.cSet:
            return True
        return False

    def setC (self, c):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c').debug3Func(): logFunc('called. c=%s, old=%s', c, self.c)
        self.cSet = True
        self.c = c

    def requestB (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b').debug3Func(): logFunc('called. requested=%s', requested)
        self.bRequested = requested
        self.bSet = False

    def isBRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b-requested').debug3Func(): logFunc('called. requested=%s', self.bRequested)
        return self.bRequested

    def getB (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b').debug3Func(): logFunc('called. self.bSet=%s, self.b=%s', self.bSet, self.b)
        if self.bSet:
            return self.b
        return None

    def hasB (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b').debug3Func(): logFunc('called. self.bSet=%s, self.b=%s', self.bSet, self.b)
        if self.bSet:
            return True
        return False

    def setB (self, b):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b').debug3Func(): logFunc('called. b=%s, old=%s', b, self.b)
        self.bSet = True
        self.b = b

    def requestE (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-e').debug3Func(): logFunc('called. requested=%s', requested)
        self.eRequested = requested
        self.eSet = False

    def isERequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-e-requested').debug3Func(): logFunc('called. requested=%s', self.eRequested)
        return self.eRequested

    def getE (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-e').debug3Func(): logFunc('called. self.eSet=%s, self.e=%s', self.eSet, self.e)
        if self.eSet:
            return self.e
        return None

    def hasE (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-e').debug3Func(): logFunc('called. self.eSet=%s, self.e=%s', self.eSet, self.e)
        if self.eSet:
            return True
        return False

    def setE (self, e):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-e').debug3Func(): logFunc('called. e=%s, old=%s', e, self.e)
        self.eSet = True
        self.e = e

    def requestD (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-d').debug3Func(): logFunc('called. requested=%s', requested)
        self.dRequested = requested
        self.dSet = False

    def isDRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-d-requested').debug3Func(): logFunc('called. requested=%s', self.dRequested)
        return self.dRequested

    def getD (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-d').debug3Func(): logFunc('called. self.dSet=%s, self.d=%s', self.dSet, self.d)
        if self.dSet:
            return self.d
        return None

    def hasD (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-d').debug3Func(): logFunc('called. self.dSet=%s, self.d=%s', self.dSet, self.d)
        if self.dSet:
            return True
        return False

    def setD (self, d):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-d').debug3Func(): logFunc('called. d=%s, old=%s', d, self.d)
        self.dSet = True
        self.d = d

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

    def requestA1 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a1').debug3Func(): logFunc('called. requested=%s', requested)
        self.a1Requested = requested
        self.a1Set = False

    def isA1Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a1-requested').debug3Func(): logFunc('called. requested=%s', self.a1Requested)
        return self.a1Requested

    def getA1 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a1').debug3Func(): logFunc('called. self.a1Set=%s, self.a1=%s', self.a1Set, self.a1)
        if self.a1Set:
            return self.a1
        return None

    def hasA1 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a1').debug3Func(): logFunc('called. self.a1Set=%s, self.a1=%s', self.a1Set, self.a1)
        if self.a1Set:
            return True
        return False

    def setA1 (self, a1):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a1').debug3Func(): logFunc('called. a1=%s, old=%s', a1, self.a1)
        self.a1Set = True
        self.a1 = a1

    def requestB1 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b1').debug3Func(): logFunc('called. requested=%s', requested)
        self.b1Requested = requested
        self.b1Set = False

    def isB1Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b1-requested').debug3Func(): logFunc('called. requested=%s', self.b1Requested)
        return self.b1Requested

    def getB1 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b1').debug3Func(): logFunc('called. self.b1Set=%s, self.b1=%s', self.b1Set, self.b1)
        if self.b1Set:
            return self.b1
        return None

    def hasB1 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b1').debug3Func(): logFunc('called. self.b1Set=%s, self.b1=%s', self.b1Set, self.b1)
        if self.b1Set:
            return True
        return False

    def setB1 (self, b1):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b1').debug3Func(): logFunc('called. b1=%s, old=%s', b1, self.b1)
        self.b1Set = True
        self.b1 = b1

    def requestC1 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c1').debug3Func(): logFunc('called. requested=%s', requested)
        self.c1Requested = requested
        self.c1Set = False

    def isC1Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c1-requested').debug3Func(): logFunc('called. requested=%s', self.c1Requested)
        return self.c1Requested

    def getC1 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c1').debug3Func(): logFunc('called. self.c1Set=%s, self.c1=%s', self.c1Set, self.c1)
        if self.c1Set:
            return self.c1
        return None

    def hasC1 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c1').debug3Func(): logFunc('called. self.c1Set=%s, self.c1=%s', self.c1Set, self.c1)
        if self.c1Set:
            return True
        return False

    def setC1 (self, c1):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c1').debug3Func(): logFunc('called. c1=%s, old=%s', c1, self.c1)
        self.c1Set = True
        self.c1 = c1


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.partListObj:
            self.partListObj._clearAllReadData()
        

        
        self.a = 0
        self.aSet = False
        
        self.c = 0
        self.cSet = False
        
        self.b = 0
        self.bSet = False
        
        self.e = 0
        self.eSet = False
        
        self.d = 0
        self.dSet = False
        
        self.height = 0
        self.heightSet = False
        
        self.a1 = 0
        self.a1Set = False
        
        self.b1 = 0
        self.b1Set = False
        
        self.c1 = 0
        self.c1Set = False
        

    def _getSelfKeyPath (self, lake
                         , fish_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("antenna", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
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

        
        if self.partListObj:
            res = self.partListObj._collectItemsToDelete(lake, 
                                                                          fish_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-parts-failed').errorFunc(): logFunc('partListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasA():
            valA = Value()
            if self.a is not None:
                valA.setInt64(self.a)
            else:
                valA.setEmpty()
            tagValueList.push(("a", "http://qwilt.com/model/lake-example"), valA)
        
        if self.hasC():
            valC = Value()
            if self.c is not None:
                valC.setInt64(self.c)
            else:
                valC.setEmpty()
            tagValueList.push(("c", "http://qwilt.com/model/lake-example"), valC)
        
        if self.hasB():
            valB = Value()
            if self.b is not None:
                valB.setInt64(self.b)
            else:
                valB.setEmpty()
            tagValueList.push(("b", "http://qwilt.com/model/lake-example"), valB)
        
        if self.hasE():
            valE = Value()
            if self.e is not None:
                valE.setInt64(self.e)
            else:
                valE.setEmpty()
            tagValueList.push(("e", "http://qwilt.com/model/lake-example"), valE)
        
        if self.hasD():
            valD = Value()
            if self.d is not None:
                valD.setInt64(self.d)
            else:
                valD.setEmpty()
            tagValueList.push(("d", "http://qwilt.com/model/lake-example"), valD)
        
        if self.hasHeight():
            valHeight = Value()
            if self.height is not None:
                valHeight.setInt64(self.height)
            else:
                valHeight.setEmpty()
            tagValueList.push(("height", "http://qwilt.com/model/lake-example"), valHeight)
        
        if self.hasA1():
            valA1 = Value()
            if self.a1 is not None:
                valA1.setString(self.a1)
            else:
                valA1.setEmpty()
            tagValueList.push(("a1", "http://qwilt.com/model/lake-example"), valA1)
        
        if self.hasB1():
            valB1 = Value()
            if self.b1 is not None:
                valB1.setString(self.b1)
            else:
                valB1.setEmpty()
            tagValueList.push(("b1", "http://qwilt.com/model/lake-example"), valB1)
        
        if self.hasC1():
            valC1 = Value()
            if self.c1 is not None:
                valC1.setString(self.c1)
            else:
                valC1.setEmpty()
            tagValueList.push(("c1", "http://qwilt.com/model/lake-example"), valC1)
        

        
        if self.partListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("parts" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.partListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-parts-failed').errorFunc(): logFunc('partListObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isARequested():
            valA = Value()
            valA.setEmpty()
            tagValueList.push(("a", "http://qwilt.com/model/lake-example"), valA)
        
        if self.isCRequested():
            valC = Value()
            valC.setEmpty()
            tagValueList.push(("c", "http://qwilt.com/model/lake-example"), valC)
        
        if self.isBRequested():
            valB = Value()
            valB.setEmpty()
            tagValueList.push(("b", "http://qwilt.com/model/lake-example"), valB)
        
        if self.isERequested():
            valE = Value()
            valE.setEmpty()
            tagValueList.push(("e", "http://qwilt.com/model/lake-example"), valE)
        
        if self.isDRequested():
            valD = Value()
            valD.setEmpty()
            tagValueList.push(("d", "http://qwilt.com/model/lake-example"), valD)
        
        if self.isHeightRequested():
            valHeight = Value()
            valHeight.setEmpty()
            tagValueList.push(("height", "http://qwilt.com/model/lake-example"), valHeight)
        
        if self.isA1Requested():
            valA1 = Value()
            valA1.setEmpty()
            tagValueList.push(("a1", "http://qwilt.com/model/lake-example"), valA1)
        
        if self.isB1Requested():
            valB1 = Value()
            valB1.setEmpty()
            tagValueList.push(("b1", "http://qwilt.com/model/lake-example"), valB1)
        
        if self.isC1Requested():
            valC1 = Value()
            valC1.setEmpty()
            tagValueList.push(("c1", "http://qwilt.com/model/lake-example"), valC1)
        

        
        if self.partListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("parts" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.partListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-parts-failed').errorFunc(): logFunc('partListObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isARequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a", "a", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a-bad-value').infoFunc(): logFunc('a not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA(tempVar)
            for logFunc in self._log('read-tag-values-a').debug3Func(): logFunc('read a. a=%s, tempValue=%s', self.a, tempValue.getType())
        
        if self.isCRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c", "c", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c-bad-value').infoFunc(): logFunc('c not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC(tempVar)
            for logFunc in self._log('read-tag-values-c').debug3Func(): logFunc('read c. c=%s, tempValue=%s', self.c, tempValue.getType())
        
        if self.isBRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b", "b", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b-bad-value').infoFunc(): logFunc('b not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB(tempVar)
            for logFunc in self._log('read-tag-values-b').debug3Func(): logFunc('read b. b=%s, tempValue=%s', self.b, tempValue.getType())
        
        if self.isERequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "e") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-e').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "e", "e", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-e-bad-value').infoFunc(): logFunc('e not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setE(tempVar)
            for logFunc in self._log('read-tag-values-e').debug3Func(): logFunc('read e. e=%s, tempValue=%s', self.e, tempValue.getType())
        
        if self.isDRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "d") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-d').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "d", "d", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-d-bad-value').infoFunc(): logFunc('d not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setD(tempVar)
            for logFunc in self._log('read-tag-values-d').debug3Func(): logFunc('read d. d=%s, tempValue=%s', self.d, tempValue.getType())
        
        if self.isHeightRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "height") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-height').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "height", "height", "http://qwilt.com/model/lake-example", tag, ns)
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
        
        if self.isA1Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a1") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a1').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a1", "a1", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a1-bad-value').infoFunc(): logFunc('a1 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA1(tempVar)
            for logFunc in self._log('read-tag-values-a1').debug3Func(): logFunc('read a1. a1=%s, tempValue=%s', self.a1, tempValue.getType())
        
        if self.isB1Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b1") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b1').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b1", "b1", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b1-bad-value').infoFunc(): logFunc('b1 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB1(tempVar)
            for logFunc in self._log('read-tag-values-b1').debug3Func(): logFunc('read b1. b1=%s, tempValue=%s', self.b1, tempValue.getType())
        
        if self.isC1Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c1") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c1').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c1", "c1", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c1-bad-value').infoFunc(): logFunc('c1 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC1(tempVar)
            for logFunc in self._log('read-tag-values-c1').debug3Func(): logFunc('read c1. c1=%s, tempValue=%s', self.c1, tempValue.getType())
        

        
        if self.partListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "parts") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "parts", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.partListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-parts-failed').errorFunc(): logFunc('partListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "parts") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "parts", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "antenna", 
        "namespace": "antenna", 
        "className": "AntennaMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.antenna_maapi_gen import AntennaMaapi", 
        "baseClassName": "AntennaMaapiBase", 
        "baseModule": "antenna_maapi_base_gen"
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
            "isCurrent": false, 
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
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "antenna", 
            "namespace": "antenna", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "antenna"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "partList", 
            "yangName": "parts", 
            "className": "BlinkyPartMaapiList", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.antenna.part.part_maapi_list_gen import BlinkyPartMaapiList", 
            "isList": true, 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "a", 
            "yangName": "a", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "c", 
            "yangName": "c", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "b", 
            "yangName": "b", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "e", 
            "yangName": "e", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "d", 
            "yangName": "d", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a1", 
            "yangName": "a1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b1", 
            "yangName": "b1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c1", 
            "yangName": "c1", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "a", 
            "yangName": "a", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "c", 
            "yangName": "c", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "b", 
            "yangName": "b", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "e", 
            "yangName": "e", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "d", 
            "yangName": "d", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a1", 
            "yangName": "a1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b1", 
            "yangName": "b1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c1", 
            "yangName": "c1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


