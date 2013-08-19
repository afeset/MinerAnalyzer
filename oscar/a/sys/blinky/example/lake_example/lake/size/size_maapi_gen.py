


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

        

        
        self.widthRequested = False
        self.width = None
        self.widthSet = False
        
        self.lengthRequested = False
        self.length = None
        self.lengthSet = False
        
        self.patternNameRequested = False
        self.patternName = None
        self.patternNameSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestWidth(True)
        
        self.requestLength(True)
        
        self.requestPatternName(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestWidth(True)
        
        self.requestLength(True)
        
        self.requestPatternName(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestWidth(False)
        
        self.requestLength(False)
        
        self.requestPatternName(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestWidth(False)
        
        self.requestLength(False)
        
        self.requestPatternName(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setWidth(None)
        self.widthSet = False
        
        self.setLength(None)
        self.lengthSet = False
        
        self.setPatternName(None)
        self.patternNameSet = False
        
        

    def write (self
              , lake
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(lake, trxContext)

    def read (self
              , lake
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lake, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , lake
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lake, 
                                  True,
                                  trxContext)



    def requestWidth (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-width').debug3Func(): logFunc('called. requested=%s', requested)
        self.widthRequested = requested
        self.widthSet = False

    def isWidthRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-width-requested').debug3Func(): logFunc('called. requested=%s', self.widthRequested)
        return self.widthRequested

    def getWidth (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-width').debug3Func(): logFunc('called. self.widthSet=%s, self.width=%s', self.widthSet, self.width)
        if self.widthSet:
            return self.width
        return None

    def hasWidth (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-width').debug3Func(): logFunc('called. self.widthSet=%s, self.width=%s', self.widthSet, self.width)
        if self.widthSet:
            return True
        return False

    def setWidth (self, width):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-width').debug3Func(): logFunc('called. width=%s, old=%s', width, self.width)
        self.widthSet = True
        self.width = width

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

    def requestPatternName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-patternname').debug3Func(): logFunc('called. requested=%s', requested)
        self.patternNameRequested = requested
        self.patternNameSet = False

    def isPatternNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-patternname-requested').debug3Func(): logFunc('called. requested=%s', self.patternNameRequested)
        return self.patternNameRequested

    def getPatternName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-patternname').debug3Func(): logFunc('called. self.patternNameSet=%s, self.patternName=%s', self.patternNameSet, self.patternName)
        if self.patternNameSet:
            return self.patternName
        return None

    def hasPatternName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-patternname').debug3Func(): logFunc('called. self.patternNameSet=%s, self.patternName=%s', self.patternNameSet, self.patternName)
        if self.patternNameSet:
            return True
        return False

    def setPatternName (self, patternName):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-patternname').debug3Func(): logFunc('called. patternName=%s, old=%s', patternName, self.patternName)
        self.patternNameSet = True
        self.patternName = patternName


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.width = 0
        self.widthSet = False
        
        self.length = 0
        self.lengthSet = False
        
        self.patternName = 0
        self.patternNameSet = False
        

    def _getSelfKeyPath (self, lake
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("size", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(lake);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("lake", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        lake, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(lake, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(lake, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       lake, 
                       
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

        keyPath = self._getSelfKeyPath(lake, 
                                       
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
                               lake, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasWidth():
            valWidth = Value()
            if self.width is not None:
                valWidth.setInt64(self.width)
            else:
                valWidth.setEmpty()
            tagValueList.push(("width", "http://qwilt.com/model/lake-example"), valWidth)
        
        if self.hasLength():
            valLength = Value()
            if self.length is not None:
                valLength.setInt64(self.length)
            else:
                valLength.setEmpty()
            tagValueList.push(("length", "http://qwilt.com/model/lake-example"), valLength)
        
        if self.hasPatternName():
            valPatternName = Value()
            if self.patternName is not None:
                valPatternName.setString(self.patternName)
            else:
                valPatternName.setEmpty()
            tagValueList.push(("pattern-name", "http://qwilt.com/model/lake-example"), valPatternName)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isWidthRequested():
            valWidth = Value()
            valWidth.setEmpty()
            tagValueList.push(("width", "http://qwilt.com/model/lake-example"), valWidth)
        
        if self.isLengthRequested():
            valLength = Value()
            valLength.setEmpty()
            tagValueList.push(("length", "http://qwilt.com/model/lake-example"), valLength)
        
        if self.isPatternNameRequested():
            valPatternName = Value()
            valPatternName.setEmpty()
            tagValueList.push(("pattern-name", "http://qwilt.com/model/lake-example"), valPatternName)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isWidthRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "width") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-width').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "width", "width", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-width-bad-value').infoFunc(): logFunc('width not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setWidth(tempVar)
            for logFunc in self._log('read-tag-values-width').debug3Func(): logFunc('read width. width=%s, tempValue=%s', self.width, tempValue.getType())
        
        if self.isLengthRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "length") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-length').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "length", "length", "http://qwilt.com/model/lake-example", tag, ns)
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
        
        if self.isPatternNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pattern-name") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-patternname').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "patternName", "pattern-name", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pattern-name-bad-value').infoFunc(): logFunc('patternName not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPatternName(tempVar)
            for logFunc in self._log('read-tag-values-pattern-name').debug3Func(): logFunc('read patternName. patternName=%s, tempValue=%s', self.patternName, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "size", 
        "namespace": "size", 
        "className": "SizeMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.size.size_maapi_gen import SizeMaapi", 
        "baseClassName": "SizeMaapiBase", 
        "baseModule": "size_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": false, 
            "yangName": "lake", 
            "namespace": "lake", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "lake", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lake"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "size", 
            "namespace": "size", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "size"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "width", 
            "yangName": "width", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "15", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "patternName", 
            "yangName": "pattern-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "solid", 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "lake_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "width", 
            "yangName": "width", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "15", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "length", 
            "yangName": "length", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "patternName", 
            "yangName": "pattern-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "solid", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


