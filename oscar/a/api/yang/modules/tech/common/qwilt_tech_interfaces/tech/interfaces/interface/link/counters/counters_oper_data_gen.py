


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

        self.resultDown = 0
        self._myHasResultDown=False
        self._myResultDownRequested=False
        
        self.resultUnknown = 0
        self._myHasResultUnknown=False
        self._myResultUnknownRequested=False
        
        self.tests = 0
        self._myHasTests=False
        self._myTestsRequested=False
        
        self.resultUp = 0
        self._myHasResultUp=False
        self._myResultUpRequested=False
        


    def copyFrom (self, other):

        self.resultDown=other.resultDown
        self._myHasResultDown=other._myHasResultDown
        self._myResultDownRequested=other._myResultDownRequested
        
        self.resultUnknown=other.resultUnknown
        self._myHasResultUnknown=other._myHasResultUnknown
        self._myResultUnknownRequested=other._myResultUnknownRequested
        
        self.tests=other.tests
        self._myHasTests=other._myHasTests
        self._myTestsRequested=other._myTestsRequested
        
        self.resultUp=other.resultUp
        self._myHasResultUp=other._myHasResultUp
        self._myResultUpRequested=other._myResultUpRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isResultDownRequested():
            self.resultDown=other.resultDown
            self._myHasResultDown=other._myHasResultDown
            self._myResultDownRequested=other._myResultDownRequested
        
        if self.isResultUnknownRequested():
            self.resultUnknown=other.resultUnknown
            self._myHasResultUnknown=other._myHasResultUnknown
            self._myResultUnknownRequested=other._myResultUnknownRequested
        
        if self.isTestsRequested():
            self.tests=other.tests
            self._myHasTests=other._myHasTests
            self._myTestsRequested=other._myTestsRequested
        
        if self.isResultUpRequested():
            self.resultUp=other.resultUp
            self._myHasResultUp=other._myHasResultUp
            self._myResultUpRequested=other._myResultUpRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasResultDown():
            self.resultDown=other.resultDown
            self._myHasResultDown=other._myHasResultDown
            self._myResultDownRequested=other._myResultDownRequested
        
        if other.hasResultUnknown():
            self.resultUnknown=other.resultUnknown
            self._myHasResultUnknown=other._myHasResultUnknown
            self._myResultUnknownRequested=other._myResultUnknownRequested
        
        if other.hasTests():
            self.tests=other.tests
            self._myHasTests=other._myHasTests
            self._myTestsRequested=other._myTestsRequested
        
        if other.hasResultUp():
            self.resultUp=other.resultUp
            self._myHasResultUp=other._myHasResultUp
            self._myResultUpRequested=other._myResultUpRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.resultDown=other.resultDown
        self._myHasResultDown=other._myHasResultDown
        
        self.resultUnknown=other.resultUnknown
        self._myHasResultUnknown=other._myHasResultUnknown
        
        self.tests=other.tests
        self._myHasTests=other._myHasTests
        
        self.resultUp=other.resultUp
        self._myHasResultUp=other._myHasResultUp
        


    def setAllNumericToZero (self):
        
        self.resultDown=0
        self.setHasResultDown()
        self.resultUnknown=0
        self.setHasResultUnknown()
        self.tests=0
        self.setHasTests()
        self.resultUp=0
        self.setHasResultUp()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasResultDown():
            if other.hasResultDown():
                self.resultDown -= other.resultDown
        
        if self.hasResultUnknown():
            if other.hasResultUnknown():
                self.resultUnknown -= other.resultUnknown
        
        if self.hasTests():
            if other.hasTests():
                self.tests -= other.tests
        
        if self.hasResultUp():
            if other.hasResultUp():
                self.resultUp -= other.resultUp
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasResultDown():
            if other.hasResultDown():
                self.resultDown += other.resultDown
        
        if self.hasResultUnknown():
            if other.hasResultUnknown():
                self.resultUnknown += other.resultUnknown
        
        if self.hasTests():
            if other.hasTests():
                self.tests += other.tests
        
        if self.hasResultUp():
            if other.hasResultUp():
                self.resultUp += other.resultUp
        
        
        pass


    # has...() methods

    def hasResultDown (self):
        return self._myHasResultDown

    def hasResultUnknown (self):
        return self._myHasResultUnknown

    def hasTests (self):
        return self._myHasTests

    def hasResultUp (self):
        return self._myHasResultUp




    # setHas...() methods

    def setHasResultDown (self):
        self._myHasResultDown=True

    def setHasResultUnknown (self):
        self._myHasResultUnknown=True

    def setHasTests (self):
        self._myHasTests=True

    def setHasResultUp (self):
        self._myHasResultUp=True




    # isRequested...() methods

    def isResultDownRequested (self):
        return self._myResultDownRequested

    def isResultUnknownRequested (self):
        return self._myResultUnknownRequested

    def isTestsRequested (self):
        return self._myTestsRequested

    def isResultUpRequested (self):
        return self._myResultUpRequested




    # setRequested...() methods

    def setResultDownRequested (self):
        self._myResultDownRequested=True

    def setResultUnknownRequested (self):
        self._myResultUnknownRequested=True

    def setTestsRequested (self):
        self._myTestsRequested=True

    def setResultUpRequested (self):
        self._myResultUpRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myResultDownRequested:
            x = "+ResultDown="
            if self._myHasResultDown:
                leafStr = str(self.resultDown)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myResultUnknownRequested:
            x = "+ResultUnknown="
            if self._myHasResultUnknown:
                leafStr = str(self.resultUnknown)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myTestsRequested:
            x = "+Tests="
            if self._myHasTests:
                leafStr = str(self.tests)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myResultUpRequested:
            x = "+ResultUp="
            if self._myHasResultUp:
                leafStr = str(self.resultUp)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{CountersOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ResultDown="
        if self._myHasResultDown:
            leafStr = str(self.resultDown)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myResultDownRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ResultUnknown="
        if self._myHasResultUnknown:
            leafStr = str(self.resultUnknown)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myResultUnknownRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Tests="
        if self._myHasTests:
            leafStr = str(self.tests)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTestsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ResultUp="
        if self._myHasResultUp:
            leafStr = str(self.resultUp)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myResultUpRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setResultDownRequested()
        self.setResultUnknownRequested()
        self.setTestsRequested()
        self.setResultUpRequested()
        
        


    def setResultDown (self, resultDown):
        self.resultDown = resultDown
        self.setHasResultDown()

    def setResultUnknown (self, resultUnknown):
        self.resultUnknown = resultUnknown
        self.setHasResultUnknown()

    def setTests (self, tests):
        self.tests = tests
        self.setHasTests()

    def setResultUp (self, resultUp):
        self.resultUp = resultUp
        self.setHasResultUp()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.link.counters.counters_oper_data_gen import CountersOperData"
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
            "namespace": "link", 
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
            "memberName": "resultDown", 
            "yangName": "result-down", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "resultUnknown", 
            "yangName": "result-unknown", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "tests", 
            "yangName": "tests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "resultUp", 
            "yangName": "result-up", 
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


