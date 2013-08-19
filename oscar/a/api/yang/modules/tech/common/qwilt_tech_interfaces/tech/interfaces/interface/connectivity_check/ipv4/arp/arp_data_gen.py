


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ArpData(object):

    def __init__ (self):

        self.testTimeoutMsec = 0
        self._myHasTestTimeoutMsec=False
        
        self.testIntervalMsec = 0
        self._myHasTestIntervalMsec=False
        
        self.upPeriod = 0
        self._myHasUpPeriod=False
        
        self.downPeriod = 0
        self._myHasDownPeriod=False
        

    def copyFrom (self, other):

        self.testTimeoutMsec=other.testTimeoutMsec
        self._myHasTestTimeoutMsec=other._myHasTestTimeoutMsec
        
        self.testIntervalMsec=other.testIntervalMsec
        self._myHasTestIntervalMsec=other._myHasTestIntervalMsec
        
        self.upPeriod=other.upPeriod
        self._myHasUpPeriod=other._myHasUpPeriod
        
        self.downPeriod=other.downPeriod
        self._myHasDownPeriod=other._myHasDownPeriod
        
    # has...() methods

    def hasTestTimeoutMsec (self):
        return self._myHasTestTimeoutMsec

    def hasTestIntervalMsec (self):
        return self._myHasTestIntervalMsec

    def hasUpPeriod (self):
        return self._myHasUpPeriod

    def hasDownPeriod (self):
        return self._myHasDownPeriod


    # setHas...() methods

    def setHasTestTimeoutMsec (self):
        self._myHasTestTimeoutMsec=True

    def setHasTestIntervalMsec (self):
        self._myHasTestIntervalMsec=True

    def setHasUpPeriod (self):
        self._myHasUpPeriod=True

    def setHasDownPeriod (self):
        self._myHasDownPeriod=True


    def clearAllHas (self):

        self._myHasTestTimeoutMsec=False

        self._myHasTestIntervalMsec=False

        self._myHasUpPeriod=False

        self._myHasDownPeriod=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasTestTimeoutMsec:
            x = "+"
        leafStr = str(self.testTimeoutMsec)
        items.append(x + "TestTimeoutMsec="+leafStr)

        x=""
        if self._myHasTestIntervalMsec:
            x = "+"
        leafStr = str(self.testIntervalMsec)
        items.append(x + "TestIntervalMsec="+leafStr)

        x=""
        if self._myHasUpPeriod:
            x = "+"
        leafStr = str(self.upPeriod)
        items.append(x + "UpPeriod="+leafStr)

        x=""
        if self._myHasDownPeriod:
            x = "+"
        leafStr = str(self.downPeriod)
        items.append(x + "DownPeriod="+leafStr)

        return "{ArpData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ArpData", 
        "namespace": "arp", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.arp.arp_data_gen import ArpData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "interfaces", 
            "isCurrent": false
        }, 
        {
            "namespace": "interface", 
            "isCurrent": false
        }, 
        {
            "namespace": "connectivity_check", 
            "isCurrent": false
        }, 
        {
            "namespace": "ipv4", 
            "isCurrent": false
        }, 
        {
            "namespace": "arp", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "testTimeoutMsec", 
            "yangName": "test-timeout-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "testIntervalMsec", 
            "yangName": "test-interval-msec", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "upPeriod", 
            "yangName": "up-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "downPeriod", 
            "yangName": "down-period", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }
    ], 
    "module": {}, 
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
    "createTime": "2013"
}
"""


