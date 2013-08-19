


# Copyright Qwilt, 2012
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: naamas

from a.infra.misc.enum_with_value import EnumWithValue
from a.infra.basic.return_codes import ReturnCodes
from a.infra.misc.init_guard import InitGuard

from a.sys.confd.pyconfdlib.tag_values import TagValues
from a.sys.confd.pyconfdlib.value import Value
from a.sys.confd.pyconfdlib.key_path import KeyPath

from counters_maapi_base_gen import CountersMaapiBase




class BlinkyCountersMaapi(CountersMaapiBase):
    def __init__ (self, logger):
        self.myInitGuard = InitGuard()
        self._log=logger.createLogger("sys-blinky-oper-example","blinky-maapi-counters")
        self.domain = None

        

        
        self.outGratuitousArpPacketsRequested = False
        self.outGratuitousArpPackets = None
        self.outGratuitousArpPacketsSet = False
        
        self.outUnicastPacketsRequested = False
        self.outUnicastPackets = None
        self.outUnicastPacketsSet = False
        
        self.inUnknownProtocolPacketsRequested = False
        self.inUnknownProtocolPackets = None
        self.inUnknownProtocolPacketsSet = False
        
        self.outDiscardPacketsRequested = False
        self.outDiscardPackets = None
        self.outDiscardPacketsSet = False
        
        self.inOctetsRequested = False
        self.inOctets = None
        self.inOctetsSet = False
        
        self.inErrorPacketsRequested = False
        self.inErrorPackets = None
        self.inErrorPacketsSet = False
        
        self.inPacketsRateRequested = False
        self.inPacketsRate = None
        self.inPacketsRateSet = False
        
        self.outPacketsRequested = False
        self.outPackets = None
        self.outPacketsSet = False
        
        self.inDiscardPacketsRequested = False
        self.inDiscardPackets = None
        self.inDiscardPacketsSet = False
        
        self.inMulticastPacketsRequested = False
        self.inMulticastPackets = None
        self.inMulticastPacketsSet = False
        
        self.outBroadcastPacketsRequested = False
        self.outBroadcastPackets = None
        self.outBroadcastPacketsSet = False
        
        self.outOctetsRequested = False
        self.outOctets = None
        self.outOctetsSet = False
        
        self.outMulticastPacketsRequested = False
        self.outMulticastPackets = None
        self.outMulticastPacketsSet = False
        
        self.inUnicastPacketsRequested = False
        self.inUnicastPackets = None
        self.inUnicastPacketsSet = False
        
        self.outErrorPacketsRequested = False
        self.outErrorPackets = None
        self.outErrorPacketsSet = False
        
        self.outPacketsRateRequested = False
        self.outPacketsRate = None
        self.outPacketsRateSet = False
        
        self.inPacketsRequested = False
        self.inPackets = None
        self.inPacketsSet = False
        
        self.operationalStatusChangesRequested = False
        self.operationalStatusChanges = None
        self.operationalStatusChangesSet = False
        
        self.inBitsRateRequested = False
        self.inBitsRate = None
        self.inBitsRateSet = False
        
        self.outBitsRateRequested = False
        self.outBitsRate = None
        self.outBitsRateSet = False
        
        self.inBroadcastPacketsRequested = False
        self.inBroadcastPackets = None
        self.inBroadcastPacketsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOutGratuitousArpPackets(True)
        
        self.requestOutUnicastPackets(True)
        
        self.requestInUnknownProtocolPackets(True)
        
        self.requestOutDiscardPackets(True)
        
        self.requestInOctets(True)
        
        self.requestInErrorPackets(True)
        
        self.requestInPacketsRate(True)
        
        self.requestOutPackets(True)
        
        self.requestInDiscardPackets(True)
        
        self.requestInMulticastPackets(True)
        
        self.requestOutBroadcastPackets(True)
        
        self.requestOutOctets(True)
        
        self.requestOutMulticastPackets(True)
        
        self.requestInUnicastPackets(True)
        
        self.requestOutErrorPackets(True)
        
        self.requestOutPacketsRate(True)
        
        self.requestInPackets(True)
        
        self.requestOperationalStatusChanges(True)
        
        self.requestInBitsRate(True)
        
        self.requestOutBitsRate(True)
        
        self.requestInBroadcastPackets(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOutGratuitousArpPackets(False)
        
        self.requestOutUnicastPackets(False)
        
        self.requestInUnknownProtocolPackets(False)
        
        self.requestOutDiscardPackets(False)
        
        self.requestInOctets(False)
        
        self.requestInErrorPackets(False)
        
        self.requestInPacketsRate(False)
        
        self.requestOutPackets(False)
        
        self.requestInDiscardPackets(False)
        
        self.requestInMulticastPackets(False)
        
        self.requestOutBroadcastPackets(False)
        
        self.requestOutOctets(False)
        
        self.requestOutMulticastPackets(False)
        
        self.requestInUnicastPackets(False)
        
        self.requestOutErrorPackets(False)
        
        self.requestOutPacketsRate(False)
        
        self.requestInPackets(False)
        
        self.requestOperationalStatusChanges(False)
        
        self.requestInBitsRate(False)
        
        self.requestOutBitsRate(False)
        
        self.requestInBroadcastPackets(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOutGratuitousArpPackets(True)
        
        self.requestOutUnicastPackets(True)
        
        self.requestInUnknownProtocolPackets(True)
        
        self.requestOutDiscardPackets(True)
        
        self.requestInOctets(True)
        
        self.requestInErrorPackets(True)
        
        self.requestInPacketsRate(True)
        
        self.requestOutPackets(True)
        
        self.requestInDiscardPackets(True)
        
        self.requestInMulticastPackets(True)
        
        self.requestOutBroadcastPackets(True)
        
        self.requestOutOctets(True)
        
        self.requestOutMulticastPackets(True)
        
        self.requestInUnicastPackets(True)
        
        self.requestOutErrorPackets(True)
        
        self.requestOutPacketsRate(True)
        
        self.requestInPackets(True)
        
        self.requestOperationalStatusChanges(True)
        
        self.requestInBitsRate(True)
        
        self.requestOutBitsRate(True)
        
        self.requestInBroadcastPackets(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestOutGratuitousArpPackets(False)
        
        self.requestOutUnicastPackets(False)
        
        self.requestInUnknownProtocolPackets(False)
        
        self.requestOutDiscardPackets(False)
        
        self.requestInOctets(False)
        
        self.requestInErrorPackets(False)
        
        self.requestInPacketsRate(False)
        
        self.requestOutPackets(False)
        
        self.requestInDiscardPackets(False)
        
        self.requestInMulticastPackets(False)
        
        self.requestOutBroadcastPackets(False)
        
        self.requestOutOctets(False)
        
        self.requestOutMulticastPackets(False)
        
        self.requestInUnicastPackets(False)
        
        self.requestOutErrorPackets(False)
        
        self.requestOutPacketsRate(False)
        
        self.requestInPackets(False)
        
        self.requestOperationalStatusChanges(False)
        
        self.requestInBitsRate(False)
        
        self.requestOutBitsRate(False)
        
        self.requestInBroadcastPackets(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , interface
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(interface, trxContext)

    def read (self
              , interface
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       , interface
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(interface, 
                                  True,
                                  trxContext)



    def requestOutGratuitousArpPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-outgratuitousarppackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.outGratuitousArpPacketsRequested = requested
        self.outGratuitousArpPacketsSet = False

    def isOutGratuitousArpPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-outgratuitousarppackets-requested').debug3Func(): logFunc('called. requested=%s', self.outGratuitousArpPacketsRequested)
        return self.outGratuitousArpPacketsRequested

    def getOutGratuitousArpPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-outgratuitousarppackets').debug3Func(): logFunc('called. self.outGratuitousArpPacketsSet=%s, self.outGratuitousArpPackets=%s', self.outGratuitousArpPacketsSet, self.outGratuitousArpPackets)
        if self.outGratuitousArpPacketsSet:
            return self.outGratuitousArpPackets
        return None

    def hasOutGratuitousArpPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-outgratuitousarppackets').debug3Func(): logFunc('called. self.outGratuitousArpPacketsSet=%s, self.outGratuitousArpPackets=%s', self.outGratuitousArpPacketsSet, self.outGratuitousArpPackets)
        if self.outGratuitousArpPacketsSet:
            return True
        return False

    def setOutGratuitousArpPackets (self, outGratuitousArpPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-outgratuitousarppackets').debug3Func(): logFunc('called. outGratuitousArpPackets=%s, old=%s', outGratuitousArpPackets, self.outGratuitousArpPackets)
        self.outGratuitousArpPacketsSet = True
        self.outGratuitousArpPackets = outGratuitousArpPackets

    def requestOutUnicastPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-outunicastpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.outUnicastPacketsRequested = requested
        self.outUnicastPacketsSet = False

    def isOutUnicastPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-outunicastpackets-requested').debug3Func(): logFunc('called. requested=%s', self.outUnicastPacketsRequested)
        return self.outUnicastPacketsRequested

    def getOutUnicastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-outunicastpackets').debug3Func(): logFunc('called. self.outUnicastPacketsSet=%s, self.outUnicastPackets=%s', self.outUnicastPacketsSet, self.outUnicastPackets)
        if self.outUnicastPacketsSet:
            return self.outUnicastPackets
        return None

    def hasOutUnicastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-outunicastpackets').debug3Func(): logFunc('called. self.outUnicastPacketsSet=%s, self.outUnicastPackets=%s', self.outUnicastPacketsSet, self.outUnicastPackets)
        if self.outUnicastPacketsSet:
            return True
        return False

    def setOutUnicastPackets (self, outUnicastPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-outunicastpackets').debug3Func(): logFunc('called. outUnicastPackets=%s, old=%s', outUnicastPackets, self.outUnicastPackets)
        self.outUnicastPacketsSet = True
        self.outUnicastPackets = outUnicastPackets

    def requestInUnknownProtocolPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inunknownprotocolpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inUnknownProtocolPacketsRequested = requested
        self.inUnknownProtocolPacketsSet = False

    def isInUnknownProtocolPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inunknownprotocolpackets-requested').debug3Func(): logFunc('called. requested=%s', self.inUnknownProtocolPacketsRequested)
        return self.inUnknownProtocolPacketsRequested

    def getInUnknownProtocolPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inunknownprotocolpackets').debug3Func(): logFunc('called. self.inUnknownProtocolPacketsSet=%s, self.inUnknownProtocolPackets=%s', self.inUnknownProtocolPacketsSet, self.inUnknownProtocolPackets)
        if self.inUnknownProtocolPacketsSet:
            return self.inUnknownProtocolPackets
        return None

    def hasInUnknownProtocolPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inunknownprotocolpackets').debug3Func(): logFunc('called. self.inUnknownProtocolPacketsSet=%s, self.inUnknownProtocolPackets=%s', self.inUnknownProtocolPacketsSet, self.inUnknownProtocolPackets)
        if self.inUnknownProtocolPacketsSet:
            return True
        return False

    def setInUnknownProtocolPackets (self, inUnknownProtocolPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inunknownprotocolpackets').debug3Func(): logFunc('called. inUnknownProtocolPackets=%s, old=%s', inUnknownProtocolPackets, self.inUnknownProtocolPackets)
        self.inUnknownProtocolPacketsSet = True
        self.inUnknownProtocolPackets = inUnknownProtocolPackets

    def requestOutDiscardPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-outdiscardpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.outDiscardPacketsRequested = requested
        self.outDiscardPacketsSet = False

    def isOutDiscardPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-outdiscardpackets-requested').debug3Func(): logFunc('called. requested=%s', self.outDiscardPacketsRequested)
        return self.outDiscardPacketsRequested

    def getOutDiscardPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-outdiscardpackets').debug3Func(): logFunc('called. self.outDiscardPacketsSet=%s, self.outDiscardPackets=%s', self.outDiscardPacketsSet, self.outDiscardPackets)
        if self.outDiscardPacketsSet:
            return self.outDiscardPackets
        return None

    def hasOutDiscardPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-outdiscardpackets').debug3Func(): logFunc('called. self.outDiscardPacketsSet=%s, self.outDiscardPackets=%s', self.outDiscardPacketsSet, self.outDiscardPackets)
        if self.outDiscardPacketsSet:
            return True
        return False

    def setOutDiscardPackets (self, outDiscardPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-outdiscardpackets').debug3Func(): logFunc('called. outDiscardPackets=%s, old=%s', outDiscardPackets, self.outDiscardPackets)
        self.outDiscardPacketsSet = True
        self.outDiscardPackets = outDiscardPackets

    def requestInOctets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inoctets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inOctetsRequested = requested
        self.inOctetsSet = False

    def isInOctetsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inoctets-requested').debug3Func(): logFunc('called. requested=%s', self.inOctetsRequested)
        return self.inOctetsRequested

    def getInOctets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inoctets').debug3Func(): logFunc('called. self.inOctetsSet=%s, self.inOctets=%s', self.inOctetsSet, self.inOctets)
        if self.inOctetsSet:
            return self.inOctets
        return None

    def hasInOctets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inoctets').debug3Func(): logFunc('called. self.inOctetsSet=%s, self.inOctets=%s', self.inOctetsSet, self.inOctets)
        if self.inOctetsSet:
            return True
        return False

    def setInOctets (self, inOctets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inoctets').debug3Func(): logFunc('called. inOctets=%s, old=%s', inOctets, self.inOctets)
        self.inOctetsSet = True
        self.inOctets = inOctets

    def requestInErrorPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inerrorpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inErrorPacketsRequested = requested
        self.inErrorPacketsSet = False

    def isInErrorPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inerrorpackets-requested').debug3Func(): logFunc('called. requested=%s', self.inErrorPacketsRequested)
        return self.inErrorPacketsRequested

    def getInErrorPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inerrorpackets').debug3Func(): logFunc('called. self.inErrorPacketsSet=%s, self.inErrorPackets=%s', self.inErrorPacketsSet, self.inErrorPackets)
        if self.inErrorPacketsSet:
            return self.inErrorPackets
        return None

    def hasInErrorPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inerrorpackets').debug3Func(): logFunc('called. self.inErrorPacketsSet=%s, self.inErrorPackets=%s', self.inErrorPacketsSet, self.inErrorPackets)
        if self.inErrorPacketsSet:
            return True
        return False

    def setInErrorPackets (self, inErrorPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inerrorpackets').debug3Func(): logFunc('called. inErrorPackets=%s, old=%s', inErrorPackets, self.inErrorPackets)
        self.inErrorPacketsSet = True
        self.inErrorPackets = inErrorPackets

    def requestInPacketsRate (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inpacketsrate').debug3Func(): logFunc('called. requested=%s', requested)
        self.inPacketsRateRequested = requested
        self.inPacketsRateSet = False

    def isInPacketsRateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inpacketsrate-requested').debug3Func(): logFunc('called. requested=%s', self.inPacketsRateRequested)
        return self.inPacketsRateRequested

    def getInPacketsRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inpacketsrate').debug3Func(): logFunc('called. self.inPacketsRateSet=%s, self.inPacketsRate=%s', self.inPacketsRateSet, self.inPacketsRate)
        if self.inPacketsRateSet:
            return self.inPacketsRate
        return None

    def hasInPacketsRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inpacketsrate').debug3Func(): logFunc('called. self.inPacketsRateSet=%s, self.inPacketsRate=%s', self.inPacketsRateSet, self.inPacketsRate)
        if self.inPacketsRateSet:
            return True
        return False

    def setInPacketsRate (self, inPacketsRate):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inpacketsrate').debug3Func(): logFunc('called. inPacketsRate=%s, old=%s', inPacketsRate, self.inPacketsRate)
        self.inPacketsRateSet = True
        self.inPacketsRate = inPacketsRate

    def requestOutPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-outpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.outPacketsRequested = requested
        self.outPacketsSet = False

    def isOutPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-outpackets-requested').debug3Func(): logFunc('called. requested=%s', self.outPacketsRequested)
        return self.outPacketsRequested

    def getOutPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-outpackets').debug3Func(): logFunc('called. self.outPacketsSet=%s, self.outPackets=%s', self.outPacketsSet, self.outPackets)
        if self.outPacketsSet:
            return self.outPackets
        return None

    def hasOutPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-outpackets').debug3Func(): logFunc('called. self.outPacketsSet=%s, self.outPackets=%s', self.outPacketsSet, self.outPackets)
        if self.outPacketsSet:
            return True
        return False

    def setOutPackets (self, outPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-outpackets').debug3Func(): logFunc('called. outPackets=%s, old=%s', outPackets, self.outPackets)
        self.outPacketsSet = True
        self.outPackets = outPackets

    def requestInDiscardPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-indiscardpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inDiscardPacketsRequested = requested
        self.inDiscardPacketsSet = False

    def isInDiscardPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-indiscardpackets-requested').debug3Func(): logFunc('called. requested=%s', self.inDiscardPacketsRequested)
        return self.inDiscardPacketsRequested

    def getInDiscardPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-indiscardpackets').debug3Func(): logFunc('called. self.inDiscardPacketsSet=%s, self.inDiscardPackets=%s', self.inDiscardPacketsSet, self.inDiscardPackets)
        if self.inDiscardPacketsSet:
            return self.inDiscardPackets
        return None

    def hasInDiscardPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-indiscardpackets').debug3Func(): logFunc('called. self.inDiscardPacketsSet=%s, self.inDiscardPackets=%s', self.inDiscardPacketsSet, self.inDiscardPackets)
        if self.inDiscardPacketsSet:
            return True
        return False

    def setInDiscardPackets (self, inDiscardPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-indiscardpackets').debug3Func(): logFunc('called. inDiscardPackets=%s, old=%s', inDiscardPackets, self.inDiscardPackets)
        self.inDiscardPacketsSet = True
        self.inDiscardPackets = inDiscardPackets

    def requestInMulticastPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inmulticastpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inMulticastPacketsRequested = requested
        self.inMulticastPacketsSet = False

    def isInMulticastPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inmulticastpackets-requested').debug3Func(): logFunc('called. requested=%s', self.inMulticastPacketsRequested)
        return self.inMulticastPacketsRequested

    def getInMulticastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inmulticastpackets').debug3Func(): logFunc('called. self.inMulticastPacketsSet=%s, self.inMulticastPackets=%s', self.inMulticastPacketsSet, self.inMulticastPackets)
        if self.inMulticastPacketsSet:
            return self.inMulticastPackets
        return None

    def hasInMulticastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inmulticastpackets').debug3Func(): logFunc('called. self.inMulticastPacketsSet=%s, self.inMulticastPackets=%s', self.inMulticastPacketsSet, self.inMulticastPackets)
        if self.inMulticastPacketsSet:
            return True
        return False

    def setInMulticastPackets (self, inMulticastPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inmulticastpackets').debug3Func(): logFunc('called. inMulticastPackets=%s, old=%s', inMulticastPackets, self.inMulticastPackets)
        self.inMulticastPacketsSet = True
        self.inMulticastPackets = inMulticastPackets

    def requestOutBroadcastPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-outbroadcastpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.outBroadcastPacketsRequested = requested
        self.outBroadcastPacketsSet = False

    def isOutBroadcastPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-outbroadcastpackets-requested').debug3Func(): logFunc('called. requested=%s', self.outBroadcastPacketsRequested)
        return self.outBroadcastPacketsRequested

    def getOutBroadcastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-outbroadcastpackets').debug3Func(): logFunc('called. self.outBroadcastPacketsSet=%s, self.outBroadcastPackets=%s', self.outBroadcastPacketsSet, self.outBroadcastPackets)
        if self.outBroadcastPacketsSet:
            return self.outBroadcastPackets
        return None

    def hasOutBroadcastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-outbroadcastpackets').debug3Func(): logFunc('called. self.outBroadcastPacketsSet=%s, self.outBroadcastPackets=%s', self.outBroadcastPacketsSet, self.outBroadcastPackets)
        if self.outBroadcastPacketsSet:
            return True
        return False

    def setOutBroadcastPackets (self, outBroadcastPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-outbroadcastpackets').debug3Func(): logFunc('called. outBroadcastPackets=%s, old=%s', outBroadcastPackets, self.outBroadcastPackets)
        self.outBroadcastPacketsSet = True
        self.outBroadcastPackets = outBroadcastPackets

    def requestOutOctets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-outoctets').debug3Func(): logFunc('called. requested=%s', requested)
        self.outOctetsRequested = requested
        self.outOctetsSet = False

    def isOutOctetsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-outoctets-requested').debug3Func(): logFunc('called. requested=%s', self.outOctetsRequested)
        return self.outOctetsRequested

    def getOutOctets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-outoctets').debug3Func(): logFunc('called. self.outOctetsSet=%s, self.outOctets=%s', self.outOctetsSet, self.outOctets)
        if self.outOctetsSet:
            return self.outOctets
        return None

    def hasOutOctets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-outoctets').debug3Func(): logFunc('called. self.outOctetsSet=%s, self.outOctets=%s', self.outOctetsSet, self.outOctets)
        if self.outOctetsSet:
            return True
        return False

    def setOutOctets (self, outOctets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-outoctets').debug3Func(): logFunc('called. outOctets=%s, old=%s', outOctets, self.outOctets)
        self.outOctetsSet = True
        self.outOctets = outOctets

    def requestOutMulticastPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-outmulticastpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.outMulticastPacketsRequested = requested
        self.outMulticastPacketsSet = False

    def isOutMulticastPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-outmulticastpackets-requested').debug3Func(): logFunc('called. requested=%s', self.outMulticastPacketsRequested)
        return self.outMulticastPacketsRequested

    def getOutMulticastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-outmulticastpackets').debug3Func(): logFunc('called. self.outMulticastPacketsSet=%s, self.outMulticastPackets=%s', self.outMulticastPacketsSet, self.outMulticastPackets)
        if self.outMulticastPacketsSet:
            return self.outMulticastPackets
        return None

    def hasOutMulticastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-outmulticastpackets').debug3Func(): logFunc('called. self.outMulticastPacketsSet=%s, self.outMulticastPackets=%s', self.outMulticastPacketsSet, self.outMulticastPackets)
        if self.outMulticastPacketsSet:
            return True
        return False

    def setOutMulticastPackets (self, outMulticastPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-outmulticastpackets').debug3Func(): logFunc('called. outMulticastPackets=%s, old=%s', outMulticastPackets, self.outMulticastPackets)
        self.outMulticastPacketsSet = True
        self.outMulticastPackets = outMulticastPackets

    def requestInUnicastPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inunicastpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inUnicastPacketsRequested = requested
        self.inUnicastPacketsSet = False

    def isInUnicastPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inunicastpackets-requested').debug3Func(): logFunc('called. requested=%s', self.inUnicastPacketsRequested)
        return self.inUnicastPacketsRequested

    def getInUnicastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inunicastpackets').debug3Func(): logFunc('called. self.inUnicastPacketsSet=%s, self.inUnicastPackets=%s', self.inUnicastPacketsSet, self.inUnicastPackets)
        if self.inUnicastPacketsSet:
            return self.inUnicastPackets
        return None

    def hasInUnicastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inunicastpackets').debug3Func(): logFunc('called. self.inUnicastPacketsSet=%s, self.inUnicastPackets=%s', self.inUnicastPacketsSet, self.inUnicastPackets)
        if self.inUnicastPacketsSet:
            return True
        return False

    def setInUnicastPackets (self, inUnicastPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inunicastpackets').debug3Func(): logFunc('called. inUnicastPackets=%s, old=%s', inUnicastPackets, self.inUnicastPackets)
        self.inUnicastPacketsSet = True
        self.inUnicastPackets = inUnicastPackets

    def requestOutErrorPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-outerrorpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.outErrorPacketsRequested = requested
        self.outErrorPacketsSet = False

    def isOutErrorPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-outerrorpackets-requested').debug3Func(): logFunc('called. requested=%s', self.outErrorPacketsRequested)
        return self.outErrorPacketsRequested

    def getOutErrorPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-outerrorpackets').debug3Func(): logFunc('called. self.outErrorPacketsSet=%s, self.outErrorPackets=%s', self.outErrorPacketsSet, self.outErrorPackets)
        if self.outErrorPacketsSet:
            return self.outErrorPackets
        return None

    def hasOutErrorPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-outerrorpackets').debug3Func(): logFunc('called. self.outErrorPacketsSet=%s, self.outErrorPackets=%s', self.outErrorPacketsSet, self.outErrorPackets)
        if self.outErrorPacketsSet:
            return True
        return False

    def setOutErrorPackets (self, outErrorPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-outerrorpackets').debug3Func(): logFunc('called. outErrorPackets=%s, old=%s', outErrorPackets, self.outErrorPackets)
        self.outErrorPacketsSet = True
        self.outErrorPackets = outErrorPackets

    def requestOutPacketsRate (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-outpacketsrate').debug3Func(): logFunc('called. requested=%s', requested)
        self.outPacketsRateRequested = requested
        self.outPacketsRateSet = False

    def isOutPacketsRateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-outpacketsrate-requested').debug3Func(): logFunc('called. requested=%s', self.outPacketsRateRequested)
        return self.outPacketsRateRequested

    def getOutPacketsRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-outpacketsrate').debug3Func(): logFunc('called. self.outPacketsRateSet=%s, self.outPacketsRate=%s', self.outPacketsRateSet, self.outPacketsRate)
        if self.outPacketsRateSet:
            return self.outPacketsRate
        return None

    def hasOutPacketsRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-outpacketsrate').debug3Func(): logFunc('called. self.outPacketsRateSet=%s, self.outPacketsRate=%s', self.outPacketsRateSet, self.outPacketsRate)
        if self.outPacketsRateSet:
            return True
        return False

    def setOutPacketsRate (self, outPacketsRate):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-outpacketsrate').debug3Func(): logFunc('called. outPacketsRate=%s, old=%s', outPacketsRate, self.outPacketsRate)
        self.outPacketsRateSet = True
        self.outPacketsRate = outPacketsRate

    def requestInPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inPacketsRequested = requested
        self.inPacketsSet = False

    def isInPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inpackets-requested').debug3Func(): logFunc('called. requested=%s', self.inPacketsRequested)
        return self.inPacketsRequested

    def getInPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inpackets').debug3Func(): logFunc('called. self.inPacketsSet=%s, self.inPackets=%s', self.inPacketsSet, self.inPackets)
        if self.inPacketsSet:
            return self.inPackets
        return None

    def hasInPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inpackets').debug3Func(): logFunc('called. self.inPacketsSet=%s, self.inPackets=%s', self.inPacketsSet, self.inPackets)
        if self.inPacketsSet:
            return True
        return False

    def setInPackets (self, inPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inpackets').debug3Func(): logFunc('called. inPackets=%s, old=%s', inPackets, self.inPackets)
        self.inPacketsSet = True
        self.inPackets = inPackets

    def requestOperationalStatusChanges (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-operationalstatuschanges').debug3Func(): logFunc('called. requested=%s', requested)
        self.operationalStatusChangesRequested = requested
        self.operationalStatusChangesSet = False

    def isOperationalStatusChangesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-operationalstatuschanges-requested').debug3Func(): logFunc('called. requested=%s', self.operationalStatusChangesRequested)
        return self.operationalStatusChangesRequested

    def getOperationalStatusChanges (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-operationalstatuschanges').debug3Func(): logFunc('called. self.operationalStatusChangesSet=%s, self.operationalStatusChanges=%s', self.operationalStatusChangesSet, self.operationalStatusChanges)
        if self.operationalStatusChangesSet:
            return self.operationalStatusChanges
        return None

    def hasOperationalStatusChanges (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-operationalstatuschanges').debug3Func(): logFunc('called. self.operationalStatusChangesSet=%s, self.operationalStatusChanges=%s', self.operationalStatusChangesSet, self.operationalStatusChanges)
        if self.operationalStatusChangesSet:
            return True
        return False

    def setOperationalStatusChanges (self, operationalStatusChanges):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-operationalstatuschanges').debug3Func(): logFunc('called. operationalStatusChanges=%s, old=%s', operationalStatusChanges, self.operationalStatusChanges)
        self.operationalStatusChangesSet = True
        self.operationalStatusChanges = operationalStatusChanges

    def requestInBitsRate (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inbitsrate').debug3Func(): logFunc('called. requested=%s', requested)
        self.inBitsRateRequested = requested
        self.inBitsRateSet = False

    def isInBitsRateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inbitsrate-requested').debug3Func(): logFunc('called. requested=%s', self.inBitsRateRequested)
        return self.inBitsRateRequested

    def getInBitsRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inbitsrate').debug3Func(): logFunc('called. self.inBitsRateSet=%s, self.inBitsRate=%s', self.inBitsRateSet, self.inBitsRate)
        if self.inBitsRateSet:
            return self.inBitsRate
        return None

    def hasInBitsRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inbitsrate').debug3Func(): logFunc('called. self.inBitsRateSet=%s, self.inBitsRate=%s', self.inBitsRateSet, self.inBitsRate)
        if self.inBitsRateSet:
            return True
        return False

    def setInBitsRate (self, inBitsRate):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inbitsrate').debug3Func(): logFunc('called. inBitsRate=%s, old=%s', inBitsRate, self.inBitsRate)
        self.inBitsRateSet = True
        self.inBitsRate = inBitsRate

    def requestOutBitsRate (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-outbitsrate').debug3Func(): logFunc('called. requested=%s', requested)
        self.outBitsRateRequested = requested
        self.outBitsRateSet = False

    def isOutBitsRateRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-outbitsrate-requested').debug3Func(): logFunc('called. requested=%s', self.outBitsRateRequested)
        return self.outBitsRateRequested

    def getOutBitsRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-outbitsrate').debug3Func(): logFunc('called. self.outBitsRateSet=%s, self.outBitsRate=%s', self.outBitsRateSet, self.outBitsRate)
        if self.outBitsRateSet:
            return self.outBitsRate
        return None

    def hasOutBitsRate (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-outbitsrate').debug3Func(): logFunc('called. self.outBitsRateSet=%s, self.outBitsRate=%s', self.outBitsRateSet, self.outBitsRate)
        if self.outBitsRateSet:
            return True
        return False

    def setOutBitsRate (self, outBitsRate):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-outbitsrate').debug3Func(): logFunc('called. outBitsRate=%s, old=%s', outBitsRate, self.outBitsRate)
        self.outBitsRateSet = True
        self.outBitsRate = outBitsRate

    def requestInBroadcastPackets (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-inbroadcastpackets').debug3Func(): logFunc('called. requested=%s', requested)
        self.inBroadcastPacketsRequested = requested
        self.inBroadcastPacketsSet = False

    def isInBroadcastPacketsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-inbroadcastpackets-requested').debug3Func(): logFunc('called. requested=%s', self.inBroadcastPacketsRequested)
        return self.inBroadcastPacketsRequested

    def getInBroadcastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-inbroadcastpackets').debug3Func(): logFunc('called. self.inBroadcastPacketsSet=%s, self.inBroadcastPackets=%s', self.inBroadcastPacketsSet, self.inBroadcastPackets)
        if self.inBroadcastPacketsSet:
            return self.inBroadcastPackets
        return None

    def hasInBroadcastPackets (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-inbroadcastpackets').debug3Func(): logFunc('called. self.inBroadcastPacketsSet=%s, self.inBroadcastPackets=%s', self.inBroadcastPacketsSet, self.inBroadcastPackets)
        if self.inBroadcastPacketsSet:
            return True
        return False

    def setInBroadcastPackets (self, inBroadcastPackets):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-inbroadcastpackets').debug3Func(): logFunc('called. inBroadcastPackets=%s, old=%s', inBroadcastPackets, self.inBroadcastPackets)
        self.inBroadcastPacketsSet = True
        self.inBroadcastPackets = inBroadcastPackets


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.outGratuitousArpPackets = 0
        self.outGratuitousArpPacketsSet = False
        
        self.outUnicastPackets = 0
        self.outUnicastPacketsSet = False
        
        self.inUnknownProtocolPackets = 0
        self.inUnknownProtocolPacketsSet = False
        
        self.outDiscardPackets = 0
        self.outDiscardPacketsSet = False
        
        self.inOctets = 0
        self.inOctetsSet = False
        
        self.inErrorPackets = 0
        self.inErrorPacketsSet = False
        
        self.inPacketsRate = 0
        self.inPacketsRateSet = False
        
        self.outPackets = 0
        self.outPacketsSet = False
        
        self.inDiscardPackets = 0
        self.inDiscardPacketsSet = False
        
        self.inMulticastPackets = 0
        self.inMulticastPacketsSet = False
        
        self.outBroadcastPackets = 0
        self.outBroadcastPacketsSet = False
        
        self.outOctets = 0
        self.outOctetsSet = False
        
        self.outMulticastPackets = 0
        self.outMulticastPacketsSet = False
        
        self.inUnicastPackets = 0
        self.inUnicastPacketsSet = False
        
        self.outErrorPackets = 0
        self.outErrorPacketsSet = False
        
        self.outPacketsRate = 0
        self.outPacketsRateSet = False
        
        self.inPackets = 0
        self.inPacketsSet = False
        
        self.operationalStatusChanges = 0
        self.operationalStatusChangesSet = False
        
        self.inBitsRate = 0
        self.inBitsRateSet = False
        
        self.outBitsRate = 0
        self.outBitsRateSet = False
        
        self.inBroadcastPackets = 0
        self.inBroadcastPacketsSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        ancestorVal = Value()
        ancestorVal.setString(interface);
        keyPath.addKeyPathPrefix(ancestorVal)
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interface", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("interfaces", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        interface, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(interface, 
                                         
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       interface, 
                       
                       readAllOrFail,
                       trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-read').debug3Func(): logFunc('called. PARAMS, readAllOrFail=%s', readAllOrFail)

        if readAllOrFail:
            self._clearAllReadData()

        tagValueList = TagValues()

        res = self._fillReadTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-fill-read-tag-value-failed').errorFunc(): logFunc('_fillReadTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(interface, 
                                       
                                       None)

        res = self.domain.readMaapi(tagValueList, keyPath, trxContext)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-domain-failed').errorFunc(): logFunc('domain.readMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        res = self._readTagValues(tagValueList, readAllOrFail)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('read-read-tag-values-failed').errorFunc(): logFunc('_readTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-read-done').debug3Func(): logFunc('done. PARAMS, readAllOrFail=%s', readAllOrFail)
        return ReturnCodes.kOk

    def _collectItemsToDelete (self,
                               interface, 
                               
                               itemsToDelete):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('collect-items-to-delete').debug3Func(): logFunc('called: itemsToDelete=%s. PARAMS', itemsToDelete)

        

        for logFunc in self._log('collect-items-to-delete-done').debug3Func(): logFunc('done: itemsToDelete=%s. PARAMS', itemsToDelete)
        return ReturnCodes.kOk

    def _fillWriteTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-write-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        

        

        return ReturnCodes.kOk

    def _fillReadTagValues (self, tagValueList):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('fill-read-tag-values').debug3Func(): logFunc('called: tagValueList=%s', tagValueList)

        
        if self.isOutGratuitousArpPacketsRequested():
            valOutGratuitousArpPackets = Value()
            valOutGratuitousArpPackets.setEmpty()
            tagValueList.push(("out-gratuitous-arp-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOutGratuitousArpPackets)
        
        if self.isOutUnicastPacketsRequested():
            valOutUnicastPackets = Value()
            valOutUnicastPackets.setEmpty()
            tagValueList.push(("out-unicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOutUnicastPackets)
        
        if self.isInUnknownProtocolPacketsRequested():
            valInUnknownProtocolPackets = Value()
            valInUnknownProtocolPackets.setEmpty()
            tagValueList.push(("in-unknown-protocol-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInUnknownProtocolPackets)
        
        if self.isOutDiscardPacketsRequested():
            valOutDiscardPackets = Value()
            valOutDiscardPackets.setEmpty()
            tagValueList.push(("out-discard-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOutDiscardPackets)
        
        if self.isInOctetsRequested():
            valInOctets = Value()
            valInOctets.setEmpty()
            tagValueList.push(("in-octets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInOctets)
        
        if self.isInErrorPacketsRequested():
            valInErrorPackets = Value()
            valInErrorPackets.setEmpty()
            tagValueList.push(("in-error-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInErrorPackets)
        
        if self.isInPacketsRateRequested():
            valInPacketsRate = Value()
            valInPacketsRate.setEmpty()
            tagValueList.push(("in-packets-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInPacketsRate)
        
        if self.isOutPacketsRequested():
            valOutPackets = Value()
            valOutPackets.setEmpty()
            tagValueList.push(("out-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOutPackets)
        
        if self.isInDiscardPacketsRequested():
            valInDiscardPackets = Value()
            valInDiscardPackets.setEmpty()
            tagValueList.push(("in-discard-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInDiscardPackets)
        
        if self.isInMulticastPacketsRequested():
            valInMulticastPackets = Value()
            valInMulticastPackets.setEmpty()
            tagValueList.push(("in-multicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInMulticastPackets)
        
        if self.isOutBroadcastPacketsRequested():
            valOutBroadcastPackets = Value()
            valOutBroadcastPackets.setEmpty()
            tagValueList.push(("out-broadcast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOutBroadcastPackets)
        
        if self.isOutOctetsRequested():
            valOutOctets = Value()
            valOutOctets.setEmpty()
            tagValueList.push(("out-octets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOutOctets)
        
        if self.isOutMulticastPacketsRequested():
            valOutMulticastPackets = Value()
            valOutMulticastPackets.setEmpty()
            tagValueList.push(("out-multicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOutMulticastPackets)
        
        if self.isInUnicastPacketsRequested():
            valInUnicastPackets = Value()
            valInUnicastPackets.setEmpty()
            tagValueList.push(("in-unicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInUnicastPackets)
        
        if self.isOutErrorPacketsRequested():
            valOutErrorPackets = Value()
            valOutErrorPackets.setEmpty()
            tagValueList.push(("out-error-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOutErrorPackets)
        
        if self.isOutPacketsRateRequested():
            valOutPacketsRate = Value()
            valOutPacketsRate.setEmpty()
            tagValueList.push(("out-packets-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOutPacketsRate)
        
        if self.isInPacketsRequested():
            valInPackets = Value()
            valInPackets.setEmpty()
            tagValueList.push(("in-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInPackets)
        
        if self.isOperationalStatusChangesRequested():
            valOperationalStatusChanges = Value()
            valOperationalStatusChanges.setEmpty()
            tagValueList.push(("operational-status-changes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOperationalStatusChanges)
        
        if self.isInBitsRateRequested():
            valInBitsRate = Value()
            valInBitsRate.setEmpty()
            tagValueList.push(("in-bits-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInBitsRate)
        
        if self.isOutBitsRateRequested():
            valOutBitsRate = Value()
            valOutBitsRate.setEmpty()
            tagValueList.push(("out-bits-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valOutBitsRate)
        
        if self.isInBroadcastPacketsRequested():
            valInBroadcastPackets = Value()
            valInBroadcastPackets.setEmpty()
            tagValueList.push(("in-broadcast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valInBroadcastPackets)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isOutGratuitousArpPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "out-gratuitous-arp-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-outgratuitousarppackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "outGratuitousArpPackets", "out-gratuitous-arp-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-out-gratuitous-arp-packets-bad-value').infoFunc(): logFunc('outGratuitousArpPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOutGratuitousArpPackets(tempVar)
            for logFunc in self._log('read-tag-values-out-gratuitous-arp-packets').debug3Func(): logFunc('read outGratuitousArpPackets. outGratuitousArpPackets=%s, tempValue=%s', self.outGratuitousArpPackets, tempValue.getType())
        
        if self.isOutUnicastPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "out-unicast-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-outunicastpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "outUnicastPackets", "out-unicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-out-unicast-packets-bad-value').infoFunc(): logFunc('outUnicastPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOutUnicastPackets(tempVar)
            for logFunc in self._log('read-tag-values-out-unicast-packets').debug3Func(): logFunc('read outUnicastPackets. outUnicastPackets=%s, tempValue=%s', self.outUnicastPackets, tempValue.getType())
        
        if self.isInUnknownProtocolPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-unknown-protocol-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inunknownprotocolpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inUnknownProtocolPackets", "in-unknown-protocol-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-unknown-protocol-packets-bad-value').infoFunc(): logFunc('inUnknownProtocolPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInUnknownProtocolPackets(tempVar)
            for logFunc in self._log('read-tag-values-in-unknown-protocol-packets').debug3Func(): logFunc('read inUnknownProtocolPackets. inUnknownProtocolPackets=%s, tempValue=%s', self.inUnknownProtocolPackets, tempValue.getType())
        
        if self.isOutDiscardPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "out-discard-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-outdiscardpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "outDiscardPackets", "out-discard-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-out-discard-packets-bad-value').infoFunc(): logFunc('outDiscardPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOutDiscardPackets(tempVar)
            for logFunc in self._log('read-tag-values-out-discard-packets').debug3Func(): logFunc('read outDiscardPackets. outDiscardPackets=%s, tempValue=%s', self.outDiscardPackets, tempValue.getType())
        
        if self.isInOctetsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-octets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inoctets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inOctets", "in-octets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-octets-bad-value').infoFunc(): logFunc('inOctets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInOctets(tempVar)
            for logFunc in self._log('read-tag-values-in-octets').debug3Func(): logFunc('read inOctets. inOctets=%s, tempValue=%s', self.inOctets, tempValue.getType())
        
        if self.isInErrorPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-error-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inerrorpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inErrorPackets", "in-error-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-error-packets-bad-value').infoFunc(): logFunc('inErrorPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInErrorPackets(tempVar)
            for logFunc in self._log('read-tag-values-in-error-packets').debug3Func(): logFunc('read inErrorPackets. inErrorPackets=%s, tempValue=%s', self.inErrorPackets, tempValue.getType())
        
        if self.isInPacketsRateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-packets-rate") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inpacketsrate').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inPacketsRate", "in-packets-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-packets-rate-bad-value').infoFunc(): logFunc('inPacketsRate not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInPacketsRate(tempVar)
            for logFunc in self._log('read-tag-values-in-packets-rate').debug3Func(): logFunc('read inPacketsRate. inPacketsRate=%s, tempValue=%s', self.inPacketsRate, tempValue.getType())
        
        if self.isOutPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "out-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-outpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "outPackets", "out-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-out-packets-bad-value').infoFunc(): logFunc('outPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOutPackets(tempVar)
            for logFunc in self._log('read-tag-values-out-packets').debug3Func(): logFunc('read outPackets. outPackets=%s, tempValue=%s', self.outPackets, tempValue.getType())
        
        if self.isInDiscardPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-discard-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-indiscardpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inDiscardPackets", "in-discard-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-discard-packets-bad-value').infoFunc(): logFunc('inDiscardPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInDiscardPackets(tempVar)
            for logFunc in self._log('read-tag-values-in-discard-packets').debug3Func(): logFunc('read inDiscardPackets. inDiscardPackets=%s, tempValue=%s', self.inDiscardPackets, tempValue.getType())
        
        if self.isInMulticastPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-multicast-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inmulticastpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inMulticastPackets", "in-multicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-multicast-packets-bad-value').infoFunc(): logFunc('inMulticastPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInMulticastPackets(tempVar)
            for logFunc in self._log('read-tag-values-in-multicast-packets').debug3Func(): logFunc('read inMulticastPackets. inMulticastPackets=%s, tempValue=%s', self.inMulticastPackets, tempValue.getType())
        
        if self.isOutBroadcastPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "out-broadcast-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-outbroadcastpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "outBroadcastPackets", "out-broadcast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-out-broadcast-packets-bad-value').infoFunc(): logFunc('outBroadcastPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOutBroadcastPackets(tempVar)
            for logFunc in self._log('read-tag-values-out-broadcast-packets').debug3Func(): logFunc('read outBroadcastPackets. outBroadcastPackets=%s, tempValue=%s', self.outBroadcastPackets, tempValue.getType())
        
        if self.isOutOctetsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "out-octets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-outoctets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "outOctets", "out-octets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-out-octets-bad-value').infoFunc(): logFunc('outOctets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOutOctets(tempVar)
            for logFunc in self._log('read-tag-values-out-octets').debug3Func(): logFunc('read outOctets. outOctets=%s, tempValue=%s', self.outOctets, tempValue.getType())
        
        if self.isOutMulticastPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "out-multicast-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-outmulticastpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "outMulticastPackets", "out-multicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-out-multicast-packets-bad-value').infoFunc(): logFunc('outMulticastPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOutMulticastPackets(tempVar)
            for logFunc in self._log('read-tag-values-out-multicast-packets').debug3Func(): logFunc('read outMulticastPackets. outMulticastPackets=%s, tempValue=%s', self.outMulticastPackets, tempValue.getType())
        
        if self.isInUnicastPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-unicast-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inunicastpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inUnicastPackets", "in-unicast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-unicast-packets-bad-value').infoFunc(): logFunc('inUnicastPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInUnicastPackets(tempVar)
            for logFunc in self._log('read-tag-values-in-unicast-packets').debug3Func(): logFunc('read inUnicastPackets. inUnicastPackets=%s, tempValue=%s', self.inUnicastPackets, tempValue.getType())
        
        if self.isOutErrorPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "out-error-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-outerrorpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "outErrorPackets", "out-error-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-out-error-packets-bad-value').infoFunc(): logFunc('outErrorPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOutErrorPackets(tempVar)
            for logFunc in self._log('read-tag-values-out-error-packets').debug3Func(): logFunc('read outErrorPackets. outErrorPackets=%s, tempValue=%s', self.outErrorPackets, tempValue.getType())
        
        if self.isOutPacketsRateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "out-packets-rate") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-outpacketsrate').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "outPacketsRate", "out-packets-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-out-packets-rate-bad-value').infoFunc(): logFunc('outPacketsRate not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOutPacketsRate(tempVar)
            for logFunc in self._log('read-tag-values-out-packets-rate').debug3Func(): logFunc('read outPacketsRate. outPacketsRate=%s, tempValue=%s', self.outPacketsRate, tempValue.getType())
        
        if self.isInPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inPackets", "in-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-packets-bad-value').infoFunc(): logFunc('inPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInPackets(tempVar)
            for logFunc in self._log('read-tag-values-in-packets').debug3Func(): logFunc('read inPackets. inPackets=%s, tempValue=%s', self.inPackets, tempValue.getType())
        
        if self.isOperationalStatusChangesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "operational-status-changes") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-operationalstatuschanges').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "operationalStatusChanges", "operational-status-changes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-operational-status-changes-bad-value').infoFunc(): logFunc('operationalStatusChanges not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOperationalStatusChanges(tempVar)
            for logFunc in self._log('read-tag-values-operational-status-changes').debug3Func(): logFunc('read operationalStatusChanges. operationalStatusChanges=%s, tempValue=%s', self.operationalStatusChanges, tempValue.getType())
        
        if self.isInBitsRateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-bits-rate") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inbitsrate').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inBitsRate", "in-bits-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-bits-rate-bad-value').infoFunc(): logFunc('inBitsRate not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInBitsRate(tempVar)
            for logFunc in self._log('read-tag-values-in-bits-rate').debug3Func(): logFunc('read inBitsRate. inBitsRate=%s, tempValue=%s', self.inBitsRate, tempValue.getType())
        
        if self.isOutBitsRateRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "out-bits-rate") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-outbitsrate').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "outBitsRate", "out-bits-rate", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-out-bits-rate-bad-value').infoFunc(): logFunc('outBitsRate not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOutBitsRate(tempVar)
            for logFunc in self._log('read-tag-values-out-bits-rate').debug3Func(): logFunc('read outBitsRate. outBitsRate=%s, tempValue=%s', self.outBitsRate, tempValue.getType())
        
        if self.isInBroadcastPacketsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "in-broadcast-packets") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-inbroadcastpackets').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "inBroadcastPackets", "in-broadcast-packets", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asUint64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-in-broadcast-packets-bad-value').infoFunc(): logFunc('inBroadcastPackets not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setInBroadcastPackets(tempVar)
            for logFunc in self._log('read-tag-values-in-broadcast-packets').debug3Func(): logFunc('read inBroadcastPackets. inBroadcastPackets=%s, tempValue=%s', self.inBroadcastPackets, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.counters.counters_maapi_gen import CountersMaapi", 
        "baseClassName": "CountersMaapiBase", 
        "baseModule": "counters_maapi_base_gen"
    }, 
    "ancestors": [
        {
            "moduleYangNamespacePrefix": "qt", 
            "yangName": "tech", 
            "namespace": "tech", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech", 
            "name": "tech"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "interfaces", 
            "namespace": "interfaces", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "interfaces"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "isCurrent": false, 
            "yangName": "interface", 
            "namespace": "interface", 
            "isList": true, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "keyLeaf": {
                "varName": "interface", 
                "defaultVal": null, 
                "typeHandler": "handler: StringHandler"
            }, 
            "name": "interface"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outGratuitousArpPackets", 
            "yangName": "out-gratuitous-arp-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outUnicastPackets", 
            "yangName": "out-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnknownProtocolPackets", 
            "yangName": "in-unknown-protocol-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outDiscardPackets", 
            "yangName": "out-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inOctets", 
            "yangName": "in-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inErrorPackets", 
            "yangName": "in-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPacketsRate", 
            "yangName": "in-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPackets", 
            "yangName": "out-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inDiscardPackets", 
            "yangName": "in-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inMulticastPackets", 
            "yangName": "in-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBroadcastPackets", 
            "yangName": "out-broadcast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outOctets", 
            "yangName": "out-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outMulticastPackets", 
            "yangName": "out-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnicastPackets", 
            "yangName": "in-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outErrorPackets", 
            "yangName": "out-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPacketsRate", 
            "yangName": "out-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPackets", 
            "yangName": "in-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "operationalStatusChanges", 
            "yangName": "operational-status-changes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBitsRate", 
            "yangName": "in-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBitsRate", 
            "yangName": "out-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
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
    "configLeaves": [], 
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
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outGratuitousArpPackets", 
            "yangName": "out-gratuitous-arp-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outUnicastPackets", 
            "yangName": "out-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnknownProtocolPackets", 
            "yangName": "in-unknown-protocol-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outDiscardPackets", 
            "yangName": "out-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inOctets", 
            "yangName": "in-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inErrorPackets", 
            "yangName": "in-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPacketsRate", 
            "yangName": "in-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPackets", 
            "yangName": "out-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inDiscardPackets", 
            "yangName": "in-discard-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inMulticastPackets", 
            "yangName": "in-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBroadcastPackets", 
            "yangName": "out-broadcast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outOctets", 
            "yangName": "out-octets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outMulticastPackets", 
            "yangName": "out-multicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inUnicastPackets", 
            "yangName": "in-unicast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outErrorPackets", 
            "yangName": "out-error-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outPacketsRate", 
            "yangName": "out-packets-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inPackets", 
            "yangName": "in-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "operationalStatusChanges", 
            "yangName": "operational-status-changes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBitsRate", 
            "yangName": "in-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "outBitsRate", 
            "yangName": "out-bits-rate", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "inBroadcastPackets", 
            "yangName": "in-broadcast-packets", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


