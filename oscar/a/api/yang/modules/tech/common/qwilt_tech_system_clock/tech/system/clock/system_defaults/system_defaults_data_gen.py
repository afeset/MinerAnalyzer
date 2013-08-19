


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

        self.timezone = ""
        self._myHasTimezone=False
        

    def copyFrom (self, other):

        self.timezone=other.timezone
        self._myHasTimezone=other._myHasTimezone
        
    # has...() methods

    def hasTimezone (self):
        return self._myHasTimezone


    # setHas...() methods

    def setHasTimezone (self):
        self._myHasTimezone=True


    def clearAllHas (self):

        self._myHasTimezone=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasTimezone:
            x = "+"
        leafStr = str(self.timezone)
        items.append(x + "Timezone="+leafStr)

        return "{SystemDefaultsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemDefaultsData", 
        "namespace": "system_defaults", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_clock.tech.system.clock.system_defaults.system_defaults_data_gen import SystemDefaultsData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "system", 
            "isCurrent": false
        }, 
        {
            "namespace": "clock", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "timezone", 
            "yangName": "timezone", 
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
            "qwilt_tech_system_clock"
        ]
    }, 
    "createTime": "2013"
}
"""


