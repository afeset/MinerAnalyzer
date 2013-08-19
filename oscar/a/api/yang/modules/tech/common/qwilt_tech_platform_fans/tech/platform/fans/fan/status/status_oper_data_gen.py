


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanOperationalStatusType


class StatusOperData (object):

    def __init__ (self):

        self.operationalStatus = FanOperationalStatusType.kDown
        self._myHasOperationalStatus=False
        self._myOperationalStatusRequested=False
        
        self.operationalStatusReason = FanOperationalStatusReasonType.kNone
        self._myHasOperationalStatusReason=False
        self._myOperationalStatusReasonRequested=False
        
        self.location = ""
        self._myHasLocation=False
        self._myLocationRequested=False
        


    def copyFrom (self, other):

        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        
        self.location=other.location
        self._myHasLocation=other._myHasLocation
        self._myLocationRequested=other._myLocationRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isOperationalStatusRequested():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        if self.isOperationalStatusReasonRequested():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        
        if self.isLocationRequested():
            self.location=other.location
            self._myHasLocation=other._myHasLocation
            self._myLocationRequested=other._myLocationRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasOperationalStatus():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        if other.hasOperationalStatusReason():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        
        if other.hasLocation():
            self.location=other.location
            self._myHasLocation=other._myHasLocation
            self._myLocationRequested=other._myLocationRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        
        self.location=other.location
        self._myHasLocation=other._myHasLocation
        


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

    def hasOperationalStatus (self):
        return self._myHasOperationalStatus

    def hasOperationalStatusReason (self):
        return self._myHasOperationalStatusReason

    def hasLocation (self):
        return self._myHasLocation




    # setHas...() methods

    def setHasOperationalStatus (self):
        self._myHasOperationalStatus=True

    def setHasOperationalStatusReason (self):
        self._myHasOperationalStatusReason=True

    def setHasLocation (self):
        self._myHasLocation=True




    # isRequested...() methods

    def isOperationalStatusRequested (self):
        return self._myOperationalStatusRequested

    def isOperationalStatusReasonRequested (self):
        return self._myOperationalStatusReasonRequested

    def isLocationRequested (self):
        return self._myLocationRequested




    # setRequested...() methods

    def setOperationalStatusRequested (self):
        self._myOperationalStatusRequested=True

    def setOperationalStatusReasonRequested (self):
        self._myOperationalStatusReasonRequested=True

    def setLocationRequested (self):
        self._myLocationRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myOperationalStatusRequested:
            x = "+OperationalStatus="
            if self._myHasOperationalStatus:
                leafStr = str(self.operationalStatus)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOperationalStatusReasonRequested:
            x = "+OperationalStatusReason="
            if self._myHasOperationalStatusReason:
                leafStr = str(self.operationalStatusReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myLocationRequested:
            x = "+Location="
            if self._myHasLocation:
                leafStr = str(self.location)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+OperationalStatus="
        if self._myHasOperationalStatus:
            leafStr = str(self.operationalStatus)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOperationalStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OperationalStatusReason="
        if self._myHasOperationalStatusReason:
            leafStr = str(self.operationalStatusReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOperationalStatusReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Location="
        if self._myHasLocation:
            leafStr = str(self.location)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myLocationRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setOperationalStatusRequested()
        self.setOperationalStatusReasonRequested()
        self.setLocationRequested()
        
        


    def setOperationalStatus (self, operationalStatus):
        self.operationalStatus = operationalStatus
        self.setHasOperationalStatus()

    def setOperationalStatusReason (self, operationalStatusReason):
        self.operationalStatusReason = operationalStatusReason
        self.setHasOperationalStatusReason()

    def setLocation (self, location):
        self.location = location
        self.setHasLocation()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "platform", 
            "isCurrent": false
        }, 
        {
            "namespace": "fans", 
            "isCurrent": false
        }, 
        {
            "namespace": "fan", 
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
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatus", 
            "yangName": "operational-status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "operationalStatusReason", 
            "yangName": "operational-status-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "location", 
            "yangName": "location", 
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
            "qwilt_tech_platform_fans"
        ]
    }, 
    "createTime": "2013"
}
"""


