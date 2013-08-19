


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

from a.build.example.yang.modules.room.table.fish_.antenna.antenna_maapi_gen import BlinkyAntennaMaapi



class BlinkyFishMaapi(FishMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-fish_")
        self.domain = None

        
        self.antennaObj = None
        

        
        self.eyeNumberRequested = False
        self.eyeNumber = None
        self.eyeNumberSet = False
        
        self.transparentFieldRequested = False
        self.transparentField = None
        self.transparentFieldSet = False
        
        self.idRequested = False
        self.id = None
        self.idSet = False
        
        self.hasTailRequested = False
        self.hasTail = None
        self.hasTailSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEyeNumber(True)
        
        self.requestTransparentField(True)
        
        self.requestId(True)
        
        self.requestHasTail(True)
        
        
        
        if not self.antennaObj:
            self.antennaObj = self.newAntenna()
            self.antennaObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEyeNumber(True)
        
        self.requestTransparentField(True)
        
        self.requestId(True)
        
        self.requestHasTail(True)
        
        
        
        if not self.antennaObj:
            self.antennaObj = self.newAntenna()
            self.antennaObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEyeNumber(False)
        
        self.requestTransparentField(False)
        
        self.requestId(False)
        
        self.requestHasTail(False)
        
        
        
        if not self.antennaObj:
            self.antennaObj = self.newAntenna()
            self.antennaObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEyeNumber(False)
        
        self.requestTransparentField(False)
        
        self.requestId(False)
        
        self.requestHasTail(False)
        
        
        
        if not self.antennaObj:
            self.antennaObj = self.newAntenna()
            self.antennaObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setEyeNumber(None)
        self.eyeNumberSet = False
        
        self.setTransparentField(None)
        self.transparentFieldSet = False
        
        self.setId(None)
        self.idSet = False
        
        self.setHasTail(None)
        self.hasTailSet = False
        
        
        if self.antennaObj:
            self.antennaObj.clearAllSet()
        

    def write (self
              , table
              , fish_
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(table, fish_, trxContext)

    def read (self
              , table
              , fish_
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(table, fish_, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , table
                       , fish_
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(table, fish_, 
                                  True,
                                  trxContext)

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.antennaObj:
            self.antennaObj._clearAllReadData()
        

        
        self.eyeNumber = 0
        self.eyeNumberSet = False
        
        self.transparentField = 0
        self.transparentFieldSet = False
        
        self.id = 0
        self.idSet = False
        
        self.hasTail = 0
        self.hasTailSet = False
        

    def _getSelfKeyPath (self, table
                         , fish_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(fish_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fish", "http://qwilt.com/model/room", "room"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(table);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("table", "http://qwilt.com/model/room", "room"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        table, 
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
        res = self._collectItemsToDelete(table, 
                                         fish_, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(table, 
                                       fish_, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       table, 
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

        keyPath = self._getSelfKeyPath(table, 
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
                               table, 
                               fish_, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.antennaObj:
            res = self.antennaObj._collectItemsToDelete(table, 
                                                                          fish_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-antenna-failed').errorFunc(): logFunc('antennaObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasEyeNumber():
            valEyeNumber = Value()
            if self.eyeNumber is not None:
                valEyeNumber.setInt64(self.eyeNumber)
            else:
                valEyeNumber.setEmpty()
            tagValueList.push(("eye-number", "http://qwilt.com/model/room"), valEyeNumber)
        
        if self.hasTransparentField():
            valTransparentField = Value()
            if self.transparentField is not None:
                valTransparentField.setBool(self.transparentField)
            else:
                valTransparentField.setEmpty()
            tagValueList.push(("transparent-field", "http://qwilt.com/model/room"), valTransparentField)
        
        if self.hasId():
            valId = Value()
            if self.id is not None:
                valId.setString(self.id)
            else:
                valId.setEmpty()
            tagValueList.push(("id", "http://qwilt.com/model/room"), valId)
        
        if self.hasHasTail():
            valHasTail = Value()
            if self.hasTail is not None:
                valHasTail.setBool(self.hasTail)
            else:
                valHasTail.setEmpty()
            tagValueList.push(("has-tail", "http://qwilt.com/model/room"), valHasTail)
        

        
        if self.antennaObj:
            valBegin = Value()
            (tag, ns, prefix) = ("antenna" , "http://qwilt.com/model/room", "room")
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
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isEyeNumberRequested():
            valEyeNumber = Value()
            valEyeNumber.setEmpty()
            tagValueList.push(("eye-number", "http://qwilt.com/model/room"), valEyeNumber)
        
        if self.isTransparentFieldRequested():
            valTransparentField = Value()
            valTransparentField.setEmpty()
            tagValueList.push(("transparent-field", "http://qwilt.com/model/room"), valTransparentField)
        
        if self.isIdRequested():
            valId = Value()
            valId.setEmpty()
            tagValueList.push(("id", "http://qwilt.com/model/room"), valId)
        
        if self.isHasTailRequested():
            valHasTail = Value()
            valHasTail.setEmpty()
            tagValueList.push(("has-tail", "http://qwilt.com/model/room"), valHasTail)
        

        
        if self.antennaObj:
            valBegin = Value()
            (tag, ns, prefix) = ("antenna" , "http://qwilt.com/model/room", "room")
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
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isEyeNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "eye-number") or \
                (ns != "http://qwilt.com/model/room"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-eyenumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "eyeNumber", "eye-number", "http://qwilt.com/model/room", tag, ns)
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
        
        if self.isTransparentFieldRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "transparent-field") or \
                (ns != "http://qwilt.com/model/room"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-transparentfield').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "transparentField", "transparent-field", "http://qwilt.com/model/room", tag, ns)
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
        
        if self.isIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "id") or \
                (ns != "http://qwilt.com/model/room"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-id').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "id", "id", "http://qwilt.com/model/room", tag, ns)
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
        
        if self.isHasTailRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "has-tail") or \
                (ns != "http://qwilt.com/model/room"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-hastail').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "hasTail", "has-tail", "http://qwilt.com/model/room", tag, ns)
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
        

        
        if self.antennaObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "antenna") or \
                (ns != "http://qwilt.com/model/room") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "antenna", "http://qwilt.com/model/room", Value.kXmlBegin,
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
                (ns != "http://qwilt.com/model/room") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "antenna", "http://qwilt.com/model/room", Value.kXmlEnd,
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
        "importStatement": "from a.build.example.yang.modules.room.table.fish_.fish__maapi_gen import FishMaapi", 
        "baseClassName": "FishMaapiBase", 
        "baseModule": "fish__maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "room", 
            "isCurrent": false, 
            "yangName": "table", 
            "namespace": "table", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "keyLeaf": {
                "varName": "table", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "table"
        }, 
        {
            "moduleYangNamespacePrefix": "room", 
            "isCurrent": true, 
            "yangName": "fish", 
            "namespace": "fish_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/room", 
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
            "moduleYangNamespacePrefix": "room", 
            "memberName": "antenna", 
            "yangName": "antenna", 
            "className": "BlinkyAntennaMaapi", 
            "importStatement": "from a.build.example.yang.modules.room.table.fish_.antenna.antenna_maapi_gen import BlinkyAntennaMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/room"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "build", 
            "example", 
            "yang", 
            "modules", 
            "room"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


