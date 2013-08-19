


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

from dpdk_maapi_base_gen import DpdkMaapiBase




class BlinkyDpdkMaapi(DpdkMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-dpdk")
        self.domain = None

        

        
        self.channelQueueSizeRequested = False
        self.channelQueueSize = None
        self.channelQueueSizeSet = False
        
        self.memSizeRequested = False
        self.memSize = None
        self.memSizeSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestChannelQueueSize(True)
        
        self.requestMemSize(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestChannelQueueSize(True)
        
        self.requestMemSize(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestChannelQueueSize(False)
        
        self.requestMemSize(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestChannelQueueSize(False)
        
        self.requestMemSize(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setChannelQueueSize(None)
        self.channelQueueSizeSet = False
        
        self.setMemSize(None)
        self.memSizeSet = False
        
        

    def write (self
              , line
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(line, trxContext)

    def read (self
              , line
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , line
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(line, 
                                  True,
                                  trxContext)



    def requestChannelQueueSize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-channelqueuesize').debug3Func(): logFunc('called. requested=%s', requested)
        self.channelQueueSizeRequested = requested
        self.channelQueueSizeSet = False

    def isChannelQueueSizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-channelqueuesize-requested').debug3Func(): logFunc('called. requested=%s', self.channelQueueSizeRequested)
        return self.channelQueueSizeRequested

    def getChannelQueueSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-channelqueuesize').debug3Func(): logFunc('called. self.channelQueueSizeSet=%s, self.channelQueueSize=%s', self.channelQueueSizeSet, self.channelQueueSize)
        if self.channelQueueSizeSet:
            return self.channelQueueSize
        return None

    def hasChannelQueueSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-channelqueuesize').debug3Func(): logFunc('called. self.channelQueueSizeSet=%s, self.channelQueueSize=%s', self.channelQueueSizeSet, self.channelQueueSize)
        if self.channelQueueSizeSet:
            return True
        return False

    def setChannelQueueSize (self, channelQueueSize):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-channelqueuesize').debug3Func(): logFunc('called. channelQueueSize=%s, old=%s', channelQueueSize, self.channelQueueSize)
        self.channelQueueSizeSet = True
        self.channelQueueSize = channelQueueSize

    def requestMemSize (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-memsize').debug3Func(): logFunc('called. requested=%s', requested)
        self.memSizeRequested = requested
        self.memSizeSet = False

    def isMemSizeRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-memsize-requested').debug3Func(): logFunc('called. requested=%s', self.memSizeRequested)
        return self.memSizeRequested

    def getMemSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-memsize').debug3Func(): logFunc('called. self.memSizeSet=%s, self.memSize=%s', self.memSizeSet, self.memSize)
        if self.memSizeSet:
            return self.memSize
        return None

    def hasMemSize (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-memsize').debug3Func(): logFunc('called. self.memSizeSet=%s, self.memSize=%s', self.memSizeSet, self.memSize)
        if self.memSizeSet:
            return True
        return False

    def setMemSize (self, memSize):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-memsize').debug3Func(): logFunc('called. memSize=%s, old=%s', memSize, self.memSize)
        self.memSizeSet = True
        self.memSize = memSize


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.channelQueueSize = 0
        self.channelQueueSizeSet = False
        
        self.memSize = 0
        self.memSizeSet = False
        

    def _getSelfKeyPath (self, line
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("dpdk", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
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
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(line, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       line, 
                       
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
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasChannelQueueSize():
            valChannelQueueSize = Value()
            if self.channelQueueSize is not None:
                valChannelQueueSize.setInt64(self.channelQueueSize)
            else:
                valChannelQueueSize.setEmpty()
            tagValueList.push(("channel-queue-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valChannelQueueSize)
        
        if self.hasMemSize():
            valMemSize = Value()
            if self.memSize is not None:
                valMemSize.setInt64(self.memSize)
            else:
                valMemSize.setEmpty()
            tagValueList.push(("mem-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMemSize)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isChannelQueueSizeRequested():
            valChannelQueueSize = Value()
            valChannelQueueSize.setEmpty()
            tagValueList.push(("channel-queue-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valChannelQueueSize)
        
        if self.isMemSizeRequested():
            valMemSize = Value()
            valMemSize.setEmpty()
            tagValueList.push(("mem-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valMemSize)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isChannelQueueSizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "channel-queue-size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-channelqueuesize').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "channelQueueSize", "channel-queue-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-channel-queue-size-bad-value').infoFunc(): logFunc('channelQueueSize not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setChannelQueueSize(tempVar)
            for logFunc in self._log('read-tag-values-channel-queue-size').debug3Func(): logFunc('read channelQueueSize. channelQueueSize=%s, tempValue=%s', self.channelQueueSize, tempValue.getType())
        
        if self.isMemSizeRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "mem-size") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-memsize').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "memSize", "mem-size", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-mem-size-bad-value').infoFunc(): logFunc('memSize not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setMemSize(tempVar)
            for logFunc in self._log('read-tag-values-mem-size').debug3Func(): logFunc('read memSize. memSize=%s, tempValue=%s', self.memSize, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "dpdk", 
        "namespace": "dpdk", 
        "className": "DpdkMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.dispatcher.dpdk.dpdk_maapi_gen import DpdkMaapi", 
        "baseClassName": "DpdkMaapiBase", 
        "baseModule": "dpdk_maapi_base_gen"
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
            "yangName": "dpdk", 
            "namespace": "dpdk", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "dpdk"
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
            "memberName": "channelQueueSize", 
            "yangName": "channel-queue-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "memSize", 
            "yangName": "mem-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "memberName": "channelQueueSize", 
            "yangName": "channel-queue-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "memSize", 
            "yangName": "mem-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


