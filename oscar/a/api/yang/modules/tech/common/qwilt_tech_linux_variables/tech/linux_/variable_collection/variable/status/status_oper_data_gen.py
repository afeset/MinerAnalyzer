


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





class StatusOperData (object):

    def __init__ (self):

        self.initialValue = ""
        self._myHasInitialValue=False
        self._myInitialValueRequested=False
        
        self.actualValue = ""
        self._myHasActualValue=False
        self._myActualValueRequested=False
        


    def copyFrom (self, other):

        self.initialValue=other.initialValue
        self._myHasInitialValue=other._myHasInitialValue
        self._myInitialValueRequested=other._myInitialValueRequested
        
        self.actualValue=other.actualValue
        self._myHasActualValue=other._myHasActualValue
        self._myActualValueRequested=other._myActualValueRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isInitialValueRequested():
            self.initialValue=other.initialValue
            self._myHasInitialValue=other._myHasInitialValue
            self._myInitialValueRequested=other._myInitialValueRequested
        
        if self.isActualValueRequested():
            self.actualValue=other.actualValue
            self._myHasActualValue=other._myHasActualValue
            self._myActualValueRequested=other._myActualValueRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasInitialValue():
            self.initialValue=other.initialValue
            self._myHasInitialValue=other._myHasInitialValue
            self._myInitialValueRequested=other._myInitialValueRequested
        
        if other.hasActualValue():
            self.actualValue=other.actualValue
            self._myHasActualValue=other._myHasActualValue
            self._myActualValueRequested=other._myActualValueRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.initialValue=other.initialValue
        self._myHasInitialValue=other._myHasInitialValue
        
        self.actualValue=other.actualValue
        self._myHasActualValue=other._myHasActualValue
        


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

    def hasInitialValue (self):
        return self._myHasInitialValue

    def hasActualValue (self):
        return self._myHasActualValue




    # setHas...() methods

    def setHasInitialValue (self):
        self._myHasInitialValue=True

    def setHasActualValue (self):
        self._myHasActualValue=True




    # isRequested...() methods

    def isInitialValueRequested (self):
        return self._myInitialValueRequested

    def isActualValueRequested (self):
        return self._myActualValueRequested




    # setRequested...() methods

    def setInitialValueRequested (self):
        self._myInitialValueRequested=True

    def setActualValueRequested (self):
        self._myActualValueRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myInitialValueRequested:
            x = "+InitialValue="
            if self._myHasInitialValue:
                leafStr = str(self.initialValue)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myActualValueRequested:
            x = "+ActualValue="
            if self._myHasActualValue:
                leafStr = str(self.actualValue)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+InitialValue="
        if self._myHasInitialValue:
            leafStr = str(self.initialValue)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInitialValueRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+ActualValue="
        if self._myHasActualValue:
            leafStr = str(self.actualValue)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myActualValueRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setInitialValueRequested()
        self.setActualValueRequested()
        
        


    def setInitialValue (self, initialValue):
        self.initialValue = initialValue
        self.setHasInitialValue()

    def setActualValue (self, actualValue):
        self.actualValue = actualValue
        self.setHasActualValue()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_linux_variables.tech.linux_.variable_collection.variable.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "linux_", 
            "isCurrent": false
        }, 
        {
            "namespace": "variable_collection", 
            "isCurrent": false
        }, 
        {
            "namespace": "variable", 
            "isCurrent": false
        }, 
        {
            "namespace": "status", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "initialValue", 
            "yangName": "initial-value", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "actualValue", 
            "yangName": "actual-value", 
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
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_linux_variables"
        ]
    }, 
    "createTime": "2013"
}
"""


