


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class LoggerClassData(object):

    def __init__ (self):

        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{LoggerClassData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "LoggerClassData", 
        "namespace": "logger_class", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.logger_class_data_gen import LoggerClassData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "logger_class", 
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
            "qwilt_tech_debug"
        ]
    }, 
    "createTime": "2013"
}
"""


