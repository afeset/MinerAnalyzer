


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





class TempMemoryOperData (object):

    def __init__ (self):

        self.virtualSize = 0
        self._myHasVirtualSize=False
        self._myVirtualSizeRequested=False
        
        self.rssSize = 0
        self._myHasRssSize=False
        self._myRssSizeRequested=False
        


    def copyFrom (self, other):

        self.virtualSize=other.virtualSize
        self._myHasVirtualSize=other._myHasVirtualSize
        self._myVirtualSizeRequested=other._myVirtualSizeRequested
        
        self.rssSize=other.rssSize
        self._myHasRssSize=other._myHasRssSize
        self._myRssSizeRequested=other._myRssSizeRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isVirtualSizeRequested():
            self.virtualSize=other.virtualSize
            self._myHasVirtualSize=other._myHasVirtualSize
            self._myVirtualSizeRequested=other._myVirtualSizeRequested
        
        if self.isRssSizeRequested():
            self.rssSize=other.rssSize
            self._myHasRssSize=other._myHasRssSize
            self._myRssSizeRequested=other._myRssSizeRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasVirtualSize():
            self.virtualSize=other.virtualSize
            self._myHasVirtualSize=other._myHasVirtualSize
            self._myVirtualSizeRequested=other._myVirtualSizeRequested
        
        if other.hasRssSize():
            self.rssSize=other.rssSize
            self._myHasRssSize=other._myHasRssSize
            self._myRssSizeRequested=other._myRssSizeRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.virtualSize=other.virtualSize
        self._myHasVirtualSize=other._myHasVirtualSize
        
        self.rssSize=other.rssSize
        self._myHasRssSize=other._myHasRssSize
        


    def setAllNumericToZero (self):
        
        self.virtualSize=0
        self.setHasVirtualSize()
        self.rssSize=0
        self.setHasRssSize()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasVirtualSize():
            if other.hasVirtualSize():
                self.virtualSize -= other.virtualSize
        
        if self.hasRssSize():
            if other.hasRssSize():
                self.rssSize -= other.rssSize
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasVirtualSize():
            if other.hasVirtualSize():
                self.virtualSize += other.virtualSize
        
        if self.hasRssSize():
            if other.hasRssSize():
                self.rssSize += other.rssSize
        
        
        pass


    # has...() methods

    def hasVirtualSize (self):
        return self._myHasVirtualSize

    def hasRssSize (self):
        return self._myHasRssSize




    # setHas...() methods

    def setHasVirtualSize (self):
        self._myHasVirtualSize=True

    def setHasRssSize (self):
        self._myHasRssSize=True




    # isRequested...() methods

    def isVirtualSizeRequested (self):
        return self._myVirtualSizeRequested

    def isRssSizeRequested (self):
        return self._myRssSizeRequested




    # setRequested...() methods

    def setVirtualSizeRequested (self):
        self._myVirtualSizeRequested=True

    def setRssSizeRequested (self):
        self._myRssSizeRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myVirtualSizeRequested:
            x = "+VirtualSize="
            if self._myHasVirtualSize:
                leafStr = str(self.virtualSize)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myRssSizeRequested:
            x = "+RssSize="
            if self._myHasRssSize:
                leafStr = str(self.rssSize)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{TempMemoryOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+VirtualSize="
        if self._myHasVirtualSize:
            leafStr = str(self.virtualSize)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myVirtualSizeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+RssSize="
        if self._myHasRssSize:
            leafStr = str(self.rssSize)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myRssSizeRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{TempMemoryOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setVirtualSizeRequested()
        self.setRssSizeRequested()
        
        


    def setVirtualSize (self, virtualSize):
        self.virtualSize = virtualSize
        self.setHasVirtualSize()

    def setRssSize (self, rssSize):
        self.rssSize = rssSize
        self.setHasRssSize()


"""
Extracted from the below data: 
{
    "node": {
        "className": "TempMemoryOperData", 
        "namespace": "temp_memory", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_process.tech.process.execution.status.temp_memory.temp_memory_oper_data_gen import TempMemoryOperData"
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
            "isCurrent": false
        }, 
        {
            "namespace": "temp_memory", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "virtualSize", 
            "yangName": "virtual-size", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "rssSize", 
            "yangName": "rss-size", 
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
            "qwilt_tech_process"
        ]
    }, 
    "createTime": "2013"
}
"""


