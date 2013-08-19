


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class TempMemoryMaapiBase(object):
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

    # virtualSize
    def requestVirtualSize (self, requested):
        raise NotImplementedError()

    def isVirtualSizeRequested (self):
        raise NotImplementedError()

    def getVirtualSize (self):
        raise NotImplementedError()

    def hasVirtualSize (self):
        raise NotImplementedError()

    def setVirtualSize (self, virtualSize):
        raise NotImplementedError()

    # rssSize
    def requestRssSize (self, requested):
        raise NotImplementedError()

    def isRssSizeRequested (self):
        raise NotImplementedError()

    def getRssSize (self):
        raise NotImplementedError()

    def hasRssSize (self):
        raise NotImplementedError()

    def setRssSize (self, rssSize):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "tempMemory", 
        "namespace": "temp_memory", 
        "className": "TempMemoryMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.temp_memory.temp_memory_maapi_gen import TempMemoryMaapi", 
        "baseClassName": "TempMemoryMaapiBase", 
        "baseModule": "temp_memory_maapi_base_gen"
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
            "yangName": "temp-memory", 
            "namespace": "temp_memory", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "name": "temp-memory"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "virtualSize", 
            "yangName": "virtual-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rssSize", 
            "yangName": "rss-size", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "virtualSize", 
            "yangName": "virtual-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-process", 
            "moduleYangNamespacePrefix": "qt-proc", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rssSize", 
            "yangName": "rss-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


