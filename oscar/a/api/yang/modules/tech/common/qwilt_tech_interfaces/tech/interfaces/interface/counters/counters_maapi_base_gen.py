


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







    # oper leaves

    # outGratuitousArpPackets
    def requestOutGratuitousArpPackets (self, requested):
        raise NotImplementedError()

    def isOutGratuitousArpPacketsRequested (self):
        raise NotImplementedError()

    def getOutGratuitousArpPackets (self):
        raise NotImplementedError()

    def hasOutGratuitousArpPackets (self):
        raise NotImplementedError()

    def setOutGratuitousArpPackets (self, outGratuitousArpPackets):
        raise NotImplementedError()

    # outUnicastPackets
    def requestOutUnicastPackets (self, requested):
        raise NotImplementedError()

    def isOutUnicastPacketsRequested (self):
        raise NotImplementedError()

    def getOutUnicastPackets (self):
        raise NotImplementedError()

    def hasOutUnicastPackets (self):
        raise NotImplementedError()

    def setOutUnicastPackets (self, outUnicastPackets):
        raise NotImplementedError()

    # inUnknownProtocolPackets
    def requestInUnknownProtocolPackets (self, requested):
        raise NotImplementedError()

    def isInUnknownProtocolPacketsRequested (self):
        raise NotImplementedError()

    def getInUnknownProtocolPackets (self):
        raise NotImplementedError()

    def hasInUnknownProtocolPackets (self):
        raise NotImplementedError()

    def setInUnknownProtocolPackets (self, inUnknownProtocolPackets):
        raise NotImplementedError()

    # outDiscardPackets
    def requestOutDiscardPackets (self, requested):
        raise NotImplementedError()

    def isOutDiscardPacketsRequested (self):
        raise NotImplementedError()

    def getOutDiscardPackets (self):
        raise NotImplementedError()

    def hasOutDiscardPackets (self):
        raise NotImplementedError()

    def setOutDiscardPackets (self, outDiscardPackets):
        raise NotImplementedError()

    # inOctets
    def requestInOctets (self, requested):
        raise NotImplementedError()

    def isInOctetsRequested (self):
        raise NotImplementedError()

    def getInOctets (self):
        raise NotImplementedError()

    def hasInOctets (self):
        raise NotImplementedError()

    def setInOctets (self, inOctets):
        raise NotImplementedError()

    # inErrorPackets
    def requestInErrorPackets (self, requested):
        raise NotImplementedError()

    def isInErrorPacketsRequested (self):
        raise NotImplementedError()

    def getInErrorPackets (self):
        raise NotImplementedError()

    def hasInErrorPackets (self):
        raise NotImplementedError()

    def setInErrorPackets (self, inErrorPackets):
        raise NotImplementedError()

    # inPacketsRate
    def requestInPacketsRate (self, requested):
        raise NotImplementedError()

    def isInPacketsRateRequested (self):
        raise NotImplementedError()

    def getInPacketsRate (self):
        raise NotImplementedError()

    def hasInPacketsRate (self):
        raise NotImplementedError()

    def setInPacketsRate (self, inPacketsRate):
        raise NotImplementedError()

    # outPackets
    def requestOutPackets (self, requested):
        raise NotImplementedError()

    def isOutPacketsRequested (self):
        raise NotImplementedError()

    def getOutPackets (self):
        raise NotImplementedError()

    def hasOutPackets (self):
        raise NotImplementedError()

    def setOutPackets (self, outPackets):
        raise NotImplementedError()

    # inDiscardPackets
    def requestInDiscardPackets (self, requested):
        raise NotImplementedError()

    def isInDiscardPacketsRequested (self):
        raise NotImplementedError()

    def getInDiscardPackets (self):
        raise NotImplementedError()

    def hasInDiscardPackets (self):
        raise NotImplementedError()

    def setInDiscardPackets (self, inDiscardPackets):
        raise NotImplementedError()

    # inMulticastPackets
    def requestInMulticastPackets (self, requested):
        raise NotImplementedError()

    def isInMulticastPacketsRequested (self):
        raise NotImplementedError()

    def getInMulticastPackets (self):
        raise NotImplementedError()

    def hasInMulticastPackets (self):
        raise NotImplementedError()

    def setInMulticastPackets (self, inMulticastPackets):
        raise NotImplementedError()

    # outBroadcastPackets
    def requestOutBroadcastPackets (self, requested):
        raise NotImplementedError()

    def isOutBroadcastPacketsRequested (self):
        raise NotImplementedError()

    def getOutBroadcastPackets (self):
        raise NotImplementedError()

    def hasOutBroadcastPackets (self):
        raise NotImplementedError()

    def setOutBroadcastPackets (self, outBroadcastPackets):
        raise NotImplementedError()

    # outOctets
    def requestOutOctets (self, requested):
        raise NotImplementedError()

    def isOutOctetsRequested (self):
        raise NotImplementedError()

    def getOutOctets (self):
        raise NotImplementedError()

    def hasOutOctets (self):
        raise NotImplementedError()

    def setOutOctets (self, outOctets):
        raise NotImplementedError()

    # outMulticastPackets
    def requestOutMulticastPackets (self, requested):
        raise NotImplementedError()

    def isOutMulticastPacketsRequested (self):
        raise NotImplementedError()

    def getOutMulticastPackets (self):
        raise NotImplementedError()

    def hasOutMulticastPackets (self):
        raise NotImplementedError()

    def setOutMulticastPackets (self, outMulticastPackets):
        raise NotImplementedError()

    # inUnicastPackets
    def requestInUnicastPackets (self, requested):
        raise NotImplementedError()

    def isInUnicastPacketsRequested (self):
        raise NotImplementedError()

    def getInUnicastPackets (self):
        raise NotImplementedError()

    def hasInUnicastPackets (self):
        raise NotImplementedError()

    def setInUnicastPackets (self, inUnicastPackets):
        raise NotImplementedError()

    # outErrorPackets
    def requestOutErrorPackets (self, requested):
        raise NotImplementedError()

    def isOutErrorPacketsRequested (self):
        raise NotImplementedError()

    def getOutErrorPackets (self):
        raise NotImplementedError()

    def hasOutErrorPackets (self):
        raise NotImplementedError()

    def setOutErrorPackets (self, outErrorPackets):
        raise NotImplementedError()

    # outPacketsRate
    def requestOutPacketsRate (self, requested):
        raise NotImplementedError()

    def isOutPacketsRateRequested (self):
        raise NotImplementedError()

    def getOutPacketsRate (self):
        raise NotImplementedError()

    def hasOutPacketsRate (self):
        raise NotImplementedError()

    def setOutPacketsRate (self, outPacketsRate):
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

    # operationalStatusChanges
    def requestOperationalStatusChanges (self, requested):
        raise NotImplementedError()

    def isOperationalStatusChangesRequested (self):
        raise NotImplementedError()

    def getOperationalStatusChanges (self):
        raise NotImplementedError()

    def hasOperationalStatusChanges (self):
        raise NotImplementedError()

    def setOperationalStatusChanges (self, operationalStatusChanges):
        raise NotImplementedError()

    # inBitsRate
    def requestInBitsRate (self, requested):
        raise NotImplementedError()

    def isInBitsRateRequested (self):
        raise NotImplementedError()

    def getInBitsRate (self):
        raise NotImplementedError()

    def hasInBitsRate (self):
        raise NotImplementedError()

    def setInBitsRate (self, inBitsRate):
        raise NotImplementedError()

    # outBitsRate
    def requestOutBitsRate (self, requested):
        raise NotImplementedError()

    def isOutBitsRateRequested (self):
        raise NotImplementedError()

    def getOutBitsRate (self):
        raise NotImplementedError()

    def hasOutBitsRate (self):
        raise NotImplementedError()

    def setOutBitsRate (self, outBitsRate):
        raise NotImplementedError()

    # inBroadcastPackets
    def requestInBroadcastPackets (self, requested):
        raise NotImplementedError()

    def isInBroadcastPacketsRequested (self):
        raise NotImplementedError()

    def getInBroadcastPackets (self):
        raise NotImplementedError()

    def hasInBroadcastPackets (self):
        raise NotImplementedError()

    def setInBroadcastPackets (self, inBroadcastPackets):
        raise NotImplementedError()




