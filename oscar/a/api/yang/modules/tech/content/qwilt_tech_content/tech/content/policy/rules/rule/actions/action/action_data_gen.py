


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: orens

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket



class ActionData(object):

    def __init__ (self):

        self.delivery = False
        self._myHasDelivery=False
        
        self.analytics = True
        self._myHasAnalytics=False
        
        self.cachingPotential = True
        self._myHasCachingPotential=False
        
        self.acquisition = True
        self._myHasAcquisition=False
        

    def copyFrom (self, other):

        self.delivery=other.delivery
        self._myHasDelivery=other._myHasDelivery
        
        self.analytics=other.analytics
        self._myHasAnalytics=other._myHasAnalytics
        
        self.cachingPotential=other.cachingPotential
        self._myHasCachingPotential=other._myHasCachingPotential
        
        self.acquisition=other.acquisition
        self._myHasAcquisition=other._myHasAcquisition
        
    # has...() methods

    def hasDelivery (self):
        return self._myHasDelivery

    def hasAnalytics (self):
        return self._myHasAnalytics

    def hasCachingPotential (self):
        return self._myHasCachingPotential

    def hasAcquisition (self):
        return self._myHasAcquisition


    # setHas...() methods

    def setHasDelivery (self):
        self._myHasDelivery=True

    def setHasAnalytics (self):
        self._myHasAnalytics=True

    def setHasCachingPotential (self):
        self._myHasCachingPotential=True

    def setHasAcquisition (self):
        self._myHasAcquisition=True


    def clearAllHas (self):

        self._myHasDelivery=False

        self._myHasAnalytics=False

        self._myHasCachingPotential=False

        self._myHasAcquisition=False


    def __str__ (self):
        items=[]

        x=""
        if self._myHasDelivery:
            x = "+"
        leafStr = str(self.delivery)
        items.append(x + "Delivery="+leafStr)

        x=""
        if self._myHasAnalytics:
            x = "+"
        leafStr = str(self.analytics)
        items.append(x + "Analytics="+leafStr)

        x=""
        if self._myHasCachingPotential:
            x = "+"
        leafStr = str(self.cachingPotential)
        items.append(x + "CachingPotential="+leafStr)

        x=""
        if self._myHasAcquisition:
            x = "+"
        leafStr = str(self.acquisition)
        items.append(x + "Acquisition="+leafStr)

        return "{ActionData: "+",".join(items)+"}"

"""
Extracted from the below data: 
{
    "node": {
        "className": "ActionData", 
        "namespace": "action", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content.tech.content.policy.rules.rule.actions.action.action_data_gen import ActionData"
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
            "namespace": "actions", 
            "isCurrent": false
        }, 
        {
            "namespace": "action", 
            "isCurrent": true
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "delivery", 
            "yangName": "delivery", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "false", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "analytics", 
            "yangName": "analytics", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "cachingPotential", 
            "yangName": "caching-potential", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "acquisition", 
            "yangName": "acquisition", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": "true", 
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


