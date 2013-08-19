


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

from chair_maapi_base_gen import ChairMaapiBase

from a.sys.blinky.example.python.simple.container.ut.simple_example.chair.status.status_maapi_gen import BlinkyStatusMaapi



class BlinkyChairMaapi(ChairMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-chair")
        self.domain = None

        
        self.statusObj = None
        

        
        self.colorRequested = False
        self.color = None
        self.colorSet = False
        
        self.prettyRequested = False
        self.pretty = None
        self.prettySet = False
        
        self.numOfLegsRequested = False
        self.numOfLegs = None
        self.numOfLegsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestColor(True)
        
        self.requestPretty(True)
        
        self.requestNumOfLegs(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestColor(True)
        
        self.requestPretty(True)
        
        self.requestNumOfLegs(True)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestColor(False)
        
        self.requestPretty(False)
        
        self.requestNumOfLegs(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestColor(False)
        
        self.requestPretty(False)
        
        self.requestNumOfLegs(False)
        
        
        
        if not self.statusObj:
            self.statusObj = self.newStatus()
            self.statusObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setColor(None)
        self.colorSet = False
        
        self.setPretty(None)
        self.prettySet = False
        
        self.setNumOfLegs(None)
        self.numOfLegsSet = False
        
        
        if self.statusObj:
            self.statusObj.clearAllSet()
        

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

    def newStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-status').debug3Func(): logFunc('called.')
        status = BlinkyStatusMaapi(self._log)
        status.init(self.domain)
        return status

    def setStatusObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-status').debug3Func(): logFunc('called. obj=%s', obj)
        self.statusObj = obj

    def getStatusObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        return self.statusObj

    def hasStatus (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-status').debug3Func(): logFunc('called. self.statusObj=%s', self.statusObj)
        if self.statusObj:
            return True
        return False



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

    def requestPretty (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pretty').debug3Func(): logFunc('called. requested=%s', requested)
        self.prettyRequested = requested
        self.prettySet = False

    def isPrettyRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pretty-requested').debug3Func(): logFunc('called. requested=%s', self.prettyRequested)
        return self.prettyRequested

    def getPretty (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pretty').debug3Func(): logFunc('called. self.prettySet=%s, self.pretty=%s', self.prettySet, self.pretty)
        if self.prettySet:
            return self.pretty
        return None

    def hasPretty (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pretty').debug3Func(): logFunc('called. self.prettySet=%s, self.pretty=%s', self.prettySet, self.pretty)
        if self.prettySet:
            return True
        return False

    def setPretty (self, pretty):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pretty').debug3Func(): logFunc('called. pretty=%s, old=%s', pretty, self.pretty)
        self.prettySet = True
        self.pretty = pretty

    def requestNumOfLegs (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-numoflegs').debug3Func(): logFunc('called. requested=%s', requested)
        self.numOfLegsRequested = requested
        self.numOfLegsSet = False

    def isNumOfLegsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-numoflegs-requested').debug3Func(): logFunc('called. requested=%s', self.numOfLegsRequested)
        return self.numOfLegsRequested

    def getNumOfLegs (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-numoflegs').debug3Func(): logFunc('called. self.numOfLegsSet=%s, self.numOfLegs=%s', self.numOfLegsSet, self.numOfLegs)
        if self.numOfLegsSet:
            return self.numOfLegs
        return None

    def hasNumOfLegs (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-numoflegs').debug3Func(): logFunc('called. self.numOfLegsSet=%s, self.numOfLegs=%s', self.numOfLegsSet, self.numOfLegs)
        if self.numOfLegsSet:
            return True
        return False

    def setNumOfLegs (self, numOfLegs):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-numoflegs').debug3Func(): logFunc('called. numOfLegs=%s, old=%s', numOfLegs, self.numOfLegs)
        self.numOfLegsSet = True
        self.numOfLegs = numOfLegs


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.statusObj:
            self.statusObj._clearAllReadData()
        

        
        self.color = 0
        self.colorSet = False
        
        self.pretty = 0
        self.prettySet = False
        
        self.numOfLegs = 0
        self.numOfLegsSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("chair", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", "se"))
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

        
        if self.statusObj:
            res = self.statusObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-status-failed').errorFunc(): logFunc('statusObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasColor():
            valColor = Value()
            if self.color is not None:
                valColor.setString(self.color)
            else:
                valColor.setEmpty()
            tagValueList.push(("color", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"), valColor)
        
        if self.hasPretty():
            valPretty = Value()
            if self.pretty is not None:
                valPretty.setBool(self.pretty)
            else:
                valPretty.setEmpty()
            tagValueList.push(("pretty", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"), valPretty)
        
        if self.hasNumOfLegs():
            valNumOfLegs = Value()
            if self.numOfLegs is not None:
                valNumOfLegs.setInt64(self.numOfLegs)
            else:
                valNumOfLegs.setEmpty()
            tagValueList.push(("num-of-legs", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"), valNumOfLegs)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", "se")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isColorRequested():
            valColor = Value()
            valColor.setEmpty()
            tagValueList.push(("color", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"), valColor)
        
        if self.isPrettyRequested():
            valPretty = Value()
            valPretty.setEmpty()
            tagValueList.push(("pretty", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"), valPretty)
        
        if self.isNumOfLegsRequested():
            valNumOfLegs = Value()
            valNumOfLegs.setEmpty()
            tagValueList.push(("num-of-legs", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"), valNumOfLegs)
        

        
        if self.statusObj:
            valBegin = Value()
            (tag, ns, prefix) = ("status" , "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", "se")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.statusObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-status-failed').errorFunc(): logFunc('statusObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isColorRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "color") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-color').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "color", "color", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-color-bad-value').infoFunc(): logFunc('color not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setColor(tempVar)
            for logFunc in self._log('read-tag-values-color').debug3Func(): logFunc('read color. color=%s, tempValue=%s', self.color, tempValue.getType())
        
        if self.isPrettyRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "pretty") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pretty').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pretty", "pretty", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-pretty-bad-value').infoFunc(): logFunc('pretty not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPretty(tempVar)
            for logFunc in self._log('read-tag-values-pretty').debug3Func(): logFunc('read pretty. pretty=%s, tempValue=%s', self.pretty, tempValue.getType())
        
        if self.isNumOfLegsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "num-of-legs") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-numoflegs').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "numOfLegs", "num-of-legs", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-num-of-legs-bad-value').infoFunc(): logFunc('numOfLegs not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNumOfLegs(tempVar)
            for logFunc in self._log('read-tag-values-num-of-legs').debug3Func(): logFunc('read numOfLegs. numOfLegs=%s, tempValue=%s', self.numOfLegs, tempValue.getType())
        

        
        if self.statusObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "status", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.statusObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-status-failed').errorFunc(): logFunc('statusObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "status") or \
                (ns != "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "status", "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "chair", 
        "namespace": "chair", 
        "className": "ChairMaapi", 
        "importStatement": "from a.sys.blinky.example.python.simple.container.ut.simple_example.chair.chair_maapi_gen import ChairMaapi", 
        "baseClassName": "ChairMaapiBase", 
        "baseModule": "chair_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "se", 
            "yangName": "chair", 
            "namespace": "chair", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "name": "chair"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "se", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.sys.blinky.example.python.simple.container.ut.simple_example.chair.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "yellow", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "pretty", 
            "yangName": "pretty", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "numOfLegs", 
            "yangName": "num-of-legs", 
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
            "python", 
            "simple", 
            "container", 
            "ut", 
            "simple_example"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "yellow", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "pretty", 
            "yangName": "pretty", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/ut/sys/blinky/example/python/simple-example", 
            "moduleYangNamespacePrefix": "se", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "numOfLegs", 
            "yangName": "num-of-legs", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


