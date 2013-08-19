


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureForceOperationalStatusType


class SimulationData(object):

    def __init__ (self):

        self.forceOperationalStatus = TemperatureForceOperationalStatusType.kNone
        self._myHasForceOperationalStatus=False
        

    def copyFrom (self, other):

        self.forceOperationalStatus=other.forceOperationalStatus
        self._myHasForceOperationalStatus=other._myHasForceOperationalStatus
        
    # has...() methods

    def hasForceOperationalStatus (self):
        return self._myHasForceOperationalStatus


    # setHas...() methods

    def setHasForceOperationalStatus (self):
        self._myHasForceOperationalStatus=True


    def clearAllHas (self):

        self._myHasForceOperationalStatus=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasForceOperationalStatus:
            x = "+"
        leafStr = str(self.forceOperationalStatus)
        items.append(x + "ForceOperationalStatus="+leafStr)

        return "{SimulationData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SimulationData", 
        "namespace": "simulation", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.system_defaults.simulation.simulation_data_gen import SimulationData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "platform", 
            "isCurrent": false
        }, 
        {
            "namespace": "temperature", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "simulation", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "forceOperationalStatus", 
            "yangName": "force-operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
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
            "qwilt_tech_platform_temperature"
        ]
    }, 
    "createTime": "2013"
}
"""


