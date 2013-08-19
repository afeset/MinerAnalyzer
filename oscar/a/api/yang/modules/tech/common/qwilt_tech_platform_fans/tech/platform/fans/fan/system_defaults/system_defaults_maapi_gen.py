


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

from system_defaults_maapi_base_gen import SystemDefaultsMaapiBase

from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.system_defaults.device.device_maapi_gen import BlinkyDeviceMaapi
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.system_defaults.simulation.simulation_maapi_gen import BlinkySimulationMaapi



class BlinkySystemDefaultsMaapi(SystemDefaultsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-systemDefaults")
        self.domain = None

        
        self.deviceObj = None
        
        self.simulationObj = None
        

        
        self.muteReportingRequested = False
        self.muteReporting = None
        self.muteReportingSet = False
        
        self.locationRequested = False
        self.location = None
        self.locationSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMuteReporting(True)
        
        self.requestLocation(True)
        
        
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.requestConfigAndOper()
        
        if not self.simulationObj:
            self.simulationObj = self.newSimulation()
            self.simulationObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMuteReporting(True)
        
        self.requestLocation(True)
        
        
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.requestConfig()
        
        if not self.simulationObj:
            self.simulationObj = self.newSimulation()
            self.simulationObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMuteReporting(False)
        
        self.requestLocation(False)
        
        
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.requestOper()
        
        if not self.simulationObj:
            self.simulationObj = self.newSimulation()
            self.simulationObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestMuteReporting(False)
        
        self.requestLocation(False)
        
        
        
        if not self.deviceObj:
            self.deviceObj = self.newDevice()
            self.deviceObj.clearAllRequested()
        
        if not self.simulationObj:
            self.simulationObj = self.newSimulation()
            self.simulationObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setMuteReporting(None)
        self.muteReportingSet = False
        
        self.setLocation(None)
        self.locationSet = False
        
        
        if self.deviceObj:
            self.deviceObj.clearAllSet()
        
        if self.simulationObj:
            self.simulationObj.clearAllSet()
        

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

    def newDevice (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-device').debug3Func(): logFunc('called.')
        device = BlinkyDeviceMaapi(self._log)
        device.init(self.domain)
        return device

    def setDeviceObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-device').debug3Func(): logFunc('called. obj=%s', obj)
        self.deviceObj = obj

    def getDeviceObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-device').debug3Func(): logFunc('called. self.deviceObj=%s', self.deviceObj)
        return self.deviceObj

    def hasDevice (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-device').debug3Func(): logFunc('called. self.deviceObj=%s', self.deviceObj)
        if self.deviceObj:
            return True
        return False

    def newSimulation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-simulation').debug3Func(): logFunc('called.')
        simulation = BlinkySimulationMaapi(self._log)
        simulation.init(self.domain)
        return simulation

    def setSimulationObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-simulation').debug3Func(): logFunc('called. obj=%s', obj)
        self.simulationObj = obj

    def getSimulationObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-simulation').debug3Func(): logFunc('called. self.simulationObj=%s', self.simulationObj)
        return self.simulationObj

    def hasSimulation (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-simulation').debug3Func(): logFunc('called. self.simulationObj=%s', self.simulationObj)
        if self.simulationObj:
            return True
        return False



    def requestMuteReporting (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-mutereporting').debug3Func(): logFunc('called. requested=%s', requested)
        self.muteReportingRequested = requested
        self.muteReportingSet = False

    def isMuteReportingRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-mutereporting-requested').debug3Func(): logFunc('called. requested=%s', self.muteReportingRequested)
        return self.muteReportingRequested

    def getMuteReporting (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-mutereporting').debug3Func(): logFunc('called. self.muteReportingSet=%s, self.muteReporting=%s', self.muteReportingSet, self.muteReporting)
        if self.muteReportingSet:
            return self.muteReporting
        return None

    def hasMuteReporting (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-mutereporting').debug3Func(): logFunc('called. self.muteReportingSet=%s, self.muteReporting=%s', self.muteReportingSet, self.muteReporting)
        if self.muteReportingSet:
            return True
        return False

    def setMuteReporting (self, muteReporting):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-mutereporting').debug3Func(): logFunc('called. muteReporting=%s, old=%s', muteReporting, self.muteReporting)
        self.muteReportingSet = True
        self.muteReporting = muteReporting

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.deviceObj:
            self.deviceObj._clearAllReadData()
        
        if self.simulationObj:
            self.simulationObj._clearAllReadData()
        

        
        self.muteReporting = 0
        self.muteReportingSet = False
        
        self.location = 0
        self.locationSet = False
        

    def _getSelfKeyPath (self, fan
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans"))
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

        
        if self.deviceObj:
            res = self.deviceObj._collectItemsToDelete(fan, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-device-failed').errorFunc(): logFunc('deviceObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.simulationObj:
            res = self.simulationObj._collectItemsToDelete(fan, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-simulation-failed').errorFunc(): logFunc('simulationObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasMuteReporting():
            valMuteReporting = Value()
            if self.muteReporting is not None:
                valMuteReporting.setBool(self.muteReporting)
            else:
                valMuteReporting.setEmpty()
            tagValueList.push(("mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valMuteReporting)
        
        if self.hasLocation():
            valLocation = Value()
            if self.location is not None:
                valLocation.setString(self.location)
            else:
                valLocation.setEmpty()
            tagValueList.push(("location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valLocation)
        

        
        if self.deviceObj:
            valBegin = Value()
            (tag, ns, prefix) = ("device" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.deviceObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-device-failed').errorFunc(): logFunc('deviceObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.simulationObj:
            valBegin = Value()
            (tag, ns, prefix) = ("simulation" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.simulationObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-simulation-failed').errorFunc(): logFunc('simulationObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isMuteReportingRequested():
            valMuteReporting = Value()
            valMuteReporting.setEmpty()
            tagValueList.push(("mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valMuteReporting)
        
        if self.isLocationRequested():
            valLocation = Value()
            valLocation.setEmpty()
            tagValueList.push(("location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valLocation)
        

        
        if self.deviceObj:
            valBegin = Value()
            (tag, ns, prefix) = ("device" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.deviceObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-device-failed').errorFunc(): logFunc('deviceObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.simulationObj:
            valBegin = Value()
            (tag, ns, prefix) = ("simulation" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.simulationObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-simulation-failed').errorFunc(): logFunc('simulationObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isMuteReportingRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mute-reporting") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-mutereporting').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "muteReporting", "mute-reporting", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mute-reporting-bad-value').infoFunc(): logFunc('muteReporting not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMuteReporting(tempVar)
            for logFunc in self._log('read-tag-values-mute-reporting').debug3Func(): logFunc('read muteReporting. muteReporting=%s, tempValue=%s', self.muteReporting, tempValue.getType())
        
        if self.isLocationRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "location") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-location').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "location", "location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
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
        

        
        if self.deviceObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "device") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.deviceObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-device-failed').errorFunc(): logFunc('deviceObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "device") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "device", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.simulationObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "simulation") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "simulation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.simulationObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-simulation-failed').errorFunc(): logFunc('simulationObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "simulation") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "simulation", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
        "baseClassName": "SystemDefaultsMaapiBase", 
        "baseModule": "system_defaults_maapi_base_gen"
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
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "memberName": "device", 
            "yangName": "device", 
            "className": "BlinkyDeviceMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.system_defaults.device.device_maapi_gen import BlinkyDeviceMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "memberName": "simulation", 
            "yangName": "simulation", 
            "className": "BlinkySimulationMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.system_defaults.simulation.simulation_maapi_gen import BlinkySimulationMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "common", 
            "qwilt_tech_platform_fans"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "muteReporting", 
            "yangName": "mute-reporting", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


