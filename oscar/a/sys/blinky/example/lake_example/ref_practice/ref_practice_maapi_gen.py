


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

from ref_practice_maapi_base_gen import RefPracticeMaapiBase

from a.sys.blinky.example.lake_example.ref_practice.some_list.some_list_maapi_list_gen import BlinkySomeListMaapiList



class BlinkyRefPracticeMaapi(RefPracticeMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-refPractice")
        self.domain = None

        
        self.someListListObj = None
        

        
        self.someLeafRefRequested = False
        self.someLeafRef = None
        self.someLeafRefSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSomeLeafRef(True)
        
        
        
        if not self.someListListObj:
            self.someListListObj = self.newSomeListList()
            self.someListListObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSomeLeafRef(True)
        
        
        
        if not self.someListListObj:
            self.someListListObj = self.newSomeListList()
            self.someListListObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSomeLeafRef(False)
        
        
        
        if not self.someListListObj:
            self.someListListObj = self.newSomeListList()
            self.someListListObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestSomeLeafRef(False)
        
        
        
        if not self.someListListObj:
            self.someListListObj = self.newSomeListList()
            self.someListListObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setSomeLeafRef(None)
        self.someLeafRefSet = False
        
        
        if self.someListListObj:
            self.someListListObj.clearAllSet()
        

    def write (self
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(trxContext)

    def read (self
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  True,
                                  trxContext)

    def newSomeListList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-somelistlist').debug3Func(): logFunc('called.')
        someListList = BlinkySomeListMaapiList(self._log)
        someListList.init(self.domain)
        return someListList

    def setSomeListListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-somelistlist').debug3Func(): logFunc('called. obj=%s', obj)
        self.someListListObj = obj

    def getSomeListListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-somelistlist').debug3Func(): logFunc('called. self.someListListObj=%s', self.someListListObj)
        return self.someListListObj

    def hasSomeListList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-somelistlist').debug3Func(): logFunc('called. self.someListListObj=%s', self.someListListObj)
        if self.someListListObj:
            return True
        return False



    def requestSomeLeafRef (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-someleafref').debug3Func(): logFunc('called. requested=%s', requested)
        self.someLeafRefRequested = requested
        self.someLeafRefSet = False

    def isSomeLeafRefRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-someleafref-requested').debug3Func(): logFunc('called. requested=%s', self.someLeafRefRequested)
        return self.someLeafRefRequested

    def getSomeLeafRef (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-someleafref').debug3Func(): logFunc('called. self.someLeafRefSet=%s, self.someLeafRef=%s', self.someLeafRefSet, self.someLeafRef)
        if self.someLeafRefSet:
            return self.someLeafRef
        return None

    def hasSomeLeafRef (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-someleafref').debug3Func(): logFunc('called. self.someLeafRefSet=%s, self.someLeafRef=%s', self.someLeafRefSet, self.someLeafRef)
        if self.someLeafRefSet:
            return True
        return False

    def setSomeLeafRef (self, someLeafRef):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-someleafref').debug3Func(): logFunc('called. someLeafRef=%s, old=%s', someLeafRef, self.someLeafRef)
        self.someLeafRefSet = True
        self.someLeafRef = someLeafRef


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.someListListObj:
            self.someListListObj._clearAllReadData()
        

        
        self.someLeafRef = 0
        self.someLeafRefSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ref-practice", "http://qwilt.com/model/lake-example", "lake-example"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       
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

        keyPath = self._getSelfKeyPath(
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
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.someListListObj:
            res = self.someListListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-some-list-failed').errorFunc(): logFunc('someListListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasSomeLeafRef():
            valSomeLeafRef = Value()
            if self.someLeafRef is not None:
                valSomeLeafRef.setString(self.someLeafRef)
            else:
                valSomeLeafRef.setEmpty()
            tagValueList.push(("some-leaf-ref", "http://qwilt.com/model/lake-example"), valSomeLeafRef)
        

        
        if self.someListListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("some-list" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.someListListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-some-list-failed').errorFunc(): logFunc('someListListObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isSomeLeafRefRequested():
            valSomeLeafRef = Value()
            valSomeLeafRef.setEmpty()
            tagValueList.push(("some-leaf-ref", "http://qwilt.com/model/lake-example"), valSomeLeafRef)
        

        
        if self.someListListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("some-list" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.someListListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-some-list-failed').errorFunc(): logFunc('someListListObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isSomeLeafRefRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "some-leaf-ref") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-someleafref').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "someLeafRef", "some-leaf-ref", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-some-leaf-ref-bad-value').infoFunc(): logFunc('someLeafRef not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setSomeLeafRef(tempVar)
            for logFunc in self._log('read-tag-values-some-leaf-ref').debug3Func(): logFunc('read someLeafRef. someLeafRef=%s, tempValue=%s', self.someLeafRef, tempValue.getType())
        

        
        if self.someListListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "some-list") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "some-list", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.someListListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-some-list-failed').errorFunc(): logFunc('someListListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "some-list") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "some-list", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "refPractice", 
        "namespace": "ref_practice", 
        "className": "RefPracticeMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.ref_practice.ref_practice_maapi_gen import RefPracticeMaapi", 
        "baseClassName": "RefPracticeMaapiBase", 
        "baseModule": "ref_practice_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "yangName": "ref-practice", 
            "namespace": "ref_practice", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "name": "ref-practice"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "someListList", 
            "yangName": "some-list", 
            "className": "BlinkySomeListMaapiList", 
            "importStatement": "from a.sys.blinky.example.lake_example.ref_practice.some_list.some_list_maapi_list_gen import BlinkySomeListMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "someLeafRef", 
            "yangName": "some-leaf-ref", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "someLeafRef", 
            "yangName": "some-leaf-ref", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


