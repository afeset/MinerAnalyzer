


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





class ConfigAOperData (object):

    def __init__ (self):

        self.opZ = ""
        self._myHasOpZ=False
        self._myOpZRequested=False
        
        self.opY = ""
        self._myHasOpY=False
        self._myOpYRequested=False
        


    def copyFrom (self, other):

        self.opZ=other.opZ
        self._myHasOpZ=other._myHasOpZ
        self._myOpZRequested=other._myOpZRequested
        
        self.opY=other.opY
        self._myHasOpY=other._myHasOpY
        self._myOpYRequested=other._myOpYRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isOpZRequested():
            self.opZ=other.opZ
            self._myHasOpZ=other._myHasOpZ
            self._myOpZRequested=other._myOpZRequested
        
        if self.isOpYRequested():
            self.opY=other.opY
            self._myHasOpY=other._myHasOpY
            self._myOpYRequested=other._myOpYRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasOpZ():
            self.opZ=other.opZ
            self._myHasOpZ=other._myHasOpZ
            self._myOpZRequested=other._myOpZRequested
        
        if other.hasOpY():
            self.opY=other.opY
            self._myHasOpY=other._myHasOpY
            self._myOpYRequested=other._myOpYRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.opZ=other.opZ
        self._myHasOpZ=other._myHasOpZ
        
        self.opY=other.opY
        self._myHasOpY=other._myHasOpY
        


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

    def hasOpZ (self):
        return self._myHasOpZ

    def hasOpY (self):
        return self._myHasOpY




    # setHas...() methods

    def setHasOpZ (self):
        self._myHasOpZ=True

    def setHasOpY (self):
        self._myHasOpY=True




    # isRequested...() methods

    def isOpZRequested (self):
        return self._myOpZRequested

    def isOpYRequested (self):
        return self._myOpYRequested




    # setRequested...() methods

    def setOpZRequested (self):
        self._myOpZRequested=True

    def setOpYRequested (self):
        self._myOpYRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myOpZRequested:
            x = "+OpZ="
            if self._myHasOpZ:
                leafStr = str(self.opZ)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOpYRequested:
            x = "+OpY="
            if self._myHasOpY:
                leafStr = str(self.opY)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{ConfigAOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+OpZ="
        if self._myHasOpZ:
            leafStr = str(self.opZ)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOpZRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OpY="
        if self._myHasOpY:
            leafStr = str(self.opY)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOpYRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{ConfigAOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setOpZRequested()
        self.setOpYRequested()
        
        


    def setOpZ (self, opZ):
        self.opZ = opZ
        self.setHasOpZ()

    def setOpY (self, opY):
        self.opY = opY
        self.setHasOpY()


"""
Extracted from the below data: 
{
    "node": {
        "className": "ConfigAOperData", 
        "namespace": "config_a", 
        "importStatement": "from a.sys.blinky.example.oper.oper.config_a.config_a_oper_data_gen import ConfigAOperData"
    }, 
    "ancestors": [
        {
            "namespace": "config_a", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "opZ", 
            "yangName": "op-z", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "opY", 
            "yangName": "op-y", 
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


