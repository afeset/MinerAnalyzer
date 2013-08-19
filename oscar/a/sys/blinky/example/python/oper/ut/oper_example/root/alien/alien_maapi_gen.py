


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

from alien_maapi_base_gen import AlienMaapiBase

from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.status_wrapper.status_wrapper_maapi_gen import BlinkyStatusWrapperMaapi



class BlinkyAlienMaapi(AlienMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-alien")
        self.domain = None

        
        self.statusWrapperObj = None
        

        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        
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
        
        self.requestName(True)
        
        self.requestHeight(True)
        
        
        
        if not self.statusWrapperObj:
            self.statusWrapperObj = self.newStatusWrapper()
            self.statusWrapperObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(True)
        
        self.requestHeight(True)
        
        
        
        if not self.statusWrapperObj:
            self.statusWrapperObj = self.newStatusWrapper()
            self.statusWrapperObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(False)
        
        self.requestHeight(False)
        
        
        
        if not self.statusWrapperObj:
            self.statusWrapperObj = self.newStatusWrapper()
            self.statusWrapperObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestName(False)
        
        self.requestHeight(False)
        
        
        
        if not self.statusWrapperObj:
            self.statusWrapperObj = self.newStatusWrapper()
            self.statusWrapperObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setName(None)
        self.nameSet = False
        
        self.setHeight(None)
        self.heightSet = False
        
        
        if self.statusWrapperObj:
            self.statusWrapperObj.clearAllSet()
        

    def write (self
              , alien
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(alien, trxContext)

    def read (self
              , alien
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(alien, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , alien
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(alien, 
                                  True,
                                  trxContext)

    def newStatusWrapper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-statuswrapper').debug3Func(): logFunc('called.')
        statusWrapper = BlinkyStatusWrapperMaapi(self._log)
        statusWrapper.init(self.domain)
        return statusWrapper

    def setStatusWrapperObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-statuswrapper').debug3Func(): logFunc('called. obj=%s', obj)
        self.statusWrapperObj = obj

    def getStatusWrapperObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-statuswrapper').debug3Func(): logFunc('called. self.statusWrapperObj=%s', self.statusWrapperObj)
        return self.statusWrapperObj

    def hasStatusWrapper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-statuswrapper').debug3Func(): logFunc('called. self.statusWrapperObj=%s', self.statusWrapperObj)
        if self.statusWrapperObj:
            return True
        return False



    def requestName (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-name').debug3Func(): logFunc('called. requested=%s', requested)
        self.nameRequested = requested
        self.nameSet = False

    def isNameRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-name-requested').debug3Func(): logFunc('called. requested=%s', self.nameRequested)
        return self.nameRequested

    def getName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return self.name
        return None

    def hasName (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-name').debug3Func(): logFunc('called. self.nameSet=%s, self.name=%s', self.nameSet, self.name)
        if self.nameSet:
            return True
        return False

    def setName (self, name):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-name').debug3Func(): logFunc('called. name=%s, old=%s', name, self.name)
        self.nameSet = True
        self.name = name

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

        
        if self.statusWrapperObj:
            self.statusWrapperObj._clearAllReadData()
        

        
        self.name = 0
        self.nameSet = False
        
        self.height = 0
        self.heightSet = False
        

    def _getSelfKeyPath (self, alien
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(alien);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("alien", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", "oe"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("root", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", "oe"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        alien, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(alien, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(alien, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       alien, 
                       
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

        keyPath = self._getSelfKeyPath(alien, 
                                       
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
                               alien, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.statusWrapperObj:
            res = self.statusWrapperObj._collectItemsToDelete(alien, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-wrapper-failed').errorFunc(): logFunc('statusWrapperObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"), valName)
        
        if self.hasHeight():
            valHeight = Value()
            if self.height is not None:
                valHeight.setInt64(self.height)
            else:
                valHeight.setEmpty()
            tagValueList.push(("height", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"), valHeight)
        

        
        if self.statusWrapperObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status-wrapper" , "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", "oe")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusWrapperObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-status-wrapper-failed').errorFunc(): logFunc('statusWrapperObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"), valName)
        
        if self.isHeightRequested():
            valHeight = Value()
            valHeight.setEmpty()
            tagValueList.push(("height", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"), valHeight)
        

        
        if self.statusWrapperObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status-wrapper" , "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", "oe")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusWrapperObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-status-wrapper-failed').errorFunc(): logFunc('statusWrapperObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-name-bad-value').infoFunc(): logFunc('name not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setName(tempVar)
            for logFunc in self._log('read-tag-values-name').debug3Func(): logFunc('read name. name=%s, tempValue=%s', self.name, tempValue.getType())
        
        if self.isHeightRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "height") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-height').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "height", "height", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", tag, ns)
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
        

        
        if self.statusWrapperObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status-wrapper") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status-wrapper", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.statusWrapperObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-status-wrapper-failed').errorFunc(): logFunc('statusWrapperObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "status-wrapper") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status-wrapper", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "alien", 
        "namespace": "alien", 
        "className": "AlienMaapi", 
        "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.alien_maapi_gen import AlienMaapi", 
        "baseClassName": "AlienMaapiBase", 
        "baseModule": "alien_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oe", 
            "yangName": "root", 
            "namespace": "root", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "name": "root"
        }, 
        {
            "moduleYangNamespacePrefix": "oe", 
            "isCurrent": true, 
            "yangName": "alien", 
            "namespace": "alien", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "keyLeaf": {
                "varName": "alien", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "alien"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oe", 
            "memberName": "statusWrapper", 
            "yangName": "status-wrapper", 
            "className": "BlinkyStatusWrapperMaapi", 
            "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.status_wrapper.status_wrapper_maapi_gen import BlinkyStatusWrapperMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "150", 
            "hasDefaultRef": false
        }
    ], 
    "env": {
        "namespaces": [
            "a", 
            "sys", 
            "blinky", 
            "example", 
            "python", 
            "oper", 
            "ut", 
            "oper_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/oper-example", 
            "moduleYangNamespacePrefix": "oe", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "height", 
            "yangName": "height", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "150", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


