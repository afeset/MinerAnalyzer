


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

        self.numOfCracks = 0
        self._myHasNumOfCracks=False
        self._myNumOfCracksRequested=False
        
        self.version = ""
        self._myHasVersion=False
        self._myVersionRequested=False
        
        self.health = ""
        self._myHasHealth=False
        self._myHealthRequested=False
        
        self.linux_ = ""
        self._myHasLinux_=False
        self._myLinux_Requested=False
        


    def copyFrom (self, other):

        self.numOfCracks=other.numOfCracks
        self._myHasNumOfCracks=other._myHasNumOfCracks
        self._myNumOfCracksRequested=other._myNumOfCracksRequested
        
        self.version=other.version
        self._myHasVersion=other._myHasVersion
        self._myVersionRequested=other._myVersionRequested
        
        self.health=other.health
        self._myHasHealth=other._myHasHealth
        self._myHealthRequested=other._myHealthRequested
        
        self.linux_=other.linux_
        self._myHasLinux_=other._myHasLinux_
        self._myLinux_Requested=other._myLinux_Requested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isNumOfCracksRequested():
            self.numOfCracks=other.numOfCracks
            self._myHasNumOfCracks=other._myHasNumOfCracks
            self._myNumOfCracksRequested=other._myNumOfCracksRequested
        
        if self.isVersionRequested():
            self.version=other.version
            self._myHasVersion=other._myHasVersion
            self._myVersionRequested=other._myVersionRequested
        
        if self.isHealthRequested():
            self.health=other.health
            self._myHasHealth=other._myHasHealth
            self._myHealthRequested=other._myHealthRequested
        
        if self.isLinux_Requested():
            self.linux_=other.linux_
            self._myHasLinux_=other._myHasLinux_
            self._myLinux_Requested=other._myLinux_Requested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasNumOfCracks():
            self.numOfCracks=other.numOfCracks
            self._myHasNumOfCracks=other._myHasNumOfCracks
            self._myNumOfCracksRequested=other._myNumOfCracksRequested
        
        if other.hasVersion():
            self.version=other.version
            self._myHasVersion=other._myHasVersion
            self._myVersionRequested=other._myVersionRequested
        
        if other.hasHealth():
            self.health=other.health
            self._myHasHealth=other._myHasHealth
            self._myHealthRequested=other._myHealthRequested
        
        if other.hasLinux_():
            self.linux_=other.linux_
            self._myHasLinux_=other._myHasLinux_
            self._myLinux_Requested=other._myLinux_Requested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.numOfCracks=other.numOfCracks
        self._myHasNumOfCracks=other._myHasNumOfCracks
        
        self.version=other.version
        self._myHasVersion=other._myHasVersion
        
        self.health=other.health
        self._myHasHealth=other._myHasHealth
        
        self.linux_=other.linux_
        self._myHasLinux_=other._myHasLinux_
        


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

    def hasNumOfCracks (self):
        return self._myHasNumOfCracks

    def hasVersion (self):
        return self._myHasVersion

    def hasHealth (self):
        return self._myHasHealth

    def hasLinux_ (self):
        return self._myHasLinux_




    # setHas...() methods

    def setHasNumOfCracks (self):
        self._myHasNumOfCracks=True

    def setHasVersion (self):
        self._myHasVersion=True

    def setHasHealth (self):
        self._myHasHealth=True

    def setHasLinux_ (self):
        self._myHasLinux_=True




    # isRequested...() methods

    def isNumOfCracksRequested (self):
        return self._myNumOfCracksRequested

    def isVersionRequested (self):
        return self._myVersionRequested

    def isHealthRequested (self):
        return self._myHealthRequested

    def isLinux_Requested (self):
        return self._myLinux_Requested




    # setRequested...() methods

    def setNumOfCracksRequested (self):
        self._myNumOfCracksRequested=True

    def setVersionRequested (self):
        self._myVersionRequested=True

    def setHealthRequested (self):
        self._myHealthRequested=True

    def setLinux_Requested (self):
        self._myLinux_Requested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myNumOfCracksRequested:
            x = "+NumOfCracks="
            if self._myHasNumOfCracks:
                leafStr = str(self.numOfCracks)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

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
        if self._myLinux_Requested:
            x = "+Linux_="
            if self._myHasLinux_:
                leafStr = str(self.linux_)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{StatusOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

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
        x = "+Linux_="
        if self._myHasLinux_:
            leafStr = str(self.linux_)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myLinux_Requested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{StatusOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setNumOfCracksRequested()
        self.setVersionRequested()
        self.setHealthRequested()
        self.setLinux_Requested()
        
        


    def setNumOfCracks (self, numOfCracks):
        self.numOfCracks = numOfCracks
        self.setHasNumOfCracks()

    def setVersion (self, version):
        self.version = version
        self.setHasVersion()

    def setHealth (self, health):
        self.health = health
        self.setHasHealth()

    def setLinux_ (self, linux_):
        self.linux_ = linux_
        self.setHasLinux_()


"""
Extracted from the below data: 
{
    "node": {
        "className": "StatusOperData", 
        "namespace": "status", 
        "importStatement": "from a.sys.blinky.example.python.generator_test.ut.generator_test.person.status.status_oper_data_gen import StatusOperData"
    }, 
    "ancestors": [
        {
            "namespace": "person", 
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
            "memberName": "numOfCracks", 
            "yangName": "num-of-cracks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
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
            "typeHandler": "handler: StringHandler", 
            "memberName": "linux_", 
            "yangName": "linux", 
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
            "generator_test", 
            "ut", 
            "generator_test"
        ]
    }, 
    "createTime": "2013"
}
"""


