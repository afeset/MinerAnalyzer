


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

        self.tableLastChangeTicks = 0
        self._myHasTableLastChangeTicks=False
        self._myTableLastChangeTicksRequested=False
        
        self.interfaceNumber = 0
        self._myHasInterfaceNumber=False
        self._myInterfaceNumberRequested=False
        


    def copyFrom (self, other):

        self.tableLastChangeTicks=other.tableLastChangeTicks
        self._myHasTableLastChangeTicks=other._myHasTableLastChangeTicks
        self._myTableLastChangeTicksRequested=other._myTableLastChangeTicksRequested
        
        self.interfaceNumber=other.interfaceNumber
        self._myHasInterfaceNumber=other._myHasInterfaceNumber
        self._myInterfaceNumberRequested=other._myInterfaceNumberRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isTableLastChangeTicksRequested():
            self.tableLastChangeTicks=other.tableLastChangeTicks
            self._myHasTableLastChangeTicks=other._myHasTableLastChangeTicks
            self._myTableLastChangeTicksRequested=other._myTableLastChangeTicksRequested
        
        if self.isInterfaceNumberRequested():
            self.interfaceNumber=other.interfaceNumber
            self._myHasInterfaceNumber=other._myHasInterfaceNumber
            self._myInterfaceNumberRequested=other._myInterfaceNumberRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasTableLastChangeTicks():
            self.tableLastChangeTicks=other.tableLastChangeTicks
            self._myHasTableLastChangeTicks=other._myHasTableLastChangeTicks
            self._myTableLastChangeTicksRequested=other._myTableLastChangeTicksRequested
        
        if other.hasInterfaceNumber():
            self.interfaceNumber=other.interfaceNumber
            self._myHasInterfaceNumber=other._myHasInterfaceNumber
            self._myInterfaceNumberRequested=other._myInterfaceNumberRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.tableLastChangeTicks=other.tableLastChangeTicks
        self._myHasTableLastChangeTicks=other._myHasTableLastChangeTicks
        
        self.interfaceNumber=other.interfaceNumber
        self._myHasInterfaceNumber=other._myHasInterfaceNumber
        


    def setAllNumericToZero (self):
        
        self.tableLastChangeTicks=0
        self.setHasTableLastChangeTicks()
        self.interfaceNumber=0
        self.setHasInterfaceNumber()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasTableLastChangeTicks():
            if other.hasTableLastChangeTicks():
                self.tableLastChangeTicks -= other.tableLastChangeTicks
        
        if self.hasInterfaceNumber():
            if other.hasInterfaceNumber():
                self.interfaceNumber -= other.interfaceNumber
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasTableLastChangeTicks():
            if other.hasTableLastChangeTicks():
                self.tableLastChangeTicks += other.tableLastChangeTicks
        
        if self.hasInterfaceNumber():
            if other.hasInterfaceNumber():
                self.interfaceNumber += other.interfaceNumber
        
        
        pass


    # has...() methods

    def hasTableLastChangeTicks (self):
        return self._myHasTableLastChangeTicks

    def hasInterfaceNumber (self):
        return self._myHasInterfaceNumber




    # setHas...() methods

    def setHasTableLastChangeTicks (self):
        self._myHasTableLastChangeTicks=True

    def setHasInterfaceNumber (self):
        self._myHasInterfaceNumber=True




    # isRequested...() methods

    def isTableLastChangeTicksRequested (self):
        return self._myTableLastChangeTicksRequested

    def isInterfaceNumberRequested (self):
        return self._myInterfaceNumberRequested




    # setRequested...() methods

    def setTableLastChangeTicksRequested (self):
        self._myTableLastChangeTicksRequested=True

    def setInterfaceNumberRequested (self):
        self._myInterfaceNumberRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myTableLastChangeTicksRequested:
            x = "+TableLastChangeTicks="
            if self._myHasTableLastChangeTicks:
                leafStr = str(self.tableLastChangeTicks)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInterfaceNumberRequested:
            x = "+InterfaceNumber="
            if self._myHasInterfaceNumber:
                leafStr = str(self.interfaceNumber)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+TableLastChangeTicks="
        if self._myHasTableLastChangeTicks:
            leafStr = str(self.tableLastChangeTicks)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myTableLastChangeTicksRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InterfaceNumber="
        if self._myHasInterfaceNumber:
            leafStr = str(self.interfaceNumber)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInterfaceNumberRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setTableLastChangeTicksRequested()
        self.setInterfaceNumberRequested()
        
        


    def setTableLastChangeTicks (self, tableLastChangeTicks):
        self.tableLastChangeTicks = tableLastChangeTicks
        self.setHasTableLastChangeTicks()

    def setInterfaceNumber (self, interfaceNumber):
        self.interfaceNumber = interfaceNumber
        self.setHasInterfaceNumber()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "interfaces", 
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
            "typeHandler": "handler: IntHandler", 
            "memberName": "tableLastChangeTicks", 
            "yangName": "table-last-change-ticks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "interfaceNumber", 
            "yangName": "interface-number", 
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
            "qwilt_tech_interfaces"
        ]
    }, 
    "createTime": "2013"
}
"""


