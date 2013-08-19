


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

from controller_maapi_base_gen import ControllerMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.acquisition.controller.efficiency_algorithm.efficiency_algorithm_maapi_gen import BlinkyEfficiencyAlgorithmMaapi

from a.api.yang.modules.tech.content.qwilt_tech_content_line_types.qwilt_tech_content_line_types_module_gen import AcquisitionAlgorithmType


class BlinkyControllerMaapi(ControllerMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-controller")
        self.domain = None

        
        self.efficiencyAlgorithmObj = None
        

        
        self.lazyFileOpenRequested = False
        self.lazyFileOpen = None
        self.lazyFileOpenSet = False
        
        self.logPeriodicStatsRequested = False
        self.logPeriodicStats = None
        self.logPeriodicStatsSet = False
        
        self.maxSessionsRequested = False
        self.maxSessions = None
        self.maxSessionsSet = False
        
        self.sessionQueueLowWaterMarkPercentRequested = False
        self.sessionQueueLowWaterMarkPercent = None
        self.sessionQueueLowWaterMarkPercentSet = False
        
        self.maxActiveSessionsRequested = False
        self.maxActiveSessions = None
        self.maxActiveSessionsSet = False
        
        self.algorithmRequested = False
        self.algorithm = None
        self.algorithmSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLazyFileOpen(True)
        
        self.requestLogPeriodicStats(True)
        
        self.requestMaxSessions(True)
        
        self.requestSessionQueueLowWaterMarkPercent(True)
        
        self.requestMaxActiveSessions(True)
        
        self.requestAlgorithm(True)
        
        
        
        if not self.efficiencyAlgorithmObj:
            self.efficiencyAlgorithmObj = self.newEfficiencyAlgorithm()
            self.efficiencyAlgorithmObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLazyFileOpen(True)
        
        self.requestLogPeriodicStats(True)
        
        self.requestMaxSessions(True)
        
        self.requestSessionQueueLowWaterMarkPercent(True)
        
        self.requestMaxActiveSessions(True)
        
        self.requestAlgorithm(True)
        
        
        
        if not self.efficiencyAlgorithmObj:
            self.efficiencyAlgorithmObj = self.newEfficiencyAlgorithm()
            self.efficiencyAlgorithmObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLazyFileOpen(False)
        
        self.requestLogPeriodicStats(False)
        
        self.requestMaxSessions(False)
        
        self.requestSessionQueueLowWaterMarkPercent(False)
        
        self.requestMaxActiveSessions(False)
        
        self.requestAlgorithm(False)
        
        
        
        if not self.efficiencyAlgorithmObj:
            self.efficiencyAlgorithmObj = self.newEfficiencyAlgorithm()
            self.efficiencyAlgorithmObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLazyFileOpen(False)
        
        self.requestLogPeriodicStats(False)
        
        self.requestMaxSessions(False)
        
        self.requestSessionQueueLowWaterMarkPercent(False)
        
        self.requestMaxActiveSessions(False)
        
        self.requestAlgorithm(False)
        
        
        
        if not self.efficiencyAlgorithmObj:
            self.efficiencyAlgorithmObj = self.newEfficiencyAlgorithm()
            self.efficiencyAlgorithmObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setLazyFileOpen(None)
        self.lazyFileOpenSet = False
        
        self.setLogPeriodicStats(None)
        self.logPeriodicStatsSet = False
        
        self.setMaxSessions(None)
        self.maxSessionsSet = False
        
        self.setSessionQueueLowWaterMarkPercent(None)
        self.sessionQueueLowWaterMarkPercentSet = False
        
        self.setMaxActiveSessions(None)
        self.maxActiveSessionsSet = False
        
        self.setAlgorithm(None)
        self.algorithmSet = False
        
        
        if self.efficiencyAlgorithmObj:
            self.efficiencyAlgorithmObj.clearAllSet()
        

    def write (self
              , line
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(line, trxContext)

    def read (self
              , line
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , line
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  True,
                                  trxContext)

    def newEfficiencyAlgorithm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-efficiencyalgorithm').debug3Func(): logFunc('called.')
        efficiencyAlgorithm = BlinkyEfficiencyAlgorithmMaapi(self._log)
        efficiencyAlgorithm.init(self.domain)
        return efficiencyAlgorithm

    def setEfficiencyAlgorithmObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-efficiencyalgorithm').debug3Func(): logFunc('called. obj=%s', obj)
        self.efficiencyAlgorithmObj = obj

    def getEfficiencyAlgorithmObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-efficiencyalgorithm').debug3Func(): logFunc('called. self.efficiencyAlgorithmObj=%s', self.efficiencyAlgorithmObj)
        return self.efficiencyAlgorithmObj

    def hasEfficiencyAlgorithm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-efficiencyalgorithm').debug3Func(): logFunc('called. self.efficiencyAlgorithmObj=%s', self.efficiencyAlgorithmObj)
        if self.efficiencyAlgorithmObj:
            return True
        return False



    def requestLazyFileOpen (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-lazyfileopen').debug3Func(): logFunc('called. requested=%s', requested)
        self.lazyFileOpenRequested = requested
        self.lazyFileOpenSet = False

    def isLazyFileOpenRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-lazyfileopen-requested').debug3Func(): logFunc('called. requested=%s', self.lazyFileOpenRequested)
        return self.lazyFileOpenRequested

    def getLazyFileOpen (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-lazyfileopen').debug3Func(): logFunc('called. self.lazyFileOpenSet=%s, self.lazyFileOpen=%s', self.lazyFileOpenSet, self.lazyFileOpen)
        if self.lazyFileOpenSet:
            return self.lazyFileOpen
        return None

    def hasLazyFileOpen (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-lazyfileopen').debug3Func(): logFunc('called. self.lazyFileOpenSet=%s, self.lazyFileOpen=%s', self.lazyFileOpenSet, self.lazyFileOpen)
        if self.lazyFileOpenSet:
            return True
        return False

    def setLazyFileOpen (self, lazyFileOpen):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-lazyfileopen').debug3Func(): logFunc('called. lazyFileOpen=%s, old=%s', lazyFileOpen, self.lazyFileOpen)
        self.lazyFileOpenSet = True
        self.lazyFileOpen = lazyFileOpen

    def requestLogPeriodicStats (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-logperiodicstats').debug3Func(): logFunc('called. requested=%s', requested)
        self.logPeriodicStatsRequested = requested
        self.logPeriodicStatsSet = False

    def isLogPeriodicStatsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-logperiodicstats-requested').debug3Func(): logFunc('called. requested=%s', self.logPeriodicStatsRequested)
        return self.logPeriodicStatsRequested

    def getLogPeriodicStats (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-logperiodicstats').debug3Func(): logFunc('called. self.logPeriodicStatsSet=%s, self.logPeriodicStats=%s', self.logPeriodicStatsSet, self.logPeriodicStats)
        if self.logPeriodicStatsSet:
            return self.logPeriodicStats
        return None

    def hasLogPeriodicStats (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-logperiodicstats').debug3Func(): logFunc('called. self.logPeriodicStatsSet=%s, self.logPeriodicStats=%s', self.logPeriodicStatsSet, self.logPeriodicStats)
        if self.logPeriodicStatsSet:
            return True
        return False

    def setLogPeriodicStats (self, logPeriodicStats):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-logperiodicstats').debug3Func(): logFunc('called. logPeriodicStats=%s, old=%s', logPeriodicStats, self.logPeriodicStats)
        self.logPeriodicStatsSet = True
        self.logPeriodicStats = logPeriodicStats

    def requestMaxSessions (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxsessions').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxSessionsRequested = requested
        self.maxSessionsSet = False

    def isMaxSessionsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxsessions-requested').debug3Func(): logFunc('called. requested=%s', self.maxSessionsRequested)
        return self.maxSessionsRequested

    def getMaxSessions (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxsessions').debug3Func(): logFunc('called. self.maxSessionsSet=%s, self.maxSessions=%s', self.maxSessionsSet, self.maxSessions)
        if self.maxSessionsSet:
            return self.maxSessions
        return None

    def hasMaxSessions (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxsessions').debug3Func(): logFunc('called. self.maxSessionsSet=%s, self.maxSessions=%s', self.maxSessionsSet, self.maxSessions)
        if self.maxSessionsSet:
            return True
        return False

    def setMaxSessions (self, maxSessions):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxsessions').debug3Func(): logFunc('called. maxSessions=%s, old=%s', maxSessions, self.maxSessions)
        self.maxSessionsSet = True
        self.maxSessions = maxSessions

    def requestSessionQueueLowWaterMarkPercent (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-sessionqueuelowwatermarkpercent').debug3Func(): logFunc('called. requested=%s', requested)
        self.sessionQueueLowWaterMarkPercentRequested = requested
        self.sessionQueueLowWaterMarkPercentSet = False

    def isSessionQueueLowWaterMarkPercentRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-sessionqueuelowwatermarkpercent-requested').debug3Func(): logFunc('called. requested=%s', self.sessionQueueLowWaterMarkPercentRequested)
        return self.sessionQueueLowWaterMarkPercentRequested

    def getSessionQueueLowWaterMarkPercent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-sessionqueuelowwatermarkpercent').debug3Func(): logFunc('called. self.sessionQueueLowWaterMarkPercentSet=%s, self.sessionQueueLowWaterMarkPercent=%s', self.sessionQueueLowWaterMarkPercentSet, self.sessionQueueLowWaterMarkPercent)
        if self.sessionQueueLowWaterMarkPercentSet:
            return self.sessionQueueLowWaterMarkPercent
        return None

    def hasSessionQueueLowWaterMarkPercent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-sessionqueuelowwatermarkpercent').debug3Func(): logFunc('called. self.sessionQueueLowWaterMarkPercentSet=%s, self.sessionQueueLowWaterMarkPercent=%s', self.sessionQueueLowWaterMarkPercentSet, self.sessionQueueLowWaterMarkPercent)
        if self.sessionQueueLowWaterMarkPercentSet:
            return True
        return False

    def setSessionQueueLowWaterMarkPercent (self, sessionQueueLowWaterMarkPercent):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-sessionqueuelowwatermarkpercent').debug3Func(): logFunc('called. sessionQueueLowWaterMarkPercent=%s, old=%s', sessionQueueLowWaterMarkPercent, self.sessionQueueLowWaterMarkPercent)
        self.sessionQueueLowWaterMarkPercentSet = True
        self.sessionQueueLowWaterMarkPercent = sessionQueueLowWaterMarkPercent

    def requestMaxActiveSessions (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maxactivesessions').debug3Func(): logFunc('called. requested=%s', requested)
        self.maxActiveSessionsRequested = requested
        self.maxActiveSessionsSet = False

    def isMaxActiveSessionsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maxactivesessions-requested').debug3Func(): logFunc('called. requested=%s', self.maxActiveSessionsRequested)
        return self.maxActiveSessionsRequested

    def getMaxActiveSessions (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maxactivesessions').debug3Func(): logFunc('called. self.maxActiveSessionsSet=%s, self.maxActiveSessions=%s', self.maxActiveSessionsSet, self.maxActiveSessions)
        if self.maxActiveSessionsSet:
            return self.maxActiveSessions
        return None

    def hasMaxActiveSessions (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maxactivesessions').debug3Func(): logFunc('called. self.maxActiveSessionsSet=%s, self.maxActiveSessions=%s', self.maxActiveSessionsSet, self.maxActiveSessions)
        if self.maxActiveSessionsSet:
            return True
        return False

    def setMaxActiveSessions (self, maxActiveSessions):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maxactivesessions').debug3Func(): logFunc('called. maxActiveSessions=%s, old=%s', maxActiveSessions, self.maxActiveSessions)
        self.maxActiveSessionsSet = True
        self.maxActiveSessions = maxActiveSessions

    def requestAlgorithm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-algorithm').debug3Func(): logFunc('called. requested=%s', requested)
        self.algorithmRequested = requested
        self.algorithmSet = False

    def isAlgorithmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-algorithm-requested').debug3Func(): logFunc('called. requested=%s', self.algorithmRequested)
        return self.algorithmRequested

    def getAlgorithm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-algorithm').debug3Func(): logFunc('called. self.algorithmSet=%s, self.algorithm=%s', self.algorithmSet, self.algorithm)
        if self.algorithmSet:
            return self.algorithm
        return None

    def hasAlgorithm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-algorithm').debug3Func(): logFunc('called. self.algorithmSet=%s, self.algorithm=%s', self.algorithmSet, self.algorithm)
        if self.algorithmSet:
            return True
        return False

    def setAlgorithm (self, algorithm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-algorithm').debug3Func(): logFunc('called. algorithm=%s, old=%s', algorithm, self.algorithm)
        self.algorithmSet = True
        self.algorithm = algorithm


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.efficiencyAlgorithmObj:
            self.efficiencyAlgorithmObj._clearAllReadData()
        

        
        self.lazyFileOpen = 0
        self.lazyFileOpenSet = False
        
        self.logPeriodicStats = 0
        self.logPeriodicStatsSet = False
        
        self.maxSessions = 0
        self.maxSessionsSet = False
        
        self.sessionQueueLowWaterMarkPercent = 0
        self.sessionQueueLowWaterMarkPercentSet = False
        
        self.maxActiveSessions = 0
        self.maxActiveSessionsSet = False
        
        self.algorithm = 0
        self.algorithmSet = False
        

    def _getSelfKeyPath (self, line
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("acquisition", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("analyzer", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(line);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        line, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(line, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(line, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       line, 
                       
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

        keyPath = self._getSelfKeyPath(line, 
                                       
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
                               line, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.efficiencyAlgorithmObj:
            res = self.efficiencyAlgorithmObj._collectItemsToDelete(line, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-efficiency-algorithm-failed').errorFunc(): logFunc('efficiencyAlgorithmObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasLazyFileOpen():
            valLazyFileOpen = Value()
            if self.lazyFileOpen is not None:
                valLazyFileOpen.setBool(self.lazyFileOpen)
            else:
                valLazyFileOpen.setEmpty()
            tagValueList.push(("lazy-file-open", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valLazyFileOpen)
        
        if self.hasLogPeriodicStats():
            valLogPeriodicStats = Value()
            if self.logPeriodicStats is not None:
                valLogPeriodicStats.setBool(self.logPeriodicStats)
            else:
                valLogPeriodicStats.setEmpty()
            tagValueList.push(("log-periodic-stats", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valLogPeriodicStats)
        
        if self.hasMaxSessions():
            valMaxSessions = Value()
            if self.maxSessions is not None:
                valMaxSessions.setInt64(self.maxSessions)
            else:
                valMaxSessions.setEmpty()
            tagValueList.push(("max-sessions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMaxSessions)
        
        if self.hasSessionQueueLowWaterMarkPercent():
            valSessionQueueLowWaterMarkPercent = Value()
            if self.sessionQueueLowWaterMarkPercent is not None:
                valSessionQueueLowWaterMarkPercent.setInt64(self.sessionQueueLowWaterMarkPercent)
            else:
                valSessionQueueLowWaterMarkPercent.setEmpty()
            tagValueList.push(("session-queue-low-water-mark-percent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valSessionQueueLowWaterMarkPercent)
        
        if self.hasMaxActiveSessions():
            valMaxActiveSessions = Value()
            if self.maxActiveSessions is not None:
                valMaxActiveSessions.setInt64(self.maxActiveSessions)
            else:
                valMaxActiveSessions.setEmpty()
            tagValueList.push(("max-active-sessions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMaxActiveSessions)
        
        if self.hasAlgorithm():
            valAlgorithm = Value()
            if self.algorithm is not None:
                valAlgorithm.setEnum(self.algorithm.getValue())
            else:
                valAlgorithm.setEmpty()
            tagValueList.push(("algorithm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valAlgorithm)
        

        
        if self.efficiencyAlgorithmObj:
            valBegin = Value()
            (tag, ns, prefix) = ("efficiency-algorithm" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.efficiencyAlgorithmObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-efficiency-algorithm-failed').errorFunc(): logFunc('efficiencyAlgorithmObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isLazyFileOpenRequested():
            valLazyFileOpen = Value()
            valLazyFileOpen.setEmpty()
            tagValueList.push(("lazy-file-open", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valLazyFileOpen)
        
        if self.isLogPeriodicStatsRequested():
            valLogPeriodicStats = Value()
            valLogPeriodicStats.setEmpty()
            tagValueList.push(("log-periodic-stats", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valLogPeriodicStats)
        
        if self.isMaxSessionsRequested():
            valMaxSessions = Value()
            valMaxSessions.setEmpty()
            tagValueList.push(("max-sessions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMaxSessions)
        
        if self.isSessionQueueLowWaterMarkPercentRequested():
            valSessionQueueLowWaterMarkPercent = Value()
            valSessionQueueLowWaterMarkPercent.setEmpty()
            tagValueList.push(("session-queue-low-water-mark-percent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valSessionQueueLowWaterMarkPercent)
        
        if self.isMaxActiveSessionsRequested():
            valMaxActiveSessions = Value()
            valMaxActiveSessions.setEmpty()
            tagValueList.push(("max-active-sessions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMaxActiveSessions)
        
        if self.isAlgorithmRequested():
            valAlgorithm = Value()
            valAlgorithm.setEmpty()
            tagValueList.push(("algorithm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valAlgorithm)
        

        
        if self.efficiencyAlgorithmObj:
            valBegin = Value()
            (tag, ns, prefix) = ("efficiency-algorithm" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.efficiencyAlgorithmObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-efficiency-algorithm-failed').errorFunc(): logFunc('efficiencyAlgorithmObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isLazyFileOpenRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "lazy-file-open") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-lazyfileopen').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "lazyFileOpen", "lazy-file-open", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-lazy-file-open-bad-value').infoFunc(): logFunc('lazyFileOpen not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLazyFileOpen(tempVar)
            for logFunc in self._log('read-tag-values-lazy-file-open').debug3Func(): logFunc('read lazyFileOpen. lazyFileOpen=%s, tempValue=%s', self.lazyFileOpen, tempValue.getType())
        
        if self.isLogPeriodicStatsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "log-periodic-stats") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-logperiodicstats').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "logPeriodicStats", "log-periodic-stats", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-log-periodic-stats-bad-value').infoFunc(): logFunc('logPeriodicStats not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLogPeriodicStats(tempVar)
            for logFunc in self._log('read-tag-values-log-periodic-stats').debug3Func(): logFunc('read logPeriodicStats. logPeriodicStats=%s, tempValue=%s', self.logPeriodicStats, tempValue.getType())
        
        if self.isMaxSessionsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-sessions") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxsessions').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxSessions", "max-sessions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-sessions-bad-value').infoFunc(): logFunc('maxSessions not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxSessions(tempVar)
            for logFunc in self._log('read-tag-values-max-sessions').debug3Func(): logFunc('read maxSessions. maxSessions=%s, tempValue=%s', self.maxSessions, tempValue.getType())
        
        if self.isSessionQueueLowWaterMarkPercentRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "session-queue-low-water-mark-percent") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-sessionqueuelowwatermarkpercent').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "sessionQueueLowWaterMarkPercent", "session-queue-low-water-mark-percent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-session-queue-low-water-mark-percent-bad-value').infoFunc(): logFunc('sessionQueueLowWaterMarkPercent not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSessionQueueLowWaterMarkPercent(tempVar)
            for logFunc in self._log('read-tag-values-session-queue-low-water-mark-percent').debug3Func(): logFunc('read sessionQueueLowWaterMarkPercent. sessionQueueLowWaterMarkPercent=%s, tempValue=%s', self.sessionQueueLowWaterMarkPercent, tempValue.getType())
        
        if self.isMaxActiveSessionsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "max-active-sessions") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maxactivesessions').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maxActiveSessions", "max-active-sessions", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-max-active-sessions-bad-value').infoFunc(): logFunc('maxActiveSessions not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaxActiveSessions(tempVar)
            for logFunc in self._log('read-tag-values-max-active-sessions').debug3Func(): logFunc('read maxActiveSessions. maxActiveSessions=%s, tempValue=%s', self.maxActiveSessions, tempValue.getType())
        
        if self.isAlgorithmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "algorithm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-algorithm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "algorithm", "algorithm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-algorithm-bad-value').infoFunc(): logFunc('algorithm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAlgorithm(tempVar)
            for logFunc in self._log('read-tag-values-algorithm').debug3Func(): logFunc('read algorithm. algorithm=%s, tempValue=%s', self.algorithm, tempValue.getType())
        

        
        if self.efficiencyAlgorithmObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "efficiency-algorithm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "efficiency-algorithm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.efficiencyAlgorithmObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-efficiency-algorithm-failed').errorFunc(): logFunc('efficiencyAlgorithmObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "efficiency-algorithm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "efficiency-algorithm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "controller", 
        "namespace": "controller", 
        "className": "ControllerMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.acquisition.controller.controller_maapi_gen import ControllerMaapi", 
        "baseClassName": "ControllerMaapiBase", 
        "baseModule": "controller_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": false, 
            "yangName": "line", 
            "namespace": "line", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "line", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "analyzer", 
            "namespace": "analyzer", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "analyzer"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "acquisition", 
            "namespace": "acquisition", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "acquisition"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "controller", 
            "namespace": "controller", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "controller"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "efficiencyAlgorithm", 
            "yangName": "efficiency-algorithm", 
            "className": "BlinkyEfficiencyAlgorithmMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.acquisition.controller.efficiency_algorithm.efficiency_algorithm_maapi_gen import BlinkyEfficiencyAlgorithmMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "lazyFileOpen", 
            "yangName": "lazy-file-open", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "logPeriodicStats", 
            "yangName": "log-periodic-stats", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessions", 
            "yangName": "max-sessions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "sessionQueueLowWaterMarkPercent", 
            "yangName": "session-queue-low-water-mark-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxActiveSessions", 
            "yangName": "max-active-sessions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "algorithm", 
            "yangName": "algorithm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "lazyFileOpen", 
            "yangName": "lazy-file-open", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "logPeriodicStats", 
            "yangName": "log-periodic-stats", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessions", 
            "yangName": "max-sessions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "sessionQueueLowWaterMarkPercent", 
            "yangName": "session-queue-low-water-mark-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxActiveSessions", 
            "yangName": "max-active-sessions", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "algorithm", 
            "yangName": "algorithm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


