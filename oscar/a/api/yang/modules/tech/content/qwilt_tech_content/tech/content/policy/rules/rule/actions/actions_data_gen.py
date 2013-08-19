


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ActionsData(object):

    def __init__ (self):

        self.ignore = False
        self._myHasIgnore=False
        

    def copyFrom (self, other):

        self.ignore=other.ignore
        self._myHasIgnore=other._myHasIgnore
        
    # has...() methods

    def hasIgnore (self):
        return self._myHasIgnore


    # setHas...() methods

    def setHasIgnore (self):
        self._myHasIgnore=True


    def clearAllHas (self):

        self._myHasIgnore=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasIgnore:
            x = "+"
        leafStr = str(self.ignore)
        items.append(x + "Ignore="+leafStr)

        return "{ActionsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ActionsData", 
        "namespace": "actions", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.actions.actions_data_gen import ActionsData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "content", 
            "isCurrent": false
        }, 
        {
            "namespace": "policy", 
            "isCurrent": false
        }, 
        {
            "namespace": "rules", 
            "isCurrent": false
        }, 
        {
            "namespace": "rule", 
            "isCurrent": false
        }, 
        {
            "namespace": "actions", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "ignore", 
            "yangName": "ignore", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
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
            "content", 
            "qwilt_tech_content"
        ]
    }, 
    "createTime": "2013"
}
"""


