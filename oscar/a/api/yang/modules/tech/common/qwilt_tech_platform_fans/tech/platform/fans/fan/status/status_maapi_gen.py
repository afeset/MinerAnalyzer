


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


from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanOperationalStatusType


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
        
        
        self.requestOperationalStatus(True)
        
        self.requestOperationalStatusReason(True)
        
        self.requestLocation(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOperationalStatus(False)
        
        self.requestOperationalStatusReason(False)
        
        self.requestLocation(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOperationalStatus(True)
        
        self.requestOperationalStatusReason(True)
        
        self.requestLocation(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOperationalStatus(False)
        
        self.requestOperationalStatusReason(False)
        
        self.requestLocation(False)
        
        

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

        

        
        self.operationalStatus = 0
        self.operationalStatusSet = False
        
        self.operationalStatusReason = 0
        self.operationalStatusReasonSet = False
        
        self.location = 0
        self.locationSet = False
        

    def _getSelfKeyPath (self, fan
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans"))
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

        
        if self.isOperationalStatusRequested():
            valOperationalStatus = Value()
            valOperationalStatus.setEmpty()
            tagValueList.push(("operational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valOperationalStatus)
        
        if self.isOperationalStatusReasonRequested():
            valOperationalStatusReason = Value()
            valOperationalStatusReason.setEmpty()
            tagValueList.push(("operational-status-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valOperationalStatusReason)
        
        if self.isLocationRequested():
            valLocation = Value()
            valLocation.setEmpty()
            tagValueList.push(("location", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valLocation)
        

        

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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-operationalstatus').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "operationalStatus", "operational-status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-operationalstatusreason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "operationalStatusReason", "operational-status-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
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
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.status.status_maapi_gen import StatusMaapi", 
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
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


