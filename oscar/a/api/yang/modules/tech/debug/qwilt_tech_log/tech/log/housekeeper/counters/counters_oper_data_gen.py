


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





class CountersOperData (object):

    def __init__ (self):

        self.activeSeconds = 0
        self._myHasActiveSeconds=False
        self._myActiveSecondsRequested=False
        
        self.totalSeconds = 0
        self._myHasTotalSeconds=False
        self._myTotalSecondsRequested=False
        
        self.polls = 0
        self._myHasPolls=False
        self._myPollsRequested=False
        
        self.pollsMissed = 0
        self._myHasPollsMissed=False
        self._myPollsMissedRequested=False
        
        self.pollLatencyWarnings = 0
        self._myHasPollLatencyWarnings=False
        self._myPollLatencyWarningsRequested=False
        
        self.pollLatencyErrors = 0
        self._myHasPollLatencyErrors=False
        self._myPollLatencyErrorsRequested=False
        


    def copyFrom (self, other):

        self.activeSeconds=other.activeSeconds
        self._myHasActiveSeconds=other._myHasActiveSeconds
        self._myActiveSecondsRequested=other._myActiveSecondsRequested
        
        self.totalSeconds=other.totalSeconds
        self._myHasTotalSeconds=other._myHasTotalSeconds
        self._myTotalSecondsRequested=other._myTotalSecondsRequested
        
        self.polls=other.polls
        self._myHasPolls=other._myHasPolls
        self._myPollsRequested=other._myPollsRequested
        
        self.pollsMissed=other.pollsMissed
        self._myHasPollsMissed=other._myHasPollsMissed
        self._myPollsMissedRequested=other._myPollsMissedRequested
        
        self.pollLatencyWarnings=other.pollLatencyWarnings
        self._myHasPollLatencyWarnings=other._myHasPollLatencyWarnings
        self._myPollLatencyWarningsRequested=other._myPollLatencyWarningsRequested
        
        self.pollLatencyErrors=other.pollLatencyErrors
        self._myHasPollLatencyErrors=other._myHasPollLatencyErrors
        self._myPollLatencyErrorsRequested=other._myPollLatencyErrorsRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isActiveSecondsRequested():
            self.activeSeconds=other.activeSeconds
            self._myHasActiveSeconds=other._myHasActiveSeconds
            self._myActiveSecondsRequested=other._myActiveSecondsRequested
        
        if self.isTotalSecondsRequested():
            self.totalSeconds=other.totalSeconds
            self._myHasTotalSeconds=other._myHasTotalSeconds
            self._myTotalSecondsRequested=other._myTotalSecondsRequested
        
        if self.isPollsRequested():
            self.polls=other.polls
            self._myHasPolls=other._myHasPolls
            self._myPollsRequested=other._myPollsRequested
        
        if self.isPollsMissedRequested():
            self.pollsMissed=other.pollsMissed
            self._myHasPollsMissed=other._myHasPollsMissed
            self._myPollsMissedRequested=other._myPollsMissedRequested
        
        if self.isPollLatencyWarningsRequested():
            self.pollLatencyWarnings=other.pollLatencyWarnings
            self._myHasPollLatencyWarnings=other._myHasPollLatencyWarnings
            self._myPollLatencyWarningsRequested=other._myPollLatencyWarningsRequested
        
        if self.isPollLatencyErrorsRequested():
            self.pollLatencyErrors=other.pollLatencyErrors
            self._myHasPollLatencyErrors=other._myHasPollLatencyErrors
            self._myPollLatencyErrorsRequested=other._myPollLatencyErrorsRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasActiveSeconds():
            self.activeSeconds=other.activeSeconds
            self._myHasActiveSeconds=other._myHasActiveSeconds
            self._myActiveSecondsRequested=other._myActiveSecondsRequested
        
        if other.hasTotalSeconds():
            self.totalSeconds=other.totalSeconds
            self._myHasTotalSeconds=other._myHasTotalSeconds
            self._myTotalSecondsRequested=other._myTotalSecondsRequested
        
        if other.hasPolls():
            self.polls=other.polls
            self._myHasPolls=other._myHasPolls
            self._myPollsRequested=other._myPollsRequested
        
        if other.hasPollsMissed():
            self.pollsMissed=other.pollsMissed
            self._myHasPollsMissed=other._myHasPollsMissed
            self._myPollsMissedRequested=other._myPollsMissedRequested
        
        if other.hasPollLatencyWarnings():
            self.pollLatencyWarnings=other.pollLatencyWarnings
            self._myHasPollLatencyWarnings=other._myHasPollLatencyWarnings
            self._myPollLatencyWarningsRequested=other._myPollLatencyWarningsRequested
        
        if other.hasPollLatencyErrors():
            self.pollLatencyErrors=other.pollLatencyErrors
            self._myHasPollLatencyErrors=other._myHasPollLatencyErrors
            self._myPollLatencyErrorsRequested=other._myPollLatencyErrorsRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.activeSeconds=other.activeSeconds
        self._myHasActiveSeconds=other._myHasActiveSeconds
        
        self.totalSeconds=other.totalSeconds
        self._myHasTotalSeconds=other._myHasTotalSeconds
        
        self.polls=other.polls
        self._myHasPolls=other._myHasPolls
        
        self.pollsMissed=other.pollsMissed
        self._myHasPollsMissed=other._myHasPollsMissed
        
        self.pollLatencyWarnings=other.pollLatencyWarnings
        self._myHasPollLatencyWarnings=other._myHasPollLatencyWarnings
        
        self.pollLatencyErrors=other.pollLatencyErrors
        self._myHasPollLatencyErrors=other._myHasPollLatencyErrors
        


    def setAllNumericToZero (self):
        
        self.activeSeconds=0
        self.setHasActiveSeconds()
        self.totalSeconds=0
        self.setHasTotalSeconds()
        self.polls=0
        self.setHasPolls()
        self.pollsMissed=0
        self.setHasPollsMissed()
        self.pollLatencyWarnings=0
        self.setHasPollLatencyWarnings()
        self.pollLatencyErrors=0
        self.setHasPollLatencyErrors()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasActiveSeconds():
            if other.hasActiveSeconds():
                self.activeSeconds -= other.activeSeconds
        
        if self.hasTotalSeconds():
            if other.hasTotalSeconds():
                self.totalSeconds -= other.totalSeconds
        
        if self.hasPolls():
            if other.hasPolls():
                self.polls -= other.polls
        
        if self.hasPollsMissed():
            if other.hasPollsMissed():
                self.pollsMissed -= other.pollsMissed
        
        if self.hasPollLatencyWarnings():
            if other.hasPollLatencyWarnings():
                self.pollLatencyWarnings -= other.pollLatencyWarnings
        
        if self.hasPollLatencyErrors():
            if other.hasPollLatencyErrors():
                self.pollLatencyErrors -= other.pollLatencyErrors
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasActiveSeconds():
            if other.hasActiveSeconds():
                self.activeSeconds += other.activeSeconds
        
        if self.hasTotalSeconds():
            if other.hasTotalSeconds():
                self.totalSeconds += other.totalSeconds
        
        if self.hasPolls():
            if other.hasPolls():
                self.polls += other.polls
        
        if self.hasPollsMissed():
            if other.hasPollsMissed():
                self.pollsMissed += other.pollsMissed
        
        if self.hasPollLatencyWarnings():
            if other.hasPollLatencyWarnings():
                self.pollLatencyWarnings += other.pollLatencyWarnings
        
        if self.hasPollLatencyErrors():
            if other.hasPollLatencyErrors():
                self.pollLatencyErrors += other.pollLatencyErrors
        
        
        pass


    # has...() methods

    def hasActiveSeconds (self):
        return self._myHasActiveSeconds

    def hasTotalSeconds (self):
        return self._myHasTotalSeconds

    def hasPolls (self):
        return self._myHasPolls

    def hasPollsMissed (self):
        return self._myHasPollsMissed

    def hasPollLatencyWarnings (self):
        return self._myHasPollLatencyWarnings

    def hasPollLatencyErrors (self):
        return self._myHasPollLatencyErrors




    # setHas...() methods

    def setHasActiveSeconds (self):
        self._myHasActiveSeconds=True

    def setHasTotalSeconds (self):
        self._myHasTotalSeconds=True

    def setHasPolls (self):
        self._myHasPolls=True

    def setHasPollsMissed (self):
        self._myHasPollsMissed=True

    def setHasPollLatencyWarnings (self):
        self._myHasPollLatencyWarnings=True

    def setHasPollLatencyErrors (self):
        self._myHasPollLatencyErrors=True




    # isRequested...() methods

    def isActiveSecondsRequested (self):
        return self._myActiveSecondsRequested

    def isTotalSecondsRequested (self):
        return self._myTotalSecondsRequested

    def isPollsRequested (self):
        return self._myPollsRequested

    def isPollsMissedRequested (self):
        return self._myPollsMissedRequested

    def isPollLatencyWarningsRequested (self):
        return self._myPollLatencyWarningsRequested

    def isPollLatencyErrorsRequested (self):
        return self._myPollLatencyErrorsRequested




    # setRequested...() methods

    def setActiveSecondsRequested (self):
        self._myActiveSecondsRequested=True

    def setTotalSecondsRequested (self):
        self._myTotalSecondsRequested=True

    def setPollsRequested (self):
        self._myPollsRequested=True

    def setPollsMissedRequested (self):
        self._myPollsMissedRequested=True

    def setPollLatencyWarningsRequested (self):
        self._myPollLatencyWarningsRequested=True

    def setPollLatencyErrorsRequested (self):
        self._myPollLatencyErrorsRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myActiveSecondsRequested:
            x = "+ActiveSeconds="
            if self._myHasActiveSeconds:
                leafStr = str(self.activeSeconds)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTotalSecondsRequested:
            x = "+TotalSeconds="
            if self._myHasTotalSeconds:
                leafStr = str(self.totalSeconds)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPollsRequested:
            x = "+Polls="
            if self._myHasPolls:
                leafStr = str(self.polls)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPollsMissedRequested:
            x = "+PollsMissed="
            if self._myHasPollsMissed:
                leafStr = str(self.pollsMissed)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPollLatencyWarningsRequested:
            x = "+PollLatencyWarnings="
            if self._myHasPollLatencyWarnings:
                leafStr = str(self.pollLatencyWarnings)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPollLatencyErrorsRequested:
            x = "+PollLatencyErrors="
            if self._myHasPollLatencyErrors:
                leafStr = str(self.pollLatencyErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{CountersOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ActiveSeconds="
        if self._myHasActiveSeconds:
            leafStr = str(self.activeSeconds)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myActiveSecondsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+TotalSeconds="
        if self._myHasTotalSeconds:
            leafStr = str(self.totalSeconds)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTotalSecondsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Polls="
        if self._myHasPolls:
            leafStr = str(self.polls)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPollsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PollsMissed="
        if self._myHasPollsMissed:
            leafStr = str(self.pollsMissed)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPollsMissedRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PollLatencyWarnings="
        if self._myHasPollLatencyWarnings:
            leafStr = str(self.pollLatencyWarnings)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPollLatencyWarningsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PollLatencyErrors="
        if self._myHasPollLatencyErrors:
            leafStr = str(self.pollLatencyErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPollLatencyErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setActiveSecondsRequested()
        self.setTotalSecondsRequested()
        self.setPollsRequested()
        self.setPollsMissedRequested()
        self.setPollLatencyWarningsRequested()
        self.setPollLatencyErrorsRequested()
        
        


    def setActiveSeconds (self, activeSeconds):
        self.activeSeconds = activeSeconds
        self.setHasActiveSeconds()

    def setTotalSeconds (self, totalSeconds):
        self.totalSeconds = totalSeconds
        self.setHasTotalSeconds()

    def setPolls (self, polls):
        self.polls = polls
        self.setHasPolls()

    def setPollsMissed (self, pollsMissed):
        self.pollsMissed = pollsMissed
        self.setHasPollsMissed()

    def setPollLatencyWarnings (self, pollLatencyWarnings):
        self.pollLatencyWarnings = pollLatencyWarnings
        self.setHasPollLatencyWarnings()

    def setPollLatencyErrors (self, pollLatencyErrors):
        self.pollLatencyErrors = pollLatencyErrors
        self.setHasPollLatencyErrors()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.debug.qwilt_tech_log.tech.log.housekeeper.counters.counters_oper_data_gen import CountersOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "log", 
            "isCurrent": false
        }, 
        {
            "namespace": "housekeeper", 
            "isCurrent": false
        }, 
        {
            "namespace": "counters", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "activeSeconds", 
            "yangName": "active-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "totalSeconds", 
            "yangName": "total-seconds", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "polls", 
            "yangName": "polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollsMissed", 
            "yangName": "polls-missed", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyWarnings", 
            "yangName": "poll-latency-warnings", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pollLatencyErrors", 
            "yangName": "poll-latency-errors", 
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
            "debug", 
            "qwilt_tech_log"
        ]
    }, 
    "createTime": "2013"
}
"""


