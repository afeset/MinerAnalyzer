


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

from status_maapi_base_gen import StatusMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureOperationalStatusType


class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.operationalStatusRequested = False
        self.operationalStatus = None
        self.operationalStatusSet = False
        
        self.operationalStatusReasonRequested = False
        self.operationalStatusReason = None
        self.operationalStatusReasonSet = False
        
        self.temperatureStatusRawRequested = False
        self.temperatureStatusRaw = None
        self.temperatureStatusRawSet = False
        
        self.temperatureStatusRequested = False
        self.temperatureStatus = None
        self.temperatureStatusSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOperationalStatus(True)
        
        self.requestOperationalStatusReason(True)
        
        self.requestTemperatureStatusRaw(True)
        
        self.requestTemperatureStatus(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOperationalStatus(False)
        
        self.requestOperationalStatusReason(False)
        
        self.requestTemperatureStatusRaw(False)
        
        self.requestTemperatureStatus(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOperationalStatus(True)
        
        self.requestOperationalStatusReason(True)
        
        self.requestTemperatureStatusRaw(True)
        
        self.requestTemperatureStatus(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOperationalStatus(False)
        
        self.requestOperationalStatusReason(False)
        
        self.requestTemperatureStatusRaw(False)
        
        self.requestTemperatureStatus(False)
        
        

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



    def requestOperationalStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-operationalstatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.operationalStatusRequested = requested
        self.operationalStatusSet = False

    def isOperationalStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-operationalstatus-requested').debug3Func(): logFunc('called. requested=%s', self.operationalStatusRequested)
        return self.operationalStatusRequested

    def getOperationalStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-operationalstatus').debug3Func(): logFunc('called. self.operationalStatusSet=%s, self.operationalStatus=%s', self.operationalStatusSet, self.operationalStatus)
        if self.operationalStatusSet:
            return self.operationalStatus
        return None

    def hasOperationalStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-operationalstatus').debug3Func(): logFunc('called. self.operationalStatusSet=%s, self.operationalStatus=%s', self.operationalStatusSet, self.operationalStatus)
        if self.operationalStatusSet:
            return True
        return False

    def setOperationalStatus (self, operationalStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-operationalstatus').debug3Func(): logFunc('called. operationalStatus=%s, old=%s', operationalStatus, self.operationalStatus)
        self.operationalStatusSet = True
        self.operationalStatus = operationalStatus

    def requestOperationalStatusReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-operationalstatusreason').debug3Func(): logFunc('called. requested=%s', requested)
        self.operationalStatusReasonRequested = requested
        self.operationalStatusReasonSet = False

    def isOperationalStatusReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-operationalstatusreason-requested').debug3Func(): logFunc('called. requested=%s', self.operationalStatusReasonRequested)
        return self.operationalStatusReasonRequested

    def getOperationalStatusReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-operationalstatusreason').debug3Func(): logFunc('called. self.operationalStatusReasonSet=%s, self.operationalStatusReason=%s', self.operationalStatusReasonSet, self.operationalStatusReason)
        if self.operationalStatusReasonSet:
            return self.operationalStatusReason
        return None

    def hasOperationalStatusReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-operationalstatusreason').debug3Func(): logFunc('called. self.operationalStatusReasonSet=%s, self.operationalStatusReason=%s', self.operationalStatusReasonSet, self.operationalStatusReason)
        if self.operationalStatusReasonSet:
            return True
        return False

    def setOperationalStatusReason (self, operationalStatusReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-operationalstatusreason').debug3Func(): logFunc('called. operationalStatusReason=%s, old=%s', operationalStatusReason, self.operationalStatusReason)
        self.operationalStatusReasonSet = True
        self.operationalStatusReason = operationalStatusReason

    def requestTemperatureStatusRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-temperaturestatusraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.temperatureStatusRawRequested = requested
        self.temperatureStatusRawSet = False

    def isTemperatureStatusRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-temperaturestatusraw-requested').debug3Func(): logFunc('called. requested=%s', self.temperatureStatusRawRequested)
        return self.temperatureStatusRawRequested

    def getTemperatureStatusRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-temperaturestatusraw').debug3Func(): logFunc('called. self.temperatureStatusRawSet=%s, self.temperatureStatusRaw=%s', self.temperatureStatusRawSet, self.temperatureStatusRaw)
        if self.temperatureStatusRawSet:
            return self.temperatureStatusRaw
        return None

    def hasTemperatureStatusRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-temperaturestatusraw').debug3Func(): logFunc('called. self.temperatureStatusRawSet=%s, self.temperatureStatusRaw=%s', self.temperatureStatusRawSet, self.temperatureStatusRaw)
        if self.temperatureStatusRawSet:
            return True
        return False

    def setTemperatureStatusRaw (self, temperatureStatusRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-temperaturestatusraw').debug3Func(): logFunc('called. temperatureStatusRaw=%s, old=%s', temperatureStatusRaw, self.temperatureStatusRaw)
        self.temperatureStatusRawSet = True
        self.temperatureStatusRaw = temperatureStatusRaw

    def requestTemperatureStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-temperaturestatus').debug3Func(): logFunc('called. requested=%s', requested)
        self.temperatureStatusRequested = requested
        self.temperatureStatusSet = False

    def isTemperatureStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-temperaturestatus-requested').debug3Func(): logFunc('called. requested=%s', self.temperatureStatusRequested)
        return self.temperatureStatusRequested

    def getTemperatureStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-temperaturestatus').debug3Func(): logFunc('called. self.temperatureStatusSet=%s, self.temperatureStatus=%s', self.temperatureStatusSet, self.temperatureStatus)
        if self.temperatureStatusSet:
            return self.temperatureStatus
        return None

    def hasTemperatureStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-temperaturestatus').debug3Func(): logFunc('called. self.temperatureStatusSet=%s, self.temperatureStatus=%s', self.temperatureStatusSet, self.temperatureStatus)
        if self.temperatureStatusSet:
            return True
        return False

    def setTemperatureStatus (self, temperatureStatus):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-temperaturestatus').debug3Func(): logFunc('called. temperatureStatus=%s, old=%s', temperatureStatus, self.temperatureStatus)
        self.temperatureStatusSet = True
        self.temperatureStatus = temperatureStatus


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.operationalStatus = 0
        self.operationalStatusSet = False
        
        self.operationalStatusReason = 0
        self.operationalStatusReasonSet = False
        
        self.temperatureStatusRaw = 0
        self.temperatureStatusRawSet = False
        
        self.temperatureStatus = 0
        self.temperatureStatusSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", "qt-pltf-temperature"))
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

        
        if self.isOperationalStatusRequested():
            valOperationalStatus = Value()
            valOperationalStatus.setEmpty()
            tagValueList.push(("operational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valOperationalStatus)
        
        if self.isOperationalStatusReasonRequested():
            valOperationalStatusReason = Value()
            valOperationalStatusReason.setEmpty()
            tagValueList.push(("operational-status-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valOperationalStatusReason)
        
        if self.isTemperatureStatusRawRequested():
            valTemperatureStatusRaw = Value()
            valTemperatureStatusRaw.setEmpty()
            tagValueList.push(("temperature-status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valTemperatureStatusRaw)
        
        if self.isTemperatureStatusRequested():
            valTemperatureStatus = Value()
            valTemperatureStatus.setEmpty()
            tagValueList.push(("temperature-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valTemperatureStatus)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isOperationalStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "operational-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-operationalstatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "operationalStatus", "operational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-operational-status-bad-value').infoFunc(): logFunc('operationalStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOperationalStatus(tempVar)
            for logFunc in self._log('read-tag-values-operational-status').debug3Func(): logFunc('read operationalStatus. operationalStatus=%s, tempValue=%s', self.operationalStatus, tempValue.getType())
        
        if self.isOperationalStatusReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "operational-status-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-operationalstatusreason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "operationalStatusReason", "operational-status-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-operational-status-reason-bad-value').infoFunc(): logFunc('operationalStatusReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOperationalStatusReason(tempVar)
            for logFunc in self._log('read-tag-values-operational-status-reason').debug3Func(): logFunc('read operationalStatusReason. operationalStatusReason=%s, tempValue=%s', self.operationalStatusReason, tempValue.getType())
        
        if self.isTemperatureStatusRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temperature-status-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-temperaturestatusraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "temperatureStatusRaw", "temperature-status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temperature-status-raw-bad-value').infoFunc(): logFunc('temperatureStatusRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTemperatureStatusRaw(tempVar)
            for logFunc in self._log('read-tag-values-temperature-status-raw').debug3Func(): logFunc('read temperatureStatusRaw. temperatureStatusRaw=%s, tempValue=%s', self.temperatureStatusRaw, tempValue.getType())
        
        if self.isTemperatureStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temperature-status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-temperaturestatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "temperatureStatus", "temperature-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temperature-status-bad-value').infoFunc(): logFunc('temperatureStatus not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTemperatureStatus(tempVar)
            for logFunc in self._log('read-tag-values-temperature-status').debug3Func(): logFunc('read temperatureStatus. temperatureStatus=%s, tempValue=%s', self.temperatureStatus, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
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
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "temperatureStatusRaw", 
            "yangName": "temperature-status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "temperatureStatus", 
            "yangName": "temperature-status", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "temperatureStatusRaw", 
            "yangName": "temperature-status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "temperatureStatus", 
            "yangName": "temperature-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


