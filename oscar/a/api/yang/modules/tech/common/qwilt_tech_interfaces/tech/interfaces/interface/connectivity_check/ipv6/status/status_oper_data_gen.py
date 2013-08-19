


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



from a.api.yang.modules.tech.common.qwilt_tech_interfaces_types.qwilt_tech_interfaces_types_module_gen import ConnectivityCheckIpv6MethodType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import ConnectivityOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import ConnectivityOperationalStatusType


class StatusOperData (object):

    def __init__ (self):

        self.actualMethod = ConnectivityCheckIpv6MethodType.kPing
        self._myHasActualMethod=False
        self._myActualMethodRequested=False
        
        self.operationalStatus = ConnectivityOperationalStatusType.kDown
        self._myHasOperationalStatus=False
        self._myOperationalStatusRequested=False
        
        self.operationalStatusReason = ConnectivityOperationalStatusReasonType.kLinkOperationalStatusDown
        self._myHasOperationalStatusReason=False
        self._myOperationalStatusReasonRequested=False
        


    def copyFrom (self, other):

        self.actualMethod=other.actualMethod
        self._myHasActualMethod=other._myHasActualMethod
        self._myActualMethodRequested=other._myActualMethodRequested
        
        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isActualMethodRequested():
            self.actualMethod=other.actualMethod
            self._myHasActualMethod=other._myHasActualMethod
            self._myActualMethodRequested=other._myActualMethodRequested
        
        if self.isOperationalStatusRequested():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        if self.isOperationalStatusReasonRequested():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasActualMethod():
            self.actualMethod=other.actualMethod
            self._myHasActualMethod=other._myHasActualMethod
            self._myActualMethodRequested=other._myActualMethodRequested
        
        if other.hasOperationalStatus():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        if other.hasOperationalStatusReason():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.actualMethod=other.actualMethod
        self._myHasActualMethod=other._myHasActualMethod
        
        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        


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

    def hasActualMethod (self):
        return self._myHasActualMethod

    def hasOperationalStatus (self):
        return self._myHasOperationalStatus

    def hasOperationalStatusReason (self):
        return self._myHasOperationalStatusReason




    # setHas...() methods

    def setHasActualMethod (self):
        self._myHasActualMethod=True

    def setHasOperationalStatus (self):
        self._myHasOperationalStatus=True

    def setHasOperationalStatusReason (self):
        self._myHasOperationalStatusReason=True




    # isRequested...() methods

    def isActualMethodRequested (self):
        return self._myActualMethodRequested

    def isOperationalStatusRequested (self):
        return self._myOperationalStatusRequested

    def isOperationalStatusReasonRequested (self):
        return self._myOperationalStatusReasonRequested




    # setRequested...() methods

    def setActualMethodRequested (self):
        self._myActualMethodRequested=True

    def setOperationalStatusRequested (self):
        self._myOperationalStatusRequested=True

    def setOperationalStatusReasonRequested (self):
        self._myOperationalStatusReasonRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myActualMethodRequested:
            x = "+ActualMethod="
            if self._myHasActualMethod:
                leafStr = str(self.actualMethod)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

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


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ActualMethod="
        if self._myHasActualMethod:
            leafStr = str(self.actualMethod)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myActualMethodRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

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


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setActualMethodRequested()
        self.setOperationalStatusRequested()
        self.setOperationalStatusReasonRequested()
        
        


    def setActualMethod (self, actualMethod):
        self.actualMethod = actualMethod
        self.setHasActualMethod()

    def setOperationalStatus (self, operationalStatus):
        self.operationalStatus = operationalStatus
        self.setHasOperationalStatus()

    def setOperationalStatusReason (self, operationalStatusReason):
        self.operationalStatusReason = operationalStatusReason
        self.setHasOperationalStatusReason()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv6.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
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
            "namespace": "connectivity_check", 
            "isCurrent": false
        }, 
        {
            "namespace": "ipv6", 
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
            "memberName": "actualMethod", 
            "yangName": "actual-method", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "createTime": "2013"
}
"""


