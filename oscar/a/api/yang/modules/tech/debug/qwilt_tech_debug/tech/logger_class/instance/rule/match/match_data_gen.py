


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import LogSeverity
from a.api.yang.modules.tech.debug.qwilt_tech_debug.qwilt_tech_debug_module_gen import MatchBoolean


class MatchData(object):

    def __init__ (self):

        self.minSeverity = LogSeverity.kAny
        self._myHasMinSeverity=False
        
        self.function = ""
        self._myHasFunction=False
        
        self.messageName = ""
        self._myHasMessageName=False
        
        self.group = ""
        self._myHasGroup=False
        
        self.maxLine = 0
        self._myHasMaxLine=False
        
        self.minLine = 0
        self._myHasMinLine=False
        
        self.module = ""
        self._myHasModule=False
        
        self.file = ""
        self._myHasFile=False
        
        self.conditional = MatchBoolean.kAny
        self._myHasConditional=False
        
        self.maxSeverity = LogSeverity.kAny
        self._myHasMaxSeverity=False
        

    def copyFrom (self, other):

        self.minSeverity=other.minSeverity
        self._myHasMinSeverity=other._myHasMinSeverity
        
        self.function=other.function
        self._myHasFunction=other._myHasFunction
        
        self.messageName=other.messageName
        self._myHasMessageName=other._myHasMessageName
        
        self.group=other.group
        self._myHasGroup=other._myHasGroup
        
        self.maxLine=other.maxLine
        self._myHasMaxLine=other._myHasMaxLine
        
        self.minLine=other.minLine
        self._myHasMinLine=other._myHasMinLine
        
        self.module=other.module
        self._myHasModule=other._myHasModule
        
        self.file=other.file
        self._myHasFile=other._myHasFile
        
        self.conditional=other.conditional
        self._myHasConditional=other._myHasConditional
        
        self.maxSeverity=other.maxSeverity
        self._myHasMaxSeverity=other._myHasMaxSeverity
        
    # has...() methods

    def hasMinSeverity (self):
        return self._myHasMinSeverity

    def hasFunction (self):
        return self._myHasFunction

    def hasMessageName (self):
        return self._myHasMessageName

    def hasGroup (self):
        return self._myHasGroup

    def hasMaxLine (self):
        return self._myHasMaxLine

    def hasMinLine (self):
        return self._myHasMinLine

    def hasModule (self):
        return self._myHasModule

    def hasFile (self):
        return self._myHasFile

    def hasConditional (self):
        return self._myHasConditional

    def hasMaxSeverity (self):
        return self._myHasMaxSeverity


    # setHas...() methods

    def setHasMinSeverity (self):
        self._myHasMinSeverity=True

    def setHasFunction (self):
        self._myHasFunction=True

    def setHasMessageName (self):
        self._myHasMessageName=True

    def setHasGroup (self):
        self._myHasGroup=True

    def setHasMaxLine (self):
        self._myHasMaxLine=True

    def setHasMinLine (self):
        self._myHasMinLine=True

    def setHasModule (self):
        self._myHasModule=True

    def setHasFile (self):
        self._myHasFile=True

    def setHasConditional (self):
        self._myHasConditional=True

    def setHasMaxSeverity (self):
        self._myHasMaxSeverity=True


    def clearAllHas (self):

        self._myHasMinSeverity=False

        self._myHasFunction=False

        self._myHasMessageName=False

        self._myHasGroup=False

        self._myHasMaxLine=False

        self._myHasMinLine=False

        self._myHasModule=False

        self._myHasFile=False

        self._myHasConditional=False

        self._myHasMaxSeverity=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasMinSeverity:
            x = "+"
        leafStr = str(self.minSeverity)
        items.append(x + "MinSeverity="+leafStr)

        x=""
        if self._myHasFunction:
            x = "+"
        leafStr = str(self.function)
        items.append(x + "Function="+leafStr)

        x=""
        if self._myHasMessageName:
            x = "+"
        leafStr = str(self.messageName)
        items.append(x + "MessageName="+leafStr)

        x=""
        if self._myHasGroup:
            x = "+"
        leafStr = str(self.group)
        items.append(x + "Group="+leafStr)

        x=""
        if self._myHasMaxLine:
            x = "+"
        leafStr = str(self.maxLine)
        items.append(x + "MaxLine="+leafStr)

        x=""
        if self._myHasMinLine:
            x = "+"
        leafStr = str(self.minLine)
        items.append(x + "MinLine="+leafStr)

        x=""
        if self._myHasModule:
            x = "+"
        leafStr = str(self.module)
        items.append(x + "Module="+leafStr)

        x=""
        if self._myHasFile:
            x = "+"
        leafStr = str(self.file)
        items.append(x + "File="+leafStr)

        x=""
        if self._myHasConditional:
            x = "+"
        leafStr = str(self.conditional)
        items.append(x + "Conditional="+leafStr)

        x=""
        if self._myHasMaxSeverity:
            x = "+"
        leafStr = str(self.maxSeverity)
        items.append(x + "MaxSeverity="+leafStr)

        return "{MatchData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "MatchData", 
        "namespace": "match", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.rule.match.match_data_gen import MatchData"
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
            "namespace": "match", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "minSeverity", 
            "yangName": "min-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "function", 
            "yangName": "function", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "messageName", 
            "yangName": "message-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "group", 
            "yangName": "group", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxLine", 
            "yangName": "max-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "minLine", 
            "yangName": "min-line", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "module", 
            "yangName": "module", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "file", 
            "yangName": "file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "conditional", 
            "yangName": "conditional", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "maxSeverity", 
            "yangName": "max-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "any", 
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


