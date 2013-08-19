


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





class CountersOperData (object):

    def __init__ (self):

        self.silentDroppedPackets = 0
        self._myHasSilentDroppedPackets=False
        self._mySilentDroppedPacketsRequested=False
        
        self.inPackets = 0
        self._myHasInPackets=False
        self._myInPacketsRequested=False
        
        self.inBadVersionPackets = 0
        self._myHasInBadVersionPackets=False
        self._myInBadVersionPacketsRequested=False
        
        self.inBadCommunityUsePackets = 0
        self._myHasInBadCommunityUsePackets=False
        self._myInBadCommunityUsePacketsRequested=False
        
        self.inAsnParseErrors = 0
        self._myHasInAsnParseErrors=False
        self._myInAsnParseErrorsRequested=False
        
        self.inBadCommunityPackets = 0
        self._myHasInBadCommunityPackets=False
        self._myInBadCommunityPacketsRequested=False
        


    def copyFrom (self, other):

        self.silentDroppedPackets=other.silentDroppedPackets
        self._myHasSilentDroppedPackets=other._myHasSilentDroppedPackets
        self._mySilentDroppedPacketsRequested=other._mySilentDroppedPacketsRequested
        
        self.inPackets=other.inPackets
        self._myHasInPackets=other._myHasInPackets
        self._myInPacketsRequested=other._myInPacketsRequested
        
        self.inBadVersionPackets=other.inBadVersionPackets
        self._myHasInBadVersionPackets=other._myHasInBadVersionPackets
        self._myInBadVersionPacketsRequested=other._myInBadVersionPacketsRequested
        
        self.inBadCommunityUsePackets=other.inBadCommunityUsePackets
        self._myHasInBadCommunityUsePackets=other._myHasInBadCommunityUsePackets
        self._myInBadCommunityUsePacketsRequested=other._myInBadCommunityUsePacketsRequested
        
        self.inAsnParseErrors=other.inAsnParseErrors
        self._myHasInAsnParseErrors=other._myHasInAsnParseErrors
        self._myInAsnParseErrorsRequested=other._myInAsnParseErrorsRequested
        
        self.inBadCommunityPackets=other.inBadCommunityPackets
        self._myHasInBadCommunityPackets=other._myHasInBadCommunityPackets
        self._myInBadCommunityPacketsRequested=other._myInBadCommunityPacketsRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isSilentDroppedPacketsRequested():
            self.silentDroppedPackets=other.silentDroppedPackets
            self._myHasSilentDroppedPackets=other._myHasSilentDroppedPackets
            self._mySilentDroppedPacketsRequested=other._mySilentDroppedPacketsRequested
        
        if self.isInPacketsRequested():
            self.inPackets=other.inPackets
            self._myHasInPackets=other._myHasInPackets
            self._myInPacketsRequested=other._myInPacketsRequested
        
        if self.isInBadVersionPacketsRequested():
            self.inBadVersionPackets=other.inBadVersionPackets
            self._myHasInBadVersionPackets=other._myHasInBadVersionPackets
            self._myInBadVersionPacketsRequested=other._myInBadVersionPacketsRequested
        
        if self.isInBadCommunityUsePacketsRequested():
            self.inBadCommunityUsePackets=other.inBadCommunityUsePackets
            self._myHasInBadCommunityUsePackets=other._myHasInBadCommunityUsePackets
            self._myInBadCommunityUsePacketsRequested=other._myInBadCommunityUsePacketsRequested
        
        if self.isInAsnParseErrorsRequested():
            self.inAsnParseErrors=other.inAsnParseErrors
            self._myHasInAsnParseErrors=other._myHasInAsnParseErrors
            self._myInAsnParseErrorsRequested=other._myInAsnParseErrorsRequested
        
        if self.isInBadCommunityPacketsRequested():
            self.inBadCommunityPackets=other.inBadCommunityPackets
            self._myHasInBadCommunityPackets=other._myHasInBadCommunityPackets
            self._myInBadCommunityPacketsRequested=other._myInBadCommunityPacketsRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasSilentDroppedPackets():
            self.silentDroppedPackets=other.silentDroppedPackets
            self._myHasSilentDroppedPackets=other._myHasSilentDroppedPackets
            self._mySilentDroppedPacketsRequested=other._mySilentDroppedPacketsRequested
        
        if other.hasInPackets():
            self.inPackets=other.inPackets
            self._myHasInPackets=other._myHasInPackets
            self._myInPacketsRequested=other._myInPacketsRequested
        
        if other.hasInBadVersionPackets():
            self.inBadVersionPackets=other.inBadVersionPackets
            self._myHasInBadVersionPackets=other._myHasInBadVersionPackets
            self._myInBadVersionPacketsRequested=other._myInBadVersionPacketsRequested
        
        if other.hasInBadCommunityUsePackets():
            self.inBadCommunityUsePackets=other.inBadCommunityUsePackets
            self._myHasInBadCommunityUsePackets=other._myHasInBadCommunityUsePackets
            self._myInBadCommunityUsePacketsRequested=other._myInBadCommunityUsePacketsRequested
        
        if other.hasInAsnParseErrors():
            self.inAsnParseErrors=other.inAsnParseErrors
            self._myHasInAsnParseErrors=other._myHasInAsnParseErrors
            self._myInAsnParseErrorsRequested=other._myInAsnParseErrorsRequested
        
        if other.hasInBadCommunityPackets():
            self.inBadCommunityPackets=other.inBadCommunityPackets
            self._myHasInBadCommunityPackets=other._myHasInBadCommunityPackets
            self._myInBadCommunityPacketsRequested=other._myInBadCommunityPacketsRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.silentDroppedPackets=other.silentDroppedPackets
        self._myHasSilentDroppedPackets=other._myHasSilentDroppedPackets
        
        self.inPackets=other.inPackets
        self._myHasInPackets=other._myHasInPackets
        
        self.inBadVersionPackets=other.inBadVersionPackets
        self._myHasInBadVersionPackets=other._myHasInBadVersionPackets
        
        self.inBadCommunityUsePackets=other.inBadCommunityUsePackets
        self._myHasInBadCommunityUsePackets=other._myHasInBadCommunityUsePackets
        
        self.inAsnParseErrors=other.inAsnParseErrors
        self._myHasInAsnParseErrors=other._myHasInAsnParseErrors
        
        self.inBadCommunityPackets=other.inBadCommunityPackets
        self._myHasInBadCommunityPackets=other._myHasInBadCommunityPackets
        


    def setAllNumericToZero (self):
        
        self.silentDroppedPackets=0
        self.setHasSilentDroppedPackets()
        self.inPackets=0
        self.setHasInPackets()
        self.inBadVersionPackets=0
        self.setHasInBadVersionPackets()
        self.inBadCommunityUsePackets=0
        self.setHasInBadCommunityUsePackets()
        self.inAsnParseErrors=0
        self.setHasInAsnParseErrors()
        self.inBadCommunityPackets=0
        self.setHasInBadCommunityPackets()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasSilentDroppedPackets():
            if other.hasSilentDroppedPackets():
                self.silentDroppedPackets -= other.silentDroppedPackets
        
        if self.hasInPackets():
            if other.hasInPackets():
                self.inPackets -= other.inPackets
        
        if self.hasInBadVersionPackets():
            if other.hasInBadVersionPackets():
                self.inBadVersionPackets -= other.inBadVersionPackets
        
        if self.hasInBadCommunityUsePackets():
            if other.hasInBadCommunityUsePackets():
                self.inBadCommunityUsePackets -= other.inBadCommunityUsePackets
        
        if self.hasInAsnParseErrors():
            if other.hasInAsnParseErrors():
                self.inAsnParseErrors -= other.inAsnParseErrors
        
        if self.hasInBadCommunityPackets():
            if other.hasInBadCommunityPackets():
                self.inBadCommunityPackets -= other.inBadCommunityPackets
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasSilentDroppedPackets():
            if other.hasSilentDroppedPackets():
                self.silentDroppedPackets += other.silentDroppedPackets
        
        if self.hasInPackets():
            if other.hasInPackets():
                self.inPackets += other.inPackets
        
        if self.hasInBadVersionPackets():
            if other.hasInBadVersionPackets():
                self.inBadVersionPackets += other.inBadVersionPackets
        
        if self.hasInBadCommunityUsePackets():
            if other.hasInBadCommunityUsePackets():
                self.inBadCommunityUsePackets += other.inBadCommunityUsePackets
        
        if self.hasInAsnParseErrors():
            if other.hasInAsnParseErrors():
                self.inAsnParseErrors += other.inAsnParseErrors
        
        if self.hasInBadCommunityPackets():
            if other.hasInBadCommunityPackets():
                self.inBadCommunityPackets += other.inBadCommunityPackets
        
        
        pass


    # has...() methods

    def hasSilentDroppedPackets (self):
        return self._myHasSilentDroppedPackets

    def hasInPackets (self):
        return self._myHasInPackets

    def hasInBadVersionPackets (self):
        return self._myHasInBadVersionPackets

    def hasInBadCommunityUsePackets (self):
        return self._myHasInBadCommunityUsePackets

    def hasInAsnParseErrors (self):
        return self._myHasInAsnParseErrors

    def hasInBadCommunityPackets (self):
        return self._myHasInBadCommunityPackets




    # setHas...() methods

    def setHasSilentDroppedPackets (self):
        self._myHasSilentDroppedPackets=True

    def setHasInPackets (self):
        self._myHasInPackets=True

    def setHasInBadVersionPackets (self):
        self._myHasInBadVersionPackets=True

    def setHasInBadCommunityUsePackets (self):
        self._myHasInBadCommunityUsePackets=True

    def setHasInAsnParseErrors (self):
        self._myHasInAsnParseErrors=True

    def setHasInBadCommunityPackets (self):
        self._myHasInBadCommunityPackets=True




    # isRequested...() methods

    def isSilentDroppedPacketsRequested (self):
        return self._mySilentDroppedPacketsRequested

    def isInPacketsRequested (self):
        return self._myInPacketsRequested

    def isInBadVersionPacketsRequested (self):
        return self._myInBadVersionPacketsRequested

    def isInBadCommunityUsePacketsRequested (self):
        return self._myInBadCommunityUsePacketsRequested

    def isInAsnParseErrorsRequested (self):
        return self._myInAsnParseErrorsRequested

    def isInBadCommunityPacketsRequested (self):
        return self._myInBadCommunityPacketsRequested




    # setRequested...() methods

    def setSilentDroppedPacketsRequested (self):
        self._mySilentDroppedPacketsRequested=True

    def setInPacketsRequested (self):
        self._myInPacketsRequested=True

    def setInBadVersionPacketsRequested (self):
        self._myInBadVersionPacketsRequested=True

    def setInBadCommunityUsePacketsRequested (self):
        self._myInBadCommunityUsePacketsRequested=True

    def setInAsnParseErrorsRequested (self):
        self._myInAsnParseErrorsRequested=True

    def setInBadCommunityPacketsRequested (self):
        self._myInBadCommunityPacketsRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._mySilentDroppedPacketsRequested:
            x = "+SilentDroppedPackets="
            if self._myHasSilentDroppedPackets:
                leafStr = str(self.silentDroppedPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInPacketsRequested:
            x = "+InPackets="
            if self._myHasInPackets:
                leafStr = str(self.inPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInBadVersionPacketsRequested:
            x = "+InBadVersionPackets="
            if self._myHasInBadVersionPackets:
                leafStr = str(self.inBadVersionPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInBadCommunityUsePacketsRequested:
            x = "+InBadCommunityUsePackets="
            if self._myHasInBadCommunityUsePackets:
                leafStr = str(self.inBadCommunityUsePackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInAsnParseErrorsRequested:
            x = "+InAsnParseErrors="
            if self._myHasInAsnParseErrors:
                leafStr = str(self.inAsnParseErrors)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInBadCommunityPacketsRequested:
            x = "+InBadCommunityPackets="
            if self._myHasInBadCommunityPackets:
                leafStr = str(self.inBadCommunityPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{CountersOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+SilentDroppedPackets="
        if self._myHasSilentDroppedPackets:
            leafStr = str(self.silentDroppedPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._mySilentDroppedPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InPackets="
        if self._myHasInPackets:
            leafStr = str(self.inPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InBadVersionPackets="
        if self._myHasInBadVersionPackets:
            leafStr = str(self.inBadVersionPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInBadVersionPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InBadCommunityUsePackets="
        if self._myHasInBadCommunityUsePackets:
            leafStr = str(self.inBadCommunityUsePackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInBadCommunityUsePacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InAsnParseErrors="
        if self._myHasInAsnParseErrors:
            leafStr = str(self.inAsnParseErrors)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInAsnParseErrorsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InBadCommunityPackets="
        if self._myHasInBadCommunityPackets:
            leafStr = str(self.inBadCommunityPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInBadCommunityPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setSilentDroppedPacketsRequested()
        self.setInPacketsRequested()
        self.setInBadVersionPacketsRequested()
        self.setInBadCommunityUsePacketsRequested()
        self.setInAsnParseErrorsRequested()
        self.setInBadCommunityPacketsRequested()
        
        


    def setSilentDroppedPackets (self, silentDroppedPackets):
        self.silentDroppedPackets = silentDroppedPackets
        self.setHasSilentDroppedPackets()

    def setInPackets (self, inPackets):
        self.inPackets = inPackets
        self.setHasInPackets()

    def setInBadVersionPackets (self, inBadVersionPackets):
        self.inBadVersionPackets = inBadVersionPackets
        self.setHasInBadVersionPackets()

    def setInBadCommunityUsePackets (self, inBadCommunityUsePackets):
        self.inBadCommunityUsePackets = inBadCommunityUsePackets
        self.setHasInBadCommunityUsePackets()

    def setInAsnParseErrors (self, inAsnParseErrors):
        self.inAsnParseErrors = inAsnParseErrors
        self.setHasInAsnParseErrors()

    def setInBadCommunityPackets (self, inBadCommunityPackets):
        self.inBadCommunityPackets = inBadCommunityPackets
        self.setHasInBadCommunityPackets()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_snmp.tech.snmp.counters.counters_oper_data_gen import CountersOperData"
    }, 
    "ancestors": [
        {
            "namespace": "tech", 
            "isCurrent": false
        }, 
        {
            "namespace": "snmp", 
            "isCurrent": false
        }, 
        {
            "namespace": "counters", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "silentDroppedPackets", 
            "yangName": "silent-dropped-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPackets", 
            "yangName": "in-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadVersionPackets", 
            "yangName": "in-bad-version-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadCommunityUsePackets", 
            "yangName": "in-bad-community-use-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inAsnParseErrors", 
            "yangName": "in-asn-parse-errors", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBadCommunityPackets", 
            "yangName": "in-bad-community-packets", 
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
            "qwilt_tech_snmp"
        ]
    }, 
    "createTime": "2013"
}
"""


