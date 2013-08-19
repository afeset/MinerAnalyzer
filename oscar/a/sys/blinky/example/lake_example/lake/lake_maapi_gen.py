


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

from lake_maapi_base_gen import LakeMaapiBase

from a.sys.blinky.example.lake_example.lake.fish_.fish__maapi_list_gen import BlinkyFishMaapiList
from a.sys.blinky.example.lake_example.lake.size.size_maapi_gen import BlinkySizeMaapi

import struct


class BlinkyLakeMaapi(LakeMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-lake")
        self.domain = None

        
        self.fish_ListObj = None
        
        self.sizeObj = None
        

        
        self.ipRequested = False
        self.ip = None
        self.ipSet = False
        
        self.nameRequested = False
        self.name = None
        self.nameSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestIp(True)
        
        self.requestName(True)
        
        
        
        if not self.fish_ListObj:
            self.fish_ListObj = self.newFish_List()
            self.fish_ListObj.requestConfigAndOper()
        
        if not self.sizeObj:
            self.sizeObj = self.newSize()
            self.sizeObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestIp(True)
        
        self.requestName(True)
        
        
        
        if not self.fish_ListObj:
            self.fish_ListObj = self.newFish_List()
            self.fish_ListObj.requestConfig()
        
        if not self.sizeObj:
            self.sizeObj = self.newSize()
            self.sizeObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestIp(False)
        
        self.requestName(False)
        
        
        
        if not self.fish_ListObj:
            self.fish_ListObj = self.newFish_List()
            self.fish_ListObj.requestOper()
        
        if not self.sizeObj:
            self.sizeObj = self.newSize()
            self.sizeObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestIp(False)
        
        self.requestName(False)
        
        
        
        if not self.fish_ListObj:
            self.fish_ListObj = self.newFish_List()
            self.fish_ListObj.clearAllRequested()
        
        if not self.sizeObj:
            self.sizeObj = self.newSize()
            self.sizeObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setIp(None)
        self.ipSet = False
        
        self.setName(None)
        self.nameSet = False
        
        
        if self.fish_ListObj:
            self.fish_ListObj.clearAllSet()
        
        if self.sizeObj:
            self.sizeObj.clearAllSet()
        

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

    def newFish_List (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-fish_list').debug3Func(): logFunc('called.')
        fish_List = BlinkyFishMaapiList(self._log)
        fish_List.init(self.domain)
        return fish_List

    def setFish_ListObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-fish_list').debug3Func(): logFunc('called. obj=%s', obj)
        self.fish_ListObj = obj

    def getFish_ListObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-fish_list').debug3Func(): logFunc('called. self.fish_ListObj=%s', self.fish_ListObj)
        return self.fish_ListObj

    def hasFish_List (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-fish_list').debug3Func(): logFunc('called. self.fish_ListObj=%s', self.fish_ListObj)
        if self.fish_ListObj:
            return True
        return False

    def newSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-size').debug3Func(): logFunc('called.')
        size = BlinkySizeMaapi(self._log)
        size.init(self.domain)
        return size

    def setSizeObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-size').debug3Func(): logFunc('called. obj=%s', obj)
        self.sizeObj = obj

    def getSizeObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-size').debug3Func(): logFunc('called. self.sizeObj=%s', self.sizeObj)
        return self.sizeObj

    def hasSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-size').debug3Func(): logFunc('called. self.sizeObj=%s', self.sizeObj)
        if self.sizeObj:
            return True
        return False



    def requestIp (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-ip').debug3Func(): logFunc('called. requested=%s', requested)
        self.ipRequested = requested
        self.ipSet = False

    def isIpRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-ip-requested').debug3Func(): logFunc('called. requested=%s', self.ipRequested)
        return self.ipRequested

    def getIp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ip').debug3Func(): logFunc('called. self.ipSet=%s, self.ip=%s', self.ipSet, self.ip)
        if self.ipSet:
            return self.ip
        return None

    def hasIp (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ip').debug3Func(): logFunc('called. self.ipSet=%s, self.ip=%s', self.ipSet, self.ip)
        if self.ipSet:
            return True
        return False

    def setIp (self, ip):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ip').debug3Func(): logFunc('called. ip=%s, old=%s', ip, self.ip)
        self.ipSet = True
        self.ip = ip

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.fish_ListObj:
            self.fish_ListObj._clearAllReadData()
        
        if self.sizeObj:
            self.sizeObj._clearAllReadData()
        

        
        self.ip = 0
        self.ipSet = False
        
        self.name = 0
        self.nameSet = False
        

    def _getSelfKeyPath (self, lake
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
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

        
        if self.fish_ListObj:
            res = self.fish_ListObj._collectItemsToDelete(lake, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-fish-failed').errorFunc(): logFunc('fish_ListObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.sizeObj:
            res = self.sizeObj._collectItemsToDelete(lake, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-size-failed').errorFunc(): logFunc('sizeObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasIp():
            valIp = Value()
            if self.ip is not None:
                valIp.setIPv4(self.ip)
            else:
                valIp.setEmpty()
            tagValueList.push(("ip", "http://qwilt.com/model/lake-example"), valIp)
        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/model/lake-example"), valName)
        

        
        if self.fish_ListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("fish" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.fish_ListObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-fish-failed').errorFunc(): logFunc('fish_ListObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.sizeObj:
            valBegin = Value()
            (tag, ns, prefix) = ("size" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.sizeObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-size-failed').errorFunc(): logFunc('sizeObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isIpRequested():
            valIp = Value()
            valIp.setEmpty()
            tagValueList.push(("ip", "http://qwilt.com/model/lake-example"), valIp)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/model/lake-example"), valName)
        

        
        if self.fish_ListObj:
            valBegin = Value()
            (tag, ns, prefix) = ("fish" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.fish_ListObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-fish-failed').errorFunc(): logFunc('fish_ListObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.sizeObj:
            valBegin = Value()
            (tag, ns, prefix) = ("size" , "http://qwilt.com/model/lake-example", "lake-example")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.sizeObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-size-failed').errorFunc(): logFunc('sizeObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isIpRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ip") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-ip').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "ip", "ip", "http://qwilt.com/model/lake-example", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = (tempValue.asIPv4())
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ip-bad-value').infoFunc(): logFunc('ip not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setIp(tempVar)
            for logFunc in self._log('read-tag-values-ip').debug3Func(): logFunc('read ip. ip=%s, tempValue=%s', self.ip, tempValue.getType())
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/model/lake-example"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/model/lake-example", tag, ns)
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
        

        
        if self.fish_ListObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "fish") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "fish", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.fish_ListObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-fish-failed').errorFunc(): logFunc('fish_ListObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "fish") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "fish", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.sizeObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "size") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "size", "http://qwilt.com/model/lake-example", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.sizeObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-size-failed').errorFunc(): logFunc('sizeObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "size") or \
                (ns != "http://qwilt.com/model/lake-example") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "size", "http://qwilt.com/model/lake-example", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "lake", 
        "namespace": "lake", 
        "className": "LakeMaapi", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.lake_maapi_gen import LakeMaapi", 
        "baseClassName": "LakeMaapiBase", 
        "baseModule": "lake_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "fish_List", 
            "yangName": "fish", 
            "className": "BlinkyFishMaapiList", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.fish__maapi_list_gen import BlinkyFishMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/lake-example"
        }, 
        {
            "moduleYangNamespacePrefix": "lake-example", 
            "memberName": "size", 
            "yangName": "size", 
            "className": "BlinkySizeMaapi", 
            "importStatement": "from a.sys.blinky.example.lake_example.lake.size.size_maapi_gen import BlinkySizeMaapi", 
            "isList": false, 
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
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
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
            "typeHandler": "handler: Ipv4AddressHandlerPy", 
            "memberName": "ip", 
            "yangName": "ip", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/lake-example", 
            "moduleYangNamespacePrefix": "lake-example", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