"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.counters.counters_maapi_gen import CountersMaapi", 
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
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outGratuitousArpPackets", 
            "yangName": "out-gratuitous-arp-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outUnicastPackets", 
            "yangName": "out-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnknownProtocolPackets", 
            "yangName": "in-unknown-protocol-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outDiscardPackets", 
            "yangName": "out-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inOctets", 
            "yangName": "in-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inErrorPackets", 
            "yangName": "in-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPacketsRate", 
            "yangName": "in-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPackets", 
            "yangName": "out-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inDiscardPackets", 
            "yangName": "in-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inMulticastPackets", 
            "yangName": "in-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBroadcastPackets", 
            "yangName": "out-broadcast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outOctets", 
            "yangName": "out-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outMulticastPackets", 
            "yangName": "out-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnicastPackets", 
            "yangName": "in-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outErrorPackets", 
            "yangName": "out-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPacketsRate", 
            "yangName": "out-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPackets", 
            "yangName": "in-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "operationalStatusChanges", 
            "yangName": "operational-status-changes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBitsRate", 
            "yangName": "in-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBitsRate", 
            "yangName": "out-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBroadcastPackets", 
            "yangName": "in-broadcast-packets", 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outGratuitousArpPackets", 
            "yangName": "out-gratuitous-arp-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outUnicastPackets", 
            "yangName": "out-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnknownProtocolPackets", 
            "yangName": "in-unknown-protocol-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outDiscardPackets", 
            "yangName": "out-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inOctets", 
            "yangName": "in-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inErrorPackets", 
            "yangName": "in-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPacketsRate", 
            "yangName": "in-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPackets", 
            "yangName": "out-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inDiscardPackets", 
            "yangName": "in-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inMulticastPackets", 
            "yangName": "in-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBroadcastPackets", 
            "yangName": "out-broadcast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outOctets", 
            "yangName": "out-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outMulticastPackets", 
            "yangName": "out-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnicastPackets", 
            "yangName": "in-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outErrorPackets", 
            "yangName": "out-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPacketsRate", 
            "yangName": "out-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPackets", 
            "yangName": "in-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "operationalStatusChanges", 
            "yangName": "operational-status-changes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBitsRate", 
            "yangName": "in-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBitsRate", 
            "yangName": "out-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBroadcastPackets", 
            "yangName": "in-broadcast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


