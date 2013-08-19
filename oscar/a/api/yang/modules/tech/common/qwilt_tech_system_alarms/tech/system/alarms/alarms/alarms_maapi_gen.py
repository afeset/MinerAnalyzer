


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

from alarms_maapi_base_gen import AlarmsMaapiBase


from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import TestAlarmReasonType


class BlinkyAlarmsMaapi(AlarmsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-alarms")
        self.domain = None

        

        
        self.testAlarmReasonRequested = False
        self.testAlarmReason = None
        self.testAlarmReasonSet = False
        
        self.testAlarmRequested = False
        self.testAlarm = None
        self.testAlarmSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestTestAlarmReason(True)
        
        self.requestTestAlarm(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestTestAlarmReason(False)
        
        self.requestTestAlarm(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestTestAlarmReason(True)
        
        self.requestTestAlarm(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestTestAlarmReason(False)
        
        self.requestTestAlarm(False)
        
        

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



    def requestTestAlarmReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-testalarmreason').debug3Func(): logFunc('called. requested=%s', requested)
        self.testAlarmReasonRequested = requested
        self.testAlarmReasonSet = False

    def isTestAlarmReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-testalarmreason-requested').debug3Func(): logFunc('called. requested=%s', self.testAlarmReasonRequested)
        return self.testAlarmReasonRequested

    def getTestAlarmReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-testalarmreason').debug3Func(): logFunc('called. self.testAlarmReasonSet=%s, self.testAlarmReason=%s', self.testAlarmReasonSet, self.testAlarmReason)
        if self.testAlarmReasonSet:
            return self.testAlarmReason
        return None

    def hasTestAlarmReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-testalarmreason').debug3Func(): logFunc('called. self.testAlarmReasonSet=%s, self.testAlarmReason=%s', self.testAlarmReasonSet, self.testAlarmReason)
        if self.testAlarmReasonSet:
            return True
        return False

    def setTestAlarmReason (self, testAlarmReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-testalarmreason').debug3Func(): logFunc('called. testAlarmReason=%s, old=%s', testAlarmReason, self.testAlarmReason)
        self.testAlarmReasonSet = True
        self.testAlarmReason = testAlarmReason

    def requestTestAlarm (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-testalarm').debug3Func(): logFunc('called. requested=%s', requested)
        self.testAlarmRequested = requested
        self.testAlarmSet = False

    def isTestAlarmRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-testalarm-requested').debug3Func(): logFunc('called. requested=%s', self.testAlarmRequested)
        return self.testAlarmRequested

    def getTestAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-testalarm').debug3Func(): logFunc('called. self.testAlarmSet=%s, self.testAlarm=%s', self.testAlarmSet, self.testAlarm)
        if self.testAlarmSet:
            return self.testAlarm
        return None

    def hasTestAlarm (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-testalarm').debug3Func(): logFunc('called. self.testAlarmSet=%s, self.testAlarm=%s', self.testAlarmSet, self.testAlarm)
        if self.testAlarmSet:
            return True
        return False

    def setTestAlarm (self, testAlarm):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-testalarm').debug3Func(): logFunc('called. testAlarm=%s, old=%s', testAlarm, self.testAlarm)
        self.testAlarmSet = True
        self.testAlarm = testAlarm


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.testAlarmReason = 0
        self.testAlarmReasonSet = False
        
        self.testAlarm = 0
        self.testAlarmSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarms", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", "qt-sys-alarms"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", "qt-sys"))
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

        
        if self.isTestAlarmReasonRequested():
            valTestAlarmReason = Value()
            valTestAlarmReason.setEmpty()
            tagValueList.push(("test-alarm-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valTestAlarmReason)
        
        if self.isTestAlarmRequested():
            valTestAlarm = Value()
            valTestAlarm.setEmpty()
            tagValueList.push(("test-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"), valTestAlarm)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isTestAlarmReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "test-alarm-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-testalarmreason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "testAlarmReason", "test-alarm-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-test-alarm-reason-bad-value').infoFunc(): logFunc('testAlarmReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTestAlarmReason(tempVar)
            for logFunc in self._log('read-tag-values-test-alarm-reason').debug3Func(): logFunc('read testAlarmReason. testAlarmReason=%s, tempValue=%s', self.testAlarmReason, tempValue.getType())
        
        if self.isTestAlarmRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "test-alarm") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-testalarm').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "testAlarm", "test-alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-test-alarm-bad-value').infoFunc(): logFunc('testAlarm not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTestAlarm(tempVar)
            for logFunc in self._log('read-tag-values-test-alarm').debug3Func(): logFunc('read testAlarm. testAlarm=%s, tempValue=%s', self.testAlarm, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "alarms", 
        "namespace": "alarms", 
        "className": "AlarmsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.alarms.alarms_maapi_gen import AlarmsMaapi", 
        "baseClassName": "AlarmsMaapiBase", 
        "baseModule": "alarms_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-sys", 
            "yangName": "system", 
            "namespace": "system", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system", 
            "name": "system"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "alarms"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "yangName": "alarms", 
            "namespace": "alarms", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "name": "alarms"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "testAlarmReason", 
            "yangName": "test-alarm-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "testAlarm", 
            "yangName": "test-alarm", 
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
            "qwilt_tech_system_alarms"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "testAlarmReason", 
            "yangName": "test-alarm-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-system-alarms", 
            "moduleYangNamespacePrefix": "qt-sys-alarms", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "testAlarm", 
            "yangName": "test-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


