


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import EnableDecision


class DecisionData(object):

    def __init__ (self):

        self.logBacktrace = EnableDecision.kPassThrough
        self._myHasLogBacktrace=False
        
        self.ignoreCondition = EnableDecision.kPassThrough
        self._myHasIgnoreCondition=False
        
        self.log = EnableDecision.kPassThrough
        self._myHasLog=False
        

    def copyFrom (self, other):

        self.logBacktrace=other.logBacktrace
        self._myHasLogBacktrace=other._myHasLogBacktrace
        
        self.ignoreCondition=other.ignoreCondition
        self._myHasIgnoreCondition=other._myHasIgnoreCondition
        
        self.log=other.log
        self._myHasLog=other._myHasLog
        
    # has...() methods

    def hasLogBacktrace (self):
        return self._myHasLogBacktrace

    def hasIgnoreCondition (self):
        return self._myHasIgnoreCondition

    def hasLog (self):
        return self._myHasLog


    # setHas...() methods

    def setHasLogBacktrace (self):
        self._myHasLogBacktrace=True

    def setHasIgnoreCondition (self):
        self._myHasIgnoreCondition=True

    def setHasLog (self):
        self._myHasLog=True


    def clearAllHas (self):

        self._myHasLogBacktrace=False

        self._myHasIgnoreCondition=False

        self._myHasLog=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasLogBacktrace:
            x = "+"
        leafStr = str(self.logBacktrace)
        items.append(x + "LogBacktrace="+leafStr)

        x=""
        if self._myHasIgnoreCondition:
            x = "+"
        leafStr = str(self.ignoreCondition)
        items.append(x + "IgnoreCondition="+leafStr)

        x=""
        if self._myHasLog:
            x = "+"
        leafStr = str(self.log)
        items.append(x + "Log="+leafStr)

        return "{DecisionData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "DecisionData", 
        "namespace": "decision", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.rule.decision.decision_data_gen import DecisionData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "logger_class", 
            "isCurrent": false
        }, 
        {
            "namespace": "instance", 
            "isCurrent": false
        }, 
        {
            "namespace": "rule", 
            "isCurrent": false
        }, 
        {
            "namespace": "decision", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "logBacktrace", 
            "yangName": "log-backtrace", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "ignoreCondition", 
            "yangName": "ignore-condition", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "log", 
            "yangName": "log", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "pass-through", 
            "hasDefaultRef": false
        }
    ], 
    "module": {}, 
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
    "createTime": "2013"
}
"""


