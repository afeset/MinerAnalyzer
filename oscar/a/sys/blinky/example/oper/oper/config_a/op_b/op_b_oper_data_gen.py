


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


from a.sys.blinky.example.oper.oper.config_a.op_b.op_d.op_d_oper_data_gen import OpDOperData



class OpBOperData (object):

    def __init__ (self):

        self.opValueB = ""
        self._myHasOpValueB=False
        self._myOpValueBRequested=False
        

        self.myOpD = OpDOperData()
        self._myHasOpD=False
        self._myOpDRequested=False

    def copyFrom (self, other):

        self.opValueB=other.opValueB
        self._myHasOpValueB=other._myHasOpValueB
        self._myOpValueBRequested=other._myOpValueBRequested
        

        self.myOpD = OpDOperData()
        self.myOpD.copyFrom(other.OpD)
        self._myHasOpD=other._myHasOpD
        self._myOpDRequested=other._myOpDRequested

    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isOpValueBRequested():
            self.opValueB=other.opValueB
            self._myHasOpValueB=other._myHasOpValueB
            self._myOpValueBRequested=other._myOpValueBRequested
        

        if self.isOpDRequested():
            self.myOpD = OpDOperData()
            self.myOpD.copyRequestedFrom(other.OpD)
            self._myHasOpD=other._myHasOpD
            self._myOpDRequested=other._myOpDRequested

    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasOpValueB():
            self.opValueB=other.opValueB
            self._myHasOpValueB=other._myHasOpValueB
            self._myOpValueBRequested=other._myOpValueBRequested
        

        if other.hasOpD():
            self.myOpD = OpDOperData()
            self.myOpD.copySetFrom(other.OpD)
            self._myHasOpD=other._myHasOpD
            self._myOpDRequested=other._myOpDRequested

    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.opValueB=other.opValueB
        self._myHasOpValueB=other._myHasOpValueB
        

        self.myOpD = OpDOperData()
        self.myOpD.copyDataFrom(other.OpD)
        self._myHasOpD=other._myHasOpD

    def setAllNumericToZero (self):
        
        
        self.myOpD.setAllNumericToZero()
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        self.myOpD.subtractAllNumericHas(other, log)
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        self.myOpD.addAllNumericHas(other, log)
        pass


    # has...() methods

    def hasOpValueB (self):
        return self._myHasOpValueB



    def hasOpD (self):
        return self._myHasOpD


    # setHas...() methods

    def setHasOpValueB (self):
        self._myHasOpValueB=True



    def setHasOpD (self):
        self._myHasOpD=True


    # isRequested...() methods

    def isOpValueBRequested (self):
        return self._myOpValueBRequested



    def isOpDRequested (self):
        return self._myOpDRequested


    # setRequested...() methods

    def setOpValueBRequested (self):
        self._myOpValueBRequested=True



    def setOpDRequested (self):
        self._myOpDRequested=True


    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myOpValueBRequested:
            x = "+OpValueB="
            if self._myHasOpValueB:
                leafStr = str(self.opValueB)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        x=""
        if self._myOpDRequested:
            x = "+OpD="
            if self._myHasOpD:
                descendantStr = str(self.myOpD)
            else:
                descendantStr = "<UNSET>"
            items.append(x + descendantStr)

        return "{OpBOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+OpValueB="
        if self._myHasOpValueB:
            leafStr = str(self.opValueB)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOpValueBRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        x=""
        x = "+OpD="
        if self._myHasOpD:
            descendantStr = str(self.myOpD)
        else:
            descendantStr = "<UNSET>"
            requestedStr = ''
        if includeRequested:
            if self._myOpDRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + descendantStr)

        return "{OpBOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setOpValueBRequested()
        
        self.setOpDRequested()
        


    def setOpValueB (self, opValueB):
        self.opValueB = opValueB
        self.setHasOpValueB()


"""
Extracted from the below data: 
{
    "node": {
        "className": "OpBOperData", 
        "namespace": "op_b", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_b_oper_data_gen import OpBOperData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": false
        }, 
        {
            "namespace": "op_b", 
            "isCurrent": true
        }
    ], 
    "descendants": [
        {
            "className": "OpDOperData", 
            "memberName": "opD", 
            "importStatement": "from a.sys.blinky.example.oper.oper.config_a.op_b.op_d.op_d_oper_data_gen import OpDOperData"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "opValueB", 
            "yangName": "op-value-b", 
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


