


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.content.qwilt_tech_content.qwilt_tech_content_module_gen import SiteListType


class RuleData(object):

    def __init__ (self):

        self.description = ""
        self._myHasDescription=False
        
        self.enabled = True
        self._myHasEnabled=False
        
        self.siteList = SiteListType.kInclude
        self._myHasSiteList=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.siteList=other.siteList
        self._myHasSiteList=other._myHasSiteList
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasDescription (self):
        return self._myHasDescription

    def hasEnabled (self):
        return self._myHasEnabled

    def hasSiteList (self):
        return self._myHasSiteList

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasSiteList (self):
        self._myHasSiteList=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasDescription=False

        self._myHasEnabled=False

        self._myHasSiteList=False

        self._myHasName=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDescription:
            x = "+"
        leafStr = str(self.description)
        items.append(x + "Description="+leafStr)

        x=""
        if self._myHasEnabled:
            x = "+"
        leafStr = str(self.enabled)
        items.append(x + "Enabled="+leafStr)

        x=""
        if self._myHasSiteList:
            x = "+"
        leafStr = str(self.siteList)
        items.append(x + "SiteList="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{RuleData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "RuleData", 
        "namespace": "rule", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.rule_data_gen import RuleData"
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
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "description", 
            "yangName": "description", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "enabled", 
            "yangName": "enabled", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "siteList", 
            "yangName": "site-list", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "include", 
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


