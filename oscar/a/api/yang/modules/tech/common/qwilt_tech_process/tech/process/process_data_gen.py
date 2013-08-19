


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ProcessData(object):

    def __init__ (self):

        self.enabled = False
        self._myHasEnabled=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasEnabled (self):
        return self._myHasEnabled

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasEnabled=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{ProcessData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ProcessData", 
        "namespace": "process", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.process_data_gen import ProcessData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "process", 
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
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "name", 
            "yangName": "name", 
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
            "qwilt_tech_process"
        ]
    }, 
    "createTime": "2013"
}
"""


