


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

        self.applicationEntryCount = 0
        self._myHasApplicationEntryCount=False
        self._myApplicationEntryCountRequested=False
        
        self.concurrentRequests = 0
        self._myHasConcurrentRequests=False
        self._myConcurrentRequestsRequested=False
        


    def copyFrom (self, other):

        self.applicationEntryCount=other.applicationEntryCount
        self._myHasApplicationEntryCount=other._myHasApplicationEntryCount
        self._myApplicationEntryCountRequested=other._myApplicationEntryCountRequested
        
        self.concurrentRequests=other.concurrentRequests
        self._myHasConcurrentRequests=other._myHasConcurrentRequests
        self._myConcurrentRequestsRequested=other._myConcurrentRequestsRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isApplicationEntryCountRequested():
            self.applicationEntryCount=other.applicationEntryCount
            self._myHasApplicationEntryCount=other._myHasApplicationEntryCount
            self._myApplicationEntryCountRequested=other._myApplicationEntryCountRequested
        
        if self.isConcurrentRequestsRequested():
            self.concurrentRequests=other.concurrentRequests
            self._myHasConcurrentRequests=other._myHasConcurrentRequests
            self._myConcurrentRequestsRequested=other._myConcurrentRequestsRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasApplicationEntryCount():
            self.applicationEntryCount=other.applicationEntryCount
            self._myHasApplicationEntryCount=other._myHasApplicationEntryCount
            self._myApplicationEntryCountRequested=other._myApplicationEntryCountRequested
        
        if other.hasConcurrentRequests():
            self.concurrentRequests=other.concurrentRequests
            self._myHasConcurrentRequests=other._myHasConcurrentRequests
            self._myConcurrentRequestsRequested=other._myConcurrentRequestsRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.applicationEntryCount=other.applicationEntryCount
        self._myHasApplicationEntryCount=other._myHasApplicationEntryCount
        
        self.concurrentRequests=other.concurrentRequests
        self._myHasConcurrentRequests=other._myHasConcurrentRequests
        


    def setAllNumericToZero (self):
        
        self.applicationEntryCount=0
        self.setHasApplicationEntryCount()
        self.concurrentRequests=0
        self.setHasConcurrentRequests()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasApplicationEntryCount():
            if other.hasApplicationEntryCount():
                self.applicationEntryCount -= other.applicationEntryCount
        
        if self.hasConcurrentRequests():
            if other.hasConcurrentRequests():
                self.concurrentRequests -= other.concurrentRequests
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasApplicationEntryCount():
            if other.hasApplicationEntryCount():
                self.applicationEntryCount += other.applicationEntryCount
        
        if self.hasConcurrentRequests():
            if other.hasConcurrentRequests():
                self.concurrentRequests += other.concurrentRequests
        
        
        pass


    # has...() methods

    def hasApplicationEntryCount (self):
        return self._myHasApplicationEntryCount

    def hasConcurrentRequests (self):
        return self._myHasConcurrentRequests




    # setHas...() methods

    def setHasApplicationEntryCount (self):
        self._myHasApplicationEntryCount=True

    def setHasConcurrentRequests (self):
        self._myHasConcurrentRequests=True




    # isRequested...() methods

    def isApplicationEntryCountRequested (self):
        return self._myApplicationEntryCountRequested

    def isConcurrentRequestsRequested (self):
        return self._myConcurrentRequestsRequested




    # setRequested...() methods

    def setApplicationEntryCountRequested (self):
        self._myApplicationEntryCountRequested=True

    def setConcurrentRequestsRequested (self):
        self._myConcurrentRequestsRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myApplicationEntryCountRequested:
            x = "+ApplicationEntryCount="
            if self._myHasApplicationEntryCount:
                leafStr = str(self.applicationEntryCount)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myConcurrentRequestsRequested:
            x = "+ConcurrentRequests="
            if self._myHasConcurrentRequests:
                leafStr = str(self.concurrentRequests)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ApplicationEntryCount="
        if self._myHasApplicationEntryCount:
            leafStr = str(self.applicationEntryCount)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myApplicationEntryCountRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ConcurrentRequests="
        if self._myHasConcurrentRequests:
            leafStr = str(self.concurrentRequests)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myConcurrentRequestsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setApplicationEntryCountRequested()
        self.setConcurrentRequestsRequested()
        
        


    def setApplicationEntryCount (self, applicationEntryCount):
        self.applicationEntryCount = applicationEntryCount
        self.setHasApplicationEntryCount()

    def setConcurrentRequests (self, concurrentRequests):
        self.concurrentRequests = concurrentRequests
        self.setHasConcurrentRequests()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.status.status_oper_data_gen import StatusOperData"
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
            "namespace": "status", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryCount", 
            "yangName": "application-entry-count", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "concurrentRequests", 
            "yangName": "concurrent-requests", 
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


