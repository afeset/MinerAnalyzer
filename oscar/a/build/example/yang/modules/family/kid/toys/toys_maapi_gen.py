


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

from toys_maapi_base_gen import ToysMaapiBase




class BlinkyToysMaapi(ToysMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-toys")
        self.domain = None

        

        
        self.eyeNumberRequested = False
        self.eyeNumber = None
        self.eyeNumberSet = False
        
        self.transparentFieldRequested = False
        self.transparentField = None
        self.transparentFieldSet = False
        
        self.idRequested = False
        self.id = None
        self.idSet = False
        
        self.hasTailRequested = False
        self.hasTail = None
        self.hasTailSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEyeNumber(True)
        
        self.requestTransparentField(True)
        
        self.requestId(True)
        
        self.requestHasTail(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEyeNumber(True)
        
        self.requestTransparentField(True)
        
        self.requestId(True)
        
        self.requestHasTail(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEyeNumber(False)
        
        self.requestTransparentField(False)
        
        self.requestId(False)
        
        self.requestHasTail(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestEyeNumber(False)
        
        self.requestTransparentField(False)
        
        self.requestId(False)
        
        self.requestHasTail(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setEyeNumber(None)
        self.eyeNumberSet = False
        
        self.setTransparentField(None)
        self.transparentFieldSet = False
        
        self.setId(None)
        self.idSet = False
        
        self.setHasTail(None)
        self.hasTailSet = False
        
        

    def write (self
              , kid
              , toys
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(kid, toys, trxContext)

    def read (self
              , kid
              , toys
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(kid, toys, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , kid
                       , toys
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(kid, toys, 
                                  True,
                                  trxContext)



    def requestEyeNumber (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-eyenumber').debug3Func(): logFunc('called. requested=%s', requested)
        self.eyeNumberRequested = requested
        self.eyeNumberSet = False

    def isEyeNumberRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-eyenumber-requested').debug3Func(): logFunc('called. requested=%s', self.eyeNumberRequested)
        return self.eyeNumberRequested

    def getEyeNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-eyenumber').debug3Func(): logFunc('called. self.eyeNumberSet=%s, self.eyeNumber=%s', self.eyeNumberSet, self.eyeNumber)
        if self.eyeNumberSet:
            return self.eyeNumber
        return None

    def hasEyeNumber (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-eyenumber').debug3Func(): logFunc('called. self.eyeNumberSet=%s, self.eyeNumber=%s', self.eyeNumberSet, self.eyeNumber)
        if self.eyeNumberSet:
            return True
        return False

    def setEyeNumber (self, eyeNumber):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-eyenumber').debug3Func(): logFunc('called. eyeNumber=%s, old=%s', eyeNumber, self.eyeNumber)
        self.eyeNumberSet = True
        self.eyeNumber = eyeNumber

    def requestTransparentField (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-transparentfield').debug3Func(): logFunc('called. requested=%s', requested)
        self.transparentFieldRequested = requested
        self.transparentFieldSet = False

    def isTransparentFieldRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-transparentfield-requested').debug3Func(): logFunc('called. requested=%s', self.transparentFieldRequested)
        return self.transparentFieldRequested

    def getTransparentField (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-transparentfield').debug3Func(): logFunc('called. self.transparentFieldSet=%s, self.transparentField=%s', self.transparentFieldSet, self.transparentField)
        if self.transparentFieldSet:
            return self.transparentField
        return None

    def hasTransparentField (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-transparentfield').debug3Func(): logFunc('called. self.transparentFieldSet=%s, self.transparentField=%s', self.transparentFieldSet, self.transparentField)
        if self.transparentFieldSet:
            return True
        return False

    def setTransparentField (self, transparentField):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-transparentfield').debug3Func(): logFunc('called. transparentField=%s, old=%s', transparentField, self.transparentField)
        self.transparentFieldSet = True
        self.transparentField = transparentField

    def requestId (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-id').debug3Func(): logFunc('called. requested=%s', requested)
        self.idRequested = requested
        self.idSet = False

    def isIdRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-id-requested').debug3Func(): logFunc('called. requested=%s', self.idRequested)
        return self.idRequested

    def getId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-id').debug3Func(): logFunc('called. self.idSet=%s, self.id=%s', self.idSet, self.id)
        if self.idSet:
            return self.id
        return None

    def hasId (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-id').debug3Func(): logFunc('called. self.idSet=%s, self.id=%s', self.idSet, self.id)
        if self.idSet:
            return True
        return False

    def setId (self, id):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-id').debug3Func(): logFunc('called. id=%s, old=%s', id, self.id)
        self.idSet = True
        self.id = id

    def requestHasTail (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-hastail').debug3Func(): logFunc('called. requested=%s', requested)
        self.hasTailRequested = requested
        self.hasTailSet = False

    def isHasTailRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-hastail-requested').debug3Func(): logFunc('called. requested=%s', self.hasTailRequested)
        return self.hasTailRequested

    def getHasTail (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-hastail').debug3Func(): logFunc('called. self.hasTailSet=%s, self.hasTail=%s', self.hasTailSet, self.hasTail)
        if self.hasTailSet:
            return self.hasTail
        return None

    def hasHasTail (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-hastail').debug3Func(): logFunc('called. self.hasTailSet=%s, self.hasTail=%s', self.hasTailSet, self.hasTail)
        if self.hasTailSet:
            return True
        return False

    def setHasTail (self, hasTail):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-hastail').debug3Func(): logFunc('called. hasTail=%s, old=%s', hasTail, self.hasTail)
        self.hasTailSet = True
        self.hasTail = hasTail


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.eyeNumber = 0
        self.eyeNumberSet = False
        
        self.transparentField = 0
        self.transparentFieldSet = False
        
        self.id = 0
        self.idSet = False
        
        self.hasTail = 0
        self.hasTailSet = False
        

    def _getSelfKeyPath (self, kid
                         , toys
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(toys);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("toys", "http://qwilt.com/model/family", "family"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(kid);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("kid", "http://qwilt.com/model/family", "family"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        kid, 
                        toys, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(kid, 
                                         toys, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(kid, 
                                       toys, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       kid, 
                       toys, 
                       
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

        keyPath = self._getSelfKeyPath(kid, 
                                       toys, 
                                       
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
                               kid, 
                               toys, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasEyeNumber():
            valEyeNumber = Value()
            if self.eyeNumber is not None:
                valEyeNumber.setInt64(self.eyeNumber)
            else:
                valEyeNumber.setEmpty()
            tagValueList.push(("eye-number", "http://qwilt.com/model/family"), valEyeNumber)
        
        if self.hasTransparentField():
            valTransparentField = Value()
            if self.transparentField is not None:
                valTransparentField.setBool(self.transparentField)
            else:
                valTransparentField.setEmpty()
            tagValueList.push(("transparent-field", "http://qwilt.com/model/family"), valTransparentField)
        
        if self.hasId():
            valId = Value()
            if self.id is not None:
                valId.setString(self.id)
            else:
                valId.setEmpty()
            tagValueList.push(("id", "http://qwilt.com/model/family"), valId)
        
        if self.hasHasTail():
            valHasTail = Value()
            if self.hasTail is not None:
                valHasTail.setBool(self.hasTail)
            else:
                valHasTail.setEmpty()
            tagValueList.push(("has-tail", "http://qwilt.com/model/family"), valHasTail)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isEyeNumberRequested():
            valEyeNumber = Value()
            valEyeNumber.setEmpty()
            tagValueList.push(("eye-number", "http://qwilt.com/model/family"), valEyeNumber)
        
        if self.isTransparentFieldRequested():
            valTransparentField = Value()
            valTransparentField.setEmpty()
            tagValueList.push(("transparent-field", "http://qwilt.com/model/family"), valTransparentField)
        
        if self.isIdRequested():
            valId = Value()
            valId.setEmpty()
            tagValueList.push(("id", "http://qwilt.com/model/family"), valId)
        
        if self.isHasTailRequested():
            valHasTail = Value()
            valHasTail.setEmpty()
            tagValueList.push(("has-tail", "http://qwilt.com/model/family"), valHasTail)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isEyeNumberRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "eye-number") or \
                (ns != "http://qwilt.com/model/family"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-eyenumber').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "eyeNumber", "eye-number", "http://qwilt.com/model/family", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-eye-number-bad-value').infoFunc(): logFunc('eyeNumber not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setEyeNumber(tempVar)
            for logFunc in self._log('read-tag-values-eye-number').debug3Func(): logFunc('read eyeNumber. eyeNumber=%s, tempValue=%s', self.eyeNumber, tempValue.getType())
        
        if self.isTransparentFieldRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "transparent-field") or \
                (ns != "http://qwilt.com/model/family"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-transparentfield').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "transparentField", "transparent-field", "http://qwilt.com/model/family", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-transparent-field-bad-value').infoFunc(): logFunc('transparentField not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setTransparentField(tempVar)
            for logFunc in self._log('read-tag-values-transparent-field').debug3Func(): logFunc('read transparentField. transparentField=%s, tempValue=%s', self.transparentField, tempValue.getType())
        
        if self.isIdRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "id") or \
                (ns != "http://qwilt.com/model/family"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-id').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "id", "id", "http://qwilt.com/model/family", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-id-bad-value').infoFunc(): logFunc('id not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setId(tempVar)
            for logFunc in self._log('read-tag-values-id').debug3Func(): logFunc('read id. id=%s, tempValue=%s', self.id, tempValue.getType())
        
        if self.isHasTailRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "has-tail") or \
                (ns != "http://qwilt.com/model/family"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-hastail').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "hasTail", "has-tail", "http://qwilt.com/model/family", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-has-tail-bad-value').infoFunc(): logFunc('hasTail not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHasTail(tempVar)
            for logFunc in self._log('read-tag-values-has-tail').debug3Func(): logFunc('read hasTail. hasTail=%s, tempValue=%s', self.hasTail, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "toys", 
        "namespace": "toys", 
        "className": "ToysMaapi", 
        "importStatement": "from a.build.example.yang.modules.family.kid.toys.toys_maapi_gen import ToysMaapi", 
        "baseClassName": "ToysMaapiBase", 
        "baseModule": "toys_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "family", 
            "isCurrent": false, 
            "yangName": "kid", 
            "namespace": "kid", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "keyLeaf": {
                "varName": "kid", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "kid"
        }, 
        {
            "moduleYangNamespacePrefix": "family", 
            "isCurrent": true, 
            "yangName": "toys", 
            "namespace": "toys", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "keyLeaf": {
                "varName": "toys", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "toys"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "build", 
            "example", 
            "yang", 
            "modules", 
            "family"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "eyeNumber", 
            "yangName": "eye-number", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "transparentField", 
            "yangName": "transparent-field", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "hasTail", 
            "yangName": "has-tail", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


