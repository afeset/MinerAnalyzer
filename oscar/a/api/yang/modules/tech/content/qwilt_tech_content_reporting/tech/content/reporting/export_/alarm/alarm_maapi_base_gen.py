


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class AlarmMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , export_
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , export_
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , export_
                       
                       , trxContext=None):
        raise NotImplementedError()







    # oper leaves

    # reportsQueueGettingFullReason
    def requestReportsQueueGettingFullReason (self, requested):
        raise NotImplementedError()

    def isReportsQueueGettingFullReasonRequested (self):
        raise NotImplementedError()

    def getReportsQueueGettingFullReason (self):
        raise NotImplementedError()

    def hasReportsQueueGettingFullReason (self):
        raise NotImplementedError()

    def setReportsQueueGettingFullReason (self, reportsQueueGettingFullReason):
        raise NotImplementedError()

    # reportsQueueGettingFull
    def requestReportsQueueGettingFull (self, requested):
        raise NotImplementedError()

    def isReportsQueueGettingFullRequested (self):
        raise NotImplementedError()

    def getReportsQueueGettingFull (self):
        raise NotImplementedError()

    def hasReportsQueueGettingFull (self):
        raise NotImplementedError()

    def setReportsQueueGettingFull (self, reportsQueueGettingFull):
        raise NotImplementedError()

    # reportsQueueFullReason
    def requestReportsQueueFullReason (self, requested):
        raise NotImplementedError()

    def isReportsQueueFullReasonRequested (self):
        raise NotImplementedError()

    def getReportsQueueFullReason (self):
        raise NotImplementedError()

    def hasReportsQueueFullReason (self):
        raise NotImplementedError()

    def setReportsQueueFullReason (self, reportsQueueFullReason):
        raise NotImplementedError()

    # reportsQueueFull
    def requestReportsQueueFull (self, requested):
        raise NotImplementedError()

    def isReportsQueueFullRequested (self):
        raise NotImplementedError()

    def getReportsQueueFull (self):
        raise NotImplementedError()

    def hasReportsQueueFull (self):
        raise NotImplementedError()

    def setReportsQueueFull (self, reportsQueueFull):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "alarm", 
        "namespace": "alarm", 
        "className": "AlarmMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.alarm.alarm_maapi_gen import AlarmMaapi", 
        "baseClassName": "AlarmMaapiBase", 
        "baseModule": "alarm_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-report", 
            "yangName": "reporting", 
            "namespace": "reporting", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "name": "reporting"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-report", 
            "isCurrent": false, 
            "yangName": "export", 
            "namespace": "export_", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "keyLeaf": {
                "varName": "export_", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "export_"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-report", 
            "yangName": "alarm", 
            "namespace": "alarm", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "name": "alarm"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "reportsQueueGettingFullReason", 
            "yangName": "reports-queue-getting-full-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "reportsQueueGettingFull", 
            "yangName": "reports-queue-getting-full", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "reportsQueueFullReason", 
            "yangName": "reports-queue-full-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "reportsQueueFull", 
            "yangName": "reports-queue-full", 
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
            "content", 
            "qwilt_tech_content_reporting"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "reportsQueueGettingFullReason", 
            "yangName": "reports-queue-getting-full-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "reportsQueueGettingFull", 
            "yangName": "reports-queue-getting-full", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "reportsQueueFullReason", 
            "yangName": "reports-queue-full-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "reportsQueueFull", 
            "yangName": "reports-queue-full", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


