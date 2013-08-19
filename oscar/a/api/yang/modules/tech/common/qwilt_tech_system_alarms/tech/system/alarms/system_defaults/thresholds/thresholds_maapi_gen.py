


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

        

        
        self.singlePollDurationWarningMsecRequested = False
        self.singlePollDurationWarningMsec = None
        self.singlePollDurationWarningMsecSet = False
        
        self.pollLatencyErrorSecondsRequested = False
        self.pollLatencyErrorSeconds = None
        self.pollLatencyErrorSecondsSet = False
        
        self.singlePollDurationErrorMsecRequested = False
        self.singlePollDurationErrorMsec = None
        self.singlePollDurationErrorMsecSet = False
        
        self.overallPollDurationErrorMsecRequested = False
        self.overallPollDurationErrorMsec = None
        self.overallPollDurationErrorMsecSet = False
        
        self.pollLatencyWarningSecondsRequested = False
        self.pollLatencyWarningSeconds = None
        self.pollLatencyWarningSecondsSet = False
        
        self.overallPollDurationWarningMsecRequested = False
        self.overallPollDurationWarningMsec = None
        self.overallPollDurationWarningMsecSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSinglePollDurationWarningMsec(True)
        
        self.requestPollLatencyErrorSeconds(True)
        
        self.requestSinglePollDurationErrorMsec(True)
        
        self.requestOverallPollDurationErrorMsec(True)
        
        self.requestPollLatencyWarningSeconds(True)
        
        self.requestOverallPollDurationWarningMsec(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSinglePollDurationWarningMsec(True)
        
        self.requestPollLatencyErrorSeconds(True)
        
        self.requestSinglePollDurationErrorMsec(True)
        
        self.requestOverallPollDurationErrorMsec(True)
        
        self.requestPollLatencyWarningSeconds(True)
        
        self.requestOverallPollDurationWarningMsec(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSinglePollDurationWarningMsec(False)
        
        self.requestPollLatencyErrorSeconds(False)
        
        self.requestSinglePollDurationErrorMsec(False)
        
        self.requestOverallPollDurationErrorMsec(False)
        
        self.requestPollLatencyWarningSeconds(False)
        
        self.requestOverallPollDurationWarningMsec(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSinglePollDurationWarningMsec(False)
        
        self.requestPollLatencyErrorSeconds(False)
        
        self.requestSinglePollDurationErrorMsec(False)
        
        self.requestOverallPollDurationErrorMsec(False)
        
        self.requestPollLatencyWarningSeconds(False)
        
        self.requestOverallPollDurationWarningMsec(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setSinglePollDurationWarningMsec(None)
        self.singlePollDurationWarningMsecSet = False
        
        self.setPollLatencyErrorSeconds(None)
        self.pollLatencyErrorSecondsSet = False
        
        self.setSinglePollDurationErrorMsec(None)
        self.singlePollDurationErrorMsecSet = False
        
        self.setOverallPollDurationErrorMsec(None)
        self.overallPollDurationErrorMsecSet = False
        
        self.setPollLatencyWarningSeconds(None)
        self.pollLatencyWarningSecondsSet = False
        
        self.setOverallPollDurationWarningMsec(None)
        self.overallPollDurationWarningMsecSet = False
        
        

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



    def requestSinglePollDurationWarningMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-singlepolldurationwarningmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.singlePollDurationWarningMsecRequested = requested
        self.singlePollDurationWarningMsecSet = False

    def isSinglePollDurationWarningMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-singlepolldurationwarningmsec-requested').debug3Func(): logFunc('called. requested=%s', self.singlePollDurationWarningMsecRequested)
        return self.singlePollDurationWarningMsecRequested

    def getSinglePollDurationWarningMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-singlepolldurationwarningmsec').debug3Func(): logFunc('called. self.singlePollDurationWarningMsecSet=%s, self.singlePollDurationWarningMsec=%s', self.singlePollDurationWarningMsecSet, self.singlePollDurationWarningMsec)
        if self.singlePollDurationWarningMsecSet:
            return self.singlePollDurationWarningMsec
        return None

    def hasSinglePollDurationWarningMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-singlepolldurationwarningmsec').debug3Func(): logFunc('called. self.singlePollDurationWarningMsecSet=%s, self.singlePollDurationWarningMsec=%s', self.singlePollDurationWarningMsecSet, self.singlePollDurationWarningMsec)
        if self.singlePollDurationWarningMsecSet:
            return True
        return False

    def setSinglePollDurationWarningMsec (self, singlePollDurationWarningMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-singlepolldurationwarningmsec').debug3Func(): logFunc('called. singlePollDurationWarningMsec=%s, old=%s', singlePollDurationWarningMsec, self.singlePollDurationWarningMsec)
        self.singlePollDurationWarningMsecSet = True
        self.singlePollDurationWarningMsec = singlePollDurationWarningMsec

    def requestPollLatencyErrorSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-polllatencyerrorseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollLatencyErrorSecondsRequested = requested
        self.pollLatencyErrorSecondsSet = False

    def isPollLatencyErrorSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-polllatencyerrorseconds-requested').debug3Func(): logFunc('called. requested=%s', self.pollLatencyErrorSecondsRequested)
        return self.pollLatencyErrorSecondsRequested

    def getPollLatencyErrorSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-polllatencyerrorseconds').debug3Func(): logFunc('called. self.pollLatencyErrorSecondsSet=%s, self.pollLatencyErrorSeconds=%s', self.pollLatencyErrorSecondsSet, self.pollLatencyErrorSeconds)
        if self.pollLatencyErrorSecondsSet:
            return self.pollLatencyErrorSeconds
        return None

    def hasPollLatencyErrorSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-polllatencyerrorseconds').debug3Func(): logFunc('called. self.pollLatencyErrorSecondsSet=%s, self.pollLatencyErrorSeconds=%s', self.pollLatencyErrorSecondsSet, self.pollLatencyErrorSeconds)
        if self.pollLatencyErrorSecondsSet:
            return True
        return False

    def setPollLatencyErrorSeconds (self, pollLatencyErrorSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-polllatencyerrorseconds').debug3Func(): logFunc('called. pollLatencyErrorSeconds=%s, old=%s', pollLatencyErrorSeconds, self.pollLatencyErrorSeconds)
        self.pollLatencyErrorSecondsSet = True
        self.pollLatencyErrorSeconds = pollLatencyErrorSeconds

    def requestSinglePollDurationErrorMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-singlepolldurationerrormsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.singlePollDurationErrorMsecRequested = requested
        self.singlePollDurationErrorMsecSet = False

    def isSinglePollDurationErrorMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-singlepolldurationerrormsec-requested').debug3Func(): logFunc('called. requested=%s', self.singlePollDurationErrorMsecRequested)
        return self.singlePollDurationErrorMsecRequested

    def getSinglePollDurationErrorMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-singlepolldurationerrormsec').debug3Func(): logFunc('called. self.singlePollDurationErrorMsecSet=%s, self.singlePollDurationErrorMsec=%s', self.singlePollDurationErrorMsecSet, self.singlePollDurationErrorMsec)
        if self.singlePollDurationErrorMsecSet:
            return self.singlePollDurationErrorMsec
        return None

    def hasSinglePollDurationErrorMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-singlepolldurationerrormsec').debug3Func(): logFunc('called. self.singlePollDurationErrorMsecSet=%s, self.singlePollDurationErrorMsec=%s', self.singlePollDurationErrorMsecSet, self.singlePollDurationErrorMsec)
        if self.singlePollDurationErrorMsecSet:
            return True
        return False

    def setSinglePollDurationErrorMsec (self, singlePollDurationErrorMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-singlepolldurationerrormsec').debug3Func(): logFunc('called. singlePollDurationErrorMsec=%s, old=%s', singlePollDurationErrorMsec, self.singlePollDurationErrorMsec)
        self.singlePollDurationErrorMsecSet = True
        self.singlePollDurationErrorMsec = singlePollDurationErrorMsec

    def requestOverallPollDurationErrorMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-overallpolldurationerrormsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.overallPollDurationErrorMsecRequested = requested
        self.overallPollDurationErrorMsecSet = False

    def isOverallPollDurationErrorMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-overallpolldurationerrormsec-requested').debug3Func(): logFunc('called. requested=%s', self.overallPollDurationErrorMsecRequested)
        return self.overallPollDurationErrorMsecRequested

    def getOverallPollDurationErrorMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-overallpolldurationerrormsec').debug3Func(): logFunc('called. self.overallPollDurationErrorMsecSet=%s, self.overallPollDurationErrorMsec=%s', self.overallPollDurationErrorMsecSet, self.overallPollDurationErrorMsec)
        if self.overallPollDurationErrorMsecSet:
            return self.overallPollDurationErrorMsec
        return None

    def hasOverallPollDurationErrorMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-overallpolldurationerrormsec').debug3Func(): logFunc('called. self.overallPollDurationErrorMsecSet=%s, self.overallPollDurationErrorMsec=%s', self.overallPollDurationErrorMsecSet, self.overallPollDurationErrorMsec)
        if self.overallPollDurationErrorMsecSet:
            return True
        return False

    def setOverallPollDurationErrorMsec (self, overallPollDurationErrorMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-overallpolldurationerrormsec').debug3Func(): logFunc('called. overallPollDurationErrorMsec=%s, old=%s', overallPollDurationErrorMsec, self.overallPollDurationErrorMsec)
        self.overallPollDurationErrorMsecSet = True
        self.overallPollDurationErrorMsec = overallPollDurationErrorMsec

    def requestPollLatencyWarningSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-polllatencywarningseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollLatencyWarningSecondsRequested = requested
        self.pollLatencyWarningSecondsSet = False

    def isPollLatencyWarningSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-polllatencywarningseconds-requested').debug3Func(): logFunc('called. requested=%s', self.pollLatencyWarningSecondsRequested)
        return self.pollLatencyWarningSecondsRequested

    def getPollLatencyWarningSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-polllatencywarningseconds').debug3Func(): logFunc('called. self.pollLatencyWarningSecondsSet=%s, self.pollLatencyWarningSeconds=%s', self.pollLatencyWarningSecondsSet, self.pollLatencyWarningSeconds)
        if self.pollLatencyWarningSecondsSet:
            return self.pollLatencyWarningSeconds
        return None

    def hasPollLatencyWarningSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-polllatencywarningseconds').debug3Func(): logFunc('called. self.pollLatencyWarningSecondsSet=%s, self.pollLatencyWarningSeconds=%s', self.pollLatencyWarningSecondsSet, self.pollLatencyWarningSeconds)
        if self.pollLatencyWarningSecondsSet:
            return True
        return False

    def setPollLatencyWarningSeconds (self, pollLatencyWarningSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-polllatencywarningseconds').debug3Func(): logFunc('called. pollLatencyWarningSeconds=%s, old=%s', pollLatencyWarningSeconds, self.pollLatencyWarningSeconds)
        self.pollLatencyWarningSecondsSet = True
        self.pollLatencyWarningSeconds = pollLatencyWarningSeconds

    def requestOverallPollDurationWarningMsec (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-overallpolldurationwarningmsec').debug3Func(): logFunc('called. requested=%s', requested)
        self.overallPollDurationWarningMsecRequested = requested
        self.overallPollDurationWarningMsecSet = False

    def isOverallPollDurationWarningMsecRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-overallpolldurationwarningmsec-requested').debug3Func(): logFunc('called. requested=%s', self.overallPollDurationWarningMsecRequested)
        return self.overallPollDurationWarningMsecRequested

    def getOverallPollDurationWarningMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-overallpolldurationwarningmsec').debug3Func(): logFunc('called. self.overallPollDurationWarningMsecSet=%s, self.overallPollDurationWarningMsec=%s', self.overallPollDurationWarningMsecSet, self.overallPollDurationWarningMsec)
        if self.overallPollDurationWarningMsecSet:
            return self.overallPollDurationWarningMsec
        return None

    def hasOverallPollDurationWarningMsec (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-overallpolldurationwarningmsec').debug3Func(): logFunc('called. self.overallPollDurationWarningMsecSet=%s, self.overallPollDurationWarningMsec=%s', self.overallPollDurationWarningMsecSet, self.overallPollDurationWarningMsec)
        if self.overallPollDurationWarningMsecSet:
            return True
        return False

    def setOverallPollDurationWarningMsec (self, overallPollDurationWarningMsec):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-overallpolldurationwarningmsec').debug3Func(): logFunc('called. overallPollDurationWarningMsec=%s, old=%s', overallPollDurationWarningMsec, self.overallPollDurationWarningMsec)
        self.overallPollDurationWarningMsecSet = True
        self.overallPollDurationWarningMsec = overallPollDurationWarningMsec


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.singlePollDurationWarningMsec = 0
        self.singlePollDurationWarningMsecSet = False
        
        self.pollLatencyErrorSeconds = 0
        self.pollLatencyErrorSecondsSet = False
        
        self.singlePollDurationErrorMsec = 0
        self.singlePollDurationErrorMsecSet = False
        
        self.overallPollDurationErrorMsec = 0
        self.overallPollDurationErrorMsecSet = False
        
        self.pollLatencyWarningSeconds = 0
        self.pollLatencyWarningSecondsSet = False
        
        self.overallPollDurationWarningMsec = 0
        self.overallPollDurationWarningMsecSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
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

        
        if self.hasSinglePollDurationWarningMsec():
            valSinglePollDurationWarningMsec = Value()
            if self.singlePollDurationWarningMsec is not None:
                valSinglePollDurationWarningMsec.setInt64(self.singlePollDurationWarningMsec)
            else:
                valSinglePollDurationWarningMsec.setEmpty()
            tagValueList.push(("single-poll-duration-warning-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valSinglePollDurationWarningMsec)
        
        if self.hasPollLatencyErrorSeconds():
            valPollLatencyErrorSeconds = Value()
            if self.pollLatencyErrorSeconds is not None:
                valPollLatencyErrorSeconds.setInt64(self.pollLatencyErrorSeconds)
            else:
                valPollLatencyErrorSeconds.setEmpty()
            tagValueList.push(("poll-latency-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valPollLatencyErrorSeconds)
        
        if self.hasSinglePollDurationErrorMsec():
            valSinglePollDurationErrorMsec = Value()
            if self.singlePollDurationErrorMsec is not None:
                valSinglePollDurationErrorMsec.setInt64(self.singlePollDurationErrorMsec)
            else:
                valSinglePollDurationErrorMsec.setEmpty()
            tagValueList.push(("single-poll-duration-error-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valSinglePollDurationErrorMsec)
        
        if self.hasOverallPollDurationErrorMsec():
            valOverallPollDurationErrorMsec = Value()
            if self.overallPollDurationErrorMsec is not None:
                valOverallPollDurationErrorMsec.setInt64(self.overallPollDurationErrorMsec)
            else:
                valOverallPollDurationErrorMsec.setEmpty()
            tagValueList.push(("overall-poll-duration-error-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valOverallPollDurationErrorMsec)
        
        if self.hasPollLatencyWarningSeconds():
            valPollLatencyWarningSeconds = Value()
            if self.pollLatencyWarningSeconds is not None:
                valPollLatencyWarningSeconds.setInt64(self.pollLatencyWarningSeconds)
            else:
                valPollLatencyWarningSeconds.setEmpty()
            tagValueList.push(("poll-latency-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valPollLatencyWarningSeconds)
        
        if self.hasOverallPollDurationWarningMsec():
            valOverallPollDurationWarningMsec = Value()
            if self.overallPollDurationWarningMsec is not None:
                valOverallPollDurationWarningMsec.setInt64(self.overallPollDurationWarningMsec)
            else:
                valOverallPollDurationWarningMsec.setEmpty()
            tagValueList.push(("overall-poll-duration-warning-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valOverallPollDurationWarningMsec)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isSinglePollDurationWarningMsecRequested():
            valSinglePollDurationWarningMsec = Value()
            valSinglePollDurationWarningMsec.setEmpty()
            tagValueList.push(("single-poll-duration-warning-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valSinglePollDurationWarningMsec)
        
        if self.isPollLatencyErrorSecondsRequested():
            valPollLatencyErrorSeconds = Value()
            valPollLatencyErrorSeconds.setEmpty()
            tagValueList.push(("poll-latency-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valPollLatencyErrorSeconds)
        
        if self.isSinglePollDurationErrorMsecRequested():
            valSinglePollDurationErrorMsec = Value()
            valSinglePollDurationErrorMsec.setEmpty()
            tagValueList.push(("single-poll-duration-error-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valSinglePollDurationErrorMsec)
        
        if self.isOverallPollDurationErrorMsecRequested():
            valOverallPollDurationErrorMsec = Value()
            valOverallPollDurationErrorMsec.setEmpty()
            tagValueList.push(("overall-poll-duration-error-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valOverallPollDurationErrorMsec)
        
        if self.isPollLatencyWarningSecondsRequested():
            valPollLatencyWarningSeconds = Value()
            valPollLatencyWarningSeconds.setEmpty()
            tagValueList.push(("poll-latency-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valPollLatencyWarningSeconds)
        
        if self.isOverallPollDurationWarningMsecRequested():
            valOverallPollDurationWarningMsec = Value()
            valOverallPollDurationWarningMsec.setEmpty()
            tagValueList.push(("overall-poll-duration-warning-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valOverallPollDurationWarningMsec)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isSinglePollDurationWarningMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "single-poll-duration-warning-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-singlepolldurationwarningmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "singlePollDurationWarningMsec", "single-poll-duration-warning-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-single-poll-duration-warning-msec-bad-value').infoFunc(): logFunc('singlePollDurationWarningMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSinglePollDurationWarningMsec(tempVar)
            for logFunc in self._log('read-tag-values-single-poll-duration-warning-msec').debug3Func(): logFunc('read singlePollDurationWarningMsec. singlePollDurationWarningMsec=%s, tempValue=%s', self.singlePollDurationWarningMsec, tempValue.getType())
        
        if self.isPollLatencyErrorSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-latency-error-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-polllatencyerrorseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollLatencyErrorSeconds", "poll-latency-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-latency-error-seconds-bad-value').infoFunc(): logFunc('pollLatencyErrorSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollLatencyErrorSeconds(tempVar)
            for logFunc in self._log('read-tag-values-poll-latency-error-seconds').debug3Func(): logFunc('read pollLatencyErrorSeconds. pollLatencyErrorSeconds=%s, tempValue=%s', self.pollLatencyErrorSeconds, tempValue.getType())
        
        if self.isSinglePollDurationErrorMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "single-poll-duration-error-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-singlepolldurationerrormsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "singlePollDurationErrorMsec", "single-poll-duration-error-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-single-poll-duration-error-msec-bad-value').infoFunc(): logFunc('singlePollDurationErrorMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSinglePollDurationErrorMsec(tempVar)
            for logFunc in self._log('read-tag-values-single-poll-duration-error-msec').debug3Func(): logFunc('read singlePollDurationErrorMsec. singlePollDurationErrorMsec=%s, tempValue=%s', self.singlePollDurationErrorMsec, tempValue.getType())
        
        if self.isOverallPollDurationErrorMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "overall-poll-duration-error-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-overallpolldurationerrormsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "overallPollDurationErrorMsec", "overall-poll-duration-error-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-overall-poll-duration-error-msec-bad-value').infoFunc(): logFunc('overallPollDurationErrorMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOverallPollDurationErrorMsec(tempVar)
            for logFunc in self._log('read-tag-values-overall-poll-duration-error-msec').debug3Func(): logFunc('read overallPollDurationErrorMsec. overallPollDurationErrorMsec=%s, tempValue=%s', self.overallPollDurationErrorMsec, tempValue.getType())
        
        if self.isPollLatencyWarningSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-latency-warning-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-polllatencywarningseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollLatencyWarningSeconds", "poll-latency-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-latency-warning-seconds-bad-value').infoFunc(): logFunc('pollLatencyWarningSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollLatencyWarningSeconds(tempVar)
            for logFunc in self._log('read-tag-values-poll-latency-warning-seconds').debug3Func(): logFunc('read pollLatencyWarningSeconds. pollLatencyWarningSeconds=%s, tempValue=%s', self.pollLatencyWarningSeconds, tempValue.getType())
        
        if self.isOverallPollDurationWarningMsecRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "overall-poll-duration-warning-msec") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-overallpolldurationwarningmsec').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "overallPollDurationWarningMsec", "overall-poll-duration-warning-msec", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-overall-poll-duration-warning-msec-bad-value').infoFunc(): logFunc('overallPollDurationWarningMsec not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOverallPollDurationWarningMsec(tempVar)
            for logFunc in self._log('read-tag-values-overall-poll-duration-warning-msec').debug3Func(): logFunc('read overallPollDurationWarningMsec. overallPollDurationWarningMsec=%s, tempValue=%s', self.overallPollDurationWarningMsec, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "thresholds", 
        "namespace": "thresholds", 
        "className": "ThresholdsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.system_defaults.thresholds.thresholds_maapi_gen import ThresholdsMaapi", 
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
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "system", 
            "namespace": "system", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "thresholds", 
            "namespace": "thresholds", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "thresholds"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationWarningMsec", 
            "yangName": "single-poll-duration-warning-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyErrorSeconds", 
            "yangName": "poll-latency-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationErrorMsec", 
            "yangName": "single-poll-duration-error-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationErrorMsec", 
            "yangName": "overall-poll-duration-error-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarningSeconds", 
            "yangName": "poll-latency-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationWarningMsec", 
            "yangName": "overall-poll-duration-warning-msec", 
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
            "qwilt_tech_system_alarms"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationWarningMsec", 
            "yangName": "single-poll-duration-warning-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyErrorSeconds", 
            "yangName": "poll-latency-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationErrorMsec", 
            "yangName": "single-poll-duration-error-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationErrorMsec", 
            "yangName": "overall-poll-duration-error-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarningSeconds", 
            "yangName": "poll-latency-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationWarningMsec", 
            "yangName": "overall-poll-duration-warning-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


