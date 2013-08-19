


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



from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.qwilt_tech_platform_fans_module_gen import FanDeviceStatusType


class StatusOperData (object):

    def __init__ (self):

        self.status = FanDeviceStatusType.kNone
        self._myHasStatus=False
        self._myStatusRequested=False
        
        self.index = ""
        self._myHasIndex=False
        self._myIndexRequested=False
        
        self.minimumWarningRpm = ""
        self._myHasMinimumWarningRpm=False
        self._myMinimumWarningRpmRequested=False
        
        self.currentRpm = ""
        self._myHasCurrentRpm=False
        self._myCurrentRpmRequested=False
        
        self.maximumWarningRpm = ""
        self._myHasMaximumWarningRpm=False
        self._myMaximumWarningRpmRequested=False
        
        self.probeName = ""
        self._myHasProbeName=False
        self._myProbeNameRequested=False
        
        self.statusRaw = ""
        self._myHasStatusRaw=False
        self._myStatusRawRequested=False
        
        self.minimumErrorRpm = ""
        self._myHasMinimumErrorRpm=False
        self._myMinimumErrorRpmRequested=False
        
        self.maximumErrorRpm = ""
        self._myHasMaximumErrorRpm=False
        self._myMaximumErrorRpmRequested=False
        


    def copyFrom (self, other):

        self.status=other.status
        self._myHasStatus=other._myHasStatus
        self._myStatusRequested=other._myStatusRequested
        
        self.index=other.index
        self._myHasIndex=other._myHasIndex
        self._myIndexRequested=other._myIndexRequested
        
        self.minimumWarningRpm=other.minimumWarningRpm
        self._myHasMinimumWarningRpm=other._myHasMinimumWarningRpm
        self._myMinimumWarningRpmRequested=other._myMinimumWarningRpmRequested
        
        self.currentRpm=other.currentRpm
        self._myHasCurrentRpm=other._myHasCurrentRpm
        self._myCurrentRpmRequested=other._myCurrentRpmRequested
        
        self.maximumWarningRpm=other.maximumWarningRpm
        self._myHasMaximumWarningRpm=other._myHasMaximumWarningRpm
        self._myMaximumWarningRpmRequested=other._myMaximumWarningRpmRequested
        
        self.probeName=other.probeName
        self._myHasProbeName=other._myHasProbeName
        self._myProbeNameRequested=other._myProbeNameRequested
        
        self.statusRaw=other.statusRaw
        self._myHasStatusRaw=other._myHasStatusRaw
        self._myStatusRawRequested=other._myStatusRawRequested
        
        self.minimumErrorRpm=other.minimumErrorRpm
        self._myHasMinimumErrorRpm=other._myHasMinimumErrorRpm
        self._myMinimumErrorRpmRequested=other._myMinimumErrorRpmRequested
        
        self.maximumErrorRpm=other.maximumErrorRpm
        self._myHasMaximumErrorRpm=other._myHasMaximumErrorRpm
        self._myMaximumErrorRpmRequested=other._myMaximumErrorRpmRequested
        


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
        
        if self.isMinimumWarningRpmRequested():
            self.minimumWarningRpm=other.minimumWarningRpm
            self._myHasMinimumWarningRpm=other._myHasMinimumWarningRpm
            self._myMinimumWarningRpmRequested=other._myMinimumWarningRpmRequested
        
        if self.isCurrentRpmRequested():
            self.currentRpm=other.currentRpm
            self._myHasCurrentRpm=other._myHasCurrentRpm
            self._myCurrentRpmRequested=other._myCurrentRpmRequested
        
        if self.isMaximumWarningRpmRequested():
            self.maximumWarningRpm=other.maximumWarningRpm
            self._myHasMaximumWarningRpm=other._myHasMaximumWarningRpm
            self._myMaximumWarningRpmRequested=other._myMaximumWarningRpmRequested
        
        if self.isProbeNameRequested():
            self.probeName=other.probeName
            self._myHasProbeName=other._myHasProbeName
            self._myProbeNameRequested=other._myProbeNameRequested
        
        if self.isStatusRawRequested():
            self.statusRaw=other.statusRaw
            self._myHasStatusRaw=other._myHasStatusRaw
            self._myStatusRawRequested=other._myStatusRawRequested
        
        if self.isMinimumErrorRpmRequested():
            self.minimumErrorRpm=other.minimumErrorRpm
            self._myHasMinimumErrorRpm=other._myHasMinimumErrorRpm
            self._myMinimumErrorRpmRequested=other._myMinimumErrorRpmRequested
        
        if self.isMaximumErrorRpmRequested():
            self.maximumErrorRpm=other.maximumErrorRpm
            self._myHasMaximumErrorRpm=other._myHasMaximumErrorRpm
            self._myMaximumErrorRpmRequested=other._myMaximumErrorRpmRequested
        


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
        
        if other.hasMinimumWarningRpm():
            self.minimumWarningRpm=other.minimumWarningRpm
            self._myHasMinimumWarningRpm=other._myHasMinimumWarningRpm
            self._myMinimumWarningRpmRequested=other._myMinimumWarningRpmRequested
        
        if other.hasCurrentRpm():
            self.currentRpm=other.currentRpm
            self._myHasCurrentRpm=other._myHasCurrentRpm
            self._myCurrentRpmRequested=other._myCurrentRpmRequested
        
        if other.hasMaximumWarningRpm():
            self.maximumWarningRpm=other.maximumWarningRpm
            self._myHasMaximumWarningRpm=other._myHasMaximumWarningRpm
            self._myMaximumWarningRpmRequested=other._myMaximumWarningRpmRequested
        
        if other.hasProbeName():
            self.probeName=other.probeName
            self._myHasProbeName=other._myHasProbeName
            self._myProbeNameRequested=other._myProbeNameRequested
        
        if other.hasStatusRaw():
            self.statusRaw=other.statusRaw
            self._myHasStatusRaw=other._myHasStatusRaw
            self._myStatusRawRequested=other._myStatusRawRequested
        
        if other.hasMinimumErrorRpm():
            self.minimumErrorRpm=other.minimumErrorRpm
            self._myHasMinimumErrorRpm=other._myHasMinimumErrorRpm
            self._myMinimumErrorRpmRequested=other._myMinimumErrorRpmRequested
        
        if other.hasMaximumErrorRpm():
            self.maximumErrorRpm=other.maximumErrorRpm
            self._myHasMaximumErrorRpm=other._myHasMaximumErrorRpm
            self._myMaximumErrorRpmRequested=other._myMaximumErrorRpmRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.status=other.status
        self._myHasStatus=other._myHasStatus
        
        self.index=other.index
        self._myHasIndex=other._myHasIndex
        
        self.minimumWarningRpm=other.minimumWarningRpm
        self._myHasMinimumWarningRpm=other._myHasMinimumWarningRpm
        
        self.currentRpm=other.currentRpm
        self._myHasCurrentRpm=other._myHasCurrentRpm
        
        self.maximumWarningRpm=other.maximumWarningRpm
        self._myHasMaximumWarningRpm=other._myHasMaximumWarningRpm
        
        self.probeName=other.probeName
        self._myHasProbeName=other._myHasProbeName
        
        self.statusRaw=other.statusRaw
        self._myHasStatusRaw=other._myHasStatusRaw
        
        self.minimumErrorRpm=other.minimumErrorRpm
        self._myHasMinimumErrorRpm=other._myHasMinimumErrorRpm
        
        self.maximumErrorRpm=other.maximumErrorRpm
        self._myHasMaximumErrorRpm=other._myHasMaximumErrorRpm
        


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

    def hasMinimumWarningRpm (self):
        return self._myHasMinimumWarningRpm

    def hasCurrentRpm (self):
        return self._myHasCurrentRpm

    def hasMaximumWarningRpm (self):
        return self._myHasMaximumWarningRpm

    def hasProbeName (self):
        return self._myHasProbeName

    def hasStatusRaw (self):
        return self._myHasStatusRaw

    def hasMinimumErrorRpm (self):
        return self._myHasMinimumErrorRpm

    def hasMaximumErrorRpm (self):
        return self._myHasMaximumErrorRpm




    # setHas...() methods

    def setHasStatus (self):
        self._myHasStatus=True

    def setHasIndex (self):
        self._myHasIndex=True

    def setHasMinimumWarningRpm (self):
        self._myHasMinimumWarningRpm=True

    def setHasCurrentRpm (self):
        self._myHasCurrentRpm=True

    def setHasMaximumWarningRpm (self):
        self._myHasMaximumWarningRpm=True

    def setHasProbeName (self):
        self._myHasProbeName=True

    def setHasStatusRaw (self):
        self._myHasStatusRaw=True

    def setHasMinimumErrorRpm (self):
        self._myHasMinimumErrorRpm=True

    def setHasMaximumErrorRpm (self):
        self._myHasMaximumErrorRpm=True




    # isRequested...() methods

    def isStatusRequested (self):
        return self._myStatusRequested

    def isIndexRequested (self):
        return self._myIndexRequested

    def isMinimumWarningRpmRequested (self):
        return self._myMinimumWarningRpmRequested

    def isCurrentRpmRequested (self):
        return self._myCurrentRpmRequested

    def isMaximumWarningRpmRequested (self):
        return self._myMaximumWarningRpmRequested

    def isProbeNameRequested (self):
        return self._myProbeNameRequested

    def isStatusRawRequested (self):
        return self._myStatusRawRequested

    def isMinimumErrorRpmRequested (self):
        return self._myMinimumErrorRpmRequested

    def isMaximumErrorRpmRequested (self):
        return self._myMaximumErrorRpmRequested




    # setRequested...() methods

    def setStatusRequested (self):
        self._myStatusRequested=True

    def setIndexRequested (self):
        self._myIndexRequested=True

    def setMinimumWarningRpmRequested (self):
        self._myMinimumWarningRpmRequested=True

    def setCurrentRpmRequested (self):
        self._myCurrentRpmRequested=True

    def setMaximumWarningRpmRequested (self):
        self._myMaximumWarningRpmRequested=True

    def setProbeNameRequested (self):
        self._myProbeNameRequested=True

    def setStatusRawRequested (self):
        self._myStatusRawRequested=True

    def setMinimumErrorRpmRequested (self):
        self._myMinimumErrorRpmRequested=True

    def setMaximumErrorRpmRequested (self):
        self._myMaximumErrorRpmRequested=True




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
        if self._myMinimumWarningRpmRequested:
            x = "+MinimumWarningRpm="
            if self._myHasMinimumWarningRpm:
                leafStr = str(self.minimumWarningRpm)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myCurrentRpmRequested:
            x = "+CurrentRpm="
            if self._myHasCurrentRpm:
                leafStr = str(self.currentRpm)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMaximumWarningRpmRequested:
            x = "+MaximumWarningRpm="
            if self._myHasMaximumWarningRpm:
                leafStr = str(self.maximumWarningRpm)
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

        x=""
        if self._myMinimumErrorRpmRequested:
            x = "+MinimumErrorRpm="
            if self._myHasMinimumErrorRpm:
                leafStr = str(self.minimumErrorRpm)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMaximumErrorRpmRequested:
            x = "+MaximumErrorRpm="
            if self._myHasMaximumErrorRpm:
                leafStr = str(self.maximumErrorRpm)
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
        x = "+MinimumWarningRpm="
        if self._myHasMinimumWarningRpm:
            leafStr = str(self.minimumWarningRpm)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMinimumWarningRpmRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+CurrentRpm="
        if self._myHasCurrentRpm:
            leafStr = str(self.currentRpm)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCurrentRpmRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MaximumWarningRpm="
        if self._myHasMaximumWarningRpm:
            leafStr = str(self.maximumWarningRpm)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMaximumWarningRpmRequested:
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

        x=""
        x = "+MinimumErrorRpm="
        if self._myHasMinimumErrorRpm:
            leafStr = str(self.minimumErrorRpm)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMinimumErrorRpmRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+MaximumErrorRpm="
        if self._myHasMaximumErrorRpm:
            leafStr = str(self.maximumErrorRpm)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMaximumErrorRpmRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setStatusRequested()
        self.setIndexRequested()
        self.setMinimumWarningRpmRequested()
        self.setCurrentRpmRequested()
        self.setMaximumWarningRpmRequested()
        self.setProbeNameRequested()
        self.setStatusRawRequested()
        self.setMinimumErrorRpmRequested()
        self.setMaximumErrorRpmRequested()
        
        


    def setStatus (self, status):
        self.status = status
        self.setHasStatus()

    def setIndex (self, index):
        self.index = index
        self.setHasIndex()

    def setMinimumWarningRpm (self, minimumWarningRpm):
        self.minimumWarningRpm = minimumWarningRpm
        self.setHasMinimumWarningRpm()

    def setCurrentRpm (self, currentRpm):
        self.currentRpm = currentRpm
        self.setHasCurrentRpm()

    def setMaximumWarningRpm (self, maximumWarningRpm):
        self.maximumWarningRpm = maximumWarningRpm
        self.setHasMaximumWarningRpm()

    def setProbeName (self, probeName):
        self.probeName = probeName
        self.setHasProbeName()

    def setStatusRaw (self, statusRaw):
        self.statusRaw = statusRaw
        self.setHasStatusRaw()

    def setMinimumErrorRpm (self, minimumErrorRpm):
        self.minimumErrorRpm = minimumErrorRpm
        self.setHasMinimumErrorRpm()

    def setMaximumErrorRpm (self, maximumErrorRpm):
        self.maximumErrorRpm = maximumErrorRpm
        self.setHasMaximumErrorRpm()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_fans.tech.platform.fans.fan.device.status.status_oper_data_gen import StatusOperData"
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
            "memberName": "minimumWarningRpm", 
            "yangName": "minimum-warning-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "currentRpm", 
            "yangName": "current-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumWarningRpm", 
            "yangName": "maximum-warning-rpm", 
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
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "minimumErrorRpm", 
            "yangName": "minimum-error-rpm", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "maximumErrorRpm", 
            "yangName": "maximum-error-rpm", 
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


