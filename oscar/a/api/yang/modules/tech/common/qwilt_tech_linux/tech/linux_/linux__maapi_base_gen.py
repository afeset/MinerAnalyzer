


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class LinuxMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , linux_
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , linux_
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , linux_
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # instance
    def requestInstance (self, requested):
        raise NotImplementedError()

    def isInstanceRequested (self):
        raise NotImplementedError()

    def getInstance (self):
        raise NotImplementedError()

    def hasInstance (self):
        raise NotImplementedError()

    def setInstance (self, instance):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "linux_", 
        "namespace": "linux_", 
        "className": "LinuxMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux.tech.linux_.linux__maapi_gen import LinuxMaapi", 
        "baseClassName": "LinuxMaapiBase", 
        "baseModule": "linux__maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-lnx", 
            "isCurrent": true, 
            "yangName": "linux", 
            "namespace": "linux_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux", 
            "keyLeaf": {
                "varName": "linux_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "linux_"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux", 
            "moduleYangNamespacePrefix": "qt-lnx", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "instance", 
            "yangName": "instance", 
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
            "qwilt_tech_linux"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-linux", 
            "moduleYangNamespacePrefix": "qt-lnx", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "instance", 
            "yangName": "instance", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


