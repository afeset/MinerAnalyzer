


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

        self.arpFailures = 0
        self._myHasArpFailures=False
        self._myArpFailuresRequested=False
        
        self.arpRequestsSent = 0
        self._myHasArpRequestsSent=False
        self._myArpRequestsSentRequested=False
        
        self.pingSuccesses = 0
        self._myHasPingSuccesses=False
        self._myPingSuccessesRequested=False
        
        self.pingRequestsSent = 0
        self._myHasPingRequestsSent=False
        self._myPingRequestsSentRequested=False
        
        self.arpSuccesses = 0
        self._myHasArpSuccesses=False
        self._myArpSuccessesRequested=False
        
        self.pingFailures = 0
        self._myHasPingFailures=False
        self._myPingFailuresRequested=False
        
        self.arpTimeouts = 0
        self._myHasArpTimeouts=False
        self._myArpTimeoutsRequested=False
        
        self.pingTimeouts = 0
        self._myHasPingTimeouts=False
        self._myPingTimeoutsRequested=False
        


    def copyFrom (self, other):

        self.arpFailures=other.arpFailures
        self._myHasArpFailures=other._myHasArpFailures
        self._myArpFailuresRequested=other._myArpFailuresRequested
        
        self.arpRequestsSent=other.arpRequestsSent
        self._myHasArpRequestsSent=other._myHasArpRequestsSent
        self._myArpRequestsSentRequested=other._myArpRequestsSentRequested
        
        self.pingSuccesses=other.pingSuccesses
        self._myHasPingSuccesses=other._myHasPingSuccesses
        self._myPingSuccessesRequested=other._myPingSuccessesRequested
        
        self.pingRequestsSent=other.pingRequestsSent
        self._myHasPingRequestsSent=other._myHasPingRequestsSent
        self._myPingRequestsSentRequested=other._myPingRequestsSentRequested
        
        self.arpSuccesses=other.arpSuccesses
        self._myHasArpSuccesses=other._myHasArpSuccesses
        self._myArpSuccessesRequested=other._myArpSuccessesRequested
        
        self.pingFailures=other.pingFailures
        self._myHasPingFailures=other._myHasPingFailures
        self._myPingFailuresRequested=other._myPingFailuresRequested
        
        self.arpTimeouts=other.arpTimeouts
        self._myHasArpTimeouts=other._myHasArpTimeouts
        self._myArpTimeoutsRequested=other._myArpTimeoutsRequested
        
        self.pingTimeouts=other.pingTimeouts
        self._myHasPingTimeouts=other._myHasPingTimeouts
        self._myPingTimeoutsRequested=other._myPingTimeoutsRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isArpFailuresRequested():
            self.arpFailures=other.arpFailures
            self._myHasArpFailures=other._myHasArpFailures
            self._myArpFailuresRequested=other._myArpFailuresRequested
        
        if self.isArpRequestsSentRequested():
            self.arpRequestsSent=other.arpRequestsSent
            self._myHasArpRequestsSent=other._myHasArpRequestsSent
            self._myArpRequestsSentRequested=other._myArpRequestsSentRequested
        
        if self.isPingSuccessesRequested():
            self.pingSuccesses=other.pingSuccesses
            self._myHasPingSuccesses=other._myHasPingSuccesses
            self._myPingSuccessesRequested=other._myPingSuccessesRequested
        
        if self.isPingRequestsSentRequested():
            self.pingRequestsSent=other.pingRequestsSent
            self._myHasPingRequestsSent=other._myHasPingRequestsSent
            self._myPingRequestsSentRequested=other._myPingRequestsSentRequested
        
        if self.isArpSuccessesRequested():
            self.arpSuccesses=other.arpSuccesses
            self._myHasArpSuccesses=other._myHasArpSuccesses
            self._myArpSuccessesRequested=other._myArpSuccessesRequested
        
        if self.isPingFailuresRequested():
            self.pingFailures=other.pingFailures
            self._myHasPingFailures=other._myHasPingFailures
            self._myPingFailuresRequested=other._myPingFailuresRequested
        
        if self.isArpTimeoutsRequested():
            self.arpTimeouts=other.arpTimeouts
            self._myHasArpTimeouts=other._myHasArpTimeouts
            self._myArpTimeoutsRequested=other._myArpTimeoutsRequested
        
        if self.isPingTimeoutsRequested():
            self.pingTimeouts=other.pingTimeouts
            self._myHasPingTimeouts=other._myHasPingTimeouts
            self._myPingTimeoutsRequested=other._myPingTimeoutsRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasArpFailures():
            self.arpFailures=other.arpFailures
            self._myHasArpFailures=other._myHasArpFailures
            self._myArpFailuresRequested=other._myArpFailuresRequested
        
        if other.hasArpRequestsSent():
            self.arpRequestsSent=other.arpRequestsSent
            self._myHasArpRequestsSent=other._myHasArpRequestsSent
            self._myArpRequestsSentRequested=other._myArpRequestsSentRequested
        
        if other.hasPingSuccesses():
            self.pingSuccesses=other.pingSuccesses
            self._myHasPingSuccesses=other._myHasPingSuccesses
            self._myPingSuccessesRequested=other._myPingSuccessesRequested
        
        if other.hasPingRequestsSent():
            self.pingRequestsSent=other.pingRequestsSent
            self._myHasPingRequestsSent=other._myHasPingRequestsSent
            self._myPingRequestsSentRequested=other._myPingRequestsSentRequested
        
        if other.hasArpSuccesses():
            self.arpSuccesses=other.arpSuccesses
            self._myHasArpSuccesses=other._myHasArpSuccesses
            self._myArpSuccessesRequested=other._myArpSuccessesRequested
        
        if other.hasPingFailures():
            self.pingFailures=other.pingFailures
            self._myHasPingFailures=other._myHasPingFailures
            self._myPingFailuresRequested=other._myPingFailuresRequested
        
        if other.hasArpTimeouts():
            self.arpTimeouts=other.arpTimeouts
            self._myHasArpTimeouts=other._myHasArpTimeouts
            self._myArpTimeoutsRequested=other._myArpTimeoutsRequested
        
        if other.hasPingTimeouts():
            self.pingTimeouts=other.pingTimeouts
            self._myHasPingTimeouts=other._myHasPingTimeouts
            self._myPingTimeoutsRequested=other._myPingTimeoutsRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.arpFailures=other.arpFailures
        self._myHasArpFailures=other._myHasArpFailures
        
        self.arpRequestsSent=other.arpRequestsSent
        self._myHasArpRequestsSent=other._myHasArpRequestsSent
        
        self.pingSuccesses=other.pingSuccesses
        self._myHasPingSuccesses=other._myHasPingSuccesses
        
        self.pingRequestsSent=other.pingRequestsSent
        self._myHasPingRequestsSent=other._myHasPingRequestsSent
        
        self.arpSuccesses=other.arpSuccesses
        self._myHasArpSuccesses=other._myHasArpSuccesses
        
        self.pingFailures=other.pingFailures
        self._myHasPingFailures=other._myHasPingFailures
        
        self.arpTimeouts=other.arpTimeouts
        self._myHasArpTimeouts=other._myHasArpTimeouts
        
        self.pingTimeouts=other.pingTimeouts
        self._myHasPingTimeouts=other._myHasPingTimeouts
        


    def setAllNumericToZero (self):
        
        self.arpFailures=0
        self.setHasArpFailures()
        self.arpRequestsSent=0
        self.setHasArpRequestsSent()
        self.pingSuccesses=0
        self.setHasPingSuccesses()
        self.pingRequestsSent=0
        self.setHasPingRequestsSent()
        self.arpSuccesses=0
        self.setHasArpSuccesses()
        self.pingFailures=0
        self.setHasPingFailures()
        self.arpTimeouts=0
        self.setHasArpTimeouts()
        self.pingTimeouts=0
        self.setHasPingTimeouts()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasArpFailures():
            if other.hasArpFailures():
                self.arpFailures -= other.arpFailures
        
        if self.hasArpRequestsSent():
            if other.hasArpRequestsSent():
                self.arpRequestsSent -= other.arpRequestsSent
        
        if self.hasPingSuccesses():
            if other.hasPingSuccesses():
                self.pingSuccesses -= other.pingSuccesses
        
        if self.hasPingRequestsSent():
            if other.hasPingRequestsSent():
                self.pingRequestsSent -= other.pingRequestsSent
        
        if self.hasArpSuccesses():
            if other.hasArpSuccesses():
                self.arpSuccesses -= other.arpSuccesses
        
        if self.hasPingFailures():
            if other.hasPingFailures():
                self.pingFailures -= other.pingFailures
        
        if self.hasArpTimeouts():
            if other.hasArpTimeouts():
                self.arpTimeouts -= other.arpTimeouts
        
        if self.hasPingTimeouts():
            if other.hasPingTimeouts():
                self.pingTimeouts -= other.pingTimeouts
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasArpFailures():
            if other.hasArpFailures():
                self.arpFailures += other.arpFailures
        
        if self.hasArpRequestsSent():
            if other.hasArpRequestsSent():
                self.arpRequestsSent += other.arpRequestsSent
        
        if self.hasPingSuccesses():
            if other.hasPingSuccesses():
                self.pingSuccesses += other.pingSuccesses
        
        if self.hasPingRequestsSent():
            if other.hasPingRequestsSent():
                self.pingRequestsSent += other.pingRequestsSent
        
        if self.hasArpSuccesses():
            if other.hasArpSuccesses():
                self.arpSuccesses += other.arpSuccesses
        
        if self.hasPingFailures():
            if other.hasPingFailures():
                self.pingFailures += other.pingFailures
        
        if self.hasArpTimeouts():
            if other.hasArpTimeouts():
                self.arpTimeouts += other.arpTimeouts
        
        if self.hasPingTimeouts():
            if other.hasPingTimeouts():
                self.pingTimeouts += other.pingTimeouts
        
        
        pass


    # has...() methods

    def hasArpFailures (self):
        return self._myHasArpFailures

    def hasArpRequestsSent (self):
        return self._myHasArpRequestsSent

    def hasPingSuccesses (self):
        return self._myHasPingSuccesses

    def hasPingRequestsSent (self):
        return self._myHasPingRequestsSent

    def hasArpSuccesses (self):
        return self._myHasArpSuccesses

    def hasPingFailures (self):
        return self._myHasPingFailures

    def hasArpTimeouts (self):
        return self._myHasArpTimeouts

    def hasPingTimeouts (self):
        return self._myHasPingTimeouts




    # setHas...() methods

    def setHasArpFailures (self):
        self._myHasArpFailures=True

    def setHasArpRequestsSent (self):
        self._myHasArpRequestsSent=True

    def setHasPingSuccesses (self):
        self._myHasPingSuccesses=True

    def setHasPingRequestsSent (self):
        self._myHasPingRequestsSent=True

    def setHasArpSuccesses (self):
        self._myHasArpSuccesses=True

    def setHasPingFailures (self):
        self._myHasPingFailures=True

    def setHasArpTimeouts (self):
        self._myHasArpTimeouts=True

    def setHasPingTimeouts (self):
        self._myHasPingTimeouts=True




    # isRequested...() methods

    def isArpFailuresRequested (self):
        return self._myArpFailuresRequested

    def isArpRequestsSentRequested (self):
        return self._myArpRequestsSentRequested

    def isPingSuccessesRequested (self):
        return self._myPingSuccessesRequested

    def isPingRequestsSentRequested (self):
        return self._myPingRequestsSentRequested

    def isArpSuccessesRequested (self):
        return self._myArpSuccessesRequested

    def isPingFailuresRequested (self):
        return self._myPingFailuresRequested

    def isArpTimeoutsRequested (self):
        return self._myArpTimeoutsRequested

    def isPingTimeoutsRequested (self):
        return self._myPingTimeoutsRequested




    # setRequested...() methods

    def setArpFailuresRequested (self):
        self._myArpFailuresRequested=True

    def setArpRequestsSentRequested (self):
        self._myArpRequestsSentRequested=True

    def setPingSuccessesRequested (self):
        self._myPingSuccessesRequested=True

    def setPingRequestsSentRequested (self):
        self._myPingRequestsSentRequested=True

    def setArpSuccessesRequested (self):
        self._myArpSuccessesRequested=True

    def setPingFailuresRequested (self):
        self._myPingFailuresRequested=True

    def setArpTimeoutsRequested (self):
        self._myArpTimeoutsRequested=True

    def setPingTimeoutsRequested (self):
        self._myPingTimeoutsRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myArpFailuresRequested:
            x = "+ArpFailures="
            if self._myHasArpFailures:
                leafStr = str(self.arpFailures)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myArpRequestsSentRequested:
            x = "+ArpRequestsSent="
            if self._myHasArpRequestsSent:
                leafStr = str(self.arpRequestsSent)
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
        if self._myPingRequestsSentRequested:
            x = "+PingRequestsSent="
            if self._myHasPingRequestsSent:
                leafStr = str(self.pingRequestsSent)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myArpSuccessesRequested:
            x = "+ArpSuccesses="
            if self._myHasArpSuccesses:
                leafStr = str(self.arpSuccesses)
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
        if self._myArpTimeoutsRequested:
            x = "+ArpTimeouts="
            if self._myHasArpTimeouts:
                leafStr = str(self.arpTimeouts)
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
        x = "+ArpFailures="
        if self._myHasArpFailures:
            leafStr = str(self.arpFailures)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myArpFailuresRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ArpRequestsSent="
        if self._myHasArpRequestsSent:
            leafStr = str(self.arpRequestsSent)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myArpRequestsSentRequested:
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
        x = "+ArpSuccesses="
        if self._myHasArpSuccesses:
            leafStr = str(self.arpSuccesses)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myArpSuccessesRequested:
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
        x = "+ArpTimeouts="
        if self._myHasArpTimeouts:
            leafStr = str(self.arpTimeouts)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myArpTimeoutsRequested:
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
        self.setArpFailuresRequested()
        self.setArpRequestsSentRequested()
        self.setPingSuccessesRequested()
        self.setPingRequestsSentRequested()
        self.setArpSuccessesRequested()
        self.setPingFailuresRequested()
        self.setArpTimeoutsRequested()
        self.setPingTimeoutsRequested()
        
        


    def setArpFailures (self, arpFailures):
        self.arpFailures = arpFailures
        self.setHasArpFailures()

    def setArpRequestsSent (self, arpRequestsSent):
        self.arpRequestsSent = arpRequestsSent
        self.setHasArpRequestsSent()

    def setPingSuccesses (self, pingSuccesses):
        self.pingSuccesses = pingSuccesses
        self.setHasPingSuccesses()

    def setPingRequestsSent (self, pingRequestsSent):
        self.pingRequestsSent = pingRequestsSent
        self.setHasPingRequestsSent()

    def setArpSuccesses (self, arpSuccesses):
        self.arpSuccesses = arpSuccesses
        self.setHasArpSuccesses()

    def setPingFailures (self, pingFailures):
        self.pingFailures = pingFailures
        self.setHasPingFailures()

    def setArpTimeouts (self, arpTimeouts):
        self.arpTimeouts = arpTimeouts
        self.setHasArpTimeouts()

    def setPingTimeouts (self, pingTimeouts):
        self.pingTimeouts = pingTimeouts
        self.setHasPingTimeouts()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv4.counters.counters_oper_data_gen import CountersOperData"
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
            "namespace": "ipv4", 
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
            "memberName": "arpFailures", 
            "yangName": "arp-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "arpRequestsSent", 
            "yangName": "arp-requests-sent", 
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
            "memberName": "pingRequestsSent", 
            "yangName": "ping-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "arpSuccesses", 
            "yangName": "arp-successes", 
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
            "memberName": "arpTimeouts", 
            "yangName": "arp-timeouts", 
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


