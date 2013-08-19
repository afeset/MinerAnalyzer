


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





class StatusOperData (object):

    def __init__ (self):

        self.localTimeString = ""
        self._myHasLocalTimeString=False
        self._myLocalTimeStringRequested=False
        
        self.utcTimeString = ""
        self._myHasUtcTimeString=False
        self._myUtcTimeStringRequested=False
        
        self.daylightSavingTime = False
        self._myHasDaylightSavingTime=False
        self._myDaylightSavingTimeRequested=False
        
        self.epoch = 0
        self._myHasEpoch=False
        self._myEpochRequested=False
        
        self.utcOffsetMinutes = 0
        self._myHasUtcOffsetMinutes=False
        self._myUtcOffsetMinutesRequested=False
        


    def copyFrom (self, other):

        self.localTimeString=other.localTimeString
        self._myHasLocalTimeString=other._myHasLocalTimeString
        self._myLocalTimeStringRequested=other._myLocalTimeStringRequested
        
        self.utcTimeString=other.utcTimeString
        self._myHasUtcTimeString=other._myHasUtcTimeString
        self._myUtcTimeStringRequested=other._myUtcTimeStringRequested
        
        self.daylightSavingTime=other.daylightSavingTime
        self._myHasDaylightSavingTime=other._myHasDaylightSavingTime
        self._myDaylightSavingTimeRequested=other._myDaylightSavingTimeRequested
        
        self.epoch=other.epoch
        self._myHasEpoch=other._myHasEpoch
        self._myEpochRequested=other._myEpochRequested
        
        self.utcOffsetMinutes=other.utcOffsetMinutes
        self._myHasUtcOffsetMinutes=other._myHasUtcOffsetMinutes
        self._myUtcOffsetMinutesRequested=other._myUtcOffsetMinutesRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isLocalTimeStringRequested():
            self.localTimeString=other.localTimeString
            self._myHasLocalTimeString=other._myHasLocalTimeString
            self._myLocalTimeStringRequested=other._myLocalTimeStringRequested
        
        if self.isUtcTimeStringRequested():
            self.utcTimeString=other.utcTimeString
            self._myHasUtcTimeString=other._myHasUtcTimeString
            self._myUtcTimeStringRequested=other._myUtcTimeStringRequested
        
        if self.isDaylightSavingTimeRequested():
            self.daylightSavingTime=other.daylightSavingTime
            self._myHasDaylightSavingTime=other._myHasDaylightSavingTime
            self._myDaylightSavingTimeRequested=other._myDaylightSavingTimeRequested
        
        if self.isEpochRequested():
            self.epoch=other.epoch
            self._myHasEpoch=other._myHasEpoch
            self._myEpochRequested=other._myEpochRequested
        
        if self.isUtcOffsetMinutesRequested():
            self.utcOffsetMinutes=other.utcOffsetMinutes
            self._myHasUtcOffsetMinutes=other._myHasUtcOffsetMinutes
            self._myUtcOffsetMinutesRequested=other._myUtcOffsetMinutesRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasLocalTimeString():
            self.localTimeString=other.localTimeString
            self._myHasLocalTimeString=other._myHasLocalTimeString
            self._myLocalTimeStringRequested=other._myLocalTimeStringRequested
        
        if other.hasUtcTimeString():
            self.utcTimeString=other.utcTimeString
            self._myHasUtcTimeString=other._myHasUtcTimeString
            self._myUtcTimeStringRequested=other._myUtcTimeStringRequested
        
        if other.hasDaylightSavingTime():
            self.daylightSavingTime=other.daylightSavingTime
            self._myHasDaylightSavingTime=other._myHasDaylightSavingTime
            self._myDaylightSavingTimeRequested=other._myDaylightSavingTimeRequested
        
        if other.hasEpoch():
            self.epoch=other.epoch
            self._myHasEpoch=other._myHasEpoch
            self._myEpochRequested=other._myEpochRequested
        
        if other.hasUtcOffsetMinutes():
            self.utcOffsetMinutes=other.utcOffsetMinutes
            self._myHasUtcOffsetMinutes=other._myHasUtcOffsetMinutes
            self._myUtcOffsetMinutesRequested=other._myUtcOffsetMinutesRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.localTimeString=other.localTimeString
        self._myHasLocalTimeString=other._myHasLocalTimeString
        
        self.utcTimeString=other.utcTimeString
        self._myHasUtcTimeString=other._myHasUtcTimeString
        
        self.daylightSavingTime=other.daylightSavingTime
        self._myHasDaylightSavingTime=other._myHasDaylightSavingTime
        
        self.epoch=other.epoch
        self._myHasEpoch=other._myHasEpoch
        
        self.utcOffsetMinutes=other.utcOffsetMinutes
        self._myHasUtcOffsetMinutes=other._myHasUtcOffsetMinutes
        


    def setAllNumericToZero (self):
        
        self.epoch=0
        self.setHasEpoch()
        self.utcOffsetMinutes=0
        self.setHasUtcOffsetMinutes()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasEpoch():
            if other.hasEpoch():
                self.epoch -= other.epoch
        
        if self.hasUtcOffsetMinutes():
            if other.hasUtcOffsetMinutes():
                self.utcOffsetMinutes -= other.utcOffsetMinutes
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasEpoch():
            if other.hasEpoch():
                self.epoch += other.epoch
        
        if self.hasUtcOffsetMinutes():
            if other.hasUtcOffsetMinutes():
                self.utcOffsetMinutes += other.utcOffsetMinutes
        
        
        pass


    # has...() methods

    def hasLocalTimeString (self):
        return self._myHasLocalTimeString

    def hasUtcTimeString (self):
        return self._myHasUtcTimeString

    def hasDaylightSavingTime (self):
        return self._myHasDaylightSavingTime

    def hasEpoch (self):
        return self._myHasEpoch

    def hasUtcOffsetMinutes (self):
        return self._myHasUtcOffsetMinutes




    # setHas...() methods

    def setHasLocalTimeString (self):
        self._myHasLocalTimeString=True

    def setHasUtcTimeString (self):
        self._myHasUtcTimeString=True

    def setHasDaylightSavingTime (self):
        self._myHasDaylightSavingTime=True

    def setHasEpoch (self):
        self._myHasEpoch=True

    def setHasUtcOffsetMinutes (self):
        self._myHasUtcOffsetMinutes=True




    # isRequested...() methods

    def isLocalTimeStringRequested (self):
        return self._myLocalTimeStringRequested

    def isUtcTimeStringRequested (self):
        return self._myUtcTimeStringRequested

    def isDaylightSavingTimeRequested (self):
        return self._myDaylightSavingTimeRequested

    def isEpochRequested (self):
        return self._myEpochRequested

    def isUtcOffsetMinutesRequested (self):
        return self._myUtcOffsetMinutesRequested




    # setRequested...() methods

    def setLocalTimeStringRequested (self):
        self._myLocalTimeStringRequested=True

    def setUtcTimeStringRequested (self):
        self._myUtcTimeStringRequested=True

    def setDaylightSavingTimeRequested (self):
        self._myDaylightSavingTimeRequested=True

    def setEpochRequested (self):
        self._myEpochRequested=True

    def setUtcOffsetMinutesRequested (self):
        self._myUtcOffsetMinutesRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myLocalTimeStringRequested:
            x = "+LocalTimeString="
            if self._myHasLocalTimeString:
                leafStr = str(self.localTimeString)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myUtcTimeStringRequested:
            x = "+UtcTimeString="
            if self._myHasUtcTimeString:
                leafStr = str(self.utcTimeString)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myDaylightSavingTimeRequested:
            x = "+DaylightSavingTime="
            if self._myHasDaylightSavingTime:
                leafStr = str(self.daylightSavingTime)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myEpochRequested:
            x = "+Epoch="
            if self._myHasEpoch:
                leafStr = str(self.epoch)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myUtcOffsetMinutesRequested:
            x = "+UtcOffsetMinutes="
            if self._myHasUtcOffsetMinutes:
                leafStr = str(self.utcOffsetMinutes)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+LocalTimeString="
        if self._myHasLocalTimeString:
            leafStr = str(self.localTimeString)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myLocalTimeStringRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+UtcTimeString="
        if self._myHasUtcTimeString:
            leafStr = str(self.utcTimeString)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myUtcTimeStringRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+DaylightSavingTime="
        if self._myHasDaylightSavingTime:
            leafStr = str(self.daylightSavingTime)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myDaylightSavingTimeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Epoch="
        if self._myHasEpoch:
            leafStr = str(self.epoch)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myEpochRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+UtcOffsetMinutes="
        if self._myHasUtcOffsetMinutes:
            leafStr = str(self.utcOffsetMinutes)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myUtcOffsetMinutesRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setLocalTimeStringRequested()
        self.setUtcTimeStringRequested()
        self.setDaylightSavingTimeRequested()
        self.setEpochRequested()
        self.setUtcOffsetMinutesRequested()
        
        


    def setLocalTimeString (self, localTimeString):
        self.localTimeString = localTimeString
        self.setHasLocalTimeString()

    def setUtcTimeString (self, utcTimeString):
        self.utcTimeString = utcTimeString
        self.setHasUtcTimeString()

    def setDaylightSavingTime (self, daylightSavingTime):
        self.daylightSavingTime = daylightSavingTime
        self.setHasDaylightSavingTime()

    def setEpoch (self, epoch):
        self.epoch = epoch
        self.setHasEpoch()

    def setUtcOffsetMinutes (self, utcOffsetMinutes):
        self.utcOffsetMinutes = utcOffsetMinutes
        self.setHasUtcOffsetMinutes()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_system_clock.tech.system.clock.status.status_oper_data_gen import StatusOperData"
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
            "namespace": "clock", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "localTimeString", 
            "yangName": "local-time-string", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "utcTimeString", 
            "yangName": "utc-time-string", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: BoolPyHandler", 
            "memberName": "daylightSavingTime", 
            "yangName": "daylight-saving-time", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "epoch", 
            "yangName": "epoch", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "utcOffsetMinutes", 
            "yangName": "utc-offset-minutes", 
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
            "qwilt_tech_system_clock"
        ]
    }, 
    "createTime": "2013"
}
"""


