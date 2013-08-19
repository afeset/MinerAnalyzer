


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

from bbb_maapi_base_gen import BbbMaapiBase




class BlinkyBbbMaapi(BbbMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-bbb")
        self.domain = None

        

        
        self.b4int64Requested = False
        self.b4int64 = None
        self.b4int64Set = False
        
        self.b6strRequested = False
        self.b6str = None
        self.b6strSet = False
        
        self.b3strRequested = False
        self.b3str = None
        self.b3strSet = False
        
        self.b5strRequested = False
        self.b5str = None
        self.b5strSet = False
        
        self.b7strRequested = False
        self.b7str = None
        self.b7strSet = False
        
        self.b9strRequested = False
        self.b9str = None
        self.b9strSet = False
        
        self.b1strRequested = False
        self.b1str = None
        self.b1strSet = False
        
        self.b8strRequested = False
        self.b8str = None
        self.b8strSet = False
        
        self.b2strRequested = False
        self.b2str = None
        self.b2strSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestB4int64(True)
        
        self.requestB6str(True)
        
        self.requestB3str(True)
        
        self.requestB5str(True)
        
        self.requestB7str(True)
        
        self.requestB9str(True)
        
        self.requestB1str(True)
        
        self.requestB8str(True)
        
        self.requestB2str(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestB4int64(True)
        
        self.requestB6str(True)
        
        self.requestB3str(True)
        
        self.requestB5str(True)
        
        self.requestB7str(True)
        
        self.requestB9str(True)
        
        self.requestB1str(True)
        
        self.requestB8str(True)
        
        self.requestB2str(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestB4int64(False)
        
        self.requestB6str(False)
        
        self.requestB3str(False)
        
        self.requestB5str(False)
        
        self.requestB7str(False)
        
        self.requestB9str(False)
        
        self.requestB1str(False)
        
        self.requestB8str(False)
        
        self.requestB2str(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestB4int64(False)
        
        self.requestB6str(False)
        
        self.requestB3str(False)
        
        self.requestB5str(False)
        
        self.requestB7str(False)
        
        self.requestB9str(False)
        
        self.requestB1str(False)
        
        self.requestB8str(False)
        
        self.requestB2str(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setB4int64(None)
        self.b4int64Set = False
        
        self.setB6str(None)
        self.b6strSet = False
        
        self.setB3str(None)
        self.b3strSet = False
        
        self.setB5str(None)
        self.b5strSet = False
        
        self.setB7str(None)
        self.b7strSet = False
        
        self.setB9str(None)
        self.b9strSet = False
        
        self.setB1str(None)
        self.b1strSet = False
        
        self.setB8str(None)
        self.b8strSet = False
        
        self.setB2str(None)
        self.b2strSet = False
        
        

    def write (self
              , lll
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(lll, trxContext)

    def read (self
              , lll
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lll, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , lll
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lll, 
                                  True,
                                  trxContext)



    def requestB4int64 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b4int64').debug3Func(): logFunc('called. requested=%s', requested)
        self.b4int64Requested = requested
        self.b4int64Set = False

    def isB4int64Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b4int64-requested').debug3Func(): logFunc('called. requested=%s', self.b4int64Requested)
        return self.b4int64Requested

    def getB4int64 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b4int64').debug3Func(): logFunc('called. self.b4int64Set=%s, self.b4int64=%s', self.b4int64Set, self.b4int64)
        if self.b4int64Set:
            return self.b4int64
        return None

    def hasB4int64 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b4int64').debug3Func(): logFunc('called. self.b4int64Set=%s, self.b4int64=%s', self.b4int64Set, self.b4int64)
        if self.b4int64Set:
            return True
        return False

    def setB4int64 (self, b4int64):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b4int64').debug3Func(): logFunc('called. b4int64=%s, old=%s', b4int64, self.b4int64)
        self.b4int64Set = True
        self.b4int64 = b4int64

    def requestB6str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b6str').debug3Func(): logFunc('called. requested=%s', requested)
        self.b6strRequested = requested
        self.b6strSet = False

    def isB6strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b6str-requested').debug3Func(): logFunc('called. requested=%s', self.b6strRequested)
        return self.b6strRequested

    def getB6str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b6str').debug3Func(): logFunc('called. self.b6strSet=%s, self.b6str=%s', self.b6strSet, self.b6str)
        if self.b6strSet:
            return self.b6str
        return None

    def hasB6str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b6str').debug3Func(): logFunc('called. self.b6strSet=%s, self.b6str=%s', self.b6strSet, self.b6str)
        if self.b6strSet:
            return True
        return False

    def setB6str (self, b6str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b6str').debug3Func(): logFunc('called. b6str=%s, old=%s', b6str, self.b6str)
        self.b6strSet = True
        self.b6str = b6str

    def requestB3str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b3str').debug3Func(): logFunc('called. requested=%s', requested)
        self.b3strRequested = requested
        self.b3strSet = False

    def isB3strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b3str-requested').debug3Func(): logFunc('called. requested=%s', self.b3strRequested)
        return self.b3strRequested

    def getB3str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b3str').debug3Func(): logFunc('called. self.b3strSet=%s, self.b3str=%s', self.b3strSet, self.b3str)
        if self.b3strSet:
            return self.b3str
        return None

    def hasB3str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b3str').debug3Func(): logFunc('called. self.b3strSet=%s, self.b3str=%s', self.b3strSet, self.b3str)
        if self.b3strSet:
            return True
        return False

    def setB3str (self, b3str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b3str').debug3Func(): logFunc('called. b3str=%s, old=%s', b3str, self.b3str)
        self.b3strSet = True
        self.b3str = b3str

    def requestB5str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b5str').debug3Func(): logFunc('called. requested=%s', requested)
        self.b5strRequested = requested
        self.b5strSet = False

    def isB5strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b5str-requested').debug3Func(): logFunc('called. requested=%s', self.b5strRequested)
        return self.b5strRequested

    def getB5str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b5str').debug3Func(): logFunc('called. self.b5strSet=%s, self.b5str=%s', self.b5strSet, self.b5str)
        if self.b5strSet:
            return self.b5str
        return None

    def hasB5str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b5str').debug3Func(): logFunc('called. self.b5strSet=%s, self.b5str=%s', self.b5strSet, self.b5str)
        if self.b5strSet:
            return True
        return False

    def setB5str (self, b5str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b5str').debug3Func(): logFunc('called. b5str=%s, old=%s', b5str, self.b5str)
        self.b5strSet = True
        self.b5str = b5str

    def requestB7str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b7str').debug3Func(): logFunc('called. requested=%s', requested)
        self.b7strRequested = requested
        self.b7strSet = False

    def isB7strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b7str-requested').debug3Func(): logFunc('called. requested=%s', self.b7strRequested)
        return self.b7strRequested

    def getB7str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b7str').debug3Func(): logFunc('called. self.b7strSet=%s, self.b7str=%s', self.b7strSet, self.b7str)
        if self.b7strSet:
            return self.b7str
        return None

    def hasB7str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b7str').debug3Func(): logFunc('called. self.b7strSet=%s, self.b7str=%s', self.b7strSet, self.b7str)
        if self.b7strSet:
            return True
        return False

    def setB7str (self, b7str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b7str').debug3Func(): logFunc('called. b7str=%s, old=%s', b7str, self.b7str)
        self.b7strSet = True
        self.b7str = b7str

    def requestB9str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b9str').debug3Func(): logFunc('called. requested=%s', requested)
        self.b9strRequested = requested
        self.b9strSet = False

    def isB9strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b9str-requested').debug3Func(): logFunc('called. requested=%s', self.b9strRequested)
        return self.b9strRequested

    def getB9str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b9str').debug3Func(): logFunc('called. self.b9strSet=%s, self.b9str=%s', self.b9strSet, self.b9str)
        if self.b9strSet:
            return self.b9str
        return None

    def hasB9str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b9str').debug3Func(): logFunc('called. self.b9strSet=%s, self.b9str=%s', self.b9strSet, self.b9str)
        if self.b9strSet:
            return True
        return False

    def setB9str (self, b9str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b9str').debug3Func(): logFunc('called. b9str=%s, old=%s', b9str, self.b9str)
        self.b9strSet = True
        self.b9str = b9str

    def requestB1str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b1str').debug3Func(): logFunc('called. requested=%s', requested)
        self.b1strRequested = requested
        self.b1strSet = False

    def isB1strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b1str-requested').debug3Func(): logFunc('called. requested=%s', self.b1strRequested)
        return self.b1strRequested

    def getB1str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b1str').debug3Func(): logFunc('called. self.b1strSet=%s, self.b1str=%s', self.b1strSet, self.b1str)
        if self.b1strSet:
            return self.b1str
        return None

    def hasB1str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b1str').debug3Func(): logFunc('called. self.b1strSet=%s, self.b1str=%s', self.b1strSet, self.b1str)
        if self.b1strSet:
            return True
        return False

    def setB1str (self, b1str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b1str').debug3Func(): logFunc('called. b1str=%s, old=%s', b1str, self.b1str)
        self.b1strSet = True
        self.b1str = b1str

    def requestB8str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b8str').debug3Func(): logFunc('called. requested=%s', requested)
        self.b8strRequested = requested
        self.b8strSet = False

    def isB8strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b8str-requested').debug3Func(): logFunc('called. requested=%s', self.b8strRequested)
        return self.b8strRequested

    def getB8str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b8str').debug3Func(): logFunc('called. self.b8strSet=%s, self.b8str=%s', self.b8strSet, self.b8str)
        if self.b8strSet:
            return self.b8str
        return None

    def hasB8str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b8str').debug3Func(): logFunc('called. self.b8strSet=%s, self.b8str=%s', self.b8strSet, self.b8str)
        if self.b8strSet:
            return True
        return False

    def setB8str (self, b8str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b8str').debug3Func(): logFunc('called. b8str=%s, old=%s', b8str, self.b8str)
        self.b8strSet = True
        self.b8str = b8str

    def requestB2str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-b2str').debug3Func(): logFunc('called. requested=%s', requested)
        self.b2strRequested = requested
        self.b2strSet = False

    def isB2strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-b2str-requested').debug3Func(): logFunc('called. requested=%s', self.b2strRequested)
        return self.b2strRequested

    def getB2str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-b2str').debug3Func(): logFunc('called. self.b2strSet=%s, self.b2str=%s', self.b2strSet, self.b2str)
        if self.b2strSet:
            return self.b2str
        return None

    def hasB2str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-b2str').debug3Func(): logFunc('called. self.b2strSet=%s, self.b2str=%s', self.b2strSet, self.b2str)
        if self.b2strSet:
            return True
        return False

    def setB2str (self, b2str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-b2str').debug3Func(): logFunc('called. b2str=%s, old=%s', b2str, self.b2str)
        self.b2strSet = True
        self.b2str = b2str


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.b4int64 = 0
        self.b4int64Set = False
        
        self.b6str = 0
        self.b6strSet = False
        
        self.b3str = 0
        self.b3strSet = False
        
        self.b5str = 0
        self.b5strSet = False
        
        self.b7str = 0
        self.b7strSet = False
        
        self.b9str = 0
        self.b9strSet = False
        
        self.b1str = 0
        self.b1strSet = False
        
        self.b8str = 0
        self.b8strSet = False
        
        self.b2str = 0
        self.b2strSet = False
        

    def _getSelfKeyPath (self, lll
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("bbb", "http://qwilt.com/model/benchmark", "bnch"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(lll);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("lll", "http://qwilt.com/model/benchmark", "bnch"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("base", "http://qwilt.com/model/benchmark", "bnch"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        lll, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(lll, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(lll, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       lll, 
                       
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

        keyPath = self._getSelfKeyPath(lll, 
                                       
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
                               lll, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasB4int64():
            valB4int64 = Value()
            if self.b4int64 is not None:
                valB4int64.setInt64(self.b4int64)
            else:
                valB4int64.setEmpty()
            tagValueList.push(("b4int64", "http://qwilt.com/model/benchmark"), valB4int64)
        
        if self.hasB6str():
            valB6str = Value()
            if self.b6str is not None:
                valB6str.setString(self.b6str)
            else:
                valB6str.setEmpty()
            tagValueList.push(("b6str", "http://qwilt.com/model/benchmark"), valB6str)
        
        if self.hasB3str():
            valB3str = Value()
            if self.b3str is not None:
                valB3str.setString(self.b3str)
            else:
                valB3str.setEmpty()
            tagValueList.push(("b3str", "http://qwilt.com/model/benchmark"), valB3str)
        
        if self.hasB5str():
            valB5str = Value()
            if self.b5str is not None:
                valB5str.setString(self.b5str)
            else:
                valB5str.setEmpty()
            tagValueList.push(("b5str", "http://qwilt.com/model/benchmark"), valB5str)
        
        if self.hasB7str():
            valB7str = Value()
            if self.b7str is not None:
                valB7str.setString(self.b7str)
            else:
                valB7str.setEmpty()
            tagValueList.push(("b7str", "http://qwilt.com/model/benchmark"), valB7str)
        
        if self.hasB9str():
            valB9str = Value()
            if self.b9str is not None:
                valB9str.setString(self.b9str)
            else:
                valB9str.setEmpty()
            tagValueList.push(("b9str", "http://qwilt.com/model/benchmark"), valB9str)
        
        if self.hasB1str():
            valB1str = Value()
            if self.b1str is not None:
                valB1str.setString(self.b1str)
            else:
                valB1str.setEmpty()
            tagValueList.push(("b1str", "http://qwilt.com/model/benchmark"), valB1str)
        
        if self.hasB8str():
            valB8str = Value()
            if self.b8str is not None:
                valB8str.setString(self.b8str)
            else:
                valB8str.setEmpty()
            tagValueList.push(("b8str", "http://qwilt.com/model/benchmark"), valB8str)
        
        if self.hasB2str():
            valB2str = Value()
            if self.b2str is not None:
                valB2str.setString(self.b2str)
            else:
                valB2str.setEmpty()
            tagValueList.push(("b2str", "http://qwilt.com/model/benchmark"), valB2str)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isB4int64Requested():
            valB4int64 = Value()
            valB4int64.setEmpty()
            tagValueList.push(("b4int64", "http://qwilt.com/model/benchmark"), valB4int64)
        
        if self.isB6strRequested():
            valB6str = Value()
            valB6str.setEmpty()
            tagValueList.push(("b6str", "http://qwilt.com/model/benchmark"), valB6str)
        
        if self.isB3strRequested():
            valB3str = Value()
            valB3str.setEmpty()
            tagValueList.push(("b3str", "http://qwilt.com/model/benchmark"), valB3str)
        
        if self.isB5strRequested():
            valB5str = Value()
            valB5str.setEmpty()
            tagValueList.push(("b5str", "http://qwilt.com/model/benchmark"), valB5str)
        
        if self.isB7strRequested():
            valB7str = Value()
            valB7str.setEmpty()
            tagValueList.push(("b7str", "http://qwilt.com/model/benchmark"), valB7str)
        
        if self.isB9strRequested():
            valB9str = Value()
            valB9str.setEmpty()
            tagValueList.push(("b9str", "http://qwilt.com/model/benchmark"), valB9str)
        
        if self.isB1strRequested():
            valB1str = Value()
            valB1str.setEmpty()
            tagValueList.push(("b1str", "http://qwilt.com/model/benchmark"), valB1str)
        
        if self.isB8strRequested():
            valB8str = Value()
            valB8str.setEmpty()
            tagValueList.push(("b8str", "http://qwilt.com/model/benchmark"), valB8str)
        
        if self.isB2strRequested():
            valB2str = Value()
            valB2str.setEmpty()
            tagValueList.push(("b2str", "http://qwilt.com/model/benchmark"), valB2str)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isB4int64Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b4int64") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b4int64').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b4int64", "b4int64", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b4int64-bad-value').infoFunc(): logFunc('b4int64 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB4int64(tempVar)
            for logFunc in self._log('read-tag-values-b4int64').debug3Func(): logFunc('read b4int64. b4int64=%s, tempValue=%s', self.b4int64, tempValue.getType())
        
        if self.isB6strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b6str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b6str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b6str", "b6str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b6str-bad-value').infoFunc(): logFunc('b6str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB6str(tempVar)
            for logFunc in self._log('read-tag-values-b6str').debug3Func(): logFunc('read b6str. b6str=%s, tempValue=%s', self.b6str, tempValue.getType())
        
        if self.isB3strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b3str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b3str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b3str", "b3str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b3str-bad-value').infoFunc(): logFunc('b3str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB3str(tempVar)
            for logFunc in self._log('read-tag-values-b3str').debug3Func(): logFunc('read b3str. b3str=%s, tempValue=%s', self.b3str, tempValue.getType())
        
        if self.isB5strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b5str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b5str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b5str", "b5str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b5str-bad-value').infoFunc(): logFunc('b5str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB5str(tempVar)
            for logFunc in self._log('read-tag-values-b5str').debug3Func(): logFunc('read b5str. b5str=%s, tempValue=%s', self.b5str, tempValue.getType())
        
        if self.isB7strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b7str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b7str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b7str", "b7str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b7str-bad-value').infoFunc(): logFunc('b7str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB7str(tempVar)
            for logFunc in self._log('read-tag-values-b7str').debug3Func(): logFunc('read b7str. b7str=%s, tempValue=%s', self.b7str, tempValue.getType())
        
        if self.isB9strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b9str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b9str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b9str", "b9str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b9str-bad-value').infoFunc(): logFunc('b9str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB9str(tempVar)
            for logFunc in self._log('read-tag-values-b9str').debug3Func(): logFunc('read b9str. b9str=%s, tempValue=%s', self.b9str, tempValue.getType())
        
        if self.isB1strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b1str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b1str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b1str", "b1str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b1str-bad-value').infoFunc(): logFunc('b1str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB1str(tempVar)
            for logFunc in self._log('read-tag-values-b1str').debug3Func(): logFunc('read b1str. b1str=%s, tempValue=%s', self.b1str, tempValue.getType())
        
        if self.isB8strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b8str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b8str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b8str", "b8str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b8str-bad-value').infoFunc(): logFunc('b8str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB8str(tempVar)
            for logFunc in self._log('read-tag-values-b8str').debug3Func(): logFunc('read b8str. b8str=%s, tempValue=%s', self.b8str, tempValue.getType())
        
        if self.isB2strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "b2str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-b2str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "b2str", "b2str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-b2str-bad-value').infoFunc(): logFunc('b2str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setB2str(tempVar)
            for logFunc in self._log('read-tag-values-b2str').debug3Func(): logFunc('read b2str. b2str=%s, tempValue=%s', self.b2str, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "bbb", 
        "namespace": "bbb", 
        "className": "BbbMaapi", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.bbb.bbb_maapi_gen import BbbMaapi", 
        "baseClassName": "BbbMaapiBase", 
        "baseModule": "bbb_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "bnch", 
            "yangName": "base", 
            "namespace": "base", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "base"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "isCurrent": false, 
            "yangName": "lll", 
            "namespace": "lll", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "keyLeaf": {
                "varName": "lll", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lll"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "yangName": "bbb", 
            "namespace": "bbb", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "bbb"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "b4int64", 
            "yangName": "b4int64", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b6str", 
            "yangName": "b6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b3str", 
            "yangName": "b3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b5str", 
            "yangName": "b5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b7str", 
            "yangName": "b7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b9str", 
            "yangName": "b9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b1str", 
            "yangName": "b1str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b8str", 
            "yangName": "b8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b2str", 
            "yangName": "b2str", 
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
            "benchmark", 
            "benchmark"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "b4int64", 
            "yangName": "b4int64", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b6str", 
            "yangName": "b6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b3str", 
            "yangName": "b3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b5str", 
            "yangName": "b5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b7str", 
            "yangName": "b7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b9str", 
            "yangName": "b9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b1str", 
            "yangName": "b1str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b8str", 
            "yangName": "b8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "b2str", 
            "yangName": "b2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


