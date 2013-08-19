


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

from antenna_maapi_base_gen import AntennaMaapiBase

from a.build.example.yang.modules.room.table.fish_.antenna.part.part_maapi_list_gen import BlinkyPartMaapiList



class BlinkyAntennaMaapi(AntennaMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-antenna")
        self.domain = None

        
        self.partListObj = None
        

        
        self.heightRequested = False
        self.height = None
        self.heightSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestHeight(True)
        
        
        
        if not self.partListObj:
            self.partListObj = self.newPartList()
            self.partListObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestHeight(True)
        
        
        
        if not self.partListObj:
            self.partListObj = self.newPartList()
            self.partListObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestHeight(False)
        
        
        
        if not self.partListObj:
            self.partListObj = self.newPartList()
            self.partListObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestHeight(False)
        
        
        
        if not self.partListObj:
            self.partListObj = self.newPartList()
            self.partListObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setHeight(None)
        self.heightSet = False
        
        
        if self.partListObj:
            self.partListObj.clearAllSet()
        

    def write (self
              , table
              , fish_
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(table, fish_, trxContext)

    def read (self
              , table
              , fish_
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(table, fish_, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , table
                       , fish_
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(table, fish_, 
                                  True,
                                  trxContext)

    def newPartList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-partlist').debug3Func(): logFunc('called.')
        partList = BlinkyPartMaapiList(self._log)
        partList.init(self.domain)
        return partList

    def setPartListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-partlist').debug3Func(): logFunc('called. obj=%s', obj)
        self.partListObj = obj

    def getPartListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-partlist').debug3Func(): logFunc('called. self.partListObj=%s', self.partListObj)
        return self.partListObj

    def hasPartList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-partlist').debug3Func(): logFunc('called. self.partListObj=%s', self.partListObj)
        if self.partListObj:
            return True
        return False



    def requestHeight (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-height').debug3Func(): logFunc('called. requested=%s', requested)
        self.heightRequested = requested
        self.heightSet = False

    def isHeightRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-height-requested').debug3Func(): logFunc('called. requested=%s', self.heightRequested)
        return self.heightRequested

    def getHeight (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-height').debug3Func(): logFunc('called. self.heightSet=%s, self.height=%s', self.heightSet, self.height)
        if self.heightSet:
            return self.height
        return None

    def hasHeight (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-height').debug3Func(): logFunc('called. self.heightSet=%s, self.height=%s', self.heightSet, self.height)
        if self.heightSet:
            return True
        return False

    def setHeight (self, height):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-height').debug3Func(): logFunc('called. height=%s, old=%s', height, self.height)
        self.heightSet = True
        self.height = height


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.partListObj:
            self.partListObj._clearAllReadData()
        

        
        self.height = 0
        self.heightSet = False
        

    def _getSelfKeyPath (self, table
                         , fish_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("antenna", "http://qwilt.com/model/room", "room"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(fish_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("fish", "http://qwilt.com/model/room", "room"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(table);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("table", "http://qwilt.com/model/room", "room"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        table, 
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
        res = self._collectItemsToDelete(table, 
                                         fish_, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(table, 
                                       fish_, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       table, 
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

        keyPath = self._getSelfKeyPath(table, 
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
                               table, 
                               fish_, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.partListObj:
            res = self.partListObj._collectItemsToDelete(table, 
                                                                          fish_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-parts-failed').errorFunc(): logFunc('partListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasHeight():
            valHeight = Value()
            if self.height is not None:
                valHeight.setInt64(self.height)
            else:
                valHeight.setEmpty()
            tagValueList.push(("height", "http://qwilt.com/model/room"), valHeight)
        

        
        if self.partListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("parts" , "http://qwilt.com/model/room", "room")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.partListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-parts-failed').errorFunc(): logFunc('partListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isHeightRequested():
            valHeight = Value()
            valHeight.setEmpty()
            tagValueList.push(("height", "http://qwilt.com/model/room"), valHeight)
        

        
        if self.partListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("parts" , "http://qwilt.com/model/room", "room")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.partListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-parts-failed').errorFunc(): logFunc('partListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isHeightRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "height") or \
                (ns != "http://qwilt.com/model/room"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-height').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "height", "height", "http://qwilt.com/model/room", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-height-bad-value').infoFunc(): logFunc('height not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setHeight(tempVar)
            for logFunc in self._log('read-tag-values-height').debug3Func(): logFunc('read height. height=%s, tempValue=%s', self.height, tempValue.getType())
        

        
        if self.partListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "parts") or \
                (ns != "http://qwilt.com/model/room") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "parts", "http://qwilt.com/model/room", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.partListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-parts-failed').errorFunc(): logFunc('partListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "parts") or \
                (ns != "http://qwilt.com/model/room") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "parts", "http://qwilt.com/model/room", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "antenna", 
        "namespace": "antenna", 
        "className": "AntennaMaapi", 
        "importStatement": "from a.build.example.yang.modules.room.table.fish_.antenna.antenna_maapi_gen import AntennaMaapi", 
        "baseClassName": "AntennaMaapiBase", 
        "baseModule": "antenna_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "room", 
            "isCurrent": false, 
            "yangName": "table", 
            "namespace": "table", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "keyLeaf": {
                "varName": "table", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "table"
        }, 
        {
            "moduleYangNamespacePrefix": "room", 
            "isCurrent": false, 
            "yangName": "fish", 
            "namespace": "fish_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "keyLeaf": {
                "varName": "fish_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "fish_"
        }, 
        {
            "moduleYangNamespacePrefix": "room", 
            "yangName": "antenna", 
            "namespace": "antenna", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "name": "antenna"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "room", 
            "memberName": "partList", 
            "yangName": "parts", 
            "className": "BlinkyPartMaapiList", 
            "importStatement": "from a.build.example.yang.modules.room.table.fish_.antenna.part.part_maapi_list_gen import BlinkyPartMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/room"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
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
            "room"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/room", 
            "moduleYangNamespacePrefix": "room", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


