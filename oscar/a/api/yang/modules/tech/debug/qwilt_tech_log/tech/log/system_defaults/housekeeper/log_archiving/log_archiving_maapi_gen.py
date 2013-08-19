


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

from log_archiving_maapi_base_gen import LogArchivingMaapiBase

from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.system_defaults.housekeeper.log_archiving.thresholds.thresholds_maapi_gen import BlinkyThresholdsMaapi



class BlinkyLogArchivingMaapi(LogArchivingMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-logArchiving")
        self.domain = None

        
        self.thresholdsObj = None
        

        
        self.dummyRequested = False
        self.dummy = None
        self.dummySet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDummy(True)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestConfigAndOper()
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDummy(True)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestConfig()
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDummy(False)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.requestOper()
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestDummy(False)
        
        
        
        if not self.thresholdsObj:
            self.thresholdsObj = self.newThresholds()
            self.thresholdsObj.clearAllRequested()
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setDummy(None)
        self.dummySet = False
        
        
        if self.thresholdsObj:
            self.thresholdsObj.clearAllSet()
        

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

    def newThresholds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('new-thresholds').debug3Func(): logFunc('called.')
        thresholds = BlinkyThresholdsMaapi(self._log)
        thresholds.init(self.domain)
        return thresholds

    def setThresholdsObj (self, obj):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-thresholds').debug3Func(): logFunc('called. obj=%s', obj)
        self.thresholdsObj = obj

    def getThresholdsObj (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-thresholds').debug3Func(): logFunc('called. self.thresholdsObj=%s', self.thresholdsObj)
        return self.thresholdsObj

    def hasThresholds (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-thresholds').debug3Func(): logFunc('called. self.thresholdsObj=%s', self.thresholdsObj)
        if self.thresholdsObj:
            return True
        return False



    def requestDummy (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-dummy').debug3Func(): logFunc('called. requested=%s', requested)
        self.dummyRequested = requested
        self.dummySet = False

    def isDummyRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-dummy-requested').debug3Func(): logFunc('called. requested=%s', self.dummyRequested)
        return self.dummyRequested

    def getDummy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-dummy').debug3Func(): logFunc('called. self.dummySet=%s, self.dummy=%s', self.dummySet, self.dummy)
        if self.dummySet:
            return self.dummy
        return None

    def hasDummy (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-dummy').debug3Func(): logFunc('called. self.dummySet=%s, self.dummy=%s', self.dummySet, self.dummy)
        if self.dummySet:
            return True
        return False

    def setDummy (self, dummy):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-dummy').debug3Func(): logFunc('called. dummy=%s, old=%s', dummy, self.dummy)
        self.dummySet = True
        self.dummy = dummy


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        
        if self.thresholdsObj:
            self.thresholdsObj._clearAllReadData()
        

        
        self.dummy = 0
        self.dummySet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("log-archiving", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("housekeeper", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("log", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
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

        
        if self.thresholdsObj:
            res = self.thresholdsObj._collectItemsToDelete(
                                                                          itemsToDelete)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('collect-items-to-delete-thresholds-failed').errorFunc(): logFunc('thresholdsObj._collectItemsToDelete() failed. PARAMS')
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasDummy():
            valDummy = Value()
            if self.dummy is not None:
                valDummy.setBool(self.dummy)
            else:
                valDummy.setEmpty()
            tagValueList.push(("dummy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valDummy)
        

        
        if self.thresholdsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("thresholds" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.thresholdsObj._fillWriteTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-write-tag-values-thresholds-failed').errorFunc(): logFunc('thresholdsObj._fillWriteTagValues() failed. PARAMS')
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

        
        if self.isDummyRequested():
            valDummy = Value()
            valDummy.setEmpty()
            tagValueList.push(("dummy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"), valDummy)
        

        
        if self.thresholdsObj:
            valBegin = Value()
            (tag, ns, prefix) = ("thresholds" , "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", "qt-log")
            valBegin.setXmlBegin((tag, ns, prefix))
            tagValueList.push((tag, ns), valBegin)

            tagValueListLen = tagValueList.getLen()

            res = self.thresholdsObj._fillReadTagValues(tagValueList)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('fill-read-tag-values-thresholds-failed').errorFunc(): logFunc('thresholdsObj._fillReadTagValues() failed. PARAMS')
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
        
        if self.isDummyRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "dummy") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-dummy').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "dummy", "dummy", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asBool()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-dummy-bad-value').infoFunc(): logFunc('dummy not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setDummy(tempVar)
            for logFunc in self._log('read-tag-values-dummy').debug3Func(): logFunc('read dummy. dummy=%s, tempValue=%s', self.dummy, tempValue.getType())
        

        
        if self.thresholdsObj:
            ((tag, ns), valBegin) = tagValueList.popFront()
            if (tag != "thresholds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log") or \
                (valBegin.getType() != Value.kXmlBegin):
                for logFunc in self._log('reag-tag-values-unexpected-tag-begin').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                        "thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", Value.kXmlBegin,
                                                                        tag, ns, valBegin.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
            
            res = self.thresholdsObj._readTagValues(tagValueList, readAllOrFail)
            if res != ReturnCodes.kOk:
                for logFunc in self._log('read-tag-values-thresholds-failed').errorFunc(): logFunc('thresholdsObj._readTagValues() failed. tagValueList=%s', tagValueList)
                if readAllOrFail:
                    self._clearAllReadData()
                return ReturnCodes.kGeneralError

            ((tag, ns), valEnd) = tagValueList.popFront()
            if (tag != "thresholds") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log") or \
                (valEnd.getType() != Value.kXmlEnd):
                for logFunc in self._log('reag-tag-values-unexpected-tag-end').errorFunc(): logFunc('got unexpected tag-value. expected: (%s, %s, type=%s), got: (%s, %s, type=%s)',
                                                                      "thresholds", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", Value.kXmlEnd,
                                                                        tag, ns, valEnd.getType())
                self._clearAllReadData()
                return ReturnCodes.kGeneralError
        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "logArchiving", 
        "namespace": "log_archiving", 
        "className": "LogArchivingMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.system_defaults.housekeeper.log_archiving.log_archiving_maapi_gen import LogArchivingMaapi", 
        "baseClassName": "LogArchivingMaapiBase", 
        "baseModule": "log_archiving_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log", 
            "namespace": "log", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "housekeeper", 
            "namespace": "housekeeper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "housekeeper"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "yangName": "log-archiving", 
            "namespace": "log_archiving", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "name": "log-archiving"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-log", 
            "memberName": "thresholds", 
            "yangName": "thresholds", 
            "className": "BlinkyThresholdsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.system_defaults.housekeeper.log_archiving.thresholds.thresholds_maapi_gen import BlinkyThresholdsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "dummy", 
            "yangName": "dummy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
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
            "debug", 
            "qwilt_tech_log"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-log", 
            "moduleYangNamespacePrefix": "qt-log", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "dummy", 
            "yangName": "dummy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


