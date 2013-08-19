


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

from summary_maapi_base_gen import SummaryMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType


class BlinkySummaryMaapi(SummaryMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-summary")
        self.domain = None

        

        
        self.errorCountRequested = False
        self.errorCount = None
        self.errorCountSet = False
        
        self.emergencyCountRequested = False
        self.emergencyCount = None
        self.emergencyCountSet = False
        
        self.highestSeverityRequested = False
        self.highestSeverity = None
        self.highestSeveritySet = False
        
        self.criticalCountRequested = False
        self.criticalCount = None
        self.criticalCountSet = False
        
        self.warningCountRequested = False
        self.warningCount = None
        self.warningCountSet = False
        
        self.alertCountRequested = False
        self.alertCount = None
        self.alertCountSet = False
        
        self.noticeCountRequested = False
        self.noticeCount = None
        self.noticeCountSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestErrorCount(True)
        
        self.requestEmergencyCount(True)
        
        self.requestHighestSeverity(True)
        
        self.requestCriticalCount(True)
        
        self.requestWarningCount(True)
        
        self.requestAlertCount(True)
        
        self.requestNoticeCount(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestErrorCount(False)
        
        self.requestEmergencyCount(False)
        
        self.requestHighestSeverity(False)
        
        self.requestCriticalCount(False)
        
        self.requestWarningCount(False)
        
        self.requestAlertCount(False)
        
        self.requestNoticeCount(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestErrorCount(True)
        
        self.requestEmergencyCount(True)
        
        self.requestHighestSeverity(True)
        
        self.requestCriticalCount(True)
        
        self.requestWarningCount(True)
        
        self.requestAlertCount(True)
        
        self.requestNoticeCount(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestErrorCount(False)
        
        self.requestEmergencyCount(False)
        
        self.requestHighestSeverity(False)
        
        self.requestCriticalCount(False)
        
        self.requestWarningCount(False)
        
        self.requestAlertCount(False)
        
        self.requestNoticeCount(False)
        
        

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



    def requestErrorCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-errorcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.errorCountRequested = requested
        self.errorCountSet = False

    def isErrorCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-errorcount-requested').debug3Func(): logFunc('called. requested=%s', self.errorCountRequested)
        return self.errorCountRequested

    def getErrorCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-errorcount').debug3Func(): logFunc('called. self.errorCountSet=%s, self.errorCount=%s', self.errorCountSet, self.errorCount)
        if self.errorCountSet:
            return self.errorCount
        return None

    def hasErrorCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-errorcount').debug3Func(): logFunc('called. self.errorCountSet=%s, self.errorCount=%s', self.errorCountSet, self.errorCount)
        if self.errorCountSet:
            return True
        return False

    def setErrorCount (self, errorCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-errorcount').debug3Func(): logFunc('called. errorCount=%s, old=%s', errorCount, self.errorCount)
        self.errorCountSet = True
        self.errorCount = errorCount

    def requestEmergencyCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-emergencycount').debug3Func(): logFunc('called. requested=%s', requested)
        self.emergencyCountRequested = requested
        self.emergencyCountSet = False

    def isEmergencyCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-emergencycount-requested').debug3Func(): logFunc('called. requested=%s', self.emergencyCountRequested)
        return self.emergencyCountRequested

    def getEmergencyCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-emergencycount').debug3Func(): logFunc('called. self.emergencyCountSet=%s, self.emergencyCount=%s', self.emergencyCountSet, self.emergencyCount)
        if self.emergencyCountSet:
            return self.emergencyCount
        return None

    def hasEmergencyCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-emergencycount').debug3Func(): logFunc('called. self.emergencyCountSet=%s, self.emergencyCount=%s', self.emergencyCountSet, self.emergencyCount)
        if self.emergencyCountSet:
            return True
        return False

    def setEmergencyCount (self, emergencyCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-emergencycount').debug3Func(): logFunc('called. emergencyCount=%s, old=%s', emergencyCount, self.emergencyCount)
        self.emergencyCountSet = True
        self.emergencyCount = emergencyCount

    def requestHighestSeverity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-highestseverity').debug3Func(): logFunc('called. requested=%s', requested)
        self.highestSeverityRequested = requested
        self.highestSeveritySet = False

    def isHighestSeverityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-highestseverity-requested').debug3Func(): logFunc('called. requested=%s', self.highestSeverityRequested)
        return self.highestSeverityRequested

    def getHighestSeverity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-highestseverity').debug3Func(): logFunc('called. self.highestSeveritySet=%s, self.highestSeverity=%s', self.highestSeveritySet, self.highestSeverity)
        if self.highestSeveritySet:
            return self.highestSeverity
        return None

    def hasHighestSeverity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-highestseverity').debug3Func(): logFunc('called. self.highestSeveritySet=%s, self.highestSeverity=%s', self.highestSeveritySet, self.highestSeverity)
        if self.highestSeveritySet:
            return True
        return False

    def setHighestSeverity (self, highestSeverity):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-highestseverity').debug3Func(): logFunc('called. highestSeverity=%s, old=%s', highestSeverity, self.highestSeverity)
        self.highestSeveritySet = True
        self.highestSeverity = highestSeverity

    def requestCriticalCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-criticalcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.criticalCountRequested = requested
        self.criticalCountSet = False

    def isCriticalCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-criticalcount-requested').debug3Func(): logFunc('called. requested=%s', self.criticalCountRequested)
        return self.criticalCountRequested

    def getCriticalCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-criticalcount').debug3Func(): logFunc('called. self.criticalCountSet=%s, self.criticalCount=%s', self.criticalCountSet, self.criticalCount)
        if self.criticalCountSet:
            return self.criticalCount
        return None

    def hasCriticalCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-criticalcount').debug3Func(): logFunc('called. self.criticalCountSet=%s, self.criticalCount=%s', self.criticalCountSet, self.criticalCount)
        if self.criticalCountSet:
            return True
        return False

    def setCriticalCount (self, criticalCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-criticalcount').debug3Func(): logFunc('called. criticalCount=%s, old=%s', criticalCount, self.criticalCount)
        self.criticalCountSet = True
        self.criticalCount = criticalCount

    def requestWarningCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-warningcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.warningCountRequested = requested
        self.warningCountSet = False

    def isWarningCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-warningcount-requested').debug3Func(): logFunc('called. requested=%s', self.warningCountRequested)
        return self.warningCountRequested

    def getWarningCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-warningcount').debug3Func(): logFunc('called. self.warningCountSet=%s, self.warningCount=%s', self.warningCountSet, self.warningCount)
        if self.warningCountSet:
            return self.warningCount
        return None

    def hasWarningCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-warningcount').debug3Func(): logFunc('called. self.warningCountSet=%s, self.warningCount=%s', self.warningCountSet, self.warningCount)
        if self.warningCountSet:
            return True
        return False

    def setWarningCount (self, warningCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-warningcount').debug3Func(): logFunc('called. warningCount=%s, old=%s', warningCount, self.warningCount)
        self.warningCountSet = True
        self.warningCount = warningCount

    def requestAlertCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-alertcount').debug3Func(): logFunc('called. requested=%s', requested)
        self.alertCountRequested = requested
        self.alertCountSet = False

    def isAlertCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-alertcount-requested').debug3Func(): logFunc('called. requested=%s', self.alertCountRequested)
        return self.alertCountRequested

    def getAlertCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-alertcount').debug3Func(): logFunc('called. self.alertCountSet=%s, self.alertCount=%s', self.alertCountSet, self.alertCount)
        if self.alertCountSet:
            return self.alertCount
        return None

    def hasAlertCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-alertcount').debug3Func(): logFunc('called. self.alertCountSet=%s, self.alertCount=%s', self.alertCountSet, self.alertCount)
        if self.alertCountSet:
            return True
        return False

    def setAlertCount (self, alertCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-alertcount').debug3Func(): logFunc('called. alertCount=%s, old=%s', alertCount, self.alertCount)
        self.alertCountSet = True
        self.alertCount = alertCount

    def requestNoticeCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-noticecount').debug3Func(): logFunc('called. requested=%s', requested)
        self.noticeCountRequested = requested
        self.noticeCountSet = False

    def isNoticeCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-noticecount-requested').debug3Func(): logFunc('called. requested=%s', self.noticeCountRequested)
        return self.noticeCountRequested

    def getNoticeCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-noticecount').debug3Func(): logFunc('called. self.noticeCountSet=%s, self.noticeCount=%s', self.noticeCountSet, self.noticeCount)
        if self.noticeCountSet:
            return self.noticeCount
        return None

    def hasNoticeCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-noticecount').debug3Func(): logFunc('called. self.noticeCountSet=%s, self.noticeCount=%s', self.noticeCountSet, self.noticeCount)
        if self.noticeCountSet:
            return True
        return False

    def setNoticeCount (self, noticeCount):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-noticecount').debug3Func(): logFunc('called. noticeCount=%s, old=%s', noticeCount, self.noticeCount)
        self.noticeCountSet = True
        self.noticeCount = noticeCount


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.errorCount = 0
        self.errorCountSet = False
        
        self.emergencyCount = 0
        self.emergencyCountSet = False
        
        self.highestSeverity = 0
        self.highestSeveritySet = False
        
        self.criticalCount = 0
        self.criticalCountSet = False
        
        self.warningCount = 0
        self.warningCountSet = False
        
        self.alertCount = 0
        self.alertCountSet = False
        
        self.noticeCount = 0
        self.noticeCountSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("summary", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
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

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isErrorCountRequested():
            valErrorCount = Value()
            valErrorCount.setEmpty()
            tagValueList.push(("error-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valErrorCount)
        
        if self.isEmergencyCountRequested():
            valEmergencyCount = Value()
            valEmergencyCount.setEmpty()
            tagValueList.push(("emergency-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valEmergencyCount)
        
        if self.isHighestSeverityRequested():
            valHighestSeverity = Value()
            valHighestSeverity.setEmpty()
            tagValueList.push(("highest-severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valHighestSeverity)
        
        if self.isCriticalCountRequested():
            valCriticalCount = Value()
            valCriticalCount.setEmpty()
            tagValueList.push(("critical-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valCriticalCount)
        
        if self.isWarningCountRequested():
            valWarningCount = Value()
            valWarningCount.setEmpty()
            tagValueList.push(("warning-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valWarningCount)
        
        if self.isAlertCountRequested():
            valAlertCount = Value()
            valAlertCount.setEmpty()
            tagValueList.push(("alert-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valAlertCount)
        
        if self.isNoticeCountRequested():
            valNoticeCount = Value()
            valNoticeCount.setEmpty()
            tagValueList.push(("notice-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valNoticeCount)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isErrorCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "error-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-errorcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "errorCount", "error-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-error-count-bad-value').infoFunc(): logFunc('errorCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setErrorCount(tempVar)
            for logFunc in self._log('read-tag-values-error-count').debug3Func(): logFunc('read errorCount. errorCount=%s, tempValue=%s', self.errorCount, tempValue.getType())
        
        if self.isEmergencyCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "emergency-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-emergencycount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "emergencyCount", "emergency-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-emergency-count-bad-value').infoFunc(): logFunc('emergencyCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEmergencyCount(tempVar)
            for logFunc in self._log('read-tag-values-emergency-count').debug3Func(): logFunc('read emergencyCount. emergencyCount=%s, tempValue=%s', self.emergencyCount, tempValue.getType())
        
        if self.isHighestSeverityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "highest-severity") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-highestseverity').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "highestSeverity", "highest-severity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-highest-severity-bad-value').infoFunc(): logFunc('highestSeverity not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHighestSeverity(tempVar)
            for logFunc in self._log('read-tag-values-highest-severity').debug3Func(): logFunc('read highestSeverity. highestSeverity=%s, tempValue=%s', self.highestSeverity, tempValue.getType())
        
        if self.isCriticalCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "critical-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-criticalcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "criticalCount", "critical-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-critical-count-bad-value').infoFunc(): logFunc('criticalCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCriticalCount(tempVar)
            for logFunc in self._log('read-tag-values-critical-count').debug3Func(): logFunc('read criticalCount. criticalCount=%s, tempValue=%s', self.criticalCount, tempValue.getType())
        
        if self.isWarningCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "warning-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-warningcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "warningCount", "warning-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-warning-count-bad-value').infoFunc(): logFunc('warningCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setWarningCount(tempVar)
            for logFunc in self._log('read-tag-values-warning-count').debug3Func(): logFunc('read warningCount. warningCount=%s, tempValue=%s', self.warningCount, tempValue.getType())
        
        if self.isAlertCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "alert-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-alertcount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "alertCount", "alert-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-alert-count-bad-value').infoFunc(): logFunc('alertCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAlertCount(tempVar)
            for logFunc in self._log('read-tag-values-alert-count').debug3Func(): logFunc('read alertCount. alertCount=%s, tempValue=%s', self.alertCount, tempValue.getType())
        
        if self.isNoticeCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "notice-count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-noticecount').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "noticeCount", "notice-count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-notice-count-bad-value').infoFunc(): logFunc('noticeCount not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNoticeCount(tempVar)
            for logFunc in self._log('read-tag-values-notice-count').debug3Func(): logFunc('read noticeCount. noticeCount=%s, tempValue=%s', self.noticeCount, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "summary", 
        "namespace": "summary", 
        "className": "SummaryMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.summary.summary_maapi_gen import SummaryMaapi", 
        "baseClassName": "SummaryMaapiBase", 
        "baseModule": "summary_maapi_base_gen"
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
            "yangName": "summary", 
            "namespace": "summary", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "summary"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "errorCount", 
            "yangName": "error-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "emergencyCount", 
            "yangName": "emergency-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "highestSeverity", 
            "yangName": "highest-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "criticalCount", 
            "yangName": "critical-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warningCount", 
            "yangName": "warning-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "alertCount", 
            "yangName": "alert-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "noticeCount", 
            "yangName": "notice-count", 
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
            "common", 
            "qwilt_tech_system_alarms"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "errorCount", 
            "yangName": "error-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "emergencyCount", 
            "yangName": "emergency-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "highestSeverity", 
            "yangName": "highest-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "criticalCount", 
            "yangName": "critical-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warningCount", 
            "yangName": "warning-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "alertCount", 
            "yangName": "alert-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "noticeCount", 
            "yangName": "notice-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


