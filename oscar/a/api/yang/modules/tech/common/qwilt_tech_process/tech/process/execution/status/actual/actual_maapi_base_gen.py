


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ActualMaapiBase(object):
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







    # oper leaves

    # priority
    def requestPriority (self, requested):
        raise NotImplementedError()

    def isPriorityRequested (self):
        raise NotImplementedError()

    def getPriority (self):
        raise NotImplementedError()

    def hasPriority (self):
        raise NotImplementedError()

    def setPriority (self, priority):
        raise NotImplementedError()

    # affinity
    def requestAffinity (self, requested):
        raise NotImplementedError()

    def isAffinityRequested (self):
        raise NotImplementedError()

    def getAffinity (self):
        raise NotImplementedError()

    def hasAffinity (self):
        raise NotImplementedError()

    def setAffinity (self, affinity):
        raise NotImplementedError()

    # commandLine
    def requestCommandLine (self, requested):
        raise NotImplementedError()

    def isCommandLineRequested (self):
        raise NotImplementedError()

    def getCommandLine (self):
        raise NotImplementedError()

    def hasCommandLine (self):
        raise NotImplementedError()

    def setCommandLine (self, commandLine):
        raise NotImplementedError()




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


