


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class RuleMaapiBase(object):
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



    # descendants

    # destinationZoneList
    def newDestinationZoneList (self):
        raise NotImplementedError()

    def setDestinationZoneListObj (self, obj):
        raise NotImplementedError()

    def getDestinationZoneListObj (self):
        raise NotImplementedError()

    def hasDestinationZoneList (self):
        raise NotImplementedError()

    # siteList
    def newSiteList (self):
        raise NotImplementedError()

    def setSiteListObj (self, obj):
        raise NotImplementedError()

    def getSiteListObj (self):
        raise NotImplementedError()

    def hasSiteList (self):
        raise NotImplementedError()

    # actions
    def newActions (self):
        raise NotImplementedError()

    def setActionsObj (self, obj):
        raise NotImplementedError()

    def getActionsObj (self):
        raise NotImplementedError()

    def hasActions (self):
        raise NotImplementedError()

    # sourceZoneList
    def newSourceZoneList (self):
        raise NotImplementedError()

    def setSourceZoneListObj (self, obj):
        raise NotImplementedError()

    def getSourceZoneListObj (self):
        raise NotImplementedError()

    def hasSourceZoneList (self):
        raise NotImplementedError()




    # config leaves

    # description
    def requestDescription (self, requested):
        raise NotImplementedError()

    def isDescriptionRequested (self):
        raise NotImplementedError()

    def getDescription (self):
        raise NotImplementedError()

    def hasDescription (self):
        raise NotImplementedError()

    def setDescription (self, description):
        raise NotImplementedError()

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

    # siteList
    def requestSiteList (self, requested):
        raise NotImplementedError()

    def isSiteListRequested (self):
        raise NotImplementedError()

    def getSiteList (self):
        raise NotImplementedError()

    def hasSiteList (self):
        raise NotImplementedError()

    def setSiteList (self, siteList):
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
        "name": "rule", 
        "namespace": "rule", 
        "className": "RuleMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.rule_maapi_gen import RuleMaapi", 
        "baseClassName": "RuleMaapiBase", 
        "baseModule": "rule_maapi_base_gen"
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
            "isCurrent": true, 
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
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "destinationZoneList", 
            "yangName": "destination-zone", 
            "className": "BlinkyDestinationZoneMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.destination_zone.destination_zone_maapi_list_gen import BlinkyDestinationZoneMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "siteList", 
            "yangName": "site", 
            "className": "BlinkySiteMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.site.site_maapi_list_gen import BlinkySiteMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "actions", 
            "yangName": "actions", 
            "className": "BlinkyActionsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.actions.actions_maapi_gen import BlinkyActionsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "sourceZoneList", 
            "yangName": "source-zone", 
            "className": "BlinkySourceZoneMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.source_zone.source_zone_maapi_list_gen import BlinkySourceZoneMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "siteList", 
            "yangName": "site-list", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "include", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
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
            "content", 
            "qwilt_tech_content"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "siteList", 
            "yangName": "site-list", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "include", 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "moduleYangNamespacePrefix": "qtc", 
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


