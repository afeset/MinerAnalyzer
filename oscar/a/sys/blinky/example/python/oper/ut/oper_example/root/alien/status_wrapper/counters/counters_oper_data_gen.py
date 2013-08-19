


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

        self.strTest = ""
        self._myHasStrTest=False
        self._myStrTestRequested=False
        
        self.mood = 0
        self._myHasMood=False
        self._myMoodRequested=False
        


    def copyFrom (self, other):

        self.strTest=other.strTest
        self._myHasStrTest=other._myHasStrTest
        self._myStrTestRequested=other._myStrTestRequested
        
        self.mood=other.mood
        self._myHasMood=other._myHasMood
        self._myMoodRequested=other._myMoodRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isStrTestRequested():
            self.strTest=other.strTest
            self._myHasStrTest=other._myHasStrTest
            self._myStrTestRequested=other._myStrTestRequested
        
        if self.isMoodRequested():
            self.mood=other.mood
            self._myHasMood=other._myHasMood
            self._myMoodRequested=other._myMoodRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasStrTest():
            self.strTest=other.strTest
            self._myHasStrTest=other._myHasStrTest
            self._myStrTestRequested=other._myStrTestRequested
        
        if other.hasMood():
            self.mood=other.mood
            self._myHasMood=other._myHasMood
            self._myMoodRequested=other._myMoodRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.strTest=other.strTest
        self._myHasStrTest=other._myHasStrTest
        
        self.mood=other.mood
        self._myHasMood=other._myHasMood
        


    def setAllNumericToZero (self):
        
        self.mood=0
        self.setHasMood()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasMood():
            if other.hasMood():
                self.mood -= other.mood
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasMood():
            if other.hasMood():
                self.mood += other.mood
        
        
        pass


    # has...() methods

    def hasStrTest (self):
        return self._myHasStrTest

    def hasMood (self):
        return self._myHasMood




    # setHas...() methods

    def setHasStrTest (self):
        self._myHasStrTest=True

    def setHasMood (self):
        self._myHasMood=True




    # isRequested...() methods

    def isStrTestRequested (self):
        return self._myStrTestRequested

    def isMoodRequested (self):
        return self._myMoodRequested




    # setRequested...() methods

    def setStrTestRequested (self):
        self._myStrTestRequested=True

    def setMoodRequested (self):
        self._myMoodRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myStrTestRequested:
            x = "+StrTest="
            if self._myHasStrTest:
                leafStr = str(self.strTest)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myMoodRequested:
            x = "+Mood="
            if self._myHasMood:
                leafStr = str(self.mood)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{CountersOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+StrTest="
        if self._myHasStrTest:
            leafStr = str(self.strTest)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myStrTestRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Mood="
        if self._myHasMood:
            leafStr = str(self.mood)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myMoodRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setStrTestRequested()
        self.setMoodRequested()
        
        


    def setStrTest (self, strTest):
        self.strTest = strTest
        self.setHasStrTest()

    def setMood (self, mood):
        self.mood = mood
        self.setHasMood()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.sys.blinky.example.python.oper.ut.oper_example.root.alien.status_wrapper.counters.counters_oper_data_gen import CountersOperData"
    }, 
    "ancestors": [
        {
            "namespace": "root", 
            "isCurrent": false
        }, 
        {
            "namespace": "alien", 
            "isCurrent": false
        }, 
        {
            "namespace": "status_wrapper", 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "strTest", 
            "yangName": "str-test", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "mood", 
            "yangName": "mood", 
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
            "python", 
            "oper", 
            "ut", 
            "oper_example"
        ]
    }, 
    "createTime": "2013"
}
"""


