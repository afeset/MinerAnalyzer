


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



from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceIpv6ConnectivityFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceFailureReasonType
from a.api.yang.modules.tech.common.qwilt_tech_interfaces.qwilt_tech_interfaces_module_gen import InterfaceIpv4ConnectivityFailureReasonType


class AlarmsOperData (object):

    def __init__ (self):

        self.interfaceFailureReason = InterfaceFailureReasonType.kNone
        self._myHasInterfaceFailureReason=False
        self._myInterfaceFailureReasonRequested=False
        
        self.interfaceIpv6ConnectivityFailureAlarm = False
        self._myHasInterfaceIpv6ConnectivityFailureAlarm=False
        self._myInterfaceIpv6ConnectivityFailureAlarmRequested=False
        
        self.interfaceFailureAlarm = False
        self._myHasInterfaceFailureAlarm=False
        self._myInterfaceFailureAlarmRequested=False
        
        self.interfaceIpv4ConnectivityFailureAlarm = False
        self._myHasInterfaceIpv4ConnectivityFailureAlarm=False
        self._myInterfaceIpv4ConnectivityFailureAlarmRequested=False
        
        self.interfaceIpv4ConnectivityFailureReason = InterfaceIpv4ConnectivityFailureReasonType.kNone
        self._myHasInterfaceIpv4ConnectivityFailureReason=False
        self._myInterfaceIpv4ConnectivityFailureReasonRequested=False
        
        self.interfaceIpv6ConnectivityFailureReason = InterfaceIpv6ConnectivityFailureReasonType.kNone
        self._myHasInterfaceIpv6ConnectivityFailureReason=False
        self._myInterfaceIpv6ConnectivityFailureReasonRequested=False
        


    def copyFrom (self, other):

        self.interfaceFailureReason=other.interfaceFailureReason
        self._myHasInterfaceFailureReason=other._myHasInterfaceFailureReason
        self._myInterfaceFailureReasonRequested=other._myInterfaceFailureReasonRequested
        
        self.interfaceIpv6ConnectivityFailureAlarm=other.interfaceIpv6ConnectivityFailureAlarm
        self._myHasInterfaceIpv6ConnectivityFailureAlarm=other._myHasInterfaceIpv6ConnectivityFailureAlarm
        self._myInterfaceIpv6ConnectivityFailureAlarmRequested=other._myInterfaceIpv6ConnectivityFailureAlarmRequested
        
        self.interfaceFailureAlarm=other.interfaceFailureAlarm
        self._myHasInterfaceFailureAlarm=other._myHasInterfaceFailureAlarm
        self._myInterfaceFailureAlarmRequested=other._myInterfaceFailureAlarmRequested
        
        self.interfaceIpv4ConnectivityFailureAlarm=other.interfaceIpv4ConnectivityFailureAlarm
        self._myHasInterfaceIpv4ConnectivityFailureAlarm=other._myHasInterfaceIpv4ConnectivityFailureAlarm
        self._myInterfaceIpv4ConnectivityFailureAlarmRequested=other._myInterfaceIpv4ConnectivityFailureAlarmRequested
        
        self.interfaceIpv4ConnectivityFailureReason=other.interfaceIpv4ConnectivityFailureReason
        self._myHasInterfaceIpv4ConnectivityFailureReason=other._myHasInterfaceIpv4ConnectivityFailureReason
        self._myInterfaceIpv4ConnectivityFailureReasonRequested=other._myInterfaceIpv4ConnectivityFailureReasonRequested
        
        self.interfaceIpv6ConnectivityFailureReason=other.interfaceIpv6ConnectivityFailureReason
        self._myHasInterfaceIpv6ConnectivityFailureReason=other._myHasInterfaceIpv6ConnectivityFailureReason
        self._myInterfaceIpv6ConnectivityFailureReasonRequested=other._myInterfaceIpv6ConnectivityFailureReasonRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isInterfaceFailureReasonRequested():
            self.interfaceFailureReason=other.interfaceFailureReason
            self._myHasInterfaceFailureReason=other._myHasInterfaceFailureReason
            self._myInterfaceFailureReasonRequested=other._myInterfaceFailureReasonRequested
        
        if self.isInterfaceIpv6ConnectivityFailureAlarmRequested():
            self.interfaceIpv6ConnectivityFailureAlarm=other.interfaceIpv6ConnectivityFailureAlarm
            self._myHasInterfaceIpv6ConnectivityFailureAlarm=other._myHasInterfaceIpv6ConnectivityFailureAlarm
            self._myInterfaceIpv6ConnectivityFailureAlarmRequested=other._myInterfaceIpv6ConnectivityFailureAlarmRequested
        
        if self.isInterfaceFailureAlarmRequested():
            self.interfaceFailureAlarm=other.interfaceFailureAlarm
            self._myHasInterfaceFailureAlarm=other._myHasInterfaceFailureAlarm
            self._myInterfaceFailureAlarmRequested=other._myInterfaceFailureAlarmRequested
        
        if self.isInterfaceIpv4ConnectivityFailureAlarmRequested():
            self.interfaceIpv4ConnectivityFailureAlarm=other.interfaceIpv4ConnectivityFailureAlarm
            self._myHasInterfaceIpv4ConnectivityFailureAlarm=other._myHasInterfaceIpv4ConnectivityFailureAlarm
            self._myInterfaceIpv4ConnectivityFailureAlarmRequested=other._myInterfaceIpv4ConnectivityFailureAlarmRequested
        
        if self.isInterfaceIpv4ConnectivityFailureReasonRequested():
            self.interfaceIpv4ConnectivityFailureReason=other.interfaceIpv4ConnectivityFailureReason
            self._myHasInterfaceIpv4ConnectivityFailureReason=other._myHasInterfaceIpv4ConnectivityFailureReason
            self._myInterfaceIpv4ConnectivityFailureReasonRequested=other._myInterfaceIpv4ConnectivityFailureReasonRequested
        
        if self.isInterfaceIpv6ConnectivityFailureReasonRequested():
            self.interfaceIpv6ConnectivityFailureReason=other.interfaceIpv6ConnectivityFailureReason
            self._myHasInterfaceIpv6ConnectivityFailureReason=other._myHasInterfaceIpv6ConnectivityFailureReason
            self._myInterfaceIpv6ConnectivityFailureReasonRequested=other._myInterfaceIpv6ConnectivityFailureReasonRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasInterfaceFailureReason():
            self.interfaceFailureReason=other.interfaceFailureReason
            self._myHasInterfaceFailureReason=other._myHasInterfaceFailureReason
            self._myInterfaceFailureReasonRequested=other._myInterfaceFailureReasonRequested
        
        if other.hasInterfaceIpv6ConnectivityFailureAlarm():
            self.interfaceIpv6ConnectivityFailureAlarm=other.interfaceIpv6ConnectivityFailureAlarm
            self._myHasInterfaceIpv6ConnectivityFailureAlarm=other._myHasInterfaceIpv6ConnectivityFailureAlarm
            self._myInterfaceIpv6ConnectivityFailureAlarmRequested=other._myInterfaceIpv6ConnectivityFailureAlarmRequested
        
        if other.hasInterfaceFailureAlarm():
            self.interfaceFailureAlarm=other.interfaceFailureAlarm
            self._myHasInterfaceFailureAlarm=other._myHasInterfaceFailureAlarm
            self._myInterfaceFailureAlarmRequested=other._myInterfaceFailureAlarmRequested
        
        if other.hasInterfaceIpv4ConnectivityFailureAlarm():
            self.interfaceIpv4ConnectivityFailureAlarm=other.interfaceIpv4ConnectivityFailureAlarm
            self._myHasInterfaceIpv4ConnectivityFailureAlarm=other._myHasInterfaceIpv4ConnectivityFailureAlarm
            self._myInterfaceIpv4ConnectivityFailureAlarmRequested=other._myInterfaceIpv4ConnectivityFailureAlarmRequested
        
        if other.hasInterfaceIpv4ConnectivityFailureReason():
            self.interfaceIpv4ConnectivityFailureReason=other.interfaceIpv4ConnectivityFailureReason
            self._myHasInterfaceIpv4ConnectivityFailureReason=other._myHasInterfaceIpv4ConnectivityFailureReason
            self._myInterfaceIpv4ConnectivityFailureReasonRequested=other._myInterfaceIpv4ConnectivityFailureReasonRequested
        
        if other.hasInterfaceIpv6ConnectivityFailureReason():
            self.interfaceIpv6ConnectivityFailureReason=other.interfaceIpv6ConnectivityFailureReason
            self._myHasInterfaceIpv6ConnectivityFailureReason=other._myHasInterfaceIpv6ConnectivityFailureReason
            self._myInterfaceIpv6ConnectivityFailureReasonRequested=other._myInterfaceIpv6ConnectivityFailureReasonRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.interfaceFailureReason=other.interfaceFailureReason
        self._myHasInterfaceFailureReason=other._myHasInterfaceFailureReason
        
        self.interfaceIpv6ConnectivityFailureAlarm=other.interfaceIpv6ConnectivityFailureAlarm
        self._myHasInterfaceIpv6ConnectivityFailureAlarm=other._myHasInterfaceIpv6ConnectivityFailureAlarm
        
        self.interfaceFailureAlarm=other.interfaceFailureAlarm
        self._myHasInterfaceFailureAlarm=other._myHasInterfaceFailureAlarm
        
        self.interfaceIpv4ConnectivityFailureAlarm=other.interfaceIpv4ConnectivityFailureAlarm
        self._myHasInterfaceIpv4ConnectivityFailureAlarm=other._myHasInterfaceIpv4ConnectivityFailureAlarm
        
        self.interfaceIpv4ConnectivityFailureReason=other.interfaceIpv4ConnectivityFailureReason
        self._myHasInterfaceIpv4ConnectivityFailureReason=other._myHasInterfaceIpv4ConnectivityFailureReason
        
        self.interfaceIpv6ConnectivityFailureReason=other.interfaceIpv6ConnectivityFailureReason
        self._myHasInterfaceIpv6ConnectivityFailureReason=other._myHasInterfaceIpv6ConnectivityFailureReason
        


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

    def hasInterfaceFailureReason (self):
        return self._myHasInterfaceFailureReason

    def hasInterfaceIpv6ConnectivityFailureAlarm (self):
        return self._myHasInterfaceIpv6ConnectivityFailureAlarm

    def hasInterfaceFailureAlarm (self):
        return self._myHasInterfaceFailureAlarm

    def hasInterfaceIpv4ConnectivityFailureAlarm (self):
        return self._myHasInterfaceIpv4ConnectivityFailureAlarm

    def hasInterfaceIpv4ConnectivityFailureReason (self):
        return self._myHasInterfaceIpv4ConnectivityFailureReason

    def hasInterfaceIpv6ConnectivityFailureReason (self):
        return self._myHasInterfaceIpv6ConnectivityFailureReason




    # setHas...() methods

    def setHasInterfaceFailureReason (self):
        self._myHasInterfaceFailureReason=True

    def setHasInterfaceIpv6ConnectivityFailureAlarm (self):
        self._myHasInterfaceIpv6ConnectivityFailureAlarm=True

    def setHasInterfaceFailureAlarm (self):
        self._myHasInterfaceFailureAlarm=True

    def setHasInterfaceIpv4ConnectivityFailureAlarm (self):
        self._myHasInterfaceIpv4ConnectivityFailureAlarm=True

    def setHasInterfaceIpv4ConnectivityFailureReason (self):
        self._myHasInterfaceIpv4ConnectivityFailureReason=True

    def setHasInterfaceIpv6ConnectivityFailureReason (self):
        self._myHasInterfaceIpv6ConnectivityFailureReason=True




    # isRequested...() methods

    def isInterfaceFailureReasonRequested (self):
        return self._myInterfaceFailureReasonRequested

    def isInterfaceIpv6ConnectivityFailureAlarmRequested (self):
        return self._myInterfaceIpv6ConnectivityFailureAlarmRequested

    def isInterfaceFailureAlarmRequested (self):
        return self._myInterfaceFailureAlarmRequested

    def isInterfaceIpv4ConnectivityFailureAlarmRequested (self):
        return self._myInterfaceIpv4ConnectivityFailureAlarmRequested

    def isInterfaceIpv4ConnectivityFailureReasonRequested (self):
        return self._myInterfaceIpv4ConnectivityFailureReasonRequested

    def isInterfaceIpv6ConnectivityFailureReasonRequested (self):
        return self._myInterfaceIpv6ConnectivityFailureReasonRequested




    # setRequested...() methods

    def setInterfaceFailureReasonRequested (self):
        self._myInterfaceFailureReasonRequested=True

    def setInterfaceIpv6ConnectivityFailureAlarmRequested (self):
        self._myInterfaceIpv6ConnectivityFailureAlarmRequested=True

    def setInterfaceFailureAlarmRequested (self):
        self._myInterfaceFailureAlarmRequested=True

    def setInterfaceIpv4ConnectivityFailureAlarmRequested (self):
        self._myInterfaceIpv4ConnectivityFailureAlarmRequested=True

    def setInterfaceIpv4ConnectivityFailureReasonRequested (self):
        self._myInterfaceIpv4ConnectivityFailureReasonRequested=True

    def setInterfaceIpv6ConnectivityFailureReasonRequested (self):
        self._myInterfaceIpv6ConnectivityFailureReasonRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myInterfaceFailureReasonRequested:
            x = "+InterfaceFailureReason="
            if self._myHasInterfaceFailureReason:
                leafStr = str(self.interfaceFailureReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInterfaceIpv6ConnectivityFailureAlarmRequested:
            x = "+InterfaceIpv6ConnectivityFailureAlarm="
            if self._myHasInterfaceIpv6ConnectivityFailureAlarm:
                leafStr = str(self.interfaceIpv6ConnectivityFailureAlarm)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInterfaceFailureAlarmRequested:
            x = "+InterfaceFailureAlarm="
            if self._myHasInterfaceFailureAlarm:
                leafStr = str(self.interfaceFailureAlarm)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInterfaceIpv4ConnectivityFailureAlarmRequested:
            x = "+InterfaceIpv4ConnectivityFailureAlarm="
            if self._myHasInterfaceIpv4ConnectivityFailureAlarm:
                leafStr = str(self.interfaceIpv4ConnectivityFailureAlarm)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInterfaceIpv4ConnectivityFailureReasonRequested:
            x = "+InterfaceIpv4ConnectivityFailureReason="
            if self._myHasInterfaceIpv4ConnectivityFailureReason:
                leafStr = str(self.interfaceIpv4ConnectivityFailureReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInterfaceIpv6ConnectivityFailureReasonRequested:
            x = "+InterfaceIpv6ConnectivityFailureReason="
            if self._myHasInterfaceIpv6ConnectivityFailureReason:
                leafStr = str(self.interfaceIpv6ConnectivityFailureReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{AlarmsOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+InterfaceFailureReason="
        if self._myHasInterfaceFailureReason:
            leafStr = str(self.interfaceFailureReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInterfaceFailureReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InterfaceIpv6ConnectivityFailureAlarm="
        if self._myHasInterfaceIpv6ConnectivityFailureAlarm:
            leafStr = str(self.interfaceIpv6ConnectivityFailureAlarm)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInterfaceIpv6ConnectivityFailureAlarmRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InterfaceFailureAlarm="
        if self._myHasInterfaceFailureAlarm:
            leafStr = str(self.interfaceFailureAlarm)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInterfaceFailureAlarmRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InterfaceIpv4ConnectivityFailureAlarm="
        if self._myHasInterfaceIpv4ConnectivityFailureAlarm:
            leafStr = str(self.interfaceIpv4ConnectivityFailureAlarm)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInterfaceIpv4ConnectivityFailureAlarmRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InterfaceIpv4ConnectivityFailureReason="
        if self._myHasInterfaceIpv4ConnectivityFailureReason:
            leafStr = str(self.interfaceIpv4ConnectivityFailureReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInterfaceIpv4ConnectivityFailureReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InterfaceIpv6ConnectivityFailureReason="
        if self._myHasInterfaceIpv6ConnectivityFailureReason:
            leafStr = str(self.interfaceIpv6ConnectivityFailureReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInterfaceIpv6ConnectivityFailureReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{AlarmsOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setInterfaceFailureReasonRequested()
        self.setInterfaceIpv6ConnectivityFailureAlarmRequested()
        self.setInterfaceFailureAlarmRequested()
        self.setInterfaceIpv4ConnectivityFailureAlarmRequested()
        self.setInterfaceIpv4ConnectivityFailureReasonRequested()
        self.setInterfaceIpv6ConnectivityFailureReasonRequested()
        
        


    def setInterfaceFailureReason (self, interfaceFailureReason):
        self.interfaceFailureReason = interfaceFailureReason
        self.setHasInterfaceFailureReason()

    def setInterfaceIpv6ConnectivityFailureAlarm (self, interfaceIpv6ConnectivityFailureAlarm):
        self.interfaceIpv6ConnectivityFailureAlarm = interfaceIpv6ConnectivityFailureAlarm
        self.setHasInterfaceIpv6ConnectivityFailureAlarm()

    def setInterfaceFailureAlarm (self, interfaceFailureAlarm):
        self.interfaceFailureAlarm = interfaceFailureAlarm
        self.setHasInterfaceFailureAlarm()

    def setInterfaceIpv4ConnectivityFailureAlarm (self, interfaceIpv4ConnectivityFailureAlarm):
        self.interfaceIpv4ConnectivityFailureAlarm = interfaceIpv4ConnectivityFailureAlarm
        self.setHasInterfaceIpv4ConnectivityFailureAlarm()

    def setInterfaceIpv4ConnectivityFailureReason (self, interfaceIpv4ConnectivityFailureReason):
        self.interfaceIpv4ConnectivityFailureReason = interfaceIpv4ConnectivityFailureReason
        self.setHasInterfaceIpv4ConnectivityFailureReason()

    def setInterfaceIpv6ConnectivityFailureReason (self, interfaceIpv6ConnectivityFailureReason):
        self.interfaceIpv6ConnectivityFailureReason = interfaceIpv6ConnectivityFailureReason
        self.setHasInterfaceIpv6ConnectivityFailureReason()


"""
Extracted from the below data: 
{
    "node": {
        "className": "AlarmsOperData", 
        "namespace": "alarms", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.alarms.alarms_oper_data_gen import AlarmsOperData"
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
            "namespace": "alarms", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceFailureReason", 
            "yangName": "interface-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceIpv6ConnectivityFailureAlarm", 
            "yangName": "interface-ipv6-connectivity-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceFailureAlarm", 
            "yangName": "interface-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "interfaceIpv4ConnectivityFailureAlarm", 
            "yangName": "interface-ipv4-connectivity-failure-alarm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceIpv4ConnectivityFailureReason", 
            "yangName": "interface-ipv4-connectivity-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "interfaceIpv6ConnectivityFailureReason", 
            "yangName": "interface-ipv6-connectivity-failure-reason", 
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


