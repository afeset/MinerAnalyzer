


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


from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.qwilt_tech_linux_variables_module_gen import InitPhase


class BlinkySystemDefaultsMaapi(SystemDefaultsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-systemDefaults")
        self.domain = None

        

        
        self.systemProtectedRequested = False
        self.systemProtected = None
        self.systemProtectedSet = False
        
        self.initPhaseRequested = False
        self.initPhase = None
        self.initPhaseSet = False
        
        self.descriptionRequested = False
        self.description = None
        self.descriptionSet = False
        
        self.valueRequested = False
        self.value = None
        self.valueSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSystemProtected(True)
        
        self.requestInitPhase(True)
        
        self.requestDescription(True)
        
        self.requestValue(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSystemProtected(True)
        
        self.requestInitPhase(True)
        
        self.requestDescription(True)
        
        self.requestValue(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSystemProtected(False)
        
        self.requestInitPhase(False)
        
        self.requestDescription(False)
        
        self.requestValue(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSystemProtected(False)
        
        self.requestInitPhase(False)
        
        self.requestDescription(False)
        
        self.requestValue(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setSystemProtected(None)
        self.systemProtectedSet = False
        
        self.setInitPhase(None)
        self.initPhaseSet = False
        
        self.setDescription(None)
        self.descriptionSet = False
        
        self.setValue(None)
        self.valueSet = False
        
        

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



    def requestSystemProtected (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-systemprotected').debug3Func(): logFunc('called. requested=%s', requested)
        self.systemProtectedRequested = requested
        self.systemProtectedSet = False

    def isSystemProtectedRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-systemprotected-requested').debug3Func(): logFunc('called. requested=%s', self.systemProtectedRequested)
        return self.systemProtectedRequested

    def getSystemProtected (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemprotected').debug3Func(): logFunc('called. self.systemProtectedSet=%s, self.systemProtected=%s', self.systemProtectedSet, self.systemProtected)
        if self.systemProtectedSet:
            return self.systemProtected
        return None

    def hasSystemProtected (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemprotected').debug3Func(): logFunc('called. self.systemProtectedSet=%s, self.systemProtected=%s', self.systemProtectedSet, self.systemProtected)
        if self.systemProtectedSet:
            return True
        return False

    def setSystemProtected (self, systemProtected):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemprotected').debug3Func(): logFunc('called. systemProtected=%s, old=%s', systemProtected, self.systemProtected)
        self.systemProtectedSet = True
        self.systemProtected = systemProtected

    def requestInitPhase (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-initphase').debug3Func(): logFunc('called. requested=%s', requested)
        self.initPhaseRequested = requested
        self.initPhaseSet = False

    def isInitPhaseRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-initphase-requested').debug3Func(): logFunc('called. requested=%s', self.initPhaseRequested)
        return self.initPhaseRequested

    def getInitPhase (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-initphase').debug3Func(): logFunc('called. self.initPhaseSet=%s, self.initPhase=%s', self.initPhaseSet, self.initPhase)
        if self.initPhaseSet:
            return self.initPhase
        return None

    def hasInitPhase (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-initphase').debug3Func(): logFunc('called. self.initPhaseSet=%s, self.initPhase=%s', self.initPhaseSet, self.initPhase)
        if self.initPhaseSet:
            return True
        return False

    def setInitPhase (self, initPhase):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-initphase').debug3Func(): logFunc('called. initPhase=%s, old=%s', initPhase, self.initPhase)
        self.initPhaseSet = True
        self.initPhase = initPhase

    def requestDescription (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-description').debug3Func(): logFunc('called. requested=%s', requested)
        self.descriptionRequested = requested
        self.descriptionSet = False

    def isDescriptionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-description-requested').debug3Func(): logFunc('called. requested=%s', self.descriptionRequested)
        return self.descriptionRequested

    def getDescription (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-description').debug3Func(): logFunc('called. self.descriptionSet=%s, self.description=%s', self.descriptionSet, self.description)
        if self.descriptionSet:
            return self.description
        return None

    def hasDescription (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-description').debug3Func(): logFunc('called. self.descriptionSet=%s, self.description=%s', self.descriptionSet, self.description)
        if self.descriptionSet:
            return True
        return False

    def setDescription (self, description):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-description').debug3Func(): logFunc('called. description=%s, old=%s', description, self.description)
        self.descriptionSet = True
        self.description = description

    def requestValue (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-value').debug3Func(): logFunc('called. requested=%s', requested)
        self.valueRequested = requested
        self.valueSet = False

    def isValueRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-value-requested').debug3Func(): logFunc('called. requested=%s', self.valueRequested)
        return self.valueRequested

    def getValue (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-value').debug3Func(): logFunc('called. self.valueSet=%s, self.value=%s', self.valueSet, self.value)
        if self.valueSet:
            return self.value
        return None

    def hasValue (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-value').debug3Func(): logFunc('called. self.valueSet=%s, self.value=%s', self.valueSet, self.value)
        if self.valueSet:
            return True
        return False

    def setValue (self, value):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-value').debug3Func(): logFunc('called. value=%s, old=%s', value, self.value)
        self.valueSet = True
        self.value = value


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.systemProtected = 0
        self.systemProtectedSet = False
        
        self.initPhase = 0
        self.initPhaseSet = False
        
        self.description = 0
        self.descriptionSet = False
        
        self.value = 0
        self.valueSet = False
        

    def _getSelfKeyPath (self, linux_
                         , variableCollection
                         , variable
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", "qt-lnx-variables"))
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

        
        if self.hasSystemProtected():
            valSystemProtected = Value()
            if self.systemProtected is not None:
                valSystemProtected.setBool(self.systemProtected)
            else:
                valSystemProtected.setEmpty()
            tagValueList.push(("system-protected", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valSystemProtected)
        
        if self.hasInitPhase():
            valInitPhase = Value()
            if self.initPhase is not None:
                valInitPhase.setEnum(self.initPhase.getValue())
            else:
                valInitPhase.setEmpty()
            tagValueList.push(("init-phase", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valInitPhase)
        
        if self.hasDescription():
            valDescription = Value()
            if self.description is not None:
                valDescription.setString(self.description)
            else:
                valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valDescription)
        
        if self.hasValue():
            valValue = Value()
            if self.value is not None:
                valValue.setString(self.value)
            else:
                valValue.setEmpty()
            tagValueList.push(("value", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valValue)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isSystemProtectedRequested():
            valSystemProtected = Value()
            valSystemProtected.setEmpty()
            tagValueList.push(("system-protected", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valSystemProtected)
        
        if self.isInitPhaseRequested():
            valInitPhase = Value()
            valInitPhase.setEmpty()
            tagValueList.push(("init-phase", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valInitPhase)
        
        if self.isDescriptionRequested():
            valDescription = Value()
            valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valDescription)
        
        if self.isValueRequested():
            valValue = Value()
            valValue.setEmpty()
            tagValueList.push(("value", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"), valValue)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isSystemProtectedRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "system-protected") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-systemprotected').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "systemProtected", "system-protected", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-system-protected-bad-value').infoFunc(): logFunc('systemProtected not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSystemProtected(tempVar)
            for logFunc in self._log('read-tag-values-system-protected').debug3Func(): logFunc('read systemProtected. systemProtected=%s, tempValue=%s', self.systemProtected, tempValue.getType())
        
        if self.isInitPhaseRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "init-phase") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-initphase').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "initPhase", "init-phase", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-init-phase-bad-value').infoFunc(): logFunc('initPhase not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInitPhase(tempVar)
            for logFunc in self._log('read-tag-values-init-phase').debug3Func(): logFunc('read initPhase. initPhase=%s, tempValue=%s', self.initPhase, tempValue.getType())
        
        if self.isDescriptionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "description") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-description').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "description", "description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-description-bad-value').infoFunc(): logFunc('description not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDescription(tempVar)
            for logFunc in self._log('read-tag-values-description').debug3Func(): logFunc('read description. description=%s, tempValue=%s', self.description, tempValue.getType())
        
        if self.isValueRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "value") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-value').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "value", "value", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-value-bad-value').infoFunc(): logFunc('value not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setValue(tempVar)
            for logFunc in self._log('read-tag-values-value').debug3Func(): logFunc('read value. value=%s, tempValue=%s', self.value, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
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
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "systemProtected", 
            "yangName": "system-protected", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "initPhase", 
            "yangName": "init-phase", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "initial", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "value", 
            "yangName": "value", 
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
            "qwilt_tech_linux_variables"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "systemProtected", 
            "yangName": "system-protected", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "initPhase", 
            "yangName": "init-phase", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "initial", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux-variables", 
            "moduleYangNamespacePrefix": "qt-lnx-variables", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "value", 
            "yangName": "value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


