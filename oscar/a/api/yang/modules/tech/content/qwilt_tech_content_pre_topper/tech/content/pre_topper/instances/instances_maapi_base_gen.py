


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class InstancesMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , instances
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , instances
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , instances
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # warnTotalRecordCount
    def requestWarnTotalRecordCount (self, requested):
        raise NotImplementedError()

    def isWarnTotalRecordCountRequested (self):
        raise NotImplementedError()

    def getWarnTotalRecordCount (self):
        raise NotImplementedError()

    def hasWarnTotalRecordCount (self):
        raise NotImplementedError()

    def setWarnTotalRecordCount (self, warnTotalRecordCount):
        raise NotImplementedError()

    # periodicWorkRecordCount
    def requestPeriodicWorkRecordCount (self, requested):
        raise NotImplementedError()

    def isPeriodicWorkRecordCountRequested (self):
        raise NotImplementedError()

    def getPeriodicWorkRecordCount (self):
        raise NotImplementedError()

    def hasPeriodicWorkRecordCount (self):
        raise NotImplementedError()

    def setPeriodicWorkRecordCount (self, periodicWorkRecordCount):
        raise NotImplementedError()

    # aggregationPeriod
    def requestAggregationPeriod (self, requested):
        raise NotImplementedError()

    def isAggregationPeriodRequested (self):
        raise NotImplementedError()

    def getAggregationPeriod (self):
        raise NotImplementedError()

    def hasAggregationPeriod (self):
        raise NotImplementedError()

    def setAggregationPeriod (self, aggregationPeriod):
        raise NotImplementedError()

    # maxTotalRecordCount
    def requestMaxTotalRecordCount (self, requested):
        raise NotImplementedError()

    def isMaxTotalRecordCountRequested (self):
        raise NotImplementedError()

    def getMaxTotalRecordCount (self):
        raise NotImplementedError()

    def hasMaxTotalRecordCount (self):
        raise NotImplementedError()

    def setMaxTotalRecordCount (self, maxTotalRecordCount):
        raise NotImplementedError()

    # periodicWorkInterval
    def requestPeriodicWorkInterval (self, requested):
        raise NotImplementedError()

    def isPeriodicWorkIntervalRequested (self):
        raise NotImplementedError()

    def getPeriodicWorkInterval (self):
        raise NotImplementedError()

    def hasPeriodicWorkInterval (self):
        raise NotImplementedError()

    def setPeriodicWorkInterval (self, periodicWorkInterval):
        raise NotImplementedError()

    # warnSessionIdCount
    def requestWarnSessionIdCount (self, requested):
        raise NotImplementedError()

    def isWarnSessionIdCountRequested (self):
        raise NotImplementedError()

    def getWarnSessionIdCount (self):
        raise NotImplementedError()

    def hasWarnSessionIdCount (self):
        raise NotImplementedError()

    def setWarnSessionIdCount (self, warnSessionIdCount):
        raise NotImplementedError()

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

    # maxSessionIdCount
    def requestMaxSessionIdCount (self, requested):
        raise NotImplementedError()

    def isMaxSessionIdCountRequested (self):
        raise NotImplementedError()

    def getMaxSessionIdCount (self):
        raise NotImplementedError()

    def hasMaxSessionIdCount (self):
        raise NotImplementedError()

    def setMaxSessionIdCount (self, maxSessionIdCount):
        raise NotImplementedError()

    # rotateFileInterval
    def requestRotateFileInterval (self, requested):
        raise NotImplementedError()

    def isRotateFileIntervalRequested (self):
        raise NotImplementedError()

    def getRotateFileInterval (self):
        raise NotImplementedError()

    def hasRotateFileInterval (self):
        raise NotImplementedError()

    def setRotateFileInterval (self, rotateFileInterval):
        raise NotImplementedError()

    # recordWriteInterval
    def requestRecordWriteInterval (self, requested):
        raise NotImplementedError()

    def isRecordWriteIntervalRequested (self):
        raise NotImplementedError()

    def getRecordWriteInterval (self):
        raise NotImplementedError()

    def hasRecordWriteInterval (self):
        raise NotImplementedError()

    def setRecordWriteInterval (self, recordWriteInterval):
        raise NotImplementedError()

    # archive
    def requestArchive (self, requested):
        raise NotImplementedError()

    def isArchiveRequested (self):
        raise NotImplementedError()

    def getArchive (self):
        raise NotImplementedError()

    def hasArchive (self):
        raise NotImplementedError()

    def setArchive (self, archive):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "instances", 
        "namespace": "instances", 
        "className": "InstancesMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_pre_topper.tech.content.pre_topper.instances.instances_maapi_gen import InstancesMaapi", 
        "baseClassName": "InstancesMaapiBase", 
        "baseModule": "instances_maapi_base_gen"
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
                "defaultVal": null, 
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


