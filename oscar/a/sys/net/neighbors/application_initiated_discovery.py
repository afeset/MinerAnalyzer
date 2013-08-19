# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: alex

from a.infra.basic.return_codes import ReturnCodes

from a.sys.net.tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.status.blinky_status_oper_gen import BlinkyOperStatus as AIDBlinkyOperStatus
from a.sys.net.tech_network_ipv6.tech.network.ipv6.neighbors.application_initiated_discovery.counters.blinky_counters_oper_gen import BlinkyOperCounters as AIDBlinkyOperCounters

G_NAME_GROUP_NET_NEIGHBORS_APPLICATION_INITIATED_DISCOVERY = "application-initiated-discovery"

class ApplicationInitiatedDiscoveryContainer(object):
    """This class manages the network neighbors application initiated discovery information"""

### config value valid input ranges ###
    POLL_INTERVAL_RANGE = (1,3600)
    REQUEST_TIMEOUT_RANGE = (0,3600)
    REQUEST_COUNT_RANGE = (0,2147483647)
    MAX_CONCURRENT_REQUESTS_RANGE = (0,100)
    MAX_REQUEST_RATE_RANGE = (0,1000)
    MAX_APPLICATION_ENTRIES_RANGE = (32, 256) 
    MAX_PENDING_REQUESTS_RANGE = (1, 1000)
#######################################

#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_NEIGHBORS_APPLICATION_INITIATED_DISCOVERY)
        self.name = "application-initiated-discovery"

        ### ndisc implementation class here ###
        self.localAddressResolver = None

        ### ndisc periodic task ###
        self.localAddressResolverPeriodicRequestReadTask = None

        self.localAddressResolverPeriodicTableReadTask = None

        self.blinkyApplicationInitiatedDiscovery = None

        #configurations
        self.enabled = True
        self.pollInterval = 10
        self.requestTimeout = 2
        self.requestCount = 5
        self.maxConcurrentRequests = 100
        self.maxApplicationEntries = 128

        ### candidate needed for passing configuration to line ###
        self.maxRequestRate = 100
        self.maxRequestRateCandidate = self.maxRequestRate

        self.maxPendingRequests = 100
        self.maxPendingRequestsCandidate = self.maxPendingRequests

        self.enabledCandidate = self.enabled
        
        


    def notifyAttachToBlinky(self, blinkyApplicationInitiatedDiscovery):
        self.blinkyApplicationInitiatedDiscovery = blinkyApplicationInitiatedDiscovery

#-----------------------------------------------------------------------------------------------------------------------
    def setConfigErrorStr(self, msg):
        if self.blinkyApplicationInitiatedDiscovery:
            self.blinkyApplicationInitiatedDiscovery.setConfigErrorStr(msg)

#-----------------------------------------------------------------------------------------------------------------------
    def setOperErrorStr(self, tctx, msg):
        if self.blinkyApplicationInitiatedDiscovery and tctx:
            self.blinkyApplicationInitiatedDiscovery.setTransError(tctx, msg)

