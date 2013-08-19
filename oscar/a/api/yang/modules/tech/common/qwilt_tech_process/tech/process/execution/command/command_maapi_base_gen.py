


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class CommandMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , process
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , process
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , process
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # executable
    def requestExecutable (self, requested):
        raise NotImplementedError()

    def isExecutableRequested (self):
        raise NotImplementedError()

    def getExecutable (self):
        raise NotImplementedError()

    def hasExecutable (self):
        raise NotImplementedError()

    def setExecutable (self, executable):
        raise NotImplementedError()

    # shell
    def requestShell (self, requested):
        raise NotImplementedError()

    def isShellRequested (self):
        raise NotImplementedError()

    def getShell (self):
        raise NotImplementedError()

    def hasShell (self):
        raise NotImplementedError()

    def setShell (self, shell):
        raise NotImplementedError()

    # extraArgs
    def requestExtraArgs (self, requested):
        raise NotImplementedError()

    def isExtraArgsRequested (self):
        raise NotImplementedError()

    def getExtraArgs (self):
        raise NotImplementedError()

    def hasExtraArgs (self):
        raise NotImplementedError()

    def setExtraArgs (self, extraArgs):
        raise NotImplementedError()

    # args
    def requestArgs (self, requested):
        raise NotImplementedError()

    def isArgsRequested (self):
        raise NotImplementedError()

    def getArgs (self):
        raise NotImplementedError()

    def hasArgs (self):
        raise NotImplementedError()

    def setArgs (self, args):
        raise NotImplementedError()

    # valgrind
    def requestValgrind (self, requested):
        raise NotImplementedError()

    def isValgrindRequested (self):
        raise NotImplementedError()

    def getValgrind (self):
        raise NotImplementedError()

    def hasValgrind (self):
        raise NotImplementedError()

    def setValgrind (self, valgrind):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "command", 
        "namespace": "command", 
        "className": "CommandMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.command.command_maapi_gen import CommandMaapi", 
        "baseClassName": "CommandMaapiBase", 
        "baseModule": "command_maapi_base_gen"
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
            "yangName": "command", 
            "namespace": "command", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "name": "command"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "executable", 
            "yangName": "executable", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shell", 
            "yangName": "shell", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "extraArgs", 
            "yangName": "extra-args", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "args", 
            "yangName": "args", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "valgrind", 
            "yangName": "valgrind", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "common", 
            "qwilt_tech_process"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "executable", 
            "yangName": "executable", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "shell", 
            "yangName": "shell", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "extraArgs", 
            "yangName": "extra-args", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "args", 
            "yangName": "args", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "valgrind", 
            "yangName": "valgrind", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


