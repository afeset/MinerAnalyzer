


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

from housekeeper_maapi_base_gen import HousekeeperMaapiBase

from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.thresholds.thresholds_maapi_gen import BlinkyThresholdsMaapi
from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.log_archiving.log_archiving_maapi_gen import BlinkyLogArchivingMaapi
from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.counters.counters_maapi_gen import BlinkyCountersMaapi



class BlinkyHousekeeperMaapi(HousekeeperMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-housekeeper")
        self.domain = None

        
        self.thresholdsObj = None
        
        self.logArchivingObj = None
        
        self.countersObj = None
        

        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.pollIntervalRequested = False
        self.pollInterval = None
        self.pollIntervalSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(True)
        
        self.requestPollInterval(True)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestConfigAndOper()
        
        if not self.logArchivingObj:
            self.logArchivingObj = self.newLogArchiving()
            self.logArchivingObj.requestConfigAndOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(True)
        
        self.requestPollInterval(True)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestConfig()
        
        if not self.logArchivingObj:
            self.logArchivingObj = self.newLogArchiving()
            self.logArchivingObj.requestConfig()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(False)
        
        self.requestPollInterval(False)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestOper()
        
        if not self.logArchivingObj:
            self.logArchivingObj = self.newLogArchiving()
            self.logArchivingObj.requestOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(False)
        
        self.requestPollInterval(False)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.clearAllRequested()
        
        if not self.logArchivingObj:
            self.logArchivingObj = self.newLogArchiving()
            self.logArchivingObj.clearAllRequested()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setPollInterval(None)
        self.pollIntervalSet = False
        
        
        if self.thresholdsObj:
            self.thresholdsObj.clearAllSet()
        
        if self.logArchivingObj:
            self.logArchivingObj.clearAllSet()
        
        if self.countersObj:
            self.countersObj.clearAllSet()
        

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

    def newThresholds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-thresholds').debug3Func(): logFunc('called.')
        thresholds = BlinkyThresholdsMaapi(self._log)
        thresholds.init(self.domain)
        return thresholds

    def setThresholdsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-thresholds').debug3Func(): logFunc('called. obj=%s', obj)
        self.thresholdsObj = obj

    def getThresholdsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-thresholds').debug3Func(): logFunc('called. self.thresholdsObj=%s', self.thresholdsObj)
        return self.thresholdsObj

    def hasThresholds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-thresholds').debug3Func(): logFunc('called. self.thresholdsObj=%s', self.thresholdsObj)
        if self.thresholdsObj:
            return True
        return False

    def newLogArchiving (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-logarchiving').debug3Func(): logFunc('called.')
        logArchiving = BlinkyLogArchivingMaapi(self._log)
        logArchiving.init(self.domain)
        return logArchiving

    def setLogArchivingObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-logarchiving').debug3Func(): logFunc('called. obj=%s', obj)
        self.logArchivingObj = obj

    def getLogArchivingObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-logarchiving').debug3Func(): logFunc('called. self.logArchivingObj=%s', self.logArchivingObj)
        return self.logArchivingObj

    def hasLogArchiving (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-logarchiving').debug3Func(): logFunc('called. self.logArchivingObj=%s', self.logArchivingObj)
        if self.logArchivingObj:
            return True
        return False

    def newCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-counters').debug3Func(): logFunc('called.')
        counters = BlinkyCountersMaapi(self._log)
        counters.init(self.domain)
        return counters

    def setCountersObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-counters').debug3Func(): logFunc('called. obj=%s', obj)
        self.countersObj = obj

    def getCountersObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-counters').debug3Func(): logFunc('called. self.countersObj=%s', self.countersObj)
        return self.countersObj

    def hasCounters (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-counters').debug3Func(): logFunc('called. self.countersObj=%s', self.countersObj)
        if self.countersObj:
            return True
        return False



    def requestEnabled (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-enabled').debug3Func(): logFunc('called. requested=%s', requested)
        self.enabledRequested = requested
        self.enabledSet = False

    def isEnabledRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-enabled-requested').debug3Func(): logFunc('called. requested=%s', self.enabledRequested)
        return self.enabledRequested

    def getEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return self.enabled
        return None

    def hasEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return True
        return False

    def setEnabled (self, enabled):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-enabled').debug3Func(): logFunc('called. enabled=%s, old=%s', enabled, self.enabled)
        self.enabledSet = True
        self.enabled = enabled

    def requestPollInterval (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pollinterval').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollIntervalRequested = requested
        self.pollIntervalSet = False

    def isPollIntervalRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pollinterval-requested').debug3Func(): logFunc('called. requested=%s', self.pollIntervalRequested)
        return self.pollIntervalRequested

    def getPollInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pollinterval').debug3Func(): logFunc('called. self.pollIntervalSet=%s, self.pollInterval=%s', self.pollIntervalSet, self.pollInterval)
        if self.pollIntervalSet:
            return self.pollInterval
        return None

    def hasPollInterval (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pollinterval').debug3Func(): logFunc('called. self.pollIntervalSet=%s, self.pollInterval=%s', self.pollIntervalSet, self.pollInterval)
        if self.pollIntervalSet:
            return True
        return False

    def setPollInterval (self, pollInterval):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pollinterval').debug3Func(): logFunc('called. pollInterval=%s, old=%s', pollInterval, self.pollInterval)
        self.pollIntervalSet = True
        self.pollInterval = pollInterval


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.thresholdsObj:
            self.thresholdsObj._clearAllReadData()
        
        if self.logArchivingObj:
            self.logArchivingObj._clearAllReadData()
        
        if self.countersObj:
            self.countersObj._clearAllReadData()
        

        
        self.enabled = 0
        self.enabledSet = False
        
        self.pollInterval = 0
        self.pollIntervalSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
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

        
        if self.thresholdsObj:
            res = self.thresholdsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-thresholds-failed').errorFunc(): logFunc('thresholdsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.logArchivingObj:
            res = self.logArchivingObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-log-archiving-failed').errorFunc(): logFunc('logArchivingObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            res = self.countersObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-counters-failed').errorFunc(): logFunc('countersObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valEnabled)
        
        if self.hasPollInterval():
            valPollInterval = Value()
            if self.pollInterval is not None:
                valPollInterval.setInt64(self.pollInterval)
            else:
                valPollInterval.setEmpty()
            tagValueList.push(("poll-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPollInterval)
        

        
        if self.thresholdsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("thresholds" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.thresholdsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-thresholds-failed').errorFunc(): logFunc('thresholdsObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.logArchivingObj:
            valBegin = Value()
            (tag, ns, prefix) = ("log-archiving" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.logArchivingObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-log-archiving-failed').errorFunc(): logFunc('logArchivingObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.countersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.countersObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-counters-failed').errorFunc(): logFunc('countersObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valEnabled)
        
        if self.isPollIntervalRequested():
            valPollInterval = Value()
            valPollInterval.setEmpty()
            tagValueList.push(("poll-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPollInterval)
        

        
        if self.thresholdsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("thresholds" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.thresholdsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-thresholds-failed').errorFunc(): logFunc('thresholdsObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.logArchivingObj:
            valBegin = Value()
            (tag, ns, prefix) = ("log-archiving" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.logArchivingObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-log-archiving-failed').errorFunc(): logFunc('logArchivingObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.countersObj:
            valBegin = Value()
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.countersObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-counters-failed').errorFunc(): logFunc('countersObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-enabled-bad-value').infoFunc(): logFunc('enabled not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEnabled(tempVar)
            for logFunc in self._log('read-tag-values-enabled').debug3Func(): logFunc('read enabled. enabled=%s, tempValue=%s', self.enabled, tempValue.getType())
        
        if self.isPollIntervalRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-interval") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pollinterval').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollInterval", "poll-interval", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-interval-bad-value').infoFunc(): logFunc('pollInterval not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollInterval(tempVar)
            for logFunc in self._log('read-tag-values-poll-interval').debug3Func(): logFunc('read pollInterval. pollInterval=%s, tempValue=%s', self.pollInterval, tempValue.getType())
        

        
        if self.thresholdsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "thresholds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.thresholdsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-thresholds-failed').errorFunc(): logFunc('thresholdsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "thresholds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.logArchivingObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "log-archiving") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "log-archiving", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.logArchivingObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-log-archiving-failed').errorFunc(): logFunc('logArchivingObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "log-archiving") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "log-archiving", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.countersObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-counters-failed').errorFunc(): logFunc('countersObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "housekeeper", 
        "namespace": "housekeeper", 
        "className": "HousekeeperMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.housekeeper_maapi_gen import HousekeeperMaapi", 
        "baseClassName": "HousekeeperMaapiBase", 
        "baseModule": "housekeeper_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "housekeeper"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "memberName": "thresholds", 
            "yangName": "thresholds", 
            "className": "BlinkyThresholdsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.thresholds.thresholds_maapi_gen import BlinkyThresholdsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "memberName": "logArchiving", 
            "yangName": "log-archiving", 
            "className": "BlinkyLogArchivingMaapi", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.log_archiving.log_archiving_maapi_gen import BlinkyLogArchivingMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


