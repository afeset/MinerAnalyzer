


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.basic.return_codes import ReturnCodes

class LinkMaapiBase(object):
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

    # counters
    def newCounters (self):
        raise NotImplementedError()

    def setCountersObj (self, obj):
        raise NotImplementedError()

    def getCountersObj (self):
        raise NotImplementedError()

    def hasCounters (self):
        raise NotImplementedError()




    # config leaves

    # upPeriod
    def requestUpPeriod (self, requested):
        raise NotImplementedError()

    def isUpPeriodRequested (self):
        raise NotImplementedError()

    def getUpPeriod (self):
        raise NotImplementedError()

    def hasUpPeriod (self):
        raise NotImplementedError()

    def setUpPeriod (self, upPeriod):
        raise NotImplementedError()

    # downPeriod
    def requestDownPeriod (self, requested):
        raise NotImplementedError()

    def isDownPeriodRequested (self):
        raise NotImplementedError()

    def getDownPeriod (self):
        raise NotImplementedError()

    def hasDownPeriod (self):
        raise NotImplementedError()

    def setDownPeriod (self, downPeriod):
        raise NotImplementedError()

    # testTimeoutMsec
    def requestTestTimeoutMsec (self, requested):
        raise NotImplementedError()

    def isTestTimeoutMsecRequested (self):
        raise NotImplementedError()

    def getTestTimeoutMsec (self):
        raise NotImplementedError()

    def hasTestTimeoutMsec (self):
        raise NotImplementedError()

    def setTestTimeoutMsec (self, testTimeoutMsec):
        raise NotImplementedError()

    # testIntervalMsec
    def requestTestIntervalMsec (self, requested):
        raise NotImplementedError()

    def isTestIntervalMsecRequested (self):
        raise NotImplementedError()

    def getTestIntervalMsec (self):
        raise NotImplementedError()

    def hasTestIntervalMsec (self):
        raise NotImplementedError()

    def setTestIntervalMsec (self, testIntervalMsec):
        raise NotImplementedError()






"""
Extracted from the below data: 
{
    "node": {
        "name": "link", 
        "namespace": "link", 
        "className": "LinkMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.link.link_maapi_gen import LinkMaapi", 
        "baseClassName": "LinkMaapiBase", 
        "baseModule": "link_maapi_base_gen"
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
            "yangName": "link", 
            "namespace": "link", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "link"
        }
    ], 
    "descendants": [
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "memberName": "counters", 
            "yangName": "counters", 
            "className": "BlinkyCountersMaapi", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.link.counters.counters_maapi_gen import BlinkyCountersMaapi", 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"
        }
    ], 
    "conditionalDebugName": null, 
    "operLeaves": [], 
    "module": {}, 
    "configLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "upPeriod", 
            "yangName": "up-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "downPeriod", 
            "yangName": "down-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "testTimeoutMsec", 
            "yangName": "test-timeout-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "testIntervalMsec", 
            "yangName": "test-interval-msec", 
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
            "common", 
            "qwilt_tech_interfaces"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "upPeriod", 
            "yangName": "up-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "downPeriod", 
            "yangName": "down-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "testTimeoutMsec", 
            "yangName": "test-timeout-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "testIntervalMsec", 
            "yangName": "test-interval-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "createTime": "2013"
}
"""


