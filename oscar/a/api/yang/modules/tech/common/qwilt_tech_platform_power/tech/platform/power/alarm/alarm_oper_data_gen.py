


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerNoRedundancyReasonType


class AlarmOperData (object):

    def __init__ (self):

        self.noRedundancyReason = PowerNoRedundancyReasonType.kNone
        self._myHasNoRedundancyReason=False
        self._myNoRedundancyReasonRequested=False
        
        self.noRedundancy = False
        self._myHasNoRedundancy=False
        self._myNoRedundancyRequested=False
        


    def copyFrom (self, other):

        self.noRedundancyReason=other.noRedundancyReason
        self._myHasNoRedundancyReason=other._myHasNoRedundancyReason
        self._myNoRedundancyReasonRequested=other._myNoRedundancyReasonRequested
        
        self.noRedundancy=other.noRedundancy
        self._myHasNoRedundancy=other._myHasNoRedundancy
        self._myNoRedundancyRequested=other._myNoRedundancyRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isNoRedundancyReasonRequested():
            self.noRedundancyReason=other.noRedundancyReason
            self._myHasNoRedundancyReason=other._myHasNoRedundancyReason
            self._myNoRedundancyReasonRequested=other._myNoRedundancyReasonRequested
        
        if self.isNoRedundancyRequested():
            self.noRedundancy=other.noRedundancy
            self._myHasNoRedundancy=other._myHasNoRedundancy
            self._myNoRedundancyRequested=other._myNoRedundancyRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasNoRedundancyReason():
            self.noRedundancyReason=other.noRedundancyReason
            self._myHasNoRedundancyReason=other._myHasNoRedundancyReason
            self._myNoRedundancyReasonRequested=other._myNoRedundancyReasonRequested
        
        if other.hasNoRedundancy():
            self.noRedundancy=other.noRedundancy
            self._myHasNoRedundancy=other._myHasNoRedundancy
            self._myNoRedundancyRequested=other._myNoRedundancyRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.noRedundancyReason=other.noRedundancyReason
        self._myHasNoRedundancyReason=other._myHasNoRedundancyReason
        
        self.noRedundancy=other.noRedundancy
        self._myHasNoRedundancy=other._myHasNoRedundancy
        


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

    def hasNoRedundancyReason (self):
        return self._myHasNoRedundancyReason

    def hasNoRedundancy (self):
        return self._myHasNoRedundancy




    # setHas...() methods

    def setHasNoRedundancyReason (self):
        self._myHasNoRedundancyReason=True

    def setHasNoRedundancy (self):
        self._myHasNoRedundancy=True




    # isRequested...() methods

    def isNoRedundancyReasonRequested (self):
        return self._myNoRedundancyReasonRequested

    def isNoRedundancyRequested (self):
        return self._myNoRedundancyRequested




    # setRequested...() methods

    def setNoRedundancyReasonRequested (self):
        self._myNoRedundancyReasonRequested=True

    def setNoRedundancyRequested (self):
        self._myNoRedundancyRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myNoRedundancyReasonRequested:
            x = "+NoRedundancyReason="
            if self._myHasNoRedundancyReason:
                leafStr = str(self.noRedundancyReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNoRedundancyRequested:
            x = "+NoRedundancy="
            if self._myHasNoRedundancy:
                leafStr = str(self.noRedundancy)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{AlarmOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+NoRedundancyReason="
        if self._myHasNoRedundancyReason:
            leafStr = str(self.noRedundancyReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNoRedundancyReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+NoRedundancy="
        if self._myHasNoRedundancy:
            leafStr = str(self.noRedundancy)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNoRedundancyRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{AlarmOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setNoRedundancyReasonRequested()
        self.setNoRedundancyRequested()
        
        


    def setNoRedundancyReason (self, noRedundancyReason):
        self.noRedundancyReason = noRedundancyReason
        self.setHasNoRedundancyReason()

    def setNoRedundancy (self, noRedundancy):
        self.noRedundancy = noRedundancy
        self.setHasNoRedundancy()


"""
Extracted from the below data: 
{
    "node": {
        "className": "AlarmOperData", 
        "namespace": "alarm", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.alarm.alarm_oper_data_gen import AlarmOperData"
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
            "namespace": "alarm", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "noRedundancyReason", 
            "yangName": "no-redundancy-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "noRedundancy", 
            "yangName": "no-redundancy", 
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


