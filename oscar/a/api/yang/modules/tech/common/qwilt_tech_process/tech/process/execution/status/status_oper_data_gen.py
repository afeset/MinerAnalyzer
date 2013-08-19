


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


from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.actual.actual_oper_data_gen import ActualOperData
from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.temp_memory.temp_memory_oper_data_gen import TempMemoryOperData



class StatusOperData (object):

    def __init__ (self):

        pass
        

        self.myActual = ActualOperData()
        self._myHasActual=False
        self._myActualRequested=False
        self.myTempMemory = TempMemoryOperData()
        self._myHasTempMemory=False
        self._myTempMemoryRequested=False

    def copyFrom (self, other):

        pass
        

        self.myActual = ActualOperData()
        self.myActual.copyFrom(other.Actual)
        self._myHasActual=other._myHasActual
        self._myActualRequested=other._myActualRequested
        self.myTempMemory = TempMemoryOperData()
        self.myTempMemory.copyFrom(other.TempMemory)
        self._myHasTempMemory=other._myHasTempMemory
        self._myTempMemoryRequested=other._myTempMemoryRequested

    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        pass
        

        if self.isActualRequested():
            self.myActual = ActualOperData()
            self.myActual.copyRequestedFrom(other.Actual)
            self._myHasActual=other._myHasActual
            self._myActualRequested=other._myActualRequested
        if self.isTempMemoryRequested():
            self.myTempMemory = TempMemoryOperData()
            self.myTempMemory.copyRequestedFrom(other.TempMemory)
            self._myHasTempMemory=other._myHasTempMemory
            self._myTempMemoryRequested=other._myTempMemoryRequested

    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        pass
        

        if other.hasActual():
            self.myActual = ActualOperData()
            self.myActual.copySetFrom(other.Actual)
            self._myHasActual=other._myHasActual
            self._myActualRequested=other._myActualRequested
        if other.hasTempMemory():
            self.myTempMemory = TempMemoryOperData()
            self.myTempMemory.copySetFrom(other.TempMemory)
            self._myHasTempMemory=other._myHasTempMemory
            self._myTempMemoryRequested=other._myTempMemoryRequested

    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        pass
        

        self.myActual = ActualOperData()
        self.myActual.copyDataFrom(other.Actual)
        self._myHasActual=other._myHasActual
        self.myTempMemory = TempMemoryOperData()
        self.myTempMemory.copyDataFrom(other.TempMemory)
        self._myHasTempMemory=other._myHasTempMemory

    def setAllNumericToZero (self):
        
        
        self.myActual.setAllNumericToZero()
        self.myTempMemory.setAllNumericToZero()
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        self.myActual.subtractAllNumericHas(other, log)
        self.myTempMemory.subtractAllNumericHas(other, log)
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        
        self.myActual.addAllNumericHas(other, log)
        self.myTempMemory.addAllNumericHas(other, log)
        pass


    # has...() methods



    def hasActual (self):
        return self._myHasActual

    def hasTempMemory (self):
        return self._myHasTempMemory


    # setHas...() methods



    def setHasActual (self):
        self._myHasActual=True

    def setHasTempMemory (self):
        self._myHasTempMemory=True


    # isRequested...() methods



    def isActualRequested (self):
        return self._myActualRequested

    def isTempMemoryRequested (self):
        return self._myTempMemoryRequested


    # setRequested...() methods



    def setActualRequested (self):
        self._myActualRequested=True

    def setTempMemoryRequested (self):
        self._myTempMemoryRequested=True


    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]


        x=""
        if self._myActualRequested:
            x = "+Actual="
            if self._myHasActual:
                descendantStr = str(self.myActual)
            else:
                descendantStr = "<UNSET>"
            items.append(x + descendantStr)

        x=""
        if self._myTempMemoryRequested:
            x = "+TempMemory="
            if self._myHasTempMemory:
                descendantStr = str(self.myTempMemory)
            else:
                descendantStr = "<UNSET>"
            items.append(x + descendantStr)

        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]


        x=""
        x = "+Actual="
        if self._myHasActual:
            descendantStr = str(self.myActual)
        else:
            descendantStr = "<UNSET>"
            requestedStr = ''
        if includeRequested:
            if self._myActualRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + descendantStr)

        x=""
        x = "+TempMemory="
        if self._myHasTempMemory:
            descendantStr = str(self.myTempMemory)
        else:
            descendantStr = "<UNSET>"
            requestedStr = ''
        if includeRequested:
            if self._myTempMemoryRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + descendantStr)

        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        
        pass
        
        self.setActualRequested()
        self.setTempMemoryRequested()
        



"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "process", 
            "isCurrent": false
        }, 
        {
            "namespace": "execution", 
            "isCurrent": false
        }, 
        {
            "namespace": "status", 
            "isCurrent": true
        }
    ], 
    "descendants": [
        {
            "className": "ActualOperData", 
            "memberName": "actual", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.actual.actual_oper_data_gen import ActualOperData"
        }, 
        {
            "className": "TempMemoryOperData", 
            "memberName": "tempMemory", 
            "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.temp_memory.temp_memory_oper_data_gen import TempMemoryOperData"
        }
    ], 
    "conditionalDebugName": null, 
    "leaves": [], 
    "module": {}, 
    "env": {
        "namespaces": [
            "a", 
            "api", 
            "yang", 
            "modules", 
            "tech", 
            "common", 
            "qwilt_tech_process"
        ]
    }, 
    "createTime": "2013"
}
"""


