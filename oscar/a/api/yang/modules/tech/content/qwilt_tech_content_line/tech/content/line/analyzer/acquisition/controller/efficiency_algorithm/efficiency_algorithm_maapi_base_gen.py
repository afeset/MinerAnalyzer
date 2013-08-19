


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class EfficiencyAlgorithmMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , line
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , line
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , line
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # pastVolumeAttenuationPromil
    def requestPastVolumeAttenuationPromil (self, requested):
        raise NotImplementedError()

    def isPastVolumeAttenuationPromilRequested (self):
        raise NotImplementedError()

    def getPastVolumeAttenuationPromil (self):
        raise NotImplementedError()

    def hasPastVolumeAttenuationPromil (self):
        raise NotImplementedError()

    def setPastVolumeAttenuationPromil (self, pastVolumeAttenuationPromil):
        raise NotImplementedError()

    # thresholdMarginPpm
    def requestThresholdMarginPpm (self, requested):
        raise NotImplementedError()

    def isThresholdMarginPpmRequested (self):
        raise NotImplementedError()

    def getThresholdMarginPpm (self):
        raise NotImplementedError()

    def hasThresholdMarginPpm (self):
        raise NotImplementedError()

    def setThresholdMarginPpm (self, thresholdMarginPpm):
        raise NotImplementedError()

    # ageHistogramIntervalMinutes
    def requestAgeHistogramIntervalMinutes (self, requested):
        raise NotImplementedError()

    def isAgeHistogramIntervalMinutesRequested (self):
        raise NotImplementedError()

    def getAgeHistogramIntervalMinutes (self):
        raise NotImplementedError()

    def hasAgeHistogramIntervalMinutes (self):
        raise NotImplementedError()

    def setAgeHistogramIntervalMinutes (self, ageHistogramIntervalMinutes):
        raise NotImplementedError()

    # onlyIfRangeOverlaps
    def requestOnlyIfRangeOverlaps (self, requested):
        raise NotImplementedError()

    def isOnlyIfRangeOverlapsRequested (self):
        raise NotImplementedError()

    def getOnlyIfRangeOverlaps (self):
        raise NotImplementedError()

    def hasOnlyIfRangeOverlaps (self):
        raise NotImplementedError()

    def setOnlyIfRangeOverlaps (self, onlyIfRangeOverlaps):
        raise NotImplementedError()

    # useContentItemSize
    def requestUseContentItemSize (self, requested):
        raise NotImplementedError()

    def isUseContentItemSizeRequested (self):
        raise NotImplementedError()

    def getUseContentItemSize (self):
        raise NotImplementedError()

    def hasUseContentItemSize (self):
        raise NotImplementedError()

    def setUseContentItemSize (self, useContentItemSize):
        raise NotImplementedError()

    # thresholdPpm
    def requestThresholdPpm (self, requested):
        raise NotImplementedError()

    def isThresholdPpmRequested (self):
        raise NotImplementedError()

    def getThresholdPpm (self):
        raise NotImplementedError()

    def hasThresholdPpm (self):
        raise NotImplementedError()

    def setThresholdPpm (self, thresholdPpm):
        raise NotImplementedError()

    # continueOnceStarted
    def requestContinueOnceStarted (self, requested):
        raise NotImplementedError()

    def isContinueOnceStartedRequested (self):
        raise NotImplementedError()

    def getContinueOnceStarted (self):
        raise NotImplementedError()

    def hasContinueOnceStarted (self):
        raise NotImplementedError()

    def setContinueOnceStarted (self, continueOnceStarted):
        raise NotImplementedError()

    # pastVolumeAttenuationIntervalMinutes
    def requestPastVolumeAttenuationIntervalMinutes (self, requested):
        raise NotImplementedError()

    def isPastVolumeAttenuationIntervalMinutesRequested (self):
        raise NotImplementedError()

    def getPastVolumeAttenuationIntervalMinutes (self):
        raise NotImplementedError()

    def hasPastVolumeAttenuationIntervalMinutes (self):
        raise NotImplementedError()

    def setPastVolumeAttenuationIntervalMinutes (self, pastVolumeAttenuationIntervalMinutes):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "efficiencyAlgorithm", 
        "namespace": "efficiency_algorithm", 
        "className": "EfficiencyAlgorithmMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.acquisition.controller.efficiency_algorithm.efficiency_algorithm_maapi_gen import EfficiencyAlgorithmMaapi", 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "thresholdMarginPpm", 
            "yangName": "threshold-margin-ppm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "ageHistogramIntervalMinutes", 
            "yangName": "age-histogram-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "onlyIfRangeOverlaps", 
            "yangName": "only-if-range-overlaps", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "useContentItemSize", 
            "yangName": "use-content-item-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "thresholdPpm", 
            "yangName": "threshold-ppm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "continueOnceStarted", 
            "yangName": "continue-once-started", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pastVolumeAttenuationIntervalMinutes", 
            "yangName": "past-volume-attenuation-interval-minutes", 
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
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "thresholdMarginPpm", 
            "yangName": "threshold-margin-ppm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "ageHistogramIntervalMinutes", 
            "yangName": "age-histogram-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "onlyIfRangeOverlaps", 
            "yangName": "only-if-range-overlaps", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "useContentItemSize", 
            "yangName": "use-content-item-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "thresholdPpm", 
            "yangName": "threshold-ppm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "continueOnceStarted", 
            "yangName": "continue-once-started", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pastVolumeAttenuationIntervalMinutes", 
            "yangName": "past-volume-attenuation-interval-minutes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


