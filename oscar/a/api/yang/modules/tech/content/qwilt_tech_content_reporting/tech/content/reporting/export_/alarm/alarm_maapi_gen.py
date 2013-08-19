


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

from alarm_maapi_base_gen import AlarmMaapiBase


from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.qwilt_tech_content_reporting_module_gen import ReportingExportQueueFullReasonType


class BlinkyAlarmMaapi(AlarmMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-alarm")
        self.domain = None

        

        
        self.reportsQueueGettingFullReasonRequested = False
        self.reportsQueueGettingFullReason = None
        self.reportsQueueGettingFullReasonSet = False
        
        self.reportsQueueGettingFullRequested = False
        self.reportsQueueGettingFull = None
        self.reportsQueueGettingFullSet = False
        
        self.reportsQueueFullReasonRequested = False
        self.reportsQueueFullReason = None
        self.reportsQueueFullReasonSet = False
        
        self.reportsQueueFullRequested = False
        self.reportsQueueFull = None
        self.reportsQueueFullSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestReportsQueueGettingFullReason(True)
        
        self.requestReportsQueueGettingFull(True)
        
        self.requestReportsQueueFullReason(True)
        
        self.requestReportsQueueFull(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestReportsQueueGettingFullReason(False)
        
        self.requestReportsQueueGettingFull(False)
        
        self.requestReportsQueueFullReason(False)
        
        self.requestReportsQueueFull(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestReportsQueueGettingFullReason(True)
        
        self.requestReportsQueueGettingFull(True)
        
        self.requestReportsQueueFullReason(True)
        
        self.requestReportsQueueFull(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestReportsQueueGettingFullReason(False)
        
        self.requestReportsQueueGettingFull(False)
        
        self.requestReportsQueueFullReason(False)
        
        self.requestReportsQueueFull(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , export_
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(export_, trxContext)

    def read (self
              , export_
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(export_, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , export_
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(export_, 
                                  True,
                                  trxContext)



    def requestReportsQueueGettingFullReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-reportsqueuegettingfullreason').debug3Func(): logFunc('called. requested=%s', requested)
        self.reportsQueueGettingFullReasonRequested = requested
        self.reportsQueueGettingFullReasonSet = False

    def isReportsQueueGettingFullReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-reportsqueuegettingfullreason-requested').debug3Func(): logFunc('called. requested=%s', self.reportsQueueGettingFullReasonRequested)
        return self.reportsQueueGettingFullReasonRequested

    def getReportsQueueGettingFullReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-reportsqueuegettingfullreason').debug3Func(): logFunc('called. self.reportsQueueGettingFullReasonSet=%s, self.reportsQueueGettingFullReason=%s', self.reportsQueueGettingFullReasonSet, self.reportsQueueGettingFullReason)
        if self.reportsQueueGettingFullReasonSet:
            return self.reportsQueueGettingFullReason
        return None

    def hasReportsQueueGettingFullReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-reportsqueuegettingfullreason').debug3Func(): logFunc('called. self.reportsQueueGettingFullReasonSet=%s, self.reportsQueueGettingFullReason=%s', self.reportsQueueGettingFullReasonSet, self.reportsQueueGettingFullReason)
        if self.reportsQueueGettingFullReasonSet:
            return True
        return False

    def setReportsQueueGettingFullReason (self, reportsQueueGettingFullReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-reportsqueuegettingfullreason').debug3Func(): logFunc('called. reportsQueueGettingFullReason=%s, old=%s', reportsQueueGettingFullReason, self.reportsQueueGettingFullReason)
        self.reportsQueueGettingFullReasonSet = True
        self.reportsQueueGettingFullReason = reportsQueueGettingFullReason

    def requestReportsQueueGettingFull (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-reportsqueuegettingfull').debug3Func(): logFunc('called. requested=%s', requested)
        self.reportsQueueGettingFullRequested = requested
        self.reportsQueueGettingFullSet = False

    def isReportsQueueGettingFullRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-reportsqueuegettingfull-requested').debug3Func(): logFunc('called. requested=%s', self.reportsQueueGettingFullRequested)
        return self.reportsQueueGettingFullRequested

    def getReportsQueueGettingFull (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-reportsqueuegettingfull').debug3Func(): logFunc('called. self.reportsQueueGettingFullSet=%s, self.reportsQueueGettingFull=%s', self.reportsQueueGettingFullSet, self.reportsQueueGettingFull)
        if self.reportsQueueGettingFullSet:
            return self.reportsQueueGettingFull
        return None

    def hasReportsQueueGettingFull (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-reportsqueuegettingfull').debug3Func(): logFunc('called. self.reportsQueueGettingFullSet=%s, self.reportsQueueGettingFull=%s', self.reportsQueueGettingFullSet, self.reportsQueueGettingFull)
        if self.reportsQueueGettingFullSet:
            return True
        return False

    def setReportsQueueGettingFull (self, reportsQueueGettingFull):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-reportsqueuegettingfull').debug3Func(): logFunc('called. reportsQueueGettingFull=%s, old=%s', reportsQueueGettingFull, self.reportsQueueGettingFull)
        self.reportsQueueGettingFullSet = True
        self.reportsQueueGettingFull = reportsQueueGettingFull

    def requestReportsQueueFullReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-reportsqueuefullreason').debug3Func(): logFunc('called. requested=%s', requested)
        self.reportsQueueFullReasonRequested = requested
        self.reportsQueueFullReasonSet = False

    def isReportsQueueFullReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-reportsqueuefullreason-requested').debug3Func(): logFunc('called. requested=%s', self.reportsQueueFullReasonRequested)
        return self.reportsQueueFullReasonRequested

    def getReportsQueueFullReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-reportsqueuefullreason').debug3Func(): logFunc('called. self.reportsQueueFullReasonSet=%s, self.reportsQueueFullReason=%s', self.reportsQueueFullReasonSet, self.reportsQueueFullReason)
        if self.reportsQueueFullReasonSet:
            return self.reportsQueueFullReason
        return None

    def hasReportsQueueFullReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-reportsqueuefullreason').debug3Func(): logFunc('called. self.reportsQueueFullReasonSet=%s, self.reportsQueueFullReason=%s', self.reportsQueueFullReasonSet, self.reportsQueueFullReason)
        if self.reportsQueueFullReasonSet:
            return True
        return False

    def setReportsQueueFullReason (self, reportsQueueFullReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-reportsqueuefullreason').debug3Func(): logFunc('called. reportsQueueFullReason=%s, old=%s', reportsQueueFullReason, self.reportsQueueFullReason)
        self.reportsQueueFullReasonSet = True
        self.reportsQueueFullReason = reportsQueueFullReason

    def requestReportsQueueFull (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-reportsqueuefull').debug3Func(): logFunc('called. requested=%s', requested)
        self.reportsQueueFullRequested = requested
        self.reportsQueueFullSet = False

    def isReportsQueueFullRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-reportsqueuefull-requested').debug3Func(): logFunc('called. requested=%s', self.reportsQueueFullRequested)
        return self.reportsQueueFullRequested

    def getReportsQueueFull (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-reportsqueuefull').debug3Func(): logFunc('called. self.reportsQueueFullSet=%s, self.reportsQueueFull=%s', self.reportsQueueFullSet, self.reportsQueueFull)
        if self.reportsQueueFullSet:
            return self.reportsQueueFull
        return None

    def hasReportsQueueFull (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-reportsqueuefull').debug3Func(): logFunc('called. self.reportsQueueFullSet=%s, self.reportsQueueFull=%s', self.reportsQueueFullSet, self.reportsQueueFull)
        if self.reportsQueueFullSet:
            return True
        return False

    def setReportsQueueFull (self, reportsQueueFull):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-reportsqueuefull').debug3Func(): logFunc('called. reportsQueueFull=%s, old=%s', reportsQueueFull, self.reportsQueueFull)
        self.reportsQueueFullSet = True
        self.reportsQueueFull = reportsQueueFull


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.reportsQueueGettingFullReason = 0
        self.reportsQueueGettingFullReasonSet = False
        
        self.reportsQueueGettingFull = 0
        self.reportsQueueGettingFullSet = False
        
        self.reportsQueueFullReason = 0
        self.reportsQueueFullReasonSet = False
        
        self.reportsQueueFull = 0
        self.reportsQueueFullSet = False
        

    def _getSelfKeyPath (self, export_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", "qtc-report"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(export_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("export", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", "qtc-report"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", "qtc-report"))
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
                        export_, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(export_, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(export_, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       export_, 
                       
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

        keyPath = self._getSelfKeyPath(export_, 
                                       
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
                               export_, 
                               
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

        
        if self.isReportsQueueGettingFullReasonRequested():
            valReportsQueueGettingFullReason = Value()
            valReportsQueueGettingFullReason.setEmpty()
            tagValueList.push(("reports-queue-getting-full-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valReportsQueueGettingFullReason)
        
        if self.isReportsQueueGettingFullRequested():
            valReportsQueueGettingFull = Value()
            valReportsQueueGettingFull.setEmpty()
            tagValueList.push(("reports-queue-getting-full", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valReportsQueueGettingFull)
        
        if self.isReportsQueueFullReasonRequested():
            valReportsQueueFullReason = Value()
            valReportsQueueFullReason.setEmpty()
            tagValueList.push(("reports-queue-full-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valReportsQueueFullReason)
        
        if self.isReportsQueueFullRequested():
            valReportsQueueFull = Value()
            valReportsQueueFull.setEmpty()
            tagValueList.push(("reports-queue-full", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"), valReportsQueueFull)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isReportsQueueGettingFullReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "reports-queue-getting-full-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-reportsqueuegettingfullreason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "reportsQueueGettingFullReason", "reports-queue-getting-full-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-reports-queue-getting-full-reason-bad-value').infoFunc(): logFunc('reportsQueueGettingFullReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReportsQueueGettingFullReason(tempVar)
            for logFunc in self._log('read-tag-values-reports-queue-getting-full-reason').debug3Func(): logFunc('read reportsQueueGettingFullReason. reportsQueueGettingFullReason=%s, tempValue=%s', self.reportsQueueGettingFullReason, tempValue.getType())
        
        if self.isReportsQueueGettingFullRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "reports-queue-getting-full") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-reportsqueuegettingfull').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "reportsQueueGettingFull", "reports-queue-getting-full", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-reports-queue-getting-full-bad-value').infoFunc(): logFunc('reportsQueueGettingFull not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReportsQueueGettingFull(tempVar)
            for logFunc in self._log('read-tag-values-reports-queue-getting-full').debug3Func(): logFunc('read reportsQueueGettingFull. reportsQueueGettingFull=%s, tempValue=%s', self.reportsQueueGettingFull, tempValue.getType())
        
        if self.isReportsQueueFullReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "reports-queue-full-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-reportsqueuefullreason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "reportsQueueFullReason", "reports-queue-full-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-reports-queue-full-reason-bad-value').infoFunc(): logFunc('reportsQueueFullReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReportsQueueFullReason(tempVar)
            for logFunc in self._log('read-tag-values-reports-queue-full-reason').debug3Func(): logFunc('read reportsQueueFullReason. reportsQueueFullReason=%s, tempValue=%s', self.reportsQueueFullReason, tempValue.getType())
        
        if self.isReportsQueueFullRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "reports-queue-full") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-reportsqueuefull').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "reportsQueueFull", "reports-queue-full", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-reports-queue-full-bad-value').infoFunc(): logFunc('reportsQueueFull not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setReportsQueueFull(tempVar)
            for logFunc in self._log('read-tag-values-reports-queue-full').debug3Func(): logFunc('read reportsQueueFull. reportsQueueFull=%s, tempValue=%s', self.reportsQueueFull, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "alarm", 
        "namespace": "alarm", 
        "className": "AlarmMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.alarm.alarm_maapi_gen import AlarmMaapi", 
        "baseClassName": "AlarmMaapiBase", 
        "baseModule": "alarm_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-report", 
            "yangName": "reporting", 
            "namespace": "reporting", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "name": "reporting"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-report", 
            "isCurrent": false, 
            "yangName": "export", 
            "namespace": "export_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "keyLeaf": {
                "varName": "export_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "export_"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-report", 
            "yangName": "alarm", 
            "namespace": "alarm", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "name": "alarm"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "reportsQueueGettingFullReason", 
            "yangName": "reports-queue-getting-full-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "reportsQueueGettingFull", 
            "yangName": "reports-queue-getting-full", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "reportsQueueFullReason", 
            "yangName": "reports-queue-full-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "reportsQueueFull", 
            "yangName": "reports-queue-full", 
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
            "content", 
            "qwilt_tech_content_reporting"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "reportsQueueGettingFullReason", 
            "yangName": "reports-queue-getting-full-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "reportsQueueGettingFull", 
            "yangName": "reports-queue-getting-full", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "reportsQueueFullReason", 
            "yangName": "reports-queue-full-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "reportsQueueFull", 
            "yangName": "reports-queue-full", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


