


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

from actual_maapi_base_gen import ActualMaapiBase




class BlinkyActualMaapi(ActualMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-actual")
        self.domain = None

        

        
        self.priorityRequested = False
        self.priority = None
        self.prioritySet = False
        
        self.affinityRequested = False
        self.affinity = None
        self.affinitySet = False
        
        self.commandLineRequested = False
        self.commandLine = None
        self.commandLineSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPriority(True)
        
        self.requestAffinity(True)
        
        self.requestCommandLine(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPriority(False)
        
        self.requestAffinity(False)
        
        self.requestCommandLine(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPriority(True)
        
        self.requestAffinity(True)
        
        self.requestCommandLine(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestPriority(False)
        
        self.requestAffinity(False)
        
        self.requestCommandLine(False)
        
        

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



    def requestPriority (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-priority').debug3Func(): logFunc('called. requested=%s', requested)
        self.priorityRequested = requested
        self.prioritySet = False

    def isPriorityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-priority-requested').debug3Func(): logFunc('called. requested=%s', self.priorityRequested)
        return self.priorityRequested

    def getPriority (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-priority').debug3Func(): logFunc('called. self.prioritySet=%s, self.priority=%s', self.prioritySet, self.priority)
        if self.prioritySet:
            return self.priority
        return None

    def hasPriority (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-priority').debug3Func(): logFunc('called. self.prioritySet=%s, self.priority=%s', self.prioritySet, self.priority)
        if self.prioritySet:
            return True
        return False

    def setPriority (self, priority):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-priority').debug3Func(): logFunc('called. priority=%s, old=%s', priority, self.priority)
        self.prioritySet = True
        self.priority = priority

    def requestAffinity (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-affinity').debug3Func(): logFunc('called. requested=%s', requested)
        self.affinityRequested = requested
        self.affinitySet = False

    def isAffinityRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-affinity-requested').debug3Func(): logFunc('called. requested=%s', self.affinityRequested)
        return self.affinityRequested

    def getAffinity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-affinity').debug3Func(): logFunc('called. self.affinitySet=%s, self.affinity=%s', self.affinitySet, self.affinity)
        if self.affinitySet:
            return self.affinity
        return None

    def hasAffinity (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-affinity').debug3Func(): logFunc('called. self.affinitySet=%s, self.affinity=%s', self.affinitySet, self.affinity)
        if self.affinitySet:
            return True
        return False

    def setAffinity (self, affinity):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-affinity').debug3Func(): logFunc('called. affinity=%s, old=%s', affinity, self.affinity)
        self.affinitySet = True
        self.affinity = affinity

    def requestCommandLine (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-commandline').debug3Func(): logFunc('called. requested=%s', requested)
        self.commandLineRequested = requested
        self.commandLineSet = False

    def isCommandLineRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-commandline-requested').debug3Func(): logFunc('called. requested=%s', self.commandLineRequested)
        return self.commandLineRequested

    def getCommandLine (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-commandline').debug3Func(): logFunc('called. self.commandLineSet=%s, self.commandLine=%s', self.commandLineSet, self.commandLine)
        if self.commandLineSet:
            return self.commandLine
        return None

    def hasCommandLine (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-commandline').debug3Func(): logFunc('called. self.commandLineSet=%s, self.commandLine=%s', self.commandLineSet, self.commandLine)
        if self.commandLineSet:
            return True
        return False

    def setCommandLine (self, commandLine):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-commandline').debug3Func(): logFunc('called. commandLine=%s, old=%s', commandLine, self.commandLine)
        self.commandLineSet = True
        self.commandLine = commandLine


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.priority = 0
        self.prioritySet = False
        
        self.affinity = 0
        self.affinitySet = False
        
        self.commandLine = 0
        self.commandLineSet = False
        

    def _getSelfKeyPath (self, process
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("actual", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", "qt-proc"))
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

        
        if self.isPriorityRequested():
            valPriority = Value()
            valPriority.setEmpty()
            tagValueList.push(("priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valPriority)
        
        if self.isAffinityRequested():
            valAffinity = Value()
            valAffinity.setEmpty()
            tagValueList.push(("affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valAffinity)
        
        if self.isCommandLineRequested():
            valCommandLine = Value()
            valCommandLine.setEmpty()
            tagValueList.push(("command-line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"), valCommandLine)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isPriorityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "priority") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-priority').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "priority", "priority", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-priority-bad-value').infoFunc(): logFunc('priority not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPriority(tempVar)
            for logFunc in self._log('read-tag-values-priority').debug3Func(): logFunc('read priority. priority=%s, tempValue=%s', self.priority, tempValue.getType())
        
        if self.isAffinityRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "affinity") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-affinity').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "affinity", "affinity", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-affinity-bad-value').infoFunc(): logFunc('affinity not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setAffinity(tempVar)
            for logFunc in self._log('read-tag-values-affinity').debug3Func(): logFunc('read affinity. affinity=%s, tempValue=%s', self.affinity, tempValue.getType())
        
        if self.isCommandLineRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "command-line") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-commandline').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "commandLine", "command-line", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asString()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-command-line-bad-value').infoFunc(): logFunc('commandLine not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setCommandLine(tempVar)
            for logFunc in self._log('read-tag-values-command-line').debug3Func(): logFunc('read commandLine. commandLine=%s, tempValue=%s', self.commandLine, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "actual", 
        "namespace": "actual", 
        "className": "ActualMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.actual.actual_maapi_gen import ActualMaapi", 
        "baseClassName": "ActualMaapiBase", 
        "baseModule": "actual_maapi_base_gen"
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
            "yangName": "actual", 
            "namespace": "actual", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "name": "actual"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "priority", 
            "yangName": "priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "affinity", 
            "yangName": "affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "commandLine", 
            "yangName": "command-line", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "priority", 
            "yangName": "priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "affinity", 
            "yangName": "affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "commandLine", 
            "yangName": "command-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


