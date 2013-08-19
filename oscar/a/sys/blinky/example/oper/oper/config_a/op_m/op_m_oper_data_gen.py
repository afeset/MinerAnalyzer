


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





class OpMOperData (object):

    def __init__ (self):

        self.valueOpM1 = ""
        self._myHasValueOpM1=False
        self._myValueOpM1Requested=False
        


    def copyFrom (self, other):

        self.valueOpM1=other.valueOpM1
        self._myHasValueOpM1=other._myHasValueOpM1
        self._myValueOpM1Requested=other._myValueOpM1Requested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isValueOpM1Requested():
            self.valueOpM1=other.valueOpM1
            self._myHasValueOpM1=other._myHasValueOpM1
            self._myValueOpM1Requested=other._myValueOpM1Requested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasValueOpM1():
            self.valueOpM1=other.valueOpM1
            self._myHasValueOpM1=other._myHasValueOpM1
            self._myValueOpM1Requested=other._myValueOpM1Requested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.valueOpM1=other.valueOpM1
        self._myHasValueOpM1=other._myHasValueOpM1
        


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

    def hasValueOpM1 (self):
        return self._myHasValueOpM1




    # setHas...() methods

    def setHasValueOpM1 (self):
        self._myHasValueOpM1=True




    # isRequested...() methods

    def isValueOpM1Requested (self):
        return self._myValueOpM1Requested




    # setRequested...() methods

    def setValueOpM1Requested (self):
        self._myValueOpM1Requested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myValueOpM1Requested:
            x = "+ValueOpM1="
            if self._myHasValueOpM1:
                leafStr = str(self.valueOpM1)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{OpMOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ValueOpM1="
        if self._myHasValueOpM1:
            leafStr = str(self.valueOpM1)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myValueOpM1Requested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{OpMOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setValueOpM1Requested()
        
        


    def setValueOpM1 (self, valueOpM1):
        self.valueOpM1 = valueOpM1
        self.setHasValueOpM1()


"""
Extracted from the below data: 
{
    "node": {
        "className": "OpMOperData", 
        "namespace": "op_m", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_m.op_m_oper_data_gen import OpMOperData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_m", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpM1", 
            "yangName": "value-op-m1", 
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


