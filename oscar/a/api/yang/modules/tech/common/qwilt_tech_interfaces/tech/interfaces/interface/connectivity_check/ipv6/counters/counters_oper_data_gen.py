


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

        self.neighborDiscoveryFailures = 0
        self._myHasNeighborDiscoveryFailures=False
        self._myNeighborDiscoveryFailuresRequested=False
        
        self.neighborDiscoveryTimeouts = 0
        self._myHasNeighborDiscoveryTimeouts=False
        self._myNeighborDiscoveryTimeoutsRequested=False
        
        self.neighborDiscoverySuccesses = 0
        self._myHasNeighborDiscoverySuccesses=False
        self._myNeighborDiscoverySuccessesRequested=False
        
        self.pingRequestsSent = 0
        self._myHasPingRequestsSent=False
        self._myPingRequestsSentRequested=False
        
        self.pingFailures = 0
        self._myHasPingFailures=False
        self._myPingFailuresRequested=False
        
        self.pingSuccesses = 0
        self._myHasPingSuccesses=False
        self._myPingSuccessesRequested=False
        
        self.neighborDiscoveryRequestsSent = 0
        self._myHasNeighborDiscoveryRequestsSent=False
        self._myNeighborDiscoveryRequestsSentRequested=False
        
        self.pingTimeouts = 0
        self._myHasPingTimeouts=False
        self._myPingTimeoutsRequested=False
        


    def copyFrom (self, other):

        self.neighborDiscoveryFailures=other.neighborDiscoveryFailures
        self._myHasNeighborDiscoveryFailures=other._myHasNeighborDiscoveryFailures
        self._myNeighborDiscoveryFailuresRequested=other._myNeighborDiscoveryFailuresRequested
        
        self.neighborDiscoveryTimeouts=other.neighborDiscoveryTimeouts
        self._myHasNeighborDiscoveryTimeouts=other._myHasNeighborDiscoveryTimeouts
        self._myNeighborDiscoveryTimeoutsRequested=other._myNeighborDiscoveryTimeoutsRequested
        
        self.neighborDiscoverySuccesses=other.neighborDiscoverySuccesses
        self._myHasNeighborDiscoverySuccesses=other._myHasNeighborDiscoverySuccesses
        self._myNeighborDiscoverySuccessesRequested=other._myNeighborDiscoverySuccessesRequested
        
        self.pingRequestsSent=other.pingRequestsSent
        self._myHasPingRequestsSent=other._myHasPingRequestsSent
        self._myPingRequestsSentRequested=other._myPingRequestsSentRequested
        
        self.pingFailures=other.pingFailures
        self._myHasPingFailures=other._myHasPingFailures
        self._myPingFailuresRequested=other._myPingFailuresRequested
        
        self.pingSuccesses=other.pingSuccesses
        self._myHasPingSuccesses=other._myHasPingSuccesses
        self._myPingSuccessesRequested=other._myPingSuccessesRequested
        
        self.neighborDiscoveryRequestsSent=other.neighborDiscoveryRequestsSent
        self._myHasNeighborDiscoveryRequestsSent=other._myHasNeighborDiscoveryRequestsSent
        self._myNeighborDiscoveryRequestsSentRequested=other._myNeighborDiscoveryRequestsSentRequested
        
        self.pingTimeouts=other.pingTimeouts
        self._myHasPingTimeouts=other._myHasPingTimeouts
        self._myPingTimeoutsRequested=other._myPingTimeoutsRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

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
        
        if self.isPingRequestsSentRequested():
            self.pingRequestsSent=other.pingRequestsSent
            self._myHasPingRequestsSent=other._myHasPingRequestsSent
            self._myPingRequestsSentRequested=other._myPingRequestsSentRequested
        
        if self.isPingFailuresRequested():
            self.pingFailures=other.pingFailures
            self._myHasPingFailures=other._myHasPingFailures
            self._myPingFailuresRequested=other._myPingFailuresRequested
        
        if self.isPingSuccessesRequested():
            self.pingSuccesses=other.pingSuccesses
            self._myHasPingSuccesses=other._myHasPingSuccesses
            self._myPingSuccessesRequested=other._myPingSuccessesRequested
        
        if self.isNeighborDiscoveryRequestsSentRequested():
            self.neighborDiscoveryRequestsSent=other.neighborDiscoveryRequestsSent
            self._myHasNeighborDiscoveryRequestsSent=other._myHasNeighborDiscoveryRequestsSent
            self._myNeighborDiscoveryRequestsSentRequested=other._myNeighborDiscoveryRequestsSentRequested
        
        if self.isPingTimeoutsRequested():
            self.pingTimeouts=other.pingTimeouts
            self._myHasPingTimeouts=other._myHasPingTimeouts
            self._myPingTimeoutsRequested=other._myPingTimeoutsRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

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
        
        if other.hasPingRequestsSent():
            self.pingRequestsSent=other.pingRequestsSent
            self._myHasPingRequestsSent=other._myHasPingRequestsSent
            self._myPingRequestsSentRequested=other._myPingRequestsSentRequested
        
        if other.hasPingFailures():
            self.pingFailures=other.pingFailures
            self._myHasPingFailures=other._myHasPingFailures
            self._myPingFailuresRequested=other._myPingFailuresRequested
        
        if other.hasPingSuccesses():
            self.pingSuccesses=other.pingSuccesses
            self._myHasPingSuccesses=other._myHasPingSuccesses
            self._myPingSuccessesRequested=other._myPingSuccessesRequested
        
        if other.hasNeighborDiscoveryRequestsSent():
            self.neighborDiscoveryRequestsSent=other.neighborDiscoveryRequestsSent
            self._myHasNeighborDiscoveryRequestsSent=other._myHasNeighborDiscoveryRequestsSent
            self._myNeighborDiscoveryRequestsSentRequested=other._myNeighborDiscoveryRequestsSentRequested
        
        if other.hasPingTimeouts():
            self.pingTimeouts=other.pingTimeouts
            self._myHasPingTimeouts=other._myHasPingTimeouts
            self._myPingTimeoutsRequested=other._myPingTimeoutsRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.neighborDiscoveryFailures=other.neighborDiscoveryFailures
        self._myHasNeighborDiscoveryFailures=other._myHasNeighborDiscoveryFailures
        
        self.neighborDiscoveryTimeouts=other.neighborDiscoveryTimeouts
        self._myHasNeighborDiscoveryTimeouts=other._myHasNeighborDiscoveryTimeouts
        
        self.neighborDiscoverySuccesses=other.neighborDiscoverySuccesses
        self._myHasNeighborDiscoverySuccesses=other._myHasNeighborDiscoverySuccesses
        
        self.pingRequestsSent=other.pingRequestsSent
        self._myHasPingRequestsSent=other._myHasPingRequestsSent
        
        self.pingFailures=other.pingFailures
        self._myHasPingFailures=other._myHasPingFailures
        
        self.pingSuccesses=other.pingSuccesses
        self._myHasPingSuccesses=other._myHasPingSuccesses
        
        self.neighborDiscoveryRequestsSent=other.neighborDiscoveryRequestsSent
        self._myHasNeighborDiscoveryRequestsSent=other._myHasNeighborDiscoveryRequestsSent
        
        self.pingTimeouts=other.pingTimeouts
        self._myHasPingTimeouts=other._myHasPingTimeouts
        


    def setAllNumericToZero (self):
        
        self.neighborDiscoveryFailures=0
        self.setHasNeighborDiscoveryFailures()
        self.neighborDiscoveryTimeouts=0
        self.setHasNeighborDiscoveryTimeouts()
        self.neighborDiscoverySuccesses=0
        self.setHasNeighborDiscoverySuccesses()
        self.pingRequestsSent=0
        self.setHasPingRequestsSent()
        self.pingFailures=0
        self.setHasPingFailures()
        self.pingSuccesses=0
        self.setHasPingSuccesses()
        self.neighborDiscoveryRequestsSent=0
        self.setHasNeighborDiscoveryRequestsSent()
        self.pingTimeouts=0
        self.setHasPingTimeouts()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasNeighborDiscoveryFailures():
            if other.hasNeighborDiscoveryFailures():
                self.neighborDiscoveryFailures -= other.neighborDiscoveryFailures
        
        if self.hasNeighborDiscoveryTimeouts():
            if other.hasNeighborDiscoveryTimeouts():
                self.neighborDiscoveryTimeouts -= other.neighborDiscoveryTimeouts
        
        if self.hasNeighborDiscoverySuccesses():
            if other.hasNeighborDiscoverySuccesses():
                self.neighborDiscoverySuccesses -= other.neighborDiscoverySuccesses
        
        if self.hasPingRequestsSent():
            if other.hasPingRequestsSent():
                self.pingRequestsSent -= other.pingRequestsSent
        
        if self.hasPingFailures():
            if other.hasPingFailures():
                self.pingFailures -= other.pingFailures
        
        if self.hasPingSuccesses():
            if other.hasPingSuccesses():
                self.pingSuccesses -= other.pingSuccesses
        
        if self.hasNeighborDiscoveryRequestsSent():
            if other.hasNeighborDiscoveryRequestsSent():
                self.neighborDiscoveryRequestsSent -= other.neighborDiscoveryRequestsSent
        
        if self.hasPingTimeouts():
            if other.hasPingTimeouts():
                self.pingTimeouts -= other.pingTimeouts
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasNeighborDiscoveryFailures():
            if other.hasNeighborDiscoveryFailures():
                self.neighborDiscoveryFailures += other.neighborDiscoveryFailures
        
        if self.hasNeighborDiscoveryTimeouts():
            if other.hasNeighborDiscoveryTimeouts():
                self.neighborDiscoveryTimeouts += other.neighborDiscoveryTimeouts
        
        if self.hasNeighborDiscoverySuccesses():
            if other.hasNeighborDiscoverySuccesses():
                self.neighborDiscoverySuccesses += other.neighborDiscoverySuccesses
        
        if self.hasPingRequestsSent():
            if other.hasPingRequestsSent():
                self.pingRequestsSent += other.pingRequestsSent
        
        if self.hasPingFailures():
            if other.hasPingFailures():
                self.pingFailures += other.pingFailures
        
        if self.hasPingSuccesses():
            if other.hasPingSuccesses():
                self.pingSuccesses += other.pingSuccesses
        
        if self.hasNeighborDiscoveryRequestsSent():
            if other.hasNeighborDiscoveryRequestsSent():
                self.neighborDiscoveryRequestsSent += other.neighborDiscoveryRequestsSent
        
        if self.hasPingTimeouts():
            if other.hasPingTimeouts():
                self.pingTimeouts += other.pingTimeouts
        
        
        pass


    # has...() methods

    def hasNeighborDiscoveryFailures (self):
        return self._myHasNeighborDiscoveryFailures

    def hasNeighborDiscoveryTimeouts (self):
        return self._myHasNeighborDiscoveryTimeouts

    def hasNeighborDiscoverySuccesses (self):
        return self._myHasNeighborDiscoverySuccesses

    def hasPingRequestsSent (self):
        return self._myHasPingRequestsSent

    def hasPingFailures (self):
        return self._myHasPingFailures

    def hasPingSuccesses (self):
        return self._myHasPingSuccesses

    def hasNeighborDiscoveryRequestsSent (self):
        return self._myHasNeighborDiscoveryRequestsSent

    def hasPingTimeouts (self):
        return self._myHasPingTimeouts




    # setHas...() methods

    def setHasNeighborDiscoveryFailures (self):
        self._myHasNeighborDiscoveryFailures=True

    def setHasNeighborDiscoveryTimeouts (self):
        self._myHasNeighborDiscoveryTimeouts=True

    def setHasNeighborDiscoverySuccesses (self):
        self._myHasNeighborDiscoverySuccesses=True

    def setHasPingRequestsSent (self):
        self._myHasPingRequestsSent=True

    def setHasPingFailures (self):
        self._myHasPingFailures=True

    def setHasPingSuccesses (self):
        self._myHasPingSuccesses=True

    def setHasNeighborDiscoveryRequestsSent (self):
        self._myHasNeighborDiscoveryRequestsSent=True

    def setHasPingTimeouts (self):
        self._myHasPingTimeouts=True




    # isRequested...() methods

    def isNeighborDiscoveryFailuresRequested (self):
        return self._myNeighborDiscoveryFailuresRequested

    def isNeighborDiscoveryTimeoutsRequested (self):
        return self._myNeighborDiscoveryTimeoutsRequested

    def isNeighborDiscoverySuccessesRequested (self):
        return self._myNeighborDiscoverySuccessesRequested

    def isPingRequestsSentRequested (self):
        return self._myPingRequestsSentRequested

    def isPingFailuresRequested (self):
        return self._myPingFailuresRequested

    def isPingSuccessesRequested (self):
        return self._myPingSuccessesRequested

    def isNeighborDiscoveryRequestsSentRequested (self):
        return self._myNeighborDiscoveryRequestsSentRequested

    def isPingTimeoutsRequested (self):
        return self._myPingTimeoutsRequested




    # setRequested...() methods

    def setNeighborDiscoveryFailuresRequested (self):
        self._myNeighborDiscoveryFailuresRequested=True

    def setNeighborDiscoveryTimeoutsRequested (self):
        self._myNeighborDiscoveryTimeoutsRequested=True

    def setNeighborDiscoverySuccessesRequested (self):
        self._myNeighborDiscoverySuccessesRequested=True

    def setPingRequestsSentRequested (self):
        self._myPingRequestsSentRequested=True

    def setPingFailuresRequested (self):
        self._myPingFailuresRequested=True

    def setPingSuccessesRequested (self):
        self._myPingSuccessesRequested=True

    def setNeighborDiscoveryRequestsSentRequested (self):
        self._myNeighborDiscoveryRequestsSentRequested=True

    def setPingTimeoutsRequested (self):
        self._myPingTimeoutsRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

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
        if self._myPingRequestsSentRequested:
            x = "+PingRequestsSent="
            if self._myHasPingRequestsSent:
                leafStr = str(self.pingRequestsSent)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPingFailuresRequested:
            x = "+PingFailures="
            if self._myHasPingFailures:
                leafStr = str(self.pingFailures)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myPingSuccessesRequested:
            x = "+PingSuccesses="
            if self._myHasPingSuccesses:
                leafStr = str(self.pingSuccesses)
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
        if self._myPingTimeoutsRequested:
            x = "+PingTimeouts="
            if self._myHasPingTimeouts:
                leafStr = str(self.pingTimeouts)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{CountersOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

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
        x = "+PingRequestsSent="
        if self._myHasPingRequestsSent:
            leafStr = str(self.pingRequestsSent)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPingRequestsSentRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PingFailures="
        if self._myHasPingFailures:
            leafStr = str(self.pingFailures)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPingFailuresRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+PingSuccesses="
        if self._myHasPingSuccesses:
            leafStr = str(self.pingSuccesses)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPingSuccessesRequested:
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
        x = "+PingTimeouts="
        if self._myHasPingTimeouts:
            leafStr = str(self.pingTimeouts)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPingTimeoutsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setNeighborDiscoveryFailuresRequested()
        self.setNeighborDiscoveryTimeoutsRequested()
        self.setNeighborDiscoverySuccessesRequested()
        self.setPingRequestsSentRequested()
        self.setPingFailuresRequested()
        self.setPingSuccessesRequested()
        self.setNeighborDiscoveryRequestsSentRequested()
        self.setPingTimeoutsRequested()
        
        


    def setNeighborDiscoveryFailures (self, neighborDiscoveryFailures):
        self.neighborDiscoveryFailures = neighborDiscoveryFailures
        self.setHasNeighborDiscoveryFailures()

    def setNeighborDiscoveryTimeouts (self, neighborDiscoveryTimeouts):
        self.neighborDiscoveryTimeouts = neighborDiscoveryTimeouts
        self.setHasNeighborDiscoveryTimeouts()

    def setNeighborDiscoverySuccesses (self, neighborDiscoverySuccesses):
        self.neighborDiscoverySuccesses = neighborDiscoverySuccesses
        self.setHasNeighborDiscoverySuccesses()

    def setPingRequestsSent (self, pingRequestsSent):
        self.pingRequestsSent = pingRequestsSent
        self.setHasPingRequestsSent()

    def setPingFailures (self, pingFailures):
        self.pingFailures = pingFailures
        self.setHasPingFailures()

    def setPingSuccesses (self, pingSuccesses):
        self.pingSuccesses = pingSuccesses
        self.setHasPingSuccesses()

    def setNeighborDiscoveryRequestsSent (self, neighborDiscoveryRequestsSent):
        self.neighborDiscoveryRequestsSent = neighborDiscoveryRequestsSent
        self.setHasNeighborDiscoveryRequestsSent()

    def setPingTimeouts (self, pingTimeouts):
        self.pingTimeouts = pingTimeouts
        self.setHasPingTimeouts()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv6.counters.counters_oper_data_gen import CountersOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "interfaces", 
            "isCurrent": false
        }, 
        {
            "namespace": "interface", 
            "isCurrent": false
        }, 
        {
            "namespace": "connectivity_check", 
            "isCurrent": false
        }, 
        {
            "namespace": "ipv6", 
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
            "memberName": "pingRequestsSent", 
            "yangName": "ping-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingFailures", 
            "yangName": "ping-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingSuccesses", 
            "yangName": "ping-successes", 
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
            "memberName": "pingTimeouts", 
            "yangName": "ping-timeouts", 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "createTime": "2013"
}
"""


