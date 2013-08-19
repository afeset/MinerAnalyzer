


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class CountersMaapiBase(object):
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







    # oper leaves

    # silentDroppedPackets
    def requestSilentDroppedPackets (self, requested):
        raise NotImplementedError()

    def isSilentDroppedPacketsRequested (self):
        raise NotImplementedError()

    def getSilentDroppedPackets (self):
        raise NotImplementedError()

    def hasSilentDroppedPackets (self):
        raise NotImplementedError()

    def setSilentDroppedPackets (self, silentDroppedPackets):
        raise NotImplementedError()

    # inPackets
    def requestInPackets (self, requested):
        raise NotImplementedError()

    def isInPacketsRequested (self):
        raise NotImplementedError()

    def getInPackets (self):
        raise NotImplementedError()

    def hasInPackets (self):
        raise NotImplementedError()

    def setInPackets (self, inPackets):
        raise NotImplementedError()

    # inBadVersionPackets
    def requestInBadVersionPackets (self, requested):
        raise NotImplementedError()

    def isInBadVersionPacketsRequested (self):
        raise NotImplementedError()

    def getInBadVersionPackets (self):
        raise NotImplementedError()

    def hasInBadVersionPackets (self):
        raise NotImplementedError()

    def setInBadVersionPackets (self, inBadVersionPackets):
        raise NotImplementedError()

    # inBadCommunityUsePackets
    def requestInBadCommunityUsePackets (self, requested):
        raise NotImplementedError()

    def isInBadCommunityUsePacketsRequested (self):
        raise NotImplementedError()

    def getInBadCommunityUsePackets (self):
        raise NotImplementedError()

    def hasInBadCommunityUsePackets (self):
        raise NotImplementedError()

    def setInBadCommunityUsePackets (self, inBadCommunityUsePackets):
        raise NotImplementedError()

    # inAsnParseErrors
    def requestInAsnParseErrors (self, requested):
        raise NotImplementedError()

    def isInAsnParseErrorsRequested (self):
        raise NotImplementedError()

    def getInAsnParseErrors (self):
        raise NotImplementedError()

    def hasInAsnParseErrors (self):
        raise NotImplementedError()

    def setInAsnParseErrors (self, inAsnParseErrors):
        raise NotImplementedError()

    # inBadCommunityPackets
    def requestInBadCommunityPackets (self, requested):
        raise NotImplementedError()

    def isInBadCommunityPacketsRequested (self):
        raise NotImplementedError()

    def getInBadCommunityPackets (self):
        raise NotImplementedError()

    def hasInBadCommunityPackets (self):
        raise NotImplementedError()

    def setInBadCommunityPackets (self, inBadCommunityPackets):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
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
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "silentDroppedPackets", 
            "yangName": "silent-dropped-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPackets", 
            "yangName": "in-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadVersionPackets", 
            "yangName": "in-bad-version-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadCommunityUsePackets", 
            "yangName": "in-bad-community-use-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inAsnParseErrors", 
            "yangName": "in-asn-parse-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadCommunityPackets", 
            "yangName": "in-bad-community-packets", 
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
            "common", 
            "qwilt_tech_snmp"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "silentDroppedPackets", 
            "yangName": "silent-dropped-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPackets", 
            "yangName": "in-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadVersionPackets", 
            "yangName": "in-bad-version-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadCommunityUsePackets", 
            "yangName": "in-bad-community-use-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inAsnParseErrors", 
            "yangName": "in-asn-parse-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-snmp", 
            "moduleYangNamespacePrefix": "qt-snmp", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadCommunityPackets", 
            "yangName": "in-bad-community-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


