


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

from counters_maapi_base_gen import CountersMaapiBase




class BlinkyCountersMaapi(CountersMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-counters")
        self.domain = None

        

        
        self.activeSecondsRequested = False
        self.activeSeconds = None
        self.activeSecondsSet = False
        
        self.totalSecondsRequested = False
        self.totalSeconds = None
        self.totalSecondsSet = False
        
        self.pollsRequested = False
        self.polls = None
        self.pollsSet = False
        
        self.pollsMissedRequested = False
        self.pollsMissed = None
        self.pollsMissedSet = False
        
        self.pollLatencyWarningsRequested = False
        self.pollLatencyWarnings = None
        self.pollLatencyWarningsSet = False
        
        self.pollLatencyErrorsRequested = False
        self.pollLatencyErrors = None
        self.pollLatencyErrorsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestActiveSeconds(True)
        
        self.requestTotalSeconds(True)
        
        self.requestPolls(True)
        
        self.requestPollsMissed(True)
        
        self.requestPollLatencyWarnings(True)
        
        self.requestPollLatencyErrors(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestActiveSeconds(False)
        
        self.requestTotalSeconds(False)
        
        self.requestPolls(False)
        
        self.requestPollsMissed(False)
        
        self.requestPollLatencyWarnings(False)
        
        self.requestPollLatencyErrors(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestActiveSeconds(True)
        
        self.requestTotalSeconds(True)
        
        self.requestPolls(True)
        
        self.requestPollsMissed(True)
        
        self.requestPollLatencyWarnings(True)
        
        self.requestPollLatencyErrors(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestActiveSeconds(False)
        
        self.requestTotalSeconds(False)
        
        self.requestPolls(False)
        
        self.requestPollsMissed(False)
        
        self.requestPollLatencyWarnings(False)
        
        self.requestPollLatencyErrors(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

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



    def requestActiveSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-activeseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.activeSecondsRequested = requested
        self.activeSecondsSet = False

    def isActiveSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-activeseconds-requested').debug3Func(): logFunc('called. requested=%s', self.activeSecondsRequested)
        return self.activeSecondsRequested

    def getActiveSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-activeseconds').debug3Func(): logFunc('called. self.activeSecondsSet=%s, self.activeSeconds=%s', self.activeSecondsSet, self.activeSeconds)
        if self.activeSecondsSet:
            return self.activeSeconds
        return None

    def hasActiveSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-activeseconds').debug3Func(): logFunc('called. self.activeSecondsSet=%s, self.activeSeconds=%s', self.activeSecondsSet, self.activeSeconds)
        if self.activeSecondsSet:
            return True
        return False

    def setActiveSeconds (self, activeSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-activeseconds').debug3Func(): logFunc('called. activeSeconds=%s, old=%s', activeSeconds, self.activeSeconds)
        self.activeSecondsSet = True
        self.activeSeconds = activeSeconds

    def requestTotalSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-totalseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.totalSecondsRequested = requested
        self.totalSecondsSet = False

    def isTotalSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-totalseconds-requested').debug3Func(): logFunc('called. requested=%s', self.totalSecondsRequested)
        return self.totalSecondsRequested

    def getTotalSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-totalseconds').debug3Func(): logFunc('called. self.totalSecondsSet=%s, self.totalSeconds=%s', self.totalSecondsSet, self.totalSeconds)
        if self.totalSecondsSet:
            return self.totalSeconds
        return None

    def hasTotalSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-totalseconds').debug3Func(): logFunc('called. self.totalSecondsSet=%s, self.totalSeconds=%s', self.totalSecondsSet, self.totalSeconds)
        if self.totalSecondsSet:
            return True
        return False

    def setTotalSeconds (self, totalSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-totalseconds').debug3Func(): logFunc('called. totalSeconds=%s, old=%s', totalSeconds, self.totalSeconds)
        self.totalSecondsSet = True
        self.totalSeconds = totalSeconds

    def requestPolls (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-polls').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollsRequested = requested
        self.pollsSet = False

    def isPollsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-polls-requested').debug3Func(): logFunc('called. requested=%s', self.pollsRequested)
        return self.pollsRequested

    def getPolls (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-polls').debug3Func(): logFunc('called. self.pollsSet=%s, self.polls=%s', self.pollsSet, self.polls)
        if self.pollsSet:
            return self.polls
        return None

    def hasPolls (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-polls').debug3Func(): logFunc('called. self.pollsSet=%s, self.polls=%s', self.pollsSet, self.polls)
        if self.pollsSet:
            return True
        return False

    def setPolls (self, polls):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-polls').debug3Func(): logFunc('called. polls=%s, old=%s', polls, self.polls)
        self.pollsSet = True
        self.polls = polls

    def requestPollsMissed (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pollsmissed').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollsMissedRequested = requested
        self.pollsMissedSet = False

    def isPollsMissedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pollsmissed-requested').debug3Func(): logFunc('called. requested=%s', self.pollsMissedRequested)
        return self.pollsMissedRequested

    def getPollsMissed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pollsmissed').debug3Func(): logFunc('called. self.pollsMissedSet=%s, self.pollsMissed=%s', self.pollsMissedSet, self.pollsMissed)
        if self.pollsMissedSet:
            return self.pollsMissed
        return None

    def hasPollsMissed (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pollsmissed').debug3Func(): logFunc('called. self.pollsMissedSet=%s, self.pollsMissed=%s', self.pollsMissedSet, self.pollsMissed)
        if self.pollsMissedSet:
            return True
        return False

    def setPollsMissed (self, pollsMissed):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pollsmissed').debug3Func(): logFunc('called. pollsMissed=%s, old=%s', pollsMissed, self.pollsMissed)
        self.pollsMissedSet = True
        self.pollsMissed = pollsMissed

    def requestPollLatencyWarnings (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-polllatencywarnings').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollLatencyWarningsRequested = requested
        self.pollLatencyWarningsSet = False

    def isPollLatencyWarningsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-polllatencywarnings-requested').debug3Func(): logFunc('called. requested=%s', self.pollLatencyWarningsRequested)
        return self.pollLatencyWarningsRequested

    def getPollLatencyWarnings (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-polllatencywarnings').debug3Func(): logFunc('called. self.pollLatencyWarningsSet=%s, self.pollLatencyWarnings=%s', self.pollLatencyWarningsSet, self.pollLatencyWarnings)
        if self.pollLatencyWarningsSet:
            return self.pollLatencyWarnings
        return None

    def hasPollLatencyWarnings (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-polllatencywarnings').debug3Func(): logFunc('called. self.pollLatencyWarningsSet=%s, self.pollLatencyWarnings=%s', self.pollLatencyWarningsSet, self.pollLatencyWarnings)
        if self.pollLatencyWarningsSet:
            return True
        return False

    def setPollLatencyWarnings (self, pollLatencyWarnings):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-polllatencywarnings').debug3Func(): logFunc('called. pollLatencyWarnings=%s, old=%s', pollLatencyWarnings, self.pollLatencyWarnings)
        self.pollLatencyWarningsSet = True
        self.pollLatencyWarnings = pollLatencyWarnings

    def requestPollLatencyErrors (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-polllatencyerrors').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollLatencyErrorsRequested = requested
        self.pollLatencyErrorsSet = False

    def isPollLatencyErrorsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-polllatencyerrors-requested').debug3Func(): logFunc('called. requested=%s', self.pollLatencyErrorsRequested)
        return self.pollLatencyErrorsRequested

    def getPollLatencyErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-polllatencyerrors').debug3Func(): logFunc('called. self.pollLatencyErrorsSet=%s, self.pollLatencyErrors=%s', self.pollLatencyErrorsSet, self.pollLatencyErrors)
        if self.pollLatencyErrorsSet:
            return self.pollLatencyErrors
        return None

    def hasPollLatencyErrors (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-polllatencyerrors').debug3Func(): logFunc('called. self.pollLatencyErrorsSet=%s, self.pollLatencyErrors=%s', self.pollLatencyErrorsSet, self.pollLatencyErrors)
        if self.pollLatencyErrorsSet:
            return True
        return False

    def setPollLatencyErrors (self, pollLatencyErrors):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-polllatencyerrors').debug3Func(): logFunc('called. pollLatencyErrors=%s, old=%s', pollLatencyErrors, self.pollLatencyErrors)
        self.pollLatencyErrorsSet = True
        self.pollLatencyErrors = pollLatencyErrors


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.activeSeconds = 0
        self.activeSecondsSet = False
        
        self.totalSeconds = 0
        self.totalSecondsSet = False
        
        self.polls = 0
        self.pollsSet = False
        
        self.pollsMissed = 0
        self.pollsMissedSet = False
        
        self.pollLatencyWarnings = 0
        self.pollLatencyWarningsSet = False
        
        self.pollLatencyErrors = 0
        self.pollLatencyErrorsSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("housekeeper", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("log", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
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

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isActiveSecondsRequested():
            valActiveSeconds = Value()
            valActiveSeconds.setEmpty()
            tagValueList.push(("active-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valActiveSeconds)
        
        if self.isTotalSecondsRequested():
            valTotalSeconds = Value()
            valTotalSeconds.setEmpty()
            tagValueList.push(("total-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valTotalSeconds)
        
        if self.isPollsRequested():
            valPolls = Value()
            valPolls.setEmpty()
            tagValueList.push(("polls", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPolls)
        
        if self.isPollsMissedRequested():
            valPollsMissed = Value()
            valPollsMissed.setEmpty()
            tagValueList.push(("polls-missed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPollsMissed)
        
        if self.isPollLatencyWarningsRequested():
            valPollLatencyWarnings = Value()
            valPollLatencyWarnings.setEmpty()
            tagValueList.push(("poll-latency-warnings", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPollLatencyWarnings)
        
        if self.isPollLatencyErrorsRequested():
            valPollLatencyErrors = Value()
            valPollLatencyErrors.setEmpty()
            tagValueList.push(("poll-latency-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPollLatencyErrors)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isActiveSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "active-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-activeseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "activeSeconds", "active-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-active-seconds-bad-value').infoFunc(): logFunc('activeSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setActiveSeconds(tempVar)
            for logFunc in self._log('read-tag-values-active-seconds').debug3Func(): logFunc('read activeSeconds. activeSeconds=%s, tempValue=%s', self.activeSeconds, tempValue.getType())
        
        if self.isTotalSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "total-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-totalseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "totalSeconds", "total-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-total-seconds-bad-value').infoFunc(): logFunc('totalSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTotalSeconds(tempVar)
            for logFunc in self._log('read-tag-values-total-seconds').debug3Func(): logFunc('read totalSeconds. totalSeconds=%s, tempValue=%s', self.totalSeconds, tempValue.getType())
        
        if self.isPollsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "polls") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-polls').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "polls", "polls", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-polls-bad-value').infoFunc(): logFunc('polls not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPolls(tempVar)
            for logFunc in self._log('read-tag-values-polls').debug3Func(): logFunc('read polls. polls=%s, tempValue=%s', self.polls, tempValue.getType())
        
        if self.isPollsMissedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "polls-missed") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pollsmissed').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollsMissed", "polls-missed", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-polls-missed-bad-value').infoFunc(): logFunc('pollsMissed not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollsMissed(tempVar)
            for logFunc in self._log('read-tag-values-polls-missed').debug3Func(): logFunc('read pollsMissed. pollsMissed=%s, tempValue=%s', self.pollsMissed, tempValue.getType())
        
        if self.isPollLatencyWarningsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-latency-warnings") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-polllatencywarnings').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollLatencyWarnings", "poll-latency-warnings", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-latency-warnings-bad-value').infoFunc(): logFunc('pollLatencyWarnings not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollLatencyWarnings(tempVar)
            for logFunc in self._log('read-tag-values-poll-latency-warnings').debug3Func(): logFunc('read pollLatencyWarnings. pollLatencyWarnings=%s, tempValue=%s', self.pollLatencyWarnings, tempValue.getType())
        
        if self.isPollLatencyErrorsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-latency-errors") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-polllatencyerrors').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollLatencyErrors", "poll-latency-errors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-latency-errors-bad-value').infoFunc(): logFunc('pollLatencyErrors not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollLatencyErrors(tempVar)
            for logFunc in self._log('read-tag-values-poll-latency-errors').debug3Func(): logFunc('read pollLatencyErrors. pollLatencyErrors=%s, tempValue=%s', self.pollLatencyErrors, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log", 
            "namespace": "log", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "housekeeper", 
            "namespace": "housekeeper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "housekeeper"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activeSeconds", 
            "yangName": "active-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "totalSeconds", 
            "yangName": "total-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "polls", 
            "yangName": "polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollsMissed", 
            "yangName": "polls-missed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarnings", 
            "yangName": "poll-latency-warnings", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyErrors", 
            "yangName": "poll-latency-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
    "configLeaves": [], 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "debug", 
            "qwilt_tech_log"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "activeSeconds", 
            "yangName": "active-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "totalSeconds", 
            "yangName": "total-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "polls", 
            "yangName": "polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollsMissed", 
            "yangName": "polls-missed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarnings", 
            "yangName": "poll-latency-warnings", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyErrors", 
            "yangName": "poll-latency-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


