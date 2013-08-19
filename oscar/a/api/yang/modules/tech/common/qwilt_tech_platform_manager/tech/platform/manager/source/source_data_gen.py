


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SourceData(object):

    def __init__ (self):

        self.name = ""
        self._myHasName=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.simulationFile = ""
        self._myHasSimulationFile=False
        
        self.commandTimeout = 0
        self._myHasCommandTimeout=False
        
        self.commandWarningTimeout = 0
        self._myHasCommandWarningTimeout=False
        

    def copyFrom (self, other):

        self.name=other.name
        self._myHasName=other._myHasName
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.simulationFile=other.simulationFile
        self._myHasSimulationFile=other._myHasSimulationFile
        
        self.commandTimeout=other.commandTimeout
        self._myHasCommandTimeout=other._myHasCommandTimeout
        
        self.commandWarningTimeout=other.commandWarningTimeout
        self._myHasCommandWarningTimeout=other._myHasCommandWarningTimeout
        
    # has...() methods

    def hasName (self):
        return self._myHasName

    def hasEnabled (self):
        return self._myHasEnabled

    def hasSimulationFile (self):
        return self._myHasSimulationFile

    def hasCommandTimeout (self):
        return self._myHasCommandTimeout

    def hasCommandWarningTimeout (self):
        return self._myHasCommandWarningTimeout


    # setHas...() methods

    def setHasName (self):
        self._myHasName=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasSimulationFile (self):
        self._myHasSimulationFile=True

    def setHasCommandTimeout (self):
        self._myHasCommandTimeout=True

    def setHasCommandWarningTimeout (self):
        self._myHasCommandWarningTimeout=True


    def clearAllHas (self):

        self._myHasName=False

        self._myHasEnabled=False

        self._myHasSimulationFile=False

        self._myHasCommandTimeout=False

        self._myHasCommandWarningTimeout=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

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

        x=""
        if self._myHasCommandTimeout:
            x = "+"
        leafStr = str(self.commandTimeout)
        items.append(x + "CommandTimeout="+leafStr)

        x=""
        if self._myHasCommandWarningTimeout:
            x = "+"
        leafStr = str(self.commandWarningTimeout)
        items.append(x + "CommandWarningTimeout="+leafStr)

        return "{SourceData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SourceData", 
        "namespace": "source", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.source.source_data_gen import SourceData"
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
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "simulationFile", 
            "yangName": "simulation-file", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandTimeout", 
            "yangName": "command-timeout", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "commandWarningTimeout", 
            "yangName": "command-warning-timeout", 
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
            "qwilt_tech_platform_manager"
        ]
    }, 
    "createTime": "2013"
}
"""


