


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


from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanDeviceStatusType


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
        
        self.minimumWarningRpmRequested = False
        self.minimumWarningRpm = None
        self.minimumWarningRpmSet = False
        
        self.currentRpmRequested = False
        self.currentRpm = None
        self.currentRpmSet = False
        
        self.maximumWarningRpmRequested = False
        self.maximumWarningRpm = None
        self.maximumWarningRpmSet = False
        
        self.probeNameRequested = False
        self.probeName = None
        self.probeNameSet = False
        
        self.statusRawRequested = False
        self.statusRaw = None
        self.statusRawSet = False
        
        self.minimumErrorRpmRequested = False
        self.minimumErrorRpm = None
        self.minimumErrorRpmSet = False
        
        self.maximumErrorRpmRequested = False
        self.maximumErrorRpm = None
        self.maximumErrorRpmSet = False
        

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
        
        self.requestMinimumWarningRpm(True)
        
        self.requestCurrentRpm(True)
        
        self.requestMaximumWarningRpm(True)
        
        self.requestProbeName(True)
        
        self.requestStatusRaw(True)
        
        self.requestMinimumErrorRpm(True)
        
        self.requestMaximumErrorRpm(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStatus(False)
        
        self.requestIndex(False)
        
        self.requestMinimumWarningRpm(False)
        
        self.requestCurrentRpm(False)
        
        self.requestMaximumWarningRpm(False)
        
        self.requestProbeName(False)
        
        self.requestStatusRaw(False)
        
        self.requestMinimumErrorRpm(False)
        
        self.requestMaximumErrorRpm(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStatus(True)
        
        self.requestIndex(True)
        
        self.requestMinimumWarningRpm(True)
        
        self.requestCurrentRpm(True)
        
        self.requestMaximumWarningRpm(True)
        
        self.requestProbeName(True)
        
        self.requestStatusRaw(True)
        
        self.requestMinimumErrorRpm(True)
        
        self.requestMaximumErrorRpm(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestStatus(False)
        
        self.requestIndex(False)
        
        self.requestMinimumWarningRpm(False)
        
        self.requestCurrentRpm(False)
        
        self.requestMaximumWarningRpm(False)
        
        self.requestProbeName(False)
        
        self.requestStatusRaw(False)
        
        self.requestMinimumErrorRpm(False)
        
        self.requestMaximumErrorRpm(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , fan
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(fan, trxContext)

    def read (self
              , fan
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(fan, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , fan
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(fan, 
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

    def requestMinimumWarningRpm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-minimumwarningrpm').debug3Func(): logFunc('called. requested=%s', requested)
        self.minimumWarningRpmRequested = requested
        self.minimumWarningRpmSet = False

    def isMinimumWarningRpmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-minimumwarningrpm-requested').debug3Func(): logFunc('called. requested=%s', self.minimumWarningRpmRequested)
        return self.minimumWarningRpmRequested

    def getMinimumWarningRpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-minimumwarningrpm').debug3Func(): logFunc('called. self.minimumWarningRpmSet=%s, self.minimumWarningRpm=%s', self.minimumWarningRpmSet, self.minimumWarningRpm)
        if self.minimumWarningRpmSet:
            return self.minimumWarningRpm
        return None

    def hasMinimumWarningRpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-minimumwarningrpm').debug3Func(): logFunc('called. self.minimumWarningRpmSet=%s, self.minimumWarningRpm=%s', self.minimumWarningRpmSet, self.minimumWarningRpm)
        if self.minimumWarningRpmSet:
            return True
        return False

    def setMinimumWarningRpm (self, minimumWarningRpm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-minimumwarningrpm').debug3Func(): logFunc('called. minimumWarningRpm=%s, old=%s', minimumWarningRpm, self.minimumWarningRpm)
        self.minimumWarningRpmSet = True
        self.minimumWarningRpm = minimumWarningRpm

    def requestCurrentRpm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-currentrpm').debug3Func(): logFunc('called. requested=%s', requested)
        self.currentRpmRequested = requested
        self.currentRpmSet = False

    def isCurrentRpmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-currentrpm-requested').debug3Func(): logFunc('called. requested=%s', self.currentRpmRequested)
        return self.currentRpmRequested

    def getCurrentRpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-currentrpm').debug3Func(): logFunc('called. self.currentRpmSet=%s, self.currentRpm=%s', self.currentRpmSet, self.currentRpm)
        if self.currentRpmSet:
            return self.currentRpm
        return None

    def hasCurrentRpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-currentrpm').debug3Func(): logFunc('called. self.currentRpmSet=%s, self.currentRpm=%s', self.currentRpmSet, self.currentRpm)
        if self.currentRpmSet:
            return True
        return False

    def setCurrentRpm (self, currentRpm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-currentrpm').debug3Func(): logFunc('called. currentRpm=%s, old=%s', currentRpm, self.currentRpm)
        self.currentRpmSet = True
        self.currentRpm = currentRpm

    def requestMaximumWarningRpm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maximumwarningrpm').debug3Func(): logFunc('called. requested=%s', requested)
        self.maximumWarningRpmRequested = requested
        self.maximumWarningRpmSet = False

    def isMaximumWarningRpmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maximumwarningrpm-requested').debug3Func(): logFunc('called. requested=%s', self.maximumWarningRpmRequested)
        return self.maximumWarningRpmRequested

    def getMaximumWarningRpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maximumwarningrpm').debug3Func(): logFunc('called. self.maximumWarningRpmSet=%s, self.maximumWarningRpm=%s', self.maximumWarningRpmSet, self.maximumWarningRpm)
        if self.maximumWarningRpmSet:
            return self.maximumWarningRpm
        return None

    def hasMaximumWarningRpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maximumwarningrpm').debug3Func(): logFunc('called. self.maximumWarningRpmSet=%s, self.maximumWarningRpm=%s', self.maximumWarningRpmSet, self.maximumWarningRpm)
        if self.maximumWarningRpmSet:
            return True
        return False

    def setMaximumWarningRpm (self, maximumWarningRpm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maximumwarningrpm').debug3Func(): logFunc('called. maximumWarningRpm=%s, old=%s', maximumWarningRpm, self.maximumWarningRpm)
        self.maximumWarningRpmSet = True
        self.maximumWarningRpm = maximumWarningRpm

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

    def requestMinimumErrorRpm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-minimumerrorrpm').debug3Func(): logFunc('called. requested=%s', requested)
        self.minimumErrorRpmRequested = requested
        self.minimumErrorRpmSet = False

    def isMinimumErrorRpmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-minimumerrorrpm-requested').debug3Func(): logFunc('called. requested=%s', self.minimumErrorRpmRequested)
        return self.minimumErrorRpmRequested

    def getMinimumErrorRpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-minimumerrorrpm').debug3Func(): logFunc('called. self.minimumErrorRpmSet=%s, self.minimumErrorRpm=%s', self.minimumErrorRpmSet, self.minimumErrorRpm)
        if self.minimumErrorRpmSet:
            return self.minimumErrorRpm
        return None

    def hasMinimumErrorRpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-minimumerrorrpm').debug3Func(): logFunc('called. self.minimumErrorRpmSet=%s, self.minimumErrorRpm=%s', self.minimumErrorRpmSet, self.minimumErrorRpm)
        if self.minimumErrorRpmSet:
            return True
        return False

    def setMinimumErrorRpm (self, minimumErrorRpm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-minimumerrorrpm').debug3Func(): logFunc('called. minimumErrorRpm=%s, old=%s', minimumErrorRpm, self.minimumErrorRpm)
        self.minimumErrorRpmSet = True
        self.minimumErrorRpm = minimumErrorRpm

    def requestMaximumErrorRpm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-maximumerrorrpm').debug3Func(): logFunc('called. requested=%s', requested)
        self.maximumErrorRpmRequested = requested
        self.maximumErrorRpmSet = False

    def isMaximumErrorRpmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-maximumerrorrpm-requested').debug3Func(): logFunc('called. requested=%s', self.maximumErrorRpmRequested)
        return self.maximumErrorRpmRequested

    def getMaximumErrorRpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-maximumerrorrpm').debug3Func(): logFunc('called. self.maximumErrorRpmSet=%s, self.maximumErrorRpm=%s', self.maximumErrorRpmSet, self.maximumErrorRpm)
        if self.maximumErrorRpmSet:
            return self.maximumErrorRpm
        return None

    def hasMaximumErrorRpm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-maximumerrorrpm').debug3Func(): logFunc('called. self.maximumErrorRpmSet=%s, self.maximumErrorRpm=%s', self.maximumErrorRpmSet, self.maximumErrorRpm)
        if self.maximumErrorRpmSet:
            return True
        return False

    def setMaximumErrorRpm (self, maximumErrorRpm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-maximumerrorrpm').debug3Func(): logFunc('called. maximumErrorRpm=%s, old=%s', maximumErrorRpm, self.maximumErrorRpm)
        self.maximumErrorRpmSet = True
        self.maximumErrorRpm = maximumErrorRpm


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.status = 0
        self.statusSet = False
        
        self.index = 0
        self.indexSet = False
        
        self.minimumWarningRpm = 0
        self.minimumWarningRpmSet = False
        
        self.currentRpm = 0
        self.currentRpmSet = False
        
        self.maximumWarningRpm = 0
        self.maximumWarningRpmSet = False
        
        self.probeName = 0
        self.probeNameSet = False
        
        self.statusRaw = 0
        self.statusRawSet = False
        
        self.minimumErrorRpm = 0
        self.minimumErrorRpmSet = False
        
        self.maximumErrorRpm = 0
        self.maximumErrorRpmSet = False
        

    def _getSelfKeyPath (self, fan
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(fan);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fan", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fans", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans"))
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
                        fan, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(fan, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(fan, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       fan, 
                       
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

        keyPath = self._getSelfKeyPath(fan, 
                                       
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
                               fan, 
                               
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
            tagValueList.push(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valStatus)
        
        if self.isIndexRequested():
            valIndex = Value()
            valIndex.setEmpty()
            tagValueList.push(("index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valIndex)
        
        if self.isMinimumWarningRpmRequested():
            valMinimumWarningRpm = Value()
            valMinimumWarningRpm.setEmpty()
            tagValueList.push(("minimum-warning-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valMinimumWarningRpm)
        
        if self.isCurrentRpmRequested():
            valCurrentRpm = Value()
            valCurrentRpm.setEmpty()
            tagValueList.push(("current-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valCurrentRpm)
        
        if self.isMaximumWarningRpmRequested():
            valMaximumWarningRpm = Value()
            valMaximumWarningRpm.setEmpty()
            tagValueList.push(("maximum-warning-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valMaximumWarningRpm)
        
        if self.isProbeNameRequested():
            valProbeName = Value()
            valProbeName.setEmpty()
            tagValueList.push(("probe-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valProbeName)
        
        if self.isStatusRawRequested():
            valStatusRaw = Value()
            valStatusRaw.setEmpty()
            tagValueList.push(("status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valStatusRaw)
        
        if self.isMinimumErrorRpmRequested():
            valMinimumErrorRpm = Value()
            valMinimumErrorRpm.setEmpty()
            tagValueList.push(("minimum-error-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valMinimumErrorRpm)
        
        if self.isMaximumErrorRpmRequested():
            valMaximumErrorRpm = Value()
            valMaximumErrorRpm.setEmpty()
            tagValueList.push(("maximum-error-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valMaximumErrorRpm)
        

        

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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-status').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "status", "status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-index').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "index", "index", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
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
        
        if self.isMinimumWarningRpmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "minimum-warning-rpm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-minimumwarningrpm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "minimumWarningRpm", "minimum-warning-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-minimum-warning-rpm-bad-value').infoFunc(): logFunc('minimumWarningRpm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMinimumWarningRpm(tempVar)
            for logFunc in self._log('read-tag-values-minimum-warning-rpm').debug3Func(): logFunc('read minimumWarningRpm. minimumWarningRpm=%s, tempValue=%s', self.minimumWarningRpm, tempValue.getType())
        
        if self.isCurrentRpmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "current-rpm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-currentrpm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "currentRpm", "current-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-current-rpm-bad-value').infoFunc(): logFunc('currentRpm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCurrentRpm(tempVar)
            for logFunc in self._log('read-tag-values-current-rpm').debug3Func(): logFunc('read currentRpm. currentRpm=%s, tempValue=%s', self.currentRpm, tempValue.getType())
        
        if self.isMaximumWarningRpmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "maximum-warning-rpm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maximumwarningrpm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maximumWarningRpm", "maximum-warning-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-maximum-warning-rpm-bad-value').infoFunc(): logFunc('maximumWarningRpm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaximumWarningRpm(tempVar)
            for logFunc in self._log('read-tag-values-maximum-warning-rpm').debug3Func(): logFunc('read maximumWarningRpm. maximumWarningRpm=%s, tempValue=%s', self.maximumWarningRpm, tempValue.getType())
        
        if self.isProbeNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "probe-name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-probename').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "probeName", "probe-name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-statusraw').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "statusRaw", "status-raw", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
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
        
        if self.isMinimumErrorRpmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "minimum-error-rpm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-minimumerrorrpm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "minimumErrorRpm", "minimum-error-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-minimum-error-rpm-bad-value').infoFunc(): logFunc('minimumErrorRpm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMinimumErrorRpm(tempVar)
            for logFunc in self._log('read-tag-values-minimum-error-rpm').debug3Func(): logFunc('read minimumErrorRpm. minimumErrorRpm=%s, tempValue=%s', self.minimumErrorRpm, tempValue.getType())
        
        if self.isMaximumErrorRpmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "maximum-error-rpm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-maximumerrorrpm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "maximumErrorRpm", "maximum-error-rpm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-maximum-error-rpm-bad-value').infoFunc(): logFunc('maximumErrorRpm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMaximumErrorRpm(tempVar)
            for logFunc in self._log('read-tag-values-maximum-error-rpm').debug3Func(): logFunc('read maximumErrorRpm. maximumErrorRpm=%s, tempValue=%s', self.maximumErrorRpm, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.status.status_maapi_gen import StatusMaapi", 
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
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "yangName": "fans", 
            "namespace": "fans", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "fans"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "isCurrent": false, 
            "yangName": "fan", 
            "namespace": "fan", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "keyLeaf": {
                "varName": "fan", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fan"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "yangName": "device", 
            "namespace": "device", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "device"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "index", 
            "yangName": "index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumWarningRpm", 
            "yangName": "minimum-warning-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "currentRpm", 
            "yangName": "current-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumWarningRpm", 
            "yangName": "maximum-warning-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "probeName", 
            "yangName": "probe-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumErrorRpm", 
            "yangName": "minimum-error-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumErrorRpm", 
            "yangName": "maximum-error-rpm", 
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
            "qwilt_tech_platform_fans"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "index", 
            "yangName": "index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumWarningRpm", 
            "yangName": "minimum-warning-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "currentRpm", 
            "yangName": "current-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumWarningRpm", 
            "yangName": "maximum-warning-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "probeName", 
            "yangName": "probe-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumErrorRpm", 
            "yangName": "minimum-error-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumErrorRpm", 
            "yangName": "maximum-error-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


