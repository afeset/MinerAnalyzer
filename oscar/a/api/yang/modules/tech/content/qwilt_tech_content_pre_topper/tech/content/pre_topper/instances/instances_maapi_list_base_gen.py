


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class InstancesMaapiListBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def newInstances (self):
        raise NotImplementedError()

    def setInstancesObj (self, key, instancesObj):
        raise NotImplementedError()

    def getInstancesObj (self, key):
        raise NotImplementedError()

    def deleteInstances (self, key):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def getListKeys (self):
        raise NotImplementedError()

    def readListKeys (self
                      
                      , trxContext=None):
        raise NotImplementedError()

    def write (self
               , trxContext=None
               ):
        raise NotImplementedError()

    def read (self
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       
                       , trxContext=None):
        raise NotImplementedError()


"""
Extracted from the below data: 
{
    "node": {
        "containerClassName": "BlinkyInstancesMaapi", 
        "name": "instances", 
        "keyLeaf": {
            "varName": "instances", 
            "yangName": "instance", 
            "typeHandler": "handler: StringHandler"
        }, 
        "yangName": "instances", 
        "namespace": "instances", 
        "moduleYangNamespacePrefix": "qtc-pt", 
        "className": "InstancesMaapiList", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_pre_topper.tech.content.pre_topper.instances.instances_maapi_list_gen import InstancesMaapiList", 
        "baseClassName": "InstancesMaapiListBase", 
        "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
        "containerModule": "instances_maapi_gen", 
        "baseModule": "instances_maapi_list_base_gen"
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
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "content", 
            "namespace": "content", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-pt", 
            "yangName": "pre-topper", 
            "namespace": "pre_topper", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "name": "pre-topper"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-pt", 
            "isCurrent": true, 
            "yangName": "instances", 
            "namespace": "instances", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "keyLeaf": {
                "varName": "instances", 
                "yangName": "instance", 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "instances"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnTotalRecordCount", 
            "yangName": "warn-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkRecordCount", 
            "yangName": "periodic-work-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "aggregationPeriod", 
            "yangName": "aggregation-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxTotalRecordCount", 
            "yangName": "max-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkInterval", 
            "yangName": "periodic-work-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnSessionIdCount", 
            "yangName": "warn-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "instance", 
            "yangName": "instance", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessionIdCount", 
            "yangName": "max-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rotateFileInterval", 
            "yangName": "rotate-file-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "recordWriteInterval", 
            "yangName": "record-write-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "archive", 
            "yangName": "archive", 
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
            "content", 
            "qwilt_tech_content_pre_topper"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnTotalRecordCount", 
            "yangName": "warn-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkRecordCount", 
            "yangName": "periodic-work-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "aggregationPeriod", 
            "yangName": "aggregation-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxTotalRecordCount", 
            "yangName": "max-total-record-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "periodicWorkInterval", 
            "yangName": "periodic-work-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "warnSessionIdCount", 
            "yangName": "warn-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "instance", 
            "yangName": "instance", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "maxSessionIdCount", 
            "yangName": "max-session-id-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "rotateFileInterval", 
            "yangName": "rotate-file-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "recordWriteInterval", 
            "yangName": "record-write-interval", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-pre-topper", 
            "moduleYangNamespacePrefix": "qtc-pt", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "archive", 
            "yangName": "archive", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


