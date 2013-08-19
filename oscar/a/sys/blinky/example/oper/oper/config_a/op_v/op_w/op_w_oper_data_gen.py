


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





class OpWOperData (object):

    def __init__ (self):

        self.opWValue = ""
        self._myHasOpWValue=False
        self._myOpWValueRequested=False
        


    def copyFrom (self, other):

        self.opWValue=other.opWValue
        self._myHasOpWValue=other._myHasOpWValue
        self._myOpWValueRequested=other._myOpWValueRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isOpWValueRequested():
            self.opWValue=other.opWValue
            self._myHasOpWValue=other._myHasOpWValue
            self._myOpWValueRequested=other._myOpWValueRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasOpWValue():
            self.opWValue=other.opWValue
            self._myHasOpWValue=other._myHasOpWValue
            self._myOpWValueRequested=other._myOpWValueRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.opWValue=other.opWValue
        self._myHasOpWValue=other._myHasOpWValue
        


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

    def hasOpWValue (self):
        return self._myHasOpWValue




    # setHas...() methods

    def setHasOpWValue (self):
        self._myHasOpWValue=True




    # isRequested...() methods

    def isOpWValueRequested (self):
        return self._myOpWValueRequested




    # setRequested...() methods

    def setOpWValueRequested (self):
        self._myOpWValueRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myOpWValueRequested:
            x = "+OpWValue="
            if self._myHasOpWValue:
                leafStr = str(self.opWValue)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{OpWOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+OpWValue="
        if self._myHasOpWValue:
            leafStr = str(self.opWValue)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOpWValueRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{OpWOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setOpWValueRequested()
        
        


    def setOpWValue (self, opWValue):
        self.opWValue = opWValue
        self.setHasOpWValue()


"""
Extracted from the below data: 
{
    "node": {
        "className": "OpWOperData", 
        "namespace": "op_w", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_v.op_w.op_w_oper_data_gen import OpWOperData"
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
            "namespace": "op_w", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "opWValue", 
            "yangName": "op-w-value", 
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


