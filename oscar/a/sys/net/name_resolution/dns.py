# Copyright Qwilt, 2010
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: amiry

G_NAME_GROUP_NET_NAME_RESOLUTION_DNS = "dns"

from a.infra.basic.return_codes import ReturnCodes
from a.sys.blinky.util.simple_container_wrapper import SimpleContainerWrapper
from a.sys.blinky.util.simple_list_wrapper import SimpleStringList
import a.infra.net.ip_address

class DnsContainer(object):
    """This class manages the system dns client information"""
    def __init__ (self, logger):
        self._log = logger.createLoggerSameModule(G_NAME_GROUP_NET_NAME_RESOLUTION_DNS)
        self.name = "network-name-resolution-dns"
        self.blinkyDns = None
        self.nameServers = None
        self.searchList = None
        self.enabled = None
        self.candidateEnabled = None

    #-------------------------------------------------------------------------------------------------------------------
    def getEnabled(self):
        return self.candidateEnabled

    #-------------------------------------------------------------------------------------------------------------------
    def getNameServers(self):
        nameServers = []
        if self.nameServers and self.nameServers.ipv4:
            nameServers = self.nameServers.ipv4.getServers()                
        return nameServers

    #-------------------------------------------------------------------------------------------------------------------
    def getSearchDomains(self):
        searchDomains = []
        if self.searchList:
            candidates = self.searchList.candidateValues()
            for candidate in candidates:
                searchDomains.append(candidate.getName())
        return searchDomains

    #-------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyDns):
        # --- /tech/system/name-resolution/dns/name-servers
        blinkyDns.setCreateNameServersFunctor(self.createNameServers)
        blinkyDns.setDeleteNameServersFunctor(self.deleteNameServers)
        # --- /tech/system/name-resolution/dns/search
        blinkyDns.setCreateSearchListFunctor(self.createSearchList)
        blinkyDns.setDeleteSearchListFunctor(self.deleteSearchList)
        self.blinkyDns = blinkyDns

    #-------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        """the dns client is being evaluated and verified for correctness"""
        self._log("dns-prepare-private-value-set").debug4("%s: prepare data - %s", self.name, data)
        self.candidateEnabled = data.enabled
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        """the dns client changes are being aborted

            Raises:
                FATAL if fails
        """
        self._log("dns-abort-private-value-set").debug4("%s: abort data - %s", self.name, data)
        self.candidateEnabled = self.enabled
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        """the dns client changes are being commited

            Raises:
                FATAL if fails
        """
        self._log("dns-commit-private-value-set").debug4("%s: commit data - %s", self.name, data)
        self.enabled = self.candidateEnabled
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def createNameServers(self, phase, blinkyNameServers):
        self._log("create-nameservers").debug2("%s: blinkyNameServers=%s", phase, blinkyNameServers)
        if (phase.isPreparePrivate()):
            nameServers = NameServersContainer(self._log)
            self.nameServers = SimpleContainerWrapper(self._log, nameServers)
            self.nameServers.attachToBlinky(blinkyNameServers)
        elif (phase.isAbortPrivate()):
            self.nameServers = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def deleteNameServers(self, phase):
        self._log("delete-nameservers").debug2("phase=%s", phase)
        if (phase.isCommitPrivate()):
            self.nameServers = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def createSearchList(self, phase, blinkySearchList):
        self._log("create-search").debug2("%s: blinkySearchList=%s", phase, blinkySearchList)
        if (phase.isPreparePrivate()):
            createSearchFunctor = self.CreateSearchFunctor()
            self.searchList = SimpleStringList(self._log, createSearchFunctor)
            self.searchList.attachToBlinky(blinkySearchList)
        elif (phase.isAbortPrivate()):
            self.searchList = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def deleteSearchList(self, phase):
        self._log("delete-search").debug2("phase=%s", phase)
        if (phase.isCommitPrivate()):
            self.searchList = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    class CreateSearchFunctor(object):
        def __call__(self, logger, name):
            search = SearchContainer(logger, name)
            searchWrapper = SimpleContainerWrapper(logger, search)
            return searchWrapper

    #-------------------------------------------------------------------------------------------------------------------
    def preparePrivateAfter(self):

        # The below limitations are taken from the resolv.conf man page.
        # "The search list is currently limited to six domains with a total of 256 characters."

        searchDomains = self.getSearchDomains()

        if len(searchDomains) > 6:
            self.blinkyDns.setConfigErrorStr("The search list is limited to 6 domains")
            return ReturnCodes.kGeneralError

        searchDomainsLen = 0
        for searchDomain in searchDomains:
            searchDomainsLen += len(searchDomain)

        if searchDomainsLen > 256:
            self.blinkyDns.setConfigErrorStr("The search list is limited to 256 characters")
            return ReturnCodes.kGeneralError

        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
