


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

        self.applicationEntryDiscards = 0
        self._myHasApplicationEntryDiscards=False
        self._myApplicationEntryDiscardsRequested=False
        
        self.neighborDiscoveryFailures = 0
        self._myHasNeighborDiscoveryFailures=False
        self._myNeighborDiscoveryFailuresRequested=False
        
        self.neighborDiscoveryTimeouts = 0
        self._myHasNeighborDiscoveryTimeouts=False
        self._myNeighborDiscoveryTimeoutsRequested=False
        
        self.neighborDiscoverySuccesses = 0
        self._myHasNeighborDiscoverySuccesses=False
        self._myNeighborDiscoverySuccessesRequested=False
        
        self.polls = 0
        self._myHasPolls=False
        self._myPollsRequested=False
        
        self.applicationRequestFailures = 0
        self._myHasApplicationRequestFailures=False
        self._myApplicationRequestFailuresRequested=False
        
        self.applicationEntryUpdates = 0
        self._myHasApplicationEntryUpdates=False
        self._myApplicationEntryUpdatesRequested=False
        
        self.osTableLoadFailures = 0
        self._myHasOsTableLoadFailures=False
        self._myOsTableLoadFailuresRequested=False
        
        self.applicationRequestDiscards = 0
        self._myHasApplicationRequestDiscards=False
        self._myApplicationRequestDiscardsRequested=False
        
        self.applicationRequestBlocks = 0
        self._myHasApplicationRequestBlocks=False
        self._myApplicationRequestBlocksRequested=False
        
        self.applicationRequests = 0
        self._myHasApplicationRequests=False
        self._myApplicationRequestsRequested=False
        
        self.osTableLoads = 0
        self._myHasOsTableLoads=False
        self._myOsTableLoadsRequested=False
        
        self.neighborDiscoveryRequestsSent = 0
        self._myHasNeighborDiscoveryRequestsSent=False
        self._myNeighborDiscoveryRequestsSentRequested=False
        
        self.applicationEntryFailures = 0
        self._myHasApplicationEntryFailures=False
        self._myApplicationEntryFailuresRequested=False
        


    def copyFrom (self, other):

        self.applicationEntryDiscards=other.applicationEntryDiscards
        self._myHasApplicationEntryDiscards=other._myHasApplicationEntryDiscards
        self._myApplicationEntryDiscardsRequested=other._myApplicationEntryDiscardsRequested
        
        self.neighborDiscoveryFailures=other.neighborDiscoveryFailures
        self._myHasNeighborDiscoveryFailures=other._myHasNeighborDiscoveryFailures
        self._myNeighborDiscoveryFailuresRequested=other._myNeighborDiscoveryFailuresRequested
        
        self.neighborDiscoveryTimeouts=other.neighborDiscoveryTimeouts
        self._myHasNeighborDiscoveryTimeouts=other._myHasNeighborDiscoveryTimeouts
        self._myNeighborDiscoveryTimeoutsRequested=other._myNeighborDiscoveryTimeoutsRequested
        
        self.neighborDiscoverySuccesses=other.neighborDiscoverySuccesses
        self._myHasNeighborDiscoverySuccesses=other._myHasNeighborDiscoverySuccesses
        self._myNeighborDiscoverySuccessesRequested=other._myNeighborDiscoverySuccessesRequested
        
        self.polls=other.polls
        self._myHasPolls=other._myHasPolls
        self._myPollsRequested=other._myPollsRequested
        
        self.applicationRequestFailures=other.applicationRequestFailures
        self._myHasApplicationRequestFailures=other._myHasApplicationRequestFailures
        self._myApplicationRequestFailuresRequested=other._myApplicationRequestFailuresRequested
        
        self.applicationEntryUpdates=other.applicationEntryUpdates
        self._myHasApplicationEntryUpdates=other._myHasApplicationEntryUpdates
        self._myApplicationEntryUpdatesRequested=other._myApplicationEntryUpdatesRequested
        
        self.osTableLoadFailures=other.osTableLoadFailures
        self._myHasOsTableLoadFailures=other._myHasOsTableLoadFailures
        self._myOsTableLoadFailuresRequested=other._myOsTableLoadFailuresRequested
        
        self.applicationRequestDiscards=other.applicationRequestDiscards
        self._myHasApplicationRequestDiscards=other._myHasApplicationRequestDiscards
        self._myApplicationRequestDiscardsRequested=other._myApplicationRequestDiscardsRequested
        
        self.applicationRequestBlocks=other.applicationRequestBlocks
        self._myHasApplicationRequestBlocks=other._myHasApplicationRequestBlocks
        self._myApplicationRequestBlocksRequested=other._myApplicationRequestBlocksRequested
        
        self.applicationRequests=other.applicationRequests
        self._myHasApplicationRequests=other._myHasApplicationRequests
        self._myApplicationRequestsRequested=other._myApplicationRequestsRequested
        
        self.osTableLoads=other.osTableLoads
        self._myHasOsTableLoads=other._myHasOsTableLoads
        self._myOsTableLoadsRequested=other._myOsTableLoadsRequested
        
        self.neighborDiscoveryRequestsSent=other.neighborDiscoveryRequestsSent
        self._myHasNeighborDiscoveryRequestsSent=other._myHasNeighborDiscoveryRequestsSent
        self._myNeighborDiscoveryRequestsSentRequested=other._myNeighborDiscoveryRequestsSentRequested
        
        self.applicationEntryFailures=other.applicationEntryFailures
        self._myHasApplicationEntryFailures=other._myHasApplicationEntryFailures
        self._myApplicationEntryFailuresRequested=other._myApplicationEntryFailuresRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isApplicationEntryDiscardsRequested():
            self.applicationEntryDiscards=other.applicationEntryDiscards
            self._myHasApplicationEntryDiscards=other._myHasApplicationEntryDiscards
            self._myApplicationEntryDiscardsRequested=other._myApplicationEntryDiscardsRequested
        
        if self.isNeighborDiscoveryFailuresRequested():
            self.neighborDiscoveryFailures=other.neighborDiscoveryFailures
            self._myHasNeighborDiscoveryFailures=other._myHasNeighborDiscoveryFailures
            self._myNeighborDiscoveryFailuresRequested=other._myNeighborDiscoveryFailuresRequested
        
        if self.isNeighborDiscoveryTimeoutsRequested():
            self.neighborDiscoveryTimeouts=other.neighborDiscoveryTimeouts
            self._myHasNeighborDiscoveryTimeouts=other._myHasNeighborDiscoveryTimeouts
            self._myNeighborDiscoveryTimeoutsRequested=other._myNeighborDiscoveryTimeoutsRequested
        
        if self.isNeighborDiscoverySuccessesRequested():
            self.neighborDiscoverySuccesses=other.neighborDiscoverySuccesses
            self._myHasNeighborDiscoverySuccesses=other._myHasNeighborDiscoverySuccesses
            self._myNeighborDiscoverySuccessesRequested=other._myNeighborDiscoverySuccessesRequested
        
        if self.isPollsRequested():
            self.polls=other.polls
            self._myHasPolls=other._myHasPolls
            self._myPollsRequested=other._myPollsRequested
        
        if self.isApplicationRequestFailuresRequested():
            self.applicationRequestFailures=other.applicationRequestFailures
            self._myHasApplicationRequestFailures=other._myHasApplicationRequestFailures
            self._myApplicationRequestFailuresRequested=other._myApplicationRequestFailuresRequested
        
        if self.isApplicationEntryUpdatesRequested():
            self.applicationEntryUpdates=other.applicationEntryUpdates
            self._myHasApplicationEntryUpdates=other._myHasApplicationEntryUpdates
            self._myApplicationEntryUpdatesRequested=other._myApplicationEntryUpdatesRequested
        
        if self.isOsTableLoadFailuresRequested():
            self.osTableLoadFailures=other.osTableLoadFailures
            self._myHasOsTableLoadFailures=other._myHasOsTableLoadFailures
            self._myOsTableLoadFailuresRequested=other._myOsTableLoadFailuresRequested
        
        if self.isApplicationRequestDiscardsRequested():
            self.applicationRequestDiscards=other.applicationRequestDiscards
            self._myHasApplicationRequestDiscards=other._myHasApplicationRequestDiscards
            self._myApplicationRequestDiscardsRequested=other._myApplicationRequestDiscardsRequested
        
        if self.isApplicationRequestBlocksRequested():
            self.applicationRequestBlocks=other.applicationRequestBlocks
            self._myHasApplicationRequestBlocks=other._myHasApplicationRequestBlocks
            self._myApplicationRequestBlocksRequested=other._myApplicationRequestBlocksRequested
        
        if self.isApplicationRequestsRequested():
            self.applicationRequests=other.applicationRequests
            self._myHasApplicationRequests=other._myHasApplicationRequests
            self._myApplicationRequestsRequested=other._myApplicationRequestsRequested
        
        if self.isOsTableLoadsRequested():
            self.osTableLoads=other.osTableLoads
            self._myHasOsTableLoads=other._myHasOsTableLoads
            self._myOsTableLoadsRequested=other._myOsTableLoadsRequested
        
        if self.isNeighborDiscoveryRequestsSentRequested():
            self.neighborDiscoveryRequestsSent=other.neighborDiscoveryRequestsSent
            self._myHasNeighborDiscoveryRequestsSent=other._myHasNeighborDiscoveryRequestsSent
            self._myNeighborDiscoveryRequestsSentRequested=other._myNeighborDiscoveryRequestsSentRequested
        
        if self.isApplicationEntryFailuresRequested():
            self.applicationEntryFailures=other.applicationEntryFailures
            self._myHasApplicationEntryFailures=other._myHasApplicationEntryFailures
            self._myApplicationEntryFailuresRequested=other._myApplicationEntryFailuresRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasApplicationEntryDiscards():
            self.applicationEntryDiscards=other.applicationEntryDiscards
            self._myHasApplicationEntryDiscards=other._myHasApplicationEntryDiscards
            self._myApplicationEntryDiscardsRequested=other._myApplicationEntryDiscardsRequested
        
        if other.hasNeighborDiscoveryFailures():
            self.neighborDiscoveryFailures=other.neighborDiscoveryFailures
            self._myHasNeighborDiscoveryFailures=other._myHasNeighborDiscoveryFailures
            self._myNeighborDiscoveryFailuresRequested=other._myNeighborDiscoveryFailuresRequested
        
        if other.hasNeighborDiscoveryTimeouts():
            self.neighborDiscoveryTimeouts=other.neighborDiscoveryTimeouts
            self._myHasNeighborDiscoveryTimeouts=other._myHasNeighborDiscoveryTimeouts
            self._myNeighborDiscoveryTimeoutsRequested=other._myNeighborDiscoveryTimeoutsRequested
        
        if other.hasNeighborDiscoverySuccesses():
            self.neighborDiscoverySuccesses=other.neighborDiscoverySuccesses
            self._myHasNeighborDiscoverySuccesses=other._myHasNeighborDiscoverySuccesses
            self._myNeighborDiscoverySuccessesRequested=other._myNeighborDiscoverySuccessesRequested
        
        if other.hasPolls():
            self.polls=other.polls
            self._myHasPolls=other._myHasPolls
            self._myPollsRequested=other._myPollsRequested
        
        if other.hasApplicationRequestFailures():
            self.applicationRequestFailures=other.applicationRequestFailures
            self._myHasApplicationRequestFailures=other._myHasApplicationRequestFailures
            self._myApplicationRequestFailuresRequested=other._myApplicationRequestFailuresRequested
        
        if other.hasApplicationEntryUpdates():
            self.applicationEntryUpdates=other.applicationEntryUpdates
            self._myHasApplicationEntryUpdates=other._myHasApplicationEntryUpdates
            self._myApplicationEntryUpdatesRequested=other._myApplicationEntryUpdatesRequested
        
        if other.hasOsTableLoadFailures():
            self.osTableLoadFailures=other.osTableLoadFailures
            self._myHasOsTableLoadFailures=other._myHasOsTableLoadFailures
            self._myOsTableLoadFailuresRequested=other._myOsTableLoadFailuresRequested
        
        if other.hasApplicationRequestDiscards():
            self.applicationRequestDiscards=other.applicationRequestDiscards
            self._myHasApplicationRequestDiscards=other._myHasApplicationRequestDiscards
            self._myApplicationRequestDiscardsRequested=other._myApplicationRequestDiscardsRequested
        
        if other.hasApplicationRequestBlocks():
            self.applicationRequestBlocks=other.applicationRequestBlocks
            self._myHasApplicationRequestBlocks=other._myHasApplicationRequestBlocks
            self._myApplicationRequestBlocksRequested=other._myApplicationRequestBlocksRequested
        
        if other.hasApplicationRequests():
            self.applicationRequests=other.applicationRequests
            self._myHasApplicationRequests=other._myHasApplicationRequests
            self._myApplicationRequestsRequested=other._myApplicationRequestsRequested
        
        if other.hasOsTableLoads():
            self.osTableLoads=other.osTableLoads
            self._myHasOsTableLoads=other._myHasOsTableLoads
            self._myOsTableLoadsRequested=other._myOsTableLoadsRequested
        
        if other.hasNeighborDiscoveryRequestsSent():
            self.neighborDiscoveryRequestsSent=other.neighborDiscoveryRequestsSent
            self._myHasNeighborDiscoveryRequestsSent=other._myHasNeighborDiscoveryRequestsSent
            self._myNeighborDiscoveryRequestsSentRequested=other._myNeighborDiscoveryRequestsSentRequested
        
        if other.hasApplicationEntryFailures():
            self.applicationEntryFailures=other.applicationEntryFailures
            self._myHasApplicationEntryFailures=other._myHasApplicationEntryFailures
            self._myApplicationEntryFailuresRequested=other._myApplicationEntryFailuresRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.applicationEntryDiscards=other.applicationEntryDiscards
        self._myHasApplicationEntryDiscards=other._myHasApplicationEntryDiscards
        
        self.neighborDiscoveryFailures=other.neighborDiscoveryFailures
        self._myHasNeighborDiscoveryFailures=other._myHasNeighborDiscoveryFailures
        
        self.neighborDiscoveryTimeouts=other.neighborDiscoveryTimeouts
        self._myHasNeighborDiscoveryTimeouts=other._myHasNeighborDiscoveryTimeouts
        
        self.neighborDiscoverySuccesses=other.neighborDiscoverySuccesses
        self._myHasNeighborDiscoverySuccesses=other._myHasNeighborDiscoverySuccesses
        
        self.polls=other.polls
        self._myHasPolls=other._myHasPolls
        
        self.applicationRequestFailures=other.applicationRequestFailures
        self._myHasApplicationRequestFailures=other._myHasApplicationRequestFailures
        
        self.applicationEntryUpdates=other.applicationEntryUpdates
        self._myHasApplicationEntryUpdates=other._myHasApplicationEntryUpdates
        
        self.osTableLoadFailures=other.osTableLoadFailures
        self._myHasOsTableLoadFailures=other._myHasOsTableLoadFailures
        
        self.applicationRequestDiscards=other.applicationRequestDiscards
        self._myHasApplicationRequestDiscards=other._myHasApplicationRequestDiscards
        
        self.applicationRequestBlocks=other.applicationRequestBlocks
        self._myHasApplicationRequestBlocks=other._myHasApplicationRequestBlocks
        
        self.applicationRequests=other.applicationRequests
        self._myHasApplicationRequests=other._myHasApplicationRequests
        
        self.osTableLoads=other.osTableLoads
        self._myHasOsTableLoads=other._myHasOsTableLoads
        
        self.neighborDiscoveryRequestsSent=other.neighborDiscoveryRequestsSent
        self._myHasNeighborDiscoveryRequestsSent=other._myHasNeighborDiscoveryRequestsSent
        
        self.applicationEntryFailures=other.applicationEntryFailures
        self._myHasApplicationEntryFailures=other._myHasApplicationEntryFailures
        


    def setAllNumericToZero (self):
        
        self.applicationEntryDiscards=0
        self.setHasApplicationEntryDiscards()
        self.neighborDiscoveryFailures=0
        self.setHasNeighborDiscoveryFailures()
        self.neighborDiscoveryTimeouts=0
        self.setHasNeighborDiscoveryTimeouts()
        self.neighborDiscoverySuccesses=0
        self.setHasNeighborDiscoverySuccesses()
        self.polls=0
        self.setHasPolls()
        self.applicationRequestFailures=0
        self.setHasApplicationRequestFailures()
        self.applicationEntryUpdates=0
        self.setHasApplicationEntryUpdates()
        self.osTableLoadFailures=0
        self.setHasOsTableLoadFailures()
        self.applicationRequestDiscards=0
        self.setHasApplicationRequestDiscards()
        self.applicationRequestBlocks=0
        self.setHasApplicationRequestBlocks()
        self.applicationRequests=0
        self.setHasApplicationRequests()
        self.osTableLoads=0
        self.setHasOsTableLoads()
        self.neighborDiscoveryRequestsSent=0
        self.setHasNeighborDiscoveryRequestsSent()
        self.applicationEntryFailures=0
        self.setHasApplicationEntryFailures()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasApplicationEntryDiscards():
            if other.hasApplicationEntryDiscards():
                self.applicationEntryDiscards -= other.applicationEntryDiscards
        
        if self.hasNeighborDiscoveryFailures():
            if other.hasNeighborDiscoveryFailures():
                self.neighborDiscoveryFailures -= other.neighborDiscoveryFailures
        
        if self.hasNeighborDiscoveryTimeouts():
            if other.hasNeighborDiscoveryTimeouts():
                self.neighborDiscoveryTimeouts -= other.neighborDiscoveryTimeouts
        
        if self.hasNeighborDiscoverySuccesses():
            if other.hasNeighborDiscoverySuccesses():
                self.neighborDiscoverySuccesses -= other.neighborDiscoverySuccesses
        
        if self.hasPolls():
            if other.hasPolls():
                self.polls -= other.polls
        
        if self.hasApplicationRequestFailures():
            if other.hasApplicationRequestFailures():
                self.applicationRequestFailures -= other.applicationRequestFailures
        
        if self.hasApplicationEntryUpdates():
            if other.hasApplicationEntryUpdates():
                self.applicationEntryUpdates -= other.applicationEntryUpdates
        
        if self.hasOsTableLoadFailures():
            if other.hasOsTableLoadFailures():
                self.osTableLoadFailures -= other.osTableLoadFailures
        
        if self.hasApplicationRequestDiscards():
            if other.hasApplicationRequestDiscards():
                self.applicationRequestDiscards -= other.applicationRequestDiscards
        
        if self.hasApplicationRequestBlocks():
            if other.hasApplicationRequestBlocks():
                self.applicationRequestBlocks -= other.applicationRequestBlocks
        
        if self.hasApplicationRequests():
            if other.hasApplicationRequests():
                self.applicationRequests -= other.applicationRequests
        
        if self.hasOsTableLoads():
            if other.hasOsTableLoads():
                self.osTableLoads -= other.osTableLoads
        
        if self.hasNeighborDiscoveryRequestsSent():
            if other.hasNeighborDiscoveryRequestsSent():
                self.neighborDiscoveryRequestsSent -= other.neighborDiscoveryRequestsSent
        
        if self.hasApplicationEntryFailures():
            if other.hasApplicationEntryFailures():
                self.applicationEntryFailures -= other.applicationEntryFailures
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasApplicationEntryDiscards():
            if other.hasApplicationEntryDiscards():
                self.applicationEntryDiscards += other.applicationEntryDiscards
        
        if self.hasNeighborDiscoveryFailures():
            if other.hasNeighborDiscoveryFailures():
                self.neighborDiscoveryFailures += other.neighborDiscoveryFailures
        
        if self.hasNeighborDiscoveryTimeouts():
            if other.hasNeighborDiscoveryTimeouts():
                self.neighborDiscoveryTimeouts += other.neighborDiscoveryTimeouts
        
        if self.hasNeighborDiscoverySuccesses():
            if other.hasNeighborDiscoverySuccesses():
                self.neighborDiscoverySuccesses += other.neighborDiscoverySuccesses
        
        if self.hasPolls():
            if other.hasPolls():
                self.polls += other.polls
        
        if self.hasApplicationRequestFailures():
            if other.hasApplicationRequestFailures():
                self.applicationRequestFailures += other.applicationRequestFailures
        
        if self.hasApplicationEntryUpdates():
            if other.hasApplicationEntryUpdates():
                self.applicationEntryUpdates += other.applicationEntryUpdates
        
        if self.hasOsTableLoadFailures():
            if other.hasOsTableLoadFailures():
                self.osTableLoadFailures += other.osTableLoadFailures
        
        if self.hasApplicationRequestDiscards():
            if other.hasApplicationRequestDiscards():
                self.applicationRequestDiscards += other.applicationRequestDiscards
        
        if self.hasApplicationRequestBlocks():
            if other.hasApplicationRequestBlocks():
                self.applicationRequestBlocks += other.applicationRequestBlocks
        
        if self.hasApplicationRequests():
            if other.hasApplicationRequests():
                self.applicationRequests += other.applicationRequests
        
        if self.hasOsTableLoads():
            if other.hasOsTableLoads():
                self.osTableLoads += other.osTableLoads
        
        if self.hasNeighborDiscoveryRequestsSent():
            if other.hasNeighborDiscoveryRequestsSent():
                self.neighborDiscoveryRequestsSent += other.neighborDiscoveryRequestsSent
        
        if self.hasApplicationEntryFailures():
            if other.hasApplicationEntryFailures():
                self.applicationEntryFailures += other.applicationEntryFailures
        
        
        pass


    # has...() methods

    def hasApplicationEntryDiscards (self):
        return self._myHasApplicationEntryDiscards

    def hasNeighborDiscoveryFailures (self):
        return self._myHasNeighborDiscoveryFailures

    def hasNeighborDiscoveryTimeouts (self):
        return self._myHasNeighborDiscoveryTimeouts

    def hasNeighborDiscoverySuccesses (self):
        return self._myHasNeighborDiscoverySuccesses

    def hasPolls (self):
        return self._myHasPolls

    def hasApplicationRequestFailures (self):
        return self._myHasApplicationRequestFailures

    def hasApplicationEntryUpdates (self):
        return self._myHasApplicationEntryUpdates

    def hasOsTableLoadFailures (self):
        return self._myHasOsTableLoadFailures

    def hasApplicationRequestDiscards (self):
        return self._myHasApplicationRequestDiscards

    def hasApplicationRequestBlocks (self):
        return self._myHasApplicationRequestBlocks

    def hasApplicationRequests (self):
        return self._myHasApplicationRequests

    def hasOsTableLoads (self):
        return self._myHasOsTableLoads

    def hasNeighborDiscoveryRequestsSent (self):
        return self._myHasNeighborDiscoveryRequestsSent

    def hasApplicationEntryFailures (self):
        return self._myHasApplicationEntryFailures




    # setHas...() methods

    def setHasApplicationEntryDiscards (self):
        self._myHasApplicationEntryDiscards=True

    def setHasNeighborDiscoveryFailures (self):
        self._myHasNeighborDiscoveryFailures=True

    def setHasNeighborDiscoveryTimeouts (self):
        self._myHasNeighborDiscoveryTimeouts=True

    def setHasNeighborDiscoverySuccesses (self):
        self._myHasNeighborDiscoverySuccesses=True

    def setHasPolls (self):
        self._myHasPolls=True

    def setHasApplicationRequestFailures (self):
        self._myHasApplicationRequestFailures=True

    def setHasApplicationEntryUpdates (self):
        self._myHasApplicationEntryUpdates=True

    def setHasOsTableLoadFailures (self):
        self._myHasOsTableLoadFailures=True

    def setHasApplicationRequestDiscards (self):
        self._myHasApplicationRequestDiscards=True

    def setHasApplicationRequestBlocks (self):
        self._myHasApplicationRequestBlocks=True

    def setHasApplicationRequests (self):
        self._myHasApplicationRequests=True

    def setHasOsTableLoads (self):
        self._myHasOsTableLoads=True

    def setHasNeighborDiscoveryRequestsSent (self):
        self._myHasNeighborDiscoveryRequestsSent=True

    def setHasApplicationEntryFailures (self):
        self._myHasApplicationEntryFailures=True




    # isRequested...() methods

    def isApplicationEntryDiscardsRequested (self):
        return self._myApplicationEntryDiscardsRequested

    def isNeighborDiscoveryFailuresRequested (self):
        return self._myNeighborDiscoveryFailuresRequested

    def isNeighborDiscoveryTimeoutsRequested (self):
        return self._myNeighborDiscoveryTimeoutsRequested

    def isNeighborDiscoverySuccessesRequested (self):
        return self._myNeighborDiscoverySuccessesRequested

    def isPollsRequested (self):
        return self._myPollsRequested

    def isApplicationRequestFailuresRequested (self):
        return self._myApplicationRequestFailuresRequested

    def isApplicationEntryUpdatesRequested (self):
        return self._myApplicationEntryUpdatesRequested

    def isOsTableLoadFailuresRequested (self):
        return self._myOsTableLoadFailuresRequested

    def isApplicationRequestDiscardsRequested (self):
        return self._myApplicationRequestDiscardsRequested

    def isApplicationRequestBlocksRequested (self):
        return self._myApplicationRequestBlocksRequested

    def isApplicationRequestsRequested (self):
        return self._myApplicationRequestsRequested

    def isOsTableLoadsRequested (self):
        return self._myOsTableLoadsRequested

    def isNeighborDiscoveryRequestsSentRequested (self):
        return self._myNeighborDiscoveryRequestsSentRequested

    def isApplicationEntryFailuresRequested (self):
        return self._myApplicationEntryFailuresRequested




    # setRequested...() methods

    def setApplicationEntryDiscardsRequested (self):
        self._myApplicationEntryDiscardsRequested=True

    def setNeighborDiscoveryFailuresRequested (self):
        self._myNeighborDiscoveryFailuresRequested=True

    def setNeighborDiscoveryTimeoutsRequested (self):
        self._myNeighborDiscoveryTimeoutsRequested=True

    def setNeighborDiscoverySuccessesRequested (self):
        self._myNeighborDiscoverySuccessesRequested=True

    def setPollsRequested (self):
        self._myPollsRequested=True

    def setApplicationRequestFailuresRequested (self):
        self._myApplicationRequestFailuresRequested=True

    def setApplicationEntryUpdatesRequested (self):
        self._myApplicationEntryUpdatesRequested=True

    def setOsTableLoadFailuresRequested (self):
        self._myOsTableLoadFailuresRequested=True

    def setApplicationRequestDiscardsRequested (self):
        self._myApplicationRequestDiscardsRequested=True

    def setApplicationRequestBlocksRequested (self):
        self._myApplicationRequestBlocksRequested=True

    def setApplicationRequestsRequested (self):
        self._myApplicationRequestsRequested=True

    def setOsTableLoadsRequested (self):
        self._myOsTableLoadsRequested=True

    def setNeighborDiscoveryRequestsSentRequested (self):
        self._myNeighborDiscoveryRequestsSentRequested=True

    def setApplicationEntryFailuresRequested (self):
        self._myApplicationEntryFailuresRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myApplicationEntryDiscardsRequested:
            x = "+ApplicationEntryDiscards="
            if self._myHasApplicationEntryDiscards:
                leafStr = str(self.applicationEntryDiscards)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNeighborDiscoveryFailuresRequested:
            x = "+NeighborDiscoveryFailures="
            if self._myHasNeighborDiscoveryFailures:
                leafStr = str(self.neighborDiscoveryFailures)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNeighborDiscoveryTimeoutsRequested:
            x = "+NeighborDiscoveryTimeouts="
            if self._myHasNeighborDiscoveryTimeouts:
                leafStr = str(self.neighborDiscoveryTimeouts)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNeighborDiscoverySuccessesRequested:
            x = "+NeighborDiscoverySuccesses="
            if self._myHasNeighborDiscoverySuccesses:
                leafStr = str(self.neighborDiscoverySuccesses)
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
        if self._myApplicationRequestFailuresRequested:
            x = "+ApplicationRequestFailures="
            if self._myHasApplicationRequestFailures:
                leafStr = str(self.applicationRequestFailures)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myApplicationEntryUpdatesRequested:
            x = "+ApplicationEntryUpdates="
            if self._myHasApplicationEntryUpdates:
                leafStr = str(self.applicationEntryUpdates)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOsTableLoadFailuresRequested:
            x = "+OsTableLoadFailures="
            if self._myHasOsTableLoadFailures:
                leafStr = str(self.osTableLoadFailures)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myApplicationRequestDiscardsRequested:
            x = "+ApplicationRequestDiscards="
            if self._myHasApplicationRequestDiscards:
                leafStr = str(self.applicationRequestDiscards)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myApplicationRequestBlocksRequested:
            x = "+ApplicationRequestBlocks="
            if self._myHasApplicationRequestBlocks:
                leafStr = str(self.applicationRequestBlocks)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myApplicationRequestsRequested:
            x = "+ApplicationRequests="
            if self._myHasApplicationRequests:
                leafStr = str(self.applicationRequests)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOsTableLoadsRequested:
            x = "+OsTableLoads="
            if self._myHasOsTableLoads:
                leafStr = str(self.osTableLoads)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNeighborDiscoveryRequestsSentRequested:
            x = "+NeighborDiscoveryRequestsSent="
            if self._myHasNeighborDiscoveryRequestsSent:
                leafStr = str(self.neighborDiscoveryRequestsSent)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myApplicationEntryFailuresRequested:
            x = "+ApplicationEntryFailures="
            if self._myHasApplicationEntryFailures:
                leafStr = str(self.applicationEntryFailures)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{CountersOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ApplicationEntryDiscards="
        if self._myHasApplicationEntryDiscards:
            leafStr = str(self.applicationEntryDiscards)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myApplicationEntryDiscardsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+NeighborDiscoveryFailures="
        if self._myHasNeighborDiscoveryFailures:
            leafStr = str(self.neighborDiscoveryFailures)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNeighborDiscoveryFailuresRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+NeighborDiscoveryTimeouts="
        if self._myHasNeighborDiscoveryTimeouts:
            leafStr = str(self.neighborDiscoveryTimeouts)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNeighborDiscoveryTimeoutsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+NeighborDiscoverySuccesses="
        if self._myHasNeighborDiscoverySuccesses:
            leafStr = str(self.neighborDiscoverySuccesses)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNeighborDiscoverySuccessesRequested:
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
        x = "+ApplicationRequestFailures="
        if self._myHasApplicationRequestFailures:
            leafStr = str(self.applicationRequestFailures)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myApplicationRequestFailuresRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ApplicationEntryUpdates="
        if self._myHasApplicationEntryUpdates:
            leafStr = str(self.applicationEntryUpdates)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myApplicationEntryUpdatesRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OsTableLoadFailures="
        if self._myHasOsTableLoadFailures:
            leafStr = str(self.osTableLoadFailures)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOsTableLoadFailuresRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ApplicationRequestDiscards="
        if self._myHasApplicationRequestDiscards:
            leafStr = str(self.applicationRequestDiscards)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myApplicationRequestDiscardsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ApplicationRequestBlocks="
        if self._myHasApplicationRequestBlocks:
            leafStr = str(self.applicationRequestBlocks)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myApplicationRequestBlocksRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ApplicationRequests="
        if self._myHasApplicationRequests:
            leafStr = str(self.applicationRequests)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myApplicationRequestsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OsTableLoads="
        if self._myHasOsTableLoads:
            leafStr = str(self.osTableLoads)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOsTableLoadsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+NeighborDiscoveryRequestsSent="
        if self._myHasNeighborDiscoveryRequestsSent:
            leafStr = str(self.neighborDiscoveryRequestsSent)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNeighborDiscoveryRequestsSentRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ApplicationEntryFailures="
        if self._myHasApplicationEntryFailures:
            leafStr = str(self.applicationEntryFailures)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myApplicationEntryFailuresRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setApplicationEntryDiscardsRequested()
        self.setNeighborDiscoveryFailuresRequested()
        self.setNeighborDiscoveryTimeoutsRequested()
        self.setNeighborDiscoverySuccessesRequested()
        self.setPollsRequested()
        self.setApplicationRequestFailuresRequested()
        self.setApplicationEntryUpdatesRequested()
        self.setOsTableLoadFailuresRequested()
        self.setApplicationRequestDiscardsRequested()
        self.setApplicationRequestBlocksRequested()
        self.setApplicationRequestsRequested()
        self.setOsTableLoadsRequested()
        self.setNeighborDiscoveryRequestsSentRequested()
        self.setApplicationEntryFailuresRequested()
        
        


    def setApplicationEntryDiscards (self, applicationEntryDiscards):
        self.applicationEntryDiscards = applicationEntryDiscards
        self.setHasApplicationEntryDiscards()

    def setNeighborDiscoveryFailures (self, neighborDiscoveryFailures):
        self.neighborDiscoveryFailures = neighborDiscoveryFailures
        self.setHasNeighborDiscoveryFailures()

    def setNeighborDiscoveryTimeouts (self, neighborDiscoveryTimeouts):
        self.neighborDiscoveryTimeouts = neighborDiscoveryTimeouts
        self.setHasNeighborDiscoveryTimeouts()

    def setNeighborDiscoverySuccesses (self, neighborDiscoverySuccesses):
        self.neighborDiscoverySuccesses = neighborDiscoverySuccesses
        self.setHasNeighborDiscoverySuccesses()

    def setPolls (self, polls):
        self.polls = polls
        self.setHasPolls()

    def setApplicationRequestFailures (self, applicationRequestFailures):
        self.applicationRequestFailures = applicationRequestFailures
        self.setHasApplicationRequestFailures()

    def setApplicationEntryUpdates (self, applicationEntryUpdates):
        self.applicationEntryUpdates = applicationEntryUpdates
        self.setHasApplicationEntryUpdates()

    def setOsTableLoadFailures (self, osTableLoadFailures):
        self.osTableLoadFailures = osTableLoadFailures
        self.setHasOsTableLoadFailures()

    def setApplicationRequestDiscards (self, applicationRequestDiscards):
        self.applicationRequestDiscards = applicationRequestDiscards
        self.setHasApplicationRequestDiscards()

    def setApplicationRequestBlocks (self, applicationRequestBlocks):
        self.applicationRequestBlocks = applicationRequestBlocks
        self.setHasApplicationRequestBlocks()

    def setApplicationRequests (self, applicationRequests):
        self.applicationRequests = applicationRequests
        self.setHasApplicationRequests()

    def setOsTableLoads (self, osTableLoads):
        self.osTableLoads = osTableLoads
        self.setHasOsTableLoads()

    def setNeighborDiscoveryRequestsSent (self, neighborDiscoveryRequestsSent):
        self.neighborDiscoveryRequestsSent = neighborDiscoveryRequestsSent
        self.setHasNeighborDiscoveryRequestsSent()

    def setApplicationEntryFailures (self, applicationEntryFailures):
        self.applicationEntryFailures = applicationEntryFailures
        self.setHasApplicationEntryFailures()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.counters.counters_oper_data_gen import CountersOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "network", 
            "isCurrent": false
        }, 
        {
            "namespace": "ipv6", 
            "isCurrent": false
        }, 
        {
            "namespace": "neighbors", 
            "isCurrent": false
        }, 
        {
            "namespace": "application_initiated_discovery", 
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
            "memberName": "applicationEntryDiscards", 
            "yangName": "application-entry-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryFailures", 
            "yangName": "neighbor-discovery-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryTimeouts", 
            "yangName": "neighbor-discovery-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoverySuccesses", 
            "yangName": "neighbor-discovery-successes", 
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
            "memberName": "applicationRequestFailures", 
            "yangName": "application-request-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryUpdates", 
            "yangName": "application-entry-updates", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoadFailures", 
            "yangName": "os-table-load-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestDiscards", 
            "yangName": "application-request-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestBlocks", 
            "yangName": "application-request-blocks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequests", 
            "yangName": "application-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoads", 
            "yangName": "os-table-loads", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryRequestsSent", 
            "yangName": "neighbor-discovery-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryFailures", 
            "yangName": "application-entry-failures", 
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
            "qwilt_tech_network_ipv6"
        ]
    }, 
    "createTime": "2013"
}
"""


