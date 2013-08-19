


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

from aaa_maapi_base_gen import AaaMaapiBase




class BlinkyAaaMaapi(AaaMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-aaa")
        self.domain = None

        

        
        self.a1int64Requested = False
        self.a1int64 = None
        self.a1int64Set = False
        
        self.a8strRequested = False
        self.a8str = None
        self.a8strSet = False
        
        self.a5strRequested = False
        self.a5str = None
        self.a5strSet = False
        
        self.a3strRequested = False
        self.a3str = None
        self.a3strSet = False
        
        self.a6strRequested = False
        self.a6str = None
        self.a6strSet = False
        
        self.a2strRequested = False
        self.a2str = None
        self.a2strSet = False
        
        self.a4strRequested = False
        self.a4str = None
        self.a4strSet = False
        
        self.a7strRequested = False
        self.a7str = None
        self.a7strSet = False
        
        self.a9strRequested = False
        self.a9str = None
        self.a9strSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestA1int64(True)
        
        self.requestA8str(True)
        
        self.requestA5str(True)
        
        self.requestA3str(True)
        
        self.requestA6str(True)
        
        self.requestA2str(True)
        
        self.requestA4str(True)
        
        self.requestA7str(True)
        
        self.requestA9str(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestA1int64(True)
        
        self.requestA8str(True)
        
        self.requestA5str(True)
        
        self.requestA3str(True)
        
        self.requestA6str(True)
        
        self.requestA2str(True)
        
        self.requestA4str(True)
        
        self.requestA7str(True)
        
        self.requestA9str(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestA1int64(False)
        
        self.requestA8str(False)
        
        self.requestA5str(False)
        
        self.requestA3str(False)
        
        self.requestA6str(False)
        
        self.requestA2str(False)
        
        self.requestA4str(False)
        
        self.requestA7str(False)
        
        self.requestA9str(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestA1int64(False)
        
        self.requestA8str(False)
        
        self.requestA5str(False)
        
        self.requestA3str(False)
        
        self.requestA6str(False)
        
        self.requestA2str(False)
        
        self.requestA4str(False)
        
        self.requestA7str(False)
        
        self.requestA9str(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setA1int64(None)
        self.a1int64Set = False
        
        self.setA8str(None)
        self.a8strSet = False
        
        self.setA5str(None)
        self.a5strSet = False
        
        self.setA3str(None)
        self.a3strSet = False
        
        self.setA6str(None)
        self.a6strSet = False
        
        self.setA2str(None)
        self.a2strSet = False
        
        self.setA4str(None)
        self.a4strSet = False
        
        self.setA7str(None)
        self.a7strSet = False
        
        self.setA9str(None)
        self.a9strSet = False
        
        

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



    def requestA1int64 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a1int64').debug3Func(): logFunc('called. requested=%s', requested)
        self.a1int64Requested = requested
        self.a1int64Set = False

    def isA1int64Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a1int64-requested').debug3Func(): logFunc('called. requested=%s', self.a1int64Requested)
        return self.a1int64Requested

    def getA1int64 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a1int64').debug3Func(): logFunc('called. self.a1int64Set=%s, self.a1int64=%s', self.a1int64Set, self.a1int64)
        if self.a1int64Set:
            return self.a1int64
        return None

    def hasA1int64 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a1int64').debug3Func(): logFunc('called. self.a1int64Set=%s, self.a1int64=%s', self.a1int64Set, self.a1int64)
        if self.a1int64Set:
            return True
        return False

    def setA1int64 (self, a1int64):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a1int64').debug3Func(): logFunc('called. a1int64=%s, old=%s', a1int64, self.a1int64)
        self.a1int64Set = True
        self.a1int64 = a1int64

    def requestA8str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a8str').debug3Func(): logFunc('called. requested=%s', requested)
        self.a8strRequested = requested
        self.a8strSet = False

    def isA8strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a8str-requested').debug3Func(): logFunc('called. requested=%s', self.a8strRequested)
        return self.a8strRequested

    def getA8str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a8str').debug3Func(): logFunc('called. self.a8strSet=%s, self.a8str=%s', self.a8strSet, self.a8str)
        if self.a8strSet:
            return self.a8str
        return None

    def hasA8str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a8str').debug3Func(): logFunc('called. self.a8strSet=%s, self.a8str=%s', self.a8strSet, self.a8str)
        if self.a8strSet:
            return True
        return False

    def setA8str (self, a8str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a8str').debug3Func(): logFunc('called. a8str=%s, old=%s', a8str, self.a8str)
        self.a8strSet = True
        self.a8str = a8str

    def requestA5str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a5str').debug3Func(): logFunc('called. requested=%s', requested)
        self.a5strRequested = requested
        self.a5strSet = False

    def isA5strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a5str-requested').debug3Func(): logFunc('called. requested=%s', self.a5strRequested)
        return self.a5strRequested

    def getA5str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a5str').debug3Func(): logFunc('called. self.a5strSet=%s, self.a5str=%s', self.a5strSet, self.a5str)
        if self.a5strSet:
            return self.a5str
        return None

    def hasA5str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a5str').debug3Func(): logFunc('called. self.a5strSet=%s, self.a5str=%s', self.a5strSet, self.a5str)
        if self.a5strSet:
            return True
        return False

    def setA5str (self, a5str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a5str').debug3Func(): logFunc('called. a5str=%s, old=%s', a5str, self.a5str)
        self.a5strSet = True
        self.a5str = a5str

    def requestA3str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a3str').debug3Func(): logFunc('called. requested=%s', requested)
        self.a3strRequested = requested
        self.a3strSet = False

    def isA3strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a3str-requested').debug3Func(): logFunc('called. requested=%s', self.a3strRequested)
        return self.a3strRequested

    def getA3str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a3str').debug3Func(): logFunc('called. self.a3strSet=%s, self.a3str=%s', self.a3strSet, self.a3str)
        if self.a3strSet:
            return self.a3str
        return None

    def hasA3str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a3str').debug3Func(): logFunc('called. self.a3strSet=%s, self.a3str=%s', self.a3strSet, self.a3str)
        if self.a3strSet:
            return True
        return False

    def setA3str (self, a3str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a3str').debug3Func(): logFunc('called. a3str=%s, old=%s', a3str, self.a3str)
        self.a3strSet = True
        self.a3str = a3str

    def requestA6str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a6str').debug3Func(): logFunc('called. requested=%s', requested)
        self.a6strRequested = requested
        self.a6strSet = False

    def isA6strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a6str-requested').debug3Func(): logFunc('called. requested=%s', self.a6strRequested)
        return self.a6strRequested

    def getA6str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a6str').debug3Func(): logFunc('called. self.a6strSet=%s, self.a6str=%s', self.a6strSet, self.a6str)
        if self.a6strSet:
            return self.a6str
        return None

    def hasA6str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a6str').debug3Func(): logFunc('called. self.a6strSet=%s, self.a6str=%s', self.a6strSet, self.a6str)
        if self.a6strSet:
            return True
        return False

    def setA6str (self, a6str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a6str').debug3Func(): logFunc('called. a6str=%s, old=%s', a6str, self.a6str)
        self.a6strSet = True
        self.a6str = a6str

    def requestA2str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a2str').debug3Func(): logFunc('called. requested=%s', requested)
        self.a2strRequested = requested
        self.a2strSet = False

    def isA2strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a2str-requested').debug3Func(): logFunc('called. requested=%s', self.a2strRequested)
        return self.a2strRequested

    def getA2str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a2str').debug3Func(): logFunc('called. self.a2strSet=%s, self.a2str=%s', self.a2strSet, self.a2str)
        if self.a2strSet:
            return self.a2str
        return None

    def hasA2str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a2str').debug3Func(): logFunc('called. self.a2strSet=%s, self.a2str=%s', self.a2strSet, self.a2str)
        if self.a2strSet:
            return True
        return False

    def setA2str (self, a2str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a2str').debug3Func(): logFunc('called. a2str=%s, old=%s', a2str, self.a2str)
        self.a2strSet = True
        self.a2str = a2str

    def requestA4str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a4str').debug3Func(): logFunc('called. requested=%s', requested)
        self.a4strRequested = requested
        self.a4strSet = False

    def isA4strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a4str-requested').debug3Func(): logFunc('called. requested=%s', self.a4strRequested)
        return self.a4strRequested

    def getA4str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a4str').debug3Func(): logFunc('called. self.a4strSet=%s, self.a4str=%s', self.a4strSet, self.a4str)
        if self.a4strSet:
            return self.a4str
        return None

    def hasA4str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a4str').debug3Func(): logFunc('called. self.a4strSet=%s, self.a4str=%s', self.a4strSet, self.a4str)
        if self.a4strSet:
            return True
        return False

    def setA4str (self, a4str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a4str').debug3Func(): logFunc('called. a4str=%s, old=%s', a4str, self.a4str)
        self.a4strSet = True
        self.a4str = a4str

    def requestA7str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a7str').debug3Func(): logFunc('called. requested=%s', requested)
        self.a7strRequested = requested
        self.a7strSet = False

    def isA7strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a7str-requested').debug3Func(): logFunc('called. requested=%s', self.a7strRequested)
        return self.a7strRequested

    def getA7str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a7str').debug3Func(): logFunc('called. self.a7strSet=%s, self.a7str=%s', self.a7strSet, self.a7str)
        if self.a7strSet:
            return self.a7str
        return None

    def hasA7str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a7str').debug3Func(): logFunc('called. self.a7strSet=%s, self.a7str=%s', self.a7strSet, self.a7str)
        if self.a7strSet:
            return True
        return False

    def setA7str (self, a7str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a7str').debug3Func(): logFunc('called. a7str=%s, old=%s', a7str, self.a7str)
        self.a7strSet = True
        self.a7str = a7str

    def requestA9str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-a9str').debug3Func(): logFunc('called. requested=%s', requested)
        self.a9strRequested = requested
        self.a9strSet = False

    def isA9strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-a9str-requested').debug3Func(): logFunc('called. requested=%s', self.a9strRequested)
        return self.a9strRequested

    def getA9str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-a9str').debug3Func(): logFunc('called. self.a9strSet=%s, self.a9str=%s', self.a9strSet, self.a9str)
        if self.a9strSet:
            return self.a9str
        return None

    def hasA9str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-a9str').debug3Func(): logFunc('called. self.a9strSet=%s, self.a9str=%s', self.a9strSet, self.a9str)
        if self.a9strSet:
            return True
        return False

    def setA9str (self, a9str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-a9str').debug3Func(): logFunc('called. a9str=%s, old=%s', a9str, self.a9str)
        self.a9strSet = True
        self.a9str = a9str


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.a1int64 = 0
        self.a1int64Set = False
        
        self.a8str = 0
        self.a8strSet = False
        
        self.a5str = 0
        self.a5strSet = False
        
        self.a3str = 0
        self.a3strSet = False
        
        self.a6str = 0
        self.a6strSet = False
        
        self.a2str = 0
        self.a2strSet = False
        
        self.a4str = 0
        self.a4strSet = False
        
        self.a7str = 0
        self.a7strSet = False
        
        self.a9str = 0
        self.a9strSet = False
        

    def _getSelfKeyPath (self, lll
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("aaa", "http://qwilt.com/model/benchmark", "bnch"))
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

        
        if self.hasA1int64():
            valA1int64 = Value()
            if self.a1int64 is not None:
                valA1int64.setInt64(self.a1int64)
            else:
                valA1int64.setEmpty()
            tagValueList.push(("a1int64", "http://qwilt.com/model/benchmark"), valA1int64)
        
        if self.hasA8str():
            valA8str = Value()
            if self.a8str is not None:
                valA8str.setString(self.a8str)
            else:
                valA8str.setEmpty()
            tagValueList.push(("a8str", "http://qwilt.com/model/benchmark"), valA8str)
        
        if self.hasA5str():
            valA5str = Value()
            if self.a5str is not None:
                valA5str.setString(self.a5str)
            else:
                valA5str.setEmpty()
            tagValueList.push(("a5str", "http://qwilt.com/model/benchmark"), valA5str)
        
        if self.hasA3str():
            valA3str = Value()
            if self.a3str is not None:
                valA3str.setString(self.a3str)
            else:
                valA3str.setEmpty()
            tagValueList.push(("a3str", "http://qwilt.com/model/benchmark"), valA3str)
        
        if self.hasA6str():
            valA6str = Value()
            if self.a6str is not None:
                valA6str.setString(self.a6str)
            else:
                valA6str.setEmpty()
            tagValueList.push(("a6str", "http://qwilt.com/model/benchmark"), valA6str)
        
        if self.hasA2str():
            valA2str = Value()
            if self.a2str is not None:
                valA2str.setString(self.a2str)
            else:
                valA2str.setEmpty()
            tagValueList.push(("a2str", "http://qwilt.com/model/benchmark"), valA2str)
        
        if self.hasA4str():
            valA4str = Value()
            if self.a4str is not None:
                valA4str.setString(self.a4str)
            else:
                valA4str.setEmpty()
            tagValueList.push(("a4str", "http://qwilt.com/model/benchmark"), valA4str)
        
        if self.hasA7str():
            valA7str = Value()
            if self.a7str is not None:
                valA7str.setString(self.a7str)
            else:
                valA7str.setEmpty()
            tagValueList.push(("a7str", "http://qwilt.com/model/benchmark"), valA7str)
        
        if self.hasA9str():
            valA9str = Value()
            if self.a9str is not None:
                valA9str.setString(self.a9str)
            else:
                valA9str.setEmpty()
            tagValueList.push(("a9str", "http://qwilt.com/model/benchmark"), valA9str)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isA1int64Requested():
            valA1int64 = Value()
            valA1int64.setEmpty()
            tagValueList.push(("a1int64", "http://qwilt.com/model/benchmark"), valA1int64)
        
        if self.isA8strRequested():
            valA8str = Value()
            valA8str.setEmpty()
            tagValueList.push(("a8str", "http://qwilt.com/model/benchmark"), valA8str)
        
        if self.isA5strRequested():
            valA5str = Value()
            valA5str.setEmpty()
            tagValueList.push(("a5str", "http://qwilt.com/model/benchmark"), valA5str)
        
        if self.isA3strRequested():
            valA3str = Value()
            valA3str.setEmpty()
            tagValueList.push(("a3str", "http://qwilt.com/model/benchmark"), valA3str)
        
        if self.isA6strRequested():
            valA6str = Value()
            valA6str.setEmpty()
            tagValueList.push(("a6str", "http://qwilt.com/model/benchmark"), valA6str)
        
        if self.isA2strRequested():
            valA2str = Value()
            valA2str.setEmpty()
            tagValueList.push(("a2str", "http://qwilt.com/model/benchmark"), valA2str)
        
        if self.isA4strRequested():
            valA4str = Value()
            valA4str.setEmpty()
            tagValueList.push(("a4str", "http://qwilt.com/model/benchmark"), valA4str)
        
        if self.isA7strRequested():
            valA7str = Value()
            valA7str.setEmpty()
            tagValueList.push(("a7str", "http://qwilt.com/model/benchmark"), valA7str)
        
        if self.isA9strRequested():
            valA9str = Value()
            valA9str.setEmpty()
            tagValueList.push(("a9str", "http://qwilt.com/model/benchmark"), valA9str)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isA1int64Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a1int64") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a1int64').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a1int64", "a1int64", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a1int64-bad-value').infoFunc(): logFunc('a1int64 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA1int64(tempVar)
            for logFunc in self._log('read-tag-values-a1int64').debug3Func(): logFunc('read a1int64. a1int64=%s, tempValue=%s', self.a1int64, tempValue.getType())
        
        if self.isA8strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a8str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a8str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a8str", "a8str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a8str-bad-value').infoFunc(): logFunc('a8str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA8str(tempVar)
            for logFunc in self._log('read-tag-values-a8str').debug3Func(): logFunc('read a8str. a8str=%s, tempValue=%s', self.a8str, tempValue.getType())
        
        if self.isA5strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a5str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a5str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a5str", "a5str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a5str-bad-value').infoFunc(): logFunc('a5str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA5str(tempVar)
            for logFunc in self._log('read-tag-values-a5str').debug3Func(): logFunc('read a5str. a5str=%s, tempValue=%s', self.a5str, tempValue.getType())
        
        if self.isA3strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a3str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a3str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a3str", "a3str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a3str-bad-value').infoFunc(): logFunc('a3str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA3str(tempVar)
            for logFunc in self._log('read-tag-values-a3str').debug3Func(): logFunc('read a3str. a3str=%s, tempValue=%s', self.a3str, tempValue.getType())
        
        if self.isA6strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a6str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a6str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a6str", "a6str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a6str-bad-value').infoFunc(): logFunc('a6str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA6str(tempVar)
            for logFunc in self._log('read-tag-values-a6str').debug3Func(): logFunc('read a6str. a6str=%s, tempValue=%s', self.a6str, tempValue.getType())
        
        if self.isA2strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a2str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a2str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a2str", "a2str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a2str-bad-value').infoFunc(): logFunc('a2str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA2str(tempVar)
            for logFunc in self._log('read-tag-values-a2str').debug3Func(): logFunc('read a2str. a2str=%s, tempValue=%s', self.a2str, tempValue.getType())
        
        if self.isA4strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a4str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a4str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a4str", "a4str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a4str-bad-value').infoFunc(): logFunc('a4str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA4str(tempVar)
            for logFunc in self._log('read-tag-values-a4str').debug3Func(): logFunc('read a4str. a4str=%s, tempValue=%s', self.a4str, tempValue.getType())
        
        if self.isA7strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a7str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a7str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a7str", "a7str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a7str-bad-value').infoFunc(): logFunc('a7str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA7str(tempVar)
            for logFunc in self._log('read-tag-values-a7str').debug3Func(): logFunc('read a7str. a7str=%s, tempValue=%s', self.a7str, tempValue.getType())
        
        if self.isA9strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "a9str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-a9str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "a9str", "a9str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-a9str-bad-value').infoFunc(): logFunc('a9str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setA9str(tempVar)
            for logFunc in self._log('read-tag-values-a9str').debug3Func(): logFunc('read a9str. a9str=%s, tempValue=%s', self.a9str, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "aaa", 
        "namespace": "aaa", 
        "className": "AaaMaapi", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.aaa.aaa_maapi_gen import AaaMaapi", 
        "baseClassName": "AaaMaapiBase", 
        "baseModule": "aaa_maapi_base_gen"
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
            "yangName": "aaa", 
            "namespace": "aaa", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "aaa"
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
            "memberName": "a1int64", 
            "yangName": "a1int64", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a8str", 
            "yangName": "a8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a5str", 
            "yangName": "a5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a3str", 
            "yangName": "a3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a6str", 
            "yangName": "a6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a2str", 
            "yangName": "a2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a4str", 
            "yangName": "a4str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a7str", 
            "yangName": "a7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a9str", 
            "yangName": "a9str", 
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
            "memberName": "a1int64", 
            "yangName": "a1int64", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a8str", 
            "yangName": "a8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a5str", 
            "yangName": "a5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a3str", 
            "yangName": "a3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a6str", 
            "yangName": "a6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a2str", 
            "yangName": "a2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a4str", 
            "yangName": "a4str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a7str", 
            "yangName": "a7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "a9str", 
            "yangName": "a9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


