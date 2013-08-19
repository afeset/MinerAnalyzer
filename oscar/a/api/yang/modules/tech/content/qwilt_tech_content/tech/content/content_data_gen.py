


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ContentData(object):

    def __init__ (self):

        self.tempJunkDescriptionType = ""
        self._myHasTempJunkDescriptionType=False
        

    def copyFrom (self, other):

        self.tempJunkDescriptionType=other.tempJunkDescriptionType
        self._myHasTempJunkDescriptionType=other._myHasTempJunkDescriptionType
        
    # has...() methods

    def hasTempJunkDescriptionType (self):
        return self._myHasTempJunkDescriptionType


    # setHas...() methods

    def setHasTempJunkDescriptionType (self):
        self._myHasTempJunkDescriptionType=True


    def clearAllHas (self):

        self._myHasTempJunkDescriptionType=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasTempJunkDescriptionType:
            x = "+"
        leafStr = str(self.tempJunkDescriptionType)
        items.append(x + "TempJunkDescriptionType="+leafStr)

        return "{ContentData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ContentData", 
        "namespace": "content", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.content_data_gen import ContentData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "content", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "tempJunkDescriptionType", 
            "yangName": "temp-junk-description-type", 
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
            "qwilt_tech_content"
        ]
    }, 
    "createTime": "2013"
}
"""


