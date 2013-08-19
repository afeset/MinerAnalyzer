


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class SiteData(object):

    def __init__ (self):

        self.name = ""
        self._myHasName=False
        
        self.description = ""
        self._myHasDescription=False
        

    def copyFrom (self, other):

        self.name=other.name
        self._myHasName=other._myHasName
        
        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
    # has...() methods

    def hasName (self):
        return self._myHasName

    def hasDescription (self):
        return self._myHasDescription


    # setHas...() methods

    def setHasName (self):
        self._myHasName=True

    def setHasDescription (self):
        self._myHasDescription=True


    def clearAllHas (self):

        self._myHasName=False

        self._myHasDescription=False


    def __str__ (self):
        items=[]

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

        return "{SiteData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SiteData", 
        "namespace": "site", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.signatures.sites.site.site_data_gen import SiteData"
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
            "namespace": "signatures", 
            "isCurrent": false
        }, 
        {
            "namespace": "sites", 
            "isCurrent": false
        }, 
        {
            "namespace": "site", 
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
            "content", 
            "qwilt_tech_content"
        ]
    }, 
    "createTime": "2013"
}
"""


