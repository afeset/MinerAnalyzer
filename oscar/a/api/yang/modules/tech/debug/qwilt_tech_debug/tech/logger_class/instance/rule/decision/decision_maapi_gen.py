


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

from decision_maapi_base_gen import DecisionMaapiBase


from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import EnableDecision


class BlinkyDecisionMaapi(DecisionMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-decision")
        self.domain = None

        

        
        self.logBacktraceRequested = False
        self.logBacktrace = None
        self.logBacktraceSet = False
        
        self.ignoreConditionRequested = False
        self.ignoreCondition = None
        self.ignoreConditionSet = False
        
        self.logRequested = False
        self.log = None
        self.logSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLogBacktrace(True)
        
        self.requestIgnoreCondition(True)
        
        self.requestLog(True)
        
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLogBacktrace(True)
        
        self.requestIgnoreCondition(True)
        
        self.requestLog(True)
        
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLogBacktrace(False)
        
        self.requestIgnoreCondition(False)
        
        self.requestLog(False)
        
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        self.requestLogBacktrace(False)
        
        self.requestIgnoreCondition(False)
        
        self.requestLog(False)
        
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        self.setLogBacktrace(None)
        self.logBacktraceSet = False
        
        self.setIgnoreCondition(None)
        self.ignoreConditionSet = False
        
        self.setLog(None)
        self.logSet = False
        
        

    def write (self
              , loggerClass
              , instance
              , rule
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(loggerClass, instance, rule, trxContext)

    def read (self
              , loggerClass
              , instance
              , rule
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, rule, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , loggerClass
                       , instance
                       , rule
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(loggerClass, instance, rule, 
                                  True,
                                  trxContext)



    def requestLogBacktrace (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-logbacktrace').debug3Func(): logFunc('called. requested=%s', requested)
        self.logBacktraceRequested = requested
        self.logBacktraceSet = False

    def isLogBacktraceRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-logbacktrace-requested').debug3Func(): logFunc('called. requested=%s', self.logBacktraceRequested)
        return self.logBacktraceRequested

    def getLogBacktrace (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-logbacktrace').debug3Func(): logFunc('called. self.logBacktraceSet=%s, self.logBacktrace=%s', self.logBacktraceSet, self.logBacktrace)
        if self.logBacktraceSet:
            return self.logBacktrace
        return None

    def hasLogBacktrace (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-logbacktrace').debug3Func(): logFunc('called. self.logBacktraceSet=%s, self.logBacktrace=%s', self.logBacktraceSet, self.logBacktrace)
        if self.logBacktraceSet:
            return True
        return False

    def setLogBacktrace (self, logBacktrace):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-logbacktrace').debug3Func(): logFunc('called. logBacktrace=%s, old=%s', logBacktrace, self.logBacktrace)
        self.logBacktraceSet = True
        self.logBacktrace = logBacktrace

    def requestIgnoreCondition (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-ignorecondition').debug3Func(): logFunc('called. requested=%s', requested)
        self.ignoreConditionRequested = requested
        self.ignoreConditionSet = False

    def isIgnoreConditionRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-ignorecondition-requested').debug3Func(): logFunc('called. requested=%s', self.ignoreConditionRequested)
        return self.ignoreConditionRequested

    def getIgnoreCondition (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ignorecondition').debug3Func(): logFunc('called. self.ignoreConditionSet=%s, self.ignoreCondition=%s', self.ignoreConditionSet, self.ignoreCondition)
        if self.ignoreConditionSet:
            return self.ignoreCondition
        return None

    def hasIgnoreCondition (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ignorecondition').debug3Func(): logFunc('called. self.ignoreConditionSet=%s, self.ignoreCondition=%s', self.ignoreConditionSet, self.ignoreCondition)
        if self.ignoreConditionSet:
            return True
        return False

    def setIgnoreCondition (self, ignoreCondition):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ignorecondition').debug3Func(): logFunc('called. ignoreCondition=%s, old=%s', ignoreCondition, self.ignoreCondition)
        self.ignoreConditionSet = True
        self.ignoreCondition = ignoreCondition

    def requestLog (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-log').debug3Func(): logFunc('called. requested=%s', requested)
        self.logRequested = requested
        self.logSet = False

    def isLogRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-log-requested').debug3Func(): logFunc('called. requested=%s', self.logRequested)
        return self.logRequested

    def getLog (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-log').debug3Func(): logFunc('called. self.logSet=%s, self.log=%s', self.logSet, self.log)
        if self.logSet:
            return self.log
        return None

    def hasLog (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-log').debug3Func(): logFunc('called. self.logSet=%s, self.log=%s', self.logSet, self.log)
        if self.logSet:
            return True
        return False

    def setLog (self, log):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-log').debug3Func(): logFunc('called. log=%s, old=%s', log, self.log)
        self.logSet = True
        self.log = log


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.logBacktrace = 0
        self.logBacktraceSet = False
        
        self.ignoreCondition = 0
        self.ignoreConditionSet = False
        
        self.log = 0
        self.logSet = False
        

    def _getSelfKeyPath (self, loggerClass
                         , instance
                         , rule
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("decision", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(rule);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("rule", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(instance);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("instance", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(loggerClass);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("logger-class", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", "qt-debug"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        loggerClass, 
                        instance, 
                        rule, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(loggerClass, 
                                         instance, 
                                         rule, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       rule, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       loggerClass, 
                       instance, 
                       rule, 
                       
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

        keyPath = self._getSelfKeyPath(loggerClass, 
                                       instance, 
                                       rule, 
                                       
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
                               loggerClass, 
                               instance, 
                               rule, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.hasLogBacktrace():
            valLogBacktrace = Value()
            if self.logBacktrace is not None:
                valLogBacktrace.setEnum(self.logBacktrace.getValue())
            else:
                valLogBacktrace.setEmpty()
            tagValueList.push(("log-backtrace", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLogBacktrace)
        
        if self.hasIgnoreCondition():
            valIgnoreCondition = Value()
            if self.ignoreCondition is not None:
                valIgnoreCondition.setEnum(self.ignoreCondition.getValue())
            else:
                valIgnoreCondition.setEmpty()
            tagValueList.push(("ignore-condition", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valIgnoreCondition)
        
        if self.hasLog():
            valLog = Value()
            if self.log is not None:
                valLog.setEnum(self.log.getValue())
            else:
                valLog.setEmpty()
            tagValueList.push(("log", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLog)
        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isLogBacktraceRequested():
            valLogBacktrace = Value()
            valLogBacktrace.setEmpty()
            tagValueList.push(("log-backtrace", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLogBacktrace)
        
        if self.isIgnoreConditionRequested():
            valIgnoreCondition = Value()
            valIgnoreCondition.setEmpty()
            tagValueList.push(("ignore-condition", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valIgnoreCondition)
        
        if self.isLogRequested():
            valLog = Value()
            valLog.setEmpty()
            tagValueList.push(("log", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"), valLog)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isLogBacktraceRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "log-backtrace") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-logbacktrace').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "logBacktrace", "log-backtrace", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-log-backtrace-bad-value').infoFunc(): logFunc('logBacktrace not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLogBacktrace(tempVar)
            for logFunc in self._log('read-tag-values-log-backtrace').debug3Func(): logFunc('read logBacktrace. logBacktrace=%s, tempValue=%s', self.logBacktrace, tempValue.getType())
        
        if self.isIgnoreConditionRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ignore-condition") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-ignorecondition').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "ignoreCondition", "ignore-condition", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ignore-condition-bad-value').infoFunc(): logFunc('ignoreCondition not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setIgnoreCondition(tempVar)
            for logFunc in self._log('read-tag-values-ignore-condition').debug3Func(): logFunc('read ignoreCondition. ignoreCondition=%s, tempValue=%s', self.ignoreCondition, tempValue.getType())
        
        if self.isLogRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "log") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-log').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "log", "log", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asEnum()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-log-bad-value').infoFunc(): logFunc('log not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setLog(tempVar)
            for logFunc in self._log('read-tag-values-log').debug3Func(): logFunc('read log. log=%s, tempValue=%s', self.log, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "decision", 
        "namespace": "decision", 
        "className": "DecisionMaapi", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.rule.decision.decision_maapi_gen import DecisionMaapi", 
        "baseClassName": "DecisionMaapiBase", 
        "baseModule": "decision_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "logger-class", 
            "namespace": "logger_class", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "loggerClass", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "logger-class"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "instance", 
            "namespace": "instance", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "instance", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "instance"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "isCurrent": false, 
            "yangName": "rule", 
            "namespace": "rule", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "keyLeaf": {
                "varName": "rule", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "rule"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-debug", 
            "yangName": "decision", 
            "namespace": "decision", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "name": "decision"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logBacktrace", 
            "yangName": "log-backtrace", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "ignoreCondition", 
            "yangName": "ignore-condition", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "log", 
            "yangName": "log", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
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
            "qwilt_tech_debug"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logBacktrace", 
            "yangName": "log-backtrace", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "ignoreCondition", 
            "yangName": "ignore-condition", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-debug", 
            "moduleYangNamespacePrefix": "qt-debug", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "log", 
            "yangName": "log", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


