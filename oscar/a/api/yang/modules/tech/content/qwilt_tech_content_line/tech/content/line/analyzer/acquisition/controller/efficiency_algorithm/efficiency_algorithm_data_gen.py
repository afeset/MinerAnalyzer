


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import DecisionType


class EfficiencyAlgorithmData(object):

    def __init__ (self):

        self.pastVolumeAttenuationPromil = 0
        self._myHasPastVolumeAttenuationPromil=False
        
        self.thresholdMarginPpm = 0
        self._myHasThresholdMarginPpm=False
        
        self.ageHistogramIntervalMinutes = 0
        self._myHasAgeHistogramIntervalMinutes=False
        
        self.onlyIfRangeOverlaps = DecisionType.kTrue
        self._myHasOnlyIfRangeOverlaps=False
        
        self.useContentItemSize = DecisionType.kTrue
        self._myHasUseContentItemSize=False
        
        self.thresholdPpm = 0
        self._myHasThresholdPpm=False
        
        self.continueOnceStarted = DecisionType.kTrue
        self._myHasContinueOnceStarted=False
        
        self.pastVolumeAttenuationIntervalMinutes = 0
        self._myHasPastVolumeAttenuationIntervalMinutes=False
        

    def copyFrom (self, other):

        self.pastVolumeAttenuationPromil=other.pastVolumeAttenuationPromil
        self._myHasPastVolumeAttenuationPromil=other._myHasPastVolumeAttenuationPromil
        
        self.thresholdMarginPpm=other.thresholdMarginPpm
        self._myHasThresholdMarginPpm=other._myHasThresholdMarginPpm
        
        self.ageHistogramIntervalMinutes=other.ageHistogramIntervalMinutes
        self._myHasAgeHistogramIntervalMinutes=other._myHasAgeHistogramIntervalMinutes
        
        self.onlyIfRangeOverlaps=other.onlyIfRangeOverlaps
        self._myHasOnlyIfRangeOverlaps=other._myHasOnlyIfRangeOverlaps
        
        self.useContentItemSize=other.useContentItemSize
        self._myHasUseContentItemSize=other._myHasUseContentItemSize
        
        self.thresholdPpm=other.thresholdPpm
        self._myHasThresholdPpm=other._myHasThresholdPpm
        
        self.continueOnceStarted=other.continueOnceStarted
        self._myHasContinueOnceStarted=other._myHasContinueOnceStarted
        
        self.pastVolumeAttenuationIntervalMinutes=other.pastVolumeAttenuationIntervalMinutes
        self._myHasPastVolumeAttenuationIntervalMinutes=other._myHasPastVolumeAttenuationIntervalMinutes
        
    # has...() methods

    def hasPastVolumeAttenuationPromil (self):
        return self._myHasPastVolumeAttenuationPromil

    def hasThresholdMarginPpm (self):
        return self._myHasThresholdMarginPpm

    def hasAgeHistogramIntervalMinutes (self):
        return self._myHasAgeHistogramIntervalMinutes

    def hasOnlyIfRangeOverlaps (self):
        return self._myHasOnlyIfRangeOverlaps

    def hasUseContentItemSize (self):
        return self._myHasUseContentItemSize

    def hasThresholdPpm (self):
        return self._myHasThresholdPpm

    def hasContinueOnceStarted (self):
        return self._myHasContinueOnceStarted

    def hasPastVolumeAttenuationIntervalMinutes (self):
        return self._myHasPastVolumeAttenuationIntervalMinutes


    # setHas...() methods

    def setHasPastVolumeAttenuationPromil (self):
        self._myHasPastVolumeAttenuationPromil=True

    def setHasThresholdMarginPpm (self):
        self._myHasThresholdMarginPpm=True

    def setHasAgeHistogramIntervalMinutes (self):
        self._myHasAgeHistogramIntervalMinutes=True

    def setHasOnlyIfRangeOverlaps (self):
        self._myHasOnlyIfRangeOverlaps=True

    def setHasUseContentItemSize (self):
        self._myHasUseContentItemSize=True

    def setHasThresholdPpm (self):
        self._myHasThresholdPpm=True

    def setHasContinueOnceStarted (self):
        self._myHasContinueOnceStarted=True

    def setHasPastVolumeAttenuationIntervalMinutes (self):
        self._myHasPastVolumeAttenuationIntervalMinutes=True


    def clearAllHas (self):

        self._myHasPastVolumeAttenuationPromil=False

        self._myHasThresholdMarginPpm=False

        self._myHasAgeHistogramIntervalMinutes=False

        self._myHasOnlyIfRangeOverlaps=False

        self._myHasUseContentItemSize=False

        self._myHasThresholdPpm=False

        self._myHasContinueOnceStarted=False

        self._myHasPastVolumeAttenuationIntervalMinutes=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasPastVolumeAttenuationPromil:
            x = "+"
        leafStr = str(self.pastVolumeAttenuationPromil)
        items.append(x + "PastVolumeAttenuationPromil="+leafStr)

        x=""
        if self._myHasThresholdMarginPpm:
            x = "+"
        leafStr = str(self.thresholdMarginPpm)
        items.append(x + "ThresholdMarginPpm="+leafStr)

        x=""
        if self._myHasAgeHistogramIntervalMinutes:
            x = "+"
        leafStr = str(self.ageHistogramIntervalMinutes)
        items.append(x + "AgeHistogramIntervalMinutes="+leafStr)

        x=""
        if self._myHasOnlyIfRangeOverlaps:
            x = "+"
        leafStr = str(self.onlyIfRangeOverlaps)
        items.append(x + "OnlyIfRangeOverlaps="+leafStr)

        x=""
        if self._myHasUseContentItemSize:
            x = "+"
        leafStr = str(self.useContentItemSize)
        items.append(x + "UseContentItemSize="+leafStr)

        x=""
        if self._myHasThresholdPpm:
            x = "+"
        leafStr = str(self.thresholdPpm)
        items.append(x + "ThresholdPpm="+leafStr)

        x=""
        if self._myHasContinueOnceStarted:
            x = "+"
        leafStr = str(self.continueOnceStarted)
        items.append(x + "ContinueOnceStarted="+leafStr)

        x=""
        if self._myHasPastVolumeAttenuationIntervalMinutes:
            x = "+"
        leafStr = str(self.pastVolumeAttenuationIntervalMinutes)
        items.append(x + "PastVolumeAttenuationIntervalMinutes="+leafStr)

        return "{EfficiencyAlgorithmData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "EfficiencyAlgorithmData", 
        "namespace": "efficiency_algorithm", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.acquisition.controller.efficiency_algorithm.efficiency_algorithm_data_gen import EfficiencyAlgorithmData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "content", 
            "isCurrent": false
        }, 
        {
            "namespace": "line", 
            "isCurrent": false
        }, 
        {
            "namespace": "analyzer", 
            "isCurrent": false
        }, 
        {
            "namespace": "acquisition", 
            "isCurrent": false
        }, 
        {
            "namespace": "controller", 
            "isCurrent": false
        }, 
        {
            "namespace": "efficiency_algorithm", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pastVolumeAttenuationPromil", 
            "yangName": "past-volume-attenuation-promil", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "thresholdMarginPpm", 
            "yangName": "threshold-margin-ppm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "ageHistogramIntervalMinutes", 
            "yangName": "age-histogram-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "onlyIfRangeOverlaps", 
            "yangName": "only-if-range-overlaps", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "useContentItemSize", 
            "yangName": "use-content-item-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "thresholdPpm", 
            "yangName": "threshold-ppm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "continueOnceStarted", 
            "yangName": "continue-once-started", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pastVolumeAttenuationIntervalMinutes", 
            "yangName": "past-volume-attenuation-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "module": {}, 
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
    "createTime": "2013"
}
"""


