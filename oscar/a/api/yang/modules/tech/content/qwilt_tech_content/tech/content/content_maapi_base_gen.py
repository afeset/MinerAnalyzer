


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class ContentMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
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



    # descendants

    # delivery
    def newDelivery (self):
        raise NotImplementedError()

    def setDeliveryObj (self, obj):
        raise NotImplementedError()

    def getDeliveryObj (self):
        raise NotImplementedError()

    def hasDelivery (self):
        raise NotImplementedError()

    # signatures
    def newSignatures (self):
        raise NotImplementedError()

    def setSignaturesObj (self, obj):
        raise NotImplementedError()

    def getSignaturesObj (self):
        raise NotImplementedError()

    def hasSignatures (self):
        raise NotImplementedError()

    # zones
    def newZones (self):
        raise NotImplementedError()

    def setZonesObj (self, obj):
        raise NotImplementedError()

    def getZonesObj (self):
        raise NotImplementedError()

    def hasZones (self):
        raise NotImplementedError()

    # systemDefaults
    def newSystemDefaults (self):
        raise NotImplementedError()

    def setSystemDefaultsObj (self, obj):
        raise NotImplementedError()

    def getSystemDefaultsObj (self):
        raise NotImplementedError()

    def hasSystemDefaults (self):
        raise NotImplementedError()

    # policy
    def newPolicy (self):
        raise NotImplementedError()

    def setPolicyObj (self, obj):
        raise NotImplementedError()

    def getPolicyObj (self):
        raise NotImplementedError()

    def hasPolicy (self):
        raise NotImplementedError()




    # config leaves

    # tempJunkDescriptionType
    def requestTempJunkDescriptionType (self, requested):
        raise NotImplementedError()

    def isTempJunkDescriptionTypeRequested (self):
        raise NotImplementedError()

    def getTempJunkDescriptionType (self):
        raise NotImplementedError()

    def hasTempJunkDescriptionType (self):
        raise NotImplementedError()

    def setTempJunkDescriptionType (self, tempJunkDescriptionType):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "content", 
        "namespace": "content", 
        "className": "ContentMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.content_maapi_gen import ContentMaapi", 
        "baseClassName": "ContentMaapiBase", 
        "baseModule": "content_maapi_base_gen"
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
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content", 
            "name": "content"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "delivery", 
            "yangName": "delivery", 
            "className": "BlinkyDeliveryMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.delivery.delivery_maapi_gen import BlinkyDeliveryMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "signatures", 
            "yangName": "signatures", 
            "className": "BlinkySignaturesMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.signatures.signatures_maapi_gen import BlinkySignaturesMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "zones", 
            "yangName": "zones", 
            "className": "BlinkyZonesMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.zones.zones_maapi_gen import BlinkyZonesMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "systemDefaults", 
            "yangName": "system-defaults", 
            "className": "BlinkySystemDefaultsMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.system_defaults.system_defaults_maapi_gen import BlinkySystemDefaultsMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc", 
            "memberName": "policy", 
            "yangName": "policy", 
            "className": "BlinkyPolicyMaapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.policy_maapi_gen import BlinkyPolicyMaapi", 
            "isList": false, 
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
            "memberName": "tempJunkDescriptionType", 
            "yangName": "temp-junk-description-type", 
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
            "memberName": "tempJunkDescriptionType", 
            "yangName": "temp-junk-description-type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


