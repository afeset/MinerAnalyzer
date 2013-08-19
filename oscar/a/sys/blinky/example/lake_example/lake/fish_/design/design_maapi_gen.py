


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

from design_maapi_base_gen import DesignMaapiBase


from a.infra.net.mac_address import MacAddress
from a.sys.blinky.example.lake_example.lake_example_module_gen import DesignColorT


class BlinkyDesignMaapi(DesignMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-design")
        self.domain = None

        

        
        self.colorRequested = False
        self.color = None
        self.colorSet = False
        
        self.patternRequested = False
        self.pattern = None
        self.patternSet = False
        
        self.macAddressRequested = False
        self.macAddress = None
        self.macAddressSet = False
        
        self.lineWidthRequested = False
        self.lineWidth = None
        self.lineWidthSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestColor(True)
        
        self.requestPattern(True)
        
        self.requestMacAddress(True)
        
        self.requestLineWidth(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestColor(False)
        
        self.requestPattern(False)
        
        self.requestMacAddress(False)
        
        self.requestLineWidth(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestColor(True)
        
        self.requestPattern(True)
        
        self.requestMacAddress(True)
        
        self.requestLineWidth(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestColor(False)
        
        self.requestPattern(False)
        
        self.requestMacAddress(False)
        
        self.requestLineWidth(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , lake
              , fish_
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(lake, fish_, trxContext)

    def read (self
              , lake
              , fish_
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lake, fish_, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , lake
                       , fish_
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lake, fish_, 
                                  True,
                                  trxContext)



    def requestColor (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-color').debug3Func(): logFunc('called. requested=%s', requested)
        self.colorRequested = requested
        self.colorSet = False

    def isColorRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-color-requested').debug3Func(): logFunc('called. requested=%s', self.colorRequested)
        return self.colorRequested

    def getColor (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-color').debug3Func(): logFunc('called. self.colorSet=%s, self.color=%s', self.colorSet, self.color)
        if self.colorSet:
            return self.color
        return None

    def hasColor (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-color').debug3Func(): logFunc('called. self.colorSet=%s, self.color=%s', self.colorSet, self.color)
        if self.colorSet:
            return True
        return False

    def setColor (self, color):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-color').debug3Func(): logFunc('called. color=%s, old=%s', color, self.color)
        self.colorSet = True
        self.color = color

    def requestPattern (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pattern').debug3Func(): logFunc('called. requested=%s', requested)
        self.patternRequested = requested
        self.patternSet = False

    def isPatternRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pattern-requested').debug3Func(): logFunc('called. requested=%s', self.patternRequested)
        return self.patternRequested

    def getPattern (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pattern').debug3Func(): logFunc('called. self.patternSet=%s, self.pattern=%s', self.patternSet, self.pattern)
        if self.patternSet:
            return self.pattern
        return None

    def hasPattern (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pattern').debug3Func(): logFunc('called. self.patternSet=%s, self.pattern=%s', self.patternSet, self.pattern)
        if self.patternSet:
            return True
        return False

    def setPattern (self, pattern):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pattern').debug3Func(): logFunc('called. pattern=%s, old=%s', pattern, self.pattern)
        self.patternSet = True
        self.pattern = pattern

    def requestMacAddress (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-macaddress').debug3Func(): logFunc('called. requested=%s', requested)
        self.macAddressRequested = requested
        self.macAddressSet = False

    def isMacAddressRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-macaddress-requested').debug3Func(): logFunc('called. requested=%s', self.macAddressRequested)
        return self.macAddressRequested

    def getMacAddress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-macaddress').debug3Func(): logFunc('called. self.macAddressSet=%s, self.macAddress=%s', self.macAddressSet, self.macAddress)
        if self.macAddressSet:
            return self.macAddress
        return None

    def hasMacAddress (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-macaddress').debug3Func(): logFunc('called. self.macAddressSet=%s, self.macAddress=%s', self.macAddressSet, self.macAddress)
        if self.macAddressSet:
            return True
        return False

    def setMacAddress (self, macAddress):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-macaddress').debug3Func(): logFunc('called. macAddress=%s, old=%s', macAddress, self.macAddress)
        self.macAddressSet = True
        self.macAddress = macAddress

    def requestLineWidth (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-linewidth').debug3Func(): logFunc('called. requested=%s', requested)
        self.lineWidthRequested = requested
        self.lineWidthSet = False

    def isLineWidthRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-linewidth-requested').debug3Func(): logFunc('called. requested=%s', self.lineWidthRequested)
        return self.lineWidthRequested

    def getLineWidth (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-linewidth').debug3Func(): logFunc('called. self.lineWidthSet=%s, self.lineWidth=%s', self.lineWidthSet, self.lineWidth)
        if self.lineWidthSet:
            return self.lineWidth
        return None

    def hasLineWidth (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-linewidth').debug3Func(): logFunc('called. self.lineWidthSet=%s, self.lineWidth=%s', self.lineWidthSet, self.lineWidth)
        if self.lineWidthSet:
            return True
        return False

    def setLineWidth (self, lineWidth):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-linewidth').debug3Func(): logFunc('called. lineWidth=%s, old=%s', lineWidth, self.lineWidth)
        self.lineWidthSet = True
        self.lineWidth = lineWidth


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.color = 0
        self.colorSet = False
        
        self.pattern = 0
        self.patternSet = False
        
        self.macAddress = 0
        self.macAddressSet = False
        
        self.lineWidth = 0
        self.lineWidthSet = False
        

    def _getSelfKeyPath (self, lake
                         , fish_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("design", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(fish_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fish", "http://qwilt.com/model/lake-example", "lake-example"))
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
                        fish_, 
                        
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
                                         fish_, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(lake, 
                                       fish_, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       lake, 
                       fish_, 
                       
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
                                       fish_, 
                                       
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
                               fish_, 
                               
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

        
        if self.isColorRequested():
            valColor = Value()
            valColor.setEmpty()
            tagValueList.push(("color", "http://qwilt.com/model/lake-example"), valColor)
        
        if self.isPatternRequested():
            valPattern = Value()
            valPattern.setEmpty()
            tagValueList.push(("pattern", "http://qwilt.com/model/lake-example"), valPattern)
        
        if self.isMacAddressRequested():
            valMacAddress = Value()
            valMacAddress.setEmpty()
            tagValueList.push(("mac-address", "http://qwilt.com/model/lake-example"), valMacAddress)
        
        if self.isLineWidthRequested():
            valLineWidth = Value()
            valLineWidth.setEmpty()
            tagValueList.push(("line-width", "http://qwilt.com/model/lake-example"), valLineWidth)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isColorRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "color") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-color').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "color", "color", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-color-bad-value').infoFunc(): logFunc('color not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setColor(tempVar)
            for logFunc in self._log('read-tag-values-color').debug3Func(): logFunc('read color. color=%s, tempValue=%s', self.color, tempValue.getType())
        
        if self.isPatternRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pattern") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pattern').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pattern", "pattern", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pattern-bad-value').infoFunc(): logFunc('pattern not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPattern(tempVar)
            for logFunc in self._log('read-tag-values-pattern').debug3Func(): logFunc('read pattern. pattern=%s, tempValue=%s', self.pattern, tempValue.getType())
        
        if self.isMacAddressRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mac-address") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-macaddress').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "macAddress", "mac-address", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = MacAddress('\0'*6)
            tempVar = MacAddress(tempValue.asBinary())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mac-address-bad-value').infoFunc(): logFunc('macAddress not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMacAddress(tempVar)
            for logFunc in self._log('read-tag-values-mac-address').debug3Func(): logFunc('read macAddress. macAddress=%s, tempValue=%s', self.macAddress, tempValue.getType())
        
        if self.isLineWidthRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "line-width") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-linewidth').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "lineWidth", "line-width", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt8()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-line-width-bad-value').infoFunc(): logFunc('lineWidth not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLineWidth(tempVar)
            for logFunc in self._log('read-tag-values-line-width').debug3Func(): logFunc('read lineWidth. lineWidth=%s, tempValue=%s', self.lineWidth, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "design", 
        "namespace": "design", 
        "className": "DesignMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.design.design_maapi_gen import DesignMaapi", 
        "baseClassName": "DesignMaapiBase", 
        "baseModule": "design_maapi_base_gen"
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
            "isCurrent": false, 
            "yangName": "fish", 
            "namespace": "fish_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "keyLeaf": {
                "varName": "fish_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fish_"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "design", 
            "namespace": "design", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "design"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pattern", 
            "yangName": "pattern", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "lineWidth", 
            "yangName": "line-width", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "pattern", 
            "yangName": "pattern", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: MacAddressHandlerPy", 
            "memberName": "macAddress", 
            "yangName": "mac-address", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "lineWidth", 
            "yangName": "line-width", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


