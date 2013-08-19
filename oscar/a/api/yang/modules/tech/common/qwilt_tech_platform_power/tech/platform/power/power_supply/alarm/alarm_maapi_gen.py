


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


from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyFailureReasonType


class BlinkyAlarmMaapi(AlarmMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-alarm")
        self.domain = None

        

        
        self.powerSupplyFailureRequested = False
        self.powerSupplyFailure = None
        self.powerSupplyFailureSet = False
        
        self.powerSupplyFailureReasonRequested = False
        self.powerSupplyFailureReason = None
        self.powerSupplyFailureReasonSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPowerSupplyFailure(True)
        
        self.requestPowerSupplyFailureReason(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPowerSupplyFailure(False)
        
        self.requestPowerSupplyFailureReason(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPowerSupplyFailure(True)
        
        self.requestPowerSupplyFailureReason(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPowerSupplyFailure(False)
        
        self.requestPowerSupplyFailureReason(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , powerSupply
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(powerSupply, trxContext)

    def read (self
              , powerSupply
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(powerSupply, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , powerSupply
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(powerSupply, 
                                  True,
                                  trxContext)



    def requestPowerSupplyFailure (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-powersupplyfailure').debug3Func(): logFunc('called. requested=%s', requested)
        self.powerSupplyFailureRequested = requested
        self.powerSupplyFailureSet = False

    def isPowerSupplyFailureRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-powersupplyfailure-requested').debug3Func(): logFunc('called. requested=%s', self.powerSupplyFailureRequested)
        return self.powerSupplyFailureRequested

    def getPowerSupplyFailure (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-powersupplyfailure').debug3Func(): logFunc('called. self.powerSupplyFailureSet=%s, self.powerSupplyFailure=%s', self.powerSupplyFailureSet, self.powerSupplyFailure)
        if self.powerSupplyFailureSet:
            return self.powerSupplyFailure
        return None

    def hasPowerSupplyFailure (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-powersupplyfailure').debug3Func(): logFunc('called. self.powerSupplyFailureSet=%s, self.powerSupplyFailure=%s', self.powerSupplyFailureSet, self.powerSupplyFailure)
        if self.powerSupplyFailureSet:
            return True
        return False

    def setPowerSupplyFailure (self, powerSupplyFailure):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-powersupplyfailure').debug3Func(): logFunc('called. powerSupplyFailure=%s, old=%s', powerSupplyFailure, self.powerSupplyFailure)
        self.powerSupplyFailureSet = True
        self.powerSupplyFailure = powerSupplyFailure

    def requestPowerSupplyFailureReason (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-powersupplyfailurereason').debug3Func(): logFunc('called. requested=%s', requested)
        self.powerSupplyFailureReasonRequested = requested
        self.powerSupplyFailureReasonSet = False

    def isPowerSupplyFailureReasonRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-powersupplyfailurereason-requested').debug3Func(): logFunc('called. requested=%s', self.powerSupplyFailureReasonRequested)
        return self.powerSupplyFailureReasonRequested

    def getPowerSupplyFailureReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-powersupplyfailurereason').debug3Func(): logFunc('called. self.powerSupplyFailureReasonSet=%s, self.powerSupplyFailureReason=%s', self.powerSupplyFailureReasonSet, self.powerSupplyFailureReason)
        if self.powerSupplyFailureReasonSet:
            return self.powerSupplyFailureReason
        return None

    def hasPowerSupplyFailureReason (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-powersupplyfailurereason').debug3Func(): logFunc('called. self.powerSupplyFailureReasonSet=%s, self.powerSupplyFailureReason=%s', self.powerSupplyFailureReasonSet, self.powerSupplyFailureReason)
        if self.powerSupplyFailureReasonSet:
            return True
        return False

    def setPowerSupplyFailureReason (self, powerSupplyFailureReason):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-powersupplyfailurereason').debug3Func(): logFunc('called. powerSupplyFailureReason=%s, old=%s', powerSupplyFailureReason, self.powerSupplyFailureReason)
        self.powerSupplyFailureReasonSet = True
        self.powerSupplyFailureReason = powerSupplyFailureReason


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.powerSupplyFailure = 0
        self.powerSupplyFailureSet = False
        
        self.powerSupplyFailureReason = 0
        self.powerSupplyFailureReasonSet = False
        

    def _getSelfKeyPath (self, powerSupply
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alarm", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(powerSupply);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("power-supply", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("power", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", "qt-pltf-pwr"))
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
                        powerSupply, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(powerSupply, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(powerSupply, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       powerSupply, 
                       
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

        keyPath = self._getSelfKeyPath(powerSupply, 
                                       
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
                               powerSupply, 
                               
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

        
        if self.isPowerSupplyFailureRequested():
            valPowerSupplyFailure = Value()
            valPowerSupplyFailure.setEmpty()
            tagValueList.push(("power-supply-failure", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valPowerSupplyFailure)
        
        if self.isPowerSupplyFailureReasonRequested():
            valPowerSupplyFailureReason = Value()
            valPowerSupplyFailureReason.setEmpty()
            tagValueList.push(("power-supply-failure-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"), valPowerSupplyFailureReason)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isPowerSupplyFailureRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "power-supply-failure") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-powersupplyfailure').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "powerSupplyFailure", "power-supply-failure", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-power-supply-failure-bad-value').infoFunc(): logFunc('powerSupplyFailure not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPowerSupplyFailure(tempVar)
            for logFunc in self._log('read-tag-values-power-supply-failure').debug3Func(): logFunc('read powerSupplyFailure. powerSupplyFailure=%s, tempValue=%s', self.powerSupplyFailure, tempValue.getType())
        
        if self.isPowerSupplyFailureReasonRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "power-supply-failure-reason") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-powersupplyfailurereason').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "powerSupplyFailureReason", "power-supply-failure-reason", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-power-supply-failure-reason-bad-value').infoFunc(): logFunc('powerSupplyFailureReason not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPowerSupplyFailureReason(tempVar)
            for logFunc in self._log('read-tag-values-power-supply-failure-reason').debug3Func(): logFunc('read powerSupplyFailureReason. powerSupplyFailureReason=%s, tempValue=%s', self.powerSupplyFailureReason, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "alarm", 
        "namespace": "alarm", 
        "className": "AlarmMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.alarm.alarm_maapi_gen import AlarmMaapi", 
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
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "yangName": "power", 
            "namespace": "power", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "power"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "isCurrent": false, 
            "yangName": "power-supply", 
            "namespace": "power_supply", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "keyLeaf": {
                "varName": "powerSupply", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "power-supply"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "yangName": "alarm", 
            "namespace": "alarm", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "name": "alarm"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "powerSupplyFailure", 
            "yangName": "power-supply-failure", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "powerSupplyFailureReason", 
            "yangName": "power-supply-failure-reason", 
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
            "qwilt_tech_platform_power"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "powerSupplyFailure", 
            "yangName": "power-supply-failure", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-platform-power", 
            "moduleYangNamespacePrefix": "qt-pltf-pwr", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "powerSupplyFailureReason", 
            "yangName": "power-supply-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


