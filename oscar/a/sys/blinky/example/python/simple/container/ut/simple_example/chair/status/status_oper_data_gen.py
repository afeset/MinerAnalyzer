


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

        self.version = ""
        self._myHasVersion=False
        self._myVersionRequested=False
        
        self.health = ""
        self._myHasHealth=False
        self._myHealthRequested=False
        
        self.numOfCracks = 0
        self._myHasNumOfCracks=False
        self._myNumOfCracksRequested=False
        


    def copyFrom (self, other):

        self.version=other.version
        self._myHasVersion=other._myHasVersion
        self._myVersionRequested=other._myVersionRequested
        
        self.health=other.health
        self._myHasHealth=other._myHasHealth
        self._myHealthRequested=other._myHealthRequested
        
        self.numOfCracks=other.numOfCracks
        self._myHasNumOfCracks=other._myHasNumOfCracks
        self._myNumOfCracksRequested=other._myNumOfCracksRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isVersionRequested():
            self.version=other.version
            self._myHasVersion=other._myHasVersion
            self._myVersionRequested=other._myVersionRequested
        
        if self.isHealthRequested():
            self.health=other.health
            self._myHasHealth=other._myHasHealth
            self._myHealthRequested=other._myHealthRequested
        
        if self.isNumOfCracksRequested():
            self.numOfCracks=other.numOfCracks
            self._myHasNumOfCracks=other._myHasNumOfCracks
            self._myNumOfCracksRequested=other._myNumOfCracksRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasVersion():
            self.version=other.version
            self._myHasVersion=other._myHasVersion
            self._myVersionRequested=other._myVersionRequested
        
        if other.hasHealth():
            self.health=other.health
            self._myHasHealth=other._myHasHealth
            self._myHealthRequested=other._myHealthRequested
        
        if other.hasNumOfCracks():
            self.numOfCracks=other.numOfCracks
            self._myHasNumOfCracks=other._myHasNumOfCracks
            self._myNumOfCracksRequested=other._myNumOfCracksRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.version=other.version
        self._myHasVersion=other._myHasVersion
        
        self.health=other.health
        self._myHasHealth=other._myHasHealth
        
        self.numOfCracks=other.numOfCracks
        self._myHasNumOfCracks=other._myHasNumOfCracks
        


    def setAllNumericToZero (self):
        
        self.numOfCracks=0
        self.setHasNumOfCracks()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasNumOfCracks():
            if other.hasNumOfCracks():
                self.numOfCracks -= other.numOfCracks
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasNumOfCracks():
            if other.hasNumOfCracks():
                self.numOfCracks += other.numOfCracks
        
        
        pass


    # has...() methods

    def hasVersion (self):
        return self._myHasVersion

    def hasHealth (self):
        return self._myHasHealth

    def hasNumOfCracks (self):
        return self._myHasNumOfCracks




    # setHas...() methods

    def setHasVersion (self):
        self._myHasVersion=True

    def setHasHealth (self):
        self._myHasHealth=True

    def setHasNumOfCracks (self):
        self._myHasNumOfCracks=True




    # isRequested...() methods

    def isVersionRequested (self):
        return self._myVersionRequested

    def isHealthRequested (self):
        return self._myHealthRequested

    def isNumOfCracksRequested (self):
        return self._myNumOfCracksRequested




    # setRequested...() methods

    def setVersionRequested (self):
        self._myVersionRequested=True

    def setHealthRequested (self):
        self._myHealthRequested=True

    def setNumOfCracksRequested (self):
        self._myNumOfCracksRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myVersionRequested:
            x = "+Version="
            if self._myHasVersion:
                leafStr = str(self.version)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myHealthRequested:
            x = "+Health="
            if self._myHasHealth:
                leafStr = str(self.health)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myNumOfCracksRequested:
            x = "+NumOfCracks="
            if self._myHasNumOfCracks:
                leafStr = str(self.numOfCracks)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+Version="
        if self._myHasVersion:
            leafStr = str(self.version)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myVersionRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+Health="
        if self._myHasHealth:
            leafStr = str(self.health)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myHealthRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+NumOfCracks="
        if self._myHasNumOfCracks:
            leafStr = str(self.numOfCracks)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myNumOfCracksRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setVersionRequested()
        self.setHealthRequested()
        self.setNumOfCracksRequested()
        
        


    def setVersion (self, version):
        self.version = version
        self.setHasVersion()

    def setHealth (self, health):
        self.health = health
        self.setHasHealth()

    def setNumOfCracks (self, numOfCracks):
        self.numOfCracks = numOfCracks
        self.setHasNumOfCracks()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.sys.blinky.example.python.simple.container.ut.simple_example.chair.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "chair", 
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
            "memberName": "version", 
            "yangName": "version", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: StringHandler", 
            "memberName": "health", 
            "yangName": "health", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "numOfCracks", 
            "yangName": "num-of-cracks", 
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
            "python", 
            "simple", 
            "container", 
            "ut", 
            "simple_example"
        ]
    }, 
    "createTime": "2013"
}
"""


