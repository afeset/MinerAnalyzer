


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


from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FansNoRedundancyReasonType


class BlinkyAlarmMaapi(AlarmMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-alarm")
        self.domain = None

        

        
        self.noRedundancyReasonRequested = False
        self.noRedundancyReason = None
        self.noRedundancyReasonSet = False
        
        self.noRedundancyRequested = False
        self.noRedundancy = None
        self.noRedundancySet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestNoRedundancyReason(True)
        
        self.requestNoRedundancy(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestNoRedundancyReason(False)
        
        self.requestNoRedundancy(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestNoRedundancyReason(True)
        
        self.requestNoRedundancy(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestNoRedundancyReason(False)
        
        self.requestNoRedundancy(False)
        
        

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



    def requestNoRedundancyReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-noredundancyreason').debug3Func(): logFunc('called. requested=%s', requested)
        self.noRedundancyReasonRequested = requested
        self.noRedundancyReasonSet = False

    def isNoRedundancyReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-noredundancyreason-requested').debug3Func(): logFunc('called. requested=%s', self.noRedundancyReasonRequested)
        return self.noRedundancyReasonRequested

    def getNoRedundancyReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-noredundancyreason').debug3Func(): logFunc('called. self.noRedundancyReasonSet=%s, self.noRedundancyReason=%s', self.noRedundancyReasonSet, self.noRedundancyReason)
        if self.noRedundancyReasonSet:
            return self.noRedundancyReason
        return None

    def hasNoRedundancyReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-noredundancyreason').debug3Func(): logFunc('called. self.noRedundancyReasonSet=%s, self.noRedundancyReason=%s', self.noRedundancyReasonSet, self.noRedundancyReason)
        if self.noRedundancyReasonSet:
            return True
        return False

    def setNoRedundancyReason (self, noRedundancyReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-noredundancyreason').debug3Func(): logFunc('called. noRedundancyReason=%s, old=%s', noRedundancyReason, self.noRedundancyReason)
        self.noRedundancyReasonSet = True
        self.noRedundancyReason = noRedundancyReason

    def requestNoRedundancy (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-noredundancy').debug3Func(): logFunc('called. requested=%s', requested)
        self.noRedundancyRequested = requested
        self.noRedundancySet = False

    def isNoRedundancyRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-noredundancy-requested').debug3Func(): logFunc('called. requested=%s', self.noRedundancyRequested)
        return self.noRedundancyRequested

    def getNoRedundancy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-noredundancy').debug3Func(): logFunc('called. self.noRedundancySet=%s, self.noRedundancy=%s', self.noRedundancySet, self.noRedundancy)
        if self.noRedundancySet:
            return self.noRedundancy
        return None

    def hasNoRedundancy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-noredundancy').debug3Func(): logFunc('called. self.noRedundancySet=%s, self.noRedundancy=%s', self.noRedundancySet, self.noRedundancy)
        if self.noRedundancySet:
            return True
        return False

    def setNoRedundancy (self, noRedundancy):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-noredundancy').debug3Func(): logFunc('called. noRedundancy=%s, old=%s', noRedundancy, self.noRedundancy)
        self.noRedundancySet = True
        self.noRedundancy = noRedundancy


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.noRedundancyReason = 0
        self.noRedundancyReasonSet = False
        
        self.noRedundancy = 0
        self.noRedundancySet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", "qt-pltf-fans"))
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

        
        if self.isNoRedundancyReasonRequested():
            valNoRedundancyReason = Value()
            valNoRedundancyReason.setEmpty()
            tagValueList.push(("no-redundancy-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valNoRedundancyReason)
        
        if self.isNoRedundancyRequested():
            valNoRedundancy = Value()
            valNoRedundancy.setEmpty()
            tagValueList.push(("no-redundancy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"), valNoRedundancy)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isNoRedundancyReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "no-redundancy-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-noredundancyreason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "noRedundancyReason", "no-redundancy-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-no-redundancy-reason-bad-value').infoFunc(): logFunc('noRedundancyReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNoRedundancyReason(tempVar)
            for logFunc in self._log('read-tag-values-no-redundancy-reason').debug3Func(): logFunc('read noRedundancyReason. noRedundancyReason=%s, tempValue=%s', self.noRedundancyReason, tempValue.getType())
        
        if self.isNoRedundancyRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "no-redundancy") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-noredundancy').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "noRedundancy", "no-redundancy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-no-redundancy-bad-value').infoFunc(): logFunc('noRedundancy not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNoRedundancy(tempVar)
            for logFunc in self._log('read-tag-values-no-redundancy').debug3Func(): logFunc('read noRedundancy. noRedundancy=%s, tempValue=%s', self.noRedundancy, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "alarm", 
        "namespace": "alarm", 
        "className": "AlarmMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.alarm.alarm_maapi_gen import AlarmMaapi", 
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
            "yangName": "alarm", 
            "namespace": "alarm", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "name": "alarm"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "noRedundancyReason", 
            "yangName": "no-redundancy-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "noRedundancy", 
            "yangName": "no-redundancy", 
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
            "memberName": "noRedundancyReason", 
            "yangName": "no-redundancy-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-fans", 
            "moduleYangNamespacePrefix": "qt-pltf-fans", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "noRedundancy", 
            "yangName": "no-redundancy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


