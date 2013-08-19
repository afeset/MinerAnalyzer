


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

        self.trimContentItemSizeMb = 0
        self._myHasTrimContentItemSizeMb=False
        

    def copyFrom (self, other):

        self.trimContentItemSizeMb=other.trimContentItemSizeMb
        self._myHasTrimContentItemSizeMb=other._myHasTrimContentItemSizeMb
        
    # has...() methods

    def hasTrimContentItemSizeMb (self):
        return self._myHasTrimContentItemSizeMb


    # setHas...() methods

    def setHasTrimContentItemSizeMb (self):
        self._myHasTrimContentItemSizeMb=True


    def clearAllHas (self):

        self._myHasTrimContentItemSizeMb=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasTrimContentItemSizeMb:
            x = "+"
        leafStr = str(self.trimContentItemSizeMb)
        items.append(x + "TrimContentItemSizeMb="+leafStr)

        return "{SystemDefaultsData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SystemDefaultsData", 
        "namespace": "system_defaults", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_line.tech.content.line.analyzer.potential.method.system_defaults.system_defaults_data_gen import SystemDefaultsData"
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "trimContentItemSizeMb", 
            "yangName": "trim-content-item-size-mb", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "0", 
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


