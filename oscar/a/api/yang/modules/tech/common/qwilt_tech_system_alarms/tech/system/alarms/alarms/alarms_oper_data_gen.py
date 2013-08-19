


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



from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.qwilt_tech_system_alarms_module_gen import TestAlarmReasonType


class AlarmsOperData (object):

    def __init__ (self):

        self.testAlarmReason = TestAlarmReasonType.kNone
        self._myHasTestAlarmReason=False
        self._myTestAlarmReasonRequested=False
        
        self.testAlarm = False
        self._myHasTestAlarm=False
        self._myTestAlarmRequested=False
        


    def copyFrom (self, other):

        self.testAlarmReason=other.testAlarmReason
        self._myHasTestAlarmReason=other._myHasTestAlarmReason
        self._myTestAlarmReasonRequested=other._myTestAlarmReasonRequested
        
        self.testAlarm=other.testAlarm
        self._myHasTestAlarm=other._myHasTestAlarm
        self._myTestAlarmRequested=other._myTestAlarmRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isTestAlarmReasonRequested():
            self.testAlarmReason=other.testAlarmReason
            self._myHasTestAlarmReason=other._myHasTestAlarmReason
            self._myTestAlarmReasonRequested=other._myTestAlarmReasonRequested
        
        if self.isTestAlarmRequested():
            self.testAlarm=other.testAlarm
            self._myHasTestAlarm=other._myHasTestAlarm
            self._myTestAlarmRequested=other._myTestAlarmRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasTestAlarmReason():
            self.testAlarmReason=other.testAlarmReason
            self._myHasTestAlarmReason=other._myHasTestAlarmReason
            self._myTestAlarmReasonRequested=other._myTestAlarmReasonRequested
        
        if other.hasTestAlarm():
            self.testAlarm=other.testAlarm
            self._myHasTestAlarm=other._myHasTestAlarm
            self._myTestAlarmRequested=other._myTestAlarmRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.testAlarmReason=other.testAlarmReason
        self._myHasTestAlarmReason=other._myHasTestAlarmReason
        
        self.testAlarm=other.testAlarm
        self._myHasTestAlarm=other._myHasTestAlarm
        


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

    def hasTestAlarmReason (self):
        return self._myHasTestAlarmReason

    def hasTestAlarm (self):
        return self._myHasTestAlarm




    # setHas...() methods

    def setHasTestAlarmReason (self):
        self._myHasTestAlarmReason=True

    def setHasTestAlarm (self):
        self._myHasTestAlarm=True




    # isRequested...() methods

    def isTestAlarmReasonRequested (self):
        return self._myTestAlarmReasonRequested

    def isTestAlarmRequested (self):
        return self._myTestAlarmRequested




    # setRequested...() methods

    def setTestAlarmReasonRequested (self):
        self._myTestAlarmReasonRequested=True

    def setTestAlarmRequested (self):
        self._myTestAlarmRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myTestAlarmReasonRequested:
            x = "+TestAlarmReason="
            if self._myHasTestAlarmReason:
                leafStr = str(self.testAlarmReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTestAlarmRequested:
            x = "+TestAlarm="
            if self._myHasTestAlarm:
                leafStr = str(self.testAlarm)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{AlarmsOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+TestAlarmReason="
        if self._myHasTestAlarmReason:
            leafStr = str(self.testAlarmReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTestAlarmReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TestAlarm="
        if self._myHasTestAlarm:
            leafStr = str(self.testAlarm)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTestAlarmRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{AlarmsOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setTestAlarmReasonRequested()
        self.setTestAlarmRequested()
        
        


    def setTestAlarmReason (self, testAlarmReason):
        self.testAlarmReason = testAlarmReason
        self.setHasTestAlarmReason()

    def setTestAlarm (self, testAlarm):
        self.testAlarm = testAlarm
        self.setHasTestAlarm()


"""
Extracted from the below data: 
{
    "node": {
        "className": "AlarmsOperData", 
        "namespace": "alarms", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.alarms.alarms_oper_data_gen import AlarmsOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "system", 
            "isCurrent": false
        }, 
        {
            "namespace": "alarms", 
            "isCurrent": false
        }, 
        {
            "namespace": "alarms", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "testAlarmReason", 
            "yangName": "test-alarm-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "testAlarm", 
            "yangName": "test-alarm", 
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
            "qwilt_tech_system_alarms"
        ]
    }, 
    "createTime": "2013"
}
"""


