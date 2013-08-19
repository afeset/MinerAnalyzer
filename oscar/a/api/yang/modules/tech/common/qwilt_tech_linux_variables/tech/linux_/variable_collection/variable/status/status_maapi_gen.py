


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




class BlinkyStatusMaapi(StatusMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-status")
        self.domain = None

        

        
        self.initialValueRequested = False
        self.initialValue = None
        self.initialValueSet = False
        
        self.actualValueRequested = False
        self.actualValue = None
        self.actualValueSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInitialValue(True)
        
        self.requestActualValue(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInitialValue(False)
        
        self.requestActualValue(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInitialValue(True)
        
        self.requestActualValue(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestInitialValue(False)
        
        self.requestActualValue(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , linux_
              , variableCollection
              , variable
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(linux_, variableCollection, variable, trxContext)

    def read (self
              , linux_
              , variableCollection
              , variable
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(linux_, variableCollection, variable, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , linux_
                       , variableCollection
                       , variable
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(linux_, variableCollection, variable, 
                                  True,
                                  trxContext)



    def requestInitialValue (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-initialvalue').debug3Func(): logFunc('called. requested=%s', requested)
        self.initialValueRequested = requested
        self.initialValueSet = False

    def isInitialValueRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-initialvalue-requested').debug3Func(): logFunc('called. requested=%s', self.initialValueRequested)
        return self.initialValueRequested

    def getInitialValue (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-initialvalue').debug3Func(): logFunc('called. self.initialValueSet=%s, self.initialValue=%s', self.initialValueSet, self.initialValue)
        if self.initialValueSet:
            return self.initialValue
        return None

    def hasInitialValue (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-initialvalue').debug3Func(): logFunc('called. self.initialValueSet=%s, self.initialValue=%s', self.initialValueSet, self.initialValue)
        if self.initialValueSet:
            return True
        return False

    def setInitialValue (self, initialValue):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-initialvalue').debug3Func(): logFunc('called. initialValue=%s, old=%s', initialValue, self.initialValue)
        self.initialValueSet = True
        self.initialValue = initialValue

    def requestActualValue (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-actualvalue').debug3Func(): logFunc('called. requested=%s', requested)
        self.actualValueRequested = requested
        self.actualValueSet = False

    def isActualValueRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-actualvalue-requested').debug3Func(): logFunc('called. requested=%s', self.actualValueRequested)
        return self.actualValueRequested

    def getActualValue (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-actualvalue').debug3Func(): logFunc('called. self.actualValueSet=%s, self.actualValue=%s', self.actualValueSet, self.actualValue)
        if self.actualValueSet:
            return self.actualValue
        return None

    def hasActualValue (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-actualvalue').debug3Func(): logFunc('called. self.actualValueSet=%s, self.actualValue=%s', self.actualValueSet, self.actualValue)
        if self.actualValueSet:
            return True
        return False

    def setActualValue (self, actualValue):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-actualvalue').debug3Func(): logFunc('called. actualValue=%s, old=%s', actualValue, self.actualValue)
        self.actualValueSet = True
        self.actualValue = actualValue


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.initialValue = 0
        self.initialValueSet = False
        
        self.actualValue = 0
        self.actualValueSet = False
        

    def _getSelfKeyPath (self, linux_
                         , variableCollection
                         , variable
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(variable);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("variable", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(variableCollection);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("variable-collection", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(linux_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("linux", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux", "qt-lnx"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        linux_, 
                        variableCollection, 
                        variable, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(linux_, 
                                         variableCollection, 
                                         variable, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(linux_, 
                                       variableCollection, 
                                       variable, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       linux_, 
                       variableCollection, 
                       variable, 
                       
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

        keyPath = self._getSelfKeyPath(linux_, 
                                       variableCollection, 
                                       variable, 
                                       
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
                               linux_, 
                               variableCollection, 
                               variable, 
                               
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

        
        if self.isInitialValueRequested():
            valInitialValue = Value()
            valInitialValue.setEmpty()
            tagValueList.push(("initial-value", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valInitialValue)
        
        if self.isActualValueRequested():
            valActualValue = Value()
            valActualValue.setEmpty()
            tagValueList.push(("actual-value", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valActualValue)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isInitialValueRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "initial-value") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-initialvalue').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "initialValue", "initial-value", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-initial-value-bad-value').infoFunc(): logFunc('initialValue not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInitialValue(tempVar)
            for logFunc in self._log('read-tag-values-initial-value').debug3Func(): logFunc('read initialValue. initialValue=%s, tempValue=%s', self.initialValue, tempValue.getType())
        
        if self.isActualValueRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "actual-value") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-actualvalue').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "actualValue", "actual-value", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-actual-value-bad-value').infoFunc(): logFunc('actualValue not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setActualValue(tempVar)
            for logFunc in self._log('read-tag-values-actual-value').debug3Func(): logFunc('read actualValue. actualValue=%s, tempValue=%s', self.actualValue, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.status.status_maapi_gen import StatusMaapi", 
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
            "moduleYangNamespacePrefix": "qt-lnx", 
            "isCurrent": false, 
            "yangName": "linux", 
            "namespace": "linux_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux", 
            "keyLeaf": {
                "varName": "linux_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "linux_"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "isCurrent": false, 
            "yangName": "variable-collection", 
            "namespace": "variable_collection", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "keyLeaf": {
                "varName": "variableCollection", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "variable-collection"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "isCurrent": false, 
            "yangName": "variable", 
            "namespace": "variable", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "keyLeaf": {
                "varName": "variable", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "variable"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "initialValue", 
            "yangName": "initial-value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "actualValue", 
            "yangName": "actual-value", 
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
            "qwilt_tech_linux_variables"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "initialValue", 
            "yangName": "initial-value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "actualValue", 
            "yangName": "actual-value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


