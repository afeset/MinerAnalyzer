# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: yoave

import a.sys.net.lnx.neighbour
import os
import Queue
import a.infra.format.json

from a.sys.net import config_file
from threading import Thread
from threading import Lock
from a.infra.basic import memory_definitions

class LocalIpv6AddressResolver:
    """ resolves MAC addresses from LAN IPs
    """

    class Counters:

        def __init__ (self):
            ### number of ndisc6 file request read function called  ###
            self.polls = memory_definitions.AtomicInt()

            ### application requests (ndisc6 requests) counters ###
            self.applicationRequestFailures = memory_definitions.AtomicInt()
            self.applicationRequestDiscards = memory_definitions.AtomicInt()
            self.applicationRequestBlocks = memory_definitions.AtomicInt()
            self.applicationRequests = memory_definitions.AtomicInt()
            
            ### neighbor discovery (ndisc6) counters ###
            self.neighborDiscoverySuccesses = memory_definitions.AtomicInt()
            self.neighborDiscoveryTimeouts = memory_definitions.AtomicInt()
            self.neighborDiscoveryFailures = memory_definitions.AtomicInt()
            self.neighborDiscoveryRequestsSent = memory_definitions.AtomicInt()

            ### application entries (write neighbor table file which is read by line) counters ###
            self.applicationEntryDiscards = memory_definitions.AtomicInt()
            self.applicationEntryUpdates = memory_definitions.AtomicInt()
            self.applicationEntryFailures = memory_definitions.AtomicInt()

            ### os-table loads (linux neighbor table reads) counters ###
            self.osTableLoadFailures = memory_definitions.AtomicInt()
            self.osTableLoads = memory_definitions.AtomicInt()

            ### these ones are more of a status like ###
            self.concurrentRequests = memory_definitions.AtomicInt()
            self.applicationEntryCount = memory_definitions.AtomicInt()


    class Configs:

        #default config
        ourDefaultMaxConcurrentRequests = 100
        ourDefaultMaxApplicationEntries = 128
        ourDefaultRequestTimeout = 2
        ourDefaultRequestCount = 5

        def __init__ (self):
            ### LocalIpv6AddressResolver configs ###
            self.maxConcurrentRequests = memory_definitions.AtomicInt()
            self.maxApplicationEntries = memory_definitions.AtomicInt()

            self.maxConcurrentRequests.set(LocalIpv6AddressResolver.Configs.ourDefaultMaxConcurrentRequests)
            self.maxApplicationEntries.set(LocalIpv6AddressResolver.Configs.ourDefaultMaxApplicationEntries)

            ### shared global ndisc6 thread config ###
            self.requestTimeout = memory_definitions.AtomicInt()
            self.requestCount = memory_definitions.AtomicInt()

            self.requestTimeout.set(LocalIpv6AddressResolver.Configs.ourDefaultRequestTimeout)
            self.requestCount.set(LocalIpv6AddressResolver.Configs.ourDefaultRequestCount)


#-----------------------------------------------------------------------------------------------------------------------
    def __init__ (self, ndisc6RequestsDirectory, neighborTableFileName):

        self.ndisc6LanCounters = self.Counters()
        self.ndisc6LanConfigs = self.Configs()
        
        self.ndisc6RequestsDirectory = ndisc6RequestsDirectory

        self.ipv6NeighborTableFile = config_file.LineNeighborTableFile(neighborTableFileName)

        #snapshot for "diff'ing" kernel neighbor table reads
        self.ipv6NeighborTableSnapshot = config_file.NeighborTable()

        self._log = None

        #currently running threads can be found here
        self.runningThreadsDict = {}

        #finished threads put themselves into this queue
        self.finishedThreadsQueue = Queue.Queue()
        
        #we assign a unique name for each thread
        self.threadUniqueKey = 0

        #config thread appends configuration changes in here... todo!
        self.configQueue = Queue.Queue()

#-----------------------------------------------------------------------------------------------------------------------
    def shutDown (self):
        #since we dont have a friendly api for thread termination in python, ommit this warning if we still have threads running
        if self.ndisc6LanCounters.concurrentRequests.get() > 0:
            self._log("local-ipv6-resolver-shutdown").notice("Shutting down LocalIpv6AddressResolver... note! there are {%d} ndisc6 threads running", self.ndisc6LanCounters.concurrentRequests.get() )

