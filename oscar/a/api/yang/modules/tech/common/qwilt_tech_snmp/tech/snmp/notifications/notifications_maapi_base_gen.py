


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class NotificationsMaapiBase(object):
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

    # destinationList
    def newDestinationList (self):
        raise NotImplementedError()

    def setDestinationListObj (self, obj):
        raise NotImplementedError()

    def getDestinationListObj (self):
        raise NotImplementedError()

    def hasDestinationList (self):
        raise NotImplementedError()








"""
Extracted from the below data: 
{
    "node": {
        "name": "notifications", 
        "namespace": "notifications", 
        "className": "NotificationsMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.notifications.notifications_maapi_gen import NotificationsMaapi", 
        "baseClassName": "NotificationsMaapiBase", 
        "baseModule": "notifications_maapi_base_gen"
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
            "moduleYangNamespacePrefix": "qt-snmp", 
            "yangName": "snmp", 
            "namespace": "snmp", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "snmp"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "yangName": "notifications", 
            "namespace": "notifications", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "notifications"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-snmp", 
            "memberName": "destinationList", 
            "yangName": "destination", 
            "className": "BlinkyDestinationMaapiList", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.notifications.destination.destination_maapi_list_gen import BlinkyDestinationMaapiList", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
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
            "qwilt_tech_snmp"
        ]
    }, 
    "leaves": [], 
    "createTime": "2013"
}
"""


