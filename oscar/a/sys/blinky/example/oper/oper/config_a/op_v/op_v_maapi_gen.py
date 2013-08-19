


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

from op_v_maapi_base_gen import OpVMaapiBase

from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.op_y_maapi_gen import BlinkyOpYMaapi
from a.sys.blinky.example.oper.oper.config_a.op_v.op_w.op_w_maapi_gen import BlinkyOpWMaapi



class BlinkyOpVMaapi(OpVMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-opV")
        self.domain = None

        
        self.opYObj = None
        
        self.opWObj = None
        

        
        self.valueOpV1Requested = False
        self.valueOpV1 = None
        self.valueOpV1Set = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestValueOpV1(True)
        
        
        if not self.opYObj:
            self.opYObj = self.newOpY()
            self.opYObj.requestConfigAndOper()
        
        if not self.opWObj:
            self.opWObj = self.newOpW()
            self.opWObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestValueOpV1(False)
        
        
        if not self.opYObj:
            self.opYObj = self.newOpY()
            self.opYObj.requestConfig()
        
        if not self.opWObj:
            self.opWObj = self.newOpW()
            self.opWObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestValueOpV1(True)
        
        
        if not self.opYObj:
            self.opYObj = self.newOpY()
            self.opYObj.requestOper()
        
        if not self.opWObj:
            self.opWObj = self.newOpW()
            self.opWObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestValueOpV1(False)
        
        
        if not self.opYObj:
            self.opYObj = self.newOpY()
            self.opYObj.clearAllRequested()
        
        if not self.opWObj:
            self.opWObj = self.newOpW()
            self.opWObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        
        if self.opYObj:
            self.opYObj.clearAllSet()
        
        if self.opWObj:
            self.opWObj.clearAllSet()
        

    def write (self
              , opV
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(opV, trxContext)

    def read (self
              , opV
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(opV, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , opV
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(opV, 
                                  True,
                                  trxContext)

    def newOpY (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-opy').debug3Func(): logFunc('called.')
        opY = BlinkyOpYMaapi(self._log)
        opY.init(self.domain)
        return opY

    def setOpYObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opy').debug3Func(): logFunc('called. obj=%s', obj)
        self.opYObj = obj

    def getOpYObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opy').debug3Func(): logFunc('called. self.opYObj=%s', self.opYObj)
        return self.opYObj

    def hasOpY (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opy').debug3Func(): logFunc('called. self.opYObj=%s', self.opYObj)
        if self.opYObj:
            return True
        return False

    def newOpW (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-opw').debug3Func(): logFunc('called.')
        opW = BlinkyOpWMaapi(self._log)
        opW.init(self.domain)
        return opW

    def setOpWObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-opw').debug3Func(): logFunc('called. obj=%s', obj)
        self.opWObj = obj

    def getOpWObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-opw').debug3Func(): logFunc('called. self.opWObj=%s', self.opWObj)
        return self.opWObj

    def hasOpW (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-opw').debug3Func(): logFunc('called. self.opWObj=%s', self.opWObj)
        if self.opWObj:
            return True
        return False



    def requestValueOpV1 (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-valueopv1').debug3Func(): logFunc('called. requested=%s', requested)
        self.valueOpV1Requested = requested
        self.valueOpV1Set = False

    def isValueOpV1Requested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-valueopv1-requested').debug3Func(): logFunc('called. requested=%s', self.valueOpV1Requested)
        return self.valueOpV1Requested

    def getValueOpV1 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-valueopv1').debug3Func(): logFunc('called. self.valueOpV1Set=%s, self.valueOpV1=%s', self.valueOpV1Set, self.valueOpV1)
        if self.valueOpV1Set:
            return self.valueOpV1
        return None

    def hasValueOpV1 (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-valueopv1').debug3Func(): logFunc('called. self.valueOpV1Set=%s, self.valueOpV1=%s', self.valueOpV1Set, self.valueOpV1)
        if self.valueOpV1Set:
            return True
        return False

    def setValueOpV1 (self, valueOpV1):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-valueopv1').debug3Func(): logFunc('called. valueOpV1=%s, old=%s', valueOpV1, self.valueOpV1)
        self.valueOpV1Set = True
        self.valueOpV1 = valueOpV1


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.opYObj:
            self.opYObj._clearAllReadData()
        
        if self.opWObj:
            self.opWObj._clearAllReadData()
        

        
        self.valueOpV1 = 0
        self.valueOpV1Set = False
        

    def _getSelfKeyPath (self, opV
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(opV);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("op-v", "http://qwilt.com/model/oper", "oper"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("config-a", "http://qwilt.com/model/oper", "oper"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        opV, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(opV, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(opV, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       opV, 
                       
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

        keyPath = self._getSelfKeyPath(opV, 
                                       
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
                               opV, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.opYObj:
            res = self.opYObj._collectItemsToDelete(opV, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-op-y-failed').errorFunc(): logFunc('opYObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.opWObj:
            res = self.opWObj._collectItemsToDelete(opV, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-op-w-failed').errorFunc(): logFunc('opWObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        
        if self.opYObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-y" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opYObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-op-y-failed').errorFunc(): logFunc('opYObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opWObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-w" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opWObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-op-w-failed').errorFunc(): logFunc('opWObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isValueOpV1Requested():
            valValueOpV1 = Value()
            valValueOpV1.setEmpty()
            tagValueList.push(("value-op-v1", "http://qwilt.com/model/oper"), valValueOpV1)
        

        
        if self.opYObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-y" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opYObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-op-y-failed').errorFunc(): logFunc('opYObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.opWObj:
            valBegin = Value()
            (tag, ns, prefix) = ("op-w" , "http://qwilt.com/model/oper", "oper")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.opWObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-op-w-failed').errorFunc(): logFunc('opWObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isValueOpV1Requested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "value-op-v1") or \
                (ns != "http://qwilt.com/model/oper"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-valueopv1').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "valueOpV1", "value-op-v1", "http://qwilt.com/model/oper", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-value-op-v1-bad-value').infoFunc(): logFunc('valueOpV1 not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setValueOpV1(tempVar)
            for logFunc in self._log('read-tag-values-value-op-v1').debug3Func(): logFunc('read valueOpV1. valueOpV1=%s, tempValue=%s', self.valueOpV1, tempValue.getType())
        

        
        if self.opYObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "op-y") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "op-y", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.opYObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-op-y-failed').errorFunc(): logFunc('opYObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "op-y") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "op-y", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.opWObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "op-w") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "op-w", "http://qwilt.com/model/oper", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.opWObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-op-w-failed').errorFunc(): logFunc('opWObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "op-w") or \
                (ns != "http://qwilt.com/model/oper") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "op-w", "http://qwilt.com/model/oper", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "opV", 
        "namespace": "op_v", 
        "className": "OpVMaapi", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_v_maapi_gen import OpVMaapi", 
        "baseClassName": "OpVMaapiBase", 
        "baseModule": "op_v_maapi_base_gen"
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
            "isCurrent": true, 
            "yangName": "op-v", 
            "namespace": "op_v", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/oper", 
            "keyLeaf": {
                "varName": "opV", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "op-v"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opY", 
            "yangName": "op-y", 
            "className": "BlinkyOpYMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.op_y_maapi_gen import BlinkyOpYMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/oper"
        }, 
        {
            "moduleYangNamespacePrefix": "oper", 
            "memberName": "opW", 
            "yangName": "op-w", 
            "className": "BlinkyOpWMaapi", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_w.op_w_maapi_gen import BlinkyOpWMaapi", 
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
            "memberName": "valueOpV1", 
            "yangName": "value-op-v1", 
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
            "memberName": "valueOpV1", 
            "yangName": "value-op-v1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


