


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ProcessMaapiBase(object):
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

    # execution
    def newExecution (self):
        raise NotImplementedError()

    def setExecutionObj (self, obj):
        raise NotImplementedError()

    def getExecutionObj (self):
        raise NotImplementedError()

    def hasExecution (self):
        raise NotImplementedError()




    # config leaves

    # enabled
    def requestEnabled (self, requested):
        raise NotImplementedError()

    def isEnabledRequested (self):
        raise NotImplementedError()

    def getEnabled (self):
        raise NotImplementedError()

    def hasEnabled (self):
        raise NotImplementedError()

    def setEnabled (self, enabled):
        raise NotImplementedError()

    # name
    def requestName (self, requested):
        raise NotImplementedError()

    def isNameRequested (self):
        raise NotImplementedError()

    def getName (self):
        raise NotImplementedError()

    def hasName (self):
        raise NotImplementedError()

    def setName (self, name):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "process", 
        "namespace": "process", 
        "className": "ProcessMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.process_maapi_gen import ProcessMaapi", 
        "baseClassName": "ProcessMaapiBase", 
        "baseModule": "process_maapi_base_gen"
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
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-proc", 
            "memberName": "execution", 
            "yangName": "execution", 
            "className": "BlinkyExecutionMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.execution_maapi_gen import BlinkyExecutionMaapi", 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


