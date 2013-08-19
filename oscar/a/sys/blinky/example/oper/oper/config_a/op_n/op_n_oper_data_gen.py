


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





class OpNOperData (object):

    def __init__ (self):

        self.valueOpN1 = ""
        self._myHasValueOpN1=False
        self._myValueOpN1Requested=False
        


    def copyFrom (self, other):

        self.valueOpN1=other.valueOpN1
        self._myHasValueOpN1=other._myHasValueOpN1
        self._myValueOpN1Requested=other._myValueOpN1Requested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isValueOpN1Requested():
            self.valueOpN1=other.valueOpN1
            self._myHasValueOpN1=other._myHasValueOpN1
            self._myValueOpN1Requested=other._myValueOpN1Requested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasValueOpN1():
            self.valueOpN1=other.valueOpN1
            self._myHasValueOpN1=other._myHasValueOpN1
            self._myValueOpN1Requested=other._myValueOpN1Requested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.valueOpN1=other.valueOpN1
        self._myHasValueOpN1=other._myHasValueOpN1
        


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

    def hasValueOpN1 (self):
        return self._myHasValueOpN1




    # setHas...() methods

    def setHasValueOpN1 (self):
        self._myHasValueOpN1=True




    # isRequested...() methods

    def isValueOpN1Requested (self):
        return self._myValueOpN1Requested




    # setRequested...() methods

    def setValueOpN1Requested (self):
        self._myValueOpN1Requested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myValueOpN1Requested:
            x = "+ValueOpN1="
            if self._myHasValueOpN1:
                leafStr = str(self.valueOpN1)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{OpNOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ValueOpN1="
        if self._myHasValueOpN1:
            leafStr = str(self.valueOpN1)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myValueOpN1Requested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{OpNOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setValueOpN1Requested()
        
        


    def setValueOpN1 (self, valueOpN1):
        self.valueOpN1 = valueOpN1
        self.setHasValueOpN1()


"""
Extracted from the below data: 
{
    "node": {
        "className": "OpNOperData", 
        "namespace": "op_n", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_n.op_n_oper_data_gen import OpNOperData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_n", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpN1", 
            "yangName": "value-op-n1", 
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


