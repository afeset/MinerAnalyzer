


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class HousekeeperData(object):

    def __init__ (self):

        self.enabled = False
        self._myHasEnabled=False
        
        self.pollInterval = 0
        self._myHasPollInterval=False
        

    def copyFrom (self, other):

        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.pollInterval=other.pollInterval
        self._myHasPollInterval=other._myHasPollInterval
        
    # has...() methods

    def hasEnabled (self):
        return self._myHasEnabled

    def hasPollInterval (self):
        return self._myHasPollInterval


    # setHas...() methods

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasPollInterval (self):
        self._myHasPollInterval=True


    def clearAllHas (self):

        self._myHasEnabled=False

        self._myHasPollInterval=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasPollInterval:
            x = "+"
        leafStr = str(self.pollInterval)
        items.append(x + "PollInterval="+leafStr)

        return "{HousekeeperData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "HousekeeperData", 
        "namespace": "housekeeper", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.housekeeper_data_gen import HousekeeperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "log", 
            "isCurrent": false
        }, 
        {
            "namespace": "housekeeper", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
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
            "memberName": "pollInterval", 
            "yangName": "poll-interval", 
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
            "debug", 
            "qwilt_tech_log"
        ]
    }, 
    "createTime": "2013"
}
"""


