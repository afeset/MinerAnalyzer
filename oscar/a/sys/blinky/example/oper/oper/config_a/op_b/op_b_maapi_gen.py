


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

from op_b_maapi_base_gen import OpBMaapiBase

from a.sys.blinky.example.oper.oper.config_a.op_b.op_c.op_c_maapi_list_gen import BlinkyOpCMaapiList
from a.sys.blinky.example.oper.oper.config_a.op_b.op_d.op_d_maapi_gen import BlinkyOpDMaapi



class BlinkyOpBMaapi(OpBMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-opB")
        self.domain = None

        
        self.opCListObj = None
        
        self.opDObj = None
        

        
        self.opValueBRequested = False
        self.opValueB = None
        self.opValueBSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOpValueB(True)
        
        
        if not self.opCListObj:
            self.opCListObj = self.newOpCList()
            self.opCListObj.requestConfigAndOper()
        
        if not self.opDObj:
            self.opDObj = self.newOpD()
            self.opDObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOpValueB(False)
        
        
        if not self.opCListObj:
            self.opCListObj = self.newOpCList()
            self.opCListObj.requestConfig()
        
        if not self.opDObj:
            self.opDObj = self.newOpD()
            self.opDObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOpValueB(True)
        
        
        if not self.opCListObj:
            self.opCListObj = self.newOpCList()
            self.opCListObj.requestOper()
        
        if not self.opDObj:
            self.opDObj = self.newOpD()
            self.opDObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOpValueB(False)
        
        
        if not self.opCListObj:
            self.opCListObj = self.newOpCList()
            self.opCListObj.clearAllRequested()
        
        if not self.opDObj:
            self.opDObj = self.newOpD()
            self.opDObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        
        if self.opCListObj:
            self.opCListObj.clearAllSet()
        
        if self.opDObj:
            self.opDObj.clearAllSet()
        

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

    def newOpCList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-opclist').debug3Func(): logFunc('called.')
        opCList = BlinkyOpCMaapiList(self._log)
        opCList.init(self.domain)
        return opCList

    def setOpCListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opclist').debug3Func(): logFunc('called. obj=%s', obj)
        self.opCListObj = obj

    def getOpCListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opclist').debug3Func(): logFunc('called. self.opCListObj=%s', self.opCListObj)
        return self.opCListObj

    def hasOpCList (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opclist').debug3Func(): logFunc('called. self.opCListObj=%s', self.opCListObj)
        if self.opCListObj:
            return True
        return False

    def newOpD (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-opd').debug3Func(): logFunc('called.')
        opD = BlinkyOpDMaapi(self._log)
        opD.init(self.domain)
        return opD

    def setOpDObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opd').debug3Func(): logFunc('called. obj=%s', obj)
        self.opDObj = obj

    def getOpDObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opd').debug3Func(): logFunc('called. self.opDObj=%s', self.opDObj)
        return self.opDObj

    def hasOpD (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opd').debug3Func(): logFunc('called. self.opDObj=%s', self.opDObj)
        if self.opDObj:
            return True
        return False



    def requestOpValueB (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-opvalueb').debug3Func(): logFunc('called. requested=%s', requested)
        self.opValueBRequested = requested
        self.opValueBSet = False

    def isOpValueBRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-opvalueb-requested').debug3Func(): logFunc('called. requested=%s', self.opValueBRequested)
        return self.opValueBRequested

    def getOpValueB (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opvalueb').debug3Func(): logFunc('called. self.opValueBSet=%s, self.opValueB=%s', self.opValueBSet, self.opValueB)
        if self.opValueBSet:
            return self.opValueB
        return None

    def hasOpValueB (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opvalueb').debug3Func(): logFunc('called. self.opValueBSet=%s, self.opValueB=%s', self.opValueBSet, self.opValueB)
        if self.opValueBSet:
            return True
        return False

    def setOpValueB (self, opValueB):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opvalueb').debug3Func(): logFunc('called. opValueB=%s, old=%s', opValueB, self.opValueB)
        self.opValueBSet = True
        self.opValueB = opValueB


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.opCListObj:
            self.opCListObj._clearAllReadData()
        
        if self.opDObj:
            self.opDObj._clearAllReadData()
        

        
        self.opValueB = 0
        self.opValueBSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("op-b", "http://qwilt.com/model/oper", "oper"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("config-a", "http://qwilt.com/model/oper", "oper"))
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

        
        if self.opCListObj:
            res = self.opCListObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-op-c-failed').errorFunc(): logFunc('opCListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.opDObj:
            res = self.opDObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-op-d-failed').errorFunc(): logFunc('opDObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        
        if self.opCListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-c" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opCListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-op-c-failed').errorFunc(): logFunc('opCListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opDObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-d" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opDObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-op-d-failed').errorFunc(): logFunc('opDObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isOpValueBRequested():
            valOpValueB = Value()
            valOpValueB.setEmpty()
            tagValueList.push(("op-value-b", "http://qwilt.com/model/oper"), valOpValueB)
        

        
        if self.opCListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-c" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opCListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-op-c-failed').errorFunc(): logFunc('opCListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opDObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-d" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opDObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-op-d-failed').errorFunc(): logFunc('opDObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isOpValueBRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "op-value-b") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-opvalueb').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "opValueB", "op-value-b", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-op-value-b-bad-value').infoFunc(): logFunc('opValueB not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOpValueB(tempVar)
            for logFunc in self._log('read-tag-values-op-value-b').debug3Func(): logFunc('read opValueB. opValueB=%s, tempValue=%s', self.opValueB, tempValue.getType())
        

        
        if self.opCListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "op-c") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "op-c", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.opCListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-op-c-failed').errorFunc(): logFunc('opCListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "op-c") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "op-c", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.opDObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "op-d") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "op-d", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.opDObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-op-d-failed').errorFunc(): logFunc('opDObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "op-d") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "op-d", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "opB", 
        "namespace": "op_b", 
        "className": "OpBMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_b_maapi_gen import OpBMaapi", 
        "baseClassName": "OpBMaapiBase", 
        "baseModule": "op_b_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "config-a", 
            "namespace": "config_a", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "config-a"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "yangName": "op-b", 
            "namespace": "op_b", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "name": "op-b"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opCList", 
            "yangName": "op-c", 
            "className": "BlinkyOpCMaapiList", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_c.op_c_maapi_list_gen import BlinkyOpCMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opD", 
            "yangName": "op-d", 
            "className": "BlinkyOpDMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_d.op_d_maapi_gen import BlinkyOpDMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opValueB", 
            "yangName": "op-value-b", 
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
            "oper", 
            "oper"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "moduleYangNamespacePrefix": "oper", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "opValueB", 
            "yangName": "op-value-b", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