#-----------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        """the interface is being evaluated and verified for correctness"""

        self._log("application-initiated-discovery-prepare-private-value-set").debug3("%s: prepare data - %s", self.name, data)

        if self.localAddressResolver == None:
            self._log("application-initiated-discovery-prepare-private-value-set-no-address-resolver").error("localAddressResolver is None!")
            return ReturnCodes.kBadState

        if self.localAddressResolverPeriodicRequestReadTask == None or self.localAddressResolverPeriodicTableReadTask == None:
            self._log("application-initiated-discovery-prepare-private-value-set-no-address-resolver-task").error("localAddressResolverPeriodicTask is None!")
            return ReturnCodes.kBadState


        if data.pollInterval < ApplicationInitiatedDiscoveryContainer.POLL_INTERVAL_RANGE[0] or data.pollInterval > ApplicationInitiatedDiscoveryContainer.POLL_INTERVAL_RANGE[1]:
            self._log("poll-interval-not-in-range").error("poll-interval must be in range of [%s,%s], got: %s",ApplicationInitiatedDiscoveryContainer.POLL_INTERVAL_RANGE[0],ApplicationInitiatedDiscoveryContainer.POLL_INTERVAL_RANGE[1], data.pollInterval)
            self.setConfigErrorStr("poll-interval must be in range of [%s,%s], got: %s" % (ApplicationInitiatedDiscoveryContainer.POLL_INTERVAL_RANGE[0],ApplicationInitiatedDiscoveryContainer.POLL_INTERVAL_RANGE[1], data.pollInterval))
            return ReturnCodes.kGeneralError

        if data.requestTimeout < ApplicationInitiatedDiscoveryContainer.REQUEST_TIMEOUT_RANGE[0] or data.requestTimeout > ApplicationInitiatedDiscoveryContainer.REQUEST_TIMEOUT_RANGE[1]:
            self._log("request-timeout-not-in-range").error("request-timeout must be in range of [%s,%s], got: %s",ApplicationInitiatedDiscoveryContainer.REQUEST_TIMEOUT_RANGE[0],ApplicationInitiatedDiscoveryContainer.REQUEST_TIMEOUT_RANGE[1], data.requestTimeout)
            self.setConfigErrorStr("request-timeout must be in range of [%s,%s], got: %s" % (ApplicationInitiatedDiscoveryContainer.REQUEST_TIMEOUT_RANGE[0],ApplicationInitiatedDiscoveryContainer.REQUEST_TIMEOUT_RANGE[1], data.requestTimeout))
            return ReturnCodes.kGeneralError

        if data.requestCount < ApplicationInitiatedDiscoveryContainer.REQUEST_COUNT_RANGE[0] or data.requestCount > ApplicationInitiatedDiscoveryContainer.REQUEST_COUNT_RANGE[1]:
            self._log("request-count-not-in-range").error("request-count must be in range of [%s,%s], got: %s",ApplicationInitiatedDiscoveryContainer.REQUEST_COUNT_RANGE[0],ApplicationInitiatedDiscoveryContainer.REQUEST_COUNT_RANGE[1], data.requestCount)
            self.setConfigErrorStr("request-count must be in range of [%s,%s], got: %s" % (ApplicationInitiatedDiscoveryContainer.REQUEST_COUNT_RANGE[0],ApplicationInitiatedDiscoveryContainer.REQUEST_COUNT_RANGE[1], data.requestCount))
            return ReturnCodes.kGeneralError

        if data.maxConcurrentRequests < ApplicationInitiatedDiscoveryContainer.MAX_CONCURRENT_REQUESTS_RANGE[0] or data.maxConcurrentRequests > ApplicationInitiatedDiscoveryContainer.MAX_CONCURRENT_REQUESTS_RANGE[1]:
            self._log("max-concurrent-requests-not-in-range").error("max-concurrent-requests must be in range of [%s,%s], got: %s",ApplicationInitiatedDiscoveryContainer.MAX_CONCURRENT_REQUESTS_RANGE[0],ApplicationInitiatedDiscoveryContainer.MAX_CONCURRENT_REQUESTS_RANGE[1], data.maxConcurrentRequests)
            self.setConfigErrorStr("max-concurrent-requests must be in range of [%s,%s], got: %s" % (ApplicationInitiatedDiscoveryContainer.MAX_CONCURRENT_REQUESTS_RANGE[0],ApplicationInitiatedDiscoveryContainer.MAX_CONCURRENT_REQUESTS_RANGE[1], data.maxConcurrentRequests))
            return ReturnCodes.kGeneralError

        if data.maxRequestRate < ApplicationInitiatedDiscoveryContainer.MAX_REQUEST_RATE_RANGE[0] or data.maxRequestRate > ApplicationInitiatedDiscoveryContainer.MAX_REQUEST_RATE_RANGE[1]:
            self._log("max-request-rate-not-in-range").error("max-request-rate must be in range of [%s,%s], got: %s",ApplicationInitiatedDiscoveryContainer.MAX_REQUEST_RATE_RANGE[0],ApplicationInitiatedDiscoveryContainer.MAX_REQUEST_RATE_RANGE[1], data.maxRequestRate)
            self.setConfigErrorStr("max-request-rate must be in range of [%s,%s], got: %s" % (ApplicationInitiatedDiscoveryContainer.MAX_REQUEST_RATE_RANGE[0],ApplicationInitiatedDiscoveryContainer.MAX_REQUEST_RATE_RANGE[1], data.maxRequestRate))
            return ReturnCodes.kGeneralError
        
        if data.maxPendingRequests < ApplicationInitiatedDiscoveryContainer.MAX_PENDING_REQUESTS_RANGE[0] or data.maxPendingRequests > ApplicationInitiatedDiscoveryContainer.MAX_PENDING_REQUESTS_RANGE[1]:
            self._log("max-pending-requests-not-in-range").error("max-pending-requests must be in range of [%s,%s], got: %s",ApplicationInitiatedDiscoveryContainer.MAX_PENDING_REQUESTS_RANGE[0],ApplicationInitiatedDiscoveryContainer.MAX_PENDING_REQUESTS_RANGE[1], data.maxPendingRequests)
            self.setConfigErrorStr("max-pending-requests must be in range of [%s,%s], got: %s" % (ApplicationInitiatedDiscoveryContainer.MAX_PENDING_REQUESTS_RANGE[0],ApplicationInitiatedDiscoveryContainer.MAX_PENDING_REQUESTS_RANGE[1], data.maxPendingRequests))
            return ReturnCodes.kGeneralError
        
        if data.maxApplicationEntries < ApplicationInitiatedDiscoveryContainer.MAX_APPLICATION_ENTRIES_RANGE[0] or data.maxApplicationEntries > ApplicationInitiatedDiscoveryContainer.MAX_APPLICATION_ENTRIES_RANGE[1]:
            self._log("max-application-entries-not-in-range").error("max-application-entries must be in range of [%s,%s], got: %s",ApplicationInitiatedDiscoveryContainer.MAX_APPLICATION_ENTRIES_RANGE[0],ApplicationInitiatedDiscoveryContainer.MAX_APPLICATION_ENTRIES_RANGE[1], data.maxApplicationEntries)
            self.setConfigErrorStr("max-application-entries must be in range of [%s,%s], got: %s" % (ApplicationInitiatedDiscoveryContainer.MAX_APPLICATION_ENTRIES_RANGE[0],ApplicationInitiatedDiscoveryContainer.MAX_APPLICATION_ENTRIES_RANGE[1], data.maxApplicationEntries))
            return ReturnCodes.kGeneralError

        ### set candidate data
        self.enabledCandidate = data.enabled
        self.maxRequestRateCandidate = data.maxRequestRate
        self.maxPendingRequestsCandidate = data.maxPendingRequests

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        """the interface changes are being aborted
    
            Raises:
                FATAL if fails
        """
    
        self._log("application-initiated-discovery-abort-private-value-set").debug3("%s: abort data - %s", self.name, data)
    
        self.maxRequestRateCandidate = self.maxRequestRate
        self.maxPendingRequestsCandidate = self.maxPendingRequests
        self.enabledCandidate = self.enabled
    
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        """the interface changes are being commited

            Raises:
                FATAL if fails
        """

        self._log("application-initiated-discovery-commit-private-value-set").debug3("%s: commit data - %s", self.name, data)

        ### set from data
        periodicTaskConfig = self.localAddressResolverPeriodicRequestReadTask.createConfig()
        periodicTaskConfig.isEnabled = data.enabled
        periodicTaskConfig.interval = data.pollInterval
        self.localAddressResolverPeriodicRequestReadTask.setConfig(periodicTaskConfig)

        periodicTaskConfig = self.localAddressResolverPeriodicTableReadTask.createConfig()
        periodicTaskConfig.isEnabled = data.enabled
        periodicTaskConfig.interval = data.pollInterval
        self.localAddressResolverPeriodicTableReadTask.setConfig(periodicTaskConfig)

        self.localAddressResolver.ndisc6LanConfigs.maxConcurrentRequests.set(data.maxConcurrentRequests)
        self.localAddressResolver.ndisc6LanConfigs.maxApplicationEntries.set(data.maxApplicationEntries)

        self.localAddressResolver.ndisc6LanConfigs.requestTimeout.set(data.requestTimeout)
        self.localAddressResolver.ndisc6LanConfigs.requestCount.set(data.requestCount)

        self.maxRequestRate = self.maxRequestRateCandidate
        self.maxPendingRequests = self.maxPendingRequestsCandidate
        self.enabled = self.enabledCandidate
                                    
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getCounters(self, tctx, operData):

        self._log("application-initiated-discovery-counters").debug3("%s: get counters was called. tctx=%s", self.name, tctx)

        if self.localAddressResolver == None:
            self._log("application-initiated-discovery-counters-no-address-resolver").error("localAddressResolver is None!")
            self.setOperErrorStr(tctx, "No counters available, localAddressResolver object is None!" % self.name)
            return ReturnCodes.kBadState

        operData.setPolls(self.localAddressResolver.ndisc6LanCounters.polls.get())

        operData.setApplicationRequestFailures(self.localAddressResolver.ndisc6LanCounters.applicationRequestFailures.get())
        operData.setApplicationRequestDiscards(self.localAddressResolver.ndisc6LanCounters.applicationRequestDiscards.get())
        operData.setApplicationRequestBlocks(self.localAddressResolver.ndisc6LanCounters.applicationRequestBlocks.get())
        operData.setApplicationRequests(self.localAddressResolver.ndisc6LanCounters.applicationRequests.get())

        operData.setNeighborDiscoverySuccesses(self.localAddressResolver.ndisc6LanCounters.neighborDiscoverySuccesses.get())
        operData.setNeighborDiscoveryTimeouts(self.localAddressResolver.ndisc6LanCounters.neighborDiscoveryTimeouts.get())
        operData.setNeighborDiscoveryFailures(self.localAddressResolver.ndisc6LanCounters.neighborDiscoveryFailures.get())
        operData.setNeighborDiscoveryRequestsSent(self.localAddressResolver.ndisc6LanCounters.neighborDiscoveryRequestsSent.get())

        operData.setApplicationEntryDiscards(self.localAddressResolver.ndisc6LanCounters.applicationEntryDiscards.get())
        operData.setApplicationEntryUpdates(self.localAddressResolver.ndisc6LanCounters.applicationEntryUpdates.get())
        operData.setApplicationEntryFailures(self.localAddressResolver.ndisc6LanCounters.applicationEntryFailures.get())

        operData.setOsTableLoadFailures(self.localAddressResolver.ndisc6LanCounters.osTableLoadFailures.get())
        operData.setOsTableLoads(self.localAddressResolver.ndisc6LanCounters.osTableLoads.get())

        self._log("application-initiated-discovery-status-counters").debug3("%s: get counters oper data=%s", self.name, operData)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getStatus(self, tctx, operData):

        self._log("application-initiated-discovery-status").debug3("%s: get status was called. tctx=%s", self.name, tctx)

        if self.localAddressResolver == None:
            self._log("application-initiated-discovery-status-no-address-resolver").error("localAddressResolver is None!")
            self.setOperErrorStr(tctx, "No counters available, localAddressResolver object is None!" % self.name)
            return ReturnCodes.kBadState

        operData.setApplicationEntryCount(self.localAddressResolver.ndisc6LanCounters.applicationEntryCount.get())
        operData.setConcurrentRequests(self.localAddressResolver.ndisc6LanCounters.concurrentRequests.get())
        
        self._log("application-initiated-discovery-status-data").debug3("%s: get status oper data=%s", self.name, operData)
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperStatusObj (self):
        blinkyOperStatus = AIDBlinkyOperStatus(self._log)
        return blinkyOperStatus

#-----------------------------------------------------------------------------------------------------------------------
    def getBlinkyOperCountersObj (self):
        blinkyOperCounters = AIDBlinkyOperCounters(self._log)
        return blinkyOperCounters

    def setLocalAddressResolver (self, localAddressResolver):
        self.localAddressResolver = localAddressResolver

    def setRequestReadPeriodicTask (self, localAddressResolverPeriodicRequestReadTask):
        self.localAddressResolverPeriodicRequestReadTask = localAddressResolverPeriodicRequestReadTask

    def setTableReadPeriodicTask (self, localAddressResolverPeriodicTableReadTask):
        self.localAddressResolverPeriodicTableReadTask = localAddressResolverPeriodicTableReadTask
