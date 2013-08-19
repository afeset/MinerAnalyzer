


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


from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorOperationalStatusReasonType


class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.maximumCriticalRequested = False
        self.maximumCritical = None
        self.maximumCriticalSet = False
        
        self.operationalStatusRequested = False
        self.operationalStatus = None
        self.operationalStatusSet = False
        
        self.temperatureRequested = False
        self.temperature = None
        self.temperatureSet = False
        
        self.minimumWarningRequested = False
        self.minimumWarning = None
        self.minimumWarningSet = False
        
        self.minimumCriticalRequested = False
        self.minimumCritical = None
        self.minimumCriticalSet = False
        
        self.locationRequested = False
        self.location = None
        self.locationSet = False
        
        self.maximumWarningRequested = False
        self.maximumWarning = None
        self.maximumWarningSet = False
        
        self.operationalStatusReasonRequested = False
        self.operationalStatusReason = None
        self.operationalStatusReasonSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestMaximumCritical(True)
        
        self.requestOperationalStatus(True)
        
        self.requestTemperature(True)
        
        self.requestMinimumWarning(True)
        
        self.requestMinimumCritical(True)
        
        self.requestLocation(True)
        
        self.requestMaximumWarning(True)
        
        self.requestOperationalStatusReason(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestMaximumCritical(False)
        
        self.requestOperationalStatus(False)
        
        self.requestTemperature(False)
        
        self.requestMinimumWarning(False)
        
        self.requestMinimumCritical(False)
        
        self.requestLocation(False)
        
        self.requestMaximumWarning(False)
        
        self.requestOperationalStatusReason(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestMaximumCritical(True)
        
        self.requestOperationalStatus(True)
        
        self.requestTemperature(True)
        
        self.requestMinimumWarning(True)
        
        self.requestMinimumCritical(True)
        
        self.requestLocation(True)
        
        self.requestMaximumWarning(True)
        
        self.requestOperationalStatusReason(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestMaximumCritical(False)
        
        self.requestOperationalStatus(False)
        
        self.requestTemperature(False)
        
        self.requestMinimumWarning(False)
        
        self.requestMinimumCritical(False)
        
        self.requestLocation(False)
        
        self.requestMaximumWarning(False)
        
        self.requestOperationalStatusReason(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , sensor
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(sensor, trxContext)

    def read (self
              , sensor
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(sensor, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , sensor
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(sensor, 
                                  True,
                                  trxContext)



    def requestMaximumCritical (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maximumcritical').debug3Func(): logFunc('called. requested=%s', requested)
        self.maximumCriticalRequested = requested
        self.maximumCriticalSet = False

    def isMaximumCriticalRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maximumcritical-requested').debug3Func(): logFunc('called. requested=%s', self.maximumCriticalRequested)
        return self.maximumCriticalRequested

    def getMaximumCritical (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maximumcritical').debug3Func(): logFunc('called. self.maximumCriticalSet=%s, self.maximumCritical=%s', self.maximumCriticalSet, self.maximumCritical)
        if self.maximumCriticalSet:
            return self.maximumCritical
        return None

    def hasMaximumCritical (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maximumcritical').debug3Func(): logFunc('called. self.maximumCriticalSet=%s, self.maximumCritical=%s', self.maximumCriticalSet, self.maximumCritical)
        if self.maximumCriticalSet:
            return True
        return False

    def setMaximumCritical (self, maximumCritical):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maximumcritical').debug3Func(): logFunc('called. maximumCritical=%s, old=%s', maximumCritical, self.maximumCritical)
        self.maximumCriticalSet = True
        self.maximumCritical = maximumCritical

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

    def requestTemperature (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-temperature').debug3Func(): logFunc('called. requested=%s', requested)
        self.temperatureRequested = requested
        self.temperatureSet = False

    def isTemperatureRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-temperature-requested').debug3Func(): logFunc('called. requested=%s', self.temperatureRequested)
        return self.temperatureRequested

    def getTemperature (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-temperature').debug3Func(): logFunc('called. self.temperatureSet=%s, self.temperature=%s', self.temperatureSet, self.temperature)
        if self.temperatureSet:
            return self.temperature
        return None

    def hasTemperature (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-temperature').debug3Func(): logFunc('called. self.temperatureSet=%s, self.temperature=%s', self.temperatureSet, self.temperature)
        if self.temperatureSet:
            return True
        return False

    def setTemperature (self, temperature):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-temperature').debug3Func(): logFunc('called. temperature=%s, old=%s', temperature, self.temperature)
        self.temperatureSet = True
        self.temperature = temperature

    def requestMinimumWarning (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-minimumwarning').debug3Func(): logFunc('called. requested=%s', requested)
        self.minimumWarningRequested = requested
        self.minimumWarningSet = False

    def isMinimumWarningRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-minimumwarning-requested').debug3Func(): logFunc('called. requested=%s', self.minimumWarningRequested)
        return self.minimumWarningRequested

    def getMinimumWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-minimumwarning').debug3Func(): logFunc('called. self.minimumWarningSet=%s, self.minimumWarning=%s', self.minimumWarningSet, self.minimumWarning)
        if self.minimumWarningSet:
            return self.minimumWarning
        return None

    def hasMinimumWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-minimumwarning').debug3Func(): logFunc('called. self.minimumWarningSet=%s, self.minimumWarning=%s', self.minimumWarningSet, self.minimumWarning)
        if self.minimumWarningSet:
            return True
        return False

    def setMinimumWarning (self, minimumWarning):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-minimumwarning').debug3Func(): logFunc('called. minimumWarning=%s, old=%s', minimumWarning, self.minimumWarning)
        self.minimumWarningSet = True
        self.minimumWarning = minimumWarning

    def requestMinimumCritical (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-minimumcritical').debug3Func(): logFunc('called. requested=%s', requested)
        self.minimumCriticalRequested = requested
        self.minimumCriticalSet = False

    def isMinimumCriticalRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-minimumcritical-requested').debug3Func(): logFunc('called. requested=%s', self.minimumCriticalRequested)
        return self.minimumCriticalRequested

    def getMinimumCritical (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-minimumcritical').debug3Func(): logFunc('called. self.minimumCriticalSet=%s, self.minimumCritical=%s', self.minimumCriticalSet, self.minimumCritical)
        if self.minimumCriticalSet:
            return self.minimumCritical
        return None

    def hasMinimumCritical (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-minimumcritical').debug3Func(): logFunc('called. self.minimumCriticalSet=%s, self.minimumCritical=%s', self.minimumCriticalSet, self.minimumCritical)
        if self.minimumCriticalSet:
            return True
        return False

    def setMinimumCritical (self, minimumCritical):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-minimumcritical').debug3Func(): logFunc('called. minimumCritical=%s, old=%s', minimumCritical, self.minimumCritical)
        self.minimumCriticalSet = True
        self.minimumCritical = minimumCritical

    def requestLocation (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-location').debug3Func(): logFunc('called. requested=%s', requested)
        self.locationRequested = requested
        self.locationSet = False

    def isLocationRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-location-requested').debug3Func(): logFunc('called. requested=%s', self.locationRequested)
        return self.locationRequested

    def getLocation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-location').debug3Func(): logFunc('called. self.locationSet=%s, self.location=%s', self.locationSet, self.location)
        if self.locationSet:
            return self.location
        return None

    def hasLocation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-location').debug3Func(): logFunc('called. self.locationSet=%s, self.location=%s', self.locationSet, self.location)
        if self.locationSet:
            return True
        return False

    def setLocation (self, location):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-location').debug3Func(): logFunc('called. location=%s, old=%s', location, self.location)
        self.locationSet = True
        self.location = location

    def requestMaximumWarning (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maximumwarning').debug3Func(): logFunc('called. requested=%s', requested)
        self.maximumWarningRequested = requested
        self.maximumWarningSet = False

    def isMaximumWarningRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maximumwarning-requested').debug3Func(): logFunc('called. requested=%s', self.maximumWarningRequested)
        return self.maximumWarningRequested

    def getMaximumWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maximumwarning').debug3Func(): logFunc('called. self.maximumWarningSet=%s, self.maximumWarning=%s', self.maximumWarningSet, self.maximumWarning)
        if self.maximumWarningSet:
            return self.maximumWarning
        return None

    def hasMaximumWarning (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maximumwarning').debug3Func(): logFunc('called. self.maximumWarningSet=%s, self.maximumWarning=%s', self.maximumWarningSet, self.maximumWarning)
        if self.maximumWarningSet:
            return True
        return False

    def setMaximumWarning (self, maximumWarning):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maximumwarning').debug3Func(): logFunc('called. maximumWarning=%s, old=%s', maximumWarning, self.maximumWarning)
        self.maximumWarningSet = True
        self.maximumWarning = maximumWarning

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.maximumCritical = 0
        self.maximumCriticalSet = False
        
        self.operationalStatus = 0
        self.operationalStatusSet = False
        
        self.temperature = 0
        self.temperatureSet = False
        
        self.minimumWarning = 0
        self.minimumWarningSet = False
        
        self.minimumCritical = 0
        self.minimumCriticalSet = False
        
        self.location = 0
        self.locationSet = False
        
        self.maximumWarning = 0
        self.maximumWarningSet = False
        
        self.operationalStatusReason = 0
        self.operationalStatusReasonSet = False
        

    def _getSelfKeyPath (self, sensor
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", "qt-pltf-temperature"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(sensor);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("sensor", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", "qt-pltf-temperature"))
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
                        sensor, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(sensor, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(sensor, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       sensor, 
                       
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

        keyPath = self._getSelfKeyPath(sensor, 
                                       
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
                               sensor, 
                               
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

        
        if self.isMaximumCriticalRequested():
            valMaximumCritical = Value()
            valMaximumCritical.setEmpty()
            tagValueList.push(("maximum-critical", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valMaximumCritical)
        
        if self.isOperationalStatusRequested():
            valOperationalStatus = Value()
            valOperationalStatus.setEmpty()
            tagValueList.push(("operational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valOperationalStatus)
        
        if self.isTemperatureRequested():
            valTemperature = Value()
            valTemperature.setEmpty()
            tagValueList.push(("temperature", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valTemperature)
        
        if self.isMinimumWarningRequested():
            valMinimumWarning = Value()
            valMinimumWarning.setEmpty()
            tagValueList.push(("minimum-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valMinimumWarning)
        
        if self.isMinimumCriticalRequested():
            valMinimumCritical = Value()
            valMinimumCritical.setEmpty()
            tagValueList.push(("minimum-critical", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valMinimumCritical)
        
        if self.isLocationRequested():
            valLocation = Value()
            valLocation.setEmpty()
            tagValueList.push(("location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valLocation)
        
        if self.isMaximumWarningRequested():
            valMaximumWarning = Value()
            valMaximumWarning.setEmpty()
            tagValueList.push(("maximum-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valMaximumWarning)
        
        if self.isOperationalStatusReasonRequested():
            valOperationalStatusReason = Value()
            valOperationalStatusReason.setEmpty()
            tagValueList.push(("operational-status-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valOperationalStatusReason)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isMaximumCriticalRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "maximum-critical") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maximumcritical').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maximumCritical", "maximum-critical", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-maximum-critical-bad-value').infoFunc(): logFunc('maximumCritical not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaximumCritical(tempVar)
            for logFunc in self._log('read-tag-values-maximum-critical').debug3Func(): logFunc('read maximumCritical. maximumCritical=%s, tempValue=%s', self.maximumCritical, tempValue.getType())
        
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
        
        if self.isTemperatureRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temperature") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-temperature').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "temperature", "temperature", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temperature-bad-value').infoFunc(): logFunc('temperature not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTemperature(tempVar)
            for logFunc in self._log('read-tag-values-temperature').debug3Func(): logFunc('read temperature. temperature=%s, tempValue=%s', self.temperature, tempValue.getType())
        
        if self.isMinimumWarningRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "minimum-warning") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-minimumwarning').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "minimumWarning", "minimum-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-minimum-warning-bad-value').infoFunc(): logFunc('minimumWarning not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMinimumWarning(tempVar)
            for logFunc in self._log('read-tag-values-minimum-warning').debug3Func(): logFunc('read minimumWarning. minimumWarning=%s, tempValue=%s', self.minimumWarning, tempValue.getType())
        
        if self.isMinimumCriticalRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "minimum-critical") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-minimumcritical').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "minimumCritical", "minimum-critical", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-minimum-critical-bad-value').infoFunc(): logFunc('minimumCritical not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMinimumCritical(tempVar)
            for logFunc in self._log('read-tag-values-minimum-critical').debug3Func(): logFunc('read minimumCritical. minimumCritical=%s, tempValue=%s', self.minimumCritical, tempValue.getType())
        
        if self.isLocationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "location") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-location').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "location", "location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-location-bad-value').infoFunc(): logFunc('location not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLocation(tempVar)
            for logFunc in self._log('read-tag-values-location').debug3Func(): logFunc('read location. location=%s, tempValue=%s', self.location, tempValue.getType())
        
        if self.isMaximumWarningRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "maximum-warning") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maximumwarning').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maximumWarning", "maximum-warning", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-maximum-warning-bad-value').infoFunc(): logFunc('maximumWarning not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaximumWarning(tempVar)
            for logFunc in self._log('read-tag-values-maximum-warning').debug3Func(): logFunc('read maximumWarning. maximumWarning=%s, tempValue=%s', self.maximumWarning, tempValue.getType())
        
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
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.status.status_maapi_gen import StatusMaapi", 
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
            "isCurrent": false, 
            "yangName": "sensor", 
            "namespace": "sensor", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "keyLeaf": {
                "varName": "sensor", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "sensor"
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "maximumCritical", 
            "yangName": "maximum-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "temperature", 
            "yangName": "temperature", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minimumWarning", 
            "yangName": "minimum-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minimumCritical", 
            "yangName": "minimum-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maximumWarning", 
            "yangName": "maximum-warning", 
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
            "memberName": "maximumCritical", 
            "yangName": "maximum-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "temperature", 
            "yangName": "temperature", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minimumWarning", 
            "yangName": "minimum-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "minimumCritical", 
            "yangName": "minimum-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maximumWarning", 
            "yangName": "maximum-warning", 
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
        }
    ], 
    "createTime": "2013"
}
"""


