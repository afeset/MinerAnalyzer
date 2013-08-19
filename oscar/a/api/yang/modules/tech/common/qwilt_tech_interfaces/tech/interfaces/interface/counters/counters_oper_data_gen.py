


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

        self.outGratuitousArpPackets = 0
        self._myHasOutGratuitousArpPackets=False
        self._myOutGratuitousArpPacketsRequested=False
        
        self.outUnicastPackets = 0
        self._myHasOutUnicastPackets=False
        self._myOutUnicastPacketsRequested=False
        
        self.inUnknownProtocolPackets = 0
        self._myHasInUnknownProtocolPackets=False
        self._myInUnknownProtocolPacketsRequested=False
        
        self.outDiscardPackets = 0
        self._myHasOutDiscardPackets=False
        self._myOutDiscardPacketsRequested=False
        
        self.inOctets = 0
        self._myHasInOctets=False
        self._myInOctetsRequested=False
        
        self.inErrorPackets = 0
        self._myHasInErrorPackets=False
        self._myInErrorPacketsRequested=False
        
        self.inPacketsRate = 0
        self._myHasInPacketsRate=False
        self._myInPacketsRateRequested=False
        
        self.outPackets = 0
        self._myHasOutPackets=False
        self._myOutPacketsRequested=False
        
        self.inDiscardPackets = 0
        self._myHasInDiscardPackets=False
        self._myInDiscardPacketsRequested=False
        
        self.inMulticastPackets = 0
        self._myHasInMulticastPackets=False
        self._myInMulticastPacketsRequested=False
        
        self.outBroadcastPackets = 0
        self._myHasOutBroadcastPackets=False
        self._myOutBroadcastPacketsRequested=False
        
        self.outOctets = 0
        self._myHasOutOctets=False
        self._myOutOctetsRequested=False
        
        self.outMulticastPackets = 0
        self._myHasOutMulticastPackets=False
        self._myOutMulticastPacketsRequested=False
        
        self.inUnicastPackets = 0
        self._myHasInUnicastPackets=False
        self._myInUnicastPacketsRequested=False
        
        self.outErrorPackets = 0
        self._myHasOutErrorPackets=False
        self._myOutErrorPacketsRequested=False
        
        self.outPacketsRate = 0
        self._myHasOutPacketsRate=False
        self._myOutPacketsRateRequested=False
        
        self.inPackets = 0
        self._myHasInPackets=False
        self._myInPacketsRequested=False
        
        self.operationalStatusChanges = 0
        self._myHasOperationalStatusChanges=False
        self._myOperationalStatusChangesRequested=False
        
        self.inBitsRate = 0
        self._myHasInBitsRate=False
        self._myInBitsRateRequested=False
        
        self.outBitsRate = 0
        self._myHasOutBitsRate=False
        self._myOutBitsRateRequested=False
        
        self.inBroadcastPackets = 0
        self._myHasInBroadcastPackets=False
        self._myInBroadcastPacketsRequested=False
        


    def copyFrom (self, other):

        self.outGratuitousArpPackets=other.outGratuitousArpPackets
        self._myHasOutGratuitousArpPackets=other._myHasOutGratuitousArpPackets
        self._myOutGratuitousArpPacketsRequested=other._myOutGratuitousArpPacketsRequested
        
        self.outUnicastPackets=other.outUnicastPackets
        self._myHasOutUnicastPackets=other._myHasOutUnicastPackets
        self._myOutUnicastPacketsRequested=other._myOutUnicastPacketsRequested
        
        self.inUnknownProtocolPackets=other.inUnknownProtocolPackets
        self._myHasInUnknownProtocolPackets=other._myHasInUnknownProtocolPackets
        self._myInUnknownProtocolPacketsRequested=other._myInUnknownProtocolPacketsRequested
        
        self.outDiscardPackets=other.outDiscardPackets
        self._myHasOutDiscardPackets=other._myHasOutDiscardPackets
        self._myOutDiscardPacketsRequested=other._myOutDiscardPacketsRequested
        
        self.inOctets=other.inOctets
        self._myHasInOctets=other._myHasInOctets
        self._myInOctetsRequested=other._myInOctetsRequested
        
        self.inErrorPackets=other.inErrorPackets
        self._myHasInErrorPackets=other._myHasInErrorPackets
        self._myInErrorPacketsRequested=other._myInErrorPacketsRequested
        
        self.inPacketsRate=other.inPacketsRate
        self._myHasInPacketsRate=other._myHasInPacketsRate
        self._myInPacketsRateRequested=other._myInPacketsRateRequested
        
        self.outPackets=other.outPackets
        self._myHasOutPackets=other._myHasOutPackets
        self._myOutPacketsRequested=other._myOutPacketsRequested
        
        self.inDiscardPackets=other.inDiscardPackets
        self._myHasInDiscardPackets=other._myHasInDiscardPackets
        self._myInDiscardPacketsRequested=other._myInDiscardPacketsRequested
        
        self.inMulticastPackets=other.inMulticastPackets
        self._myHasInMulticastPackets=other._myHasInMulticastPackets
        self._myInMulticastPacketsRequested=other._myInMulticastPacketsRequested
        
        self.outBroadcastPackets=other.outBroadcastPackets
        self._myHasOutBroadcastPackets=other._myHasOutBroadcastPackets
        self._myOutBroadcastPacketsRequested=other._myOutBroadcastPacketsRequested
        
        self.outOctets=other.outOctets
        self._myHasOutOctets=other._myHasOutOctets
        self._myOutOctetsRequested=other._myOutOctetsRequested
        
        self.outMulticastPackets=other.outMulticastPackets
        self._myHasOutMulticastPackets=other._myHasOutMulticastPackets
        self._myOutMulticastPacketsRequested=other._myOutMulticastPacketsRequested
        
        self.inUnicastPackets=other.inUnicastPackets
        self._myHasInUnicastPackets=other._myHasInUnicastPackets
        self._myInUnicastPacketsRequested=other._myInUnicastPacketsRequested
        
        self.outErrorPackets=other.outErrorPackets
        self._myHasOutErrorPackets=other._myHasOutErrorPackets
        self._myOutErrorPacketsRequested=other._myOutErrorPacketsRequested
        
        self.outPacketsRate=other.outPacketsRate
        self._myHasOutPacketsRate=other._myHasOutPacketsRate
        self._myOutPacketsRateRequested=other._myOutPacketsRateRequested
        
        self.inPackets=other.inPackets
        self._myHasInPackets=other._myHasInPackets
        self._myInPacketsRequested=other._myInPacketsRequested
        
        self.operationalStatusChanges=other.operationalStatusChanges
        self._myHasOperationalStatusChanges=other._myHasOperationalStatusChanges
        self._myOperationalStatusChangesRequested=other._myOperationalStatusChangesRequested
        
        self.inBitsRate=other.inBitsRate
        self._myHasInBitsRate=other._myHasInBitsRate
        self._myInBitsRateRequested=other._myInBitsRateRequested
        
        self.outBitsRate=other.outBitsRate
        self._myHasOutBitsRate=other._myHasOutBitsRate
        self._myOutBitsRateRequested=other._myOutBitsRateRequested
        
        self.inBroadcastPackets=other.inBroadcastPackets
        self._myHasInBroadcastPackets=other._myHasInBroadcastPackets
        self._myInBroadcastPacketsRequested=other._myInBroadcastPacketsRequested
        


    def copyRequestedFrom (self, other):
        """
        This method will copy from other only the leaves & descendant that are requested in ***self***
        """

        if self.isOutGratuitousArpPacketsRequested():
            self.outGratuitousArpPackets=other.outGratuitousArpPackets
            self._myHasOutGratuitousArpPackets=other._myHasOutGratuitousArpPackets
            self._myOutGratuitousArpPacketsRequested=other._myOutGratuitousArpPacketsRequested
        
        if self.isOutUnicastPacketsRequested():
            self.outUnicastPackets=other.outUnicastPackets
            self._myHasOutUnicastPackets=other._myHasOutUnicastPackets
            self._myOutUnicastPacketsRequested=other._myOutUnicastPacketsRequested
        
        if self.isInUnknownProtocolPacketsRequested():
            self.inUnknownProtocolPackets=other.inUnknownProtocolPackets
            self._myHasInUnknownProtocolPackets=other._myHasInUnknownProtocolPackets
            self._myInUnknownProtocolPacketsRequested=other._myInUnknownProtocolPacketsRequested
        
        if self.isOutDiscardPacketsRequested():
            self.outDiscardPackets=other.outDiscardPackets
            self._myHasOutDiscardPackets=other._myHasOutDiscardPackets
            self._myOutDiscardPacketsRequested=other._myOutDiscardPacketsRequested
        
        if self.isInOctetsRequested():
            self.inOctets=other.inOctets
            self._myHasInOctets=other._myHasInOctets
            self._myInOctetsRequested=other._myInOctetsRequested
        
        if self.isInErrorPacketsRequested():
            self.inErrorPackets=other.inErrorPackets
            self._myHasInErrorPackets=other._myHasInErrorPackets
            self._myInErrorPacketsRequested=other._myInErrorPacketsRequested
        
        if self.isInPacketsRateRequested():
            self.inPacketsRate=other.inPacketsRate
            self._myHasInPacketsRate=other._myHasInPacketsRate
            self._myInPacketsRateRequested=other._myInPacketsRateRequested
        
        if self.isOutPacketsRequested():
            self.outPackets=other.outPackets
            self._myHasOutPackets=other._myHasOutPackets
            self._myOutPacketsRequested=other._myOutPacketsRequested
        
        if self.isInDiscardPacketsRequested():
            self.inDiscardPackets=other.inDiscardPackets
            self._myHasInDiscardPackets=other._myHasInDiscardPackets
            self._myInDiscardPacketsRequested=other._myInDiscardPacketsRequested
        
        if self.isInMulticastPacketsRequested():
            self.inMulticastPackets=other.inMulticastPackets
            self._myHasInMulticastPackets=other._myHasInMulticastPackets
            self._myInMulticastPacketsRequested=other._myInMulticastPacketsRequested
        
        if self.isOutBroadcastPacketsRequested():
            self.outBroadcastPackets=other.outBroadcastPackets
            self._myHasOutBroadcastPackets=other._myHasOutBroadcastPackets
            self._myOutBroadcastPacketsRequested=other._myOutBroadcastPacketsRequested
        
        if self.isOutOctetsRequested():
            self.outOctets=other.outOctets
            self._myHasOutOctets=other._myHasOutOctets
            self._myOutOctetsRequested=other._myOutOctetsRequested
        
        if self.isOutMulticastPacketsRequested():
            self.outMulticastPackets=other.outMulticastPackets
            self._myHasOutMulticastPackets=other._myHasOutMulticastPackets
            self._myOutMulticastPacketsRequested=other._myOutMulticastPacketsRequested
        
        if self.isInUnicastPacketsRequested():
            self.inUnicastPackets=other.inUnicastPackets
            self._myHasInUnicastPackets=other._myHasInUnicastPackets
            self._myInUnicastPacketsRequested=other._myInUnicastPacketsRequested
        
        if self.isOutErrorPacketsRequested():
            self.outErrorPackets=other.outErrorPackets
            self._myHasOutErrorPackets=other._myHasOutErrorPackets
            self._myOutErrorPacketsRequested=other._myOutErrorPacketsRequested
        
        if self.isOutPacketsRateRequested():
            self.outPacketsRate=other.outPacketsRate
            self._myHasOutPacketsRate=other._myHasOutPacketsRate
            self._myOutPacketsRateRequested=other._myOutPacketsRateRequested
        
        if self.isInPacketsRequested():
            self.inPackets=other.inPackets
            self._myHasInPackets=other._myHasInPackets
            self._myInPacketsRequested=other._myInPacketsRequested
        
        if self.isOperationalStatusChangesRequested():
            self.operationalStatusChanges=other.operationalStatusChanges
            self._myHasOperationalStatusChanges=other._myHasOperationalStatusChanges
            self._myOperationalStatusChangesRequested=other._myOperationalStatusChangesRequested
        
        if self.isInBitsRateRequested():
            self.inBitsRate=other.inBitsRate
            self._myHasInBitsRate=other._myHasInBitsRate
            self._myInBitsRateRequested=other._myInBitsRateRequested
        
        if self.isOutBitsRateRequested():
            self.outBitsRate=other.outBitsRate
            self._myHasOutBitsRate=other._myHasOutBitsRate
            self._myOutBitsRateRequested=other._myOutBitsRateRequested
        
        if self.isInBroadcastPacketsRequested():
            self.inBroadcastPackets=other.inBroadcastPackets
            self._myHasInBroadcastPackets=other._myHasInBroadcastPackets
            self._myInBroadcastPacketsRequested=other._myInBroadcastPacketsRequested
        


    def copySetFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that are set in ***other***
        """

        if other.hasOutGratuitousArpPackets():
            self.outGratuitousArpPackets=other.outGratuitousArpPackets
            self._myHasOutGratuitousArpPackets=other._myHasOutGratuitousArpPackets
            self._myOutGratuitousArpPacketsRequested=other._myOutGratuitousArpPacketsRequested
        
        if other.hasOutUnicastPackets():
            self.outUnicastPackets=other.outUnicastPackets
            self._myHasOutUnicastPackets=other._myHasOutUnicastPackets
            self._myOutUnicastPacketsRequested=other._myOutUnicastPacketsRequested
        
        if other.hasInUnknownProtocolPackets():
            self.inUnknownProtocolPackets=other.inUnknownProtocolPackets
            self._myHasInUnknownProtocolPackets=other._myHasInUnknownProtocolPackets
            self._myInUnknownProtocolPacketsRequested=other._myInUnknownProtocolPacketsRequested
        
        if other.hasOutDiscardPackets():
            self.outDiscardPackets=other.outDiscardPackets
            self._myHasOutDiscardPackets=other._myHasOutDiscardPackets
            self._myOutDiscardPacketsRequested=other._myOutDiscardPacketsRequested
        
        if other.hasInOctets():
            self.inOctets=other.inOctets
            self._myHasInOctets=other._myHasInOctets
            self._myInOctetsRequested=other._myInOctetsRequested
        
        if other.hasInErrorPackets():
            self.inErrorPackets=other.inErrorPackets
            self._myHasInErrorPackets=other._myHasInErrorPackets
            self._myInErrorPacketsRequested=other._myInErrorPacketsRequested
        
        if other.hasInPacketsRate():
            self.inPacketsRate=other.inPacketsRate
            self._myHasInPacketsRate=other._myHasInPacketsRate
            self._myInPacketsRateRequested=other._myInPacketsRateRequested
        
        if other.hasOutPackets():
            self.outPackets=other.outPackets
            self._myHasOutPackets=other._myHasOutPackets
            self._myOutPacketsRequested=other._myOutPacketsRequested
        
        if other.hasInDiscardPackets():
            self.inDiscardPackets=other.inDiscardPackets
            self._myHasInDiscardPackets=other._myHasInDiscardPackets
            self._myInDiscardPacketsRequested=other._myInDiscardPacketsRequested
        
        if other.hasInMulticastPackets():
            self.inMulticastPackets=other.inMulticastPackets
            self._myHasInMulticastPackets=other._myHasInMulticastPackets
            self._myInMulticastPacketsRequested=other._myInMulticastPacketsRequested
        
        if other.hasOutBroadcastPackets():
            self.outBroadcastPackets=other.outBroadcastPackets
            self._myHasOutBroadcastPackets=other._myHasOutBroadcastPackets
            self._myOutBroadcastPacketsRequested=other._myOutBroadcastPacketsRequested
        
        if other.hasOutOctets():
            self.outOctets=other.outOctets
            self._myHasOutOctets=other._myHasOutOctets
            self._myOutOctetsRequested=other._myOutOctetsRequested
        
        if other.hasOutMulticastPackets():
            self.outMulticastPackets=other.outMulticastPackets
            self._myHasOutMulticastPackets=other._myHasOutMulticastPackets
            self._myOutMulticastPacketsRequested=other._myOutMulticastPacketsRequested
        
        if other.hasInUnicastPackets():
            self.inUnicastPackets=other.inUnicastPackets
            self._myHasInUnicastPackets=other._myHasInUnicastPackets
            self._myInUnicastPacketsRequested=other._myInUnicastPacketsRequested
        
        if other.hasOutErrorPackets():
            self.outErrorPackets=other.outErrorPackets
            self._myHasOutErrorPackets=other._myHasOutErrorPackets
            self._myOutErrorPacketsRequested=other._myOutErrorPacketsRequested
        
        if other.hasOutPacketsRate():
            self.outPacketsRate=other.outPacketsRate
            self._myHasOutPacketsRate=other._myHasOutPacketsRate
            self._myOutPacketsRateRequested=other._myOutPacketsRateRequested
        
        if other.hasInPackets():
            self.inPackets=other.inPackets
            self._myHasInPackets=other._myHasInPackets
            self._myInPacketsRequested=other._myInPacketsRequested
        
        if other.hasOperationalStatusChanges():
            self.operationalStatusChanges=other.operationalStatusChanges
            self._myHasOperationalStatusChanges=other._myHasOperationalStatusChanges
            self._myOperationalStatusChangesRequested=other._myOperationalStatusChangesRequested
        
        if other.hasInBitsRate():
            self.inBitsRate=other.inBitsRate
            self._myHasInBitsRate=other._myHasInBitsRate
            self._myInBitsRateRequested=other._myInBitsRateRequested
        
        if other.hasOutBitsRate():
            self.outBitsRate=other.outBitsRate
            self._myHasOutBitsRate=other._myHasOutBitsRate
            self._myOutBitsRateRequested=other._myOutBitsRateRequested
        
        if other.hasInBroadcastPackets():
            self.inBroadcastPackets=other.inBroadcastPackets
            self._myHasInBroadcastPackets=other._myHasInBroadcastPackets
            self._myInBroadcastPacketsRequested=other._myInBroadcastPacketsRequested
        


    def copyDataFrom (self, other):
        """
        This method will copy to self only the leaves & descendant that and their "has" values from ***other***. 
        It will leave "requested" fields unchanged
        """

        self.outGratuitousArpPackets=other.outGratuitousArpPackets
        self._myHasOutGratuitousArpPackets=other._myHasOutGratuitousArpPackets
        
        self.outUnicastPackets=other.outUnicastPackets
        self._myHasOutUnicastPackets=other._myHasOutUnicastPackets
        
        self.inUnknownProtocolPackets=other.inUnknownProtocolPackets
        self._myHasInUnknownProtocolPackets=other._myHasInUnknownProtocolPackets
        
        self.outDiscardPackets=other.outDiscardPackets
        self._myHasOutDiscardPackets=other._myHasOutDiscardPackets
        
        self.inOctets=other.inOctets
        self._myHasInOctets=other._myHasInOctets
        
        self.inErrorPackets=other.inErrorPackets
        self._myHasInErrorPackets=other._myHasInErrorPackets
        
        self.inPacketsRate=other.inPacketsRate
        self._myHasInPacketsRate=other._myHasInPacketsRate
        
        self.outPackets=other.outPackets
        self._myHasOutPackets=other._myHasOutPackets
        
        self.inDiscardPackets=other.inDiscardPackets
        self._myHasInDiscardPackets=other._myHasInDiscardPackets
        
        self.inMulticastPackets=other.inMulticastPackets
        self._myHasInMulticastPackets=other._myHasInMulticastPackets
        
        self.outBroadcastPackets=other.outBroadcastPackets
        self._myHasOutBroadcastPackets=other._myHasOutBroadcastPackets
        
        self.outOctets=other.outOctets
        self._myHasOutOctets=other._myHasOutOctets
        
        self.outMulticastPackets=other.outMulticastPackets
        self._myHasOutMulticastPackets=other._myHasOutMulticastPackets
        
        self.inUnicastPackets=other.inUnicastPackets
        self._myHasInUnicastPackets=other._myHasInUnicastPackets
        
        self.outErrorPackets=other.outErrorPackets
        self._myHasOutErrorPackets=other._myHasOutErrorPackets
        
        self.outPacketsRate=other.outPacketsRate
        self._myHasOutPacketsRate=other._myHasOutPacketsRate
        
        self.inPackets=other.inPackets
        self._myHasInPackets=other._myHasInPackets
        
        self.operationalStatusChanges=other.operationalStatusChanges
        self._myHasOperationalStatusChanges=other._myHasOperationalStatusChanges
        
        self.inBitsRate=other.inBitsRate
        self._myHasInBitsRate=other._myHasInBitsRate
        
        self.outBitsRate=other.outBitsRate
        self._myHasOutBitsRate=other._myHasOutBitsRate
        
        self.inBroadcastPackets=other.inBroadcastPackets
        self._myHasInBroadcastPackets=other._myHasInBroadcastPackets
        


    def setAllNumericToZero (self):
        
        self.outGratuitousArpPackets=0
        self.setHasOutGratuitousArpPackets()
        self.outUnicastPackets=0
        self.setHasOutUnicastPackets()
        self.inUnknownProtocolPackets=0
        self.setHasInUnknownProtocolPackets()
        self.outDiscardPackets=0
        self.setHasOutDiscardPackets()
        self.inOctets=0
        self.setHasInOctets()
        self.inErrorPackets=0
        self.setHasInErrorPackets()
        self.inPacketsRate=0
        self.setHasInPacketsRate()
        self.outPackets=0
        self.setHasOutPackets()
        self.inDiscardPackets=0
        self.setHasInDiscardPackets()
        self.inMulticastPackets=0
        self.setHasInMulticastPackets()
        self.outBroadcastPackets=0
        self.setHasOutBroadcastPackets()
        self.outOctets=0
        self.setHasOutOctets()
        self.outMulticastPackets=0
        self.setHasOutMulticastPackets()
        self.inUnicastPackets=0
        self.setHasInUnicastPackets()
        self.outErrorPackets=0
        self.setHasOutErrorPackets()
        self.outPacketsRate=0
        self.setHasOutPacketsRate()
        self.inPackets=0
        self.setHasInPackets()
        self.operationalStatusChanges=0
        self.setHasOperationalStatusChanges()
        self.inBitsRate=0
        self.setHasInBitsRate()
        self.outBitsRate=0
        self.setHasOutBitsRate()
        self.inBroadcastPackets=0
        self.setHasInBroadcastPackets()
        
        pass

    def subtractAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasOutGratuitousArpPackets():
            if other.hasOutGratuitousArpPackets():
                self.outGratuitousArpPackets -= other.outGratuitousArpPackets
        
        if self.hasOutUnicastPackets():
            if other.hasOutUnicastPackets():
                self.outUnicastPackets -= other.outUnicastPackets
        
        if self.hasInUnknownProtocolPackets():
            if other.hasInUnknownProtocolPackets():
                self.inUnknownProtocolPackets -= other.inUnknownProtocolPackets
        
        if self.hasOutDiscardPackets():
            if other.hasOutDiscardPackets():
                self.outDiscardPackets -= other.outDiscardPackets
        
        if self.hasInOctets():
            if other.hasInOctets():
                self.inOctets -= other.inOctets
        
        if self.hasInErrorPackets():
            if other.hasInErrorPackets():
                self.inErrorPackets -= other.inErrorPackets
        
        if self.hasInPacketsRate():
            if other.hasInPacketsRate():
                self.inPacketsRate -= other.inPacketsRate
        
        if self.hasOutPackets():
            if other.hasOutPackets():
                self.outPackets -= other.outPackets
        
        if self.hasInDiscardPackets():
            if other.hasInDiscardPackets():
                self.inDiscardPackets -= other.inDiscardPackets
        
        if self.hasInMulticastPackets():
            if other.hasInMulticastPackets():
                self.inMulticastPackets -= other.inMulticastPackets
        
        if self.hasOutBroadcastPackets():
            if other.hasOutBroadcastPackets():
                self.outBroadcastPackets -= other.outBroadcastPackets
        
        if self.hasOutOctets():
            if other.hasOutOctets():
                self.outOctets -= other.outOctets
        
        if self.hasOutMulticastPackets():
            if other.hasOutMulticastPackets():
                self.outMulticastPackets -= other.outMulticastPackets
        
        if self.hasInUnicastPackets():
            if other.hasInUnicastPackets():
                self.inUnicastPackets -= other.inUnicastPackets
        
        if self.hasOutErrorPackets():
            if other.hasOutErrorPackets():
                self.outErrorPackets -= other.outErrorPackets
        
        if self.hasOutPacketsRate():
            if other.hasOutPacketsRate():
                self.outPacketsRate -= other.outPacketsRate
        
        if self.hasInPackets():
            if other.hasInPackets():
                self.inPackets -= other.inPackets
        
        if self.hasOperationalStatusChanges():
            if other.hasOperationalStatusChanges():
                self.operationalStatusChanges -= other.operationalStatusChanges
        
        if self.hasInBitsRate():
            if other.hasInBitsRate():
                self.inBitsRate -= other.inBitsRate
        
        if self.hasOutBitsRate():
            if other.hasOutBitsRate():
                self.outBitsRate -= other.outBitsRate
        
        if self.hasInBroadcastPackets():
            if other.hasInBroadcastPackets():
                self.inBroadcastPackets -= other.inBroadcastPackets
        
        
        pass


    def addAllNumericHas (self, other):
        """
        Only *numeric* members with *has* flag set to on will be subtracted
        """
        
        if self.hasOutGratuitousArpPackets():
            if other.hasOutGratuitousArpPackets():
                self.outGratuitousArpPackets += other.outGratuitousArpPackets
        
        if self.hasOutUnicastPackets():
            if other.hasOutUnicastPackets():
                self.outUnicastPackets += other.outUnicastPackets
        
        if self.hasInUnknownProtocolPackets():
            if other.hasInUnknownProtocolPackets():
                self.inUnknownProtocolPackets += other.inUnknownProtocolPackets
        
        if self.hasOutDiscardPackets():
            if other.hasOutDiscardPackets():
                self.outDiscardPackets += other.outDiscardPackets
        
        if self.hasInOctets():
            if other.hasInOctets():
                self.inOctets += other.inOctets
        
        if self.hasInErrorPackets():
            if other.hasInErrorPackets():
                self.inErrorPackets += other.inErrorPackets
        
        if self.hasInPacketsRate():
            if other.hasInPacketsRate():
                self.inPacketsRate += other.inPacketsRate
        
        if self.hasOutPackets():
            if other.hasOutPackets():
                self.outPackets += other.outPackets
        
        if self.hasInDiscardPackets():
            if other.hasInDiscardPackets():
                self.inDiscardPackets += other.inDiscardPackets
        
        if self.hasInMulticastPackets():
            if other.hasInMulticastPackets():
                self.inMulticastPackets += other.inMulticastPackets
        
        if self.hasOutBroadcastPackets():
            if other.hasOutBroadcastPackets():
                self.outBroadcastPackets += other.outBroadcastPackets
        
        if self.hasOutOctets():
            if other.hasOutOctets():
                self.outOctets += other.outOctets
        
        if self.hasOutMulticastPackets():
            if other.hasOutMulticastPackets():
                self.outMulticastPackets += other.outMulticastPackets
        
        if self.hasInUnicastPackets():
            if other.hasInUnicastPackets():
                self.inUnicastPackets += other.inUnicastPackets
        
        if self.hasOutErrorPackets():
            if other.hasOutErrorPackets():
                self.outErrorPackets += other.outErrorPackets
        
        if self.hasOutPacketsRate():
            if other.hasOutPacketsRate():
                self.outPacketsRate += other.outPacketsRate
        
        if self.hasInPackets():
            if other.hasInPackets():
                self.inPackets += other.inPackets
        
        if self.hasOperationalStatusChanges():
            if other.hasOperationalStatusChanges():
                self.operationalStatusChanges += other.operationalStatusChanges
        
        if self.hasInBitsRate():
            if other.hasInBitsRate():
                self.inBitsRate += other.inBitsRate
        
        if self.hasOutBitsRate():
            if other.hasOutBitsRate():
                self.outBitsRate += other.outBitsRate
        
        if self.hasInBroadcastPackets():
            if other.hasInBroadcastPackets():
                self.inBroadcastPackets += other.inBroadcastPackets
        
        
        pass


    # has...() methods

    def hasOutGratuitousArpPackets (self):
        return self._myHasOutGratuitousArpPackets

    def hasOutUnicastPackets (self):
        return self._myHasOutUnicastPackets

    def hasInUnknownProtocolPackets (self):
        return self._myHasInUnknownProtocolPackets

    def hasOutDiscardPackets (self):
        return self._myHasOutDiscardPackets

    def hasInOctets (self):
        return self._myHasInOctets

    def hasInErrorPackets (self):
        return self._myHasInErrorPackets

    def hasInPacketsRate (self):
        return self._myHasInPacketsRate

    def hasOutPackets (self):
        return self._myHasOutPackets

    def hasInDiscardPackets (self):
        return self._myHasInDiscardPackets

    def hasInMulticastPackets (self):
        return self._myHasInMulticastPackets

    def hasOutBroadcastPackets (self):
        return self._myHasOutBroadcastPackets

    def hasOutOctets (self):
        return self._myHasOutOctets

    def hasOutMulticastPackets (self):
        return self._myHasOutMulticastPackets

    def hasInUnicastPackets (self):
        return self._myHasInUnicastPackets

    def hasOutErrorPackets (self):
        return self._myHasOutErrorPackets

    def hasOutPacketsRate (self):
        return self._myHasOutPacketsRate

    def hasInPackets (self):
        return self._myHasInPackets

    def hasOperationalStatusChanges (self):
        return self._myHasOperationalStatusChanges

    def hasInBitsRate (self):
        return self._myHasInBitsRate

    def hasOutBitsRate (self):
        return self._myHasOutBitsRate

    def hasInBroadcastPackets (self):
        return self._myHasInBroadcastPackets




    # setHas...() methods

    def setHasOutGratuitousArpPackets (self):
        self._myHasOutGratuitousArpPackets=True

    def setHasOutUnicastPackets (self):
        self._myHasOutUnicastPackets=True

    def setHasInUnknownProtocolPackets (self):
        self._myHasInUnknownProtocolPackets=True

    def setHasOutDiscardPackets (self):
        self._myHasOutDiscardPackets=True

    def setHasInOctets (self):
        self._myHasInOctets=True

    def setHasInErrorPackets (self):
        self._myHasInErrorPackets=True

    def setHasInPacketsRate (self):
        self._myHasInPacketsRate=True

    def setHasOutPackets (self):
        self._myHasOutPackets=True

    def setHasInDiscardPackets (self):
        self._myHasInDiscardPackets=True

    def setHasInMulticastPackets (self):
        self._myHasInMulticastPackets=True

    def setHasOutBroadcastPackets (self):
        self._myHasOutBroadcastPackets=True

    def setHasOutOctets (self):
        self._myHasOutOctets=True

    def setHasOutMulticastPackets (self):
        self._myHasOutMulticastPackets=True

    def setHasInUnicastPackets (self):
        self._myHasInUnicastPackets=True

    def setHasOutErrorPackets (self):
        self._myHasOutErrorPackets=True

    def setHasOutPacketsRate (self):
        self._myHasOutPacketsRate=True

    def setHasInPackets (self):
        self._myHasInPackets=True

    def setHasOperationalStatusChanges (self):
        self._myHasOperationalStatusChanges=True

    def setHasInBitsRate (self):
        self._myHasInBitsRate=True

    def setHasOutBitsRate (self):
        self._myHasOutBitsRate=True

    def setHasInBroadcastPackets (self):
        self._myHasInBroadcastPackets=True




    # isRequested...() methods

    def isOutGratuitousArpPacketsRequested (self):
        return self._myOutGratuitousArpPacketsRequested

    def isOutUnicastPacketsRequested (self):
        return self._myOutUnicastPacketsRequested

    def isInUnknownProtocolPacketsRequested (self):
        return self._myInUnknownProtocolPacketsRequested

    def isOutDiscardPacketsRequested (self):
        return self._myOutDiscardPacketsRequested

    def isInOctetsRequested (self):
        return self._myInOctetsRequested

    def isInErrorPacketsRequested (self):
        return self._myInErrorPacketsRequested

    def isInPacketsRateRequested (self):
        return self._myInPacketsRateRequested

    def isOutPacketsRequested (self):
        return self._myOutPacketsRequested

    def isInDiscardPacketsRequested (self):
        return self._myInDiscardPacketsRequested

    def isInMulticastPacketsRequested (self):
        return self._myInMulticastPacketsRequested

    def isOutBroadcastPacketsRequested (self):
        return self._myOutBroadcastPacketsRequested

    def isOutOctetsRequested (self):
        return self._myOutOctetsRequested

    def isOutMulticastPacketsRequested (self):
        return self._myOutMulticastPacketsRequested

    def isInUnicastPacketsRequested (self):
        return self._myInUnicastPacketsRequested

    def isOutErrorPacketsRequested (self):
        return self._myOutErrorPacketsRequested

    def isOutPacketsRateRequested (self):
        return self._myOutPacketsRateRequested

    def isInPacketsRequested (self):
        return self._myInPacketsRequested

    def isOperationalStatusChangesRequested (self):
        return self._myOperationalStatusChangesRequested

    def isInBitsRateRequested (self):
        return self._myInBitsRateRequested

    def isOutBitsRateRequested (self):
        return self._myOutBitsRateRequested

    def isInBroadcastPacketsRequested (self):
        return self._myInBroadcastPacketsRequested




    # setRequested...() methods

    def setOutGratuitousArpPacketsRequested (self):
        self._myOutGratuitousArpPacketsRequested=True

    def setOutUnicastPacketsRequested (self):
        self._myOutUnicastPacketsRequested=True

    def setInUnknownProtocolPacketsRequested (self):
        self._myInUnknownProtocolPacketsRequested=True

    def setOutDiscardPacketsRequested (self):
        self._myOutDiscardPacketsRequested=True

    def setInOctetsRequested (self):
        self._myInOctetsRequested=True

    def setInErrorPacketsRequested (self):
        self._myInErrorPacketsRequested=True

    def setInPacketsRateRequested (self):
        self._myInPacketsRateRequested=True

    def setOutPacketsRequested (self):
        self._myOutPacketsRequested=True

    def setInDiscardPacketsRequested (self):
        self._myInDiscardPacketsRequested=True

    def setInMulticastPacketsRequested (self):
        self._myInMulticastPacketsRequested=True

    def setOutBroadcastPacketsRequested (self):
        self._myOutBroadcastPacketsRequested=True

    def setOutOctetsRequested (self):
        self._myOutOctetsRequested=True

    def setOutMulticastPacketsRequested (self):
        self._myOutMulticastPacketsRequested=True

    def setInUnicastPacketsRequested (self):
        self._myInUnicastPacketsRequested=True

    def setOutErrorPacketsRequested (self):
        self._myOutErrorPacketsRequested=True

    def setOutPacketsRateRequested (self):
        self._myOutPacketsRateRequested=True

    def setInPacketsRequested (self):
        self._myInPacketsRequested=True

    def setOperationalStatusChangesRequested (self):
        self._myOperationalStatusChangesRequested=True

    def setInBitsRateRequested (self):
        self._myInBitsRateRequested=True

    def setOutBitsRateRequested (self):
        self._myOutBitsRateRequested=True

    def setInBroadcastPacketsRequested (self):
        self._myInBroadcastPacketsRequested=True




    def __str__ (self):
        __pychecker__='maxlines=1000'
        items=[]

        x=""
        if self._myOutGratuitousArpPacketsRequested:
            x = "+OutGratuitousArpPackets="
            if self._myHasOutGratuitousArpPackets:
                leafStr = str(self.outGratuitousArpPackets)
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
        if self._myInOctetsRequested:
            x = "+InOctets="
            if self._myHasInOctets:
                leafStr = str(self.inOctets)
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
        if self._myInPacketsRateRequested:
            x = "+InPacketsRate="
            if self._myHasInPacketsRate:
                leafStr = str(self.inPacketsRate)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOutPacketsRequested:
            x = "+OutPackets="
            if self._myHasOutPackets:
                leafStr = str(self.outPackets)
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
        if self._myOutOctetsRequested:
            x = "+OutOctets="
            if self._myHasOutOctets:
                leafStr = str(self.outOctets)
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
        if self._myInUnicastPacketsRequested:
            x = "+InUnicastPackets="
            if self._myHasInUnicastPackets:
                leafStr = str(self.inUnicastPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOutErrorPacketsRequested:
            x = "+OutErrorPackets="
            if self._myHasOutErrorPackets:
                leafStr = str(self.outErrorPackets)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOutPacketsRateRequested:
            x = "+OutPacketsRate="
            if self._myHasOutPacketsRate:
                leafStr = str(self.outPacketsRate)
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
        if self._myOperationalStatusChangesRequested:
            x = "+OperationalStatusChanges="
            if self._myHasOperationalStatusChanges:
                leafStr = str(self.operationalStatusChanges)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myInBitsRateRequested:
            x = "+InBitsRate="
            if self._myHasInBitsRate:
                leafStr = str(self.inBitsRate)
            else:
                leafStr = "<UNSET>"
            items.append(x + leafStr)

        x=""
        if self._myOutBitsRateRequested:
            x = "+OutBitsRate="
            if self._myHasOutBitsRate:
                leafStr = str(self.outBitsRate)
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


        return "{CountersOperData: "+",".join(items)+"}"

    def debugStr (self, includeRequested=False):
        __pychecker__='maxlines=1000 maxbranches=100'
        items=[]

        x=""
        x = "+OutGratuitousArpPackets="
        if self._myHasOutGratuitousArpPackets:
            leafStr = str(self.outGratuitousArpPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOutGratuitousArpPacketsRequested:
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
        x = "+InPacketsRate="
        if self._myHasInPacketsRate:
            leafStr = str(self.inPacketsRate)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInPacketsRateRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OutPackets="
        if self._myHasOutPackets:
            leafStr = str(self.outPackets)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOutPacketsRequested:
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
        x = "+OutPacketsRate="
        if self._myHasOutPacketsRate:
            leafStr = str(self.outPacketsRate)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOutPacketsRateRequested:
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
        x = "+OperationalStatusChanges="
        if self._myHasOperationalStatusChanges:
            leafStr = str(self.operationalStatusChanges)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOperationalStatusChangesRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+InBitsRate="
        if self._myHasInBitsRate:
            leafStr = str(self.inBitsRate)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myInBitsRateRequested:
                requestedStr = ('(requested)')
            else:
                requestedStr = ('(not-requested)')
        items.append(x + leafStr + requestedStr)

        x=""
        x = "+OutBitsRate="
        if self._myHasOutBitsRate:
            leafStr = str(self.outBitsRate)
        else:
            leafStr = "<UNSET>"
        requestedStr = ''
        if includeRequested:
            if self._myOutBitsRateRequested:
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


        return "{CountersOperData: "+",".join(items)+"}"


    def setAllRequested(self):
        self.setOutGratuitousArpPacketsRequested()
        self.setOutUnicastPacketsRequested()
        self.setInUnknownProtocolPacketsRequested()
        self.setOutDiscardPacketsRequested()
        self.setInOctetsRequested()
        self.setInErrorPacketsRequested()
        self.setInPacketsRateRequested()
        self.setOutPacketsRequested()
        self.setInDiscardPacketsRequested()
        self.setInMulticastPacketsRequested()
        self.setOutBroadcastPacketsRequested()
        self.setOutOctetsRequested()
        self.setOutMulticastPacketsRequested()
        self.setInUnicastPacketsRequested()
        self.setOutErrorPacketsRequested()
        self.setOutPacketsRateRequested()
        self.setInPacketsRequested()
        self.setOperationalStatusChangesRequested()
        self.setInBitsRateRequested()
        self.setOutBitsRateRequested()
        self.setInBroadcastPacketsRequested()
        
        


    def setOutGratuitousArpPackets (self, outGratuitousArpPackets):
        self.outGratuitousArpPackets = outGratuitousArpPackets
        self.setHasOutGratuitousArpPackets()

    def setOutUnicastPackets (self, outUnicastPackets):
        self.outUnicastPackets = outUnicastPackets
        self.setHasOutUnicastPackets()

    def setInUnknownProtocolPackets (self, inUnknownProtocolPackets):
        self.inUnknownProtocolPackets = inUnknownProtocolPackets
        self.setHasInUnknownProtocolPackets()

    def setOutDiscardPackets (self, outDiscardPackets):
        self.outDiscardPackets = outDiscardPackets
        self.setHasOutDiscardPackets()

    def setInOctets (self, inOctets):
        self.inOctets = inOctets
        self.setHasInOctets()

    def setInErrorPackets (self, inErrorPackets):
        self.inErrorPackets = inErrorPackets
        self.setHasInErrorPackets()

    def setInPacketsRate (self, inPacketsRate):
        self.inPacketsRate = inPacketsRate
        self.setHasInPacketsRate()

    def setOutPackets (self, outPackets):
        self.outPackets = outPackets
        self.setHasOutPackets()

    def setInDiscardPackets (self, inDiscardPackets):
        self.inDiscardPackets = inDiscardPackets
        self.setHasInDiscardPackets()

    def setInMulticastPackets (self, inMulticastPackets):
        self.inMulticastPackets = inMulticastPackets
        self.setHasInMulticastPackets()

    def setOutBroadcastPackets (self, outBroadcastPackets):
        self.outBroadcastPackets = outBroadcastPackets
        self.setHasOutBroadcastPackets()

    def setOutOctets (self, outOctets):
        self.outOctets = outOctets
        self.setHasOutOctets()

    def setOutMulticastPackets (self, outMulticastPackets):
        self.outMulticastPackets = outMulticastPackets
        self.setHasOutMulticastPackets()

    def setInUnicastPackets (self, inUnicastPackets):
        self.inUnicastPackets = inUnicastPackets
        self.setHasInUnicastPackets()

    def setOutErrorPackets (self, outErrorPackets):
        self.outErrorPackets = outErrorPackets
        self.setHasOutErrorPackets()

    def setOutPacketsRate (self, outPacketsRate):
        self.outPacketsRate = outPacketsRate
        self.setHasOutPacketsRate()

    def setInPackets (self, inPackets):
        self.inPackets = inPackets
        self.setHasInPackets()

    def setOperationalStatusChanges (self, operationalStatusChanges):
        self.operationalStatusChanges = operationalStatusChanges
        self.setHasOperationalStatusChanges()

    def setInBitsRate (self, inBitsRate):
        self.inBitsRate = inBitsRate
        self.setHasInBitsRate()

    def setOutBitsRate (self, outBitsRate):
        self.outBitsRate = outBitsRate
        self.setHasOutBitsRate()

    def setInBroadcastPackets (self, inBroadcastPackets):
        self.inBroadcastPackets = inBroadcastPackets
        self.setHasInBroadcastPackets()


"""
Extracted from the below data: 
{
    "node": {
        "className": "CountersOperData", 
        "namespace": "counters", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.counters.counters_oper_data_gen import CountersOperData"
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
            "namespace": "counters", 
            "isCurrent": true
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "leaves": [
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outGratuitousArpPackets", 
            "yangName": "out-gratuitous-arp-packets", 
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
            "memberName": "inOctets", 
            "yangName": "in-octets", 
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
            "memberName": "inPacketsRate", 
            "yangName": "in-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPackets", 
            "yangName": "out-packets", 
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
            "memberName": "outOctets", 
            "yangName": "out-octets", 
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
            "memberName": "inUnicastPackets", 
            "yangName": "in-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
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
            "memberName": "outPacketsRate", 
            "yangName": "out-packets-rate", 
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
            "memberName": "operationalStatusChanges", 
            "yangName": "operational-status-changes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBitsRate", 
            "yangName": "in-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBitsRate", 
            "yangName": "out-bits-rate", 
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


