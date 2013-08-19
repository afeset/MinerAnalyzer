


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.qwilt_tech_platform_temperature_module_gen import SensorDeviceStatusType


class StatusOperData (object):

    def __init__ (self):

        self.status = SensorDeviceStatusType.kOk
        self._myHasStatus=False
        self._myStatusRequested=False
        
        self.index = ""
        self._myHasIndex=False
        self._myIndexRequested=False
        
        self.temperatureRaw = ""
        self._myHasTemperatureRaw=False
        self._myTemperatureRawRequested=False
        
        self.maximumCriticalRaw = ""
        self._myHasMaximumCriticalRaw=False
        self._myMaximumCriticalRawRequested=False
        
        self.maximumWarningRaw = ""
        self._myHasMaximumWarningRaw=False
        self._myMaximumWarningRawRequested=False
        
        self.minimumWarningRaw = ""
        self._myHasMinimumWarningRaw=False
        self._myMinimumWarningRawRequested=False
        
        self.minimumCriticalRaw = ""
        self._myHasMinimumCriticalRaw=False
        self._myMinimumCriticalRawRequested=False
        
        self.probeName = ""
        self._myHasProbeName=False
        self._myProbeNameRequested=False
        
        self.statusRaw = ""
        self._myHasStatusRaw=False
        self._myStatusRawRequested=False
        


    def copyFrom (self, other):

        self.status=other.status
        self._myHasStatus=other._myHasStatus
        self._myStatusRequested=other._myStatusRequested
        
        self.index=other.index
        self._myHasIndex=other._myHasIndex
        self._myIndexRequested=other._myIndexRequested
        
        self.temperatureRaw=other.temperatureRaw
        self._myHasTemperatureRaw=other._myHasTemperatureRaw
        self._myTemperatureRawRequested=other._myTemperatureRawRequested
        
        self.maximumCriticalRaw=other.maximumCriticalRaw
        self._myHasMaximumCriticalRaw=other._myHasMaximumCriticalRaw
        self._myMaximumCriticalRawRequested=other._myMaximumCriticalRawRequested
        
        self.maximumWarningRaw=other.maximumWarningRaw
        self._myHasMaximumWarningRaw=other._myHasMaximumWarningRaw
        self._myMaximumWarningRawRequested=other._myMaximumWarningRawRequested
        
        self.minimumWarningRaw=other.minimumWarningRaw
        self._myHasMinimumWarningRaw=other._myHasMinimumWarningRaw
        self._myMinimumWarningRawRequested=other._myMinimumWarningRawRequested
        
        self.minimumCriticalRaw=other.minimumCriticalRaw
        self._myHasMinimumCriticalRaw=other._myHasMinimumCriticalRaw
        self._myMinimumCriticalRawRequested=other._myMinimumCriticalRawRequested
        
        self.probeName=other.probeName
        self._myHasProbeName=other._myHasProbeName
        self._myProbeNameRequested=other._myProbeNameRequested
        
        self.statusRaw=other.statusRaw
        self._myHasStatusRaw=other._myHasStatusRaw
        self._myStatusRawRequested=other._myStatusRawRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isStatusRequested():
            self.status=other.status
            self._myHasStatus=other._myHasStatus
            self._myStatusRequested=other._myStatusRequested
        
        if self.isIndexRequested():
            self.index=other.index
            self._myHasIndex=other._myHasIndex
            self._myIndexRequested=other._myIndexRequested
        
        if self.isTemperatureRawRequested():
            self.temperatureRaw=other.temperatureRaw
            self._myHasTemperatureRaw=other._myHasTemperatureRaw
            self._myTemperatureRawRequested=other._myTemperatureRawRequested
        
        if self.isMaximumCriticalRawRequested():
            self.maximumCriticalRaw=other.maximumCriticalRaw
            self._myHasMaximumCriticalRaw=other._myHasMaximumCriticalRaw
            self._myMaximumCriticalRawRequested=other._myMaximumCriticalRawRequested
        
        if self.isMaximumWarningRawRequested():
            self.maximumWarningRaw=other.maximumWarningRaw
            self._myHasMaximumWarningRaw=other._myHasMaximumWarningRaw
            self._myMaximumWarningRawRequested=other._myMaximumWarningRawRequested
        
        if self.isMinimumWarningRawRequested():
            self.minimumWarningRaw=other.minimumWarningRaw
            self._myHasMinimumWarningRaw=other._myHasMinimumWarningRaw
            self._myMinimumWarningRawRequested=other._myMinimumWarningRawRequested
        
        if self.isMinimumCriticalRawRequested():
            self.minimumCriticalRaw=other.minimumCriticalRaw
            self._myHasMinimumCriticalRaw=other._myHasMinimumCriticalRaw
            self._myMinimumCriticalRawRequested=other._myMinimumCriticalRawRequested
        
        if self.isProbeNameRequested():
            self.probeName=other.probeName
            self._myHasProbeName=other._myHasProbeName
            self._myProbeNameRequested=other._myProbeNameRequested
        
        if self.isStatusRawRequested():
            self.statusRaw=other.statusRaw
            self._myHasStatusRaw=other._myHasStatusRaw
            self._myStatusRawRequested=other._myStatusRawRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasStatus():
            self.status=other.status
            self._myHasStatus=other._myHasStatus
            self._myStatusRequested=other._myStatusRequested
        
        if other.hasIndex():
            self.index=other.index
            self._myHasIndex=other._myHasIndex
            self._myIndexRequested=other._myIndexRequested
        
        if other.hasTemperatureRaw():
            self.temperatureRaw=other.temperatureRaw
            self._myHasTemperatureRaw=other._myHasTemperatureRaw
            self._myTemperatureRawRequested=other._myTemperatureRawRequested
        
        if other.hasMaximumCriticalRaw():
            self.maximumCriticalRaw=other.maximumCriticalRaw
            self._myHasMaximumCriticalRaw=other._myHasMaximumCriticalRaw
            self._myMaximumCriticalRawRequested=other._myMaximumCriticalRawRequested
        
        if other.hasMaximumWarningRaw():
            self.maximumWarningRaw=other.maximumWarningRaw
            self._myHasMaximumWarningRaw=other._myHasMaximumWarningRaw
            self._myMaximumWarningRawRequested=other._myMaximumWarningRawRequested
        
        if other.hasMinimumWarningRaw():
            self.minimumWarningRaw=other.minimumWarningRaw
            self._myHasMinimumWarningRaw=other._myHasMinimumWarningRaw
            self._myMinimumWarningRawRequested=other._myMinimumWarningRawRequested
        
        if other.hasMinimumCriticalRaw():
            self.minimumCriticalRaw=other.minimumCriticalRaw
            self._myHasMinimumCriticalRaw=other._myHasMinimumCriticalRaw
            self._myMinimumCriticalRawRequested=other._myMinimumCriticalRawRequested
        
        if other.hasProbeName():
            self.probeName=other.probeName
            self._myHasProbeName=other._myHasProbeName
            self._myProbeNameRequested=other._myProbeNameRequested
        
        if other.hasStatusRaw():
            self.statusRaw=other.statusRaw
            self._myHasStatusRaw=other._myHasStatusRaw
            self._myStatusRawRequested=other._myStatusRawRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.status=other.status
        self._myHasStatus=other._myHasStatus
        
        self.index=other.index
        self._myHasIndex=other._myHasIndex
        
        self.temperatureRaw=other.temperatureRaw
        self._myHasTemperatureRaw=other._myHasTemperatureRaw
        
        self.maximumCriticalRaw=other.maximumCriticalRaw
        self._myHasMaximumCriticalRaw=other._myHasMaximumCriticalRaw
        
        self.maximumWarningRaw=other.maximumWarningRaw
        self._myHasMaximumWarningRaw=other._myHasMaximumWarningRaw
        
        self.minimumWarningRaw=other.minimumWarningRaw
        self._myHasMinimumWarningRaw=other._myHasMinimumWarningRaw
        
        self.minimumCriticalRaw=other.minimumCriticalRaw
        self._myHasMinimumCriticalRaw=other._myHasMinimumCriticalRaw
        
        self.probeName=other.probeName
        self._myHasProbeName=other._myHasProbeName
        
        self.statusRaw=other.statusRaw
        self._myHasStatusRaw=other._myHasStatusRaw
        


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

    def hasStatus (self):
        return self._myHasStatus

    def hasIndex (self):
        return self._myHasIndex

    def hasTemperatureRaw (self):
        return self._myHasTemperatureRaw

    def hasMaximumCriticalRaw (self):
        return self._myHasMaximumCriticalRaw

    def hasMaximumWarningRaw (self):
        return self._myHasMaximumWarningRaw

    def hasMinimumWarningRaw (self):
        return self._myHasMinimumWarningRaw

    def hasMinimumCriticalRaw (self):
        return self._myHasMinimumCriticalRaw

    def hasProbeName (self):
        return self._myHasProbeName

    def hasStatusRaw (self):
        return self._myHasStatusRaw




    # setHas...() methods

    def setHasStatus (self):
        self._myHasStatus=True

    def setHasIndex (self):
        self._myHasIndex=True

    def setHasTemperatureRaw (self):
        self._myHasTemperatureRaw=True

    def setHasMaximumCriticalRaw (self):
        self._myHasMaximumCriticalRaw=True

    def setHasMaximumWarningRaw (self):
        self._myHasMaximumWarningRaw=True

    def setHasMinimumWarningRaw (self):
        self._myHasMinimumWarningRaw=True

    def setHasMinimumCriticalRaw (self):
        self._myHasMinimumCriticalRaw=True

    def setHasProbeName (self):
        self._myHasProbeName=True

    def setHasStatusRaw (self):
        self._myHasStatusRaw=True




    # isRequested...() methods

    def isStatusRequested (self):
        return self._myStatusRequested

    def isIndexRequested (self):
        return self._myIndexRequested

    def isTemperatureRawRequested (self):
        return self._myTemperatureRawRequested

    def isMaximumCriticalRawRequested (self):
        return self._myMaximumCriticalRawRequested

    def isMaximumWarningRawRequested (self):
        return self._myMaximumWarningRawRequested

    def isMinimumWarningRawRequested (self):
        return self._myMinimumWarningRawRequested

    def isMinimumCriticalRawRequested (self):
        return self._myMinimumCriticalRawRequested

    def isProbeNameRequested (self):
        return self._myProbeNameRequested

    def isStatusRawRequested (self):
        return self._myStatusRawRequested




    # setRequested...() methods

    def setStatusRequested (self):
        self._myStatusRequested=True

    def setIndexRequested (self):
        self._myIndexRequested=True

    def setTemperatureRawRequested (self):
        self._myTemperatureRawRequested=True

    def setMaximumCriticalRawRequested (self):
        self._myMaximumCriticalRawRequested=True

    def setMaximumWarningRawRequested (self):
        self._myMaximumWarningRawRequested=True

    def setMinimumWarningRawRequested (self):
        self._myMinimumWarningRawRequested=True

    def setMinimumCriticalRawRequested (self):
        self._myMinimumCriticalRawRequested=True

    def setProbeNameRequested (self):
        self._myProbeNameRequested=True

    def setStatusRawRequested (self):
        self._myStatusRawRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myStatusRequested:
            x = "+Status="
            if self._myHasStatus:
                leafStr = str(self.status)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myIndexRequested:
            x = "+Index="
            if self._myHasIndex:
                leafStr = str(self.index)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTemperatureRawRequested:
            x = "+TemperatureRaw="
            if self._myHasTemperatureRaw:
                leafStr = str(self.temperatureRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMaximumCriticalRawRequested:
            x = "+MaximumCriticalRaw="
            if self._myHasMaximumCriticalRaw:
                leafStr = str(self.maximumCriticalRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMaximumWarningRawRequested:
            x = "+MaximumWarningRaw="
            if self._myHasMaximumWarningRaw:
                leafStr = str(self.maximumWarningRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMinimumWarningRawRequested:
            x = "+MinimumWarningRaw="
            if self._myHasMinimumWarningRaw:
                leafStr = str(self.minimumWarningRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMinimumCriticalRawRequested:
            x = "+MinimumCriticalRaw="
            if self._myHasMinimumCriticalRaw:
                leafStr = str(self.minimumCriticalRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myProbeNameRequested:
            x = "+ProbeName="
            if self._myHasProbeName:
                leafStr = str(self.probeName)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myStatusRawRequested:
            x = "+StatusRaw="
            if self._myHasStatusRaw:
                leafStr = str(self.statusRaw)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+Status="
        if self._myHasStatus:
            leafStr = str(self.status)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStatusRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Index="
        if self._myHasIndex:
            leafStr = str(self.index)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myIndexRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TemperatureRaw="
        if self._myHasTemperatureRaw:
            leafStr = str(self.temperatureRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTemperatureRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MaximumCriticalRaw="
        if self._myHasMaximumCriticalRaw:
            leafStr = str(self.maximumCriticalRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMaximumCriticalRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MaximumWarningRaw="
        if self._myHasMaximumWarningRaw:
            leafStr = str(self.maximumWarningRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMaximumWarningRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MinimumWarningRaw="
        if self._myHasMinimumWarningRaw:
            leafStr = str(self.minimumWarningRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMinimumWarningRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MinimumCriticalRaw="
        if self._myHasMinimumCriticalRaw:
            leafStr = str(self.minimumCriticalRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMinimumCriticalRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ProbeName="
        if self._myHasProbeName:
            leafStr = str(self.probeName)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myProbeNameRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+StatusRaw="
        if self._myHasStatusRaw:
            leafStr = str(self.statusRaw)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStatusRawRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setStatusRequested()
        self.setIndexRequested()
        self.setTemperatureRawRequested()
        self.setMaximumCriticalRawRequested()
        self.setMaximumWarningRawRequested()
        self.setMinimumWarningRawRequested()
        self.setMinimumCriticalRawRequested()
        self.setProbeNameRequested()
        self.setStatusRawRequested()
        
        


    def setStatus (self, status):
        self.status = status
        self.setHasStatus()

    def setIndex (self, index):
        self.index = index
        self.setHasIndex()

    def setTemperatureRaw (self, temperatureRaw):
        self.temperatureRaw = temperatureRaw
        self.setHasTemperatureRaw()

    def setMaximumCriticalRaw (self, maximumCriticalRaw):
        self.maximumCriticalRaw = maximumCriticalRaw
        self.setHasMaximumCriticalRaw()

    def setMaximumWarningRaw (self, maximumWarningRaw):
        self.maximumWarningRaw = maximumWarningRaw
        self.setHasMaximumWarningRaw()

    def setMinimumWarningRaw (self, minimumWarningRaw):
        self.minimumWarningRaw = minimumWarningRaw
        self.setHasMinimumWarningRaw()

    def setMinimumCriticalRaw (self, minimumCriticalRaw):
        self.minimumCriticalRaw = minimumCriticalRaw
        self.setHasMinimumCriticalRaw()

    def setProbeName (self, probeName):
        self.probeName = probeName
        self.setHasProbeName()

    def setStatusRaw (self, statusRaw):
        self.statusRaw = statusRaw
        self.setHasStatusRaw()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_temperature.tech.platform.temperature.sensor.device.status.status_oper_data_gen import StatusOperData"
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
            "namespace": "device", 
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
            "memberName": "status", 
            "yangName": "status", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "index", 
            "yangName": "index", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "temperatureRaw", 
            "yangName": "temperature-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumCriticalRaw", 
            "yangName": "maximum-critical-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumWarningRaw", 
            "yangName": "maximum-warning-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumWarningRaw", 
            "yangName": "minimum-warning-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumCriticalRaw", 
            "yangName": "minimum-critical-raw", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "probeName", 
            "yangName": "probe-name", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "statusRaw", 
            "yangName": "status-raw", 
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


