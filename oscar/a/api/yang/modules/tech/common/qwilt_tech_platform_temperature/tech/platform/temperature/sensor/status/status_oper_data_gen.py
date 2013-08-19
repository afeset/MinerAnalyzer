


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorOperationalStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorOperationalStatusReasonType


class StatusOperData (object):

    def __init__ (self):

        self.maximumCritical = 0
        self._myHasMaximumCritical=False
        self._myMaximumCriticalRequested=False
        
        self.operationalStatus = SensorOperationalStatusType.kOk
        self._myHasOperationalStatus=False
        self._myOperationalStatusRequested=False
        
        self.temperature = 0
        self._myHasTemperature=False
        self._myTemperatureRequested=False
        
        self.minimumWarning = 0
        self._myHasMinimumWarning=False
        self._myMinimumWarningRequested=False
        
        self.minimumCritical = 0
        self._myHasMinimumCritical=False
        self._myMinimumCriticalRequested=False
        
        self.location = ""
        self._myHasLocation=False
        self._myLocationRequested=False
        
        self.maximumWarning = 0
        self._myHasMaximumWarning=False
        self._myMaximumWarningRequested=False
        
        self.operationalStatusReason = SensorOperationalStatusReasonType.kSimulation
        self._myHasOperationalStatusReason=False
        self._myOperationalStatusReasonRequested=False
        


    def copyFrom (self, other):

        self.maximumCritical=other.maximumCritical
        self._myHasMaximumCritical=other._myHasMaximumCritical
        self._myMaximumCriticalRequested=other._myMaximumCriticalRequested
        
        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        self.temperature=other.temperature
        self._myHasTemperature=other._myHasTemperature
        self._myTemperatureRequested=other._myTemperatureRequested
        
        self.minimumWarning=other.minimumWarning
        self._myHasMinimumWarning=other._myHasMinimumWarning
        self._myMinimumWarningRequested=other._myMinimumWarningRequested
        
        self.minimumCritical=other.minimumCritical
        self._myHasMinimumCritical=other._myHasMinimumCritical
        self._myMinimumCriticalRequested=other._myMinimumCriticalRequested
        
        self.location=other.location
        self._myHasLocation=other._myHasLocation
        self._myLocationRequested=other._myLocationRequested
        
        self.maximumWarning=other.maximumWarning
        self._myHasMaximumWarning=other._myHasMaximumWarning
        self._myMaximumWarningRequested=other._myMaximumWarningRequested
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isMaximumCriticalRequested():
            self.maximumCritical=other.maximumCritical
            self._myHasMaximumCritical=other._myHasMaximumCritical
            self._myMaximumCriticalRequested=other._myMaximumCriticalRequested
        
        if self.isOperationalStatusRequested():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        if self.isTemperatureRequested():
            self.temperature=other.temperature
            self._myHasTemperature=other._myHasTemperature
            self._myTemperatureRequested=other._myTemperatureRequested
        
        if self.isMinimumWarningRequested():
            self.minimumWarning=other.minimumWarning
            self._myHasMinimumWarning=other._myHasMinimumWarning
            self._myMinimumWarningRequested=other._myMinimumWarningRequested
        
        if self.isMinimumCriticalRequested():
            self.minimumCritical=other.minimumCritical
            self._myHasMinimumCritical=other._myHasMinimumCritical
            self._myMinimumCriticalRequested=other._myMinimumCriticalRequested
        
        if self.isLocationRequested():
            self.location=other.location
            self._myHasLocation=other._myHasLocation
            self._myLocationRequested=other._myLocationRequested
        
        if self.isMaximumWarningRequested():
            self.maximumWarning=other.maximumWarning
            self._myHasMaximumWarning=other._myHasMaximumWarning
            self._myMaximumWarningRequested=other._myMaximumWarningRequested
        
        if self.isOperationalStatusReasonRequested():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasMaximumCritical():
            self.maximumCritical=other.maximumCritical
            self._myHasMaximumCritical=other._myHasMaximumCritical
            self._myMaximumCriticalRequested=other._myMaximumCriticalRequested
        
        if other.hasOperationalStatus():
            self.operationalStatus=other.operationalStatus
            self._myHasOperationalStatus=other._myHasOperationalStatus
            self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        if other.hasTemperature():
            self.temperature=other.temperature
            self._myHasTemperature=other._myHasTemperature
            self._myTemperatureRequested=other._myTemperatureRequested
        
        if other.hasMinimumWarning():
            self.minimumWarning=other.minimumWarning
            self._myHasMinimumWarning=other._myHasMinimumWarning
            self._myMinimumWarningRequested=other._myMinimumWarningRequested
        
        if other.hasMinimumCritical():
            self.minimumCritical=other.minimumCritical
            self._myHasMinimumCritical=other._myHasMinimumCritical
            self._myMinimumCriticalRequested=other._myMinimumCriticalRequested
        
        if other.hasLocation():
            self.location=other.location
            self._myHasLocation=other._myHasLocation
            self._myLocationRequested=other._myLocationRequested
        
        if other.hasMaximumWarning():
            self.maximumWarning=other.maximumWarning
            self._myHasMaximumWarning=other._myHasMaximumWarning
            self._myMaximumWarningRequested=other._myMaximumWarningRequested
        
        if other.hasOperationalStatusReason():
            self.operationalStatusReason=other.operationalStatusReason
            self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
            self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.maximumCritical=other.maximumCritical
        self._myHasMaximumCritical=other._myHasMaximumCritical
        
        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        
        self.temperature=other.temperature
        self._myHasTemperature=other._myHasTemperature
        
        self.minimumWarning=other.minimumWarning
        self._myHasMinimumWarning=other._myHasMinimumWarning
        
        self.minimumCritical=other.minimumCritical
        self._myHasMinimumCritical=other._myHasMinimumCritical
        
        self.location=other.location
        self._myHasLocation=other._myHasLocation
        
        self.maximumWarning=other.maximumWarning
        self._myHasMaximumWarning=other._myHasMaximumWarning
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        


    def setAllNumericToZero (self):
        
        self.maximumCritical=0
        self.setHasMaximumCritical()
        self.temperature=0
        self.setHasTemperature()
        self.minimumWarning=0
        self.setHasMinimumWarning()
        self.minimumCritical=0
        self.setHasMinimumCritical()
        self.maximumWarning=0
        self.setHasMaximumWarning()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasMaximumCritical():
            if other.hasMaximumCritical():
                self.maximumCritical -= other.maximumCritical
        
        if self.hasTemperature():
            if other.hasTemperature():
                self.temperature -= other.temperature
        
        if self.hasMinimumWarning():
            if other.hasMinimumWarning():
                self.minimumWarning -= other.minimumWarning
        
        if self.hasMinimumCritical():
            if other.hasMinimumCritical():
                self.minimumCritical -= other.minimumCritical
        
        if self.hasMaximumWarning():
            if other.hasMaximumWarning():
                self.maximumWarning -= other.maximumWarning
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasMaximumCritical():
            if other.hasMaximumCritical():
                self.maximumCritical += other.maximumCritical
        
        if self.hasTemperature():
            if other.hasTemperature():
                self.temperature += other.temperature
        
        if self.hasMinimumWarning():
            if other.hasMinimumWarning():
                self.minimumWarning += other.minimumWarning
        
        if self.hasMinimumCritical():
            if other.hasMinimumCritical():
                self.minimumCritical += other.minimumCritical
        
        if self.hasMaximumWarning():
            if other.hasMaximumWarning():
                self.maximumWarning += other.maximumWarning
        
        
        pass


    # has...() methods

    def hasMaximumCritical (self):
        return self._myHasMaximumCritical

    def hasOperationalStatus (self):
        return self._myHasOperationalStatus

    def hasTemperature (self):
        return self._myHasTemperature

    def hasMinimumWarning (self):
        return self._myHasMinimumWarning

    def hasMinimumCritical (self):
        return self._myHasMinimumCritical

    def hasLocation (self):
        return self._myHasLocation

    def hasMaximumWarning (self):
        return self._myHasMaximumWarning

    def hasOperationalStatusReason (self):
        return self._myHasOperationalStatusReason




    # setHas...() methods

    def setHasMaximumCritical (self):
        self._myHasMaximumCritical=True

    def setHasOperationalStatus (self):
        self._myHasOperationalStatus=True

    def setHasTemperature (self):
        self._myHasTemperature=True

    def setHasMinimumWarning (self):
        self._myHasMinimumWarning=True

    def setHasMinimumCritical (self):
        self._myHasMinimumCritical=True

    def setHasLocation (self):
        self._myHasLocation=True

    def setHasMaximumWarning (self):
        self._myHasMaximumWarning=True

    def setHasOperationalStatusReason (self):
        self._myHasOperationalStatusReason=True




    # isRequested...() methods

    def isMaximumCriticalRequested (self):
        return self._myMaximumCriticalRequested

    def isOperationalStatusRequested (self):
        return self._myOperationalStatusRequested

    def isTemperatureRequested (self):
        return self._myTemperatureRequested

    def isMinimumWarningRequested (self):
        return self._myMinimumWarningRequested

    def isMinimumCriticalRequested (self):
        return self._myMinimumCriticalRequested

    def isLocationRequested (self):
        return self._myLocationRequested

    def isMaximumWarningRequested (self):
        return self._myMaximumWarningRequested

    def isOperationalStatusReasonRequested (self):
        return self._myOperationalStatusReasonRequested




    # setRequested...() methods

    def setMaximumCriticalRequested (self):
        self._myMaximumCriticalRequested=True

    def setOperationalStatusRequested (self):
        self._myOperationalStatusRequested=True

    def setTemperatureRequested (self):
        self._myTemperatureRequested=True

    def setMinimumWarningRequested (self):
        self._myMinimumWarningRequested=True

    def setMinimumCriticalRequested (self):
        self._myMinimumCriticalRequested=True

    def setLocationRequested (self):
        self._myLocationRequested=True

    def setMaximumWarningRequested (self):
        self._myMaximumWarningRequested=True

    def setOperationalStatusReasonRequested (self):
        self._myOperationalStatusReasonRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myMaximumCriticalRequested:
            x = "+MaximumCritical="
            if self._myHasMaximumCritical:
                leafStr = str(self.maximumCritical)
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
        if self._myTemperatureRequested:
            x = "+Temperature="
            if self._myHasTemperature:
                leafStr = str(self.temperature)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMinimumWarningRequested:
            x = "+MinimumWarning="
            if self._myHasMinimumWarning:
                leafStr = str(self.minimumWarning)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMinimumCriticalRequested:
            x = "+MinimumCritical="
            if self._myHasMinimumCritical:
                leafStr = str(self.minimumCritical)
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

        x=""
        if self._myMaximumWarningRequested:
            x = "+MaximumWarning="
            if self._myHasMaximumWarning:
                leafStr = str(self.maximumWarning)
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
        x = "+MaximumCritical="
        if self._myHasMaximumCritical:
            leafStr = str(self.maximumCritical)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMaximumCriticalRequested:
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
        x = "+Temperature="
        if self._myHasTemperature:
            leafStr = str(self.temperature)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTemperatureRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MinimumWarning="
        if self._myHasMinimumWarning:
            leafStr = str(self.minimumWarning)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMinimumWarningRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MinimumCritical="
        if self._myHasMinimumCritical:
            leafStr = str(self.minimumCritical)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMinimumCriticalRequested:
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

        x=""
        x = "+MaximumWarning="
        if self._myHasMaximumWarning:
            leafStr = str(self.maximumWarning)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMaximumWarningRequested:
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
        self.setMaximumCriticalRequested()
        self.setOperationalStatusRequested()
        self.setTemperatureRequested()
        self.setMinimumWarningRequested()
        self.setMinimumCriticalRequested()
        self.setLocationRequested()
        self.setMaximumWarningRequested()
        self.setOperationalStatusReasonRequested()
        
        


    def setMaximumCritical (self, maximumCritical):
        self.maximumCritical = maximumCritical
        self.setHasMaximumCritical()

    def setOperationalStatus (self, operationalStatus):
        self.operationalStatus = operationalStatus
        self.setHasOperationalStatus()

    def setTemperature (self, temperature):
        self.temperature = temperature
        self.setHasTemperature()

    def setMinimumWarning (self, minimumWarning):
        self.minimumWarning = minimumWarning
        self.setHasMinimumWarning()

    def setMinimumCritical (self, minimumCritical):
        self.minimumCritical = minimumCritical
        self.setHasMinimumCritical()

    def setLocation (self, location):
        self.location = location
        self.setHasLocation()

    def setMaximumWarning (self, maximumWarning):
        self.maximumWarning = maximumWarning
        self.setHasMaximumWarning()

    def setOperationalStatusReason (self, operationalStatusReason):
        self.operationalStatusReason = operationalStatusReason
        self.setHasOperationalStatusReason()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.status.status_oper_data_gen import StatusOperData"
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
            "namespace": "sensor", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "maximumCritical", 
            "yangName": "maximum-critical", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "temperature", 
            "yangName": "temperature", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "minimumWarning", 
            "yangName": "minimum-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "minimumCritical", 
            "yangName": "minimum-critical", 
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
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "maximumWarning", 
            "yangName": "maximum-warning", 
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
            "qwilt_tech_platform_temperature"
        ]
    }, 
    "createTime": "2013"
}
"""


