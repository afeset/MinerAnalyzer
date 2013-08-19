


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class LogArchivingData(object):

    def __init__ (self):

        self.dummy = True
        self._myHasDummy=False
        

    def copyFrom (self, other):

        self.dummy=other.dummy
        self._myHasDummy=other._myHasDummy
        
    # has...() methods

    def hasDummy (self):
        return self._myHasDummy


    # setHas...() methods

    def setHasDummy (self):
        self._myHasDummy=True


    def clearAllHas (self):

        self._myHasDummy=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDummy:
            x = "+"
        leafStr = str(self.dummy)
        items.append(x + "Dummy="+leafStr)

        return "{LogArchivingData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "LogArchivingData", 
        "namespace": "log_archiving", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.system_defaults.housekeeper.log_archiving.log_archiving_data_gen import LogArchivingData"
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
            "namespace": "system_defaults", 
            "isCurrent": false
        }, 
        {
            "namespace": "housekeeper", 
            "isCurrent": false
        }, 
        {
            "namespace": "log_archiving", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "dummy", 
            "yangName": "dummy", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
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
            "debug", 
            "qwilt_tech_log"
        ]
    }, 
    "createTime": "2013"
}
"""


