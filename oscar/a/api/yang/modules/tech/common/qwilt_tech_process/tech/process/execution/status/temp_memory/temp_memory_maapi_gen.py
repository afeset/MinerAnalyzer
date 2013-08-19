


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

from temp_memory_maapi_base_gen import TempMemoryMaapiBase




class BlinkyTempMemoryMaapi(TempMemoryMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-tempMemory")
        self.domain = None

        

        
        self.virtualSizeRequested = False
        self.virtualSize = None
        self.virtualSizeSet = False
        
        self.rssSizeRequested = False
        self.rssSize = None
        self.rssSizeSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestVirtualSize(True)
        
        self.requestRssSize(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestVirtualSize(False)
        
        self.requestRssSize(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestVirtualSize(True)
        
        self.requestRssSize(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestVirtualSize(False)
        
        self.requestRssSize(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , process
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(process, trxContext)

    def read (self
              , process
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(process, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , process
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(process, 
                                  True,
                                  trxContext)



    def requestVirtualSize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-virtualsize').debug3Func(): logFunc('called. requested=%s', requested)
        self.virtualSizeRequested = requested
        self.virtualSizeSet = False

    def isVirtualSizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-virtualsize-requested').debug3Func(): logFunc('called. requested=%s', self.virtualSizeRequested)
        return self.virtualSizeRequested

    def getVirtualSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-virtualsize').debug3Func(): logFunc('called. self.virtualSizeSet=%s, self.virtualSize=%s', self.virtualSizeSet, self.virtualSize)
        if self.virtualSizeSet:
            return self.virtualSize
        return None

    def hasVirtualSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-virtualsize').debug3Func(): logFunc('called. self.virtualSizeSet=%s, self.virtualSize=%s', self.virtualSizeSet, self.virtualSize)
        if self.virtualSizeSet:
            return True
        return False

    def setVirtualSize (self, virtualSize):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-virtualsize').debug3Func(): logFunc('called. virtualSize=%s, old=%s', virtualSize, self.virtualSize)
        self.virtualSizeSet = True
        self.virtualSize = virtualSize

    def requestRssSize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-rsssize').debug3Func(): logFunc('called. requested=%s', requested)
        self.rssSizeRequested = requested
        self.rssSizeSet = False

    def isRssSizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-rsssize-requested').debug3Func(): logFunc('called. requested=%s', self.rssSizeRequested)
        return self.rssSizeRequested

    def getRssSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-rsssize').debug3Func(): logFunc('called. self.rssSizeSet=%s, self.rssSize=%s', self.rssSizeSet, self.rssSize)
        if self.rssSizeSet:
            return self.rssSize
        return None

    def hasRssSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-rsssize').debug3Func(): logFunc('called. self.rssSizeSet=%s, self.rssSize=%s', self.rssSizeSet, self.rssSize)
        if self.rssSizeSet:
            return True
        return False

    def setRssSize (self, rssSize):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-rsssize').debug3Func(): logFunc('called. rssSize=%s, old=%s', rssSize, self.rssSize)
        self.rssSizeSet = True
        self.rssSize = rssSize


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.virtualSize = 0
        self.virtualSizeSet = False
        
        self.rssSize = 0
        self.rssSizeSet = False
        

    def _getSelfKeyPath (self, process
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("temp-memory", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("status", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("execution", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(process);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("process", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        process, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(process, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(process, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       process, 
                       
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

        keyPath = self._getSelfKeyPath(process, 
                                       
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
                               process, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isVirtualSizeRequested():
            valVirtualSize = Value()
            valVirtualSize.setEmpty()
            tagValueList.push(("virtual-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valVirtualSize)
        
        if self.isRssSizeRequested():
            valRssSize = Value()
            valRssSize.setEmpty()
            tagValueList.push(("rss-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valRssSize)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isVirtualSizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "virtual-size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-virtualsize').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "virtualSize", "virtual-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-virtual-size-bad-value').infoFunc(): logFunc('virtualSize not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setVirtualSize(tempVar)
            for logFunc in self._log('read-tag-values-virtual-size').debug3Func(): logFunc('read virtualSize. virtualSize=%s, tempValue=%s', self.virtualSize, tempValue.getType())
        
        if self.isRssSizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "rss-size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-rsssize').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "rssSize", "rss-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-rss-size-bad-value').infoFunc(): logFunc('rssSize not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setRssSize(tempVar)
            for logFunc in self._log('read-tag-values-rss-size').debug3Func(): logFunc('read rssSize. rssSize=%s, tempValue=%s', self.rssSize, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "tempMemory", 
        "namespace": "temp_memory", 
        "className": "TempMemoryMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.temp_memory.temp_memory_maapi_gen import TempMemoryMaapi", 
        "baseClassName": "TempMemoryMaapiBase", 
        "baseModule": "temp_memory_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-proc", 
            "isCurrent": false, 
            "yangName": "process", 
            "namespace": "process", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "keyLeaf": {
                "varName": "process", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "process"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "yangName": "execution", 
            "namespace": "execution", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "name": "execution"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "name": "status"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "yangName": "temp-memory", 
            "namespace": "temp_memory", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "name": "temp-memory"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "virtualSize", 
            "yangName": "virtual-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rssSize", 
            "yangName": "rss-size", 
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
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_process"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "virtualSize", 
            "yangName": "virtual-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rssSize", 
            "yangName": "rss-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


