


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ConditionalData(object):

    def __init__ (self):

        self.enabled = False
        self._myHasEnabled=False
        
        self.cid = ""
        self._myHasCid=False
        

    def copyFrom (self, other):

        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.cid=other.cid
        self._myHasCid=other._myHasCid
        
    # has...() methods

    def hasEnabled (self):
        return self._myHasEnabled

    def hasCid (self):
        return self._myHasCid


    # setHas...() methods

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasCid (self):
        self._myHasCid=True


    def clearAllHas (self):

        self._myHasEnabled=False

        self._myHasCid=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasCid:
            x = "+"
        leafStr = str(self.cid)
        items.append(x + "Cid="+leafStr)

        return "{ConditionalData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ConditionalData", 
        "namespace": "conditional", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.unit.logging.conditional.conditional_data_gen import ConditionalData"
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
            "namespace": "line", 
            "isCurrent": false
        }, 
        {
            "namespace": "analyzer", 
            "isCurrent": false
        }, 
        {
            "namespace": "unit", 
            "isCurrent": false
        }, 
        {
            "namespace": "logging", 
            "isCurrent": false
        }, 
        {
            "namespace": "conditional", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "cid", 
            "yangName": "cid", 
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "createTime": "2013"
}
"""


