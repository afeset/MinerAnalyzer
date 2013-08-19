


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

from system_defaults_maapi_base_gen import SystemDefaultsMaapiBase




class BlinkySystemDefaultsMaapi(SystemDefaultsMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-systemDefaults")
        self.domain = None

        

        
        self.queueThresholdLowRequested = False
        self.queueThresholdLow = None
        self.queueThresholdLowSet = False
        
        self.queueThresholdHighRequested = False
        self.queueThresholdHigh = None
        self.queueThresholdHighSet = False
        
        self.queueSizeRequested = False
        self.queueSize = None
        self.queueSizeSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestQueueThresholdLow(True)
        
        self.requestQueueThresholdHigh(True)
        
        self.requestQueueSize(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestQueueThresholdLow(True)
        
        self.requestQueueThresholdHigh(True)
        
        self.requestQueueSize(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestQueueThresholdLow(False)
        
        self.requestQueueThresholdHigh(False)
        
        self.requestQueueSize(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestQueueThresholdLow(False)
        
        self.requestQueueThresholdHigh(False)
        
        self.requestQueueSize(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setQueueThresholdLow(None)
        self.queueThresholdLowSet = False
        
        self.setQueueThresholdHigh(None)
        self.queueThresholdHighSet = False
        
        self.setQueueSize(None)
        self.queueSizeSet = False
        
        

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


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.queueThresholdLow = 0
        self.queueThresholdLowSet = False
        
        self.queueThresholdHigh = 0
        self.queueThresholdHighSet = False
        
        self.queueSize = 0
        self.queueSizeSet = False
        

    def _getSelfKeyPath (self, line
                         , queueGroup
                         , queue_
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
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
        
        if self.hasQueueThresholdHigh():
            valQueueThresholdHigh = Value()
            if self.queueThresholdHigh is not None:
                valQueueThresholdHigh.setInt64(self.queueThresholdHigh)
            else:
                valQueueThresholdHigh.setEmpty()
            tagValueList.push(("queue-threshold-high", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueThresholdHigh)
        
        if self.hasQueueSize():
            valQueueSize = Value()
            if self.queueSize is not None:
                valQueueSize.setInt64(self.queueSize)
            else:
                valQueueSize.setEmpty()
            tagValueList.push(("queue-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueSize)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isQueueThresholdLowRequested():
            valQueueThresholdLow = Value()
            valQueueThresholdLow.setEmpty()
            tagValueList.push(("queue-threshold-low", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueThresholdLow)
        
        if self.isQueueThresholdHighRequested():
            valQueueThresholdHigh = Value()
            valQueueThresholdHigh.setEmpty()
            tagValueList.push(("queue-threshold-high", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueThresholdHigh)
        
        if self.isQueueSizeRequested():
            valQueueSize = Value()
            valQueueSize.setEmpty()
            tagValueList.push(("queue-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valQueueSize)
        

        

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
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "systemDefaults", 
        "namespace": "system_defaults", 
        "className": "SystemDefaultsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.queue_group.queue_.system_defaults.system_defaults_maapi_gen import SystemDefaultsMaapi", 
        "baseClassName": "SystemDefaultsMaapiBase", 
        "baseModule": "system_defaults_maapi_base_gen"
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
            "isCurrent": false, 
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
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "system-defaults"
        }
    ], 
    "descendants": [], 
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
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdHigh", 
            "yangName": "queue-threshold-high", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueSize", 
            "yangName": "queue-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
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
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueThresholdHigh", 
            "yangName": "queue-threshold-high", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueSize", 
            "yangName": "queue-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


