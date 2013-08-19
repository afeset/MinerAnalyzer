


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SystemDefaultsData(object):

    def __init__ (self):

        self.commandWarningTimeout = 0
        self._myHasCommandWarningTimeout=False
        
        self.commandTimeout = 0
        self._myHasCommandTimeout=False
        
        self.enabled = True
        self._myHasEnabled=False
        
        self.simulationFile = ""
        self._myHasSimulationFile=False
        

    def copyFrom (self, other):

        self.commandWarningTimeout=other.commandWarningTimeout
        self._myHasCommandWarningTimeout=other._myHasCommandWarningTimeout
        
        self.commandTimeout=other.commandTimeout
        self._myHasCommandTimeout=other._myHasCommandTimeout
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.simulationFile=other.simulationFile
        self._myHasSimulationFile=other._myHasSimulationFile
        
    # has...() methods

    def hasCommandWarningTimeout (self):
        return self._myHasCommandWarningTimeout

    def hasCommandTimeout (self):
        return self._myHasCommandTimeout

    def hasEnabled (self):
        return self._myHasEnabled

    def hasSimulationFile (self):
        return self._myHasSimulationFile


    # setHas...() methods

    def setHasCommandWarningTimeout (self):
        self._myHasCommandWarningTimeout=True

    def setHasCommandTimeout (self):
        self._myHasCommandTimeout=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasSimulationFile (self):
        self._myHasSimulationFile=True


    def clearAllHas (self):

        self._myHasCommandWarningTimeout=False

        self._myHasCommandTimeout=False

        self._myHasEnabled=False

        self._myHasSimulationFile=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasCommandWarningTimeout:
            x = "+"
        leafStr = str(self.commandWarningTimeout)
        items.append(x + "CommandWarningTimeout="+leafStr)

        x=""
        if self._myHasCommandTimeout:
            x = "+"
        leafStr = str(self.commandTimeout)
        items.append(x + "CommandTimeout="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasSimulationFile:
            x = "+"
        leafStr = str(self.simulationFile)
        items.append(x + "SimulationFile="+leafStr)

        return "{SystemDefaultsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemDefaultsData", 
        "namespace": "system_defaults", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.system_defaults.system_defaults_data_gen import SystemDefaultsData"
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
            "namespace": "manager", 
            "isCurrent": false
        }, 
        {
            "namespace": "source", 
            "isCurrent": false
        }, 
        {
            "namespace": "system_defaults", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeout", 
            "yangName": "command-warning-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeout", 
            "yangName": "command-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "simulationFile", 
            "yangName": "simulation-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "", 
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
            "qwilt_tech_platform_manager"
        ]
    }, 
    "createTime": "2013"
}
"""


