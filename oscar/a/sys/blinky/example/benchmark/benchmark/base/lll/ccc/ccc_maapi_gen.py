


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

from ccc_maapi_base_gen import CccMaapiBase




class BlinkyCccMaapi(CccMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-ccc")
        self.domain = None

        

        
        self.c9strRequested = False
        self.c9str = None
        self.c9strSet = False
        
        self.c2strRequested = False
        self.c2str = None
        self.c2strSet = False
        
        self.c8strRequested = False
        self.c8str = None
        self.c8strSet = False
        
        self.c6strRequested = False
        self.c6str = None
        self.c6strSet = False
        
        self.c5strRequested = False
        self.c5str = None
        self.c5strSet = False
        
        self.c1strRequested = False
        self.c1str = None
        self.c1strSet = False
        
        self.c7strRequested = False
        self.c7str = None
        self.c7strSet = False
        
        self.c10strRequested = False
        self.c10str = None
        self.c10strSet = False
        
        self.c3strRequested = False
        self.c3str = None
        self.c3strSet = False
        
        self.c4strRequested = False
        self.c4str = None
        self.c4strSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestC9str(True)
        
        self.requestC2str(True)
        
        self.requestC8str(True)
        
        self.requestC6str(True)
        
        self.requestC5str(True)
        
        self.requestC1str(True)
        
        self.requestC7str(True)
        
        self.requestC10str(True)
        
        self.requestC3str(True)
        
        self.requestC4str(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestC9str(True)
        
        self.requestC2str(True)
        
        self.requestC8str(True)
        
        self.requestC6str(True)
        
        self.requestC5str(True)
        
        self.requestC1str(True)
        
        self.requestC7str(True)
        
        self.requestC10str(True)
        
        self.requestC3str(True)
        
        self.requestC4str(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestC9str(False)
        
        self.requestC2str(False)
        
        self.requestC8str(False)
        
        self.requestC6str(False)
        
        self.requestC5str(False)
        
        self.requestC1str(False)
        
        self.requestC7str(False)
        
        self.requestC10str(False)
        
        self.requestC3str(False)
        
        self.requestC4str(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestC9str(False)
        
        self.requestC2str(False)
        
        self.requestC8str(False)
        
        self.requestC6str(False)
        
        self.requestC5str(False)
        
        self.requestC1str(False)
        
        self.requestC7str(False)
        
        self.requestC10str(False)
        
        self.requestC3str(False)
        
        self.requestC4str(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setC9str(None)
        self.c9strSet = False
        
        self.setC2str(None)
        self.c2strSet = False
        
        self.setC8str(None)
        self.c8strSet = False
        
        self.setC6str(None)
        self.c6strSet = False
        
        self.setC5str(None)
        self.c5strSet = False
        
        self.setC1str(None)
        self.c1strSet = False
        
        self.setC7str(None)
        self.c7strSet = False
        
        self.setC10str(None)
        self.c10strSet = False
        
        self.setC3str(None)
        self.c3strSet = False
        
        self.setC4str(None)
        self.c4strSet = False
        
        

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



    def requestC9str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c9str').debug3Func(): logFunc('called. requested=%s', requested)
        self.c9strRequested = requested
        self.c9strSet = False

    def isC9strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c9str-requested').debug3Func(): logFunc('called. requested=%s', self.c9strRequested)
        return self.c9strRequested

    def getC9str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c9str').debug3Func(): logFunc('called. self.c9strSet=%s, self.c9str=%s', self.c9strSet, self.c9str)
        if self.c9strSet:
            return self.c9str
        return None

    def hasC9str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c9str').debug3Func(): logFunc('called. self.c9strSet=%s, self.c9str=%s', self.c9strSet, self.c9str)
        if self.c9strSet:
            return True
        return False

    def setC9str (self, c9str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c9str').debug3Func(): logFunc('called. c9str=%s, old=%s', c9str, self.c9str)
        self.c9strSet = True
        self.c9str = c9str

    def requestC2str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c2str').debug3Func(): logFunc('called. requested=%s', requested)
        self.c2strRequested = requested
        self.c2strSet = False

    def isC2strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c2str-requested').debug3Func(): logFunc('called. requested=%s', self.c2strRequested)
        return self.c2strRequested

    def getC2str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c2str').debug3Func(): logFunc('called. self.c2strSet=%s, self.c2str=%s', self.c2strSet, self.c2str)
        if self.c2strSet:
            return self.c2str
        return None

    def hasC2str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c2str').debug3Func(): logFunc('called. self.c2strSet=%s, self.c2str=%s', self.c2strSet, self.c2str)
        if self.c2strSet:
            return True
        return False

    def setC2str (self, c2str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c2str').debug3Func(): logFunc('called. c2str=%s, old=%s', c2str, self.c2str)
        self.c2strSet = True
        self.c2str = c2str

    def requestC8str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c8str').debug3Func(): logFunc('called. requested=%s', requested)
        self.c8strRequested = requested
        self.c8strSet = False

    def isC8strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c8str-requested').debug3Func(): logFunc('called. requested=%s', self.c8strRequested)
        return self.c8strRequested

    def getC8str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c8str').debug3Func(): logFunc('called. self.c8strSet=%s, self.c8str=%s', self.c8strSet, self.c8str)
        if self.c8strSet:
            return self.c8str
        return None

    def hasC8str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c8str').debug3Func(): logFunc('called. self.c8strSet=%s, self.c8str=%s', self.c8strSet, self.c8str)
        if self.c8strSet:
            return True
        return False

    def setC8str (self, c8str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c8str').debug3Func(): logFunc('called. c8str=%s, old=%s', c8str, self.c8str)
        self.c8strSet = True
        self.c8str = c8str

    def requestC6str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c6str').debug3Func(): logFunc('called. requested=%s', requested)
        self.c6strRequested = requested
        self.c6strSet = False

    def isC6strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c6str-requested').debug3Func(): logFunc('called. requested=%s', self.c6strRequested)
        return self.c6strRequested

    def getC6str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c6str').debug3Func(): logFunc('called. self.c6strSet=%s, self.c6str=%s', self.c6strSet, self.c6str)
        if self.c6strSet:
            return self.c6str
        return None

    def hasC6str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c6str').debug3Func(): logFunc('called. self.c6strSet=%s, self.c6str=%s', self.c6strSet, self.c6str)
        if self.c6strSet:
            return True
        return False

    def setC6str (self, c6str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c6str').debug3Func(): logFunc('called. c6str=%s, old=%s', c6str, self.c6str)
        self.c6strSet = True
        self.c6str = c6str

    def requestC5str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c5str').debug3Func(): logFunc('called. requested=%s', requested)
        self.c5strRequested = requested
        self.c5strSet = False

    def isC5strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c5str-requested').debug3Func(): logFunc('called. requested=%s', self.c5strRequested)
        return self.c5strRequested

    def getC5str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c5str').debug3Func(): logFunc('called. self.c5strSet=%s, self.c5str=%s', self.c5strSet, self.c5str)
        if self.c5strSet:
            return self.c5str
        return None

    def hasC5str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c5str').debug3Func(): logFunc('called. self.c5strSet=%s, self.c5str=%s', self.c5strSet, self.c5str)
        if self.c5strSet:
            return True
        return False

    def setC5str (self, c5str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c5str').debug3Func(): logFunc('called. c5str=%s, old=%s', c5str, self.c5str)
        self.c5strSet = True
        self.c5str = c5str

    def requestC1str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c1str').debug3Func(): logFunc('called. requested=%s', requested)
        self.c1strRequested = requested
        self.c1strSet = False

    def isC1strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c1str-requested').debug3Func(): logFunc('called. requested=%s', self.c1strRequested)
        return self.c1strRequested

    def getC1str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c1str').debug3Func(): logFunc('called. self.c1strSet=%s, self.c1str=%s', self.c1strSet, self.c1str)
        if self.c1strSet:
            return self.c1str
        return None

    def hasC1str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c1str').debug3Func(): logFunc('called. self.c1strSet=%s, self.c1str=%s', self.c1strSet, self.c1str)
        if self.c1strSet:
            return True
        return False

    def setC1str (self, c1str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c1str').debug3Func(): logFunc('called. c1str=%s, old=%s', c1str, self.c1str)
        self.c1strSet = True
        self.c1str = c1str

    def requestC7str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c7str').debug3Func(): logFunc('called. requested=%s', requested)
        self.c7strRequested = requested
        self.c7strSet = False

    def isC7strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c7str-requested').debug3Func(): logFunc('called. requested=%s', self.c7strRequested)
        return self.c7strRequested

    def getC7str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c7str').debug3Func(): logFunc('called. self.c7strSet=%s, self.c7str=%s', self.c7strSet, self.c7str)
        if self.c7strSet:
            return self.c7str
        return None

    def hasC7str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c7str').debug3Func(): logFunc('called. self.c7strSet=%s, self.c7str=%s', self.c7strSet, self.c7str)
        if self.c7strSet:
            return True
        return False

    def setC7str (self, c7str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c7str').debug3Func(): logFunc('called. c7str=%s, old=%s', c7str, self.c7str)
        self.c7strSet = True
        self.c7str = c7str

    def requestC10str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c10str').debug3Func(): logFunc('called. requested=%s', requested)
        self.c10strRequested = requested
        self.c10strSet = False

    def isC10strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c10str-requested').debug3Func(): logFunc('called. requested=%s', self.c10strRequested)
        return self.c10strRequested

    def getC10str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c10str').debug3Func(): logFunc('called. self.c10strSet=%s, self.c10str=%s', self.c10strSet, self.c10str)
        if self.c10strSet:
            return self.c10str
        return None

    def hasC10str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c10str').debug3Func(): logFunc('called. self.c10strSet=%s, self.c10str=%s', self.c10strSet, self.c10str)
        if self.c10strSet:
            return True
        return False

    def setC10str (self, c10str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c10str').debug3Func(): logFunc('called. c10str=%s, old=%s', c10str, self.c10str)
        self.c10strSet = True
        self.c10str = c10str

    def requestC3str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c3str').debug3Func(): logFunc('called. requested=%s', requested)
        self.c3strRequested = requested
        self.c3strSet = False

    def isC3strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c3str-requested').debug3Func(): logFunc('called. requested=%s', self.c3strRequested)
        return self.c3strRequested

    def getC3str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c3str').debug3Func(): logFunc('called. self.c3strSet=%s, self.c3str=%s', self.c3strSet, self.c3str)
        if self.c3strSet:
            return self.c3str
        return None

    def hasC3str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c3str').debug3Func(): logFunc('called. self.c3strSet=%s, self.c3str=%s', self.c3strSet, self.c3str)
        if self.c3strSet:
            return True
        return False

    def setC3str (self, c3str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c3str').debug3Func(): logFunc('called. c3str=%s, old=%s', c3str, self.c3str)
        self.c3strSet = True
        self.c3str = c3str

    def requestC4str (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-c4str').debug3Func(): logFunc('called. requested=%s', requested)
        self.c4strRequested = requested
        self.c4strSet = False

    def isC4strRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-c4str-requested').debug3Func(): logFunc('called. requested=%s', self.c4strRequested)
        return self.c4strRequested

    def getC4str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-c4str').debug3Func(): logFunc('called. self.c4strSet=%s, self.c4str=%s', self.c4strSet, self.c4str)
        if self.c4strSet:
            return self.c4str
        return None

    def hasC4str (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-c4str').debug3Func(): logFunc('called. self.c4strSet=%s, self.c4str=%s', self.c4strSet, self.c4str)
        if self.c4strSet:
            return True
        return False

    def setC4str (self, c4str):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-c4str').debug3Func(): logFunc('called. c4str=%s, old=%s', c4str, self.c4str)
        self.c4strSet = True
        self.c4str = c4str


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.c9str = 0
        self.c9strSet = False
        
        self.c2str = 0
        self.c2strSet = False
        
        self.c8str = 0
        self.c8strSet = False
        
        self.c6str = 0
        self.c6strSet = False
        
        self.c5str = 0
        self.c5strSet = False
        
        self.c1str = 0
        self.c1strSet = False
        
        self.c7str = 0
        self.c7strSet = False
        
        self.c10str = 0
        self.c10strSet = False
        
        self.c3str = 0
        self.c3strSet = False
        
        self.c4str = 0
        self.c4strSet = False
        

    def _getSelfKeyPath (self, lll
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ccc", "http://qwilt.com/model/benchmark", "bnch"))
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

        
        if self.hasC9str():
            valC9str = Value()
            if self.c9str is not None:
                valC9str.setString(self.c9str)
            else:
                valC9str.setEmpty()
            tagValueList.push(("c9str", "http://qwilt.com/model/benchmark"), valC9str)
        
        if self.hasC2str():
            valC2str = Value()
            if self.c2str is not None:
                valC2str.setString(self.c2str)
            else:
                valC2str.setEmpty()
            tagValueList.push(("c2str", "http://qwilt.com/model/benchmark"), valC2str)
        
        if self.hasC8str():
            valC8str = Value()
            if self.c8str is not None:
                valC8str.setString(self.c8str)
            else:
                valC8str.setEmpty()
            tagValueList.push(("c8str", "http://qwilt.com/model/benchmark"), valC8str)
        
        if self.hasC6str():
            valC6str = Value()
            if self.c6str is not None:
                valC6str.setString(self.c6str)
            else:
                valC6str.setEmpty()
            tagValueList.push(("c6str", "http://qwilt.com/model/benchmark"), valC6str)
        
        if self.hasC5str():
            valC5str = Value()
            if self.c5str is not None:
                valC5str.setString(self.c5str)
            else:
                valC5str.setEmpty()
            tagValueList.push(("c5str", "http://qwilt.com/model/benchmark"), valC5str)
        
        if self.hasC1str():
            valC1str = Value()
            if self.c1str is not None:
                valC1str.setString(self.c1str)
            else:
                valC1str.setEmpty()
            tagValueList.push(("c1str", "http://qwilt.com/model/benchmark"), valC1str)
        
        if self.hasC7str():
            valC7str = Value()
            if self.c7str is not None:
                valC7str.setString(self.c7str)
            else:
                valC7str.setEmpty()
            tagValueList.push(("c7str", "http://qwilt.com/model/benchmark"), valC7str)
        
        if self.hasC10str():
            valC10str = Value()
            if self.c10str is not None:
                valC10str.setString(self.c10str)
            else:
                valC10str.setEmpty()
            tagValueList.push(("c10str", "http://qwilt.com/model/benchmark"), valC10str)
        
        if self.hasC3str():
            valC3str = Value()
            if self.c3str is not None:
                valC3str.setString(self.c3str)
            else:
                valC3str.setEmpty()
            tagValueList.push(("c3str", "http://qwilt.com/model/benchmark"), valC3str)
        
        if self.hasC4str():
            valC4str = Value()
            if self.c4str is not None:
                valC4str.setString(self.c4str)
            else:
                valC4str.setEmpty()
            tagValueList.push(("c4str", "http://qwilt.com/model/benchmark"), valC4str)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isC9strRequested():
            valC9str = Value()
            valC9str.setEmpty()
            tagValueList.push(("c9str", "http://qwilt.com/model/benchmark"), valC9str)
        
        if self.isC2strRequested():
            valC2str = Value()
            valC2str.setEmpty()
            tagValueList.push(("c2str", "http://qwilt.com/model/benchmark"), valC2str)
        
        if self.isC8strRequested():
            valC8str = Value()
            valC8str.setEmpty()
            tagValueList.push(("c8str", "http://qwilt.com/model/benchmark"), valC8str)
        
        if self.isC6strRequested():
            valC6str = Value()
            valC6str.setEmpty()
            tagValueList.push(("c6str", "http://qwilt.com/model/benchmark"), valC6str)
        
        if self.isC5strRequested():
            valC5str = Value()
            valC5str.setEmpty()
            tagValueList.push(("c5str", "http://qwilt.com/model/benchmark"), valC5str)
        
        if self.isC1strRequested():
            valC1str = Value()
            valC1str.setEmpty()
            tagValueList.push(("c1str", "http://qwilt.com/model/benchmark"), valC1str)
        
        if self.isC7strRequested():
            valC7str = Value()
            valC7str.setEmpty()
            tagValueList.push(("c7str", "http://qwilt.com/model/benchmark"), valC7str)
        
        if self.isC10strRequested():
            valC10str = Value()
            valC10str.setEmpty()
            tagValueList.push(("c10str", "http://qwilt.com/model/benchmark"), valC10str)
        
        if self.isC3strRequested():
            valC3str = Value()
            valC3str.setEmpty()
            tagValueList.push(("c3str", "http://qwilt.com/model/benchmark"), valC3str)
        
        if self.isC4strRequested():
            valC4str = Value()
            valC4str.setEmpty()
            tagValueList.push(("c4str", "http://qwilt.com/model/benchmark"), valC4str)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isC9strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c9str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c9str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c9str", "c9str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c9str-bad-value').infoFunc(): logFunc('c9str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC9str(tempVar)
            for logFunc in self._log('read-tag-values-c9str').debug3Func(): logFunc('read c9str. c9str=%s, tempValue=%s', self.c9str, tempValue.getType())
        
        if self.isC2strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c2str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c2str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c2str", "c2str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c2str-bad-value').infoFunc(): logFunc('c2str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC2str(tempVar)
            for logFunc in self._log('read-tag-values-c2str').debug3Func(): logFunc('read c2str. c2str=%s, tempValue=%s', self.c2str, tempValue.getType())
        
        if self.isC8strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c8str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c8str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c8str", "c8str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c8str-bad-value').infoFunc(): logFunc('c8str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC8str(tempVar)
            for logFunc in self._log('read-tag-values-c8str').debug3Func(): logFunc('read c8str. c8str=%s, tempValue=%s', self.c8str, tempValue.getType())
        
        if self.isC6strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c6str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c6str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c6str", "c6str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c6str-bad-value').infoFunc(): logFunc('c6str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC6str(tempVar)
            for logFunc in self._log('read-tag-values-c6str').debug3Func(): logFunc('read c6str. c6str=%s, tempValue=%s', self.c6str, tempValue.getType())
        
        if self.isC5strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c5str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c5str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c5str", "c5str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c5str-bad-value').infoFunc(): logFunc('c5str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC5str(tempVar)
            for logFunc in self._log('read-tag-values-c5str').debug3Func(): logFunc('read c5str. c5str=%s, tempValue=%s', self.c5str, tempValue.getType())
        
        if self.isC1strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c1str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c1str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c1str", "c1str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c1str-bad-value').infoFunc(): logFunc('c1str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC1str(tempVar)
            for logFunc in self._log('read-tag-values-c1str').debug3Func(): logFunc('read c1str. c1str=%s, tempValue=%s', self.c1str, tempValue.getType())
        
        if self.isC7strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c7str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c7str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c7str", "c7str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c7str-bad-value').infoFunc(): logFunc('c7str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC7str(tempVar)
            for logFunc in self._log('read-tag-values-c7str').debug3Func(): logFunc('read c7str. c7str=%s, tempValue=%s', self.c7str, tempValue.getType())
        
        if self.isC10strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c10str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c10str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c10str", "c10str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c10str-bad-value').infoFunc(): logFunc('c10str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC10str(tempVar)
            for logFunc in self._log('read-tag-values-c10str').debug3Func(): logFunc('read c10str. c10str=%s, tempValue=%s', self.c10str, tempValue.getType())
        
        if self.isC3strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c3str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c3str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c3str", "c3str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c3str-bad-value').infoFunc(): logFunc('c3str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC3str(tempVar)
            for logFunc in self._log('read-tag-values-c3str').debug3Func(): logFunc('read c3str. c3str=%s, tempValue=%s', self.c3str, tempValue.getType())
        
        if self.isC4strRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "c4str") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-c4str').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "c4str", "c4str", "http://qwilt.com/model/benchmark", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-c4str-bad-value').infoFunc(): logFunc('c4str not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setC4str(tempVar)
            for logFunc in self._log('read-tag-values-c4str').debug3Func(): logFunc('read c4str. c4str=%s, tempValue=%s', self.c4str, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "ccc", 
        "namespace": "ccc", 
        "className": "CccMaapi", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.ccc.ccc_maapi_gen import CccMaapi", 
        "baseClassName": "CccMaapiBase", 
        "baseModule": "ccc_maapi_base_gen"
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
            "yangName": "ccc", 
            "namespace": "ccc", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "ccc"
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "c9str", 
            "yangName": "c9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c2str", 
            "yangName": "c2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c8str", 
            "yangName": "c8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c6str", 
            "yangName": "c6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c5str", 
            "yangName": "c5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c1str", 
            "yangName": "c1str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c7str", 
            "yangName": "c7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c10str", 
            "yangName": "c10str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c3str", 
            "yangName": "c3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c4str", 
            "yangName": "c4str", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "c9str", 
            "yangName": "c9str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c2str", 
            "yangName": "c2str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c8str", 
            "yangName": "c8str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c6str", 
            "yangName": "c6str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c5str", 
            "yangName": "c5str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c1str", 
            "yangName": "c1str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c7str", 
            "yangName": "c7str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c10str", 
            "yangName": "c10str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c3str", 
            "yangName": "c3str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "c4str", 
            "yangName": "c4str", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


