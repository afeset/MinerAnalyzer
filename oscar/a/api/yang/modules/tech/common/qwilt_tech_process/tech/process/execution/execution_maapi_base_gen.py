


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ExecutionMaapiBase(object):
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



    # descendants

    # status
    def newStatus (self):
        raise NotImplementedError()

    def setStatusObj (self, obj):
        raise NotImplementedError()

    def getStatusObj (self):
        raise NotImplementedError()

    def hasStatus (self):
        raise NotImplementedError()

    # command
    def newCommand (self):
        raise NotImplementedError()

    def setCommandObj (self, obj):
        raise NotImplementedError()

    def getCommandObj (self):
        raise NotImplementedError()

    def hasCommand (self):
        raise NotImplementedError()




    # config leaves

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

    # umask
    def requestUmask (self, requested):
        raise NotImplementedError()

    def isUmaskRequested (self):
        raise NotImplementedError()

    def getUmask (self):
        raise NotImplementedError()

    def hasUmask (self):
        raise NotImplementedError()

    def setUmask (self, umask):
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






"""
Extracted from the below data: 
{
    "node": {
        "name": "execution", 
        "namespace": "execution", 
        "className": "ExecutionMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.execution_maapi_gen import ExecutionMaapi", 
        "baseClassName": "ExecutionMaapiBase", 
        "baseModule": "execution_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "name": "execution"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "memberName": "status", 
            "yangName": "status", 
            "className": "BlinkyStatusMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.status_maapi_gen import BlinkyStatusMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "memberName": "command", 
            "yangName": "command", 
            "className": "BlinkyCommandMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.command.command_maapi_gen import BlinkyCommandMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "umask", 
            "yangName": "umask", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "umask", 
            "yangName": "umask", 
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
        }
    ], 
    "createTime": "2013"
}
"""