#-----------------------------------------------------------------------------------------------------------------------
    def initLogger (self, logger):
        self._log = logger

#-----------------------------------------------------------------------------------------------------------------------
    def sendNdiscRequest (self, osDevice, ipAddress, numRequests, timeout, threadName):
        # run ndisc6 process
        rc, retStdout, retStdErr = a.sys.net.lnx.neighbour.Ndisc.sendNdiscRequest(self._log, osDevice, str(ipAddress),
                                                                                count=numRequests,timeout=timeout,blocking=True)

        # update total number of requests sent
        self.ndisc6LanCounters.neighborDiscoveryRequestsSent.add(1)

        # 0 == success
        if rc == 0:
            self.ndisc6LanCounters.neighborDiscoverySuccesses.add(1)
            self._log("ndisc6-thread-success").debug3("Ndisc6 for {%s} on device {%s} was successful", str(ipAddress), osDevice)

        # 1 == timed out
        elif rc == 1:
            self.ndisc6LanCounters.neighborDiscoveryTimeouts.add(1)
            self._log("ndisc6-thread-timeout").debug1("Ndisc6 for {%s} on device {%s} has timed out!", str(ipAddress), osDevice)

        # anything else == error
        else:
            self.ndisc6LanCounters.neighborDiscoveryFailures.add(1)
            self._log("ndisc6-thread-fail").debug1("Ndisc6 for {%s} on device {%s} has failed: returned code {%d} stderr = {%s}", str(ipAddress), osDevice, rc, retStdErr)

        # add to removal queue
        self.finishedThreadsQueue.put_nowait(threadName)

        # we need to know this param whenever we query for it
        self.ndisc6LanCounters.concurrentRequests.add(-1)

        return

#-----------------------------------------------------------------------------------------------------------------------
    def createNdisc6Thread (self, osDevice, ipAddress, numRequests, timeout):
        #remove finished threads from our dictionary
        while not self.finishedThreadsQueue.empty():
            finishedThreadKey = self.finishedThreadsQueue.get_nowait()
            del self.runningThreadsDict[finishedThreadKey]

        if self.ndisc6LanCounters.concurrentRequests.get() >= self.ndisc6LanConfigs.maxConcurrentRequests.get():
            self.ndisc6LanCounters.applicationRequestDiscards.add(1)
            self._log("create-ndisc6-thread-no-room").debug1("Discarding ndisc6 request thread because number of executing threads has reached maximum threashold!")
            return
        threadDictName = 'ndisc-' + str(self.threadUniqueKey)
        self.threadUniqueKey += 1
        newThread = Thread(target = self.sendNdiscRequest, args = (osDevice,ipAddress,numRequests,timeout,threadDictName))
        newThread.daemon = True # a daemon thread - does not affect app exit
        newThread.name = threadDictName

        self.runningThreadsDict[threadDictName] = newThread
        self.ndisc6LanCounters.concurrentRequests.add(1)

        newThread.start()

#-----------------------------------------------------------------------------------------------------------------------
    def sendNdisc6ToRequestedIps(self, ipv6List, availableDeviceList):

        for ipAddress, device in ipv6List:
            if device not in availableDeviceList:
                continue

            self.createNdisc6Thread(device,ipAddress, self.ndisc6LanConfigs.requestCount.get(), self.ndisc6LanConfigs.requestTimeout.get())

