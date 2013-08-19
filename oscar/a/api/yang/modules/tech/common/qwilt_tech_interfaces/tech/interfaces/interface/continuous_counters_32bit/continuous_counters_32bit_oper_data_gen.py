


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





class ContinuousCounters32BitOperData (object):

    def __init__ (self):

        self.outErrorPackets = 0
        self._myHasOutErrorPackets=False
        self._myOutErrorPacketsRequested=False
        
        self.inErrorPackets = 0
        self._myHasInErrorPackets=False
        self._myInErrorPacketsRequested=False
        
        self.inDiscardPackets = 0
        self._myHasInDiscardPackets=False
        self._myInDiscardPacketsRequested=False
        
        self.outUnicastPackets = 0
        self._myHasOutUnicastPackets=False
        self._myOutUnicastPacketsRequested=False
        
        self.inMulticastPackets = 0
        self._myHasInMulticastPackets=False
        self._myInMulticastPacketsRequested=False
        
        self.outBroadcastPackets = 0
        self._myHasOutBroadcastPackets=False
        self._myOutBroadcastPacketsRequested=False
        
        self.inBroadcastPackets = 0
        self._myHasInBroadcastPackets=False
        self._myInBroadcastPacketsRequested=False
        
        self.outMulticastPackets = 0
        self._myHasOutMulticastPackets=False
        self._myOutMulticastPacketsRequested=False
        
        self.inUnknownProtocolPackets = 0
        self._myHasInUnknownProtocolPackets=False
        self._myInUnknownProtocolPacketsRequested=False
        
        self.outDiscardPackets = 0
        self._myHasOutDiscardPackets=False
        self._myOutDiscardPacketsRequested=False
        
        self.inUnicastPackets = 0
        self._myHasInUnicastPackets=False
        self._myInUnicastPacketsRequested=False
        
        self.outOctets = 0
        self._myHasOutOctets=False
        self._myOutOctetsRequested=False
        
        self.inOctets = 0
        self._myHasInOctets=False
        self._myInOctetsRequested=False
        


    def copyFrom (self, other):

        self.outErrorPackets=other.outErrorPackets
        self._myHasOutErrorPackets=other._myHasOutErrorPackets
        self._myOutErrorPacketsRequested=other._myOutErrorPacketsRequested
        
        self.inErrorPackets=other.inErrorPackets
        self._myHasInErrorPackets=other._myHasInErrorPackets
        self._myInErrorPacketsRequested=other._myInErrorPacketsRequested
        
        self.inDiscardPackets=other.inDiscardPackets
        self._myHasInDiscardPackets=other._myHasInDiscardPackets
        self._myInDiscardPacketsRequested=other._myInDiscardPacketsRequested
        
        self.outUnicastPackets=other.outUnicastPackets
        self._myHasOutUnicastPackets=other._myHasOutUnicastPackets
        self._myOutUnicastPacketsRequested=other._myOutUnicastPacketsRequested
        
        self.inMulticastPackets=other.inMulticastPackets
        self._myHasInMulticastPackets=other._myHasInMulticastPackets
        self._myInMulticastPacketsRequested=other._myInMulticastPacketsRequested
        
        self.outBroadcastPackets=other.outBroadcastPackets
        self._myHasOutBroadcastPackets=other._myHasOutBroadcastPackets
        self._myOutBroadcastPacketsRequested=other._myOutBroadcastPacketsRequested
        
        self.inBroadcastPackets=other.inBroadcastPackets
        self._myHasInBroadcastPackets=other._myHasInBroadcastPackets
        self._myInBroadcastPacketsRequested=other._myInBroadcastPacketsRequested
        
        self.outMulticastPackets=other.outMulticastPackets
        self._myHasOutMulticastPackets=other._myHasOutMulticastPackets
        self._myOutMulticastPacketsRequested=other._myOutMulticastPacketsRequested
        
        self.inUnknownProtocolPackets=other.inUnknownProtocolPackets
        self._myHasInUnknownProtocolPackets=other._myHasInUnknownProtocolPackets
        self._myInUnknownProtocolPacketsRequested=other._myInUnknownProtocolPacketsRequested
        
        self.outDiscardPackets=other.outDiscardPackets
        self._myHasOutDiscardPackets=other._myHasOutDiscardPackets
        self._myOutDiscardPacketsRequested=other._myOutDiscardPacketsRequested
        
        self.inUnicastPackets=other.inUnicastPackets
        self._myHasInUnicastPackets=other._myHasInUnicastPackets
        self._myInUnicastPacketsRequested=other._myInUnicastPacketsRequested
        
        self.outOctets=other.outOctets
        self._myHasOutOctets=other._myHasOutOctets
        self._myOutOctetsRequested=other._myOutOctetsRequested
        
        self.inOctets=other.inOctets
        self._myHasInOctets=other._myHasInOctets
        self._myInOctetsRequested=other._myInOctetsRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isOutErrorPacketsRequested():
            self.outErrorPackets=other.outErrorPackets
            self._myHasOutErrorPackets=other._myHasOutErrorPackets
            self._myOutErrorPacketsRequested=other._myOutErrorPacketsRequested
        
        if self.isInErrorPacketsRequested():
            self.inErrorPackets=other.inErrorPackets
            self._myHasInErrorPackets=other._myHasInErrorPackets
            self._myInErrorPacketsRequested=other._myInErrorPacketsRequested
        
        if self.isInDiscardPacketsRequested():
            self.inDiscardPackets=other.inDiscardPackets
            self._myHasInDiscardPackets=other._myHasInDiscardPackets
            self._myInDiscardPacketsRequested=other._myInDiscardPacketsRequested
        
        if self.isOutUnicastPacketsRequested():
            self.outUnicastPackets=other.outUnicastPackets
            self._myHasOutUnicastPackets=other._myHasOutUnicastPackets
            self._myOutUnicastPacketsRequested=other._myOutUnicastPacketsRequested
        
        if self.isInMulticastPacketsRequested():
            self.inMulticastPackets=other.inMulticastPackets
            self._myHasInMulticastPackets=other._myHasInMulticastPackets
            self._myInMulticastPacketsRequested=other._myInMulticastPacketsRequested
        
        if self.isOutBroadcastPacketsRequested():
            self.outBroadcastPackets=other.outBroadcastPackets
            self._myHasOutBroadcastPackets=other._myHasOutBroadcastPackets
            self._myOutBroadcastPacketsRequested=other._myOutBroadcastPacketsRequested
        
        if self.isInBroadcastPacketsRequested():
            self.inBroadcastPackets=other.inBroadcastPackets
            self._myHasInBroadcastPackets=other._myHasInBroadcastPackets
            self._myInBroadcastPacketsRequested=other._myInBroadcastPacketsRequested
        
        if self.isOutMulticastPacketsRequested():
            self.outMulticastPackets=other.outMulticastPackets
            self._myHasOutMulticastPackets=other._myHasOutMulticastPackets
            self._myOutMulticastPacketsRequested=other._myOutMulticastPacketsRequested
        
        if self.isInUnknownProtocolPacketsRequested():
            self.inUnknownProtocolPackets=other.inUnknownProtocolPackets
            self._myHasInUnknownProtocolPackets=other._myHasInUnknownProtocolPackets
            self._myInUnknownProtocolPacketsRequested=other._myInUnknownProtocolPacketsRequested
        
        if self.isOutDiscardPacketsRequested():
            self.outDiscardPackets=other.outDiscardPackets
            self._myHasOutDiscardPackets=other._myHasOutDiscardPackets
            self._myOutDiscardPacketsRequested=other._myOutDiscardPacketsRequested
        
        if self.isInUnicastPacketsRequested():
            self.inUnicastPackets=other.inUnicastPackets
            self._myHasInUnicastPackets=other._myHasInUnicastPackets
            self._myInUnicastPacketsRequested=other._myInUnicastPacketsRequested
        
        if self.isOutOctetsRequested():
            self.outOctets=other.outOctets
            self._myHasOutOctets=other._myHasOutOctets
            self._myOutOctetsRequested=other._myOutOctetsRequested
        
        if self.isInOctetsRequested():
            self.inOctets=other.inOctets
            self._myHasInOctets=other._myHasInOctets
            self._myInOctetsRequested=other._myInOctetsRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasOutErrorPackets():
            self.outErrorPackets=other.outErrorPackets
            self._myHasOutErrorPackets=other._myHasOutErrorPackets
            self._myOutErrorPacketsRequested=other._myOutErrorPacketsRequested
        
        if other.hasInErrorPackets():
            self.inErrorPackets=other.inErrorPackets
            self._myHasInErrorPackets=other._myHasInErrorPackets
            self._myInErrorPacketsRequested=other._myInErrorPacketsRequested
        
        if other.hasInDiscardPackets():
            self.inDiscardPackets=other.inDiscardPackets
            self._myHasInDiscardPackets=other._myHasInDiscardPackets
            self._myInDiscardPacketsRequested=other._myInDiscardPacketsRequested
        
        if other.hasOutUnicastPackets():
            self.outUnicastPackets=other.outUnicastPackets
            self._myHasOutUnicastPackets=other._myHasOutUnicastPackets
            self._myOutUnicastPacketsRequested=other._myOutUnicastPacketsRequested
        
        if other.hasInMulticastPackets():
            self.inMulticastPackets=other.inMulticastPackets
            self._myHasInMulticastPackets=other._myHasInMulticastPackets
            self._myInMulticastPacketsRequested=other._myInMulticastPacketsRequested
        
        if other.hasOutBroadcastPackets():
            self.outBroadcastPackets=other.outBroadcastPackets
            self._myHasOutBroadcastPackets=other._myHasOutBroadcastPackets
            self._myOutBroadcastPacketsRequested=other._myOutBroadcastPacketsRequested
        
        if other.hasInBroadcastPackets():
            self.inBroadcastPackets=other.inBroadcastPackets
            self._myHasInBroadcastPackets=other._myHasInBroadcastPackets
            self._myInBroadcastPacketsRequested=other._myInBroadcastPacketsRequested
        
        if other.hasOutMulticastPackets():
            self.outMulticastPackets=other.outMulticastPackets
            self._myHasOutMulticastPackets=other._myHasOutMulticastPackets
            self._myOutMulticastPacketsRequested=other._myOutMulticastPacketsRequested
        
        if other.hasInUnknownProtocolPackets():
            self.inUnknownProtocolPackets=other.inUnknownProtocolPackets
            self._myHasInUnknownProtocolPackets=other._myHasInUnknownProtocolPackets
            self._myInUnknownProtocolPacketsRequested=other._myInUnknownProtocolPacketsRequested
        
        if other.hasOutDiscardPackets():
            self.outDiscardPackets=other.outDiscardPackets
            self._myHasOutDiscardPackets=other._myHasOutDiscardPackets
            self._myOutDiscardPacketsRequested=other._myOutDiscardPacketsRequested
        
        if other.hasInUnicastPackets():
            self.inUnicastPackets=other.inUnicastPackets
            self._myHasInUnicastPackets=other._myHasInUnicastPackets
            self._myInUnicastPacketsRequested=other._myInUnicastPacketsRequested
        
        if other.hasOutOctets():
            self.outOctets=other.outOctets
            self._myHasOutOctets=other._myHasOutOctets
            self._myOutOctetsRequested=other._myOutOctetsRequested
        
        if other.hasInOctets():
            self.inOctets=other.inOctets
            self._myHasInOctets=other._myHasInOctets
            self._myInOctetsRequested=other._myInOctetsRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.outErrorPackets=other.outErrorPackets
        self._myHasOutErrorPackets=other._myHasOutErrorPackets
        
        self.inErrorPackets=other.inErrorPackets
        self._myHasInErrorPackets=other._myHasInErrorPackets
        
        self.inDiscardPackets=other.inDiscardPackets
        self._myHasInDiscardPackets=other._myHasInDiscardPackets
        
        self.outUnicastPackets=other.outUnicastPackets
        self._myHasOutUnicastPackets=other._myHasOutUnicastPackets
        
        self.inMulticastPackets=other.inMulticastPackets
        self._myHasInMulticastPackets=other._myHasInMulticastPackets
        
        self.outBroadcastPackets=other.outBroadcastPackets
        self._myHasOutBroadcastPackets=other._myHasOutBroadcastPackets
        
        self.inBroadcastPackets=other.inBroadcastPackets
        self._myHasInBroadcastPackets=other._myHasInBroadcastPackets
        
        self.outMulticastPackets=other.outMulticastPackets
        self._myHasOutMulticastPackets=other._myHasOutMulticastPackets
        
        self.inUnknownProtocolPackets=other.inUnknownProtocolPackets
        self._myHasInUnknownProtocolPackets=other._myHasInUnknownProtocolPackets
        
        self.outDiscardPackets=other.outDiscardPackets
        self._myHasOutDiscardPackets=other._myHasOutDiscardPackets
        
        self.inUnicastPackets=other.inUnicastPackets
        self._myHasInUnicastPackets=other._myHasInUnicastPackets
        
        self.outOctets=other.outOctets
        self._myHasOutOctets=other._myHasOutOctets
        
        self.inOctets=other.inOctets
        self._myHasInOctets=other._myHasInOctets
        


    def setAllNumericToZero (self):
        
        self.outErrorPackets=0
        self.setHasOutErrorPackets()
        self.inErrorPackets=0
        self.setHasInErrorPackets()
        self.inDiscardPackets=0
        self.setHasInDiscardPackets()
        self.outUnicastPackets=0
        self.setHasOutUnicastPackets()
        self.inMulticastPackets=0
        self.setHasInMulticastPackets()
        self.outBroadcastPackets=0
        self.setHasOutBroadcastPackets()
        self.inBroadcastPackets=0
        self.setHasInBroadcastPackets()
        self.outMulticastPackets=0
        self.setHasOutMulticastPackets()
        self.inUnknownProtocolPackets=0
        self.setHasInUnknownProtocolPackets()
        self.outDiscardPackets=0
        self.setHasOutDiscardPackets()
        self.inUnicastPackets=0
        self.setHasInUnicastPackets()
        self.outOctets=0
        self.setHasOutOctets()
        self.inOctets=0
        self.setHasInOctets()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasOutErrorPackets():
            if other.hasOutErrorPackets():
                self.outErrorPackets -= other.outErrorPackets
        
        if self.hasInErrorPackets():
            if other.hasInErrorPackets():
                self.inErrorPackets -= other.inErrorPackets
        
        if self.hasInDiscardPackets():
            if other.hasInDiscardPackets():
                self.inDiscardPackets -= other.inDiscardPackets
        
        if self.hasOutUnicastPackets():
            if other.hasOutUnicastPackets():
                self.outUnicastPackets -= other.outUnicastPackets
        
        if self.hasInMulticastPackets():
            if other.hasInMulticastPackets():
                self.inMulticastPackets -= other.inMulticastPackets
        
        if self.hasOutBroadcastPackets():
            if other.hasOutBroadcastPackets():
                self.outBroadcastPackets -= other.outBroadcastPackets
        
        if self.hasInBroadcastPackets():
            if other.hasInBroadcastPackets():
                self.inBroadcastPackets -= other.inBroadcastPackets
        
        if self.hasOutMulticastPackets():
            if other.hasOutMulticastPackets():
                self.outMulticastPackets -= other.outMulticastPackets
        
        if self.hasInUnknownProtocolPackets():
            if other.hasInUnknownProtocolPackets():
                self.inUnknownProtocolPackets -= other.inUnknownProtocolPackets
        
        if self.hasOutDiscardPackets():
            if other.hasOutDiscardPackets():
                self.outDiscardPackets -= other.outDiscardPackets
        
        if self.hasInUnicastPackets():
            if other.hasInUnicastPackets():
                self.inUnicastPackets -= other.inUnicastPackets
        
        if self.hasOutOctets():
            if other.hasOutOctets():
                self.outOctets -= other.outOctets
        
        if self.hasInOctets():
            if other.hasInOctets():
                self.inOctets -= other.inOctets
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasOutErrorPackets():
            if other.hasOutErrorPackets():
                self.outErrorPackets += other.outErrorPackets
        
        if self.hasInErrorPackets():
            if other.hasInErrorPackets():
                self.inErrorPackets += other.inErrorPackets
        
        if self.hasInDiscardPackets():
            if other.hasInDiscardPackets():
                self.inDiscardPackets += other.inDiscardPackets
        
        if self.hasOutUnicastPackets():
            if other.hasOutUnicastPackets():
                self.outUnicastPackets += other.outUnicastPackets
        
        if self.hasInMulticastPackets():
            if other.hasInMulticastPackets():
                self.inMulticastPackets += other.inMulticastPackets
        
        if self.hasOutBroadcastPackets():
            if other.hasOutBroadcastPackets():
                self.outBroadcastPackets += other.outBroadcastPackets
        
        if self.hasInBroadcastPackets():
            if other.hasInBroadcastPackets():
                self.inBroadcastPackets += other.inBroadcastPackets
        
        if self.hasOutMulticastPackets():
            if other.hasOutMulticastPackets():
                self.outMulticastPackets += other.outMulticastPackets
        
        if self.hasInUnknownProtocolPackets():
            if other.hasInUnknownProtocolPackets():
                self.inUnknownProtocolPackets += other.inUnknownProtocolPackets
        
        if self.hasOutDiscardPackets():
            if other.hasOutDiscardPackets():
                self.outDiscardPackets += other.outDiscardPackets
        
        if self.hasInUnicastPackets():
            if other.hasInUnicastPackets():
                self.inUnicastPackets += other.inUnicastPackets
        
        if self.hasOutOctets():
            if other.hasOutOctets():
                self.outOctets += other.outOctets
        
        if self.hasInOctets():
            if other.hasInOctets():
                self.inOctets += other.inOctets
        
        
        pass


    # has...() methods

    def hasOutErrorPackets (self):
        return self._myHasOutErrorPackets

    def hasInErrorPackets (self):
        return self._myHasInErrorPackets

    def hasInDiscardPackets (self):
        return self._myHasInDiscardPackets

    def hasOutUnicastPackets (self):
        return self._myHasOutUnicastPackets

    def hasInMulticastPackets (self):
        return self._myHasInMulticastPackets

    def hasOutBroadcastPackets (self):
        return self._myHasOutBroadcastPackets

    def hasInBroadcastPackets (self):
        return self._myHasInBroadcastPackets

    def hasOutMulticastPackets (self):
        return self._myHasOutMulticastPackets

    def hasInUnknownProtocolPackets (self):
        return self._myHasInUnknownProtocolPackets

    def hasOutDiscardPackets (self):
        return self._myHasOutDiscardPackets

    def hasInUnicastPackets (self):
        return self._myHasInUnicastPackets

    def hasOutOctets (self):
        return self._myHasOutOctets

    def hasInOctets (self):
        return self._myHasInOctets




    # setHas...() methods

    def setHasOutErrorPackets (self):
        self._myHasOutErrorPackets=True

    def setHasInErrorPackets (self):
        self._myHasInErrorPackets=True

    def setHasInDiscardPackets (self):
        self._myHasInDiscardPackets=True

    def setHasOutUnicastPackets (self):
        self._myHasOutUnicastPackets=True

    def setHasInMulticastPackets (self):
        self._myHasInMulticastPackets=True

    def setHasOutBroadcastPackets (self):
        self._myHasOutBroadcastPackets=True

    def setHasInBroadcastPackets (self):
        self._myHasInBroadcastPackets=True

    def setHasOutMulticastPackets (self):
        self._myHasOutMulticastPackets=True

    def setHasInUnknownProtocolPackets (self):
        self._myHasInUnknownProtocolPackets=True

    def setHasOutDiscardPackets (self):
        self._myHasOutDiscardPackets=True

    def setHasInUnicastPackets (self):
        self._myHasInUnicastPackets=True

    def setHasOutOctets (self):
        self._myHasOutOctets=True

    def setHasInOctets (self):
        self._myHasInOctets=True




    # isRequested...() methods

    def isOutErrorPacketsRequested (self):
        return self._myOutErrorPacketsRequested

    def isInErrorPacketsRequested (self):
        return self._myInErrorPacketsRequested

    def isInDiscardPacketsRequested (self):
        return self._myInDiscardPacketsRequested

    def isOutUnicastPacketsRequested (self):
        return self._myOutUnicastPacketsRequested

    def isInMulticastPacketsRequested (self):
        return self._myInMulticastPacketsRequested

    def isOutBroadcastPacketsRequested (self):
        return self._myOutBroadcastPacketsRequested

    def isInBroadcastPacketsRequested (self):
        return self._myInBroadcastPacketsRequested

    def isOutMulticastPacketsRequested (self):
        return self._myOutMulticastPacketsRequested

    def isInUnknownProtocolPacketsRequested (self):
        return self._myInUnknownProtocolPacketsRequested

    def isOutDiscardPacketsRequested (self):
        return self._myOutDiscardPacketsRequested

    def isInUnicastPacketsRequested (self):
        return self._myInUnicastPacketsRequested

    def isOutOctetsRequested (self):
        return self._myOutOctetsRequested

    def isInOctetsRequested (self):
        return self._myInOctetsRequested




    # setRequested...() methods

    def setOutErrorPacketsRequested (self):
        self._myOutErrorPacketsRequested=True

    def setInErrorPacketsRequested (self):
        self._myInErrorPacketsRequested=True

    def setInDiscardPacketsRequested (self):
        self._myInDiscardPacketsRequested=True

    def setOutUnicastPacketsRequested (self):
        self._myOutUnicastPacketsRequested=True

    def setInMulticastPacketsRequested (self):
        self._myInMulticastPacketsRequested=True

    def setOutBroadcastPacketsRequested (self):
        self._myOutBroadcastPacketsRequested=True

    def setInBroadcastPacketsRequested (self):
        self._myInBroadcastPacketsRequested=True

    def setOutMulticastPacketsRequested (self):
        self._myOutMulticastPacketsRequested=True

    def setInUnknownProtocolPacketsRequested (self):
        self._myInUnknownProtocolPacketsRequested=True

    def setOutDiscardPacketsRequested (self):
        self._myOutDiscardPacketsRequested=True

    def setInUnicastPacketsRequested (self):
        self._myInUnicastPacketsRequested=True

    def setOutOctetsRequested (self):
        self._myOutOctetsRequested=True

    def setInOctetsRequested (self):
        self._myInOctetsRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myOutErrorPacketsRequested:
            x = "+OutErrorPackets="
            if self._myHasOutErrorPackets:
                leafStr = str(self.outErrorPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInErrorPacketsRequested:
            x = "+InErrorPackets="
            if self._myHasInErrorPackets:
                leafStr = str(self.inErrorPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInDiscardPacketsRequested:
            x = "+InDiscardPackets="
            if self._myHasInDiscardPackets:
                leafStr = str(self.inDiscardPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOutUnicastPacketsRequested:
            x = "+OutUnicastPackets="
            if self._myHasOutUnicastPackets:
                leafStr = str(self.outUnicastPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInMulticastPacketsRequested:
            x = "+InMulticastPackets="
            if self._myHasInMulticastPackets:
                leafStr = str(self.inMulticastPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOutBroadcastPacketsRequested:
            x = "+OutBroadcastPackets="
            if self._myHasOutBroadcastPackets:
                leafStr = str(self.outBroadcastPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInBroadcastPacketsRequested:
            x = "+InBroadcastPackets="
            if self._myHasInBroadcastPackets:
                leafStr = str(self.inBroadcastPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOutMulticastPacketsRequested:
            x = "+OutMulticastPackets="
            if self._myHasOutMulticastPackets:
                leafStr = str(self.outMulticastPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInUnknownProtocolPacketsRequested:
            x = "+InUnknownProtocolPackets="
            if self._myHasInUnknownProtocolPackets:
                leafStr = str(self.inUnknownProtocolPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOutDiscardPacketsRequested:
            x = "+OutDiscardPackets="
            if self._myHasOutDiscardPackets:
                leafStr = str(self.outDiscardPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInUnicastPacketsRequested:
            x = "+InUnicastPackets="
            if self._myHasInUnicastPackets:
                leafStr = str(self.inUnicastPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOutOctetsRequested:
            x = "+OutOctets="
            if self._myHasOutOctets:
                leafStr = str(self.outOctets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInOctetsRequested:
            x = "+InOctets="
            if self._myHasInOctets:
                leafStr = str(self.inOctets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)


        return "{ContinuousCounters32BitOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+OutErrorPackets="
        if self._myHasOutErrorPackets:
            leafStr = str(self.outErrorPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOutErrorPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InErrorPackets="
        if self._myHasInErrorPackets:
            leafStr = str(self.inErrorPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInErrorPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InDiscardPackets="
        if self._myHasInDiscardPackets:
            leafStr = str(self.inDiscardPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInDiscardPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OutUnicastPackets="
        if self._myHasOutUnicastPackets:
            leafStr = str(self.outUnicastPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOutUnicastPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InMulticastPackets="
        if self._myHasInMulticastPackets:
            leafStr = str(self.inMulticastPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInMulticastPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OutBroadcastPackets="
        if self._myHasOutBroadcastPackets:
            leafStr = str(self.outBroadcastPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOutBroadcastPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InBroadcastPackets="
        if self._myHasInBroadcastPackets:
            leafStr = str(self.inBroadcastPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInBroadcastPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OutMulticastPackets="
        if self._myHasOutMulticastPackets:
            leafStr = str(self.outMulticastPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOutMulticastPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InUnknownProtocolPackets="
        if self._myHasInUnknownProtocolPackets:
            leafStr = str(self.inUnknownProtocolPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInUnknownProtocolPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OutDiscardPackets="
        if self._myHasOutDiscardPackets:
            leafStr = str(self.outDiscardPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOutDiscardPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InUnicastPackets="
        if self._myHasInUnicastPackets:
            leafStr = str(self.inUnicastPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInUnicastPacketsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OutOctets="
        if self._myHasOutOctets:
            leafStr = str(self.outOctets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOutOctetsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InOctets="
        if self._myHasInOctets:
            leafStr = str(self.inOctets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInOctetsRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)


        return "{ContinuousCounters32BitOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setOutErrorPacketsRequested()
        self.setInErrorPacketsRequested()
        self.setInDiscardPacketsRequested()
        self.setOutUnicastPacketsRequested()
        self.setInMulticastPacketsRequested()
        self.setOutBroadcastPacketsRequested()
        self.setInBroadcastPacketsRequested()
        self.setOutMulticastPacketsRequested()
        self.setInUnknownProtocolPacketsRequested()
        self.setOutDiscardPacketsRequested()
        self.setInUnicastPacketsRequested()
        self.setOutOctetsRequested()
        self.setInOctetsRequested()
        
        


    def setOutErrorPackets (self, outErrorPackets):
        self.outErrorPackets = outErrorPackets
        self.setHasOutErrorPackets()

    def setInErrorPackets (self, inErrorPackets):
        self.inErrorPackets = inErrorPackets
        self.setHasInErrorPackets()

    def setInDiscardPackets (self, inDiscardPackets):
        self.inDiscardPackets = inDiscardPackets
        self.setHasInDiscardPackets()

    def setOutUnicastPackets (self, outUnicastPackets):
        self.outUnicastPackets = outUnicastPackets
        self.setHasOutUnicastPackets()

    def setInMulticastPackets (self, inMulticastPackets):
        self.inMulticastPackets = inMulticastPackets
        self.setHasInMulticastPackets()

    def setOutBroadcastPackets (self, outBroadcastPackets):
        self.outBroadcastPackets = outBroadcastPackets
        self.setHasOutBroadcastPackets()

    def setInBroadcastPackets (self, inBroadcastPackets):
        self.inBroadcastPackets = inBroadcastPackets
        self.setHasInBroadcastPackets()

    def setOutMulticastPackets (self, outMulticastPackets):
        self.outMulticastPackets = outMulticastPackets
        self.setHasOutMulticastPackets()

    def setInUnknownProtocolPackets (self, inUnknownProtocolPackets):
        self.inUnknownProtocolPackets = inUnknownProtocolPackets
        self.setHasInUnknownProtocolPackets()

    def setOutDiscardPackets (self, outDiscardPackets):
        self.outDiscardPackets = outDiscardPackets
        self.setHasOutDiscardPackets()

    def setInUnicastPackets (self, inUnicastPackets):
        self.inUnicastPackets = inUnicastPackets
        self.setHasInUnicastPackets()

    def setOutOctets (self, outOctets):
        self.outOctets = outOctets
        self.setHasOutOctets()

    def setInOctets (self, inOctets):
        self.inOctets = inOctets
        self.setHasInOctets()


"""
Extracted from the below data: 
{
    "node": {
        "className": "ContinuousCounters32BitOperData", 
        "namespace": "continuous_counters_32bit", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.continuous_counters_32bit.continuous_counters_32bit_oper_data_gen import ContinuousCounters32BitOperData"
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
            "namespace": "interface", 
            "isCurrent": false
        }, 
        {
            "namespace": "continuous_counters_32bit", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outErrorPackets", 
            "yangName": "out-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inErrorPackets", 
            "yangName": "in-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inDiscardPackets", 
            "yangName": "in-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outUnicastPackets", 
            "yangName": "out-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inMulticastPackets", 
            "yangName": "in-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBroadcastPackets", 
            "yangName": "out-broadcast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBroadcastPackets", 
            "yangName": "in-broadcast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outMulticastPackets", 
            "yangName": "out-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnknownProtocolPackets", 
            "yangName": "in-unknown-protocol-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outDiscardPackets", 
            "yangName": "out-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnicastPackets", 
            "yangName": "in-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outOctets", 
            "yangName": "out-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inOctets", 
            "yangName": "in-octets", 
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


