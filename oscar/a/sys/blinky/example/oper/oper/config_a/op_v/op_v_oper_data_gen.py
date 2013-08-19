


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


from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.op_y_oper_data_gen import OpYOperData



class OpVOperData (object):

    def __init__ (self):

        self.valueOpV1 = ""
        self._myHasValueOpV1=False
        self._myValueOpV1Requested=False
        

        self.myOpY = OpYOperData()
        self._myHasOpY=False
        self._myOpYRequested=False

    def copyFrom (self, other):

        self.valueOpV1=other.valueOpV1
        self._myHasValueOpV1=other._myHasValueOpV1
        self._myValueOpV1Requested=other._myValueOpV1Requested
        

        self.myOpY = OpYOperData()
        self.myOpY.copyFrom(other.OpY)
        self._myHasOpY=other._myHasOpY
        self._myOpYRequested=other._myOpYRequested

    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isValueOpV1Requested():
            self.valueOpV1=other.valueOpV1
            self._myHasValueOpV1=other._myHasValueOpV1
            self._myValueOpV1Requested=other._myValueOpV1Requested
        

        if self.isOpYRequested():
            self.myOpY = OpYOperData()
            self.myOpY.copyRequestedFrom(other.OpY)
            self._myHasOpY=other._myHasOpY
            self._myOpYRequested=other._myOpYRequested

    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasValueOpV1():
            self.valueOpV1=other.valueOpV1
            self._myHasValueOpV1=other._myHasValueOpV1
            self._myValueOpV1Requested=other._myValueOpV1Requested
        

        if other.hasOpY():
            self.myOpY = OpYOperData()
            self.myOpY.copySetFrom(other.OpY)
            self._myHasOpY=other._myHasOpY
            self._myOpYRequested=other._myOpYRequested

    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.valueOpV1=other.valueOpV1
        self._myHasValueOpV1=other._myHasValueOpV1
        

        self.myOpY = OpYOperData()
        self.myOpY.copyDataFrom(other.OpY)
        self._myHasOpY=other._myHasOpY

    def setAllNumericToZero (self):
        
        
        self.myOpY.setAllNumericToZero()
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        self.myOpY.subtractAllNumericHas(other, log)
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        self.myOpY.addAllNumericHas(other, log)
        pass


    # has...() methods

    def hasValueOpV1 (self):
        return self._myHasValueOpV1



    def hasOpY (self):
        return self._myHasOpY


    # setHas...() methods

    def setHasValueOpV1 (self):
        self._myHasValueOpV1=True



    def setHasOpY (self):
        self._myHasOpY=True


    # isRequested...() methods

    def isValueOpV1Requested (self):
        return self._myValueOpV1Requested



    def isOpYRequested (self):
        return self._myOpYRequested


    # setRequested...() methods

    def setValueOpV1Requested (self):
        self._myValueOpV1Requested=True



    def setOpYRequested (self):
        self._myOpYRequested=True


    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myValueOpV1Requested:
            x = "+ValueOpV1="
            if self._myHasValueOpV1:
                leafStr = str(self.valueOpV1)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        x=""
        if self._myOpYRequested:
            x = "+OpY="
            if self._myHasOpY:
                descendantStr = str(self.myOpY)
            else:
                descendantStr = "<UNSET>"
            items.append(x + descendantStr)

        return "{OpVOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+ValueOpV1="
        if self._myHasValueOpV1:
            leafStr = str(self.valueOpV1)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myValueOpV1Requested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        x=""
        x = "+OpY="
        if self._myHasOpY:
            descendantStr = str(self.myOpY)
        else:
            descendantStr = "<UNSET>"
            requestedStr = ''
        if includeRequested:
            if self._myOpYRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + descendantStr)

        return "{OpVOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setValueOpV1Requested()
        
        self.setOpYRequested()
        


    def setValueOpV1 (self, valueOpV1):
        self.valueOpV1 = valueOpV1
        self.setHasValueOpV1()


"""
Extracted from the below data: 
{
    "node": {
        "className": "OpVOperData", 
        "namespace": "op_v", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_v_oper_data_gen import OpVOperData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_v", 
            "isCurrent": true
        }
    ], 
    "descendants": [
        {
            "className": "OpYOperData", 
            "memberName": "opY", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_y.op_y_oper_data_gen import OpYOperData"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "valueOpV1", 
            "yangName": "value-op-v1", 
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


