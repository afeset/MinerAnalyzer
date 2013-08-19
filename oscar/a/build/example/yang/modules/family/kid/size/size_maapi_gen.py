


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

from size_maapi_base_gen import SizeMaapiBase




class BlinkySizeMaapi(SizeMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-size")
        self.domain = None

        

        
        self.lengthRequested = False
        self.length = None
        self.lengthSet = False
        
        self.smartnessRequested = False
        self.smartness = None
        self.smartnessSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLength(True)
        
        self.requestSmartness(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLength(True)
        
        self.requestSmartness(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLength(False)
        
        self.requestSmartness(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLength(False)
        
        self.requestSmartness(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setLength(None)
        self.lengthSet = False
        
        self.setSmartness(None)
        self.smartnessSet = False
        
        

    def write (self
              , kid
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(kid, trxContext)

    def read (self
              , kid
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(kid, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , kid
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(kid, 
                                  True,
                                  trxContext)



    def requestLength (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-length').debug3Func(): logFunc('called. requested=%s', requested)
        self.lengthRequested = requested
        self.lengthSet = False

    def isLengthRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-length-requested').debug3Func(): logFunc('called. requested=%s', self.lengthRequested)
        return self.lengthRequested

    def getLength (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-length').debug3Func(): logFunc('called. self.lengthSet=%s, self.length=%s', self.lengthSet, self.length)
        if self.lengthSet:
            return self.length
        return None

    def hasLength (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-length').debug3Func(): logFunc('called. self.lengthSet=%s, self.length=%s', self.lengthSet, self.length)
        if self.lengthSet:
            return True
        return False

    def setLength (self, length):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-length').debug3Func(): logFunc('called. length=%s, old=%s', length, self.length)
        self.lengthSet = True
        self.length = length

    def requestSmartness (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-smartness').debug3Func(): logFunc('called. requested=%s', requested)
        self.smartnessRequested = requested
        self.smartnessSet = False

    def isSmartnessRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-smartness-requested').debug3Func(): logFunc('called. requested=%s', self.smartnessRequested)
        return self.smartnessRequested

    def getSmartness (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-smartness').debug3Func(): logFunc('called. self.smartnessSet=%s, self.smartness=%s', self.smartnessSet, self.smartness)
        if self.smartnessSet:
            return self.smartness
        return None

    def hasSmartness (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-smartness').debug3Func(): logFunc('called. self.smartnessSet=%s, self.smartness=%s', self.smartnessSet, self.smartness)
        if self.smartnessSet:
            return True
        return False

    def setSmartness (self, smartness):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-smartness').debug3Func(): logFunc('called. smartness=%s, old=%s', smartness, self.smartness)
        self.smartnessSet = True
        self.smartness = smartness


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.length = 0
        self.lengthSet = False
        
        self.smartness = 0
        self.smartnessSet = False
        

    def _getSelfKeyPath (self, kid
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("size", "http://qwilt.com/model/family", "family"))
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
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(kid, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       kid, 
                       
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
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasLength():
            valLength = Value()
            if self.length is not None:
                valLength.setInt64(self.length)
            else:
                valLength.setEmpty()
            tagValueList.push(("length", "http://qwilt.com/model/family"), valLength)
        
        if self.hasSmartness():
            valSmartness = Value()
            if self.smartness is not None:
                valSmartness.setInt64(self.smartness)
            else:
                valSmartness.setEmpty()
            tagValueList.push(("smartness", "http://qwilt.com/model/family"), valSmartness)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isLengthRequested():
            valLength = Value()
            valLength.setEmpty()
            tagValueList.push(("length", "http://qwilt.com/model/family"), valLength)
        
        if self.isSmartnessRequested():
            valSmartness = Value()
            valSmartness.setEmpty()
            tagValueList.push(("smartness", "http://qwilt.com/model/family"), valSmartness)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isLengthRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "length") or \
                (ns != "http://qwilt.com/model/family"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-length').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "length", "length", "http://qwilt.com/model/family", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-length-bad-value').infoFunc(): logFunc('length not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLength(tempVar)
            for logFunc in self._log('read-tag-values-length').debug3Func(): logFunc('read length. length=%s, tempValue=%s', self.length, tempValue.getType())
        
        if self.isSmartnessRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "smartness") or \
                (ns != "http://qwilt.com/model/family"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-smartness').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "smartness", "smartness", "http://qwilt.com/model/family", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-smartness-bad-value').infoFunc(): logFunc('smartness not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSmartness(tempVar)
            for logFunc in self._log('read-tag-values-smartness').debug3Func(): logFunc('read smartness. smartness=%s, tempValue=%s', self.smartness, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "size", 
        "namespace": "size", 
        "className": "SizeMaapi", 
        "importStatement": "from a.build.example.yang.modules.family.kid.size.size_maapi_gen import SizeMaapi", 
        "baseClassName": "SizeMaapiBase", 
        "baseModule": "size_maapi_base_gen"
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
            "yangName": "size", 
            "namespace": "size", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "name": "size"
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
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "smartness", 
            "yangName": "smartness", 
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
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/family", 
            "moduleYangNamespacePrefix": "family", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "smartness", 
            "yangName": "smartness", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


