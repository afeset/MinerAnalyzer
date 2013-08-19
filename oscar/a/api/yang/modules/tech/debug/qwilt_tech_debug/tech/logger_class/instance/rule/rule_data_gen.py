


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class RuleData(object):

    def __init__ (self):

        self.disabled = False
        self._myHasDisabled=False
        
        self.name = ""
        self._myHasName=False
        
        self.description = ""
        self._myHasDescription=False
        

    def copyFrom (self, other):

        self.disabled=other.disabled
        self._myHasDisabled=other._myHasDisabled
        
        self.name=other.name
        self._myHasName=other._myHasName
        
        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
    # has...() methods

    def hasDisabled (self):
        return self._myHasDisabled

    def hasName (self):
        return self._myHasName

    def hasDescription (self):
        return self._myHasDescription


    # setHas...() methods

    def setHasDisabled (self):
        self._myHasDisabled=True

    def setHasName (self):
        self._myHasName=True

    def setHasDescription (self):
        self._myHasDescription=True


    def clearAllHas (self):

        self._myHasDisabled=False

        self._myHasName=False

        self._myHasDescription=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDisabled:
            x = "+"
        leafStr = str(self.disabled)
        items.append(x + "Disabled="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        x=""
        if self._myHasDescription:
            x = "+"
        leafStr = str(self.description)
        items.append(x + "Description="+leafStr)

        return "{RuleData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "RuleData", 
        "namespace": "rule", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_debug.tech.logger_class.instance.rule.rule_data_gen import RuleData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "logger_class", 
            "isCurrent": false
        }, 
        {
            "namespace": "instance", 
            "isCurrent": false
        }, 
        {
            "namespace": "rule", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "disabled", 
            "yangName": "disabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
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
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
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


