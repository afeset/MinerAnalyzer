


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



from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.qwilt_tech_storage_disk_module_gen import ContentDiskFailureReasonType


class AlarmsOperData (object):

    def __init__ (self):

        self.contentDiskFailureReason = ContentDiskFailureReasonType.kNone
        self._myHasContentDiskFailureReason=False
        self._myContentDiskFailureReasonRequested=False
        
        self.contentDiskFailureAlarm = False
        self._myHasContentDiskFailureAlarm=False
        self._myContentDiskFailureAlarmRequested=False
        


    def copyFrom (self, other):

        self.contentDiskFailureReason=other.contentDiskFailureReason
        self._myHasContentDiskFailureReason=other._myHasContentDiskFailureReason
        self._myContentDiskFailureReasonRequested=other._myContentDiskFailureReasonRequested
        
        self.contentDiskFailureAlarm=other.contentDiskFailureAlarm
        self._myHasContentDiskFailureAlarm=other._myHasContentDiskFailureAlarm
        self._myContentDiskFailureAlarmRequested=other._myContentDiskFailureAlarmRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isContentDiskFailureReasonRequested():
            self.contentDiskFailureReason=other.contentDiskFailureReason
            self._myHasContentDiskFailureReason=other._myHasContentDiskFailureReason
            self._myContentDiskFailureReasonRequested=other._myContentDiskFailureReasonRequested
        
        if self.isContentDiskFailureAlarmRequested():
            self.contentDiskFailureAlarm=other.contentDiskFailureAlarm
            self._myHasContentDiskFailureAlarm=other._myHasContentDiskFailureAlarm
            self._myContentDiskFailureAlarmRequested=other._myContentDiskFailureAlarmRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasContentDiskFailureReason():
            self.contentDiskFailureReason=other.contentDiskFailureReason
            self._myHasContentDiskFailureReason=other._myHasContentDiskFailureReason
            self._myContentDiskFailureReasonRequested=other._myContentDiskFailureReasonRequested
        
        if other.hasContentDiskFailureAlarm():
            self.contentDiskFailureAlarm=other.contentDiskFailureAlarm
            self._myHasContentDiskFailureAlarm=other._myHasContentDiskFailureAlarm
            self._myContentDiskFailureAlarmRequested=other._myContentDiskFailureAlarmRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.contentDiskFailureReason=other.contentDiskFailureReason
        self._myHasContentDiskFailureReason=other._myHasContentDiskFailureReason
        
        self.contentDiskFailureAlarm=other.contentDiskFailureAlarm
        self._myHasContentDiskFailureAlarm=other._myHasContentDiskFailureAlarm
        


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

    def hasContentDiskFailureReason (self):
        return self._myHasContentDiskFailureReason

    def hasContentDiskFailureAlarm (self):
        return self._myHasContentDiskFailureAlarm




    # setHas...() methods

    def setHasContentDiskFailureReason (self):
        self._myHasContentDiskFailureReason=True

    def setHasContentDiskFailureAlarm (self):
        self._myHasContentDiskFailureAlarm=True




    # isRequested...() methods

    def isContentDiskFailureReasonRequested (self):
        return self._myContentDiskFailureReasonRequested

    def isContentDiskFailureAlarmRequested (self):
        return self._myContentDiskFailureAlarmRequested




    # setRequested...() methods

    def setContentDiskFailureReasonRequested (self):
        self._myContentDiskFailureReasonRequested=True

    def setContentDiskFailureAlarmRequested (self):
        self._myContentDiskFailureAlarmRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myContentDiskFailureReasonRequested:
            x = "+ContentDiskFailureReason="
            if self._myHasContentDiskFailureReason:
                leafStr = str(self.contentDiskFailureReason)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myContentDiskFailureAlarmRequested:
            x = "+ContentDiskFailureAlarm="
            if self._myHasContentDiskFailureAlarm:
                leafStr = str(self.contentDiskFailureAlarm)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{AlarmsOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ContentDiskFailureReason="
        if self._myHasContentDiskFailureReason:
            leafStr = str(self.contentDiskFailureReason)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myContentDiskFailureReasonRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ContentDiskFailureAlarm="
        if self._myHasContentDiskFailureAlarm:
            leafStr = str(self.contentDiskFailureAlarm)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myContentDiskFailureAlarmRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{AlarmsOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setContentDiskFailureReasonRequested()
        self.setContentDiskFailureAlarmRequested()
        
        


    def setContentDiskFailureReason (self, contentDiskFailureReason):
        self.contentDiskFailureReason = contentDiskFailureReason
        self.setHasContentDiskFailureReason()

    def setContentDiskFailureAlarm (self, contentDiskFailureAlarm):
        self.contentDiskFailureAlarm = contentDiskFailureAlarm
        self.setHasContentDiskFailureAlarm()


"""
Extracted from the below data: 
{
    "node": {
        "className": "AlarmsOperData", 
        "namespace": "alarms", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_storage_disk.tech.storage.disk.alarms.alarms_oper_data_gen import AlarmsOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "storage", 
            "isCurrent": false
        }, 
        {
            "namespace": "disk", 
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
            "memberName": "contentDiskFailureReason", 
            "yangName": "content-disk-failure-reason", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "contentDiskFailureAlarm", 
            "yangName": "content-disk-failure-alarm", 
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
            "qwilt_tech_storage_disk"
        ]
    }, 
    "createTime": "2013"
}
"""


