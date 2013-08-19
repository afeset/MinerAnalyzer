


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

from thresholds_maapi_base_gen import ThresholdsMaapiBase




class BlinkyThresholdsMaapi(ThresholdsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-thresholds")
        self.domain = None

        

        
        self.pollLatencyErrorRequested = False
        self.pollLatencyError = None
        self.pollLatencyErrorSet = False
        
        self.overallPollDurationWarningRequested = False
        self.overallPollDurationWarning = None
        self.overallPollDurationWarningSet = False
        
        self.pollLatencyWarningRequested = False
        self.pollLatencyWarning = None
        self.pollLatencyWarningSet = False
        
        self.singlePollDurationWarningRequested = False
        self.singlePollDurationWarning = None
        self.singlePollDurationWarningSet = False
        
        self.singlePollDurationErrorRequested = False
        self.singlePollDurationError = None
        self.singlePollDurationErrorSet = False
        
        self.overallPollDurationErrorRequested = False
        self.overallPollDurationError = None
        self.overallPollDurationErrorSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPollLatencyError(True)
        
        self.requestOverallPollDurationWarning(True)
        
        self.requestPollLatencyWarning(True)
        
        self.requestSinglePollDurationWarning(True)
        
        self.requestSinglePollDurationError(True)
        
        self.requestOverallPollDurationError(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPollLatencyError(True)
        
        self.requestOverallPollDurationWarning(True)
        
        self.requestPollLatencyWarning(True)
        
        self.requestSinglePollDurationWarning(True)
        
        self.requestSinglePollDurationError(True)
        
        self.requestOverallPollDurationError(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPollLatencyError(False)
        
        self.requestOverallPollDurationWarning(False)
        
        self.requestPollLatencyWarning(False)
        
        self.requestSinglePollDurationWarning(False)
        
        self.requestSinglePollDurationError(False)
        
        self.requestOverallPollDurationError(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPollLatencyError(False)
        
        self.requestOverallPollDurationWarning(False)
        
        self.requestPollLatencyWarning(False)
        
        self.requestSinglePollDurationWarning(False)
        
        self.requestSinglePollDurationError(False)
        
        self.requestOverallPollDurationError(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setPollLatencyError(None)
        self.pollLatencyErrorSet = False
        
        self.setOverallPollDurationWarning(None)
        self.overallPollDurationWarningSet = False
        
        self.setPollLatencyWarning(None)
        self.pollLatencyWarningSet = False
        
        self.setSinglePollDurationWarning(None)
        self.singlePollDurationWarningSet = False
        
        self.setSinglePollDurationError(None)
        self.singlePollDurationErrorSet = False
        
        self.setOverallPollDurationError(None)
        self.overallPollDurationErrorSet = False
        
        

    def write (self
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(trxContext)

    def read (self
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  True,
                                  trxContext)



    def requestPollLatencyError (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-polllatencyerror').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollLatencyErrorRequested = requested
        self.pollLatencyErrorSet = False

    def isPollLatencyErrorRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-polllatencyerror-requested').debug3Func(): logFunc('called. requested=%s', self.pollLatencyErrorRequested)
        return self.pollLatencyErrorRequested

    def getPollLatencyError (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-polllatencyerror').debug3Func(): logFunc('called. self.pollLatencyErrorSet=%s, self.pollLatencyError=%s', self.pollLatencyErrorSet, self.pollLatencyError)
        if self.pollLatencyErrorSet:
            return self.pollLatencyError
        return None

    def hasPollLatencyError (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-polllatencyerror').debug3Func(): logFunc('called. self.pollLatencyErrorSet=%s, self.pollLatencyError=%s', self.pollLatencyErrorSet, self.pollLatencyError)
        if self.pollLatencyErrorSet:
            return True
        return False

    def setPollLatencyError (self, pollLatencyError):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-polllatencyerror').debug3Func(): logFunc('called. pollLatencyError=%s, old=%s', pollLatencyError, self.pollLatencyError)
        self.pollLatencyErrorSet = True
        self.pollLatencyError = pollLatencyError

    def requestOverallPollDurationWarning (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-overallpolldurationwarning').debug3Func(): logFunc('called. requested=%s', requested)
        self.overallPollDurationWarningRequested = requested
        self.overallPollDurationWarningSet = False

    def isOverallPollDurationWarningRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-overallpolldurationwarning-requested').debug3Func(): logFunc('called. requested=%s', self.overallPollDurationWarningRequested)
        return self.overallPollDurationWarningRequested

    def getOverallPollDurationWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-overallpolldurationwarning').debug3Func(): logFunc('called. self.overallPollDurationWarningSet=%s, self.overallPollDurationWarning=%s', self.overallPollDurationWarningSet, self.overallPollDurationWarning)
        if self.overallPollDurationWarningSet:
            return self.overallPollDurationWarning
        return None

    def hasOverallPollDurationWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-overallpolldurationwarning').debug3Func(): logFunc('called. self.overallPollDurationWarningSet=%s, self.overallPollDurationWarning=%s', self.overallPollDurationWarningSet, self.overallPollDurationWarning)
        if self.overallPollDurationWarningSet:
            return True
        return False

    def setOverallPollDurationWarning (self, overallPollDurationWarning):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-overallpolldurationwarning').debug3Func(): logFunc('called. overallPollDurationWarning=%s, old=%s', overallPollDurationWarning, self.overallPollDurationWarning)
        self.overallPollDurationWarningSet = True
        self.overallPollDurationWarning = overallPollDurationWarning

    def requestPollLatencyWarning (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-polllatencywarning').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollLatencyWarningRequested = requested
        self.pollLatencyWarningSet = False

    def isPollLatencyWarningRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-polllatencywarning-requested').debug3Func(): logFunc('called. requested=%s', self.pollLatencyWarningRequested)
        return self.pollLatencyWarningRequested

    def getPollLatencyWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-polllatencywarning').debug3Func(): logFunc('called. self.pollLatencyWarningSet=%s, self.pollLatencyWarning=%s', self.pollLatencyWarningSet, self.pollLatencyWarning)
        if self.pollLatencyWarningSet:
            return self.pollLatencyWarning
        return None

    def hasPollLatencyWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-polllatencywarning').debug3Func(): logFunc('called. self.pollLatencyWarningSet=%s, self.pollLatencyWarning=%s', self.pollLatencyWarningSet, self.pollLatencyWarning)
        if self.pollLatencyWarningSet:
            return True
        return False

    def setPollLatencyWarning (self, pollLatencyWarning):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-polllatencywarning').debug3Func(): logFunc('called. pollLatencyWarning=%s, old=%s', pollLatencyWarning, self.pollLatencyWarning)
        self.pollLatencyWarningSet = True
        self.pollLatencyWarning = pollLatencyWarning

    def requestSinglePollDurationWarning (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-singlepolldurationwarning').debug3Func(): logFunc('called. requested=%s', requested)
        self.singlePollDurationWarningRequested = requested
        self.singlePollDurationWarningSet = False

    def isSinglePollDurationWarningRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-singlepolldurationwarning-requested').debug3Func(): logFunc('called. requested=%s', self.singlePollDurationWarningRequested)
        return self.singlePollDurationWarningRequested

    def getSinglePollDurationWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-singlepolldurationwarning').debug3Func(): logFunc('called. self.singlePollDurationWarningSet=%s, self.singlePollDurationWarning=%s', self.singlePollDurationWarningSet, self.singlePollDurationWarning)
        if self.singlePollDurationWarningSet:
            return self.singlePollDurationWarning
        return None

    def hasSinglePollDurationWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-singlepolldurationwarning').debug3Func(): logFunc('called. self.singlePollDurationWarningSet=%s, self.singlePollDurationWarning=%s', self.singlePollDurationWarningSet, self.singlePollDurationWarning)
        if self.singlePollDurationWarningSet:
            return True
        return False

    def setSinglePollDurationWarning (self, singlePollDurationWarning):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-singlepolldurationwarning').debug3Func(): logFunc('called. singlePollDurationWarning=%s, old=%s', singlePollDurationWarning, self.singlePollDurationWarning)
        self.singlePollDurationWarningSet = True
        self.singlePollDurationWarning = singlePollDurationWarning

    def requestSinglePollDurationError (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-singlepolldurationerror').debug3Func(): logFunc('called. requested=%s', requested)
        self.singlePollDurationErrorRequested = requested
        self.singlePollDurationErrorSet = False

    def isSinglePollDurationErrorRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-singlepolldurationerror-requested').debug3Func(): logFunc('called. requested=%s', self.singlePollDurationErrorRequested)
        return self.singlePollDurationErrorRequested

    def getSinglePollDurationError (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-singlepolldurationerror').debug3Func(): logFunc('called. self.singlePollDurationErrorSet=%s, self.singlePollDurationError=%s', self.singlePollDurationErrorSet, self.singlePollDurationError)
        if self.singlePollDurationErrorSet:
            return self.singlePollDurationError
        return None

    def hasSinglePollDurationError (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-singlepolldurationerror').debug3Func(): logFunc('called. self.singlePollDurationErrorSet=%s, self.singlePollDurationError=%s', self.singlePollDurationErrorSet, self.singlePollDurationError)
        if self.singlePollDurationErrorSet:
            return True
        return False

    def setSinglePollDurationError (self, singlePollDurationError):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-singlepolldurationerror').debug3Func(): logFunc('called. singlePollDurationError=%s, old=%s', singlePollDurationError, self.singlePollDurationError)
        self.singlePollDurationErrorSet = True
        self.singlePollDurationError = singlePollDurationError

    def requestOverallPollDurationError (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-overallpolldurationerror').debug3Func(): logFunc('called. requested=%s', requested)
        self.overallPollDurationErrorRequested = requested
        self.overallPollDurationErrorSet = False

    def isOverallPollDurationErrorRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-overallpolldurationerror-requested').debug3Func(): logFunc('called. requested=%s', self.overallPollDurationErrorRequested)
        return self.overallPollDurationErrorRequested

    def getOverallPollDurationError (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-overallpolldurationerror').debug3Func(): logFunc('called. self.overallPollDurationErrorSet=%s, self.overallPollDurationError=%s', self.overallPollDurationErrorSet, self.overallPollDurationError)
        if self.overallPollDurationErrorSet:
            return self.overallPollDurationError
        return None

    def hasOverallPollDurationError (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-overallpolldurationerror').debug3Func(): logFunc('called. self.overallPollDurationErrorSet=%s, self.overallPollDurationError=%s', self.overallPollDurationErrorSet, self.overallPollDurationError)
        if self.overallPollDurationErrorSet:
            return True
        return False

    def setOverallPollDurationError (self, overallPollDurationError):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-overallpolldurationerror').debug3Func(): logFunc('called. overallPollDurationError=%s, old=%s', overallPollDurationError, self.overallPollDurationError)
        self.overallPollDurationErrorSet = True
        self.overallPollDurationError = overallPollDurationError


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.pollLatencyError = 0
        self.pollLatencyErrorSet = False
        
        self.overallPollDurationWarning = 0
        self.overallPollDurationWarningSet = False
        
        self.pollLatencyWarning = 0
        self.pollLatencyWarningSet = False
        
        self.singlePollDurationWarning = 0
        self.singlePollDurationWarningSet = False
        
        self.singlePollDurationError = 0
        self.singlePollDurationErrorSet = False
        
        self.overallPollDurationError = 0
        self.overallPollDurationErrorSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("manager", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("platform", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", "qt-pltf"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       
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

        keyPath = self._getSelfKeyPath(
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
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasPollLatencyError():
            valPollLatencyError = Value()
            if self.pollLatencyError is not None:
                valPollLatencyError.setInt64(self.pollLatencyError)
            else:
                valPollLatencyError.setEmpty()
            tagValueList.push(("poll-latency-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valPollLatencyError)
        
        if self.hasOverallPollDurationWarning():
            valOverallPollDurationWarning = Value()
            if self.overallPollDurationWarning is not None:
                valOverallPollDurationWarning.setInt64(self.overallPollDurationWarning)
            else:
                valOverallPollDurationWarning.setEmpty()
            tagValueList.push(("overall-poll-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valOverallPollDurationWarning)
        
        if self.hasPollLatencyWarning():
            valPollLatencyWarning = Value()
            if self.pollLatencyWarning is not None:
                valPollLatencyWarning.setInt64(self.pollLatencyWarning)
            else:
                valPollLatencyWarning.setEmpty()
            tagValueList.push(("poll-latency-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valPollLatencyWarning)
        
        if self.hasSinglePollDurationWarning():
            valSinglePollDurationWarning = Value()
            if self.singlePollDurationWarning is not None:
                valSinglePollDurationWarning.setInt64(self.singlePollDurationWarning)
            else:
                valSinglePollDurationWarning.setEmpty()
            tagValueList.push(("single-poll-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valSinglePollDurationWarning)
        
        if self.hasSinglePollDurationError():
            valSinglePollDurationError = Value()
            if self.singlePollDurationError is not None:
                valSinglePollDurationError.setInt64(self.singlePollDurationError)
            else:
                valSinglePollDurationError.setEmpty()
            tagValueList.push(("single-poll-duration-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valSinglePollDurationError)
        
        if self.hasOverallPollDurationError():
            valOverallPollDurationError = Value()
            if self.overallPollDurationError is not None:
                valOverallPollDurationError.setInt64(self.overallPollDurationError)
            else:
                valOverallPollDurationError.setEmpty()
            tagValueList.push(("overall-poll-duration-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valOverallPollDurationError)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isPollLatencyErrorRequested():
            valPollLatencyError = Value()
            valPollLatencyError.setEmpty()
            tagValueList.push(("poll-latency-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valPollLatencyError)
        
        if self.isOverallPollDurationWarningRequested():
            valOverallPollDurationWarning = Value()
            valOverallPollDurationWarning.setEmpty()
            tagValueList.push(("overall-poll-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valOverallPollDurationWarning)
        
        if self.isPollLatencyWarningRequested():
            valPollLatencyWarning = Value()
            valPollLatencyWarning.setEmpty()
            tagValueList.push(("poll-latency-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valPollLatencyWarning)
        
        if self.isSinglePollDurationWarningRequested():
            valSinglePollDurationWarning = Value()
            valSinglePollDurationWarning.setEmpty()
            tagValueList.push(("single-poll-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valSinglePollDurationWarning)
        
        if self.isSinglePollDurationErrorRequested():
            valSinglePollDurationError = Value()
            valSinglePollDurationError.setEmpty()
            tagValueList.push(("single-poll-duration-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valSinglePollDurationError)
        
        if self.isOverallPollDurationErrorRequested():
            valOverallPollDurationError = Value()
            valOverallPollDurationError.setEmpty()
            tagValueList.push(("overall-poll-duration-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valOverallPollDurationError)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isPollLatencyErrorRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-latency-error") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-polllatencyerror').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollLatencyError", "poll-latency-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-latency-error-bad-value').infoFunc(): logFunc('pollLatencyError not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollLatencyError(tempVar)
            for logFunc in self._log('read-tag-values-poll-latency-error').debug3Func(): logFunc('read pollLatencyError. pollLatencyError=%s, tempValue=%s', self.pollLatencyError, tempValue.getType())
        
        if self.isOverallPollDurationWarningRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "overall-poll-duration-warning") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-overallpolldurationwarning').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "overallPollDurationWarning", "overall-poll-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-overall-poll-duration-warning-bad-value').infoFunc(): logFunc('overallPollDurationWarning not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOverallPollDurationWarning(tempVar)
            for logFunc in self._log('read-tag-values-overall-poll-duration-warning').debug3Func(): logFunc('read overallPollDurationWarning. overallPollDurationWarning=%s, tempValue=%s', self.overallPollDurationWarning, tempValue.getType())
        
        if self.isPollLatencyWarningRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-latency-warning") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-polllatencywarning').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollLatencyWarning", "poll-latency-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-latency-warning-bad-value').infoFunc(): logFunc('pollLatencyWarning not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollLatencyWarning(tempVar)
            for logFunc in self._log('read-tag-values-poll-latency-warning').debug3Func(): logFunc('read pollLatencyWarning. pollLatencyWarning=%s, tempValue=%s', self.pollLatencyWarning, tempValue.getType())
        
        if self.isSinglePollDurationWarningRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "single-poll-duration-warning") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-singlepolldurationwarning').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "singlePollDurationWarning", "single-poll-duration-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-single-poll-duration-warning-bad-value').infoFunc(): logFunc('singlePollDurationWarning not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSinglePollDurationWarning(tempVar)
            for logFunc in self._log('read-tag-values-single-poll-duration-warning').debug3Func(): logFunc('read singlePollDurationWarning. singlePollDurationWarning=%s, tempValue=%s', self.singlePollDurationWarning, tempValue.getType())
        
        if self.isSinglePollDurationErrorRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "single-poll-duration-error") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-singlepolldurationerror').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "singlePollDurationError", "single-poll-duration-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-single-poll-duration-error-bad-value').infoFunc(): logFunc('singlePollDurationError not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSinglePollDurationError(tempVar)
            for logFunc in self._log('read-tag-values-single-poll-duration-error').debug3Func(): logFunc('read singlePollDurationError. singlePollDurationError=%s, tempValue=%s', self.singlePollDurationError, tempValue.getType())
        
        if self.isOverallPollDurationErrorRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "overall-poll-duration-error") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-overallpolldurationerror').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "overallPollDurationError", "overall-poll-duration-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-overall-poll-duration-error-bad-value').infoFunc(): logFunc('overallPollDurationError not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOverallPollDurationError(tempVar)
            for logFunc in self._log('read-tag-values-overall-poll-duration-error').debug3Func(): logFunc('read overallPollDurationError. overallPollDurationError=%s, tempValue=%s', self.overallPollDurationError, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "thresholds", 
        "namespace": "thresholds", 
        "className": "ThresholdsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.system_defaults.thresholds.thresholds_maapi_gen import ThresholdsMaapi", 
        "baseClassName": "ThresholdsMaapiBase", 
        "baseModule": "thresholds_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "yangName": "manager", 
            "namespace": "manager", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "name": "manager"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "yangName": "thresholds", 
            "namespace": "thresholds", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "name": "thresholds"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyError", 
            "yangName": "poll-latency-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationWarning", 
            "yangName": "overall-poll-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarning", 
            "yangName": "poll-latency-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationWarning", 
            "yangName": "single-poll-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationError", 
            "yangName": "single-poll-duration-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationError", 
            "yangName": "overall-poll-duration-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_platform_manager"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyError", 
            "yangName": "poll-latency-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationWarning", 
            "yangName": "overall-poll-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarning", 
            "yangName": "poll-latency-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationWarning", 
            "yangName": "single-poll-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationError", 
            "yangName": "single-poll-duration-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationError", 
            "yangName": "overall-poll-duration-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


