


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class MethodData(object):

    def __init__ (self):

        self.trimContentItemSizeMb = 0
        self._myHasTrimContentItemSizeMb=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.trimContentItemSizeMb=other.trimContentItemSizeMb
        self._myHasTrimContentItemSizeMb=other._myHasTrimContentItemSizeMb
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasTrimContentItemSizeMb (self):
        return self._myHasTrimContentItemSizeMb

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasTrimContentItemSizeMb (self):
        self._myHasTrimContentItemSizeMb=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasTrimContentItemSizeMb=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasTrimContentItemSizeMb:
            x = "+"
        leafStr = str(self.trimContentItemSizeMb)
        items.append(x + "TrimContentItemSizeMb="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{MethodData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "MethodData", 
        "namespace": "method", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.potential.method.method_data_gen import MethodData"
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
            "namespace": "potential", 
            "isCurrent": false
        }, 
        {
            "namespace": "method", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "trimContentItemSizeMb", 
            "yangName": "trim-content-item-size-mb", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": true
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
            "content", 
            "qwilt_tech_content_line"
        ]
    }, 
    "createTime": "2013"
}
"""


