


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


from a.api.yang.modules.tech.common.qwilt_tech_storage_module.qwilt_tech_storage_module_module_gen import StorageModuleLocationTypeType


class BlinkySystemDefaultsMaapi(SystemDefaultsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-systemDefaults")
        self.domain = None

        

        
        self.controllerRequested = False
        self.controller = None
        self.controllerSet = False
        
        self.enabledRequested = False
        self.enabled = None
        self.enabledSet = False
        
        self.descriptionRequested = False
        self.description = None
        self.descriptionSet = False
        
        self.locationTypeRequested = False
        self.locationType = None
        self.locationTypeSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestController(True)
        
        self.requestEnabled(True)
        
        self.requestDescription(True)
        
        self.requestLocationType(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestController(True)
        
        self.requestEnabled(True)
        
        self.requestDescription(True)
        
        self.requestLocationType(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestController(False)
        
        self.requestEnabled(False)
        
        self.requestDescription(False)
        
        self.requestLocationType(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestController(False)
        
        self.requestEnabled(False)
        
        self.requestDescription(False)
        
        self.requestLocationType(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setController(None)
        self.controllerSet = False
        
        self.setEnabled(None)
        self.enabledSet = False
        
        self.setDescription(None)
        self.descriptionSet = False
        
        self.setLocationType(None)
        self.locationTypeSet = False
        
        

    def write (self
              , module
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(module, trxContext)

    def read (self
              , module
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(module, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , module
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(module, 
                                  True,
                                  trxContext)



    def requestController (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-controller').debug3Func(): logFunc('called. requested=%s', requested)
        self.controllerRequested = requested
        self.controllerSet = False

    def isControllerRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-controller-requested').debug3Func(): logFunc('called. requested=%s', self.controllerRequested)
        return self.controllerRequested

    def getController (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-controller').debug3Func(): logFunc('called. self.controllerSet=%s, self.controller=%s', self.controllerSet, self.controller)
        if self.controllerSet:
            return self.controller
        return None

    def hasController (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-controller').debug3Func(): logFunc('called. self.controllerSet=%s, self.controller=%s', self.controllerSet, self.controller)
        if self.controllerSet:
            return True
        return False

    def setController (self, controller):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-controller').debug3Func(): logFunc('called. controller=%s, old=%s', controller, self.controller)
        self.controllerSet = True
        self.controller = controller

    def requestEnabled (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-enabled').debug3Func(): logFunc('called. requested=%s', requested)
        self.enabledRequested = requested
        self.enabledSet = False

    def isEnabledRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-enabled-requested').debug3Func(): logFunc('called. requested=%s', self.enabledRequested)
        return self.enabledRequested

    def getEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return self.enabled
        return None

    def hasEnabled (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-enabled').debug3Func(): logFunc('called. self.enabledSet=%s, self.enabled=%s', self.enabledSet, self.enabled)
        if self.enabledSet:
            return True
        return False

    def setEnabled (self, enabled):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-enabled').debug3Func(): logFunc('called. enabled=%s, old=%s', enabled, self.enabled)
        self.enabledSet = True
        self.enabled = enabled

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

    def requestLocationType (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-locationtype').debug3Func(): logFunc('called. requested=%s', requested)
        self.locationTypeRequested = requested
        self.locationTypeSet = False

    def isLocationTypeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-locationtype-requested').debug3Func(): logFunc('called. requested=%s', self.locationTypeRequested)
        return self.locationTypeRequested

    def getLocationType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-locationtype').debug3Func(): logFunc('called. self.locationTypeSet=%s, self.locationType=%s', self.locationTypeSet, self.locationType)
        if self.locationTypeSet:
            return self.locationType
        return None

    def hasLocationType (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-locationtype').debug3Func(): logFunc('called. self.locationTypeSet=%s, self.locationType=%s', self.locationTypeSet, self.locationType)
        if self.locationTypeSet:
            return True
        return False

    def setLocationType (self, locationType):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-locationtype').debug3Func(): logFunc('called. locationType=%s, old=%s', locationType, self.locationType)
        self.locationTypeSet = True
        self.locationType = locationType


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.controller = 0
        self.controllerSet = False
        
        self.enabled = 0
        self.enabledSet = False
        
        self.description = 0
        self.descriptionSet = False
        
        self.locationType = 0
        self.locationTypeSet = False
        

    def _getSelfKeyPath (self, module
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", "qt-strg-module"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(module);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("module", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", "qt-strg-module"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("storage", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", "qt-strg"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        module, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(module, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(module, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       module, 
                       
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

        keyPath = self._getSelfKeyPath(module, 
                                       
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
                               module, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasController():
            valController = Value()
            if self.controller is not None:
                valController.setString(self.controller)
            else:
                valController.setEmpty()
            tagValueList.push(("controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"), valController)
        
        if self.hasEnabled():
            valEnabled = Value()
            if self.enabled is not None:
                valEnabled.setBool(self.enabled)
            else:
                valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"), valEnabled)
        
        if self.hasDescription():
            valDescription = Value()
            if self.description is not None:
                valDescription.setString(self.description)
            else:
                valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"), valDescription)
        
        if self.hasLocationType():
            valLocationType = Value()
            if self.locationType is not None:
                valLocationType.setEnum(self.locationType.getValue())
            else:
                valLocationType.setEmpty()
            tagValueList.push(("location-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"), valLocationType)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isControllerRequested():
            valController = Value()
            valController.setEmpty()
            tagValueList.push(("controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"), valController)
        
        if self.isEnabledRequested():
            valEnabled = Value()
            valEnabled.setEmpty()
            tagValueList.push(("enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"), valEnabled)
        
        if self.isDescriptionRequested():
            valDescription = Value()
            valDescription.setEmpty()
            tagValueList.push(("description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"), valDescription)
        
        if self.isLocationTypeRequested():
            valLocationType = Value()
            valLocationType.setEmpty()
            tagValueList.push(("location-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"), valLocationType)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isControllerRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "controller") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-controller').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "controller", "controller", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-controller-bad-value').infoFunc(): logFunc('controller not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setController(tempVar)
            for logFunc in self._log('read-tag-values-controller').debug3Func(): logFunc('read controller. controller=%s, tempValue=%s', self.controller, tempValue.getType())
        
        if self.isEnabledRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "enabled") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-enabled').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "enabled", "enabled", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-enabled-bad-value').infoFunc(): logFunc('enabled not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEnabled(tempVar)
            for logFunc in self._log('read-tag-values-enabled').debug3Func(): logFunc('read enabled. enabled=%s, tempValue=%s', self.enabled, tempValue.getType())
        
        if self.isDescriptionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "description") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-description').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "description", "description", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", tag, ns)
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
        
        if self.isLocationTypeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "location-type") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-locationtype').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "locationType", "location-type", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-location-type-bad-value').infoFunc(): logFunc('locationType not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLocationType(tempVar)
            for logFunc in self._log('read-tag-values-location-type').debug3Func(): logFunc('read locationType. locationType=%s, tempValue=%s', self.locationType, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_module.tech.storage.module.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
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
            "moduleYangNamespacePrefix": "qt-strg", 
            "yangName": "storage", 
            "namespace": "storage", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage", 
            "name": "storage"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "isCurrent": false, 
            "yangName": "module", 
            "namespace": "module", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "keyLeaf": {
                "varName": "module", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "module"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "controller", 
            "yangName": "controller", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "locationType", 
            "yangName": "location-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
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
            "qwilt_tech_storage_module"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "controller", 
            "yangName": "controller", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-storage-module", 
            "moduleYangNamespacePrefix": "qt-strg-module", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "locationType", 
            "yangName": "location-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


