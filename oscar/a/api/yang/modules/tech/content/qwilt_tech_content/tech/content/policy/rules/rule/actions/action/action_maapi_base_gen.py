


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ActionMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , rule
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , rule
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , rule
                       
                       , trxContext=None):
        raise NotImplementedError()





    # config leaves

    # delivery
    def requestDelivery (self, requested):
        raise NotImplementedError()

    def isDeliveryRequested (self):
        raise NotImplementedError()

    def getDelivery (self):
        raise NotImplementedError()

    def hasDelivery (self):
        raise NotImplementedError()

    def setDelivery (self, delivery):
        raise NotImplementedError()

    # analytics
    def requestAnalytics (self, requested):
        raise NotImplementedError()

    def isAnalyticsRequested (self):
        raise NotImplementedError()

    def getAnalytics (self):
        raise NotImplementedError()

    def hasAnalytics (self):
        raise NotImplementedError()

    def setAnalytics (self, analytics):
        raise NotImplementedError()

    # cachingPotential
    def requestCachingPotential (self, requested):
        raise NotImplementedError()

    def isCachingPotentialRequested (self):
        raise NotImplementedError()

    def getCachingPotential (self):
        raise NotImplementedError()

    def hasCachingPotential (self):
        raise NotImplementedError()

    def setCachingPotential (self, cachingPotential):
        raise NotImplementedError()

    # acquisition
    def requestAcquisition (self, requested):
        raise NotImplementedError()

    def isAcquisitionRequested (self):
        raise NotImplementedError()

    def getAcquisition (self):
        raise NotImplementedError()

    def hasAcquisition (self):
        raise NotImplementedError()

    def setAcquisition (self, acquisition):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "action", 
        "namespace": "action", 
        "className": "ActionMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.actions.action.action_maapi_gen import ActionMaapi", 
        "baseClassName": "ActionMaapiBase", 
        "baseModule": "action_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "policy", 
            "namespace": "policy", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "policy"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "rules", 
            "namespace": "rules", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "rules"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "isCurrent": false, 
            "yangName": "rule", 
            "namespace": "rule", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "keyLeaf": {
                "varName": "rule", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "rule"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "actions", 
            "namespace": "actions", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "actions"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "yangName": "action", 
            "namespace": "action", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "action"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "delivery", 
            "yangName": "delivery", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "analytics", 
            "yangName": "analytics", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "cachingPotential", 
            "yangName": "caching-potential", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "acquisition", 
            "yangName": "acquisition", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
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
            "qwilt_tech_content"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "delivery", 
            "yangName": "delivery", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "analytics", 
            "yangName": "analytics", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "cachingPotential", 
            "yangName": "caching-potential", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "acquisition", 
            "yangName": "acquisition", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