#-----------------------------------------------------------------------------------------------------------------------
    def processNdisc6Requests(self, availableDeviceList):
        ### update function call counter ###
        self.ndisc6LanCounters.polls.add(1)

        #read requests from files
        #construct a set, we dont need to ndisc duplicated requests
        ndisc6RequestSet = set()
        for fileName in os.listdir(self.ndisc6RequestsDirectory):
            fullFileName = os.path.join(self.ndisc6RequestsDirectory,fileName)
            if os.path.isfile(fullFileName):
                self.ndisc6LanCounters.applicationRequestBlocks.add(1)
                try:
                    data = a.infra.format.json.readFromFile(self._log, fullFileName)
                except IOError as ex:
                    self.ndisc6LanCounters.applicationRequestFailures.add(1)
                    self._log("process-ndisc-request-io-except").error("failed reading json file {%s} - %s", fullFileName, ex)
    
                except ValueError as ex:
                    self.ndisc6LanCounters.applicationRequestFailures.add(1)
                    self._log("process-ndisc-request-parse-except").error("failed parsing json file {%s} - %s", fullFileName, ex)
    
                else:
                    ndiscRequests = data.get("requests",None)
                    
                    if ndiscRequests != None:
                        for request in ndiscRequests:
                            if ("ip" not in request) or ("deviceName" not in request):
                                self._log("process-ndisc-request-get-requests-bad").error("bad ndisc request line from file %s - {%s}", fullFileName, request)
                                continue
                            ipAndDevice = (request["ip"], request["deviceName"])
                            ndisc6RequestSet.add(ipAndDevice)
                            ### we may want to count duplicate requests ###
                            self.ndisc6LanCounters.applicationRequests.add(1)
                    else:
                        self.ndisc6LanCounters.applicationRequestFailures.add(1)
                        self._log("process-ndisc-request-get-requests-none").error("found valid Json file format, but empty request format - {%s}", fullFileName)
                finally:
                    os.remove(fullFileName)
        
        self.sendNdisc6ToRequestedIps(ndisc6RequestSet, availableDeviceList)
        return 

#-----------------------------------------------------------------------------------------------------------------------
    def updateDeliveryIpv6NeighborTable(self, deviceList):

        self.ipv6NeighborTableFile.clearInterfaceNeighborTables()
        i = 0
        for device in deviceList:

            interfaceNeighborTable = a.sys.net.lnx.neighbour.NeighbourUtils.getNeighbourTable(self._log, device,6)

            if interfaceNeighborTable == None:
                self._log("update-neigh-mac-failed-table-read").debug1("failed reading linux neighbor table for some reason")
                self.ndisc6LanCounters.osTableLoadFailures.add(1)
                

            ### update number of table entries status & counter ###
            self.ndisc6LanCounters.applicationEntryCount.set(len(interfaceNeighborTable))
            self.ndisc6LanCounters.osTableLoads.add(1)

            ### trimm size if needed ###
            maxTableSize = self.ndisc6LanConfigs.maxApplicationEntries.get()
            tableLen = len(interfaceNeighborTable)
            if tableLen > maxTableSize:
                if self._log:
                    self._log("update-neigh-mac-big-table").warning("read a table size of %s, while configured max is %s. Trimming table." % (tableLen, maxTableSize))
                self.ndisc6LanCounters.applicationEntryDiscards.add(tableLen - maxTableSize)
                interfaceNeighborTable = interfaceNeighborTable[:maxTableSize]


            

            # example:
            # ipv4 --> 199.120.69.13 dev eth-tg8 lladdr 00:0d:66:33:dc:19 REACHABLE
            # ipv6 --> 2000::223:5eff:fe2d:cf81 dev eth-tg8 lladdr 00:23:5e:2d:cf:81 router STALE
            for tableLine in interfaceNeighborTable:
                dstIp = tableLine.split()[0]
                try:
                    mac = tableLine.split("lladdr",1)[1].split()[0]
                    if self._log:
                        self._log("update-neigh-mac-show").debug3("Destination IP's ('%s') MAC address is '%s'", dstIp, mac)
        
                except IndexError:
                    mac = None
                    if self._log:
                        self._log("update-neigh-mac-failed").debug1("failed extracting destination IP's ('%s') MAC address from table {%s}", dstIp, interfaceNeighborTable)
                    continue

                tableLineEntry = config_file.NeighborTableLineEntry()
                tableLineEntry.ip = dstIp
                tableLineEntry.mac = mac

            
                
                # fill updated neighbor table
                self.ipv6NeighborTableFile.neighborTables.interfaceNeighborTableList[i].tableLine.append(tableLineEntry)
            self.ipv6NeighborTableFile.neighborTables.interfaceNeighborTableList[i].deviceName = device
            i += 1

        #write file only if there was an actual update, if so, update the copy as well
        if self.ipv6NeighborTableFile.neighborTables != self.ipv6NeighborTableSnapshot:
            self.ipv6NeighborTableSnapshot.copy(self.ipv6NeighborTableFile.neighborTables)
            self.ipv6NeighborTableFile.dumpData()
            self.ipv6NeighborTableFile.commit()

            ### update number of lines written ###
            self.ndisc6LanCounters.applicationEntryUpdates.add(len(interfaceNeighborTable))
