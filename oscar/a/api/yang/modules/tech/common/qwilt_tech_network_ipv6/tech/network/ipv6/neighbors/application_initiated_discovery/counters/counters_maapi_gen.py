


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

        

        
        self.applicationEntryDiscardsRequested = False
        self.applicationEntryDiscards = None
        self.applicationEntryDiscardsSet = False
        
        self.neighborDiscoveryFailuresRequested = False
        self.neighborDiscoveryFailures = None
        self.neighborDiscoveryFailuresSet = False
        
        self.neighborDiscoveryTimeoutsRequested = False
        self.neighborDiscoveryTimeouts = None
        self.neighborDiscoveryTimeoutsSet = False
        
        self.neighborDiscoverySuccessesRequested = False
        self.neighborDiscoverySuccesses = None
        self.neighborDiscoverySuccessesSet = False
        
        self.pollsRequested = False
        self.polls = None
        self.pollsSet = False
        
        self.applicationRequestFailuresRequested = False
        self.applicationRequestFailures = None
        self.applicationRequestFailuresSet = False
        
        self.applicationEntryUpdatesRequested = False
        self.applicationEntryUpdates = None
        self.applicationEntryUpdatesSet = False
        
        self.osTableLoadFailuresRequested = False
        self.osTableLoadFailures = None
        self.osTableLoadFailuresSet = False
        
        self.applicationRequestDiscardsRequested = False
        self.applicationRequestDiscards = None
        self.applicationRequestDiscardsSet = False
        
        self.applicationRequestBlocksRequested = False
        self.applicationRequestBlocks = None
        self.applicationRequestBlocksSet = False
        
        self.applicationRequestsRequested = False
        self.applicationRequests = None
        self.applicationRequestsSet = False
        
        self.osTableLoadsRequested = False
        self.osTableLoads = None
        self.osTableLoadsSet = False
        
        self.neighborDiscoveryRequestsSentRequested = False
        self.neighborDiscoveryRequestsSent = None
        self.neighborDiscoveryRequestsSentSet = False
        
        self.applicationEntryFailuresRequested = False
        self.applicationEntryFailures = None
        self.applicationEntryFailuresSet = False
        

    def init (self, domain):
        self.myInitGuard.crashIfInitDone()
        for logFunc in self._log('init').debug3Func(): logFunc('called. domain=%s', domain)
        self.domain = domain
        self.myInitGuard.initDone()

    def requestConfigAndOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config-and-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestApplicationEntryDiscards(True)
        
        self.requestNeighborDiscoveryFailures(True)
        
        self.requestNeighborDiscoveryTimeouts(True)
        
        self.requestNeighborDiscoverySuccesses(True)
        
        self.requestPolls(True)
        
        self.requestApplicationRequestFailures(True)
        
        self.requestApplicationEntryUpdates(True)
        
        self.requestOsTableLoadFailures(True)
        
        self.requestApplicationRequestDiscards(True)
        
        self.requestApplicationRequestBlocks(True)
        
        self.requestApplicationRequests(True)
        
        self.requestOsTableLoads(True)
        
        self.requestNeighborDiscoveryRequestsSent(True)
        
        self.requestApplicationEntryFailures(True)
        
        

    def requestConfig (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-config').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestApplicationEntryDiscards(False)
        
        self.requestNeighborDiscoveryFailures(False)
        
        self.requestNeighborDiscoveryTimeouts(False)
        
        self.requestNeighborDiscoverySuccesses(False)
        
        self.requestPolls(False)
        
        self.requestApplicationRequestFailures(False)
        
        self.requestApplicationEntryUpdates(False)
        
        self.requestOsTableLoadFailures(False)
        
        self.requestApplicationRequestDiscards(False)
        
        self.requestApplicationRequestBlocks(False)
        
        self.requestApplicationRequests(False)
        
        self.requestOsTableLoads(False)
        
        self.requestNeighborDiscoveryRequestsSent(False)
        
        self.requestApplicationEntryFailures(False)
        
        

    def requestOper (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-oper').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestApplicationEntryDiscards(True)
        
        self.requestNeighborDiscoveryFailures(True)
        
        self.requestNeighborDiscoveryTimeouts(True)
        
        self.requestNeighborDiscoverySuccesses(True)
        
        self.requestPolls(True)
        
        self.requestApplicationRequestFailures(True)
        
        self.requestApplicationEntryUpdates(True)
        
        self.requestOsTableLoadFailures(True)
        
        self.requestApplicationRequestDiscards(True)
        
        self.requestApplicationRequestBlocks(True)
        
        self.requestApplicationRequests(True)
        
        self.requestOsTableLoads(True)
        
        self.requestNeighborDiscoveryRequestsSent(True)
        
        self.requestApplicationEntryFailures(True)
        
        

    def clearAllRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-requested').debug3Func(): logFunc('called, PARAMS')
        
        
        self.requestApplicationEntryDiscards(False)
        
        self.requestNeighborDiscoveryFailures(False)
        
        self.requestNeighborDiscoveryTimeouts(False)
        
        self.requestNeighborDiscoverySuccesses(False)
        
        self.requestPolls(False)
        
        self.requestApplicationRequestFailures(False)
        
        self.requestApplicationEntryUpdates(False)
        
        self.requestOsTableLoadFailures(False)
        
        self.requestApplicationRequestDiscards(False)
        
        self.requestApplicationRequestBlocks(False)
        
        self.requestApplicationRequests(False)
        
        self.requestOsTableLoads(False)
        
        self.requestNeighborDiscoveryRequestsSent(False)
        
        self.requestApplicationEntryFailures(False)
        
        

    def clearAllSet (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-set').debug3Func(): logFunc('called, PARAMS')
        
        

    def write (self
              , trxContext=None
              ):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('write').debug3Func(): logFunc('called, PARAMS')
        return self._internalWrite(trxContext)

    def read (self
              
              , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  False,
                                  trxContext)

    def readAllOrFail (self
                       
                       , trxContext=None):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-all-or-fail').debug3Func(): logFunc('called, PARAMS')
        return self._internalRead(
                                  True,
                                  trxContext)



    def requestApplicationEntryDiscards (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-applicationentrydiscards').debug3Func(): logFunc('called. requested=%s', requested)
        self.applicationEntryDiscardsRequested = requested
        self.applicationEntryDiscardsSet = False

    def isApplicationEntryDiscardsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-applicationentrydiscards-requested').debug3Func(): logFunc('called. requested=%s', self.applicationEntryDiscardsRequested)
        return self.applicationEntryDiscardsRequested

    def getApplicationEntryDiscards (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-applicationentrydiscards').debug3Func(): logFunc('called. self.applicationEntryDiscardsSet=%s, self.applicationEntryDiscards=%s', self.applicationEntryDiscardsSet, self.applicationEntryDiscards)
        if self.applicationEntryDiscardsSet:
            return self.applicationEntryDiscards
        return None

    def hasApplicationEntryDiscards (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-applicationentrydiscards').debug3Func(): logFunc('called. self.applicationEntryDiscardsSet=%s, self.applicationEntryDiscards=%s', self.applicationEntryDiscardsSet, self.applicationEntryDiscards)
        if self.applicationEntryDiscardsSet:
            return True
        return False

    def setApplicationEntryDiscards (self, applicationEntryDiscards):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-applicationentrydiscards').debug3Func(): logFunc('called. applicationEntryDiscards=%s, old=%s', applicationEntryDiscards, self.applicationEntryDiscards)
        self.applicationEntryDiscardsSet = True
        self.applicationEntryDiscards = applicationEntryDiscards

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

    def requestPolls (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-polls').debug3Func(): logFunc('called. requested=%s', requested)
        self.pollsRequested = requested
        self.pollsSet = False

    def isPollsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-polls-requested').debug3Func(): logFunc('called. requested=%s', self.pollsRequested)
        return self.pollsRequested

    def getPolls (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-polls').debug3Func(): logFunc('called. self.pollsSet=%s, self.polls=%s', self.pollsSet, self.polls)
        if self.pollsSet:
            return self.polls
        return None

    def hasPolls (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-polls').debug3Func(): logFunc('called. self.pollsSet=%s, self.polls=%s', self.pollsSet, self.polls)
        if self.pollsSet:
            return True
        return False

    def setPolls (self, polls):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-polls').debug3Func(): logFunc('called. polls=%s, old=%s', polls, self.polls)
        self.pollsSet = True
        self.polls = polls

    def requestApplicationRequestFailures (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-applicationrequestfailures').debug3Func(): logFunc('called. requested=%s', requested)
        self.applicationRequestFailuresRequested = requested
        self.applicationRequestFailuresSet = False

    def isApplicationRequestFailuresRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-applicationrequestfailures-requested').debug3Func(): logFunc('called. requested=%s', self.applicationRequestFailuresRequested)
        return self.applicationRequestFailuresRequested

    def getApplicationRequestFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-applicationrequestfailures').debug3Func(): logFunc('called. self.applicationRequestFailuresSet=%s, self.applicationRequestFailures=%s', self.applicationRequestFailuresSet, self.applicationRequestFailures)
        if self.applicationRequestFailuresSet:
            return self.applicationRequestFailures
        return None

    def hasApplicationRequestFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-applicationrequestfailures').debug3Func(): logFunc('called. self.applicationRequestFailuresSet=%s, self.applicationRequestFailures=%s', self.applicationRequestFailuresSet, self.applicationRequestFailures)
        if self.applicationRequestFailuresSet:
            return True
        return False

    def setApplicationRequestFailures (self, applicationRequestFailures):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-applicationrequestfailures').debug3Func(): logFunc('called. applicationRequestFailures=%s, old=%s', applicationRequestFailures, self.applicationRequestFailures)
        self.applicationRequestFailuresSet = True
        self.applicationRequestFailures = applicationRequestFailures

    def requestApplicationEntryUpdates (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-applicationentryupdates').debug3Func(): logFunc('called. requested=%s', requested)
        self.applicationEntryUpdatesRequested = requested
        self.applicationEntryUpdatesSet = False

    def isApplicationEntryUpdatesRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-applicationentryupdates-requested').debug3Func(): logFunc('called. requested=%s', self.applicationEntryUpdatesRequested)
        return self.applicationEntryUpdatesRequested

    def getApplicationEntryUpdates (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-applicationentryupdates').debug3Func(): logFunc('called. self.applicationEntryUpdatesSet=%s, self.applicationEntryUpdates=%s', self.applicationEntryUpdatesSet, self.applicationEntryUpdates)
        if self.applicationEntryUpdatesSet:
            return self.applicationEntryUpdates
        return None

    def hasApplicationEntryUpdates (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-applicationentryupdates').debug3Func(): logFunc('called. self.applicationEntryUpdatesSet=%s, self.applicationEntryUpdates=%s', self.applicationEntryUpdatesSet, self.applicationEntryUpdates)
        if self.applicationEntryUpdatesSet:
            return True
        return False

    def setApplicationEntryUpdates (self, applicationEntryUpdates):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-applicationentryupdates').debug3Func(): logFunc('called. applicationEntryUpdates=%s, old=%s', applicationEntryUpdates, self.applicationEntryUpdates)
        self.applicationEntryUpdatesSet = True
        self.applicationEntryUpdates = applicationEntryUpdates

    def requestOsTableLoadFailures (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-ostableloadfailures').debug3Func(): logFunc('called. requested=%s', requested)
        self.osTableLoadFailuresRequested = requested
        self.osTableLoadFailuresSet = False

    def isOsTableLoadFailuresRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-ostableloadfailures-requested').debug3Func(): logFunc('called. requested=%s', self.osTableLoadFailuresRequested)
        return self.osTableLoadFailuresRequested

    def getOsTableLoadFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ostableloadfailures').debug3Func(): logFunc('called. self.osTableLoadFailuresSet=%s, self.osTableLoadFailures=%s', self.osTableLoadFailuresSet, self.osTableLoadFailures)
        if self.osTableLoadFailuresSet:
            return self.osTableLoadFailures
        return None

    def hasOsTableLoadFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ostableloadfailures').debug3Func(): logFunc('called. self.osTableLoadFailuresSet=%s, self.osTableLoadFailures=%s', self.osTableLoadFailuresSet, self.osTableLoadFailures)
        if self.osTableLoadFailuresSet:
            return True
        return False

    def setOsTableLoadFailures (self, osTableLoadFailures):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ostableloadfailures').debug3Func(): logFunc('called. osTableLoadFailures=%s, old=%s', osTableLoadFailures, self.osTableLoadFailures)
        self.osTableLoadFailuresSet = True
        self.osTableLoadFailures = osTableLoadFailures

    def requestApplicationRequestDiscards (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-applicationrequestdiscards').debug3Func(): logFunc('called. requested=%s', requested)
        self.applicationRequestDiscardsRequested = requested
        self.applicationRequestDiscardsSet = False

    def isApplicationRequestDiscardsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-applicationrequestdiscards-requested').debug3Func(): logFunc('called. requested=%s', self.applicationRequestDiscardsRequested)
        return self.applicationRequestDiscardsRequested

    def getApplicationRequestDiscards (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-applicationrequestdiscards').debug3Func(): logFunc('called. self.applicationRequestDiscardsSet=%s, self.applicationRequestDiscards=%s', self.applicationRequestDiscardsSet, self.applicationRequestDiscards)
        if self.applicationRequestDiscardsSet:
            return self.applicationRequestDiscards
        return None

    def hasApplicationRequestDiscards (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-applicationrequestdiscards').debug3Func(): logFunc('called. self.applicationRequestDiscardsSet=%s, self.applicationRequestDiscards=%s', self.applicationRequestDiscardsSet, self.applicationRequestDiscards)
        if self.applicationRequestDiscardsSet:
            return True
        return False

    def setApplicationRequestDiscards (self, applicationRequestDiscards):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-applicationrequestdiscards').debug3Func(): logFunc('called. applicationRequestDiscards=%s, old=%s', applicationRequestDiscards, self.applicationRequestDiscards)
        self.applicationRequestDiscardsSet = True
        self.applicationRequestDiscards = applicationRequestDiscards

    def requestApplicationRequestBlocks (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-applicationrequestblocks').debug3Func(): logFunc('called. requested=%s', requested)
        self.applicationRequestBlocksRequested = requested
        self.applicationRequestBlocksSet = False

    def isApplicationRequestBlocksRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-applicationrequestblocks-requested').debug3Func(): logFunc('called. requested=%s', self.applicationRequestBlocksRequested)
        return self.applicationRequestBlocksRequested

    def getApplicationRequestBlocks (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-applicationrequestblocks').debug3Func(): logFunc('called. self.applicationRequestBlocksSet=%s, self.applicationRequestBlocks=%s', self.applicationRequestBlocksSet, self.applicationRequestBlocks)
        if self.applicationRequestBlocksSet:
            return self.applicationRequestBlocks
        return None

    def hasApplicationRequestBlocks (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-applicationrequestblocks').debug3Func(): logFunc('called. self.applicationRequestBlocksSet=%s, self.applicationRequestBlocks=%s', self.applicationRequestBlocksSet, self.applicationRequestBlocks)
        if self.applicationRequestBlocksSet:
            return True
        return False

    def setApplicationRequestBlocks (self, applicationRequestBlocks):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-applicationrequestblocks').debug3Func(): logFunc('called. applicationRequestBlocks=%s, old=%s', applicationRequestBlocks, self.applicationRequestBlocks)
        self.applicationRequestBlocksSet = True
        self.applicationRequestBlocks = applicationRequestBlocks

    def requestApplicationRequests (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-applicationrequests').debug3Func(): logFunc('called. requested=%s', requested)
        self.applicationRequestsRequested = requested
        self.applicationRequestsSet = False

    def isApplicationRequestsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-applicationrequests-requested').debug3Func(): logFunc('called. requested=%s', self.applicationRequestsRequested)
        return self.applicationRequestsRequested

    def getApplicationRequests (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-applicationrequests').debug3Func(): logFunc('called. self.applicationRequestsSet=%s, self.applicationRequests=%s', self.applicationRequestsSet, self.applicationRequests)
        if self.applicationRequestsSet:
            return self.applicationRequests
        return None

    def hasApplicationRequests (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-applicationrequests').debug3Func(): logFunc('called. self.applicationRequestsSet=%s, self.applicationRequests=%s', self.applicationRequestsSet, self.applicationRequests)
        if self.applicationRequestsSet:
            return True
        return False

    def setApplicationRequests (self, applicationRequests):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-applicationrequests').debug3Func(): logFunc('called. applicationRequests=%s, old=%s', applicationRequests, self.applicationRequests)
        self.applicationRequestsSet = True
        self.applicationRequests = applicationRequests

    def requestOsTableLoads (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-ostableloads').debug3Func(): logFunc('called. requested=%s', requested)
        self.osTableLoadsRequested = requested
        self.osTableLoadsSet = False

    def isOsTableLoadsRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-ostableloads-requested').debug3Func(): logFunc('called. requested=%s', self.osTableLoadsRequested)
        return self.osTableLoadsRequested

    def getOsTableLoads (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-ostableloads').debug3Func(): logFunc('called. self.osTableLoadsSet=%s, self.osTableLoads=%s', self.osTableLoadsSet, self.osTableLoads)
        if self.osTableLoadsSet:
            return self.osTableLoads
        return None

    def hasOsTableLoads (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-ostableloads').debug3Func(): logFunc('called. self.osTableLoadsSet=%s, self.osTableLoads=%s', self.osTableLoadsSet, self.osTableLoads)
        if self.osTableLoadsSet:
            return True
        return False

    def setOsTableLoads (self, osTableLoads):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-ostableloads').debug3Func(): logFunc('called. osTableLoads=%s, old=%s', osTableLoads, self.osTableLoads)
        self.osTableLoadsSet = True
        self.osTableLoads = osTableLoads

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

    def requestApplicationEntryFailures (self, requested):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('request-applicationentryfailures').debug3Func(): logFunc('called. requested=%s', requested)
        self.applicationEntryFailuresRequested = requested
        self.applicationEntryFailuresSet = False

    def isApplicationEntryFailuresRequested (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('is-applicationentryfailures-requested').debug3Func(): logFunc('called. requested=%s', self.applicationEntryFailuresRequested)
        return self.applicationEntryFailuresRequested

    def getApplicationEntryFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('get-applicationentryfailures').debug3Func(): logFunc('called. self.applicationEntryFailuresSet=%s, self.applicationEntryFailures=%s', self.applicationEntryFailuresSet, self.applicationEntryFailures)
        if self.applicationEntryFailuresSet:
            return self.applicationEntryFailures
        return None

    def hasApplicationEntryFailures (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('has-applicationentryfailures').debug3Func(): logFunc('called. self.applicationEntryFailuresSet=%s, self.applicationEntryFailures=%s', self.applicationEntryFailuresSet, self.applicationEntryFailures)
        if self.applicationEntryFailuresSet:
            return True
        return False

    def setApplicationEntryFailures (self, applicationEntryFailures):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('set-applicationentryfailures').debug3Func(): logFunc('called. applicationEntryFailures=%s, old=%s', applicationEntryFailures, self.applicationEntryFailures)
        self.applicationEntryFailuresSet = True
        self.applicationEntryFailures = applicationEntryFailures


    def _clearAllReadData (self):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('clear-all-read-data').debug3Func(): logFunc('called')

        

        
        self.applicationEntryDiscards = 0
        self.applicationEntryDiscardsSet = False
        
        self.neighborDiscoveryFailures = 0
        self.neighborDiscoveryFailuresSet = False
        
        self.neighborDiscoveryTimeouts = 0
        self.neighborDiscoveryTimeoutsSet = False
        
        self.neighborDiscoverySuccesses = 0
        self.neighborDiscoverySuccessesSet = False
        
        self.polls = 0
        self.pollsSet = False
        
        self.applicationRequestFailures = 0
        self.applicationRequestFailuresSet = False
        
        self.applicationEntryUpdates = 0
        self.applicationEntryUpdatesSet = False
        
        self.osTableLoadFailures = 0
        self.osTableLoadFailuresSet = False
        
        self.applicationRequestDiscards = 0
        self.applicationRequestDiscardsSet = False
        
        self.applicationRequestBlocks = 0
        self.applicationRequestBlocksSet = False
        
        self.applicationRequests = 0
        self.applicationRequestsSet = False
        
        self.osTableLoads = 0
        self.osTableLoadsSet = False
        
        self.neighborDiscoveryRequestsSent = 0
        self.neighborDiscoveryRequestsSentSet = False
        
        self.applicationEntryFailures = 0
        self.applicationEntryFailuresSet = False
        

    def _getSelfKeyPath (self
                         , junkForTemplate):
        for logFunc in self._log('get-self-key-path').debug3Func(): logFunc('called. PARAMS, junkForTemplate=%s', junkForTemplate)
        keyPath = KeyPath()
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("counters", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("application-initiated-discovery", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("neighbors", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("ipv6", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", "qt-net-ip6"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("network", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network", "qt-net"))
        keyPath.addKeyPathPrefix(xmlVal)
        
        
        xmlVal = Value()
        xmlVal.setXmlTag(("tech", "http://qwilt.com/ns/yang/device/tech/qwilt-tech", "qt"))
        keyPath.addKeyPathPrefix(xmlVal)
        

        for logFunc in self._log('get-self-key-path-done').debug3Func(): logFunc('done. keyPath=%s. PARAMS', keyPath)
        return keyPath

    def _internalWrite (self, 
                        
                        trxContext):
        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('internal-write').debug3Func(): logFunc('called. PARAMS')

        tagValueList = TagValues()

        res = self._fillWriteTagValues(tagValueList)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-fill-write-tag-value-failed').errorFunc(): logFunc('_fillWriteTagValues() failed. PARAMS')
            return ReturnCodes.kGeneralError

        itemsToDelete = []
        res = self._collectItemsToDelete(
                                         itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-collect-items-to-delete-failed').errorFunc(): logFunc('_collectItemsToDelete() failed. PARAMS')
            return ReturnCodes.kGeneralError

        keyPath = self._getSelfKeyPath(
                                       None)

        res = self.domain.writeMaapi(tagValueList, keyPath, trxContext, itemsToDelete)
        if res != ReturnCodes.kOk:
            for logFunc in self._log('write-domain-failed').errorFunc(): logFunc('domain.writeMaapi() failed. PARAMS')
            return ReturnCodes.kGeneralError

        for logFunc in self._log('internal-write-done').debug3Func(): logFunc('done. PARAMS')
        return ReturnCodes.kOk

    def _internalRead (self, 
                       
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

        keyPath = self._getSelfKeyPath(
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

        
        if self.isApplicationEntryDiscardsRequested():
            valApplicationEntryDiscards = Value()
            valApplicationEntryDiscards.setEmpty()
            tagValueList.push(("application-entry-discards", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valApplicationEntryDiscards)
        
        if self.isNeighborDiscoveryFailuresRequested():
            valNeighborDiscoveryFailures = Value()
            valNeighborDiscoveryFailures.setEmpty()
            tagValueList.push(("neighbor-discovery-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valNeighborDiscoveryFailures)
        
        if self.isNeighborDiscoveryTimeoutsRequested():
            valNeighborDiscoveryTimeouts = Value()
            valNeighborDiscoveryTimeouts.setEmpty()
            tagValueList.push(("neighbor-discovery-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valNeighborDiscoveryTimeouts)
        
        if self.isNeighborDiscoverySuccessesRequested():
            valNeighborDiscoverySuccesses = Value()
            valNeighborDiscoverySuccesses.setEmpty()
            tagValueList.push(("neighbor-discovery-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valNeighborDiscoverySuccesses)
        
        if self.isPollsRequested():
            valPolls = Value()
            valPolls.setEmpty()
            tagValueList.push(("polls", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valPolls)
        
        if self.isApplicationRequestFailuresRequested():
            valApplicationRequestFailures = Value()
            valApplicationRequestFailures.setEmpty()
            tagValueList.push(("application-request-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valApplicationRequestFailures)
        
        if self.isApplicationEntryUpdatesRequested():
            valApplicationEntryUpdates = Value()
            valApplicationEntryUpdates.setEmpty()
            tagValueList.push(("application-entry-updates", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valApplicationEntryUpdates)
        
        if self.isOsTableLoadFailuresRequested():
            valOsTableLoadFailures = Value()
            valOsTableLoadFailures.setEmpty()
            tagValueList.push(("os-table-load-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valOsTableLoadFailures)
        
        if self.isApplicationRequestDiscardsRequested():
            valApplicationRequestDiscards = Value()
            valApplicationRequestDiscards.setEmpty()
            tagValueList.push(("application-request-discards", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valApplicationRequestDiscards)
        
        if self.isApplicationRequestBlocksRequested():
            valApplicationRequestBlocks = Value()
            valApplicationRequestBlocks.setEmpty()
            tagValueList.push(("application-request-blocks", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valApplicationRequestBlocks)
        
        if self.isApplicationRequestsRequested():
            valApplicationRequests = Value()
            valApplicationRequests.setEmpty()
            tagValueList.push(("application-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valApplicationRequests)
        
        if self.isOsTableLoadsRequested():
            valOsTableLoads = Value()
            valOsTableLoads.setEmpty()
            tagValueList.push(("os-table-loads", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valOsTableLoads)
        
        if self.isNeighborDiscoveryRequestsSentRequested():
            valNeighborDiscoveryRequestsSent = Value()
            valNeighborDiscoveryRequestsSent.setEmpty()
            tagValueList.push(("neighbor-discovery-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valNeighborDiscoveryRequestsSent)
        
        if self.isApplicationEntryFailuresRequested():
            valApplicationEntryFailures = Value()
            valApplicationEntryFailures.setEmpty()
            tagValueList.push(("application-entry-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"), valApplicationEntryFailures)
        

        

        return ReturnCodes.kOk

    def _readTagValues (self, tagValueList, readAllOrFail):
        __pychecker__ = 'maxlines=300'
        __pychecker__ = 'maxreturns=30'

        self.myInitGuard.isInitOrCrash()
        for logFunc in self._log('read-tag-values').debug3Func(): logFunc('called. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)

        res = ReturnCodes.kOk

        for logFunc in self._log('read-tag-values-leaves').debug3Func(): logFunc('reading leaves. tagValueList=%s', tagValueList)
        
        if self.isApplicationEntryDiscardsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "application-entry-discards") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-applicationentrydiscards').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "applicationEntryDiscards", "application-entry-discards", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-application-entry-discards-bad-value').infoFunc(): logFunc('applicationEntryDiscards not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setApplicationEntryDiscards(tempVar)
            for logFunc in self._log('read-tag-values-application-entry-discards').debug3Func(): logFunc('read applicationEntryDiscards. applicationEntryDiscards=%s, tempValue=%s', self.applicationEntryDiscards, tempValue.getType())
        
        if self.isNeighborDiscoveryFailuresRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "neighbor-discovery-failures") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-neighbordiscoveryfailures').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "neighborDiscoveryFailures", "neighbor-discovery-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-neighbordiscoverytimeouts').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "neighborDiscoveryTimeouts", "neighbor-discovery-timeouts", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
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
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-neighbordiscoverysuccesses').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "neighborDiscoverySuccesses", "neighbor-discovery-successes", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
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
        
        if self.isPollsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "polls") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-polls').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "polls", "polls", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-polls-bad-value').infoFunc(): logFunc('polls not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setPolls(tempVar)
            for logFunc in self._log('read-tag-values-polls').debug3Func(): logFunc('read polls. polls=%s, tempValue=%s', self.polls, tempValue.getType())
        
        if self.isApplicationRequestFailuresRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "application-request-failures") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-applicationrequestfailures').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "applicationRequestFailures", "application-request-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-application-request-failures-bad-value').infoFunc(): logFunc('applicationRequestFailures not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setApplicationRequestFailures(tempVar)
            for logFunc in self._log('read-tag-values-application-request-failures').debug3Func(): logFunc('read applicationRequestFailures. applicationRequestFailures=%s, tempValue=%s', self.applicationRequestFailures, tempValue.getType())
        
        if self.isApplicationEntryUpdatesRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "application-entry-updates") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-applicationentryupdates').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "applicationEntryUpdates", "application-entry-updates", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-application-entry-updates-bad-value').infoFunc(): logFunc('applicationEntryUpdates not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setApplicationEntryUpdates(tempVar)
            for logFunc in self._log('read-tag-values-application-entry-updates').debug3Func(): logFunc('read applicationEntryUpdates. applicationEntryUpdates=%s, tempValue=%s', self.applicationEntryUpdates, tempValue.getType())
        
        if self.isOsTableLoadFailuresRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "os-table-load-failures") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-ostableloadfailures').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "osTableLoadFailures", "os-table-load-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-os-table-load-failures-bad-value').infoFunc(): logFunc('osTableLoadFailures not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOsTableLoadFailures(tempVar)
            for logFunc in self._log('read-tag-values-os-table-load-failures').debug3Func(): logFunc('read osTableLoadFailures. osTableLoadFailures=%s, tempValue=%s', self.osTableLoadFailures, tempValue.getType())
        
        if self.isApplicationRequestDiscardsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "application-request-discards") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-applicationrequestdiscards').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "applicationRequestDiscards", "application-request-discards", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-application-request-discards-bad-value').infoFunc(): logFunc('applicationRequestDiscards not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setApplicationRequestDiscards(tempVar)
            for logFunc in self._log('read-tag-values-application-request-discards').debug3Func(): logFunc('read applicationRequestDiscards. applicationRequestDiscards=%s, tempValue=%s', self.applicationRequestDiscards, tempValue.getType())
        
        if self.isApplicationRequestBlocksRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "application-request-blocks") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-applicationrequestblocks').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "applicationRequestBlocks", "application-request-blocks", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-application-request-blocks-bad-value').infoFunc(): logFunc('applicationRequestBlocks not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setApplicationRequestBlocks(tempVar)
            for logFunc in self._log('read-tag-values-application-request-blocks').debug3Func(): logFunc('read applicationRequestBlocks. applicationRequestBlocks=%s, tempValue=%s', self.applicationRequestBlocks, tempValue.getType())
        
        if self.isApplicationRequestsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "application-requests") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-applicationrequests').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "applicationRequests", "application-requests", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-application-requests-bad-value').infoFunc(): logFunc('applicationRequests not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setApplicationRequests(tempVar)
            for logFunc in self._log('read-tag-values-application-requests').debug3Func(): logFunc('read applicationRequests. applicationRequests=%s, tempValue=%s', self.applicationRequests, tempValue.getType())
        
        if self.isOsTableLoadsRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "os-table-loads") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-ostableloads').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "osTableLoads", "os-table-loads", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-os-table-loads-bad-value').infoFunc(): logFunc('osTableLoads not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setOsTableLoads(tempVar)
            for logFunc in self._log('read-tag-values-os-table-loads').debug3Func(): logFunc('read osTableLoads. osTableLoads=%s, tempValue=%s', self.osTableLoads, tempValue.getType())
        
        if self.isNeighborDiscoveryRequestsSentRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "neighbor-discovery-requests-sent") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-neighbordiscoveryrequestssent').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "neighborDiscoveryRequestsSent", "neighbor-discovery-requests-sent", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
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
        
        if self.isApplicationEntryFailuresRequested():
            ((tag, ns), tempValue) = tagValueList.popFront()
            if (tag != "application-entry-failures") or \
                (ns != "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6"):
                for logFunc in self._log('reag-tag-values-unexpected-tag-leaf-applicationentryfailures').errorFunc(): logFunc('got unexpected tag-value for leaf: %s. expected: (%s, %s), got: (%s, %s)',
                                                                                                 "applicationEntryFailures", "application-entry-failures", "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", tag, ns)
                self._clearAllReadData()
                return ReturnCodes.kGeneralError

            tempVar = None
            tempVar = tempValue.asInt64()
            if res != ReturnCodes.kOk or tempVar is None:
                for logFunc in self._log('read-tag-values-application-entry-failures-bad-value').infoFunc(): logFunc('applicationEntryFailures not read')
                if readAllOrFail:
                    self._clearAllReadData()
                    return ReturnCodes.kGeneralError
            if tempVar is not None:
                self.setApplicationEntryFailures(tempVar)
            for logFunc in self._log('read-tag-values-application-entry-failures').debug3Func(): logFunc('read applicationEntryFailures. applicationEntryFailures=%s, tempValue=%s', self.applicationEntryFailures, tempValue.getType())
        

        

        for logFunc in self._log('read-tag-values-done').debug3Func(): logFunc('done. readAllOrFail=%s, tagValueList=%s', readAllOrFail, tagValueList)
        return ReturnCodes.kOk



"""
Extracted from the below data: 
{
    "node": {
        "name": "counters", 
        "namespace": "counters", 
        "className": "CountersMaapi", 
        "importStatement": "from a.api.yang.modules.tech.common.qwilt_tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.counters.counters_maapi_gen import CountersMaapi", 
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
            "moduleYangNamespacePrefix": "qt-net", 
            "yangName": "network", 
            "namespace": "network", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network", 
            "name": "network"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "ipv6", 
            "namespace": "ipv6", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "ipv6"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "neighbors", 
            "namespace": "neighbors", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "neighbors"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "application-initiated-discovery", 
            "namespace": "application_initiated_discovery", 
            "isCurrent": false, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "application-initiated-discovery"
        }, 
        {
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "yangName": "counters", 
            "namespace": "counters", 
            "isCurrent": true, 
            "isList": false, 
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "name": "counters"
        }
    ], 
    "descendants": [], 
    "conditionalDebugName": null, 
    "operLeaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryDiscards", 
            "yangName": "application-entry-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryFailures", 
            "yangName": "neighbor-discovery-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryTimeouts", 
            "yangName": "neighbor-discovery-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoverySuccesses", 
            "yangName": "neighbor-discovery-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "polls", 
            "yangName": "polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestFailures", 
            "yangName": "application-request-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryUpdates", 
            "yangName": "application-entry-updates", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoadFailures", 
            "yangName": "os-table-load-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestDiscards", 
            "yangName": "application-request-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestBlocks", 
            "yangName": "application-request-blocks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequests", 
            "yangName": "application-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoads", 
            "yangName": "os-table-loads", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryRequestsSent", 
            "yangName": "neighbor-discovery-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryFailures", 
            "yangName": "application-entry-failures", 
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
            "qwilt_tech_network_ipv6"
        ]
    }, 
    "leaves": [
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryDiscards", 
            "yangName": "application-entry-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryFailures", 
            "yangName": "neighbor-discovery-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryTimeouts", 
            "yangName": "neighbor-discovery-timeouts", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoverySuccesses", 
            "yangName": "neighbor-discovery-successes", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "polls", 
            "yangName": "polls", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestFailures", 
            "yangName": "application-request-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryUpdates", 
            "yangName": "application-entry-updates", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoadFailures", 
            "yangName": "os-table-load-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestDiscards", 
            "yangName": "application-request-discards", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequestBlocks", 
            "yangName": "application-request-blocks", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationRequests", 
            "yangName": "application-requests", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "osTableLoads", 
            "yangName": "os-table-loads", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "neighborDiscoveryRequestsSent", 
            "yangName": "neighbor-discovery-requests-sent", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }, 
        {
            "moduleYangNamespace": "http://qwilt.com/ns/yang/device/tech/qwilt-tech-network-ipv6", 
            "moduleYangNamespacePrefix": "qt-net-ip6", 
            "typeHandler": "handler: IntHandler", 
            "memberName": "applicationEntryFailures", 
            "yangName": "application-entry-failures", 
            "object": "", 
            "leafrefPath": null, 
            "defaultVal": null, 
            "hasDefaultRef": false
        }
    ], 
    "createTime": "2013"
}
"""