class NameServersContainer(object):
    """This class manages the system dns client name servers information"""
    def __init__ (self, logger):
        self._log = logger
        self.blinkyNameServers = None
        self.ipv4 = None

    #-------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyNameServers):
        # --- /tech/system/name-resolution/dns/name-servers/ipv4
        blinkyNameServers.setCreateIpv4Functor(self.createIpv4)
        blinkyNameServers.setDeleteIpv4Functor(self.deleteIpv4)
        self.blinkyNameServers = blinkyNameServers

    #-------------------------------------------------------------------------------------------------------------------
    def createIpv4(self, phase, blinkyIpv4):
        self._log("create-ipv4").debug2("%s: blinkyIpv4=%s", phase, blinkyIpv4)
        if (phase.isPreparePrivate()):
            ipv4 = Ipv4Container(self._log)
            self.ipv4 = SimpleContainerWrapper(self._log, ipv4,
                                               notifyTrxProgressFunctor = True,
                                               notifyDescendantsModifications = True)
            self.ipv4 .attachToBlinky(blinkyIpv4)
        elif (phase.isAbortPrivate()):
            self.ipv4= None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def deleteIpv4(self, phase):
        self._log("delete-ipv4").debug2("phase=%s", phase)
        if (phase.isCommitPrivate()):
            self.ipv4 = None
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
class Ipv4Container(object):
    """This class manages the system dns client ipv4 name servers information"""
    def __init__ (self, logger):
        self._log = logger
        self.blinkyIpv4 = None
        self.serverList = None

    #-------------------------------------------------------------------------------------------------------------------
    def getServers (self):
        servers = []
        if self.serverList:
            candidates = self.serverList.candidateValues()
            for candidate in candidates:
                servers.append(candidate.getAddress())
        return servers

    #-------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyIpv4):
        # --- /tech/system/name-resolution/dns/name-servers/ipv4/servers
        blinkyIpv4.setCreateServerListFunctor(self.createServerList)
        blinkyIpv4.setDeleteServerListFunctor(self.deleteServerList)
        self.blinkyIpv4 = blinkyIpv4

    #-------------------------------------------------------------------------------------------------------------------
    def createServerList(self, phase, blinkyServerList):
        self._log("create-server-list").debug2("%s: blinkyServerList=%s", phase, blinkyServerList)
        if (phase.isPreparePrivate()):
            createServerFunctor = self.CreateServerFunctor()
            self.serverList = SimpleStringList(self._log, createServerFunctor)
            self.serverList.attachToBlinky(blinkyServerList)
        elif (phase.isAbortPrivate()):
            self.serverList = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def deleteServerList(self, phase):
        self._log("delete-server-list").debug2("phase=%s", phase)
        if (phase.isCommitPrivate()):
            self.serverList = None
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    class CreateServerFunctor(object):
        def __call__(self, logger, name):
            # TODO(amiry) - reuse the IP version class
            server = ServerContainer(logger, name, 4)
            serverWrapper = SimpleContainerWrapper(logger, server)
            return serverWrapper

    #-------------------------------------------------------------------------------------------------------------------
    def preparePrivateAfter(self):
        # Maximum number of name servers is 3
        servers = self.getServers()
        if len(servers) > 3:
            self.blinkyIpv4.setConfigErrorStr("Maximum number of name servers is 3")
            return ReturnCodes.kGeneralError
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
class ServerContainer(object):
    """This class manages the system dns client name server ip addresses"""
    def __init__ (self, logger, name, version):
        self._log = logger
        self.name = name
        self.version = version
        self.blinkyServer = None
        self.address = None
        self.candidateAddress = None

    #-------------------------------------------------------------------------------------------------------------------
    def getAddress (self):
        return self.candidateAddress

    #-------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkyServer):
        self.blinkyServer = blinkyServer

    #-------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        """the name server is being evaluated and verified for correctness"""
        self._log("name-server-value-set").debug4("%s: prepare data - %s", self.name, data)
        self.candidateAddress = a.infra.net.ip_address.IpAddress(data.address, self.version)
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        """the name server changes are being aborted

            Raises:
                FATAL if fails
        """
        self._log("name-server-abort-private-value-set").debug4("%s: abort data - %s", self.name, data)
        self.candidateAddress = self.address
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        """the name server changes are being commited

            Raises:
                FATAL if fails
        """
        self._log("name-server-commit-private-value-set").debug4("%s: commit data - %s", self.name, data)
        self.address = self.candidateAddress
        return ReturnCodes.kOk

#-----------------------------------------------------------------------------------------------------------------------
class SearchContainer(object):
    """This class manages the system dns client domain search suffixes"""
    def __init__ (self, logger, name):
        self._log = logger
        self.name = name
        self.blinkySearch = None
        self.nameField = None
        self.candidateName = None

    #-------------------------------------------------------------------------------------------------------------------
    def getName (self):
        return self.candidateName

    #-------------------------------------------------------------------------------------------------------------------
    def notifyAttachToBlinky(self, blinkySearch):
        self.blinkySearch = blinkySearch

    #-------------------------------------------------------------------------------------------------------------------
    def preparePrivateValueSet(self, data):
        """the search suffix is being evaluated and verified for correctness"""
        self._log("search-value-set").debug4("%s: prepare data - %s", self.name, data)
        self.candidateName = data.name
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def abortPrivateValueSet(self, data):
        """the search suffix changes are being aborted

            Raises:
                FATAL if fails
        """
        self._log("search-abort-private-value-set").debug4("%s: abort data - %s", self.name, data)
        self.candidateName = self.nameField
        return ReturnCodes.kOk

    #-------------------------------------------------------------------------------------------------------------------
    def commitPrivateValueSet(self, data):
        """the search suffix changes are being commited

            Raises:
                FATAL if fails
        """
        self._log("search-commit-private-value-set").debug4("%s: commit data - %s", self.name, data)
        self.nameField = self.candidateName
        return ReturnCodes.kOk

