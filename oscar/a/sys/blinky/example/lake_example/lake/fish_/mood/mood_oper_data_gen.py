


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





class MoodOperData (object):

    def __init__ (self):

        self.current = ""
        self._myHasCurrent=False
        self._myCurrentRequested=False
        


    def copyFrom (self, other):

        self.current=other.current
        self._myHasCurrent=other._myHasCurrent
        self._myCurrentRequested=other._myCurrentRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isCurrentRequested():
            self.current=other.current
            self._myHasCurrent=other._myHasCurrent
            self._myCurrentRequested=other._myCurrentRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasCurrent():
            self.current=other.current
            self._myHasCurrent=other._myHasCurrent
            self._myCurrentRequested=other._myCurrentRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.current=other.current
        self._myHasCurrent=other._myHasCurrent
        


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

    def hasCurrent (self):
        return self._myHasCurrent




    # setHas...() methods

    def setHasCurrent (self):
        self._myHasCurrent=True




    # isRequested...() methods

    def isCurrentRequested (self):
        return self._myCurrentRequested




    # setRequested...() methods

    def setCurrentRequested (self):
        self._myCurrentRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myCurrentRequested:
            x = "+Current="
            if self._myHasCurrent:
                leafStr = str(self.current)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{MoodOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+Current="
        if self._myHasCurrent:
            leafStr = str(self.current)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myCurrentRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{MoodOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setCurrentRequested()
        
        


    def setCurrent (self, current):
        self.current = current
        self.setHasCurrent()


"""
Extracted from the below data: 
{
    "node": {
        "className": "MoodOperData", 
        "namespace": "mood", 
        "importStatement": "from a.sys.blinky.example.lake_example.lake.fish_.mood.mood_oper_data_gen import MoodOperData"
    }, 
    "ancestors": [
        {
            "namespace": "lake", 
            "isCurrent": false
        }, 
        {
            "namespace": "fish_", 
            "isCurrent": false
        }, 
        {
            "namespace": "mood", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "current", 
            "yangName": "current", 
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
            "sys", 
            "blinky", 
            "example", 
            "lake_example"
        ]
    }, 
    "createTime": "2013"
}
"""


