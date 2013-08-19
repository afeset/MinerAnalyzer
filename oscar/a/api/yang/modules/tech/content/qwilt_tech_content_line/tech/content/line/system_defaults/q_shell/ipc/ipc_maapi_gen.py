


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

from ipc_maapi_base_gen import IpcMaapiBase




class BlinkyIpcMaapi(IpcMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-ipc")
        self.domain = None

        

        
        self.threadPriorityRequested = False
        self.threadPriority = None
        self.threadPrioritySet = False
        
        self.threadAffinityRequested = False
        self.threadAffinity = None
        self.threadAffinitySet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadPriority(True)
        
        self.requestThreadAffinity(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadPriority(True)
        
        self.requestThreadAffinity(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadPriority(False)
        
        self.requestThreadAffinity(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestThreadPriority(False)
        
        self.requestThreadAffinity(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setThreadPriority(None)
        self.threadPrioritySet = False
        
        self.setThreadAffinity(None)
        self.threadAffinitySet = False
        
        

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



    def requestThreadPriority (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-threadpriority').debug3Func(): logFunc('called. requested=%s', requested)
        self.threadPriorityRequested = requested
        self.threadPrioritySet = False

    def isThreadPriorityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-threadpriority-requested').debug3Func(): logFunc('called. requested=%s', self.threadPriorityRequested)
        return self.threadPriorityRequested

    def getThreadPriority (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-threadpriority').debug3Func(): logFunc('called. self.threadPrioritySet=%s, self.threadPriority=%s', self.threadPrioritySet, self.threadPriority)
        if self.threadPrioritySet:
            return self.threadPriority
        return None

    def hasThreadPriority (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-threadpriority').debug3Func(): logFunc('called. self.threadPrioritySet=%s, self.threadPriority=%s', self.threadPrioritySet, self.threadPriority)
        if self.threadPrioritySet:
            return True
        return False

    def setThreadPriority (self, threadPriority):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-threadpriority').debug3Func(): logFunc('called. threadPriority=%s, old=%s', threadPriority, self.threadPriority)
        self.threadPrioritySet = True
        self.threadPriority = threadPriority

    def requestThreadAffinity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-threadaffinity').debug3Func(): logFunc('called. requested=%s', requested)
        self.threadAffinityRequested = requested
        self.threadAffinitySet = False

    def isThreadAffinityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-threadaffinity-requested').debug3Func(): logFunc('called. requested=%s', self.threadAffinityRequested)
        return self.threadAffinityRequested

    def getThreadAffinity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-threadaffinity').debug3Func(): logFunc('called. self.threadAffinitySet=%s, self.threadAffinity=%s', self.threadAffinitySet, self.threadAffinity)
        if self.threadAffinitySet:
            return self.threadAffinity
        return None

    def hasThreadAffinity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-threadaffinity').debug3Func(): logFunc('called. self.threadAffinitySet=%s, self.threadAffinity=%s', self.threadAffinitySet, self.threadAffinity)
        if self.threadAffinitySet:
            return True
        return False

    def setThreadAffinity (self, threadAffinity):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-threadaffinity').debug3Func(): logFunc('called. threadAffinity=%s, old=%s', threadAffinity, self.threadAffinity)
        self.threadAffinitySet = True
        self.threadAffinity = threadAffinity


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.threadPriority = 0
        self.threadPrioritySet = False
        
        self.threadAffinity = 0
        self.threadAffinitySet = False
        

    def _getSelfKeyPath (self, line
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ipc", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("q-shell", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("system-defaults", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", "qtc-line"))
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

        
        if self.hasThreadPriority():
            valThreadPriority = Value()
            if self.threadPriority is not None:
                valThreadPriority.setString(self.threadPriority)
            else:
                valThreadPriority.setEmpty()
            tagValueList.push(("thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadPriority)
        
        if self.hasThreadAffinity():
            valThreadAffinity = Value()
            if self.threadAffinity is not None:
                valThreadAffinity.setString(self.threadAffinity)
            else:
                valThreadAffinity.setEmpty()
            tagValueList.push(("thread-affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadAffinity)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isThreadPriorityRequested():
            valThreadPriority = Value()
            valThreadPriority.setEmpty()
            tagValueList.push(("thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadPriority)
        
        if self.isThreadAffinityRequested():
            valThreadAffinity = Value()
            valThreadAffinity.setEmpty()
            tagValueList.push(("thread-affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"), valThreadAffinity)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isThreadPriorityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "thread-priority") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-threadpriority').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "threadPriority", "thread-priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-thread-priority-bad-value').infoFunc(): logFunc('threadPriority not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setThreadPriority(tempVar)
            for logFunc in self._log('read-tag-values-thread-priority').debug3Func(): logFunc('read threadPriority. threadPriority=%s, tempValue=%s', self.threadPriority, tempValue.getType())
        
        if self.isThreadAffinityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "thread-affinity") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-threadaffinity').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "threadAffinity", "thread-affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-thread-affinity-bad-value').infoFunc(): logFunc('threadAffinity not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setThreadAffinity(tempVar)
            for logFunc in self._log('read-tag-values-thread-affinity').debug3Func(): logFunc('read threadAffinity. threadAffinity=%s, tempValue=%s', self.threadAffinity, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "ipc", 
        "namespace": "ipc", 
        "className": "IpcMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.system_defaults.q_shell.ipc.ipc_maapi_gen import IpcMaapi", 
        "baseClassName": "IpcMaapiBase", 
        "baseModule": "ipc_maapi_base_gen"
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
            "yangName": "system-defaults", 
            "namespace": "system_defaults", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "system-defaults"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "q-shell", 
            "namespace": "q_shell", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "q-shell"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-line", 
            "yangName": "ipc", 
            "namespace": "ipc", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "name": "ipc"
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadAffinity", 
            "yangName": "thread-affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadPriority", 
            "yangName": "thread-priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-line", 
            "moduleYangNamespacePrefix": "qtc-line", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "threadAffinity", 
            "yangName": "thread-affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


