


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





class OpYOperData (object):

    def __init__ (self):

        self.valueOpY1 = ""
        self._myHasValueOpY1=False
        self._myValueOpY1Requested=False
        


    def copyFrom (self, other):

        self.valueOpY1=other.valueOpY1
        self._myHasValueOpY1=other._myHasValueOpY1
        self._myValueOpY1Requested=other._myValueOpY1Requested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isValueOpY1Requested():
            self.valueOpY1=other.valueOpY1
            self._myHasValueOpY1=other._myHasValueOpY1
            self._myValueOpY1Requested=other._myValueOpY1Requested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasValueOpY1():
            self.valueOpY1=other.valueOpY1
            self._myHasValueOpY1=other._myHasValueOpY1
            self._myValueOpY1Requested=other._myValueOpY1Requested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.valueOpY1=other.valueOpY1
        self._myHasValueOpY1=other._myHasValueOpY1
        


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

    def hasValueOpY1 (self):
        return self._myHasValueOpY1




    # setHas...() methods

    def setHasValueOpY1 (self):
        self._myHasValueOpY1=True




    # isRequested...() methods

    def isValueOpY1Requested (self):
        return self._myValueOpY1Requested




    # setRequested...() methods

    def setValueOpY1Requested (self):
        self._myValueOpY1Requested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myValueOpY1Requested:
            x = "+ValueOpY1="
            if self._myHasValueOpY1:
                leafStr = str(self.valueOpY1)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{OpYOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ValueOpY1="
        if self._myHasValueOpY1:
            leafStr = str(self.valueOpY1)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myValueOpY1Requested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{OpYOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setValueOpY1Requested()
        
        


    def setValueOpY1 (self, valueOpY1):
        self.valueOpY1 = valueOpY1
        self.setHasValueOpY1()


"""
Extracted from the below data: 
{
    "node": {
        "className": "OpYOperData", 
        "namespace": "op_y", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.op_y_oper_data_gen import OpYOperData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_v", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_y", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpY1", 
            "yangName": "value-op-y1", 
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


