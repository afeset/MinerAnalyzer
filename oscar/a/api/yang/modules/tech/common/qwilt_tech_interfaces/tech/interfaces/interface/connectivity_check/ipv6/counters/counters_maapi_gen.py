


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

        

        
        self.neighborDiscoveryFailuresRequested = False
        self.neighborDiscoveryFailures = None
        self.neighborDiscoveryFailuresSet = False
        
        self.neighborDiscoveryTimeoutsRequested = False
        self.neighborDiscoveryTimeouts = None
        self.neighborDiscoveryTimeoutsSet = False
        
        self.neighborDiscoverySuccessesRequested = False
        self.neighborDiscoverySuccesses = None
        self.neighborDiscoverySuccessesSet = False
        
        self.pingRequestsSentRequested = False
        self.pingRequestsSent = None
        self.pingRequestsSentSet = False
        
        self.pingFailuresRequested = False
        self.pingFailures = None
        self.pingFailuresSet = False
        
        self.pingSuccessesRequested = False
        self.pingSuccesses = None
        self.pingSuccessesSet = False
        
        self.neighborDiscoveryRequestsSentRequested = False
        self.neighborDiscoveryRequestsSent = None
        self.neighborDiscoveryRequestsSentSet = False
        
        self.pingTimeoutsRequested = False
        self.pingTimeouts = None
        self.pingTimeoutsSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestNeighborDiscoveryFailures(True)
        
        self.requestNeighborDiscoveryTimeouts(True)
        
        self.requestNeighborDiscoverySuccesses(True)
        
        self.requestPingRequestsSent(True)
        
        self.requestPingFailures(True)
        
        self.requestPingSuccesses(True)
        
        self.requestNeighborDiscoveryRequestsSent(True)
        
        self.requestPingTimeouts(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestNeighborDiscoveryFailures(False)
        
        self.requestNeighborDiscoveryTimeouts(False)
        
        self.requestNeighborDiscoverySuccesses(False)
        
        self.requestPingRequestsSent(False)
        
        self.requestPingFailures(False)
        
        self.requestPingSuccesses(False)
        
        self.requestNeighborDiscoveryRequestsSent(False)
        
        self.requestPingTimeouts(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestNeighborDiscoveryFailures(True)
        
        self.requestNeighborDiscoveryTimeouts(True)
        
        self.requestNeighborDiscoverySuccesses(True)
        
        self.requestPingRequestsSent(True)
        
        self.requestPingFailures(True)
        
        self.requestPingSuccesses(True)
        
        self.requestNeighborDiscoveryRequestsSent(True)
        
        self.requestPingTimeouts(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestNeighborDiscoveryFailures(False)
        
        self.requestNeighborDiscoveryTimeouts(False)
        
        self.requestNeighborDiscoverySuccesses(False)
        
        self.requestPingRequestsSent(False)
        
        self.requestPingFailures(False)
        
        self.requestPingSuccesses(False)
        
        self.requestNeighborDiscoveryRequestsSent(False)
        
        self.requestPingTimeouts(False)
        
        

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



    def requestNeighborDiscoveryFailures (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-neighbordiscoveryfailures').debug3Func(): logFunc('called. requested=%s', requested)
        self.neighborDiscoveryFailuresRequested = requested
        self.neighborDiscoveryFailuresSet = False

    def isNeighborDiscoveryFailuresRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-neighbordiscoveryfailures-requested').debug3Func(): logFunc('called. requested=%s', self.neighborDiscoveryFailuresRequested)
        return self.neighborDiscoveryFailuresRequested

    def getNeighborDiscoveryFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-neighbordiscoveryfailures').debug3Func(): logFunc('called. self.neighborDiscoveryFailuresSet=%s, self.neighborDiscoveryFailures=%s', self.neighborDiscoveryFailuresSet, self.neighborDiscoveryFailures)
        if self.neighborDiscoveryFailuresSet:
            return self.neighborDiscoveryFailures
        return None

    def hasNeighborDiscoveryFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-neighbordiscoveryfailures').debug3Func(): logFunc('called. self.neighborDiscoveryFailuresSet=%s, self.neighborDiscoveryFailures=%s', self.neighborDiscoveryFailuresSet, self.neighborDiscoveryFailures)
        if self.neighborDiscoveryFailuresSet:
            return True
        return False

    def setNeighborDiscoveryFailures (self, neighborDiscoveryFailures):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-neighbordiscoveryfailures').debug3Func(): logFunc('called. neighborDiscoveryFailures=%s, old=%s', neighborDiscoveryFailures, self.neighborDiscoveryFailures)
        self.neighborDiscoveryFailuresSet = True
        self.neighborDiscoveryFailures = neighborDiscoveryFailures

    def requestNeighborDiscoveryTimeouts (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-neighbordiscoverytimeouts').debug3Func(): logFunc('called. requested=%s', requested)
        self.neighborDiscoveryTimeoutsRequested = requested
        self.neighborDiscoveryTimeoutsSet = False

    def isNeighborDiscoveryTimeoutsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-neighbordiscoverytimeouts-requested').debug3Func(): logFunc('called. requested=%s', self.neighborDiscoveryTimeoutsRequested)
        return self.neighborDiscoveryTimeoutsRequested

    def getNeighborDiscoveryTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-neighbordiscoverytimeouts').debug3Func(): logFunc('called. self.neighborDiscoveryTimeoutsSet=%s, self.neighborDiscoveryTimeouts=%s', self.neighborDiscoveryTimeoutsSet, self.neighborDiscoveryTimeouts)
        if self.neighborDiscoveryTimeoutsSet:
            return self.neighborDiscoveryTimeouts
        return None

    def hasNeighborDiscoveryTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-neighbordiscoverytimeouts').debug3Func(): logFunc('called. self.neighborDiscoveryTimeoutsSet=%s, self.neighborDiscoveryTimeouts=%s', self.neighborDiscoveryTimeoutsSet, self.neighborDiscoveryTimeouts)
        if self.neighborDiscoveryTimeoutsSet:
            return True
        return False

    def setNeighborDiscoveryTimeouts (self, neighborDiscoveryTimeouts):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-neighbordiscoverytimeouts').debug3Func(): logFunc('called. neighborDiscoveryTimeouts=%s, old=%s', neighborDiscoveryTimeouts, self.neighborDiscoveryTimeouts)
        self.neighborDiscoveryTimeoutsSet = True
        self.neighborDiscoveryTimeouts = neighborDiscoveryTimeouts

    def requestNeighborDiscoverySuccesses (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-neighbordiscoverysuccesses').debug3Func(): logFunc('called. requested=%s', requested)
        self.neighborDiscoverySuccessesRequested = requested
        self.neighborDiscoverySuccessesSet = False

    def isNeighborDiscoverySuccessesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-neighbordiscoverysuccesses-requested').debug3Func(): logFunc('called. requested=%s', self.neighborDiscoverySuccessesRequested)
        return self.neighborDiscoverySuccessesRequested

    def getNeighborDiscoverySuccesses (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-neighbordiscoverysuccesses').debug3Func(): logFunc('called. self.neighborDiscoverySuccessesSet=%s, self.neighborDiscoverySuccesses=%s', self.neighborDiscoverySuccessesSet, self.neighborDiscoverySuccesses)
        if self.neighborDiscoverySuccessesSet:
            return self.neighborDiscoverySuccesses
        return None

    def hasNeighborDiscoverySuccesses (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-neighbordiscoverysuccesses').debug3Func(): logFunc('called. self.neighborDiscoverySuccessesSet=%s, self.neighborDiscoverySuccesses=%s', self.neighborDiscoverySuccessesSet, self.neighborDiscoverySuccesses)
        if self.neighborDiscoverySuccessesSet:
            return True
        return False

    def setNeighborDiscoverySuccesses (self, neighborDiscoverySuccesses):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-neighbordiscoverysuccesses').debug3Func(): logFunc('called. neighborDiscoverySuccesses=%s, old=%s', neighborDiscoverySuccesses, self.neighborDiscoverySuccesses)
        self.neighborDiscoverySuccessesSet = True
        self.neighborDiscoverySuccesses = neighborDiscoverySuccesses

    def requestPingRequestsSent (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pingrequestssent').debug3Func(): logFunc('called. requested=%s', requested)
        self.pingRequestsSentRequested = requested
        self.pingRequestsSentSet = False

    def isPingRequestsSentRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pingrequestssent-requested').debug3Func(): logFunc('called. requested=%s', self.pingRequestsSentRequested)
        return self.pingRequestsSentRequested

    def getPingRequestsSent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pingrequestssent').debug3Func(): logFunc('called. self.pingRequestsSentSet=%s, self.pingRequestsSent=%s', self.pingRequestsSentSet, self.pingRequestsSent)
        if self.pingRequestsSentSet:
            return self.pingRequestsSent
        return None

    def hasPingRequestsSent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pingrequestssent').debug3Func(): logFunc('called. self.pingRequestsSentSet=%s, self.pingRequestsSent=%s', self.pingRequestsSentSet, self.pingRequestsSent)
        if self.pingRequestsSentSet:
            return True
        return False

    def setPingRequestsSent (self, pingRequestsSent):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pingrequestssent').debug3Func(): logFunc('called. pingRequestsSent=%s, old=%s', pingRequestsSent, self.pingRequestsSent)
        self.pingRequestsSentSet = True
        self.pingRequestsSent = pingRequestsSent

    def requestPingFailures (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pingfailures').debug3Func(): logFunc('called. requested=%s', requested)
        self.pingFailuresRequested = requested
        self.pingFailuresSet = False

    def isPingFailuresRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pingfailures-requested').debug3Func(): logFunc('called. requested=%s', self.pingFailuresRequested)
        return self.pingFailuresRequested

    def getPingFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pingfailures').debug3Func(): logFunc('called. self.pingFailuresSet=%s, self.pingFailures=%s', self.pingFailuresSet, self.pingFailures)
        if self.pingFailuresSet:
            return self.pingFailures
        return None

    def hasPingFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pingfailures').debug3Func(): logFunc('called. self.pingFailuresSet=%s, self.pingFailures=%s', self.pingFailuresSet, self.pingFailures)
        if self.pingFailuresSet:
            return True
        return False

    def setPingFailures (self, pingFailures):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pingfailures').debug3Func(): logFunc('called. pingFailures=%s, old=%s', pingFailures, self.pingFailures)
        self.pingFailuresSet = True
        self.pingFailures = pingFailures

    def requestPingSuccesses (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pingsuccesses').debug3Func(): logFunc('called. requested=%s', requested)
        self.pingSuccessesRequested = requested
        self.pingSuccessesSet = False

    def isPingSuccessesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pingsuccesses-requested').debug3Func(): logFunc('called. requested=%s', self.pingSuccessesRequested)
        return self.pingSuccessesRequested

    def getPingSuccesses (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pingsuccesses').debug3Func(): logFunc('called. self.pingSuccessesSet=%s, self.pingSuccesses=%s', self.pingSuccessesSet, self.pingSuccesses)
        if self.pingSuccessesSet:
            return self.pingSuccesses
        return None

    def hasPingSuccesses (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pingsuccesses').debug3Func(): logFunc('called. self.pingSuccessesSet=%s, self.pingSuccesses=%s', self.pingSuccessesSet, self.pingSuccesses)
        if self.pingSuccessesSet:
            return True
        return False

    def setPingSuccesses (self, pingSuccesses):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pingsuccesses').debug3Func(): logFunc('called. pingSuccesses=%s, old=%s', pingSuccesses, self.pingSuccesses)
        self.pingSuccessesSet = True
        self.pingSuccesses = pingSuccesses

    def requestNeighborDiscoveryRequestsSent (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-neighbordiscoveryrequestssent').debug3Func(): logFunc('called. requested=%s', requested)
        self.neighborDiscoveryRequestsSentRequested = requested
        self.neighborDiscoveryRequestsSentSet = False

    def isNeighborDiscoveryRequestsSentRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-neighbordiscoveryrequestssent-requested').debug3Func(): logFunc('called. requested=%s', self.neighborDiscoveryRequestsSentRequested)
        return self.neighborDiscoveryRequestsSentRequested

    def getNeighborDiscoveryRequestsSent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-neighbordiscoveryrequestssent').debug3Func(): logFunc('called. self.neighborDiscoveryRequestsSentSet=%s, self.neighborDiscoveryRequestsSent=%s', self.neighborDiscoveryRequestsSentSet, self.neighborDiscoveryRequestsSent)
        if self.neighborDiscoveryRequestsSentSet:
            return self.neighborDiscoveryRequestsSent
        return None

    def hasNeighborDiscoveryRequestsSent (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-neighbordiscoveryrequestssent').debug3Func(): logFunc('called. self.neighborDiscoveryRequestsSentSet=%s, self.neighborDiscoveryRequestsSent=%s', self.neighborDiscoveryRequestsSentSet, self.neighborDiscoveryRequestsSent)
        if self.neighborDiscoveryRequestsSentSet:
            return True
        return False

    def setNeighborDiscoveryRequestsSent (self, neighborDiscoveryRequestsSent):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-neighbordiscoveryrequestssent').debug3Func(): logFunc('called. neighborDiscoveryRequestsSent=%s, old=%s', neighborDiscoveryRequestsSent, self.neighborDiscoveryRequestsSent)
        self.neighborDiscoveryRequestsSentSet = True
        self.neighborDiscoveryRequestsSent = neighborDiscoveryRequestsSent

    def requestPingTimeouts (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-pingtimeouts').debug3Func(): logFunc('called. requested=%s', requested)
        self.pingTimeoutsRequested = requested
        self.pingTimeoutsSet = False

    def isPingTimeoutsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-pingtimeouts-requested').debug3Func(): logFunc('called. requested=%s', self.pingTimeoutsRequested)
        return self.pingTimeoutsRequested

    def getPingTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-pingtimeouts').debug3Func(): logFunc('called. self.pingTimeoutsSet=%s, self.pingTimeouts=%s', self.pingTimeoutsSet, self.pingTimeouts)
        if self.pingTimeoutsSet:
            return self.pingTimeouts
        return None

    def hasPingTimeouts (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-pingtimeouts').debug3Func(): logFunc('called. self.pingTimeoutsSet=%s, self.pingTimeouts=%s', self.pingTimeoutsSet, self.pingTimeouts)
        if self.pingTimeoutsSet:
            return True
        return False

    def setPingTimeouts (self, pingTimeouts):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-pingtimeouts').debug3Func(): logFunc('called. pingTimeouts=%s, old=%s', pingTimeouts, self.pingTimeouts)
        self.pingTimeoutsSet = True
        self.pingTimeouts = pingTimeouts


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.neighborDiscoveryFailures = 0
        self.neighborDiscoveryFailuresSet = False
        
        self.neighborDiscoveryTimeouts = 0
        self.neighborDiscoveryTimeoutsSet = False
        
        self.neighborDiscoverySuccesses = 0
        self.neighborDiscoverySuccessesSet = False
        
        self.pingRequestsSent = 0
        self.pingRequestsSentSet = False
        
        self.pingFailures = 0
        self.pingFailuresSet = False
        
        self.pingSuccesses = 0
        self.pingSuccessesSet = False
        
        self.neighborDiscoveryRequestsSent = 0
        self.neighborDiscoveryRequestsSentSet = False
        
        self.pingTimeouts = 0
        self.pingTimeoutsSet = False
        

    def _getSelfKeyPath (self, interface
                         
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ipv6", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("connectivity-check", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", "qt-if"))
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

        
        if self.isNeighborDiscoveryFailuresRequested():
            valNeighborDiscoveryFailures = Value()
            valNeighborDiscoveryFailures.setEmpty()
            tagValueList.push(("neighbor-discovery-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valNeighborDiscoveryFailures)
        
        if self.isNeighborDiscoveryTimeoutsRequested():
            valNeighborDiscoveryTimeouts = Value()
            valNeighborDiscoveryTimeouts.setEmpty()
            tagValueList.push(("neighbor-discovery-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valNeighborDiscoveryTimeouts)
        
        if self.isNeighborDiscoverySuccessesRequested():
            valNeighborDiscoverySuccesses = Value()
            valNeighborDiscoverySuccesses.setEmpty()
            tagValueList.push(("neighbor-discovery-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valNeighborDiscoverySuccesses)
        
        if self.isPingRequestsSentRequested():
            valPingRequestsSent = Value()
            valPingRequestsSent.setEmpty()
            tagValueList.push(("ping-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPingRequestsSent)
        
        if self.isPingFailuresRequested():
            valPingFailures = Value()
            valPingFailures.setEmpty()
            tagValueList.push(("ping-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPingFailures)
        
        if self.isPingSuccessesRequested():
            valPingSuccesses = Value()
            valPingSuccesses.setEmpty()
            tagValueList.push(("ping-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPingSuccesses)
        
        if self.isNeighborDiscoveryRequestsSentRequested():
            valNeighborDiscoveryRequestsSent = Value()
            valNeighborDiscoveryRequestsSent.setEmpty()
            tagValueList.push(("neighbor-discovery-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valNeighborDiscoveryRequestsSent)
        
        if self.isPingTimeoutsRequested():
            valPingTimeouts = Value()
            valPingTimeouts.setEmpty()
            tagValueList.push(("ping-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"), valPingTimeouts)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isNeighborDiscoveryFailuresRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "neighbor-discovery-failures") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-neighbordiscoveryfailures').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "neighborDiscoveryFailures", "neighbor-discovery-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-neighbor-discovery-failures-bad-value').infoFunc(): logFunc('neighborDiscoveryFailures not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNeighborDiscoveryFailures(tempVar)
            for logFunc in self._log('read-tag-values-neighbor-discovery-failures').debug3Func(): logFunc('read neighborDiscoveryFailures. neighborDiscoveryFailures=%s, tempValue=%s', self.neighborDiscoveryFailures, tempValue.getType())
        
        if self.isNeighborDiscoveryTimeoutsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "neighbor-discovery-timeouts") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-neighbordiscoverytimeouts').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "neighborDiscoveryTimeouts", "neighbor-discovery-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-neighbor-discovery-timeouts-bad-value').infoFunc(): logFunc('neighborDiscoveryTimeouts not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNeighborDiscoveryTimeouts(tempVar)
            for logFunc in self._log('read-tag-values-neighbor-discovery-timeouts').debug3Func(): logFunc('read neighborDiscoveryTimeouts. neighborDiscoveryTimeouts=%s, tempValue=%s', self.neighborDiscoveryTimeouts, tempValue.getType())
        
        if self.isNeighborDiscoverySuccessesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "neighbor-discovery-successes") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-neighbordiscoverysuccesses').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "neighborDiscoverySuccesses", "neighbor-discovery-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-neighbor-discovery-successes-bad-value').infoFunc(): logFunc('neighborDiscoverySuccesses not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNeighborDiscoverySuccesses(tempVar)
            for logFunc in self._log('read-tag-values-neighbor-discovery-successes').debug3Func(): logFunc('read neighborDiscoverySuccesses. neighborDiscoverySuccesses=%s, tempValue=%s', self.neighborDiscoverySuccesses, tempValue.getType())
        
        if self.isPingRequestsSentRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ping-requests-sent") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pingrequestssent').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pingRequestsSent", "ping-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ping-requests-sent-bad-value').infoFunc(): logFunc('pingRequestsSent not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPingRequestsSent(tempVar)
            for logFunc in self._log('read-tag-values-ping-requests-sent').debug3Func(): logFunc('read pingRequestsSent. pingRequestsSent=%s, tempValue=%s', self.pingRequestsSent, tempValue.getType())
        
        if self.isPingFailuresRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ping-failures") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pingfailures').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pingFailures", "ping-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ping-failures-bad-value').infoFunc(): logFunc('pingFailures not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPingFailures(tempVar)
            for logFunc in self._log('read-tag-values-ping-failures').debug3Func(): logFunc('read pingFailures. pingFailures=%s, tempValue=%s', self.pingFailures, tempValue.getType())
        
        if self.isPingSuccessesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ping-successes") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pingsuccesses').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pingSuccesses", "ping-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ping-successes-bad-value').infoFunc(): logFunc('pingSuccesses not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPingSuccesses(tempVar)
            for logFunc in self._log('read-tag-values-ping-successes').debug3Func(): logFunc('read pingSuccesses. pingSuccesses=%s, tempValue=%s', self.pingSuccesses, tempValue.getType())
        
        if self.isNeighborDiscoveryRequestsSentRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "neighbor-discovery-requests-sent") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-neighbordiscoveryrequestssent').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "neighborDiscoveryRequestsSent", "neighbor-discovery-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-neighbor-discovery-requests-sent-bad-value').infoFunc(): logFunc('neighborDiscoveryRequestsSent not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setNeighborDiscoveryRequestsSent(tempVar)
            for logFunc in self._log('read-tag-values-neighbor-discovery-requests-sent').debug3Func(): logFunc('read neighborDiscoveryRequestsSent. neighborDiscoveryRequestsSent=%s, tempValue=%s', self.neighborDiscoveryRequestsSent, tempValue.getType())
        
        if self.isPingTimeoutsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "ping-timeouts") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-pingtimeouts').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "pingTimeouts", "ping-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-ping-timeouts-bad-value').infoFunc(): logFunc('pingTimeouts not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPingTimeouts(tempVar)
            for logFunc in self._log('read-tag-values-ping-timeouts').debug3Func(): logFunc('read pingTimeouts. pingTimeouts=%s, tempValue=%s', self.pingTimeouts, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_interfaces.tech.interfaces.interface.connectivity_check.ipv6.counters.counters_maapi_gen import CountersMaapi", 
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
            "yangName": "connectivity-check", 
            "namespace": "connectivity_check", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "connectivity-check"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-if", 
            "yangName": "ipv6", 
            "namespace": "ipv6", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "name": "ipv6"
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
            "memberName": "neighborDiscoveryFailures", 
            "yangName": "neighbor-discovery-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryTimeouts", 
            "yangName": "neighbor-discovery-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoverySuccesses", 
            "yangName": "neighbor-discovery-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingRequestsSent", 
            "yangName": "ping-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingFailures", 
            "yangName": "ping-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingSuccesses", 
            "yangName": "ping-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryRequestsSent", 
            "yangName": "neighbor-discovery-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingTimeouts", 
            "yangName": "ping-timeouts", 
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
            "memberName": "neighborDiscoveryFailures", 
            "yangName": "neighbor-discovery-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryTimeouts", 
            "yangName": "neighbor-discovery-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoverySuccesses", 
            "yangName": "neighbor-discovery-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingRequestsSent", 
            "yangName": "ping-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingFailures", 
            "yangName": "ping-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingSuccesses", 
            "yangName": "ping-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryRequestsSent", 
            "yangName": "neighbor-discovery-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-interfaces", 
            "moduleYangNamespacePrefix": "qt-if", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "pingTimeouts", 
            "yangName": "ping-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


