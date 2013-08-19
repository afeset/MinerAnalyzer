


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class StatusMaapiBase(object):
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

    # queueUtilizationPercent
    def requestQueueUtilizationPercent (self, requested):
        raise NotImplementedError()

    def isQueueUtilizationPercentRequested (self):
        raise NotImplementedError()

    def getQueueUtilizationPercent (self):
        raise NotImplementedError()

    def hasQueueUtilizationPercent (self):
        raise NotImplementedError()

    def setQueueUtilizationPercent (self, queueUtilizationPercent):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "status", 
        "namespace": "status", 
        "className": "StatusMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.status.status_maapi_gen import StatusMaapi", 
        "baseClassName": "StatusMaapiBase", 
        "baseModule": "status_maapi_base_gen"
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
            "yangName": "status", 
            "namespace": "status", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "name": "status"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-reporting", 
            "moduleYangNamespacePrefix": "qtc-report", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueUtilizationPercent", 
            "yangName": "queue-utilization-percent", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueUtilizationPercent", 
            "yangName": "queue-utilization-percent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


