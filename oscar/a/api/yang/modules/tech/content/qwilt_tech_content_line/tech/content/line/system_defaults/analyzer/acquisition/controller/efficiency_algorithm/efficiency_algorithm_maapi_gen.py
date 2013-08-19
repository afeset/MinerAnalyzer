


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

from efficiency_algorithm_maapi_base_gen import EfficiencyAlgorithmMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import DecisionType


class BlinkyEfficiencyAlgorithmMaapi(EfficiencyAlgorithmMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-efficiencyAlgorithm")
        self.domain = None

        

        
        self.pastVolumeAttenuationPromilRequested = False
        self.pastVolumeAttenuationPromil = None
        self.pastVolumeAttenuationPromilSet = False
        
        self.thresholdMarginPpmRequested = False
        self.thresholdMarginPpm = None
        self.thresholdMarginPpmSet = False
        
        self.ageHistogramIntervalMinutesRequested = False
        self.ageHistogramIntervalMinutes = None
        self.ageHistogramIntervalMinutesSet = False
        
        self.onlyIfRangeOverlapsRequested = False
        self.onlyIfRangeOverlaps = None
        self.onlyIfRangeOverlapsSet = False
        
        self.useContentItemSizeRequested = False
        self.useContentItemSize = None
        self.useContentItemSizeSet = False
        
        self.thresholdPpmRequested = False
        self.thresholdPpm = None
        self.thresholdPpmSet = False
        
        self.continueOnceStartedRequested = False
        self.continueOnceStarted = None
        self.continueOnceStartedSet = False
        
        self.pastVolumeAttenuationIntervalMinutesRequested = False
        self.pastVolumeAttenuationIntervalMinutes = None
        self.pastVolumeAttenuationIntervalMinutesSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPastVolumeAttenuationPromil(True)
        
        self.requestThresholdMarginPpm(True)
        
        self.requestAgeHistogramIntervalMinutes(True)
        
        self.requestOnlyIfRangeOverlaps(True)
        
        self.requestUseContentItemSize(True)
        
        self.requestThresholdPpm(True)
        
        self.requestContinueOnceStarted(True)
        
        self.requestPastVolumeAttenuationIntervalMinutes(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPastVolumeAttenuationPromil(True)
        
        self.requestThresholdMarginPpm(True)
        
        self.requestAgeHistogramIntervalMinutes(True)
        
        self.requestOnlyIfRangeOverlaps(True)
        
        self.requestUseContentItemSize(True)
        
        self.requestThresholdPpm(True)
        
        self.requestContinueOnceStarted(True)
        
        self.requestPastVolumeAttenuationIntervalMinutes(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPastVolumeAttenuationPromil(False)
        
        self.requestThresholdMarginPpm(False)
        
        self.requestAgeHistogramIntervalMinutes(False)
        
        self.requestOnlyIfRangeOverlaps(False)
        
        self.requestUseContentItemSize(False)
        
        self.requestThresholdPpm(False)
        
        self.requestContinueOnceStarted(False)
        
        self.requestPastVolumeAttenuationIntervalMinutes(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPastVolumeAttenuationPromil(False)
        
        self.requestThresholdMarginPpm(False)
        
        self.requestAgeHistogramIntervalMinutes(False)
        
        self.requestOnlyIfRangeOverlaps(False)
        
        self.requestUseContentItemSize(False)
        
        self.requestThresholdPpm(False)
        
        self.requestContinueOnceStarted(False)
        
        self.requestPastVolumeAttenuationIntervalMinutes(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setPastVolumeAttenuationPromil(None)
        self.pastVolumeAttenuationPromilSet = False
        
        self.setThresholdMarginPpm(None)
        self.thresholdMarginPpmSet = False
        
        self.setAgeHistogramIntervalMinutes(None)
        self.ageHistogramIntervalMinutesSet = False
        
        self.setOnlyIfRangeOverlaps(None)
        self.onlyIfRangeOverlapsSet = False
        
        self.setUseContentItemSize(None)
        self.useContentItemSizeSet = False
        
        self.setThresholdPpm(None)
        self.thresholdPpmSet = False
        
        self.setContinueOnceStarted(None)
        self.continueOnceStartedSet = False
        
        self.setPastVolumeAttenuationIntervalMinutes(None)
        self.pastVolumeAttenuationIntervalMinutesSet = False
        
        

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



    def requestPastVolumeAttenuationPromil (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pastvolumeattenuationpromil').debug3Func(): logFunc('called. requested=%s', requested)
        self.pastVolumeAttenuationPromilRequested = requested
        self.pastVolumeAttenuationPromilSet = False

    def isPastVolumeAttenuationPromilRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pastvolumeattenuationpromil-requested').debug3Func(): logFunc('called. requested=%s', self.pastVolumeAttenuationPromilRequested)
        return self.pastVolumeAttenuationPromilRequested

    def getPastVolumeAttenuationPromil (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pastvolumeattenuationpromil').debug3Func(): logFunc('called. self.pastVolumeAttenuationPromilSet=%s, self.pastVolumeAttenuationPromil=%s', self.pastVolumeAttenuationPromilSet, self.pastVolumeAttenuationPromil)
        if self.pastVolumeAttenuationPromilSet:
            return self.pastVolumeAttenuationPromil
        return None

    def hasPastVolumeAttenuationPromil (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pastvolumeattenuationpromil').debug3Func(): logFunc('called. self.pastVolumeAttenuationPromilSet=%s, self.pastVolumeAttenuationPromil=%s', self.pastVolumeAttenuationPromilSet, self.pastVolumeAttenuationPromil)
        if self.pastVolumeAttenuationPromilSet:
            return True
        return False

    def setPastVolumeAttenuationPromil (self, pastVolumeAttenuationPromil):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pastvolumeattenuationpromil').debug3Func(): logFunc('called. pastVolumeAttenuationPromil=%s, old=%s', pastVolumeAttenuationPromil, self.pastVolumeAttenuationPromil)
        self.pastVolumeAttenuationPromilSet = True
        self.pastVolumeAttenuationPromil = pastVolumeAttenuationPromil

    def requestThresholdMarginPpm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-thresholdmarginppm').debug3Func(): logFunc('called. requested=%s', requested)
        self.thresholdMarginPpmRequested = requested
        self.thresholdMarginPpmSet = False

    def isThresholdMarginPpmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-thresholdmarginppm-requested').debug3Func(): logFunc('called. requested=%s', self.thresholdMarginPpmRequested)
        return self.thresholdMarginPpmRequested

    def getThresholdMarginPpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-thresholdmarginppm').debug3Func(): logFunc('called. self.thresholdMarginPpmSet=%s, self.thresholdMarginPpm=%s', self.thresholdMarginPpmSet, self.thresholdMarginPpm)
        if self.thresholdMarginPpmSet:
            return self.thresholdMarginPpm
        return None

    def hasThresholdMarginPpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-thresholdmarginppm').debug3Func(): logFunc('called. self.thresholdMarginPpmSet=%s, self.thresholdMarginPpm=%s', self.thresholdMarginPpmSet, self.thresholdMarginPpm)
        if self.thresholdMarginPpmSet:
            return True
        return False

    def setThresholdMarginPpm (self, thresholdMarginPpm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-thresholdmarginppm').debug3Func(): logFunc('called. thresholdMarginPpm=%s, old=%s', thresholdMarginPpm, self.thresholdMarginPpm)
        self.thresholdMarginPpmSet = True
        self.thresholdMarginPpm = thresholdMarginPpm

    def requestAgeHistogramIntervalMinutes (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-agehistogramintervalminutes').debug3Func(): logFunc('called. requested=%s', requested)
        self.ageHistogramIntervalMinutesRequested = requested
        self.ageHistogramIntervalMinutesSet = False

    def isAgeHistogramIntervalMinutesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-agehistogramintervalminutes-requested').debug3Func(): logFunc('called. requested=%s', self.ageHistogramIntervalMinutesRequested)
        return self.ageHistogramIntervalMinutesRequested

    def getAgeHistogramIntervalMinutes (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-agehistogramintervalminutes').debug3Func(): logFunc('called. self.ageHistogramIntervalMinutesSet=%s, self.ageHistogramIntervalMinutes=%s', self.ageHistogramIntervalMinutesSet, self.ageHistogramIntervalMinutes)
        if self.ageHistogramIntervalMinutesSet:
            return self.ageHistogramIntervalMinutes
        return None

    def hasAgeHistogramIntervalMinutes (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-agehistogramintervalminutes').debug3Func(): logFunc('called. self.ageHistogramIntervalMinutesSet=%s, self.ageHistogramIntervalMinutes=%s', self.ageHistogramIntervalMinutesSet, self.ageHistogramIntervalMinutes)
        if self.ageHistogramIntervalMinutesSet:
            return True
        return False

    def setAgeHistogramIntervalMinutes (self, ageHistogramIntervalMinutes):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-agehistogramintervalminutes').debug3Func(): logFunc('called. ageHistogramIntervalMinutes=%s, old=%s', ageHistogramIntervalMinutes, self.ageHistogramIntervalMinutes)
        self.ageHistogramIntervalMinutesSet = True
        self.ageHistogramIntervalMinutes = ageHistogramIntervalMinutes

    def requestOnlyIfRangeOverlaps (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-onlyifrangeoverlaps').debug3Func(): logFunc('called. requested=%s', requested)
        self.onlyIfRangeOverlapsRequested = requested
        self.onlyIfRangeOverlapsSet = False

    def isOnlyIfRangeOverlapsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-onlyifrangeoverlaps-requested').debug3Func(): logFunc('called. requested=%s', self.onlyIfRangeOverlapsRequested)
        return self.onlyIfRangeOverlapsRequested

    def getOnlyIfRangeOverlaps (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-onlyifrangeoverlaps').debug3Func(): logFunc('called. self.onlyIfRangeOverlapsSet=%s, self.onlyIfRangeOverlaps=%s', self.onlyIfRangeOverlapsSet, self.onlyIfRangeOverlaps)
        if self.onlyIfRangeOverlapsSet:
            return self.onlyIfRangeOverlaps
        return None

    def hasOnlyIfRangeOverlaps (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-onlyifrangeoverlaps').debug3Func(): logFunc('called. self.onlyIfRangeOverlapsSet=%s, self.onlyIfRangeOverlaps=%s', self.onlyIfRangeOverlapsSet, self.onlyIfRangeOverlaps)
        if self.onlyIfRangeOverlapsSet:
            return True
        return False

    def setOnlyIfRangeOverlaps (self, onlyIfRangeOverlaps):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-onlyifrangeoverlaps').debug3Func(): logFunc('called. onlyIfRangeOverlaps=%s, old=%s', onlyIfRangeOverlaps, self.onlyIfRangeOverlaps)
        self.onlyIfRangeOverlapsSet = True
        self.onlyIfRangeOverlaps = onlyIfRangeOverlaps

    def requestUseContentItemSize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-usecontentitemsize').debug3Func(): logFunc('called. requested=%s', requested)
        self.useContentItemSizeRequested = requested
        self.useContentItemSizeSet = False

    def isUseContentItemSizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-usecontentitemsize-requested').debug3Func(): logFunc('called. requested=%s', self.useContentItemSizeRequested)
        return self.useContentItemSizeRequested

    def getUseContentItemSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-usecontentitemsize').debug3Func(): logFunc('called. self.useContentItemSizeSet=%s, self.useContentItemSize=%s', self.useContentItemSizeSet, self.useContentItemSize)
        if self.useContentItemSizeSet:
            return self.useContentItemSize
        return None

    def hasUseContentItemSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-usecontentitemsize').debug3Func(): logFunc('called. self.useContentItemSizeSet=%s, self.useContentItemSize=%s', self.useContentItemSizeSet, self.useContentItemSize)
        if self.useContentItemSizeSet:
            return True
        return False

    def setUseContentItemSize (self, useContentItemSize):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-usecontentitemsize').debug3Func(): logFunc('called. useContentItemSize=%s, old=%s', useContentItemSize, self.useContentItemSize)
        self.useContentItemSizeSet = True
        self.useContentItemSize = useContentItemSize

    def requestThresholdPpm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-thresholdppm').debug3Func(): logFunc('called. requested=%s', requested)
        self.thresholdPpmRequested = requested
        self.thresholdPpmSet = False

    def isThresholdPpmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-thresholdppm-requested').debug3Func(): logFunc('called. requested=%s', self.thresholdPpmRequested)
        return self.thresholdPpmRequested

    def getThresholdPpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-thresholdppm').debug3Func(): logFunc('called. self.thresholdPpmSet=%s, self.thresholdPpm=%s', self.thresholdPpmSet, self.thresholdPpm)
        if self.thresholdPpmSet:
            return self.thresholdPpm
        return None

    def hasThresholdPpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-thresholdppm').debug3Func(): logFunc('called. self.thresholdPpmSet=%s, self.thresholdPpm=%s', self.thresholdPpmSet, self.thresholdPpm)
        if self.thresholdPpmSet:
            return True
        return False

    def setThresholdPpm (self, thresholdPpm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-thresholdppm').debug3Func(): logFunc('called. thresholdPpm=%s, old=%s', thresholdPpm, self.thresholdPpm)
        self.thresholdPpmSet = True
        self.thresholdPpm = thresholdPpm

    def requestContinueOnceStarted (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-continueoncestarted').debug3Func(): logFunc('called. requested=%s', requested)
        self.continueOnceStartedRequested = requested
        self.continueOnceStartedSet = False

    def isContinueOnceStartedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-continueoncestarted-requested').debug3Func(): logFunc('called. requested=%s', self.continueOnceStartedRequested)
        return self.continueOnceStartedRequested

    def getContinueOnceStarted (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-continueoncestarted').debug3Func(): logFunc('called. self.continueOnceStartedSet=%s, self.continueOnceStarted=%s', self.continueOnceStartedSet, self.continueOnceStarted)
        if self.continueOnceStartedSet:
            return self.continueOnceStarted
        return None

    def hasContinueOnceStarted (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-continueoncestarted').debug3Func(): logFunc('called. self.continueOnceStartedSet=%s, self.continueOnceStarted=%s', self.continueOnceStartedSet, self.continueOnceStarted)
        if self.continueOnceStartedSet:
            return True
        return False

    def setContinueOnceStarted (self, continueOnceStarted):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-continueoncestarted').debug3Func(): logFunc('called. continueOnceStarted=%s, old=%s', continueOnceStarted, self.continueOnceStarted)
        self.continueOnceStartedSet = True
        self.continueOnceStarted = continueOnceStarted

    def requestPastVolumeAttenuationIntervalMinutes (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pastvolumeattenuationintervalminutes').debug3Func(): logFunc('called. requested=%s', requested)
        self.pastVolumeAttenuationIntervalMinutesRequested = requested
        self.pastVolumeAttenuationIntervalMinutesSet = False

    def isPastVolumeAttenuationIntervalMinutesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pastvolumeattenuationintervalminutes-requested').debug3Func(): logFunc('called. requested=%s', self.pastVolumeAttenuationIntervalMinutesRequested)
        return self.pastVolumeAttenuationIntervalMinutesRequested

    def getPastVolumeAttenuationIntervalMinutes (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pastvolumeattenuationintervalminutes').debug3Func(): logFunc('called. self.pastVolumeAttenuationIntervalMinutesSet=%s, self.pastVolumeAttenuationIntervalMinutes=%s', self.pastVolumeAttenuationIntervalMinutesSet, self.pastVolumeAttenuationIntervalMinutes)
        if self.pastVolumeAttenuationIntervalMinutesSet:
            return self.pastVolumeAttenuationIntervalMinutes
        return None

    def hasPastVolumeAttenuationIntervalMinutes (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pastvolumeattenuationintervalminutes').debug3Func(): logFunc('called. self.pastVolumeAttenuationIntervalMinutesSet=%s, self.pastVolumeAttenuationIntervalMinutes=%s', self.pastVolumeAttenuationIntervalMinutesSet, self.pastVolumeAttenuationIntervalMinutes)
        if self.pastVolumeAttenuationIntervalMinutesSet:
            return True
        return False

    def setPastVolumeAttenuationIntervalMinutes (self, pastVolumeAttenuationIntervalMinutes):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pastvolumeattenuationintervalminutes').debug3Func(): logFunc('called. pastVolumeAttenuationIntervalMinutes=%s, old=%s', pastVolumeAttenuationIntervalMinutes, self.pastVolumeAttenuationIntervalMinutes)
        self.pastVolumeAttenuationIntervalMinutesSet = True
        self.pastVolumeAttenuationIntervalMinutes = pastVolumeAttenuationIntervalMinutes


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.pastVolumeAttenuationPromil = 0
        self.pastVolumeAttenuationPromilSet = False
        
        self.thresholdMarginPpm = 0
        self.thresholdMarginPpmSet = False
        
        self.ageHistogramIntervalMinutes = 0
        self.ageHistogramIntervalMinutesSet = False
        
        self.onlyIfRangeOverlaps = 0
        self.onlyIfRangeOverlapsSet = False
        
        self.useContentItemSize = 0
        self.useContentItemSizeSet = False
        
        self.thresholdPpm = 0
        self.thresholdPpmSet = False
        
        self.continueOnceStarted = 0
        self.continueOnceStartedSet = False
        
        self.pastVolumeAttenuationIntervalMinutes = 0
        self.pastVolumeAttenuationIntervalMinutesSet = False
        

    def _getSelfKeyPath (self, line
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("efficiency-algorithm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
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

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasPastVolumeAttenuationPromil():
            valPastVolumeAttenuationPromil = Value()
            if self.pastVolumeAttenuationPromil is not None:
                valPastVolumeAttenuationPromil.setInt64(self.pastVolumeAttenuationPromil)
            else:
                valPastVolumeAttenuationPromil.setEmpty()
            tagValueList.push(("past-volume-attenuation-promil", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valPastVolumeAttenuationPromil)
        
        if self.hasThresholdMarginPpm():
            valThresholdMarginPpm = Value()
            if self.thresholdMarginPpm is not None:
                valThresholdMarginPpm.setInt64(self.thresholdMarginPpm)
            else:
                valThresholdMarginPpm.setEmpty()
            tagValueList.push(("threshold-margin-ppm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThresholdMarginPpm)
        
        if self.hasAgeHistogramIntervalMinutes():
            valAgeHistogramIntervalMinutes = Value()
            if self.ageHistogramIntervalMinutes is not None:
                valAgeHistogramIntervalMinutes.setInt64(self.ageHistogramIntervalMinutes)
            else:
                valAgeHistogramIntervalMinutes.setEmpty()
            tagValueList.push(("age-histogram-interval-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valAgeHistogramIntervalMinutes)
        
        if self.hasOnlyIfRangeOverlaps():
            valOnlyIfRangeOverlaps = Value()
            if self.onlyIfRangeOverlaps is not None:
                valOnlyIfRangeOverlaps.setEnum(self.onlyIfRangeOverlaps.getValue())
            else:
                valOnlyIfRangeOverlaps.setEmpty()
            tagValueList.push(("only-if-range-overlaps", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valOnlyIfRangeOverlaps)
        
        if self.hasUseContentItemSize():
            valUseContentItemSize = Value()
            if self.useContentItemSize is not None:
                valUseContentItemSize.setEnum(self.useContentItemSize.getValue())
            else:
                valUseContentItemSize.setEmpty()
            tagValueList.push(("use-content-item-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valUseContentItemSize)
        
        if self.hasThresholdPpm():
            valThresholdPpm = Value()
            if self.thresholdPpm is not None:
                valThresholdPpm.setInt64(self.thresholdPpm)
            else:
                valThresholdPpm.setEmpty()
            tagValueList.push(("threshold-ppm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThresholdPpm)
        
        if self.hasContinueOnceStarted():
            valContinueOnceStarted = Value()
            if self.continueOnceStarted is not None:
                valContinueOnceStarted.setEnum(self.continueOnceStarted.getValue())
            else:
                valContinueOnceStarted.setEmpty()
            tagValueList.push(("continue-once-started", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valContinueOnceStarted)
        
        if self.hasPastVolumeAttenuationIntervalMinutes():
            valPastVolumeAttenuationIntervalMinutes = Value()
            if self.pastVolumeAttenuationIntervalMinutes is not None:
                valPastVolumeAttenuationIntervalMinutes.setInt64(self.pastVolumeAttenuationIntervalMinutes)
            else:
                valPastVolumeAttenuationIntervalMinutes.setEmpty()
            tagValueList.push(("past-volume-attenuation-interval-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valPastVolumeAttenuationIntervalMinutes)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isPastVolumeAttenuationPromilRequested():
            valPastVolumeAttenuationPromil = Value()
            valPastVolumeAttenuationPromil.setEmpty()
            tagValueList.push(("past-volume-attenuation-promil", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valPastVolumeAttenuationPromil)
        
        if self.isThresholdMarginPpmRequested():
            valThresholdMarginPpm = Value()
            valThresholdMarginPpm.setEmpty()
            tagValueList.push(("threshold-margin-ppm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThresholdMarginPpm)
        
        if self.isAgeHistogramIntervalMinutesRequested():
            valAgeHistogramIntervalMinutes = Value()
            valAgeHistogramIntervalMinutes.setEmpty()
            tagValueList.push(("age-histogram-interval-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valAgeHistogramIntervalMinutes)
        
        if self.isOnlyIfRangeOverlapsRequested():
            valOnlyIfRangeOverlaps = Value()
            valOnlyIfRangeOverlaps.setEmpty()
            tagValueList.push(("only-if-range-overlaps", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valOnlyIfRangeOverlaps)
        
        if self.isUseContentItemSizeRequested():
            valUseContentItemSize = Value()
            valUseContentItemSize.setEmpty()
            tagValueList.push(("use-content-item-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valUseContentItemSize)
        
        if self.isThresholdPpmRequested():
            valThresholdPpm = Value()
            valThresholdPpm.setEmpty()
            tagValueList.push(("threshold-ppm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThresholdPpm)
        
        if self.isContinueOnceStartedRequested():
            valContinueOnceStarted = Value()
            valContinueOnceStarted.setEmpty()
            tagValueList.push(("continue-once-started", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valContinueOnceStarted)
        
        if self.isPastVolumeAttenuationIntervalMinutesRequested():
            valPastVolumeAttenuationIntervalMinutes = Value()
            valPastVolumeAttenuationIntervalMinutes.setEmpty()
            tagValueList.push(("past-volume-attenuation-interval-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valPastVolumeAttenuationIntervalMinutes)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isPastVolumeAttenuationPromilRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "past-volume-attenuation-promil") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pastvolumeattenuationpromil').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pastVolumeAttenuationPromil", "past-volume-attenuation-promil", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-past-volume-attenuation-promil-bad-value').infoFunc(): logFunc('pastVolumeAttenuationPromil not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPastVolumeAttenuationPromil(tempVar)
            for logFunc in self._log('read-tag-values-past-volume-attenuation-promil').debug3Func(): logFunc('read pastVolumeAttenuationPromil. pastVolumeAttenuationPromil=%s, tempValue=%s', self.pastVolumeAttenuationPromil, tempValue.getType())
        
        if self.isThresholdMarginPpmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "threshold-margin-ppm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-thresholdmarginppm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "thresholdMarginPpm", "threshold-margin-ppm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-threshold-margin-ppm-bad-value').infoFunc(): logFunc('thresholdMarginPpm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setThresholdMarginPpm(tempVar)
            for logFunc in self._log('read-tag-values-threshold-margin-ppm').debug3Func(): logFunc('read thresholdMarginPpm. thresholdMarginPpm=%s, tempValue=%s', self.thresholdMarginPpm, tempValue.getType())
        
        if self.isAgeHistogramIntervalMinutesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "age-histogram-interval-minutes") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-agehistogramintervalminutes').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "ageHistogramIntervalMinutes", "age-histogram-interval-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-age-histogram-interval-minutes-bad-value').infoFunc(): logFunc('ageHistogramIntervalMinutes not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAgeHistogramIntervalMinutes(tempVar)
            for logFunc in self._log('read-tag-values-age-histogram-interval-minutes').debug3Func(): logFunc('read ageHistogramIntervalMinutes. ageHistogramIntervalMinutes=%s, tempValue=%s', self.ageHistogramIntervalMinutes, tempValue.getType())
        
        if self.isOnlyIfRangeOverlapsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "only-if-range-overlaps") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-onlyifrangeoverlaps').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "onlyIfRangeOverlaps", "only-if-range-overlaps", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-only-if-range-overlaps-bad-value').infoFunc(): logFunc('onlyIfRangeOverlaps not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOnlyIfRangeOverlaps(tempVar)
            for logFunc in self._log('read-tag-values-only-if-range-overlaps').debug3Func(): logFunc('read onlyIfRangeOverlaps. onlyIfRangeOverlaps=%s, tempValue=%s', self.onlyIfRangeOverlaps, tempValue.getType())
        
        if self.isUseContentItemSizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "use-content-item-size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-usecontentitemsize').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "useContentItemSize", "use-content-item-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-use-content-item-size-bad-value').infoFunc(): logFunc('useContentItemSize not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setUseContentItemSize(tempVar)
            for logFunc in self._log('read-tag-values-use-content-item-size').debug3Func(): logFunc('read useContentItemSize. useContentItemSize=%s, tempValue=%s', self.useContentItemSize, tempValue.getType())
        
        if self.isThresholdPpmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "threshold-ppm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-thresholdppm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "thresholdPpm", "threshold-ppm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-threshold-ppm-bad-value').infoFunc(): logFunc('thresholdPpm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setThresholdPpm(tempVar)
            for logFunc in self._log('read-tag-values-threshold-ppm').debug3Func(): logFunc('read thresholdPpm. thresholdPpm=%s, tempValue=%s', self.thresholdPpm, tempValue.getType())
        
        if self.isContinueOnceStartedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "continue-once-started") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-continueoncestarted').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "continueOnceStarted", "continue-once-started", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-continue-once-started-bad-value').infoFunc(): logFunc('continueOnceStarted not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setContinueOnceStarted(tempVar)
            for logFunc in self._log('read-tag-values-continue-once-started').debug3Func(): logFunc('read continueOnceStarted. continueOnceStarted=%s, tempValue=%s', self.continueOnceStarted, tempValue.getType())
        
        if self.isPastVolumeAttenuationIntervalMinutesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "past-volume-attenuation-interval-minutes") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pastvolumeattenuationintervalminutes').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pastVolumeAttenuationIntervalMinutes", "past-volume-attenuation-interval-minutes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-past-volume-attenuation-interval-minutes-bad-value').infoFunc(): logFunc('pastVolumeAttenuationIntervalMinutes not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPastVolumeAttenuationIntervalMinutes(tempVar)
            for logFunc in self._log('read-tag-values-past-volume-attenuation-interval-minutes').debug3Func(): logFunc('read pastVolumeAttenuationIntervalMinutes. pastVolumeAttenuationIntervalMinutes=%s, tempValue=%s', self.pastVolumeAttenuationIntervalMinutes, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "efficiencyAlgorithm", 
        "namespace": "efficiency_algorithm", 
        "className": "EfficiencyAlgorithmMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.analyzer.acquisition.controller.efficiency_algorithm.efficiency_algorithm_maapi_gen import EfficiencyAlgorithmMaapi", 
        "baseClassName": "EfficiencyAlgorithmMaapiBase", 
        "baseModule": "efficiency_algorithm_maapi_base_gen"
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
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "controller"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "efficiency-algorithm", 
            "namespace": "efficiency_algorithm", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "efficiency-algorithm"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pastVolumeAttenuationPromil", 
            "yangName": "past-volume-attenuation-promil", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "thresholdMarginPpm", 
            "yangName": "threshold-margin-ppm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "ageHistogramIntervalMinutes", 
            "yangName": "age-histogram-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "onlyIfRangeOverlaps", 
            "yangName": "only-if-range-overlaps", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "useContentItemSize", 
            "yangName": "use-content-item-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "thresholdPpm", 
            "yangName": "threshold-ppm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "continueOnceStarted", 
            "yangName": "continue-once-started", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pastVolumeAttenuationIntervalMinutes", 
            "yangName": "past-volume-attenuation-interval-minutes", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pastVolumeAttenuationPromil", 
            "yangName": "past-volume-attenuation-promil", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "thresholdMarginPpm", 
            "yangName": "threshold-margin-ppm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "ageHistogramIntervalMinutes", 
            "yangName": "age-histogram-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "onlyIfRangeOverlaps", 
            "yangName": "only-if-range-overlaps", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "useContentItemSize", 
            "yangName": "use-content-item-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "thresholdPpm", 
            "yangName": "threshold-ppm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "continueOnceStarted", 
            "yangName": "continue-once-started", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pastVolumeAttenuationIntervalMinutes", 
            "yangName": "past-volume-attenuation-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


