


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





class OpDOperData (object):

    def __init__ (self):

        self.opValueD = 0
        self._myHasOpValueD=False
        self._myOpValueDRequested=False
        


    def copyFrom (self, other):

        self.opValueD=other.opValueD
        self._myHasOpValueD=other._myHasOpValueD
        self._myOpValueDRequested=other._myOpValueDRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isOpValueDRequested():
            self.opValueD=other.opValueD
            self._myHasOpValueD=other._myHasOpValueD
            self._myOpValueDRequested=other._myOpValueDRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasOpValueD():
            self.opValueD=other.opValueD
            self._myHasOpValueD=other._myHasOpValueD
            self._myOpValueDRequested=other._myOpValueDRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.opValueD=other.opValueD
        self._myHasOpValueD=other._myHasOpValueD
        


    def setAllNumericToZero (self):
        
        self.opValueD=0
        self.setHasOpValueD()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasOpValueD():
            if other.hasOpValueD():
                self.opValueD -= other.opValueD
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasOpValueD():
            if other.hasOpValueD():
                self.opValueD += other.opValueD
        
        
        pass


    # has...() methods

    def hasOpValueD (self):
        return self._myHasOpValueD




    # setHas...() methods

    def setHasOpValueD (self):
        self._myHasOpValueD=True




    # isRequested...() methods

    def isOpValueDRequested (self):
        return self._myOpValueDRequested




    # setRequested...() methods

    def setOpValueDRequested (self):
        self._myOpValueDRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myOpValueDRequested:
            x = "+OpValueD="
            if self._myHasOpValueD:
                leafStr = str(self.opValueD)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{OpDOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+OpValueD="
        if self._myHasOpValueD:
            leafStr = str(self.opValueD)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOpValueDRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{OpDOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setOpValueDRequested()
        
        


    def setOpValueD (self, opValueD):
        self.opValueD = opValueD
        self.setHasOpValueD()


"""
Extracted from the below data: 
{
    "node": {
        "className": "OpDOperData", 
        "namespace": "op_d", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_d.op_d_oper_data_gen import OpDOperData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_b", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_d", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "opValueD", 
            "yangName": "op-value-d", 
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


