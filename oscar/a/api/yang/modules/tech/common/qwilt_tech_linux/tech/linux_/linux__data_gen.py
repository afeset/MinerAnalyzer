


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class LinuxData(object):

    def __init__ (self):

        self.instance = ""
        self._myHasInstance=False
        

    def copyFrom (self, other):

        self.instance=other.instance
        self._myHasInstance=other._myHasInstance
        
    # has...() methods

    def hasInstance (self):
        return self._myHasInstance


    # setHas...() methods

    def setHasInstance (self):
        self._myHasInstance=True


    def clearAllHas (self):

        self._myHasInstance=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasInstance:
            x = "+"
        leafStr = str(self.instance)
        items.append(x + "Instance="+leafStr)

        return "{LinuxData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "LinuxData", 
        "namespace": "linux_", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux.tech.linux_.linux__data_gen import LinuxData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "linux_", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "instance", 
            "yangName": "instance", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
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
            "qwilt_tech_linux"
        ]
    }, 
    "createTime": "2013"
}
"""


