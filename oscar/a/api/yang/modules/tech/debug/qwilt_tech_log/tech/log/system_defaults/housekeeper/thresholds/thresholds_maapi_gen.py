


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

        

        
        self.pollLatencyErrorSecondsRequested = False
        self.pollLatencyErrorSeconds = None
        self.pollLatencyErrorSecondsSet = False
        
        self.pollLatencyWarningSecondsRequested = False
        self.pollLatencyWarningSeconds = None
        self.pollLatencyWarningSecondsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPollLatencyErrorSeconds(True)
        
        self.requestPollLatencyWarningSeconds(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPollLatencyErrorSeconds(True)
        
        self.requestPollLatencyWarningSeconds(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPollLatencyErrorSeconds(False)
        
        self.requestPollLatencyWarningSeconds(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestPollLatencyErrorSeconds(False)
        
        self.requestPollLatencyWarningSeconds(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setPollLatencyErrorSeconds(None)
        self.pollLatencyErrorSecondsSet = False
        
        self.setPollLatencyWarningSeconds(None)
        self.pollLatencyWarningSecondsSet = False
        
        

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



    def requestPollLatencyErrorSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-polllatencyerrorseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollLatencyErrorSecondsRequested = requested
        self.pollLatencyErrorSecondsSet = False

    def isPollLatencyErrorSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-polllatencyerrorseconds-requested').debug3Func(): logFunc('called. requested=%s', self.pollLatencyErrorSecondsRequested)
        return self.pollLatencyErrorSecondsRequested

    def getPollLatencyErrorSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-polllatencyerrorseconds').debug3Func(): logFunc('called. self.pollLatencyErrorSecondsSet=%s, self.pollLatencyErrorSeconds=%s', self.pollLatencyErrorSecondsSet, self.pollLatencyErrorSeconds)
        if self.pollLatencyErrorSecondsSet:
            return self.pollLatencyErrorSeconds
        return None

    def hasPollLatencyErrorSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-polllatencyerrorseconds').debug3Func(): logFunc('called. self.pollLatencyErrorSecondsSet=%s, self.pollLatencyErrorSeconds=%s', self.pollLatencyErrorSecondsSet, self.pollLatencyErrorSeconds)
        if self.pollLatencyErrorSecondsSet:
            return True
        return False

    def setPollLatencyErrorSeconds (self, pollLatencyErrorSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-polllatencyerrorseconds').debug3Func(): logFunc('called. pollLatencyErrorSeconds=%s, old=%s', pollLatencyErrorSeconds, self.pollLatencyErrorSeconds)
        self.pollLatencyErrorSecondsSet = True
        self.pollLatencyErrorSeconds = pollLatencyErrorSeconds

    def requestPollLatencyWarningSeconds (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-polllatencywarningseconds').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollLatencyWarningSecondsRequested = requested
        self.pollLatencyWarningSecondsSet = False

    def isPollLatencyWarningSecondsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-polllatencywarningseconds-requested').debug3Func(): logFunc('called. requested=%s', self.pollLatencyWarningSecondsRequested)
        return self.pollLatencyWarningSecondsRequested

    def getPollLatencyWarningSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-polllatencywarningseconds').debug3Func(): logFunc('called. self.pollLatencyWarningSecondsSet=%s, self.pollLatencyWarningSeconds=%s', self.pollLatencyWarningSecondsSet, self.pollLatencyWarningSeconds)
        if self.pollLatencyWarningSecondsSet:
            return self.pollLatencyWarningSeconds
        return None

    def hasPollLatencyWarningSeconds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-polllatencywarningseconds').debug3Func(): logFunc('called. self.pollLatencyWarningSecondsSet=%s, self.pollLatencyWarningSeconds=%s', self.pollLatencyWarningSecondsSet, self.pollLatencyWarningSeconds)
        if self.pollLatencyWarningSecondsSet:
            return True
        return False

    def setPollLatencyWarningSeconds (self, pollLatencyWarningSeconds):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-polllatencywarningseconds').debug3Func(): logFunc('called. pollLatencyWarningSeconds=%s, old=%s', pollLatencyWarningSeconds, self.pollLatencyWarningSeconds)
        self.pollLatencyWarningSecondsSet = True
        self.pollLatencyWarningSeconds = pollLatencyWarningSeconds


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.pollLatencyErrorSeconds = 0
        self.pollLatencyErrorSecondsSet = False
        
        self.pollLatencyWarningSeconds = 0
        self.pollLatencyWarningSecondsSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
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

        
        if self.hasPollLatencyErrorSeconds():
            valPollLatencyErrorSeconds = Value()
            if self.pollLatencyErrorSeconds is not None:
                valPollLatencyErrorSeconds.setInt64(self.pollLatencyErrorSeconds)
            else:
                valPollLatencyErrorSeconds.setEmpty()
            tagValueList.push(("poll-latency-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPollLatencyErrorSeconds)
        
        if self.hasPollLatencyWarningSeconds():
            valPollLatencyWarningSeconds = Value()
            if self.pollLatencyWarningSeconds is not None:
                valPollLatencyWarningSeconds.setInt64(self.pollLatencyWarningSeconds)
            else:
                valPollLatencyWarningSeconds.setEmpty()
            tagValueList.push(("poll-latency-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPollLatencyWarningSeconds)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isPollLatencyErrorSecondsRequested():
            valPollLatencyErrorSeconds = Value()
            valPollLatencyErrorSeconds.setEmpty()
            tagValueList.push(("poll-latency-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPollLatencyErrorSeconds)
        
        if self.isPollLatencyWarningSecondsRequested():
            valPollLatencyWarningSeconds = Value()
            valPollLatencyWarningSeconds.setEmpty()
            tagValueList.push(("poll-latency-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valPollLatencyWarningSeconds)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isPollLatencyErrorSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-latency-error-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-polllatencyerrorseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollLatencyErrorSeconds", "poll-latency-error-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-latency-error-seconds-bad-value').infoFunc(): logFunc('pollLatencyErrorSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollLatencyErrorSeconds(tempVar)
            for logFunc in self._log('read-tag-values-poll-latency-error-seconds').debug3Func(): logFunc('read pollLatencyErrorSeconds. pollLatencyErrorSeconds=%s, tempValue=%s', self.pollLatencyErrorSeconds, tempValue.getType())
        
        if self.isPollLatencyWarningSecondsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "poll-latency-warning-seconds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-polllatencywarningseconds').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pollLatencyWarningSeconds", "poll-latency-warning-seconds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-poll-latency-warning-seconds-bad-value').infoFunc(): logFunc('pollLatencyWarningSeconds not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPollLatencyWarningSeconds(tempVar)
            for logFunc in self._log('read-tag-values-poll-latency-warning-seconds').debug3Func(): logFunc('read pollLatencyWarningSeconds. pollLatencyWarningSeconds=%s, tempValue=%s', self.pollLatencyWarningSeconds, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "thresholds", 
        "namespace": "thresholds", 
        "className": "ThresholdsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.system_defaults.housekeeper.thresholds.thresholds_maapi_gen import ThresholdsMaapi", 
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
            "memberName": "pollLatencyErrorSeconds", 
            "yangName": "poll-latency-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarningSeconds", 
            "yangName": "poll-latency-warning-seconds", 
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
            "memberName": "pollLatencyErrorSeconds", 
            "yangName": "poll-latency-error-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarningSeconds", 
            "yangName": "poll-latency-warning-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


