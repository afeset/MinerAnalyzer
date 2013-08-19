


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanFailureReasonType


class AlarmOperData (object):

    def __init__ (self):

        self.fanFailureReason = FanFailureReasonType.kNone
        self._myHasFanFailureReason=False
        self._myFanFailureReasonRequested=False
        
        self.fanFailure = False
        self._myHasFanFailure=False
        self._myFanFailureRequested=False
        


    def copyFrom (self, other):

        self.fanFailureReason=other.fanFailureReason
        self._myHasFanFailureReason=other._myHasFanFailureReason
        self._myFanFailureReasonRequested=other._myFanFailureReasonRequested
        
        self.fanFailure=other.fanFailure
        self._myHasFanFailure=other._myHasFanFailure
        self._myFanFailureRequested=other._myFanFailureRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isFanFailureReasonRequested():
            self.fanFailureReason=other.fanFailureReason
            self._myHasFanFailureReason=other._myHasFanFailureReason
            self._myFanFailureReasonRequested=other._myFanFailureReasonRequested
        
        if self.isFanFailureRequested():
            self.fanFailure=other.fanFailure
            self._myHasFanFailure=other._myHasFanFailure
            self._myFanFailureRequested=other._myFanFailureRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasFanFailureReason():
            self.fanFailureReason=other.fanFailureReason
            self._myHasFanFailureReason=other._myHasFanFailureReason
            self._myFanFailureReasonRequested=other._myFanFailureReasonRequested
        
        if other.hasFanFailure():
            self.fanFailure=other.fanFailure
            self._myHasFanFailure=other._myHasFanFailure
            self._myFanFailureRequested=other._myFanFailureRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.fanFailureReason=other.fanFailureReason
        self._myHasFanFailureReason=other._myHasFanFailureReason
        
        self.fanFailure=other.fanFailure
        self._myHasFanFailure=other._myHasFanFailure
        


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

    def hasFanFailureReason (self):
        return self._myHasFanFailureReason

    def hasFanFailure (self):
        return self._myHasFanFailure




    # setHas...() methods

    def setHasFanFailureReason (self):
        self._myHasFanFailureReason=True

    def setHasFanFailure (self):
        self._myHasFanFailure=True




    # isRequested...() methods

    def isFanFailureReasonRequested (self):
        return self._myFanFailureReasonRequested

    def isFanFailureRequested (self):
        return self._myFanFailureRequested




    # setRequested...() methods

    def setFanFailureReasonRequested (self):
        self._myFanFailureReasonRequested=True

    def setFanFailureRequested (self):
        self._myFanFailureRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myFanFailureReasonRequested:
            x = "+FanFailureReason="
            if self._myHasFanFailureReason:
                leafStr = str(self.fanFailureReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myFanFailureRequested:
            x = "+FanFailure="
            if self._myHasFanFailure:
                leafStr = str(self.fanFailure)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{AlarmOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+FanFailureReason="
        if self._myHasFanFailureReason:
            leafStr = str(self.fanFailureReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFanFailureReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+FanFailure="
        if self._myHasFanFailure:
            leafStr = str(self.fanFailure)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myFanFailureRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{AlarmOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setFanFailureReasonRequested()
        self.setFanFailureRequested()
        
        


    def setFanFailureReason (self, fanFailureReason):
        self.fanFailureReason = fanFailureReason
        self.setHasFanFailureReason()

    def setFanFailure (self, fanFailure):
        self.fanFailure = fanFailure
        self.setHasFanFailure()


"""
Extracted from the below data: 
{
    "node": {
        "className": "AlarmOperData", 
        "namespace": "alarm", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.alarm.alarm_oper_data_gen import AlarmOperData"
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
            "namespace": "alarm", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "fanFailureReason", 
            "yangName": "fan-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "fanFailure", 
            "yangName": "fan-failure", 
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


