


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


from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorDeviceStatusType


class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.statusRequested = False
        self.status = None
        self.statusSet = False
        
        self.indexRequested = False
        self.index = None
        self.indexSet = False
        
        self.temperatureRawRequested = False
        self.temperatureRaw = None
        self.temperatureRawSet = False
        
        self.maximumCriticalRawRequested = False
        self.maximumCriticalRaw = None
        self.maximumCriticalRawSet = False
        
        self.maximumWarningRawRequested = False
        self.maximumWarningRaw = None
        self.maximumWarningRawSet = False
        
        self.minimumWarningRawRequested = False
        self.minimumWarningRaw = None
        self.minimumWarningRawSet = False
        
        self.minimumCriticalRawRequested = False
        self.minimumCriticalRaw = None
        self.minimumCriticalRawSet = False
        
        self.probeNameRequested = False
        self.probeName = None
        self.probeNameSet = False
        
        self.statusRawRequested = False
        self.statusRaw = None
        self.statusRawSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStatus(True)
        
        self.requestIndex(True)
        
        self.requestTemperatureRaw(True)
        
        self.requestMaximumCriticalRaw(True)
        
        self.requestMaximumWarningRaw(True)
        
        self.requestMinimumWarningRaw(True)
        
        self.requestMinimumCriticalRaw(True)
        
        self.requestProbeName(True)
        
        self.requestStatusRaw(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStatus(False)
        
        self.requestIndex(False)
        
        self.requestTemperatureRaw(False)
        
        self.requestMaximumCriticalRaw(False)
        
        self.requestMaximumWarningRaw(False)
        
        self.requestMinimumWarningRaw(False)
        
        self.requestMinimumCriticalRaw(False)
        
        self.requestProbeName(False)
        
        self.requestStatusRaw(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStatus(True)
        
        self.requestIndex(True)
        
        self.requestTemperatureRaw(True)
        
        self.requestMaximumCriticalRaw(True)
        
        self.requestMaximumWarningRaw(True)
        
        self.requestMinimumWarningRaw(True)
        
        self.requestMinimumCriticalRaw(True)
        
        self.requestProbeName(True)
        
        self.requestStatusRaw(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStatus(False)
        
        self.requestIndex(False)
        
        self.requestTemperatureRaw(False)
        
        self.requestMaximumCriticalRaw(False)
        
        self.requestMaximumWarningRaw(False)
        
        self.requestMinimumWarningRaw(False)
        
        self.requestMinimumCriticalRaw(False)
        
        self.requestProbeName(False)
        
        self.requestStatusRaw(False)
        
        

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



    def requestStatus (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-status').debug3Func(): logFunc('called. requested=%s', requested)
        self.statusRequested = requested
        self.statusSet = False

    def isStatusRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-status-requested').debug3Func(): logFunc('called. requested=%s', self.statusRequested)
        return self.statusRequested

    def getStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusSet=%s, self.status=%s', self.statusSet, self.status)
        if self.statusSet:
            return self.status
        return None

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusSet=%s, self.status=%s', self.statusSet, self.status)
        if self.statusSet:
            return True
        return False

    def setStatus (self, status):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. status=%s, old=%s', status, self.status)
        self.statusSet = True
        self.status = status

    def requestIndex (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-index').debug3Func(): logFunc('called. requested=%s', requested)
        self.indexRequested = requested
        self.indexSet = False

    def isIndexRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-index-requested').debug3Func(): logFunc('called. requested=%s', self.indexRequested)
        return self.indexRequested

    def getIndex (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-index').debug3Func(): logFunc('called. self.indexSet=%s, self.index=%s', self.indexSet, self.index)
        if self.indexSet:
            return self.index
        return None

    def hasIndex (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-index').debug3Func(): logFunc('called. self.indexSet=%s, self.index=%s', self.indexSet, self.index)
        if self.indexSet:
            return True
        return False

    def setIndex (self, index):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-index').debug3Func(): logFunc('called. index=%s, old=%s', index, self.index)
        self.indexSet = True
        self.index = index

    def requestTemperatureRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-temperatureraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.temperatureRawRequested = requested
        self.temperatureRawSet = False

    def isTemperatureRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-temperatureraw-requested').debug3Func(): logFunc('called. requested=%s', self.temperatureRawRequested)
        return self.temperatureRawRequested

    def getTemperatureRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-temperatureraw').debug3Func(): logFunc('called. self.temperatureRawSet=%s, self.temperatureRaw=%s', self.temperatureRawSet, self.temperatureRaw)
        if self.temperatureRawSet:
            return self.temperatureRaw
        return None

    def hasTemperatureRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-temperatureraw').debug3Func(): logFunc('called. self.temperatureRawSet=%s, self.temperatureRaw=%s', self.temperatureRawSet, self.temperatureRaw)
        if self.temperatureRawSet:
            return True
        return False

    def setTemperatureRaw (self, temperatureRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-temperatureraw').debug3Func(): logFunc('called. temperatureRaw=%s, old=%s', temperatureRaw, self.temperatureRaw)
        self.temperatureRawSet = True
        self.temperatureRaw = temperatureRaw

    def requestMaximumCriticalRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maximumcriticalraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.maximumCriticalRawRequested = requested
        self.maximumCriticalRawSet = False

    def isMaximumCriticalRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maximumcriticalraw-requested').debug3Func(): logFunc('called. requested=%s', self.maximumCriticalRawRequested)
        return self.maximumCriticalRawRequested

    def getMaximumCriticalRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maximumcriticalraw').debug3Func(): logFunc('called. self.maximumCriticalRawSet=%s, self.maximumCriticalRaw=%s', self.maximumCriticalRawSet, self.maximumCriticalRaw)
        if self.maximumCriticalRawSet:
            return self.maximumCriticalRaw
        return None

    def hasMaximumCriticalRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maximumcriticalraw').debug3Func(): logFunc('called. self.maximumCriticalRawSet=%s, self.maximumCriticalRaw=%s', self.maximumCriticalRawSet, self.maximumCriticalRaw)
        if self.maximumCriticalRawSet:
            return True
        return False

    def setMaximumCriticalRaw (self, maximumCriticalRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maximumcriticalraw').debug3Func(): logFunc('called. maximumCriticalRaw=%s, old=%s', maximumCriticalRaw, self.maximumCriticalRaw)
        self.maximumCriticalRawSet = True
        self.maximumCriticalRaw = maximumCriticalRaw

    def requestMaximumWarningRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maximumwarningraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.maximumWarningRawRequested = requested
        self.maximumWarningRawSet = False

    def isMaximumWarningRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maximumwarningraw-requested').debug3Func(): logFunc('called. requested=%s', self.maximumWarningRawRequested)
        return self.maximumWarningRawRequested

    def getMaximumWarningRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maximumwarningraw').debug3Func(): logFunc('called. self.maximumWarningRawSet=%s, self.maximumWarningRaw=%s', self.maximumWarningRawSet, self.maximumWarningRaw)
        if self.maximumWarningRawSet:
            return self.maximumWarningRaw
        return None

    def hasMaximumWarningRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maximumwarningraw').debug3Func(): logFunc('called. self.maximumWarningRawSet=%s, self.maximumWarningRaw=%s', self.maximumWarningRawSet, self.maximumWarningRaw)
        if self.maximumWarningRawSet:
            return True
        return False

    def setMaximumWarningRaw (self, maximumWarningRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maximumwarningraw').debug3Func(): logFunc('called. maximumWarningRaw=%s, old=%s', maximumWarningRaw, self.maximumWarningRaw)
        self.maximumWarningRawSet = True
        self.maximumWarningRaw = maximumWarningRaw

    def requestMinimumWarningRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-minimumwarningraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.minimumWarningRawRequested = requested
        self.minimumWarningRawSet = False

    def isMinimumWarningRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-minimumwarningraw-requested').debug3Func(): logFunc('called. requested=%s', self.minimumWarningRawRequested)
        return self.minimumWarningRawRequested

    def getMinimumWarningRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-minimumwarningraw').debug3Func(): logFunc('called. self.minimumWarningRawSet=%s, self.minimumWarningRaw=%s', self.minimumWarningRawSet, self.minimumWarningRaw)
        if self.minimumWarningRawSet:
            return self.minimumWarningRaw
        return None

    def hasMinimumWarningRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-minimumwarningraw').debug3Func(): logFunc('called. self.minimumWarningRawSet=%s, self.minimumWarningRaw=%s', self.minimumWarningRawSet, self.minimumWarningRaw)
        if self.minimumWarningRawSet:
            return True
        return False

    def setMinimumWarningRaw (self, minimumWarningRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-minimumwarningraw').debug3Func(): logFunc('called. minimumWarningRaw=%s, old=%s', minimumWarningRaw, self.minimumWarningRaw)
        self.minimumWarningRawSet = True
        self.minimumWarningRaw = minimumWarningRaw

    def requestMinimumCriticalRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-minimumcriticalraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.minimumCriticalRawRequested = requested
        self.minimumCriticalRawSet = False

    def isMinimumCriticalRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-minimumcriticalraw-requested').debug3Func(): logFunc('called. requested=%s', self.minimumCriticalRawRequested)
        return self.minimumCriticalRawRequested

    def getMinimumCriticalRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-minimumcriticalraw').debug3Func(): logFunc('called. self.minimumCriticalRawSet=%s, self.minimumCriticalRaw=%s', self.minimumCriticalRawSet, self.minimumCriticalRaw)
        if self.minimumCriticalRawSet:
            return self.minimumCriticalRaw
        return None

    def hasMinimumCriticalRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-minimumcriticalraw').debug3Func(): logFunc('called. self.minimumCriticalRawSet=%s, self.minimumCriticalRaw=%s', self.minimumCriticalRawSet, self.minimumCriticalRaw)
        if self.minimumCriticalRawSet:
            return True
        return False

    def setMinimumCriticalRaw (self, minimumCriticalRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-minimumcriticalraw').debug3Func(): logFunc('called. minimumCriticalRaw=%s, old=%s', minimumCriticalRaw, self.minimumCriticalRaw)
        self.minimumCriticalRawSet = True
        self.minimumCriticalRaw = minimumCriticalRaw

    def requestProbeName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-probename').debug3Func(): logFunc('called. requested=%s', requested)
        self.probeNameRequested = requested
        self.probeNameSet = False

    def isProbeNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-probename-requested').debug3Func(): logFunc('called. requested=%s', self.probeNameRequested)
        return self.probeNameRequested

    def getProbeName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-probename').debug3Func(): logFunc('called. self.probeNameSet=%s, self.probeName=%s', self.probeNameSet, self.probeName)
        if self.probeNameSet:
            return self.probeName
        return None

    def hasProbeName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-probename').debug3Func(): logFunc('called. self.probeNameSet=%s, self.probeName=%s', self.probeNameSet, self.probeName)
        if self.probeNameSet:
            return True
        return False

    def setProbeName (self, probeName):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-probename').debug3Func(): logFunc('called. probeName=%s, old=%s', probeName, self.probeName)
        self.probeNameSet = True
        self.probeName = probeName

    def requestStatusRaw (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-statusraw').debug3Func(): logFunc('called. requested=%s', requested)
        self.statusRawRequested = requested
        self.statusRawSet = False

    def isStatusRawRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-statusraw-requested').debug3Func(): logFunc('called. requested=%s', self.statusRawRequested)
        return self.statusRawRequested

    def getStatusRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-statusraw').debug3Func(): logFunc('called. self.statusRawSet=%s, self.statusRaw=%s', self.statusRawSet, self.statusRaw)
        if self.statusRawSet:
            return self.statusRaw
        return None

    def hasStatusRaw (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-statusraw').debug3Func(): logFunc('called. self.statusRawSet=%s, self.statusRaw=%s', self.statusRawSet, self.statusRaw)
        if self.statusRawSet:
            return True
        return False

    def setStatusRaw (self, statusRaw):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-statusraw').debug3Func(): logFunc('called. statusRaw=%s, old=%s', statusRaw, self.statusRaw)
        self.statusRawSet = True
        self.statusRaw = statusRaw


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.status = 0
        self.statusSet = False
        
        self.index = 0
        self.indexSet = False
        
        self.temperatureRaw = 0
        self.temperatureRawSet = False
        
        self.maximumCriticalRaw = 0
        self.maximumCriticalRawSet = False
        
        self.maximumWarningRaw = 0
        self.maximumWarningRawSet = False
        
        self.minimumWarningRaw = 0
        self.minimumWarningRawSet = False
        
        self.minimumCriticalRaw = 0
        self.minimumCriticalRawSet = False
        
        self.probeName = 0
        self.probeNameSet = False
        
        self.statusRaw = 0
        self.statusRawSet = False
        

    def _getSelfKeyPath (self, sensor
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", "qt-pltf-temperature"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", "qt-pltf-temperature"))
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

        
        if self.isStatusRequested():
            valStatus = Value()
            valStatus.setEmpty()
            tagValueList.push(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valStatus)
        
        if self.isIndexRequested():
            valIndex = Value()
            valIndex.setEmpty()
            tagValueList.push(("index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valIndex)
        
        if self.isTemperatureRawRequested():
            valTemperatureRaw = Value()
            valTemperatureRaw.setEmpty()
            tagValueList.push(("temperature-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valTemperatureRaw)
        
        if self.isMaximumCriticalRawRequested():
            valMaximumCriticalRaw = Value()
            valMaximumCriticalRaw.setEmpty()
            tagValueList.push(("maximum-critical-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valMaximumCriticalRaw)
        
        if self.isMaximumWarningRawRequested():
            valMaximumWarningRaw = Value()
            valMaximumWarningRaw.setEmpty()
            tagValueList.push(("maximum-warning-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valMaximumWarningRaw)
        
        if self.isMinimumWarningRawRequested():
            valMinimumWarningRaw = Value()
            valMinimumWarningRaw.setEmpty()
            tagValueList.push(("minimum-warning-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valMinimumWarningRaw)
        
        if self.isMinimumCriticalRawRequested():
            valMinimumCriticalRaw = Value()
            valMinimumCriticalRaw.setEmpty()
            tagValueList.push(("minimum-critical-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valMinimumCriticalRaw)
        
        if self.isProbeNameRequested():
            valProbeName = Value()
            valProbeName.setEmpty()
            tagValueList.push(("probe-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valProbeName)
        
        if self.isStatusRawRequested():
            valStatusRaw = Value()
            valStatusRaw.setEmpty()
            tagValueList.push(("status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"), valStatusRaw)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isStatusRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-status').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "status", "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-status-bad-value').infoFunc(): logFunc('status not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStatus(tempVar)
            for logFunc in self._log('read-tag-values-status').debug3Func(): logFunc('read status. status=%s, tempValue=%s', self.status, tempValue.getType())
        
        if self.isIndexRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "index") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-index').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "index", "index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-index-bad-value').infoFunc(): logFunc('index not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setIndex(tempVar)
            for logFunc in self._log('read-tag-values-index').debug3Func(): logFunc('read index. index=%s, tempValue=%s', self.index, tempValue.getType())
        
        if self.isTemperatureRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "temperature-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-temperatureraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "temperatureRaw", "temperature-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-temperature-raw-bad-value').infoFunc(): logFunc('temperatureRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTemperatureRaw(tempVar)
            for logFunc in self._log('read-tag-values-temperature-raw').debug3Func(): logFunc('read temperatureRaw. temperatureRaw=%s, tempValue=%s', self.temperatureRaw, tempValue.getType())
        
        if self.isMaximumCriticalRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "maximum-critical-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maximumcriticalraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maximumCriticalRaw", "maximum-critical-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-maximum-critical-raw-bad-value').infoFunc(): logFunc('maximumCriticalRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaximumCriticalRaw(tempVar)
            for logFunc in self._log('read-tag-values-maximum-critical-raw').debug3Func(): logFunc('read maximumCriticalRaw. maximumCriticalRaw=%s, tempValue=%s', self.maximumCriticalRaw, tempValue.getType())
        
        if self.isMaximumWarningRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "maximum-warning-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maximumwarningraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maximumWarningRaw", "maximum-warning-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-maximum-warning-raw-bad-value').infoFunc(): logFunc('maximumWarningRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaximumWarningRaw(tempVar)
            for logFunc in self._log('read-tag-values-maximum-warning-raw').debug3Func(): logFunc('read maximumWarningRaw. maximumWarningRaw=%s, tempValue=%s', self.maximumWarningRaw, tempValue.getType())
        
        if self.isMinimumWarningRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "minimum-warning-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-minimumwarningraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "minimumWarningRaw", "minimum-warning-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-minimum-warning-raw-bad-value').infoFunc(): logFunc('minimumWarningRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMinimumWarningRaw(tempVar)
            for logFunc in self._log('read-tag-values-minimum-warning-raw').debug3Func(): logFunc('read minimumWarningRaw. minimumWarningRaw=%s, tempValue=%s', self.minimumWarningRaw, tempValue.getType())
        
        if self.isMinimumCriticalRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "minimum-critical-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-minimumcriticalraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "minimumCriticalRaw", "minimum-critical-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-minimum-critical-raw-bad-value').infoFunc(): logFunc('minimumCriticalRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMinimumCriticalRaw(tempVar)
            for logFunc in self._log('read-tag-values-minimum-critical-raw').debug3Func(): logFunc('read minimumCriticalRaw. minimumCriticalRaw=%s, tempValue=%s', self.minimumCriticalRaw, tempValue.getType())
        
        if self.isProbeNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "probe-name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-probename').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "probeName", "probe-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-probe-name-bad-value').infoFunc(): logFunc('probeName not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setProbeName(tempVar)
            for logFunc in self._log('read-tag-values-probe-name').debug3Func(): logFunc('read probeName. probeName=%s, tempValue=%s', self.probeName, tempValue.getType())
        
        if self.isStatusRawRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "status-raw") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-statusraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "statusRaw", "status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-status-raw-bad-value').infoFunc(): logFunc('statusRaw not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setStatusRaw(tempVar)
            for logFunc in self._log('read-tag-values-status-raw').debug3Func(): logFunc('read statusRaw. statusRaw=%s, tempValue=%s', self.statusRaw, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.device.status.status_maapi_gen import StatusMaapi", 
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
            "yangName": "device", 
            "namespace": "device", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "name": "device"
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
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "index", 
            "yangName": "index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "temperatureRaw", 
            "yangName": "temperature-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumCriticalRaw", 
            "yangName": "maximum-critical-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumWarningRaw", 
            "yangName": "maximum-warning-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumWarningRaw", 
            "yangName": "minimum-warning-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumCriticalRaw", 
            "yangName": "minimum-critical-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "probeName", 
            "yangName": "probe-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
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
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "index", 
            "yangName": "index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "temperatureRaw", 
            "yangName": "temperature-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumCriticalRaw", 
            "yangName": "maximum-critical-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumWarningRaw", 
            "yangName": "maximum-warning-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumWarningRaw", 
            "yangName": "minimum-warning-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumCriticalRaw", 
            "yangName": "minimum-critical-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "probeName", 
            "yangName": "probe-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-temperature", 
            "moduleYangNamespacePrefix": "qt-pltf-temperature", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


