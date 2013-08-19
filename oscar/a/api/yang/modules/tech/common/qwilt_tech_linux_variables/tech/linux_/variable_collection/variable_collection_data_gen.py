


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class VariableCollectionData(object):

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

        return "{VariableCollectionData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "VariableCollectionData", 
        "namespace": "variable_collection", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable_collection_data_gen import VariableCollectionData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "linux_", 
            "isCurrent": false
        }, 
        {
            "namespace": "variable_collection", 
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
            "common", 
            "qwilt_tech_linux_variables"
        ]
    }, 
    "createTime": "2013"
}
"""


