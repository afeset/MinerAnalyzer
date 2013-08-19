


# Copyright Qwilt, 2011
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: auto-generated

# Must be set here to avoid stupid warnings about stuff in BlinkyOperData
__pychecker__="no-classattr"

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes

import socket





class StatusOperData (object):

    def __init__ (self):

        self.actualDeliveryInterface = ""
        self._myHasActualDeliveryInterface=False
        self._myActualDeliveryInterfaceRequested=False
        


    def copyFrom (self, other):

        self.actualDeliveryInterface=other.actualDeliveryInterface
        self._myHasActualDeliveryInterface=other._myHasActualDeliveryInterface
        self._myActualDeliveryInterfaceRequested=other._myActualDeliveryInterfaceRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isActualDeliveryInterfaceRequested():
            self.actualDeliveryInterface=other.actualDeliveryInterface
            self._myHasActualDeliveryInterface=other._myHasActualDeliveryInterface
            self._myActualDeliveryInterfaceRequested=other._myActualDeliveryInterfaceRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasActualDeliveryInterface():
            self.actualDeliveryInterface=other.actualDeliveryInterface
            self._myHasActualDeliveryInterface=other._myHasActualDeliveryInterface
            self._myActualDeliveryInterfaceRequested=other._myActualDeliveryInterfaceRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.actualDeliveryInterface=other.actualDeliveryInterface
        self._myHasActualDeliveryInterface=other._myHasActualDeliveryInterface
        


    def setAllNumericToZero (self):
        
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        pass


    # has...() methods

    def hasActualDeliveryInterface (self):
        return self._myHasActualDeliveryInterface




    # setHas...() methods

    def setHasActualDeliveryInterface (self):
        self._myHasActualDeliveryInterface=True




    # isRequested...() methods

    def isActualDeliveryInterfaceRequested (self):
        return self._myActualDeliveryInterfaceRequested




    # setRequested...() methods

    def setActualDeliveryInterfaceRequested (self):
        self._myActualDeliveryInterfaceRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myActualDeliveryInterfaceRequested:
            x = "+ActualDeliveryInterface="
            if self._myHasActualDeliveryInterface:
                leafStr = str(self.actualDeliveryInterface)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ActualDeliveryInterface="
        if self._myHasActualDeliveryInterface:
            leafStr = str(self.actualDeliveryInterface)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myActualDeliveryInterfaceRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setActualDeliveryInterfaceRequested()
        
        


    def setActualDeliveryInterface (self, actualDeliveryInterface):
        self.actualDeliveryInterface = actualDeliveryInterface
        self.setHasActualDeliveryInterface()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_interfaces.tech.content.interfaces.interface.delivery.ipv4.status.status_oper_data_gen import StatusOperData"
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
            "namespace": "interfaces", 
            "isCurrent": false
        }, 
        {
            "namespace": "interface", 
            "isCurrent": false
        }, 
        {
            "namespace": "delivery", 
            "isCurrent": false
        }, 
        {
            "namespace": "ipv4", 
            "isCurrent": false
        }, 
        {
            "namespace": "status", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "actualDeliveryInterface", 
            "yangName": "actual-delivery-interface", 
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
            "qwilt_tech_content_interfaces"
        ]
    }, 
    "createTime": "2013"
}
"""


