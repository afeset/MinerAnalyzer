# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: amiry


from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper
from a.sys.blinky.util.simple_list_wrapper import SimpleStringList
import a.infra.net.ip_address

G_NAME_GROUP_NET_NAME_RESOLUTION_STATIC = "static-resolution"

class StaticResolutionContainer(object):
    """This class manages the system static resolution information"""

    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_NAME_RESOLUTION_STATIC)
        self.name = "network-name-resolution-static"
        self.hosts = None
        self.blinkyStaticResolution = None

    #-------------------------------------------------------------------------------------------------------------------
    def getHosts (self):
        hosts = []
        if self.hosts and self.hosts.ipv4List:
            candidates = self.hosts.ipv4List.candidateValues()
            for candidate in candidates:
                hosts.append((candidate.getAddress(), candidate.getHostNames()))
        return hosts

    #-------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyStaticResolution):
        # --- /tech/system/name-resolution/static/hosts
        blinkyStaticResolution.setCreateHostsFunctor(self.createHosts)
        blinkyStaticResolution.setDeleteHostsFunctor(self.deleteHosts)
        self.blinkyStaticResolution = blinkyStaticResolution

    #-------------------------------------------------------------------------------------------------------------------
    def createHosts(self, phase, blinkyHosts):
        self._log("create-hosts").debug2("%s: blinkyHosts=%s", phase, blinkyHosts)
        if (phase.isPreparePrivate()):
            hosts = HostsContainer(self._log)
            self.hosts = SimpleContainerWrapper(self._log, hosts)
            self.hosts.attachToBlinky(blinkyHosts)
        elif (phase.isAbortPrivate()):
            self.hosts = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def deleteHosts(self, phase):
        self._log("delete-hosts").debug2("phase=%s", phase)
        if (phase.isCommitPrivate()):
            self.hosts = None
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
class HostsContainer(object):
    """This class manages the system dns static resolution hosts information"""
    def __init__ (self, logger):
        self._log = logger
        self.blinkyHosts = None
        self.ipv4List = None

    #-------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyHosts):
        # --- /tech/system/name-resolution/static/hosts/ipv4
        blinkyHosts.setCreateIpv4ListFunctor(self.createIpv4List)
        blinkyHosts.setDeleteIpv4ListFunctor(self.deleteIpv4List)
        self.blinkyHosts = blinkyHosts

    #-------------------------------------------------------------------------------------------------------------------
    def createIpv4List(self, phase, blinkyIpv4List):
        self._log("create-ipv4-list").debug2("%s: blinkyIpv4List=%s", phase, blinkyIpv4List)
        if (phase.isPreparePrivate()):
            createIpv4Functor = self.CreateIpv4Functor()
            self.ipv4List = SimpleStringList(self._log, createIpv4Functor)
            self.ipv4List.attachToBlinky(blinkyIpv4List)
        elif (phase.isAbortPrivate()):
            self.ipv4List = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def deleteIpv4List(self, phase):
        self._log("delete-ipv4-list").debug2("phase=%s", phase)
        if (phase.isCommitPrivate()):
            self.ipv4List = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    class CreateIpv4Functor(object):
        def __call__(self, logger, name):
            ipv4 = Ipv4Container(logger, name)
            ipv4Wrapper = SimpleContainerWrapper(logger, ipv4)
            return ipv4Wrapper

#-----------------------------------------------------------------------------------------------------------------------
class Ipv4Container(object):
    """This class manages the system dns static resolution ipv4 host information"""
    def __init__ (self, logger, name):
        self._log = logger
        self.name = name
        self.blinkyIpv4 = None
        self.hostList = None
        self.address = None
        self.candidateAddress = None

    #-------------------------------------------------------------------------------------------------------------------
    def getAddress (self):
        return self.candidateAddress

    #-------------------------------------------------------------------------------------------------------------------
    def getHostNames (self):
        hostNames = []
        if self.hostList is None:
            return []
        hosts = self.hostList.candidateValues()
        for host in hosts:
            hostNames.append(host.getHostName())
        return hostNames

    #-------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyIpv4):
        # --- /tech/system/name-resolution/static/hosts/ipv4/host
        blinkyIpv4.setCreateHostListFunctor(self.createHostList)
        blinkyIpv4.setDeleteHostListFunctor(self.deleteHostList)
        self.blinkyIpv4 = blinkyIpv4

    #-------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        """the ipv4 host is being evaluated and verified for correctness"""
        self._log("ipv4-host-value-set").debug4("%s: prepare data - %s", self.name, data)
        # TODO(amiry) - reuse the IP version class
        self.candidateAddress = a.infra.net.ip_address.IpAddress(data.address, 4)
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        """the ipv4 host changes are being aborted

            Raises:
                FATAL if fails
        """
        self._log("ipv4-host-abort-private-value-set").debug4("%s: abort data - %s", self.name, data)
        self.candidateAddress = self.address
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        """the ipv4 host changes are being commited

            Raises:
                FATAL if fails
        """
        self._log("ipv4-host-commit-private-value-set").debug4("%s: commit data - %s", self.name, data)
        self.address = self.candidateAddress
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def createHostList(self, phase, blinkyHostList):
        self._log("create-host").debug2("%s: blinkyHostList=%s", phase, blinkyHostList)
        if (phase.isPreparePrivate()):
            createHostFunctor = self.CreateHostFunctor()
            self.hostList = SimpleStringList(self._log, createHostFunctor)
            self.hostList.attachToBlinky(blinkyHostList)
        elif (phase.isAbortPrivate()):
            self.hostList = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def deleteHostList(self, phase):
        self._log("delete-host").debug2("phase=%s", phase)
        if (phase.isCommitPrivate()):
            self.hostList = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    class CreateHostFunctor(object):
        def __call__(self, logger, name):
            host = HostContainer(logger, name)
            hostWrapper = SimpleContainerWrapper(logger, host)
            return hostWrapper

#-----------------------------------------------------------------------------------------------------------------------
class HostContainer(object):
    """This class manages the system dns static resolution ipv4 host"""
    def __init__ (self, logger, name):
        self._log = logger
        self.name = name
        self.blinkyHost = None
        self.hostName = None
        self.candidateHostName = None

    #-------------------------------------------------------------------------------------------------------------------
    def getHostName(self):
        return self.candidateHostName

    #-------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyHost):
        self.blinkyHost = blinkyHost

    #-------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        """the host is being evaluated and verified for correctness"""
        self._log("host-value-set").debug4("%s: prepare data - %s", self.name, data)
        self.candidateHostName = data.hostname
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        """the host changes are being aborted

            Raises:
                FATAL if fails
        """
        self._log("host-abort-private-value-set").debug4("%s: abort data - %s", self.name, data)
        self.candidateHostName = self.hostName
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        """the host changes are being commited

            Raises:
                FATAL if fails
        """
        self._log("host-commit-private-value-set").debug4("%s: commit data - %s", self.name, data)
        self.hostName = self.candidateHostName
        return ReturnCodes.kOk

