


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

        self.site = ""
        self._myHasSite=False
        

    def copyFrom (self, other):

        self.site=other.site
        self._myHasSite=other._myHasSite
        
    # has...() methods

    def hasSite (self):
        return self._myHasSite


    # setHas...() methods

    def setHasSite (self):
        self._myHasSite=True


    def clearAllHas (self):

        self._myHasSite=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasSite:
            x = "+"
        leafStr = str(self.site)
        items.append(x + "Site="+leafStr)

        return "{SiteData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "SiteData", 
        "namespace": "site", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.site.site_data_gen import SiteData"
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
            "namespace": "site", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "site", 
            "yangName": "site", 
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


