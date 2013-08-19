


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

from queue__maapi_base_gen import QueueMaapiBase

from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.queue_group.queue_.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi



class BlinkyQueueMaapi(QueueMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-queue_")
        self.domain = None

        
        self.systemDefaultsObj = None
        

        
        self.queueThresholdLowRequested = False
        self.queueThresholdLow = None
        self.queueThresholdLowSet = False
        
        self.queueSizeRequested = False
        self.queueSize = None
        self.queueSizeSet = False
        
        self.queueThresholdHighRequested = False
        self.queueThresholdHigh = None
        self.queueThresholdHighSet = False
        
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
        
        self.requestQueueThresholdLow(True)
        
        self.requestQueueSize(True)
        
        self.requestQueueThresholdHigh(True)
        
        self.requestName(True)
        
        
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestQueueThresholdLow(True)
        
        self.requestQueueSize(True)
        
        self.requestQueueThresholdHigh(True)
        
        self.requestName(True)
        
        
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestQueueThresholdLow(False)
        
        self.requestQueueSize(False)
        
        self.requestQueueThresholdHigh(False)
        
        self.requestName(False)
        
        
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestQueueThresholdLow(False)
        
        self.requestQueueSize(False)
        
        self.requestQueueThresholdHigh(False)
        
        self.requestName(False)
        
        
        
        if not self.systemDefaultsObj:
            self.systemDefaultsObj = self.newSystemDefaults()
            self.systemDefaultsObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setQueueThresholdLow(None)
        self.queueThresholdLowSet = False
        
        self.setQueueSize(None)
        self.queueSizeSet = False
        
        self.setQueueThresholdHigh(None)
        self.queueThresholdHighSet = False
        
        self.setName(None)
        self.nameSet = False
        
        
        if self.systemDefaultsObj:
            self.systemDefaultsObj.clearAllSet()
        

    def write (self
              , line
              , queueGroup
              , queue_
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(line, queueGroup, queue_, trxContext)

    def read (self
              , line
              , queueGroup
              , queue_
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, queueGroup, queue_, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , line
                       , queueGroup
                       , queue_
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, queueGroup, queue_, 
                                  True,
                                  trxContext)

    def newSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-systemdefaults').debug3Func(): logFunc('called.')
        systemDefaults = BlinkySystemDefaultsMaapi(self._log)
        systemDefaults.init(self.domain)
        return systemDefaults

    def setSystemDefaultsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-systemdefaults').debug3Func(): logFunc('called. obj=%s', obj)
        self.systemDefaultsObj = obj

    def getSystemDefaultsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        return self.systemDefaultsObj

    def hasSystemDefaults (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-systemdefaults').debug3Func(): logFunc('called. self.systemDefaultsObj=%s', self.systemDefaultsObj)
        if self.systemDefaultsObj:
            return True
        return False



    def requestQueueThresholdLow (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-queuethresholdlow').debug3Func(): logFunc('called. requested=%s', requested)
        self.queueThresholdLowRequested = requested
        self.queueThresholdLowSet = False

    def isQueueThresholdLowRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-queuethresholdlow-requested').debug3Func(): logFunc('called. requested=%s', self.queueThresholdLowRequested)
        return self.queueThresholdLowRequested

    def getQueueThresholdLow (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-queuethresholdlow').debug3Func(): logFunc('called. self.queueThresholdLowSet=%s, self.queueThresholdLow=%s', self.queueThresholdLowSet, self.queueThresholdLow)
        if self.queueThresholdLowSet:
            return self.queueThresholdLow
        return None

    def hasQueueThresholdLow (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-queuethresholdlow').debug3Func(): logFunc('called. self.queueThresholdLowSet=%s, self.queueThresholdLow=%s', self.queueThresholdLowSet, self.queueThresholdLow)
        if self.queueThresholdLowSet:
            return True
        return False

    def setQueueThresholdLow (self, queueThresholdLow):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-queuethresholdlow').debug3Func(): logFunc('called. queueThresholdLow=%s, old=%s', queueThresholdLow, self.queueThresholdLow)
        self.queueThresholdLowSet = True
        self.queueThresholdLow = queueThresholdLow

    def requestQueueSize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-queuesize').debug3Func(): logFunc('called. requested=%s', requested)
        self.queueSizeRequested = requested
        self.queueSizeSet = False

    def isQueueSizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-queuesize-requested').debug3Func(): logFunc('called. requested=%s', self.queueSizeRequested)
        return self.queueSizeRequested

    def getQueueSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-queuesize').debug3Func(): logFunc('called. self.queueSizeSet=%s, self.queueSize=%s', self.queueSizeSet, self.queueSize)
        if self.queueSizeSet:
            return self.queueSize
        return None

    def hasQueueSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-queuesize').debug3Func(): logFunc('called. self.queueSizeSet=%s, self.queueSize=%s', self.queueSizeSet, self.queueSize)
        if self.queueSizeSet:
            return True
        return False

    def setQueueSize (self, queueSize):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-queuesize').debug3Func(): logFunc('called. queueSize=%s, old=%s', queueSize, self.queueSize)
        self.queueSizeSet = True
        self.queueSize = queueSize

    def requestQueueThresholdHigh (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-queuethresholdhigh').debug3Func(): logFunc('called. requested=%s', requested)
        self.queueThresholdHighRequested = requested
        self.queueThresholdHighSet = False

    def isQueueThresholdHighRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-queuethresholdhigh-requested').debug3Func(): logFunc('called. requested=%s', self.queueThresholdHighRequested)
        return self.queueThresholdHighRequested

    def getQueueThresholdHigh (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-queuethresholdhigh').debug3Func(): logFunc('called. self.queueThresholdHighSet=%s, self.queueThresholdHigh=%s', self.queueThresholdHighSet, self.queueThresholdHigh)
        if self.queueThresholdHighSet:
            return self.queueThresholdHigh
        return None

    def hasQueueThresholdHigh (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-queuethresholdhigh').debug3Func(): logFunc('called. self.queueThresholdHighSet=%s, self.queueThresholdHigh=%s', self.queueThresholdHighSet, self.queueThresholdHigh)
        if self.queueThresholdHighSet:
            return True
        return False

    def setQueueThresholdHigh (self, queueThresholdHigh):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-queuethresholdhigh').debug3Func(): logFunc('called. queueThresholdHigh=%s, old=%s', queueThresholdHigh, self.queueThresholdHigh)
        self.queueThresholdHighSet = True
        self.queueThresholdHigh = queueThresholdHigh

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

        
        if self.systemDefaultsObj:
            self.systemDefaultsObj._clearAllReadData()
        

        
        self.queueThresholdLow = 0
        self.queueThresholdLowSet = False
        
        self.queueSize = 0
        self.queueSizeSet = False
        
        self.queueThresholdHigh = 0
        self.queueThresholdHighSet = False
        
        self.name = 0
        self.nameSet = False
        

    def _getSelfKeyPath (self, line
                         , queueGroup
                         , queue_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        ancestorVal = Value()
        ancestorVal.setString(queue_);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("queue", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(queueGroup);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("queue-group", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("dispatcher", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(line);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("content", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", "qtc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        line, 
                        queueGroup, 
                        queue_, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(line, 
                                         queueGroup, 
                                         queue_, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(line, 
                                       queueGroup, 
                                       queue_, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       line, 
                       queueGroup, 
                       queue_, 
                       
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

        keyPath = self._getSelfKeyPath(line, 
                                       queueGroup, 
                                       queue_, 
                                       
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
                               line, 
                               queueGroup, 
                               queue_, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        
        if self.systemDefaultsObj:
            res = self.systemDefaultsObj._collectItemsToDelete(line, 
                                                                          queueGroup, 
                                                                          queue_, 
                                                                          
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasQueueThresholdLow():
            valQueueThresholdLow = Value()
            if self.queueThresholdLow is not None:
                valQueueThresholdLow.setInt64(self.queueThresholdLow)
            else:
                valQueueThresholdLow.setEmpty()
            tagValueList.push(("queue-threshold-low", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueThresholdLow)
        
        if self.hasQueueSize():
            valQueueSize = Value()
            if self.queueSize is not None:
                valQueueSize.setInt64(self.queueSize)
            else:
                valQueueSize.setEmpty()
            tagValueList.push(("queue-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueSize)
        
        if self.hasQueueThresholdHigh():
            valQueueThresholdHigh = Value()
            if self.queueThresholdHigh is not None:
                valQueueThresholdHigh.setInt64(self.queueThresholdHigh)
            else:
                valQueueThresholdHigh.setEmpty()
            tagValueList.push(("queue-threshold-high", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueThresholdHigh)
        
        if self.hasName():
            valName = Value()
            if self.name is not None:
                valName.setString(self.name)
            else:
                valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valName)
        

        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isQueueThresholdLowRequested():
            valQueueThresholdLow = Value()
            valQueueThresholdLow.setEmpty()
            tagValueList.push(("queue-threshold-low", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueThresholdLow)
        
        if self.isQueueSizeRequested():
            valQueueSize = Value()
            valQueueSize.setEmpty()
            tagValueList.push(("queue-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueSize)
        
        if self.isQueueThresholdHighRequested():
            valQueueThresholdHigh = Value()
            valQueueThresholdHigh.setEmpty()
            tagValueList.push(("queue-threshold-high", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueThresholdHigh)
        
        if self.isNameRequested():
            valName = Value()
            valName.setEmpty()
            tagValueList.push(("name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valName)
        

        
        if self.systemDefaultsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("system-defaults" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.systemDefaultsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isQueueThresholdLowRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "queue-threshold-low") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-queuethresholdlow').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "queueThresholdLow", "queue-threshold-low", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-queue-threshold-low-bad-value').infoFunc(): logFunc('queueThresholdLow not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setQueueThresholdLow(tempVar)
            for logFunc in self._log('read-tag-values-queue-threshold-low').debug3Func(): logFunc('read queueThresholdLow. queueThresholdLow=%s, tempValue=%s', self.queueThresholdLow, tempValue.getType())
        
        if self.isQueueSizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "queue-size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-queuesize').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "queueSize", "queue-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-queue-size-bad-value').infoFunc(): logFunc('queueSize not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setQueueSize(tempVar)
            for logFunc in self._log('read-tag-values-queue-size').debug3Func(): logFunc('read queueSize. queueSize=%s, tempValue=%s', self.queueSize, tempValue.getType())
        
        if self.isQueueThresholdHighRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "queue-threshold-high") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-queuethresholdhigh').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "queueThresholdHigh", "queue-threshold-high", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-queue-threshold-high-bad-value').infoFunc(): logFunc('queueThresholdHigh not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setQueueThresholdHigh(tempVar)
            for logFunc in self._log('read-tag-values-queue-threshold-high').debug3Func(): logFunc('read queueThresholdHigh. queueThresholdHigh=%s, tempValue=%s', self.queueThresholdHigh, tempValue.getType())
        
        if self.isNameRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "name") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-name').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "name", "name", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
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
        

        
        if self.systemDefaultsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.systemDefaultsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-system-defaults-failed').errorFunc(): logFunc('systemDefaultsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "system-defaults") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "queue_", 
        "namespace": "queue_", 
        "className": "QueueMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.queue_group.queue_.queue__maapi_gen import QueueMaapi", 
        "baseClassName": "QueueMaapiBase", 
        "baseModule": "queue__maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": false, 
            "yangName": "line", 
            "namespace": "line", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "line", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "line"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "dispatcher", 
            "namespace": "dispatcher", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "dispatcher"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": false, 
            "yangName": "queue-group", 
            "namespace": "queue_group", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "queueGroup", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "queue-group"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "isCurrent": true, 
            "yangName": "queue", 
            "namespace": "queue_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "keyLeaf": {
                "varName": "queue_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "queue_"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.queue_group.queue_.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdLow", 
            "yangName": "queue-threshold-low", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueSize", 
            "yangName": "queue-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdHigh", 
            "yangName": "queue-threshold-high", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
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
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdLow", 
            "yangName": "queue-threshold-low", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueSize", 
            "yangName": "queue-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdHigh", 
            "yangName": "queue-threshold-high", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
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


