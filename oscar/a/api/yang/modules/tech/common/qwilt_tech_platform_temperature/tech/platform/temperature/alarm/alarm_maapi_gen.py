


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


from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureAlarmReasonType


class BlinkyAlarmMaapi(AlarmMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-alarm")
        self.domain = None

        

        
        self.countRequested = False
        self.count = None
        self.countSet = False
        
        self.temperatureWarningRequested = False
        self.temperatureWarning = None
        self.temperatureWarningSet = False
        
        self.temperatureCriticalRequested = False
        self.temperatureCritical = None
        self.temperatureCriticalSet = False
        
        self.temperatureCriticalReasonRequested = False
        self.temperatureCriticalReason = None
        self.temperatureCriticalReasonSet = False
        
        self.temperatureWarningReasonRequested = False
        self.temperatureWarningReason = None
        self.temperatureWarningReasonSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestCount(True)
        
        self.requestTemperatureWarning(True)
        
        self.requestTemperatureCritical(True)
        
        self.requestTemperatureCriticalReason(True)
        
        self.requestTemperatureWarningReason(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestCount(False)
        
        self.requestTemperatureWarning(False)
        
        self.requestTemperatureCritical(False)
        
        self.requestTemperatureCriticalReason(False)
        
        self.requestTemperatureWarningReason(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestCount(True)
        
        self.requestTemperatureWarning(True)
        
        self.requestTemperatureCritical(True)
        
        self.requestTemperatureCriticalReason(True)
        
        self.requestTemperatureWarningReason(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestCount(False)
        
        self.requestTemperatureWarning(False)
        
        self.requestTemperatureCritical(False)
        
        self.requestTemperatureCriticalReason(False)
        
        self.requestTemperatureWarningReason(False)
        
        

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



    def requestCount (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-count').debug3Func(): logFunc('called. requested=%s', requested)
        self.countRequested = requested
        self.countSet = False

    def isCountRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-count-requested').debug3Func(): logFunc('called. requested=%s', self.countRequested)
        return self.countRequested

    def getCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-count').debug3Func(): logFunc('called. self.countSet=%s, self.count=%s', self.countSet, self.count)
        if self.countSet:
            return self.count
        return None

    def hasCount (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-count').debug3Func(): logFunc('called. self.countSet=%s, self.count=%s', self.countSet, self.count)
        if self.countSet:
            return True
        return False

    def setCount (self, count):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-count').debug3Func(): logFunc('called. count=%s, old=%s', count, self.count)
        self.countSet = True
        self.count = count

    def requestTemperatureWarning (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-temperaturewarning').debug3Func(): logFunc('called. requested=%s', requested)
        self.temperatureWarningRequested = requested
        self.temperatureWarningSet = False

    def isTemperatureWarningRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-temperaturewarning-requested').debug3Func(): logFunc('called. requested=%s', self.temperatureWarningRequested)
        return self.temperatureWarningRequested

    def getTemperatureWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-temperaturewarning').debug3Func(): logFunc('called. self.temperatureWarningSet=%s, self.temperatureWarning=%s', self.temperatureWarningSet, self.temperatureWarning)
        if self.temperatureWarningSet:
            return self.temperatureWarning
        return None

    def hasTemperatureWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-temperaturewarning').debug3Func(): logFunc('called. self.temperatureWarningSet=%s, self.temperatureWarning=%s', self.temperatureWarningSet, self.temperatureWarning)
        if self.temperatureWarningSet:
            return True
        return False

    def setTemperatureWarning (self, temperatureWarning):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-temperaturewarning').debug3Func(): logFunc('called. temperatureWarning=%s, old=%s', temperatureWarning, self.temperatureWarning)
        self.temperatureWarningSet = True
        self.temperatureWarning = temperatureWarning

    def requestTemperatureCritical (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-temperaturecritical').debug3Func(): logFunc('called. requested=%s', requested)
        self.temperatureCriticalRequested = requested
        self.temperatureCriticalSet = False

    def isTemperatureCriticalRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-temperaturecritical-requested').debug3Func(): logFunc('called. requested=%s', self.temperatureCriticalRequested)
        return self.temperatureCriticalRequested

    def getTemperatureCritical (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-temperaturecritical').debug3Func(): logFunc('called. self.temperatureCriticalSet=%s, self.temperatureCritical=%s', self.temperatureCriticalSet, self.temperatureCritical)
        if self.temperatureCriticalSet:
            return self.temperatureCritical
        return None

    def hasTemperatureCritical (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-temperaturecritical').debug3Func(): logFunc('called. self.temperatureCriticalSet=%s, self.temperatureCritical=%s', self.temperatureCriticalSet, self.temperatureCritical)
        if self.temperatureCriticalSet:
            return True
        return False

    def setTemperatureCritical (self, temperatureCritical):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-temperaturecritical').debug3Func(): logFunc('called. temperatureCritical=%s, old=%s', temperatureCritical, self.temperatureCritical)
        self.temperatureCriticalSet = True
        self.temperatureCritical = temperatureCritical

    def requestTemperatureCriticalReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-temperaturecriticalreason').debug3Func(): logFunc('called. requested=%s', requested)
        self.temperatureCriticalReasonRequested = requested
        self.temperatureCriticalReasonSet = False

    def isTemperatureCriticalReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-temperaturecriticalreason-requested').debug3Func(): logFunc('called. requested=%s', self.temperatureCriticalReasonRequested)
        return self.temperatureCriticalReasonRequested

    def getTemperatureCriticalReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-temperaturecriticalreason').debug3Func(): logFunc('called. self.temperatureCriticalReasonSet=%s, self.temperatureCriticalReason=%s', self.temperatureCriticalReasonSet, self.temperatureCriticalReason)
        if self.temperatureCriticalReasonSet:
            return self.temperatureCriticalReason
        return None

    def hasTemperatureCriticalReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-temperaturecriticalreason').debug3Func(): logFunc('called. self.temperatureCriticalReasonSet=%s, self.temperatureCriticalReason=%s', self.temperatureCriticalReasonSet, self.temperatureCriticalReason)
        if self.temperatureCriticalReasonSet:
            return True
        return False

    def setTemperatureCriticalReason (self, temperatureCriticalReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-temperaturecriticalreason').debug3Func(): logFunc('called. temperatureCriticalReason=%s, old=%s', temperatureCriticalReason, self.temperatureCriticalReason)
        self.temperatureCriticalReasonSet = True
        self.temperatureCriticalReason = temperatureCriticalReason

    def requestTemperatureWarningReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-temperaturewarningreason').debug3Func(): logFunc('called. requested=%s', requested)
        self.temperatureWarningReasonRequested = requested
        self.temperatureWarningReasonSet = False

    def isTemperatureWarningReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-temperaturewarningreason-requested').debug3Func(): logFunc('called. requested=%s', self.temperatureWarningReasonRequested)
        return self.temperatureWarningReasonRequested

    def getTemperatureWarningReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-temperaturewarningreason').debug3Func(): logFunc('called. self.temperatureWarningReasonSet=%s, self.temperatureWarningReason=%s', self.temperatureWarningReasonSet, self.temperatureWarningReason)
        if self.temperatureWarningReasonSet:
            return self.temperatureWarningReason
        return None

    def hasTemperatureWarningReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-temperaturewarningreason').debug3Func(): logFunc('called. self.temperatureWarningReasonSet=%s, self.temperatureWarningReason=%s', self.temperatureWarningReasonSet, self.temperatureWarningReason)
        if self.temperatureWarningReasonSet:
            return True
        return False

    def setTemperatureWarningReason (self, temperatureWarningReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-temperaturewarningreason').debug3Func(): logFunc('called. temperatureWarningReason=%s, old=%s', temperatureWarningReason, self.temperatureWarningReason)
        self.temperatureWarningReasonSet = True
        self.temperatureWarningReason = temperatureWarningReason


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.count = 0
        self.countSet = False
        
        self.temperatureWarning = 0
        self.temperatureWarningSet = False
        
        self.temperatureCritical = 0
        self.temperatureCriticalSet = False
        
        self.temperatureCriticalReason = 0
        self.temperatureCriticalReasonSet = False
        
        self.temperatureWarningReason = 0
        self.temperatureWarningReasonSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", "qt-pltf-temperature"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("temperature", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", "qt-pltf-temperature"))
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

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isCountRequested():
            valCount = Value()
            valCount.setEmpty()
            tagValueList.push(("count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valCount)
        
        if self.isTemperatureWarningRequested():
            valTemperatureWarning = Value()
            valTemperatureWarning.setEmpty()
            tagValueList.push(("temperature-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valTemperatureWarning)
        
        if self.isTemperatureCriticalRequested():
            valTemperatureCritical = Value()
            valTemperatureCritical.setEmpty()
            tagValueList.push(("temperature-critical", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valTemperatureCritical)
        
        if self.isTemperatureCriticalReasonRequested():
            valTemperatureCriticalReason = Value()
            valTemperatureCriticalReason.setEmpty()
            tagValueList.push(("temperature-critical-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valTemperatureCriticalReason)
        
        if self.isTemperatureWarningReasonRequested():
            valTemperatureWarningReason = Value()
            valTemperatureWarningReason.setEmpty()
            tagValueList.push(("temperature-warning-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valTemperatureWarningReason)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isCountRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "count") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-count').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "count", "count", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-count-bad-value').infoFunc(): logFunc('count not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCount(tempVar)
            for logFunc in self._log('read-tag-values-count').debug3Func(): logFunc('read count. count=%s, tempValue=%s', self.count, tempValue.getType())
        
        if self.isTemperatureWarningRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temperature-warning") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-temperaturewarning').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "temperatureWarning", "temperature-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temperature-warning-bad-value').infoFunc(): logFunc('temperatureWarning not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTemperatureWarning(tempVar)
            for logFunc in self._log('read-tag-values-temperature-warning').debug3Func(): logFunc('read temperatureWarning. temperatureWarning=%s, tempValue=%s', self.temperatureWarning, tempValue.getType())
        
        if self.isTemperatureCriticalRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temperature-critical") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-temperaturecritical').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "temperatureCritical", "temperature-critical", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temperature-critical-bad-value').infoFunc(): logFunc('temperatureCritical not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTemperatureCritical(tempVar)
            for logFunc in self._log('read-tag-values-temperature-critical').debug3Func(): logFunc('read temperatureCritical. temperatureCritical=%s, tempValue=%s', self.temperatureCritical, tempValue.getType())
        
        if self.isTemperatureCriticalReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temperature-critical-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-temperaturecriticalreason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "temperatureCriticalReason", "temperature-critical-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temperature-critical-reason-bad-value').infoFunc(): logFunc('temperatureCriticalReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTemperatureCriticalReason(tempVar)
            for logFunc in self._log('read-tag-values-temperature-critical-reason').debug3Func(): logFunc('read temperatureCriticalReason. temperatureCriticalReason=%s, tempValue=%s', self.temperatureCriticalReason, tempValue.getType())
        
        if self.isTemperatureWarningReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temperature-warning-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-temperaturewarningreason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "temperatureWarningReason", "temperature-warning-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temperature-warning-reason-bad-value').infoFunc(): logFunc('temperatureWarningReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTemperatureWarningReason(tempVar)
            for logFunc in self._log('read-tag-values-temperature-warning-reason').debug3Func(): logFunc('read temperatureWarningReason. temperatureWarningReason=%s, tempValue=%s', self.temperatureWarningReason, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "alarm", 
        "namespace": "alarm", 
        "className": "AlarmMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.alarm.alarm_maapi_gen import AlarmMaapi", 
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
            "moduleYangNamespacePrefix": "qt-pltf", 
            "yangName": "platform", 
            "namespace": "platform", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform", 
            "name": "platform"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "yangName": "temperature", 
            "namespace": "temperature", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "name": "temperature"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "yangName": "alarm", 
            "namespace": "alarm", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "name": "alarm"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "count", 
            "yangName": "count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "temperatureWarning", 
            "yangName": "temperature-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "temperatureCritical", 
            "yangName": "temperature-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "temperatureCriticalReason", 
            "yangName": "temperature-critical-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "temperatureWarningReason", 
            "yangName": "temperature-warning-reason", 
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
            "qwilt_tech_platform_temperature"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "count", 
            "yangName": "count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "temperatureWarning", 
            "yangName": "temperature-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "temperatureCritical", 
            "yangName": "temperature-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "temperatureCriticalReason", 
            "yangName": "temperature-critical-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "temperatureWarningReason", 
            "yangName": "temperature-warning-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


