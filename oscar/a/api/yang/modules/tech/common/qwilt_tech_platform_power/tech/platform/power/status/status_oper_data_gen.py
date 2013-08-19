


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerRedundancyStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerOperationalStatusReasonType


class StatusOperData (object):

    def __init__ (self):

        self.redundancyStatusRaw = ""
        self._myHasRedundancyStatusRaw=False
        self._myRedundancyStatusRawRequested=False
        
        self.operationalStatus = PowerOperationalStatusType.kDegraded
        self._myHasOperationalStatus=False
        self._myOperationalStatusRequested=False
        
        self.redundancyStatus = PowerRedundancyStatusType.kUnknown
        self._myHasRedundancyStatus=False
        self._myRedundancyStatusRequested=False
        
        self.operationalStatusReason = PowerOperationalStatusReasonType.kNone
        self._myHasOperationalStatusReason=False
        self._myOperationalStatusReasonRequested=False
        


    def copyFrom (self, other):

        self.redundancyStatusRaw=other.redundancyStatusRaw
        self._myHasRedundancyStatusRaw=other._myHasRedundancyStatusRaw
        self._myRedundancyStatusRawRequested=other._myRedundancyStatusRawRequested
        
        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        self.redundancyStatus=other.redundancyStatus
        self._myHasRedundancyStatus=other._myHasRedundancyStatus
        self._myRedundancyStatusRequested=other._myRedundancyStatusRequested
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isRedundancyStatusRawRequested():
            self.redundancyStatusRaw=other.redundancyStatusRaw
            self._myHasRedundancyStatusRaw=other._myHasRedundancyStatusRaw
            self._myRedundancyStatusRawRequested=other._myRedundancyStatusRawRequested
        
        if self.isOperationalStatusRequested():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        if self.isRedundancyStatusRequested():
            self.redundancyStatus=other.redundancyStatus
            self._myHasRedundancyStatus=other._myHasRedundancyStatus
            self._myRedundancyStatusRequested=other._myRedundancyStatusRequested
        
        if self.isOperationalStatusReasonRequested():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasRedundancyStatusRaw():
            self.redundancyStatusRaw=other.redundancyStatusRaw
            self._myHasRedundancyStatusRaw=other._myHasRedundancyStatusRaw
            self._myRedundancyStatusRawRequested=other._myRedundancyStatusRawRequested
        
        if other.hasOperationalStatus():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        if other.hasRedundancyStatus():
            self.redundancyStatus=other.redundancyStatus
            self._myHasRedundancyStatus=other._myHasRedundancyStatus
            self._myRedundancyStatusRequested=other._myRedundancyStatusRequested
        
        if other.hasOperationalStatusReason():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.redundancyStatusRaw=other.redundancyStatusRaw
        self._myHasRedundancyStatusRaw=other._myHasRedundancyStatusRaw
        
        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        
        self.redundancyStatus=other.redundancyStatus
        self._myHasRedundancyStatus=other._myHasRedundancyStatus
        
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

    def hasRedundancyStatusRaw (self):
        return self._myHasRedundancyStatusRaw

    def hasOperationalStatus (self):
        return self._myHasOperationalStatus

    def hasRedundancyStatus (self):
        return self._myHasRedundancyStatus

    def hasOperationalStatusReason (self):
        return self._myHasOperationalStatusReason




    # setHas...() methods

    def setHasRedundancyStatusRaw (self):
        self._myHasRedundancyStatusRaw=True

    def setHasOperationalStatus (self):
        self._myHasOperationalStatus=True

    def setHasRedundancyStatus (self):
        self._myHasRedundancyStatus=True

    def setHasOperationalStatusReason (self):
        self._myHasOperationalStatusReason=True




    # isRequested...() methods

    def isRedundancyStatusRawRequested (self):
        return self._myRedundancyStatusRawRequested

    def isOperationalStatusRequested (self):
        return self._myOperationalStatusRequested

    def isRedundancyStatusRequested (self):
        return self._myRedundancyStatusRequested

    def isOperationalStatusReasonRequested (self):
        return self._myOperationalStatusReasonRequested




    # setRequested...() methods

    def setRedundancyStatusRawRequested (self):
        self._myRedundancyStatusRawRequested=True

    def setOperationalStatusRequested (self):
        self._myOperationalStatusRequested=True

    def setRedundancyStatusRequested (self):
        self._myRedundancyStatusRequested=True

    def setOperationalStatusReasonRequested (self):
        self._myOperationalStatusReasonRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myRedundancyStatusRawRequested:
            x = "+RedundancyStatusRaw="
            if self._myHasRedundancyStatusRaw:
                leafStr = str(self.redundancyStatusRaw)
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
        if self._myRedundancyStatusRequested:
            x = "+RedundancyStatus="
            if self._myHasRedundancyStatus:
                leafStr = str(self.redundancyStatus)
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
        x = "+RedundancyStatusRaw="
        if self._myHasRedundancyStatusRaw:
            leafStr = str(self.redundancyStatusRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRedundancyStatusRawRequested:
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
        x = "+RedundancyStatus="
        if self._myHasRedundancyStatus:
            leafStr = str(self.redundancyStatus)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRedundancyStatusRequested:
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
        self.setRedundancyStatusRawRequested()
        self.setOperationalStatusRequested()
        self.setRedundancyStatusRequested()
        self.setOperationalStatusReasonRequested()
        
        


    def setRedundancyStatusRaw (self, redundancyStatusRaw):
        self.redundancyStatusRaw = redundancyStatusRaw
        self.setHasRedundancyStatusRaw()

    def setOperationalStatus (self, operationalStatus):
        self.operationalStatus = operationalStatus
        self.setHasOperationalStatus()

    def setRedundancyStatus (self, redundancyStatus):
        self.redundancyStatus = redundancyStatus
        self.setHasRedundancyStatus()

    def setOperationalStatusReason (self, operationalStatusReason):
        self.operationalStatusReason = operationalStatusReason
        self.setHasOperationalStatusReason()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.status.status_oper_data_gen import StatusOperData"
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
            "namespace": "power", 
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
            "memberName": "redundancyStatusRaw", 
            "yangName": "redundancy-status-raw", 
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
            "memberName": "redundancyStatus", 
            "yangName": "redundancy-status", 
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
            "qwilt_tech_platform_power"
        ]
    }, 
    "createTime": "2013"
}
"""


