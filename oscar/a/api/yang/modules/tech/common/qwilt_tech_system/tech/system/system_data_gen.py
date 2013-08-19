


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SystemData(object):

    def __init__ (self):

        self.hostname = ""
        self._myHasHostname=False
        

    def copyFrom (self, other):

        self.hostname=other.hostname
        self._myHasHostname=other._myHasHostname
        
    # has...() methods

    def hasHostname (self):
        return self._myHasHostname


    # setHas...() methods

    def setHasHostname (self):
        self._myHasHostname=True


    def clearAllHas (self):

        self._myHasHostname=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasHostname:
            x = "+"
        leafStr = str(self.hostname)
        items.append(x + "Hostname="+leafStr)

        return "{SystemData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemData", 
        "namespace": "system", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.system_data_gen import SystemData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "system", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "hostname", 
            "yangName": "hostname", 
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
            "qwilt_tech_system"
        ]
    }, 
    "createTime": "2013"
}
"""


