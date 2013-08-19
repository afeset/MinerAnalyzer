


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

        

        
        self.fileArchiveDurationWarningSecondsRequested = False
        self.fileArchiveDurationWarningSeconds = None
        self.fileArchiveDurationWarningSecondsSet = False
        
        self.pendingFileCountWarningRequested = False
        self.pendingFileCountWarning = None
        self.pendingFileCountWarningSet = False
        
        self.overallArchiveDurationWarningSecondsRequested = False
        self.overallArchiveDurationWarningSeconds = None
        self.overallArchiveDurationWarningSecondsSet = False
        
        self.pendingFileCountErrorRequested = False
        self.pendingFileCountError = None
        self.pendingFileCountErrorSet = False
        
        self.fileArchiveDurationErrorSecondsRequested = False
        self.fileArchiveDurationErrorSeconds = None
        self.fileArchiveDurationErrorSecondsSet = False
        
        self.overallArchiveDurationErrorSecondsRequested = False
        self.overallArchiveDurationErrorSeconds = None
        self.overallArchiveDurationErrorSecondsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestFileArchiveDurationWarningSeconds(True)
        
        self.requestPendingFileCountWarning(True)
        
        self.requestOverallArchiveDurationWarningSeconds(True)
        
        self.requestPendingFileCountError(True)
        
        self.requestFileArchiveDurationErrorSeconds(True)
        
        self.requestOverallArchiveDurationErrorSeconds(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestFileArchiveDurationWarningSeconds(True)
        
        self.requestPendingFileCountWarning(True)
        
        self.requestOverallArchiveDurationWarningSeconds(True)
        
        self.requestPendingFileCountError(True)
        
        self.requestFileArchiveDurationErrorSeconds(True)
        
        self.requestOverallArchiveDurationErrorSeconds(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestFileArchiveDurationWarningSeconds(False)
        
        self.requestPendingFileCountWarning(False)
        
        self.requestOverallArchiveDurationWarningSeconds(False)
        
        self.requestPendingFileCountError(False)
        
        self.requestFileArchiveDurationErrorSeconds(False)
        
        self.requestOverallArchiveDurationErrorSeconds(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestFileArchiveDurationWarningSeconds(False)
        
        self.requestPendingFileCountWarning(False)
        
        self.requestOverallArchiveDurationWarningSeconds(False)
        
        self.requestPendingFileCountError(False)
        
        self.requestFileArchiveDurationErrorSeconds(False)
        
        self.requestOverallArchiveDurationErrorSeconds(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setFileArchiveDurationWarningSeconds(None)
        self.fileArchiveDurationWarningSecondsSet = False
        
        self.setPendingFileCountWarning(None)
        self.pendingFileCountWarningSet = False
        
        self.setOverallArchiveDurationWarningSeconds(None)
        self.overallArchiveDurationWarningSecondsSet = False
        
        self.setPendingFileCountError(None)
        self.pendingFileCountErrorSet = False
        
        self.setFileArchiveDurationErrorSeconds(None)
        self.fileArchiveDurationErrorSecondsSet = False
        
        self.setOverallArchiveDurationErrorSeconds(None)
        self.overallArchiveDurationErrorSecondsSet = False
        
        

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



    def requestFileArchiveDurationWarningSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-filearchivedurationwarningseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileArchiveDurationWarningSecondsRequested = requested
        self.fileArchiveDurationWarningSecondsSet = False

    def isFileArchiveDurationWarningSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-filearchivedurationwarningseconds-requested').debug3Func(): logFunc('called. requested=%s', self.fileArchiveDurationWarningSecondsRequested)
        return self.fileArchiveDurationWarningSecondsRequested

    def getFileArchiveDurationWarningSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-filearchivedurationwarningseconds').debug3Func(): logFunc('called. self.fileArchiveDurationWarningSecondsSet=%s, self.fileArchiveDurationWarningSeconds=%s', self.fileArchiveDurationWarningSecondsSet, self.fileArchiveDurationWarningSeconds)
        if self.fileArchiveDurationWarningSecondsSet:
            return self.fileArchiveDurationWarningSeconds
        return None

    def hasFileArchiveDurationWarningSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-filearchivedurationwarningseconds').debug3Func(): logFunc('called. self.fileArchiveDurationWarningSecondsSet=%s, self.fileArchiveDurationWarningSeconds=%s', self.fileArchiveDurationWarningSecondsSet, self.fileArchiveDurationWarningSeconds)
        if self.fileArchiveDurationWarningSecondsSet:
            return True
        return False

    def setFileArchiveDurationWarningSeconds (self, fileArchiveDurationWarningSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-filearchivedurationwarningseconds').debug3Func(): logFunc('called. fileArchiveDurationWarningSeconds=%s, old=%s', fileArchiveDurationWarningSeconds, self.fileArchiveDurationWarningSeconds)
        self.fileArchiveDurationWarningSecondsSet = True
        self.fileArchiveDurationWarningSeconds = fileArchiveDurationWarningSeconds

    def requestPendingFileCountWarning (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pendingfilecountwarning').debug3Func(): logFunc('called. requested=%s', requested)
        self.pendingFileCountWarningRequested = requested
        self.pendingFileCountWarningSet = False

    def isPendingFileCountWarningRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pendingfilecountwarning-requested').debug3Func(): logFunc('called. requested=%s', self.pendingFileCountWarningRequested)
        return self.pendingFileCountWarningRequested

    def getPendingFileCountWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pendingfilecountwarning').debug3Func(): logFunc('called. self.pendingFileCountWarningSet=%s, self.pendingFileCountWarning=%s', self.pendingFileCountWarningSet, self.pendingFileCountWarning)
        if self.pendingFileCountWarningSet:
            return self.pendingFileCountWarning
        return None

    def hasPendingFileCountWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pendingfilecountwarning').debug3Func(): logFunc('called. self.pendingFileCountWarningSet=%s, self.pendingFileCountWarning=%s', self.pendingFileCountWarningSet, self.pendingFileCountWarning)
        if self.pendingFileCountWarningSet:
            return True
        return False

    def setPendingFileCountWarning (self, pendingFileCountWarning):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pendingfilecountwarning').debug3Func(): logFunc('called. pendingFileCountWarning=%s, old=%s', pendingFileCountWarning, self.pendingFileCountWarning)
        self.pendingFileCountWarningSet = True
        self.pendingFileCountWarning = pendingFileCountWarning

    def requestOverallArchiveDurationWarningSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-overallarchivedurationwarningseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.overallArchiveDurationWarningSecondsRequested = requested
        self.overallArchiveDurationWarningSecondsSet = False

    def isOverallArchiveDurationWarningSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-overallarchivedurationwarningseconds-requested').debug3Func(): logFunc('called. requested=%s', self.overallArchiveDurationWarningSecondsRequested)
        return self.overallArchiveDurationWarningSecondsRequested

    def getOverallArchiveDurationWarningSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-overallarchivedurationwarningseconds').debug3Func(): logFunc('called. self.overallArchiveDurationWarningSecondsSet=%s, self.overallArchiveDurationWarningSeconds=%s', self.overallArchiveDurationWarningSecondsSet, self.overallArchiveDurationWarningSeconds)
        if self.overallArchiveDurationWarningSecondsSet:
            return self.overallArchiveDurationWarningSeconds
        return None

    def hasOverallArchiveDurationWarningSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-overallarchivedurationwarningseconds').debug3Func(): logFunc('called. self.overallArchiveDurationWarningSecondsSet=%s, self.overallArchiveDurationWarningSeconds=%s', self.overallArchiveDurationWarningSecondsSet, self.overallArchiveDurationWarningSeconds)
        if self.overallArchiveDurationWarningSecondsSet:
            return True
        return False

    def setOverallArchiveDurationWarningSeconds (self, overallArchiveDurationWarningSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-overallarchivedurationwarningseconds').debug3Func(): logFunc('called. overallArchiveDurationWarningSeconds=%s, old=%s', overallArchiveDurationWarningSeconds, self.overallArchiveDurationWarningSeconds)
        self.overallArchiveDurationWarningSecondsSet = True
        self.overallArchiveDurationWarningSeconds = overallArchiveDurationWarningSeconds

    def requestPendingFileCountError (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pendingfilecounterror').debug3Func(): logFunc('called. requested=%s', requested)
        self.pendingFileCountErrorRequested = requested
        self.pendingFileCountErrorSet = False

    def isPendingFileCountErrorRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pendingfilecounterror-requested').debug3Func(): logFunc('called. requested=%s', self.pendingFileCountErrorRequested)
        return self.pendingFileCountErrorRequested

    def getPendingFileCountError (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pendingfilecounterror').debug3Func(): logFunc('called. self.pendingFileCountErrorSet=%s, self.pendingFileCountError=%s', self.pendingFileCountErrorSet, self.pendingFileCountError)
        if self.pendingFileCountErrorSet:
            return self.pendingFileCountError
        return None

    def hasPendingFileCountError (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pendingfilecounterror').debug3Func(): logFunc('called. self.pendingFileCountErrorSet=%s, self.pendingFileCountError=%s', self.pendingFileCountErrorSet, self.pendingFileCountError)
        if self.pendingFileCountErrorSet:
            return True
        return False

    def setPendingFileCountError (self, pendingFileCountError):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pendingfilecounterror').debug3Func(): logFunc('called. pendingFileCountError=%s, old=%s', pendingFileCountError, self.pendingFileCountError)
        self.pendingFileCountErrorSet = True
        self.pendingFileCountError = pendingFileCountError

    def requestFileArchiveDurationErrorSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-filearchivedurationerrorseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.fileArchiveDurationErrorSecondsRequested = requested
        self.fileArchiveDurationErrorSecondsSet = False

    def isFileArchiveDurationErrorSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-filearchivedurationerrorseconds-requested').debug3Func(): logFunc('called. requested=%s', self.fileArchiveDurationErrorSecondsRequested)
        return self.fileArchiveDurationErrorSecondsRequested

    def getFileArchiveDurationErrorSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-filearchivedurationerrorseconds').debug3Func(): logFunc('called. self.fileArchiveDurationErrorSecondsSet=%s, self.fileArchiveDurationErrorSeconds=%s', self.fileArchiveDurationErrorSecondsSet, self.fileArchiveDurationErrorSeconds)
        if self.fileArchiveDurationErrorSecondsSet:
            return self.fileArchiveDurationErrorSeconds
        return None

    def hasFileArchiveDurationErrorSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-filearchivedurationerrorseconds').debug3Func(): logFunc('called. self.fileArchiveDurationErrorSecondsSet=%s, self.fileArchiveDurationErrorSeconds=%s', self.fileArchiveDurationErrorSecondsSet, self.fileArchiveDurationErrorSeconds)
        if self.fileArchiveDurationErrorSecondsSet:
            return True
        return False

    def setFileArchiveDurationErrorSeconds (self, fileArchiveDurationErrorSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-filearchivedurationerrorseconds').debug3Func(): logFunc('called. fileArchiveDurationErrorSeconds=%s, old=%s', fileArchiveDurationErrorSeconds, self.fileArchiveDurationErrorSeconds)
        self.fileArchiveDurationErrorSecondsSet = True
        self.fileArchiveDurationErrorSeconds = fileArchiveDurationErrorSeconds

    def requestOverallArchiveDurationErrorSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-overallarchivedurationerrorseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.overallArchiveDurationErrorSecondsRequested = requested
        self.overallArchiveDurationErrorSecondsSet = False

    def isOverallArchiveDurationErrorSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-overallarchivedurationerrorseconds-requested').debug3Func(): logFunc('called. requested=%s', self.overallArchiveDurationErrorSecondsRequested)
        return self.overallArchiveDurationErrorSecondsRequested

    def getOverallArchiveDurationErrorSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-overallarchivedurationerrorseconds').debug3Func(): logFunc('called. self.overallArchiveDurationErrorSecondsSet=%s, self.overallArchiveDurationErrorSeconds=%s', self.overallArchiveDurationErrorSecondsSet, self.overallArchiveDurationErrorSeconds)
        if self.overallArchiveDurationErrorSecondsSet:
            return self.overallArchiveDurationErrorSeconds
        return None

    def hasOverallArchiveDurationErrorSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-overallarchivedurationerrorseconds').debug3Func(): logFunc('called. self.overallArchiveDurationErrorSecondsSet=%s, self.overallArchiveDurationErrorSeconds=%s', self.overallArchiveDurationErrorSecondsSet, self.overallArchiveDurationErrorSeconds)
        if self.overallArchiveDurationErrorSecondsSet:
            return True
        return False

    def setOverallArchiveDurationErrorSeconds (self, overallArchiveDurationErrorSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-overallarchivedurationerrorseconds').debug3Func(): logFunc('called. overallArchiveDurationErrorSeconds=%s, old=%s', overallArchiveDurationErrorSeconds, self.overallArchiveDurationErrorSeconds)
        self.overallArchiveDurationErrorSecondsSet = True
        self.overallArchiveDurationErrorSeconds = overallArchiveDurationErrorSeconds


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.fileArchiveDurationWarningSeconds = 0
        self.fileArchiveDurationWarningSecondsSet = False
        
        self.pendingFileCountWarning = 0
        self.pendingFileCountWarningSet = False
        
        self.overallArchiveDurationWarningSeconds = 0
        self.overallArchiveDurationWarningSecondsSet = False
        
        self.pendingFileCountError = 0
        self.pendingFileCountErrorSet = False
        
        self.fileArchiveDurationErrorSeconds = 0
        self.fileArchiveDurationErrorSecondsSet = False
        
        self.overallArchiveDurationErrorSeconds = 0
        self.overallArchiveDurationErrorSecondsSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("log-archiving", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("housekeeper", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
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

        
        if self.hasFileArchiveDurationWarningSeconds():
            valFileArchiveDurationWarningSeconds = Value()
            if self.fileArchiveDurationWarningSeconds is not None:
                valFileArchiveDurationWarningSeconds.setInt64(self.fileArchiveDurationWarningSeconds)
            else:
                valFileArchiveDurationWarningSeconds.setEmpty()
            tagValueList.push(("file-archive-duration-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valFileArchiveDurationWarningSeconds)
        
        if self.hasPendingFileCountWarning():
            valPendingFileCountWarning = Value()
            if self.pendingFileCountWarning is not None:
                valPendingFileCountWarning.setInt64(self.pendingFileCountWarning)
            else:
                valPendingFileCountWarning.setEmpty()
            tagValueList.push(("pending-file-count-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPendingFileCountWarning)
        
        if self.hasOverallArchiveDurationWarningSeconds():
            valOverallArchiveDurationWarningSeconds = Value()
            if self.overallArchiveDurationWarningSeconds is not None:
                valOverallArchiveDurationWarningSeconds.setInt64(self.overallArchiveDurationWarningSeconds)
            else:
                valOverallArchiveDurationWarningSeconds.setEmpty()
            tagValueList.push(("overall-archive-duration-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valOverallArchiveDurationWarningSeconds)
        
        if self.hasPendingFileCountError():
            valPendingFileCountError = Value()
            if self.pendingFileCountError is not None:
                valPendingFileCountError.setInt64(self.pendingFileCountError)
            else:
                valPendingFileCountError.setEmpty()
            tagValueList.push(("pending-file-count-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPendingFileCountError)
        
        if self.hasFileArchiveDurationErrorSeconds():
            valFileArchiveDurationErrorSeconds = Value()
            if self.fileArchiveDurationErrorSeconds is not None:
                valFileArchiveDurationErrorSeconds.setInt64(self.fileArchiveDurationErrorSeconds)
            else:
                valFileArchiveDurationErrorSeconds.setEmpty()
            tagValueList.push(("file-archive-duration-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valFileArchiveDurationErrorSeconds)
        
        if self.hasOverallArchiveDurationErrorSeconds():
            valOverallArchiveDurationErrorSeconds = Value()
            if self.overallArchiveDurationErrorSeconds is not None:
                valOverallArchiveDurationErrorSeconds.setInt64(self.overallArchiveDurationErrorSeconds)
            else:
                valOverallArchiveDurationErrorSeconds.setEmpty()
            tagValueList.push(("overall-archive-duration-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valOverallArchiveDurationErrorSeconds)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isFileArchiveDurationWarningSecondsRequested():
            valFileArchiveDurationWarningSeconds = Value()
            valFileArchiveDurationWarningSeconds.setEmpty()
            tagValueList.push(("file-archive-duration-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valFileArchiveDurationWarningSeconds)
        
        if self.isPendingFileCountWarningRequested():
            valPendingFileCountWarning = Value()
            valPendingFileCountWarning.setEmpty()
            tagValueList.push(("pending-file-count-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPendingFileCountWarning)
        
        if self.isOverallArchiveDurationWarningSecondsRequested():
            valOverallArchiveDurationWarningSeconds = Value()
            valOverallArchiveDurationWarningSeconds.setEmpty()
            tagValueList.push(("overall-archive-duration-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valOverallArchiveDurationWarningSeconds)
        
        if self.isPendingFileCountErrorRequested():
            valPendingFileCountError = Value()
            valPendingFileCountError.setEmpty()
            tagValueList.push(("pending-file-count-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPendingFileCountError)
        
        if self.isFileArchiveDurationErrorSecondsRequested():
            valFileArchiveDurationErrorSeconds = Value()
            valFileArchiveDurationErrorSeconds.setEmpty()
            tagValueList.push(("file-archive-duration-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valFileArchiveDurationErrorSeconds)
        
        if self.isOverallArchiveDurationErrorSecondsRequested():
            valOverallArchiveDurationErrorSeconds = Value()
            valOverallArchiveDurationErrorSeconds.setEmpty()
            tagValueList.push(("overall-archive-duration-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valOverallArchiveDurationErrorSeconds)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isFileArchiveDurationWarningSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file-archive-duration-warning-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-filearchivedurationwarningseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fileArchiveDurationWarningSeconds", "file-archive-duration-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-archive-duration-warning-seconds-bad-value').infoFunc(): logFunc('fileArchiveDurationWarningSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFileArchiveDurationWarningSeconds(tempVar)
            for logFunc in self._log('read-tag-values-file-archive-duration-warning-seconds').debug3Func(): logFunc('read fileArchiveDurationWarningSeconds. fileArchiveDurationWarningSeconds=%s, tempValue=%s', self.fileArchiveDurationWarningSeconds, tempValue.getType())
        
        if self.isPendingFileCountWarningRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pending-file-count-warning") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pendingfilecountwarning').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pendingFileCountWarning", "pending-file-count-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pending-file-count-warning-bad-value').infoFunc(): logFunc('pendingFileCountWarning not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPendingFileCountWarning(tempVar)
            for logFunc in self._log('read-tag-values-pending-file-count-warning').debug3Func(): logFunc('read pendingFileCountWarning. pendingFileCountWarning=%s, tempValue=%s', self.pendingFileCountWarning, tempValue.getType())
        
        if self.isOverallArchiveDurationWarningSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "overall-archive-duration-warning-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-overallarchivedurationwarningseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "overallArchiveDurationWarningSeconds", "overall-archive-duration-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-overall-archive-duration-warning-seconds-bad-value').infoFunc(): logFunc('overallArchiveDurationWarningSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOverallArchiveDurationWarningSeconds(tempVar)
            for logFunc in self._log('read-tag-values-overall-archive-duration-warning-seconds').debug3Func(): logFunc('read overallArchiveDurationWarningSeconds. overallArchiveDurationWarningSeconds=%s, tempValue=%s', self.overallArchiveDurationWarningSeconds, tempValue.getType())
        
        if self.isPendingFileCountErrorRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pending-file-count-error") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pendingfilecounterror').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pendingFileCountError", "pending-file-count-error", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pending-file-count-error-bad-value').infoFunc(): logFunc('pendingFileCountError not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPendingFileCountError(tempVar)
            for logFunc in self._log('read-tag-values-pending-file-count-error').debug3Func(): logFunc('read pendingFileCountError. pendingFileCountError=%s, tempValue=%s', self.pendingFileCountError, tempValue.getType())
        
        if self.isFileArchiveDurationErrorSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "file-archive-duration-error-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-filearchivedurationerrorseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "fileArchiveDurationErrorSeconds", "file-archive-duration-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-file-archive-duration-error-seconds-bad-value').infoFunc(): logFunc('fileArchiveDurationErrorSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setFileArchiveDurationErrorSeconds(tempVar)
            for logFunc in self._log('read-tag-values-file-archive-duration-error-seconds').debug3Func(): logFunc('read fileArchiveDurationErrorSeconds. fileArchiveDurationErrorSeconds=%s, tempValue=%s', self.fileArchiveDurationErrorSeconds, tempValue.getType())
        
        if self.isOverallArchiveDurationErrorSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "overall-archive-duration-error-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-overallarchivedurationerrorseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "overallArchiveDurationErrorSeconds", "overall-archive-duration-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-overall-archive-duration-error-seconds-bad-value').infoFunc(): logFunc('overallArchiveDurationErrorSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOverallArchiveDurationErrorSeconds(tempVar)
            for logFunc in self._log('read-tag-values-overall-archive-duration-error-seconds').debug3Func(): logFunc('read overallArchiveDurationErrorSeconds. overallArchiveDurationErrorSeconds=%s, tempValue=%s', self.overallArchiveDurationErrorSeconds, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "thresholds", 
        "namespace": "thresholds", 
        "className": "ThresholdsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.system_defaults.housekeeper.log_archiving.thresholds.thresholds_maapi_gen import ThresholdsMaapi", 
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
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "system-defaults"
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
            "yangName": "log-archiving", 
            "namespace": "log_archiving", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log-archiving"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "thresholds", 
            "namespace": "thresholds", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "thresholds"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationWarningSeconds", 
            "yangName": "file-archive-duration-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountWarning", 
            "yangName": "pending-file-count-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationWarningSeconds", 
            "yangName": "overall-archive-duration-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountError", 
            "yangName": "pending-file-count-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationErrorSeconds", 
            "yangName": "file-archive-duration-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationErrorSeconds", 
            "yangName": "overall-archive-duration-error-seconds", 
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
            "debug", 
            "qwilt_tech_log"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationWarningSeconds", 
            "yangName": "file-archive-duration-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountWarning", 
            "yangName": "pending-file-count-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationWarningSeconds", 
            "yangName": "overall-archive-duration-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pendingFileCountError", 
            "yangName": "pending-file-count-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "fileArchiveDurationErrorSeconds", 
            "yangName": "file-archive-duration-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallArchiveDurationErrorSeconds", 
            "yangName": "overall-archive-duration-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


