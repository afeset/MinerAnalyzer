


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class PredictionData(object):

    def __init__ (self):

        self.estimatedDeliveryTrxPerConnection = 0
        self._myHasEstimatedDeliveryTrxPerConnection=False
        
        self.simulatedDiskSizeGb = 0
        self._myHasSimulatedDiskSizeGb=False
        
        self.deliveryMaxActiveConnections = 0
        self._myHasDeliveryMaxActiveConnections=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.deliveryMaxBwMbps = 0
        self._myHasDeliveryMaxBwMbps=False
        

    def copyFrom (self, other):

        self.estimatedDeliveryTrxPerConnection=other.estimatedDeliveryTrxPerConnection
        self._myHasEstimatedDeliveryTrxPerConnection=other._myHasEstimatedDeliveryTrxPerConnection
        
        self.simulatedDiskSizeGb=other.simulatedDiskSizeGb
        self._myHasSimulatedDiskSizeGb=other._myHasSimulatedDiskSizeGb
        
        self.deliveryMaxActiveConnections=other.deliveryMaxActiveConnections
        self._myHasDeliveryMaxActiveConnections=other._myHasDeliveryMaxActiveConnections
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.deliveryMaxBwMbps=other.deliveryMaxBwMbps
        self._myHasDeliveryMaxBwMbps=other._myHasDeliveryMaxBwMbps
        
    # has...() methods

    def hasEstimatedDeliveryTrxPerConnection (self):
        return self._myHasEstimatedDeliveryTrxPerConnection

    def hasSimulatedDiskSizeGb (self):
        return self._myHasSimulatedDiskSizeGb

    def hasDeliveryMaxActiveConnections (self):
        return self._myHasDeliveryMaxActiveConnections

    def hasEnabled (self):
        return self._myHasEnabled

    def hasDeliveryMaxBwMbps (self):
        return self._myHasDeliveryMaxBwMbps


    # setHas...() methods

    def setHasEstimatedDeliveryTrxPerConnection (self):
        self._myHasEstimatedDeliveryTrxPerConnection=True

    def setHasSimulatedDiskSizeGb (self):
        self._myHasSimulatedDiskSizeGb=True

    def setHasDeliveryMaxActiveConnections (self):
        self._myHasDeliveryMaxActiveConnections=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasDeliveryMaxBwMbps (self):
        self._myHasDeliveryMaxBwMbps=True


    def clearAllHas (self):

        self._myHasEstimatedDeliveryTrxPerConnection=False

        self._myHasSimulatedDiskSizeGb=False

        self._myHasDeliveryMaxActiveConnections=False

        self._myHasEnabled=False

        self._myHasDeliveryMaxBwMbps=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEstimatedDeliveryTrxPerConnection:
            x = "+"
        leafStr = str(self.estimatedDeliveryTrxPerConnection)
        items.append(x + "EstimatedDeliveryTrxPerConnection="+leafStr)

        x=""
        if self._myHasSimulatedDiskSizeGb:
            x = "+"
        leafStr = str(self.simulatedDiskSizeGb)
        items.append(x + "SimulatedDiskSizeGb="+leafStr)

        x=""
        if self._myHasDeliveryMaxActiveConnections:
            x = "+"
        leafStr = str(self.deliveryMaxActiveConnections)
        items.append(x + "DeliveryMaxActiveConnections="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasDeliveryMaxBwMbps:
            x = "+"
        leafStr = str(self.deliveryMaxBwMbps)
        items.append(x + "DeliveryMaxBwMbps="+leafStr)

        return "{PredictionData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "PredictionData", 
        "namespace": "prediction", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.prediction.prediction_data_gen import PredictionData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "content", 
            "isCurrent": false
        }, 
        {
            "namespace": "line", 
            "isCurrent": false
        }, 
        {
            "namespace": "analyzer", 
            "isCurrent": false
        }, 
        {
            "namespace": "prediction", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "estimatedDeliveryTrxPerConnection", 
            "yangName": "estimated-delivery-trx-per-connection", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "simulatedDiskSizeGb", 
            "yangName": "simulated-disk-size-gb", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "deliveryMaxActiveConnections", 
            "yangName": "delivery-max-active-connections", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "deliveryMaxBwMbps", 
            "yangName": "delivery-max-bw-mbps", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "createTime": "2013"
}
"""


