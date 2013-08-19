


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class DeliveryMaapiBase(object):
    def __init__ (self, logger):
        raise NotImplementedError()

    def init (self, domain):
        raise NotImplementedError()

    def requestConfigAndOper (self):
        raise NotImplementedError()

    def clearAllSet (self):
        raise NotImplementedError()

    def write (self
              , interface
              , trxContext=None
              ):
        raise NotImplementedError()

    def read (self
              , interface
              
              , trxContext=None):
        raise NotImplementedError()

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        raise NotImplementedError()



    # descendants

    # ipv4
    def newIpv4 (self):
        raise NotImplementedError()

    def setIpv4Obj (self, obj):
        raise NotImplementedError()

    def getIpv4Obj (self):
        raise NotImplementedError()

    def hasIpv4 (self):
        raise NotImplementedError()

    # ipv6
    def newIpv6 (self):
        raise NotImplementedError()

    def setIpv6Obj (self, obj):
        raise NotImplementedError()

    def getIpv6Obj (self):
        raise NotImplementedError()

    def hasIpv6 (self):
        raise NotImplementedError()




    # config leaves

    # preferredDeliveryInterface
    def requestPreferredDeliveryInterface (self, requested):
        raise NotImplementedError()

    def isPreferredDeliveryInterfaceRequested (self):
        raise NotImplementedError()

    def getPreferredDeliveryInterface (self):
        raise NotImplementedError()

    def hasPreferredDeliveryInterface (self):
        raise NotImplementedError()

    def setPreferredDeliveryInterface (self, preferredDeliveryInterface):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "delivery", 
        "namespace": "delivery", 
        "className": "DeliveryMaapi", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.delivery.delivery_maapi_gen import DeliveryMaapi", 
        "baseClassName": "DeliveryMaapiBase", 
        "baseModule": "delivery_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qtc-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-if", 
            "yangName": "delivery", 
            "namespace": "delivery", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "name": "delivery"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qtc-if", 
            "memberName": "ipv4", 
            "yangName": "ipv4", 
            "className": "BlinkyIpv4Maapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.delivery.ipv4.ipv4_maapi_gen import BlinkyIpv4Maapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qtc-if", 
            "memberName": "ipv6", 
            "yangName": "ipv6", 
            "className": "BlinkyIpv6Maapi", 
            "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.delivery.ipv6.ipv6_maapi_gen import BlinkyIpv6Maapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "moduleYangNamespacePrefix": "qtc-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "preferredDeliveryInterface", 
            "yangName": "preferred-delivery-interface", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "qwilt_tech_content_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-content-interfaces", 
            "moduleYangNamespacePrefix": "qtc-if", 
            "typeHandler": "handler: StringHandler", 
            "memberName": "preferredDeliveryInterface", 
            "yangName": "preferred-delivery-interface", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


