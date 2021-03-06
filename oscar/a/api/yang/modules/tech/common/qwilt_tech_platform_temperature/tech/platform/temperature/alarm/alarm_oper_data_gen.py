


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureAlarmReasonType


class AlarmOperData (object):

    def __init__ (self):

        self.count = 0
        self._myHasCount=False
        self._myCountRequested=False
        
        self.temperatureWarning = False
        self._myHasTemperatureWarning=False
        self._myTemperatureWarningRequested=False
        
        self.temperatureCritical = False
        self._myHasTemperatureCritical=False
        self._myTemperatureCriticalRequested=False
        
        self.temperatureCriticalReason = TemperatureAlarmReasonType.kNone
        self._myHasTemperatureCriticalReason=False
        self._myTemperatureCriticalReasonRequested=False
        
        self.temperatureWarningReason = TemperatureAlarmReasonType.kNone
        self._myHasTemperatureWarningReason=False
        self._myTemperatureWarningReasonRequested=False
        


    def copyFrom (self, other):

        self.count=other.count
        self._myHasCount=other._myHasCount
        self._myCountRequested=other._myCountRequested
        
        self.temperatureWarning=other.temperatureWarning
        self._myHasTemperatureWarning=other._myHasTemperatureWarning
        self._myTemperatureWarningRequested=other._myTemperatureWarningRequested
        
        self.temperatureCritical=other.temperatureCritical
        self._myHasTemperatureCritical=other._myHasTemperatureCritical
        self._myTemperatureCriticalRequested=other._myTemperatureCriticalRequested
        
        self.temperatureCriticalReason=other.temperatureCriticalReason
        self._myHasTemperatureCriticalReason=other._myHasTemperatureCriticalReason
        self._myTemperatureCriticalReasonRequested=other._myTemperatureCriticalReasonRequested
        
        self.temperatureWarningReason=other.temperatureWarningReason
        self._myHasTemperatureWarningReason=other._myHasTemperatureWarningReason
        self._myTemperatureWarningReasonRequested=other._myTemperatureWarningReasonRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isCountRequested():
            self.count=other.count
            self._myHasCount=other._myHasCount
            self._myCountRequested=other._myCountRequested
        
        if self.isTemperatureWarningRequested():
            self.temperatureWarning=other.temperatureWarning
            self._myHasTemperatureWarning=other._myHasTemperatureWarning
            self._myTemperatureWarningRequested=other._myTemperatureWarningRequested
        
        if self.isTemperatureCriticalRequested():
            self.temperatureCritical=other.temperatureCritical
            self._myHasTemperatureCritical=other._myHasTemperatureCritical
            self._myTemperatureCriticalRequested=other._myTemperatureCriticalRequested
        
        if self.isTemperatureCriticalReasonRequested():
            self.temperatureCriticalReason=other.temperatureCriticalReason
            self._myHasTemperatureCriticalReason=other._myHasTemperatureCriticalReason
            self._myTemperatureCriticalReasonRequested=other._myTemperatureCriticalReasonRequested
        
        if self.isTemperatureWarningReasonRequested():
            self.temperatureWarningReason=other.temperatureWarningReason
            self._myHasTemperatureWarningReason=other._myHasTemperatureWarningReason
            self._myTemperatureWarningReasonRequested=other._myTemperatureWarningReasonRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasCount():
            self.count=other.count
            self._myHasCount=other._myHasCount
            self._myCountRequested=other._myCountRequested
        
        if other.hasTemperatureWarning():
            self.temperatureWarning=other.temperatureWarning
            self._myHasTemperatureWarning=other._myHasTemperatureWarning
            self._myTemperatureWarningRequested=other._myTemperatureWarningRequested
        
        if other.hasTemperatureCritical():
            self.temperatureCritical=other.temperatureCritical
            self._myHasTemperatureCritical=other._myHasTemperatureCritical
            self._myTemperatureCriticalRequested=other._myTemperatureCriticalRequested
        
        if other.hasTemperatureCriticalReason():
            self.temperatureCriticalReason=other.temperatureCriticalReason
            self._myHasTemperatureCriticalReason=other._myHasTemperatureCriticalReason
            self._myTemperatureCriticalReasonRequested=other._myTemperatureCriticalReasonRequested
        
        if other.hasTemperatureWarningReason():
            self.temperatureWarningReason=other.temperatureWarningReason
            self._myHasTemperatureWarningReason=other._myHasTemperatureWarningReason
            self._myTemperatureWarningReasonRequested=other._myTemperatureWarningReasonRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.count=other.count
        self._myHasCount=other._myHasCount
        
        self.temperatureWarning=other.temperatureWarning
        self._myHasTemperatureWarning=other._myHasTemperatureWarning
        
        self.temperatureCritical=other.temperatureCritical
        self._myHasTemperatureCritical=other._myHasTemperatureCritical
        
        self.temperatureCriticalReason=other.temperatureCriticalReason
        self._myHasTemperatureCriticalReason=other._myHasTemperatureCriticalReason
        
        self.temperatureWarningReason=other.temperatureWarningReason
        self._myHasTemperatureWarningReason=other._myHasTemperatureWarningReason
        


    def setAllNumericToZero (self):
        
        self.count=0
        self.setHasCount()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasCount():
            if other.hasCount():
                self.count -= other.count
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasCount():
            if other.hasCount():
                self.count += other.count
        
        
        pass


    # has...() methods

    def hasCount (self):
        return self._myHasCount

    def hasTemperatureWarning (self):
        return self._myHasTemperatureWarning

    def hasTemperatureCritical (self):
        return self._myHasTemperatureCritical

    def hasTemperatureCriticalReason (self):
        return self._myHasTemperatureCriticalReason

    def hasTemperatureWarningReason (self):
        return self._myHasTemperatureWarningReason




    # setHas...() methods

    def setHasCount (self):
        self._myHasCount=True

    def setHasTemperatureWarning (self):
        self._myHasTemperatureWarning=True

    def setHasTemperatureCritical (self):
        self._myHasTemperatureCritical=True

    def setHasTemperatureCriticalReason (self):
        self._myHasTemperatureCriticalReason=True

    def setHasTemperatureWarningReason (self):
        self._myHasTemperatureWarningReason=True




    # isRequested...() methods

    def isCountRequested (self):
        return self._myCountRequested

    def isTemperatureWarningRequested (self):
        return self._myTemperatureWarningRequested

    def isTemperatureCriticalRequested (self):
        return self._myTemperatureCriticalRequested

    def isTemperatureCriticalReasonRequested (self):
        return self._myTemperatureCriticalReasonRequested

    def isTemperatureWarningReasonRequested (self):
        return self._myTemperatureWarningReasonRequested




    # setRequested...() methods

    def setCountRequested (self):
        self._myCountRequested=True

    def setTemperatureWarningRequested (self):
        self._myTemperatureWarningRequested=True

    def setTemperatureCriticalRequested (self):
        self._myTemperatureCriticalRequested=True

    def setTemperatureCriticalReasonRequested (self):
        self._myTemperatureCriticalReasonRequested=True

    def setTemperatureWarningReasonRequested (self):
        self._myTemperatureWarningReasonRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myCountRequested:
            x = "+Count="
            if self._myHasCount:
                leafStr = str(self.count)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTemperatureWarningRequested:
            x = "+TemperatureWarning="
            if self._myHasTemperatureWarning:
                leafStr = str(self.temperatureWarning)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTemperatureCriticalRequested:
            x = "+TemperatureCritical="
            if self._myHasTemperatureCritical:
                leafStr = str(self.temperatureCritical)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTemperatureCriticalReasonRequested:
            x = "+TemperatureCriticalReason="
            if self._myHasTemperatureCriticalReason:
                leafStr = str(self.temperatureCriticalReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTemperatureWarningReasonRequested:
            x = "+TemperatureWarningReason="
            if self._myHasTemperatureWarningReason:
                leafStr = str(self.temperatureWarningReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{AlarmOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+Count="
        if self._myHasCount:
            leafStr = str(self.count)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCountRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TemperatureWarning="
        if self._myHasTemperatureWarning:
            leafStr = str(self.temperatureWarning)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTemperatureWarningRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TemperatureCritical="
        if self._myHasTemperatureCritical:
            leafStr = str(self.temperatureCritical)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTemperatureCriticalRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TemperatureCriticalReason="
        if self._myHasTemperatureCriticalReason:
            leafStr = str(self.temperatureCriticalReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTemperatureCriticalReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TemperatureWarningReason="
        if self._myHasTemperatureWarningReason:
            leafStr = str(self.temperatureWarningReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTemperatureWarningReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{AlarmOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setCountRequested()
        self.setTemperatureWarningRequested()
        self.setTemperatureCriticalRequested()
        self.setTemperatureCriticalReasonRequested()
        self.setTemperatureWarningReasonRequested()
        
        


    def setCount (self, count):
        self.count = count
        self.setHasCount()

    def setTemperatureWarning (self, temperatureWarning):
        self.temperatureWarning = temperatureWarning
        self.setHasTemperatureWarning()

    def setTemperatureCritical (self, temperatureCritical):
        self.temperatureCritical = temperatureCritical
        self.setHasTemperatureCritical()

    def setTemperatureCriticalReason (self, temperatureCriticalReason):
        self.temperatureCriticalReason = temperatureCriticalReason
        self.setHasTemperatureCriticalReason()

    def setTemperatureWarningReason (self, temperatureWarningReason):
        self.temperatureWarningReason = temperatureWarningReason
        self.setHasTemperatureWarningReason()


"""
Extracted from the below data: 
{
    "node": {
        "className": "AlarmOperData", 
        "namespace": "alarm", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.alarm.alarm_oper_data_gen import AlarmOperData"
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
            "namespace": "temperature", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "count", 
            "yangName": "count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "temperatureWarning", 
            "yangName": "temperature-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "temperatureCritical", 
            "yangName": "temperature-critical", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "temperatureCriticalReason", 
            "yangName": "temperature-critical-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "temperatureWarningReason", 
            "yangName": "temperature-warning-reason", 
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
            "qwilt_tech_platform_temperature"
        ]
    }, 
    "createTime": "2013"
}
"""


