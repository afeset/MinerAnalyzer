


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

from manager_maapi_base_gen import ManagerMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.thresholds.thresholds_maapi_gen import BlinkyThresholdsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_maapi_list_gen import BlinkySourceMaapiList
from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi
from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.counters.counters_maapi_gen import BlinkyCountersMaapi



class BlinkyManagerMaapi(ManagerMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-manager")
        self.domain = None

        
        self.thresholdsObj = None
        
        self.sourceListObj = None
        
        self.systemDefaultsObj = None
        
        self.countersObj = None
        

        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.pollIntervalSecondsRequested = False
        self.pollIntervalSeconds = None
        self.pollIntervalSecondsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(True)
        
        self.requestPollIntervalSeconds(True)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestConfigAndOper()
        
        if not self.sourceListObj:
            self.sourceListObj = self.newSourceList()
            self.sourceListObj.requestConfigAndOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(True)
        
        self.requestPollIntervalSeconds(True)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestConfig()
        
        if not self.sourceListObj:
            self.sourceListObj = self.newSourceList()
            self.sourceListObj.requestConfig()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(False)
        
        self.requestPollIntervalSeconds(False)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestOper()
        
        if not self.sourceListObj:
            self.sourceListObj = self.newSourceList()
            self.sourceListObj.requestOper()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEnabled(False)
        
        self.requestPollIntervalSeconds(False)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.clearAllRequested()
        
        if not self.sourceListObj:
            self.sourceListObj = self.newSourceList()
            self.sourceListObj.clearAllRequested()
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        
        if not self.countersObj:
            self.countersObj = self.newCounters()
            self.countersObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setPollIntervalSeconds(None)
        self.pollIntervalSecondsSet = False
        
        
        if self.thresholdsObj:
            self.thresholdsObj.clearAllSet()
        
        if self.sourceListObj:
            self.sourceListObj.clearAllSet()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        
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

    def newSourceList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-sourcelist').debug3Func(): logFunc('called.')
        sourceList = BlinkySourceMaapiList(self._log)
        sourceList.init(self.domain)
        return sourceList

    def setSourceListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-sourcelist').debug3Func(): logFunc('called. obj=%s', obj)
        self.sourceListObj = obj

    def getSourceListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-sourcelist').debug3Func(): logFunc('called. self.sourceListObj=%s', self.sourceListObj)
        return self.sourceListObj

    def hasSourceList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-sourcelist').debug3Func(): logFunc('called. self.sourceListObj=%s', self.sourceListObj)
        if self.sourceListObj:
            return True
        return False

    def newSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-systemdefaults').debug3Func(): logFunc('called.')
        systemDefaults = BlinkySystemDefaultsMaapi(self._log)
        systemDefaults.init(self.domain)
        return systemDefaults

    def setSystemDefaultsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemdefaults').debug3Func(): logFunc('called. obj=%s', obj)
        self.systemDefaultsObj = obj

    def getSystemDefaultsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        return self.systemDefaultsObj

    def hasSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        if self.systemDefaultsObj:
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

    def requestPollIntervalSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pollintervalseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollIntervalSecondsRequested = requested
        self.pollIntervalSecondsSet = False

    def isPollIntervalSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pollintervalseconds-requested').debug3Func(): logFunc('called. requested=%s', self.pollIntervalSecondsRequested)
        return self.pollIntervalSecondsRequested

    def getPollIntervalSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pollintervalseconds').debug3Func(): logFunc('called. self.pollIntervalSecondsSet=%s, self.pollIntervalSeconds=%s', self.pollIntervalSecondsSet, self.pollIntervalSeconds)
        if self.pollIntervalSecondsSet:
            return self.pollIntervalSeconds
        return None

    def hasPollIntervalSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pollintervalseconds').debug3Func(): logFunc('called. self.pollIntervalSecondsSet=%s, self.pollIntervalSeconds=%s', self.pollIntervalSecondsSet, self.pollIntervalSeconds)
        if self.pollIntervalSecondsSet:
            return True
        return False

    def setPollIntervalSeconds (self, pollIntervalSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pollintervalseconds').debug3Func(): logFunc('called. pollIntervalSeconds=%s, old=%s', pollIntervalSeconds, self.pollIntervalSeconds)
        self.pollIntervalSecondsSet = True
        self.pollIntervalSeconds = pollIntervalSeconds


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.thresholdsObj:
            self.thresholdsObj._clearAllReadData()
        
        if self.sourceListObj:
            self.sourceListObj._clearAllReadData()
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        
        if self.countersObj:
            self.countersObj._clearAllReadData()
        

        
        self.enabled = 0
        self.enabledSet = False
        
        self.pollIntervalSeconds = 0
        self.pollIntervalSecondsSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
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

        
        if self.thresholdsObj:
            res = self.thresholdsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-thresholds-failed').errorFunc(): logFunc('thresholdsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.sourceListObj:
            res = self.sourceListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-source-failed').errorFunc(): logFunc('sourceListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
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
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valEnabled)
        
        if self.hasPollIntervalSeconds():
            valPollIntervalSeconds = Value()
            if self.pollIntervalSeconds is not None:
                valPollIntervalSeconds.setInt64(self.pollIntervalSeconds)
            else:
                valPollIntervalSeconds.setEmpty()
            tagValueList.push(("poll-interval-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valPollIntervalSeconds)
        

        
        if self.thresholdsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("thresholds" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr")
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
        
        if self.sourceListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("source" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.sourceListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-source-failed').errorFunc(): logFunc('sourceListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillWriteTagValues() failed. PARAMS')
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
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr")
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
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valEnabled)
        
        if self.isPollIntervalSecondsRequested():
            valPollIntervalSeconds = Value()
            valPollIntervalSeconds.setEmpty()
            tagValueList.push(("poll-interval-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"), valPollIntervalSeconds)
        

        
        if self.thresholdsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("thresholds" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr")
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
        
        if self.sourceListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("source" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.sourceListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-source-failed').errorFunc(): logFunc('sourceListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillReadTagValues() failed. PARAMS')
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
            (tag, ns, prefix) = ("counters" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", "qt-pltf-mngr")
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
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
        
        if self.isPollIntervalSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-interval-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pollintervalseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollIntervalSeconds", "poll-interval-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-interval-seconds-bad-value').infoFunc(): logFunc('pollIntervalSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollIntervalSeconds(tempVar)
            for logFunc in self._log('read-tag-values-poll-interval-seconds').debug3Func(): logFunc('read pollIntervalSeconds. pollIntervalSeconds=%s, tempValue=%s', self.pollIntervalSeconds, tempValue.getType())
        

        
        if self.thresholdsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "thresholds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", Value.kXmlBegin,
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.sourceListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "source") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.sourceListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-source-failed').errorFunc(): logFunc('sourceListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "source") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "source", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.systemDefaultsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.countersObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "counters") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", Value.kXmlBegin,
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "manager", 
        "namespace": "manager", 
        "className": "ManagerMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.manager_maapi_gen import ManagerMaapi", 
        "baseClassName": "ManagerMaapiBase", 
        "baseModule": "manager_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "name": "manager"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "memberName": "thresholds", 
            "yangName": "thresholds", 
            "className": "BlinkyThresholdsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.thresholds.thresholds_maapi_gen import BlinkyThresholdsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "memberName": "sourceList", 
            "yangName": "source", 
            "className": "BlinkySourceMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_maapi_list_gen import BlinkySourceMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollIntervalSeconds", 
            "yangName": "poll-interval-seconds", 
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
            "common", 
            "qwilt_tech_platform_manager"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-manager", 
            "moduleYangNamespacePrefix": "qt-pltf-mngr", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollIntervalSeconds", 
            "yangName": "poll-interval-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


