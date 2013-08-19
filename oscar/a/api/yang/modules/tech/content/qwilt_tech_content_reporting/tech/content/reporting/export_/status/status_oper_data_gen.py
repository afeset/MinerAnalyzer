


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

        self.queueUtilizationPercent = 0
        self._myHasQueueUtilizationPercent=False
        self._myQueueUtilizationPercentRequested=False
        


    def copyFrom (self, other):

        self.queueUtilizationPercent=other.queueUtilizationPercent
        self._myHasQueueUtilizationPercent=other._myHasQueueUtilizationPercent
        self._myQueueUtilizationPercentRequested=other._myQueueUtilizationPercentRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isQueueUtilizationPercentRequested():
            self.queueUtilizationPercent=other.queueUtilizationPercent
            self._myHasQueueUtilizationPercent=other._myHasQueueUtilizationPercent
            self._myQueueUtilizationPercentRequested=other._myQueueUtilizationPercentRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasQueueUtilizationPercent():
            self.queueUtilizationPercent=other.queueUtilizationPercent
            self._myHasQueueUtilizationPercent=other._myHasQueueUtilizationPercent
            self._myQueueUtilizationPercentRequested=other._myQueueUtilizationPercentRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.queueUtilizationPercent=other.queueUtilizationPercent
        self._myHasQueueUtilizationPercent=other._myHasQueueUtilizationPercent
        


    def setAllNumericToZero (self):
        
        self.queueUtilizationPercent=0
        self.setHasQueueUtilizationPercent()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasQueueUtilizationPercent():
            if other.hasQueueUtilizationPercent():
                self.queueUtilizationPercent -= other.queueUtilizationPercent
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasQueueUtilizationPercent():
            if other.hasQueueUtilizationPercent():
                self.queueUtilizationPercent += other.queueUtilizationPercent
        
        
        pass


    # has...() methods

    def hasQueueUtilizationPercent (self):
        return self._myHasQueueUtilizationPercent




    # setHas...() methods

    def setHasQueueUtilizationPercent (self):
        self._myHasQueueUtilizationPercent=True




    # isRequested...() methods

    def isQueueUtilizationPercentRequested (self):
        return self._myQueueUtilizationPercentRequested




    # setRequested...() methods

    def setQueueUtilizationPercentRequested (self):
        self._myQueueUtilizationPercentRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myQueueUtilizationPercentRequested:
            x = "+QueueUtilizationPercent="
            if self._myHasQueueUtilizationPercent:
                leafStr = str(self.queueUtilizationPercent)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+QueueUtilizationPercent="
        if self._myHasQueueUtilizationPercent:
            leafStr = str(self.queueUtilizationPercent)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myQueueUtilizationPercentRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setQueueUtilizationPercentRequested()
        
        


    def setQueueUtilizationPercent (self, queueUtilizationPercent):
        self.queueUtilizationPercent = queueUtilizationPercent
        self.setHasQueueUtilizationPercent()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.content.qwilt_tech_content_reporting.tech.content.reporting.export_.status.status_oper_data_gen import StatusOperData"
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
            "namespace": "status", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "queueUtilizationPercent", 
            "yangName": "queue-utilization-percent", 
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


