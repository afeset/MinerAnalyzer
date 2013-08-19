


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class CommandData(object):

    def __init__ (self):

        self.executable = ""
        self._myHasExecutable=False
        
        self.shell = False
        self._myHasShell=False
        
        self.extraArgs = ""
        self._myHasExtraArgs=False
        
        self.args = ""
        self._myHasArgs=False
        
        self.valgrind = False
        self._myHasValgrind=False
        

    def copyFrom (self, other):

        self.executable=other.executable
        self._myHasExecutable=other._myHasExecutable
        
        self.shell=other.shell
        self._myHasShell=other._myHasShell
        
        self.extraArgs=other.extraArgs
        self._myHasExtraArgs=other._myHasExtraArgs
        
        self.args=other.args
        self._myHasArgs=other._myHasArgs
        
        self.valgrind=other.valgrind
        self._myHasValgrind=other._myHasValgrind
        
    # has...() methods

    def hasExecutable (self):
        return self._myHasExecutable

    def hasShell (self):
        return self._myHasShell

    def hasExtraArgs (self):
        return self._myHasExtraArgs

    def hasArgs (self):
        return self._myHasArgs

    def hasValgrind (self):
        return self._myHasValgrind


    # setHas...() methods

    def setHasExecutable (self):
        self._myHasExecutable=True

    def setHasShell (self):
        self._myHasShell=True

    def setHasExtraArgs (self):
        self._myHasExtraArgs=True

    def setHasArgs (self):
        self._myHasArgs=True

    def setHasValgrind (self):
        self._myHasValgrind=True


    def clearAllHas (self):

        self._myHasExecutable=False

        self._myHasShell=False

        self._myHasExtraArgs=False

        self._myHasArgs=False

        self._myHasValgrind=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasExecutable:
            x = "+"
        leafStr = str(self.executable)
        items.append(x + "Executable="+leafStr)

        x=""
        if self._myHasShell:
            x = "+"
        leafStr = str(self.shell)
        items.append(x + "Shell="+leafStr)

        x=""
        if self._myHasExtraArgs:
            x = "+"
        leafStr = str(self.extraArgs)
        items.append(x + "ExtraArgs="+leafStr)

        x=""
        if self._myHasArgs:
            x = "+"
        leafStr = str(self.args)
        items.append(x + "Args="+leafStr)

        x=""
        if self._myHasValgrind:
            x = "+"
        leafStr = str(self.valgrind)
        items.append(x + "Valgrind="+leafStr)

        return "{CommandData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "CommandData", 
        "namespace": "command", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.command.command_data_gen import CommandData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "process", 
            "isCurrent": false
        }, 
        {
            "namespace": "execution", 
            "isCurrent": false
        }, 
        {
            "namespace": "command", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "executable", 
            "yangName": "executable", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shell", 
            "yangName": "shell", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "extraArgs", 
            "yangName": "extra-args", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "args", 
            "yangName": "args", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "valgrind", 
            "yangName": "valgrind", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "common", 
            "qwilt_tech_process"
        ]
    }, 
    "createTime": "2013"
}
"""


