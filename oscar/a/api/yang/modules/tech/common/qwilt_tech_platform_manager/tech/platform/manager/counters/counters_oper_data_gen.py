


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
        
        self.pollLatencyError = 0
        self._myHasPollLatencyError=False
        self._myPollLatencyErrorRequested=False
        
        self.overallPollDurationWarning = 0
        self._myHasOverallPollDurationWarning=False
        self._myOverallPollDurationWarningRequested=False
        
        self.totalSeconds = 0
        self._myHasTotalSeconds=False
        self._myTotalSecondsRequested=False
        
        self.pollLatencyWarning = 0
        self._myHasPollLatencyWarning=False
        self._myPollLatencyWarningRequested=False
        
        self.polls = 0
        self._myHasPolls=False
        self._myPollsRequested=False
        
        self.missedPolls = 0
        self._myHasMissedPolls=False
        self._myMissedPollsRequested=False
        
        self.singlePollDurationWarning = 0
        self._myHasSinglePollDurationWarning=False
        self._mySinglePollDurationWarningRequested=False
        
        self.singlePollDurationError = 0
        self._myHasSinglePollDurationError=False
        self._mySinglePollDurationErrorRequested=False
        
        self.overallPollDurationError = 0
        self._myHasOverallPollDurationError=False
        self._myOverallPollDurationErrorRequested=False
        


    def copyFrom (self, other):

        self.activeSeconds=other.activeSeconds
        self._myHasActiveSeconds=other._myHasActiveSeconds
        self._myActiveSecondsRequested=other._myActiveSecondsRequested
        
        self.pollLatencyError=other.pollLatencyError
        self._myHasPollLatencyError=other._myHasPollLatencyError
        self._myPollLatencyErrorRequested=other._myPollLatencyErrorRequested
        
        self.overallPollDurationWarning=other.overallPollDurationWarning
        self._myHasOverallPollDurationWarning=other._myHasOverallPollDurationWarning
        self._myOverallPollDurationWarningRequested=other._myOverallPollDurationWarningRequested
        
        self.totalSeconds=other.totalSeconds
        self._myHasTotalSeconds=other._myHasTotalSeconds
        self._myTotalSecondsRequested=other._myTotalSecondsRequested
        
        self.pollLatencyWarning=other.pollLatencyWarning
        self._myHasPollLatencyWarning=other._myHasPollLatencyWarning
        self._myPollLatencyWarningRequested=other._myPollLatencyWarningRequested
        
        self.polls=other.polls
        self._myHasPolls=other._myHasPolls
        self._myPollsRequested=other._myPollsRequested
        
        self.missedPolls=other.missedPolls
        self._myHasMissedPolls=other._myHasMissedPolls
        self._myMissedPollsRequested=other._myMissedPollsRequested
        
        self.singlePollDurationWarning=other.singlePollDurationWarning
        self._myHasSinglePollDurationWarning=other._myHasSinglePollDurationWarning
        self._mySinglePollDurationWarningRequested=other._mySinglePollDurationWarningRequested
        
        self.singlePollDurationError=other.singlePollDurationError
        self._myHasSinglePollDurationError=other._myHasSinglePollDurationError
        self._mySinglePollDurationErrorRequested=other._mySinglePollDurationErrorRequested
        
        self.overallPollDurationError=other.overallPollDurationError
        self._myHasOverallPollDurationError=other._myHasOverallPollDurationError
        self._myOverallPollDurationErrorRequested=other._myOverallPollDurationErrorRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isActiveSecondsRequested():
            self.activeSeconds=other.activeSeconds
            self._myHasActiveSeconds=other._myHasActiveSeconds
            self._myActiveSecondsRequested=other._myActiveSecondsRequested
        
        if self.isPollLatencyErrorRequested():
            self.pollLatencyError=other.pollLatencyError
            self._myHasPollLatencyError=other._myHasPollLatencyError
            self._myPollLatencyErrorRequested=other._myPollLatencyErrorRequested
        
        if self.isOverallPollDurationWarningRequested():
            self.overallPollDurationWarning=other.overallPollDurationWarning
            self._myHasOverallPollDurationWarning=other._myHasOverallPollDurationWarning
            self._myOverallPollDurationWarningRequested=other._myOverallPollDurationWarningRequested
        
        if self.isTotalSecondsRequested():
            self.totalSeconds=other.totalSeconds
            self._myHasTotalSeconds=other._myHasTotalSeconds
            self._myTotalSecondsRequested=other._myTotalSecondsRequested
        
        if self.isPollLatencyWarningRequested():
            self.pollLatencyWarning=other.pollLatencyWarning
            self._myHasPollLatencyWarning=other._myHasPollLatencyWarning
            self._myPollLatencyWarningRequested=other._myPollLatencyWarningRequested
        
        if self.isPollsRequested():
            self.polls=other.polls
            self._myHasPolls=other._myHasPolls
            self._myPollsRequested=other._myPollsRequested
        
        if self.isMissedPollsRequested():
            self.missedPolls=other.missedPolls
            self._myHasMissedPolls=other._myHasMissedPolls
            self._myMissedPollsRequested=other._myMissedPollsRequested
        
        if self.isSinglePollDurationWarningRequested():
            self.singlePollDurationWarning=other.singlePollDurationWarning
            self._myHasSinglePollDurationWarning=other._myHasSinglePollDurationWarning
            self._mySinglePollDurationWarningRequested=other._mySinglePollDurationWarningRequested
        
        if self.isSinglePollDurationErrorRequested():
            self.singlePollDurationError=other.singlePollDurationError
            self._myHasSinglePollDurationError=other._myHasSinglePollDurationError
            self._mySinglePollDurationErrorRequested=other._mySinglePollDurationErrorRequested
        
        if self.isOverallPollDurationErrorRequested():
            self.overallPollDurationError=other.overallPollDurationError
            self._myHasOverallPollDurationError=other._myHasOverallPollDurationError
            self._myOverallPollDurationErrorRequested=other._myOverallPollDurationErrorRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasActiveSeconds():
            self.activeSeconds=other.activeSeconds
            self._myHasActiveSeconds=other._myHasActiveSeconds
            self._myActiveSecondsRequested=other._myActiveSecondsRequested
        
        if other.hasPollLatencyError():
            self.pollLatencyError=other.pollLatencyError
            self._myHasPollLatencyError=other._myHasPollLatencyError
            self._myPollLatencyErrorRequested=other._myPollLatencyErrorRequested
        
        if other.hasOverallPollDurationWarning():
            self.overallPollDurationWarning=other.overallPollDurationWarning
            self._myHasOverallPollDurationWarning=other._myHasOverallPollDurationWarning
            self._myOverallPollDurationWarningRequested=other._myOverallPollDurationWarningRequested
        
        if other.hasTotalSeconds():
            self.totalSeconds=other.totalSeconds
            self._myHasTotalSeconds=other._myHasTotalSeconds
            self._myTotalSecondsRequested=other._myTotalSecondsRequested
        
        if other.hasPollLatencyWarning():
            self.pollLatencyWarning=other.pollLatencyWarning
            self._myHasPollLatencyWarning=other._myHasPollLatencyWarning
            self._myPollLatencyWarningRequested=other._myPollLatencyWarningRequested
        
        if other.hasPolls():
            self.polls=other.polls
            self._myHasPolls=other._myHasPolls
            self._myPollsRequested=other._myPollsRequested
        
        if other.hasMissedPolls():
            self.missedPolls=other.missedPolls
            self._myHasMissedPolls=other._myHasMissedPolls
            self._myMissedPollsRequested=other._myMissedPollsRequested
        
        if other.hasSinglePollDurationWarning():
            self.singlePollDurationWarning=other.singlePollDurationWarning
            self._myHasSinglePollDurationWarning=other._myHasSinglePollDurationWarning
            self._mySinglePollDurationWarningRequested=other._mySinglePollDurationWarningRequested
        
        if other.hasSinglePollDurationError():
            self.singlePollDurationError=other.singlePollDurationError
            self._myHasSinglePollDurationError=other._myHasSinglePollDurationError
            self._mySinglePollDurationErrorRequested=other._mySinglePollDurationErrorRequested
        
        if other.hasOverallPollDurationError():
            self.overallPollDurationError=other.overallPollDurationError
            self._myHasOverallPollDurationError=other._myHasOverallPollDurationError
            self._myOverallPollDurationErrorRequested=other._myOverallPollDurationErrorRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.activeSeconds=other.activeSeconds
        self._myHasActiveSeconds=other._myHasActiveSeconds
        
        self.pollLatencyError=other.pollLatencyError
        self._myHasPollLatencyError=other._myHasPollLatencyError
        
        self.overallPollDurationWarning=other.overallPollDurationWarning
        self._myHasOverallPollDurationWarning=other._myHasOverallPollDurationWarning
        
        self.totalSeconds=other.totalSeconds
        self._myHasTotalSeconds=other._myHasTotalSeconds
        
        self.pollLatencyWarning=other.pollLatencyWarning
        self._myHasPollLatencyWarning=other._myHasPollLatencyWarning
        
        self.polls=other.polls
        self._myHasPolls=other._myHasPolls
        
        self.missedPolls=other.missedPolls
        self._myHasMissedPolls=other._myHasMissedPolls
        
        self.singlePollDurationWarning=other.singlePollDurationWarning
        self._myHasSinglePollDurationWarning=other._myHasSinglePollDurationWarning
        
        self.singlePollDurationError=other.singlePollDurationError
        self._myHasSinglePollDurationError=other._myHasSinglePollDurationError
        
        self.overallPollDurationError=other.overallPollDurationError
        self._myHasOverallPollDurationError=other._myHasOverallPollDurationError
        


    def setAllNumericToZero (self):
        
        self.activeSeconds=0
        self.setHasActiveSeconds()
        self.pollLatencyError=0
        self.setHasPollLatencyError()
        self.overallPollDurationWarning=0
        self.setHasOverallPollDurationWarning()
        self.totalSeconds=0
        self.setHasTotalSeconds()
        self.pollLatencyWarning=0
        self.setHasPollLatencyWarning()
        self.polls=0
        self.setHasPolls()
        self.missedPolls=0
        self.setHasMissedPolls()
        self.singlePollDurationWarning=0
        self.setHasSinglePollDurationWarning()
        self.singlePollDurationError=0
        self.setHasSinglePollDurationError()
        self.overallPollDurationError=0
        self.setHasOverallPollDurationError()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasActiveSeconds():
            if other.hasActiveSeconds():
                self.activeSeconds -= other.activeSeconds
        
        if self.hasPollLatencyError():
            if other.hasPollLatencyError():
                self.pollLatencyError -= other.pollLatencyError
        
        if self.hasOverallPollDurationWarning():
            if other.hasOverallPollDurationWarning():
                self.overallPollDurationWarning -= other.overallPollDurationWarning
        
        if self.hasTotalSeconds():
            if other.hasTotalSeconds():
                self.totalSeconds -= other.totalSeconds
        
        if self.hasPollLatencyWarning():
            if other.hasPollLatencyWarning():
                self.pollLatencyWarning -= other.pollLatencyWarning
        
        if self.hasPolls():
            if other.hasPolls():
                self.polls -= other.polls
        
        if self.hasMissedPolls():
            if other.hasMissedPolls():
                self.missedPolls -= other.missedPolls
        
        if self.hasSinglePollDurationWarning():
            if other.hasSinglePollDurationWarning():
                self.singlePollDurationWarning -= other.singlePollDurationWarning
        
        if self.hasSinglePollDurationError():
            if other.hasSinglePollDurationError():
                self.singlePollDurationError -= other.singlePollDurationError
        
        if self.hasOverallPollDurationError():
            if other.hasOverallPollDurationError():
                self.overallPollDurationError -= other.overallPollDurationError
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasActiveSeconds():
            if other.hasActiveSeconds():
                self.activeSeconds += other.activeSeconds
        
        if self.hasPollLatencyError():
            if other.hasPollLatencyError():
                self.pollLatencyError += other.pollLatencyError
        
        if self.hasOverallPollDurationWarning():
            if other.hasOverallPollDurationWarning():
                self.overallPollDurationWarning += other.overallPollDurationWarning
        
        if self.hasTotalSeconds():
            if other.hasTotalSeconds():
                self.totalSeconds += other.totalSeconds
        
        if self.hasPollLatencyWarning():
            if other.hasPollLatencyWarning():
                self.pollLatencyWarning += other.pollLatencyWarning
        
        if self.hasPolls():
            if other.hasPolls():
                self.polls += other.polls
        
        if self.hasMissedPolls():
            if other.hasMissedPolls():
                self.missedPolls += other.missedPolls
        
        if self.hasSinglePollDurationWarning():
            if other.hasSinglePollDurationWarning():
                self.singlePollDurationWarning += other.singlePollDurationWarning
        
        if self.hasSinglePollDurationError():
            if other.hasSinglePollDurationError():
                self.singlePollDurationError += other.singlePollDurationError
        
        if self.hasOverallPollDurationError():
            if other.hasOverallPollDurationError():
                self.overallPollDurationError += other.overallPollDurationError
        
        
        pass


    # has...() methods

    def hasActiveSeconds (self):
        return self._myHasActiveSeconds

    def hasPollLatencyError (self):
        return self._myHasPollLatencyError

    def hasOverallPollDurationWarning (self):
        return self._myHasOverallPollDurationWarning

    def hasTotalSeconds (self):
        return self._myHasTotalSeconds

    def hasPollLatencyWarning (self):
        return self._myHasPollLatencyWarning

    def hasPolls (self):
        return self._myHasPolls

    def hasMissedPolls (self):
        return self._myHasMissedPolls

    def hasSinglePollDurationWarning (self):
        return self._myHasSinglePollDurationWarning

    def hasSinglePollDurationError (self):
        return self._myHasSinglePollDurationError

    def hasOverallPollDurationError (self):
        return self._myHasOverallPollDurationError




    # setHas...() methods

    def setHasActiveSeconds (self):
        self._myHasActiveSeconds=True

    def setHasPollLatencyError (self):
        self._myHasPollLatencyError=True

    def setHasOverallPollDurationWarning (self):
        self._myHasOverallPollDurationWarning=True

    def setHasTotalSeconds (self):
        self._myHasTotalSeconds=True

    def setHasPollLatencyWarning (self):
        self._myHasPollLatencyWarning=True

    def setHasPolls (self):
        self._myHasPolls=True

    def setHasMissedPolls (self):
        self._myHasMissedPolls=True

    def setHasSinglePollDurationWarning (self):
        self._myHasSinglePollDurationWarning=True

    def setHasSinglePollDurationError (self):
        self._myHasSinglePollDurationError=True

    def setHasOverallPollDurationError (self):
        self._myHasOverallPollDurationError=True




    # isRequested...() methods

    def isActiveSecondsRequested (self):
        return self._myActiveSecondsRequested

    def isPollLatencyErrorRequested (self):
        return self._myPollLatencyErrorRequested

    def isOverallPollDurationWarningRequested (self):
        return self._myOverallPollDurationWarningRequested

    def isTotalSecondsRequested (self):
        return self._myTotalSecondsRequested

    def isPollLatencyWarningRequested (self):
        return self._myPollLatencyWarningRequested

    def isPollsRequested (self):
        return self._myPollsRequested

    def isMissedPollsRequested (self):
        return self._myMissedPollsRequested

    def isSinglePollDurationWarningRequested (self):
        return self._mySinglePollDurationWarningRequested

    def isSinglePollDurationErrorRequested (self):
        return self._mySinglePollDurationErrorRequested

    def isOverallPollDurationErrorRequested (self):
        return self._myOverallPollDurationErrorRequested




    # setRequested...() methods

    def setActiveSecondsRequested (self):
        self._myActiveSecondsRequested=True

    def setPollLatencyErrorRequested (self):
        self._myPollLatencyErrorRequested=True

    def setOverallPollDurationWarningRequested (self):
        self._myOverallPollDurationWarningRequested=True

    def setTotalSecondsRequested (self):
        self._myTotalSecondsRequested=True

    def setPollLatencyWarningRequested (self):
        self._myPollLatencyWarningRequested=True

    def setPollsRequested (self):
        self._myPollsRequested=True

    def setMissedPollsRequested (self):
        self._myMissedPollsRequested=True

    def setSinglePollDurationWarningRequested (self):
        self._mySinglePollDurationWarningRequested=True

    def setSinglePollDurationErrorRequested (self):
        self._mySinglePollDurationErrorRequested=True

    def setOverallPollDurationErrorRequested (self):
        self._myOverallPollDurationErrorRequested=True




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
        if self._myPollLatencyErrorRequested:
            x = "+PollLatencyError="
            if self._myHasPollLatencyError:
                leafStr = str(self.pollLatencyError)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOverallPollDurationWarningRequested:
            x = "+OverallPollDurationWarning="
            if self._myHasOverallPollDurationWarning:
                leafStr = str(self.overallPollDurationWarning)
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
        if self._myPollLatencyWarningRequested:
            x = "+PollLatencyWarning="
            if self._myHasPollLatencyWarning:
                leafStr = str(self.pollLatencyWarning)
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
        if self._myMissedPollsRequested:
            x = "+MissedPolls="
            if self._myHasMissedPolls:
                leafStr = str(self.missedPolls)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySinglePollDurationWarningRequested:
            x = "+SinglePollDurationWarning="
            if self._myHasSinglePollDurationWarning:
                leafStr = str(self.singlePollDurationWarning)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._mySinglePollDurationErrorRequested:
            x = "+SinglePollDurationError="
            if self._myHasSinglePollDurationError:
                leafStr = str(self.singlePollDurationError)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOverallPollDurationErrorRequested:
            x = "+OverallPollDurationError="
            if self._myHasOverallPollDurationError:
                leafStr = str(self.overallPollDurationError)
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
        x = "+PollLatencyError="
        if self._myHasPollLatencyError:
            leafStr = str(self.pollLatencyError)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPollLatencyErrorRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OverallPollDurationWarning="
        if self._myHasOverallPollDurationWarning:
            leafStr = str(self.overallPollDurationWarning)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOverallPollDurationWarningRequested:
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
        x = "+PollLatencyWarning="
        if self._myHasPollLatencyWarning:
            leafStr = str(self.pollLatencyWarning)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPollLatencyWarningRequested:
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
        x = "+MissedPolls="
        if self._myHasMissedPolls:
            leafStr = str(self.missedPolls)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMissedPollsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+SinglePollDurationWarning="
        if self._myHasSinglePollDurationWarning:
            leafStr = str(self.singlePollDurationWarning)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySinglePollDurationWarningRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+SinglePollDurationError="
        if self._myHasSinglePollDurationError:
            leafStr = str(self.singlePollDurationError)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySinglePollDurationErrorRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OverallPollDurationError="
        if self._myHasOverallPollDurationError:
            leafStr = str(self.overallPollDurationError)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOverallPollDurationErrorRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setActiveSecondsRequested()
        self.setPollLatencyErrorRequested()
        self.setOverallPollDurationWarningRequested()
        self.setTotalSecondsRequested()
        self.setPollLatencyWarningRequested()
        self.setPollsRequested()
        self.setMissedPollsRequested()
        self.setSinglePollDurationWarningRequested()
        self.setSinglePollDurationErrorRequested()
        self.setOverallPollDurationErrorRequested()
        
        


    def setActiveSeconds (self, activeSeconds):
        self.activeSeconds = activeSeconds
        self.setHasActiveSeconds()

    def setPollLatencyError (self, pollLatencyError):
        self.pollLatencyError = pollLatencyError
        self.setHasPollLatencyError()

    def setOverallPollDurationWarning (self, overallPollDurationWarning):
        self.overallPollDurationWarning = overallPollDurationWarning
        self.setHasOverallPollDurationWarning()

    def setTotalSeconds (self, totalSeconds):
        self.totalSeconds = totalSeconds
        self.setHasTotalSeconds()

    def setPollLatencyWarning (self, pollLatencyWarning):
        self.pollLatencyWarning = pollLatencyWarning
        self.setHasPollLatencyWarning()

    def setPolls (self, polls):
        self.polls = polls
        self.setHasPolls()

    def setMissedPolls (self, missedPolls):
        self.missedPolls = missedPolls
        self.setHasMissedPolls()

    def setSinglePollDurationWarning (self, singlePollDurationWarning):
        self.singlePollDurationWarning = singlePollDurationWarning
        self.setHasSinglePollDurationWarning()

    def setSinglePollDurationError (self, singlePollDurationError):
        self.singlePollDurationError = singlePollDurationError
        self.setHasSinglePollDurationError()

    def setOverallPollDurationError (self, overallPollDurationError):
        self.overallPollDurationError = overallPollDurationError
        self.setHasOverallPollDurationError()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_platform_manager.tech.platform.manager.counters.counters_oper_data_gen import CountersOperData"
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
            "namespace": "manager", 
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
            "memberName": "pollLatencyError", 
            "yangName": "poll-latency-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationWarning", 
            "yangName": "overall-poll-duration-warning", 
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
            "memberName": "pollLatencyWarning", 
            "yangName": "poll-latency-warning", 
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
            "memberName": "missedPolls", 
            "yangName": "missed-polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationWarning", 
            "yangName": "single-poll-duration-warning", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "singlePollDurationError", 
            "yangName": "single-poll-duration-error", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "overallPollDurationError", 
            "yangName": "overall-poll-duration-error", 
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
            "qwilt_tech_platform_manager"
        ]
    }, 
    "createTime": "2013"
}
"""


