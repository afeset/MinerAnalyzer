


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SearchData(object):

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

        return "{SearchData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SearchData", 
        "namespace": "search", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system.tech.system.name_resolution.dns.search.search_data_gen import SearchData"
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
            "namespace": "name_resolution", 
            "isCurrent": false
        }, 
        {
            "namespace": "dns", 
            "isCurrent": false
        }, 
        {
            "namespace": "search", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BuiltinStringHandler", 
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
            "qwilt_tech_system"
        ]
    }, 
    "createTime": "2013"
}
"""


