


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





class OpROperData (object):

    def __init__ (self):

        self.opValueR = ""
        self._myHasOpValueR=False
        self._myOpValueRRequested=False
        


    def copyFrom (self, other):

        self.opValueR=other.opValueR
        self._myHasOpValueR=other._myHasOpValueR
        self._myOpValueRRequested=other._myOpValueRRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isOpValueRRequested():
            self.opValueR=other.opValueR
            self._myHasOpValueR=other._myHasOpValueR
            self._myOpValueRRequested=other._myOpValueRRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasOpValueR():
            self.opValueR=other.opValueR
            self._myHasOpValueR=other._myHasOpValueR
            self._myOpValueRRequested=other._myOpValueRRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.opValueR=other.opValueR
        self._myHasOpValueR=other._myHasOpValueR
        


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

    def hasOpValueR (self):
        return self._myHasOpValueR




    # setHas...() methods

    def setHasOpValueR (self):
        self._myHasOpValueR=True




    # isRequested...() methods

    def isOpValueRRequested (self):
        return self._myOpValueRRequested




    # setRequested...() methods

    def setOpValueRRequested (self):
        self._myOpValueRRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myOpValueRRequested:
            x = "+OpValueR="
            if self._myHasOpValueR:
                leafStr = str(self.opValueR)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{OpROperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+OpValueR="
        if self._myHasOpValueR:
            leafStr = str(self.opValueR)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOpValueRRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{OpROperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setOpValueRRequested()
        
        


    def setOpValueR (self, opValueR):
        self.opValueR = opValueR
        self.setHasOpValueR()


"""
Extracted from the below data: 
{
    "node": {
        "className": "OpROperData", 
        "namespace": "op_r", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_p.op_r.op_r_oper_data_gen import OpROperData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "config_p", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_r", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "opValueR", 
            "yangName": "op-value-r", 
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


