


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_power.qwilt_tech_platform_power_module_gen import PowerSupplyFailureReasonType


class AlarmOperData (object):

    def __init__ (self):

        self.powerSupplyFailure = False
        self._myHasPowerSupplyFailure=False
        self._myPowerSupplyFailureRequested=False
        
        self.powerSupplyFailureReason = PowerSupplyFailureReasonType.kPowerSourceLost
        self._myHasPowerSupplyFailureReason=False
        self._myPowerSupplyFailureReasonRequested=False
        


    def copyFrom (self, other):

        self.powerSupplyFailure=other.powerSupplyFailure
        self._myHasPowerSupplyFailure=other._myHasPowerSupplyFailure
        self._myPowerSupplyFailureRequested=other._myPowerSupplyFailureRequested
        
        self.powerSupplyFailureReason=other.powerSupplyFailureReason
        self._myHasPowerSupplyFailureReason=other._myHasPowerSupplyFailureReason
        self._myPowerSupplyFailureReasonRequested=other._myPowerSupplyFailureReasonRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isPowerSupplyFailureRequested():
            self.powerSupplyFailure=other.powerSupplyFailure
            self._myHasPowerSupplyFailure=other._myHasPowerSupplyFailure
            self._myPowerSupplyFailureRequested=other._myPowerSupplyFailureRequested
        
        if self.isPowerSupplyFailureReasonRequested():
            self.powerSupplyFailureReason=other.powerSupplyFailureReason
            self._myHasPowerSupplyFailureReason=other._myHasPowerSupplyFailureReason
            self._myPowerSupplyFailureReasonRequested=other._myPowerSupplyFailureReasonRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasPowerSupplyFailure():
            self.powerSupplyFailure=other.powerSupplyFailure
            self._myHasPowerSupplyFailure=other._myHasPowerSupplyFailure
            self._myPowerSupplyFailureRequested=other._myPowerSupplyFailureRequested
        
        if other.hasPowerSupplyFailureReason():
            self.powerSupplyFailureReason=other.powerSupplyFailureReason
            self._myHasPowerSupplyFailureReason=other._myHasPowerSupplyFailureReason
            self._myPowerSupplyFailureReasonRequested=other._myPowerSupplyFailureReasonRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.powerSupplyFailure=other.powerSupplyFailure
        self._myHasPowerSupplyFailure=other._myHasPowerSupplyFailure
        
        self.powerSupplyFailureReason=other.powerSupplyFailureReason
        self._myHasPowerSupplyFailureReason=other._myHasPowerSupplyFailureReason
        


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

    def hasPowerSupplyFailure (self):
        return self._myHasPowerSupplyFailure

    def hasPowerSupplyFailureReason (self):
        return self._myHasPowerSupplyFailureReason




    # setHas...() methods

    def setHasPowerSupplyFailure (self):
        self._myHasPowerSupplyFailure=True

    def setHasPowerSupplyFailureReason (self):
        self._myHasPowerSupplyFailureReason=True




    # isRequested...() methods

    def isPowerSupplyFailureRequested (self):
        return self._myPowerSupplyFailureRequested

    def isPowerSupplyFailureReasonRequested (self):
        return self._myPowerSupplyFailureReasonRequested




    # setRequested...() methods

    def setPowerSupplyFailureRequested (self):
        self._myPowerSupplyFailureRequested=True

    def setPowerSupplyFailureReasonRequested (self):
        self._myPowerSupplyFailureReasonRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myPowerSupplyFailureRequested:
            x = "+PowerSupplyFailure="
            if self._myHasPowerSupplyFailure:
                leafStr = str(self.powerSupplyFailure)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPowerSupplyFailureReasonRequested:
            x = "+PowerSupplyFailureReason="
            if self._myHasPowerSupplyFailureReason:
                leafStr = str(self.powerSupplyFailureReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{AlarmOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+PowerSupplyFailure="
        if self._myHasPowerSupplyFailure:
            leafStr = str(self.powerSupplyFailure)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPowerSupplyFailureRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PowerSupplyFailureReason="
        if self._myHasPowerSupplyFailureReason:
            leafStr = str(self.powerSupplyFailureReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPowerSupplyFailureReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{AlarmOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setPowerSupplyFailureRequested()
        self.setPowerSupplyFailureReasonRequested()
        
        


    def setPowerSupplyFailure (self, powerSupplyFailure):
        self.powerSupplyFailure = powerSupplyFailure
        self.setHasPowerSupplyFailure()

    def setPowerSupplyFailureReason (self, powerSupplyFailureReason):
        self.powerSupplyFailureReason = powerSupplyFailureReason
        self.setHasPowerSupplyFailureReason()


"""
Extracted from the below data: 
{
    "node": {
        "className": "AlarmOperData", 
        "namespace": "alarm", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_power.tech.platform.power.power_supply.alarm.alarm_oper_data_gen import AlarmOperData"
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
            "namespace": "power_supply", 
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
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "powerSupplyFailure", 
            "yangName": "power-supply-failure", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "powerSupplyFailureReason", 
            "yangName": "power-supply-failure-reason", 
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


