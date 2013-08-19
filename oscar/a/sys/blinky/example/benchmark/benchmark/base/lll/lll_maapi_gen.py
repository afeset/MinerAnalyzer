


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

from lll_maapi_base_gen import LllMaapiBase

from a.sys.blinky.example.benchmark.benchmark.base.lll.aaa.aaa_maapi_gen import BlinkyAaaMaapi
from a.sys.blinky.example.benchmark.benchmark.base.lll.ccc.ccc_maapi_gen import BlinkyCccMaapi
from a.sys.blinky.example.benchmark.benchmark.base.lll.bbb.bbb_maapi_gen import BlinkyBbbMaapi

from a.sys.blinky.example.benchmark.benchmark.benchmark_module_gen import ColorT


class BlinkyLllMaapi(LllMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-lll")
        self.domain = None

        
        self.aaaObj = None
        
        self.cccObj = None
        
        self.bbbObj = None
        

        
        self.colorRequested = False
        self.color = None
        self.colorSet = False
        
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
        
        self.requestColor(True)
        
        self.requestName(True)
        
        
        
        if not self.aaaObj:
            self.aaaObj = self.newAaa()
            self.aaaObj.requestConfigAndOper()
        
        if not self.cccObj:
            self.cccObj = self.newCcc()
            self.cccObj.requestConfigAndOper()
        
        if not self.bbbObj:
            self.bbbObj = self.newBbb()
            self.bbbObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestColor(True)
        
        self.requestName(True)
        
        
        
        if not self.aaaObj:
            self.aaaObj = self.newAaa()
            self.aaaObj.requestConfig()
        
        if not self.cccObj:
            self.cccObj = self.newCcc()
            self.cccObj.requestConfig()
        
        if not self.bbbObj:
            self.bbbObj = self.newBbb()
            self.bbbObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestColor(False)
        
        self.requestName(False)
        
        
        
        if not self.aaaObj:
            self.aaaObj = self.newAaa()
            self.aaaObj.requestOper()
        
        if not self.cccObj:
            self.cccObj = self.newCcc()
            self.cccObj.requestOper()
        
        if not self.bbbObj:
            self.bbbObj = self.newBbb()
            self.bbbObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestColor(False)
        
        self.requestName(False)
        
        
        
        if not self.aaaObj:
            self.aaaObj = self.newAaa()
            self.aaaObj.clearAllRequested()
        
        if not self.cccObj:
            self.cccObj = self.newCcc()
            self.cccObj.clearAllRequested()
        
        if not self.bbbObj:
            self.bbbObj = self.newBbb()
            self.bbbObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setColor(None)
        self.colorSet = False
        
        self.setName(None)
        self.nameSet = False
        
        
        if self.aaaObj:
            self.aaaObj.clearAllSet()
        
        if self.cccObj:
            self.cccObj.clearAllSet()
        
        if self.bbbObj:
            self.bbbObj.clearAllSet()
        

    def write (self
              , lll
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(lll, trxContext)

    def read (self
              , lll
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lll, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , lll
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(lll, 
                                  True,
                                  trxContext)

    def newAaa (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-aaa').debug3Func(): logFunc('called.')
        aaa = BlinkyAaaMaapi(self._log)
        aaa.init(self.domain)
        return aaa

    def setAaaObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-aaa').debug3Func(): logFunc('called. obj=%s', obj)
        self.aaaObj = obj

    def getAaaObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-aaa').debug3Func(): logFunc('called. self.aaaObj=%s', self.aaaObj)
        return self.aaaObj

    def hasAaa (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-aaa').debug3Func(): logFunc('called. self.aaaObj=%s', self.aaaObj)
        if self.aaaObj:
            return True
        return False

    def newCcc (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-ccc').debug3Func(): logFunc('called.')
        ccc = BlinkyCccMaapi(self._log)
        ccc.init(self.domain)
        return ccc

    def setCccObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ccc').debug3Func(): logFunc('called. obj=%s', obj)
        self.cccObj = obj

    def getCccObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ccc').debug3Func(): logFunc('called. self.cccObj=%s', self.cccObj)
        return self.cccObj

    def hasCcc (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ccc').debug3Func(): logFunc('called. self.cccObj=%s', self.cccObj)
        if self.cccObj:
            return True
        return False

    def newBbb (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-bbb').debug3Func(): logFunc('called.')
        bbb = BlinkyBbbMaapi(self._log)
        bbb.init(self.domain)
        return bbb

    def setBbbObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-bbb').debug3Func(): logFunc('called. obj=%s', obj)
        self.bbbObj = obj

    def getBbbObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-bbb').debug3Func(): logFunc('called. self.bbbObj=%s', self.bbbObj)
        return self.bbbObj

    def hasBbb (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-bbb').debug3Func(): logFunc('called. self.bbbObj=%s', self.bbbObj)
        if self.bbbObj:
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

        
        if self.aaaObj:
            self.aaaObj._clearAllReadData()
        
        if self.cccObj:
            self.cccObj._clearAllReadData()
        
        if self.bbbObj:
            self.bbbObj._clearAllReadData()
        

        
        self.color = 0
        self.colorSet = False
        
        self.name = 0
        self.nameSet = False
        

    def _getSelfKeyPath (self, lll
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(lll);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("lll", "http://qwilt.com/model/benchmark", "bnch"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("base", "http://qwilt.com/model/benchmark", "bnch"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        lll, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(lll, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(lll, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       lll, 
                       
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

        keyPath = self._getSelfKeyPath(lll, 
                                       
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
                               lll, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.aaaObj:
            res = self.aaaObj._collectItemsToDelete(lll, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-aaa-failed').errorFunc(): logFunc('aaaObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.cccObj:
            res = self.cccObj._collectItemsToDelete(lll, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-ccc-failed').errorFunc(): logFunc('cccObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        
        if self.bbbObj:
            res = self.bbbObj._collectItemsToDelete(lll, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-bbb-failed').errorFunc(): logFunc('bbbObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasColor():
            valColor = Value()
            if self.color is not None:
                valColor.setEnum(self.color.getValue())
            else:
                valColor.setEmpty()
            tagValueList.push(("color", "http://qwilt.com/model/benchmark"), valColor)
        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/model/benchmark"), valName)
        

        
        if self.aaaObj:
            valBegin = Value()
            (tag, ns, prefix) = ("aaa" , "http://qwilt.com/model/benchmark", "bnch")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.aaaObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-aaa-failed').errorFunc(): logFunc('aaaObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.cccObj:
            valBegin = Value()
            (tag, ns, prefix) = ("ccc" , "http://qwilt.com/model/benchmark", "bnch")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.cccObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-ccc-failed').errorFunc(): logFunc('cccObj._fillWriteTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.bbbObj:
            valBegin = Value()
            (tag, ns, prefix) = ("bbb" , "http://qwilt.com/model/benchmark", "bnch")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.bbbObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-bbb-failed').errorFunc(): logFunc('bbbObj._fillWriteTagValues() failed. PARAMS')
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
            tagValueList.push(("color", "http://qwilt.com/model/benchmark"), valColor)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/model/benchmark"), valName)
        

        
        if self.aaaObj:
            valBegin = Value()
            (tag, ns, prefix) = ("aaa" , "http://qwilt.com/model/benchmark", "bnch")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.aaaObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-aaa-failed').errorFunc(): logFunc('aaaObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.cccObj:
            valBegin = Value()
            (tag, ns, prefix) = ("ccc" , "http://qwilt.com/model/benchmark", "bnch")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.cccObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-ccc-failed').errorFunc(): logFunc('cccObj._fillReadTagValues() failed. PARAMS')
                return ReturnCodes.kGeneralError

            if tagValueList.getLen() == tagValueListLen:
                # descendant didn't add anything, no need to read it.
                tagValueList.pop()
            else:
                valEnd = Value()
                valEnd.setXmlEnd((tag, ns, prefix))
                tagValueList.push((tag, ns), valEnd)
        
        if self.bbbObj:
            valBegin = Value()
            (tag, ns, prefix) = ("bbb" , "http://qwilt.com/model/benchmark", "bnch")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.bbbObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-bbb-failed').errorFunc(): logFunc('bbbObj._fillReadTagValues() failed. PARAMS')
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
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-color').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "color", "color", "http://qwilt.com/model/benchmark", tag, ns)
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
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/model/benchmark"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/model/benchmark", tag, ns)
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
        

        
        if self.aaaObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "aaa") or \
                (ns != "http://qwilt.com/model/benchmark") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "aaa", "http://qwilt.com/model/benchmark", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.aaaObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-aaa-failed').errorFunc(): logFunc('aaaObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "aaa") or \
                (ns != "http://qwilt.com/model/benchmark") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "aaa", "http://qwilt.com/model/benchmark", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.cccObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "ccc") or \
                (ns != "http://qwilt.com/model/benchmark") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "ccc", "http://qwilt.com/model/benchmark", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.cccObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-ccc-failed').errorFunc(): logFunc('cccObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "ccc") or \
                (ns != "http://qwilt.com/model/benchmark") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "ccc", "http://qwilt.com/model/benchmark", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        
        if self.bbbObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "bbb") or \
                (ns != "http://qwilt.com/model/benchmark") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "bbb", "http://qwilt.com/model/benchmark", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.bbbObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-bbb-failed').errorFunc(): logFunc('bbbObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "bbb") or \
                (ns != "http://qwilt.com/model/benchmark") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "bbb", "http://qwilt.com/model/benchmark", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "lll", 
        "namespace": "lll", 
        "className": "LllMaapi", 
        "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.lll_maapi_gen import LllMaapi", 
        "baseClassName": "LllMaapiBase", 
        "baseModule": "lll_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "bnch", 
            "yangName": "base", 
            "namespace": "base", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "name": "base"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "isCurrent": true, 
            "yangName": "lll", 
            "namespace": "lll", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "keyLeaf": {
                "varName": "lll", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "lll"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "aaa", 
            "yangName": "aaa", 
            "className": "BlinkyAaaMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.aaa.aaa_maapi_gen import BlinkyAaaMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "ccc", 
            "yangName": "ccc", 
            "className": "BlinkyCccMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.ccc.ccc_maapi_gen import BlinkyCccMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }, 
        {
            "moduleYangNamespacePrefix": "bnch", 
            "memberName": "bbb", 
            "yangName": "bbb", 
            "className": "BlinkyBbbMaapi", 
            "importStatement": "from a.sys.blinky.example.benchmark.benchmark.base.lll.bbb.bbb_maapi_gen import BlinkyBbbMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/model/benchmark"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
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
            "benchmark", 
            "benchmark"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "color", 
            "yangName": "color", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/model/benchmark", 
            "moduleYangNamespacePrefix": "bnch", 
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


