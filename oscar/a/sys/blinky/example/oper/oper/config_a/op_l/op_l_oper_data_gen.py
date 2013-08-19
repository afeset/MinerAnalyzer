


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





class OpLOperData (object):

    def __init__ (self):

        self.valueOpL1 = ""
        self._myHasValueOpL1=False
        self._myValueOpL1Requested=False
        
        self.valueOpL2 = ""
        self._myHasValueOpL2=False
        self._myValueOpL2Requested=False
        


    def copyFrom (self, other):

        self.valueOpL1=other.valueOpL1
        self._myHasValueOpL1=other._myHasValueOpL1
        self._myValueOpL1Requested=other._myValueOpL1Requested
        
        self.valueOpL2=other.valueOpL2
        self._myHasValueOpL2=other._myHasValueOpL2
        self._myValueOpL2Requested=other._myValueOpL2Requested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isValueOpL1Requested():
            self.valueOpL1=other.valueOpL1
            self._myHasValueOpL1=other._myHasValueOpL1
            self._myValueOpL1Requested=other._myValueOpL1Requested
        
        if self.isValueOpL2Requested():
            self.valueOpL2=other.valueOpL2
            self._myHasValueOpL2=other._myHasValueOpL2
            self._myValueOpL2Requested=other._myValueOpL2Requested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasValueOpL1():
            self.valueOpL1=other.valueOpL1
            self._myHasValueOpL1=other._myHasValueOpL1
            self._myValueOpL1Requested=other._myValueOpL1Requested
        
        if other.hasValueOpL2():
            self.valueOpL2=other.valueOpL2
            self._myHasValueOpL2=other._myHasValueOpL2
            self._myValueOpL2Requested=other._myValueOpL2Requested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.valueOpL1=other.valueOpL1
        self._myHasValueOpL1=other._myHasValueOpL1
        
        self.valueOpL2=other.valueOpL2
        self._myHasValueOpL2=other._myHasValueOpL2
        


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

    def hasValueOpL1 (self):
        return self._myHasValueOpL1

    def hasValueOpL2 (self):
        return self._myHasValueOpL2




    # setHas...() methods

    def setHasValueOpL1 (self):
        self._myHasValueOpL1=True

    def setHasValueOpL2 (self):
        self._myHasValueOpL2=True




    # isRequested...() methods

    def isValueOpL1Requested (self):
        return self._myValueOpL1Requested

    def isValueOpL2Requested (self):
        return self._myValueOpL2Requested




    # setRequested...() methods

    def setValueOpL1Requested (self):
        self._myValueOpL1Requested=True

    def setValueOpL2Requested (self):
        self._myValueOpL2Requested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myValueOpL1Requested:
            x = "+ValueOpL1="
            if self._myHasValueOpL1:
                leafStr = str(self.valueOpL1)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myValueOpL2Requested:
            x = "+ValueOpL2="
            if self._myHasValueOpL2:
                leafStr = str(self.valueOpL2)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{OpLOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ValueOpL1="
        if self._myHasValueOpL1:
            leafStr = str(self.valueOpL1)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myValueOpL1Requested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ValueOpL2="
        if self._myHasValueOpL2:
            leafStr = str(self.valueOpL2)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myValueOpL2Requested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{OpLOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setValueOpL1Requested()
        self.setValueOpL2Requested()
        
        


    def setValueOpL1 (self, valueOpL1):
        self.valueOpL1 = valueOpL1
        self.setHasValueOpL1()

    def setValueOpL2 (self, valueOpL2):
        self.valueOpL2 = valueOpL2
        self.setHasValueOpL2()


"""
Extracted from the below data: 
{
    "node": {
        "className": "OpLOperData", 
        "namespace": "op_l", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_l.op_l_oper_data_gen import OpLOperData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_l", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpL1", 
            "yangName": "value-op-l1", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpL2", 
            "yangName": "value-op-l2", 
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
            "oper", 
            "oper"
        ]
    }, 
    "createTime": "2013"
}
"""


