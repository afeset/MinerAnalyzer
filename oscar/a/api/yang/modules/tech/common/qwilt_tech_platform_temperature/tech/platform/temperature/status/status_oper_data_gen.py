


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureStatusType
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureOperationalStatusReasonType
from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import TemperatureOperationalStatusType


class StatusOperData (object):

    def __init__ (self):

        self.operationalStatus = TemperatureOperationalStatusType.kUnknown
        self._myHasOperationalStatus=False
        self._myOperationalStatusRequested=False
        
        self.operationalStatusReason = TemperatureOperationalStatusReasonType.kWarningTemperatureRange
        self._myHasOperationalStatusReason=False
        self._myOperationalStatusReasonRequested=False
        
        self.temperatureStatusRaw = ""
        self._myHasTemperatureStatusRaw=False
        self._myTemperatureStatusRawRequested=False
        
        self.temperatureStatus = TemperatureStatusType.kUnknown
        self._myHasTemperatureStatus=False
        self._myTemperatureStatusRequested=False
        


    def copyFrom (self, other):

        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        self._myOperationalStatusRequested=other._myOperationalStatusRequested
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        self._myOperationalStatusReasonRequested=other._myOperationalStatusReasonRequested
        
        self.temperatureStatusRaw=other.temperatureStatusRaw
        self._myHasTemperatureStatusRaw=other._myHasTemperatureStatusRaw
        self._myTemperatureStatusRawRequested=other._myTemperatureStatusRawRequested
        
        self.temperatureStatus=other.temperatureStatus
        self._myHasTemperatureStatus=other._myHasTemperatureStatus
        self._myTemperatureStatusRequested=other._myTemperatureStatusRequested
        


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
        
        if self.isTemperatureStatusRawRequested():
            self.temperatureStatusRaw=other.temperatureStatusRaw
            self._myHasTemperatureStatusRaw=other._myHasTemperatureStatusRaw
            self._myTemperatureStatusRawRequested=other._myTemperatureStatusRawRequested
        
        if self.isTemperatureStatusRequested():
            self.temperatureStatus=other.temperatureStatus
            self._myHasTemperatureStatus=other._myHasTemperatureStatus
            self._myTemperatureStatusRequested=other._myTemperatureStatusRequested
        


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
        
        if other.hasTemperatureStatusRaw():
            self.temperatureStatusRaw=other.temperatureStatusRaw
            self._myHasTemperatureStatusRaw=other._myHasTemperatureStatusRaw
            self._myTemperatureStatusRawRequested=other._myTemperatureStatusRawRequested
        
        if other.hasTemperatureStatus():
            self.temperatureStatus=other.temperatureStatus
            self._myHasTemperatureStatus=other._myHasTemperatureStatus
            self._myTemperatureStatusRequested=other._myTemperatureStatusRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.operationalStatus=other.operationalStatus
        self._myHasOperationalStatus=other._myHasOperationalStatus
        
        self.operationalStatusReason=other.operationalStatusReason
        self._myHasOperationalStatusReason=other._myHasOperationalStatusReason
        
        self.temperatureStatusRaw=other.temperatureStatusRaw
        self._myHasTemperatureStatusRaw=other._myHasTemperatureStatusRaw
        
        self.temperatureStatus=other.temperatureStatus
        self._myHasTemperatureStatus=other._myHasTemperatureStatus
        


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

    def hasTemperatureStatusRaw (self):
        return self._myHasTemperatureStatusRaw

    def hasTemperatureStatus (self):
        return self._myHasTemperatureStatus




    # setHas...() methods

    def setHasOperationalStatus (self):
        self._myHasOperationalStatus=True

    def setHasOperationalStatusReason (self):
        self._myHasOperationalStatusReason=True

    def setHasTemperatureStatusRaw (self):
        self._myHasTemperatureStatusRaw=True

    def setHasTemperatureStatus (self):
        self._myHasTemperatureStatus=True




    # isRequested...() methods

    def isOperationalStatusRequested (self):
        return self._myOperationalStatusRequested

    def isOperationalStatusReasonRequested (self):
        return self._myOperationalStatusReasonRequested

    def isTemperatureStatusRawRequested (self):
        return self._myTemperatureStatusRawRequested

    def isTemperatureStatusRequested (self):
        return self._myTemperatureStatusRequested




    # setRequested...() methods

    def setOperationalStatusRequested (self):
        self._myOperationalStatusRequested=True

    def setOperationalStatusReasonRequested (self):
        self._myOperationalStatusReasonRequested=True

    def setTemperatureStatusRawRequested (self):
        self._myTemperatureStatusRawRequested=True

    def setTemperatureStatusRequested (self):
        self._myTemperatureStatusRequested=True




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
        if self._myTemperatureStatusRawRequested:
            x = "+TemperatureStatusRaw="
            if self._myHasTemperatureStatusRaw:
                leafStr = str(self.temperatureStatusRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTemperatureStatusRequested:
            x = "+TemperatureStatus="
            if self._myHasTemperatureStatus:
                leafStr = str(self.temperatureStatus)
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
        x = "+TemperatureStatusRaw="
        if self._myHasTemperatureStatusRaw:
            leafStr = str(self.temperatureStatusRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTemperatureStatusRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TemperatureStatus="
        if self._myHasTemperatureStatus:
            leafStr = str(self.temperatureStatus)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTemperatureStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setOperationalStatusRequested()
        self.setOperationalStatusReasonRequested()
        self.setTemperatureStatusRawRequested()
        self.setTemperatureStatusRequested()
        
        


    def setOperationalStatus (self, operationalStatus):
        self.operationalStatus = operationalStatus
        self.setHasOperationalStatus()

    def setOperationalStatusReason (self, operationalStatusReason):
        self.operationalStatusReason = operationalStatusReason
        self.setHasOperationalStatusReason()

    def setTemperatureStatusRaw (self, temperatureStatusRaw):
        self.temperatureStatusRaw = temperatureStatusRaw
        self.setHasTemperatureStatusRaw()

    def setTemperatureStatus (self, temperatureStatus):
        self.temperatureStatus = temperatureStatus
        self.setHasTemperatureStatus()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.status.status_oper_data_gen import StatusOperData"
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
            "memberName": "temperatureStatusRaw", 
            "yangName": "temperature-status-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "temperatureStatus", 
            "yangName": "temperature-status", 
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


