


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket

from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.qwilt_tech_content_reporting_module_gen import ReportingExportTypesType


class ExportData(object):

    def __init__ (self):

        self.description = ""
        self._myHasDescription=False
        
        self.enabled = False
        self._myHasEnabled=False
        
        self.analytics = False
        self._myHasAnalytics=False
        
        self.urlTranslation = False
        self._myHasUrlTranslation=False
        
        self.type_ = ReportingExportTypesType.kNone
        self._myHasType_=False
        
        self.id = "qwilt"
        self._myHasId=False
        
        self.name = ""
        self._myHasName=False
        

    def copyFrom (self, other):

        self.description=other.description
        self._myHasDescription=other._myHasDescription
        
        self.enabled=other.enabled
        self._myHasEnabled=other._myHasEnabled
        
        self.analytics=other.analytics
        self._myHasAnalytics=other._myHasAnalytics
        
        self.urlTranslation=other.urlTranslation
        self._myHasUrlTranslation=other._myHasUrlTranslation
        
        self.type_=other.type_
        self._myHasType_=other._myHasType_
        
        self.id=other.id
        self._myHasId=other._myHasId
        
        self.name=other.name
        self._myHasName=other._myHasName
        
    # has...() methods

    def hasDescription (self):
        return self._myHasDescription

    def hasEnabled (self):
        return self._myHasEnabled

    def hasAnalytics (self):
        return self._myHasAnalytics

    def hasUrlTranslation (self):
        return self._myHasUrlTranslation

    def hasType_ (self):
        return self._myHasType_

    def hasId (self):
        return self._myHasId

    def hasName (self):
        return self._myHasName


    # setHas...() methods

    def setHasDescription (self):
        self._myHasDescription=True

    def setHasEnabled (self):
        self._myHasEnabled=True

    def setHasAnalytics (self):
        self._myHasAnalytics=True

    def setHasUrlTranslation (self):
        self._myHasUrlTranslation=True

    def setHasType_ (self):
        self._myHasType_=True

    def setHasId (self):
        self._myHasId=True

    def setHasName (self):
        self._myHasName=True


    def clearAllHas (self):

        self._myHasDescription=False

        self._myHasEnabled=False

        self._myHasAnalytics=False

        self._myHasUrlTranslation=False

        self._myHasType_=False

        self._myHasId=False

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
        if self._myHasAnalytics:
            x = "+"
        leafStr = str(self.analytics)
        items.append(x + "Analytics="+leafStr)

        x=""
        if self._myHasUrlTranslation:
            x = "+"
        leafStr = str(self.urlTranslation)
        items.append(x + "UrlTranslation="+leafStr)

        x=""
        if self._myHasType_:
            x = "+"
        leafStr = str(self.type_)
        items.append(x + "Type_="+leafStr)

        x=""
        if self._myHasId:
            x = "+"
        leafStr = str(self.id)
        items.append(x + "Id="+leafStr)

        x=""
        if self._myHasName:
            x = "+"
        leafStr = str(self.name)
        items.append(x + "Name="+leafStr)

        return "{ExportData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ExportData", 
        "namespace": "export_", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.export__data_gen import ExportData"
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
            "namespace": "reporting", 
            "isCurrent": false
        }, 
        {
            "namespace": "export_", 
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
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "analytics", 
            "yangName": "analytics", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "urlTranslation", 
            "yangName": "url-translation", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "type_", 
            "yangName": "type", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "none", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "id", 
            "yangName": "id", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "qwilt", 
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
            "qwilt_tech_content_reporting"
        ]
    }, 
    "createTime": "2013"
}
"""


