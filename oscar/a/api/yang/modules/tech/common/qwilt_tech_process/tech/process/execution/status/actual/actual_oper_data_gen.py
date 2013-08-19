


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





class ActualOperData (object):

    def __init__ (self):

        self.priority = ""
        self._myHasPriority=False
        self._myPriorityRequested=False
        
        self.affinity = ""
        self._myHasAffinity=False
        self._myAffinityRequested=False
        
        self.commandLine = ""
        self._myHasCommandLine=False
        self._myCommandLineRequested=False
        


    def copyFrom (self, other):

        self.priority=other.priority
        self._myHasPriority=other._myHasPriority
        self._myPriorityRequested=other._myPriorityRequested
        
        self.affinity=other.affinity
        self._myHasAffinity=other._myHasAffinity
        self._myAffinityRequested=other._myAffinityRequested
        
        self.commandLine=other.commandLine
        self._myHasCommandLine=other._myHasCommandLine
        self._myCommandLineRequested=other._myCommandLineRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isPriorityRequested():
            self.priority=other.priority
            self._myHasPriority=other._myHasPriority
            self._myPriorityRequested=other._myPriorityRequested
        
        if self.isAffinityRequested():
            self.affinity=other.affinity
            self._myHasAffinity=other._myHasAffinity
            self._myAffinityRequested=other._myAffinityRequested
        
        if self.isCommandLineRequested():
            self.commandLine=other.commandLine
            self._myHasCommandLine=other._myHasCommandLine
            self._myCommandLineRequested=other._myCommandLineRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasPriority():
            self.priority=other.priority
            self._myHasPriority=other._myHasPriority
            self._myPriorityRequested=other._myPriorityRequested
        
        if other.hasAffinity():
            self.affinity=other.affinity
            self._myHasAffinity=other._myHasAffinity
            self._myAffinityRequested=other._myAffinityRequested
        
        if other.hasCommandLine():
            self.commandLine=other.commandLine
            self._myHasCommandLine=other._myHasCommandLine
            self._myCommandLineRequested=other._myCommandLineRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.priority=other.priority
        self._myHasPriority=other._myHasPriority
        
        self.affinity=other.affinity
        self._myHasAffinity=other._myHasAffinity
        
        self.commandLine=other.commandLine
        self._myHasCommandLine=other._myHasCommandLine
        


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

    def hasPriority (self):
        return self._myHasPriority

    def hasAffinity (self):
        return self._myHasAffinity

    def hasCommandLine (self):
        return self._myHasCommandLine




    # setHas...() methods

    def setHasPriority (self):
        self._myHasPriority=True

    def setHasAffinity (self):
        self._myHasAffinity=True

    def setHasCommandLine (self):
        self._myHasCommandLine=True




    # isRequested...() methods

    def isPriorityRequested (self):
        return self._myPriorityRequested

    def isAffinityRequested (self):
        return self._myAffinityRequested

    def isCommandLineRequested (self):
        return self._myCommandLineRequested




    # setRequested...() methods

    def setPriorityRequested (self):
        self._myPriorityRequested=True

    def setAffinityRequested (self):
        self._myAffinityRequested=True

    def setCommandLineRequested (self):
        self._myCommandLineRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myPriorityRequested:
            x = "+Priority="
            if self._myHasPriority:
                leafStr = str(self.priority)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myAffinityRequested:
            x = "+Affinity="
            if self._myHasAffinity:
                leafStr = str(self.affinity)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myCommandLineRequested:
            x = "+CommandLine="
            if self._myHasCommandLine:
                leafStr = str(self.commandLine)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{ActualOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+Priority="
        if self._myHasPriority:
            leafStr = str(self.priority)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myPriorityRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Affinity="
        if self._myHasAffinity:
            leafStr = str(self.affinity)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myAffinityRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+CommandLine="
        if self._myHasCommandLine:
            leafStr = str(self.commandLine)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCommandLineRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{ActualOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setPriorityRequested()
        self.setAffinityRequested()
        self.setCommandLineRequested()
        
        


    def setPriority (self, priority):
        self.priority = priority
        self.setHasPriority()

    def setAffinity (self, affinity):
        self.affinity = affinity
        self.setHasAffinity()

    def setCommandLine (self, commandLine):
        self.commandLine = commandLine
        self.setHasCommandLine()


"""
Extracted from the below data: 
{
    "node": {
        "className": "ActualOperData", 
        "namespace": "actual", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.actual.actual_oper_data_gen import ActualOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "process", 
            "isCurrent": false
        }, 
        {
            "namespace": "execution", 
            "isCurrent": false
        }, 
        {
            "namespace": "status", 
            "isCurrent": false
        }, 
        {
            "namespace": "actual", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "priority", 
            "yangName": "priority", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "affinity", 
            "yangName": "affinity", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "commandLine", 
            "yangName": "command-line", 
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
            "qwilt_tech_process"
        ]
    }, 
    "createTime": "2013"
}
"""


