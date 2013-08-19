


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



from a.api.yang.modules.tech.common.qwilt_tech_types.qwilt_tech_types_module_gen import SeverityType


class SummaryOperData (object):

    def __init__ (self):

        self.errorCount = 0
        self._myHasErrorCount=False
        self._myErrorCountRequested=False
        
        self.emergencyCount = 0
        self._myHasEmergencyCount=False
        self._myEmergencyCountRequested=False
        
        self.highestSeverity = SeverityType.kNone
        self._myHasHighestSeverity=False
        self._myHighestSeverityRequested=False
        
        self.criticalCount = 0
        self._myHasCriticalCount=False
        self._myCriticalCountRequested=False
        
        self.warningCount = 0
        self._myHasWarningCount=False
        self._myWarningCountRequested=False
        
        self.alertCount = 0
        self._myHasAlertCount=False
        self._myAlertCountRequested=False
        
        self.noticeCount = 0
        self._myHasNoticeCount=False
        self._myNoticeCountRequested=False
        


    def copyFrom (self, other):

        self.errorCount=other.errorCount
        self._myHasErrorCount=other._myHasErrorCount
        self._myErrorCountRequested=other._myErrorCountRequested
        
        self.emergencyCount=other.emergencyCount
        self._myHasEmergencyCount=other._myHasEmergencyCount
        self._myEmergencyCountRequested=other._myEmergencyCountRequested
        
        self.highestSeverity=other.highestSeverity
        self._myHasHighestSeverity=other._myHasHighestSeverity
        self._myHighestSeverityRequested=other._myHighestSeverityRequested
        
        self.criticalCount=other.criticalCount
        self._myHasCriticalCount=other._myHasCriticalCount
        self._myCriticalCountRequested=other._myCriticalCountRequested
        
        self.warningCount=other.warningCount
        self._myHasWarningCount=other._myHasWarningCount
        self._myWarningCountRequested=other._myWarningCountRequested
        
        self.alertCount=other.alertCount
        self._myHasAlertCount=other._myHasAlertCount
        self._myAlertCountRequested=other._myAlertCountRequested
        
        self.noticeCount=other.noticeCount
        self._myHasNoticeCount=other._myHasNoticeCount
        self._myNoticeCountRequested=other._myNoticeCountRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isErrorCountRequested():
            self.errorCount=other.errorCount
            self._myHasErrorCount=other._myHasErrorCount
            self._myErrorCountRequested=other._myErrorCountRequested
        
        if self.isEmergencyCountRequested():
            self.emergencyCount=other.emergencyCount
            self._myHasEmergencyCount=other._myHasEmergencyCount
            self._myEmergencyCountRequested=other._myEmergencyCountRequested
        
        if self.isHighestSeverityRequested():
            self.highestSeverity=other.highestSeverity
            self._myHasHighestSeverity=other._myHasHighestSeverity
            self._myHighestSeverityRequested=other._myHighestSeverityRequested
        
        if self.isCriticalCountRequested():
            self.criticalCount=other.criticalCount
            self._myHasCriticalCount=other._myHasCriticalCount
            self._myCriticalCountRequested=other._myCriticalCountRequested
        
        if self.isWarningCountRequested():
            self.warningCount=other.warningCount
            self._myHasWarningCount=other._myHasWarningCount
            self._myWarningCountRequested=other._myWarningCountRequested
        
        if self.isAlertCountRequested():
            self.alertCount=other.alertCount
            self._myHasAlertCount=other._myHasAlertCount
            self._myAlertCountRequested=other._myAlertCountRequested
        
        if self.isNoticeCountRequested():
            self.noticeCount=other.noticeCount
            self._myHasNoticeCount=other._myHasNoticeCount
            self._myNoticeCountRequested=other._myNoticeCountRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasErrorCount():
            self.errorCount=other.errorCount
            self._myHasErrorCount=other._myHasErrorCount
            self._myErrorCountRequested=other._myErrorCountRequested
        
        if other.hasEmergencyCount():
            self.emergencyCount=other.emergencyCount
            self._myHasEmergencyCount=other._myHasEmergencyCount
            self._myEmergencyCountRequested=other._myEmergencyCountRequested
        
        if other.hasHighestSeverity():
            self.highestSeverity=other.highestSeverity
            self._myHasHighestSeverity=other._myHasHighestSeverity
            self._myHighestSeverityRequested=other._myHighestSeverityRequested
        
        if other.hasCriticalCount():
            self.criticalCount=other.criticalCount
            self._myHasCriticalCount=other._myHasCriticalCount
            self._myCriticalCountRequested=other._myCriticalCountRequested
        
        if other.hasWarningCount():
            self.warningCount=other.warningCount
            self._myHasWarningCount=other._myHasWarningCount
            self._myWarningCountRequested=other._myWarningCountRequested
        
        if other.hasAlertCount():
            self.alertCount=other.alertCount
            self._myHasAlertCount=other._myHasAlertCount
            self._myAlertCountRequested=other._myAlertCountRequested
        
        if other.hasNoticeCount():
            self.noticeCount=other.noticeCount
            self._myHasNoticeCount=other._myHasNoticeCount
            self._myNoticeCountRequested=other._myNoticeCountRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.errorCount=other.errorCount
        self._myHasErrorCount=other._myHasErrorCount
        
        self.emergencyCount=other.emergencyCount
        self._myHasEmergencyCount=other._myHasEmergencyCount
        
        self.highestSeverity=other.highestSeverity
        self._myHasHighestSeverity=other._myHasHighestSeverity
        
        self.criticalCount=other.criticalCount
        self._myHasCriticalCount=other._myHasCriticalCount
        
        self.warningCount=other.warningCount
        self._myHasWarningCount=other._myHasWarningCount
        
        self.alertCount=other.alertCount
        self._myHasAlertCount=other._myHasAlertCount
        
        self.noticeCount=other.noticeCount
        self._myHasNoticeCount=other._myHasNoticeCount
        


    def setAllNumericToZero (self):
        
        self.errorCount=0
        self.setHasErrorCount()
        self.emergencyCount=0
        self.setHasEmergencyCount()
        self.criticalCount=0
        self.setHasCriticalCount()
        self.warningCount=0
        self.setHasWarningCount()
        self.alertCount=0
        self.setHasAlertCount()
        self.noticeCount=0
        self.setHasNoticeCount()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasErrorCount():
            if other.hasErrorCount():
                self.errorCount -= other.errorCount
        
        if self.hasEmergencyCount():
            if other.hasEmergencyCount():
                self.emergencyCount -= other.emergencyCount
        
        if self.hasCriticalCount():
            if other.hasCriticalCount():
                self.criticalCount -= other.criticalCount
        
        if self.hasWarningCount():
            if other.hasWarningCount():
                self.warningCount -= other.warningCount
        
        if self.hasAlertCount():
            if other.hasAlertCount():
                self.alertCount -= other.alertCount
        
        if self.hasNoticeCount():
            if other.hasNoticeCount():
                self.noticeCount -= other.noticeCount
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasErrorCount():
            if other.hasErrorCount():
                self.errorCount += other.errorCount
        
        if self.hasEmergencyCount():
            if other.hasEmergencyCount():
                self.emergencyCount += other.emergencyCount
        
        if self.hasCriticalCount():
            if other.hasCriticalCount():
                self.criticalCount += other.criticalCount
        
        if self.hasWarningCount():
            if other.hasWarningCount():
                self.warningCount += other.warningCount
        
        if self.hasAlertCount():
            if other.hasAlertCount():
                self.alertCount += other.alertCount
        
        if self.hasNoticeCount():
            if other.hasNoticeCount():
                self.noticeCount += other.noticeCount
        
        
        pass


    # has...() methods

    def hasErrorCount (self):
        return self._myHasErrorCount

    def hasEmergencyCount (self):
        return self._myHasEmergencyCount

    def hasHighestSeverity (self):
        return self._myHasHighestSeverity

    def hasCriticalCount (self):
        return self._myHasCriticalCount

    def hasWarningCount (self):
        return self._myHasWarningCount

    def hasAlertCount (self):
        return self._myHasAlertCount

    def hasNoticeCount (self):
        return self._myHasNoticeCount




    # setHas...() methods

    def setHasErrorCount (self):
        self._myHasErrorCount=True

    def setHasEmergencyCount (self):
        self._myHasEmergencyCount=True

    def setHasHighestSeverity (self):
        self._myHasHighestSeverity=True

    def setHasCriticalCount (self):
        self._myHasCriticalCount=True

    def setHasWarningCount (self):
        self._myHasWarningCount=True

    def setHasAlertCount (self):
        self._myHasAlertCount=True

    def setHasNoticeCount (self):
        self._myHasNoticeCount=True




    # isRequested...() methods

    def isErrorCountRequested (self):
        return self._myErrorCountRequested

    def isEmergencyCountRequested (self):
        return self._myEmergencyCountRequested

    def isHighestSeverityRequested (self):
        return self._myHighestSeverityRequested

    def isCriticalCountRequested (self):
        return self._myCriticalCountRequested

    def isWarningCountRequested (self):
        return self._myWarningCountRequested

    def isAlertCountRequested (self):
        return self._myAlertCountRequested

    def isNoticeCountRequested (self):
        return self._myNoticeCountRequested




    # setRequested...() methods

    def setErrorCountRequested (self):
        self._myErrorCountRequested=True

    def setEmergencyCountRequested (self):
        self._myEmergencyCountRequested=True

    def setHighestSeverityRequested (self):
        self._myHighestSeverityRequested=True

    def setCriticalCountRequested (self):
        self._myCriticalCountRequested=True

    def setWarningCountRequested (self):
        self._myWarningCountRequested=True

    def setAlertCountRequested (self):
        self._myAlertCountRequested=True

    def setNoticeCountRequested (self):
        self._myNoticeCountRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myErrorCountRequested:
            x = "+ErrorCount="
            if self._myHasErrorCount:
                leafStr = str(self.errorCount)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myEmergencyCountRequested:
            x = "+EmergencyCount="
            if self._myHasEmergencyCount:
                leafStr = str(self.emergencyCount)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myHighestSeverityRequested:
            x = "+HighestSeverity="
            if self._myHasHighestSeverity:
                leafStr = str(self.highestSeverity)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myCriticalCountRequested:
            x = "+CriticalCount="
            if self._myHasCriticalCount:
                leafStr = str(self.criticalCount)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myWarningCountRequested:
            x = "+WarningCount="
            if self._myHasWarningCount:
                leafStr = str(self.warningCount)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myAlertCountRequested:
            x = "+AlertCount="
            if self._myHasAlertCount:
                leafStr = str(self.alertCount)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNoticeCountRequested:
            x = "+NoticeCount="
            if self._myHasNoticeCount:
                leafStr = str(self.noticeCount)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{SummaryOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ErrorCount="
        if self._myHasErrorCount:
            leafStr = str(self.errorCount)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myErrorCountRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+EmergencyCount="
        if self._myHasEmergencyCount:
            leafStr = str(self.emergencyCount)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myEmergencyCountRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+HighestSeverity="
        if self._myHasHighestSeverity:
            leafStr = str(self.highestSeverity)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myHighestSeverityRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+CriticalCount="
        if self._myHasCriticalCount:
            leafStr = str(self.criticalCount)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCriticalCountRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+WarningCount="
        if self._myHasWarningCount:
            leafStr = str(self.warningCount)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myWarningCountRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+AlertCount="
        if self._myHasAlertCount:
            leafStr = str(self.alertCount)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myAlertCountRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+NoticeCount="
        if self._myHasNoticeCount:
            leafStr = str(self.noticeCount)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNoticeCountRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{SummaryOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setErrorCountRequested()
        self.setEmergencyCountRequested()
        self.setHighestSeverityRequested()
        self.setCriticalCountRequested()
        self.setWarningCountRequested()
        self.setAlertCountRequested()
        self.setNoticeCountRequested()
        
        


    def setErrorCount (self, errorCount):
        self.errorCount = errorCount
        self.setHasErrorCount()

    def setEmergencyCount (self, emergencyCount):
        self.emergencyCount = emergencyCount
        self.setHasEmergencyCount()

    def setHighestSeverity (self, highestSeverity):
        self.highestSeverity = highestSeverity
        self.setHasHighestSeverity()

    def setCriticalCount (self, criticalCount):
        self.criticalCount = criticalCount
        self.setHasCriticalCount()

    def setWarningCount (self, warningCount):
        self.warningCount = warningCount
        self.setHasWarningCount()

    def setAlertCount (self, alertCount):
        self.alertCount = alertCount
        self.setHasAlertCount()

    def setNoticeCount (self, noticeCount):
        self.noticeCount = noticeCount
        self.setHasNoticeCount()


"""
Extracted from the below data: 
{
    "node": {
        "className": "SummaryOperData", 
        "namespace": "summary", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_alarms.tech.system.alarms.summary.summary_oper_data_gen import SummaryOperData"
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
            "namespace": "summary", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "errorCount", 
            "yangName": "error-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "emergencyCount", 
            "yangName": "emergency-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: EnumHandlerPy", 
            "memberName": "highestSeverity", 
            "yangName": "highest-severity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "criticalCount", 
            "yangName": "critical-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "warningCount", 
            "yangName": "warning-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "alertCount", 
            "yangName": "alert-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "noticeCount", 
            "yangName": "notice-count", 
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


