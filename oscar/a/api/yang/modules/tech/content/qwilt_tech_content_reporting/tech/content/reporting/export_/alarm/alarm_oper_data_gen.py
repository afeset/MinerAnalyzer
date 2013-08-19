


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



from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.qwilt_tech_content_reporting_module_gen import ReportingExportQueueFullReasonType


class AlarmOperData (object):

    def __init__ (self):

        self.reportsQueueGettingFullReason = ReportingExportQueueFullReasonType.kNone
        self._myHasReportsQueueGettingFullReason=False
        self._myReportsQueueGettingFullReasonRequested=False
        
        self.reportsQueueGettingFull = False
        self._myHasReportsQueueGettingFull=False
        self._myReportsQueueGettingFullRequested=False
        
        self.reportsQueueFullReason = ReportingExportQueueFullReasonType.kNone
        self._myHasReportsQueueFullReason=False
        self._myReportsQueueFullReasonRequested=False
        
        self.reportsQueueFull = False
        self._myHasReportsQueueFull=False
        self._myReportsQueueFullRequested=False
        


    def copyFrom (self, other):

        self.reportsQueueGettingFullReason=other.reportsQueueGettingFullReason
        self._myHasReportsQueueGettingFullReason=other._myHasReportsQueueGettingFullReason
        self._myReportsQueueGettingFullReasonRequested=other._myReportsQueueGettingFullReasonRequested
        
        self.reportsQueueGettingFull=other.reportsQueueGettingFull
        self._myHasReportsQueueGettingFull=other._myHasReportsQueueGettingFull
        self._myReportsQueueGettingFullRequested=other._myReportsQueueGettingFullRequested
        
        self.reportsQueueFullReason=other.reportsQueueFullReason
        self._myHasReportsQueueFullReason=other._myHasReportsQueueFullReason
        self._myReportsQueueFullReasonRequested=other._myReportsQueueFullReasonRequested
        
        self.reportsQueueFull=other.reportsQueueFull
        self._myHasReportsQueueFull=other._myHasReportsQueueFull
        self._myReportsQueueFullRequested=other._myReportsQueueFullRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isReportsQueueGettingFullReasonRequested():
            self.reportsQueueGettingFullReason=other.reportsQueueGettingFullReason
            self._myHasReportsQueueGettingFullReason=other._myHasReportsQueueGettingFullReason
            self._myReportsQueueGettingFullReasonRequested=other._myReportsQueueGettingFullReasonRequested
        
        if self.isReportsQueueGettingFullRequested():
            self.reportsQueueGettingFull=other.reportsQueueGettingFull
            self._myHasReportsQueueGettingFull=other._myHasReportsQueueGettingFull
            self._myReportsQueueGettingFullRequested=other._myReportsQueueGettingFullRequested
        
        if self.isReportsQueueFullReasonRequested():
            self.reportsQueueFullReason=other.reportsQueueFullReason
            self._myHasReportsQueueFullReason=other._myHasReportsQueueFullReason
            self._myReportsQueueFullReasonRequested=other._myReportsQueueFullReasonRequested
        
        if self.isReportsQueueFullRequested():
            self.reportsQueueFull=other.reportsQueueFull
            self._myHasReportsQueueFull=other._myHasReportsQueueFull
            self._myReportsQueueFullRequested=other._myReportsQueueFullRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasReportsQueueGettingFullReason():
            self.reportsQueueGettingFullReason=other.reportsQueueGettingFullReason
            self._myHasReportsQueueGettingFullReason=other._myHasReportsQueueGettingFullReason
            self._myReportsQueueGettingFullReasonRequested=other._myReportsQueueGettingFullReasonRequested
        
        if other.hasReportsQueueGettingFull():
            self.reportsQueueGettingFull=other.reportsQueueGettingFull
            self._myHasReportsQueueGettingFull=other._myHasReportsQueueGettingFull
            self._myReportsQueueGettingFullRequested=other._myReportsQueueGettingFullRequested
        
        if other.hasReportsQueueFullReason():
            self.reportsQueueFullReason=other.reportsQueueFullReason
            self._myHasReportsQueueFullReason=other._myHasReportsQueueFullReason
            self._myReportsQueueFullReasonRequested=other._myReportsQueueFullReasonRequested
        
        if other.hasReportsQueueFull():
            self.reportsQueueFull=other.reportsQueueFull
            self._myHasReportsQueueFull=other._myHasReportsQueueFull
            self._myReportsQueueFullRequested=other._myReportsQueueFullRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.reportsQueueGettingFullReason=other.reportsQueueGettingFullReason
        self._myHasReportsQueueGettingFullReason=other._myHasReportsQueueGettingFullReason
        
        self.reportsQueueGettingFull=other.reportsQueueGettingFull
        self._myHasReportsQueueGettingFull=other._myHasReportsQueueGettingFull
        
        self.reportsQueueFullReason=other.reportsQueueFullReason
        self._myHasReportsQueueFullReason=other._myHasReportsQueueFullReason
        
        self.reportsQueueFull=other.reportsQueueFull
        self._myHasReportsQueueFull=other._myHasReportsQueueFull
        


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

    def hasReportsQueueGettingFullReason (self):
        return self._myHasReportsQueueGettingFullReason

    def hasReportsQueueGettingFull (self):
        return self._myHasReportsQueueGettingFull

    def hasReportsQueueFullReason (self):
        return self._myHasReportsQueueFullReason

    def hasReportsQueueFull (self):
        return self._myHasReportsQueueFull




    # setHas...() methods

    def setHasReportsQueueGettingFullReason (self):
        self._myHasReportsQueueGettingFullReason=True

    def setHasReportsQueueGettingFull (self):
        self._myHasReportsQueueGettingFull=True

    def setHasReportsQueueFullReason (self):
        self._myHasReportsQueueFullReason=True

    def setHasReportsQueueFull (self):
        self._myHasReportsQueueFull=True




    # isRequested...() methods

    def isReportsQueueGettingFullReasonRequested (self):
        return self._myReportsQueueGettingFullReasonRequested

    def isReportsQueueGettingFullRequested (self):
        return self._myReportsQueueGettingFullRequested

    def isReportsQueueFullReasonRequested (self):
        return self._myReportsQueueFullReasonRequested

    def isReportsQueueFullRequested (self):
        return self._myReportsQueueFullRequested




    # setRequested...() methods

    def setReportsQueueGettingFullReasonRequested (self):
        self._myReportsQueueGettingFullReasonRequested=True

    def setReportsQueueGettingFullRequested (self):
        self._myReportsQueueGettingFullRequested=True

    def setReportsQueueFullReasonRequested (self):
        self._myReportsQueueFullReasonRequested=True

    def setReportsQueueFullRequested (self):
        self._myReportsQueueFullRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myReportsQueueGettingFullReasonRequested:
            x = "+ReportsQueueGettingFullReason="
            if self._myHasReportsQueueGettingFullReason:
                leafStr = str(self.reportsQueueGettingFullReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myReportsQueueGettingFullRequested:
            x = "+ReportsQueueGettingFull="
            if self._myHasReportsQueueGettingFull:
                leafStr = str(self.reportsQueueGettingFull)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myReportsQueueFullReasonRequested:
            x = "+ReportsQueueFullReason="
            if self._myHasReportsQueueFullReason:
                leafStr = str(self.reportsQueueFullReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myReportsQueueFullRequested:
            x = "+ReportsQueueFull="
            if self._myHasReportsQueueFull:
                leafStr = str(self.reportsQueueFull)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{AlarmOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ReportsQueueGettingFullReason="
        if self._myHasReportsQueueGettingFullReason:
            leafStr = str(self.reportsQueueGettingFullReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myReportsQueueGettingFullReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ReportsQueueGettingFull="
        if self._myHasReportsQueueGettingFull:
            leafStr = str(self.reportsQueueGettingFull)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myReportsQueueGettingFullRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ReportsQueueFullReason="
        if self._myHasReportsQueueFullReason:
            leafStr = str(self.reportsQueueFullReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myReportsQueueFullReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ReportsQueueFull="
        if self._myHasReportsQueueFull:
            leafStr = str(self.reportsQueueFull)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myReportsQueueFullRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{AlarmOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setReportsQueueGettingFullReasonRequested()
        self.setReportsQueueGettingFullRequested()
        self.setReportsQueueFullReasonRequested()
        self.setReportsQueueFullRequested()
        
        


    def setReportsQueueGettingFullReason (self, reportsQueueGettingFullReason):
        self.reportsQueueGettingFullReason = reportsQueueGettingFullReason
        self.setHasReportsQueueGettingFullReason()

    def setReportsQueueGettingFull (self, reportsQueueGettingFull):
        self.reportsQueueGettingFull = reportsQueueGettingFull
        self.setHasReportsQueueGettingFull()

    def setReportsQueueFullReason (self, reportsQueueFullReason):
        self.reportsQueueFullReason = reportsQueueFullReason
        self.setHasReportsQueueFullReason()

    def setReportsQueueFull (self, reportsQueueFull):
        self.reportsQueueFull = reportsQueueFull
        self.setHasReportsQueueFull()


"""
Extracted from the below data: 
{
    "node": {
        "className": "AlarmOperData", 
        "namespace": "alarm", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.alarm.alarm_oper_data_gen import AlarmOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "content", 
            "isCurrent": false
        }, 
        {
            "namespace": "reporting", 
            "isCurrent": false
        }, 
        {
            "namespace": "export_", 
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
            "memberName": "reportsQueueGettingFullReason", 
            "yangName": "reports-queue-getting-full-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "reportsQueueGettingFull", 
            "yangName": "reports-queue-getting-full", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "reportsQueueFullReason", 
            "yangName": "reports-queue-full-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "reportsQueueFull", 
            "yangName": "reports-queue-full", 
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
            "content", 
            "qwilt_tech_content_reporting"
        ]
    }, 
    "createTime": "2013"
}
"""


